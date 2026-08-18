"""
Parse a clean MDCAT past-paper PDF into JSON MCQ objects.
Supports three source formats:
  - 2025 style: 'BIOLOGY (68 MCQs)' header, '(a) foo' options, 'OFFICIAL ANSWER KEY' + 'N. L' pairs
  - 2024 style: plain 'BIOLOGY' header, 'A. foo B. bar' options, tabular 'Q Ans Q Ans' key
  - 2023 style: 'Q .' marker on its own line with question number on next line,
                'A. foo\\nB. bar' one-per-line options, tabular 'Q# Ans' key,
                5 UHS-deleted questions given full credit (skipped at output).
"""

import json
import re
import sys
from pathlib import Path

import pdfplumber


SUBJECT_HEADERS = {
    "BIOLOGY": "Biology",
    "CHEMISTRY": "Chemistry",
    "PHYSICS": "Physics",
    "ENGLISH": "English",
    "LOGICAL REASONING": "Logical Reasoning",
}

# UHS-deleted questions (full credit given) — skipped at output time
DELETED_QUESTIONS: dict[int, set[int]] = {
    2023: {1, 64, 176, 189, 190},
}


def extract_year_from_filename(path: Path) -> int:
    m = re.search(r"(\d{4})", path.stem)
    return int(m.group(1)) if m else 0


def read_pdf(pdf_path: Path) -> str:
    with pdfplumber.open(pdf_path) as pdf:
        pages = [page.extract_text() or "" for page in pdf.pages]
    return "\n".join(pages)


def normalize_2023_markers(text: str) -> str:
    """2023 format: `Q .` on its own line, then question text (possibly multi-line)
    with the question number appearing on its own line SOMEWHERE inside the text,
    then options `A. ... B. ... C. ... D. ...` one per line.
    The number's line can carry a stray trailing token (e.g. a subscript digit
    from notation like F2 that pdfplumber split onto the number's line, giving
    "21 2" instead of a clean "21").
    Normalizes each Q-block to standard `<n>. <question>\\n` inline form so
    downstream parsing works unchanged. No-op for 2024/2025 formats.
    """
    def repl(match):
        block = match.group(1)
        num_match = re.search(
            r"^\s*(\d+)(?:\s+\S{1,4})?\s*$", block, flags=re.MULTILINE
        )
        if not num_match:
            return match.group(0)  # leave unchanged if no number found
        qnum = num_match.group(1)
        cleaned = block[: num_match.start()] + block[num_match.end():]
        cleaned = re.sub(r"\s+", " ", cleaned).strip()
        return f"\n{qnum}. {cleaned}\n"

    pattern = re.compile(
        r"^Q\s*\.\s*(.+?)(?=\n[A-D]\.\s)",
        re.MULTILINE | re.DOTALL,
    )
    return pattern.sub(repl, text)

    # Match `Q .` (start of line) through to just before the first option line
    pattern = re.compile(
        r"^Q\s*\.\s*(.+?)(?=\n[A-D]\.\s)",
        re.MULTILINE | re.DOTALL,
    )
    return pattern.sub(repl, text)

def split_by_subject(text: str) -> list[tuple[str, str]]:
    """Header must be on its own line. Optional '(N MCQs)' suffix."""
    pattern = "|".join(SUBJECT_HEADERS.keys())
    header_re = re.compile(
        rf"^\s*({pattern})\s*(?:\(\d+\s*MCQs?\))?\s*$",
        re.MULTILINE | re.IGNORECASE,
    )
    matches = list(header_re.finditer(text))

    if not matches:
        return [("Unknown", text)]

    chunks = []
    for i, m in enumerate(matches):
        subject = SUBJECT_HEADERS[m.group(1).upper()]
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        chunks.append((subject, text[start:end]))
    return chunks


def find_answer_key_boundary(text: str) -> int:
    """Char index where answers begin. Handles all formats. -1 if not found."""
    m1 = re.search(r"^\s*OFFICIAL ANSWER KEY\s*$", text, re.MULTILINE)
    if m1:
        return m1.start()
    m2 = re.search(
        r"^\s*(?:Q#?\s+Ans\s*){2,}$",
        text,
        re.MULTILINE | re.IGNORECASE,
    )
    if m2:
        return m2.start()
    return -1


def parse_answer_key(text: str) -> dict[int, str]:
    """Returns {qnum: 'a'|'b'|'c'|'d'}."""
    boundary = find_answer_key_boundary(text)
    if boundary < 0:
        return {}
    key_text = text[boundary:]

    # Try 2025 style first: 'N. L'
    pairs = re.findall(r"(\d+)\.\s*([A-Da-d])\b", key_text)
    # Fall back to 2024/2023 tabular: 'N L'
    if len(pairs) < 100:
        pairs = re.findall(r"\b(\d+)\s+([A-Da-d])\b", key_text)

    answers = {}
    for qnum, letter in pairs:
        qn = int(qnum)
        if 1 <= qn <= 200:
            answers[qn] = letter.lower()
    return answers


def parse_options(body: str):
    """Try both (a) and A. option styles. Returns (options_dict, question_text) or (None, body)."""
    # Style 1: '(a) foo (b) bar'
    opt_re = re.compile(r"\(([a-dA-D])\)\s*(.+?)(?=\([a-dA-D]\)|\Z)", re.DOTALL)
    matches = opt_re.findall(body)
    if len(matches) >= 4:
        first = re.search(r"\([a-dA-D]\)", body)
        q_text = body[:first.start()].strip()
        options = {L.lower(): re.sub(r"\s+", " ", t).strip() for L, t in matches[:4]}
        return options, q_text

    # Style 2: 'A. foo B. bar' or one-per-line 'A. foo\nB. bar\nC. baz\nD. qux'
    # Options begin at newline-anchored 'A.'
    a_match = re.search(r"\n\s*A\.\s", body)
    if a_match:
        q_text = body[:a_match.start()].strip()
        opts_text = body[a_match.start():].strip()
        opts_flat = re.sub(r"\s+", " ", opts_text)  # flatten multi-line
        alt = re.findall(r"\b([A-D])\.\s+(.+?)(?=\s+[A-D]\.\s+|$)", opts_flat)
        if len(alt) == 4:
            options = {L.lower(): t.strip() for L, t in alt}
            return options, q_text

    return None, body


def parse_single_mcq(qnum: int, body: str, subject: str) -> dict:
    options, q_text = parse_options(body)
    if options is None:
        return {
            "question_number": qnum,
            "subject": subject,
            "question_text": re.sub(r"\s+", " ", body[:300]).strip(),
            "options": {},
            "needs_review": True,
        }
    return {
        "question_number": qnum,
        "subject": subject,
        "question_text": re.sub(r"\s+", " ", q_text).strip(),
        "options": options,
        "needs_review": False,
    }


def parse_mcqs_from_chunk(chunk: str, subject: str) -> list[dict]:
    q_pattern = re.compile(
        r"^(\d+)\.\s*(.+?)(?=^\d+\.\s|\Z)",
        re.MULTILINE | re.DOTALL,
    )
    mcqs = []
    for m in q_pattern.finditer(chunk):
        qnum = int(m.group(1))
        if qnum > 200:
            continue
        body = m.group(2).strip()
        mcqs.append(parse_single_mcq(qnum, body, subject))
    return mcqs


def parse_paper(pdf_path: Path, year: int) -> list[dict]:
    text = read_pdf(pdf_path)
    text = normalize_2023_markers(text)

    answers = parse_answer_key(text)
    print(f"  found {len(answers)} answer key entries")

    boundary = find_answer_key_boundary(text)
    if boundary >= 0:
        text = text[:boundary]

    all_mcqs = []
    for subject, chunk in split_by_subject(text):
        chunk_mcqs = parse_mcqs_from_chunk(chunk, subject)
        print(f"  {subject}: {len(chunk_mcqs)} MCQs parsed")
        all_mcqs.extend(chunk_mcqs)

    deleted = DELETED_QUESTIONS.get(year, set())
    skipped_deleted = []
    final = []
    for mcq in all_mcqs:
        qnum = mcq["question_number"]
        if qnum in deleted:
            skipped_deleted.append(qnum)
            continue
        record = {
            "id": f"mdcat-{year}-q{qnum}",
            "paper_year": year,
            "question_number": qnum,
            "subject": mcq["subject"],
            "topic": None,
            "difficulty": None,
            "question_text": mcq["question_text"],
            "options": mcq["options"],
            "correct_answer": answers.get(qnum),
            "explanation": None,
            "needs_review": mcq["needs_review"] or (qnum not in answers) or (len(mcq["options"]) != 4),
            "source_file": pdf_path.name,
        }
        final.append(record)

    if deleted:
        found = set(skipped_deleted)
        print(f"  skipped {len(found)} UHS-deleted Qs: {sorted(found)}")
        missing = deleted - found
        if missing:
            print(f"  WARN: deleted-list Qs not found in source: {sorted(missing)}")

    return final


def main():
    if len(sys.argv) != 2:
        print("Usage: python scripts/parse_mcqs.py <path-to-pdf>")
        sys.exit(1)

    pdf_path = Path(sys.argv[1]).resolve()
    if not pdf_path.exists():
        print(f"Not found: {pdf_path}")
        sys.exit(1)

    year = extract_year_from_filename(pdf_path)
    print(f"[{pdf_path.name}] year={year}")

    mcqs = parse_paper(pdf_path, year)

    out_dir = Path("mdcat-content/parsed-mcqs")
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / (pdf_path.stem + ".json")
    out_path.write_text(json.dumps(mcqs, indent=2, ensure_ascii=False), encoding="utf-8")

    ok = sum(1 for m in mcqs if not m["needs_review"])
    review = sum(1 for m in mcqs if m["needs_review"])
    print(f"[{pdf_path.name}] done -- {ok} clean, {review} need review")
    print(f"[{pdf_path.name}] output -> {out_path}")


if __name__ == "__main__":
    main()