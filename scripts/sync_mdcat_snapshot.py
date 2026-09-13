"""Make another database's MDCAT past papers identical to a snapshot of this one.

Written after the 2026-09-13 content pass over MDCAT 2015-2025, which left the
local DB as the verified source of truth. Instead of replaying incremental
correction files (which only work if the target has had every earlier pass
applied in order), this exports the full content state of each paper and
overwrites the target's rows with it.

    # on the machine with the verified DB
    py -3.14 scripts/sync_mdcat_snapshot.py export 2015 2025

    # on production (dry run first; nothing is written without --apply)
    python scripts/sync_mdcat_snapshot.py apply
    python scripts/sync_mdcat_snapshot.py apply --apply

Rows are matched per paper, never by id (PKs differ between databases):
  1. exact (question_text, option_a) of the snapshot row;
  2. exact match on any earlier wording of that row recorded in
     scripts/mdcat_<year>_corrections_by_content.json (followed through
     chained corrections), so a target that never received a pass still
     matches;
  3. fuzzy stem + option-set similarity, accepted only when clearly unique.
Unmatched rows are reported, never created or deleted. Writing is refused if
any snapshot row matches two target rows or two snapshot rows claim the same
target row.

Overwritten per question: text, options, correct_answer, is_active,
is_verified, is_visual_required, difficulty, explanations.
Overwritten per paper: notes, student_note.
Not touched: subtopic tags, images, attempts, ids.
"""
import json
import os
import re
import sys
import unicodedata
from difflib import SequenceMatcher
from pathlib import Path

import django

ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from django.db import transaction  # noqa: E402
from content.models import PastPaper, Question  # noqa: E402

SNAPSHOT = ROOT / "scripts" / "mdcat_snapshot.json"
Q_FIELDS = ["question_text", "option_a", "option_b", "option_c", "option_d", "correct_answer",
            "is_active", "is_verified", "is_visual_required", "difficulty",
            "explanation_short", "explanation_long", "explanation_trick", "explanation_options"]
P_FIELDS = ["notes", "student_note"]

TR = str.maketrans("₀₁₂₃₄₅₆₇₈₉⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻―–—−ˉ", "01234567890123456789+------")


def norm(s):
    s = unicodedata.normalize("NFKC", (s or "").translate(TR)).lower()
    return re.sub(r"[^a-z0-9α-ω+\-/]", "", s)


def mdcat_papers(y0, y1):
    return [p for p in PastPaper.objects.filter(year__gte=y0, year__lte=y1).select_related("exam").order_by("year")
            if "MDCAT" in str(p.exam).upper()]


def old_keys(year, current_keys):
    """Map each earlier (text, option_a) recorded in the correction file to the
    row's current key, following chains of corrections."""
    path = ROOT / "scripts" / f"mdcat_{year}_corrections_by_content.json"
    if not path.exists():
        return {}
    corr = json.loads(path.read_text(encoding="utf-8"))
    step = {}
    for c in corr:
        pre = (c["match_question_text"], c["match_option_a"])
        post = (c["set"].get("question_text", pre[0]), c["set"].get("option_a", pre[1]))
        if pre != post:
            step[pre] = post
    out = {}
    for pre in step:
        k, seen = pre, set()
        while k in step and k not in seen:
            seen.add(k)
            k = step[k]
        if k in current_keys:
            out[pre] = k
    return out


def export(y0, y1):
    snap = {"papers": []}
    for p in mdcat_papers(y0, y1):
        rows = []
        cur = {}
        for q in Question.objects.filter(past_paper=p).order_by("id"):
            d = {f: getattr(q, f) for f in Q_FIELDS}
            cur[(q.question_text, q.option_a)] = d
            rows.append(d)
        aliases = old_keys(p.year, set(cur))
        for pre, k in aliases.items():
            cur[k].setdefault("aliases", []).append(list(pre))
        snap["papers"].append({"year": p.year, "name": p.name, **{f: getattr(p, f) for f in P_FIELDS},
                               "questions": rows})
        print(f"MDCAT {p.year}: {len(rows)} questions, {len(aliases)} earlier wordings recorded")
    SNAPSHOT.write_text(json.dumps(snap, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"wrote {SNAPSHOT.relative_to(ROOT)}")


def fuzzy_score(a, b):
    st = SequenceMatcher(None, norm(a["question_text"])[:200], norm(b["question_text"])[:200]).ratio()
    oa = "|".join(sorted(norm(a[f]) for f in ("option_a", "option_b", "option_c", "option_d")))
    ob = "|".join(sorted(norm(b[f]) for f in ("option_a", "option_b", "option_c", "option_d")))
    return 0.35 * st + 0.65 * SequenceMatcher(None, oa, ob).ratio()


def apply(write):
    snap = json.loads(SNAPSHOT.read_text(encoding="utf-8"))
    plan, problems, totals = [], [], {"exact": 0, "alias": 0, "fuzzy": 0, "same": 0, "change": 0}
    paper_plan = []
    for sp in snap["papers"]:
        papers = [p for p in mdcat_papers(sp["year"], sp["year"])]
        if len(papers) != 1:
            problems.append(f"MDCAT {sp['year']}: expected 1 paper on target, found {len(papers)}")
            continue
        tp = papers[0]
        pdiff = {f: sp[f] for f in P_FIELDS if getattr(tp, f) != sp[f]}
        if pdiff:
            paper_plan.append((tp, pdiff))
        target = list(Question.objects.filter(past_paper=tp).order_by("id"))
        tkey = {}
        for q in target:
            tkey.setdefault((q.question_text, q.option_a), []).append(q)
        claimed, unmatched = {}, []
        for s in sp["questions"]:
            keys = [(s["question_text"], s["option_a"])] + [tuple(a) for a in s.get("aliases", [])]
            how, hits = None, []
            for i, k in enumerate(keys):
                if k in tkey:
                    hits, how = tkey[k], ("exact" if i == 0 else "alias")
                    break
            if len(hits) > 1:
                problems.append(f"MDCAT {sp['year']}: snapshot row matches {len(hits)} target rows: {s['question_text'][:70]!r}")
                continue
            if not hits:
                scored = sorted(((fuzzy_score(s, {f: getattr(q, f) for f in ("question_text", "option_a", "option_b", "option_c", "option_d")}), q)
                                 for q in target), key=lambda x: -x[0])
                if scored and scored[0][0] >= 0.80 and (len(scored) == 1 or scored[0][0] - scored[1][0] >= 0.05):
                    hits, how = [scored[0][1]], "fuzzy"
                else:
                    best = f"{scored[0][0]:.2f}" if scored else "-"
                    unmatched.append(f"{s['question_text'][:80]!r} (best fuzzy {best})")
                    continue
            q = hits[0]
            if q.id in claimed:
                problems.append(f"MDCAT {sp['year']}: target id {q.id} claimed twice: {s['question_text'][:70]!r}")
                continue
            claimed[q.id] = s
            totals[how] += 1
            diff = {f: s[f] for f in Q_FIELDS if getattr(q, f) != s[f]}
            if diff:
                totals["change"] += 1
                plan.append((sp["year"], how, q, diff))
            else:
                totals["same"] += 1
        extra = [q for q in target if q.id not in claimed]
        print(f"MDCAT {sp['year']}: snapshot {len(sp['questions'])}, target {len(target)}, "
              f"matched {len(claimed)}, snapshot rows unmatched {len(unmatched)}, target rows not in snapshot {len(extra)}")
        for u in unmatched:
            print(f"    UNMATCHED snapshot row: {u}")
        for q in extra:
            print(f"    target-only row id {q.id} (left untouched): {q.question_text[:80]!r}")

    print("\n" + "=" * 72)
    for year, how, q, diff in plan:
        print(f"\nMDCAT {year} target id {q.id} [{how}]")
        for f, v in diff.items():
            old = getattr(q, f)
            if f.startswith("explanation"):
                print(f"  {f}: (rewritten)")
            else:
                print(f"  {f}\n    - {old!r}\n    + {v!r}")
    for tp, pdiff in paper_plan:
        print(f"\nPastPaper MDCAT {tp.year}: updating {list(pdiff)}")
    print("\n" + "=" * 72)
    print(f"matched: {totals['exact']} exact, {totals['alias']} via earlier wording, {totals['fuzzy']} fuzzy")
    print(f"rows to change: {totals['change']}   already identical: {totals['same']}   papers to update: {len(paper_plan)}")
    if problems:
        print("PROBLEMS:")
        for p in problems:
            print("  " + p)
    if not write:
        print("\nDRY RUN - nothing written. Re-run with --apply to save.")
        return
    if problems:
        print("\nRefusing to write while there are problems. Resolve them first.")
        return
    with transaction.atomic():
        for _, _, q, diff in plan:
            for f, v in diff.items():
                setattr(q, f, v)
            q.save(update_fields=list(diff) + ["updated_at"])
        for tp, pdiff in paper_plan:
            for f, v in pdiff.items():
                setattr(tp, f, v)
            tp.save(update_fields=list(pdiff))
    print(f"\nAPPLIED: {len(plan)} questions, {len(paper_plan)} papers.")


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not args or args[0] not in ("export", "apply"):
        print(__doc__)
        sys.exit(1)
    if args[0] == "export":
        y0, y1 = (int(args[1]), int(args[2])) if len(args) >= 3 else (2015, 2025)
        export(y0, y1)
    else:
        apply("--apply" in sys.argv)
