"""
Re-tag needs_review=True MCQs in a tagged JSON using a stronger Groq model.
Patches the JSON in place. Idempotent — safe to re-run.

Usage:
    python scripts\retag_flagged.py mdcat-content/parsed-mcqs/MDCAT_2025.json
"""
import json
import os
import sys
import time
from pathlib import Path
from collections import defaultdict

from dotenv import load_dotenv
from groq import Groq

load_dotenv()

MODEL = "llama-3.3-70b-versatile"
BATCH_SIZE = 5           # small — 70B has tighter TPM
SLEEP_BETWEEN_BATCHES = 90  # seconds
SYLLABUS_PATH = Path("mdcat-content/syllabus/pmdc_mdcat_syllabus.json")


def build_prompt(subject_name, syllabus_branch, batch):
    vocab_lines = []
    for topic_name, subtopics in syllabus_branch.items():
        for sub in subtopics:
            vocab_lines.append(f"- Topic: {topic_name} | Subtopic: {sub}")
    vocab = "\n".join(vocab_lines)

    q_lines = []
    for mcq in batch:
        opts = mcq.get("options", {}) or {}
        q_lines.append(
            f"Q{mcq['question_number']}: {mcq['question_text']}\n"
            f"  a) {opts.get('a','')}\n  b) {opts.get('b','')}\n"
            f"  c) {opts.get('c','')}\n  d) {opts.get('d','')}\n"
            f"  correct: {mcq.get('correct_answer','')}"
        )
    questions_block = "\n\n".join(q_lines)

    return f"""You are tagging MDCAT past-paper MCQs to the official PMDC syllabus.

Subject: {subject_name}

Allowed vocabulary (you MUST pick from this list exactly — no paraphrasing):
{vocab}

Tag each question below with the single best (topic, subtopic) pair from the vocabulary.
Return ONLY a JSON object mapping question_number (as string) to {{"topic": "...", "subtopic": "..."}}.
No prose, no markdown fences.

Questions:
{questions_block}
"""


def validate_tag(tag, syllabus_branch):
    """Fuzzy-match Groq output to canonical vocab. Returns cleaned tag or None."""
    def norm(s):
        return "".join(c.lower() for c in s if c.isalnum())

    want_t = norm(tag.get("topic", ""))
    want_s = norm(tag.get("subtopic", ""))
    for topic_name, subtopics in syllabus_branch.items():
        if norm(topic_name) == want_t:
            for sub in subtopics:
                if norm(sub) == want_s:
                    return {"topic": topic_name, "subtopic": sub}
    return None


def main():
    if len(sys.argv) < 2:
        print("Usage: python scripts/retag_flagged.py <tagged_json_path>")
        sys.exit(1)

    json_path = Path(sys.argv[1])
    data = json.loads(json_path.read_text(encoding="utf-8-sig"))
    syllabus = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8-sig"))
    syllabus_by_subject = syllabus["subjects"]

    flagged = [m for m in data if m.get("needs_review")]
    print(f"Total MCQs: {len(data)}  |  Flagged: {len(flagged)}")

    if not flagged:
        print("Nothing to re-tag.")
        return

    by_subject = defaultdict(list)
    for m in flagged:
        by_subject[m["subject"]].append(m)

    client = Groq(api_key=os.environ["GROQ_API_KEY"])
    id_index = {m["id"]: m for m in data}
    fixed = 0
    still_bad = 0

    for subject_name, mcqs in by_subject.items():
        print(f"\n=== {subject_name}: {len(mcqs)} flagged ===")
        branch = syllabus_by_subject.get(subject_name)
        if not branch:
            print(f"  ! no syllabus branch for {subject_name}, skipping")
            still_bad += len(mcqs)
            continue

        for i in range(0, len(mcqs), BATCH_SIZE):
            batch = mcqs[i:i + BATCH_SIZE]
            prompt = build_prompt(subject_name, branch, batch)
            print(f"  batch {i // BATCH_SIZE + 1}: Q#s {[m['question_number'] for m in batch]}")

            try:
                resp = client.chat.completions.create(
                    model=MODEL,
                    messages=[{"role": "user", "content": prompt}],
                    temperature=0,
                    max_tokens=800,
                    response_format={"type": "json_object"},
                )
                result = json.loads(resp.choices[0].message.content)
                print(f"    RAW: {json.dumps(result, indent=2)[:500]}")
            except Exception as e:
                print(f"    ! error: {e}  (checkpoint saved, resume tomorrow)")
                json_path.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
                sys.exit(1)

            for mcq in batch:
                qn = str(mcq["question_number"])
                raw = result.get(qn) or result.get(f"Q{qn}")
                if not raw:
                    still_bad += 1
                    continue
                clean = validate_tag(raw, branch)
                if clean:
                    target = id_index[mcq["id"]]
                    target["topic"] = clean["topic"]
                    target["subtopic"] = clean["subtopic"]
                    target["needs_review"] = False
                    fixed += 1
                else:
                    still_bad += 1
                    print(f"    ! Q{qn}: 70B returned invalid vocab: {raw}")

            # persist after each batch (checkpoint)
            json_path.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")

            if i + BATCH_SIZE < len(mcqs):
                print(f"    sleep {SLEEP_BETWEEN_BATCHES}s")
                time.sleep(SLEEP_BETWEEN_BATCHES)

    print(f"\nDone. fixed: {fixed}  |  still flagged: {still_bad}")
    print(f"JSON updated in place: {json_path}")


if __name__ == "__main__":
    main()