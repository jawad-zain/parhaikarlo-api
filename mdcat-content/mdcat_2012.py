# -*- coding: utf-8 -*-
# Transcribed from UHS MDCAT 2012 "Entrance Test" paper
# Source: uploaded compilation "MDCAT Past Papers (2008-2016) Solved.pdf"
# Paper pages 1-19 of the 2012 section, followed by the UHS 2012 answer key.
# Total MCQs: 220, Max Marks: 1100, Time Allowed: 150 Minutes
# Question Paper colour for this ID: Blue (candidates fill 'B' against ID).
#
# NUMBERING NOTE:
# One continuous numbering scheme 1-220 across all four subjects:
#   Physics    Q.1   - Q.44
#   Chemistry  Q.45  - Q.102
#   English    Q.103 - Q.132
#   Biology    Q.133 - Q.220
#
# NOTE ON DIAGRAM / GRAPH / STRUCTURE MCQs:
# Several MCQs depend on figures, graphs, circuit symbols, or chemical
# structures in the original scanned pages. Those are listed in DIAGRAM_MCQS.
# The question text/options are preserved where OCR provides them; figure-only
# options are represented by explicit source-figure placeholders.
DIAGRAM_PLACEHOLDER = "[Diagram/graph/structure required — see original PDF page.]"

# CLEANUP PASS (2026-08-18):
# - Q19/29/32/36 added below: their option text is OCR-corrupted fraction/exponent
#   garble (e.g. empty "( )" pairs, stray digits), not usable as-is. DIAGRAM_PLACEHOLDER
#   was appended to their question_text so the DB import/audit pipeline flags and
#   deactivates them pending manual retranscription from the source PDF.
# - Q31/40/44/48 (all- or partial-placeholder options) get the same treatment.
# - The stale Q214 entry below ("Food-web diagram...") was removed: it did not match
#   the actual Q214 content in QUESTIONS (a plain "residual volume of air" recall
#   question that needs no figure) — looked like a copy/paste artifact from another
#   year's file and was corrupting the audit signal for a perfectly good question.
# - Q107-112 (English "SPOT THE ERROR") are handled separately below: the sentence
#   text survived OCR but the [a]/[b]/[c]/[d] underlined-segment boundaries used by
#   this item type (see e.g. mdcat_2016.py Q107-112) did not, so the real option
#   text can't be reconstructed without the source scan. Flagged the same way.
DIAGRAM_MCQS = {
    1: {"subject": "PHYSICS", "orig_num": 1, "notes": 'Solenoid/iron-core and hanging magnet diagram is required.'},
    3: {"subject": "PHYSICS", "orig_num": 3, "notes": 'Two parallel vertical wires with equal/opposite currents and points X, Y, Z are shown in the original figure.'},
    15: {"subject": "PHYSICS", "orig_num": 15, "notes": 'Radioactive alpha/beta/gamma deviation diagram is shown in the source.'},
    19: {"subject": "PHYSICS", "orig_num": 19, "notes": 'OCR-corrupted dimensional-formula options (stray "2 -2" digits, missing exponents) — needs retranscription from source.'},
    20: {"subject": "PHYSICS", "orig_num": 20, "notes": 'Torque diagram: uniform rod OP pivoted at O with force F applied at P at angle theta.'},
    29: {"subject": "PHYSICS", "orig_num": 29, "notes": 'OCR-corrupted SHM equation options (empty "( )" pair in option b) — needs retranscription from source.'},
    31: {"subject": "PHYSICS", "orig_num": 31, "notes": 'Displacement-vs-time SHM graph; PR is a marked interval on the time axis. All four options are figure-only placeholders.'},
    32: {"subject": "PHYSICS", "orig_num": 32, "notes": 'OCR-corrupted Doppler-effect fraction options (all four garbled) — needs retranscription from source.'},
    36: {"subject": "PHYSICS", "orig_num": 36, "notes": 'Mean-square-speed formula options: two are figure-only placeholders, two are OCR-corrupted fraction/exponent text.'},
    40: {"subject": "PHYSICS", "orig_num": 40, "notes": 'Logic-gate symbol options are graphical and are not recoverable as text.'},
    44: {"subject": "PHYSICS", "orig_num": 44, "notes": 'Four graphical I-V curves for a junction diode.'},
    46: {"subject": "CHEMISTRY", "orig_num": 46, "notes": 'Four structural formula options for the amide product.'},
    48: {"subject": "CHEMISTRY", "orig_num": 48, "notes": 'Four structural formula options for alanine. Two of the four are figure-only placeholders.'},
    49: {"subject": "CHEMISTRY", "orig_num": 49, "notes": 'Four structural formula options for alpha-amino-acid classification.'},
    50: {"subject": "CHEMISTRY", "orig_num": 50, "notes": 'Dipeptide skeletal/structural formula is printed above the question.'},
    51: {"subject": "CHEMISTRY", "orig_num": 51, "notes": 'Zwitterion/ionic structural formula options are graphical.'},
    52: {"subject": "CHEMISTRY", "orig_num": 52, "notes": 'Dipeptide structural formula is printed in the stem.'},
    61: {"subject": "CHEMISTRY", "orig_num": 61, "notes": 'Molecular-formula question; options are text and no figure is required, but the source scan should be retained for the exact printed formula values.'},
    81: {"subject": "CHEMISTRY", "orig_num": 81, "notes": 'Reaction equations are printed as formatted chemical equations.'},
    90: {"subject": "CHEMISTRY", "orig_num": 90, "notes": 'Radical options include a graphical chlorine-radical notation.'},
    91: {"subject": "CHEMISTRY", "orig_num": 91, "notes": 'Acyl group is printed as a chemical structure in the stem.'},
    93: {"subject": "CHEMISTRY", "orig_num": 93, "notes": 'Four bromine-intermediate structural formulas are printed.'},
    97: {"subject": "CHEMISTRY", "orig_num": 97, "notes": 'Tertiary/secondary alcohol structural formula is printed.'},
    98: {"subject": "CHEMISTRY", "orig_num": 98, "notes": 'Esterification reaction is printed as a chemical equation.'},
    100: {"subject": "CHEMISTRY", "orig_num": 100, "notes": 'Four cyanohydrin structural formula options are printed.'},
    101: {"subject": "CHEMISTRY", "orig_num": 101, "notes": 'Four structural options for the iodoform test are printed.'},
    102: {"subject": "CHEMISTRY", "orig_num": 102, "notes": 'Four structural formula options for oxidation of ethanol are printed.'},
}

# Fully unrecoverable without the source scan (English "SPOT THE ERROR" segment
# boundaries lost to OCR). Not merged into DIAGRAM_MCQS above since these aren't
# figures — they're documented separately so the reason is clear at a glance.
SPOT_THE_ERROR_UNRESOLVED = {107, 108, 109, 110, 111, 112}

REDACTED_MCQS = {}
REDACTED_PLACEHOLDER = "[Question illegible/blank in source scan.]"

SUBJECTS = [
    ("PHYSICS", 1, 44),
    ("CHEMISTRY", 45, 102),
    ("ENGLISH", 103, 132),
    ("BIOLOGY", 133, 220),
]

QUESTIONS = {
    1: ('The diagram shows a small magnet hanging on a thread near the end of a solenoid carrying a steady current ‘I’: IRON CORE N S What happens to the magnet as the iron core is inserted into the solenoid?', ['It moves towards solenoid and rotates through 180o', 'It moves towards the solenoid', 'It moves away from solenoid', 'It moves away from solenoid and rotates through 180o']),
    2: ('A 10 cm long solenoid has 100 turns. What will be the magnetic field inside it along its axis if one micro ampere current is passed through it?', ['4π x 10-13 tesla', '4π x 10-10 tesla', '4π x 10-7 tesla', '4π x 10-16 tesla']),
    3: ('Two long straight parallel wires held vertically have equal but opposite currents as shown in the figure. I I X Y Z Which of the following effect will be observed?', ['Magnetic field at ‘X’ is stronger than that at ‘Y’ and ‘Z’', 'Magnetic field at ‘X’ is weaker than that at ‘Y’ and ‘Z’', 'Magnetic field at ‘X’, ‘Y’ and ‘Z’ is same', 'Magnetic field at ‘X’ is weaker than that at ‘Y’ but stronger than that at ‘Z’.']),
    4: ('The kinetic energy K.E. with which the electron strikes the target is given by:', ['K.E. = e2V', 'K.E. = hf2', 'K.E. = hc/λ', 'K.E. = eV']),
    5: ('LASER is an acronym for:', ['Light amplification by stimulated emission of radiation', 'Light annihilation by stimulated emission of radiation', 'Light amplitude of stimulated emission of radiation', 'Light amplification by stimulated emission of radio']),
    6: ('X-rays can be produced by bombardment of ____________ on target metal:', ['Protons', 'Neutrons', 'Electrons', 'Alpha particles']),
    7: ('Laser light is monochromatic which means', ['It consists of one ray of light', 'It consists of carbon monoxide gas', 'It consists of one wavelength', 'It consists of photons having 1 eV energy']),
    8: ('If an electron in the ‘K’ shell is removed and an electron from ‘L’ shell jumps to occupy the hole in the ‘K’ shell, it emits a photon of energy:', ['hfKα = EL – EK', 'h/λKα = EL – EK', 'hc = EL – EK', 'hfKα = EK – EL']),
    9: ('Which of the following property must be there in a substance so that it can be used as target in X-ray tube?', ['It must have low melting point', 'It must have high reflecting ability', 'It must have low atomic number', 'It must have high atomic number']),
    10: ('Which of the following can be used to produce population inversion for the emission of Laser?', ['Optical pumping', 'Optical instrument', 'Optical fibre', 'Optical polarization']),
    11: ('What is the charge on alpha particles emitted during the phenomenon of radioactivity?', ['+e', '–2e', '–e', '+2e']),
    12: ('A radioactive nuclide decays by emitting an alpha particle, a beta particle and a gamma ray photon, the change in the nucleon number will be:', ['-4', '-2', '-1', '-3']),
    13: ('A half-life of sodium-24 is _______ which is used to estimate the volume of blood in a patient:', ['6 hours', '8 hours', '15 hours', '15 days']),
    14: ('Which of the following is unit of absorbed dose?', ['Sievert', 'Roentgen', 'Gray', 'Curie']),
    15: ('In a radioactive phenomenon observation shown in figure where α deviates lesser than β in some electric or magnetic field (not shown in figure). What is the reason of less deviation of α? β γ α', ['α is charged particle', 'α is heavier particle', 'α is neutral particle', 'α is lighter particle']),
    16: ('The isotope of Iodine-131 is used in the treatment of', ['Blood cancer', 'Lung tumor', 'Bone cancer', 'Thyroid cancer']),
    17: ('Which of the following effect is observed due to emission of β ― during the phenomenon of radioactivity?', ['A increases by 1 and Z remains same', 'Z decreases by 1 and A remains same', 'Z increases by 1 and A remains same', 'A decreases by 1 and Z remains same']),
    18: ('Electric charge on an object is measured as 5 micro coulombs. How the value of this charge can be expressed in terms of base units:', ['5 x 100 ampere second', '5 x 10+6 coulomb second -6', '5 x 10 ampere second', '5 x 100 coulomb second']),
    19: ('If ‘m’ is the mass, ‘c’ is the velocity of light and x = mc2, then dimensions of ‘x’ will be: ' + DIAGRAM_PLACEHOLDER, ['[LT-1]', '[MLT-1] 2 -2', '[ML T ]', '[MLT-2]']),
    20: ('A force ‘F’ is acting at point ‘P’ of a uniform rod capable to rotate about ‘O’. What is the torque about ‘O’? F ϴ O P', ['(OP)(F tanϴ)', '(OP)(F sinϴ)', '(OP)(F)', '(OP)(F cosϴ)']),
    21: ('An object of mass ‘m’ is suspended in an elevator moving downward with acceleration equal to acceleration due to gravity. What is the apparent weight of object?', ['Zero', 'mg mg', '2mg', '2']),
    22: ('Stokes’ Law for steady motion in a fluid of infinite extent is given by', ['F = 6πηrv', 'F = 6πηr2ρ', 'F = (4/3)πr ρg 3', 'F = 2gr2ρ/9η']),
    23: ('If speed of efflux through a small hole in a large tank is 9.8 m/s. Find the height at the fluid above the hole', ['1 m', '4.9 m', '9.8 m', '19.6 m']),
    24: ('Flow speed of the fluid through a non-uniform pipe increases from 1 m/sec to 3 m/sec. If change in P.E. is zero, then pressure difference between two points will be: (density of the fluid = 1000 kg/m3)', ['1000 N/m2', '8000 N/m2', '9000 N/m 2', '4000 N/m2']),
    25: ('Polarization of light exhibited the nature of light as', ['Longitudinal wave', 'Transverse wave', 'Compressional wave', 'Electromagnetic wave']),
    26: ('The concentration of a sugar solution can be determined by', ['Un-polarized light', 'Interference of light', 'Plane polarized light', 'Diffraction of light']),
    27: ('The information from one place to another can be transmitted very safely and easily by:', ['Copper wire', 'Photodiode', 'Aluminium wire', 'Optical fibre']),
    28: ('The image of an object placed inside the focal length of a convex lens will be largest and clearest when it is at the', ['Less than 25 cm', 'Greater than 25 cm', 'Near point', 'Infinity']),
    29: ('A simple harmonic oscillator has a time period of 10 seconds. Which equation rotates its acceleration ‘a’ and displacement ‘x’? 2π 2 ' + DIAGRAM_PLACEHOLDER, ['a = -2 x', 'a = -( ) x 10', 'a = -(20π)x', 'a = -(20π)2x']),
    30: ('When the length of a simple pendulum is doubled, find the ratio of the new frequency to the old frequency?', ['1/4', '√2', '1/2', '1/√2']),
    31: ('In the diagram below, the displacement of an oscillating particle is plotted against time. What does the length ‘PR’ on the time axis represents? Displacement Time ' + DIAGRAM_PLACEHOLDER, ['Option A (see original source figure/marked segment)', 'Option B (see original source figure/marked segment)', 'Option C (see original source figure/marked segment)', 'Option D (see original source figure/marked segment)']),
    32: ('When the source of sound moves towards the stationary observer, the value of apparent frequency ‘fo’ is: v+ui v ' + DIAGRAM_PLACEHOLDER, ['fo = ( ) f', 'fo = ( )f v v+ui v v-ui', 'fo = ( ) f', 'fo = ( )f v-ui v']),
    33: ('The ratio of tensile strength to tensile strain is called', ['Modulus of elasticity', 'Young’s Modulus', 'Bulk Modulus', 'Shear Modulus']),
    34: ('A wire is stretched by a force ‘F’ which causes an extension ∆l, the energy stored in the wire is:', ['F∆l', '½ F∆l2', '2F∆l', '½ F∆l']),
    35: ('H2 and O2 both are at thermal equilibrium at temperature 300 K. Oxygen molecule is 16 times massive than hydrogen. Root mean square speed of hydrogen is', ['4 root mean square of oxygen', '1/16 root mean square of oxygen', '¼ root mean square of oxygen', '1/6 root mean square of oxygen']),
    36: ('Which of the following is expression of mean square speed of ‘N’ gas molecules contained in a cylinder? v1 + v2 +…+ vx v1 + v2 +…+ vx ' + DIAGRAM_PLACEHOLDER, ['Option A (see original source figure)', '√ N N v1 2 + v2 2 +…+ vx 2 v1 2 + v2 2 +…+ vx 2', 'Option C (see original source figure)', '√ N N']),
    37: ('If ‘Q’ is the amount of heat supplied to a system and ‘W’ is the work done, then change in internal energy can be defined as', ['Q/W', 'W/Q', 'Q – W', '1 + Q/W']),
    38: ('A heat engine operating according to second law of thermodynamics rejects one fourth of the heat taken from high temperature reservoir. What is the percentage efficiency of heat engine?', ['100%', '50%', '25%', '75%']),
    39: ('First law of thermodynamics under adiabatic conditions can be mathematically written as:', ['Q = W', 'Q = U + W', 'Q = ∆U', 'W = ̶ ∆U']),
    40: ('What is the logic symbol for a NOT Gate? ' + DIAGRAM_PLACEHOLDER, ['Option A (see original source figure/marked segment)', 'Option B (see original source figure/marked segment)', 'Option C (see original source figure/marked segment)', 'Option D (see original source figure/marked segment)']),
    41: ('The voltage that is applied across X-plates is provided by a circuit called', ['Audio generator', 'Signal generator', 'Time base generator', 'Linear generator']),
    42: ('What will be the effect on the capacitance of a capacitor if area of each plate is doubled while separation between the plates is halved?', ['Capacitance remains same', 'Capacitance becomes four times', 'Capacitance becomes double', 'Capacitance reduces to half']),
    43: ('10 V potential difference is applied across the plate of 1 µF capacitor. What is the energy storied in capacitor?', ['0.5 mJ', '5 mJ', '0.05 mJ', '50 mJ']),
    44: ('Which one of the following is I-V curve of a junction diode? I I I I V V V V ' + DIAGRAM_PLACEHOLDER, ['Option A (see original source figure/marked segment)', 'Option B (see original source figure/marked segment)', 'Option C (see original source figure/marked segment)', 'Option D (see original source figure/marked segment)']),
    45: ('In the below reaction the nucleophile which attacks on the carbon atom of acid is: O CH3COOH + PCl5 H C C Cl + POCl3 + HCl 3', ['OH–', 'Cl–', 'P', 'H–']),
    46: ('When ethanol chloride reacts with methylamine, an amide is formed. What is the structure of the amide formed? O O', ['H3C CH2 C NH2', 'H3C C NH2 O O', 'H3C CH2 C NHCH3', 'H3C C NHCH3']),
    47: ('Organic compound containing both amine and carboxyl group is known as', ['Amino acid', 'Saccharide', 'Fatty acid', 'Amide']),
    48: ('Alanine is an amino acid which shows neutral effect on litmus paper, the formula of alanine may be H H2N C COOH HOOC CH2 CH COOH ' + DIAGRAM_PLACEHOLDER, ['CH3', 'NH2 H H2N C CH COOH H2C (CH2)3 CH COOH H NH2 NH2 NH2', 'Option C (see original source figure)', 'Option D (see original source figure)']),
    49: ('Which of the following structures is not an alpha amino acid? H2N CH COOH CH2 H3C CH COOH', ['NH2', 'H2N CH COOH', 'H2N CH2 CH2 CH2 CH2 COOH', 'CH2OH']),
    50: ('The skeletal formula of dipeptide formed between aspartic acid and phenylalanine is given below: O NH2 NH HO O O OCH3 How many functional groups are present in its formula?', ['1', '4', '2', '3']),
    51: ('In basic conditions, amino acid exists in which of the following forms? + + -', ['H3N CH2 COOH', 'H3N CH2 COO -', 'H2N CH2 COOH', 'H2N CH2 COO']),
    52: ('Structure of dipeptide is O H2N CH2 C NH HC COOH CH3 This is called:', ['Glycyl glycine', 'Alaninyl alanine', 'Glycyl alanine', 'Alaninyl glycine']),
    53: ('The principle energy storage carbohydrate in animal’s is', ['Glucose', 'Protein', 'Starch', 'Glycogen']),
    54: ('Starch is a polymer of', ['β–D–glucose', 'γ–D–glucose', 'α– –glucose', 'α–L–glucose']),
    55: ('The reaction between fats and caustic soda is called', ['Hydrogenolysis', 'Esterification', 'Fermentation', 'Saponification']),
    56: ('Adipic acid and hexamethylene diamine both of which have _________ carbon atoms:', ['Seven', 'Six', 'Eight', 'Four']),
    57: ('Lactose is a sugar present in milk. It is an example of', ['Disaccharides', 'Polysaccharides', 'Monosaccharides', 'Starch']),
    58: ('Macromolecules are described as large molecules built up from small repeating units called:', ['Monomers', 'Metamers', 'Isomers', 'Tautomers']),
    59: ('The increase in concentration of oxidizing agents in smog like H 2O2, HNO3, PAN and ozone in the air is called', ['Carbonated smog', 'Photochemical smog', 'Nitrated smog', 'Sulphonated smog']),
    60: ('Which is the metal, whose elevated concentration is harmful for fish as it clogs the gills thus causing suffocation?', ['Sodium', 'Zinc', 'Lead', 'Aluminium']),
    61: ('An organic compound has empirical formula C3H3O, if molar mass of compound is 110.15 gmol-1. The molecular formula of this organic compound is (A, of C=12, H=1.008 and O=16)', ['C6H6O2', 'C9H9O3', 'C3H3O', 'C6H6O3']),
    62: ('When 8 grams (4 moles) of H2 react with 2 moles of O2, how many moles of water will be formed?', ['Five', 'Six', 'Four', 'Three']),
    63: ('The number of molecules in 22.4 dm3 of H2 gas at 0 °C and 1 atm are', ['60.2 x 1023', '6.02 x 1025', '6.02 x 10 22', '6.02 x 1022']),
    64: ('Correct order of boiling points of the given liquid is', ['H2O > HF > HCl > NH3', 'H2O > HF > NH3 > HCl', 'HF > H2O > HCl > NH3', 'HF > H2O > NH3 > HCl']),
    65: ('The relative energies of 4s, 4p and 3d orbitals are in the order', ['3d < 4p <4s', '4p < 4s < 3d', '4s < 3d < 4p', '4p < 3d < 4s']),
    66: ('With increase in the value of Principal Quantum Number ‘n’, the shape of the s-orbitals remains the same although their sizes', ['Decrease', 'Remain the same', 'Increase', 'May or may not remain the same']),
    67: ('The angle between unhybridized p-orbital and three sp2 hybrid orbitals of each carbon atom in ether is:', ['120°', '109.5°', '90°', '180°']),
    68: ('In ‘H-F’ bond electronegativity difference is ‘1.9’. What is the type of this bond?', ['Polar covalent bond', 'Pi (π) bond', 'Non-polar covalent bond', 'Co-ordinate covalent bond']),
    69: ('‘∆H’ will be given a negative sign in', ['Exothermic reactions', 'Dissociation reaction', 'Decomposition reactions', 'Endothermic reactions']),
    70: ('Lattice energy of an ionic crystal is the enthalpy of', ['Combustion', 'Dissolution', 'Dissociation', 'Formation']),
    71: ('As number of solute particles increases, freezing point of the solution:', ['Remains the same', 'First increases, then decreases', 'Increases', 'Decreases']),
    72: ('Boiling point constants help us to determine', ['Molar masses', 'Pressures', 'Volumes', 'Masses']),
    73: ('In electrolysis of aqueous CuCl2, the metal deposited at cathode is', ['Sodium', 'Lead', 'Aluminium', 'Copper']),
    74: ('In MgCl2, the oxidation state of ‘Cl’ is', ['Zero', '-2', '+2', '-1']),
    75: ('Formation of NH3 is reversible and exothermic process, what will happen on cooling?', ['More reactant will form', 'More H2 will be formed', 'More N2 will be formed', 'More product (NH3) will be formed']),
    76: ('A buffer solution is that which resists/minimizes the change in', ['pOH', 'pKa', 'pH', 'pKb']),
    77: ('In some reactions, a product formed acts as a catalyst. The phenomenon is called', ['Negative Catalysis', 'Hetergeneous catalysis', 'Activation of Catalyst', 'Autocatalysis']),
    78: ('The reaction rate in forward direction decreases with the passage of time because', ['Concentration of reactants decrease', 'The order of reaction changes', 'Concentration of product decreases', 'Temperature of the system changes']),
    79: ('Which one remains same along a period?', ['Atomic radius', 'Number of shells (orbits)', 'Melting point', 'Electrical conductivity']),
    80: ('More the ionization energy of an element:', ['More the electropositivity', 'Less the metallic character', 'More the reducing power', 'Bigger the atomic radius']),
    81: ('Alkaline earth metal hydroxides decompose on heating. Which of the following reactions is a correct representation of this decomposition?', ['M(OH)2(s) MO(s) + H2O(l)', '2MOH2(s) 2MO(s) + H2(l)', 'MOH(s) M2O(s) + H2O(l)', '4MOH(s) 4M(s) + 2H2O(l) + O2']),
    82: ('Carbon has the unique ability to form long chains by bonding with other carbon atoms. This property of self-linking in carbon is known as:', ['Condensation', 'Cyclization', 'Polymerization', 'Catenation']),
    83: ('Oxidation state of ‘Mn’ in KMnO4, K2MnO4, MnO2 and MnSO4 is in the order:', ['+7, +6, +2, +4', '+7, +6, +4, +2', '+6, +7, +2, +4', '+4, +6, +7, +2']),
    84: ('Which pair of transition elements shows abnormal electronic configuration?', ['Sc and Zn', 'Zn and Cu', 'Cu and Sc', 'Cu and Cr']),
    85: ('The acid rain water has pH:', ['Below 5', 'Between 5 and 7', '7', 'Between 7 and 14']),
    86: ('In Contact Process for manufacturing sulphuric acid, Sulphur trioxide (SO 3) is not absorbed in water because', ['The reaction does not go to completion', 'The reaction is quite slow', 'The reaction is highly exothermic', 'SO3 is insoluble in water']),
    87: ('In modern Haber Process Plants, the temperature maintained during the process is', ['670 – 770 K (400 °C – 500 °C)', '370 – 470 K (100 °C – 200 °C)', '270 – 370 K (0 °C – 100 °C)', '570 – 600 K (300 °C – 380 °C)']),
    88: ('In the Haber process for manufacturing of ammonia, Nitrogen is taken from', ['Proteins occurring in living bodies', 'Air', 'Ammonium salts obtained industrially', 'Minerals containing nitrates']),
    89: ('Ethene on polymerization, gives the product polyethene. This reaction may be called as', ['Addition', 'Substitution', 'Condensation', 'Pyrolysis']),
    90: ('In the following, which one is free radical?', ['Cl―', 'Cl2', 'Cl+', 'Clo O +']),
    91: ('The introduction of R C group in benzene is called', ['Acylation', 'Alkylation', 'Carbonyl reduction', 'Formylation']),
    92: ('The alkaline hydrolysis of bromoethane shown below gives alcohol as the product: H3C―CH2―Br H3C―CH2―OH The reagent and the condition used in this reaction may be:', ['H2O at room temperature', 'KOH in alcohol', 'Ethanol, heat', 'Dilute NaOH(aq) warm']),
    93: ('In the reaction of ethane with bromine the intermediate formed is + H C CH H2 C CH2 2 2 +', ['Br', 'Br - H2 C CH2', 'Br', 'H2C CHBr']),
    94: ('In substitution reactions, dihaloalkane or secondary halogenoalkane give / show:', ['SN1 Mechanism', 'Both E1 and E2', 'SN2 Mechanism', 'Both SN1 and SN2']),
    95: ('The dehydration of ethyl alcohol with concentrated H2SO4 at 140°C gives:', ['Ethene', 'Alcohol', 'Diethyl ether', 'Carboxylic acid']),
    96: ('Ethanol can be converted in to ethanoic acid by:', ['Oxidation', 'Hydration', 'Fermentation', 'Hydrogenation']),
    97: ('The following structure is of: R R C OH R', ['Secondary alcohol', 'Tertiary alcohol', 'Primary alcohol', 'Carboxylic acid']),
    98: ('When ethanol is warmed with ethanoic acid in the presence of strong acid catalyst, an ester ethyl ethanoate is formed. CH3CH2OH + CH3CO2H CH3CO2CH2CH3 During this reaction:', ['Alcohol is reduced', 'O ̶ H bond in ethanol is broken', 'O ̶ H bond in ethanoic acid is broken', 'Acid is oxidized']),
    99: ('Primary alcohols normally give us aldehydes when oxidized in the presence of Na 2Cr3O7, what the product will be, when the secondary alcohols are oxidized in same conditions?', ['Alkenes', 'Alkyl halides', 'Alkynes', 'Ketones']),
    100: ('Formaldehyde reacts with HCN (NaCN + HCl) to give a compound: H C 3 OH H3 C OH C C CN', ['H CN', 'H3C H OH O C', 'H CN', 'H3C C CN']),
    101: ('Iodoform test will not be positive with: O', ['H3C CH2 C CH2 CH3', 'C2H5 OH O O', 'H3C CH2 C CH3', 'H3C C H']),
    102: ('When CH3―CH2―OH is oxidized in the presence of K2Cr2O7 and H2SO4, the product formed is O O', ['H3C C OH', 'H3C C CH3 O O', 'H C OH', 'H3C C OCH3']),
    103: ('He had a heart attack and all attempts to _________ him failed.', ['Renew', 'Revise', 'Resuscitate', 'Refurnish']),
    104: ('The _________ stench of dead animals and plants made Mumtaz ill.', ['Putrid', 'Perturbed', 'Purified', 'Purchased']),
    105: ('While going up the hills, by bus, she felt __________ inside.', ['Fishy', 'Queasy', 'Itchy', 'Squeezy']),
    106: ('The craft statesman manipulated the situation by making false promises and declaring sport festivities as a __________ to fool the public.', ['Red-Hearing', 'Red-Herring', 'Red-Feather', 'Red-Haring']),
    # Q107-112: "SPOT THE ERROR" item type (see mdcat_2016.py Q107-112 for the format).
    # The sentence text survived OCR; the [a]/[b]/[c]/[d] underlined-segment markers
    # did not, so the four option strings can't be reconstructed from this source and
    # are left as explicit placeholders (see SPOT_THE_ERROR_UNRESOLVED above).
    107: ('SPOT THE ERROR: The theory was discarded as there was no corroborating evidence for its favour. ' + DIAGRAM_PLACEHOLDER, ['Option A (see original source figure/marked segment)', 'Option B (see original source figure/marked segment)', 'Option C (see original source figure/marked segment)', 'Option D (see original source figure/marked segment)']),
    108: ('SPOT THE ERROR: The workers were raising much hue and cry when their demands were turned away. ' + DIAGRAM_PLACEHOLDER, ['Option A (see original source figure/marked segment)', 'Option B (see original source figure/marked segment)', 'Option C (see original source figure/marked segment)', 'Option D (see original source figure/marked segment)']),
    109: ('SPOT THE ERROR: Aslam was badly cudgeled from his step-brother. He received many bruises and contusions. Thank God! No ' + DIAGRAM_PLACEHOLDER, ['Option A (see original source figure/marked segment)', 'Option B (see original source figure/marked segment)', 'Option C (see original source figure/marked segment)', 'Option D (see original source figure/marked segment)']),
    110: ('SPOT THE ERROR: I extend a cordial invitation for you to visit our farm house. We have grown vegetables without chemical ' + DIAGRAM_PLACEHOLDER, ['Option A (see original source figure/marked segment)', 'Option B (see original source figure/marked segment)', 'Option C (see original source figure/marked segment)', 'Option D (see original source figure/marked segment)']),
    111: ('SPOT THE ERROR: Although he is not a close relative of me, yet I was greeted with a show of deep cordiality. ' + DIAGRAM_PLACEHOLDER, ['Option A (see original source figure/marked segment)', 'Option B (see original source figure/marked segment)', 'Option C (see original source figure/marked segment)', 'Option D (see original source figure/marked segment)']),
    112: ('SPOT THE ERROR: This antibiotic destroys red corpuscles in the blood and cause pernicious anaemia. ' + DIAGRAM_PLACEHOLDER, ['Option A (see original source figure/marked segment)', 'Option B (see original source figure/marked segment)', 'Option C (see original source figure/marked segment)', 'Option D (see original source figure/marked segment)']),
    # Q113-122: "Choose the CORRECT sentence" item type — identical shared stem across
    # every MDCAT year (see e.g. mdcat_2014.py / mdcat_2016.py). The stem was dropped
    # by this source's OCR/parse pass; restored verbatim, options unchanged.
    113: ('Choose the CORRECT sentence:', ['Why does not Nomana remained true to her husband?', 'Why did not Nomana remain true to her husband?', 'Why had not Nomana remain true to her husband?', 'Why did not Nomana remained true to her husband?']),
    114: ('Choose the CORRECT sentence:', ['All my childhood, I longed desperately in for a tricycle.', 'All my childhood, I longed desperately to a tricycle.', 'All my childhood, I longed desperately for a tricycle.', 'All my childhood, I longed desperately at a tricycle.']),
    115: ('Choose the CORRECT sentence:', ['She felt unreal to the voice informed her of the subway accident.', 'She felt unreal as the voice informed her of the subway accident.', 'She felt unreal that the voice informed her of the subway accident.', 'She felt unreal for the voice informed her of the subway accident.']),
    116: ('Choose the CORRECT sentence:', ['Bill Gates is one of the wealthiest person in the world.', 'Bill Gates is one of the wealthy person in the world.', 'Bill Gates is one of the wealthiest persons in the world.', 'Bill Gates is one of the more wealthy person in the world.']),
    117: ('Choose the CORRECT sentence:', ['Her father is a SP in the Punjab Police.', 'Her father is an SP in the Punjab Police.', 'Her father was a SP in the Punjab Police.', 'Her father are a SP in the Punjab Police.']),
    118: ('Choose the CORRECT sentence:', ['There were musical instruments in the shop.', 'There has musical instruments in the shop.', 'There was musical instruments in the shop.', 'There is musical instruments in the shop.']),
    119: ('Choose the CORRECT sentence:', ['He died for heart attack in 1982.', 'He died in heart attack in 1982.', 'He died with heart attack in 1982.', 'He died of heart attack in 1982.']),
    120: ('Choose the CORRECT sentence:', ['Always speak in the truth.', 'Always tell the truth.', 'Always tell for the truth.', 'Always telling truth.']),
    121: ('Choose the CORRECT sentence:', ['Hand up the answer sheet to me.', 'Hand down the answer sheet to me.', 'Hand over the answer sheet to me.', 'Hand for the answer sheet to me.']),
    122: ('Choose the CORRECT sentence:', ['Are you noticed the peach blossoms?', 'Will you noticed the peach blossoms?', 'Have you noticed the peach blossoms?', 'Were you noticed the peach blossoms?']),
    123: ('DISSONANCE', ['Inconsistency', 'Perceptible', 'Expansion', 'Warp']),
    124: ('TRIFLE', ['Pudding', 'Deluge', 'Minor', 'Treble']),
    125: ('MURKY', ['Dusty', 'Clear', 'Squeamy', 'Unclear']),
    126: ('FAUX', ['Blunder', 'Indiscretion', 'Mistake', 'False']),
    127: ('MYRIAD', ['Countable', 'Measured', 'Multitude', 'Blurred']),
    128: ('FACILE', ['Fallacy', 'Delicate', 'Depict', 'Superficial']),
    129: ('MAGNUM', ['Masterpiece', 'Modest', 'Magnanimity', 'Magnetic']),
    130: ('SIDLE', ['Sneak', 'Siege', 'Sift', 'Sieve']),
    131: ('PLETHORA', ['Plastic', 'Measure', 'Super-fluidity', 'Malleable']),
    132: ('VERTEX', ['Poetry', 'Zenith', 'Depth', 'Diminish']),
    133: ('The part of neuron fibre which conducts nerve impulses from the cell body is', ['Dendron', 'Axon', 'Dendrites', 'Peripheral branch']),
    134: ('The number of cranial nerves in human is', ['31 pairs', '24 pairs', '12 pairs', '62 pairs']),
    135: ('The part of brain which controls breathing, heart rate and swallowing is', ['Cerebrum', 'Medulla', 'Cerebellum', 'Hypothalamus']),
    136: ('Syphilis is a sexually transmitted disease which is caused by', ['Neisseria gonorrhoeae', 'Treponema pallidum', 'E. coli', 'Mycobacterium avium']),
    137: ('Discharge of ovum or secondary oocyte from ovary or from Graafian follicle is called', ['Fertilization', 'Follicle formation', 'Pollination', 'Ovulation']),
    138: ('Second meiotic division in the secondary oocyte proceeds as far as', ['Metaphase', 'Anaphase', 'Prophase', 'Telophase']),
    139: ('Which one of the following differentiates directly into mature sperm?', ['Primary spermatocyte', 'Spermatogonia', 'Secondary spermatocyte', 'Spermatid']),
    140: ('Uterus opens into the vagina through', ['Cervix', 'External genitalia', 'Fallopian tube', 'Vulva']),
    141: ('Each muscle fibre is surrounded by membrane which is called', ['Sarcomere', 'Twitch fibre', 'Sarcolemma', 'Capsule']),
    142: ('When calcium ions are released from the sarcoplasmic reticulum they bind with ________ during muscle contraction', ['Tropomyosin', 'Cytosol’s ions', 'Sarcolemma', 'Troponin']),
    143: ('Human and mammalian skeleton can be divided into two parts, axial skeleton and', ['Appendicular skeleton', 'Endoskeleton', 'Exoskeleton', 'Hydrostatic skeleton']),
    144: ('Last four vertebrae in humans are fused to form a structure called', ['Sacrum', 'Pubis', 'Cervical vertebrae', 'Coccyx']),
    145: ('How many bones are involved in the formation of each half of pelvic girdle?', ['3 bones', '2 bones', '4 bones', '1 bone']),
    146: ('Ductless glands are known as', ['Endocrine gland', 'Salivary glands', 'Exocrine gland', 'Bile glands']),
    147: ('Gastrin is the hormone which is produced by the', ['Liver', 'Pyloric region of stomach', 'Adrenal gland', 'Mucosal lining of intestine']),
    148: ('β-cells of liver secrete a hormone that is called', ['Insulin', 'Antidiuretic hormone', 'Glucagon', 'Gastrin']),
    149: ('Vasopressin and Oxytocin are released from the', ['Placenta', 'Anterior pituitary', 'Ovary', 'Posterior pituitary']),
    150: ('Antigen is a foreign protein or any other molecule which stimulates the formation of', ['MHC complex', 'Mucus', 'Immunogen', 'Antibodies']),
    151: ('Antibodies are produced by which of the following lymphocytes?', ['B lymphocytes', 'T lymphocytes', 'A lymphocytes', 'B and T lymphocytes']),
    152: ('T-lymphocytes become mature and competent under the influence of', ['Liver', 'Thymus gland', 'Bursa of fabricius', 'Spleen']),
    153: ('Skin and mucous membranes are part of the body defense system and they form the', ['Physical barrier', 'Chemical barriers', 'Mechanical barriers', 'Biological barriers']),
    154: ('Snake bite is treated with which type of immunization?', ['Active', 'Humoral', 'Passive', 'Specific']),
    155: ('The product(s) of cyclic photophosphorylation is / are:', ['ATP', 'NADP and ATP', 'NADP', 'NADP, ATP, and O2']),
    156: ('Total NADH formed by one glucose molecule during Krebs’s Cycle are', ['6', '8', '3', '18']),
    157: ('The terminal electron acceptor in electron transport chain is', ['Hydrogen', 'Cytochrome', 'Iron', 'Oxygen']),
    158: ('The end product of glycolysis is', ['ADP', 'Citric acid', 'Reduced FAD', 'Pyruvate']),
    159: ('One molecule of FADH2 is produced in Krebs’s cycle during conversion of', ['Fumarate Malate', 'Malate Oxaloacetate', 'Succinate Fumarate', 'α-Ketoglutarate Succinate']),
    160: ('In recombinant DNA technology _________ are tools for manipulating DNA', ['Viruses', 'Enzymes', 'Chromosomes', 'Genes']),
    161: ('In DNA finger printing process, the use of __________ produces distinctive pattern on autoradiography or X-ray film', ['Restriction enzyme', 'Macrosatellites', 'Microsatellites', 'Probes for genetic markers']),
    162: ('In the recombinant DNA technology plasmids are used as', ['Genetic material', 'Vectors', 'Enzymes', 'Probes']),
    163: ('In which process, multiple copies of the desired genes are produced?', ['Polymerase chain reaction', 'Analyzing DNA', 'Gene sequencing', 'DNA finger printing']),
    164: ('The enzyme adenosine deaminase is missing in person suffering from:', ['Cystic fibrosis', 'Severe combined immunodeficiency syndrome', 'Hypercholesterolemia', 'Parkinson’s disease']),
    165: ('What is the niche of an organism in an ecosystem?', ['Role played by many organisms in an ecosystem', 'Role played by community of microorganisms in their ecosystem', 'Role played by a dead organism in an ecosystem', 'Role played by an organism in its ecosystem.']),
    166: ('The distinct levels or links of food chain are called', ['Trophic level', 'Energy pyramid', 'Food web', 'Food chain']),
    167: ('A relationship between two or more organisms of different species in which all partners get benefit is called', ['Symbiosis', 'Commensalism', 'Parasitism', 'Predation']),
    168: ('Bacteria and fungi are examples of', ['Producers', 'Consumers', 'Decomposers', 'Denvers']),
    169: ('The cause of acid rain is', ['Oxides of carbon', 'Oxides of Sulphur', 'Oxides of nitrogen and Sulphur', 'Oxides of nitrogen']),
    170: ('When the presence of a gene at one locus suppresses the effect of a gene at another locus, the phenomenon is called', ['Hypostasis', 'Epistasis', 'Pleiotropy', 'Epitropy']),
    171: ('The gene for ABO-blood group systems in humans is represented by symbol:', ['X', 'Y', 'I', 'O']),
    172: ('When a single gene affects two or more traits, the phenomenon is called', ['Epistasis', 'Dominance', 'Pleiotropy', 'Over dominance']),
    173: ('The comparative embryology of all vertebrates shows development of', ['Hairs', 'Scales', 'Gill pouches', 'Fins']),
    174: ('In men, sex-determination depends upon the nature of', ['Heterogametic male', 'Heterogametic female', 'Homogametic female', 'Homogametic male']),
    175: ('Population of different species (plants and animals) living in the same habitat form a', ['Community', 'Biosphere', 'Ecosystem', 'Microhabitat']),
    176: ('The part of the body which forms a structural and functional unit and is composed of more than one tissue is called', ['Organ', 'Organ system', 'Organelle', 'Whole organism']),
    177: ('A method in which pests are destroyed by using same living organisms or natural enemies is called', ['Pasteurization', 'Biological control', 'Integrated disease management', 'Genetic engineering']),
    178: ('Chemicals produced by microorganisms which are capable of destroying the growth of microbes are called', ['Antigen', 'Antiseptics', 'Biocidal', 'Antibiotics']),
    179: ('Plastids are only found in the', ['Animals and Plants', 'Plants', 'Animals', 'Viruses']),
    180: ('Plasma membrane is chemically composed of', ['Phospholipids only', 'Lipids and carbohydrates', 'Lipids and proteins', 'Glycoproteins']),
    181: ('Endoplasmic reticulum contains a system of flattened membrane-bounded sacs which are named as', ['Cristae', 'Cisternae', 'Marks', 'Tubules']),
    182: ('Lipids synthesis / metabolism takes place in which of the following organelle?', ['Mitochondria', 'Rough endoplasmic reticulum', 'Vacuoles', 'Smooth endoplasmic reticulum']),
    183: ('Ribosomes exist in two forms, either attached with RER or freely dispersed in the', ['Tonoplast', 'Cytoplasm', 'Golgi bodies', 'SER']),
    184: ('Exchange of segments between homologous chromosomes is called', ['Segregation', 'Crossing over', 'Independent assortment', 'Mutation']),
    185: ('If a person has 44 autosomes + XXY, he will suffer from', ['Klinefelter’s syndrome', 'Turner’s syndrome', 'Down’s syndrome', 'Edward’s syndrome']),
    186: ('The ribosomal RNA is synthesized and stored in', ['Endoplasmic reticulum', 'Golgi complex', 'Nucleolus', 'Chromosomes']),
    187: ('In which stage of Interphase, there is increase in cell size and many biochemical are formed?', ['G2 phase', 'S phase', 'G1 phase', 'C phase']),
    188: ('In Down’s syndrome, which one of the following pair of chromosome fails to segregate?', ['7', '21', '18', '19']),
    189: ('Carbohydrates are organic molecules and contain three elements', ['Carbon, water and oxygen', 'Carbon, calcium and hydrogen', 'Carbon, Sulphur and hydrogen', 'Carbon, hydrogen and oxygen']),
    190: ('Which one are intermediates in respiration and photosynthesis both?', ['Ribose and heptolose', 'Glucose and galactose', 'Glyceraldehydes and dihydroxyacetone', 'Fructose and ribulose']),
    191: ('Which of the following is a peptide bond?', ['–C–N', '–C–P', '–C–O', '–C–S']),
    192: ('Which of the following is an unsaturated fatty acid?', ['Acetic Acid', 'Oleic acid', 'Butyric acid', 'Palmitic acid']),
    193: ('Which of the following combination of base pair is absent in DNA?', ['A–T', 'A–U', 'C–G', 'T–A']),
    194: ('The type of inhibition in which inhibitor has no structural similarity to substrate and combines with enzyme at other than the active site is called', ['Irreversible inhibition', 'Non-competitive and reversible inhibition', 'Competitive inhibition', 'Reversible inhibition']),
    195: ('The inhibitors that bind tightly and permanently to enzymes and destroy their globular structure and catalytic activity are', ['Reversible inhibitors', 'Competitive inhibitors', 'Irreversible inhibitors', 'Non-competitive inhibitors']),
    196: ('Enzyme succinate dehydrogenase converts succinate into', ['Malate', 'Citrate', 'Malonic acid', 'Fumarate']),
    197: ('If the detachable co-factor is an inorganic ion then it is designated as', ['Coenzyme', 'Holoenzyme', 'Prosthetic group', 'Activator']),
    198: ('In HIV viruses, reverse transcriptase converts single-stranded RNA into double stranded viral DNA. This process is called', ['Translation', 'Replication', 'Duplication', 'Reverse Transcriptase']),
    199: ('Mesosomes are infoldings of the cell membrane and are involved in', ['DNA replication', 'Protein synthesis', 'RNA synthesis', 'Metabolism']),
    200: ('Most widespread problem of the antibiotics misuse is the', ['Rapid cure', 'Disturbance of metabolism', 'Increased resistance in pathogen', 'Immunity']),
    201: ('Which of the following component is found in the cell wall of fungi?', ['Cellulose', 'Proteins', 'Chitin', 'Glycerol']),
    202: ('The male reproductive parts of the flower are called', ['Gynoecium', 'Androecium', 'Calyx', 'Corolla']),
    203: ('Fasciola is the name given to', ['Tapeworm', 'Liver fluke', 'Planaria', 'Earthworm']),
    204: ('Ascaris is', ['Diploblastic', 'Haploid', 'Triploblastic', 'Acoelomate']),
    205: ('During development, in an animal, mesoderm layer gives rise to', ['Nervous System', 'Muscular and skeletal system', 'Alimentary canal lining', 'Mouth']),
    206: ('Polymorphism is characteristic feature of', ['Porifera', 'Annelida', 'Cnidaria', 'Nematodes']),
    207: ('The muscles of the stomach walls thoroughly mix up the food with gastric juices and the resulting semi-solid / semi-liquid material is called', ['Bolus', 'Mucus', 'Bolus or chime', 'Chyme']),
    208: ('Trypsinogen is converted into trypsin by the activity of', ['Goblet cells', 'Enterokinase', 'Absorptive cells', 'Peptidase']),
    209: ('In large intestines, vitamin K is formed by the activity of', ['Symbiotic bacteria', 'Parasitic bacteria', 'Obligate parasite', 'Facultative bacteria']),
    210: ('Goblet cells secrete', ['HCl', 'Enzymes', 'Mucus', 'Amylase']),
    211: ('Mature mammalian red blood cells do not have', ['Nucleus', 'Fluids', 'Red color', 'Haemoglobin']),
    212: ('In a normal person plasma constitutes about ___________ by volume of blood', ['50%', '45%', '60%', '55%']),
    213: ('Which vein has oxygenated blood?', ['Renal vein', 'Pulmonary vein', 'Subclavian vein', 'Jugular vein']),
    214: ('What is the residual volume of air which always remains inside the lungs of human?', ['3.5 Liters', '5.0 Liters', '0.5 Liters', '1.5 Liters']),
    215: ('In nephron, most of the reabsorption takes place in the', ['Distal tubule', 'Ascending limb', 'Proximal tubule', 'Descending limb']),
    216: ('Detection of change and signaling for effector’s response to the control system is a', ['Negative feedback', 'Inter-coordination', 'Positive feedback', 'Feedback mechanism']),
    217: ('What are three components of mechanism of homeostatic regulations?', ['Receptors, control centre and effectors', 'CNS, PNS and diffused nervous system', 'Sensory, motor and associative neurons', 'Cerebrum, cerebellum and pons']),
    218: ('Blood enters the glomerulus through', ['Efferent arteriole', 'Renal artery', 'Afferent arteriole', 'Renal vein']),
    219: ('Which portion of nephron is under the control of ADH?', ['Bowman’s capsule', 'Distal and collecting ducts', 'Ascending arm', 'Descending arm']),
    220: ('Cause of Parkinson’s disease is death of brain cells that produce', ['Dopamine', 'ADH hormone', 'Acetylcholine', 'Oxytocin']),
}

KEY_RAW = """
1 b
2 c
3 a
4 d
5 a
6 b
7 b
8 a
9 d
10 a
11 d
12 a
13 b
14 b
15 c
16 d
17 b
18 b
19 b
20 d
21 a
22 a
23 c
24 d
25 c
26 b
27 d
28 b
29 c
30 d
31 b
32 b
33 c
34 d
35 a
36 a
37 b
38 d
39 d
40 a
41 b
42 c
43 b
44 b
45 c
46 d
47 a
48 a
49 b
50 c
51 d
52 b
53 d
54 b
55 d
56 c
57 a
58 a
59 c
60 d
61 a
62 b
63 d
64 c
65 b
66 b
67 a
68 a
69 a
70 d
71 d
72 a
73 d
74 d
75 d
76 b
77 d
78 a
79 c
80 c
81 a
82 d
83 c
84 d
85 a
86 b
87 a
88 c
89 a
90 d
91 a
92 d
93 a
94 d
95 b
96 a
97 a
98 c
99 d
100 b
101 a
102 a
103 b
104 a
105 c
106 c
107 d
108 d
109 a
110 a
111 a
112 d
113 b
114 c
115 b
116 c
117 c
118 a
119 d
120 c
121 b
122 b
123 a
124 b
125 d
126 d
127 b
128 d
129 a
130 a
131 b
132 c
133 c
134 b
135 c
136 c
137 d
138 a
139 d
140 a
141 b
142 d
143 a
144 d
145 a
146 a
147 b
148 x
149 d
150 d
151 a
152 c
153 a
154 b
155 a
156 a
157 d
158 d
159 b
160 c
161 d
162 c
163 a
164 c
165 d
166 a
167 a
168 b
169 b
170 c
171 b
172 b
173 b
174 a
175 a
176 b
177 a
178 b
179 b
180 d
181 c
182 c
183 d
184 c
185 a
186 c
187 a
188 d
189 d
190 a
191 b
192 d
193 b
194 c
195 b
196 a
197 d
198 d
199 c
200 d
201 c
202 c
203 a
204 b
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
216 d
217 a
218 b
219 c
220 a
"""

# Completeness: 220/220 questions and 220/220 answer-key entries (Q148's key is
# unresolved -- printed as 'x' in the source, preserved as-is, not guessed).
# Source paper: supplied PDF pages 76-94; answer key: page 95 of the compiled PDF.
#
# CLEANUP PASS (2026-08-18) summary — see convert_2012_to_json.py for how these
# translate into is_active/needs_review on import:
#   - Mechanical bleed-text fixes (no content change to the real answer options):
#     Q106 opt D, Q122 opt D (both had the next section's boilerplate instructions
#     glued onto them by the OCR/parse pass).
#   - Recovered dropped shared stems (verbatim, matches every other year's file):
#     Q107-112 "SPOT THE ERROR: " prefix, Q113-122 "Choose the CORRECT sentence:".
#   - Flagged unresolved/unusable content (OCR-corrupted or figure-only options) via
#     DIAGRAM_PLACEHOLDER — these need the original 2012 PDF page to fix for real:
#     Q19, Q29, Q31, Q32, Q36, Q40, Q44, Q48, Q107-112 (14 questions total).
#   - Removed a stale/mismatched DIAGRAM_MCQS[214] annotation that referred to
#     content not actually present in this paper's Q214.
#   - No source PDF/scans for 2012 are present in this repo (unlike e.g. 2013's
#     mdcat-content/tmp_2013/), so no images could actually be cropped/sourced in
#     this pass -- the 14 flagged questions above stay inactive until source pages
#     are supplied.