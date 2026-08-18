# -*- coding: utf-8 -*-
# Transcribed from UHS MDCAT 2016 "Entrance Test" paper
# Source: uploaded compilation "MDCAT_Past_Papers__2008-2016__Solved.pdf"
# (contains Entrance Test papers 2008-2016 back to back; this script covers
# ONLY the 2016 paper, extracted from that compilation without transcribing
# the other years).
# Total MCQs: 220, Time Allowed: 150 Minutes
# Question Paper colour for this ID: Pink (candidates were told to fill 'C'
# against 'ID' on the response form, and the paper itself states
# "Colour of your Question Paper is Pink.")
#
# NUMBERING NOTE:
# Unlike the 2017 compilation (which numbered each subject 1..N separately
# and needed renumbering), this 2016 paper already uses ONE continuous
# numbering scheme 1-220 across all four subjects in the printed source:
#   Physics    Q.1   - Q.44
#   Chemistry  Q.45  - Q.102
#   English    Q.103 - Q.132
#   Biology    Q.133 - Q.220
# So QUESTIONS below keeps that same continuous numbering as printed,
# no renumbering was required.
#
# NOTE ON DIAGRAM / GRAPH / STRUCTURE MCQs:
# Several MCQs depend on a figure, graph, circuit, or chemical structure
# drawing in the original scanned pages that could not be reliably
# transcribed as text. These are listed in DIAGRAM_MCQS below with a
# needs_review flag. The official answer key still provides a letter for
# every one of these, and that letter is kept in KEY_RAW, but the
# image-only part of the question/options has been noted with
# DIAGRAM_PLACEHOLDER and should be checked against the original PDF page
# before use.
DIAGRAM_PLACEHOLDER = "[Diagram/graph/structure required \u2014 not transcribable from OCR text. See original PDF page for the figure.]"

DIAGRAM_MCQS = {
    1: {
        "subject": "PHYSICS", "orig_num": 1,
        "notes": "All four options (A-D) are Intensity-vs-Wavelength graphs for X-ray output shown only as images, with no text distinguishing them. Needs figure to confirm answer (a).",
    },
    32: {
        "subject": "PHYSICS", "orig_num": 32,
        "notes": "Circuit diagram of four 5-ohm resistors between points A and B. Needs figure to confirm answer (d, 6.6 Ohms).",
    },
    53: {
        "subject": "CHEMISTRY", "orig_num": 53,
        "notes": "Question stem is entirely a molecule structure image (\"Choose the right molecule\") with no text description at all. Needs figure to confirm answer (d, NH3).",
    },
    54: {
        "subject": "CHEMISTRY", "orig_num": 54,
        "notes": "Structural formula of a polyester repeat unit shown as an image; partially reconstructable from OCR (two C=O groups linked via O-CH2-CH2-O, repeating unit 'n'). Needs figure to confirm answer (d, Polyester).",
    },
    64: {
        "subject": "CHEMISTRY", "orig_num": 64,
        "notes": "Structure of a small hydrocarbon (appears to be ethylene, H2C=CH2) shown as an image for counting sigma/pi bonds. Needs figure to confirm answer (a, 1\u03c0 and 5\u03c3 bonds).",
    },
    69: {
        "subject": "CHEMISTRY", "orig_num": 69,
        "notes": "Diagram of a galvanic cell (Cu electrode in 1M CuSO4, H2 electrode in 1M HCl, joined by a porous partition). Text labels were partially recovered but the full circuit layout is image-only. Needs figure to confirm answer (a).",
    },
    86: {
        "subject": "CHEMISTRY", "orig_num": 86,
        "notes": "Skeletal (line-angle) formula of a hydrocarbon shown only as an image, to be IUPAC-named. Needs figure to confirm answer (b, 3,4-dimethyl-3-hexene).",
    },
    92: {
        "subject": "CHEMISTRY", "orig_num": 92,
        "notes": "Structure of an alcohol (partially recovered as a branched carbon skeleton ending in -OH) shown as an image, to classify as primary/secondary/tertiary. Needs figure to confirm answer (c, Tertiary).",
    },
    93: {
        "subject": "CHEMISTRY", "orig_num": 93,
        "notes": "Four brominated-phenol product structures (options A-D) shown as images. Needs figure to confirm answer (c).",
    },
    94: {
        "subject": "CHEMISTRY", "orig_num": 94,
        "notes": "Structure of a nitro-substituted phenol (positions of three -NO2 groups shown only as an image) to be named. Needs figure to confirm answer (d, Picric acid).",
    },
    95: {
        "subject": "CHEMISTRY", "orig_num": 95,
        "notes": "Structure of a hydrazone/hydrazine derivative (partially recovered: a C=N-NH- linkage to a dinitro-substituted ring) shown as an image. Needs figure to confirm answer (d, 2,4-Dinitrophenyl hydrazone).",
    },
    164: {
        "subject": "BIOLOGY", "orig_num": 164,
        "notes": "Four Haworth/ring-structure drawings (options A-D) of D-glucose shown as images. Needs figure to confirm answer (a).",
    },
    169: {
        "subject": "BIOLOGY", "orig_num": 169,
        "notes": "Diagram showing an inhibitor binding an enzyme away from the substrate/active site. Needs figure to confirm answer (b, Competitive) \u2014 note the layout as OCR'd (inhibitor not at the substrate site) would suggest non-competitive, so this should be re-checked against the original figure.",
    },
    171: {
        "subject": "BIOLOGY", "orig_num": 171,
        "notes": "Four Rate-of-Reaction-vs-pH graphs (options A-D) for pepsin activity, shown as images. Needs figure to confirm answer (d).",
    },
}

# ---------------------------------------------------------------------------
# REDACTED / ILLEGIBLE QUESTION
# The last Chemistry/Biology-range question in the source scan (Q.220) is
# rendered only as a row of capital "X" characters on the page - the
# question text and options were not printed/legible in the compiled PDF.
# The official answer key also marks it as "X" (no answer given),
# consistent with this being a blank filler row or an omitted/cancelled
# question in the source compilation. It is kept as a placeholder entry
# below with is_active=False so the total question count still reflects
# the paper's stated 220 MCQs; recommend excluding it from any scored
# import.
REDACTED_MCQS = {
    220: {"subject": "BIOLOGY", "orig_num": 220, "is_active": False},
}

REDACTED_PLACEHOLDER = "[Question illegible/blank in source scan - printed only as a row of 'X' characters. No official answer given.]"

SUBJECTS = [
    ("PHYSICS", 1, 44),
    ("CHEMISTRY", 45, 102),
    ("ENGLISH", 103, 132),
    ("BIOLOGY", 133, 220),
]

QUESTIONS = {
# ----------------------------- PHYSICS (1-44) -----------------------------
1: ("Which of the following graph represents the output of an X-ray? " + DIAGRAM_PLACEHOLDER, ["Graph A","Graph B","Graph C","Graph D"]),
2: ("The continuous spectrum of X-ray is formed due to:", ["Characteristics of X-rays","Bremsstrahlung X-ray","Soft X-ray","Hard X-ray"]),
3: ("Wavelength of \u03b3-rays is:", ["Equal to the X-rays","Longer to the X-rays","Shorter to the X-rays","Boarder to the X-rays"]),
4: ("Thorium is transformed after the transmission of \u03b2-particle into:", ["Bismuth","Protactinium","Polonium","Palladium"]),
5: ("Emission of \u03b3-rays from radioactive element results into:", ["Bismuth","Protactinium","Polonium","Palladium"]),
6: ("The relation between decay constant '\u03bb' and half-life 'T\u00bd' of radioactive substance is:", ["\u03bb = 1/T\u00bd","\u03bb = 0.693 T\u00bd","\u03bb = T\u00bd","\u03bb = 0.693/T\u00bd"]),
7: ("Radioisotope which is used to combat cancer of thyroid gland is:", ["Iodine-131","Phosphorous-32","Strontium-90","Cobalt-60"]),
8: ("Sodium-24 is used for:", ["Sterilization","Study of circulation of blood","Skin Cancer","Thyroid Cancer"]),
9: ("Energy radiation absorbed at the rate of one joule per kilogram is called:", ["1 Rad","1 Sievert","1 Yellow","1 Gray"]),
10: ("The time period 'T' of a simple pendulum depends on its length 'l' and acceleration due to gravity 'g' using unit dimension. The correct equation for time period is:", ["T = k\u221a(g/l) where 'k' is constant","T = (1/k)\u221a(g/l) where 'k' is constant","T = k\u221a(l/g) where 'k' is constant","T = (1/k)\u221a(l/g) where 'k' is constant"]),
11: ("The unit for electric charge is Coulomb and one Coulomb in terms of base unit is equivalent to:", ["Am","Js-1","As","C"]),
12: ("A man in elevator ascending with an acceleration will conclude that his weight is:", ["Increased","Decreased","Reduced to zero","Remain Constant"]),
13: ("If we double the moment arm the value of torque becomes:", ["Half","Three-times","Two-times","Four-times"]),
14: ("When fluid is incompressible, the quantity is constant is:", ["Mass","Density","Pressure","Force"]),
15: ("The minimum distance from the eye at which an object appears to be distant is:", ["25 cm","22 cm","35 cm","20 cm"]),
16: ("Using the relation for the magnifying power Lo, M = 1 + d/f, if f = 5 cm and d = 25 cm then M will be:", ["5","7","6","8"]),
17: ("Resonance occurs when the driving frequency is:", ["Greater than natural frequency","Unequal the natural frequency","Less than natural frequency","Equal to the natural frequency"]),
18: ("The red shift measurement of Doppler effect of galaxies indicate that the universe is:", ["Expanding","Contracting","Stationary","Oscillating"]),
19: ("Frequency audible range to human hearing lies in the range:", ["2-2000 kHz","15-50000 kHz","20-20000 Hz","20-20000 kHz"]),
20: ("Tuning a radio is a best example of:", ["Natural resonance","Mechanical resonance","Free resonance","Electrical resonance"]),
21: ("The ratio of applied stress to the volumetric strain is called:", ["Bulk Modulus","Shear Modulus","Tensile modulus","Young's Modulus"]),
22: ("The wire made of copper belong to which specific kind of material:", ["Ductile material","Tough material","Brittle material","Deformed material"]),
23: ("The relation R/NA = 1.38 x 10^-25 JK-1 in a gas law is known as:", ["Avogadro's constant","Charles constant","Newton's constant","Boltzmann's constant"]),
24: ("The relation 'PV = nRT' shows which law of physics:", ["Charles Law","Avogadro's Law","Newton's Constant","Ideal Gas Law"]),
25: ("The rapid escape of air from a burst tyre is an example of:", ["Adiabatic processes","Isothermal process","Cooling process","First law of thermodynamics"]),
26: ("Which relation exactly described the isothermal process?", ["Q = W","W = \u2212\u0394U","Q = \u2212\u0394U","Q = \u0394U + W"]),
27: ("If a turbine is working as a heat engine and takes that from hot body (427\u00b0C) and exhausts into a body at 77\u00b0C then what is the possible efficiency?", ["50%","70%","90%","95%"]),
28: ("Which one of the following is the Boolean expression of NAND gate?", ["X = A.B","X = A+B","X = (A.B)'","X = (A+B)'"]),
29: ("Which one of the following is the truth table of NAND gate? " + DIAGRAM_PLACEHOLDER + " (four A/B/Y truth tables shown, values partially recovered: A) 0,0->1; 0,1->0; 1,0->0; 1,1->0 | B) 0,0->1; 0,1->1; 1,0->1; 1,1->0 | C) 0,0->1; 1,1->0 | D) 0,0->0; 1,1->1)", ["Truth table A","Truth table B","Truth table C","Truth table D"]),
30: ("If the length, width and separation between the plates of a parallel plate capacitor is doubled then its capacitance becomes:", ["Double","Half","Four-times","Eight-times"]),
31: ("Resistance between two opposite faces of square thin film of area 1 mm2 having thickness of 1 \u03bcm if resistivity of material is 10^-6 \u03a9 will be:", ["1000 \u03a9","100 \u03a9","1 \u03a9","10 \u03a9"]),
32: ("Total resistance between 'A' and 'B' in the given circuit is: " + DIAGRAM_PLACEHOLDER + " (four 5\u03a9 resistors arranged between points A and B)", ["5.6 \u03a9","3.33 \u03a9","0.33 \u03a9","6.6 \u03a9"]),
33: ("'F' is maximum force acting on a conductor. Now if we change the direction of conductor by making an angle of 45\u00b0 with the magnetic field then the force becomes:", ["F/2","2F","F/\u221a2","\u221a2 F"]),
34: ("If we doubled all the parameters of the force acting on current carrying conductor and \u03b8 = 90\u00b0 then magnetic force becomes:", ["Half","Double","Eight-times","Four-times"]),
35: ("The force acting on current carrying conductor will be maximum if the angle between magnetic field and conductor is:", ["0\u00b0","30\u00b0","90\u00b0","60\u00b0"]),
36: ("The shadow of the bones in X-rays photographic film appears lighter than the surrounding flesh due to:", ["Bones reflect greater amount of X-rays","Bones absorb less amount of X-rays","Bones absorb greater amount of X-rays","Bones totally reflect X-rays"]),
37: ("The atom is excited to an energy level Ei from its ground state energy level Eo, the wavelength of the radiations emitted is:", ["\u03bb = (Eo\u2212Ei)/hc","\u03bb = (Ei\u2212Eo)/hc","\u03bb = hc/(Ei\u2212Eo)","\u03bb = Ei/hc \u2212 Eo/hc"]),
38: ("Which one of the following gas is the lasing or active medium in the laser tube?", ["Hydrogen","Helium","Neon","Carbon dioxide"]),
39: ("The target of X-ray tube is made up of which metal?", ["Iron","Nickel","Brass","Tungsten"]),
40: ("The X-rays consists of:", ["High energy proton","High energy electrons","High energy \u03b3-rays","High energy photons"]),
41: ("In Bernoulli's equation the term \u00bd\u03c1v\u00b2 is called:", ["K.E. per unit volume","K.E.","K.E. per unit area","K.E. per unit length"]),
42: ("Potential energy per unit volume is given by:", ["mgh","mgh/\u03c1","gh","\u03c1gh"]),
43: ("If general equation for destructive interference is given by the relation, Optic path difference = (m + \u00bd)\u03bb where 'm' is an integer, then first dark fringe appears from 'm' will be equal to:", ["2/3","1/2","0","1"]),
44: ("For bright fringe formation, the path difference is:", ["(n + \u00bd)\u03bb where n = 0, 1, 2, \u2026","n\u03bb where n = 0, 1, 2, \u2026","(2n+1)\u03bb/2 where n = 0, 1, 2, \u2026","((n+1)/2)\u00b2\u03bb where n = 0, 1, 2, \u2026"]),

# ----------------------------- CHEMISTRY (45-102) -----------------------------
45: ("Which one of the following is structural formula of proline? " + DIAGRAM_PLACEHOLDER, ["Structure A","Structure B (a cyclic secondary amine ring with -COOH)","Structure C","Structure D"]),
46: ("In the formation of Zwitter ion which one of the following donates the proton?", ["COOH","NH2","CH2COO\u207b","OH\u207b"]),
47: ("HOOC-CH2-CH2-CH(NH2)-COOH: What is the name of above given structural formula?", ["Aspartic Acid","Asparagine","Adipic Acid","Glutamic Acid"]),
48: ("Which one of the following is simplest amino acid?", ["Lysine","Leucine","Alanine","Glycine"]),
49: ("Which one of the following polymer is called as Nylon 6,6?", ["Polyester","Polyvinyl chloride","Polyamide","Polyvinyl acetate"]),
50: ("Which one of the following is an exact composition of a carbohydrates?", ["Carbon and Hydrogen","Carbon and Oxygen","Carbon, Hydrogen and Oxygen","Hydrogen and Oxygen"]),
51: ("Which one of the following nitrogen base is NOT present in DNA?", ["Adenine","Guanine","Uracil","Cytosine"]),
52: ("In the woody parts of trees, the %age of cellulose is:", ["50%","10%","30%","100%"]),
53: ("Choose the right molecule. " + DIAGRAM_PLACEHOLDER, ["CH3","CO","H2O","NH3"]),
54: ("Structure shown is: [-C(=O)-C6H4-C(=O)-O-CH2-CH2-O-]n " + DIAGRAM_PLACEHOLDER + ". Indicate the name of above given structure.", ["Nylon 6,6","Adipic Acid","PVA","Polyester"]),
55: ("In laboratory experiment an unknown compound was added in test tube containing iodine, the colour became intense blue. What could be the unknown compound?", ["Cellulose","Raffinose","Ribose","Starch"]),
56: ("Ozone concentration is measured in:", ["Debye units","Dupont units","Debacle units","Dobson units"]),
57: ("The gas which is mainly produced in landfills from the waste is:", ["CH4","CO2","SO2","Cl2"]),
58: ("The substance for the separation of isotopes is firstly converted into the:", ["Neutral state","Free state","Vapour state","Charged state"]),
59: ("The number of moles of CO2 which contain 8.00 gm of oxygen is:", ["0.75","1.50","0.25","1.00"]),
60: ("London dispersion forces are the only forces present among the:", ["Molecules of H2O in liquid state","Molecules of HCl gas","Atoms of helium in gaseous state at high temperature","Molecules of solid chlorine"]),
61: ("Electrical conductivity of graphite is greater in one direction than in other due to:", ["Isomorphism","Cleavage plane","Anisotropy","Symmetry"]),
62: ("Number of neutrons in Zn-66 (atomic number 30) will be:", ["30","35","38","36"]),
63: ("The maximum number of electrons in electronic configuration can be calculated by using formula:", ["2l + 1","2n\u00b2 + 2","2n\u00b2","2n\u00b2 + 1"]),
64: ("Structure shown (ethylene, H2C=CH2). " + DIAGRAM_PLACEHOLDER + " Calculate the number of \u03c3 bonds and \u03c0 bonds in the molecule.", ["1\u03c0 and 5\u03c3 bonds","2\u03c0 and 4\u03c3 bonds","3\u03c0 and 3\u03c3 bonds","6\u03c0 and 6\u03c3 bonds"]),
65: ("\u00bdH2(g) \u2192 H(g), \u0394H = 218 kJmol-1. In this reaction, \u0394H will be called:", ["Enthalpy of atomization","Enthalpy of decomposition","Enthalpy of formation","Enthalpy of the dissociation"]),
66: ("Mg + \u00bdO2(g) \u2192 MgO(g) + -692 kJmol-1 at STP. Enthalpy of the above reaction will be called:", ["\u0394H\u00b0at","\u0394H\u00b0s","\u0394H\u00b0sol","\u0394H\u00b0f"]),
67: ("Freezing point will also be defined as that temperature at which its solid and liquid phases have the same:", ["Concentration","Ratio between the particles","Vapour pressure","Attraction between the phases"]),
68: ("What mass of NaOH is present in 0.5 mol of sodium hydroxide?", ["40 gm","2.5 gm","15 gm","20 gm"]),
69: ("The diagram shows a galvanic cell (Cu electrode in 1M CuSO4 solution, H2 electrode in 1M HCl solution, joined by a porous partition). " + DIAGRAM_PLACEHOLDER + " The current will flow from:", ["Hydrogen electrode to copper electrode","Copper electrode to hydrogen electrode","Hydrogen electrode to HCl solution","CuSO4 solution to hydrogen electrode"]),
70: ("Study the following redox reaction: 10Cl\u207b + 16H+ + 2MnO4\u207b \u2192 5Cl2 + 2Mn+2 + 8H2O", ["Manganese is oxidized from +7 to +2","Chlorine ions are reduced from -1 to zero","Chlorine is reduced from zero to -1","Manganese is reduced from +7 to +2"]),
71: ("Human blood maintains its pH between:", ["6.50 - 7.00","7.20 - 7.25","7.50 - 7.55","7.35 - 7.40"]),
72: ("Value of Ksp for PbSO4 system at 25\u00b0C is equal to:", ["1.6 x 10^-5 mol2dm-6","1.6 x 10^-6 mol2dm-6","1.6 x 10^-8 mol2dm-6","1.6 x 10^-7 mol2dm-6"]),
73: ("2A + B \u2192 Product. If the reactant 'B' is in excess, the order of reaction with respect to 'A' in given rate law, Rate = k[A]\u00b2[B] is:", ["2nd order reaction","1st order reaction","Pseudo 1st order reaction","3rd order reaction"]),
74: ("The rate constant 'k' is 0.693 min-1. The half-life for the 1st order reaction will be:", ["1 min","2 min","0.693 min","4 min"]),
75: ("Melting points of group II-A elements are higher than those of group I-A because:", ["Atoms of II-A elements have smaller size","II-A elements are more reactive","Atoms of II-A elements provide two binding electrons","I-A elements have smaller atomic radius"]),
76: ("The ionic radius of fluoride ion is:", ["72 pm","95 pm","136 pm","157 pm"]),
77: ("2NaOH(aq) + Cl2(g) \u2192 NaCl + NaClO + H2O proceed at:", ["500\u00b0C","200\u00b0C","-10\u00b0C","15\u00b0C"]),
78: ("Which halogen molecule 'X2' has lowest dissociation energy?", ["Cl2","Br2","I2","F2"]),
79: ("The anomalous electronic configuration shown by chromium and copper among 3-d series of elements is due to:", ["Colour of ions of these metals","Variable oxidation states of metals","Stability associated with this configuration","Complex formation tendency of metals"]),
80: ("Which element of 3d series of periodic table shows the electronic configuration of 3d6, 4s2?", ["Copper","Cobalt","Zinc","Nickel"]),
81: ("The %age of nitrogen in ammonium nitrate is:", ["46%","82%","33%","13%"]),
82: ("Which one of the following is anhydride of sulphuric acid?", ["Sulphur (II) oxide","Sulphur (VI) oxide","Iron pyrite","Sulphur (VI) oxide"]),
83: ("During contact process of H2SO4 synthesis, the following reaction occurs: 2SO2(g) + O2(g) \u21cc 2SO3(g), \u0394H = -96 kJmol-1. Which step is used to increase the yield of SO3?", ["Temperature is raised to very high degree","SO3 formed is removed very quickly","Both temperature and pressure are kept very low","An excess of air is used to drive the equilibrium to the right side"]),
84: ("Synthesis of ammonia by Haber's process is a reversible reaction: N2(g) + 3H2(g) \u21cc 2NH3(g), \u0394H = -92 kJmol-1. What should be done to increase the yield of ammonia?", ["Pressure should be decreased","Ammonia should remain in reaction mixture","Pressure should be increased","Concentration of nitrogen should be decreased"]),
85: ("Which one of the following reactions shows combustion of a saturated hydrocarbon?", ["C2H4 + 3O2 \u2192 2CO2 + 2H2O","CH4 + 2O2 \u2192 CO2 + 2H2O","CH4 + \u00bdO2 (Cu, 400\u00b0C, 200 atm) \u2192 CH3OH","C2H2 + 5/2 O2 \u2192 2CO2 + H2O"]),
86: ("Skeletal formula of an organic compound is given below (hydrocarbon). " + DIAGRAM_PLACEHOLDER + " IUPAC name of the compound is:", ["3,3-dimethyl-3-hexene","3,4-dimethyl-3-hexene","3-hexene","2,3-dimethyl-1-hexene"]),
87: ("Which one of the following pairs can be cis-trans isomer to each other?", ["CHCl=CCl2 and CH2=CH2","CHCl=CH2 and CH2=CHCl","CH3CH=CHCH3 and H3CCH=CHCH3","CH3CH3 and CH2=CH2"]),
88: ("Consider the reaction given below: CH3CH2Br --KOH/alcohol--> H2C=CH2 + HBr. Mechanism followed by the reaction is:", ["E2","E1","SN1","SN2"]),
89: ("The average bond energy of C-Br is:", ["228 kJmol-1","200 kJmol-1","250 kJmol-1","290 kJmol-1"]),
90: ("Which one of the following is NOT a nucleophile:", ["NH2\u207b","H2O","BF3","CH3\u207b"]),
91: ("Which one of the following is an appropriate indication of positive iodoform test?", ["Formation of H2O","Release of H2 gas","Brick red precipitate","Yellow crystal"]),
92: ("Structure of an alcohol (branched carbon skeleton ending in -OH). " + DIAGRAM_PLACEHOLDER + " Which one of the following is the proper classification of above formula:", ["Primary","Secondary","Tertiary","Polyhydride"]),
93: ("Which one of the following is an appropriate structure of product of bromination? " + DIAGRAM_PLACEHOLDER, ["Structure A","Structure B","Structure C","Structure D"]),
94: ("Structure of a nitro-substituted phenol (three -NO2 groups). " + DIAGRAM_PLACEHOLDER + " Which one of the following is an appropriate name of above compound?", ["1,3,6-Trinitrophenol","m-Nitrophenol","Tartaric acid","Picric acid"]),
95: ("Structure: (CH3)2C=N-NH-C6H3(NO2)2. " + DIAGRAM_PLACEHOLDER + " It is the general formula of:", ["2,4-Dinitrophenyl hydrazine","1,3-Dinitrophenyl hydrazone","Phenyl hydrazone","2,4-Dinitrophenyl hydrazone"]),
96: ("H-C(=O)-H: Which one of the following is the IUPAC name of above given structure:", ["Propionaldehyde","Methanone","Acetaldehyde","Methanal"]),
97: ("Which one of the following test is given by both aldehyde and ketone?", ["Silver mirror test","Fehling's solution test","2,4 DNPH test","Benedict's solution test"]),
98: ("CH3COOH + CH3CH2OH \u21cc CH3COOC2H5 + H2O. Which one of the following will act as a catalyst in above reaction?", ["HNO3","H2SO4","Acidified potassium dichromate","SOCl2"]),
99: ("CH3COOH + PCl5 \u2192 ? Which one of the following options shows the products of above reaction?", ["POCl2 + CH3COCl2 + HCl","POCl3 + CH3COCl2 + H2","CH3COCl + POCl2 + HCl","POCl3 + CH3COCl + HCl"]),
100: ("Which one of the following reaction of carboxylic acid is reversible?", ["Esterification","Salt formation","Reaction with PCl5","Reaction with SOCl2"]),
101: ("Structure: R-CH(NH3+)-COO\u207b. Select the best option indicating the name of the above structure:", ["Cation","Neutral amino acid","Internal salt","Anion"]),
102: ("When acid is added to an amino acid, which one of the following will act as a base?", ["NH3+","COO\u207b","H+","R group"]),

# ----------------------------- ENGLISH (103-132) -----------------------------
103: ("His theories have been __________ by recent research.", ["Pronounced","Rearmed","Dammed","Debunked"]),
104: ("International rules __________ the number of foreign entrants.", ["Hoodwink","Stipulate","Fabricate","Traverse"]),
105: ("The assassination of the president __________ the country into war.", ["Articulated","Boomed","Hobbled","Precipitated"]),
106: ("She might be forgiven for __________ beneath the pressure.", ["Undertaking","Extricating","Buckling","Resounding"]),
107: ("SPOT THE ERROR: It showed that (he was a man capable)[a] of (looking beneath the surface of things,)[b] a man not (dependent in)[c] paper manifestations.[d]", ["he was a man capable","looking beneath the surface of things,","dependent in","paper manifestations."]),
108: ("SPOT THE ERROR: When he was a child, (every time he were naughty,)[a] (his foster-mother used to threaten)[b] (to send him)[c] to Timbuktu.[d]", ["every time he were naughty,","his foster-mother used to threaten","to send him","to Timbuktu."]),
109: ("SPOT THE ERROR: I was faced with (alternatively of either evicting the books)[a] (or else leaving them)[b] (in sole, undisturbed tenancy)[c] and taking rooms elsewhere for myself.[d]", ["alternatively of either evicting the books","or else leaving them","in sole, undisturbed tenancy","and taking rooms elsewhere for myself."]),
110: ("SPOT THE ERROR: I remember (going to the British museum one day)[a] (to read for the treatment)[b] (for some slight ailment of which I had a touch-hay fever,)[c] I fancy it was.[d]", ["going to the British museum one day","to read for the treatment","for some slight ailment of which I had a touch-hay fever,","I fancy it was."]),
111: ("SPOT THE ERROR: (The number of people in the world are)[a] rapidly increasing (rather like a gigantic snowball)[b] (which not only gets bigger as it rolls)[c] but goes faster as well.[d]", ["The number of people in the world are","rapidly increasing rather like a gigantic snowball","which not only gets bigger as it rolls","but goes faster as well."]),
112: ("SPOT THE ERROR: It has been calculated that (unless the growth is checked,)[a] (there will only be enough room)[b] (on the earth)[c] for people to stand by.[d]", ["unless the growth is checked,","there will only be enough room","on the earth","for people to stand by."]),
113: ("Choose the CORRECT sentence:", ["Inside a carton was a push-button unit fastened with a small wooden box.","Inside a carton was a push-button unit fastened by a small wooden box.","Inside a carton was a push-button unit fastened to a small wooden box.","Inside a carton was a push-button unit fastened along a small wooden box."]),
114: ("Choose the CORRECT sentence:", ["They both looked to one another, startled by all they had just finished saying.","They both looked to each another, startled by all they had just finish saying.","They both looked to each another, startle by all they had just finish saying.","They both looked to each another, startled by all they had just finished saying."]),
115: ("Choose the CORRECT sentence:", ["The lovely sentiments we go through repeating!","The lovely sentiments we go about repeating!","The lovely sentiments we go in repeating!","The lovely sentiments we go for repeating!"]),
116: ("Choose the CORRECT sentence:", ["With the bright light, still in her eyes, she moved quick out of the door.","With the bright light, still in her eyes, she moved quick out to the door.","With the bright light, still in her eyes, she moved quickly out to the door.","With the bright light, still in her eyes, she moved quickly out of the door."]),
117: ("Choose the CORRECT sentence:", ["In a short while quiet a large crowd had been collected.","In a short while quite a large crowd had collected.","In a short while quite large crowd had collected.","In a short while quite the large crowd had been collecting."]),
118: ("Choose the CORRECT sentence:", ["She watched all the important matches in the Brookfield ground.","She watched all the important matches on the Brookfield ground.","She watched all the important matches from the Brookfield ground.","She watched all the important matches within the Brookfield ground."]),
119: ("Choose the CORRECT sentence:", ["Something had happened, something whose ultimate significance had yet to be reckon.","Something had happened, something whose ultimate significance had yet was reckon.","Something had happened, something whose ultimate significance had yet to be reckoned.","Something had happened, something whose ultimate significance had yet reckoned."]),
120: ("Choose the CORRECT sentence:", ["His faculties were all unimpairment, and he had no personal worries of any kind.","His faculties were all unimparing, and he had no personal worries of any kind.","His faculties were all unimpaired, and he had no personal worry of any kind.","His faculties were all unimpaired, and he had no personal worries of any kind."]),
121: ("Choose the CORRECT sentence:", ["It was hard to him to speak out loud, but he managed to murmur something.","It was hard on him to speak out loud, but he managed to murmur something.","It was hard for him to speak out loud, but he managed to murmur something.","It was hard upon him to speak out loud, but he managed to murmur something."]),
122: ("Choose the CORRECT sentence:", ["There was a little money saved up beside.","There was little money saved in besides.","There was little money saved up beside.","There was a little money saved up besides."]),
123: ("Select the NEAREST CORRECT MEANING: STALWART", ["Loyal","Lazy","Lacking strength","High"]),
124: ("Select the NEAREST CORRECT MEANING: CHIVALRY", ["Coward","Non-cooperative","Imitating","Gallant"]),
125: ("Select the NEAREST CORRECT MEANING: RAKISH", ["Curved","Traditional","Formal","Dashing"]),
126: ("Select the NEAREST CORRECT MEANING: PRODIGIOUS", ["Huge","Trivial","Little","Square"]),
127: ("Select the NEAREST CORRECT MEANING: IMPROVISE", ["Colophon","Concoct","Divert","Respite"]),
128: ("Select the NEAREST CORRECT MEANING: PARADOX", ["Anomaly","Prototype","Steward","Fashion"]),
129: ("Select the NEAREST CORRECT MEANING: MANIFESTATION", ["Mode","Token","Quirk","Bulwark"]),
130: ("Select the NEAREST CORRECT MEANING: RECONNOITRE", ["Patrol","Arcane","Exhort","Falter"]),
131: ("Select the NEAREST CORRECT MEANING: SOJOURN", ["Visit","Belch","Furry","Inking"]),
132: ("Select the NEAREST CORRECT MEANING: MUSE", ["Immaculate","Chew over","Sigh over","Vagary"]),

# ----------------------------- BIOLOGY (133-220) -----------------------------
133: ("Random, uncontrolled activity of some cells in the brain leading to chaotic activity in both sensory and motor nerves causes patients to see and hear different strange things.", ["Epilepsy","Parkinson's Disease","Alzheimer's Disease","Huntington's Disease"]),
134: ("Part of hind brain responsible for the balance and equilibrium of body is called:", ["Medulla","Cerebellum","Pons","Thalamus"]),
135: ("Events of menustral cycle are regulated by the:", ["Ethylene","Gonadotrophins","Auxins","Gibberellins"]),
136: ("Decrease of FSH and increase of estrogen cause pituitary gland to secrete:", ["Somatotropin","Luteinizing Hormone","Testosterone","Spermatogonium"]),
137: ("Transmission of Neisseria gonorrhea is best described by which one of the following?", ["Oro-fecal Route","Unsafe Sex","Vector Borne","Droplet Infection"]),
138: ("Syphilis is caused by:", ["Spirochete","Nostoc","Water blooms","Cyanobacteria"]),
139: ("AIDS is caused by:", ["Bacteria","Virus","Fungi","Alga"]),
140: ("Brain is protected and enclosed in:", ["Lumbar vertebrae","Coccyx","Vertebral column","Cranium"]),
141: ("Longest bone in the human skeleton is:", ["Ulna","Fibula","Tibia","Femur"]),
142: ("Hips and shoulder joints are examples of:", ["Hinge Joints","Ball and Socket Joints","Synovial Joints","Cartilaginous Joints"]),
143: ("In pelvic region of human body, sacrum is formed by the fusion of:", ["4 Vertebrae","5 Vertebrae","6 Vertebrae","3 Vertebrae"]),
144: ("Each muscle fibre is surrounded by a modified cell membrane called:", ["Sarcolemma","Sarcomere","Myosin Filament","Myofilament"]),
145: ("__________ hormone is antagonistic to insulin and causes increase in blood glucose level.", ["Glucagon","Nor-epinephrine","Calcitonin","Thyroxine"]),
146: ("Beta cells of islets of Langerhans produce _________ hormone.", ["Glucagon","Insulin","Pancreatic Juice","Parathormone"]),
147: ("The central portion of adrenal gland (Adrenal Medulla) produces ________ hormone.", ["Aldosterone","Epinephrine","Androgen","Corticosterone"]),
148: ("__________ hormones are called fight and flight hormones as they prepare an organism to face stressful situation.", ["Adrenaline, Aldosterone","Epinephrine, Nor-epinephrine","Cortisone, Oxytocin","Thyroxine, Nor-epinephrine"]),
149: ("B-cells release antibodies in blood plasma, tissue fluid and lymph. This kind of immune response is called:", ["Cell Mediated Response","Humoral Response","Active Response","Compound Response"]),
150: ("The type of immunity in which antibodies are passed from one individual to another is called:", ["Passive Immunity","Artificial Active Immunity","Natural Active Immunity","Humoral Immunity"]),
151: ("To combat the active infections of tetanus, rabies and snakes the _______ method of immunization is used:", ["Active","Humoral","Active Artificial","Passive"]),
152: ("In antibody molecule, two heavy and two light chains are bonded by:", ["Disulphide Bond","Monosulphide Bond","Hydrogen Bond","Ionic Bond"]),
153: ("Variable amino acid sequences in antibody molecule are found in ________.", ["Both light chains only","Both heavy chains only","One heavy and one light chain","Both heavy and light chains"]),
154: ("Each ________ consists of a light gathering antenna complex and reaction center.", ["Chlorophyll","Photosystem","Photon","Electron"]),
155: ("Photosystem I has chlorophyll a molecules which absorb maximum light of:", ["680 nm","780 nm","700 nm","580 nm"]),
156: ("Cyclic flow or C4 photosynthesis produces:", ["ATP and CO2","ATP","Only CO2","Only Oxygen"]),
157: ("Immediate product formed after CO2 fixation in Calvin Cycle is:", ["Unstable 6-carbon compound","Unstable 5-carbon compound","Unstable 4-carbon compound","Unstable 3-carbon compound"]),
158: ("Functional group of chlorophyll a is:", ["\u2014CH3","\u2014CHO","\u2014COOH","\u2014OH"]),
159: ("The modified plasmid or phage DNA is called:", ["Clone DNA","Recombinant DNA","cDNA","rDNA"]),
160: ("The rapid exchange of materials through carrier proteins across the plasma membrane is called:", ["Passive Diffusion","Active Transport","Endocytosis","Facilitated Diffusion"]),
161: ("The inner membrane of mitochondria form extensive infoldings called:", ["Cristae","Cisternae","Lamella","Bifidae"]),
162: ("Which one of the following organelle is found in both prokaryotic and eukaryotic cells?", ["Centriole","Endoplasmic Reticulum","Nucleus","Ribosome"]),
163: ("The compounds which on hydrolysis yield polyhydroxy aldehyde or ketone subunits are:", ["Lipids","Proteins","Polynucleotides","Carbohydrates"]),
164: ("Which one of the following is the formula structure of D (\u03b1) glucose? " + DIAGRAM_PLACEHOLDER, ["Structure A","Structure B","Structure C","Structure D"]),
165: ("Secondary structure of protein is found in:", ["Trypsin","Keratin","Insulin","Glucagon"]),
166: ("Waxes are formed by combination of fatty acids with:", ["Alcohol","Glycerol","Serine","Cysteine"]),
167: ("Phosphodiester bond is:", ["P\u2014O\u2014C\u2014P\u2014O\u2014C","C\u2014O\u2014P","C\u2014O\u2014P\u2014O\u2014C","C\u2014C\u2014O\u2014P"]),
168: ("An enzyme required Mg++ to catalyze the substrate. The Mg++ is best identified as:", ["Prosthetic group","Activator","Co-enzyme","Inhibitor"]),
169: ("Diagram shows an inhibitor bound to an enzyme, not at the substrate's binding site. " + DIAGRAM_PLACEHOLDER + " This figure represents _________ inhibitor.", ["Non-competitive","Competitive","Irreversible","Isosteric"]),
170: ("According to _________ model the active site of enzyme is modified as the substrate interacts with enzyme.", ["Induced fit","Lock and Key","Emil Fischer","Fluid Mosaic"]),
171: ("Which one of the following graphs shows how the rate of reaction of pepsin is affected by pH? " + DIAGRAM_PLACEHOLDER, ["Graph A","Graph B","Graph C","Graph D"]),
172: ("All viruses can reproduce within living organisms only, so they are known as:", ["Ectoparasites","Endoparasites","Obligative Intracellular Parasites","Facultative Intracellular Parasites"]),
173: ("Many bacteria are motile due to presence of:", ["Flagella","Pilli","Cilia","Microtubules"]),
174: ("_________ is an invagination of cell membrane which helps in cell division.", ["Fimbriae","Nucleoid","Mesosome","Endospore"]),
175: ("_________ is the yeast that grows in the mucous membrane of mouth or vagina.", ["Candida albicans","Saccharomyces cerevisiae","Aspergillus fumigatus","Aspergillus flavus"]),
176: ("Taenia is an endoparasite of human, pig and cattle which belongs to phylum.", ["Cnidaria","Aschelminthes","Annelida","Platyhelminthes"]),
177: ("Body of _________ consists of segments called proglottis which contains mainly sex organs.", ["Planaria","Ascaris","Fasciola","Tapeworm"]),
178: ("__________ is a common parasite of the intestine of human and pig which belongs to phylum nematode.", ["Taenia solanum","Schistosoma","Ascaris lumbriocoides","Fasciola hepatica"]),
179: ("In radial symmetry all body parts are arranged around the central axis. Radial symmetry represents __________ mode of life.", ["Sessile","Streamlined","Active","Parasitic"]),
180: ("Pseudo-coelomates have a body cavity but it is not true coelom. Which one of the following is included in the group.", ["Planaria","Tapeworm","Earthworm","Ascaris"]),
181: ("Digestion of __________ starts in oral cavity due to the action of enzyme present in saliva.", ["Starch","Cellulose","Fatty Acids","Polypeptides"]),
182: ("Food enters from stomach into small intestine through:", ["Pyloric Sphincter","Cardiac Sphincter","Semilunar valve","Diaphragm"]),
183: ("___________ are the part of a gastric gland which produce hydrochloric acid.", ["Parietal Cells","Goblet Cells","Chief Cells","Zymogen Cells"]),
184: ("Protein components of food are digested by the enzymatic secretion of:", ["Goblet Cells","Parietal Cells","Zymogen Cells","Oxyntic Cells"]),
185: ("Digestive System consists of different layers, the innermost is known as:", ["Submucosa","Mucosa","Muscularis","Serosa"]),
186: ("In human the closed sac which surrounds the heart is:", ["Endocardium","Myocardium","Pericardium","Epicardium"]),
187: ("Chordae tendinea are fibrous cords attached with:", ["Cardiac end of stomach valve","Tricuspid valve of heart","Pyloric sphincter of stomach","Eyelid"]),
188: ("Bicuspid valve controls the flow of blood from:", ["Right atrium to right ventricle","Right ventricle to pulmonary artery","Left ventricle to aorta","Left atrium to left ventricle"]),
189: ("Carboxyhaemoglobin (10-20%) is formed when CO2 combines with:", ["Amino group of haemoglobin","Iron part of haemoglobin","Haem portion of haemoglobin","Plasma proteins"]),
190: ("Breathing consists of:", ["Four phases","Three phases","One phase","Two phases"]),
191: ("Bowman's capsule continues as extensively convoluted portion known as:", ["Peritubular capillaries","Proximal convuluted tubules","Efferent arterioles","Afferent arterioles"]),
192: ("Restriction endonucleases cleave the __________ of duplex DNA.", ["Nitrogenous base","Base sugar","Phosphodiester bond","Hydrogen bond"]),
193: ("The enzyme which is responsible for the formation of bond between two double stranded DNA fragments is:", ["Endonuclease","Urease","Ligase","Helicase"]),
194: ("The organisms of third trophic level are:", ["Primary consumer","Primary producer","Tertiary consumer","Secondary consumer"]),
195: ("The ultimate source of energy in an ecosystem is:", ["Photosynthesis","Sun","Plants","Water"]),
196: ("All the food chains and food webs begin with:", ["Detritus","Herbivores","Green plants","Omnivores"]),
197: ("The change from bare rock or open area is rapid, especially in the initial stages and follows a series of recognizable and hence predictable stages. This process is called:", ["Pioneers","Xerosere","Succession","Secondary succession"]),
198: ("The decline in the thickness of ozone layer is caused by:", ["Increasing level of nitrogen oxide","Decreasing level of O2","Decreasing level of CFCs","Increasing level of CFCs"]),
199: ("Which one of the following is considered as strong evidence of evolution?", ["Embryology Record","Molecular Record","Biochemical Record","Fossil Record"]),
200: ("Structures found in different species which are believed to have a common evolutionary origin are called:", ["Homologous","Analogous","Vestigial","Fossilized"]),
201: ("Which one of the following is X-linked trait?", ["Male pattern baldness","Diabetes mellitus","Haemophilia","Erythroblastosis fietalis"]),
202: ("A character determined by three alleles is:", ["Human skin colour","Human blood group","Human eye colour","Human Rh factor"]),
203: ("The total number of genes in a population is called:", ["Gene pool","Allele pool","Genome","Genomic library"]),
204: ("_____________ is the branch of Biology used for the identification and interpretation of fossils.", ["Evolution","Paleontology","Zoogeography","Biodiversity"]),
205: ("Out of the given options, choose the one which shows the structures found only in plants", ["Vacuole, Chloroplast, Ribosomes","Chloroplast, Microtubules, Peroxisomes","Chloroplast, Cell Wall, Vacuole","Chloroplast, Cell Wall, Mitochondria"]),
206: ("Presence of large central vacuole is the characteristic of:", ["Prokaryotes","Protists","Fungi","Plants"]),
207: ("The basic structure of plasma membrane is provided by:", ["Proteins","Cholesterols","Cytoskeleton","Phospholipids"]),
208: ("The organelle involved in detoxification of drugs and poisons in the liver cells is:", ["Smooth Endoplasmic Reticulum","Rough Endoplasmic Reticulum","Golgi Apparatus","Lysosomes"]),
209: ("Down's syndrome is characterized by _____________ at chromosome 21.", ["Trisomy","Monosomy","Polysomy","Disomy"]),
210: ("Which of the following is an example of autosomal non-disjunction?", ["Turner's Syndrome","Jacob's Syndrome","Metastasis","Down's syndrome"]),
211: ("Infertility, short height, webbed neck and low hairline at lack are symptoms of _____________ syndrome.", ["Turner's","Down's","Edward's","Patau's"]),
212: ("The concentration of sodium ions in body fluids is controlled by the hormone:", ["Renin","Aldosterone","Angiotensin","CPK"]),
213: ("A hormone released from posterior pituitary lobe acts to actively transport water from filtrate in collecting tubules back to kidney is shown as:", ["Renin","Antidiuretic hormone","Angiotensin","Growth Factor"]),
214: ("The removal of metabolic waste from the blood is called:", ["Thermoregulation","Osmoregulation","Kidney Failure","Excretion"]),
215: ("Highly toxic nitrogenous excretory product is:", ["CO2","Uric Acid","Urea","Ammonia"]),
216: ("Humans have homeostatic thermostat present in a specified portion of the brain that is:", ["Lateral ventricle","Thalamus","Spinal Cord","Hypothalamus"]),
217: ("The disease in which death of small number of cells in the basal ganglia leads to inability to select and initiate patterns of movement is known as:", ["Fever","Alzheimer's Disease","Epilepsy","Parkinson's Disease"]),
218: ("A neurological disorder characterized by the decline in brain function is _______. Its symptoms are similar to those diseases that cause dementia.", ["Parkinson's Disease","Epilepsy","Alzheimer's Disease","Diabetes"]),
219: ("A discharge by brain which causes chaotic activity in motor and sensory areas is:", ["Meningitis","Alzheimer's Disease","Epilepsy","Parkinson's Disease"]),
220: (REDACTED_PLACEHOLDER, ["-","-","-","-"]),
}

# ---------------------------------------------------------------------------
# Answer key, resolved to Paper ID: Pink (the colour identification code
# printed on the uploaded scan / compilation \u2014 candidates filled 'C'
# against 'ID' on the response form since the printed paper colour was Pink).
# Transcribed directly from the "ANSWER KEY" page included at the end of the
# 2016 section of the compiled PDF. Letters are lower-case a/b/c/d matching
# each question's option order as printed. "x" marks a question the printed
# answer key itself left blank / marked with an "X" (Q10, Q31, Q103, and
# Q220, i.e. the illegible question) - these should be treated as
# unscored / no official answer rather than guessed.
#
# KNOWN DATA ISSUES:
# - See DIAGRAM_MCQS above for questions whose full context depends on an
#   untranscribed figure/graph/structure; letter answers below are kept as
#   printed in the official key but have not been independently re-derived
#   from the (unavailable) figures.
# - See REDACTED_MCQS above for the one question (220) that was
#   illegible/blank ("XXXXX...") in the source scan.
# - The "ID" row in the printed key (paper-colour identification question)
#   is omitted here since it isn't part of the continuous 1-220 QUESTIONS
#   numbering; its answer was C (Pink).
KEY_RAW = """
1 a
2 b
3 c
4 b
5 c
6 d
7 a
8 b
9 d
10 x
11 c
12 a
13 c
14 b
15 a
16 c
17 d
18 a
19 c
20 d
21 a
22 a
23 d
24 d
25 a
26 a
27 a
28 c
29 b
30 a
31 x
32 d
33 c
34 c
35 c
36 b
37 c
38 c
39 d
40 d
41 a
42 d
43 c
44 b
45 a
46 a
47 d
48 d
49 c
50 c
51 c
52 d
53 d
54 c
55 d
56 d
57 a
58 c
59 c
60 c
61 c
62 d
63 c
64 a
65 a
66 d
67 d
68 d
69 a
70 d
71 d
72 c
73 a
74 a
75 c
76 c
77 d
78 d
79 c
80 d
81 c
82 d
83 d
84 c
85 b
86 b
87 c
88 a
89 d
90 c
91 d
92 c
93 c
94 d
95 d
96 d
97 c
98 b
99 d
100 a
101 c
102 b
103 x
104 b
105 d
106 c
107 d
108 b
109 a
110 b
111 a
112 d
113 c
114 d
115 b
116 d
117 b
118 b
119 c
120 d
121 c
122 d
123 a
124 a
125 d
126 a
127 b
128 a
129 b
130 a
131 a
132 b
133 a
134 b
135 b
136 a
137 a
138 a
139 b
140 d
141 d
142 b
143 b
144 a
145 a
146 b
147 b
148 b
149 b
150 a
151 d
152 a
153 d
154 b
155 c
156 b
157 d
158 d
159 d
160 d
161 a
162 d
163 d
164 a
165 b
166 a
167 c
168 b
169 b
170 a
171 d
172 c
173 a
174 c
175 a
176 d
177 d
178 c
179 a
180 d
181 a
182 a
183 a
184 c
185 b
186 c
187 b
188 d
189 a
190 d
191 b
192 c
193 c
194 d
195 b
196 c
197 c
198 d
199 d
200 a
201 c
202 b
203 a
204 b
205 c
206 d
207 d
208 a
209 a
210 d
211 a
212 b
213 b
214 d
215 d
216 d
217 d
218 c
219 c
220 x
"""