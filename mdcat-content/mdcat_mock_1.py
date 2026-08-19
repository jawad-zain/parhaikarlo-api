# -*- coding: utf-8 -*-
# MDCAT Full Mock Test #1 — ORIGINALLY AUTHORED content (not transcribed from any
# real UHS/PMDC past paper). Built 2026-08-18 to give the practice-question pool
# fresh, non-recycled items at the exact official MDCAT subject weightage, since
# quiz.services.select_questions_for_full_mock() samples 34/27/27/9/3% straight
# from whatever is_active+is_verified in the Question pool — until now that pool
# was 100% past-paper questions (2012-2025), so repeat mock attempts kept
# resurfacing the same historical items.
#
# Total MCQs: 200. Subject weightage matches quiz.services.FULL_MOCK_WEIGHTAGE:
#   Biology 34% (68), Chemistry 27% (54), Physics 27% (54),
#   English 9% (18), Logical Reasoning 3% (6).
# Topic/subtopic allocation is spread across (almost) every topic in
# mdcat-content/syllabus/pmdc_mdcat_syllabus.json, weighted roughly by how many
# subtopics each topic has.
#
# NUMBERING: one continuous scheme 1-200, subject order matches the modern
# (2022+) UHS paper layout: Biology, Chemistry, Physics, English, Logical Reasoning.
#   Biology            Q.1   - Q.68
#   Chemistry          Q.69  - Q.122
#   Physics            Q.123 - Q.176
#   English            Q.177 - Q.194
#   Logical Reasoning  Q.195 - Q.200
#
# IMAGE QUESTIONS: capped at 2 (per instruction — "not more than 2 image
# questions" in a mock). Both are flagged below in VISUAL_MCQS; they need a
# real diagram sourced/drawn and attached via import_question_images before
# they can go live (same pipeline used for past-paper diagram MCQs — see
# [[mdcat-image-tooling]]). Until then the JSON exporter marks them
# needs_review=True / is_visual_required=True so they import as unverified.
VISUAL_MCQS = {
    51: {
        "subject": "BIOLOGY",
        "notes": "Anterior cross-section of the human heart with four labelled "
                 "internal structures P/Q/R/S; P is the valve between left atrium "
                 "and left ventricle.",
    },
    146: {
        "subject": "PHYSICS",
        "notes": "Displacement-time graph of a particle in SHM, with point P marked "
                 "where the curve crosses the time axis moving downward.",
    },
}

SUBJECTS = [
    ("BIOLOGY", 1, 68),
    ("CHEMISTRY", 69, 122),
    ("PHYSICS", 123, 176),
    ("ENGLISH", 177, 194),
    ("LOGICAL REASONING", 195, 200),
]

QUESTIONS = {
    # ---------------- BIOLOGY (1-68) ----------------
    1: ("A virus that infects and replicates specifically within bacterial cells is called a:",
        ["Retrovirus", "Bacteriophage", "Prophage", "Virion"]),
    2: ("Which component forms the protein coat that encloses the nucleic acid of a virus?",
        ["Capsid", "Envelope", "Nucleoid", "Pilus"]),
    3: ("HIV primarily attacks which type of human cell?",
        ["Red blood cells", "Helper T (CD4+) lymphocytes", "Platelets", "Hepatocytes"]),
    4: ("HIV belongs to which group of viruses characterized by using the enzyme reverse transcriptase?",
        ["Retroviruses", "Bacteriophages", "Adenoviruses", "Rhabdoviruses"]),
    5: ("The complete aerobic oxidation of one molecule of glucose yields approximately how many ATP molecules (theoretical maximum)?",
        ["2", "4", "36-38", "100"]),
    6: ("Glycolysis, the first stage of cellular respiration, takes place in the:",
        ["Mitochondrial matrix", "Cytoplasm", "Nucleus", "Inner mitochondrial membrane"]),
    7: ("The electron transport chain in aerobic respiration is located in the:",
        ["Cytoplasm", "Outer mitochondrial membrane", "Inner mitochondrial membrane", "Mitochondrial matrix"]),
    8: ("Which of the following is classified as a macromolecule?",
        ["Glucose", "Glycerol", "Starch", "Acetic acid"]),
    9: ("The high specific heat capacity of water, which helps stabilize body temperature, is mainly due to:",
        ["Its polarity alone", "Extensive hydrogen bonding between molecules", "Its high molecular weight", "Its low density as ice"]),
    10: ("Which of the following is a disaccharide formed from glucose and fructose?",
         ["Maltose", "Lactose", "Sucrose", "Cellulose"]),
    11: ("The type of bond that links amino acids together in a protein chain is the:",
         ["Glycosidic bond", "Peptide bond", "Hydrogen bond", "Ester bond"]),
    12: ("A triglyceride molecule is formed by the combination of glycerol with:",
         ["Three fatty acids", "Three amino acids", "Three monosaccharides", "Three phosphate groups"]),
    13: ("In the DNA double helix, adenine always pairs with:",
         ["Cytosine", "Guanine", "Thymine", "Uracil"]),
    14: ("Which feature distinguishes a prokaryotic cell from a eukaryotic cell?",
         ["Presence of ribosomes", "Absence of a membrane-bound nucleus", "Presence of a plasma membrane", "Presence of cytoplasm"]),
    15: ("Which organelles are primarily responsible for the synthesis and packaging of proteins for secretion?",
         ["Golgi apparatus and rough endoplasmic reticulum", "Lysosome", "Peroxisome", "Mitochondrion"]),
    16: ("Which organelle contains hydrolytic enzymes and is responsible for intracellular digestion?",
         ["Ribosome", "Lysosome", "Centriole", "Golgi apparatus"]),
    17: ("The constricted region of a chromosome that holds sister chromatids together is called the:",
         ["Telomere", "Centromere", "Satellite", "Nucleolus"]),
    18: ("Which structure is present in a plant cell but absent in an animal cell?",
         ["Mitochondria", "Cell wall", "Ribosomes", "Nucleus"]),
    19: ("The gap between two adjacent neurons across which a nerve impulse is transmitted chemically is called the:",
         ["Synapse", "Node of Ranvier", "Axon hillock", "Dendrite"]),
    20: ("A reflex action is best described as:",
         ["A voluntary, learned response", "An involuntary, rapid response to a stimulus", "A response controlled entirely by the cerebrum", "A hormonal response"]),
    21: ("Rods and cones, the photoreceptors of the human eye, are located in the:",
         ["Cornea", "Retina", "Iris", "Lens"]),
    22: ("Which part of the human brain is primarily responsible for maintaining balance and coordinating voluntary muscle movement?",
         ["Cerebrum", "Cerebellum", "Medulla oblongata", "Hypothalamus"]),
    23: ("The part of the brain that regulates body temperature, hunger, and thirst is the:",
         ["Thalamus", "Hypothalamus", "Pons", "Cerebellum"]),
    24: ("Enzymes increase the rate of biochemical reactions primarily by:",
         ["Increasing the temperature of the reaction", "Lowering the activation energy", "Shifting the equilibrium", "Being consumed in the reaction"]),
    25: ("According to the induced fit model of enzyme action, the active site:",
         ["Is a rigid, pre-shaped structure", "Changes shape slightly to fit the substrate", "Never interacts with the substrate", "Is identical to the substrate shape at all times"]),
    26: ("Beyond the optimum temperature, enzyme activity decreases sharply mainly because the enzyme:",
         ["Becomes more soluble", "Undergoes denaturation", "Increases its affinity for substrate", "Changes its optimum pH"]),
    27: ("A competitive inhibitor of an enzyme:",
         ["Binds to the active site and resembles the substrate", "Binds only to the enzyme-substrate complex", "Permanently destroys the enzyme", "Binds at a site distinct from the active site"]),
    28: ("Darwin's theory of evolution is primarily based on the principle of:",
         ["Use and disuse of organs", "Natural selection", "Inheritance of acquired characteristics", "Mutation pressure alone"]),
    29: ("Lamarck's theory of evolution proposed that evolutionary change occurs through:",
         ["Natural selection", "Inheritance of acquired characteristics", "Random genetic drift", "Gene mutation"]),
    30: ("The process by which two or more unrelated species independently evolve similar traits due to similar environmental pressures is called:",
         ["Divergent evolution", "Convergent evolution", "Co-evolution", "Adaptive radiation"]),
    31: ("Spermatogenesis takes place within the:",
         ["Epididymis", "Seminiferous tubules of the testis", "Vas deferens", "Prostate gland"]),
    32: ("Ovulation in the human menstrual cycle typically occurs around which day of a 28-day cycle?",
         ["Day 5", "Day 14", "Day 21", "Day 28"]),
    33: ("The surge of which hormone directly triggers ovulation?",
         ["Follicle Stimulating Hormone (FSH)", "Luteinizing Hormone (LH)", "Progesterone", "Estrogen alone"]),
    34: ("Which of the following is a bacterial sexually transmitted disease?",
         ["AIDS", "Genital herpes", "Syphilis", "Genital warts"]),
    35: ("Which type of connective tissue provides a smooth, cushioning surface at the ends of long bones in joints?",
         ["Cartilage", "Tendon", "Ligament", "Bone marrow"]),
    36: ("Cardiac muscle is described as:",
         ["Voluntary and unstriated", "Involuntary and striated", "Voluntary and striated", "Involuntary and unstriated"]),
    37: ("The repeating functional unit of a skeletal muscle fibre, bounded by two Z-lines, is called the:",
         ["Sarcomere", "Sarcolemma", "Myofibril", "Sarcoplasm"]),
    38: ("According to the sliding filament theory, muscle contraction occurs when:",
         ["Actin and myosin filaments shorten individually", "Actin filaments slide over myosin filaments, shortening the sarcomere", "Myosin filaments are destroyed", "Z-lines move apart"]),
    39: ("The shoulder and hip joints, which allow movement in almost all directions, are examples of:",
         ["Hinge joints", "Ball-and-socket joints", "Pivot joints", "Gliding joints"]),
    40: ("Rheumatoid arthritis is best classified as a/an:",
         ["Bacterial infection of the joint", "Autoimmune disease affecting joint linings", "Age-related wear of cartilage only", "Genetic mineral deficiency"]),
    41: ("Mendel's Law of Segregation states that:",
         ["Two alleles for a trait separate during gamete formation", "Genes for different traits always assort together", "Dominant alleles always mask recessive ones completely in F2", "Genes are located on chromosomes"]),
    42: ("In a monohybrid cross between two heterozygous (Aa) individuals, what is the expected phenotypic ratio in the offspring?",
         ["1:1", "1:2:1", "3:1", "9:3:3:1"]),
    43: ("Genes located close together on the same chromosome tend to be inherited together; this phenomenon is called:",
         ["Independent assortment", "Gene linkage", "Polygenic inheritance", "Codominance"]),
    44: ("A colour-blind father and a homozygous normal mother have children. What proportion of their sons will be colour-blind?",
         ["0%", "25%", "50%", "100%"]),
    45: ("Haemophilia is inherited as a/an:",
         ["Autosomal dominant trait", "Autosomal recessive trait", "X-linked recessive trait", "Y-linked trait"]),
    46: ("Which chamber of the human heart pumps oxygenated blood into the aorta?",
         ["Right atrium", "Right ventricle", "Left atrium", "Left ventricle"]),
    47: ("The natural pacemaker of the human heart is the:",
         ["Atrioventricular node", "Sinoatrial node", "Bundle of His", "Purkinje fibres"]),
    48: ("Which blood vessels have thin, one-cell-thick walls that allow exchange of substances between blood and tissues?",
         ["Arteries", "Veins", "Capillaries", "Arterioles"]),
    49: ("Which of the following carries deoxygenated blood despite being an artery?",
         ["Aorta", "Pulmonary artery", "Renal artery", "Coronary artery"]),
    50: ("The lymphatic system helps maintain fluid balance mainly by:",
         ["Producing red blood cells", "Returning excess interstitial fluid to the bloodstream", "Regulating heart rate", "Producing digestive enzymes"]),
    51: ("The diagram below shows a simplified anterior cross-section of the human heart with four labelled internal "
         "structures, P, Q, R and S. Structure P is a valve located between the left atrium and the left ventricle. "
         "Which valve is P? [Diagram: human heart cross-section, structures P/Q/R/S]",
         ["Tricuspid valve", "Bicuspid (mitral) valve", "Pulmonary semilunar valve", "Aortic semilunar valve"]),
    52: ("Antibodies are produced by which type of cell?",
         ["T-lymphocytes", "B-lymphocytes (plasma cells)", "Macrophages", "Neutrophils"]),
    53: ("Immunity acquired by injecting a weakened form of a pathogen is called:",
         ["Natural passive immunity", "Artificial active immunity", "Natural active immunity", "Artificial passive immunity"]),
    54: ("Gas exchange in the human lungs occurs across the walls of the:",
         ["Bronchi", "Trachea", "Alveoli", "Bronchioles"]),
    55: ("Oxygen moves from the alveoli into the blood mainly by the process of:",
         ["Active transport", "Diffusion down a concentration gradient", "Osmosis", "Facilitated transport requiring ATP"]),
    56: ("Most carbon dioxide is transported in the blood in the form of:",
         ["Dissolved CO2 gas", "Carbaminohemoglobin", "Bicarbonate ions (HCO3-)", "Carbonic acid crystals"]),
    57: ("Chronic smoking damages the cilia lining the respiratory tract, which primarily impairs:",
         ["Gas exchange directly at the alveoli", "The clearing of mucus and trapped particles from the airway", "Blood clotting", "Heart valve function"]),
    58: ("Bile, which emulsifies fats, is produced by the:",
         ["Pancreas", "Liver", "Gallbladder", "Stomach"]),
    59: ("Protein digestion begins in the:",
         ["Mouth", "Stomach", "Duodenum", "Large intestine"]),
    60: ("Villi in the small intestine primarily function to:",
         ["Produce hydrochloric acid", "Increase surface area for absorption of nutrients", "Store undigested food", "Secrete bile"]),
    61: ("The functional and structural unit of the kidney is the:",
         ["Nephron", "Glomerulus", "Ureter", "Bowman's capsule"]),
    62: ("Glomerular filtration is driven mainly by:",
         ["Active transport of ions", "Hydrostatic (blood) pressure", "Osmotic pressure of plasma proteins", "Diffusion of glucose"]),
    63: ("Under normal conditions, glucose in the filtrate is almost completely reabsorbed in the:",
         ["Loop of Henle", "Distal convoluted tubule", "Proximal convoluted tubule", "Collecting duct"]),
    64: ("Kidney stones are most commonly formed from the crystallization of:",
         ["Uric acid only", "Calcium oxalate", "Sodium chloride", "Glucose"]),
    65: ("When body temperature rises above normal, sweating helps cool the body mainly through:",
         ["Conduction", "Evaporation of sweat, which absorbs heat", "Radiation from the skin surface only", "Convection currents in blood"]),
    66: ("The main nitrogenous waste product excreted by humans is:",
         ["Ammonia", "Urea", "Uric acid", "Creatine"]),
    67: ("Recombinant human insulin used to treat diabetes is commercially produced using genetically engineered:",
         ["Yeast cells only", "Escherichia coli bacteria", "Human liver cells", "Plant cells only"]),
    68: ("The enzyme used to cut DNA at specific sequences during genetic engineering is called a:",
         ["DNA ligase", "DNA polymerase", "Restriction endonuclease", "Reverse transcriptase"]),

    # ---------------- CHEMISTRY (69-122) ----------------
    69: ("How many moles are present in 88 g of CO2? (Molar mass of CO2 = 44 g/mol)",
         ["0.5", "1", "2", "4"]),
    70: ("In a reaction, the reactant that is completely consumed first and determines the amount of product formed is called the:",
         ["Excess reactant", "Limiting reactant", "Catalyst", "Product"]),
    71: ("If the theoretical yield of a reaction is 50 g and the actual yield obtained is 40 g, what is the percentage yield?",
         ["60%", "70%", "80%", "90%"]),
    72: ("Which quantum number describes the shape of an atomic orbital?",
         ["Principal quantum number (n)", "Azimuthal quantum number (l)", "Magnetic quantum number (ml)", "Spin quantum number (ms)"]),
    73: ("The electronic configuration of Na+ (atomic number 11) is the same as that of:",
         ["Ne", "Mg", "F", "Ar"]),
    74: ("The proton was discovered through experiments involving:",
         ["Cathode rays", "Canal rays (anode rays)", "Alpha particle scattering", "Photoelectric effect"]),
    75: ("The shape of an s-orbital is:",
         ["Dumbbell", "Spherical", "Cloverleaf", "Complex with four lobes"]),
    76: ("According to Boyle's Law, at constant temperature, the pressure of a fixed mass of gas is:",
         ["Directly proportional to volume", "Inversely proportional to volume", "Independent of volume", "Proportional to the square of volume"]),
    77: ("In the ideal gas equation PV = nRT, which assumption is NOT part of the kinetic molecular theory for an ideal gas?",
         ["Gas molecules have negligible volume", "Gas molecules have strong intermolecular forces", "Collisions between molecules are perfectly elastic", "Gas molecules are in continuous random motion"]),
    78: ("Absolute zero, the temperature at which the volume of an ideal gas theoretically becomes zero, corresponds to:",
         ["0 degrees C", "-100 degrees C", "-273 degrees C", "-373 degrees C"]),
    79: ("The unusually high boiling point of water compared to H2S is mainly due to:",
         ["Water's higher molar mass", "Hydrogen bonding between water molecules", "Water's larger molecular size", "Covalent bonding within the water molecule"]),
    80: ("Water shows anomalous behaviour by expanding when it freezes; a direct consequence of this is that:",
         ["Ice is denser than liquid water", "Ice floats on liquid water", "Ice sinks in liquid water", "Water has no surface tension"]),
    81: ("A crystal lattice is best described as:",
         ["A random arrangement of particles", "A regular, repeating three-dimensional arrangement of particles", "A gaseous arrangement of molecules", "An arrangement found only in metals"]),
    82: ("Ionic crystals generally have much higher melting points than molecular crystals because:",
         ["Ionic crystals are held together by strong electrostatic forces between ions", "Molecular crystals contain no electrons", "Ionic crystals are always coloured", "Molecular crystals are always liquids"]),
    83: ("According to Le Chatelier's Principle, if the pressure on a gaseous equilibrium system is increased, the equilibrium will shift towards the side with:",
         ["More moles of gas", "Fewer moles of gas", "No change, since pressure has no effect", "Equal moles of gas"]),
    84: ("A buffer solution resists changes in pH because it contains:",
         ["A strong acid and a strong base", "A weak acid (or base) and its conjugate salt", "Only pure water", "A strong electrolyte only"]),
    85: ("The Haber process is industrially used to manufacture:",
         ["Sulfuric acid", "Ammonia", "Nitric acid", "Sodium carbonate"]),
    86: ("A catalyst increases the rate of a reaction by:",
         ["Increasing the temperature of reactants", "Lowering the activation energy of the reaction", "Increasing the concentration of reactants", "Shifting the position of equilibrium"]),
    87: ("For a reaction that is first order overall, doubling the concentration of the single reactant will:",
         ["Leave the rate unchanged", "Double the rate", "Quadruple the rate", "Halve the rate"]),
    88: ("Increasing the temperature of a reaction generally increases the rate mainly because it:",
         ["Decreases activation energy", "Increases the fraction of molecules with energy greater than or equal to activation energy", "Decreases the concentration of reactants", "Increases the volume of the container"]),
    89: ("In an exothermic reaction, the enthalpy change (delta-H) is:",
         ["Positive", "Negative", "Zero", "Undefined"]),
    90: ("Hess's Law states that the total enthalpy change for a reaction is:",
         ["Dependent on the reaction pathway", "Independent of the reaction pathway, depending only on initial and final states", "Always zero", "Only valid for exothermic reactions"]),
    91: ("The First Law of Thermodynamics is a statement of the conservation of:",
         ["Mass", "Energy", "Momentum", "Entropy"]),
    92: ("In a redox reaction, the species that loses electrons is said to be:",
         ["Reduced", "Oxidized", "Neutralized", "Hydrolyzed"]),
    93: ("The Standard Hydrogen Electrode (SHE) is assigned a standard reduction potential of:",
         ["+1.00 V", "-1.00 V", "0.00 V", "+0.76 V"]),
    94: ("The carbon atom in methane (CH4) is:",
         ["sp hybridized", "sp2 hybridized", "sp3 hybridized", "Not hybridized"]),
    95: ("According to VSEPR theory, a molecule with four bonding pairs and no lone pairs around the central atom adopts a:",
         ["Linear shape", "Trigonal planar shape", "Tetrahedral shape", "Bent shape"]),
    96: ("A triple bond between two carbon atoms, as in an alkyne, consists of:",
         ["Three sigma bonds", "One sigma and two pi bonds", "Two sigma and one pi bond", "Three pi bonds"]),
    97: ("A molecule of carbon dioxide (CO2) has a net dipole moment of zero because:",
         ["It contains no polar bonds", "Its linear symmetric shape causes the individual bond dipoles to cancel", "Carbon and oxygen have identical electronegativities", "It has no lone pairs on oxygen"]),
    98: ("Moving across a period from left to right, atomic radius generally:",
         ["Increases", "Decreases", "Remains constant", "Increases then sharply decreases"]),
    99: ("Alkali metals (Group I) react vigorously with water to produce:",
         ["A metal oxide and hydrogen gas", "A metal hydroxide and hydrogen gas", "A metal hydride and oxygen gas", "A metal carbonate and water"]),
    100: ("Elements in which the last electron enters an f-subshell are classified as:",
          ["s-block elements", "p-block elements", "d-block (transition) elements", "f-block (inner transition) elements"]),
    101: ("Transition elements are characterized by atoms that have a partially filled:",
          ["s-subshell", "p-subshell", "d-subshell", "f-subshell"]),
    102: ("Transition metals commonly form coloured compounds mainly due to:",
          ["d-d electronic transitions", "s-orbital transitions", "Absence of unpaired electrons", "Their low melting points"]),
    103: ("The functional group -COOH characterizes which class of organic compounds?",
          ["Alcohols", "Aldehydes", "Carboxylic acids", "Ketones"]),
    104: ("Compounds having the same molecular formula but different structural arrangements are called:",
          ["Allotropes", "Isomers", "Isotopes", "Isobars"]),
    105: ("The IUPAC name of CH3-CH2-CH2-CH3 is:",
          ["Propane", "Butane", "Pentane", "Isobutane"]),
    106: ("Benzene is unusually stable compared to a hypothetical cyclohexatriene mainly because of:",
          ["Its high molecular weight", "Delocalization of pi electrons around the ring (resonance)", "Presence of only single bonds", "Its planar shape alone"]),
    107: ("Benzene typically undergoes electrophilic substitution reactions rather than addition reactions because substitution:",
          ["Destroys aromatic stability", "Preserves the stable aromatic ring system", "Requires no catalyst", "Only occurs with alkenes"]),
    108: ("Terminal alkynes (e.g., HC-triple-bond-CH) show acidic character because the hydrogen attached to the sp-hybridized carbon is:",
          ["Non-polar and unreactive", "Relatively acidic due to the high s-character of the sp orbital", "Basic in nature", "Attached to an sp3 carbon"]),
    109: ("The reaction of a primary alkyl halide with a strong nucleophile in a polar aprotic solvent typically proceeds via which mechanism?",
          ["SN1", "SN2", "E1", "E2"]),
    110: ("In an elimination reaction of an alkyl halide, the products formed are typically:",
          ["An alcohol and a halide ion", "An alkene and a hydrogen halide", "An alkane and water", "A carboxylic acid"]),
    111: ("Phenol is more acidic than a typical alcohol (e.g., ethanol) mainly because:",
          ["The phenoxide ion is stabilized by resonance with the aromatic ring", "Phenol has a higher molecular weight", "Alcohols contain no -OH group", "Phenol lacks hydrogen bonding"]),
    112: ("An alcohol in which the -OH bearing carbon is attached to three other carbon atoms is classified as:",
          ["Primary", "Secondary", "Tertiary", "Quaternary"]),
    113: ("The reaction of an alcohol with a carboxylic acid in the presence of an acid catalyst, forming an ester and water, is called:",
          ["Saponification", "Esterification", "Hydrolysis", "Oxidation"]),
    114: ("Which functional group is common to both aldehydes and ketones?",
          ["-OH", "-COOH", "Carbonyl group (C=O)", "-NH2"]),
    115: ("Reduction of an aldehyde with a suitable reducing agent (e.g., NaBH4) typically produces a:",
          ["Primary alcohol", "Secondary alcohol", "Carboxylic acid", "Ketone"]),
    116: ("Aldehydes and ketones readily undergo nucleophilic addition reactions mainly because the carbonyl carbon is:",
          ["Electron-rich", "Electrophilic (partially positive)", "Non-polar", "sp3 hybridized"]),
    117: ("Carboxylic acids are more acidic than alcohols mainly because the carboxylate anion formed after deprotonation is:",
          ["Stabilized by resonance delocalization of the negative charge", "Destabilized by resonance", "Not stable at all", "Positively charged"]),
    118: ("Reaction of a carboxylic acid with PCl5 or SOCl2 converts it into a/an:",
          ["Ester", "Acid (acyl) chloride", "Amide", "Anhydride"]),
    119: ("The specific three-dimensional folded shape of a protein, stabilized by interactions such as hydrogen bonds and disulfide bridges, is its:",
          ["Primary structure", "Secondary structure", "Tertiary structure", "Quaternary structure only"]),
    120: ("Enzymes are classified as biocatalysts because they are:",
          ["Inorganic catalysts", "Proteins that speed up biochemical reactions without being consumed", "Consumed completely during the reaction", "Only active outside living cells"]),
    121: ("Polyethylene, formed by the polymerization of ethene monomers, is an example of a/an:",
          ["Condensation polymer", "Addition polymer", "Natural polymer", "Copolymer only"]),
    122: ("Azo dyes, widely used in the textile industry, are characterized by the presence of which functional group?",
          ["-N=N- (azo) linkage", "-COOH group", "-OH group", "-CHO group"]),

    # ---------------- PHYSICS (123-176) ----------------
    123: ("The scalar (dot) product of two vectors A and B is given by A.B = AB cos(theta). If A and B are perpendicular to each other, A.B equals:",
          ["AB", "0", "-AB", "1"]),
    124: ("The vector (cross) product of two parallel vectors is:",
          ["Maximum", "Zero", "Equal to their dot product", "Undefined"]),
    125: ("Two forces of magnitude 3 N and 4 N act perpendicular to each other on a body. The magnitude of their resultant is:",
          ["1 N", "5 N", "7 N", "12 N"]),
    126: ("Newton's Second Law of Motion states that the net force acting on a body is:",
          ["Inversely proportional to its acceleration", "Directly proportional to the rate of change of its momentum", "Always equal to zero", "Independent of its mass"]),
    127: ("Newton's Third Law of Motion states that for every action there is:",
          ["An equal and opposite reaction on the same body", "An equal and opposite reaction on a different body", "A larger reaction on the same body", "No reaction at all"]),
    128: ("For a projectile launched with the same initial speed, the horizontal range at a launch angle of 30 degrees is the same as the range at a launch angle of:",
          ["45 degrees", "60 degrees", "75 degrees", "15 degrees"]),
    129: ("In an isolated system with no external forces, the total linear momentum of the system:",
          ["Continuously increases", "Continuously decreases", "Remains conserved (constant)", "Becomes zero"]),
    130: ("In a perfectly elastic collision between two bodies:",
          ["Only momentum is conserved", "Only kinetic energy is conserved", "Both momentum and kinetic energy are conserved", "Neither momentum nor kinetic energy is conserved"]),
    131: ("A body moving with uniform acceleration has a velocity-time graph that is a:",
          ["Straight horizontal line", "Straight line with non-zero slope", "Parabola", "Circle"]),
    132: ("According to the work-energy theorem, the net work done on a body equals:",
          ["Its change in momentum", "Its change in kinetic energy", "Its change in potential energy only", "Zero, always"]),
    133: ("Power is defined as the rate of doing:",
          ["Force", "Work", "Momentum", "Displacement"]),
    134: ("The gravitational potential energy of a body of mass 2 kg raised to a height of 5 m above the ground is (g = 10 m/s^2):",
          ["10 J", "50 J", "100 J", "200 J"]),
    135: ("The efficiency of a machine is defined as the ratio of:",
          ["Input energy to output energy", "Output (useful) energy to input energy, expressed as a percentage", "Force to displacement", "Work done to time taken"]),
    136: ("The relationship between linear velocity v and angular velocity omega for a particle moving in a circle of radius r is:",
          ["v = omega / r", "v = omega * r", "v = omega + r", "v = omega^2 * r"]),
    137: ("One complete revolution corresponds to an angular displacement of:",
          ["pi radians", "2 pi radians", "pi/2 radians", "4 pi radians"]),
    138: ("Bernoulli's equation is essentially a statement of the conservation of:",
          ["Mass", "Energy for a flowing incompressible fluid", "Momentum", "Charge"]),
    139: ("According to the equation of continuity, when a fluid flows through a pipe of varying cross-section, the product of area and velocity (Av) at any section is:",
          ["Always increasing", "Always decreasing", "Constant", "Zero"]),
    140: ("A small sphere falling through a viscous fluid reaches terminal velocity when:",
          ["Its acceleration is maximum", "The net force acting on it becomes zero", "It stops moving completely", "Its weight becomes zero"]),
    141: ("In a longitudinal wave, the particles of the medium vibrate:",
          ["Perpendicular to the direction of wave propagation", "Parallel to the direction of wave propagation", "In a circular path", "Not at all"]),
    142: ("A stationary (standing) wave is produced by the superposition of:",
          ["Two waves of different frequencies", "Two identical waves travelling in opposite directions", "A single travelling wave", "Two perpendicular waves of different amplitude"]),
    143: ("In a pipe closed at one end, the fundamental frequency of vibration corresponds to a wavelength that is how many times the length (L) of the pipe?",
          ["L/2", "L", "2L", "4L"]),
    144: ("In simple harmonic motion, the acceleration of the particle is always:",
          ["Constant", "Directed away from the mean position and proportional to displacement", "Directed towards the mean position and proportional to displacement", "Zero at all times"]),
    145: ("The speed of sound in air increases with an increase in:",
          ["Air pressure at constant temperature", "Air temperature", "Wavelength only", "Amplitude of the sound wave"]),
    146: ("The graph below shows the displacement-time curve of a particle executing simple harmonic motion. At the instant "
          "marked P, where the curve crosses the time axis moving downward, the particle's velocity is: "
          "[Diagram: displacement-time SHM graph with point P marked]",
          ["Zero and acceleration is maximum", "Maximum (in magnitude) and directed in the negative direction", "Maximum and directed in the positive direction", "Zero and acceleration is zero"]),
    147: ("The First Law of Thermodynamics can be written as delta-U = Q - W, where W is the work done:",
          ["On the system by the surroundings", "By the system on the surroundings", "By gravity on the system", "Only during isothermal processes"]),
    148: ("The heat required to raise the temperature of a unit mass of a substance by one degree is called its:",
          ["Latent heat", "Specific heat capacity", "Thermal conductivity", "Heat capacity of the container"]),
    149: ("Two bodies are said to be in thermal equilibrium when they have the same:",
          ["Mass", "Volume", "Temperature", "Pressure"]),
    150: ("For an ideal gas, the molar specific heat at constant pressure (Cp) is always ______ the molar specific heat at constant volume (Cv).",
          ["Equal to", "Greater than", "Less than", "Unrelated to"]),
    151: ("According to Coulomb's Law, the electrostatic force between two point charges is:",
          ["Directly proportional to the square of the distance between them", "Inversely proportional to the square of the distance between them", "Independent of distance", "Directly proportional to the distance between them"]),
    152: ("Electric field lines around an isolated positive point charge point:",
          ["Towards the charge", "Radially outward from the charge", "Tangentially around the charge", "In circles around the charge"]),
    153: ("The electric field near an infinite charged sheet is:",
          ["Directly proportional to the distance from the sheet", "Inversely proportional to the distance from the sheet", "Uniform, independent of distance from the sheet", "Zero everywhere"]),
    154: ("When a capacitor is being charged through a resistor, the charge on the capacitor:",
          ["Increases exponentially and approaches a maximum value", "Increases linearly forever", "Remains constant", "Decreases exponentially"]),
    155: ("Ohm's Law states that the current through a conductor is directly proportional to the potential difference across it, provided:",
          ["The resistance changes with current", "The temperature (and other physical conditions) remain constant", "The current is alternating", "The conductor is a semiconductor"]),
    156: ("For a metallic conductor, resistivity generally:",
          ["Decreases with increasing temperature", "Increases with increasing temperature", "Remains constant with temperature", "Is independent of temperature entirely"]),
    157: ("The terminal voltage of a battery with internal resistance, when supplying current, is _______ its EMF.",
          ["Equal to", "Always greater than", "Less than", "Always double"]),
    158: ("Maximum power is transferred from a source to a load when the load resistance is:",
          ["Zero", "Infinite", "Equal to the internal resistance of the source", "Twice the internal resistance of the source"]),
    159: ("The SI unit of magnetic flux density (magnetic field strength B) is the:",
          ["Weber", "Tesla", "Henry", "Farad"]),
    160: ("A charged particle moving parallel to a uniform magnetic field experiences a magnetic force that is:",
          ["Maximum", "Zero", "Equal to qvB", "Directed perpendicular to its velocity always"]),
    161: ("Magnetic flux through a surface is defined as the product of magnetic field strength and:",
          ["The perpendicular area through which the field lines pass", "The resistance of the surface", "The current flowing through it", "The distance from the source"]),
    162: ("Faraday's Law of electromagnetic induction states that the induced EMF in a circuit is proportional to:",
          ["The magnetic flux itself", "The rate of change of magnetic flux linkage", "The resistance of the circuit", "The area of the circuit only"]),
    163: ("Lenz's Law states that the direction of an induced current is such that it:",
          ["Aids the change that produced it", "Opposes the change in magnetic flux that produced it", "Has no definite direction", "Is always clockwise"]),
    164: ("A step-up transformer increases voltage while:",
          ["Increasing current proportionally as well", "Decreasing current in the same proportion (ideally)", "Keeping current unchanged", "Reversing the direction of current"]),
    165: ("In a purely capacitive AC circuit, the current:",
          ["Lags the voltage by 90 degrees", "Leads the voltage by 90 degrees", "Is in phase with the voltage", "Leads the voltage by 180 degrees"]),
    166: ("In a purely inductive AC circuit, the current:",
          ["Leads the voltage by 90 degrees", "Lags the voltage by 90 degrees", "Is in phase with the voltage", "Lags the voltage by 180 degrees"]),
    167: ("Arranging electromagnetic waves in order of increasing wavelength, which of the following is correct?",
          ["Gamma rays < X-rays < ultraviolet < visible light", "Visible light < ultraviolet < X-rays < gamma rays", "Radio waves < microwaves < infrared < visible light", "X-rays < gamma rays < ultraviolet < visible light"]),
    168: ("A PN junction diode conducts significant current when it is:",
          ["Reverse biased", "Forward biased with voltage exceeding the barrier potential", "Not connected to any source", "Cooled to absolute zero"]),
    169: ("A full-wave rectifier circuit converts alternating current into:",
          ["High-frequency AC", "Pulsating direct current", "Pure sinusoidal AC", "Zero current"]),
    170: ("In reverse bias, the depletion region of a PN junction diode:",
          ["Narrows and current increases sharply", "Widens and only a very small leakage current flows", "Disappears completely", "Has no effect on current flow"]),
    171: ("According to Planck's quantum theory, the energy of a photon is directly proportional to its:",
          ["Wavelength", "Frequency", "Amplitude", "Speed"]),
    172: ("In the photoelectric effect, increasing the intensity of incident light (at constant frequency above threshold) increases:",
          ["The maximum kinetic energy of emitted electrons", "The number of photoelectrons emitted per second", "The threshold frequency", "The work function of the metal"]),
    173: ("The line spectrum of hydrogen consists of discrete bright lines because electrons:",
          ["Move continuously between all energy levels", "Emit photons of specific energies when transitioning between discrete energy levels", "Are not present in the atom", "Absorb all wavelengths equally"]),
    174: ("The Balmer series in the hydrogen spectrum corresponds to electron transitions ending at energy level:",
          ["n = 1", "n = 2", "n = 3", "n = 4"]),
    175: ("The half-life of a radioactive substance is the time taken for:",
          ["All the radioactive nuclei to decay", "Half of the radioactive nuclei present to decay", "The substance to double in mass", "The substance to become stable permanently in one step"]),
    176: ("Cobalt-60, a gamma-emitting radioisotope, is commonly used in medicine for:",
          ["Blood grouping", "Radiotherapy to treat cancer", "Measuring blood pressure", "Bone setting"]),

    # ---------------- ENGLISH (177-194) ----------------
    177: ("Read the sentence: \"The detective's astute observations led him to solve the case within hours.\" The word 'astute' most nearly means:",
          ["Careless", "Shrewd / perceptive", "Slow", "Random"]),
    178: ("\"The stars danced in the night sky\" is an example of:",
          ["Simile", "Metaphor", "Personification", "Alliteration"]),
    179: ("\"Her smile was as bright as the sun\" is an example of:",
          ["Metaphor", "Simile", "Hyperbole", "Personification"]),
    180: ("Choose the word closest in meaning to 'ephemeral':",
          ["Permanent", "Short-lived", "Massive", "Bright"]),
    181: ("Passage-based comprehension questions primarily test a reader's ability to:",
          ["Memorize the passage word for word", "Locate and interpret specific information within a text", "Ignore the main idea", "Translate the passage"]),
    182: ("Identify the figure of speech in: \"The whole village came out to help\" (when only some villagers actually came):",
          ["Metaphor", "Hyperbole", "Irony", "Synecdoche"]),
    183: ("Choose the correct sentence:",
          ["She has went to the market.", "She has gone to the market.", "She have gone to the market.", "She has goes to the market."]),
    184: ("Choose the correct sentence:",
          ["Each of the students must submit their assignment.", "Each of the students must submit his or her assignment.", "Each of the students must submit they assignment.", "Each of the students must submit our assignment."]),
    185: ("Change into passive voice: \"The teacher explains the lesson.\"",
          ["The lesson is explained by the teacher.", "The lesson was explained by the teacher.", "The lesson explains the teacher.", "The lesson has been explained by teacher."]),
    186: ("Convert to indirect speech: He said, \"I am going to school.\"",
          ["He said that I am going to school.", "He said that he was going to school.", "He said that he is going to school.", "He said that he will go to school."]),
    187: ("Fill in the blank: \"She is good ___ mathematics.\"",
          ["in", "at", "on", "for"]),
    188: ("Identify the gerund in the sentence: \"Swimming is her favourite hobby.\"",
          ["Her", "Favourite", "Swimming", "Hobby"]),
    189: ("Choose the sentence with a correctly used infinitive:",
          ["He wants going home.", "He wants to go home.", "He wants go home.", "He wants went home."]),
    190: ("Choose the word closest in meaning to 'benevolent':",
          ["Cruel", "Kind and generous", "Angry", "Selfish"]),
    191: ("Choose the grammatically correct sentence:",
          ["The group of students are going on a trip.", "The group of students is going on a trip.", "The group of students were going on a trip.", "The group of students go on a trip."]),
    192: ("Identify the sentence that is grammatically correct:",
          ["Being a rainy day, we stayed inside.", "Being a rainy day, the picnic was cancelled.", "Since it was a rainy day, we stayed inside.", "Rainy being the day, we stayed inside."]),
    193: ("Identify the error in the sentence: \"Neither of the answers are correct.\"",
          ["'Neither' should be 'Either'", "'are' should be 'is'", "'answers' should be 'answer'", "No error"]),
    194: ("Choose the correctly spelled word:",
          ["Recieve", "Receive", "Receeve", "Receve"]),

    # ---------------- LOGICAL REASONING (195-200) ----------------
    195: ("Statement: \"All doctors are educated. Ali is a doctor.\" Which conclusion logically follows?",
          ["Ali is educated", "Ali is not educated", "All educated people are doctors", "No conclusion can be drawn"]),
    196: ("Find the next term in the series: 2, 4, 8, 16, ___",
          ["20", "24", "32", "30"]),
    197: ("If all Roses are Flowers, and some Flowers fade quickly, which of the following must be true?",
          ["All Roses fade quickly", "Some Roses fade quickly", "No valid conclusion can be drawn from the given statements", "All Flowers are Roses"]),
    198: ("In a certain code, 'CAT' is written as 'DBU'. How would 'DOG' be written in the same code?",
          ["EPH", "EPI", "DPH", "EOH"]),
    199: ("Problem: A school's students are consistently arriving late due to a broken bus schedule. Which is the most appropriate course of action?",
          ["Suspend all late students immediately", "Coordinate with the transport department to fix the bus schedule", "Ignore the issue as it will resolve itself", "Cancel the school bus service entirely"]),
    200: ("Effect: \"The plants in the garden wilted within a week.\" Which is the most probable cause?",
          ["The plants were watered regularly", "The plants received no water for an extended period", "The plants were given fertilizer", "The gardener trimmed the leaves"]),
}

# Answer key. Letters correspond to option position in QUESTIONS (a=1st, b=2nd, c=3rd, d=4th).
KEY_RAW = """
1 b
2 a
3 b
4 a
5 c
6 b
7 c
8 c
9 b
10 c
11 b
12 a
13 c
14 b
15 a
16 b
17 b
18 b
19 a
20 b
21 b
22 b
23 b
24 b
25 b
26 b
27 a
28 b
29 b
30 b
31 b
32 b
33 b
34 c
35 a
36 b
37 a
38 b
39 b
40 b
41 a
42 c
43 b
44 a
45 c
46 d
47 b
48 c
49 b
50 b
51 b
52 b
53 b
54 c
55 b
56 c
57 b
58 b
59 b
60 b
61 a
62 b
63 c
64 b
65 b
66 b
67 b
68 c
69 c
70 b
71 c
72 b
73 a
74 b
75 b
76 b
77 b
78 c
79 b
80 b
81 b
82 a
83 b
84 b
85 b
86 b
87 b
88 b
89 b
90 b
91 b
92 b
93 c
94 c
95 c
96 b
97 b
98 b
99 b
100 d
101 c
102 a
103 c
104 b
105 b
106 b
107 b
108 b
109 b
110 b
111 a
112 c
113 b
114 c
115 a
116 b
117 a
118 b
119 c
120 b
121 b
122 a
123 b
124 b
125 b
126 b
127 b
128 b
129 c
130 c
131 b
132 b
133 b
134 c
135 b
136 b
137 b
138 b
139 c
140 b
141 b
142 b
143 d
144 c
145 b
146 b
147 b
148 b
149 c
150 b
151 b
152 b
153 c
154 a
155 b
156 b
157 c
158 c
159 b
160 b
161 a
162 b
163 b
164 b
165 b
166 b
167 a
168 b
169 b
170 b
171 b
172 b
173 b
174 b
175 b
176 b
177 b
178 c
179 b
180 b
181 b
182 b
183 b
184 b
185 a
186 b
187 b
188 c
189 b
190 b
191 b
192 c
193 b
194 b
195 a
196 c
197 c
198 a
199 b
200 b
"""

# ---------------------------------------------------------------------------
# TOPIC_TAGS: question number -> (topic, subtopic, difficulty)
# Topic/subtopic strings are copied VERBATIM from
# mdcat-content/syllabus/pmdc_mdcat_syllabus.json (including its doubled-
# apostrophe artifacts, e.g. "Boyle''s Law") so that Topic/Subtopic rows this
# import creates line up exactly with the ones already created by
# scripts/tag_topics.py for the 2012-2025 past papers, instead of forking
# near-duplicate rows in the DB.
# ---------------------------------------------------------------------------
TOPIC_TAGS = {
    1: ("Acellular Life", "Viruses", "easy"),
    2: ("Acellular Life", "Viruses", "easy"),
    3: ("Acellular Life", "AIDS and HIV Infection", "medium"),
    4: ("Acellular Life", "AIDS and HIV Infection", "medium"),
    5: ("Bioenergetics", "Respiration", "medium"),
    6: ("Bioenergetics", "Respiration", "easy"),
    7: ("Bioenergetics", "Respiration", "medium"),
    8: ("Biological Molecules", "Biological Molecules (Definition and Classification)", "easy"),
    9: ("Biological Molecules", "Biological Importance of Water", "medium"),
    10: ("Biological Molecules", "Carbohydrates", "easy"),
    11: ("Biological Molecules", "Proteins", "easy"),
    12: ("Biological Molecules", "Lipids", "easy"),
    13: ("Biological Molecules", "Structure of DNA", "easy"),
    14: ("Cell Structure and Function", "Prokaryotic and Eukaryotic Cell", "easy"),
    15: ("Cell Structure and Function", "Cytoplasmic Organelles", "medium"),
    16: ("Cell Structure and Function", "Cytoplasmic Organelles", "easy"),
    17: ("Cell Structure and Function", "Chromosomes", "easy"),
    18: ("Cell Structure and Function", "Cell Structure (Animal vs Plant)", "easy"),
    19: ("Coordination and Control", "Neurons", "easy"),
    20: ("Coordination and Control", "Nerve Impulse and Reflexes", "easy"),
    21: ("Coordination and Control", "Receptors", "easy"),
    22: ("Coordination and Control", "Brain", "medium"),
    23: ("Coordination and Control", "Brain", "medium"),
    24: ("Enzymes", "Characteristics of Enzymes", "medium"),
    25: ("Enzymes", "Mode of Enzyme Action", "medium"),
    26: ("Enzymes", "Factors Affecting Enzyme Action", "easy"),
    27: ("Enzymes", "Enzyme Inhibitors", "medium"),
    28: ("Evolution", "Darwinism", "easy"),
    29: ("Evolution", "Lamarckism", "easy"),
    30: ("Evolution", "Concept of Evolution", "medium"),
    31: ("Reproduction", "Human Reproductive System", "easy"),
    32: ("Reproduction", "Menstrual Cycle", "medium"),
    33: ("Reproduction", "Menstrual Cycle", "medium"),
    34: ("Reproduction", "Sexually Transmitted Diseases", "medium"),
    35: ("Support and Movement", "Human Skeleton (Cartilage, Muscle, Bone)", "easy"),
    36: ("Support and Movement", "Muscles (Smooth, Cardiac, Skeletal)", "medium"),
    37: ("Support and Movement", "Skeletal Muscle Ultra-structure", "medium"),
    38: ("Support and Movement", "Muscle Contraction", "medium"),
    39: ("Support and Movement", "Joints", "easy"),
    40: ("Support and Movement", "Arthritis", "medium"),
    41: ("Inheritance", "Mendel's Laws of Inheritance", "easy"),
    42: ("Inheritance", "Mendel's Laws of Inheritance", "easy"),
    43: ("Inheritance", "Gene Linkage and Crossing Over", "medium"),
    44: ("Inheritance", "X-linked Recessive Inheritance", "medium"),
    45: ("Inheritance", "X-linked Recessive Inheritance", "easy"),
    46: ("Circulation", "Human Heart", "easy"),
    47: ("Circulation", "Cardiac Cycle and Phases of Heartbeat", "easy"),
    48: ("Circulation", "Blood Vessels (Arteries, Veins, Capillaries)", "easy"),
    49: ("Circulation", "Blood Vessels (Arteries, Veins, Capillaries)", "medium"),
    50: ("Circulation", "Lymphatic System", "medium"),
    51: ("Circulation", "Human Heart", "medium"),
    52: ("Immunity", "Specific Defense Mechanism", "easy"),
    53: ("Immunity", "Specific Defense Mechanism", "medium"),
    54: ("Respiration", "Human Respiratory System", "easy"),
    55: ("Respiration", "Gas Exchange in Lungs", "easy"),
    56: ("Respiration", "Gas Exchange in Lungs", "medium"),
    57: ("Respiration", "Effect of Smoking", "medium"),
    58: ("Digestion", "Human Digestive System", "easy"),
    59: ("Digestion", "Human Digestive System", "medium"),
    60: ("Digestion", "Human Digestive System", "easy"),
    61: ("Homeostasis", "Kidney Structure and Function", "easy"),
    62: ("Homeostasis", "Glomerular Filtration and Reabsorption", "medium"),
    63: ("Homeostasis", "Glomerular Filtration and Reabsorption", "medium"),
    64: ("Homeostasis", "Kidney Stones and Failure", "medium"),
    65: ("Homeostasis", "Thermoregulation", "easy"),
    66: ("Homeostasis", "Excretion (Nitrogenous Compounds)", "easy"),
    67: ("Biotechnology", "Biotechnology and Health Care", "medium"),
    68: ("Biotechnology", "Biotechnology and Health Care", "medium"),

    69: ("Fundamental Concepts of Chemistry", "Moles and Avogadro''s Number", "easy"),
    70: ("Fundamental Concepts of Chemistry", "Limiting and Excess Reactants", "easy"),
    71: ("Fundamental Concepts of Chemistry", "Yield (Theoretical, Actual, Percentage)", "easy"),
    72: ("Atomic Structure", "Quantum Numbers", "medium"),
    73: ("Atomic Structure", "Electronic Configuration", "medium"),
    74: ("Atomic Structure", "Discovery of Proton", "medium"),
    75: ("Atomic Structure", "Shapes of Orbitals", "easy"),
    76: ("Gases", "Boyle''s Law", "easy"),
    77: ("Gases", "Ideal Gas Equation", "medium"),
    78: ("Gases", "Absolute Zero", "easy"),
    79: ("Liquids", "Hydrogen Bonding", "easy"),
    80: ("Liquids", "Anomalous Behavior of Water", "medium"),
    81: ("Solids", "Crystal Lattice", "easy"),
    82: ("Solids", "Ionic vs Molecular Crystals", "easy"),
    83: ("Chemical Equilibrium", "Le Chatelier''s Principle", "medium"),
    84: ("Chemical Equilibrium", "Buffer Solutions", "medium"),
    85: ("Chemical Equilibrium", "Haber''s Process", "easy"),
    86: ("Reaction Kinetics", "Activation Energy and Activated Complex", "easy"),
    87: ("Reaction Kinetics", "Order of Reaction", "medium"),
    88: ("Reaction Kinetics", "Factors Affecting Rate of Reaction", "medium"),
    89: ("Thermochemistry and Energetics", "Exothermic and Endothermic Reactions", "easy"),
    90: ("Thermochemistry and Energetics", "Hess''s Law", "medium"),
    91: ("Thermochemistry and Energetics", "First Law of Thermodynamics", "easy"),
    92: ("Electrochemistry", "Oxidation and Reduction", "easy"),
    93: ("Electrochemistry", "Standard Hydrogen Electrode (SHE)", "medium"),
    94: ("Chemical Bonding", "Hybridization", "easy"),
    95: ("Chemical Bonding", "VSEPR Theory", "easy"),
    96: ("Chemical Bonding", "Sigma and Pi Bonds", "medium"),
    97: ("Chemical Bonding", "Dipole Moment", "medium"),
    98: ("s and p Block Elements", "Periodic Trends (Radii, IE, EA, Electronegativity)", "easy"),
    99: ("s and p Block Elements", "Group I Reactions", "medium"),
    100: ("s and p Block Elements", "s, p, d, f Block Demarcation", "medium"),
    101: ("Transition Elements", "Electronic Structure of d-block", "easy"),
    102: ("Transition Elements", "Electronic Structure of d-block", "medium"),
    103: ("Fundamental Principles of Organic Chemistry", "Functional Groups", "easy"),
    104: ("Fundamental Principles of Organic Chemistry", "Isomerism (Stereoisomerism)", "easy"),
    105: ("Chemistry of Hydrocarbons", "Nomenclature of Alkanes", "easy"),
    106: ("Chemistry of Hydrocarbons", "MOT of Benzene, Resonance, Resonance Energy", "medium"),
    107: ("Chemistry of Hydrocarbons", "Reactivity of Benzene", "medium"),
    108: ("Chemistry of Hydrocarbons", "Acidity of Alkynes", "hard"),
    109: ("Alkyl Halides", "Nucleophilic Substitution Mechanisms", "medium"),
    110: ("Alkyl Halides", "Elimination Mechanisms", "medium"),
    111: ("Alcohols and Phenols", "Alcohol vs Phenol", "medium"),
    112: ("Alcohols and Phenols", "Nomenclature, Structure, Reactivity of Alcohols", "easy"),
    113: ("Alcohols and Phenols", "Chemistry of Alcohols (Ethers, Esters)", "easy"),
    114: ("Aldehydes and Ketones", "Nomenclature and Structure", "easy"),
    115: ("Aldehydes and Ketones", "Reduction to Alcohols", "medium"),
    116: ("Aldehydes and Ketones", "Nucleophilic Addition Reactions", "medium"),
    117: ("Carboxylic Acids", "Reactivity of Carboxylic Acids", "medium"),
    118: ("Carboxylic Acids", "Conversion to Derivatives (Acyl Halides, Anhydrides, Esters)", "medium"),
    119: ("Macromolecules", "Classification and Structure of Proteins", "medium"),
    120: ("Macromolecules", "Enzymes as Biocatalysts", "easy"),
    121: ("Industrial Chemistry", "Polymers (Condensation and Addition)", "medium"),
    122: ("Industrial Chemistry", "Dyes", "medium"),

    123: ("Vectors and Equilibrium", "Scalar Product of Vectors", "easy"),
    124: ("Vectors and Equilibrium", "Vector Product of Vectors", "medium"),
    125: ("Vectors and Equilibrium", "Addition of Vectors (Rectangular Components)", "easy"),
    126: ("Force and Motion", "Newton''s Second Law and Linear Momentum", "easy"),
    127: ("Force and Motion", "Newton''s Third Law and Conservation of Momentum", "easy"),
    128: ("Force and Motion", "Projectile Height, Range, Time of Flight", "medium"),
    129: ("Force and Motion", "Newton''s Third Law and Conservation of Momentum", "easy"),
    130: ("Force and Motion", "Perfectly Elastic Collision", "medium"),
    131: ("Force and Motion", "Uniform and Variable Acceleration", "easy"),
    132: ("Work and Energy", "Work-Energy Theorem in Resistive Medium", "easy"),
    133: ("Work and Energy", "Power", "easy"),
    134: ("Work and Energy", "Potential Energy", "easy"),
    135: ("Work and Energy", "Energy Losses and Efficiency", "easy"),
    136: ("Rotational and Circular Motion", "Relation Between Angular and Linear Quantities", "easy"),
    137: ("Rotational and Circular Motion", "Angular Displacement", "easy"),
    138: ("Fluid Dynamics", "Bernoulli''s Equation", "medium"),
    139: ("Fluid Dynamics", "Equation of Continuity", "medium"),
    140: ("Fluid Dynamics", "Terminal Velocity", "medium"),
    141: ("Waves", "Transverse vs Longitudinal Waves", "easy"),
    142: ("Waves", "Stationary Waves", "medium"),
    143: ("Waves", "Organ Pipes", "hard"),
    144: ("Waves", "Simple Harmonic Motion (SHM)", "medium"),
    145: ("Waves", "Factors Affecting Speed of Sound", "medium"),
    146: ("Waves", "Circular Motion and SHM", "medium"),
    147: ("Thermodynamics", "First Law of Thermodynamics", "medium"),
    148: ("Thermodynamics", "Specific and Molar Specific Heat", "easy"),
    149: ("Thermodynamics", "Thermal Equilibrium and Heat", "easy"),
    150: ("Thermodynamics", "Cp minus Cv Relation for Ideal Gas", "medium"),
    151: ("Electrostatics", "Coulomb''s Law", "easy"),
    152: ("Electrostatics", "Electric Field", "easy"),
    153: ("Electrostatics", "Electric Field Due to Infinite Sheet", "medium"),
    154: ("Electrostatics", "Charging and Discharging of Capacitor", "medium"),
    155: ("Current Electricity", "Ohm''s Law", "easy"),
    156: ("Current Electricity", "Resistivity and Temperature Coefficient", "medium"),
    157: ("Current Electricity", "Internal Resistance of Sources", "medium"),
    158: ("Current Electricity", "Maximum Power Transfer", "medium"),
    159: ("Electromagnetism", "Magnetic Flux Density", "easy"),
    160: ("Electromagnetism", "Motion of Charged Particle in Magnetic Field", "medium"),
    161: ("Electromagnetism", "Magnetic Flux", "medium"),
    162: ("Electromagnetic Induction", "Faraday''s Law", "easy"),
    163: ("Electromagnetic Induction", "Lenz''s Law", "medium"),
    164: ("Electromagnetic Induction", "Transformer", "medium"),
    165: ("Alternating Current", "AC Through Capacitor", "medium"),
    166: ("Alternating Current", "AC Through Inductor", "medium"),
    167: ("Alternating Current", "Electromagnetic Spectrum", "hard"),
    168: ("Electronics", "PN Junction (Forward and Reverse Bias)", "easy"),
    169: ("Electronics", "Rectification (Half and Full Wave)", "medium"),
    170: ("Electronics", "PN Junction (Forward and Reverse Bias)", "medium"),
    171: ("Dawn of Modern Physics", "Quantum Theory and Radiation (Photons)", "easy"),
    172: ("Dawn of Modern Physics", "Quantum Theory and Radiation (Photons)", "medium"),
    173: ("Atomic Spectra", "Atomic Spectra / Line Spectrum", "medium"),
    174: ("Atomic Spectra", "Atomic Spectra / Line Spectrum", "medium"),
    175: ("Nuclear Physics", "Half-life and Rate of Decay", "easy"),
    176: ("Nuclear Physics", "Biological and Medical Uses of Radiation", "medium"),

    177: ("Reading and Thinking Skills", "Deduce Meaning from Context", "easy"),
    178: ("Reading and Thinking Skills", "Figurative Language Analysis", "easy"),
    179: ("Reading and Thinking Skills", "Figurative Language Analysis", "easy"),
    180: ("Reading and Thinking Skills", "Deduce Meaning from Context", "medium"),
    181: ("Reading and Thinking Skills", "Scan to Answer Short Questions", "easy"),
    182: ("Reading and Thinking Skills", "Figurative Language Analysis", "medium"),
    183: ("Formal and Lexical Aspect of Language", "Tenses", "easy"),
    184: ("Formal and Lexical Aspect of Language", "Pronoun-Antecedent Agreement", "medium"),
    185: ("Formal and Lexical Aspect of Language", "Active and Passive Voice", "easy"),
    186: ("Formal and Lexical Aspect of Language", "Direct and Indirect Speech", "medium"),
    187: ("Formal and Lexical Aspect of Language", "Prepositions", "easy"),
    188: ("Formal and Lexical Aspect of Language", "Gerunds and Gerund Phrases", "easy"),
    189: ("Formal and Lexical Aspect of Language", "Infinitives and Infinitive Phrases", "easy"),
    190: ("Formal and Lexical Aspect of Language", "Synonyms (Irony, Parody, Satire)", "easy"),
    191: ("Writing Skills", "Subject-Verb Agreement", "medium"),
    192: ("Writing Skills", "Faulty Sentence Structure", "medium"),
    193: ("Writing Skills", "Proofreading and Editing", "medium"),
    194: ("Writing Skills", "Errors of Function and Spelling", "easy"),

    195: ("Critical Thinking", "Evaluating Truth vs Falsehood", "easy"),
    196: ("Letter and Symbol Series", "Geometric Number Series", "easy"),
    197: ("Logical Deductions", "Predicting New Relations", "medium"),
    198: ("Logical Problems", "Puzzle Solving", "medium"),
    199: ("Course of Action", "Judging Courses via Arguments", "easy"),
    200: ("Cause and Effect", "Reasoning About Events and Accidents", "easy"),
}
