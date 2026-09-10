"""
Failure-path coverage for the Groq explanation fallback.

Every uncached question calls Groq at request time, so each way that call can
go wrong is a live 500 risk. These run without the database: a question that
fails never reaches .save(), so a stub with the handful of attributes the
prompt reads is enough, and the suite stays fast.
"""

import logging
from unittest.mock import patch

import groq
from django.test import SimpleTestCase

from ai_tutor.services import (
    ExplanationUnavailable,
    _is_cacheable,
    _parse_payload,
    generate_explanation,
)


GOOD_PAYLOAD = {
    "short": "Because mitochondria make ATP.",
    "long": "The mitochondrion is the site of oxidative phosphorylation.",
    "trick": "Mito = motor.",
    "options": {
        "a": "Wrong — ribosomes build protein.",
        "b": "Correct — ATP is made here.",
        "c": "Wrong — the nucleus stores DNA.",
        "d": "Wrong — the wall is plant-only.",
    },
}


class StubQuestion:
    """Just enough Question for the prompt and the cache check."""

    id = 4242
    question_text = "Which organelle produces ATP?"
    option_a = "Ribosome"
    option_b = "Mitochondrion"
    option_c = "Nucleus"
    option_d = "Cell wall"
    correct_answer = "B"
    has_cached_explanation = False

    def __init__(self):
        self.saved = False

    def save(self, **kwargs):
        self.saved = True


def _response(content):
    """Shape-compatible stand-in for a Groq chat completion."""

    class Message:
        def __init__(self, c):
            self.content = c

    class Choice:
        def __init__(self, c):
            self.message = Message(c)

    class Completion:
        def __init__(self, c):
            self.choices = [Choice(c)] if c is not _NO_CHOICES else []

    return Completion(content)


_NO_CHOICES = object()


class ParsePayloadTests(SimpleTestCase):
    def test_parses_a_clean_payload(self):
        import json

        result = _parse_payload(json.dumps(GOOD_PAYLOAD))
        self.assertEqual(result["short"], GOOD_PAYLOAD["short"])
        self.assertEqual(sorted(result["options"]), ["a", "b", "c", "d"])

    def test_strips_a_markdown_fence(self):
        import json

        fenced = "```json\n" + json.dumps(GOOD_PAYLOAD) + "\n```"
        self.assertEqual(_parse_payload(fenced)["short"], GOOD_PAYLOAD["short"])

    def test_malformed_json_raises(self):
        with self.assertRaises(ExplanationUnavailable):
            _parse_payload("{not json at all")

    def test_non_object_json_raises(self):
        with self.assertRaises(ExplanationUnavailable):
            _parse_payload('["a list"]')

    def test_missing_optional_fields_degrade_to_empty(self):
        result = _parse_payload('{"short": "Short only."}')
        self.assertEqual(result["short"], "Short only.")
        self.assertEqual(result["long"], "")
        self.assertEqual(result["trick"], "")
        self.assertEqual(result["options"], {})

    def test_null_fields_degrade_to_empty(self):
        result = _parse_payload(
            '{"short": "Fine.", "long": null, "trick": 7, "options": "nope"}'
        )
        self.assertEqual(result["long"], "")
        self.assertEqual(result["trick"], "")
        self.assertEqual(result["options"], {})

    def test_payload_with_no_prose_raises(self):
        with self.assertRaises(ExplanationUnavailable):
            _parse_payload('{"trick": "only a trick"}')


class IsCacheableTests(SimpleTestCase):
    def test_complete_payload_is_cacheable(self):
        self.assertTrue(_is_cacheable(dict(GOOD_PAYLOAD)))

    def test_partial_options_are_not_cacheable(self):
        partial = dict(GOOD_PAYLOAD, options={"a": "x", "b": "y"})
        self.assertFalse(_is_cacheable(partial))

    def test_missing_long_is_not_cacheable(self):
        self.assertFalse(_is_cacheable(dict(GOOD_PAYLOAD, long="")))


@patch("ai_tutor.services.Groq")
class GenerateExplanationFailureTests(SimpleTestCase):
    def setUp(self):
        # These tests deliberately trip the logger.exception branch; without
        # this the expected tracebacks bury the real test output.
        logging.disable(logging.CRITICAL)
        self.addCleanup(logging.disable, logging.NOTSET)

    def _call(self, mock_groq, side_effect=None, content=None):
        client = mock_groq.return_value
        if side_effect is not None:
            client.chat.completions.create.side_effect = side_effect
        else:
            client.chat.completions.create.return_value = _response(content)
        return generate_explanation(StubQuestion())

    def test_timeout_raises_explanation_unavailable(self, mock_groq):
        with self.assertRaises(ExplanationUnavailable):
            self._call(mock_groq, side_effect=groq.APITimeoutError(request=None))

    def test_rate_limit_raises_explanation_unavailable(self, mock_groq):
        import httpx

        response = httpx.Response(
            429, request=httpx.Request("POST", "https://api.groq.com/")
        )
        err = groq.RateLimitError("slow down", response=response, body=None)
        with self.assertRaises(ExplanationUnavailable):
            self._call(mock_groq, side_effect=err)

    def test_bad_api_key_raises_explanation_unavailable(self, mock_groq):
        mock_groq.side_effect = groq.GroqError("The api_key client option must be set")
        with self.assertRaises(ExplanationUnavailable):
            generate_explanation(StubQuestion())

    def test_unwrapped_exception_raises_explanation_unavailable(self, mock_groq):
        with self.assertRaises(ExplanationUnavailable):
            self._call(mock_groq, side_effect=OSError("DNS went away"))

    def test_empty_string_response_raises(self, mock_groq):
        with self.assertRaises(ExplanationUnavailable):
            self._call(mock_groq, content="")

    def test_none_response_raises(self, mock_groq):
        with self.assertRaises(ExplanationUnavailable):
            self._call(mock_groq, content=None)

    def test_whitespace_only_response_raises(self, mock_groq):
        with self.assertRaises(ExplanationUnavailable):
            self._call(mock_groq, content="   \n  ")

    def test_no_choices_raises(self, mock_groq):
        with self.assertRaises(ExplanationUnavailable):
            self._call(mock_groq, content=_NO_CHOICES)

    def test_partial_payload_is_served_but_not_cached(self, mock_groq):
        client = mock_groq.return_value
        client.chat.completions.create.return_value = _response(
            '{"short": "Short only.", "long": "A bit longer."}'
        )
        question = StubQuestion()
        result = generate_explanation(question)
        self.assertEqual(result["short"], "Short only.")
        self.assertFalse(
            question.saved,
            "a partial explanation must not poison the cache",
        )

    def test_complete_payload_is_cached(self, mock_groq):
        import json

        client = mock_groq.return_value
        client.chat.completions.create.return_value = _response(
            json.dumps(GOOD_PAYLOAD)
        )
        question = StubQuestion()
        result = generate_explanation(question)
        self.assertEqual(result["short"], GOOD_PAYLOAD["short"])
        self.assertTrue(question.saved)

    def test_cache_hit_never_calls_groq(self, mock_groq):
        question = StubQuestion()
        question.has_cached_explanation = True
        question.explanation_short = "cached short"
        question.explanation_long = "cached long"
        question.explanation_trick = "cached trick"
        question.explanation_options = {"a": "1", "b": "2", "c": "3", "d": "4"}
        result = generate_explanation(question)
        self.assertEqual(result["short"], "cached short")
        mock_groq.assert_not_called()
