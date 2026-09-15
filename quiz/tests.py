from datetime import timedelta

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from rest_framework.test import APIClient

from content.models import Exam, PastPaper, Question, Subject, Subtopic, Topic
from quiz.models import Attempt, AttemptQuestion
from quiz.services import get_past_paper_progress

User = get_user_model()

URL = reverse('past-paper-progress')


class PastPaperProgressTests(TestCase):
    def setUp(self):
        self.exam = Exam.objects.create(name='MDCAT', slug='mdcat', level='entry-test')
        self.other_exam = Exam.objects.create(name='LUMS', slug='lums', level='entry-test')
        subject = Subject.objects.create(exam=self.exam, name='Biology', slug='biology')
        topic = Topic.objects.create(subject=subject, name='Cells', slug='cells')
        self.subtopic = Subtopic.objects.create(topic=topic, name='Membranes', slug='membranes')
        self.user = User.objects.create_user(username='u1', email='u1@x.com', password='pw12345!')
        self.other_user = User.objects.create_user(username='u2', email='u2@x.com', password='pw12345!')
        self.client = APIClient()
        self.client.force_authenticate(self.user)
        self._slug = 0

    # -- helpers ---------------------------------------------------------
    def paper(self, year, exam=None, is_active=True):
        self._slug += 1
        return PastPaper.objects.create(
            exam=exam or self.exam, name=f'P{self._slug}', slug=f'p{self._slug}',
            year=year, is_active=is_active,
        )

    def q(self, paper, paper_order=None, is_active=True, is_verified=True):
        return Question.objects.create(
            subtopic=self.subtopic, past_paper=paper, question_text='?',
            option_a='a', option_b='b', option_c='c', option_d='d',
            correct_answer='A', paper_order=paper_order,
            is_active=is_active, is_verified=is_verified,
        )

    def attempt(self, paper, answers, user=None, mode='past_paper', completed=True,
                submitted_at=None, correct_count=0, total=None):
        """answers: list of (question, selected, is_correct, attempts_count)."""
        att = Attempt.objects.create(
            user=user or self.user, mode=mode, exam=paper.exam, past_paper=paper,
            is_completed=completed,
            submitted_at=(submitted_at or timezone.now()) if completed else None,
            correct_count=correct_count,
            total_questions=len(answers) if total is None else total,
        )
        AttemptQuestion.objects.bulk_create([
            AttemptQuestion(
                attempt=att, question=question, order_in_attempt=i + 1,
                selected_option=sel, is_correct=ok, attempts_count=n,
            )
            for i, (question, sel, ok, n) in enumerate(answers)
        ])
        return att

    def entry(self, paper, **kwargs):
        data = self.client.get(URL, kwargs).json()
        return next(e for e in data if e['past_paper_id'] == paper.id)

    # -- numbering -------------------------------------------------------
    def test_printed_numbering_with_gap_is_missing(self):
        p = self.paper(2010)
        q3 = self.q(p, paper_order=3)  # lower id, higher printed number
        q1 = self.q(p, paper_order=1)
        self.attempt(p, [(q3, 'a', True, 1), (q1, 'b', False, 1)], correct_count=1)

        e = self.entry(p)
        self.assertEqual(e['numbering'], 'printed')
        self.assertEqual(e['latest_attempt']['states'], ['wrong', 'missing', 'correct'])
        self.assertEqual(e['latest_attempt']['counts']['missing'], 1)

    def test_partial_paper_order_is_derived_by_id(self):
        p = self.paper(2017)
        q1 = self.q(p, paper_order=2)
        q2 = self.q(p, paper_order=None)
        q3 = self.q(p, paper_order=None, is_active=False)
        self.attempt(p, [(q1, 'a', True, 1), (q2, None, None, 0)])

        e = self.entry(p)
        self.assertEqual(e['numbering'], 'derived')
        self.assertEqual(e['latest_attempt']['states'], ['correct', 'unanswered', 'inactive'])
        self.assertNotIn('missing', e['latest_attempt']['states'])
        self.assertEqual(e['latest_attempt']['counts']['missing'], 0)

    def test_duplicate_paper_order_is_derived(self):
        p = self.paper(2011)
        self.q(p, paper_order=1)
        self.q(p, paper_order=1)
        self.assertEqual(self.entry(p)['numbering'], 'derived')

    # -- states ----------------------------------------------------------
    def test_all_non_missing_states(self):
        p = self.paper(2020)
        qc, qw, qr, qu, qn, qi, qv = [self.q(p) for _ in range(5)] + [
            self.q(p, is_active=False), self.q(p, is_verified=False),
        ]
        self.attempt(p, [
            (qc, 'a', True, 1),
            (qw, 'b', False, 1),
            (qr, 'b', False, 3),
            (qu, None, None, 0),
            (qi, 'a', True, 1),
            (qv, 'a', True, 1),
        ])  # qn never offered

        la = self.entry(p)['latest_attempt']
        self.assertEqual(la['states'], [
            'correct', 'wrong', 'wrong_retried', 'unanswered',
            'not_offered', 'inactive', 'inactive',
        ])
        self.assertEqual(la['counts'], {
            'correct': 1, 'wrong': 1, 'wrong_retried': 1, 'unanswered': 1,
            'not_offered': 1, 'inactive': 2, 'missing': 0,
        })

    def test_legacy_zero_attempts_count_answered_is_not_unanswered(self):
        p = self.paper(2020)
        q1, q2 = self.q(p), self.q(p)
        self.attempt(p, [(q1, 'a', True, 0), (q2, 'c', False, 0)])
        self.assertEqual(self.entry(p)['latest_attempt']['states'], ['correct', 'wrong'])

    def test_selected_null_with_is_correct_false_is_unanswered(self):
        p = self.paper(2020)
        q1 = self.q(p)
        self.attempt(p, [(q1, None, False, 2)])
        self.assertEqual(self.entry(p)['latest_attempt']['states'], ['unanswered'])

    def test_absent_from_attempt_and_now_inactive_is_inactive(self):
        p = self.paper(2020)
        q1 = self.q(p)
        q2 = self.q(p, is_active=False)
        self.attempt(p, [(q1, 'a', True, 1)])
        self.assertEqual(self.entry(p)['latest_attempt']['states'], ['correct', 'inactive'])

    def test_score_of_record_diverges_from_counts_after_deactivation(self):
        p = self.paper(2020)
        q1, q2 = self.q(p), self.q(p)
        self.attempt(p, [(q1, 'a', True, 1), (q2, 'a', True, 1)], correct_count=2)
        Question.objects.filter(id=q2.id).update(is_active=False)

        la = self.entry(p)['latest_attempt']
        self.assertEqual(la['states'], ['correct', 'inactive'])
        self.assertEqual(la['score_correct'], 2)
        self.assertEqual(la['score_total'], 2)
        self.assertEqual(la['counts']['correct'], 1)

    # -- attempt selection -----------------------------------------------
    def test_latest_completed_attempt_wins(self):
        p = self.paper(2020)
        q1 = self.q(p)
        now = timezone.now()
        self.attempt(p, [(q1, 'b', False, 1)], submitted_at=now - timedelta(days=2))
        new = self.attempt(p, [(q1, 'a', True, 1)], submitted_at=now, correct_count=1)
        self.attempt(p, [(q1, 'c', False, 1)], submitted_at=now - timedelta(days=1))

        la = self.entry(p)['latest_attempt']
        self.assertEqual(la['attempt_id'], new.id)
        self.assertEqual(la['states'], ['correct'])
        self.assertEqual(la['score_correct'], 1)
        self.assertTrue(la['submitted_at'])

    def test_other_modes_ignored(self):
        p = self.paper(2020)
        q1 = self.q(p)
        for mode in ('mock', 'practice', 'sectional'):
            self.attempt(p, [(q1, 'a', True, 1)], mode=mode)
            self.attempt(p, [(q1, 'a', True, 1)], mode=mode, completed=False)
        e = self.entry(p)
        self.assertIsNone(e['latest_attempt'])
        self.assertIsNone(e['in_progress'])

    def test_in_progress_only_in_in_progress(self):
        p = self.paper(2020)
        q1, q2, q3 = self.q(p), self.q(p), self.q(p)
        done = self.attempt(p, [(q1, 'a', True, 1), (q2, None, None, 0), (q3, None, None, 0)])
        live = self.attempt(
            p, [(q1, 'b', False, 1), (q2, 'a', True, 1), (q3, None, None, 0)],
            completed=False,
        )

        e = self.entry(p)
        self.assertEqual(e['latest_attempt']['attempt_id'], done.id)
        self.assertEqual(e['latest_attempt']['states'], ['correct', 'unanswered', 'unanswered'])
        self.assertEqual(e['in_progress'], {'attempt_id': live.id, 'answered': 2, 'total': 3})

    def test_in_progress_without_completed(self):
        p = self.paper(2020)
        q1 = self.q(p)
        live = self.attempt(p, [(q1, 'a', True, 1)], completed=False)
        e = self.entry(p)
        self.assertIsNone(e['latest_attempt'])
        self.assertEqual(e['in_progress'], {'attempt_id': live.id, 'answered': 1, 'total': 1})

    def test_untouched_and_inactive_papers(self):
        touched = self.paper(2021)
        untouched = self.paper(2022)
        hidden = self.paper(2023, is_active=False)
        empty = self.paper(2019)
        q1 = self.q(touched)
        self.q(untouched)
        self.q(hidden)
        self.attempt(touched, [(q1, 'a', True, 1)])

        data = self.client.get(URL).json()
        self.assertEqual(
            [e['past_paper_id'] for e in data], [untouched.id, touched.id, empty.id],
        )
        u = data[0]
        self.assertEqual(u['numbering'], 'derived')
        self.assertIsNone(u['latest_attempt'])
        self.assertIsNone(u['in_progress'])
        self.assertIsNone(data[2]['latest_attempt'])

    def test_other_users_attempts_not_leaked(self):
        p = self.paper(2020)
        q1 = self.q(p)
        self.attempt(p, [(q1, 'a', True, 1)], user=self.other_user)
        self.attempt(p, [(q1, 'a', True, 1)], user=self.other_user, completed=False)
        e = self.entry(p)
        self.assertIsNone(e['latest_attempt'])
        self.assertIsNone(e['in_progress'])

    def test_unauthenticated_rejected(self):
        resp = APIClient().get(URL)
        self.assertIn(resp.status_code, (401, 403))

    # -- filters -----------------------------------------------------------
    def test_exam_and_paper_filters(self):
        a = self.paper(2020)
        b = self.paper(2021)
        c = self.paper(2025, exam=self.other_exam)
        for p in (a, b, c):
            self.q(p)

        ids = lambda params: [e['past_paper_id'] for e in self.client.get(URL, params).json()]
        self.assertEqual(ids({}), [c.id, b.id, a.id])
        self.assertEqual(ids({'exam': self.exam.id}), [b.id, a.id])
        self.assertEqual(ids({'paper': a.id}), [a.id])
        self.assertEqual(ids({'exam': self.other_exam.id, 'paper': a.id}), [])
        self.assertEqual(self.client.get(URL, {'paper': 'x'}).status_code, 400)

    # -- performance -------------------------------------------------------
    def test_constant_query_count(self):
        def build(n):
            for i in range(n):
                p = self.paper(2000 + self._slug)
                qs = [self.q(p, paper_order=j + 1) for j in range(3)]
                self.attempt(p, [(x, 'a', True, 2) for x in qs])
                self.attempt(p, [(x, 'a', True, 1) for x in qs], completed=False)

        build(1)
        with self.assertNumQueries(4):
            get_past_paper_progress(self.user)
        build(5)
        with self.assertNumQueries(4):
            result = get_past_paper_progress(self.user)
        self.assertEqual(len(result), 6)
        with self.assertNumQueries(4):
            self.assertEqual(self.client.get(URL).status_code, 200)
