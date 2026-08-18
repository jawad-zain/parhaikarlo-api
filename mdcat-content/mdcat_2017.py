# -*- coding: utf-8 -*-
# Transcribed from UHS MDCAT 2017 "Entrance Test" paper
# Source: uploaded compilation "Paper_MDCaT_2017_.pdf" (compiled by Noor Mobin,
# University of Health Sciences, Lahore) - FB Group "MCAT 2017" / FB Page
# "MCAT Notes and Papers"
# Total MCQs: 220, Max Marks: 1100, Time Allowed: 150 Minutes
# Question Paper colour for this ID: Blue
#
# NUMBERING NOTE:
# The source document numbers each subject's questions starting at 1
# (Biology 1-88, Physics 1-44, English 1-30, Chemistry 1-58), in that
# page order. To match the single continuous-numbering convention used
# in the 2019 transcription script, all 220 questions have been
# renumbered here as one continuous sequence 1-220, in the same subject
# order the paper presents them (Biology, Physics, English, Chemistry).
# SUBJECTS below maps each continuous-numbering range back to its
# original subject and its original in-subject question number is noted
# in each QUESTIONS comment where helpful.
#
# NOTE ON DIAGRAM / GRAPH MCQs:
# Several MCQs depend on a figure, graph, or labeled diagram shown in the
# original scanned pages (ECG trace, circuit diagrams, force-distance
# loops, energy-vs-reaction-coordinate curves, boiling-point/melting-point
# scatter plots, organic structures, etc.) that could not be reliably
# transcribed as text. These are listed in DIAGRAM_MCQS below with a
# needs_review flag. Where the official answer key still provides a
# letter for these (most of them do), that letter is kept in KEY_RAW,
# but the option that was image-only has been replaced with the
# DIAGRAM_PLACEHOLDER text and should be checked against the original
# PDF page before use.
DIAGRAM_PLACEHOLDER = "[Diagram/graph required \u2014 not transcribable from OCR text. See original PDF page for the figure.]"

DIAGRAM_MCQS = {
    8: {
        "subject": "BIOLOGY", "orig_num": 8,
        "notes": "ECG trace diagram (P-Q-R-S-T wave). Question asks what the QRS wave represents. Answer (a, Ventricular systole) is standard physiology and not really diagram-dependent, but the figure itself is image-only.",
    },
    84: {
        "subject": "BIOLOGY", "orig_num": 84,
        "notes": "Diagram of stomach/duodenum with oesophagus, labelled point 'a' at the junction. Answer inferred as (d) Pyloric sphincter is NOT confirmed by the figure alone; kept per official key.",
    },
    86: {
        "subject": "BIOLOGY", "orig_num": 86,
        "notes": "Diagram of gastric gland structure in stomach wall with zymogen cells labelled, point 'x' unlabeled. Needs figure to confirm answer (d, Oxyntic cells).",
    },
    87: {
        "subject": "BIOLOGY", "orig_num": 87,
        "notes": "Diagram of lungs/chest cavity with part 'Y' marked by an arrow at the bottom. Needs figure to confirm answer (b, Diaphragm).",
    },
    94: {
        "subject": "PHYSICS", "orig_num": 6,
        "notes": "Force (F) vs distance (d) graph showing a closed loop (values 2-6 on both axes) representing work done over a cycle. Needs figure to confirm answer (d, Zero Nm) - consistent with net work over a closed F-d loop area interpretation, but figure needed to verify enclosed area/scale.",
    },
    109: {
        "subject": "PHYSICS", "orig_num": 21,
        "notes": "Four F-vs-x graphs (options A-D) shown as a handwritten image; one is circled as correct in the scan. Could not transcribe graph shapes reliably; kept official key answer (c) unverified against the actual curve shapes.",
    },
    114: {
        "subject": "PHYSICS", "orig_num": 26,
        "notes": "Wheatstone-bridge-like resistor network diagram (five 10-ohm resistors) between points A and B. Needs figure to confirm answer (c, 10 Ohms).",
    },
    115: {
        "subject": "PHYSICS", "orig_num": 27,
        "notes": "Circuit diagram showing a battery and a coil/solenoid symbol with current direction arrows. Needs figure to confirm answer (a, Clockwise).",
    },
    124: {
        "subject": "PHYSICS", "orig_num": 36,
        "notes": "Full-wave bridge rectifier circuit diagram with diodes D1-D4, AC source, and load resistor R. Needs figure to confirm answer (d, D2 and D4 conducts).",
    },
    127: {
        "subject": "PHYSICS", "orig_num": 39,
        "notes": "Four E-vs-I graphs (options with a checkmark next to one in the scan) for photoelectron max K.E. vs light intensity. Kept official key answer (a) unverified against exact curve shapes.",
    },
    168: {
        "subject": "CHEMISTRY", "orig_num": 6,
        "notes": "Two energy-vs-reaction-progress graphs (labelled A-D, catalysed vs uncatalysed curves) shown as handwritten images. Needs figure to confirm answer (c).",
    },
    169: {
        "subject": "CHEMISTRY", "orig_num": 7,
        "notes": "Graph of a physical property (y-axis 'Physical Property', values ~0.10-0.15) vs atomic number for period-3 elements Na-S. Needs figure to confirm answer (c, Atomic radius).",
    },
    170: {
        "subject": "CHEMISTRY", "orig_num": 8,
        "notes": "Melting point (K) vs atomic number scatter plot for 8 consecutive elements labelled A-D at specific points. Needs figure to confirm answer (c, element C = silicon).",
    },
    181: {
        "subject": "CHEMISTRY", "orig_num": 19,
        "notes": "Skeletal structure image (chlorine-substituted, methyl-branched chain) to be named by IUPAC rules. Needs figure to confirm answer (b).",
    },
    182: {
        "subject": "CHEMISTRY", "orig_num": 20,
        "notes": "Four benzene + acylium-ion arenium-intermediate structures (options A-D) shown as images. Needs figure to confirm answer (d).",
    },
    197: {
        "subject": "CHEMISTRY", "orig_num": 35,
        "notes": "Four cyanohydrin product structures (options A-D) shown as images for the reaction of a ketone (CH3-CO-C2H5) with HCN/NaCN. Needs figure to confirm answer (a).",
    },
    205: {
        "subject": "CHEMISTRY", "orig_num": 43,
        "notes": "Four pairs of monomer structures (options A-D, terephthalic-acid-like diacid + diol) shown as images for Terylene synthesis. Needs figure to confirm answer (a).",
    },
    214: {
        "subject": "CHEMISTRY", "orig_num": 52,
        "notes": "Five separate temperature(K)-vs-substance graphs (I: noble gases, II: hydrocarbons, III: group V hydrides, IV: group VI hydrides, V: group VII hydrides) shown as images. Needs figures to confirm answer (c, III+IV+V).",
    },
}

# ---------------------------------------------------------------------------
# REDACTED / ILLEGIBLE QUESTIONS
# The last four Chemistry questions in the source scan (originally
# Chemistry Q55-Q58, global 217-220) are rendered only as a row of
# capital "X" characters on the page - the question text and options were
# not printed/legible in the compiled PDF. The official answer key also
# marks all four as "X" (no answer given), consistent with these being
# either blank filler rows or omitted/cancelled questions in the source
# compilation. They are kept as placeholder entries below with
# is_active=False so the total question count still reflects the paper's
# stated 220 MCQs; recommend excluding them from any scored import.
REDACTED_MCQS = {
    217: {"subject": "CHEMISTRY", "orig_num": 55, "is_active": False},
    218: {"subject": "CHEMISTRY", "orig_num": 56, "is_active": False},
    219: {"subject": "CHEMISTRY", "orig_num": 57, "is_active": False},
    220: {"subject": "CHEMISTRY", "orig_num": 58, "is_active": False},
}

REDACTED_PLACEHOLDER = "[Question illegible/blank in source scan - printed only as a row of 'X' characters. No official answer given.]"

SUBJECTS = [
    ("BIOLOGY", 1, 88),
    ("PHYSICS", 89, 132),
    ("ENGLISH", 133, 162),
    ("CHEMISTRY", 163, 220),
]

QUESTIONS = {
# ----------------------------- BIOLOGY (1-88) -----------------------------
1: ("Low partial pressure of oxygen in tissues favours ____________ of oxyhaemoglobin.", ["Dissociation","Formation","Stability","Transformation"]),
2: ("Respiratory tubules are termed as bronchioles when they attain the diameter ____________ or lesser:", ["1.2cm","1cm","1mm","1.2mm"]),
3: ("Elastic fibres are absent in the walls of __________:", ["Aorta","Arteries","Veins","Capillaries"]),
4: ("A type of blood cell that produces heparin is ___________:", ["Basophil","Neutrophil","Eosinophil","Monocyte"]),
5: ("Thoracic lymph duct of the lymphatic system opens into ___________:", ["Superior vena cava","Subclavian Vein","Inferior vena cava","Renal vein"]),
6: ("Select the part of nephron which is NOT permeable to water and stops its outflow:", ["Glomerulus","Proximal Tubule","Ascending loop","Desceding loop"]),
7: ("Vessels which carry blood to the glomerulus are called:", ["Efferent arterioles","Renal vein","Vesa recta","Afferent arterioles"]),
8: ("In ECG, QRS wave represents: " + DIAGRAM_PLACEHOLDER, ["Ventricular systole","Atrial systole","Diastole","Recovery systole"]),
9: ("When water content in body becomes high, what will happen:", ["ADH release will be inhibited","ADH will be released in large amount","Aldosterone will be released","Anterior pituitary will produce ADH"]),
10: ("The major factor in producing hypertonic urine is:", ["Glomerulus","Influence of aldosterone","ADH influencing on collecting duct","Gradual increase in osmolarity from cortex to inner medula"]),
11: ("What is the least selective process during urine formation:", ["Reabsorption","Pressure filteration","Secretion","Differential permeability"]),
12: ("The nerve impulse which jumps from node to node in myelinated neurons is called as:", ["Resting membrane potential","Saltatory nerve impulse","Threshold stimulus","Initial nerve impulse"]),
13: ("The CNS is protected by:", ["Three layers of meninges","One layer of moninx","4 layers of meninges","2 layers of meninges"]),
14: ("White matter of spinal cord is made up of:", ["Sensory nerve fibres","Myelinated nerve fibres","Motor nerve fibres","Mixed nerve fibres"]),
15: ("There are evidences that high levels of aluminum can lead to the onset of:", ["Parkinson's disease","Alzheimer's disease","Lesch-Nyhan syndrome","Fragile X-syndrome"]),
16: ("____________ is the structure in female reproductive system in which fertilization takes place:", ["Ovaries","Uterus","Cervix","Oviduct"]),
17: ("Which of the following directly develops into sperms:", ["Primary spermatocytes","Spermatids","Secondary spermatocytes","Spermatogonia"]),
18: ("FSH stimultes the production of oestrogen hormone which has two targets _______________ and ______________:", ["Uterus, posterior pituitary","Ovaries, uterus","Uterus, anterior pituitary","Ovaries, hypothalamus"]),
19: ("Select the organelle which is only present in animal cells:", ["Centrioles","R.E.R","Microtubules","Ribosomes"]),
20: ("Syphillis is a sexually transmitted disease and can also damage:", ["Hair","Heart","P.N.S","Birth canal"]),
21: ("Spongy bone is always surrounded by:", ["Compact bone","Cartilage","Osteoblast cells","Osteoclast cells"]),
22: ("Bone matrix is hardened by the:", ["Haversian canals","Canaliculfs","Bone marrow tissues","Calcium phosphate"]),
23: ("The number of bones forming skull in man is:", ["8","14","20","22"]),
24: ("The spine consists of linear series of :", ["33 bones","24 bones","12 bones","7 bones"]),
25: ("W.O.F changes occurs when skeletal muscles contract:", ["I-band shortens only","A-band shortens and Z-lines move apart","I-band shortens and Z-lines come close to each other","Actin filament contracts"]),
26: ("The thyroxine hormones of thyroid glands act directly on:", ["Iodine metabolism","Protein metabolism","Glucose metabolism","Basal metabolic rate"]),
27: ("All the hormones released by anterior pituitary are tropic hormones except:", ["TSH","STH","ACTH","Gonadotrophin hormone"]),
28: ("W.O.F is endocrine as well as exocrine:", ["Liver","Adrenals","Thyroid","Pancreas"]),
29: ("Ovulation is suppressed by progestrone via:", ["Only by inhibition of LH","Inhibition of FSH & stimulation of LH","Inhibition of LH & stimultion of FSH","Inhibition of both FSH & LH"]),
30: ("The antibody molecule consists of ____________ polypeptide chains:", ["Eight","Four","Six","Two"]),
31: ("_________________ cells survive for a few days and secrete a huge no of antibodies in blood, tissue fluids or lymph:", ["Memory cells","B-lymphocytes","T-lymphocytes","Plasma cells"]),
32: ("The intermediate protection from infection of snake bite can be obtained by:", ["Active Immunity","Natural active immunity","Passive immunity","Vaccination"]),
33: ("Chlorophyll molecule contains:", ["Mg++","Ca++","K+","Na+"]),
34: ("The tail of chlorophyll molecule is embedded in:", ["Membrane of mitochondria","Thylakoid membrane","Membrane of S.E.R","Membrane of R.E.R"]),
35: ("Carotenoids absorb light of:", ["Yellow-orange range","Yellow-red range","Orange-red range","Blue-violet range"]),
36: ("Chlorophyll 'a' and chlorophyll 'b' differ in one of the functional groups... Chlorophyll 'a' has:", ["-CHO","-OH","-CH3","-NH2"]),
37: ("Glycerate-3-phosphate in the presence of ATP and reduced NADP from light dependent stage is reduced to:", ["3- carbon compound","Ribulose bisphosphate","5-carbon compound","6-carbon compound"]),
38: ("Calvin cycle occurs in:", ["Grana of chloroplast","Stroma of chloroplast","Chlorophyll (Reaction centre)","Roots of plants"]),
39: ("Restriction enzyme EcoR1 cuts DNA to produce:", ["Blunt ends","Non-palindromic ends","Sticky ends","Split ends"]),
40: ("Restriction endonucleases are produced by:", ["Fungi","Algae","Bacteria","Viruses"]),
41: ("DNA segments of different lengths can be separated by a process of:", ["Western blotting","Northern blotting","Autoradiography","Gel electrophoresis"]),
42: ("The is the 1st heat stable component used in PCR:", ["Taq-isomerase","Taq-helicase","Taq-polymerase","Taq SSBp"]),
43: ("Patients of cystic fibrosis (CF) produse thick mucus because of faulty:", ["Trans-membrane carrier","Cl- ions","Na+ ions","Mucus membrane"]),
44: ("Chemicals used for destroying agricultural competitors are known as:", ["Antibiotics","Pesticides","Disinfectants","Chemotherpeutic agents"]),
45: ("How denitrification does occur in soils:", ["Bacterial reduction of NO3- ions to N2 gas","Active uptake of Nitrate ions by plant roots","Drainage of manure from fields","Leaching of nitrate ions"]),
46: ("Process by which unrelated species evolve to functionally resemble each other is called:", ["Convergent evolution","Divergent evolution","Co-evolution","Parallel evolution"]),
47: ("W.O.F shows evidences from evolution through molecular biology:", ["Development of bronchial arches in verterbrate embryo","Distribution of species","Comparision of genes and proteins in different species","Study of vestigial organs"]),
48: ("Large population size, random mating, no mutation and no emigration or immigration are the postulates of:", ["Hardy-Weinberg theorem","Mendel's law of independent assortment","Mendel's law of segregation","Theory presented by Schleien and Schwann"]),
49: ("Pure breeding lines of pea were taken regarding seed shape \u2014 Round and wrinkled and were crossed with no intermediate between parents. All offsprings were found to be round. These results show:", ["Co-dominance","Dominance-recessive relationship","Incomplete dominance","Over dominance relationship"]),
50: ("Base substitution, deletion and insertion are examples of:", ["Chromosomal aberration","Point mutation","Aneuploidy","Euploidy"]),
51: ("The condition in which the heterozygote has a phenotype intermediate between contrasting homozygous parents is called as:", ["Dominance","Incomplete dominance","Co-dominance","Over- dominance"]),
52: ("The interaction between different genes occupying different loci is:", ["Dominance","Co-dominance","Pleiotropy","Epistasis"]),
53: ("Locus stands for:", ["Position of gene on homologous chromosome","Regions of chromosomes","Position of an allele within a DNA molecule","Close regions of same chromosome"]),
54: ("Self fertilization of F-1 dihybrids, following independent assortment of alleles result in:", ["3/16 Tall-round ; 3/16 dwarf-wrinkled","9/16 Tall-wrinkled ; 3/16 dwarf-round","9/16 Tall-round ; 3/16 Dwarf-round","3/16 Tall-wrinkled ; 3/16 Dwarf-round"]),
55: ("As a result of cross-fertilization of a true breeding pea plant having purple coloured flowers with that of white coloured flowers, the offsprings will have flowers with:", ["1/4 purple ; 3/4 white","1/4 white ; 3/4 purple","All white","All purple"]),
56: ("The gene for red-green colour blindness is present on:", ["Y-chromosome","X-chromosome","Autosome 7","Autosome 9"]),
57: ("W.O.F structures is present in both plant and animal cells but is absent in prokaryotic cells:", ["Centrioles","Microtubule","Plastids","Sieve-tubes"]),
58: ("Cilia and flagella are absent in:", ["Viruses","Bacteria","Higher plants","Lower animals"]),
59: ("DNA molecule in prokaryotes is:", ["Single, circular, double stranded molecule not bound by membrane","Double, circular molecule","Linear double stranded molecule","Single, circular, double stranded, membrane bound"]),
60: ("Nucleoid is a structure not found in:", ["Campylobacter","Cyanobacteria","Spirochete","Goblet cells"]),
61: ("Cell wall structure of a cell of unknown origin was studied and was found to contain polysaccharide chain linked with short chains of amino acid.. What do u think it can be??", ["Bacteria","Fungi Cell","Algae","Cortex cells"]),
62: ("Ribosomes present in prokaryotes are:", ["80S","60S","50S","70S"]),
63: ("Functionally mesosomes can be compared with:", ["Ribosomes","Mitochondria","Polysomes","Golgi bodies"]),
64: ("Students were asked to give a guess about a unicellular organism with darkly stained nucleus.. W.O.F can be straight away excluded from the list:", ["Paramecium","Amoeba","Plasmodium","Lactobacillus"]),
65: ("Binary fission is a characteristic cell division NOT found in:", ["Pseudomonas","Campylobacter","Euglena","E.coli"]),
66: ("______________ are the specific structures related to monosaccharides:", ["Glycosidic bond","Keto group","Maltose","Fructose"]),
67: ("______________ are the major site for storage of glycogen in animal's body:", ["Muscle and liver","Around thighs and belly","Around belly and hips","Liver and kidneys"]),
68: ("The number of amina acids that have been found to occur in cells and tissues are:", ["170","20","25","45"]),
69: ("Most proteins are made up of ____________ type of amino acids:", ["20","170","25","200"]),
70: ("If in lipids there is an higher proportion of unsaturated fatty acids then it will be:", ["Oils","Waxes","Phenols","Fats"]),
71: ("When X-rays are passed through crystalline DNA, it shows helix making one twist every:", ["2nm","3.4nm","34nm","4nm"]),
72: ("Following is the structure of: " + DIAGRAM_PLACEHOLDER + " (a pyrimidine ring with an -NH2 substituent shown)", ["Uracil","Thymine","Guanine","Cytosine"]),
73: ("All enzymes are _________________:", ["Fibrous proteins","Low molecular weight proteins","Lipoproteins","Globular proteins"]),
74: ("The reactants on which enzyme works are:", ["Products","Metabolites","Substrates","Catabolites"]),
75: ("W.O.F comprises of inorganic ions:", ["Coenzymes","Activators","Prosthetic group","Apoenzyme"]),
76: ("W.O.F is a non-cellular infecious entity:", ["Mycoplasma","Escherichia coli","Herpes virus","Diplococcus"]),
77: ("The viruses can reproduce:", ["Without invading any cell","In bacterial cell","By mitosis","By meiosis"]),
78: ("The life cycle in which the phage kills the bacteria is known as:", ["Transduction","Temperate phage cycle","Lytic cycle","Lysogenic phage cycle"]),
79: ("In W.O.F shapes, gut living symbiont Escherichia coli is found:", ["Round","Oval","Spiral","Rod"]),
80: ("Chitin, a chemical found in exoskeleton of arthropods is also found in cell wall of:", ["Bacteria","Fungi","Cyanobacteria","Algae"]),
81: ("Snails are the intermediate hosts in:", ["Fasciola hepatica","Taenia solium","Schistoma","Ancyclosoma duodenale"]),
82: ("_______________ is an intestinal parasite of man belonging to phylum nematoda:", ["Taenia solium","Wucheronia bancrolti","Ascaria lumbricoides","Schistoma"]),
83: ("Food is diverted in the oesophagous by:", ["Glottis","Tongue","Cheeks","Epiglottis"]),
84: ("Label 'a' in the following diagram: " + DIAGRAM_PLACEHOLDER + " (stomach with oesophagus/duodenum, 'a' marks the junction near the duodenum)", ["Cardiac sphincter","Sinoatrial valve","Stomach valve","Pyloric sphincter"]),
85: ("Enzyme pepsin acts on: (table: Options / Substrate / Products - A: Protein/Polypeptides, B: Polypeptide/Dipeptides, C: Fats/Fatty acids-glycerol, D: Protein/Amino Acids)", ["Protein -> Polypeptides","Polypeptide -> Dipeptides","Fats -> Fatty acids/glycerol","Protein -> Amino Acids"]),
86: ("Following is the structure of gastric glands in stomach wall where 'x' is: " + DIAGRAM_PLACEHOLDER + " (zymogen cells labelled, 'x' unlabeled)", ["Mucosa","Mucus cells","Visceral fat cells","Oxyntic cells"]),
87: ("Label the part 'Y' in the following diagram: " + DIAGRAM_PLACEHOLDER + " (lungs/chest cavity diagram, 'Y' at bottom)", ["Pleura","Diaphragm","Chest cavity","Intercoastal muscles"]),
88: ("W.O.F is a respiratory disorder related to malnutrition:", ["Cancer","Asthma","Emphysema","Tuberculosis"]),

# ----------------------------- PHYSICS (89-132, orig Q1-44) -----------------------------
89: ("The quantities which can be measured accurately are:", ["Base quantities","Physical Quantities","Derived Quantities","Supplementary quntities"]),
90: ("An observer notes reading of scale from different angles (parallax) while measuring the length of wire, what type of error is possible:", ["Systematic error","Zero error","Precised error","Random error"]),
91: ("The ratio of displacement along diameter of cirle and total distance along circle is:", ["1:\u03c0","\u03c0:1","2:\u03c0","\u03c0:2"]),
92: ("Arshad is driving down 7th street, he drives 150m in 18s.. Assume he doesnot speed up or slow down, what is his speed:", ["0.38 m/s","126 m/s","8.33 m/s","58.33 m/s"]),
93: ("The distance travelled by a moving car with velocity 15 m/s in 2s, decelerates at 2m/s is equal to:", ["30m","34m","16m","26m"]),
94: ("Total work done in figure is: " + DIAGRAM_PLACEHOLDER + " (F vs d graph showing a closed loop, values 2-6 on both axes)", ["24 Nm","16 Nm","8 Nm","Zero Nm"]),
95: ("Work done will be zero if angle between force and displacement is:", ["0\u00b0","60\u00b0","270\u00b0","360\u00b0"]),
96: ("If mass 'm' is dropped from height 'h' vertically, 'f' is the force of friction during downward motion and 'v' is the velocity at bottom, following will hold:", ["\u00bdmv\u00b2 = mgh + fh","mgh = \u00bdmv\u00b2 \u2212 fh","fh = mgh+ \u00bdmv\u00b2","mgh = \u00bdmv\u00b2 + fh"]),
97: ("A body moves in a circle with increasing angular velocity, at time 't'= 6s the angular velocity is 27rad/s... What is the radius of circle where linear velocity is 81cm/s:", ["6cm","9cm","7cm","3cm"]),
98: ("A moon rotates about its axis. In future scientists may wish to put a satellite into an orbit around the moon such that the satellite remains stationary above one point on moon surface, the period of rotation of moon abou its axis is 27.4 days, what is the radius of required orbit? Mm= 7.35 x 10^22 kg", ["3.59 x 10^7 m","4.23 x 10^7 m","8.86 x 10^7 m","6.96 x 10^6 m"]),
99: ("In mass spring system mass 'm' is attached with spring of spring constant 'k' with time period 'T1'.. Then the mass is replaced by '2m' with same spring, what is the time period 'T2'", ["T2 = T1","T2 = 2T1","T2 = \u221a2 T1","T2 = T1/ \u221a2"]),
100: ("A body performing SHM with displacement x=xo sin(wt+fi), when t=0, x=xo.. Then what is the phase angle fi??", ["\u03c0","\u03c0/2","\u03c0/4","\u2212\u03c0"]),
101: ("Angular displacement of a point moving in a circle 10cm when displacement of projection of this point along vertical diameter of circle is 8.66cm will be:", ["30\u00b0","45\u00b0","60\u00b0","75\u00b0"]),
102: ("A wave travelling with speed of 130 m/s having wavelength of 5m. What is its frequency:", ["650 Hz","20 Hz","26 Hz","3.8 x 10^2 Hz"]),
103: ("A metallic wire of length 2m hooked between two points has tension 10N. If mass per unit length is 0.004 kg/m, their fundamental frequency emitted by wire on vibration is:", ["48 Hz","24 Hz","12.5 Hz","6.25 Hz"]),
104: ("Coherent lines emerge from two fine parallel slits 'A' and 'B' as shown in figure: " + DIAGRAM_PLACEHOLDER + " If 'P' is the position of nth dark fringe from centre of interference, then phase difference between wave train 'A' and 'B' is:", ["n\u03c0 radian","2\u03c0n radian","(n+\u00bd)\u03c0 radian","(2n+1)\u03c0 radian"]),
105: ("The wavelength of light which produces second order spectrum on diffraction grating on which 5000 lines/cm are ruled at an angle of 30\u00b0 will be:", ["6 x 10^-7 m","4 x 10^-6 m","5 x 10^-7 m","3 x 10^-6 m"]),
106: ("Estimate pressure of air molecules at 273K, if mean square speed is 500 m\u00b2/s\u00b2 and density of air is 6 kg/m\u00b3:", ["1 x 10^3 Pa","2.5 x 10^2 Pa","1 x 10^2 Pa","2.7 x 10^3 Pa"]),
107: ("1 mole of a gas occupies volume 1.00 x 10^-2 m\u00b3 in a gas cylinder whose pressure is equal to 2.50 x 10^5 Pa. The temperature of cylinder is:", ["227K","300K","370K","390K"]),
108: ("The value of pressure and volume of fixed mass of gas in thermometer at triple point of water Pf= 1.00 x 10^5 Pa and Vf= 1 x 10^-3 m\u00b3. When P= 1.1 x 10^5 Pa and V= 1.2 x 10^-3 m\u00b3. Then temperature of gas is:", ["361K","298K","273K","250K"]),
109: ("A point charge at distance 'x' from another point charge experiences a force F of repulsion, which graph shows relationship of force F to 'x': " + DIAGRAM_PLACEHOLDER, ["Graph A","Graph B","Graph C","Graph D"]),
110: ("The Coulumbs force between two point charges q1=1C and q2 is 2N. Where distance between them is 3m, The charge q2 is:", ["1 x 10^-9 C","1 x 10^9 C","2 x 10^9 C","4 x 10^-9 C"]),
111: ("Electric field strength at position vector r=(4i + 3j)m caused by point charge q= 5uC placed at origin is:", ["1440i + 1080j V/m","1240i + 1280j N/C","1440i+ 1080j N/m","1240i + 1080j N/C"]),
112: ("2.00 x 10^6 e passing through a coductor in 1millisecond. Electric current through conductor is:", ["3.2 x 10^-10 A","32.0 x 10^-9 A","320 x 10^-10 A","0.320 x 10^-10 A"]),
113: ("A carbon resistor connected to a battery of 50V and 2A current is passing throug it. If voltage is increased to 75V then current will be:", ["1.5 A","3A","4.5 A","6A"]),
114: ("Effective resistance between point A and B is: " + DIAGRAM_PLACEHOLDER + " (five 10-ohm resistors in a bridge-like network)", ["40 Ohms","50 Ohms","10 Ohms","30 Ohms"]),
115: ("Electric current is flowing through the circuit as shown in figure, what will be the direction of magnetic lines of force: " + DIAGRAM_PLACEHOLDER, ["Clockwise","Anticlockwise","From top to bottom","From bottom to top"]),
116: ("The magnetic flux linked with a solenoid of area 'A', having 'N' turns at right angle to magnetic field is:", ["NBA","BA","1/2NBA","BAcos(theeta)"]),
117: ("A charge projected with velocity of 10m/s in a magnetic fiels of 10T at an angle of 60\u00b0, if force exerted on charge is 2.78 x 10^-17 N, then value of charge is:", ["1.6 x 10^-19 C","2.7 x 10^-19 C","3.2 x 10^-19 C","4.8 x 10^-19 C"]),
118: ("The value of magnetic flux is 10Wb, when magnetic lines of force containing magnetic field strength of 1T passing through unit area of 10m\u00b2, then angle between magnetic field and unit area is:", ["360\u00b0","180\u00b0","90\u00b0","45\u00b0"]),
119: ("A loop of 5 turns of wire is placed in uniform magnetic field of 0.5T, then area of loop shrinks at a constant rate of 10 m\u00b2/s, the emf induced is:", ["2.5V","25V","250V","0.25V"]),
120: ("The phase at negative peak of AC voltage is:", ["\u03c0/2","\u03c0","3\u03c0/2","2\u03c0/3"]),
121: ("A 1.25cm diameter cylinder is subjected to load of 2500kg, stress on bar is:", ["200 Pa","2 x 10^5 Pa","2 x 10^6 Pa","2 x 10^9 Pa"]),
122: ("Output voltage of rectifier is not smooth, it can be made smooth by a circuit known as:", ["Wheatstone Circuit","Bridge circuit","Filter circuit","Ripple circuit"]),
123: ("A wire of length 2m is attached with mass of 5kg vertically, tensile strain of wire is 0.3 x 10^-3, the extension in wire is:", ["1.5mm","2mm","0.15mm","0.6mm"]),
124: ("What happens in positive cycle of AC input? " + DIAGRAM_PLACEHOLDER + " (full-wave bridge rectifier with diodes D1-D4)", ["D1 and D3 conducts","D1 and D2 conducts","D3 and D4 conducts","D2 and D4 conducts"]),
125: ("If signal is applied to input of non-inverting amplifier through resistance of 100 kOhm, and the value of feedback resistance is 10kOhm, the gain is:", ["11","10","1.1","0.11"]),
126: ("The frequency of photon having momentum 4.42 x 10^-26 Ns is:", ["2.00 x 10^16 Hz","2.00 x 10^14 Hz","5.00 x 10^16 Hz","2.00 x 10^18 Hz"]),
127: ("The max K.E, 'E' of photoelectrons ejected by a light of certain wavelength from a metal is measured as a fucnction of intensity 'I' of light. Which graph represents the way 'E' depends on 'I': " + DIAGRAM_PLACEHOLDER, ["Graph (marked with checkmark in scan)","Graph II","Graph C","Graph D"]),
128: ("The momentum of wave where wavelength 1.32 x 10^-9 m", ["5.00 x 10^-25 Ns","5.00 x 10^-26 Ns","5.00 x 10^-43 Ns","5.00 x 10^-44 Ns"]),
129: ("Ionization energy of hydrogen atom is:", ["0.54 eV","0.85 eV","3.39 eV","13.6 eV"]),
130: ("Complete the equation: ?_?Z ------> a_bY + y", ["a_(b+1)Z","a+1_(b-1)Z","a_bZ","a+1_(b+1)Z"]),
131: ("The quantity of uranium is 400g, the amount of uranium left after 3 half lives is:", ["25g","50g","100g","200g"]),
132: ("The mass of Radium atom decreases by 8.6 x 10^-3 kg, mass defect equivalent to energy is:", ["4.48 MeV","4.84 MeV","3 x 10^2 MeV","4.84 eV"]),

# ----------------------------- ENGLISH (133-162, orig Q1-30) -----------------------------
133: ("A voice ____________ us from the either side of the street", ["Addled","Hailed","Transcend","Purified"]),
134: ("Many of the houses lacked even the basic ___________", ["Adroitness","Anomaly","Amenities","Behest"]),
135: ("The system has the ____________ to run more than one program at the same time", ["Acumen","Ability","Cadaver","Adroitness"]),
136: ("The soviet union was so vast and _____________ that it comprised all the concievable world.", ["Incisive","Prolific","Hermetic","Platonic"]),
137: ("SPOT THE ERROR: When Maulvi Abul reached (Shamim Ahmed's new shop,)[a] he found (a crowd)[b] had already assembled (there to watch)[c] (the proceeding.)[d]", ["Shamim Ahmed's new shop,","a crowd","there to watch","the proceeding."]),
138: ("SPOT THE ERROR: (One of his hands was)[a] slipped (into a pocket)[b] of his overcoat (while in other)[c] he held a short polished cane which (every now and then)[d] he twirled jauntily.", ["One of his hands was","into a pocket","while in other","every now and then"]),
139: ("SPOT THE ERROR: The finder is requested (to return)[a] the purse (to the mayor office)[b] or to (Mr. James)[c] (the caretaker of this)[d] public hall.", ["to return","to the mayor office","Mr. James","the caretaker of this"]),
140: ("SPOT THE ERROR: He told them (how the glory of)[a] their country and (of its ancient throne)[b] would be increased if (the post of court)[c] acrobat (was created.)[d]", ["how the glory of","of its ancient throne","the post of court","was created."]),
141: ("SPOT THE ERROR: With this faith we will be able (to hew out)[a] (from the mountain)[b] (of despair,)[c] (a stone of hope.)[d]", ["to hew out","from the mountain","of despair,","a stone of hope."]),
142: ("SPOT THE ERROR: (If it was possible)[a] to get (the necessities of life)[b] from the heavens (through prayers.)[c] Maulvi Abul would have prayed to Allah for a pair of shoes (for his Umda.)[d]", ["If it was possible","the necessities of life","through prayers.","for his Umda."]),
143: ("Choose the CORRECT sentence:", ["Journalists must be well acquainted in the ethics of journalism.","Journalists must be well acquainted with the ethics off journalism.","Journalists must be well acquainted from the ethics of journalism.","Journalists must be well acquainted with the ethics of journalism."]),
144: ("Choose the CORRECT sentence:", ["Heat the olive oil into a heavy pan.","Heat the olive oil in a heavy pan.","Heat the olive oil with a heavy pan.","Heat the olive oil on a heavy pan."]),
145: ("Choose the CORRECT sentence:", ["She made no attempt to be friendly on anything but the most superficial level.","She made no attempt to be friendly on anything but with most superficial level.","She made no attempt to be friendly on anything but the most superficial level. (duplicate option in source)","She made no attempt to be friendly on anything but with the most superficial level."]),
146: ("Choose the CORRECT sentence:", ["He abdicated on favour of his son.","He abdicated in favour of his son.","He abdicated by favour of his son.","He abdicated as favour of his son."]),
147: ("Choose the CORRECT sentence:", ["He was abetted by the deception by his wife.","He was abetted from the deception by his wife.","He was abetted in the deception by his wife.","He was abetted to the deception by his wife."]),
148: ("Choose the CORRECT sentence:", ["The country is stepping back from the edge of an abyss.","The country is stepping back in the edge of an abyss.","The country is stepping back of the edge of an abyss.","The country is stepping back through the edge of an abyss."]),
149: ("Choose the CORRECT sentence:", ["He lived at the style befitting a gentleman.","He lived through the style befitting a gentleman.","He lived by the style befitting a gentleman.","He lived in the style befitting a gentleman."]),
150: ("Choose the CORRECT sentence:", ["He have decided to grow a beard and a moustache.","He has decided to grow a beard and a moustache.","He has been decided to grow a beard and a moustache.","He have been decided to grow a beard and a moustache."]),
151: ("Choose the CORRECT sentence:", ["Their divorce filled a lot of column inches in the national newspaper.","Their divorce filled lot of column inches in the national newspaper.","Their divorce filled a lot of column inches to the national newspaper.","Their divorce filled lot of column inches to the national newspaper."]),
152: ("Choose the CORRECT sentence:", ["The horse reared off on its hind legs.","The horse reared of on its hind legs.","The horse reared up on its hind legs.","The horse reared down on its hind legs."]),
153: ("Select the NEAREST CORRECT MEANING: CENTENNIAL:", ["A hundredth anniversary.","Relating to continents.","Relating to sins.","Relating to countries."]),
154: ("Select the NEAREST CORRECT MEANING: COBBLE:", ["Demon","Cockerel","Convention","Stone"]),
155: ("Select the NEAREST CORRECT MEANING: COCCYX:", ["Drug","Force","Bone","Shield"]),
156: ("Select the NEAREST CORRECT MEANING: COMPLACENT:", ["Self-regarding","Self-conceited","Talented","Self-control"]),
157: ("Select the NEAREST CORRECT MEANING: ACCESSORY:", ["Fitting","Canabis","Mattock","Intrepidity"]),
158: ("Select the NEAREST CORRECT MEANING: AFFINITY:", ["Coenobium","Magnate","Propensity","Tear"]),
159: ("Select the NEAREST CORRECT MEANING: AMORPHOUS:", ["Flagrant","Nebulous","Voluptuous","Nugatory"]),
160: ("Select the NEAREST CORRECT MEANING: ADMONITION:", ["Juvenility","Puberty","Acquisition","Bashing"]),
161: ("Select the NEAREST CORRECT MEANING: AUDACIOUS:", ["Mawkish","Autocratic","Perl","Oozy"]),
162: ("Select the NEAREST CORRECT MEANING: BOUQUET:", ["Posy","Prolegomena","Necropsy","Damper"]),

# ----------------------------- CHEMISTRY (163-220, orig Q1-58) -----------------------------
163: ("In NO3- the oxidation number of N is:", ["+5","+2","+3","-3"]),
164: ("The E\u00b0 value of the standard copper half cell is +0.34, measured when it is connected with SHE i.e Standard Hydrogen Electrode. In this case the half cell reaction taking place at SHE is:", ["2H+(aq) + 2e- ----> H2(g)","H2 ----> 2H+(aq) + 2e-","2H+ + 2e- ----> 2H(g)","H2 ----> 2H(g) + 2e-"]),
165: ("Consider the following reversible reaction: CH3-CH2-OH + CH3-COOH <====H+====> CH3-CH2-O-CO-CH3 + H2O. Initial: (CH3-CH2-OH)=1mol, (CH3-COOH)=1mol, (ester)=0mol, (H2O)=0mol. Equilibrium: (CH3-CH2-OH)=0.33mol, (CH3-COOH)=0.33mol, (ester)=0.66mol, (H2O)=0.66mol. Kc=4 at 100C. What are new equilibrium concentrations of all species if 1 mole of CH3CH2OH and CH3COOH are added to this equilibrium mixture? (Apply Le-Chatelier's principle) (Temperature remains same) (Kc remains constant)", ["(CH3COOH)=0.333mol, (CH3CH2OH)=1.333mol, (ester)=1.666mol, (H2O)=1.666mol","(CH3COOH)=1.333mol, (CH3CH2OH)=0.333mol, (ester)=?mol, (H2O)=?mol","(CH3COOH)=0.666mol, (CH3CH2OH)=0.666mol, (ester)=1.333mol, (H2O)=1.333mol","(CH3COOH)=0.333mol, (CH3CH2OH)=0.333mol, (ester)=1.333mol, (H2O)=1.333mol"]),
166: ("For which of the following equilibrium reaction, Kc has no units:", ["N2 + 3H2 ----> 2NH3","SO2 + 2O2 ----> 2SO3","CO + H2O ----> CO2 + H2","2NO2 + O2 ----> 2NO3"]),
167: ("Choose the type of catalysis in the following reaction: 2SO3(g) <==NO3(g)catalyst==> 2SO2(g)", ["Homogenous Catalysis","Heterogenous Catalysis","Biological Catalysis","Gas Catalysis"]),
168: ("Which one of the following graphs is the representation for more rapid catalysed reaction? " + DIAGRAM_PLACEHOLDER, ["Graph A","Graph B","Graph C","Graph D"]),
169: ("Following graph shows a physical property along the period 3 elements. Which physical property is shown in the graph? " + DIAGRAM_PLACEHOLDER, ["Electron affinity","Non-metallic character","Atomic radius","Melting point upto group IV"]),
170: ("The following sketch shows the melting point of eight elements with consecutive atomic numbers. Which element is silicon? " + DIAGRAM_PLACEHOLDER, ["Element A","Element B","Element C","Element D"]),
171: ("6NaOH + 3Cl2 ----> 5NaCl + NaClO3 + 3H2O. In above disproportionation reaction the oxidation state of chlorine is changed from zero to __________ and __________.", ["-1, +1","-1, +3","-1, +5","+1, +5"]),
172: ("Which noble gas is alpha emitter?", ["Xenon","Radon","Krypton","Argon"]),
173: ("Scandium has atomic number 21, which one will be its electronic configuration:", ["1s2, 2s2, 2p6, 3s2, 3p6, 3d3","1s2, 2s2, 2p6, 3s2, 3p6, 4s2, 3d1","1s2, 2s2, 2p6, 3s2, 3p6, 4s2, 4p1","1s2, 2s2, 2p6, 3s2, 3p6, 4s1, 4p2"]),
174: ("Violet colour of [Ti(H2O)4]+ ion is due to:", ["Central metal ion","Complex ion","Water molecule","Outer anion"]),
175: ("Nitrogen gas reacts under ______________ conditions:", ["Standard","Normal","Cool","Harsh"]),
176: ("Liquid ammonia has become an important fertilizer for direct application to soil. It contains ____________ nitrogen", ["46%","82%","14%","17%"]),
177: ("SO3, formed in contact process is absorbed in ________% H2SO4.", ["90","80","98","89"]),
178: ("The balanced chemical equation to manufacture ammonia by Haber's process is:", ["N2(g) + 3H2(g) <====> 2NH3(g)","N2(g) + H2(g) <====> NH3(g)","3N2(g) + H2(g) <====> 2NH3(g)","N2(g) + 3H2(g) ----> 2NH3(g)"]),
179: ("Which one of the following is used as a typical catalyst for catalytic cracking:", ["Mixture of SiO2 and Ni","Mixture of Pt and Cu","Mixture of Fe and MgO","Mixture of SiO2 and Al2O3"]),
180: ("The type of structural isomerism which arises due to the difference in nature of carbon chains or carbon skeleton is:", ["Chain isomerism","Position isomerism","Cis-Trans isomerism","Optical isomerism"]),
181: ("Which one of the following is the best name according to IUPAC system for the formula given below: " + DIAGRAM_PLACEHOLDER + " (chlorine-substituted, methyl-branched carbon chain)", ["4-methyl-6-chloro heptane","2-chloro-4-methyl heptane","2-chloro-4-n propyl hexane","2-chloro-4-n propyl pentane"]),
182: ("Immediate product formed when propanoyl chloride reacts with benzene is: " + DIAGRAM_PLACEHOLDER + " (four arenium/acylation product structures A-D)", ["Structure A","Structure B","Structure C","Structure D"]),
183: ("Which of the following are 3,5(meta) directing groups when second group is induced in them: I= -NH3   II= -CHO   III= -COOH   IV= -CH3", ["II, III and IV","II and III","I and IV","I, II and IV"]),
184: ("When benzene reacts with acetyl chloride (CH3COCl) in the presence of AlCl3, acetophenone is formed. The electrophile in this reaction will be:", ["CH3C+O","AlCl3","C+H3","CH3COCl"]),
185: ("The reaction of bromine with benzene in the presence of FeBr3 follows the mechanism of:", ["Electrophilic addition","Nucleophilic substitution","Electrophilic substitution","Nucleophilic addition"]),
186: ("Which one of the following is halothane:", ["Cl-CH2-CH2-CL","CF3-CHCl-Br","Cl-CH2-CH2-CH2-Br","Br-CH2-CH2-Br"]),
187: ("The non-stick lining of pans is:", ["Difluoroethane","Chlorofluororyhane","Chloroethane","Tetrafluoroethane"]),
188: ("In elimination reaction, alcoholic KOH is used.. OH- in this case will act as:", ["Electrophile","Base","Leaving group","Acid"]),
189: ("During the SN1 reactions, the fast reaction involves:", ["Breakage of covalent bond","Formation of carbocation","Transition state","Attack of nucleophile"]),
190: ("Alcohol reacts slowly with Na-metal as compared to water because it has low concentration of H+ ion which suggests that it is:", ["Less acidic than water","Less basic than phenol","More acidic than phenol","More acidic than water"]),
191: ("CH3-CH2-OH + PCl5 ----> CH3-CH2-Cl + POCl3 + HCl.... Formation of HCl is the test for the presence of ____________ in a compound:", ["Alkyl group","Hydroxyl Group","Saturated alkyl group","Acidic H+ ion"]),
192: ("C2H5OH + CH3COOH <==H2SO4==> ?? What will be the exact product?", ["Diethyl ether","Methyl propyl ether","Ethyl acetate","Butyl alcohol"]),
193: ("C2H5-SO3H --H2O--> C2H5-OH + H2SO4, choose the correct type for this reaction from the following:", ["Reduction","Oxidation","Hydroxylation","Hydration"]),
194: ("Ethanol reacts with HCN to form cyanohydrin, it is an example of:", ["Nucleophilic addition","Electrophilic addition","Electrophilic substitution","Nucleophilic substitution"]),
195: ("The reactions of aldehydes and ketones with ammonia derivatives G-NH3 to form compounds containing >C=N-C and water is known as ___________ reaction:", ["Nucleophilic addition","Nucleophilic substitution","Electrophilic addition","Addition elimination"]),
196: ("Which one of the following compounds will give iodoform test on treatment with aqueous iodine?", ["3-pentanone","Propanone","Propanal","Butanal"]),
197: ("What will be the product of reaction given below: CH3-C(=O)-C2H5 + HCN --NaCN/HCl--> Y " + DIAGRAM_PLACEHOLDER + " (four cyanohydrin structures A-D)", ["Structure A","Structure B","Structure C","Structure D"]),
198: ("In the reaction \"?\" represents which one of the following products: Primary alcohol + [O] --K2Cr2O7/H2SO4--> ? --[O]--> Carboxylic acid", ["Ketone","Aldehyde","Formic acid","Ether"]),
199: ("Compounds having -CN group are called as:", ["Cyano compounds","Nitro compounds","Carbon nitrogen compounds","Nitriles"]),
200: ("Select the correct acidic strength order of chlorosubstituted acids:", ["CH3COOH > ClCH2COOH > Cl2CHCOOH > Cl3CCOOH","CH3COOH > Cl2CHCOOH > Cl3CCOOH > ClCH2COOH","Cl3CCOOH > Cl2CHCOOH > ClCH2COOH > CH3COOH","Cl3CCOOH > CH3COOH > Cl2CHCOOH > ClCH2COOH"]),
201: ("The phenoxide ion is more stable than ethoxide ion as:", ["Lone pair on oxygen atoms overlap with the delocalized \u03c0-bonding system in benzene","Oxygen atom is directly bonded with benzene ring in the phemoxide ion","The negative charge is localized on oxygen atom of phenoxide ion","The negative charge is delocalized on oxygen atom of ethoxide ion"]),
202: ("Acidic character of amino acid is due to:", ["-NH2","-N+H3","-COOH","-COO-"]),
203: ("IUPAC name of alanine is:", ["2-aminopropanoic acid","2-aminoethanoic acid","2-aminobutane-1,4-dioic acid","2-aminobutanoic acid"]),
204: ("The amide linkage in Nylon-6,6 has the structure:", ["-NH2-CO-","-CO-O-","-NH-CO-","-NH-O-CO-"]),
205: ("The monomers needed to make \"Terylene\", i.e a polyester are: " + DIAGRAM_PLACEHOLDER + " (four monomer-pair structures A-D)", ["Structures A","Structures B","Structures C","Structures D"]),
206: ("Which one of the followng is the main function of DNA:", ["Making of proteins","Making of amino","Breaking of ribose sugar","Carries genetic material"]),
207: ("_____________ is the major source of acid deposition in atmosphere:", ["SiO2","CO2","SO3","Al2O3"]),
208: ("The energy from ultraviolet light is sufficient to break the ________ bonds in CCl2F2", ["Cl-Cl","C-Cl","Cl-F","C-F"]),
209: ("There are almost 200 million people alive in Pakistan. If you were to distribe Rupees 100 to each Pakistani in the form of 5 Rupee coin, how many moles of coins you must have:", ["6.67 X 10^-14","1.5 X 10^-14","6.67 X 10^14","1.5 X 10^14"]),
210: ("A researcher has prepared a sample of 1-bromopropane from 10g of 1-propanol. After purification he had made 12g of product. Which of the following is percentage yield:", ["60%","58%","90%","50%"]),
211: ("Which one of the following has same number of molecules as present in 11g of CO2:", ["4g of O2","4.5g of H2O","4g of Cl","1/4 moles of NaCl"]),
212: ("An organic sample consisting of carbon, hydrogen and oxygen was subjected to combustion analysis. 0.543g of this compound gave 1.039g of Carbon dioxide, 0.636g of water vapours. The empirical formula of this compound is:", ["CH2O","C4H12O2","C3H6O","CH4O"]),
213: ("28g of N2 will at STP occupy the volume of:", ["22.41 dm3","44.82 dm3","44.82 cm3","2.241 dm3"]),
214: ("Study the following graphs of boiling points of some substances " + DIAGRAM_PLACEHOLDER + " (graphs I: noble gases, II: hydrocarbons CH4-C4H10, III: group V hydrides, IV: group VI hydrides, V: group VII hydrides). Which of the above graphs shows that some members of graph have hydrogen bonding:", ["I + IV","II + IV","III + IV + V","I + II + III"]),
215: ("No of electrons in 31^69 Ga3+ will be:", ["28","29","30","34"]),
216: ("Isotopic symbol of ion of sulphur-33 is 16^33 S-2. How many no of protons and neutrons are present if the number of electrons are 18:", ["P = 18, n =15","P =16, n = 17","P = 16, n = 16","P = 17, n = 16"]),
217: (REDACTED_PLACEHOLDER, ["-","-","-","-"]),
218: (REDACTED_PLACEHOLDER, ["-","-","-","-"]),
219: (REDACTED_PLACEHOLDER, ["-","-","-","-"]),
220: (REDACTED_PLACEHOLDER, ["-","-","-","-"]),
}

# ---------------------------------------------------------------------------
# Answer key, resolved to Paper ID: Blue (the colour identification code
# printed on the uploaded scan / compilation).
# Transcribed directly from the "ANSWER KEYS" pages included at the end of
# the compiled PDF (separate Biology / Physics / English / Chemistry answer
# tables), then renumbered into the same continuous 1-220 sequence used
# above for QUESTIONS. Letters are lower-case a/b/c/d matching each
# question's option order as printed. "x" marks a question the printed
# answer key itself left blank / marked with an "X" (Physics Q40 & Q44,
# i.e. global 128 & 132; Chemistry Q47 and Q55-Q58, i.e. global 209 and
# 217-220) - these should be treated as unscored / no official answer
# rather than guessed.
#
# KNOWN DATA ISSUES:
# - See DIAGRAM_MCQS above for questions whose full context depends on an
#   untranscribed figure/graph; letter answers below are kept as printed
#   in the official key but have not been independently re-derived from
#   the (unavailable) figures.
# - See REDACTED_MCQS above for the four Chemistry questions (global
#   217-220) that were illegible/blank ("XXXXX...") in the source scan.
# - English Q145 (orig Q13) has two option slots (a) and (c) that are
#   identical in the printed source ("...on anything but the most
#   superficial level."); this looks like a transcription artifact in the
#   original compiled PDF rather than an error introduced here.
KEY_RAW = """
1 a
2 c
3 c
4 a
5 b
6 c
7 d
8 a
9 a
10 c
11 b
12 b
13 a
14 b
15 b
16 d
17 b
18 c
19 a
20 b
21 a
22 d
23 d
24 a
25 c
26 d
27 b
28 d
29 a
30 b
31 d
32 c
33 a
34 b
35 d
36 c
37 a
38 b
39 c
40 c
41 d
42 c
43 a
44 b
45 a
46 a
47 c
48 a
49 b
50 b
51 d
52 d
53 c
54 d
55 d
56 b
57 b
58 a
59 a
60 d
61 a
62 d
63 b
64 d
65 c
66 b
67 a
68 a
69 c
70 a
71 b
72 d
73 d
74 c
75 b
76 c
77 b
78 c
79 d
80 b
81 a
82 c
83 d
84 d
85 a
86 d
87 b
88 d
89 b
90 d
91 a
92 c
93 d
94 d
95 c
96 d
97 d
98 c
99 c
100 b
101 c
102 c
103 c
104 c
105 c
106 a
107 b
108 a
109 c
110 a
111 a
112 a
113 b
114 c
115 a
116 a
117 c
118 b
119 b
120 c
121 b
122 c
123 d
124 d
125 c
126 a
127 a
128 x
129 d
130 c
131 b
132 x
133 b
134 c
135 b
136 c
137 d
138 c
139 b
140 d
141 b
142 a
143 d
144 b
145 c
146 b
147 c
148 a
149 d
150 b
151 a
152 c
153 a
154 d
155 c
156 a
157 a
158 c
159 b
160 d
161 c
162 a
163 a
164 b
165 c
166 c
167 a
168 c
169 c
170 c
171 c
172 b
173 b
174 a
175 d
176 b
177 c
178 a
179 d
180 a
181 b
182 d
183 b
184 a
185 c
186 b
187 d
188 b
189 d
190 a
191 b
192 c
193 d
194 a
195 d
196 b
197 a
198 b
199 d
200 c
201 a
202 c
203 a
204 c
205 a
206 d
207 c
208 b
209 x
210 b
211 b
212 c
213 a
214 c
215 a
216 b
217 x
218 x
219 x
220 x
"""