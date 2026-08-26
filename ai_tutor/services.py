import json

from django.conf import settings
from django.utils import timezone
from groq import Groq


def generate_explanation(question):
    """
    Return a cached explanation if available.
    Otherwise generate one with Groq, save it, and return it.
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
    client = Groq(api_key=settings.GROQ_API_KEY)

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

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        temperature=0.2,
    )

    content = response.choices[0].message.content.strip()
    result = json.loads(content)

    # 3. Save the generated explanation
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

    return result