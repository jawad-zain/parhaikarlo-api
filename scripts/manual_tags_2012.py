# -*- coding: utf-8 -*-
"""Manually assign (topic, subtopic, confidence) to all 220 MDCAT_2012.json MCQs,
using the exact vocabulary strings from pmdc_mdcat_syllabus.json. Done by hand
(no Groq/LLM call) per user instruction.

confidence is "high"/"medium" for a clean vocabulary match, "low" where the
PMDC syllabus in pmdc_mdcat_syllabus.json simply has no matching topic (e.g. no
Optics, Kinetic Theory of Gases, Ecology, Endocrine System, Digital Logic, or
Environmental Chemistry chapter exists in the vocab at all) and the nearest
available bucket was picked as a forced best-effort. "low" entries also get
needs_review=True on merge so they surface for a human to reconsider if/when
the syllabus vocabulary is extended.
"""
import json

TAGS = {
    # ---- PHYSICS (1-44) ----
    1: ("Electromagnetism", "Magnetic Flux Density", "medium"),
    2: ("Electromagnetism", "Magnetic Flux Density", "high"),
    3: ("Electromagnetism", "Magnetic Flux Density", "medium"),
    4: ("Dawn of Modern Physics", "Quantum Theory and Radiation (Photons)", "medium"),
    5: ("Dawn of Modern Physics", "Quantum Theory and Radiation (Photons)", "medium"),
    6: ("Dawn of Modern Physics", "Quantum Theory and Radiation (Photons)", "medium"),
    7: ("Dawn of Modern Physics", "Quantum Theory and Radiation (Photons)", "medium"),
    8: ("Dawn of Modern Physics", "Quantum Theory and Radiation (Photons)", "medium"),
    9: ("Dawn of Modern Physics", "Quantum Theory and Radiation (Photons)", "medium"),
    10: ("Dawn of Modern Physics", "Quantum Theory and Radiation (Photons)", "medium"),
    11: ("Nuclear Physics", "Spontaneous and Random Nuclear Decay", "high"),
    12: ("Nuclear Physics", "Spontaneous and Random Nuclear Decay", "high"),
    13: ("Nuclear Physics", "Half-life and Rate of Decay", "high"),
    14: ("Nuclear Physics", "Biological and Medical Uses of Radiation", "medium"),
    15: ("Nuclear Physics", "Spontaneous and Random Nuclear Decay", "high"),
    16: ("Nuclear Physics", "Biological and Medical Uses of Radiation", "high"),
    17: ("Nuclear Physics", "Spontaneous and Random Nuclear Decay", "high"),
    18: ("Electrostatics", "Unit of Potential", "low"),   # no "units/dimensions" chapter in vocab
    19: ("Work and Energy", "Energy", "low"),              # OCR-corrupted anyway (inactive); no units/dimensions chapter
    20: ("Rotational and Circular Motion", "Relation Between Angular and Linear Quantities", "medium"),
    21: ("Force and Motion", "Newton''s Second Law and Linear Momentum", "high"),
    22: ("Fluid Dynamics", "Fluid Drag", "high"),
    23: ("Fluid Dynamics", "Bernoulli''s Equation", "high"),
    24: ("Fluid Dynamics", "Bernoulli''s Equation", "high"),
    25: ("Waves", "Transverse vs Longitudinal Waves", "medium"),
    26: ("Waves", "Transverse vs Longitudinal Waves", "low"),   # polarization, no dedicated subtopic
    27: ("Waves", "Motion of Wave", "low"),                     # no Optics/fibre-optics chapter in vocab
    28: ("Waves", "Motion of Wave", "low"),                     # no Optics/lens chapter in vocab
    29: ("Waves", "Simple Harmonic Motion (SHM)", "medium"),    # also OCR-corrupted (inactive)
    30: ("Waves", "Simple Harmonic Motion (SHM)", "high"),
    31: ("Waves", "Simple Harmonic Motion (SHM)", "medium"),    # figure-only (inactive)
    32: ("Waves", "Characteristics of Waves", "low"),           # Doppler effect, OCR-corrupted (inactive)
    33: ("Force and Motion", "Stress and Strain", "high"),
    34: ("Force and Motion", "Stress and Strain", "high"),
    35: ("Thermodynamics", "Thermal Equilibrium and Heat", "low"),  # kinetic theory of gases not in vocab
    36: ("Thermodynamics", "Thermal Equilibrium and Heat", "low"),  # partly garbled/placeholder (inactive)
    37: ("Thermodynamics", "First Law of Thermodynamics", "high"),
    38: ("Thermodynamics", "First Law of Thermodynamics", "low"),   # 2nd-law/heat-engine efficiency, no dedicated subtopic
    39: ("Thermodynamics", "First Law of Thermodynamics", "high"),
    40: ("Electronics", "PN Junction (Forward and Reverse Bias)", "low"),  # digital logic gates not in vocab (inactive)
    41: ("Electronics", "Rectification (Half and Full Wave)", "low"),      # CRO/time-base, no dedicated subtopic
    42: ("Electrostatics", "Charging and Discharging of Capacitor", "high"),
    43: ("Electrostatics", "Charging and Discharging of Capacitor", "high"),
    44: ("Electronics", "PN Junction (Forward and Reverse Bias)", "medium"),  # figure-only (inactive)

    # ---- CHEMISTRY (45-102) ----
    45: ("Carboxylic Acids", "Conversion to Derivatives (Acyl Halides, Anhydrides, Esters)", "high"),
    46: ("Carboxylic Acids", "Conversion to Derivatives (Acyl Halides, Anhydrides, Esters)", "medium"),
    47: ("Macromolecules", "Classification and Structure of Proteins", "medium"),
    48: ("Macromolecules", "Classification and Structure of Proteins", "medium"),
    49: ("Macromolecules", "Classification and Structure of Proteins", "medium"),
    50: ("Macromolecules", "Classification and Structure of Proteins", "medium"),
    51: ("Macromolecules", "Classification and Structure of Proteins", "medium"),
    52: ("Macromolecules", "Classification and Structure of Proteins", "high"),
    53: ("Macromolecules", "Classification and Structure of Proteins", "low"),  # carbohydrates chapter not in Chemistry vocab
    54: ("Macromolecules", "Classification and Structure of Proteins", "low"),
    55: ("Carboxylic Acids", "Conversion to Derivatives (Acyl Halides, Anhydrides, Esters)", "low"),  # saponification, no dedicated subtopic
    56: ("Industrial Chemistry", "Polymers (Condensation and Addition)", "high"),
    57: ("Macromolecules", "Classification and Structure of Proteins", "low"),
    58: ("Industrial Chemistry", "Polymers (Condensation and Addition)", "high"),
    59: ("Reaction Kinetics", "Factors Affecting Rate of Reaction", "low"),  # environmental/atmospheric chemistry not in vocab
    60: ("s and p Block Elements", "Group II Reactions", "low"),            # environmental/heavy-metal toxicity not in vocab
    61: ("Fundamental Concepts of Chemistry", "Moles and Avogadro''s Number", "high"),
    62: ("Fundamental Concepts of Chemistry", "Limiting and Excess Reactants", "high"),
    63: ("Fundamental Concepts of Chemistry", "Moles and Avogadro''s Number", "high"),
    64: ("Liquids", "Hydrogen Bonding", "high"),
    65: ("Atomic Structure", "Electronic Configuration", "high"),
    66: ("Atomic Structure", "Shapes of Orbitals", "high"),
    67: ("Chemical Bonding", "Hybridization", "high"),
    68: ("Chemical Bonding", "Ionic Character of Covalent Bond", "medium"),
    69: ("Thermochemistry and Energetics", "Exothermic and Endothermic Reactions", "high"),
    70: ("Solids", "Lattice Energy", "high"),
    71: ("Liquids", "Evaporation, Boiling Point, Vapor Pressure", "low"),  # colligative properties, no dedicated subtopic
    72: ("Liquids", "Evaporation, Boiling Point, Vapor Pressure", "high"),
    73: ("Electrochemistry", "Redox Reactions", "high"),
    74: ("Electrochemistry", "Oxidation and Reduction", "high"),
    75: ("Chemical Equilibrium", "Le Chatelier''s Principle", "high"),
    76: ("Chemical Equilibrium", "Buffer Solutions", "high"),
    77: ("Reaction Kinetics", "Factors Affecting Rate of Reaction", "low"),  # autocatalysis, no dedicated subtopic
    78: ("Reaction Kinetics", "Rate of Reaction and Rate Equation", "high"),
    79: ("s and p Block Elements", "Periodic Trends (Radii, IE, EA, Electronegativity)", "high"),
    80: ("s and p Block Elements", "Periodic Trends (Radii, IE, EA, Electronegativity)", "high"),
    81: ("s and p Block Elements", "Group II Reactions", "medium"),
    82: ("Fundamental Principles of Organic Chemistry", "Definition and Classification of Organic Compounds", "high"),
    83: ("Transition Elements", "Electronic Structure of d-block", "high"),
    84: ("Transition Elements", "Electronic Structure of d-block", "high"),
    85: ("Chemical Equilibrium", "Buffer Solutions", "low"),  # acid rain pH, no dedicated subtopic
    86: ("Chemical Equilibrium", "Haber''s Process", "low"),  # Contact Process, no dedicated subtopic
    87: ("Chemical Equilibrium", "Haber''s Process", "high"),
    88: ("Chemical Equilibrium", "Haber''s Process", "high"),
    89: ("Industrial Chemistry", "Polymers (Condensation and Addition)", "high"),
    90: ("Chemistry of Hydrocarbons", "Free Radical Mechanism", "medium"),
    91: ("Chemistry of Hydrocarbons", "Reactivity of Benzene", "medium"),
    92: ("Alkyl Halides", "Nucleophilic Substitution Mechanisms", "high"),
    93: ("Chemistry of Hydrocarbons", "Structure and Reactivity of Alkenes", "medium"),
    94: ("Alkyl Halides", "Nucleophilic Substitution Mechanisms", "high"),
    95: ("Alcohols and Phenols", "Chemistry of Alcohols (Ethers, Esters)", "high"),
    96: ("Alcohols and Phenols", "Nomenclature, Structure, Reactivity of Alcohols", "high"),
    97: ("Alcohols and Phenols", "Nomenclature, Structure, Reactivity of Alcohols", "medium"),
    98: ("Carboxylic Acids", "Conversion to Derivatives (Acyl Halides, Anhydrides, Esters)", "medium"),
    99: ("Aldehydes and Ketones", "Preparation", "high"),
    100: ("Aldehydes and Ketones", "Nucleophilic Addition Reactions", "medium"),
    101: ("Aldehydes and Ketones", "Reactivity of Aldehydes and Ketones", "medium"),
    102: ("Aldehydes and Ketones", "Oxidation Reactions", "medium"),

    # ---- ENGLISH (103-132) ----
    103: ("Formal and Lexical Aspect of Language", "Contextual Vocabulary", "high"),
    104: ("Formal and Lexical Aspect of Language", "Contextual Vocabulary", "high"),
    105: ("Formal and Lexical Aspect of Language", "Contextual Vocabulary", "high"),
    106: ("Formal and Lexical Aspect of Language", "Contextual Vocabulary", "high"),
    107: ("Writing Skills", "Proofreading and Editing", "low"),   # segments lost to OCR (inactive)
    108: ("Writing Skills", "Proofreading and Editing", "low"),
    109: ("Writing Skills", "Proofreading and Editing", "low"),
    110: ("Writing Skills", "Proofreading and Editing", "low"),
    111: ("Writing Skills", "Proofreading and Editing", "low"),
    112: ("Writing Skills", "Proofreading and Editing", "low"),
    113: ("Formal and Lexical Aspect of Language", "Tenses", "medium"),
    114: ("Formal and Lexical Aspect of Language", "Prepositions", "high"),
    115: ("Formal and Lexical Aspect of Language", "Sentence Structure and Phrase Analysis", "medium"),
    116: ("Writing Skills", "Subject-Verb Agreement", "high"),
    117: ("Formal and Lexical Aspect of Language", "Sentence Structure and Phrase Analysis", "low"),  # article a/an, no dedicated subtopic
    118: ("Writing Skills", "Subject-Verb Agreement", "high"),
    119: ("Formal and Lexical Aspect of Language", "Prepositions", "high"),
    120: ("Formal and Lexical Aspect of Language", "Contextual Vocabulary", "medium"),
    121: ("Formal and Lexical Aspect of Language", "Contextual Vocabulary", "medium"),
    122: ("Formal and Lexical Aspect of Language", "Tenses", "high"),
    123: ("Formal and Lexical Aspect of Language", "Synonyms (Irony, Parody, Satire)", "medium"),
    124: ("Formal and Lexical Aspect of Language", "Synonyms (Irony, Parody, Satire)", "medium"),
    125: ("Formal and Lexical Aspect of Language", "Synonyms (Irony, Parody, Satire)", "medium"),
    126: ("Formal and Lexical Aspect of Language", "Synonyms (Irony, Parody, Satire)", "medium"),
    127: ("Formal and Lexical Aspect of Language", "Synonyms (Irony, Parody, Satire)", "medium"),
    128: ("Formal and Lexical Aspect of Language", "Synonyms (Irony, Parody, Satire)", "medium"),
    129: ("Formal and Lexical Aspect of Language", "Synonyms (Irony, Parody, Satire)", "medium"),
    130: ("Formal and Lexical Aspect of Language", "Synonyms (Irony, Parody, Satire)", "medium"),
    131: ("Formal and Lexical Aspect of Language", "Synonyms (Irony, Parody, Satire)", "medium"),
    132: ("Formal and Lexical Aspect of Language", "Synonyms (Irony, Parody, Satire)", "medium"),

    # ---- BIOLOGY (133-220) ----
    133: ("Coordination and Control", "Neurons", "high"),
    134: ("Coordination and Control", "Neurons", "medium"),
    135: ("Coordination and Control", "Brain", "high"),
    136: ("Reproduction", "Sexually Transmitted Diseases", "high"),
    137: ("Reproduction", "Human Reproductive System", "high"),
    138: ("Reproduction", "Human Reproductive System", "high"),
    139: ("Reproduction", "Human Reproductive System", "high"),
    140: ("Reproduction", "Human Reproductive System", "high"),
    141: ("Support and Movement", "Skeletal Muscle Ultra-structure", "high"),
    142: ("Support and Movement", "Muscle Contraction", "high"),
    143: ("Support and Movement", "Human Skeleton (Cartilage, Muscle, Bone)", "high"),
    144: ("Support and Movement", "Human Skeleton (Cartilage, Muscle, Bone)", "high"),
    145: ("Support and Movement", "Human Skeleton (Cartilage, Muscle, Bone)", "high"),
    146: ("Coordination and Control", "Receptors", "low"),   # no endocrine-system chapter in vocab
    147: ("Digestion", "Human Digestive System", "low"),
    148: ("Digestion", "Human Digestive System", "low"),     # inactive (unresolved key)
    149: ("Coordination and Control", "Brain", "low"),
    150: ("Immunity", "Specific Defense Mechanism", "high"),
    151: ("Immunity", "Specific Defense Mechanism", "high"),
    152: ("Immunity", "Specific Defense Mechanism", "high"),
    153: ("Immunity", "Specific Defense Mechanism", "high"),
    154: ("Immunity", "Specific Defense Mechanism", "high"),
    155: ("Bioenergetics", "Respiration", "low"),  # photosynthesis, no dedicated chapter in vocab
    156: ("Bioenergetics", "Respiration", "high"),
    157: ("Bioenergetics", "Respiration", "high"),
    158: ("Bioenergetics", "Respiration", "high"),
    159: ("Bioenergetics", "Respiration", "high"),
    160: ("Biotechnology", "Biotechnology and Health Care", "high"),
    161: ("Biotechnology", "Biotechnology and Health Care", "high"),
    162: ("Biotechnology", "Biotechnology and Health Care", "high"),
    163: ("Biotechnology", "Biotechnology and Health Care", "high"),
    164: ("Immunity", "Specific Defense Mechanism", "medium"),
    165: ("Evolution", "Concept of Evolution", "low"),  # ecology chapter not in vocab
    166: ("Evolution", "Concept of Evolution", "low"),
    167: ("Evolution", "Concept of Evolution", "low"),
    168: ("Evolution", "Concept of Evolution", "low"),
    169: ("Evolution", "Concept of Evolution", "low"),
    170: ("Inheritance", "Mendel's Laws of Inheritance", "high"),
    171: ("Inheritance", "Mendel's Laws of Inheritance", "high"),
    172: ("Inheritance", "Mendel's Laws of Inheritance", "high"),
    173: ("Evolution", "Darwinism", "high"),
    174: ("Inheritance", "X-linked Recessive Inheritance", "medium"),
    175: ("Evolution", "Concept of Evolution", "low"),
    176: ("Cell Structure and Function", "Cell Structure (Animal vs Plant)", "low"),  # no tissue/organ-level chapter
    177: ("Evolution", "Concept of Evolution", "low"),
    178: ("Acellular Life", "Viruses", "low"),  # antibiotic-producing microbes, no bacteriology chapter in vocab
    179: ("Cell Structure and Function", "Cell Structure (Animal vs Plant)", "high"),
    180: ("Cell Structure and Function", "Cell Structure (Animal vs Plant)", "medium"),
    181: ("Cell Structure and Function", "Cytoplasmic Organelles", "high"),
    182: ("Cell Structure and Function", "Cytoplasmic Organelles", "high"),
    183: ("Cell Structure and Function", "Cytoplasmic Organelles", "high"),
    184: ("Inheritance", "Gene Linkage and Crossing Over", "high"),
    185: ("Inheritance", "X-linked Recessive Inheritance", "low"),  # Klinefelter's, no dedicated subtopic
    186: ("Cell Structure and Function", "Cytoplasmic Organelles", "medium"),
    187: ("Cell Structure and Function", "Chromosomes", "low"),  # cell-cycle phases, no dedicated subtopic
    188: ("Inheritance", "X-linked Recessive Inheritance", "low"),  # Down's syndrome, no dedicated subtopic
    189: ("Biological Molecules", "Carbohydrates", "high"),
    190: ("Biological Molecules", "Carbohydrates", "medium"),
    191: ("Biological Molecules", "Proteins", "high"),
    192: ("Biological Molecules", "Lipids", "high"),
    193: ("Biological Molecules", "Structure of DNA", "high"),
    194: ("Enzymes", "Enzyme Inhibitors", "high"),
    195: ("Enzymes", "Enzyme Inhibitors", "high"),
    196: ("Bioenergetics", "Respiration", "high"),
    197: ("Enzymes", "Characteristics of Enzymes", "medium"),
    198: ("Acellular Life", "AIDS and HIV Infection", "high"),
    199: ("Cell Structure and Function", "Prokaryotic and Eukaryotic Cell", "high"),
    200: ("Acellular Life", "Viruses", "low"),  # antibiotic resistance, no bacteriology chapter in vocab
    201: ("Cell Structure and Function", "Cell Structure (Animal vs Plant)", "low"),  # fungal cell wall, no mycology chapter
    202: ("Reproduction", "Human Reproductive System", "low"),  # plant reproduction, no chapter in vocab
    203: ("Evolution", "Concept of Evolution", "low"),  # invertebrate zoology, no chapter in vocab
    204: ("Evolution", "Concept of Evolution", "low"),
    205: ("Support and Movement", "Human Skeleton (Cartilage, Muscle, Bone)", "medium"),
    206: ("Evolution", "Concept of Evolution", "low"),
    207: ("Digestion", "Human Digestive System", "high"),
    208: ("Digestion", "Human Digestive System", "high"),
    209: ("Digestion", "Human Digestive System", "high"),
    210: ("Digestion", "Human Digestive System", "high"),
    211: ("Circulation", "Blood Vessels (Arteries, Veins, Capillaries)", "low"),  # blood-cell biology, no dedicated subtopic
    212: ("Circulation", "Blood Vessels (Arteries, Veins, Capillaries)", "low"),
    213: ("Circulation", "Human Heart", "medium"),
    214: ("Respiration", "Human Respiratory System", "high"),
    215: ("Homeostasis", "Glomerular Filtration and Reabsorption", "high"),
    216: ("Homeostasis", "Thermoregulation", "low"),  # generic feedback-mechanism concept
    217: ("Homeostasis", "Thermoregulation", "low"),
    218: ("Homeostasis", "Glomerular Filtration and Reabsorption", "high"),
    219: ("Homeostasis", "Glomerular Filtration and Reabsorption", "high"),
    220: ("Coordination and Control", "Brain", "high"),
}

path = "mdcat-content/parsed-mcqs/MDCAT_2012.json"
mcqs = json.load(open(path, encoding="utf-8"))

missing = []
low_conf = 0
for mcq in mcqs:
    qn = mcq["question_number"]
    if qn not in TAGS:
        missing.append(qn)
        continue
    topic, subtopic, confidence = TAGS[qn]
    mcq["topic"] = topic
    mcq["subtopic"] = subtopic
    mcq["tag_confidence"] = confidence
    if confidence == "low":
        mcq["needs_review"] = True
        low_conf += 1

print("missing tags for:", missing)
print("total tagged:", len(mcqs) - len(missing))
print("low-confidence (forced, vocab gap):", low_conf)

with open(path, "w", encoding="utf-8") as f:
    json.dump(mcqs, f, indent=2, ensure_ascii=False)
print("wrote", path)
