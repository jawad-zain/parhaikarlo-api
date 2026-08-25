import threading
from unittest import mock

from django.contrib.auth import get_user_model
from django.db import connection
from django.test import TestCase, TransactionTestCase
from django.utils import timezone

from content.models import Exam
from payments.models import Subscription, SubscriptionPlan, has_active_subscription
from payments.services import (
    PROMO_PLAN_NAME,
    grant_free_promo_if_eligible,
    grant_free_promo_if_eligible_silently,
    looks_like_test_email,
)

User = get_user_model()


def make_user(email, password='testpass123'):
    return User.objects.create_user(username=email, email=email, password=password)


class GrantFreePromoIfEligibleTests(TestCase):
    def setUp(self):
        self.exam = Exam.objects.create(
            name='MDCAT', slug='mdcat', level='entry-test',
        )

    def test_first_signup_gets_the_subscription(self):
        user = make_user('first.real.student@gmail.com')

        sub = grant_free_promo_if_eligible(user, self.exam)

        self.assertIsNotNone(sub)
        self.assertEqual(sub.user, user)
        self.assertEqual(sub.plan.name, PROMO_PLAN_NAME)
        self.assertEqual(sub.status, 'active')
        self.assertTrue(has_active_subscription(user, self.exam))

    def test_thirtieth_signup_gets_the_subscription(self):
        for i in range(29):
            user = make_user(f'student{i}@gmail.com')
            self.assertIsNotNone(grant_free_promo_if_eligible(user, self.exam))

        thirtieth = make_user('student29@gmail.com')
        sub = grant_free_promo_if_eligible(thirtieth, self.exam)

        self.assertIsNotNone(sub)
        self.assertEqual(
            Subscription.objects.filter(plan__name=PROMO_PLAN_NAME).count(), 30,
        )

    def test_thirty_first_signup_does_not_get_it(self):
        for i in range(30):
            user = make_user(f'student{i}@gmail.com')
            self.assertIsNotNone(grant_free_promo_if_eligible(user, self.exam))

        thirty_first = make_user('student30@gmail.com')
        sub = grant_free_promo_if_eligible(thirty_first, self.exam)

        self.assertIsNone(sub)
        self.assertFalse(has_active_subscription(thirty_first, self.exam))
        self.assertEqual(
            Subscription.objects.filter(plan__name=PROMO_PLAN_NAME).count(), 30,
        )

    def test_test_email_is_excluded_and_does_not_count_against_the_slots(self):
        self.assertTrue(looks_like_test_email('qa-test-123@example.com'))

        test_user = make_user('qa-test-123@example.com')
        sub = grant_free_promo_if_eligible(test_user, self.exam)
        self.assertIsNone(sub)
        self.assertEqual(Subscription.objects.filter(plan__name=PROMO_PLAN_NAME).count(), 0)

        # A real signup right after should still get slot #1, proving the
        # test account never consumed one.
        real_user = make_user('real.student@gmail.com')
        sub = grant_free_promo_if_eligible(real_user, self.exam)
        self.assertIsNotNone(sub)

    def test_user_with_existing_paid_sub_is_skipped_and_does_not_count(self):
        plan = SubscriptionPlan.objects.create(
            exam=self.exam, name='MDCAT - 3 Months', duration_days=90, price=3000,
        )
        paid_user = make_user('already.paying@gmail.com')
        now = timezone.now()
        Subscription.objects.create(
            user=paid_user, plan=plan, status='active',
            starts_at=now, expires_at=now + timezone.timedelta(days=90),
        )

        sub = grant_free_promo_if_eligible(paid_user, self.exam)

        self.assertIsNone(sub)
        self.assertEqual(Subscription.objects.filter(plan__name=PROMO_PLAN_NAME).count(), 0)

        # Their existing paid slot didn't eat into the 30 — next real signup
        # still gets slot #1.
        next_user = make_user('next.student@gmail.com')
        sub = grant_free_promo_if_eligible(next_user, self.exam)
        self.assertIsNotNone(sub)

    def test_guest_is_not_eligible(self):
        guest = User.objects.create_user(username='guest_abc123', password=None)
        sub = grant_free_promo_if_eligible(guest, self.exam)
        self.assertIsNone(sub)

    def test_silent_wrapper_swallows_exceptions(self):
        user = make_user('boom@gmail.com')
        with mock.patch(
            'payments.services.get_or_create_promo_plan',
            side_effect=RuntimeError('DB hiccup'),
        ):
            # Must not raise — registration/signup must survive this.
            result = grant_free_promo_if_eligible_silently(user, self.exam)
        self.assertIsNone(result)

        # The unwrapped function, by contrast, does propagate — that's what
        # lets grant_free_promo_if_eligible_silently's try/except do its job,
        # and what the manual command relies on to surface real errors.
        with mock.patch(
            'payments.services.get_or_create_promo_plan',
            side_effect=RuntimeError('DB hiccup'),
        ):
            with self.assertRaises(RuntimeError):
                grant_free_promo_if_eligible(user, self.exam)


class GrantFreePromoConcurrencyTests(TransactionTestCase):
    """Two signups racing for the last of 30 slots must not both succeed.

    Uses real threads + separate DB connections so the SELECT ... FOR UPDATE
    lock in grant_free_promo_if_eligible actually serializes them — a plain
    TestCase (wrapped in one outer transaction) can't exercise this, hence
    TransactionTestCase here.
    """

    def setUp(self):
        self.exam = Exam.objects.create(
            name='MDCAT', slug='mdcat', level='entry-test',
        )
        # Fill 29 of 30 slots up front so both threads are racing for slot #30.
        for i in range(29):
            grant_free_promo_if_eligible(make_user(f'filler{i}@gmail.com'), self.exam)

    def test_concurrent_signups_do_not_exceed_the_slot_count(self):
        results = {}

        def attempt(key, email):
            user = make_user(email)
            try:
                results[key] = grant_free_promo_if_eligible(user, self.exam)
            finally:
                connection.close()

        t1 = threading.Thread(target=attempt, args=('a', 'racer.a@gmail.com'))
        t2 = threading.Thread(target=attempt, args=('b', 'racer.b@gmail.com'))
        t1.start()
        t2.start()
        t1.join()
        t2.join()

        granted_count = sum(1 for v in results.values() if v is not None)
        self.assertEqual(granted_count, 1, 'exactly one of the two racers should get the last slot')
        self.assertEqual(
            Subscription.objects.filter(plan__name=PROMO_PLAN_NAME).count(), 30,
        )
