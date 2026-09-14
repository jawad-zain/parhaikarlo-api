"""Normalize ASCII math/chemistry notation to Unicode across all MDCAT mock
questions (question_text, option_a-d, explanation_short/long/trick,
explanation_options) -- e.g. 'm/s^2' -> 'm/s\u00b2', 'H2O' -> 'H\u2082O',
'Na+' -> 'Na\u207a', '->' -> '\u2192'.

All 20 mocks were authored with plain ASCII notation throughout (not OCR'd,
not corrupted -- verified: 0 mojibake/control-char/leftover-markup hits).
This is pure typography normalization to match the Unicode style used in the
past-paper content, using an explicitly hand-reviewed whitelist of real
formulas/ions (not a blind regex) to avoid touching lookalike physics/bio
labels that are NOT chemical formulas (R1/R2/R3 resistors, T3/T4 thyroid
hormones, G0-G3 cell-cycle phases, C3/C4 photosynthesis pathways, SN1/SN2/E1/E2
reaction-mechanism names, B12/GLUT4/P450/P680/P700 protein/complex names).

Safe by default: prints the full before/after diff and writes nothing unless
--apply is passed. Fully idempotent and database-independent (no row ids
anywhere in the logic, see FULL_OVERRIDE_BY_OLD/PATCHES below) -- the exact
same script runs unchanged on any database, local or production.

Usage (from backend/, with the target DB configured in .env):
    py -3.14 scripts/fix_mock_notation.py
    py -3.14 scripts/fix_mock_notation.py --apply
    py -3.14 scripts/fix_mock_notation.py 5 14 --apply   # only mocks 5 and 14
"""
import os
import re
import sys
from pathlib import Path

import django

ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()
from quiz.models import MockTest  # noqa: E402

SUP = str.maketrans("0123456789+-", "⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻")
SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")

# ---- verified real chemical formulas / physics-equation variables (subscript
# every digit in the token) -- hand-reviewed against mock content, see
# mdcat-content/tmp_2010/recheck_tools/tokens_out.txt / tokens3_out.txt for
# the full candidate dump this was built from.
FORMULAS = """
O2 H2 H2O N2 H2SO4 Cl2 C6H12O6 N2O4 Fe2O3 Na2SO4 Br2 I2 H2S K2SO4 C3H8 C2H4 O3
C2H5OH Na2CO3 C2H6O C4H10 Al2O3 C2H6 H2A C2H4Br2 N2H4 H2O2 CO2 NH3 CH4 NO3
PCl5 CaCO3 CH3COOH NH2 SO2 CuSO4 CH2 CCl4 PCl3 SO4 NH4 NO2 CaCl2 CH3COONa
FeSO4 BF3 ZnCl2 NH4Cl HNO3 MgCl2 BeCl2 CONH2 SF6 HCO3 SO3 ZnSO4 NaNO3 MnO2
MnCl2 KNO3 BaCl2 CH3 CH3Cl FeCl2 KMnO4 H2CO3 PO2 PCO2 FeCl3 CH3CH2OH C6H6
C12H22O11 H3O AlCl3 C3H8O AgNO3 X2 AX6 AX5 AX4 AX4E2 CH2OH CH3OCH3 NR2
P1V1 P2V2 M1V1 M2V2 T1P2 P1V1T2 Gm1m2 Gm1 Gm2 m1 m2 q1 q2 kq1q2
""".split()
# NOTE: "CH3COO" (neutral, uncharged) is deliberately NOT here -- acetate in
# this corpus only ever appears charged (CH3COO-), and having the bare form
# whitelisted too would greedily match first and swallow the trailing "-"
# before the COO- ion entry below ever got a chance to see it.

# ---- verified real ions (exact hand-checked mapping: only the terminal
# digit immediately touching the +/- sign is the charge magnitude and goes
# superscript with the sign; any other digits are subscript atom counts).
IONS = {
    "H+": "H⁺", "Na+": "Na⁺", "K+": "K⁺", "OH-": "OH⁻", "Cu2+": "Cu²⁺",
    "Mg2+": "Mg²⁺", "Zn2+": "Zn²⁺", "NH4+": "NH₄⁺", "Ag+": "Ag⁺", "Cl-": "Cl⁻",
    "Pb2+": "Pb²⁺", "COO-": "COO⁻", "HCO3-": "HCO₃⁻", "Ca2+": "Ca²⁺",
    "Al3+": "Al³⁺", "I-": "I⁻", "NO3-": "NO₃⁻", "Ni2+": "Ni²⁺", "Fe2+": "Fe²⁺",
    "NAD+": "NAD⁺", "NADP+": "NADP⁺", "Br-": "Br⁻", "CN-": "CN⁻",
    "NH2-": "NH₂⁻", "H3O+": "H₃O⁺", "S2-": "S²⁻", "H2A+": "H₂A⁺",
    "NH3+": "NH₃⁺", "Sc3+": "Sc³⁺", "Fe3+": "Fe³⁺", "Sn2+": "Sn²⁺",
    "He2+": "He²⁺", "O2-": "O²⁻",
    # hardcoded as one token rather than cascading CH3 + COO-: "CH3" alone
    # can't match when directly followed by more letters (boundary rule), and
    # "CH3COO" bare is deliberately not in FORMULAS (see note above)
    "CH3COO-": "CH₃COO⁻",
}

# ---- polyatomic-group multipliers: "(GROUP)N" e.g. Cu(NO3)2, Fe(OH)3 -- the
# trailing N is a subscript multiplying the whole parenthesised group, and
# the "(" itself is commonly preceded by another element letter (Cu, Fe...)
# with no space, so these get a separate, looser front boundary below; the
# lookahead also allows a following element letter (e.g. "SO4" continuing
# straight on from "(NH4)2SO4"), not just end-of-token.
GROUP_FORMULAS = ["(NO3)2", "(OH)2", "(OH)3", "(SO4)3", "(NH4)2", "(NH3)2",
                   "(NH4)2SO4", "Al2(SO4)3"]

WHITELIST = {f: f.translate(SUB) for f in FORMULAS}
WHITELIST.update(IONS)
GROUP_WHITELIST = {g: g.translate(SUB) for g in GROUP_FORMULAS}
# longest first so e.g. H2A+ / NADP+ / H2SO4 win over shorter substrings
_ORDER = sorted(WHITELIST, key=len, reverse=True)
_WL_RE = re.compile(r"(?<![A-Za-z])(" + "|".join(re.escape(k) for k in _ORDER) + r")(?![A-Za-z0-9])")
_GROUP_ORDER = sorted(GROUP_WHITELIST, key=len, reverse=True)
_GROUP_RE = re.compile("(" + "|".join(re.escape(k) for k in _GROUP_ORDER) + r")(?![0-9])")

_CARET_RE = re.compile(r"\^([+-]?\d+)")
_X10_RE = re.compile(r"(?<=[\d.])\s*x\s*(?=\d)")
_ARROW_RE = [(re.compile(r"<->|<=>"), "⇌"), (re.compile(r"-+>"), "→")]
_SQRT_RE = re.compile(r"\bsqrt\(")
_DELTA_H_RE = re.compile(r"\bdelta H\b")
_CHARGE_CLEANUP_RE = re.compile(r"([⁰¹²³⁴⁵⁶⁷⁸⁹])([+-])(?![A-Za-z0-9])")
# "*pi*" (asterisk-flanked) is always the constant in a formula like
# "2*pi*sqrt(L/g)" -- run this BEFORE the general asterisk-multiply rule so
# it consumes its own flanking asterisks and isn't left as a bare "pi" that
# rule could re-flag; a bare word "pi" elsewhere (e.g. "a pi bond") is
# deliberately left as English prose, not forced to the Greek letter.
_PI_STAR_RE = re.compile(r"\*pi\*")
_LAMBDA_RE = re.compile(r"\blambda\b")
# asterisk used as a multiply sign between two alphanumerics (f*lambda,
# q1*q2, g*t^2, mu0*I) -- markdown emphasis (*word*, **word**) never has an
# alphanumeric on BOTH sides of the same asterisk, so this can't collide.
_STAR_MUL_RE = re.compile(r"(?<=[A-Za-z0-9)])\*(?=[A-Za-z0-9(])")
# standalone "A-" (conjugate-base anion, mock13 q6064) -- MUST be boundary-
# checked, not a naive substring replace: bare "A-" also occurs constantly as
# a dash in "A-T"/"A-U" DNA base-pairing notation and "DNA-protein" compound
# words, which this correctly leaves alone (the boundary requires nothing
# alphanumeric on either side of the token).
_A_ANION_RE = re.compile(r"(?<![A-Za-z0-9])A-(?![A-Za-z0-9])")


def fix(s):
    if not s:
        return s
    s = _CARET_RE.sub(lambda m: m.group(1).translate(SUP), s)
    s = _X10_RE.sub(" × ", s)
    for rx, repl in _ARROW_RE:
        s = rx.sub(repl, s)
    s = _DELTA_H_RE.sub("ΔH", s)
    # order matters: consume "*pi*" before the general star-multiply rule (it
    # must see its own flanking asterisks first), and both must run while
    # "sqrt(" / "lambda" are still plain ASCII -- once sqrt( becomes "√(" or
    # lambda becomes "λ", neither is in the star-multiply's [A-Za-z0-9(]
    # boundary class any more and an adjacent "*" would be missed.
    s = _PI_STAR_RE.sub("π", s)
    s = _STAR_MUL_RE.sub(" × ", s)
    s = _SQRT_RE.sub("√(", s)
    s = _LAMBDA_RE.sub("λ", s)
    s = _GROUP_RE.sub(lambda m: GROUP_WHITELIST[m.group(1)], s)
    s = _WL_RE.sub(lambda m: WHITELIST[m.group(1)], s)
    s = _CHARGE_CLEANUP_RE.sub(lambda m: m.group(1) + m.group(2).translate(SUP), s)
    s = _A_ANION_RE.sub("A⁻", s)
    return s


# ---- one-off full-field rewrites for the two questions using spelled-out
# Greek letters ("pi", "lambda") in their options -- too ambiguous as bare
# words to whitelist globally (both are common English words/prose too), so
# these exact option strings are replaced outright instead of run through
# fix(). Their explanation fields already use proper Unicode (checked).
# Keyed by the ORIGINAL (pre-fix) field value, not by row id -- every key
# here was verified to occur exactly once, in exactly this one field, across
# all 20 mocks' full content (question+options+explanations), so this dict
# is safe to apply as a global lookup and needs no database-specific id and
# runs unchanged against any DB (local already-fixed, or production
# not-yet-fixed: on the former these old strings simply no longer exist, so
# the lookup is a harmless no-op there).
FULL_OVERRIDE_BY_OLD = {
    "T = 2 pi sqrt(L/g)": "T = 2π√(L/g)",       # mock14 q6278: pendulum period, "pi" as the constant
    "T = 2 pi sqrt(g/L)": "T = 2π√(g/L)",
    "T = 2 pi L g": "T = 2π L g",
    "T = 1 / (2 pi sqrt(L g))": "T = 1 / (2π√(L g))",
    "v = f / lambda": "v = f / λ",              # mock5 q4658: wave speed, "lambda" as wavelength
    "v = f + lambda": "v = f + λ",
    "v = lambda / f^2": "v = λ / f²",
    "v = f x lambda": "v = f × λ",
}

# ---- one-off text patches applied AFTER fix() to every field of every
# question -- for notation too ambiguous as a bare token to whitelist
# globally (a lone "A-", a lowercase "delta+"/"delta-" partial-charge pair
# distinct from the capital-Delta "delta H" phrase already handled globally,
# an inline oxidation-state "Ag0") but unambiguous as these exact substrings,
# each independently verified to occur nowhere else in the full mock corpus.
# Same portability note as FULL_OVERRIDE_BY_OLD above: a flat global list,
# not gated by row id, so it runs unchanged against any DB.
PATCHES = [
    ("(delta-)", "(δ⁻)"), ("(delta+)", "(δ⁺)"),
    ("delta+", "δ⁺"), ("delta-", "δ⁻"),  # mock10 q5538: partial charge
    ("Ag⁺ to Ag0)", "Ag⁺ to Ag⁰)"),  # mock12 q5880: oxidation-state notation (runs after fix(), so Ag+ is already Ag⁺ by this point)
    ("mu0 × I", "μ₀ × I"),  # mock18 q8101: magnetic field formula B = mu0*I/(2*pi*r)
    ("q₁ x q₂", "q₁ × q₂"),  # mock18 q8096: Coulomb's law, letter-x multiply (fix() only converts digit-adjacent "x")
]
# (Gm1/Gm2/Gm1m2/m1/m2/q1/q2/kq1q2 -- the recurring gravitation- and
# Coulomb's-law-formula variables -- are handled globally via the FORMULAS
# whitelist above, not a per-question patch, since the same "F = Gm1m2/r^2"
# / "kq1q2/r^2" templates recur verbatim across many mocks.)


def apply_patches(text):
    for old, new in PATCHES:
        text = text.replace(old, new)
    return text


FIELDS = ["question_text", "option_a", "option_b", "option_c", "option_d",
          "explanation_short", "explanation_long", "explanation_trick"]


def run(mock_ids, apply_changes):
    mocks = MockTest.objects.filter(exam__name__icontains="MDCAT").order_by("id")
    if mock_ids:
        mocks = mocks.filter(id__in=mock_ids)
    planned = []
    for m in mocks:
        for q in m.questions.all():
            diff = {}
            for f in FIELDS:
                old = getattr(q, f)
                new = FULL_OVERRIDE_BY_OLD[old] if old in FULL_OVERRIDE_BY_OLD else apply_patches(fix(old))
                if new != old:
                    diff[f] = (old, new)
            eo = q.explanation_options or {}
            new_eo = dict(eo)
            eo_changed = False
            for k, v in eo.items():
                nv = FULL_OVERRIDE_BY_OLD[v] if v in FULL_OVERRIDE_BY_OLD else apply_patches(fix(v))
                if nv != v:
                    new_eo[k] = nv
                    eo_changed = True
            if eo_changed:
                diff["explanation_options"] = (eo, new_eo)
            if diff:
                planned.append((m.id, q, diff))

    print(f"questions to change: {len(planned)}")
    print(f"fields to change: {sum(len(d) for _, _, d in planned)}")
    for mid, q, diff in planned:
        print(f"\nmock{mid} q{q.id}")
        for f, (old, new) in diff.items():
            if f == "explanation_options":
                for k in old:
                    if old[k] != new[k]:
                        print(f"  eo.{k}\n    - {old[k]!r}\n    + {new[k]!r}")
            else:
                print(f"  {f}\n    - {old!r}\n    + {new!r}")
    if len(planned) > 40:
        print(f"\n... and {len(planned) - 40} more questions (not printed)")

    if not apply_changes:
        print("\nDRY RUN - nothing written. Re-run with --apply to save.")
        return

    from django.db import transaction
    with transaction.atomic():
        for _, q, diff in planned:
            for f, (old, new) in diff.items():
                setattr(q, f, new)
            q.save(update_fields=list(diff))
    print(f"\nAPPLIED to {len(planned)} questions.")


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    ids = [int(a) for a in args] if args else None
    run(ids, "--apply" in sys.argv)
