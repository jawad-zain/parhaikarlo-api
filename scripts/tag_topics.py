"""
Tag parsed MCQs with topic + subtopic using Groq (Llama 3.3 70B).

Batches by subject — 5 API calls per paper total (Bio/Chem/Phys/Eng/LR),
not one per question. Uses the PMDC MDCAT syllabus as a closed vocabulary
so Groq can't invent topic names.

Usage:
    python scripts/tag_topics.py mdcat-content/parsed-mcqs/MDCAT_2025.json
    python scripts/tag_topics.py mdcat-content/parsed-mcqs/MDCAT_2025.json --dry-run
    python scripts/tag_topics.py mdcat-content/parsed-mcqs/MDCAT_2025.json --subject Biology

Env:
    GROQ_API_KEY must be set (in .env or shell).

Output:
    Writes tags back into the same JSON file. Each MCQ gets:
        topic: "Inheritance"
        subtopic: "Mendel's Laws of Inheritance"
        tag_confidence: "high" | "medium" | "low"
        needs_review: True if confidence=low OR Groq returned invalid tag
"""

import argparse
import json
import os
import shutil
import sys
import time
from collections import defaultdict
from pathlib import Path

try:
    from groq import Groq
except ImportError:
    sys.exit("Missing dependency. Run: pip install groq python-dotenv")

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass  # optional — env may be set in shell


MODEL = "llama-3.1-8b-instant"
DEFAULT_SYLLABUS = "mdcat-content/syllabus/pmdc_mdcat_syllabus.json"
BATCH_SIZE = 15           # MCQs per Groq call — keeps under 8B's 6k TPM
SLEEP_BETWEEN_CALLS = 65  # seconds — respects TPM rolling window

SYSTEM_PROMPT = """You are an expert tagger for the Pakistani MDCAT exam curriculum (PMDC 2025).
Your job: classify each multiple-choice question into the official syllabus.

RULES:
1. You will receive a VOCABULARY (topic -> list of subtopics) and a list of QUESTIONS.
2. For each question, pick exactly ONE topic and ONE subtopic FROM THE VOCABULARY.
3. Copy the topic and subtopic strings EXACTLY as given. Do not paraphrase, do not invent.
4. If the question is ambiguous or you're unsure, still pick the closest match and set confidence="low".
5. Confidence guide: "high" = obvious fit, "medium" = plausible but not perfect, "low" = best guess.
6. Return ONLY a JSON object. No prose, no markdown fences.

OUTPUT SCHEMA:
{
  "tags": {
    "<question_id>": {"topic": "<exact topic name>", "subtopic": "<exact subtopic name>", "confidence": "high"}
  }
}

Every question ID from the input MUST appear in "tags". No skipping."""


def format_vocab(subject_tree: dict) -> str:
    """Render the subject's topic->subtopics tree as a compact string for the prompt."""
    lines = []
    for topic, subtopics in subject_tree.items():
        lines.append(f"- {topic}")
        for st in subtopics:
            lines.append(f"    * {st}")
    return "\n".join(lines)


def format_questions(mcqs: list) -> str:
    """Compact one-line-per-MCQ representation. Trims long options."""
    out = []
    for mcq in mcqs:
        opts = mcq.get("options", {}) or {}
        # trim each option to ~80 chars — enough signal, keeps prompt small
        opts_str = " | ".join(
            f"{k}) {(opts.get(k, '') or '')[:80]}"
            for k in ("a", "b", "c", "d")
        )
        q_text = (mcq.get("question_text", "") or "")[:400]
        out.append(f'{{"id": "{mcq["id"]}", "q": "{q_text}", "opts": "{opts_str}"}}')
    return "[\n  " + ",\n  ".join(out) + "\n]"


def tag_subject(client: Groq, subject: str, subject_tree: dict, mcqs: list) -> dict:
    """One Groq call for one subject. Returns dict {q_id: {topic, subtopic, confidence}}."""
    vocab = format_vocab(subject_tree)
    questions = format_questions(mcqs)

    user_msg = f"""SUBJECT: {subject}

VOCABULARY (topic -> subtopics):
{vocab}

QUESTIONS TO TAG ({len(mcqs)} total):
{questions}

Return JSON mapping every question id to {{topic, subtopic, confidence}}. Use only topic/subtopic names from the VOCABULARY above."""

    print(f"  calling Groq for {subject} ({len(mcqs)} MCQs)...", flush=True)
    resp = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_msg},
        ],
        response_format={"type": "json_object"},
        temperature=0.1,
        max_tokens=1500,
    )
    raw = resp.choices[0].message.content
    try:
        data = json.loads(raw)
    except json.JSONDecodeError as e:
        print(f"  ERROR: Groq returned invalid JSON for {subject}: {e}")
        print(f"  raw: {raw[:500]}")
        return {}

    tags = data.get("tags", data)  # accept both {"tags": {...}} and flat {...}
    return tags


def _normalize(s):
    """Lowercase, strip apostrophes/quotes/parens — for fuzzy vocab matching."""
    return (
        s.lower()
        .replace("'", "").replace("\u2019", "").replace("\u2018", "")
        .replace('"', "").replace("\u201c", "").replace("\u201d", "")
        .strip()
    )


def validate_tag(tag, subject_tree):
    """Fuzzy-match Groq's tag against the vocabulary. Returns (ok, reason, canonical_topic, canonical_subtopic)."""
    topic_in = (tag.get("topic") or "").strip()
    subtopic_in = (tag.get("subtopic") or "").strip()

    # Fuzzy match topic
    topic_norm = _normalize(topic_in)
    canonical_topic = None
    for t in subject_tree:
        t_norm = _normalize(t)
        if t_norm == topic_norm or topic_norm in t_norm or t_norm in topic_norm:
            canonical_topic = t
            break
    if not canonical_topic:
        return False, f"topic '{topic_in}' not in vocabulary", None, None

    # Fuzzy match subtopic within that topic
    subtopic_norm = _normalize(subtopic_in)
    canonical_subtopic = None
    for st in subject_tree[canonical_topic]:
        st_norm = _normalize(st)
        if st_norm == subtopic_norm or subtopic_norm in st_norm or st_norm in subtopic_norm:
            canonical_subtopic = st
            break
    if not canonical_subtopic:
        return False, f"subtopic '{subtopic_in}' not under topic '{canonical_topic}'", None, None

    return True, "", canonical_topic, canonical_subtopic


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("json_path", help="Path to parsed MCQ JSON (e.g. mdcat-content/parsed-mcqs/MDCAT_2025.json)")
    ap.add_argument("--syllabus", default=DEFAULT_SYLLABUS, help=f"Syllabus JSON path (default: {DEFAULT_SYLLABUS})")
    ap.add_argument("--subject", help="Tag only one subject (Biology/Chemistry/Physics/English/Logical Reasoning)")
    ap.add_argument("--dry-run", action="store_true", help="Show what would be tagged without writing")
    ap.add_argument("--no-backup", action="store_true", help="Skip .bak file (default: creates one)")
    args = ap.parse_args()

    json_path = Path(args.json_path)
    syllabus_path = Path(args.syllabus)

    if not json_path.exists():
        sys.exit(f"MCQ file not found: {json_path}")
    if not syllabus_path.exists():
        sys.exit(f"Syllabus file not found: {syllabus_path}")

    api_key = os.environ.get("GROQ_API_KEY")
    if not api_key:
        sys.exit("GROQ_API_KEY not set. Add it to .env or your shell.")

    syllabus = json.loads(syllabus_path.read_text(encoding="utf-8-sig"))
    subjects_vocab = syllabus["subjects"]

    mcqs = json.loads(json_path.read_text(encoding="utf-8"))
    print(f"Loaded {len(mcqs)} MCQs from {json_path.name}")
    print(f"Syllabus: {syllabus_path.name} ({sum(len(v) for v in subjects_vocab.values())} topics)")

    # Group MCQs by subject (as parsed from PDF headers)
    by_subject = defaultdict(list)
    for mcq in mcqs:
        subj = (mcq.get("subject") or "").strip()
        by_subject[subj].append(mcq)

    print("\nMCQs per subject (from parser):")
    for subj, group in sorted(by_subject.items()):
        print(f"  {subj}: {len(group)}")

    # Map parser-subject-names to syllabus-subject-names.
    # Adjust these if your parser emits different strings.
    subject_alias = {
        "BIOLOGY": "Biology",
        "CHEMISTRY": "Chemistry",
        "PHYSICS": "Physics",
        "ENGLISH": "English",
        "LOGICAL REASONING": "Logical Reasoning",
    }

    client = Groq(api_key=api_key)

    # Tag each subject in turn
    all_tags = {}
    for parser_subj, group in by_subject.items():
        canonical = subject_alias.get(parser_subj.upper(), parser_subj)
        if canonical not in subjects_vocab:
            print(f"\n  SKIP {parser_subj}: no vocabulary for '{canonical}' in syllabus")
            continue
        if args.subject and canonical.lower() != args.subject.lower():
            continue

        subject_tree = subjects_vocab[canonical]
        checkpoint_path = json_path.with_suffix(f".checkpoint.{canonical.lower().replace(' ', '_')}.json")

        # Resume from checkpoint if exists
        if checkpoint_path.exists():
            tags = json.loads(checkpoint_path.read_text(encoding="utf-8"))
            print(f"  resumed from checkpoint: {len(tags)} MCQs already tagged")
        else:
            tags = {}

        total_batches = (len(group) + BATCH_SIZE - 1) // BATCH_SIZE
        for i in range(0, len(group), BATCH_SIZE):
            batch = group[i:i + BATCH_SIZE]
            # Skip batches where all MCQs are already tagged
            if all(mcq["id"] in tags for mcq in batch):
                print(f"  batch {i // BATCH_SIZE + 1}/{total_batches} — skipped (already in checkpoint)")
                continue
            batch_num = i // BATCH_SIZE + 1
            print(f"  batch {batch_num}/{total_batches} ({len(batch)} MCQs)")
            batch_tags = tag_subject(client, canonical, subject_tree, batch)
            tags.update(batch_tags)

            # Save checkpoint after every successful batch
            checkpoint_path.write_text(json.dumps(tags, indent=2), encoding="utf-8")

            if i + BATCH_SIZE < len(group):
                print(f"  sleeping {SLEEP_BETWEEN_CALLS}s (rate limit)...")
                time.sleep(SLEEP_BETWEEN_CALLS)
 
        valid = 0

        invalid = 0
        low_conf = 0
        for q_id, tag in tags.items():
            ok, reason, _, _ = validate_tag(tag, subject_tree)
            if not ok:
                print(f"    invalid tag for {q_id}: {reason}")
                invalid += 1
            else:
                valid += 1
            if tag.get("confidence") == "low":
                low_conf += 1

        print(f"  {canonical}: {valid} valid, {invalid} invalid, {low_conf} low-confidence")
        all_tags.update(tags)

    # Merge tags back into MCQs
    tagged_count = 0
    review_flagged = 0
    for mcq in mcqs:
        q_id = mcq["id"]
        if q_id not in all_tags:
            continue
        tag = all_tags[q_id]

        canonical_subj = subject_alias.get(
            (mcq.get("subject") or "").upper(), mcq.get("subject", "")
        )
        subject_tree = subjects_vocab.get(canonical_subj, {})
        ok, _, canonical_topic, canonical_subtopic = validate_tag(tag, subject_tree)

        # Use canonical (vocab-exact) names when valid, raw Groq output otherwise
        mcq["topic"] = canonical_topic if ok else tag.get("topic", "").strip()
        mcq["subtopic"] = canonical_subtopic if ok else tag.get("subtopic", "").strip()
        mcq["tag_confidence"] = tag.get("confidence", "low")

        # Flag for review if: Groq returned invalid vocab OR low confidence
        if not ok or mcq["tag_confidence"] == "low":
            mcq["needs_review"] = True
            review_flagged += 1
        tagged_count += 1

    print(f"\nSummary: {tagged_count}/{len(mcqs)} tagged, {review_flagged} flagged for review")

    if args.dry_run:
        print("\nDRY RUN — no file written.")
        # Print first 3 tagged examples so you can eyeball
        shown = 0
        for mcq in mcqs:
            if "topic" in mcq and shown < 3:
                print(f"\n  {mcq['id']} [{mcq['subject']}]")
                print(f"  Q: {mcq['question_text'][:120]}...")
                print(f"  -> topic={mcq['topic']} / subtopic={mcq['subtopic']} ({mcq['tag_confidence']})")
                shown += 1
        return

    # Backup original before overwriting
    if not args.no_backup:
        backup_path = json_path.with_suffix(json_path.suffix + ".bak")
        shutil.copy(json_path, backup_path)
        print(f"Backup: {backup_path.name}")

    json_path.write_text(json.dumps(mcqs, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Wrote tagged MCQs to {json_path}")


if __name__ == "__main__":
    main()