import json
import logging

from django.conf import settings
from django.utils import timezone
import groq
from groq import Groq

logger = logging.getLogger(__name__)

# Every question without a cached explanation calls Groq at request time, with a
# student watching a "Thinking…" spinner. Ten seconds is about as long as that
# spinner stays believable; past it, a retry beats a longer wait.
GROQ_TIMEOUT_SECONDS = 10

OPTION_LETTERS = ('a', 'b', 'c', 'd')


class ExplanationUnavailable(Exception):
    """Groq could not be reached, or returned something we can't use."""


def _text(value):
    """Groq occasionally returns null or a number where prose was asked for."""
    return value.strip() if isinstance(value, str) else ''


def _parse_payload(content):
    """
    Turn the raw model output into {short, long, trick, options}.

    Missing or non-string fields degrade to empty rather than raising — the
    review UI guards every field except short/long, so a partial answer is
    still worth showing. Only a payload with neither short nor long is
    treated as a failure.
    """
    # "Return ONLY valid JSON" is a request, not a guarantee: the model still
    # wraps the object in a ```json fence often enough to matter.
    if content.startswith('```'):
        content = content.split('\n', 1)[-1]
        content = content.rsplit('```', 1)[0]
        content = content.strip()

    try:
        raw = json.loads(content)
    except (ValueError, TypeError) as exc:
        raise ExplanationUnavailable('Groq returned malformed JSON') from exc

    if not isinstance(raw, dict):
        raise ExplanationUnavailable('Groq returned JSON that is not an object')

    raw_options = raw.get('options')
    if not isinstance(raw_options, dict):
        raw_options = {}

    result = {
        'short': _text(raw.get('short')),
        'long': _text(raw.get('long')),
        'trick': _text(raw.get('trick')),
        'options': {
            letter: _text(raw_options.get(letter))
            for letter in OPTION_LETTERS
            if _text(raw_options.get(letter))
        },
    }

    if not result['short'] and not result['long']:
        raise ExplanationUnavailable('Groq returned no usable explanation text')

    return result


def _is_cacheable(result):
    """
    Mirror Question.has_cached_explanation. A partial result is fine to show
    once but must not be written to the cache: it would never satisfy the
    cache check on the next read, so every future request would pay for a
    fresh Groq call anyway, and the admin would see a half-filled row.
    """
    return bool(
        result['short']
        and result['long']
        and all(result['options'].get(letter) for letter in OPTION_LETTERS)
    )


def generate_explanation(question):
    """
    Return a cached explanation if available.
    Otherwise generate one with Groq, save it, and return it.

    Raises ExplanationUnavailable if Groq fails or answers with something
    unusable; the caller turns that into a 503 rather than a 500.
    """

    # 1. Cache hit — no AI call
    if question.has_cached_explanation:
        return {
            "short": question.explanation_short,
            "long": question.explanation_long,
            "trick": question.explanation_trick,
            "options": question.explanation_options,
        }

    # 2. Cache miss — call Groq
    prompt = f"""
You are a helpful MDCAT tutor.

Explain the following MCQ in simple English for a Pakistani medical-entry-test student.

IMPORTANT:
- The provided correct answer is authoritative. Do not change it.
- Do not invent information.
- Keep the explanation concise.
- Return ONLY valid JSON.
- Do not use Markdown.
- Do not add anything outside the JSON.

Question:
{question.question_text}

A. {question.option_a}
B. {question.option_b}
C. {question.option_c}
D. {question.option_d}

Correct answer:
{question.correct_answer}

Return exactly this structure:

{{
    "short": "A very short explanation of why the correct answer is correct.",
    "long": "A simple but slightly more detailed explanation.",
    "trick": "A short and easy memory trick.",
    "options": {{
        "a": "One sentence on why option A is correct or incorrect.",
        "b": "One sentence on why option B is correct or incorrect.",
        "c": "One sentence on why option C is correct or incorrect.",
        "d": "One sentence on why option D is correct or incorrect."
    }}
}}
"""

    try:
        # Client construction validates the API key, so it belongs inside the
        # guard too — a missing or blank key raises here, not at call time.
        client = Groq(
            api_key=settings.GROQ_API_KEY,
            timeout=GROQ_TIMEOUT_SECONDS,
            max_retries=1,
        )
        response = client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            temperature=0.2,
            timeout=GROQ_TIMEOUT_SECONDS,
        )
    except groq.GroqError as exc:
        logger.warning(
            "Groq explain failed for question %s: %s", question.id, exc,
        )
        raise ExplanationUnavailable(str(exc)) from exc
    except Exception as exc:
        # Anything the SDK does not wrap — DNS, TLS, a proxy hanging up.
        logger.exception(
            "Unexpected Groq failure for question %s", question.id,
        )
        raise ExplanationUnavailable(str(exc)) from exc

    try:
        content = response.choices[0].message.content
    except (AttributeError, IndexError, KeyError, TypeError) as exc:
        raise ExplanationUnavailable('Groq returned no choices') from exc

    if not isinstance(content, str) or not content.strip():
        raise ExplanationUnavailable('Groq returned an empty response')

    result = _parse_payload(content.strip())

    # 3. Save the generated explanation — only when it is complete enough to
    # count as a cache hit next time.
    if _is_cacheable(result):
        question.explanation_short = result["short"]
        question.explanation_long = result["long"]
        question.explanation_trick = result["trick"]
        question.explanation_options = result["options"]
        question.explanation_generated_at = timezone.now()
        question.save(
            update_fields=[
                "explanation_short",
                "explanation_long",
                "explanation_trick",
                "explanation_options",
                "explanation_generated_at",
                "updated_at",
            ]
        )
    else:
        logger.info(
            "Partial explanation for question %s — served but not cached",
            question.id,
        )

    return result
