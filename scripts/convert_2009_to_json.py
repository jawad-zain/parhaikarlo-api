"""
Adapter: mdcat_2009.py -> parsed-mcqs/MDCAT_2009.json

Same source PDF as 2010 (mdcat-content/tmp_2010/mdcat_2008_2016_solved.pdf,
"MDCAT Past Papers (2008-2016) Solved"), same "no answer key included"
problem as 2010's source docstring describes. Unlike 2010, the compiled
PDF's per-year structure is: [question paper for year Y] immediately
followed by [that year's own ANSWER KEY page]. For 2009 this means the
question paper is at PDF page indices 18-35 (0-indexed; "PDF pages 19-36"
1-indexed, matching mdcat_2009.py's header comment) and the answer key is
the single page at index 36, extracted with pymupdf's real text layer (not
OCR -- confirmed genuine embedded text) and cross-verified against the
inline yellow/orange answer-highlighting visible when rendering the
question pages themselves at 350dpi (every question spot-checked against
its rendered page image agreed with the extracted key; see
tmp_2009/page_*_hires.png).

KEY_RAW below is that 220-entry table verbatim; Q76 is genuinely "X"
(unresolved) in the source PDF's own key -- not an extraction failure on
our part, the official compiled key itself never resolved it.

OPTION_FIXES covers two distinct problem classes found in mdcat_2009.py:

1. Page-footer bleed-through: pymupdf's linear text extraction pulls in
   the running footer ("Page N of 18") and even a few section headers
   (CHEMISTRY/ENGLISH/BIOLOGY) or diagram/instruction-block text from the
   *next* printed page, concatenating it onto the last option/question of
   the last item on the *current* page. Purely cosmetic -- stripped back
   to the real option text after visually confirming against the
   rendered page (e.g. Q17, Q30, Q40, Q48, Q60, Q84, Q99, Q114, Q120,
   Q139, Q150, Q151, Q164). Q124, Q128, Q140 similarly had a large
   SPOT-THE-ERROR / sentence-choice instruction block glued onto their
   last option; same fix.

2. A systemic B/C (or C/D) option-letter swap bug, the same bug class
   flagged in this project's 2012 pass: this print run lays out options
   column-major (top-left=A, bottom-left=B, top-right=C, bottom-right=D),
   but on Q70, Q72, Q83, Q115 and Q169 the source PDF itself prints a
   *duplicate* letter for the bottom-left option (e.g. Q115 prints
   "D) Zinc plating" where position says it should be "B)") -- a genuine
   defect in the original 1100-mark exam paper's typesetting, not an OCR
   artifact. Whatever process first produced mdcat_2009.py took the
   printed (wrong) label at face value for exactly these 5 questions,
   producing a silent B/C or C/D swap invisible to simple letter-vs-key
   checking. Caught here by cross-referencing every option's *content*
   against the highlighted-correct-answer in the rendered page image, per
   this project's standing policy after the 2012 discovery. All 5 were
   confirmed by direct visual inspection of tmp_2009/page_*_hires.png
   before fixing (not fixed blindly).

Q9's nuclear gamma-decay equation is a special case: the original PDF sets
it in isotope notation (superscript A, subscript Z, dot for excited
state) that a plain-text layer cannot represent, so all four options had
collapsed to near-duplicate placeholder prose in the raw extraction. Its
real distinguishing content (rendered and read at 350dpi from page index
19) is reconstructed in OPTION_FIXES/9 instead.

Q125-130 (the SPOT THE ERROR cluster) have empty options in the raw
extraction because underlined text is invisible to plain-text extraction.
The four underlined segments for each were transcribed directly from the
350dpi renders (tmp_2009/page_28_hires.png, page_29_hires.png), same
technique as 2010's equivalent cluster.

Topic/subtopic tags were assigned by hand against the *existing* DB
vocabulary (queried live via Topic/Subtopic -- see tmp_2009/db_topics.txt
and db_subtopics.txt -- before writing this file) so tags reuse the same
names already created by prior papers wherever the concept matches. A
small number of genuinely new subtopics were added under existing topics
where nothing fit (e.g. "Logic Gates" under Electronics, "Apoptosis
(Programmed Cell Death)" under Cell Division) -- created directly against
the DB via import_mcqs.py's get_or_create, matching how 2010/2011 handled
new topics; mdcat-content/syllabus/pmdc_mdcat_syllabus.json is
deliberately NOT touched.
"""
import json
import importlib.util
from pathlib import Path

SOURCE_FILE = Path("mdcat-content/mdcat_2009.py")
OUTPUT_FILE = Path("mdcat-content/parsed-mcqs/MDCAT_2009.json")
PAPER_YEAR = 2009

spec = importlib.util.spec_from_file_location("mdcat_2009", SOURCE_FILE)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

QUESTIONS = mod.QUESTIONS  # list of {'number','subject','question','options':{'A'..'D'},'diagram_text'}

# --- answer key, extracted verbatim from PDF page index 36's text layer ---
KEY_RAW = """
ID:B 1:C 2:B 3:D 4:A 5:C 6:D 7:B 8:B 9:D 10:A
11:D 12:D 13:C 14:B 15:C 16:A 17:C 18:A 19:D 20:D
21:A 22:D 23:D 24:B 25:B 26:C 27:A 28:A 29:D 30:D
31:A 32:C 33:C 34:D 35:D 36:D 37:C 38:A 39:A 40:D
41:B 42:C 43:A 44:D 45:D 46:C 47:A 48:B 49:A 50:B
51:C 52:A 53:A 54:B 55:B 56:A 57:C 58:C 59:A 60:A
61:A 62:B 63:C 64:A 65:C 66:B 67:A 68:B 69:C 70:A
71:A 72:D 73:D 74:A 75:A 76:X 77:C 78:A 79:B 80:B
81:C 82:B 83:A 84:A 85:B 86:A 87:D 88:B 89:D 90:D
91:B 92:D 93:A 94:B 95:D 96:C 97:D 98:C 99:C 100:A
101:B 102:D 103:C 104:D 105:B 106:B 107:A 108:A 109:A 110:D
111:A 112:B 113:D 114:A 115:B 116:A 117:A 118:D 119:C 120:D
121:D 122:A 123:D 124:D 125:A 126:C 127:C 128:B 129:A 130:B
131:C 132:A 133:A 134:D 135:D 136:D 137:D 138:D 139:A 140:C
141:D 142:C 143:C 144:B 145:A 146:C 147:B 148:B 149:A 150:D
151:C 152:A 153:D 154:D 155:B 156:C 157:B 158:D 159:B 160:A
161:C 162:D 163:B 164:C 165:A 166:B 167:A 168:D 169:C 170:B
171:D 172:B 173:A 174:A 175:D 176:D 177:C 178:A 179:A 180:D
181:D 182:A 183:B 184:A 185:B 186:A 187:B 188:C 189:B 190:D
191:D 192:B 193:D 194:B 195:C 196:C 197:B 198:D 199:D 200:A
201:A 202:C 203:D 204:B 205:D 206:B 207:A 208:B 209:A 210:D
211:D 212:B 213:A 214:B 215:A 216:D 217:A 218:A 219:A 220:D
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
    9: {
        "A": "Ground-state nucleus (A, Z) → excited nucleus (A, Z)* + γ-radiation",
        "B": "Excited nucleus (A, Z)* → nucleus (A, Z) + β-particles",
        "C": "Excited nucleus (A, Z)* → nucleus (A, Z−1) + γ-radiation",
        "D": "Excited nucleus (A, Z)* → nucleus (A, Z) + γ-radiation",
    },
    17: {"D": "Half of the original value"},
    30: {"D": "10 ms-1"},
    40: {"D": "Double"},
    48: {"D": "Increase in temperature and decrease in resistance"},
    60: {"D": "Pentavalent Element"},
    # Q70: strip footer junk AND fix the B/C swap (source PDF prints the
    # bottom-left option as "C) Charles's Law" instead of "B)").
    70: {"B": "Charles’s Law", "C": "Boyle’s Law"},
    # Q72: strip footer/junk AND fix the C/D swap (top-right printed as
    # "D) NO3" instead of "C)").
    72: {"C": "NO₃⁻", "D": "NO₂⁺"},
    # Q83: fix the B/C swap (bottom-left printed as "C) Aldehyde Group"
    # instead of "B)").
    83: {"B": "Aldehyde Group", "C": "Hydrogen Bonding"},
    84: {"D": "4 – 40 kg per acre"},
    99: {"D": "Adding NaNO3 from outside"},
    114: {"D": "Krypton"},
    # Q115: 3-way rotation fix -- source PDF prints the bottom-left option
    # as "D) Zinc plating" (duplicating the real D label), which pushed
    # the true B/C/D values one slot off in the original extraction.
    115: {"B": "Zinc plating", "C": "Nickel plating", "D": "Copper plating"},
    120: {"D": "Ethane"},
    124: {"D": "Hit"},
    # Q125-130: SPOT THE ERROR cluster. Underlines are invisible to plain
    # text extraction, so the raw source had empty options; transcribed
    # directly from the 350dpi page renders.
    125: {"A": "better than", "B": "as well as", "C": "bags", "D": "various"},
    126: {"A": "too much", "B": "one’s hard work", "C": "provident", "D": "plays its part"},
    127: {"A": "first adventure", "B": "round", "C": "through", "D": "minimum cost"},
    128: {"A": "has been working", "B": "since", "C": "the last five years", "D": "break"},
    129: {"A": "reached at", "B": "a few", "C": "to be exact", "D": "is going to stay"},
    130: {"A": "a big rally", "B": "disintegrated", "C": "chaos", "D": "ruled"},
    139: {"D": "They felt badly while leaving their friends."},
    140: {"D": "He then struck the man himself a similar bow, which felled him in the earth like a log."},
    150: {"D": "Suitable"},
    151: {"D": "CGUTCC"},
    164: {"D": "Syphilis"},
    # Q169: fix the B/C swap (top-right printed as "B) Phenylalanine
    # oxidase" instead of "C)").
    169: {"B": "Phenylalanine phosphate", "C": "Phenylalanine oxidase"},
}

# qnum -> replacement question_text (strips page-footer/section-header/
# instruction-block junk that bled into the stem itself)
QUESTION_TEXT_FIXES = {
    70: "In the process of respiration there is application of:",
    72: "During nitration of benzene the active nitrating agent is:",
    83: "In conjugated protein molecules, the protein is attached or conjugated to some non-protein group which are called:",
    115: "The most durable metal plating on iron to protect against corrosion is:",
    169: "In phenylketonuria, phenylalanine is not degraded because of defective enzyme:",
}

# Q76's official key entry is genuinely "X" (unresolved) in the source --
# not an extraction failure on our part.
UNRESOLVED_KEY_NOTE = {
    76: "Answer key entry for Q76 unresolved in the official UHS-compiled source (printed as 'X') -- the compiled key itself never resolved this one.",
}

# Q152 is a diagram-only question (four charge-distribution diagrams
# across a neuron membrane); no text substitute fully captures it.
VISUAL_REQUIRED = {152}

# qnum -> (topic, subtopic)
TAGS = {
    # --- Physics 1-60 ---
    1: ("Electronics", "Operational Amplifiers (OP-AMP)"),
    2: ("Electronics", "Logic Gates"),
    3: ("Dawn of Modern Physics", "Black Body Radiation (Wien's Law)"),
    4: ("Dawn of Modern Physics", "Quantum Theory and Radiation (Photons)"),
    5: ("Waves", "Compton effect"),
    6: ("Dawn of Modern Physics", "Quantum Theory and Radiation (Photons)"),
    7: ("Dawn of Modern Physics", "Lasers (Working Principle and Uses)"),
    8: ("Electromagnetism", "X-rays (Production and Spectrum)"),
    9: ("Nuclear Physics", "Spontaneous and Random Nuclear Decay"),
    10: ("Dawn of Modern Physics", "Pair Production"),
    11: ("Measurements", "Dimensional Analysis"),
    12: ("Electromagnetism", "Electromagnetic Spectrum"),
    13: ("Vectors and Equilibrium", "Addition of Vectors (Rectangular Components)"),
    14: ("Vectors and Equilibrium", "Addition of Vectors (Rectangular Components)"),
    15: ("Waves", "Beats"),
    16: ("Waves", "Doppler Effect"),
    17: ("Waves", "Young's Double Slit Experiment"),
    18: ("Waves", "Interference (Newton's Rings, Thin Films)"),
    19: ("Waves", "Interference (Newton's Rings, Thin Films)"),
    20: ("Optics", "Optical Fibers and Total Internal Reflection"),
    21: ("Fluid Dynamics", "Pascal's Law and Hydraulic Systems"),
    22: ("Thermodynamics", "Kinetic Theory of Gases"),
    23: ("Thermodynamics", "Adiabatic Process"),
    24: ("Thermodynamics", "Reversible and Irreversible Processes"),
    25: ("Electrostatics", "Electric Potential Energy and Potential"),
    26: ("Electrostatics", "Electric Forces"),
    27: ("Vectors and Equilibrium", "Scalar Product of Vectors"),
    28: ("Vectors and Equilibrium", "Torque and Moment of Force"),
    29: ("Electromagnetism", "Electromagnetic Spectrum"),
    30: ("Force and Motion", "Acceleration"),
    31: ("Force and Motion", "Velocity"),
    32: ("Force and Motion", "Collisions (Elastic and Inelastic)"),
    33: ("Work and Energy", "Work"),
    34: ("Electromagnetism", "Force on Current-Carrying Conductor"),
    35: ("Electronics", "Transistors (NPN/PNP)"),
    36: ("Electronics", "Operational Amplifiers (OP-AMP)"),
    37: ("Thermodynamics", "Solar Constant and Radiation"),
    38: ("Rotational and Circular Motion", "Relation Between Angular and Linear Quantities"),
    39: ("Rotational and Circular Motion", "Moment of Inertia"),
    40: ("Rotational and Circular Motion", "Simple Harmonic Motion (SHM)"),
    41: ("Work and Energy", "Potential Energy"),
    42: ("Fluid Dynamics", "Terminal Velocity"),
    43: ("Fluid Dynamics", "Bernoulli's Equation"),
    44: ("Rotational and Circular Motion", "Circular Motion"),
    45: ("Electromagnetism", "Electromagnetic Spectrum"),
    46: ("Waves", "Wave Speed"),
    47: ("Electrostatics", "Electric Potential Energy and Potential"),
    48: ("Current Electricity", "Resistivity and Temperature Coefficient"),
    49: ("Current Electricity", "Resistivity and Temperature Coefficient"),
    50: ("Current Electricity", "Internal Resistance of Sources"),
    51: ("Electromagnetism", "Motion of Charged Particle in Magnetic Field"),
    52: ("Electromagnetism", "Magnetic Flux Density"),
    53: ("Current Electricity", "Galvanometer and Ammeter/Voltmeter Conversion"),
    54: ("Current Electricity", "Galvanometer and Ammeter/Voltmeter Conversion"),
    55: ("Electromagnetism", "Motion of Charged Particle in Magnetic Field"),
    56: ("Electromagnetic Induction", "Faraday's Law"),
    57: ("Electromagnetic Induction", "Transformer"),
    58: ("Alternating Current", "Phase of Alternating Current"),
    59: ("Alternating Current", "AC Through Capacitor"),
    60: ("Electronics", "Semiconductors (p-type, n-type)"),

    # --- Chemistry 61-120 ---
    61: ("Thermochemistry and Energetics", "Exothermic and Endothermic Reactions"),
    62: ("Reaction Kinetics", "Order of Reaction"),
    63: ("Chemical Equilibrium", "Chemical Equilibrium (Reversible Reactions)"),
    64: ("Carboxylic Acids", "Reactivity of Carboxylic Acids"),
    65: ("Macromolecules", "Classification and Structure of Proteins"),
    66: ("Fundamental Concepts of Chemistry", "Limiting and Excess Reactants"),
    67: ("Atomic Structure", "Mass Spectrometry"),
    68: ("Fundamental Concepts of Chemistry", "Purification Techniques (Sublimation, Crystallization)"),
    69: ("Fundamental Concepts of Chemistry", "Chromatography Techniques"),
    70: ("Gases", "Kinetic Molecular Theory"),
    71: ("Chemistry of Hydrocarbons", "Nomenclature of Alkenes"),
    72: ("Chemistry of Hydrocarbons", "Reactivity of Benzene"),
    73: ("Chemistry of Hydrocarbons", "Acidity of Alkynes"),
    74: ("Alkyl Halides", "Grignard Reagents"),
    75: ("Alkyl Halides", "Grignard Reagents"),
    76: ("Industrial Chemistry", "Methanol Synthesis"),
    77: ("Alcohols and Phenols", "Electrophilic Aromatic Substitution in Phenols"),
    78: ("Alcohols and Phenols", "Alcohol vs Phenol"),
    79: ("Chemistry of Hydrocarbons", "Chemistry of Alkenes"),
    80: ("Aldehydes and Ketones", "Oxidation Reactions"),
    81: ("Industrial Chemistry", "Polymers (Condensation and Addition)"),
    82: ("Aldehydes and Ketones", "Tests for Aldehydes (Fehling's, Tollens')"),
    83: ("Macromolecules", "Classification and Structure of Proteins"),
    84: ("Industrial Chemistry", "Fertilizers and Plant Nutrients"),
    85: ("Industrial Chemistry", "Fertilizers and Plant Nutrients"),
    86: ("Environmental Chemistry", "Atmospheric Pollution (Acid Rain, Smog)"),
    87: ("Industrial Chemistry", "Water Treatment"),
    88: ("Gases", "Plasma State of Matter"),
    89: ("Gases", "Absolute Zero"),
    90: ("Solids", "Metallic Bonding and Conduction"),
    91: ("Macromolecules", "Classification and Structure of Proteins"),
    92: ("Atomic Structure", "Discovery of Proton"),
    93: ("Atomic Structure", "Spectrum of Hydrogen"),
    94: ("Atomic Structure", "Spectrum of Hydrogen"),
    95: ("Chemical Bonding", "Ionic Character of Covalent Bond"),
    96: ("Chemical Bonding", "Ionic Character of Covalent Bond"),
    97: ("Chemical Bonding", "VSEPR Theory"),
    98: ("Thermochemistry and Energetics", "Exothermic and Endothermic Reactions"),
    99: ("Chemical Equilibrium", "Common Ion Effect"),
    100: ("Fundamental Concepts of Chemistry", "Concentration Units (ppm, Molarity)"),
    101: ("Solids", "Lattice Energy"),
    102: ("Electrochemistry", "Redox Reactions"),
    103: ("Electrochemistry", "Galvanic Cell (Salt Bridge)"),
    104: ("Electrochemistry", "Redox Reactions"),
    105: ("Macromolecules", "Carbohydrates"),
    106: ("s and p Block Elements", "s, p, d, f Block Demarcation"),
    107: ("Atomic Structure", "Electronic Configuration"),
    108: ("s and p Block Elements", "Group II Reactions"),
    109: ("s and p Block Elements", "Group II Reactions"),
    110: ("s and p Block Elements", "Group I Reactions"),
    111: ("Solids", "Crystalline Solids"),
    112: ("s and p Block Elements", "Group IV Reactions"),
    113: ("s and p Block Elements", "Group V Reactions"),
    114: ("s and p Block Elements", "Noble Gases and their Uses"),
    115: ("Electrochemistry", "Oxidation and Reduction"),
    116: ("Transition Elements", "Electronic Structure of d-block"),
    117: ("Fundamental Concepts of Chemistry", "Qualitative Analysis (Analytical Tests)"),
    118: ("Chemical Bonding", "Hybridization"),
    119: ("Chemical Bonding", "Isomerism (Stereoisomerism)"),
    120: ("Alkyl Halides", "Grignard Reagents"),

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
    151: ("Biological Molecules", "Structure of DNA"),
    152: ("Coordination and Control", "Neurons"),
    153: ("Immunity", "Specific Defense Mechanism"),
    154: ("Circulation", "Cardiac Cycle and Phases of Heartbeat"),
    155: ("Homeostasis", "Kidney Structure and Function"),
    156: ("Homeostasis", "Osmoregulation"),
    157: ("Homeostasis", "Kidney Stones and Failure"),
    158: ("Inheritance", "Gene Mutation"),
    159: ("Support and Movement", "Joints"),
    160: ("Support and Movement", "Human Skeleton (Cartilage, Muscle, Bone)"),
    161: ("Coordination and Control", "Neurons"),
    162: ("Coordination and Control", "Endocrine System and Hormones"),
    163: ("Reproduction", "Menstrual Cycle"),
    164: ("Reproduction", "Sexually Transmitted Diseases"),
    165: ("Growth and Development", "Germ Layers and Organogenesis"),
    166: ("Photosynthesis", "Pigments and Light Absorption"),
    167: ("Biological Molecules", "Structure of DNA"),
    168: ("Biological Molecules", "Structure of DNA"),
    169: ("Inheritance", "Gene Mutation"),
    170: ("Inheritance", "Chromosomal Disorders"),
    171: ("Cell Division", "Apoptosis (Programmed Cell Death)"),
    172: ("Cell Structure and Function", "Cytoplasmic Organelles"),
    173: ("Inheritance", "Incomplete Dominance and Codominance"),
    174: ("Immunity", "Specific Defense Mechanism"),
    175: ("Genetic Engineering", "PCR and DNA Amplification"),
    176: ("Biotechnology", "Cloning and Asexual Reproduction"),
    177: ("Biotechnology", "Biotechnology and Health Care"),
    178: ("Evolution", "Darwinism"),
    179: ("Evolution", "Concept of Evolution"),
    180: ("Evolution", "Concept of Evolution"),
    181: ("Ecology", "Symbiotic Relationships"),
    182: ("Ecology", "Food Chain and Food Web"),
    183: ("Ecology", "Levels of Biological Organization"),
    184: ("Ecology", "Energy Resources"),
    185: ("Circulation", "Blood Vessels (Arteries, Veins, Capillaries)"),
    186: ("Diversity of Life", "Kingdom Prokaryotae (Bacteria)"),
    187: ("Bioenergetics", "Respiration"),
    188: ("Biological Molecules", "Proteins"),
    189: ("Enzymes", "Mode of Enzyme Action"),
    190: ("Enzymes", "Mode of Enzyme Action"),
    191: ("Cell Structure and Function", "Cytoplasmic Organelles"),
    192: ("Cell Structure and Function", "Cytoplasmic Organelles"),
    193: ("Biological Molecules", "Lipids"),
    194: ("Inheritance", "X-linked Recessive Inheritance"),
    195: ("Reproduction", "Sexually Transmitted Diseases"),
    196: ("Acellular Life", "AIDS and HIV Infection"),
    197: ("Genetic Engineering", "Vectors (Plasmids, Bacteriophages)"),
    198: ("Diversity of Life", "Kingdom Prokaryotae (Bacteria)"),
    199: ("Diversity of Life", "Kingdom Protista"),
    200: ("Diversity of Life", "Kingdom Protista"),
    201: ("Diversity of Life", "Kingdom Fungi"),
    202: ("Biological Molecules", "Carbohydrates"),
    203: ("Diversity of Life", "Kingdom Fungi"),
    204: ("Kingdom Plantae", "Angiosperms vs Gymnosperms"),
    205: ("Kingdom Plantae", "Reproduction in Angiosperms (Double Fertilization)"),
    206: ("Kingdom Plantae", "Economic Importance of Plants"),
    207: ("Diversity of Life", "Phylum Platyhelminthes"),
    208: ("Diversity of Life", "Kingdom Protista"),
    209: ("Diversity of Life", "Body Cavities (Coelom Classification)"),
    210: ("Photosynthesis", "Cyclic and Non-Cyclic Photophosphorylation"),
    211: ("Bioenergetics", "Respiration"),
    212: ("Bioenergetics", "Respiration"),
    213: ("Digestion", "Human Digestive System"),
    214: ("Digestion", "Human Digestive System"),
    215: ("Digestion", "Human Digestive System"),
    216: ("Cell Structure and Function", "Cytoplasmic Organelles"),
    217: ("Respiration", "Gas Exchange in Lungs"),
    218: ("Respiration", "Gas Exchange in Lungs"),
    219: ("Biological Molecules", "Proteins"),
    220: ("Circulation", "Blood Composition and Cells"),
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

    text = QUESTION_TEXT_FIXES.get(qnum, q["question"])
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

    is_visual = qnum in VISUAL_REQUIRED
    if is_visual:
        needs_review = True
        notes = notes or "Diagram-only question (charge-distribution diagrams) -- needs image attached."
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
