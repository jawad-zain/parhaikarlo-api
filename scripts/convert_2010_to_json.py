"""
Adapter: mdcat_2010.py -> parsed-mcqs/MDCAT_2010.json

Unlike 2012-2019/2022 adapters, mdcat_2010.py has NO built-in answer key
(source docstring: "No answer key included") despite being sourced from a
PDF titled "MDCAT Past Papers (2008-2016) Solved" — the answer key exists
in that PDF (page index 54, a single table for all 220 questions) but the
extraction script that produced mdcat_2010.py only captured the question
pages, not the key page. The key below was extracted programmatically from
mdcat-content/tmp_2010/mdcat_2008_2016_solved.pdf page 54's text layer (a
real embedded text layer, not OCR) and cross-verified against the same
PDF's inline orange answer-highlighting on the question pages themselves
(both sources agree on every question checked).

Unlike 2011, this PDF has a genuine text layer (pymupdf extracts real
text, not a scan), so most of mdcat_2010.py's question/option text is
already clean. OPTION_FIXES below corrects a handful of real extraction
defects found by rendering specific pages and comparing to the PDF's
vector content:
  - Q7: trailing response-form-grid artifact ("A B C D ID 1 2 3 4") that
    bled into option D's text from the page-1 ID bubble legend.
  - Q21, Q28, Q36, Q54, Q57, Q59, Q103: real two-line fraction constructs
    (numerator/denominator stacked vertically in the PDF) that the linear
    text extraction flattened without the "/" — found systematically by
    scanning page vector-drawing "rects" for thin fraction-bar lines
    (page.get_drawings(), rect.height < 2) and mapping each to its
    question via y-position. Confirmed by rendering each hit at 300dpi.
  - Q124, Q140: trailing section-instruction boilerplate concatenated
    onto the last option (same root cause as Q7, different instruction
    block).
  - Q125-130 ("SPOT THE ERROR" cluster): source had unusable placeholder
    options ("Underlined segment A in the original sentence") — replaced
    with the real underlined phrases transcribed from page_46_hires.png
    at 400dpi. Q125 has an unlabeled stray underline under "his pocket"
    (between labeled segments B and C) that doesn't correspond to any of
    the 4 lettered options; treated as a PDF typesetting artifact and
    excluded from option C's text (kept as the single word "cut", matching
    the single-word-per-option style used throughout this cluster).
  - Q176: private-use-area glyph  (a Wingdings-style arrow icon that
    didn't map to a real Unicode arrow) replacing "->" between hormone
    names — confirmed via 300dpi render, replaced with real "→".
  - Q189: option B was truncated mid-word ("cDNA (complementary DN") —
    completed to "cDNA (complementary DNA)" per the PDF.

Q55's options C and D are both literally "Nm2C-2" in the official PDF
(a genuine printing duplication in the original 2010 paper, confirmed by
rendering the page) — left as-is since it doesn't affect the correct
answer being under the letter the key specifies, matching this project's
policy of transcribing the source faithfully rather than "fixing" the
original exam's own errors (same policy as 2010's Q103 sub-option B,
which is internally self-contradictory but is what the paper prints).

No diagram-only (image-required) questions were found in this paper: a
full-text keyword scan (figure/diagram/graph/curve/"shown below") across
all 17 question pages turned up no real hits (the one "graph" match was
a false-positive substring inside "Chromatography"), consistent with the
source docstring's claim that this paper has no embedded diagram content.
So unlike 2011, there is no DIAGRAM_ONLY set and no image-import step
needed for this paper.

Topic/subtopic tags were assigned by hand against the *existing* DB
vocabulary (queried live via Topic/Subtopic before writing this file) so
tags reuse the same topic/subtopic names already created by prior papers
wherever the concept matches, rather than inventing near-duplicates. A
few genuinely new subtopics were added under existing topics (e.g.
"Torque and Moment of Force" under Vectors and Equilibrium, "Moment of
Inertia" under Rotational and Circular Motion) — these are created
directly against the DB via import_mcqs.py's get_or_create, matching how
2011's new topics were handled; mdcat-content/syllabus/pmdc_mdcat_syllabus.json
(the official current-curriculum reference) is deliberately NOT touched.
"""
import json
import importlib.util
from pathlib import Path

SOURCE_FILE = Path("mdcat-content/mdcat_2010.py")
OUTPUT_FILE = Path("mdcat-content/parsed-mcqs/MDCAT_2010.json")
PAPER_YEAR = 2010

spec = importlib.util.spec_from_file_location("mdcat_2010", SOURCE_FILE)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

QUESTIONS = mod.QUESTIONS  # list of {'number','subject','question','options':{'A'..'D'},'diagram_text'}

SUBJECT_RANGES = [
    ("Physics", 1, 60),
    ("Chemistry", 61, 120),
    ("English", 121, 150),
    ("Biology", 151, 220),
]

ANSWER_KEY_RAW = """
1:B 2:A 3:C 4:D 5:C 6:A 7:B 8:A 9:D 10:B 11:B 12:B 13:A 14:A 15:C 16:D 17:B 18:D 19:D 20:A
21:A 22:D 23:C 24:D 25:A 26:C 27:C 28:B 29:B 30:B 31:B 32:D 33:C 34:B 35:D 36:D 37:A 38:D 39:A 40:A
41:C 42:A 43:D 44:D 45:B 46:D 47:A 48:D 49:A 50:A 51:A 52:A 53:D 54:A 55:C 56:D 57:D 58:A 59:C 60:C
61:C 62:C 63:D 64:D 65:B 66:C 67:B 68:C 69:B 70:A 71:B 72:B 73:A 74:A 75:A 76:D 77:C 78:D 79:D 80:A
81:B 82:D 83:A 84:A 85:D 86:B 87:D 88:B 89:A 90:D 91:D 92:C 93:A 94:A 95:D 96:C 97:B 98:B 99:A 100:D
101:C 102:C 103:D 104:A 105:C 106:C 107:D 108:D 109:C 110:C 111:A 112:C 113:C 114:D 115:A 116:B 117:D 118:C 119:B 120:C
121:A 122:D 123:C 124:B 125:B 126:D 127:C 128:A 129:A 130:D 131:C 132:C 133:B 134:D 135:C 136:D 137:B 138:B 139:A 140:B
141:A 142:C 143:D 144:A 145:D 146:B 147:D 148:A 149:B 150:D 151:D 152:A 153:B 154:D 155:C 156:D 157:D 158:B 159:A 160:C
161:C 162:D 163:B 164:A 165:B 166:A 167:A 168:C 169:A 170:D 171:A 172:A 173:D 174:B 175:B 176:D 177:C 178:C 179:D 180:D
181:D 182:C 183:A 184:D 185:A 186:C 187:D 188:A 189:D 190:C 191:B 192:A 193:C 194:B 195:D 196:D 197:A 198:C 199:A 200:A
201:C 202:D 203:C 204:B 205:D 206:D 207:C 208:C 209:B 210:B 211:D 212:A 213:C 214:A 215:D 216:C 217:D 218:C 219:D 220:B
"""

ANSWER_KEY = {}
for tok in ANSWER_KEY_RAW.split():
    qnum_str, letter = tok.split(":")
    ANSWER_KEY[int(qnum_str)] = letter.strip().lower()

assert len(ANSWER_KEY) == 220, f"expected 220 key entries, got {len(ANSWER_KEY)}"

# qnum -> (topic, subtopic)
TAGS = {
    # --- Physics 1-60 ---
    1: ("Measurements", "Dimensional Analysis"),
    2: ("Electrostatics", "Electric Charge"),
    3: ("Electromagnetic Induction", "Electrical-Mechanical Analogies"),
    4: ("Electromagnetism", "Magnetic Flux Density"),
    5: ("Dawn of Modern Physics", "Lasers (Working Principle and Uses)"),
    6: ("Electromagnetism", "Torque on Current Loop"),
    7: ("Electronics", "Cathode Ray Oscilloscope (CRO)"),
    8: ("Force and Motion", "Projectile Motion"),
    9: ("Force and Motion", "Newton's Second Law and Linear Momentum"),
    10: ("Work and Energy", "Power"),
    11: ("Electronics", "Transistors (NPN/PNP)"),
    12: ("Electronics", "Operational Amplifiers (OP-AMP)"),
    13: ("Electronics", "Semiconductors (p-type, n-type)"),
    14: ("Dawn of Modern Physics", "Black Body Radiation (Wien's Law)"),
    15: ("Dawn of Modern Physics", "Quantum Theory and Radiation (Photons)"),
    16: ("Dawn of Modern Physics", "Pair Production"),
    17: ("Dawn of Modern Physics", "Heisenberg Uncertainty Principle"),
    18: ("Atomic Spectra", "Atomic Spectra / Line Spectrum"),
    19: ("Nuclear Physics", "Nuclear Fusion"),
    20: ("Nuclear Physics", "Half-life and Rate of Decay"),
    21: ("Nuclear Physics", "Half-life and Rate of Decay"),
    22: ("Nuclear Physics", "Biological and Medical Uses of Radiation"),
    23: ("Measurements", "Dimensional Analysis"),
    24: ("Vectors and Equilibrium", "Conditions of Equilibrium"),
    25: ("Vectors and Equilibrium", "Torque and Moment of Force"),
    26: ("Vectors and Equilibrium", "Addition of Vectors (Rectangular Components)"),
    27: ("Vectors and Equilibrium", "Vector Subtraction"),
    28: ("Force and Motion", "Projectile Motion"),
    29: ("Force and Motion", "Uniform and Variable Acceleration"),
    30: ("Force and Motion", "Projectile Height, Range, Time of Flight"),
    31: ("Force and Motion", "Newton's Second Law and Linear Momentum"),
    32: ("Work and Energy", "Conservative and Non-conservative Forces"),
    33: ("Force and Motion", "Gravitation and Escape Velocity"),
    34: ("Thermodynamics", "Solar Constant and Radiation"),
    35: ("Force and Motion", "Newton's Laws of Motion"),
    36: ("Rotational and Circular Motion", "Moment of Inertia"),
    37: ("Rotational and Circular Motion", "Angular Displacement"),
    38: ("Fluid Dynamics", "Equation of Continuity"),
    39: ("Fluid Dynamics", "Bernoulli's Equation"),
    40: ("Rotational and Circular Motion", "Simple Harmonic Motion (SHM)"),
    41: ("Rotational and Circular Motion", "Simple Harmonic Motion (SHM)"),
    42: ("Waves", "Superposition of Waves"),
    43: ("Waves", "Beats"),
    44: ("Waves", "Organ Pipes"),
    45: ("Waves", "Interference (Newton's Rings, Thin Films)"),
    46: ("Waves", "Young's Double Slit Experiment"),
    47: ("Waves", "Diffraction Grating"),
    48: ("Optics", "Optical Fibers and Total Internal Reflection"),
    49: ("Thermodynamics", "Kinetic Theory of Gases"),
    50: ("Thermodynamics", "Carnot Engine and Efficiency"),
    51: ("Thermodynamics", "Kinetic Theory of Gases"),
    52: ("Thermodynamics", "Reversible and Irreversible Processes"),
    53: ("Electrostatics", "Electric Field"),
    54: ("Electrostatics", "Capacitance"),
    55: ("Electrostatics", "Electric Flux (Gauss's Law)"),
    56: ("Current Electricity", "Steady Current"),
    57: ("Current Electricity", "Electric Power and Heating Effect"),
    58: ("Electronics", "Semiconductors (p-type, n-type)"),
    59: ("Current Electricity", "Galvanometer and Ammeter/Voltmeter Conversion"),
    60: ("Electromagnetism", "Force on Current-Carrying Conductor"),

    # --- Chemistry 61-120 ---
    61: ("Electrochemistry", "Standard Hydrogen Electrode (SHE)"),
    62: ("Electrochemistry", "Redox Reactions"),
    63: ("Macromolecules", "Enzymes as Biocatalysts"),
    64: ("Reaction Kinetics", "Methods to Study Reaction Rate"),
    65: ("Thermochemistry and Energetics", "Enthalpy of Reaction"),
    66: ("s and p Block Elements", "Periodic Trends (Radii, IE, EA, Electronegativity)"),
    67: ("s and p Block Elements", "Group I Reactions"),
    68: ("s and p Block Elements", "Group II Reactions"),
    69: ("s and p Block Elements", "Group II Reactions"),
    70: ("s and p Block Elements", "Periodic Trends (Radii, IE, EA, Electronegativity)"),
    71: ("s and p Block Elements", "Group IV Reactions"),
    72: ("Chemical Bonding", "Bond Energy"),
    73: ("s and p Block Elements", "Noble Gases and their Uses"),
    74: ("Atomic Structure", "Electronic Configuration"),
    75: ("Chemical Bonding", "Hybridization"),
    76: ("Electrochemistry", "Oxidation and Reduction"),
    77: ("Chemistry of Hydrocarbons", "Octane Number and Cracking"),
    78: ("Chemical Bonding", "Sigma and Pi Bonds"),
    79: ("Chemistry of Hydrocarbons", "Preparation of Alkanes"),
    80: ("Industrial Chemistry", "Petrochemical Catalytic Processes"),
    81: ("Chemistry of Hydrocarbons", "Reactivity of Benzene"),
    82: ("Chemistry of Hydrocarbons", "Chemical Reactions of Benzene"),
    83: ("Alkyl Halides", "Nucleophilic Substitution Mechanisms"),
    84: ("Alkyl Halides", "Grignard Reagents"),
    85: ("Industrial Chemistry", "Methanol Synthesis"),
    86: ("Alcohols and Phenols", "Chemistry of Alcohols (Ethers, Esters)"),
    87: ("Alcohols and Phenols", "Alcohol vs Phenol"),
    88: ("Carboxylic Acids", "Distillation Reactions of Carboxylic Acid Salts"),
    89: ("Carboxylic Acids", "Preparation from Nitriles"),
    90: ("Aldehydes and Ketones", "Tests for Aldehydes (Fehling's, Tollens')"),
    91: ("Macromolecules", "Classification and Structure of Proteins"),
    92: ("Carboxylic Acids", "Reactivity of Carboxylic Acids"),
    93: ("Macromolecules", "Classification and Structure of Proteins"),
    94: ("Industrial Chemistry", "Urea Manufacture"),
    95: ("Industrial Chemistry", "Cement Chemistry"),
    96: ("Industrial Chemistry", "Water Treatment"),
    97: ("Industrial Chemistry", "Paper and Pulp Chemistry"),
    98: ("Gases", "Standard Temperature and Pressure"),
    99: ("Atomic Structure", "Mass Spectrometry"),
    100: ("Fundamental Concepts of Chemistry", "Stoichiometry"),
    101: ("Fundamental Concepts of Chemistry", "Purification Techniques (Sublimation, Crystallization)"),
    102: ("Fundamental Concepts of Chemistry", "Purification Techniques (Sublimation, Crystallization)"),
    103: ("Gases", "Ideal Gas Equation"),
    104: ("Gases", "Kinetic Molecular Theory"),
    105: ("Gases", "Plasma State of Matter"),
    106: ("Liquids", "Intermolecular Forces (Van der Waals)"),
    107: ("Solids", "Crystal Lattice"),
    108: ("Atomic Structure", "Discovery of Electron (Cathode Rays)"),
    109: ("Atomic Structure", "Ionization Energy of Hydrogen (Bohr Model)"),
    110: ("Atomic Structure", "Quantum Numbers"),
    111: ("Solids", "Crystal Lattice"),
    112: ("Chemical Bonding", "Sigma and Pi Bonds"),
    113: ("Chemical Bonding", "Dipole Moment"),
    114: ("Thermochemistry and Energetics", "Spontaneity and Entropy"),
    115: ("Thermochemistry and Energetics", "Enthalpy of Reaction"),
    116: ("Chemical Equilibrium", "Chemical Equilibrium (Reversible Reactions)"),
    117: ("Chemical Equilibrium", "Ka, pKa and Acid Strength"),
    118: ("Chemical Equilibrium", "Solubility Products"),
    119: ("Fundamental Concepts of Chemistry", "Concentration Units (ppm, Molarity)"),
    120: ("Solids", "Metallic Bonding and Conduction"),

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
    151: ("Diversity of Life", "Phylum Arthropoda"),
    152: ("Diversity of Life", "Phylum Echinodermata"),
    153: ("Bioenergetics", "Respiration"),
    154: ("Photosynthesis", "Pigments and Light Absorption"),
    155: ("Bioenergetics", "Respiration"),
    156: ("Digestion", "Human Digestive System"),
    157: ("Digestion", "Human Digestive System"),
    158: ("Digestion", "Eating Disorders"),
    159: ("Respiration", "Human Respiratory System"),
    160: ("Respiration", "Gas Exchange in Lungs"),
    161: ("Respiration", "Human Respiratory System"),
    162: ("Coordination and Control", "Endocrine System and Hormones"),
    163: ("Circulation", "Blood Composition and Cells"),
    164: ("Circulation", "Human Heart"),
    165: ("Circulation", "Lymphatic System"),
    166: ("Homeostasis", "Excretion (Nitrogenous Compounds)"),
    167: ("Homeostasis", "Liver Functions"),
    168: ("Homeostasis", "Kidney Structure and Function"),
    169: ("Support and Movement", "Cartilages"),
    170: ("Support and Movement", "Arthritis"),
    171: ("Support and Movement", "Muscle Contraction"),
    172: ("Coordination and Control", "Endocrine System and Hormones"),
    173: ("Coordination and Control", "Animal Behaviour (Reflexes and Instincts)"),
    174: ("Coordination and Control", "Nerve Impulse and Reflexes"),
    175: ("Reproduction", "Human Reproductive System"),
    176: ("Reproduction", "Menstrual Cycle"),
    177: ("Inheritance", "Chromosomal Disorders"),
    178: ("Growth and Development", "Germ Layers and Organogenesis"),
    179: ("Inheritance", "Gene Mutation"),
    180: ("Inheritance", "Chromosomal Disorders"),
    181: ("Biological Molecules", "Structure of DNA"),
    182: ("Biological Molecules", "Ribonucleic Acid (RNA)"),
    183: ("Cell Division", "Mitosis"),
    184: ("Cell Division", "Mitosis"),
    185: ("Cell Division", "Cancer"),
    186: ("Inheritance", "Y-linked Inheritance"),
    187: ("Inheritance", "Gene Interaction (Epistasis)"),
    188: ("Inheritance", "Chromosomal Disorders"),
    189: ("Genetic Engineering", "cDNA Synthesis and Reverse Transcriptase"),
    190: ("Genetic Engineering", "Vectors (Plasmids, Bacteriophages)"),
    191: ("Biotechnology", "Biotechnology and Health Care"),
    192: ("Ecology", "Population Ecology"),
    193: ("Bioenergetics", "Respiration"),
    194: ("Ecology", "Atmospheric Pollution (Ozone Depletion)"),
    195: ("Ecology", "Symbiotic Relationships"),
    196: ("Ecology", "Symbiotic Relationships"),
    197: ("Ecology", "Eutrophication"),
    198: ("Digestion", "Vitamin Deficiency Diseases"),
    199: ("Ecology", "Energy Resources"),
    200: ("Ecology", "Levels of Biological Organization"),
    201: ("Biological Molecules", "Biological Molecules (Definition and Classification)"),
    202: ("Diversity of Life", "Kingdom Prokaryotae (Bacteria)"),
    203: ("Enzymes", "Co-factors of Enzymes"),
    204: ("Enzymes", "Enzyme Inhibitors"),
    205: ("Diversity of Life", "Kingdom Prokaryotae (Bacteria)"),
    206: ("Diversity of Life", "Kingdom Prokaryotae (Bacteria)"),
    207: ("Bioenergetics", "Respiration"),
    208: ("Acellular Life", "Viruses"),
    209: ("Acellular Life", "Viruses"),
    210: ("Diversity of Life", "Kingdom Prokaryotae (Bacteria)"),
    211: ("Diversity of Life", "Kingdom Prokaryotae (Bacteria)"),
    212: ("Diversity of Life", "Kingdom Protista"),
    213: ("Diversity of Life", "Kingdom Protista"),
    214: ("Diversity of Life", "Kingdom Fungi"),
    215: ("Diversity of Life", "Kingdom Fungi"),
    216: ("Diversity of Life", "Kingdom Fungi"),
    217: ("Kingdom Plantae", "Classification of Plant Kingdom (Bryophyta, Pteridophyta)"),
    218: ("Kingdom Plantae", "Angiosperms vs Gymnosperms"),
    219: ("Kingdom Plantae", "Economic Importance of Plants"),
    220: ("Diversity of Life", "Phylum Chordata (Class Mammalia)"),
}

assert len(TAGS) == 220, f"expected 220 tag entries, got {len(TAGS)}"

# qnum -> corrected {'A':..,'B':..,'C':..,'D':..} for extraction defects
# (fraction constructs flattened without '/', trailing boilerplate, etc.)
OPTION_FIXES = {
    7: {"D": "Has positive potential with respect to cathode"},
    21: {
        "A": "-(ΔN/N)/Δt",
        "B": "-ΔN/Δt",
        "C": "-N/Δt",
        "D": "(ΔN/N)/Δt",
    },
    28: {
        "A": "(vi² sin²θ)/g",
        "C": "(vi² sinθ)/g",
        "B": "(2vi sinθ)/g",
        "D": "(vi²/g) sin2θ",
    },
    36: {
        "A": "(1/2)mL²",
        "C": "(1/12)mL",
        "B": "(1/4)m³L",
        "D": "(1/12)mL²",
    },
    54: {
        "C": "ΔV = E/qo",
        "D": "E = d/ΔV",
    },
    57: {
        "C": "V2/R",
    },
    59: {
        "C": "Increasing c/BAN ratio",
    },
    103: {
        "A": "V = R(nT/P) (when 'T' and 'n' are constant)",
        "C": "V = R(P/nT) (when 'P' and 'n' are constant)",
        "B": "V = R(nT/P) (when 'P', 'T' and 'n' are constant)",
        "D": "V = R(nT/P) (when 'P' and 'T' are constant)",
    },
    124: {"D": "Knock"},
    125: {
        "A": "Suddenly he stopped",
        "B": "taking his pocket knife",
        "C": "cut",
        "D": "a wisp of alfalfa",
    },
    126: {
        "A": "The study",
        "B": "population growth",
        "C": "one of the",
        "D": "paradox",
    },
    127: {
        "A": "Among the Western nations",
        "B": "death rate is followed",
        "C": "reduction in the birth",
        "D": "is not now growing",
    },
    128: {
        "A": "with",
        "B": "it is",
        "C": "to keep",
        "D": "on his surroundings",
    },
    129: {
        "A": "in",
        "B": "or",
        "C": "for",
        "D": "the",
    },
    130: {
        "A": "When a low-wage",
        "B": "worker finds",
        "C": "maintain a large family",
        "D": "exceeds his income.",
    },
    140: {"D": "The remains of the body was thrown into the sea."},
    176: {
        "A": "LH → FSH → Estrogen → Progesterone",
        "C": "FSH → Estrogen → Progesterone → LH",
        "B": "FSH → LH → Progesterone → Estrogen",
        "D": "FSH → Estrogen → LH → Progesterone",
    },
    189: {"B": "cDNA (complementary DNA)"},
}

out = []
stats = {"total": 0, "active": 0, "needs_review": 0}

for q in sorted(QUESTIONS, key=lambda x: x["number"]):
    qnum = q["number"]
    opts = dict(q["options"])
    if qnum in OPTION_FIXES:
        opts.update(OPTION_FIXES[qnum])
    if set(opts.keys()) != {"A", "B", "C", "D"}:
        print(f"WARN Q{qnum}: options keys {sorted(opts.keys())} != A-D — skipping")
        continue

    subject = None
    for name, start, end in SUBJECT_RANGES:
        if start <= qnum <= end:
            subject = name
            break
    if subject is None:
        raise ValueError(f"Q{qnum} outside any SUBJECT_RANGES")

    topic, subtopic = TAGS[qnum]
    answer = ANSWER_KEY[qnum]

    out.append({
        "id": f"mdcat-{PAPER_YEAR}-q{qnum}",
        "paper_year": PAPER_YEAR,
        "question_number": qnum,
        "subject": subject,
        "topic": topic,
        "subtopic": subtopic,
        "difficulty": None,
        "question_text": q["question"],
        "options": {"a": opts["A"], "b": opts["B"], "c": opts["C"], "d": opts["D"]},
        "correct_answer": answer,
        "explanation": None,
        "is_active": True,
        "needs_review": False,
        "notes": None,
        "source_file": SOURCE_FILE.name,
        "tag_confidence": "medium",
    })
    stats["active"] += 1
    stats["total"] += 1

OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(out, f, indent=2, ensure_ascii=False)

print(f"\nWrote {len(out)} MCQs to {OUTPUT_FILE}")
print(f"  active: {stats['active']}")
print(f"  needs_review: {stats['needs_review']}")
