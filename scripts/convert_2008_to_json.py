"""
Adapter: mdcat_2008.py -> parsed-mcqs/MDCAT_2008.json

Unlike 2009/2010 (same compiled "MDCAT Past Papers 2008-2016 Solved" PDF,
mdcat-content/tmp_2010/mdcat_2008_2016_solved.pdf), that compiled PDF's
own 2008 section (page indices 0-16) has NO answer-key page at all -- it
jumps straight from the 16-page 2008 question paper to the 2009 cover
page. mdcat_2008.py's own header comment ("No answer key included") is
accurate for that source.

The answer key used here instead comes from a different aggregator's
compiled multi-year PDF (topstudyworld.com's "UHS PAST PAPERS ... FROM
2008 TO 2017" bundle, mdcat-content/tmp_2008/topstudyworld_bundle.pdf,
217 pages) whose 2008 section is pages 1-16 (question paper, same
content/pagination as the other compiled PDF -- same original scan) plus
page 17: a genuine "UNIVERSITY OF HEALTH SCIENCES, LAHORE / Entrance Test
2008 / ANSWER KEY" table, extracted via pymupdf's real text layer (not
OCR). KEY_RAW below is that 220-entry table verbatim; Q95 and Q195 are
genuinely "X" (unresolved) in the source PDF's own key.

Verification method: mdcat_2008.py's QUESTIONS claims to be a "clean text
extraction" from the *other* compiled PDF's 2008 section. Rather than
trust that claim blindly (per this project's standing policy after the
2012/2009 B/C-swap discoveries), this session independently re-extracted
the full text of all 16 question pages from topstudyworld_bundle.pdf
(mdcat-content/tmp_2008/full_text.txt), parsed it into 220 stem+option
blocks (tmp_2008/parsed_raw.json) via regex on the "Q.N" / "A)".."D)"
markers, and diffed every field against mdcat_2008.py's QUESTIONS by
normalized string similarity (tmp_2008/diff.py, tmp_2008/diff_report.txt).
Result: 0 genuine content discrepancies across all 220 questions -- the
13 questions initially flagged were all an artifact of this session's own
page-concatenation in full_text.txt (the "=== PDF_PAGE_N ===" marker
bleeding into the last option's text), not real defects in mdcat_2008.py.
This is a stronger check than the highlight-color spot-checks used for
2009/2010 (no per-question highlighting exists in either compiled PDF's
2008 section), and confirms mdcat_2008.py's transcription is faithful:
no B/C swap, no truncation, no OCR garbling found anywhere in this paper.

Two genuine defects found, both originating in the source PDF itself
(confirmed by rendering tmp_2008/page_10_hires.png and page_16_hires.png
at 350dpi -- not extraction artifacts):

1. Q125-130 (SPOT THE ERROR cluster): underlined segments are invisible
   to any plain-text extraction, so mdcat_2008.py (like every prior
   year's equivalent cluster) has empty options for these 6 questions.
   Transcribed directly from the page_10_hires.png render; see
   OPTION_FIXES below.

2. Q220 is a verbatim duplicate of Q184 (identical stem "Name the human
   tissues that contain about 85% water", identical four options) -- an
   original print-run defect in the exam paper itself (confirmed on
   page_16_hires.png, immediately above the compiler's copyright
   footer), not a scan/OCR artifact. Both share the same key answer (C,
   "Brain cells."), so there's no conflicting-answer problem -- just a
   duplicated question left in the paper. Per this project's
   transcribe-faithfully policy (same policy applied to 2010's Q55/Q103
   printing defects), both are kept active as-is; this is documented
   here rather than silently "fixed".

No diagram/figure/graph-required questions exist in this paper: a
keyword scan (figure/diagram/graph/curve/shown below/shown in/structure
of/cross-section/labelled/etc.) across parsed_raw.json found 0 genuine
hits (one "image size to object size" substring in Q48's own text, a
false positive). mdcat_2008.py's own `diagram_text` field on 28
questions is spurious noise from whatever process first built the file
-- spot-checked against the real page renders and confirmed those
questions are pure text (e.g. Q1, Q2, Q64, Q95, Q151 have no diagram of
any kind); the field is ignored entirely by this converter.

Topic/subtopic tags were assigned by hand against the live DB vocabulary
(mdcat-content/tmp_2008/db_topics.txt, queried before writing this file)
reusing existing names wherever the concept matched. ~26 new subtopics
were added under existing topics where nothing fit -- mostly Biology
(plant hormones/tissues/movements, gene mapping, aquatic zonation,
Phylum Mollusca) and a handful of Physics/Chemistry gaps (Kirchhoff's
Rules, Graham's Law of Effusion, s/p-block Group VI and VII Reactions,
which were altogether missing from the DB vocabulary despite Groups I,
II, IV, V existing) -- created directly against the DB via
import_mcqs.py's get_or_create, same pattern as every prior year.
mdcat-content/syllabus/pmdc_mdcat_syllabus.json is deliberately NOT
touched.
"""
import json
import importlib.util
from pathlib import Path

SOURCE_FILE = Path("mdcat-content/mdcat_2008.py")
OUTPUT_FILE = Path("mdcat-content/parsed-mcqs/MDCAT_2008.json")
PAPER_YEAR = 2008

spec = importlib.util.spec_from_file_location("mdcat_2008", SOURCE_FILE)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

QUESTIONS = mod.QUESTIONS  # list of {'number','subject','question','options':{'A'..'D'},'diagram_text'}

# --- answer key, extracted verbatim from topstudyworld_bundle.pdf page index 17's text layer ---
KEY_RAW = """
ID:D 1:C 2:B 3:C 4:C 5:C 6:B 7:D 8:C 9:D 10:C
11:C 12:D 13:C 14:D 15:A 16:A 17:C 18:B 19:B 20:C
21:A 22:A 23:D 24:A 25:D 26:D 27:D 28:B 29:D 30:A
31:C 32:B 33:A 34:C 35:B 36:C 37:C 38:D 39:D 40:D
41:D 42:D 43:A 44:C 45:D 46:C 47:B 48:C 49:D 50:C
51:D 52:B 53:B 54:B 55:C 56:B 57:A 58:A 59:B 60:B
61:C 62:A 63:A 64:A 65:D 66:C 67:A 68:A 69:A 70:A
71:B 72:C 73:D 74:A 75:B 76:C 77:C 78:C 79:B 80:B
81:C 82:C 83:A 84:C 85:A 86:B 87:C 88:A 89:C 90:B
91:A 92:C 93:A 94:C 95:X 96:A 97:C 98:B 99:B 100:A
101:A 102:B 103:C 104:D 105:D 106:B 107:C 108:B 109:C 110:C
111:C 112:C 113:D 114:C 115:B 116:D 117:D 118:D 119:D 120:B
121:A 122:D 123:A 124:A 125:D 126:C 127:C 128:B 129:D 130:D
131:D 132:D 133:D 134:A 135:A 136:B 137:D 138:B 139:A 140:C
141:A 142:B 143:D 144:B 145:A 146:D 147:C 148:A 149:B 150:C
151:B 152:B 153:B 154:B 155:B 156:B 157:B 158:C 159:D 160:B
161:C 162:B 163:B 164:B 165:B 166:C 167:B 168:D 169:D 170:B
171:D 172:B 173:C 174:A 175:D 176:D 177:B 178:C 179:A 180:C
181:D 182:B 183:D 184:C 185:C 186:B 187:A 188:C 189:B 190:D
191:A 192:A 193:A 194:A 195:X 196:B 197:D 198:B 199:D 200:B
201:D 202:B 203:D 204:B 205:C 206:B 207:A 208:A 209:B 210:A
211:C 212:B 213:B 214:D 215:C 216:D 217:B 218:A 219:D 220:C
"""


def parse_key(raw: str) -> dict:
    key = {}
    for tok in raw.split():
        qnum_str, letter = tok.split(":")
        if qnum_str == "ID":
            continue
        letter = letter.strip().lower()
        key[int(qnum_str)] = letter if letter in {"a", "b", "c", "d"} else None
    return key


ANSWER_KEY = parse_key(KEY_RAW)
assert len(ANSWER_KEY) == 220, f"expected 220 key entries, got {len(ANSWER_KEY)}"

# qnum -> {'A':..,'B':..,'C':..,'D':..} full or partial override
OPTION_FIXES = {
    # Q125-130: SPOT THE ERROR cluster. Underlines are invisible to plain
    # text extraction, so the raw source had empty options; transcribed
    # directly from tmp_2008/page_10_hires.png (350dpi render).
    125: {"A": "did not", "B": "how closely", "C": "had kept in", "D": "with across"},
    126: {"A": "that if", "B": "germs were", "C": "excluded of wounds", "D": "inflammation was"},
    127: {"A": "his hair flutter", "B": "body drew", "C": "were standing", "D": "of a vacuum"},
    128: {"A": "came to the hurdles", "B": "that he remember", "C": "over which once", "D": "so easy"},
    129: {"A": "is meant", "B": "and death-rate", "C": "how do", "D": "effect the population"},
    130: {"A": "had left", "B": "calmness and a poise", "C": "that accord", "D": "own inward"},
}

# Q95 and Q195's official key entries are genuinely "X" (unresolved) in
# the source -- not an extraction failure on our part.
UNRESOLVED_KEY_NOTE = {
    95: "Answer key entry for Q95 unresolved in the official UHS-compiled source (printed as 'X') -- the compiled key itself never resolved this one.",
    195: "Answer key entry for Q195 unresolved in the official UHS-compiled source (printed as 'X') -- the compiled key itself never resolved this one.",
}

# No diagram/figure-required questions found in this paper (see docstring).
VISUAL_REQUIRED = set()

# qnum -> (topic, subtopic)
TAGS = {
    # --- Physics 1-60 ---
    1: ("Nuclear Physics", "Composition of Atomic Nuclei"),
    2: ("Nuclear Physics", "Spontaneous and Random Nuclear Decay"),
    3: ("Electromagnetism", "Magnetic Flux Density"),
    4: ("Atomic Structure", "Discovery of Electron (Cathode Rays)"),
    5: ("Rotational and Circular Motion", "Simple Harmonic Motion (SHM)"),
    6: ("Waves", "Interference (Newton's Rings, Thin Films)"),
    7: ("Nuclear Physics", "Composition of Atomic Nuclei"),
    8: ("Electrostatics", "Capacitance"),
    9: ("Electromagnetic Induction", "Lenz's Law"),
    10: ("Electronics", "Logic Gates"),
    11: ("Atomic Spectra", "Atomic Spectra / Line Spectrum"),
    12: ("Nuclear Physics", "Composition of Atomic Nuclei"),
    13: ("Force and Motion", "Uniform and Variable Acceleration"),
    14: ("Rotational and Circular Motion", "Circular Motion"),
    15: ("Rotational and Circular Motion", "Moment of Inertia"),
    16: ("Alternating Current", "Resonance (RLC Circuits)"),
    17: ("Waves", "Stationary Waves"),
    18: ("Optics", "Optical Fibers and Total Internal Reflection"),
    19: ("Current Electricity", "Kirchhoff's Rules"),
    20: ("Electronics", "PN Junction (Forward and Reverse Bias)"),
    21: ("Dawn of Modern Physics", "Pair Production"),
    22: ("Nuclear Physics", "Composition of Atomic Nuclei"),
    23: ("Force and Motion", "Projectile Motion"),
    24: ("Rotational and Circular Motion", "Moment of Inertia"),
    25: ("Rotational and Circular Motion", "Simple Harmonic Motion (SHM)"),
    26: ("Waves", "Beats"),
    27: ("Optics", "Optical Fibers and Total Internal Reflection"),
    28: ("Current Electricity", "Resistor Color Code"),
    29: ("Electronics", "PN Junction (Forward and Reverse Bias)"),
    30: ("Dawn of Modern Physics", "Quantum Theory and Radiation (Photons)"),
    31: ("Nuclear Physics", "Biological and Medical Uses of Radiation"),
    32: ("Electromagnetic Induction", "Transformer"),
    33: ("Measurements", "Dimensional Analysis"),
    34: ("Work and Energy", "Power"),
    35: ("Rotational and Circular Motion", "Simple Harmonic Motion (SHM)"),
    36: ("Waves", "Factors Affecting Speed of Sound"),
    37: ("Optics", "Lenses and Optical Instruments"),
    38: ("Waves", "Organ Pipes"),
    39: ("Current Electricity", "Resistivity and Temperature Coefficient"),
    40: ("Atomic Structure", "Quantum Numbers"),
    41: ("Dawn of Modern Physics", "Black Body Radiation (Wien's Law)"),
    42: ("Dawn of Modern Physics", "Quantum Theory and Radiation (Photons)"),
    43: ("Work and Energy", "Energy Losses and Efficiency"),
    44: ("Measurements", "Dimensional Analysis"),
    45: ("Work and Energy", "Kinetic Energy and Work-Energy Theorem"),
    46: ("Fluid Dynamics", "Equation of Continuity"),
    47: ("Waves", "Transverse vs Longitudinal Waves"),
    48: ("Optics", "Magnification and Image Formation"),
    49: ("Current Electricity", "Resistivity and Temperature Coefficient"),
    50: ("Electronics", "Semiconductors (p-type, n-type)"),
    51: ("Dawn of Modern Physics", "Special Theory of Relativity"),
    52: ("Nuclear Physics", "Half-life and Rate of Decay"),
    53: ("Alternating Current", "AC Through Inductor"),
    54: ("Work and Energy", "Work"),
    55: ("Force and Motion", "Gravitation and Escape Velocity"),
    56: ("Fluid Dynamics", "Fluid Drag"),
    57: ("Measurements", "Dimensional Analysis"),
    58: ("Waves", "Young's Double Slit Experiment"),
    59: ("Current Electricity", "Electric Power and Heating Effect"),
    60: ("Solids", "Metallic Bonding and Conduction"),

    # --- Chemistry 61-120 ---
    61: ("Chemical Bonding", "Ionic Character of Covalent Bond"),
    62: ("Electrochemistry", "Redox Reactions"),
    63: ("Aldehydes and Ketones", "Preparation"),
    64: ("Alcohols and Phenols", "Chemistry of Alcohols (Ethers, Esters)"),
    65: ("Biological Molecules", "Structure of DNA"),
    66: ("Fundamental Concepts of Chemistry", "Chromatography Techniques"),
    67: ("Gases", "Graham's Law of Effusion"),
    68: ("Chemical Bonding", "Dipole Moment"),
    69: ("Chemical Equilibrium", "Haber's Process"),
    70: ("s and p Block Elements", "Group I Reactions"),
    71: ("s and p Block Elements", "Group IV Reactions"),
    72: ("Industrial Chemistry", "Types and Composition of Steel"),
    73: ("s and p Block Elements", "Group VII Reactions (Halogens)"),
    74: ("Alcohols and Phenols", "Nomenclature, Structure, Reactivity of Alcohols"),
    75: ("Biological Molecules", "Lipids"),
    76: ("Fundamental Concepts of Chemistry", "Purification Techniques (Sublimation, Crystallization)"),
    77: ("Liquids", "Intermolecular Forces (Van der Waals)"),
    78: ("Thermochemistry and Energetics", "Exothermic and Endothermic Reactions"),
    79: ("Liquids", "Miscibility and Solubility of Liquids"),
    80: ("Chemical Bonding", "Ionic Character of Covalent Bond"),
    81: ("s and p Block Elements", "s, p, d, f Block Demarcation"),
    82: ("s and p Block Elements", "Group IV Reactions"),
    83: ("Industrial Chemistry", "Contact Process (H2SO4 Manufacture)"),
    84: ("Chemistry of Hydrocarbons", "Nomenclature of Alkanes"),
    85: ("Aldehydes and Ketones", "Preparation"),
    86: ("Fundamental Concepts of Chemistry", "Limiting and Excess Reactants"),
    87: ("Gases", "Real and Ideal Gases"),
    88: ("Chemical Bonding", "Hybridization"),
    89: ("Liquids", "Colligative Properties of Solutions"),
    90: ("s and p Block Elements", "Group II Reactions"),
    91: ("s and p Block Elements", "Group VI Reactions (Oxygen/Sulphur Family)"),
    92: ("Transition Elements", "Electronic Structure of d-block"),
    93: ("Industrial Chemistry", "Metallurgy and Extraction of Metals"),
    94: ("Chemical Bonding", "Bond Energy"),
    95: ("s and p Block Elements", "Group I Reactions"),
    96: ("s and p Block Elements", "Group IV Reactions"),
    97: ("s and p Block Elements", "Group II Reactions"),
    98: ("s and p Block Elements", "Group VII Reactions (Halogens)"),
    99: ("Alcohols and Phenols", "Nomenclature, Structure, Reactivity of Phenols"),
    100: ("Liquids", "Evaporation, Boiling Point, Vapor Pressure"),
    101: ("Fundamental Concepts of Chemistry", "Chromatography Techniques"),
    102: ("Thermochemistry and Energetics", "Enthalpy of Reaction"),
    103: ("Liquids", "Hydrogen Bonding"),
    104: ("Liquids", "Hydrogen Bonding"),
    105: ("Industrial Chemistry", "Fertilizers and Plant Nutrients"),
    106: ("s and p Block Elements", "Group IV Reactions"),
    107: ("Chemistry of Hydrocarbons", "Nomenclature of Alkenes"),
    108: ("Chemistry of Hydrocarbons", "Octane Number and Cracking"),
    109: ("Carboxylic Acids", "Nomenclature, Structure, Preparation"),
    110: ("Atomic Structure", "Electronic Configuration"),
    111: ("Fundamental Concepts of Chemistry", "Purification Techniques (Sublimation, Crystallization)"),
    112: ("Gases", "Ideal Gas Equation"),
    113: ("Solids", "Ionic vs Molecular Crystals"),
    114: ("Chemical Equilibrium", "Ka, pKa and Acid Strength"),
    115: ("Atomic Structure", "Ionization Energy of Hydrogen (Bohr Model)"),
    116: ("s and p Block Elements", "Group IV Reactions"),
    117: ("s and p Block Elements", "Group V Reactions"),
    118: ("s and p Block Elements", "Group VI Reactions (Oxygen/Sulphur Family)"),
    119: ("Fundamental Principles of Organic Chemistry", "Isomerism (Stereoisomerism)"),
    120: ("Industrial Chemistry", "Polymers (Condensation and Addition)"),

    # --- English 121-150 ---
    121: ("Formal and Lexical Aspect of Language", "Contextual Vocabulary"),
    122: ("Formal and Lexical Aspect of Language", "Contextual Vocabulary"),
    123: ("Formal and Lexical Aspect of Language", "Contextual Vocabulary"),
    124: ("Formal and Lexical Aspect of Language", "Contextual Vocabulary"),
    125: ("Writing Skills", "Errors of Function and Spelling"),
    126: ("Writing Skills", "Errors of Function and Spelling"),
    127: ("Writing Skills", "Errors of Function and Spelling"),
    128: ("Writing Skills", "Errors of Function and Spelling"),
    129: ("Writing Skills", "Errors of Function and Spelling"),
    130: ("Writing Skills", "Errors of Function and Spelling"),
    131: ("Writing Skills", "Faulty Sentence Structure"),
    132: ("Writing Skills", "Faulty Sentence Structure"),
    133: ("Writing Skills", "Faulty Sentence Structure"),
    134: ("Writing Skills", "Faulty Sentence Structure"),
    135: ("Writing Skills", "Faulty Sentence Structure"),
    136: ("Writing Skills", "Faulty Sentence Structure"),
    137: ("Writing Skills", "Faulty Sentence Structure"),
    138: ("Writing Skills", "Faulty Sentence Structure"),
    139: ("Writing Skills", "Faulty Sentence Structure"),
    140: ("Writing Skills", "Faulty Sentence Structure"),
    141: ("Formal and Lexical Aspect of Language", "Synonyms (Irony, Parody, Satire)"),
    142: ("Formal and Lexical Aspect of Language", "Synonyms (Irony, Parody, Satire)"),
    143: ("Formal and Lexical Aspect of Language", "Synonyms (Irony, Parody, Satire)"),
    144: ("Formal and Lexical Aspect of Language", "Synonyms (Irony, Parody, Satire)"),
    145: ("Formal and Lexical Aspect of Language", "Synonyms (Irony, Parody, Satire)"),
    146: ("Formal and Lexical Aspect of Language", "Synonyms (Irony, Parody, Satire)"),
    147: ("Formal and Lexical Aspect of Language", "Synonyms (Irony, Parody, Satire)"),
    148: ("Formal and Lexical Aspect of Language", "Synonyms (Irony, Parody, Satire)"),
    149: ("Formal and Lexical Aspect of Language", "Synonyms (Irony, Parody, Satire)"),
    150: ("Formal and Lexical Aspect of Language", "Synonyms (Irony, Parody, Satire)"),

    # --- Biology 151-220 ---
    151: ("Coordination and Control", "Receptors"),
    152: ("Coordination and Control", "Nerve Impulse and Reflexes"),
    153: ("Support and Movement", "Joints"),
    154: ("Homeostasis", "Liver Functions"),
    155: ("Biological Molecules", "Structure of DNA"),
    156: ("Bioenergetics", "Respiration"),
    157: ("Diversity of Life", "Classes of Fish (Agnatha, Chondrichthyes, Osteichthyes)"),
    158: ("Bioenergetics", "Respiration"),
    159: ("Respiration", "Respiratory Organs in Different Organisms"),
    160: ("Homeostasis", "Thermoregulation"),
    161: ("Reproduction", "Sexually Transmitted Diseases"),
    162: ("Inheritance", "Sex Determination"),
    163: ("Respiration", "Gas Exchange in Lungs"),
    164: ("Cell Structure and Function", "Cytoplasmic Organelles"),
    165: ("Acellular Life", "Viruses"),
    166: ("Diversity of Life", "Kingdom Fungi"),
    167: ("Diversity of Life", "Classes of Fish (Agnatha, Chondrichthyes, Osteichthyes)"),
    168: ("Respiration", "Human Respiratory System"),
    169: ("Kingdom Plantae", "Plant Tissues (Parenchyma, Collenchyma, Sclerenchyma)"),
    170: ("Kingdom Plantae", "Plant Hormones (Auxins, Gibberellins, etc.)"),
    171: ("Kingdom Plantae", "Plant Hormones (Auxins, Gibberellins, etc.)"),
    172: ("Inheritance", "Gene Location and Mapping"),
    173: ("Kingdom Plantae", "Water Movement in Plants (Guttation, Transpiration)"),
    174: ("Cell Structure and Function", "Cytoplasmic Organelles"),
    175: ("Diversity of Life", "Kingdom Prokaryotae (Bacteria)"),
    176: ("Biotechnology", "Biotechnology and Health Care"),
    177: ("Diversity of Life", "Phylum Chordata (Class Mammalia)"),
    178: ("Biological Molecules", "Biological Importance of Water"),
    179: ("Kingdom Plantae", "Plant Movements (Tropic and Nastic)"),
    180: ("Coordination and Control", "Brain"),
    181: ("Inheritance", "Chromosome Number in Organisms"),
    182: ("Biotechnology", "Plant Tissue Culture"),
    183: ("Cell Structure and Function", "Cytoplasmic Organelles"),
    184: ("Biological Molecules", "Biological Importance of Water"),
    185: ("Cell Structure and Function", "Cytoplasmic Organelles"),
    186: ("Cell Structure and Function", "Prokaryotic and Eukaryotic Cell"),
    187: ("Kingdom Plantae", "Classification of Plant Kingdom (Bryophyta, Pteridophyta)"),
    188: ("Photosynthesis", "Pigments and Light Absorption"),
    189: ("Homeostasis", "Osmoregulation"),
    190: ("Support and Movement", "Human Skeleton (Cartilage, Muscle, Bone)"),
    191: ("Coordination and Control", "Brain"),
    192: ("Cell Division", "Mitosis"),
    193: ("Evolution", "Concept of Evolution"),
    194: ("Biological Molecules", "Carbohydrates"),
    195: ("Acellular Life", "Viruses"),
    196: ("Diversity of Life", "Kingdom Prokaryotae (Bacteria)"),
    197: ("Kingdom Plantae", "Classification of Plant Kingdom (Bryophyta, Pteridophyta)"),
    198: ("Bioenergetics", "Respiration"),
    199: ("Homeostasis", "Excretion (Nitrogenous Compounds)"),
    200: ("Support and Movement", "Arthritis"),
    201: ("Coordination and Control", "Endocrine System and Hormones"),
    202: ("Inheritance", "Gene Location and Mapping"),
    203: ("Ecology", "Biotic and Abiotic Components"),
    204: ("Biological Molecules", "Structure of DNA"),
    205: ("Diversity of Life", "Phylum Arthropoda"),
    206: ("Diversity of Life", "Kingdom Protista"),
    207: ("Kingdom Plantae", "Angiosperms vs Gymnosperms"),
    208: ("Ecology", "Food Chain and Food Web"),
    209: ("Homeostasis", "Excretion (Nitrogenous Compounds)"),
    210: ("Coordination and Control", "Endocrine System and Hormones"),
    211: ("Kingdom Plantae", "Photoperiodism and Phytochrome"),
    212: ("Inheritance", "Polygenic inheritance"),
    213: ("Ecology", "Aquatic Zonation (Littoral, Profundal)"),
    214: ("Enzymes", "Factors Affecting Enzyme Action"),
    215: ("Diversity of Life", "Phylum Mollusca"),
    216: ("Diversity of Life", "Kingdom Protista"),
    217: ("Diversity of Life", "Body Cavities (Coelom Classification)"),
    218: ("Digestion", "Eating Disorders"),
    219: ("Homeostasis", "Excretion (Nitrogenous Compounds)"),
    220: ("Biological Molecules", "Biological Importance of Water"),
}

assert len(TAGS) == 220, f"expected 220 tag entries, got {len(TAGS)}"

out = []
stats = {"total": 0, "active": 0, "needs_review": 0, "inactive_unresolved_key": 0, "visual_required": 0}

for q in sorted(QUESTIONS, key=lambda x: x["number"]):
    qnum = q["number"]
    opts = dict(q["options"])
    if qnum in OPTION_FIXES:
        opts.update(OPTION_FIXES[qnum])
    if set(opts.keys()) != {"A", "B", "C", "D"}:
        print(f"WARN Q{qnum}: options keys {sorted(opts.keys())} != A-D -- skipping")
        continue

    text = q["question"]
    subject = q["subject"]
    topic, subtopic = TAGS[qnum]
    answer = ANSWER_KEY[qnum]

    is_active = True
    needs_review = False
    notes = None

    if answer is None:
        is_active = False
        needs_review = True
        notes = UNRESOLVED_KEY_NOTE.get(qnum, f"Answer key entry for Q{qnum} unresolved in source ('X') -- verify against original key image")
        stats["inactive_unresolved_key"] += 1

    if qnum == 220:
        notes = "Verbatim duplicate of Q184 in the original source PDF (confirmed via 350dpi page render) -- a genuine print-run defect in the exam paper itself, not an extraction error. Both share the same correct answer (C)."

    is_visual = qnum in VISUAL_REQUIRED
    if is_visual:
        needs_review = True
        notes = notes or "Diagram-only question -- needs image attached."
        stats["visual_required"] += 1

    if needs_review:
        stats["needs_review"] += 1
    if is_active:
        stats["active"] += 1

    out.append({
        "id": f"mdcat-{PAPER_YEAR}-q{qnum}",
        "paper_year": PAPER_YEAR,
        "question_number": qnum,
        "subject": subject,
        "topic": topic,
        "subtopic": subtopic,
        "difficulty": None,
        "question_text": text,
        "options": {"a": opts["A"], "b": opts["B"], "c": opts["C"], "d": opts["D"]},
        "correct_answer": answer,
        "explanation": None,
        "is_active": is_active,
        "needs_review": needs_review,
        "notes": notes,
        "is_visual_required": is_visual,
        "source_file": SOURCE_FILE.name,
        "tag_confidence": "medium",
    })
    stats["total"] += 1

OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(out, f, indent=2, ensure_ascii=False)

print(f"\nWrote {len(out)} MCQs to {OUTPUT_FILE}")
print(f"  active: {stats['active']}")
print(f"  needs_review: {stats['needs_review']}")
print(f"  inactive (unresolved key): {stats['inactive_unresolved_key']}")
print(f"  visual_required: {stats['visual_required']}")
