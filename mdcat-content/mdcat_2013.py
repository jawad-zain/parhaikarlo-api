# -*- coding: utf-8 -*-
# Transcribed from UHS MDCAT 2013 "Entrance Test" paper (Paper ID: Pink)
# Source: "MDCAT_Past_Papers__2008-2018__Solved" compilation (TopStudyWorld / ARK),
# cross-checked against the mdcatguide.com scanned reproduction of the same paper.
# Total MCQs: 220, Max Marks: 1100, Time Allowed: 150 Minutes
#
# THIS FILE COVERS QUESTIONS 1-112 ONLY (Physics 1-44, Chemistry 45-102, first
# 10 of English 103-132). The remaining 108 questions (rest of English + all of
# Biology 133-220) are intentionally left for a follow-up pass.
#
# NUMBERING NOTE: one continuous numbering scheme 1-220 across all subjects:
#   Physics    Q.1   - Q.44
#   Chemistry  Q.45  - Q.102
#   English    Q.103 - Q.132
#   Biology    Q.133 - Q.220
#
# NOTE ON DIAGRAM / GRAPH / STRUCTURE MCQs:
# Unlike the 2014 file, the diagram-dependent MCQs below are NOT placeholder-only --
# real cropped images from the source PDF are attached via QuestionImage after import
# (see import_question_images), so these stay is_active=True with is_visual_required=True.
# DIAGRAM_MCQS here is used only to drive that image-attachment step + editorial notes.
DIAGRAM_MCQS = {
    27: {"note": 'Circuit figure required: two NAND gates (inputs A,B each) both feeding an OR gate whose output is X. Options are real Boolean expressions, so only the stem needs the figure.'},
    28: {"note": 'Circuit figure required: three resistors each of value R connected between X and Y in an arrangement shown in the figure (not necessarily simple series -- verify topology from image).'},
    29: {"note": 'Figure required: a current-carrying wire between the N and S poles of a magnet, current I directed as shown. Options are real text, only the stem needs the figure.'},
    57: {"note": 'Figure required: Zn | ZnSO4 solution || CuSO4 solution | Cu galvanic cell with a porous partition, to determine external-circuit electron-flow direction. Options are real text, only the stem needs the figure.'},
    58: {"note": 'Graph-only options: four log K vs 1/T curve shapes (rising line / peaked curve / falling line / dipped curve) per the Arrhenius equation.'},
    66: {"note": 'Structure-only options: four Lewis-structure renderings of carbon monoxide (dot/bond placement differs).'},
    73: {"note": 'Structure-only options: four skeletal alkene drawings testing cis vs trans (Z/E) substituent placement.'},
    76: {"note": 'Structure-only options: four bromoalkane structures (Markovnikov vs anti-Markovnikov addition products of propene + HBr).'},
    80: {"note": 'Structure figure required: a benzene ring bearing one OH and three NO2 substituents (2,4,6-trinitrophenol). Options are real text, only the stem needs the figure.'},
    82: {"note": 'Structure-only options: four brominated phenol structures (mono- vs tri-bromophenol regiochemistry).'},
    84: {"note": 'Structure-only options: four alcohol structures, one of which oxidises to phenyl methyl ketone (acetophenone).'},
    85: {"note": 'Structure-only options: four carbonyl-compound structures testing ketone vs acid/amide/acid-chloride recognition.'},
    90: {"note": 'Structure-only options: four dipeptide structures formed from two glycine molecules (peptide-bond connectivity differs).'},
}

# ---------------------------------------------------------------------------
# COMPLETION FROM THE SUPPLIED 2013 PDF
# The originally supplied Python source contained Q.1-Q.112 only.
# Q.113-Q.220 below were extracted from the supplied UHS MDCAT 2013 PDF:
#   MDCAT Past Papers (2008-2016) Solved.pdf
#   UHS Entrance Test 2013, pages 14-20 of the 2013 paper.
#
# No questions were copied from another year or invented from general knowledge.
# Where the printed paper contains a figure/structure, DIAGRAM_PLACEHOLDER marks
# the visual that should be attached from the PDF during the DB image-import step.

SUBJECTS = [
    ("PHYSICS", 1, 44),
    ("CHEMISTRY", 45, 102),
    ("ENGLISH", 103, 132),
    ("BIOLOGY", 133, 220),
]

QUESTIONS = {
# ----------------------------- PHYSICS (1-44) -----------------------------
1: ("The wavelength 'λ' of a wave depends on the speed 'v' of the wave and its frequency 'f'. Decide which of the following is correct?", ['f = v λ', 'f = λ/v', 'f = v/λ', 'f = v λ-2']),
2: ("Name the quantity which can be measured by using base unit 'kgm2s-3'", ['Weight', 'Pressure', 'Power', 'Work']),
3: ("Ratio of moment of inertia of two objects 'A' and 'B' is 2:3. Which one of the following is the ratio of torques of 'A' and 'B' respectively, if both are being rotated with constant angular acceleration?", ['3:4', '2:3', '3:2', '4:3']),
4: ("Due to some mechanical fault, a lift falls freely from the top of a multistory building. Which of the followings is the apparent weight of a man inside the lift, if mass of man is 80 kg while value of 'g' is 10 ms-2?", ['900 N', 'Zero', '800 N', '700 N']),
5: ("Stokes' Law is given as:", ['F = 6πηr2v', 'F = 6πηrv', 'F = 6πηrv-1', 'F = 6π2ηr3v']),
6: ('The product of cross-sectional area of the pipe and the fluid speed at any point along the pipe:', ['Remains constant', 'Is zero', 'Exponentially increases', 'Exponentially decreases']),
7: ('A small leak is developed in a large water storage tank. If the height of water above leakage is 10 m, then find the speed of efflux through the leak:', ['14 m/sec', '10 m/sec', '9.8 m/sec', '20 m/sec']),
8: ('The minimum distance from the eye at which an object can be seen clearly without strain is called:', ['Focal point', 'Near point', 'Yield point', 'Far point']),
9: ('In the diffraction of light around an obstacle, the angle of diffraction is increased then:', ['The wavelength of incident light wave is increased', 'The wavelength of incident light wave is decreased', 'The amplitude of the incident light wave is increased', 'The amplitude of the incident light wave is decreased']),
10: ('An object 15 cm from a lens produces a real image 30 cm from the lens. What is the focal length of the lens?', ['+15 cm', '+20 cm', '+10 cm', '+25 cm']),
11: ('What is the formula for critical angle in case of light through two mediums having refractive indexes n1 and n2 such that n1 > n2?', ['sin-1(n1/n2)', 'cos-1(n1/n2)', 'cos-1(n2/n1)', 'sin-1(n2/n1)']),
12: ("For vibrating mass-spring system, the expression of kinetic energy at any displacement 'x' is given by:", ['(1/2)kxo2 (1 - x2/xo2)', '(1/2)kxo2', '(1/2)mω (1 - x2/xo2)', '(1/2)mω2xo']),
13: ('Speed of sound through a gas is measured as 340 m/s at pressure P1 and temperature T1. What will be the speed of sound if pressure of gas is doubled but temperature is kept constant?', ['342 m/s', '340 m/s', '170 m/s', '680 m/s']),
14: ('The stress-strain graph, deduced the following limits successively:', ['Proportional limit, yield limit, elastic limit', 'Yield limit, elastic limit, proportional limit', 'Proportional limit, elastic limit, yield limit', 'Elastic limit, proportional limit, yield limit']),
15: ('Variation of amplitude with respect to time for an oscillation object is shown in figure. Identify the oscillation: (The amplitude-vs-time graph shows the oscillation staying within fixed limits +Yo and -Yo, i.e. it does NOT decay over time.)', ['Damped', 'Critical', 'Undamped', 'Heavily damped']),
16: ('A 4.0 m long wire is subjected to stretching force and its length increases by 40 cm. The percent elongation which the wire undergoes is:', ['0.10 %', '40 %', '10 %', '20 %']),
17: ('What is the value of universal gas constant?', ['8314 Jmol-1K-1', '83.14 Jmol-1K-2', '831.4 Jmol-1K-1', '8.314 Jmol-1K-2']),
18: ('A gas sample contains three molecules each having speed 1 ms-1, 2 ms-1, 3 ms-1. What is the mean square speed?', ['14/3 m/s', '6 m/s', '2 m/s', '√(14/3) m/s']),
19: ('What is the factor upon which change in internal energy of an ideal gas depends?', ['Change in volume', 'Change in temperature and volume', 'Change in temperature', 'Path followed to change internal energy']),
20: ("What will be the mathematical form of first law of thermodynamics for a system whose variation of volume by pressure is shown? (The P-V graph shown is labelled 'Isothermal', i.e. temperature is constant, curving from (P1,V1) down to (P2,V2).)", ['Q = U', 'U = W', 'Q = U/W', 'Q = W']),
21: ("For a heat engine 'A' ratio of Q1 to Q2 is 2/3 while that of heat engine 'B', ratio of Q2 to Q1 is 1/3. What is the value ηA : ηB?", ['1:3', '1:2', '2:3', '2:1']),
22: ('What is the charge stored on a 5 μF capacitor charged to potential difference of 12 V?', ['60 μC', '2.4 C', '2.4 μC', '60 C']),
23: ('Which of the following is the proper way to study the sinusoidal wave form of voltage?', ["Voltage is connected to 'Y' input and time base is switched on.", "Voltage is connected to 'X' input and time base is switched off.", "Voltage is connected to 'Y' input and time base is switched off.", "Voltage is connected to 'X' input and time base is switched on."]),
24: ('12-volt battery is applied across 6-ohm resistance to have a steady flow of current. What must be the required potential difference across the same resistance to have a steady current of one ampere?', ['12 V', '6 V', '1 V', '3 V']),
25: ('A solenoid is cut into two halves. Magnetic induction due to same current in each half will be:', ['Half of the original', 'Double of the original', 'Same as original', 'Four times of the original']),
26: ('A long straight current carrying conductor has current directed from bottom to top when held vertically. What will be the direction of magnetic field lines when observed from below the conductor?', ['Clockwise', 'Anti clockwise', 'Vertically upward', 'Vertically downward']),
27: ('What is the output Boolean expression of logic diagram shown in figure below (two NAND gates, each fed by inputs A and B, both feeding into an OR gate whose output is X):', ["(A' + B').(A' + B')", "(A' + B')(A' + B')", "A'.B' + A'.B'", "(AB)' + (AB)'"]),
28: ("Three resistors each having value 'R' are connected as shown in figure. What is the equivalence resistance between 'X' and 'Y'?", ['Structure/arrangement A (see figure)', 'Structure/arrangement B (see figure)', 'Structure/arrangement C (see figure)', 'Structure/arrangement D (see figure)']),
29: ("The diagram shows a wire, carrying a current 'I', placed between the poles of magnet: In which direction does the force on the wire act?", ["Towards the 'N' pole of the magnet", 'Downwards', 'Upwards', "Towards the 'S' pole of the magnet"]),
30: ('X-rays from a given X-ray tube operating under specified conditions have a minimum wavelength. The value of this minimum wavelength could be reduced by:', ['Cooling the target', 'Reducing the temperature of the filament', 'Increasing the potential difference between the cathode and the target', 'Reducing the pressure in the tube']),
31: ('Helium-neon lasers are used for the:', ['Precise measurement of range finding', 'Optical fiber communication systems', 'Surveying for construction of tunnels', 'Welding detached bone of body']),
32: ("What is the type of characteristic X-ray photon whose energy is given by relation 'hf = EM - EK'?", ['K - alpha', 'M - alpha', 'K - beta', 'M - beta']),
33: ('Kinetic energy of electrons by applying potential difference V1 across the x-ray tube is KE1 while V2 potential difference produce kinetic energy equal to KE2. What will be the value of KE1:KE2 if ratio of potential difference V1:V2 = 2:3?', ['3:2', '4:9', '9:4', '2:3']),
34: ("What will be the relation for the speed of electron accelerated towards the target in X-ray tube by applying potential difference 'V', take mass of electron 'm' and charge on electron 'e'?", ['v = √(2Ve/m)', 'v = √(2me/V)', 'v = √(2V/me)', 'v = √(2meV)']),
35: ('For what CAT stands in X-ray technology?', ['Capacitor Amplifier Transistor', 'Computerized Axial Tomography', 'Cathode Anode Technique', 'Current Amplification Technology']),
36: ('During the production of LASER, when the excited state E2 contains more number of atoms than the ground state E1, the state is known as:', ['Population inversion', 'Ground State', 'Excited state', 'Metastable state']),
37: ('In cloud chamber the path of β-particles is:', ['Straight, thick, short', 'Thin, wavy, shorter', 'Thin, wavy, longer', 'Thin, straight, short']),
38: ('Among the three types of radioactive radiation, which have strongest penetration power?', ['Alpha', 'Gamma', 'Beta', 'All have same penetration power']),
39: ('Emission of alpha decay from a radioactive substance causes:', ["Decreases in 'Z' by 4 and decreases in 'A' by 2", "Decreases in 'A' by 1 and 'Z' remains same", "Decreases in 'Z' by 1 and 'A' remains same", "Decreases in 'A' by 4 and decreases in 'Z' by 2"]),
40: ('10 Joule of energy is absorbed by 10-gram mass from a radioactive source. What is the absorbed dose?', ['1 gray', '1000 gray', '10 gray', '100 gray']),
41: ('Isotopes are those nuclei of an element that have:', ['Same mass number but different atomic number', 'Same mass number as well as atomic number', 'Different mass number as well as atomic number', 'same atomic number but different mass number']),
42: ('Which one of the following emission takes place in a nuclear reaction? 90Th234 -> 91Pa232 + ___', ['Alpha', 'Gamma', 'Beta', 'Photons']),
43: ('Emission of radiation from radioactive substance is:', ['Dependent on both temperature and pressure', 'Independent of temperature but dependent on pressure', 'Independent of both temperature and Pressure', 'Independent of pressure but dependent on temperature']),
44: ("In a simple harmonic motion with a radius 'xo', the velocity of the particle at any point is:", ['v = ω√(xo2 - x2)', 'v = ω(x2 - xo2)', 'v = ω√(xo - x)', 'v = ω√(x - xo)']),
# ----------------------------- CHEMISTRY (45-102) -----------------------------
45: ('Hydrogen burns in chlorine to produce hydrogen chloride. The ratio of masses of reactants in chemical reaction is: H2 + Cl2 -> 2HCl', ['1:35.5', '2:35.5', '1:71', '2:70']),
46: ("A sample of Neon is found to exist as 20Ne, 21Ne, 22Ne. Mass spectrum of 'Ne' is as follow: What is the relative atomic mass (A, value) of Neon? (Mass spectrum: relative abundance 90.92% at mass number 20, 0.26% at mass number 21, 8.82% at mass number 22.)", ['20.18', '20.28', '20.10', '20.22']),
47: ('The coordination number of Na+ in NaCl crystal is:', ['6', '2', '4', '8']),
48: ('There are four gases H2, He, N2 and CO2 at 0 °C. Which gas shows greater non-ideal behavior?', ['He', 'CO2', 'H2', 'N2']),
49: ('Correct order of energy in the given subshells is:', ['5s > 3d > 3p > 4s', '5s > 3d > 4s > 3p', '3p > 3d > 5s > 4s', '3p > 3d > 4s > 5s']),
50: ('Number of electrons in the outermost shell of chloride ion (Cl―) is:', ['17', '3', '1', '8']),
51: ('According to valence shell electron pair repulsion theory, the repulsive forces between the electron pair of central atom of molecule are in the order:', ['Lone Pair - Lone-Pair > Lone Pair - Bond Pair > Bond Pair - Bond Pair', 'Lone Pair - Bond Pair > Lone Pair - Lone Pair > Bond Pair - Bond Pair', 'Bond Pair - Bond Pair > Lone Pair - Lone Pair > Lone Pair - Bond Pair', 'One Pair - Bond Pair > Bond Pair - Bond Pair > Lone Pair - Lone Pair']),
52: ('In crystal lattice of ice, each O-atom of water molecule is attached to:', ['Four H-atoms', 'Three H-atoms', 'One H-atom', 'Two H-atoms']),
53: ('Heat of formation (∆Hf°) for CO2 is:', ['-394 kJ/mole', '+394 kJ/mole', '-294 kJ/mole', '-390 kJ/mole']),
54: ('Reactants have high energy than products in:', ['Exothermic reactions', 'Endothermic reactions', 'Photochemical reactions', 'Non-spontaneous reactions']),
55: ('If 18.0 g of glucose is dissolved in 1 kg of water, boiling point of this solution should be:', ['100.52 °C', '100.00 °C', '100.052 °C', 'Less than 100 °C']),
56: ('Molal freezing point constant of water is:', ['1.86', '2.86', '11.86', '0.52']),
57: ('In the figure given below, the electron flow in external circuit is from:', ['Copper to zinc electrode', 'Right to left', 'Porous partition to zinc electrode', 'Zinc to copper electrode']),
58: ("By considering Arrhenius equation, the graph between '1/T' and 'log K' given a curve of the type:", ['Graph A', 'Graph B', 'Graph C', 'Graph D']),
59: ('Which one of the following is a redox reaction?', ['NaCl + AgNO3 -> NaNO3 + AgCl', '2Cl- -> Cl2 + 2e-', '2Na + Cl2 -> 2NaCl', 'Na+ + 1e- -> Na']),
60: ('The chemical substance, when dissolved in water, gives "H+" is called:', ['Acid', 'Base', 'Amphoteric', 'Neutral']),
61: ("The 'pH' of our blood is:", ['6.7 - 8', '7.9', '7.5', '7.35 - 7.4']),
62: ('In zero order reactions, the rate is independent of:', ['Concentration of the product', 'Concentration of the reactant', 'Temperature of the reaction', 'Surface area of the product']),
63: ('What is the trend of melting and boiling point of the elements of short periods as we move from left to right in a periodic table?', ['Melting and boiling points first decrease then increase', 'Melting and boiling points increase gradually', 'Melting and boiling points first increase then decrease', 'Melting and boiling points decrease gradually']),
64: ('Along a period, atomic radius decreases. This gradual decrease in radius is due to:', ['Increase in number of electrons in valence shells', 'Increase in number of protons in the nucleus', 'Decrease in number of shells', 'Increase in number of shells']),
65: ('Alkaline earth metal oxides react with water to give hydroxides. The solubility of alkaline earth metal oxides in water increases as we move from top to bottom in a group. Which of the following alkaline earth metal oxides is least soluble in water?', ['MgO', 'CaO', 'BaO', 'SrO']),
66: ('The electronic structure of carbon monoxide is represented as:', ['Structure A', 'Structure B', 'Structure C', 'Structure D']),
67: ("Which one pair has the same oxidation state of 'Fe'?", ['FeSO4 and FeCl3', 'FeCl2 and FeCl3', 'FeSO4 and FeCl2', 'Fe2(SO4)3 and FeSO4']),
68: ("Oxidation state of 'Fe' in K3[Fe(CN)6] is:", ['+2', '+3', '-6', '-3']),
69: ('The nature of an aqueous solution of ammonia (NH3) is:', ['Amphoteric', 'Neutral', 'Acidic', 'Basic']),
70: ('Unpolluted rain water has a pH of:', ['4.9', '5.6', '5.3', '7.0']),
71: ('In comparison with oxygen gas, a strong triple bond is present between two nitrogen atoms in a molecule and therefore nitrogen gas is:', ['Highly reactive gas', 'Completely inert like noble gases', 'Moderately reactive gas', 'Very less reactive gas']),
72: ("The catalyst used in the Haber's process is:", ['Magnesium oxide', 'Aluminium oxide', 'Silicon oxide', 'Iron crystals with metal oxide promoters']),
73: ('The cis-isomerism is shown by:', ['Structure A', 'Structure B', 'Structure C', 'Structure D']),
74: ('Select the nucleophile from the following examples:', ['NO2', 'NH3', 'NO2+', 'N+H4']),
75: ('The introduction of an alkyl group in benzene takes place in the presence of AlCl3 and:', ['R-COOH', 'R-Cl', 'R-COCl', 'R-COO-']),
76: ('What is the product formed when propene reacts with HBr?', ['Structure A', 'Structure B', 'Structure C', 'Structure D']),
77: ('The order of reactivity of alkyl halides towards nucleophile is:', ['RI > RBr > RF > RCl', 'RI > RBr > RCl > RF', 'RF > RCl > RBr > RI', 'RF > RBr > RCl > RI']),
78: ('Consider the reaction given below: CH3-CH2-CH2-CH2-Br reacts two different ways -- (I) to give CH3-CH2-CH2-CH2-OH, and (II) to give CH3-CH2-CH=CH2. Which statement is true?', ['Reagent for I is KOH in alcohol', 'Reagent for II is KOH in aqueous medium', 'Reaction I is Debromination', 'Reaction II is elimination']),
79: ('Consider the following reaction: C2H5OH + PCl5 ? What product(s) may be formed?', ['C2H5Cl only', 'C2H5Cl and HCl', 'C2H5Cl, POCl3 and HCl', 'C2H5Cl and POCl3']),
80: ('The compound shown (a phenol ring with OH and three NO2 substituents) is named as:', ['Picric acid', 'Nitro phenol', 'Benzoic acid', 'Malonic acid']),
81: ('Which group gives a yellow precipitate of triiodo methane when warmed with alkaline aqueous iodine?', ['An amide group (CH3-C(=O)-NH2)', 'Ethyl Ketone group (C2H5-C(=O)-R)', 'A primary Alcohol group as in Propanol (CH3-CH2-CH2-OH)', 'Methyl Ketone group (CH3-C(=O)-R)']),
82: ('Aqueous phenol decolorizes bromine water to form a white precipitate. What is the structure of the white precipitate formed?', ['Structure A', 'Structure B', 'Structure C', 'Structure D']),
83: ('The relative strength of carboxylic acid, water, ethanol and phenol has the following order of increasing acid strength:', ['Carboxylic Acid > Phenol > Ethanol > Water', 'Carboxylic Acid > Phenol > Water > Ethanol', 'Phenol > Carboxylic Acid > Ethanol > Water', 'Water > Ethanol > Phenol > Carboxylic Acid']),
84: ('What is the structure of alcohol which on oxidation with acidified Na2Cr2O7 gives phenyl methyl ketone (acetophenone, C6H5-C(=O)-CH3)?', ['Structure A', 'Structure B', 'Structure C', 'Structure D']),
85: ('Which of the following is the structure of ketone?', ['Structure A', 'Structure B', 'Structure C', 'Structure D']),
86: ('The formation of ester from acetic acid in presence of acid and ethanol is a:', ['Nucleophilic substitution reaction', 'Nucleophilic addition reaction', 'Electrophilic substitution reaction', 'Electrophilic addition reaction']),
87: ('Methyl cyanides, on boiling with mineral acids or alkalis yield:', ['Acetic acid', 'Formic acid', 'Propanoic acid', 'Butanoic acid']),
88: ('The amino acids which largely exist in dipolar ionic form are:', ['Acidic amino acids', 'Basic amino acids', 'Beta amino acids', 'Alpha amino acids']),
89: ('CH3-C(=O)-OH + NH3 --heat--> ? The final products formed are:', ['CH3-C(=O)-NH2 + CO2', 'CH3-C(=O)-NH2 + H2O', 'CH3-C(=O)-NH2 + H2', 'CH3-C(=O)-NH2 + HCl']),
90: ('The reaction of two amino acid molecules (glycine + glycine) shown in the figure gives a product called a dipeptide molecule. Which structure correctly represents that dipeptide?', ['Dipeptide structure A', 'Dipeptide structure B', 'Dipeptide structure C', 'Dipeptide structure D']),
91: ('Two or more amino acids condensed to form protein by a peptide linkage which is resent between two atoms:', ['C and C', 'O and C', 'C and N', 'C and H']),
92: ('α-amino acids are compounds having carboxylic acid as well as amino functional groups attached to:', ['Any H-atom in the molecule', 'Same carbon atom', 'Alternate carbon atoms', 'Neighboring carbon atoms']),
93: ("The formula of 'Zwitter ion' is represented by (R = side chain):", ['H3N+-CH(R)-CO-', 'N+H4-CH(R)-CO2-', 'H3N+-CH(R)-CO2-', 'N+H2-CH(R)-COO-']),
94: ("What is the name of amino acid H2N-CH(R)-COOH, where 'R' is CH3 group?", ['Glycine', 'Lysine', 'Aspartic acid', 'Alanine']),
95: ('Polyvinyl acetate (PVA) is colourless and non-toxic resin used as an adhesive and as a binder for making:', ['Toys', 'Gramophone recorders', 'Compact discs', 'Emulsion paints']),
96: ('Both ribose and deoxyribose are monosaccharides containing _______ carbon atoms.', ['Four', 'Six', 'Five', 'Seven']),
97: ('The increased quantities of cholesterol in blood make plaque like deposits in the arteries causing:', ['Cholera', "Down's syndrome", 'Heart attack', 'Phenylketonuria']),
98: ('Polyvinyl chloride is an example of:', ['Condensation polymer', 'Addition polymer', 'Biopolymer', 'Thermosetting polymer']),
99: ('Collagen is a fibrous protein present most abundantly in:', ['Hair', 'Nail', 'Tendons', 'Arteries']),
100: ('Animals store glucose in the form of glycogen in:', ['Stomach', 'Mouth', 'Liver and muscles', 'Small intestine']),
101: ('Aerobic decomposition of organic matter i.e. glucose by bacteria in water sediments produces:', ['Propene', 'Ethane', 'Methane', 'Butane']),
102: ('The yellowish-brown color in photochemical smog is due to the presence of:', ['Sulphur dioxide', 'Carbon monoxide', 'Carbon dioxide', 'Nitrogen dioxide']),
# ----------------------------- ENGLISH (103-132, partial: 103-112) -----------------------------
103: ('Indolence gives vent to ____ disposition in human life.', ['Static', 'Enthusiastic', 'Energetic', 'Filthy']),
104: ("The Quaid's ____ enthusiasm led the Muslims Indo-Pak to independence.", ['Simplified', 'Latent', 'Onerous', 'Threatening']),
105: ('He _____ the incident to the back of his mind.', ['Revered', 'Regulated', 'Reagitated', 'Relegated']),
106: ('He _____ the day they had bought such a large house', ['Hues', 'Rows', 'Rues', 'Dues']),
107: ('Amjad was not conscious to the aberration he had committed in the public meeting. It was disliked by all and sundry. (Spot the error: identify which underlined part is wrong.)', ['to', 'the', 'in', 'by']),
108: ('Late Agha Shahi was an outstanding genius in the international affairs. He was gifted of the acumen to judge the future events, judge the future events in advance. (Spot the error: identify which underlined part is wrong.)', ['in', 'of', 'to', 'in']),
109: ('The old man was sitting quite bamboozled when the swindler deprived him from his pension money by his evil tricks. (Spot the error: identify which underlined part is wrong.)', ['quite', 'from', 'by', 'evil']),
110: ('The prime minister fired a broadside at the opposition leaders. A few of his remarks were not up at the mark. (Spot the error: identify which underlined part is wrong.)', ['of', 'were', 'up', 'at']),
111: ('Lucy is the diva which performance as an opera singer is peerless. (Spot the error: identify which underlined part is wrong.)', ['which', 'as', 'an', 'peerless']),
112: ('The police report exonerated Anwar of all charges of corruption and job was also restored. (Spot the error: identify which underlined part is wrong.)', ['of (charges)', 'of (corruption)', 'also', 'restored']),


# ----------------------------- ENGLISH (103-132) -----------------------------
113: ('We should pay maximum accolade ___ our national heroes.', ['for', 'in', 'to', 'from']),
114: ('Choose the correct sentence: horse latitudes.', ['Does any bodys knows why the latitudes close to the equator are called the horse latitudes?', 'Do any body knows why the latitudes close to the equator are called the horse latitudes?', 'Does any body knows why the latitudes close to the equator are called the horse latitudes?', 'Does any body know why the latitudes close to the equator are called the horse latitudes?']),
115: ('Choose the correct sentence.', ['Shelley is consider to be an idealist poet.', 'Shelley is considering to be an idealist poet.', 'Shelley is considers to be an idealist poet.', 'Shelley is considered to be an idealist poet.']),
116: ('Choose the correct sentence.', ['Pakistan cricket team forged an impregnable lead.', 'Pakistan cricket team forged the impregnable lead.', 'Pakistan cricket team forged against impregnable lead.', 'Pakistan cricket team forged on impregnable lead.']),
117: ('Choose the correct sentence.', ['A person which job involves calculating insurance risks and payments for insurance companies by studying how frequently fires, accidents, death etc. happen is called an actuary.', 'A person who job involves calculating insurance risks and payments for insurance companies by studying how frequently fires, accidents, death etc. happen is called an actuary.', 'A person whose job involves calculating insurance risks and payments for insurance companies by studying how frequently fires, accidents, death etc. happen is called an actuary.', 'A person whose job involves calculating insurance risks and payments for insurance companies by studying how frequently fires, accidents, death etc. happen are called an actuary.']),
118: ('Choose the correct sentence.', ['His addled brain refuse to think clearly and solve the problem.', 'His addle brain refused to think clearly and solve the problem.', 'His addle brain refuse to think clearly and solve the problem.', 'His addled brain refused to think clearly and solve the problem.']),
119: ('Choose the correct sentence.', ['The children had bloomed while their stay on the farm.', 'The children had bloomed during their stay on the farm.', 'The children had bloomed on their stay on the farm.', 'The children was bloomed while their stay on the farm.']),
120: ('Choose the correct sentence.', ['I should had business acumen.', 'I should have business acumen.', 'I should has business acumen.', 'I should may have been business acumen.']),
121: ('Choose the correct sentence.', ['No one is casting aspersions to you.', 'No one is casting aspersions at you.', 'No one is casting aspersions on you.', 'No one is casting aspersions with you.']),
122: ('Choose the correct sentence.', ['This is one of the bifurcated road.', 'This is one of the bifurcated roads.', 'This is one of them bifurcated road', 'This is one off the bifurcated road.']),
123: ('HEINOUS — choose the nearest correct meaning.', ['Heroic', 'Humorous', 'Odious', 'Hone']),
124: ('ILLICIT — choose the nearest correct meaning.', ['Intimate', 'Licentious', 'Illegal', 'Limited']),
125: ('MOTIF — choose the nearest correct meaning.', ['Tough', 'Stuff', 'Motion', 'Design']),
126: ('INCULCATE — choose the nearest correct meaning.', ['Calculate', 'Instill', 'Instigate', 'Stimulate']),
127: ('INIQUITY — choose the nearest correct meaning.', ['Inequality', 'Injustice', 'Wickedness', 'Efficiency']),
128: ('INTRANSIGENT — choose the nearest correct meaning.', ['Parallel', 'Inflexible', 'Adventurous', 'Spirited']),
129: ('LAMPOON — choose the nearest correct meaning.', ['Irk', 'Gratification', 'Lacerate', 'Ridicule']),
130: ('MESMERIZE — choose the nearest correct meaning.', ['Objectify', 'Modify', 'Amalgamate', 'Fascinate']),
131: ('OBLITERATE — choose the nearest correct meaning.', ['Sanctify', 'Obscure', 'Annihilate', 'Oplate']),
132: ('MALEVOLENCE — choose the nearest correct meaning.', ['Empathy', 'Maligning', 'Hostility', 'Management']),

# ----------------------------- BIOLOGY (133-220) -----------------------------
133: ('The simplest independent unit of life is known as:', ['Bacterial colony', 'Cell', 'Chloroplast', 'DNA']),
134: ('The process by which unwanted structures within the cell are engulfed and digested within the lysosome is known as:', ['Endocytosis', 'Exocytosis', 'Hydrolysis', 'Autophagy']),
135: ('The plants having foreign DNA incorporated into their cells are called:', ['Clonal plants', 'Transgenic plants', 'Biotech plants', 'Tissue cultured plants']),
136: ('Pasteurization technique is widely used for preservation of:', ['Water', 'Heat', 'Milk products', 'Vaccines']),
137: ('The production of genetically identical copies of organisms by asexual reproduction is called:', ['Genetic engineering', 'Integrated disease management', 'Hydroponic culture technique', 'Cloning']),
138: ('The _______ model of plasma membrane suggests that proteins are embedded in lipid bilayer:', ['Unit membrane', 'Fluid mosaic', 'Permeable', 'Ultracentrifuge']),
139: ('The function of nucleolus is to make:', ['rDNA', 'Ribosomes', 'RNA', 'Chromosomes']),
140: ('Lipid metabolism is the function of:', ['Mitochondria', 'Sarcoplasmic reticulum', 'RER', 'SER']),
141: ('The enzymes of lysosomes are synthesized on:', ['RER', 'SER', 'Chloroplast', 'Golgi Apparatus']),
142: ('Centrioles are made up of ______ microtubules:', ['9', '27', '3', '12']),
143: ('Which of the following structures is absent in higher plants and found in animal cells:', ['Centriole', 'Cytoskeleton', 'Mitochondria', 'Cytoplasm']),
144: ('The soluble part of cytoplasm or fluid that remains when all organelles are removed is known as:', ['Solution', 'Gelatin material', 'Cytoskeleton', 'Cytosol']),
145: ('The outer membrane of the nuclear envelope is at places continuous with the:', ['Golgi apparatus', 'Endoplasmic Reticulum', 'Lysozymes', 'Peroxisomes']),
146: ("Down's syndrome is a result of non-disjunction of ______ pair of chromosomes that fails to segregate:", ['21st', '22nd', '18th', '24th']),
147: ('______ is most abundant carbohydrate in nature.', ['Waxes', 'Glycerol', 'Starch', 'Cellulose']),
148: ('Which of the following is a keto sugar:', ['Glyceraldehyde', 'Dihydroxy-acetone', 'Ribose', 'Glucose']),
149: ('Amino acid in which the R-group is hydrogen is:', ['Glycine', 'Alanine', 'Leucine', 'Valine']),
150: ('Acyl-glycerols like fats and oils are esters formed by condensation reaction between:', ['Fatty acids and water', 'Fatty acids and alcohols', 'Fatty acids and glucose', 'Fatty acids and phosphates']),
151: ('Which of the following is purine:', ['Guanine', 'Cytosine', 'Thymine', 'Uracil']),
152: ('If the co-factor is covalently or tightly and permanently bonded to enzyme then it will be called:', ['Coenzyme', 'Prosthetic group', 'Activator', 'Apoenzyme']),
153: ('Optimum pH value for the working of pancreatic lipase is:', ['4.50', '7.60', '2.00', '9.00']),
154: ('The view that active site of an enzyme is flexible and when a substrate combines with it, cause changes in enzyme structure is known as:', ['Lock & key model', 'Induce fit model', 'Sliding filament model', 'Specificity model']),
155: ('All coenzymes are derived from:', ['Proteins', 'Nucleic acids', 'Carbohydrate', 'Vitamins']),
156: ('Reverse transcription is used to make DNA copies of:', ['Host RNA', 'Viral RNA', 'Host DNA', 'Viral DNA']),
157: ('Antibiotics are produced by fungi and certain bacteria of group:', ['Actinomycetes', 'Oomycetes', 'Ascomycetes', 'Basidiomycetes']),
158: ('Which statement about bacteria is true:', ['Gram positive bacteria have more lipids in their cell wall', 'Gram negative bacteria have more lipids in their cell wall', 'Lipids are absent in cell wall of both gram positive and negative bacteria', 'Both have equal amount of lipids']),
159: ('Fungi which cause thrush in humans:', ['Sarcomeres', 'Candidiasis', 'Lovastatin', 'Aspergillus']),
160: ('When beef which is not properly cooked is consumed by humans, they become infected by:', ['Tape worm', 'Hook worm', 'Pin worm', 'Round worm']),
161: ('Sleeping sickness in humans is caused by:', ['Trypanosoma', 'Plasmodium', 'Anopheles', 'Andes']),
162: ('Schistosoma is a parasite that lives in the _____ of the host.', ['Intestine', 'Kidney', 'Liver', 'Blood']),
163: ('The cavity between body wall and alimentary canal is:', ['Coelom', 'Mesoderm', 'Endoderm', 'Mesoglea']),
164: ('The layer which forms the lining of digestive tract and glands of digestive system is:', ['Ectoderm', 'Mesoderm', 'Endoderm', 'Mesoglea']),
165: ('Which one of the following vitamins is produced by microflora of large intestine?', ['Vitamin K', 'Vitamin C', 'Vitamin A', 'Vitamin D']),
166: ('_____ is activated to _____ by Enterokinase/enteropeptidase enzyme secreted by the lining of duodenum:', ['Pepsinogen, Pepsin', 'Pepsinogen, Trypsin', 'Trypsinogen, Trypsin', 'Chymotrypsinogen, Chymotrypsin']),
167: ('Which of the following are absorbed in the large intestine?', ['Water and salts', 'Water and peptones', 'Salts and glycerol', 'Amino acids and sugars']),
168: ('Saliva is basically composed of water, mucus, amylase and:', ['Sodium bicarbonate', 'Sodium chloride', 'Sodium hydroxide', 'Hydrocarbons']),
169: ('The total inside capacity of lungs is _____ for man.', ['6.7 liters', '2.5 liters', '7 liters', '5 liters']),
170: ('The average life span of red blood cell is about:', ['Four months', 'Two months', 'Five months', 'One month']),
171: ('The lymphatic vessels of the body empty the lymph into blood stream at the:', ['Abdominal vein', 'Subclavian vein', 'Jugular vein', 'Bile duct']),
172: ('Right atrium is separated from right ventricle by:', ['Tricuspid valve', 'Bicuspid valve', 'Semilunar valve', 'Septum']),
173: ('Site of filtration in nephron is:', ["Glomerulus and Bowman's capsule", 'Proximal and Distal end', 'Ascending and descending arm', 'Loop of Henle']),
174: ('Antidiuretic hormone increases the reabsorption of:', ['Amino acids', 'Salts', 'Ammonia', 'Water']),
175: ('Active uptake of ______ in the ascending limb or thick loop of Henle is promoted by the action of aldosterone:', ['K+', 'Cl-', 'Ca++', 'Na+']),
176: ('The process through which the body maintains the internal environment from the fluctuations of external environment is called as:', ['Behavior of organisms', 'Adaptation', 'Thermoregulation', 'Homeostasis']),
177: ('Active pumping out of Na+ occurs at which part of nephron:', ['Proximal tubule', 'Descending loop of Henle', 'Ascending loop of Henle', 'Collecting ducts']),
178: ('The structures which respond when they are stimulated by impulse coming through motor neuron are:', ['Receptors', 'Responders', 'Transducers', 'Effectors']),
179: ('Thalamus and cerebrum are the part of:', ['Fore brain', 'Mid brain', 'Hind brain', 'Spinal cord']),
180: ("There is also EVIDENCE that high levels of ______ may contribute to the onset of Alzheimer's disease:", ['Mg', 'Mo', 'Al', 'Ca']),
181: ('L-dopa or Levodopa is used to get some relief from??', ['Epilepsy', "Alzheimer's disease", "Parkinson's disease", 'Dementia']),
182: ('Spermatogonia differentiate directly into?', ['Primary spermatocytes', 'Secondary spermatocytes', 'Spermatozoa', 'Spermatids']),
183: ('Treponema palladium causes?', ['AIDS', 'Genital herpes', 'Syphilis', 'Gonorrhea']),
184: ('What is the location of interstitial cells in testes?', ['Inside the seminiferous tubules', 'Between the seminiferous tubules', 'Among the germinal epithelial cells', 'Around the testes']),
185: ('A type of cells in human testes which produce testosterone are called?', ['Germ cells', 'Sertoli cells', 'Interstitial cells', 'Spermatocytes']),
186: ('The hormone produced from corpus luteum is:', ['Prolactin', 'FSH', 'Progesterone', 'LH']),
187: ('The length of myofibril from one Z-band to the next is described as:', ['Sarcolemma', 'Sarcoplasm', 'Sarcomere', 'Muscle fiber']),
188: ('The Ca++ ions released during a muscle fiber contraction attach with:', ['Myosin', 'Actin', 'Troponin', 'Tropomyosin']),
189: ('The joint that allows the movement in several directions is called:', ['Hinge joint', 'Ball and Socket joint', 'Cartilagous joint', 'Fibrous joint']),
190: ("Where can we find H zone in the fine structure of skeletal muscle's myofibril?", ['In the mid of A band', 'In I-band', 'Besides the Z-line', 'Along the I-band']),
191: ('First vertebra of cervical region of vertebral column is known as:', ['Atlas', 'Sacral', 'Thoracic', 'Axis']),
192: ('Chemically insulin and glucagon are:', ['Carbohydrates', 'Proteins', 'Lipids', 'Nucleic acids']),
193: ('Hormones secreted by anterior pituitary and which controls the secretion of hormones of other endocrine glands are known as:', ['Release factor', 'Inhibitor', 'Accelerator', 'Tropic or trophic hormones']),
194: ('Alpha cells of Islets of Langerhans secrete hormone called:', ['Glucocorticoid', 'Insulin', 'Glucagon', 'Aldosterone']),
195: ('Which of the following is the function of glucagon hormone?', ['Glucose to lipids', 'Glucose to proteins', 'Glucose to glycogen', 'Glycogen to glucose']),
196: ('In passive immunity which of the following components are injected into body?', ['Antigens', 'Immunogens', 'Serum', 'Immunoglobulins']),
197: ('Which part of the antibody recognizes the antigen during immune response?', ['Heavy part', 'Variable part', 'Light part', 'Consonant part']),
198: ('Two identical light chains and two identical heavy chains in antibody molecule are linked by:', ['Disulphide bridges', 'Peptide bond', 'Glycerol bond', 'Ionic bond']),
199: ('Antibodies are produced against invading cells by:', ['Lymphocytes', 'Basophils', 'Basophils', 'Neutrophils']),
200: ('In the structure of an antibody molecule, which portion is occupied by variable chains?', ['Lower region', 'Upper region', 'Middle region', 'In between chains']),
201: ('Every molecule of NADH, fed into ETC produces:', ['2 ATP', '3 ATP', '4 ATP', '6 ATP']),
202: ('Final acceptor of electrons in respiratory chain is:', ['Cytochrome a', 'Oxygen', 'Cytochrome a3', 'Cytochrome c']),
203: ('The end product of anaerobic respiration in humans and other mammals is:', ['Pyruvic acid', 'Ethanol', 'Lactic acid', 'Glucose']),
204: ('A biochemical process which occurs within a cell to breakdown complex compounds to produce energy is called:', ['Respiration', 'Photosynthesis', 'Oxidation reduction', 'Photophosphorylation']),
205: ('Which part of chlorophyll molecule absorbs light?', ['Phytol', 'Porphyrin ring', 'Pyrrole', 'Thylakoid membrane']),
206: ('The DNA molecule formed from messenger-RNA by reverse transcriptase is called??', ['Complementary DNA', 'Recombinant DNA', 'Chimeric DNA', 'Plasmid DNA']),
207: ('The agent which separates the two strands of DNA in PCR is??', ['DNA ligase', 'Primer', 'Heat', 'Helicase']),
208: ('Cystic fibrosis patient lack a gene that codes for trans-membrane carrier of??', ['Na+ ions', 'Cl- ions', 'Ca++ ions', 'K+ ions']),
209: ('The phage commonly used as a vector in genetic engineering is?', ['Lambda phage', 'Gamma phage', 'T2 phage', 'T4 phage']),
210: ('Restriction endonucleases are naturally occurring enzymes of:', ['Viruses', 'Bacteria', 'Fungi', 'Plants']),
211: ('In an ecosystem mycorrhizae are an example of:', ['Predation', 'Symbiosis', 'Mutualism', 'Parasitism']),
212: ('As a result of destruction of ozone layer there is significant increase in:', ['Ultra-violet radiations', 'Greenhouse gases', 'Nitrogen oxide', 'Sulphur oxide']),
213: ('Higher rate of a biological activity in a nutrient rich pond water is called:', ['Water pollution', 'Air pollution', 'Eutrophication', 'Industrial effects']),
214: ('Living part of ecosystem is:', ['lithosphere', 'Hydrosphere', 'Community', 'Biosphere']),
215: ('A living association between two living organisms of different species which is beneficial to both the partners is called:', ['Commensalism', 'Parasitism', 'Mutualism', 'Predation']),
216: ('The structures which are reduced during the course of evolution and have no apparent function are called:', ['Regenerated organs', 'Vestigial organs', 'Saltatory organs', 'Useless organs']),
217: ('When a gene suppresses the effect of another gene at another locus the phenomenon is termed as:', ['Over dominance', 'Pleiotropy', 'Epistasis', 'Co-dominance']),
218: ('Phenylketonuria is an example of:', ['Polyploidy', 'Transmutation', 'Inversion', 'Point mutation']),
219: ('A situation in which one gene affects two or more unrelated characters is called:', ['Epistasis', 'Pleiotropy', 'Dominance relation', 'Polygenes']),
220: ('The mutation which causes change in the sequence of DNA is called:', ['Point mutation', 'Chromosomal mutation', 'Deletion', 'Inversion']),
}

KEY_RAW = """
1 c
2 d
3 b
4 b
5 b
6 a
7 a
8 b
9 a
10 c
11 d
12 d
13 a
14 c
15 c
16 c
17 b
18 a
19 c
20 d
21 b
22 a
23 a
24 b
25 c
26 a
27 d
28 c
29 b
30 c
31 c
32 c
33 d
34 a
35 b
36 a
37 c
38 b
39 d
40 b
41 d
42 c
43 c
44 b
45 a
46 b
47 a
48 b
49 b
50 d
51 a
52 a
53 a
54 a
55 c
56 a
57 d
58 b
59 c
60 a
61 d
62 b
63 c
64 d
65 a
66 a
67 c
68 a
69 a
70 b
71 d
72 d
73 c
74 b
75 b
76 d
77 b
78 d
79 b
80 a
81 d
82 a
83 b
84 a
85 b
86 a
87 b
88 d
89 b
90 a
91 c
92 b
93 a
94 d
95 d
96 c
97 c
98 b
99 c
100 c
101 c
102 d
103 a
104 c
105 d
106 c
107 a
108 b
109 b
110 d
111 a
112 a
113 c
114 d
115 d
116 d
117 c
118 d
119 b
120 b
121 c
122 b
123 c
124 b
125 d
126 b
127 c
128 b
129 d
130 d
131 c
132 c
133 b
134 d
135 b
136 c
137 d
138 b
139 b
140 d
141 a
142 b
143 a
144 d
145 b
146 a
147 d
148 b
149 a
150 b
151 a
152 b
153 d
154 b
155 d
156 b
157 a
158 b
159 b
160 a
161 a
162 d
163 a
164 c
165 a
166 c
167 a
168 a
169 d
170 a
171 b
172 a
173 a
174 d
175 d
176 d
177 c
178 d
179 a
180 c
181 c
182 a
183 c
184 b
185 c
186 c
187 c
188 c
189 b
190 a
191 a
192 b
193 d
194 c
195 d
196 d
197 b
198 a
199 a
200 b
201 b
202 b
203 c
204 c
205 b
206 a
207 a
208 b
209 a
210 b
211 b
212 a
213 c
214 d
215 c
216 b
217 c
218 d
219 b
220 a
"""

# ---------------------------------------------------------------------------
# SOURCE VALIDATION
# Original supplied Python source: Q.1-Q.112 (112 MCQs)
# Added from supplied UHS 2013 PDF: Q.113-Q.220 (108 MCQs)
# Final total: 220 MCQs