# -*- coding: utf-8 -*-
# Transcribed from UHS MDCAT 2014 "Entrance Test" paper
# Source: uploaded compilation "MDCAT_Past_Papers__2008-2016__Solved.pdf"
# (contains Entrance Test papers 2008-2016 back to back; this script covers
# ONLY the 2014 paper, extracted from that compilation without transcribing
# the other years).
# Total MCQs: 220, Max Marks: 1100, Time Allowed: 150 Minutes
# Question Paper colour for this ID: Green (candidates were told to fill 'D'
# against 'ID' on the response form, and the paper itself states
# "Colour of your Question Paper is Green.")
#
# NUMBERING NOTE:
# Like the 2016 paper (and unlike the 2017 compilation), this 2014 paper
# already uses ONE continuous numbering scheme 1-220 across all four
# subjects in the printed source:
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
# before use. This 2014 paper is notably diagram-heavy (many Physics
# graphs/circuits and Chemistry structural-formula questions).
DIAGRAM_PLACEHOLDER = "[Diagram/graph/structure required \u2014 not transcribable from OCR text. See original PDF page for the figure.]"

DIAGRAM_MCQS = {
    3: {
        "subject": "PHYSICS", "orig_num": 3,
        "notes": "Diagram of a uniform meter rod suspended at its centre of gravity (50 cm mark) with 5N acting at 'O' and 10N acting at 'P', and a reaction 'R' shown. Numeric values (50 cm, 100 cm) were recovered from OCR but the exact geometry/layout of the rod and force positions is image-dependent. Needs figure to confirm answer (a, 80 cm).",
    },
    5: {
        "subject": "PHYSICS", "orig_num": 5,
        "notes": "Four Force(F)-vs-speed(v) graphs (options A-D) for drag force on a sphere through a viscous fluid, shown only as images with no distinguishing text. Needs figure to confirm answer (c).",
    },
    6: {
        "subject": "PHYSICS", "orig_num": 6,
        "notes": "Diagram of a container with points 'A' and 'B', where AB = 5 m and a small opening of height 5 cm near 'B' is shown. The exact layout (heights, position of opening) is image-dependent. Needs figure to confirm answer (b, 10 m/s).",
    },
    15: {
        "subject": "PHYSICS", "orig_num": 15,
        "notes": "Four graphs (options A-D) representing total energy vs displacement for a mass-spring system in SHM, shown only as images. Needs figure to confirm answer (b).",
    },
    16: {
        "subject": "PHYSICS", "orig_num": 16,
        "notes": "Three Stress-vs-Strain graphs (labelled X, Y, Z) shown as images; the answer options are text rows matching X/Y/Z to material types, but the graph shapes themselves are needed to determine which curve is brittle/ductile/polymer. Needs figure to confirm answer (a).",
    },
    23: {
        "subject": "PHYSICS", "orig_num": 23,
        "notes": "Circuit diagram of three NAND gates connected together (inputs A, B, output X) shown as an image. Needs figure to confirm answer (b, AND).",
    },
    24: {
        "subject": "PHYSICS", "orig_num": 24,
        "notes": "Truth table for output x = AB' + A'B (partially recovered from OCR) with blank Output column in the question, and four candidate output-column images (A-D) as options. Output values for options were partially recovered (A: 0,0,1,1; B: 1,1,1,0; C: 1,0,0,1; D: 0,1,1,1) but should be checked against the original figure. Needs figure to confirm answer (a).",
    },
    25: {
        "subject": "PHYSICS", "orig_num": 25,
        "notes": "Circuit diagram with two 6V cells, a 3\u03a9 resistor, and an ammeter 'A', shown only as an image. Needs figure to confirm answer (c, 5 A).",
    },
    26: {
        "subject": "PHYSICS", "orig_num": 26,
        "notes": "Diagram of three 6\u03a9 resistors arranged between points 'A' and 'B' (series/parallel layout shown only as an image). Needs figure to confirm answer (a, 6 \u03a9).",
    },
    34: {
        "subject": "PHYSICS", "orig_num": 34,
        "notes": "Four Intensity-vs-Wavelength spectra (options A-D) for X-ray tube output, shown only as images with no distinguishing text. Needs figure to confirm answer (a).",
    },
    43: {
        "subject": "PHYSICS", "orig_num": 43,
        "notes": "Diagram showing three radioactive radiation paths (labelled 1, 2, 3) curving between '+' and '\u2212' plates of an electric field, shown only as an image. Needs figure to confirm answer (b, Beta).",
    },
    51: {
        "subject": "CHEMISTRY", "orig_num": 51,
        "notes": "Four dot-and-cross (Lewis) structure diagrams (options A-D) of the chlorine molecule, shown only as images with no text. Needs figure to confirm answer (b).",
    },
    56: {
        "subject": "CHEMISTRY", "orig_num": 56,
        "notes": "Vapour-pressure-vs-temperature graph with four lines (i)-(iv) at different concentrations, shown as an image. Needs figure to confirm answer (a, line (i)).",
    },
    63: {
        "subject": "CHEMISTRY", "orig_num": 63,
        "notes": "Four boiling-point-elevation apparatus diagrams (labelled I-IV, each showing a solvent/solution setup with mercury manometer) shown as images. Needs figure to confirm answer (d, IV).",
    },
    67: {
        "subject": "CHEMISTRY", "orig_num": 67,
        "notes": "Four orbital-box diagrams (options A-D) showing the 3d/4s electron configuration of Manganese, shown only as images (arrows/box-filling not transcribable). Needs figure to confirm answer (a).",
    },
    73: {
        "subject": "CHEMISTRY", "orig_num": 73,
        "notes": "Four skeletal structures (options A-D) of substituted alkenes, shown as images, to identify a cis/trans isomer pair. OCR recovered fragments of the carbon skeletons but not a reliable full structure. Needs figure to confirm answer (a).",
    },
    82: {
        "subject": "CHEMISTRY", "orig_num": 82,
        "notes": "Four structural-formula diagrams (options A-D) of 2,4,6-tribromophenol showing Br substitution positions on a benzene ring, shown as images. Needs figure to confirm answer (b).",
    },
    85: {
        "subject": "CHEMISTRY", "orig_num": 85,
        "notes": "Four structural-formula diagrams (options A-D) of the 2,4-dinitrophenylhydrazone derivative of acetone, shown as images; OCR recovered partial fragments (CH3-C=N-N(H)-C6H3(NO2)2) but not the full distinguishing structure of each option. Needs figure to confirm answer (d).",
    },
    86: {
        "subject": "CHEMISTRY", "orig_num": 86,
        "notes": "Reaction scheme showing an unknown carbonyl compound '?' reacting with HCN (base-catalyzed) to give a cyanohydrin product CH3-C(OH)(CN)-C2H5, shown partly as an image. Needs figure to confirm answer (a, C2H5COCH3).",
    },
    91: {
        "subject": "CHEMISTRY", "orig_num": 91,
        "notes": "Four structural-formula diagrams (options A-D) of amino acids, to identify Glutamic Acid; OCR recovered partial fragments (H2N-CH(R)-COOH with different R groups) but not a fully reliable distinguishing structure. Needs figure to confirm answer (a).",
    },
    93: {
        "subject": "CHEMISTRY", "orig_num": 93,
        "notes": "Structural formula of an amino acid with an imidazole-like ring (partially recovered: CH=C-CH2-CH(NH2)-COOH with N/NH ring atoms) to be identified. Needs figure to confirm answer (b, Histidine).",
    },
    214: {
        "subject": "BIOLOGY", "orig_num": 214,
        "notes": "Food web diagram showing Fox, Grass Snake, Dog, Frog, Beetle, Spider, Caterpillar, Slug, Wood Boring Beetle, Wood Louse, Leaves, Wood, and Bark connected by feeding-relationship arrows, shown as an image. Needs figure to confirm answer (d, 4 food chains).",
    },
}

# ---------------------------------------------------------------------------
# REDACTED / ILLEGIBLE QUESTIONS
# Unlike the 2016 paper (which had one illegible "XXXXX" question), the
# 2014 paper's printed answer key gives a definite letter answer for every
# one of the 220 questions - no question was left blank or marked "X" in
# the source scan. REDACTED_MCQS is kept here (empty) for structural
# consistency with the other years' scripts.
REDACTED_MCQS = {}

REDACTED_PLACEHOLDER = "[Question illegible/blank in source scan - printed only as a row of 'X' characters. No official answer given.]"

SUBJECTS = [
    ("PHYSICS", 1, 44),
    ("CHEMISTRY", 45, 102),
    ("ENGLISH", 103, 132),
    ("BIOLOGY", 133, 220),
]

QUESTIONS = {
# ----------------------------- PHYSICS (1-44) -----------------------------
1: ("The formula for electric field strength is 'E = F/Q', where E is electric field strength and F is force and Q is charge. Which one of the following options gives the correct base units for electric field strength?", ["kgms-3A-1","kgs-2A-3","kg2m-2s-3A","ms-1A-3"]),
2: ("Which set of the prefixes gives values in increasing order?", ["Pico, Mega, Kilo, Tera","Pico, Micro, Mega, Giga","Tera, Pico, Micro, Kilo","Giga, Kilo, Milli, Nano"]),
3: ("Two forces, 5 N and 10 N are acting at 'O' and 'P' respectively on a uniform meter rod suspended at the position of centre of gravity 50 cm mark, as shown in the figure. " + DIAGRAM_PLACEHOLDER + " What is the position of 'P' on meter rod?", ["80 cm","75 cm","70 cm","65 cm"]),
4: ("An oil film floating on water surface exhibits colour pattern due to the phenomenon of:", ["Diffraction","Polarization","Interference","Surface tension"]),
5: ("Which of the following is the best graphical representation between drag force 'F' on a spherical object of radius 'r' and its speed 'v' through a fluid of viscosity '\u03b7'? " + DIAGRAM_PLACEHOLDER, ["Graph A","Graph B","Graph C","Graph D"]),
6: ("What is the speed of an incompressible non-viscous liquid flowing out from 'B' contained in a container as shown in the figure? Where AB = 5 m and g = 10 m/s2. " + DIAGRAM_PLACEHOLDER, ["5 m/s","10 m/s","2 m/s","50 m/s"]),
7: ("For the horizontal pipe, the fluid inside it is flowing horizontally then Bernoulli's equation can be written as", ["P + \u03c1v\u00b2 = constant","2P + \u03c1v\u00b2 = constant","P + 2\u03c1v\u00b2 = constant","2P + 2\u03c1v\u00b2 = constant"]),
8: ("The value of the least distance of distinct vision or near point is ______ for a normal human eye.", ["20 cm","25 cm","10 cm","15 cm"]),
9: ("In a compound microscope, the magnification by objective = 20, magnification by eyepiece = 11, then the total magnification is", ["M = -220","M = -0.19","M = -0.05","M = 220"]),
10: ("The distance between atoms is 0.30 nm. What will be the wavelength of X-rays at angle \u03b8 = 30\u00b0 for 1st order diffraction?", ["\u03bb = 0.60 nm","\u03bb = 0.30 nm","\u03bb = 0.20 nm","\u03bb = 0.90 nm"]),
11: ("A 100 kg man is standing in an elevator, which accidently falls freely. What will be the weight of the person in the freely falling elevator (take g=10 m/s2)", ["1000 N","10 N","500 N","Zero"]),
12: ("Frequency of simple pendulum of length 9.8 m will be", ["2\u03c0 Hertz","\u03c0/2 Hertz","1/(2\u03c0) Hertz","\u03c0/4 Hertz"]),
13: ("A body performs simple harmonic motion with a period of 0.063 s. The maximum speed is 3.0 ms-1. What are the values of the amplitude 'xo (m)' and angular frequency '\u03c9 (rads-1)'?", ["xo = 0.03, \u03c9 = 100","xo = 0.19, \u03c9 = 16","xo = 5.3, \u03c9 = 16","xo = 3.3, \u03c9 = 100"]),
14: ("Food being cooked in microwave oven is an example of", ["Beats","Overtones","Resonance","Stationary waves"]),
15: ("Potential energy of a mass spring system with respect to displacement during simple harmonic motion (SHM) is shown in the figure. Which of the following represents the total energy of mass spring system during SHM? " + DIAGRAM_PLACEHOLDER, ["Graph A","Graph B","Graph C","Graph D"]),
16: ("Three graphs for three types of materials are shown in the figure (Stress vs Strain, labelled X, Y, Z). Which row describes the correct materials? " + DIAGRAM_PLACEHOLDER, ["X: Brittle, Y: Ductile, Z: Polymer","X: Brittle, Y: Polymer, Z: Ductile","X: Polymer, Y: Brittle, Z: Ductile","X: Ductile, Y: Brittle, Z: Polymer"]),
17: ("A gas containing 'N' number of molecules of a gas having mass of each molecule 'm' is in a cubic container having length of each side 'a'. What is the density of gas contained in cube?", ["N/a\u00b2","m/a\u00b3","Nm/a\u00b3","Na\u00b3/m"]),
18: ("In 'General Gas Equation PV=nRT', 'n' represents the number of moles of gas. Which of the following represents the relation of 'n'?", ["n = N\u00b7NA","n = N/NA","n = NA/N","n = N + NA"]),
19: ("Which feature of the following graph represents Young's Modulus? " + DIAGRAM_PLACEHOLDER + " (Strain on one axis, Stress on the other)", ["Area under graph","Gradient of the graph","Reciprocal of the gradient","Product of gradient and area of the curve"]),
20: ("At triple point of water, the pressure of gas is 2680 Pa; by changing 'T' the pressure increases to 4870 Pa. Then 'T' is:", ["496.38 K","438.96 K","Zero","496.38 \u00b0F"]),
21: ("The relation between Celsius and Fahrenheit scales is: C/100 = (F\u221232)/180. At what temperature both scales give the same reading?", ["-100\u00b0","-40\u00b0","-180\u00b0","-273\u00b0"]),
22: ("A heat engine working according to second law of thermodynamics has 50% efficiency. What will be the temperature of its low temperature reservoir if high temperature reservoir is 327\u00b0C?", ["27\u00b0C","127\u00b0C","300\u00b0C","600\u00b0C"]),
23: ("Three NAND gates are connected as shown in the figure. Which of the following logic gate is formed in the connected circuit? " + DIAGRAM_PLACEHOLDER, ["OR","AND","NOR","NAND"]),
24: ("What is the output of the truth table for x = AB' + A'B? " + DIAGRAM_PLACEHOLDER, ["Output column A","Output column B","Output column C","Output column D"]),
25: ("What is the reading of Ammeter as shown in the circuit diagram? " + DIAGRAM_PLACEHOLDER + " (two 6V cells and a 3\u03a9 resistor)", ["1 A","15 A","5 A","10 A"]),
26: ("Three 6\u03a9 resistors are connected as shown in the diagram. What is the resistance between points 'A' and 'B'? " + DIAGRAM_PLACEHOLDER, ["6 \u03a9","16 \u03a9","4 \u03a9","2 \u03a9"]),
27: ("The distance between the plates of a parallel plate capacitor is 2.0 mm and area of each plate is 2.0 m\u00b2. The plates are in a vacuum. A potential difference of 1.0 x 10^4 V is applied across the plates. Find the capacitance.", ["4 x 10^-3 F","3.54 x 10^-9 F","8.85 x 10^-9 F","9.0 x 10^-9 F"]),
28: ("A solenoid 15 cm long has 300 turns of wire. A current of 5 A flows through it. What is the magnitude of magnetic field inside the solenoid?", ["75 x 10^7 T","60 x 10^+3 T","4\u03c0 x 10^-3 T","750\u03c0 x 10^+3 T"]),
29: ("Due to current in a straight conductor, the magnetic field lines' density", ["Increases away from conductor","Decreases away from conductor","Increases towards conductor","Decreases and then increases towards conductor"]),
30: ("Magnetic Resonance Imaging (MRI) is used to identify the image of", ["Tumors and inflamed tissues","Blood cells","Skin cells","Bone structures"]),
31: ("Stimulated emission of two photons 'A' and 'B' during LASER action is shown in figure (an excited atom emitting photon A at energy level E2/E1, and photon B via stimulated emission). What is the relation of wavelengths of two photons?", ["\u03bbA = \u03bbB","\u03bbA > \u03bbB","\u03bbA < \u03bbB","\u03bbA = 2\u03bbB"]),
32: ("Bones absorb greater amount of incident X-rays than flesh. This is because of the fact that", ["Bones lie between the flesh","Bones are light in color","Bones contain material of low densities","Bones contain material of high densities"]),
33: ("Which of the following techniques is the practical application of X-rays?", ["Magnetic Resonance Imaging","Ultrasonography","Computerized Axial Topography","Positron Emission Tomography"]),
34: ("Which one of the following spectra is most typical of the output of an X-ray tube? " + DIAGRAM_PLACEHOLDER, ["Graph A","Graph B","Graph C","Graph D"]),
35: ("Which one of the following has the largest energy content?", ["\u03b3-rays","X-rays","Infra-red radiations","Ultra-violet radiations"]),
36: ("What will be the energy of accelerated electron used to produce X-rays when the accelerating potential is 2 kV?", ["2 x 10^-19 J","1.6 x 10^-19 J","3.2 x 10^19 J","3.2 x 10^-16 J"]),
37: ("Process of generating three dimensional images of objects by using laser beam is called", ["Photography","3-D cinema","Holography","Tomography"]),
38: ("Which one of the following isotopes of Iodine is used for the treatment of thyroid cancer?", ["I-113","I-120","I-131","I-140"]),
39: ("A beta (\u03b2) particle is a fast-moving electron. During a \u03b2-decay how do the atomic number and mass number of a nucleus change?", ["Atomic Number remains the same, Mass Number increases by one","Atomic Number increases by one, Mass Number decreases by two","Atomic Number increases by one, Mass Number remains the same","Atomic Number decreases by two, Mass Number decreases by four"]),
40: ("A Uranium isotope 232/92 U undergoes one \u03b1-decay and one \u03b2-decay. What is the final product's atomic number?", ["90","92","89","88"]),
41: ("A naturally occurring radioactive element decays by emitting two alpha particles. Which one of the following represents the status of daughter element with respect to mass number 'A' and charge number 'Z'?", ["'Z' decreases by 4 and 'A' decreases by 2","'Z' decreases by 2 and 'A' decreases by 4","'Z' decreases by 4 and 'A' decreases by 8","'Z' decreases by 8 and 'A' decreases by 4"]),
42: ("A radioactive isotope 'W' decays to 'X' (\u03b2-decay), 'X' decays to 'Y' (\u03b1-decay), and 'Y' decays to 'Z' (\u03b1-decay). What is the change in the atomic number from 'W' to 'Z'?", ["Increases by 3","Decreases by 3","Increases by 5","Decreases by 5"]),
43: ("Three paths of radioactive radiations are observed as shown in the figure in the presence of an electric field (paths labelled 1, 2, 3 between '+' and '\u2212' plates). Which type of radiation is shown in path 1? " + DIAGRAM_PLACEHOLDER, ["Alpha","Beta","Gamma","Cathode rays"]),
44: ("What is the absorbed dose 'D' of a sample of 2 kg which is given an amount of 100 J of radioactive energy?", ["200 Gy","102 Gy","50 Gy","98 Gy"]),

# ----------------------------- CHEMISTRY (45-102) -----------------------------
45: ("A polymer of empirical formula CH2 has molar mass of 28000 g mol-1. Its molecular formula will be", ["100 times that of its empirical formula","200 times that of its empirical formula","500 times that of its empirical formula","2000 times that of its empirical formula"]),
46: ("The number of molecules in 9 g of ice (H2O) is", ["6.02 x 10^24","6.02 x 10^23","3.01 x 10^24","3.01 x 10^23"]),
47: ("Ice is less dense than water at:", ["0\u00b0C","4\u00b0C","-4\u00b0C","2\u00b0C"]),
48: ("At a given temperature and pressure, the one which shows marked deviation from ideal behavior is", ["N2","N3","CO2","He"]),
49: ("According to the number of protons, neutrons and electrons given in the table (As: 33p/42n/30e, Ga: 31p/39n/28e, Ca: 20p/20n/20e), which one of the following options is correct?", ["As-3, Ga+3, Ca","As+1, Ga+2, Ca","As+3, Ga+3, Ca+2","As+1, Ga, Ca+2"]),
50: ("If the e/m value of electron is 1.7588 x 10^11 coulombs Kg-1, then what would be the mass of electron in grams (charge on electron is 1.6022 x 10^-19 coulombs)?", ["9.1095 x 10^-31 g","91.095 x 10^-31 g","9.1095 x 10^-28 g","0.919095 x 10^-33 g"]),
51: ("The suitable representation of dot structure of chlorine molecule is: " + DIAGRAM_PLACEHOLDER, ["Structure A","Structure B","Structure C","Structure D"]),
52: ("When two partially filled atomic orbitals overlap in such a way that the probability of finding electron is maximum around the line joining the two nuclei, the result is the formation of", ["Sigma Bond","Pi-Bond","Hydrogen Bond","Metallic Bond"]),
53: ("2H2 + O2 \u2192 2H2O, \u0394H = +285.5 kJ mol-1 (as written the reaction should release energy on formation; treat the sign as printed). What will be the enthalpy change in the above reaction?", ["205.5 kJ/mol","Zero kJ/mol","-205.5 kJ/mol","1 kJ/mol"]),
54: ("Combustion of graphite to form CO2 can be done by two ways: C + O2 \u2192 CO2, \u0394H = -393.7 kJ mol-1; C + \u00bdO2 \u2192 CO, \u0394H = ?; CO + \u00bdO2 \u2192 CO2, \u0394H = -283 kJ mol-1. What will be the enthalpy of formation of CO?", ["-676 kJ mol-1","-110 kJ mol-1","110 kJ mol-1","676 kJ mol-1"]),
55: ("The value of equilibrium constant (Kc) for the reaction 2HF(s) \u21cc H2(g) + F2(g) is 10^-13 at 2000\u00b0C. Calculate the value of Kp for this reaction:", ["2 x 10^-13","10^-13","186 x 10^-13","3.48 x 10^-9"]),
56: ("The vapor pressure lines for pure as well as solutions of different concentrations are shown, with T1>T2>T3>T4. Which line represents pure water? " + DIAGRAM_PLACEHOLDER, ["Line (i)","Line (ii)","Line (iii)","Line (iv)"]),
57: ("In SO4^-2 the oxidation number of Sulphur is", ["-8","+8","-6","+6"]),
58: ("Coinage metals Cu, Ag, and Au are the least reactive because they have:", ["Negative reduction potential","Positive reduction potential","Negative oxidation potential","Positive oxidation potential"]),
59: ("What will be the pH of a solution of NaOH with a concentration of 10^-3 M?", ["3","14","11","7"]),
60: ("If the reactant or product of a chemical reaction can absorb ultraviolet, visible or infrared radiation, then the rate of a chemical reaction can best be measured by which one of the following methods?", ["Chemical method","Spectrometry","Graphical method","Differential method"]),
61: ("For the reaction 2NO + O2 \u21cc 2NO2, the rate equation for the forward reaction is", ["Rate = k[NO][O2]","Rate = k[NO]\u00b2[O2]","Rate = k[NO2]\u00b2","Rate = k[NO2]"]),
62: ("Radon is _______ emitter and being radioactive is used in ________ treatment in radiotherapy:", ["\u03b2, cancer","\u03b1, cancer","\u03b1, kidney stone","\u03b2, kidney stone"]),
63: ("One mole of glucose was dissolved in 1 kg of water, ethanol, ether and benzene separately and the molal boiling point constant of each individual solution was found to be 0.52, 1.75, 2.16 and 2.70 \u00b0C kg mol-1 respectively. Which of the following figures (I-IV) shows benzene as solvent in solution? " + DIAGRAM_PLACEHOLDER, ["I","II","III","IV"]),
64: ("The trends in melting points of the elements of 3rd period (Na, Mg, Al, Si, P, S, Cl, Ar) are depicted in a figure. The sharp decrease observed from 'Si' to 'P' is due to", ["Decrease in atomic radius from 'Si' to 'P'","Change in bonding and structure of two elements","Different universities of two elements","Increase in electron density from 'Si' to 'P'"]),
65: ("Arrange the following elements according to the trend of ionization energies. (C, N, Ne, B)", ["Ne < N < C < B","B < N < C < Na","B < C < N < Na","Ne < B < C < N"]),
66: ("Which one of the following noble gases is used for providing an inert atmosphere for welding?", ["Helium","Neon","Argon","Krypton"]),
67: ("Electronic configuration of Manganese (Mn) is shown via orbital-box diagrams for 3d and 4s subshells. " + DIAGRAM_PLACEHOLDER, ["Configuration A","Configuration B","Configuration C","Configuration D"]),
68: ("The percentage of carbon in different types of iron products is in the order of", ["Cast Iron > Wrought Iron > Steel","Wrought Iron > Steel > Cast Iron","Cast Iron > Steel > Wrought Iron","Cast Iron > Steel > Wrought Iron"]),
69: ("Which one of the following is the correct equation of 1st ionization of sulphuric acid?", ["H2SO4(aq) + H2O(l) \u2192 2H+ + SO4^2- (single arrow)","H2SO4(aq) + H2O(l) \u2192 H+(aq) + HSO4- (single arrow)","H2SO4(aq) + H2O(l) \u21cc 2H+ + SO4^2- (equilibrium arrow)","H2SO4(aq) + H2O(l) \u21cc H3O+ + SO4^2- (equilibrium arrow)"]),
70: ("Which one of the following is the correct chemical reaction for Ammonia formation by Haber process?", ["N2(g) + 3H2(g) \u2192 2NH3(g) (single arrow)","2N(g) + 3H2(g) \u21cc NH3(g)","2N(g) + 3H2(g) \u2192 2NH3(g) (single arrow)","N2(g) + 3H2(g) \u21cc 2NH3(g)"]),
71: ("The pH of acid rain is", ["7","Between 5 and 7","Below 5","Between 7 and 14"]),
72: ("Which one of the following products is obtained when sulphur trioxide is absorbed in concentrated sulphuric acid?", ["Oleum","Aqua Regia","Hydrogen sulphide","Sulphate ion"]),
73: ("Which one of the following pairs of compounds is cis and trans isomers of each other? " + DIAGRAM_PLACEHOLDER + " (four pairs of substituted-alkene skeletal structures)", ["Pair A","Pair B","Pair C","Pair D"]),
74: ("Which one of the following compounds is a ketone?", ["CH3-O-CH2-CH3","CH3-CO-CH2-CH3","CH3COCOOH","CH3-CH2CHO"]),
75: ("Addition of unsymmetrical reagent to an unsymmetrical alkene is governed by:", ["Cannizzaro's Reaction","Kirchhoff Rule","Aldol Condensation","Markownikov's Rule"]),
76: ("Ethylene glycols are used as", ["Anesthetic","Knocking agent","Freezing agent","Anti-freezing agent"]),
77: ("The halothane used in hospitals as an anesthetic is chemically", ["1-Bromo-1-chloro-2,2,2-trifluoroethane","2-Bromo-2-chloro-1,1,1-trifluoroethane","1,1,1-Trifluoro-2-bromo-2-chloroethane","2-Chloro-2-bromo-1,1,1-trifluoromethane"]),
78: ("If halogenoalkanes are mixed with an excess of ethanoic ammonia and heated under pressure, amines are formed. Which amine is formed in the reaction CH3CH2Br + NH3 \u2192 Amine?", ["CH3-CH2-NH-CH2-CH3","CH3-CH2-NH2","CH3-CH2-CH2-NH2","H2N-CH2-CH2-NH2"]),
79: ("Primary, secondary and tertiary alcohols can be identified and distinguished by", ["Lucas test","Iodoform test","Baeyer's test","Silver mirror test"]),
80: ("Which one of the following alcohols is indicated by formation of yellow crystals in Iodoform test?", ["Methanol","Ethanol","Butanol","Propanol"]),
81: ("Ethyl butyrate and butyl butanoate are esters with the flavor of", ["Pear","Banana","Pineapple","Apple"]),
82: ("The formula of 2,4,6-tribromophenol is " + DIAGRAM_PLACEHOLDER + " (four benzene-ring structures showing Br substitution positions)", ["Structure A","Structure B","Structure C","Structure D"]),
83: ("Which one of the following groups is indicated when HCl is formed by reaction of ethanol with phosphorous pentachloride?", ["Amino group","Hydroxyl group","Halide group","Hydride group"]),
84: ("A student mixed ethyl alcohol with a small amount of sodium dichromate and added it to a hot solution of dilute sulphuric acid. A vigorous reaction took place. He distilled the product formed immediately. What was the product?", ["Acetone","Acetic acid","Dimethyl ether","Acetaldehyde"]),
85: ("The structural formula of the product of reaction of acetone with 2,4-dinitrophenylhydrazine is: " + DIAGRAM_PLACEHOLDER, ["Structure A","Structure B","Structure C","Structure D"]),
86: ("For the reaction: ? + HCN --Base--> CH3-C(OH)(CN)-C2H5. " + DIAGRAM_PLACEHOLDER, ["C2H5COCH3","C2H5CH(CH3)OH","CH3COCH3","C2H5CH2CHO"]),
87: ("Acetamide is formed by dehydration of", ["Oxalic acid","Ethanoic acid","Butanoic acid","Propanoic acid"]),
88: ("Organic compounds 'X' and 'Y' both can react with Na-Metal to evolve hydrogen gas. If 'X' and 'Y' react with each other to form an organic compound 'Z' which gives fruity smell, what type of compounds are 'X', 'Y' and 'Z'?", ["X: Alcohol, Y: Ester, Z: Acetic Acid","X: Alcohol, Y: Ester, Z: Mineral Acid","X: Alcohol, Y: Acetic Acid, Z: Ester","X: Alcohol, Y: Mineral Acid, Z: Ester"]),
89: ("The amino acids which are not prepared in human body are called", ["Essential amino acids","Non-essential amino acids","Alpha amino acids","Beta amino acids"]),
90: ("Indicate the cyclic amino acid from the following:", ["Cysteine","Serine","Haloamine","Proline"]),
91: ("Which one of the following is Glutamic Acid? " + DIAGRAM_PLACEHOLDER + " (four amino-acid structures)", ["Structure A","Structure B","Structure C","Structure D"]),
92: ("At low pH or in acidic condition amino acid exists as", ["Anion","Cation","Zwitter ion","Neutral specie"]),
93: ("The structure shown below (partially recovered: CH=C-CH2-CH(NH2)-COOH with an imidazole-like N/NH ring) represents: " + DIAGRAM_PLACEHOLDER, ["Proline","Histidine","Glycine","Lysine"]),
94: ("Which one of the following reagents is used for identification of amino acids?", ["Fehling's solution","Benedict's solution","Ninhydrin","Copper (II) Sulphate"]),
95: ("Which one of the following is an example of condensation polymer?", ["Polyvinylchloride","Polystyrene","Polyethene","Polyamide"]),
96: ("Among the most common disaccharides, which one of the following is present in the milk?", ["Sucrose","Maltose","Fructose","Lactose"]),
97: ("Fats are a type of lipid called glycerides. They are esters of long chain carboxylic acids with:", ["Propene-1,2,3-triol","Propane-1,2,3-triol","Propene-1,2,3-diol","Propane-1,2,3-diol"]),
98: ("Which one of the following bases is NOT present in RNA?", ["Cytosine","Adenine","Thymine","Guanine"]),
99: ("Collagen proteins are present in _____________ throughout the body", ["Muscle","Red blood cells","Tendons","Blood plasma"]),
100: ("___________ is an eye irritant.", ["Peroxyacetyl nitrate","Peroxyacetyl nitrite","Peroxymethoxy aniline","Peroxyacetyl aniline"]),
101: ("Polystyrene is an addition polymer. Which one of the following structures represents the monomer of polystyrene?", ["CH2=CH2","CH2=CH-CH3","CH2=CH-Cl","CH2=CH-C6H5"]),
102: ("Which one of the following pollutants can cause death of a person by binding with haemoglobin of red blood cells?", ["Chlorofluorocarbons","Oxides of Sulphur","Carbon monoxide","Oxides of nitrogen"]),

# ----------------------------- ENGLISH (103-132) -----------------------------
103: ("It is our national duty to ________________ our vote in the general election.", ["Throw","Cast","Drop","Refuse"]),
104: ("She is intelligent enough to _______________ things to serve her own purpose.", ["Pick","Maneuver","Give","Take"]),
105: ("She ___________ about the excitement on hearing the news of her sister's wedding.", ["Ran","Jigged","Talked","Wept"]),
106: ("Everyone should be ______________ duties and assignments according to his/her abilities.", ["Prevented","Advised","Delegated","Suggested"]),
107: ("SPOT THE ERROR: We were ten miles up the highway (when I happened)[a] (to saw this)[b] (classified advertisement)[c] (in the newspaper.)[d]", ["when I happened","to saw this","classified advertisement","in the newspaper."]),
108: ("SPOT THE ERROR: \u201c(All is well)[a] (what ends well)[b],\u201d (said the father)[c] (when he had finished the story.)[d]", ["All is well","what ends well", "said the father","when he had finished the story."]),
109: ("SPOT THE ERROR: (Rubber tubes upon which children had swing in backyards)[a] (hung suspended)[b] (like stopped clock)[c] pendulums in the blazing air.[d]", ["Rubber tubes upon which children had swing in backyards","hung suspended","like stopped clock","pendulums in the blazing air."]),
110: ("SPOT THE ERROR: (The child was fully dressed)[a] (and sitting)[b] (in her father's lap)[c] (near the kitchen table.)[d]", ["The child was fully dressed","and sitting","in her father's lap","near the kitchen table."]),
111: ("SPOT THE ERROR: (The three Abdal Rahman,)[a] (like his illustrious predecessor,)[b] (was a young man of twenty-three)[c] when he took office.[d]", ["The three Abdal Rahman,","like his illustrious predecessor,","was a young man of twenty-three","when he took office."]),
112: ("SPOT THE ERROR: Enlarged and beautified by later Caliphs, (Al-Zahra become the)[a] (nucleus of a royal suburb)[b] (whose remain partly evacuated)[c] (in and after 1910, can still be seen.)[d]", ["Al-Zahra become the","nucleus of a royal suburb","whose remain partly evacuated","in and after 1910, can still be seen."]),
113: ("Choose the CORRECT sentence:", ["I thought it over very carefully before broaching the subject to Asma.","I thought it on very carefully before broaching the subject to Asma.","I thought it by very carefully before broaching the subject to Asma.","I thought it upon very carefully before broaching the subject to Asma."]),
114: ("Choose the CORRECT sentence:", ["He left into a blaze of anger.","He left with a blaze of anger.","He left in a blaze of anger.","He left back in a blaze of anger."]),
115: ("Choose the CORRECT sentence:", ["Shahid battered Anwar down submission.","Shahid battered Anwar into submission.","Shahid down battered Anwar into submission.","Shahid was battered Anwar down submission."]),
116: ("Choose the CORRECT sentence:", ["Pride was an intrinsic component of his personal makeup.","Pride was a intrinsic component of his personal makeup.","Pride an intrinsic component of his personal makeup.","Pride were an intrinsic component of his personal makeup."]),
117: ("Choose the CORRECT sentence:", ["The government introduced tax laws which gave incentives to factory workers to reduce pollution.","The government introduced tax laws who gave incentives to factory workers to reduce pollution.","The government introduced tax laws which have incentives to factory workers to reduce pollution.","The government introduced tax laws which has incentives to factory workers to reduce pollution."]),
118: ("Choose the CORRECT sentence:", ["It was cold and foggy, and he dared not to going out.","It was cold and foggy, and he dared not for going out.","It was cold and foggy, and he dared not go out.","It was cold and foggy, and he dared not gone out."]),
119: ("Choose the CORRECT sentence:", ["There was much cheering and singing and a bread fighting across the dining hall.","There was much cheering and singing and a bread fight across the dining hall.","There was more cheer and singing and a bread fighting across the dining hall.","There was much cheer and singing and a bread fighting across the dining hall."]),
120: ("Choose the CORRECT sentence:", ["Both parents of Jameel were then long died.","Both parents of Jameel were then long dead.","Both parents of Jameel were by then long dead.","Both parents of Jameel were by then long died."]),
121: ("Choose the CORRECT sentence:", ["But the men ate their supper with good appetites.","But the men ate their supper in good appetites.","But the men ate their supper for good appetites.","But the men ate their supper into good appetites."]),
122: ("Choose the CORRECT sentence:", ["The boy was afraid of going to jail.","The boy was afraid off going to jail.","The boy was afraid on going to jail.","The boy was afraid by going to jail."]),
123: ("Select the NEAREST CORRECT MEANING: DISDAIN", ["Vice","Dislike","Contempt","Ignorance"]),
124: ("Select the NEAREST CORRECT MEANING: SAGACITY", ["Suspicious","Cruelty","Wisdom","Foolishness"]),
125: ("Select the NEAREST CORRECT MEANING: FLAUNT", ["Snipe","Dance","Show off","Preserve"]),
126: ("Select the NEAREST CORRECT MEANING: URBANE", ["Suave","Rough","Bad","Dishonest"]),
127: ("Select the NEAREST CORRECT MEANING: DIASPORA", ["Gathering","Dispersion","Alliance","Animosity"]),
128: ("Select the NEAREST CORRECT MEANING: IMPETUOUS", ["Honest","Impulsive","Lazy","Liar"]),
129: ("Select the NEAREST CORRECT MEANING: VOCIFEROUS", ["Hidden","Loud","Strong","Weak"]),
130: ("Select the NEAREST CORRECT MEANING: TRANSIENT", ["Permanent","Temporary","Long","Good"]),
131: ("Select the NEAREST CORRECT MEANING: PROWESS", ["Hindrance","Skill","Reservation","Bad name"]),
132: ("Select the NEAREST CORRECT MEANING: BEQUEATH", ["Grant","Imbibe","Irrigate","Hope"]),

# ----------------------------- BIOLOGY (133-220) -----------------------------
133: ("The use of living organisms in industry for the production of useful products is known as", ["Parasitology","Biochemistry","Biotechnology","Molecular Biology"]),
134: ("Plants having foreign DNA incorporated into their cells are called:", ["Clone plants","Transgenic plants","Parthenocarpic plants","Mutant giants"]),
135: ("Treatment by using attenuated culture of bacteria is called", ["Chemotherapy","Sterilization","Antisepsis","Vaccination"]),
136: ("The major cause of hepatitis B is", ["Blood transfusion","Blood clotting","Absence of fibrinogen","Contaminated soil"]),
137: ("During animal cell division, the spindle fibres are formed from", ["Mitochondria","Centrioles","Ribosomes","Lysosomes"]),
138: ("Which component of the cell is concerned with cell secretions?", ["Plasma membrane","Golgi complex","Cytoskeleton","Mitochondria"]),
139: ("During which period of interphase (cell cycle) is DNA synthesized?", ["G1","G2","S","G0"]),
140: ("Peptidoglycan or murein is a special or distinctive feature of cell wall in", ["Algae","Fungi","Bacteria","Plants"]),
141: ("In mitochondria, small knob-like structures called F1 particles are found in:", ["Outer membrane","Outer compartment","Inner membrane","Inner compartment"]),
142: ("The most critical phase of mitosis which ensures equal distribution of chromatids in the daughter cells is", ["Prophase","Metaphase","Anaphase","Telophase"]),
143: ("Non-disjunction of the 21st pair of chromosomes in one of the gametes leads to 47 chromosomes in one individual. This condition is called", ["Turner's syndrome","Klinefelter's syndrome","Down's syndrome","Jacob's syndrome"]),
144: ("The intake of liquid materials across the cell membrane is", ["Phagocytosis","Endocytosis","Pinocytosis","Exocytosis"]),
145: ("Which one of the following is the site of oxidative phosphorylation in mitochondria?", ["Cristae","Matrix","Outer membrane","Ribosomes"]),
146: ("Organelle involved in the synthesis of ATP is", ["Ribosome","Mitochondria","Nucleus","Centriole"]),
147: ("The most common respiratory substrate as a source of energy is", ["Glucose","Sucrose","Fructose","Insulin"]),
148: ("The simplest monosaccharide containing a keto group is", ["Glyceraldehyde","Dihydroxy acetone","Glucose","Ribose"]),
149: ("If the genetic code is made up of three nucleotides, then total possible genetic codes will be", ["4","20","64","61"]),
150: ("Waterproof surfaces like cuticle of leaf and protective covering of an insect's body are", ["Phospholipids","Waxes","Terpenoids","Acyl glycerols"]),
151: ("In translation the terminating codon is", ["GUA","UAA","UUG","AGU"]),
152: ("All co-enzymes are derived from", ["Proteins","Carbohydrates","Metal ions","Vitamins"]),
153: ("The competitive inhibitors have structural similarity with", ["Active site","Binding site","Substrate","Co-enzyme"]),
154: ("Which one of the following is the optimum pH of pancreatic lipase enzyme?", ["7.60","8.00","9.00","9.70"]),
155: ("A co-factor tightly bound to the enzyme on a permanent basis is called", ["Activator","Co-enzyme","Prosthetic group","Apo-enzyme"]),
156: ("Which one of the following cells are mainly infected by HIV?", ["T-killer lymphocytes","T-helper lymphocytes","B-plasma cells","B-memory cells"]),
157: ("Which one of the following antibiotics causes permanent discoloration of teeth in young children if it is misused?", ["Penicillin","Streptomycin","Sulfonamide","Tetracycline"]),
158: ("What are the sequence of steps in which a bacteriophage attacks bacteria and injects its DNA?", ["Landing \u2192 Tail contraction \u2192 Penetration \u2192 DNA Injection","Penetration \u2192 Landing \u2192 Tail contraction \u2192 DNA Injection","Tail contraction \u2192 Landing \u2192 DNA Injection \u2192 Penetration","Landing \u2192 Penetration \u2192 Tail contraction \u2192 DNA Injection"]),
159: ("Athlete's Foot is a disease caused by", ["Bacteria","Virus","Fungus","Arthropod"]),
160: ("Ascaris is which one of the following?", ["Ectoparasite","Intestinal parasite","Respiratory tract parasite","Urinogenital tract parasite"]),
161: ("Polymorphism is a feature exhibited by members of", ["Coelenterates","Arthropoda","Porifera","Platyhelminthes"]),
162: ("Which one of the following is the primary host of liver fluke?", ["Man","Sheep","Snail","Dog"]),
163: ("Which one of the following is an example of a free living carnivorous flatworm?", ["Liver fluke","Dugesia","Tapeworm","Schistosoma"]),
164: ("The sources of staple food for man are plants which belong to the family:", ["Mimosaceae","Poaceae","Rosaceae","Fabaceae"]),
165: ("In human, Escherichia coli is involved in the formation of", ["Calcium","Vitamin D","Vitamin A","Vitamin K"]),
166: ("The function of Goblet cells is to secrete", ["Gastrin","Hydrochloric acid","Pepsinogen","Mucus"]),
167: ("Gastric glands are composed of ___________ types of cells", ["Two","Three","Four","Five"]),
168: ("HCl in gastric juice is secreted by which one of the following cells?", ["Chief cells","Oxyntic cells","Mucous cells","Kupffer cells"]),
169: ("Histamine is produced by which one of the following cells?", ["Basophils","Platelets","Monocyte","Eosinophils"]),
170: ("Which one of the following is the most numerous/commonest of white blood cells?", ["Eosinophils","Monocytes","Neutrophils","Lymphocytes"]),
171: ("The oxygenated blood from lungs to heart is transported by the", ["Pulmonary artery","Coronary artery","Pulmonary vein","Hepatic artery"]),
172: ("Which one of the following proteins takes part in blood clotting?", ["Prothrombin","Fibrinogen","Immunoglobulin","Globulin"]),
173: ("Which one of the following is responsible for the production of concentrated urine?", ["Juxtamedullary nephrons","Cortical nephrons","Proximal tubule","Distal tubule"]),
174: ("Reabsorption of useful constituents normally takes place in which one of the following?", ["Proximal tubule","Distal tubule","Bowman's capsule","Glomerulus"]),
175: ("Which one of the following parts of the excretory system in humans acts as a countercurrent multiplier?", ["Kidney","Cortex","Medulla","Loop of Henle"]),
176: ("Anti-Diuretic Hormone (ADH) is released from", ["Anterior pituitary lobe","Posterior pituitary lobe","Hypothalamus","Thalamus"]),
177: ("Which one of the following is the main nitrogenous waste product in humans?", ["Urea","Ammonia","Salts","Uric acid"]),
178: ("The right and left cerebral hemispheres are connected by a thick band of nerve fibres called:", ["Medulla","Corpus callosum","Pons","Hippocampus"]),
179: ("The part of the brain which guides smooth and accurate motions and maintains body position is called", ["Cerebrum","Cerebellum","Pons","Medulla"]),
180: ("Which one of the following is the effect of sympathetic nervous system?", ["Constriction of bronchi","Decrease in heart rate","Promotes digestion or peristalsis","Dilates the pupil"]),
181: ("High levels of aluminium may contribute to the onset of which one of the following?", ["Parkinson's disease","Epilepsy","Alzheimer's disease","Gonorrhea"]),
182: ("Testosterone is produced by which one of the following?", ["Sertoli cells","Germinal epithelium","Interstitial cells","Spermatogonia"]),
183: ("The oocyte released during ovulation is in", ["Anaphase I","Prophase I","Metaphase I","Metaphase II"]),
184: ("Yellowish glandular structure formed after the release of egg from the follicle is called", ["Corpus callosum","Graafian follicle","Corpus luteum","Follicle atresia"]),
185: ("On puberty, the development of primary follicles is stimulated by", ["ICSH","FSH","LH","Estrogen"]),
186: ("Causative agent of a sexually transmitted disease that affects the mucous membrane of the urinogenital tract is", ["Staphylococcus aureus","Treponema pallidum","Neisseria gonorrhoeae","Escherichia coli"]),
187: ("In a human vertebral column, the number of ______________ vertebrae is 7.", ["Cervical","Thoracic","Lumber","Sacrum"]),
188: ("Which one of the following structures holds the bones together?", ["Joints","Cartilages","Fibrous capsules","Ligaments"]),
189: ("Which one of the following cartilages is the most abundant in the human body?", ["Elastic cartilage","Chondrous cartilage","Fibrous Cartilage","Hyaline Cartilage"]),
190: ("The repeated protein pattern of myofibrils is called", ["Sarcomere","Zyomere","Sarcolemma","Cross bridges"]),
191: ("When more energy is required in muscle contraction, then that energy can also be produced by _______________ as a secondary source.", ["Glucose","Phosphocreatine","Fructose","Lactic acid"]),
192: ("Which one of the following is a steroid hormone?", ["Glucagon","Thyroxine","Epinephrine","Oestrogen"]),
193: ("The gonadotrophic hormones of the anterior lobe of pituitary include:", ["Prolactin, Thyroid Stimulating Hormone, Somatotropin Hormone","Follicle Stimulating Hormone, Luteinizing Hormone, Prolactin","Adrenocorticotrophic Hormone, Luteinizing Hormone, Follicle Stimulating Hormone","Luteinizing Hormone, Follicle Stimulating Hormone, Thyroid Stimulating Hormone"]),
194: ("Over-activity of the cortical hormone of adrenal gland causes", ["Addison's disease","Parkinson's disease","Cushing's disease","Down's syndrome"]),
195: ("How many iodine atoms are present in thyroxine?", ["3","4","2","5"]),
196: ("T-lymphocytes recognize antigen and attack microorganisms or transplanted organ and tissues. This effect is called", ["Cell-mediated response","Humoral immune response","Active immunity","Passive immunity"]),
197: ("Which part of antibody recognizes the antigen during immune response?", ["Heavy part","Light part","Constant part","Variable part"]),
198: ("What type of immunity is achieved by injecting antibodies, antiserum, anti-venom serum?", ["Active immunity","Passive immunity","Artificially induced immunity","Naturally induced immunity"]),
199: ("Which one of the following glands is involved in the production of lymphocytes?", ["Pineal","Pituitary","Thymus","Adrenal"]),
200: ("Antibodies are proteins and made up of how many polypeptide chains?", ["One","Two","Three","Four"]),
201: ("Oxidative phase of glycolysis starts with dehydrogenation of", ["Glycolysis","Ribulose Bisphosphate","Glyceraldehyde 3-phosphate","NADH"]),
202: ("In one turn, the Krebs's cycle produces one molecule of ATP, one molecule of FADH2 and __________ molecules of NADH", ["1","2","3","4"]),
203: ("Which one of the following is the stage of cellular respiration for which oxygen is not essential?", ["Glycolysis","Pyruvate oxidation","Krebs's cycle","Electron Transport Chain"]),
204: ("Pyruvate, the end product of glycolysis, moves from cytosol to mitochondrial matrix where it is oxidized into ___________ producing CO2 as a by-product.", ["Acetic acid (active)","Citrate","NAD","FAD"]),
205: ("Pyruvate \u2192 Acetyl CoA. Which pair of coenzyme transformations occurs in this reaction?", ["FAD+ \u2192 FADH","NAD+ \u2192 NADH","NADH \u2192 NAD+ + H+","FADH+ \u2192 FAD + H+"]),
206: ("pBR322 has antibiotic resistance genes for", ["Ampicillin and aspirin","Streptomycin and metronidazole","Ampicillin and Tetracycline","Penicillin and metronidazole"]),
207: ("Cystic Fibrosis affects which one of the following cells of the body?", ["Epithelial cells","Endothelial cells","Plasma cells","Blood cells"]),
208: ("The enzymes which act as molecular scissors in recombinant DNA technology are", ["Exonucleases","Endonucleases","Polymerases","Reverse transcriptases"]),
209: ("Which of the following is the correct sequence of PCR?", ["Heating \u2192 Cooling \u2192 Add Primer \u2192 Copying of strand","Heating \u2192 Add Primer \u2192 Cooling \u2192 Copying of strand","Add Primer \u2192 Heating \u2192 Cooling \u2192 Copying of strand","Cooling \u2192 Add Primer \u2192 Heating \u2192 Copying of strand"]),
210: ("When two different pieces of DNA are joined together, the result is which one of the following?", ["Complementary DNA","Mutated DNA","Recombinant DNA","Cloned DNA"]),
211: ("Individual successions are known as", ["Primary successions","Secondary successions","Seres","Xeroses"]),
212: ("Which one of the following is the ultimate distributional unit within which a species is restrained by the limitations of its physical structure and physiology?", ["Niche","Biome","Ecosystem","Habitat"]),
213: ("All herbivores belong to which trophic level in the food chain?", ["T1","T2","T3","T4"]),
214: ("How many food chains are present in the following food web (Fox, Grass Snake, Dog, Frog, Beetle, Spider, Caterpillar, Slug, Wood Boring Beetle, Wood Louse feeding from Leaves, Wood, and Bark)? " + DIAGRAM_PLACEHOLDER, ["5","3","6","4"]),
215: ("The relationship in which one organism gets benefit and the other is not affected is called", ["Mutualism","Commensalism","Predation","Parasitism"]),
216: ("A gene that has more than one phenotypic effect is called", ["Pleiotropic","Epistatic","Dominant","Mutant"]),
217: ("A gene which masks the expression of another non-allelic gene is called", ["Pleiotropic","Epistatic","Dominant","Mutant"]),
218: ("Position of a gene within a DNA molecule is", ["Locus","Origin","Amplicon","Filial"]),
219: ("Sickle cell anemia is a type of", ["Insertion","Transposition","Deletion","Base Substitution"]),
220: ("Position of a gene within a DNA molecule is", ["Locus","Origin","Amplicon","Filial"]),
}

# ---------------------------------------------------------------------------
# Answer key, resolved to Paper ID: Green (the colour identification code
# printed on the uploaded scan / compilation \u2014 candidates filled 'D'
# against 'ID' on the response form since the printed paper colour was
# Green).
# Transcribed directly from the "ANSWER KEY" page included at the end of the
# 2014 section of the compiled PDF. Letters are lower-case a/b/c/d matching
# each question's option order as printed. Unlike the 2016 paper, every one
# of the 220 questions has a definite letter answer in the printed key - no
# question was left blank or marked "X" in the source scan.
#
# KNOWN DATA ISSUES:
# - See DIAGRAM_MCQS above for questions whose full context depends on an
#   untranscribed figure/graph/structure; letter answers below are kept as
#   printed in the official key but have not been independently re-derived
#   from the (unavailable) figures.
# - Q.53's printed enthalpy value (+285.5 kJ mol-1) appears to have a sign
#   inconsistency versus the answer key's chosen option (-205.5 kJ/mol);
#   kept exactly as printed in both the question and the key rather than
#   silently corrected.
# - Q.216/Q.217/Q.220 in the source scan/answer key show adjacent
#   duplicate-looking question text and answer patterns (Pleiotropic/
#   Epistatic/Dominant/Mutant style options repeating near a duplicated
#   "Position of a gene within a DNA molecule" stem at both Q.218 and
#   Q.220); these are kept exactly as transcribed from the source rather
#   than merged or corrected, since the printed key gives distinct answers
#   for each (216=a, 217=b, 218=a, 219=a, 220=d).
# - The "ID" row in the printed key (paper-colour identification question)
#   is omitted here since it isn't part of the continuous 1-220 QUESTIONS
#   numbering; its answer was D (Green).
KEY_RAW = """
1 a
2 b
3 b
4 c
5 a
6 b
7 b
8 b
9 d
10 b
11 d
12 c
13 a
14 c
15 d
16 d
17 c
18 b
19 c
20 a
21 b
22 a
23 a
24 a
25 c
26 d
27 c
28 c
29 a
30 a
31 a
32 d
33 c
34 c
35 a
36 d
37 c
38 c
39 c
40 b
41 c
42 b
43 c
44 c
45 d
46 d
47 a
48 c
49 c
50 a
51 b
52 a
53 c
54 b
55 b
56 a
57 d
58 b
59 c
60 b
61 b
62 b
63 a
64 b
65 c
66 a
67 a
68 c
69 b
70 d
71 c
72 a
73 a
74 b
75 d
76 d
77 b
78 b
79 a
80 b
81 c
82 b
83 b
84 d
85 d
86 a
87 b
88 c
89 a
90 d
91 a
92 b
93 b
94 c
95 d
96 d
97 b
98 c
99 c
100 a
101 d
102 c
103 b
104 b
105 b
106 c
107 c
108 a
109 b
110 c
111 a
112 c
113 a
114 c
115 b
116 a
117 a
118 c
119 b
120 c
121 a
122 a
123 c
124 c
125 c
126 a
127 b
128 b
129 b
130 b
131 b
132 a
133 c
134 b
135 d
136 a
137 b
138 b
139 c
140 c
141 c
142 c
143 c
144 c
145 a
146 b
147 a
148 b
149 c
150 b
151 b
152 d
153 c
154 c
155 c
156 b
157 d
158 a
159 c
160 b
161 b
162 b
163 b
164 b
165 d
166 d
167 b
168 b
169 a
170 d
171 c
172 b
173 a
174 a
175 d
176 b
177 a
178 b
179 b
180 d
181 c
182 c
183 d
184 c
185 b
186 c
187 a
188 d
189 d
190 a
191 b
192 d
193 b
194 c
195 a
196 b
197 d
198 b
199 c
200 d
201 c
202 c
203 a
204 a
205 b
206 c
207 a
208 b
209 a
210 c
211 c
212 a
213 b
214 d
215 b
216 a
217 b
218 a
219 a
220 d
"""