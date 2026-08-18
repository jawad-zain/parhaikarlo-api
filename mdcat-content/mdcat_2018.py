# -*- coding: utf-8 -*-
# Transcribed from UHS MDCAT 2018 "Entrance Test" paper (Paper Code: C, Q1-220)
# + official answer key ("Check C-Series" grid, University of Health Sciences, Lahore, 23-09-2018)
#
# NOTE ON DIAGRAM MCQs (Option B):
# Four questions (96, 101, 150, 156) depend on an image (a structural diagram, a graph,
# or a circuit diagram) that cannot be reliably transcribed as plain text/options.
# These are kept in QUESTIONS with PLACEHOLDER options so the question_number sequence
# is preserved, but should be imported with is_active=False and needs_review=True.
# See DIAGRAM_MCQS below for the notes field your adapter should attach to each.

DIAGRAM_PLACEHOLDER = "[Diagram required \u2014 not transcribable from OCR text. See original PDF page for the figure/graph/circuit.]"

DIAGRAM_MCQS = {
    96: {
        "is_active": False,
        "needs_review": True,
        "notes": (
            "Question stem shows a molecular/structural diagram (context suggests a protein "
            "secondary-structure figure, e.g. alpha-helix) used to ask what stabilizes the "
            "structure shown. The image itself determines which answer is correct; cannot be "
            "safely transcribed as text. Options were legible (vander Waal's forces / disulfide "
            "bridges / unpaired electron / H-bonding between NH and CO groups) but placeholdered "
            "per Option B pending image support."
        ),
    },
    101: {
        "is_active": False,
        "needs_review": True,
        "notes": (
            "Question shows a line graph of an unnamed physical property vs atomic number "
            "for third-period elements (11-18), with a sharp peak around atomic number 14-15. "
            "The shape of the curve is required to identify which property (ionization energy, "
            "melting point, ionic radius, atomic radius) is plotted. Cannot be transcribed as text."
        ),
    },
    150: {
        "is_active": False,
        "needs_review": True,
        "notes": (
            "Question shows an op-amp circuit diagram with labeled resistor values and an input "
            "voltage of 0.50 V; asks for output voltage Vout. Exact resistor values, feedback "
            "topology, and node connections are only visible in the circuit image and could not "
            "be reliably OCR'd/transcribed as text."
        ),
    },
    156: {
        "is_active": False,
        "needs_review": True,
        "notes": (
            "Question shows a stress-strain (force vs extension) curve and asks which material "
            "(Copper / Iron / Lead / Glass) follows it. The curve's shape (linear then a knee/peak) "
            "is the entire basis for the answer and cannot be transcribed as text."
        ),
    },
}

SUBJECTS = [
    ("BIOLOGY", 1, 88),
    ("CHEMISTRY", 89, 146),
    ("PHYSICS", 147, 190),
    ("ENGLISH", 191, 220),
]

QUESTIONS = {
1: ("The thickest chamber of human heart is", ["Left atrium","Right atrium","Right ventricle","Left ventricle"]),
2: ("The enzymes required for Kreb cycle are found in __________.", ["F1 particles","Lysosomes","Cytoplasm","Matrix"]),
3: ("Coccyx vertebrae are located in", ["Cervical region","Lumber region","Pelvic region","Thoracic region"]),
4: ("Cell mediated immune response is given by:", ["T lymphocytes","B lymphocytes","Neutrophils","Macrophages"]),
5: ("Crossing over takes place during __________ of meiosis.", ["Prophase I","Telophase I","Metaphase I","Anaphase I"]),
6: ("During breathing air from Pharynx enters to", ["Trachea","Bronchioles","Alveoli","Bronchi"]),
7: ("Gradual break down of the alveolar wall leads to which type of disease in a smoker?", ["Coronary heart disease","Bronchitis","Emphysema","Asthma"]),
8: ("Which of the following holds the alpha helix of protein in its place", ["R group","Disulphide bond","Amino group","Hydrogen bond"]),
9: ("If molecule can bind to another site of the enzyme rather than the true active site, it is referred as---", ["Competitive Inhibitors","Allosteric inhibition","Non competitive inhibitors","Irreversible inhibition"]),
10: ("__________ is the site of light independent reaction", ["Thylakoid membrane","Thylakoid space","Stroma","Grana"]),
11: ("When a nerve impulse jumps from one node of Ranvier to the next in a myelinated neuron, it's called __________.", ["synapses","Saltatory conduction","Resting potential","Membrane potential"]),
12: ("The ability to distinguish between two separate points/objects is", ["Magnification","Fractionation","Centrifugation","Resolution"]),
13: ("The term \"Loss of appetite\" refers to disease:", ["Botulism","Anorexia nervosa","Obesity","Bulimia nervosa"]),
14: ("Lipid synthesis or lipid metabolism is the function of:", ["Smooth Endoplasmic Reticulum","mitochondria","Golgi complex","Rough Endoplasmic Reticulum"]),
15: ("Salivary Amylase begins to digest Starch to shorter polysaccharides and then to", ["Glucose","Maltose","Sucrose","Lactose"]),
16: ("Chemical nature of primer used in PCR process is ----------", ["RNA","Protein","Carbohydrate","DNA"]),
17: ("In viruses, a combined structure formed by core (Nucleic Acid) and capsid is:", ["Nucleocapsid","Prion","Envelope","Capsomeres"]),
18: ("Skull, vertebral column, ribs and sternum forms:", ["Appendicular skeleton","Hydrostatic Skeleton","Exoskeleton","Axial skeleton"]),
19: ("Synthesis of microtubules increases in", ["M-phase","S-phase","G1-phase","G2-phase"]),
20: ("The region of the chromosome or, more specifically, a length of the DNA molecule, which has a particular function is called --------", ["Kinetochore","Locus","Allele","Gene"]),
21: ("Urea cycle is the detoxification of", ["Creatinine","Amino acids","Carbon dioxide","Ammonia"]),
22: ("Chitin which makes the Exoskeleton in insects is further hardened by", ["Protein and Sodium Bicarbonate","Protein and Calcium Carbonate","Protein and Potassium Carbonate","Protein and Sodium Carbonate"]),
23: ("Number of salivary glands found in human oral cavity.", ["4","3","6","2"]),
24: ("Following group is the example of acoelomates", ["Annelids","Aschelminthes","Molluscs","Platyhelminthes"]),
25: ("Glycosidic bond is formed by the:", ["Removal of Oxygen","Addition of Oxygen","Removal of Water","Addition of Water"]),
26: ("Which of the following statement is correct about the respiratory pigments", ["Myoglobin and Heamoglobin has higher affinity for nitrogen","Cyanide and Haemoglobin has low affinity for oxygen","Myoglobin has more affinity for oxygen as compared to haemoglobin","Albumin, Globulin and Globin proteins are present in respiratory pigments"]),
27: ("Conversion of ammonium into nitrates is", ["Nitrification","Nitrogen Fixation","Ammonification","Denitrification"]),
28: ("An area previously supporting life is made barren, the subsequent recolonization is called-----", ["Climax community","Pioneer succession","Primary succession","Secondary succession"]),
29: ("In human female egg is fertilized in", ["Ovary","Vagina","Oviduct","Uterus"]),
30: ("Which hormone is released in female in response to FSH from pituitary gland?", ["Oestrogen","ADH","Oxytocin","Progestrone"]),
31: ("In cross section each Centriole consist of nine (each in triplets) of", ["Microfilaments","Microvilli","Microtubules","Intermediate filaments"]),
32: ("In immunoglobulins/antibodies, Two light chains and two heavy chains are linked to each other by:", ["Covalent bonds","Hydrogen bonds","Ionic bonds","Disulphide bonds"]),
33: ("In nervous system chemical messengers are called__________.", ["Neurotransmitters","Hormones","Chemoreceptors","Enzymes"]),
34: ("The first part of the large intestine is", ["Colon","appendix","Caecum","Rectum"]),
35: ("Scapula is a", ["Tail bone","Hip bone","Skull bone","Shoulder bone"]),
36: ("A complete turn of the double helix of DNA comprises of:", ["34 nm","3.4 Angstrom","3.4 nm","34 micrometer"]),
37: ("The enzymes required in Glycolysis are present in:", ["Golgi Apparatus","Cell cytoplasm","Inner Mitochondrial Membrane","Matrix of Mitochondria"]),
38: ("Which lipid is totally hydrophobic or insoluble", ["Triglycerides","Phospholipids","Waxes","Terpenoids"]),
39: ("__________ hormone is released from posterior lobe of pituitary gland.", ["Adrenaline","Thyroid stimulating hormone","FSH","Antidiuretic hormone"]),
40: ("Ribosomes are made up of __________ and __________.", ["Proteins and carbohydrates","RNA and Lipid","RNA and proteins","RNA and carbohydrates"]),
41: ("A non protein part essential for proper and essential functioning of enzyme is called", ["Additional factor","Co factor","Efficient co factor","Extra factor"]),
42: ("DNA made by joining pieces from two or more different sources", ["Probes","Restriction endonuclease","Mutated DNA","Recombinant DNA"]),
43: ("The Hormone which controls the uptake of the Sodium ions in kidney and its maintenance in blood plasma is", ["Somatotrophic Hormone","Aldosterone Hormone","Gonadotrophic Hormone","Thyroxin hormone"]),
44: ("Which statement is correct about mitochondria and chloroplast", ["Number of mitochondria and chloroplast are same in all cells","chloroplast and mitochondria are single membrane structures","chloroplast and mitochondria can not live independently","70 S ribosome is attached with the inner membrane of mitochondria and chloroplast."]),
45: ("The capillaries of glomerulus rejoin to form an--------", ["Efferent arteriole","Afferent arteriole","Peritubular capillaries","Collecting duct"]),
46: ("How many sodium ions are pumped out in response to two potassium ions transported into the membrane?", ["2","3","4","1"]),
47: ("Chance of a cross over between two loci is directly proportional to their", ["Thickness","Width","Length","Distance"]),
48: ("Process ensuring the survival of species over long periods of time, even though individual members of the species die.", ["Reproduction","Adaptability","Mitosis","Respiration"]),
49: ("Lysogenic Viruses are also known as", ["Enveloped Phage","Virulent Phage","Prophage","Bacteriophage"]),
50: ("Organs Specialized to perform different functions but structurally alike are", ["Analogous organs","Homologous organs","Autologous organs","Anuelogous organs"]),
51: ("By PCR we mean", ["Polymerase chronic reaction","Polymerase chain reaction","Polymerase copy reaction","Polymerase cross reaction"]),
52: ("If lipopolysaccharides did not appear in the wall of bacteria on staining then it will be known as __________", ["Gram negative","Gram positive","Capsule","Gram positive & gram negative"]),
53: ("The low levels of Surfactant produced by Alveolar epithelium causes:", ["Respiratory distress syndrome","Emphysema","Bronchitis","Asthma"]),
54: ("Deficiency of enzyme --------- causes combined immunodeficiency syndrome", ["Adenosine transcriptase","Adenosine transaminase","Adenosine polymerase","Adenosine deaminase"]),
55: ("Site of protein synthesis in cells are", ["Ribosomes","Endoplasmic Reticulum","Nucleolus","Smooth Endoplasmic Reticulum"]),
56: ("Keeping correct balance of ions and water in our body is called as:", ["Thermoregulation","Osmoregulation","Excretion","Selective reabsorption"]),
57: ("There are ------------- number of linkage groups in human", ["46","22","80","23"]),
58: ("The actual or preserved remains of the organisms that lived in the ancient past are called", ["Fossils","Impression","Ancient prints","Ancient cast"]),
59: ("Which one of the following cells does not have nucleus", ["Eosinophils","Neutrophils","Basophils","Platelets"]),
60: ("These structures are involved in the breakdown of old organelles.", ["Leucoplasts","Peroxisome","Glyoxysomes","Lysosomes"]),
61: ("Which combination is the example of ball and socket joints", ["Hip and shoulder joints","Hip and knee joints","Shoulder and knee joints","Hip and elbow joints"]),
62: ("In aerobic respiration", ["Pyruvate is completely oxidised to form carbondioxide and water","Pyruvate is completely oxidised to form oxygen and water","Pyruvate carboxylated to produce citrate","Pyruvate is converted to ethanol and carbondioxide"]),
63: ("Yeasts, the unicellular fungi belongs mostly to the group:", ["Deuteromycota","Zygomycota","Basidiomycota","Ascomycota"]),
64: ("Enzyme used by the Bacteria to cut the DNA of the invading Virus for its protection is", ["Restriction exonuclease","Restriction Ligase","Restriction Endonuclease","DNA polymerase"]),
65: ("The number and sequence of amino acids along a polypeptide chain is called__________ structure of a protein.", ["Quaternary","Tertiary","Primary","Secondary"]),
66: ("Rod-shaped bacteria are known as __________", ["Spirillia","Bacilli","Spirochete","Cocci"]),
67: ("__________ is the exact position of a gene on the chromosome.", ["Trait","Centromere","Genotype","Locus"]),
68: ("Parathormone hormone production is controlled by the blood", ["Ca level","sugar level","Na level","Mg level"]),
69: ("Which one of the following acts as a PACEMAKER in Heart", ["Bundle of His","Atrio ventricular node","Atrio ventricular bundles of fibers","Sino atrial node"]),
70: ("Single ringed pyrimidines are:", ["Uracil, Cytosine and Thymine","Cytosine, Guanine and Uracil","Adenine and Guanine","Cytosine, Adenine and Thymine"]),
71: ("Which one of the following is a Multiple allelic character?", ["Colour of flower in pea plant","Blood group of the human being","Shape of seed in pea plant","Length of stem in pea plant"]),
72: ("Which statement is correct about atrial systole", ["Atria relax and ventricles contract","Atria contract and ventricle also contract","Ventricles remain relax while atria contract","Atria and ventricles are relaxed"]),
73: ("Growth in the larva of young arthropods is restricted by", ["Exoskeleton","Appendages","Endoskeleton","Reduced mitosis"]),
74: ("At the last step of Glycolysis which of the following compound is formed", ["Pyruvic Acid/Pyruvate","Lactic acid","Ethyl Alcohol","Fructose Phosphate"]),
75: ("NADP, nicotinamide adenine dinucleotide phosphate, is a carrier of:", ["-OH Group","O2 Group","Hydrogen","Phosphate"]),
76: ("When filtration is completed the waste products through distal tube of Nephrons empties to", ["Efferent Arterioles","Collecting Tubules","Peritubular capillaries","Proximal tubules"]),
77: ("Blood solute potential is controlled by following hormone", ["Estrogen","Ephinephrin","Thyroxin","Vasopressin"]),
78: ("The temperature that promotes the maximum activity of enzyme is referred as----", ["Fixed temperature","Optimum temperature","Controlled temperature","Active temperature"]),
79: ("Divergent Evolution produces:", ["Vital Organs","Homologous Organs","Vestigial Organs","Analogous Organs"]),
80: ("Tonoplast bounds which organelle", ["Golgi Complex","Nucleus","Endoplasmic Reticulum","Vacuoles"]),
81: ("Antivenom given after a snake bite venom is an example of", ["Natural passive immunity","Artificial active immunity","Natural active immunity","Artificial passive immunity"]),
82: ("The cisternae breaks up into vesicles from __________, __________ of Golgi complex.", ["convex, maturing face","concave, forming face","convex, forming face","concave, maturing face"]),
83: ("Which hormone causes the contraction walls of uterus during the process of birth?", ["FSH","STH","Oxytocin","LTH"]),
84: ("Which of the following is Unsaturated \"Fatty Acid\"", ["Stearic Acid","Palmitic Acid","Butyric Acid","Oleic Acid"]),
85: ("When we extract Carotenoids from its source we see that it is", ["Violet in color","Blue green in color","Yellow green in color","Yellow to orange red in color"]),
86: ("When two or more Alleles do not show complete dominance or both the Alleles are expressing independently in heterozygotic condition. Such a condition is called", ["Complete dominance","Over dominance","Co dominance","Incomplete dominance"]),
87: ("Taste buds on the tongue are example of:", ["Pressure receptors","Chemoreceptors","Thermoreceptors","Photoreceptors"]),
88: ("Which of the following hormone acts on the uterus wall for thickening?", ["Progesterone","Zona pellucida","Follicle stimulating hormone","Oxytocin"]),

89: ("If concentration time graph of a reactant indicates a constant half-life, then the order of reaction with respect to that reactant is:", ["zero order","half order","second order","first order"]),
90: ("C2H5OH + CH3COOH \u21cc CH3COOC2H5 + H2O. Which of the following catalyst is used in the above reaction", ["Conc. H2SO4","Pumice stone","Pt","Ni"]),
91: ("Halothane is a halo derivative of", ["Methane","Ethane","Methanol","Ethanol"]),
92: ("The species which are produced by heterolytic bond breaking and can act as electron pair donors are known as.", ["Nucleophiles","Cations","Free radicals","Anions"]),
93: ("The product of the concentrations of each ion in a saturated solution of a sparingly soluble salt at 298 K, raised to the power of their relative concentrations is", ["Ksp","Ka","Kw","Kb"]),
94: ("The catalyst used for the manufacture of H2SO4 by contact process is", ["SO3","V2O5","Fe2O3","Pt/Pd"]),
95: ("Ligands having two lone pairs of electrons for donation to the central transition metal ion are known as", ["polydentate ligands","monodentate ligand","bidentate ligands","hexadentate ligands"]),
96: (DIAGRAM_PLACEHOLDER + " [Original stem: \"The stability in the following structure is due to the\" \u2014 shows a molecular/helical structure diagram]", [DIAGRAM_PLACEHOLDER]*4),
97: ("Which is the structure of polyvinyl chloride (polychloroethene)?", ["-[CCl2-CCl2]-","-[HCCl-CHCl]-","[H2C=CH-Cl]","-[H2C-CHCl]-"]),
98: ("Nylon-6,6 is also called", ["polystyrene","polyester","polyamide","polyvinyl alcohol"]),
99: ("Which compound will be produced by the oxidation of ethanal by acidified K2Cr2O7?", ["Ethene","Ethanol","Ethanoic acid","Ethanone"]),
100: ("Alcohol in which carbon atom bonded to OH group is further attached with three alkyl groups is", ["Tertiary alcohol","Primary alcohol","Aromatic alcohol","Secondary alcohol"]),
101: (DIAGRAM_PLACEHOLDER + " [Original stem: \"The following sketch shows the variation in a physical property of third period elements against their atomic numbers... What physical property is plotted?\" \u2014 shows a line graph, atomic number 11-18 on x-axis, sharp peak near 14-15]", [DIAGRAM_PLACEHOLDER]*4),
102: ("The standard electrode potential of hydrogen is arbitrarily taken at 298 K as------", ["0.00 volt","0.10 volt","10.0 volt","1.00 volt"]),
103: ("The potential difference of an electrochemical cell is measured by", ["Ammeter","Voltmeter","Galvanometer","Calorimeter"]),
104: ("Which of the following acts as a nucleophile in the reaction of alkyl halide with alcoholic/aqueous ammonia?", ["H+","NH3","NO2+","Br-"]),
105: ("Liquid in the container has temperature 70\u00b0C. What will be the temperature in Kelvin Scale?", ["350K","343K","300K","283K"]),
106: ("The formula which shows the simplest whole number ratio for the atoms of different elements in a compound is", ["ionic formula","structural formula","empirical formula","molecular formula"]),
107: ("Which one will act as a strong acid.", ["Chloroethanoic acid","Ethanoic acid","Trichloroethanoic acid","Dichloroethanoic acid"]),
108: ("The shape of [Co(NH3)6]3+ complex is", ["linear","square planar","tetrahedral","octahedral"]),
109: ("Amino acids react with each other such that the -COOH group of one amino acid reacts with the -NH2 group of another amino acid to give a condensed structure (H2N-CHR-CO-NH-CHR-COOH), as shown in the diagram. What is the name of the circled part of this structure?", ["Ester linkage","peptide linkage","carbide linkage","azide linkage"]),
110: ("3.0 mole of calcium will contain --------- g of calcium", ["105 gm","120 gm","80 gm","100 gm"]),
111: ("Which of the following is the correct equation to calculate relative molecular mass of a gas.", ["M=mPR/VT","M=PV/mRT","M=mPRT/V","M=mRT/PV"]),
112: ("Reaction of water with quick lime results in the rise in the temperature of the system. Using the concept of energy change, indicate the nature of the reaction?", ["Endothermic Reaction","Non spontaneous reaction","Third Order reaction","Exothermic Reaction"]),
113: ("Which one of the following compounds acts as catalyst when alcohols react with carboxylic acids.", ["Pt","conc. HNO3","Ni","conc. H2SO4"]),
114: ("In Period 2 and Period 3 maximum melting point is shown by elements:", ["Nitrogen and phosphorous","Neon and Argon","Lithium and Sodium","Carbon and Silicon"]),
115: ("Which one of the following reagents is used to distinguish between aldehydes and ketones?", ["Alkaline Iodine","Tollen's reagent","Bromine","2,4-DNPH"]),
116: ("Gas is enclosed in a container of 20cm3 with a moving piston. According to kinetic theory of gases, what will be the effect on freely moving molecules of the gas if temperature is increased from 20\u00b0C to 100\u00b0C?", ["Pressure will become one half","Volume will be increased","Temperature has no effect on freely moving molecules","Colliding capability of molecule will become lower"]),
117: ("Which of these pollutants is produced by burning of coal and causes acid rain.", ["NO","CO2","SO2","CO"]),
118: ("Role of a catalyst in a chemical reaction is to", ["Decrease yield of a reaction","Decrease rate of a reaction","Increase yield of product","Increase rate of a reaction"]),
119: ("The essential property of a fertilizer is that it should be", ["Immiscible","Highly soluble","Insoluble","Partially Soluble"]),
120: ("Which option shows all the molecules with bond angle 109.5\u00b0.", ["CH4, NH4+, PH3","SiCl4, H2O, BeCl2","SiCl4, NH4+, CH4","CH4, CCl4, NH3"]),
121: ("Down the group, acid-base behavior of metallic oxides of group 2 elements changes to", ["more basic","no change","less basic","more acidic"]),
122: ("Butane molecule can have max. no. of isomers", ["5","3","4","2"]),
123: ("Select one which is an alcohol", ["CH3-CH2-Br","CH3-O-CH3","CH3COOH","CH3-CH2-OH"]),
124: ("Which is the correct electronic configuration of Chromium (24Cr)?", ["1s2 2s2 2p6 3s2 3p6 4s2 3d4","1s2 2s2 2p6 3s2 3p6 4s2 3d6","1s2 2s2 2p6 3s2 3p6 3d6","1s2 2s2 2p6 3s2 3p6 4s1 3d5"]),
125: ("Which one of the following is the structure of Teflon?", ["(-CF2-CF2-)n","(-CF2-CCl2-)n","(-CH2-CH2-)n","(-CF2-CH2-)n"]),
126: ("Which one of the following enthalpy changes is always exothermic?", ["Enthalpy of combustion","Enthalpy of formation","Enthalpy of atomization","Enthalpy of solution"]),
127: ("While finding the relative atomic mass, which of the following standards is used to compare the atomic mass of chlorine (35.5 amu).", ["Carbon-13","Neon-20","Carbon-12","Nucleon number"]),
128: ("Which compound is obtained by the elimination of bromopropane?", ["propene","butene","ethene","propane"]),
129: ("Which product is formed by the reaction of carboxylic acid with alcohol?", ["Alkane","Ether","Aldehyde","Ester"]),
130: ("In aqueous solution amino acids exist in an ionic form, shown as +NH3-CHR-COO- in the diagram. This ionic form of amino acid is known as", ["zwitterion","amphoteric ion","cation","anion"]),
131: ("Reaction mechanism of alkanes with halogens is known as", ["Propagation","Free radical substitution","Addition","Elimination"]),
132: ("Why is it necessary to distill aldehyde formed from oxidation of primary alcohol through acidified potassium dichromate(VI) solution or acidified sodium dichromate(VI) solution?", ["Aldehyde formed may be oxidised further to carboxylic acid concerned.","Aldehyde formed is unstable and decomposes back to original precursor, i.e., primary alcohol.","Aldehyde may be oxidised further to a ketone.","Aldehyde formed may react with primary alcohol, the original reactant."]),
133: ("Electron affinity of the atom is the energy released when", ["Covalent bond of molecule is broken","Electron is added to gaseous atom","Electron is removed from gaseous atom","Covalent bond is formed between the atoms"]),
134: ("Which mechanism of reactions is shown by carbonyl compounds?", ["Electrophilic addition","Electrophilic substitution","Free radical substitution","Nucleophilic addition"]),
135: ("Which of the following compounds is solid at room temperature?", ["Ethanol","Butane","Methanol","Phenol"]),
136: ("Halogens are being used as fire extinguishers, mild antiseptics, CFCs and many other organic chemicals. Which of the following halogens is used to kill bacteria in drinking water", ["Bromine","Fluorine","Chlorine","Iodine"]),
137: ("Which of the following acts as an electrophile in the electrophilic substitution of benzene with bromine?", ["Br+","FeCl4+","Fe+2","Fe+3"]),
138: ("According to Lowry-Bronsted Acid & Base Concept, H2O is", ["An Acid","A Base","An Amphoteric Species","A Salt"]),
139: ("Which one of the following compounds is known as tertiary alcohol?", ["1-Propanol","2-methyl-2-propanol","2-methyl-1-propanol","2-Propanol"]),
140: ("Which of the following molecules has the largest number of shared pairs of electrons?", ["C2H4","N2","CO2","NH3"]),
141: ("Nitrogen is present in air as a major constituent. It is an inactive gas in comparison with oxygen, which is the next major constituent of air. The nonreactive nature of nitrogen is due to the reason;", ["there is one lone pair of electrons on each nitrogen atom in its molecule.","there is a triple covalent bond in the nitrogen molecule which is very strong and the molecule is non polar.","nitrogen has three unpaired electrons in its 2p orbital which is a comparatively stable electronic configuration.","there is a triple covalent bond in the nitrogen molecule which is very strong and the molecule is polar."]),
142: ("The dilute solution of ------------- is called vinegar", ["Formic acid","Oxalic acid","Benzoic acid","Acetic acid"]),
143: ("Percentage of nitrogen by volume in air is", ["78%","50%","20%","98%"]),
144: ("Bromination of alkene, H2C=CH2 + Br2 \u2192 H-C(Br)H-C(Br)H2, is shown in the following reaction. This reaction is used for", ["Detection of ketones","Detection of double bond","Identification of Primary and secondary alcohols","Detection of Aldehydes"]),
145: ("What is the order of increasing reactivity of alkyl halides?", ["fluoroalkane<chloroalkane<bromoalkane<iodoalkane","iodoalkane<bromoalkane<chloroalkane<fluoroalkane","iodoalkane>bromoalkane>chloroalkane>fluoroalkane","fluoroalkane>chloroalkane>bromoalkane>iodoalkane"]),
146: ("Which of the following would react with ozone in the atmosphere?", ["F radical (F\u2022)","O2","O radical (O\u2022)","Cl radical (Cl\u2022)"]),

147: ("A 5 watt LED bulb converts 80% of the power into light photons of wavelength 660 nm. What is the number of photons emitted from the bulb in one second.", ["5.8 x 10^34","7.5 x 10^18","6.6 x 10^7","1.3 x 10^19"]),
148: ("If Cv = 5/2 R, Cp will be", ["2/5 R","2/7 R","5/2 R","7/2 R"]),
149: ("The rate at which work is being done is called", ["Power","Energy","Density","Force"]),
150: (DIAGRAM_PLACEHOLDER + " [Original stem: \"An input voltage Vin of 0.50 V is applied to an op-amp connected as shown in the diagram. What is the output voltage Vout?\" \u2014 shows an op-amp circuit with labeled resistor values]", [DIAGRAM_PLACEHOLDER]*4),
151: ("A signal of -80 mV is applied to the inverting terminal of the amplifier while the non-inverting terminal is grounded. The gain of the amplifier is 25, using Rin (R1) equal to 3\u03a9 and Rf (R2) equal to 75\u03a9. What would be the value of the output signal?", ["200 mV","-3 V","2 V","3 V"]),
152: ("When the frequency of the applied force becomes equal to one of the natural frequencies of a body then the body oscillates with maximum displacement. This phenomenon is called", ["Heating","Resonance","Reverberation","Damping"]),
153: ("Force is a derived quantity; its derived unit can be expressed in terms of the base units as,", ["kg m s^-2","kg cm s^-2","kg m^2 s^2","kg m s^2"]),
154: ("e/m of an electron is given by the relationship,", ["e/m = 2(V/B^2 r^2)","e/m = (V/Br)^2","e/m = V.r/B","e/m = VB/r"]),
155: ("Lenz's law in electromagnetic induction is the direct consequence of the principle of conservation of", ["energy","charge","momentum","mass"]),
156: (DIAGRAM_PLACEHOLDER + " [Original stem: \"Which material will follow the below stress-strain curve.\" \u2014 shows a force vs extension graph]", [DIAGRAM_PLACEHOLDER]*4),
157: ("A wheel starts rotating from rest with angular acceleration of 2 rad s^-2 till its angular speed becomes 6 rad/s. The angular displacement of the wheel will be equal to", ["4 rad","9 rad","12 rad","7 rad"]),
158: ("Coulomb's law is given by the formula F = k q1 q2 / r^2. The magnitude of k, having the unit N m^2 C^-2, for free space is equal to", ["9 x 10^7","6 x 10^7","10 x 10^9","9 x 10^9"]),
159: ("Simple Harmonic Motion of a body is described by which statement(s) mentioned below: K: K.E is maximum when displacement x=0. L: P.E is maximum when x=0. M: P.E is maximum when x=\u00b1x0", ["K and L","K and M","K, L and M","L and M"]),
160: ("Which of the following gives the relationship between linear velocity and angular velocity?", ["v = r\u03c9","v = r\u03b8","v = s\u03c9","v = s\u03b8"]),
161: ("A torch is rated 2.2 V, 0.25 A. Calculate the charge passing through the bulb in one second and energy transferred by the passage of each coulomb of charge.", ["2.5 C and 0.55 J","0.25 C and 2.2 J","0.25 C and 2.2 V","0.25 C and 0.55 J"]),
162: ("Energy consumed by a 60 watt bulb in 2 minutes is equal to", ["7.2 kilo joules","720 joules","120 joules","72000 joules"]),
163: ("If one mole of an ideal gas is heated at constant pressure, then the first law of thermodynamics can be written as:", ["Cp \u0394T = Cv \u0394T + P\u0394V","Cv \u0394T = Cp \u0394T + P\u0394V","Cp \u0394T = \u0394Cv T + P\u0394V","\u0394Cp T = \u0394Cv T + P\u0394V"]),
164: ("The de Broglie wavelength of an electron travelling with a speed of 1.0x10^7 m/s is equal to, (h=6.6x10^-34 Js and me=9.1x10^-31 kg)", ["7.3x10^11 m","7.3x10^8 m","7.3x10^-11 m","7.3x10^-13 m"]),
165: ("Find the mean translational kinetic energy of ideal hydrogen gas at 17\u00b0C.", ["6.21x10^-21 J","5x10^-21 J","6.21x10^-12 J","6x10^-21 J"]),
166: ("Calculate the activity (decaying atoms per unit time) of radioactive strontium-90 having 6.7x10^21 atoms at t=0. Decay constant of strontium-90 is 8.3x10^-10 s^-1.", ["8.01x10^10 Bq","5.6x10^11 s^-1","5.6x10^12 Bq","12x10^11 Bq"]),
167: ("If the time period of the oscillation is 20 micro-sec, then what will be the frequency of that oscillating body?", ["5000 Hz","50000 Hz","20000 Hz","1000 Hz"]),
168: ("In photo-emission from a metal, if light of wavelength lambda is replaced by light of wavelength lambda/4, the maximum kinetic energy of the photo-electrons", ["decreases by an amount equal to half of an incident photon of wavelength lambda","increases by an amount equal to four times the energy of an incident photon of wavelength lambda","increases by an amount equal to the work function of the metal","decreases by an amount equal to the energy of an incident photon of wavelength lambda"]),
169: ("A cyclist is traveling at 15 ms^-1. She applies brakes so that she doesn't collide with the wall in front of her at a distance of 18m. Calculate the magnitude of deceleration.", ["6.3 ms^-2","5.3 ms^-2","13 ms^-2","12.5 ms^-2"]),
170: ("In a practical transformer, mutual induction between primary and secondary coils takes place. In such a transformer, what can be deduced about the power", ["power output = power input","power output > power input","power output \u2265 power input","power output < power input"]),
171: ("If the slope of the velocity-time graph is not constant at different points, then the body is moving with", ["uniform velocity","increasing acceleration","average acceleration","constant acceleration"]),
172: ("Electric potential due to a 2 \u03bcC charge at a distance of one meter is equal to", ["18x10^4 volt","1.8x10^6 volt","1.8x10^9 volt","1.8x10^4 volt"]),
173: ("Kirchhoff's first law is a manifestation of", ["Law of conservation of momentum","Law of conservation of mass","Law of conservation of energy","Law of conservation of charge"]),
174: ("Light photons, each of energy 3.5x10^-19 J, fall on the cathode of a photocell. The current through the cell is reduced to zero by taking the cathode to a potential +0.25 V relative to the anode. The work function of the cathode is:", ["3.35x10^-19 J","3.5x10^-19 J","3.25x10^-19 J","3.1x10^-19 J"]),
175: ("A diffraction grating has 500 lines per mm; its grating element d is equal to", ["2x10^-6 meter","2x10^-2 meter","2x10^-2 cm","2x10^-6 cm"]),
176: ("In the case of linear deformation, the ratio of tensile stress to tensile strain is called", ["energy stored in a stretched wire","Young's double slit phenomenon","Bulk modulus","Young's modulus"]),
177: ("What is the name of the energy which is released when an atom is formed from its constituent particles?", ["Atomic Energy","Radioactive Energy","Nuclear Energy","Binding Energy"]),
178: ("Calculate the half life of bismuth-214, which has a decay constant of 4.3x10^-3 s^-1.", ["2.9x10^-3 s","1.6x10^-4 s","3.9x10^3 s","2.9x10^3 s"]),
179: ("What is the main feature required by the optical fiber for the propagation of light in an optical fiber?", ["Optical glass should be cleaned","Light should be totally confined within the fiber.","They are cheaper than copper wire","LED light must be used"]),
180: ("Two long, parallel conductors which are free to move are arranged 1.0 cm apart. A steady current of 20 A flows in each of the conductors in the same direction. The conductors", ["remain stationary","move towards each other","move away from each other","move at right angles to each other"]),
181: ("A stone of mass 2.0 kg is dropped from a rest position 5.0m above the ground. What is its velocity at a height of 3.0m above the ground?", ["12.5 m/s","6.3 m/s","9.3 m/s","16.0 m/s"]),
182: ("In case of half wave rectification, the resistance of the diode during the negative half of A.C is", ["very high","very low","a few ohms","Negative"]),
183: ("Newton's first law of motion is also known as", ["law of inertia","law of electromagnetism","law of universal gravity","law of conservation of momentum"]),
184: ("When a potential difference is applied across the ends of a uniform wire of length l and radius r, a current I flows in the wire. If the same potential difference is applied to the ends of another wire of the same material but of length 2l and radius 2r, the current in the wire is", ["I/4","2I","I","I/2"]),
185: ("A shock wave is produced due to an earthquake which makes the buildings move in the direction of the shock wave. Which progressive wave would this be?", ["longitudinal wave","transverse wave","material wave","particle wave"]),
186: ("A neutron having mass equal to a proton (mp=1.6x10^-27 kg) is moving in a magnetic field of intensity 1.20x10^-3 T with a speed of 2.0x10^7 ms^-1. What is the Maximum force experienced by the neutron.", ["3.84x10^-15 N","0","3.84x10^-12 N","38.4x10^-15 N"]),
187: ("In S.H.M the kinetic energy of the body is maximum when", ["The body is at mean position","The body is at extreme position from the mean.","The body is exactly half way down between mean and extreme position","The body is somewhere between mean and extreme position."]),
188: ("The different magnitudes of the same physical quantities are measured by comparing them to:", ["available scale","standard size","each other","other physical quantities"]),
189: ("Force experienced per unit positive test charge at a point in an electric field is the definition of:", ["Electric potential energy","Electric field strength","Electric potential","Electric field"]),
190: ("A metal rod of length 10.0 cm is moving at a speed of 0.5 ms^-1 in a direction perpendicular to a 0.20 T magnetic field. Find the emf produced in the rod.", ["2.0x10^-3 V","0.50x10^-2 V","1.0x10^-2 V","1.0x10^-3 V"]),

191: ("That is just an example of what I complain__________.", ["Of","Off","To","With"]),
192: ("The region __________ which they were passing was known as the Land of Thirst and Death", ["Through","By","In","From"]),
193: ("I know how to __________ a throat for inspection.", ["Force","Prepare","Expose","Open"]),
194: ("It is better for me to __________ than to shed the blood of an innocent boy.", ["Died","Die","Had died","Have died"]),
195: ("SPOT THE ERROR \u2014 The most important and the most difficult thing to achieve is a desire between individuals to limit the size of family.", ["The most important","the most difficult thing to achieve","is a desire","between individuals"]),
196: ("SPOT THE ERROR \u2014 There is terror from the outset, and there are all the components necessary to create a melodrama-- a dimly-lit bus station, the storm accompanied by flashes of lighting, and the promise of violent action or emotion", ["from the outset","and there are all the components necessary to","the storm accompanied by","the promise of violent action or emotion"]),
197: ("SPOT THE ERROR \u2014 The king feels disturbed and on hearing these words he could not control his tears", ["feels","disturbed","and on hearing these words","he could not"]),
198: ("SPOT THE ERROR \u2014 He had earned the reputation of being a great jester, and jests were expected from him.", ["had earned the reputation","of being a great","jester, and jests were","expected from him."]),
199: ("SPOT THE ERROR \u2014 He glances back at the door, then turns his attention once more towards the paper and begins going through it casually.", ["glances back at the door","then turns his attention once more","towards the paper","begins going through it casually"]),
200: ("SPOT THE ERROR \u2014 However, by being so long in lowest form I gained an immense advantage over the cleverer boys.", ["However, by being so long in","lowest form","I gained an immense","advantage over the cleverer boys."]),
201: ("Choose the CORRECT sentence:", ["The manager looked on me in some alarm.","The manager looked on me with some alarm.","The manager looked at me with some alarm.","The manager looked at me in some alarm."]),
202: ("Choose the CORRECT sentence:", ["There is no clearly defined plot nor is there an attempt to establish a strong \"hero figure\"","There is neither clearly defined plot not is there an attempt to establish a strong \"hero figure\"","There is not clearly defined plot nor is there any attempt to establish a strong \"hero figure\"","There is not either clearly defined plot nor is there an attempt to establish a strong \"hero figure\""]),
203: ("Choose the CORRECT sentence:", ["I lost my little plough in a furrow and I cried and cried until he had made me another plough","I lost my little plough in a furrow and I have cried and cried until he made me another plough","I lost my little plough in a furrow and I had cried and cried until he made me another plough","I lost my little plough in a furrow and i cried and cried until he made me another plough."]),
204: ("Choose the CORRECT sentence:", ["A common cause of failure is a mistaking ambition for the boy on the part of the parents.","A common cause of failure is a mistook ambition for the boy on the part of the parents.","A common cause of failure is a mistaken ambition for the boy on the part of the parents.","A common cause of failure is a mistake ambition for the boy on the part of the parents."]),
205: ("Choose the CORRECT sentence:", ["In my experience, the awakening of that clear judgement as to what the college is for, is not as difficult as is often supposed.","In my experience, the awakening of a clear judgement as for what the college is for, is not as difficult as is often supposed","In my experience, the awakening of a clear judgement as to what the college is for, is not as difficult as is often supposed","In my experience, the awakening of a clear judgement as to what the college is for, is not as much as difficult as often supposed."]),
206: ("Choose the CORRECT sentence:", ["Oppressive it was, too, with the heaviness of a storm.","Oppressive it was, too, in the heaviness of a storm.","Oppressive it was, too, up the heaviness of a storm.","Oppressive it was, off the heaviness of a storm."]),
207: ("Choose the CORRECT sentence:", ["I leaned over the parapet and looked down.","I leaned at the parapet and looked down.","I leaned against the parapet and looked down.","I leaned down the parapet and looked down."]),
208: ("Choose the CORRECT sentence:", ["Towards the end of the month he took to his bed.","Towards the end of the month he took into his bed.","Toward end of month he took to his bed.","Towards the end of month he took to his beds."]),
209: ("Choose the CORRECT sentence:", ["China is now the fashion around the world.","China is now the fusion around the world.","China is now the function around the world.","China is now fissure around the world."]),
210: ("Choose the CORRECT sentence:", ["The sufferer becomes depressed and feels very ill.","The sufferer becomes depress and feels very ill.","The sufferer becomes depressed and feeling very ill.","The sufferer become depressed and feels very ill."]),
211: ("Ilk", ["Breed","Civilization","Origin","Culture"]),
212: ("Dunce", ["Brainy","Intellectual","Cautious","Oaf"]),
213: ("Hiatus", ["Lull","Longing","Heretical","Veneration"]),
214: ("Buffers", ["Shocks","Shield","Support","Window"]),
215: ("Encumber", ["Clear","Spacious","Convenient","Strained"]),
216: ("Hector", ["Harass","Helpmate","Hellish","Hefty"]),
217: ("Nexus", ["Focal point","Success","Hinterland","Politics"]),
218: ("Perpetuate", ["Skulk","Eternize","Deviate","Perish"]),
219: ("August", ["Local","Old","Venerable","Foreign"]),
220: ("Lampoon", ["Appreciate","Burlesque","Approve","Annoy"]),
}

# ---------------------------------------------------------------------------
# Answer key, transcribed from the official "Check C-Series" grid.
# That grid lists, for each question, the correct-answer LETTER under four
# columns headed A / B / C / D (one column per paper code A-D, NOT per
# option). This transcription (Paper Code: C) is filed here as a flat
# "Q letter" list, already resolved to the Paper-C column, matching the
# KEY_RAW convention used in the 2022 transcription file.
#
# KNOWN DATA ISSUE: Q188's Paper-C entry in the source grid reads "S", which
# is not a valid option letter (A-D). This is very likely a scan/OCR artifact
# in the original released key (or a since-corrected/withdrawn question).
# Flagging for manual verification against the original key image rather
# than guessing; do not import an answer for Q188 until confirmed.
KEY_RAW = """
1 d
2 d
3 c
4 a
5 a
6 a
7 c
8 d
9 c
10 c
11 b
12 d
13 b
14 a
15 b
16 d
17 a
18 d
19 d
20 d
21 d
22 a
23 c
24 d
25 c
26 c
27 a
28 d
29 a
30 c
31 c
32 d
33 a
34 d
35 d
36 c
37 b
38 a
39 b
40 c
41 d
42 d
43 d
44 c
45 a
46 b
47 a
48 a
49 b
50 a
51 b
52 b
53 b
54 b
55 a
56 b
57 d
58 d
59 b
60 a
61 a
62 d
63 d
64 d
65 c
66 a
67 d
68 a
69 a
70 b
71 b
72 a
73 a
74 a
75 b
76 b
77 b
78 b
79 a
80 d
81 d
82 d
83 c
84 c
85 d
86 a
87 b
88 a
89 d
90 a
91 d
92 a
93 a
94 b
95 c
96 c
97 a
98 c
99 c
100 c
101 b
102 a
103 b
104 b
105 a
106 c
107 c
108 a
109 b
110 b
111 d
112 d
113 d
114 d
115 b
116 b
117 a
118 d
119 b
120 c
121 a
122 d
123 d
124 d
125 a
126 a
127 a
128 a
129 d
130 a
131 d
132 b
133 d
134 d
135 d
136 c
137 a
138 a
139 a
140 b
141 d
142 d
143 a
144 b
145 d
146 c
147 d
148 d
149 d
150 c
151 c
152 b
153 a
154 a
155 a
156 d
157 b
158 d
159 d
160 a
161 b
162 a
163 c
164 c
165 d
166 c
167 b
168 a
169 a
170 d
171 a
172 d
173 b
174 b
175 d
176 a
177 d
178 c
179 d
180 b
181 d
182 a
183 d
184 a
185 a
186 b
187 a
188 UNRESOLVED
189 b
190 d
191 a
192 a
193 a
194 b
195 d
196 c
197 a
198 d
199 c
200 b
201 d
202 a
203 d
204 c
205 c
206 a
207 c
208 a
209 a
210 a
211 a
212 d
213 a
214 b
215 d
216 a
217 a
218 b
219 c
220 b
"""