"""
Adapter: mdcat_2011.py -> parsed-mcqs/MDCAT_2011.json

Unlike the 2012-2019/2022 adapters, mdcat_2011.py has NO built-in answer key
(source docstring: "No answer key included") and options are a dict keyed by
letter (not a positional list), so there's no B/C-swap risk from list-order
confusion. The answer key below was transcribed from the official UHS key
(mdcat-content/tmp_2011/mdcat2011.pdf, page index 20) and independently
re-verified twice this session against the rendered key-table image crops.

Topic/subtopic tags were assigned by hand (not via scripts/tag_topics.py's
Groq pipeline) because several genuine syllabus gaps required new topics not
in mdcat-content/syllabus/pmdc_mdcat_syllabus.json's closed vocabulary
(Optics, Measurements for Physics; Coordination/Environmental Chemistry for
Chemistry; Ecology, Cell Division, Diversity of Life, Growth and Development,
Kingdom Plantae, Photosynthesis, Genetic Engineering for Biology). These are
created directly against the DB via import_mcqs.py's get_or_create — the
syllabus JSON itself is NOT updated by this script (matches how the Physics/
Chemistry tags were already handled for this same paper in the prior
session), so a future Groq re-tag of another paper won't see them.

OPTION_FIXES corrects a handful of questions where mdcat_2011.py's OCR/text
extraction produced garbled or fabricated option text — found by rendering
the original PDF pages and reading them directly:
  - Q80: garbled structural-formula options (secondary alcohol identification)
  - Q85: garbled structural-formula options (aldehyde homologous series)
  - Q90: option B was fabricated as "glycine" but the diagram shows a
    different (non-alpha) structure; option D also corrected
  - Q95: option B was missing a CH2 from the real aspartic-acid structure
  - Q106: option D had the next section's instructions text concatenated on
  - Q107-112: "SPOT THE ERROR" cluster — source had unusable
    "[Underlined segment X]" placeholders; replaced with the real underlined
    words/phrases transcribed from page_12.png

Q8/Q23/Q24 are genuine image-only questions (options are graphs/curves, not
transcribable as text) — imported inactive with needs_review until the 3
diagram crops are attached via import_question_images (see DIAGRAM_ONLY).

Q189's official key answer (A = "Genetically Modified") looks wrong against
plain biology ("D = Clones" fits the question stem far better), but was
independently re-verified against the key-table page image twice. Kept as
the verified key value per this project's policy of trusting the transcribed
official key, but flagged needs_review=True with a note.
"""
import json
import importlib.util
from pathlib import Path

SOURCE_FILE = Path("mdcat-content/mdcat_2011.py")
OUTPUT_FILE = Path("mdcat-content/parsed-mcqs/MDCAT_2011.json")
PAPER_YEAR = 2011

spec = importlib.util.spec_from_file_location("mdcat_2011", SOURCE_FILE)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

QUESTIONS = mod.QUESTIONS  # list of {'number','subject','question','options':{'A'..'D'},'diagram_text'}

SUBJECT_RANGES = [
    ("Physics", 1, 44),
    ("Chemistry", 45, 102),
    ("English", 103, 132),
    ("Biology", 133, 220),
]

ANSWER_KEY_RAW = """
1:B 2:B 3:B 4:B 5:D 6:B 7:B 8:C 9:D 10:A 11:B 12:A 13:A 14:A 15:D 16:A 17:C 18:A 19:C 20:B
21:A 22:D 23:A 24:D 25:D 26:A 27:A 28:D 29:B 30:B 31:B 32:C 33:D 34:C 35:D 36:A 37:C 38:C 39:D 40:A
41:C 42:B 43:D 44:D 45:C 46:D 47:B 48:A 49:D 50:C 51:C 52:C 53:D 54:D 55:B 56:A 57:D 58:A 59:D 60:D
61:A 62:D 63:C 64:D 65:C 66:B 67:A 68:A 69:D 70:A 71:C 72:B 73:A 74:C 75:A 76:A 77:A 78:B 79:B 80:A
81:A 82:B 83:D 84:A 85:C 86:A 87:D 88:B 89:D 90:A 91:A 92:A 93:D 94:A 95:B 96:B 97:D 98:A 99:A 100:C
101:D 102:D 103:A 104:A 105:B 106:C 107:D 108:A 109:D 110:D 111:A 112:D 113:A 114:A 115:A 116:A 117:B 118:B 119:C 120:D
121:C 122:C 123:D 124:A 125:A 126:C 127:B 128:B 129:C 130:D 131:A 132:A 133:C 134:A 135:A 136:A 137:A 138:A 139:B 140:B
141:A 142:C 143:B 144:C 145:C 146:B 147:A 148:A 149:A 150:C 151:B 152:C 153:D 154:B 155:B 156:A 157:A 158:C 159:A 160:D
161:B 162:A 163:A 164:D 165:D 166:B 167:C 168:D 169:A 170:A 171:B 172:A 173:A 174:A 175:B 176:D 177:C 178:B 179:A 180:D
181:D 182:C 183:C 184:B 185:A 186:B 187:D 188:D 189:A 190:A 191:B 192:B 193:B 194:A 195:A 196:B 197:C 198:C 199:D 200:A
201:D 202:B 203:B 204:A 205:A 206:A 207:B 208:D 209:D 210:A 211:A 212:C 213:C 214:C 215:D 216:D 217:A 218:C 219:C 220:B
"""

ANSWER_KEY = {}
for tok in ANSWER_KEY_RAW.split():
    qnum_str, letter = tok.split(":")
    ANSWER_KEY[int(qnum_str)] = letter.strip().lower()

assert len(ANSWER_KEY) == 220, f"expected 220 key entries, got {len(ANSWER_KEY)}"

# qnum -> (topic, subtopic)
TAGS = {
    # --- Physics 1-44 ---
    1: ("Measurements", "Dimensional Analysis"),
    2: ("Rotational and Circular Motion", "Angular Displacement"),
    3: ("Force and Motion", "Newton's Laws of Motion"),
    4: ("Fluid Dynamics", "Fluid Drag"),
    5: ("Fluid Dynamics", "Terminal Velocity"),
    6: ("Rotational and Circular Motion", "Simple Harmonic Motion (SHM)"),
    7: ("Fluid Dynamics", "Density and Specific Gravity"),
    8: ("Waves", "Diffraction Grating"),
    9: ("Waves", "Superposition of Waves"),
    10: ("Waves", "Diffraction Grating"),
    11: ("Optics", "Human Eye (Near Point, Far Point)"),
    12: ("Waves", "Wave Speed"),
    13: ("Waves", "Doppler Effect"),
    14: ("Rotational and Circular Motion", "Simple Harmonic Motion (SHM)"),
    15: ("Rotational and Circular Motion", "Simple Harmonic Motion (SHM)"),
    16: ("Force and Motion", "Stress and Strain"),
    17: ("Force and Motion", "Stress and Strain"),
    18: ("Thermodynamics", "Kinetic Theory of Gases"),
    19: ("Thermodynamics", "Kinetic Theory of Gases"),
    20: ("Electronics", "Cathode Ray Oscilloscope (CRO)"),
    21: ("Electronics", "Cathode Ray Oscilloscope (CRO)"),
    22: ("Thermodynamics", "First Law of Thermodynamics"),
    23: ("Thermodynamics", "Adiabatic Process"),
    24: ("Thermodynamics", "Isothermal Process"),
    25: ("Current Electricity", "Ohm's Law"),
    26: ("Dawn of Modern Physics", "Lasers (Working Principle and Uses)"),
    27: ("Current Electricity", "Steady Current"),
    28: ("Electromagnetism", "Magnetic Flux Density"),
    29: ("Electromagnetism", "Force Between Parallel Conductors"),
    30: ("Electromagnetism", "Magnetic Flux Density"),
    31: ("Electromagnetism", "Electromagnetic Spectrum"),
    32: ("Dawn of Modern Physics", "Lasers (Working Principle and Uses)"),
    33: ("Dawn of Modern Physics", "Lasers (Working Principle and Uses)"),
    34: ("Current Electricity", "Steady Current"),
    35: ("Dawn of Modern Physics", "Quantum Theory and Radiation (Photons)"),
    36: ("Electromagnetism", "X-rays (Production and Spectrum)"),
    37: ("Electromagnetism", "X-rays (Production and Spectrum)"),
    38: ("Nuclear Physics", "Spontaneous and Random Nuclear Decay"),
    39: ("Nuclear Physics", "Half-life and Rate of Decay"),
    40: ("Nuclear Physics", "Spontaneous and Random Nuclear Decay"),
    41: ("Nuclear Physics", "Half-life and Rate of Decay"),
    42: ("Nuclear Physics", "Spontaneous and Random Nuclear Decay"),
    43: ("Nuclear Physics", "Biological and Medical Uses of Radiation"),
    44: ("Nuclear Physics", "Biological and Medical Uses of Radiation"),

    # --- Chemistry 45-102 ---
    45: ("Atomic Structure", "Mass Spectrometry"),
    46: ("Fundamental Concepts of Chemistry", "Moles and Avogadro's Number"),
    47: ("Liquids", "Hydrogen Bonding"),
    48: ("Liquids", "Hydrogen Bonding"),
    49: ("s and p Block Elements", "Periodic Trends (Radii, IE, EA, Electronegativity)"),
    50: ("Atomic Structure", "Discovery of Electron (Cathode Rays)"),
    51: ("s and p Block Elements", "Periodic Trends (Radii, IE, EA, Electronegativity)"),
    52: ("Atomic Structure", "Electronic Configuration"),
    53: ("Solids", "Lattice Energy"),
    54: ("Thermochemistry and Energetics", "Enthalpy of Reaction"),
    55: ("Fundamental Concepts of Chemistry", "Moles and Avogadro's Number"),
    56: ("Fundamental Concepts of Chemistry", "Moles and Avogadro's Number"),
    57: ("Electrochemistry", "Galvanic Cell (Salt Bridge)"),
    58: ("Electrochemistry", "Oxidation and Reduction"),
    59: ("Chemical Equilibrium", "Common Ion Effect"),
    60: ("Chemical Equilibrium", "Ka, pKa and Acid Strength"),
    61: ("Reaction Kinetics", "Activation Energy and Activated Complex"),
    62: ("Reaction Kinetics", "Activation Energy and Activated Complex"),
    63: ("Solids", "Crystalline Solids"),
    64: ("s and p Block Elements", "Periodic Trends (Radii, IE, EA, Electronegativity)"),
    65: ("s and p Block Elements", "Group II Reactions"),
    66: ("Solids", "Crystal Lattice"),
    67: ("Chemistry of Hydrocarbons", "Hydrogenation of Vegetable Oils"),
    68: ("Coordination Chemistry", "Chelates and Complex Ions"),
    69: ("Industrial Chemistry", "Contact Process (H2SO4 Manufacture)"),
    70: ("Environmental Chemistry", "Atmospheric Pollution (Acid Rain, Smog)"),
    71: ("Chemical Equilibrium", "Haber's Process"),
    72: ("s and p Block Elements", "Group V Reactions"),
    73: ("Chemical Bonding", "Nucleophilic Addition Reactions"),
    74: ("Fundamental Principles of Organic Chemistry", "Isomerism (Stereoisomerism)"),
    75: ("Chemistry of Hydrocarbons", "Friedel-Crafts alkylation reaction"),
    76: ("Chemistry of Hydrocarbons", "Chemical Reactions of Benzene"),
    77: ("Alkyl Halides", "Elimination Mechanisms"),
    78: ("Alkyl Halides", "Nomenclature, Structure, Reactivity"),
    79: ("Aldehydes and Ketones", "Preparation"),
    80: ("Alcohols and Phenols", "Nomenclature, Structure, Reactivity of Alcohols"),
    81: ("Macromolecules", "Enzymes as Biocatalysts"),
    82: ("Alcohols and Phenols", "Alcohol vs Phenol"),
    83: ("Aldehydes and Ketones", "Oxidation Reactions"),
    84: ("Aldehydes and Ketones", "Nucleophilic Addition Reactions"),
    85: ("Aldehydes and Ketones", "Nomenclature and Structure"),
    86: ("Carboxylic Acids", "Conversion to Derivatives (Acyl Halides, Anhydrides, Esters)"),
    87: ("Carboxylic Acids", "Nomenclature, Structure, Preparation"),
    88: ("Carboxylic Acids", "Reactivity of Carboxylic Acids"),
    89: ("Macromolecules", "Classification and Structure of Proteins"),
    90: ("Macromolecules", "Classification and Structure of Proteins"),
    91: ("Macromolecules", "Classification and Structure of Proteins"),
    92: ("Macromolecules", "Classification and Structure of Proteins"),
    93: ("Industrial Chemistry", "Polymers (Condensation and Addition)"),
    94: ("Macromolecules", "Classification and Structure of Proteins"),
    95: ("Macromolecules", "Classification and Structure of Proteins"),
    96: ("Macromolecules", "Carbohydrates"),
    97: ("Industrial Chemistry", "Saponification (Soap Manufacture)"),
    98: ("Industrial Chemistry", "Polymers (Condensation and Addition)"),
    99: ("Industrial Chemistry", "Polymers (Condensation and Addition)"),
    100: ("Industrial Chemistry", "Polymers (Condensation and Addition)"),
    101: ("Alkyl Halides", "Nomenclature, Structure, Reactivity"),
    102: ("Environmental Chemistry", "Atmospheric Pollution (Acid Rain, Smog)"),

    # --- English 103-132 ---
    103: ("Formal and Lexical Aspect of Language", "Contextual Vocabulary"),
    104: ("Formal and Lexical Aspect of Language", "Contextual Vocabulary"),
    105: ("Formal and Lexical Aspect of Language", "Contextual Vocabulary"),
    106: ("Formal and Lexical Aspect of Language", "Contextual Vocabulary"),
    107: ("Writing Skills", "Errors of Function and Spelling"),
    108: ("Writing Skills", "Errors of Function and Spelling"),
    109: ("Writing Skills", "Errors of Function and Spelling"),
    110: ("Writing Skills", "Errors of Function and Spelling"),
    111: ("Writing Skills", "Errors of Function and Spelling"),
    112: ("Writing Skills", "Errors of Function and Spelling"),
    113: ("Formal and Lexical Aspect of Language", "Infinitives and Infinitive Phrases"),
    114: ("Formal and Lexical Aspect of Language", "Subject-Verb Agreement"),
    115: ("Formal and Lexical Aspect of Language", "Active and Passive Voice"),
    116: ("Formal and Lexical Aspect of Language", "Tenses"),
    117: ("Formal and Lexical Aspect of Language", "Tenses"),
    118: ("Formal and Lexical Aspect of Language", "Prepositions"),
    119: ("Formal and Lexical Aspect of Language", "Prepositions"),
    120: ("Formal and Lexical Aspect of Language", "Subject-Verb Agreement"),
    121: ("Formal and Lexical Aspect of Language", "Prepositions"),
    122: ("Formal and Lexical Aspect of Language", "Tenses"),
    123: ("Formal and Lexical Aspect of Language", "Synonyms (Irony, Parody, Satire)"),
    124: ("Formal and Lexical Aspect of Language", "Synonyms (Irony, Parody, Satire)"),
    125: ("Formal and Lexical Aspect of Language", "Synonyms (Irony, Parody, Satire)"),
    126: ("Formal and Lexical Aspect of Language", "Synonyms (Irony, Parody, Satire)"),
    127: ("Formal and Lexical Aspect of Language", "Synonyms (Irony, Parody, Satire)"),
    128: ("Formal and Lexical Aspect of Language", "Synonyms (Irony, Parody, Satire)"),
    129: ("Formal and Lexical Aspect of Language", "Synonyms (Irony, Parody, Satire)"),
    130: ("Formal and Lexical Aspect of Language", "Synonyms (Irony, Parody, Satire)"),
    131: ("Formal and Lexical Aspect of Language", "Synonyms (Irony, Parody, Satire)"),
    132: ("Formal and Lexical Aspect of Language", "Synonyms (Irony, Parody, Satire)"),

    # --- Biology 133-220 ---
    133: ("Cell Division", "Mitosis"),
    134: ("Inheritance", "Chromosomal Disorders"),
    135: ("Inheritance", "Gene Linkage and Crossing Over"),
    136: ("Cell Division", "Mitosis"),
    137: ("Cell Division", "Cancer"),
    138: ("Biological Molecules", "Carbohydrates"),
    139: ("Biological Molecules", "Carbohydrates"),
    140: ("Biological Molecules", "Proteins"),
    141: ("Biological Molecules", "Lipids"),
    142: ("Biotechnology", "Biotechnology and Health Care"),
    143: ("Biotechnology", "Biotechnology and Health Care"),
    144: ("Ecology", "Atmospheric Pollution (Ozone Depletion)"),
    145: ("Ecology", "Habitat and Niche"),
    146: ("Ecology", "Eutrophication"),
    147: ("Ecology", "Symbiotic Relationships"),
    148: ("Ecology", "Food Chain and Food Web"),
    149: ("Inheritance", "Sex Determination"),
    150: ("Inheritance", "X-linked Recessive Inheritance"),
    151: ("Inheritance", "X-linked Recessive Inheritance"),
    152: ("Inheritance", "Multiple Alleles"),
    153: ("Inheritance", "Gene Interaction (Epistasis)"),
    154: ("Biological Molecules", "Structure of DNA"),
    155: ("Enzymes", "Mode of Enzyme Action"),
    156: ("Enzymes", "Co-factors of Enzymes"),
    157: ("Biological Molecules", "Structure of DNA"),
    158: ("Enzymes", "Mode of Enzyme Action"),
    159: ("Acellular Life", "Viruses"),
    160: ("Diversity of Life", "Kingdom Prokaryotae (Bacteria)"),
    161: ("Diversity of Life", "Kingdom Prokaryotae (Bacteria)"),
    162: ("Diversity of Life", "Kingdom Fungi"),
    163: ("Diversity of Life", "Phylum Nematoda"),
    164: ("Diversity of Life", "Phylum Platyhelminthes"),
    165: ("Diversity of Life", "Kingdom Protista"),
    166: ("Growth and Development", "Germ Layers and Organogenesis"),
    167: ("Kingdom Plantae", "Reproduction in Angiosperms (Double Fertilization)"),
    168: ("Digestion", "Human Digestive System"),
    169: ("Digestion", "Human Digestive System"),
    170: ("Digestion", "Human Digestive System"),
    171: ("Digestion", "Human Digestive System"),
    172: ("Circulation", "Human Heart"),
    173: ("Circulation", "Lymphatic System"),
    174: ("Circulation", "Blood Composition and Cells"),
    175: ("Circulation", "Blood Composition and Cells"),
    176: ("Homeostasis", "Osmoregulation"),
    177: ("Homeostasis", "Osmoregulation"),
    178: ("Homeostasis", "Kidney Stones and Failure"),
    179: ("Homeostasis", "Osmoregulation"),
    180: ("Homeostasis", "Glomerular Filtration and Reabsorption"),
    181: ("Coordination and Control", "Nerve Impulse and Reflexes"),
    182: ("Coordination and Control", "Nerve Impulse and Reflexes"),
    183: ("Coordination and Control", "Brain"),
    184: ("Coordination and Control", "Brain"),
    185: ("Reproduction", "Human Reproductive System"),
    186: ("Reproduction", "Menstrual Cycle"),
    187: ("Reproduction", "Human Reproductive System"),
    188: ("Immunity", "Specific Defense Mechanism"),
    189: ("Biotechnology", "Biotechnology and Health Care"),
    190: ("Acellular Life", "Viruses"),
    191: ("Ecology", "Biological Control"),
    192: ("Cell Structure and Function", "Cytoplasmic Organelles"),
    193: ("Diversity of Life", "Kingdom Prokaryotae (Bacteria)"),
    194: ("Cell Structure and Function", "Cytoplasmic Organelles"),
    195: ("Cell Structure and Function", "Cytoplasmic Organelles"),
    196: ("Cell Division", "Cell Cycle"),
    197: ("Reproduction", "Menstrual Cycle"),
    198: ("Reproduction", "Sexually Transmitted Diseases"),
    199: ("Support and Movement", "Muscles (Smooth, Cardiac, Skeletal)"),
    200: ("Support and Movement", "Skeletal Muscle Ultra-structure"),
    201: ("Support and Movement", "Muscle Contraction"),
    202: ("Support and Movement", "Muscle Contraction"),
    203: ("Support and Movement", "Skeletal Muscle Ultra-structure"),
    204: ("Coordination and Control", "Brain"),
    205: ("Coordination and Control", "Endocrine System and Hormones"),
    206: ("Coordination and Control", "Endocrine System and Hormones"),
    207: ("Coordination and Control", "Endocrine System and Hormones"),
    208: ("Immunity", "Specific Defense Mechanism"),
    209: ("Immunity", "Specific Defense Mechanism"),
    210: ("Immunity", "Non-Specific Defense Mechanism"),
    211: ("Immunity", "Specific Defense Mechanism"),
    212: ("Immunity", "Specific Defense Mechanism"),
    213: ("Bioenergetics", "Respiration"),
    214: ("Bioenergetics", "Respiration"),
    215: ("Bioenergetics", "Respiration"),
    216: ("Photosynthesis", "Cyclic and Non-Cyclic Photophosphorylation"),
    217: ("Photosynthesis", "Cyclic and Non-Cyclic Photophosphorylation"),
    218: ("Genetic Engineering", "Vectors (Plasmids, Bacteriophages)"),
    219: ("Genetic Engineering", "Restriction Enzymes and Gene Isolation"),
    220: ("Genetic Engineering", "PCR and DNA Amplification"),
}

assert len(TAGS) == 220, f"expected 220 tag entries, got {len(TAGS)}"

# qnum -> corrected {'A':..,'B':..,'C':..,'D':..} for OCR-garbled / fabricated options
OPTION_FIXES = {
    80: {
        "A": "H3C-CH(OH)-CH3 (isopropanol)",
        "B": "H3C-CH2-CH2-OH (propan-1-ol)",
        "C": "H3C-CH(CH3)-CH2-OH (isobutanol)",
        "D": "H3C-CH(CH3)-CH2-C(CH3)(OH)-CH3",
    },
    85: {
        "A": "HCOCl (formyl chloride)",
        "B": "HCONH2 (formamide)",
        "C": "HCHO (formaldehyde)",
        "D": "HCOOC2H5 (ethyl formate)",
    },
    90: {
        "A": "CH3-CH(NH2)-COOH (alanine)",
        "B": "CH3-C(H)(CH2NH2)-COOH",
        "C": "CH3-CH(NH2)-CH2-COOH",
        "D": "CH3-CH(COOH)-CH(NH2)-CH3",
    },
    95: {
        "A": "CH3-CH(NH2)-COOH",
        "B": "HOOC-CH(NH2)-CH2-COOH (aspartic acid)",
        "C": "CH3-CH(NH2)-CH2-COOH",
        "D": "CH3-C(H)(NH2)-CH-COOH",
    },
    106: {
        "A": "Festival",
        "B": "Romp",
        "C": "Pomp",
        "D": "Happiness",
    },
    107: {"A": "patient's", "B": "of", "C": "which", "D": "quiet"},
    108: {"A": "measure", "B": "to", "C": "from", "D": "the accused"},
    109: {"A": "is", "B": "of", "C": "in", "D": "lack"},
    110: {"A": "raising", "B": "much", "C": "demands", "D": "away"},
    111: {"A": "uncurable", "B": "without", "C": "judicious", "D": "use"},
    112: {"A": "to", "B": "sister's", "C": "achievement", "D": "up"},
}

# Image-only questions: options are graphs/curves, not transcribable as text.
# Imported inactive until the crop+import_question_images step attaches the
# real diagram and flips is_active. See DIAGRAM_MCQS note at top of file.
DIAGRAM_ONLY = {
    8: "Single-slit diffraction intensity-vs-position graph — 4 curve options, not transcribable as text. Needs QuestionImage from tmp_2011/pages/page_02.png.",
    23: "Isothermal/adiabatic P-V graph comparison — 4 curve options, not transcribable as text. Needs QuestionImage from tmp_2011/pages/page_04.png.",
    24: "P-V isotherm identification — 4 curve options, not transcribable as text. Needs QuestionImage from tmp_2011/pages/page_04.png.",
}

# Extra needs_review flags that aren't about missing images
SPECIAL_NOTES = {
    189: "Official key says A ('Genetically Modified'); D ('Clones') reads as the biologically correct answer for this question stem. Verified twice against the key-table page image (key_col4.png) — this is what the official key says, not a transcription slip. Kept per policy of trusting the verified official key.",
}

out = []
stats = {"total": 0, "active": 0, "diagram_inactive": 0, "needs_review": 0}

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

    is_active = True
    needs_review = False
    notes = None

    if qnum in DIAGRAM_ONLY:
        is_active = False
        needs_review = True
        notes = DIAGRAM_ONLY[qnum]
        stats["diagram_inactive"] += 1

    if qnum in SPECIAL_NOTES:
        needs_review = True
        notes = SPECIAL_NOTES[qnum] if notes is None else f"{notes} | {SPECIAL_NOTES[qnum]}"

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
        "question_text": q["question"],
        "options": {"a": opts["A"], "b": opts["B"], "c": opts["C"], "d": opts["D"]},
        "correct_answer": answer,
        "explanation": None,
        "is_active": is_active,
        "needs_review": needs_review,
        "notes": notes,
        "source_file": SOURCE_FILE.name,
        "tag_confidence": "medium",
    })
    stats["total"] += 1

OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(out, f, indent=2, ensure_ascii=False)

print(f"\nWrote {len(out)} MCQs to {OUTPUT_FILE}")
print(f"  active: {stats['active']}")
print(f"  inactive (diagram-only, needs image): {stats['diagram_inactive']}")
print(f"  needs_review: {stats['needs_review']}")
