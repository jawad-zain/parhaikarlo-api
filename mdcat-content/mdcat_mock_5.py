# -*- coding: utf-8 -*-
"""
Builder for MDCAT Mock Test 5.
Raw question data (question, correct answer, 3 distractors) is defined below;
this script assigns option letters in a shuffled, balanced rotation so correct
answers are evenly spread across A/B/C/D, then writes the final mock5.py file
in the same format as Mock 1-4.
"""
import json
import random

RAW = []

def add(id_, subject, topic, difficulty, question, correct, distractors, image=None):
    RAW.append({
        "id": id_, "subject": subject, "topic": topic, "difficulty": difficulty,
        "question": question, "correct": correct, "distractors": distractors, "image": image
    })

# ============================================================
# BIOLOGY (81) - id 1-81
# ============================================================
add(1,'Biology','Biomolecules','Easy',
    'Lipids are primarily composed of which two types of building blocks?',
    'Glycerol and fatty acids', ['Amino acids and sugars', 'Nucleotides and phosphates', 'Monosaccharides only'])
add(2,'Biology','Biomolecules','Easy',
    'Which of the following is a disaccharide?',
    'Maltose', ['Glucose', 'Cellulose', 'Glycogen'])
add(3,'Biology','Biomolecules','Medium',
    'The tertiary structure of a globular protein refers to:',
    'The overall three-dimensional folding of a single polypeptide chain, stabilized by interactions among side chains',
    ['The linear sequence of amino acids', 'The association of two or more polypeptide chains', 'Only the alpha-helical regions'])
add(4,'Biology','Biomolecules','Medium',
    'Which bond type is broken when a triglyceride undergoes hydrolysis into glycerol and fatty acids?',
    'Ester bond', ['Peptide bond', 'Glycosidic bond', 'Hydrogen bond'])
add(5,'Biology','Biomolecules','Hard',
    "Denaturation of a protein primarily disrupts its:",
    'Secondary, tertiary, and quaternary structure, while the amino acid sequence remains intact',
    ['Primary structure (amino acid sequence)', 'Only the peptide bonds between amino acids', 'Nothing; denatured proteins are structurally identical to native ones'])

add(6,'Biology','Enzymes','Easy',
    'The molecule upon which an enzyme acts is called the:',
    'Substrate', ['Coenzyme', 'Product', 'Cofactor'])
add(7,'Biology','Enzymes','Medium',
    'A non-competitive inhibitor reduces enzyme activity by:',
    "Binding at a site other than the active site, changing the enzyme's shape and reducing its efficiency",
    ['Binding at the active site, directly blocking the substrate', 'Increasing the rate of the reaction', 'Being converted into product'])
add(8,'Biology','Enzymes','Medium',
    'The graph shows the initial reaction rate of an enzyme-catalyzed reaction plotted against increasing substrate concentration, with the rate leveling off at high substrate levels. This plateau is best explained by:',
    'All available active sites becoming saturated with substrate',
    ['The enzyme being denatured at high substrate levels', 'The substrate running out', 'The reaction reversing direction'],
    image='images/q5_enzyme_substrate_saturation_graph.png')
add(9,'Biology','Enzymes','Hard',
    'Allosteric enzymes are regulated mainly through:',
    'Binding of regulatory molecules at a site distinct from the active site, altering enzyme shape and activity',
    ['Direct competition at the active site only', 'Permanent covalent modification that cannot be reversed', 'Random changes in temperature alone'])

add(10,'Biology','Cell Biology','Easy',
    'Which structure controls the movement of substances into and out of the cell?',
    'Plasma membrane', ['Cell wall', 'Nucleolus', 'Cytoskeleton'])
add(11,'Biology','Cell Biology','Easy',
    'Peroxisomes within cells are primarily responsible for:',
    'Breaking down fatty acids and detoxifying harmful substances using oxidative reactions',
    ['Photosynthesis', 'Protein synthesis', 'Cell division'])
add(12,'Biology','Cell Biology','Medium',
    'Which of the following is found in both plant and animal cells?',
    'Mitochondrion', ['Chloroplast', 'Cell wall', 'Large central vacuole'])
add(13,'Biology','Cell Biology','Medium',
    'The endomembrane system includes all of the following EXCEPT:',
    'Mitochondria', ['Endoplasmic reticulum', 'Golgi apparatus', 'Plasma membrane'])
add(14,'Biology','Cell Biology','Medium',
    'The diagram shows a plant cell with structures labeled M, N, O, and P. Structure N is a large, fluid-filled sac that maintains turgor pressure and stores water, ions, and waste products. Which structure is N?',
    'Structure N (central vacuole)',
    ['Structure M (chloroplast)', 'Structure O (cell wall)', 'Structure P (nucleus)'],
    image='images/q5_plant_cell_diagram_mnop.png')
add(15,'Biology','Cell Biology','Medium',
    'Chromatin condenses into visible chromosomes mainly in preparation for:',
    'Cell division', ['Interphase', 'Protein synthesis', 'Apoptosis only'])
add(16,'Biology','Cell Biology','Hard',
    'A cell with a defective Golgi apparatus would most directly have difficulty with:',
    'Modifying, sorting, and packaging proteins for secretion',
    ['Replicating its DNA', 'Producing ATP', 'Breaking down glucose'])

add(17,'Biology','Cell Membrane & Transport','Easy',
    'Movement of molecules from an area of high concentration to an area of low concentration, without the use of energy, is called:',
    'Diffusion', ['Active transport', 'Endocytosis', 'Exocytosis'])
add(18,'Biology','Cell Membrane & Transport','Medium',
    'An animal cell placed in a hypotonic solution will most likely:',
    'Swell and potentially burst (lysis), since it lacks a rigid cell wall',
    ['Shrink due to water leaving the cell', 'Remain completely unchanged', 'Immediately divide'])
add(19,'Biology','Cell Membrane & Transport','Medium',
    'Endocytosis is the process by which a cell:',
    'Engulfs external material by folding the plasma membrane inward to form a vesicle',
    ['Releases materials by vesicle fusion with the membrane', 'Exchanges gases passively', 'Transports water only'])
add(20,'Biology','Cell Membrane & Transport','Hard',
    'Channel proteins differ from carrier proteins in facilitated diffusion in that channel proteins:',
    'Form a continuous pore through which specific molecules or ions pass without the protein changing shape',
    ['Require ATP to function', 'Always transport substances against their gradient', 'Are found only in the nuclear envelope'])
add(21,'Biology','Cell Membrane & Transport','Easy',
    'Cholesterol molecules embedded within the plasma membrane mainly function to:',
    'Regulate membrane fluidity, preventing it from becoming too rigid or too fluid',
    ['Transport ions across the membrane', 'Catalyze biochemical reactions', "Form the majority of the membrane's phospholipids"])

add(22,'Biology','Cell Cycle & Division','Easy',
    'Which phase of the cell cycle is generally the longest?',
    'Interphase', ['M phase', 'Cytokinesis alone', 'Prophase'])
add(23,'Biology','Cell Cycle & Division','Easy',
    'During which phase does the nuclear envelope reform around each set of separated chromosomes?',
    'Telophase', ['Prophase', 'Metaphase', 'Anaphase'])
add(24,'Biology','Cell Cycle & Division','Medium',
    'The main biological significance of mitosis is to:',
    'Generate genetically identical daughter cells for growth and repair',
    ['Produce gametes with half the chromosome number', 'Introduce genetic variation', 'Reduce chromosome number by half'])
add(25,'Biology','Cell Cycle & Division','Medium',
    'A cell with a diploid chromosome number of 8 undergoes meiosis. How many chromosomes will each resulting daughter cell (gamete) contain?',
    '4', ['8', '16', '2'])
add(26,'Biology','Cell Cycle & Division','Medium',
    'Independent assortment during meiosis I refers to:',
    'The random orientation of homologous chromosome pairs at the metaphase plate, contributing to genetic variation',
    ['The exchange of segments between sister chromatids', 'The identical separation of chromosomes every time', 'The doubling of DNA content'])
add(27,'Biology','Cell Cycle & Division','Hard',
    'Apoptosis (programmed cell death) differs from necrosis in that apoptosis:',
    'Is a controlled, energy-dependent process that eliminates cells without triggering inflammation',
    ['Is an uncontrolled, damaging process triggered by injury', 'Always results from external injury alone', 'Never occurs in normal development'])

add(28,'Biology','Genetics','Easy',
    'In pea plants, round seed shape (R) is dominant over wrinkled (r). A cross between a heterozygous round plant and a wrinkled plant (Rr x rr) produces offspring with genotype:',
    '1 Rr : 1 rr', ['All Rr', 'All RR', 'All rr'])
add(29,'Biology','Genetics','Medium',
    'A dihybrid cross between two individuals heterozygous for two independently assorting traits (AaBb x AaBb) is expected to give what overall phenotypic ratio?',
    '9:3:3:1', ['1:2:1', '3:1', '1:1:1:1'])
add(30,'Biology','Genetics','Medium',
    'Color blindness is an X-linked recessive condition. If an affected father and a homozygous unaffected mother have children, what proportion of their daughters is expected to be carriers?',
    '100%', ['0%', '50%', '25%'])
add(31,'Biology','Genetics','Hard',
    'In a test cross for a single gene, Aa x aa, what fraction of offspring is expected to show the recessive phenotype?',
    '1/2', ['1/4', '3/4', '1/8'])
add(32,'Biology','Genetics','Medium',
    'A man with blood group AB and a woman with blood group O have children. Which blood groups are possible among their offspring?',
    'A and B only', ['Only AB', 'A, B, AB, and O', 'Only O'])
add(33,'Biology','Genetics','Hard',
    'A pedigree in which an affected individual always has an affected parent, and the trait appears in every generation without skipping, is most consistent with:',
    'Autosomal dominant inheritance',
    ['Autosomal recessive inheritance', 'X-linked recessive inheritance', 'Mitochondrial-only inheritance'])
add(34,'Biology','Genetics','Medium',
    'In snapdragons, crossing a red-flowered plant (RR) with a white-flowered plant (WW) produces all pink-flowered offspring (RW). This pattern is an example of:',
    'Incomplete dominance', ['Codominance', 'Epistasis', 'Polygenic inheritance'])

add(35,'Biology','Molecular Biology','Easy',
    'The four nitrogenous bases found in DNA are adenine, thymine, guanine, and:',
    'Cytosine', ['Uracil', 'Ribose', 'Phosphate'])
add(36,'Biology','Molecular Biology','Easy',
    'The overall flow of genetic information described as DNA -> RNA -> protein is known as the:',
    'Central dogma of molecular biology', ['Genetic code', 'Operon model', 'Replication fork'])
add(37,'Biology','Molecular Biology','Medium',
    'Okazaki fragments are formed during DNA replication because:',
    "DNA polymerase can only synthesize in the 5' to 3' direction, requiring discontinuous synthesis on the lagging strand",
    ['RNA primers are never used', 'The leading strand is synthesized discontinuously', 'DNA ligase cannot join fragments'])
add(38,'Biology','Molecular Biology','Medium',
    'During translation, a stop codon on the mRNA causes:',
    'Release of the completed polypeptide from the ribosome, as no tRNA recognizes it',
    ['Addition of a stop amino acid', 'Immediate degradation of the mRNA', 'Reinitiation of transcription'])
add(39,'Biology','Molecular Biology','Medium',
    "A mutation that introduces a premature stop codon into a gene's coding sequence is called a:",
    'Nonsense mutation', ['Silent mutation', 'Missense mutation', 'Frameshift mutation only'])
add(40,'Biology','Molecular Biology','Hard',
    "A deletion of three consecutive nucleotides (one full codon) from a gene's coding sequence would most likely result in:",
    'Loss of a single amino acid from the protein, with the reading frame otherwise preserved',
    ['A frameshift affecting the entire downstream sequence', 'No change to the protein at all', 'Complete loss of protein synthesis'])
add(41,'Biology','Molecular Biology','Hard',
    'In the lac operon, the presence of lactose leads to transcription of the lac genes mainly because a lactose derivative:',
    'Binds to and inactivates the repressor protein, allowing it to release the operator',
    ['Binds directly to RNA polymerase, activating it', 'Destroys the operator sequence permanently', 'Binds to the promoter, blocking transcription'])
add(42,'Biology','Molecular Biology','Medium',
    'A codon consists of how many nucleotides, and codes for:',
    'Three nucleotides, coding for one amino acid',
    ['Two nucleotides, coding for one amino acid', 'Four nucleotides, coding for two amino acids', 'One nucleotide, coding for one amino acid'])
add(43,'Biology','Molecular Biology','Medium',
    'Alternative splicing of pre-mRNA allows a single gene to:',
    'Produce multiple different protein products by combining exons in different ways',
    ["Be transcribed only once in a cell's lifetime", 'Never be translated', 'Lose its introns permanently from the DNA'])
add(44,'Biology','Molecular Biology','Easy',
    'Which of the following enzymes joins Okazaki fragments together by forming phosphodiester bonds?',
    'DNA ligase', ['DNA polymerase', 'Helicase', 'Primase'])

add(45,'Biology','Evolution','Easy',
    "The term used to describe a heritable trait that increases an organism's chance of survival and reproduction in a given environment is:",
    'Adaptation', ['Mutation', 'Speciation', 'Extinction'])
add(46,'Biology','Evolution','Medium',
    'Analogous structures, such as the wings of insects and birds, are the result of:',
    'Convergent evolution, where similar traits evolve independently in unrelated lineages facing similar environmental pressures',
    ['Common ancestry', 'Identical genetic pathways', 'Direct inheritance from a shared recent ancestor'])
add(47,'Biology','Evolution','Medium',
    'Which of the following is NOT one of the conditions required for a population to remain in Hardy-Weinberg equilibrium?',
    'Ongoing natural selection favoring certain alleles',
    ['No natural selection', 'No mutation', 'Random mating'])
add(48,'Biology','Evolution','Hard',
    "In a population in Hardy-Weinberg equilibrium, 16% of individuals show the recessive phenotype. What is the frequency of the dominant allele (p)?",
    '0.6', ['0.4', '0.16', '0.84'])

add(49,'Biology','Classification & Diversity','Easy',
    'The scientific study of classifying and naming organisms is called:',
    'Taxonomy', ['Ecology', 'Physiology', 'Genetics'])
add(50,'Biology','Classification & Diversity','Easy',
    'Members of kingdom Animalia are generally characterized as:',
    'Multicellular heterotrophs that typically ingest food and lack cell walls',
    ['Autotrophic organisms with cell walls', 'Unicellular prokaryotes', 'Decomposers that absorb nutrients'])
add(51,'Biology','Classification & Diversity','Medium',
    'The three-domain system of classification (Bacteria, Archaea, Eukarya) is based primarily on differences in:',
    'Ribosomal RNA sequences and fundamental cell biology',
    ['Body size', 'Habitat alone', 'Ability to move'])
add(52,'Biology','Classification & Diversity','Medium',
    'A newly discovered unicellular organism has a membrane-bound nucleus but lacks chloroplasts and a cell wall, and moves using pseudopodia to engulf food particles. It most likely belongs to:',
    'Kingdom Protista', ['Kingdom Monera', 'Kingdom Fungi', 'Kingdom Plantae'])
add(53,'Biology','Classification & Diversity','Easy',
    'Which taxonomic rank groups together several related genera?',
    'Family', ['Species', 'Order', 'Class'])
add(54,'Biology','Classification & Diversity','Medium',
    'Members of phylum Chordata are united by the shared presence, at some point in development, of:',
    'A notochord, dorsal nerve cord, and pharyngeal slits',
    ['A hard exoskeleton', 'Radial symmetry', 'A closed circulatory system only'])

add(55,'Biology','Plant Biology','Easy',
    'The organ of a flowering plant primarily responsible for anchoring the plant and absorbing water and minerals is the:',
    'Root', ['Stem', 'Leaf', 'Flower'])
add(56,'Biology','Plant Biology','Medium',
    'The overall equation for photosynthesis shows that plants convert carbon dioxide and water into glucose and:',
    'Oxygen', ['Nitrogen', 'Carbon monoxide', 'Methane'])
add(57,'Biology','Plant Biology','Medium',
    'Chlorophyll a and chlorophyll b absorb light most strongly in the ______ and ______ regions of the visible spectrum, reflecting green light.',
    'Red; blue', ['Yellow; orange', 'Green; violet only', 'Infrared; ultraviolet'])
add(58,'Biology','Plant Biology','Hard',
    'In C3 plants under hot, dry conditions, stomata often close to conserve water, which can lead to reduced photosynthetic efficiency mainly because:',
    'CO2 levels drop and RuBisCO increasingly binds O2 instead, causing photorespiration',
    ['Glucose production stops entirely', 'Chlorophyll is destroyed', 'The Calvin cycle no longer requires CO2'])
add(59,'Biology','Plant Biology','Medium',
    'Guard cells surrounding each stomatal pore regulate gas exchange and water loss mainly by:',
    'Changing shape to open or close the pore in response to turgor pressure changes',
    ['Producing chlorophyll', 'Secreting wax onto the leaf surface', 'Absorbing sunlight directly'])
add(60,'Biology','Plant Biology','Easy',
    'The transfer of pollen from the anther to the stigma of a flower is called:',
    'Pollination', ['Fertilization', 'Germination', 'Transpiration'])

add(61,'Biology','Human Physiology - Digestion','Easy',
    'Emulsification of fats in the small intestine is carried out by:',
    'Bile', ['Pepsin', 'Amylase', 'Hydrochloric acid'])
add(62,'Biology','Human Physiology - Digestion','Medium',
    'Trypsin, a pancreatic enzyme, is secreted in an inactive form (trypsinogen) mainly to:',
    "Prevent the enzyme from digesting the pancreas's own proteins before reaching the intestine",
    ['Slow down digestion unnecessarily', 'Allow it to work only in the stomach', 'Increase its stability at low pH'])
add(63,'Biology','Human Physiology - Digestion','Medium',
    "The large intestine's primary functions include:",
    'Absorption of water and electrolytes from indigestible food matter',
    ['Chemical digestion of proteins', 'Production of bile', 'Initial digestion of starch'])
add(64,'Biology','Human Physiology - Digestion','Hard',
    'Efficient fat digestion in the small intestine depends on bile emulsifying fats, after which pancreatic lipase:',
    'Hydrolyzes triglycerides into fatty acids and monoglycerides for absorption',
    ['Converts fats directly into glucose', 'Stores fats permanently in micelles', 'Converts fats into amino acids'])

add(65,'Biology','Human Physiology - Circulation','Easy',
    'Blood leaving the left ventricle travels directly into the:',
    'Aorta', ['Pulmonary artery', 'Vena cava', 'Pulmonary vein'])
add(66,'Biology','Human Physiology - Circulation','Medium',
    'Which of the following best explains why the left ventricle has a much thicker muscular wall than the right ventricle?',
    'The left ventricle must generate enough pressure to pump blood throughout the entire systemic circulation',
    ['The left ventricle pumps blood only to the lungs, a low-pressure circuit', 'The left ventricle contains valves while the right does not', 'The left ventricle is smaller in volume'])
add(67,'Biology','Human Physiology - Circulation','Medium',
    'Blood pressure is typically measured as two values, systolic over diastolic; the diastolic value represents:',
    'Pressure in the arteries when the heart is relaxed between beats',
    ['Pressure during ventricular contraction', 'Pressure within the veins only', 'The total blood volume'])
add(68,'Biology','Human Physiology - Circulation','Hard',
    'An increase in blood carbon dioxide levels stimulates chemoreceptors, which typically leads to:',
    'Increased heart and respiratory rate to expel excess CO2',
    ['Decreased heart and respiratory rate', 'No physiological response', 'Immediate cardiac arrest'])

add(69,'Biology','Human Physiology - Respiration','Easy',
    'The muscles located between the ribs that assist in expanding the chest cavity during inhalation are the:',
    'Intercostal muscles', ['Diaphragm only', 'Abdominal muscles', 'Cardiac muscles'])
add(70,'Biology','Human Physiology - Respiration','Medium',
    'The concentration gradient that drives oxygen diffusion from the alveoli into the surrounding capillary blood exists because:',
    'Oxygen concentration is higher in the alveoli than in the deoxygenated blood arriving at the lungs',
    ['Oxygen concentration is lower in the alveoli than in the blood', 'There is no concentration gradient; oxygen moves by active transport', 'Carbon dioxide concentration is higher in the alveoli'])
add(71,'Biology','Human Physiology - Respiration','Medium',
    'The respiratory control center located in the medulla oblongata primarily regulates breathing rate based on:',
    'Blood carbon dioxide and pH levels',
    ['Blood glucose levels', 'Blood oxygen levels exclusively', 'Body temperature'])

add(72,'Biology','Human Physiology - Excretion','Easy',
    'The functional and structural unit of the kidney responsible for filtering blood is the:',
    'Nephron', ['Ureter', 'Renal pelvis', 'Bladder'])
add(73,'Biology','Human Physiology - Excretion','Medium',
    'Substances such as excess hydrogen ions and certain drugs are added to the filtrate from the surrounding blood in the nephron through the process of:',
    'Tubular secretion', ['Filtration', 'Reabsorption', 'Excretion'])
add(74,'Biology','Human Physiology - Excretion','Hard',
    'A person who is severely dehydrated would be expected to secrete ______ ADH, resulting in urine that is ______.',
    'More; more concentrated', ['Less; more dilute', 'More; more dilute', 'Less; more concentrated'])

add(75,'Biology','Human Physiology - Nervous & Endocrine','Easy',
    'The gap between the axon terminal of one neuron and the dendrite of the next, across which nerve signals are transmitted, is called the:',
    'Synapse', ['Node of Ranvier', 'Myelin sheath', 'Axon hillock'])
add(76,'Biology','Human Physiology - Nervous & Endocrine','Medium',
    'The myelin sheath surrounding many axons functions mainly to:',
    'Increase the speed of nerve impulse conduction by enabling saltatory conduction',
    ['Produce neurotransmitters', 'Absorb excess ions', 'Generate the resting potential'])
add(77,'Biology','Human Physiology - Nervous & Endocrine','Medium',
    'Thyroxine, secreted by the thyroid gland, primarily functions to:',
    "Regulate the body's basal metabolic rate",
    ['Regulate blood calcium levels', 'Trigger the fight-or-flight response', 'Regulate blood glucose directly'])
add(78,'Biology','Human Physiology - Nervous & Endocrine','Hard',
    'The resting membrane potential of a neuron is maintained largely by:',
    "The sodium-potassium pump and the membrane's greater permeability to K+ than Na+",
    ['Equal concentrations of Na+ and K+ on both sides of the membrane', 'Continuous depolarization', 'The complete absence of ion channels'])

add(79,'Biology','Human Physiology - Reproduction','Easy',
    'The hormone responsible for triggering ovulation via a surge in its levels is:',
    'Luteinizing hormone (LH)', ['Estrogen', 'Progesterone', 'FSH'])
add(80,'Biology','Human Physiology - Reproduction','Medium',
    'If fertilization does not occur, the corpus luteum degenerates, causing progesterone levels to fall, which leads to:',
    'Shedding of the uterine lining (menstruation)', ['Implantation', 'Ovulation', 'A surge in LH'])

add(81,'Biology','Ecology','Medium',
    'In a stable ecosystem, the pyramid of energy typically shows that the amount of energy available:',
    'Decreases at each successive trophic level, as energy is lost as heat at each transfer',
    ['Increases at each successive trophic level', 'Remains exactly constant at every trophic level', 'Is concentrated entirely at the top level'])

# ============================================================
# CHEMISTRY (45) - id 82-126
# ============================================================
add(82,'Chemistry','Atomic Structure','Easy',
    'Which subatomic particle carries a negative charge and orbits the nucleus?',
    'Electron', ['Proton', 'Neutron', 'Positron'])
add(83,'Chemistry','Atomic Structure','Medium',
    'An atom of oxygen-18 (atomic number 8) contains how many neutrons?',
    '10', ['8', '18', '26'])
add(84,'Chemistry','Atomic Structure','Medium',
    'The electron configuration of a neutral chlorine atom (Z = 17) is:',
    '1s2 2s2 2p6 3s2 3p5', ['1s2 2s2 2p6 3s2 3p6', '1s2 2s2 2p5', '1s2 2s2 2p6 3s1'])
add(85,'Chemistry','Atomic Structure','Hard',
    'An ion formed from a neutral atom with 8 protons that has gained 2 electrons carries a charge of:',
    '-2', ['+2', '-1', '+1'])
add(126,'Chemistry','Atomic Structure','Easy',
    'The atomic mass of an element listed on the periodic table represents:',
    'The weighted average mass of all naturally occurring isotopes of that element',
    ['The mass of a single proton', 'The number of neutrons only', 'The total number of electrons'])

add(86,'Chemistry','Periodic Table','Easy',
    'Elements in Group 17 of the periodic table, known for being highly reactive nonmetals, are called:',
    'Halogens', ['Alkali metals', 'Noble gases', 'Transition metals'])
add(87,'Chemistry','Periodic Table','Medium',
    'Ionization energy generally increases:',
    'Across a period from left to right, and up a group',
    ['Down a group, and from left to right across a period', 'Down a group only', 'Left to right, and down a group'])
add(88,'Chemistry','Periodic Table','Medium',
    'An element with electron configuration [Ne]3s2 would most likely:',
    'Lose two electrons to form a +2 ion',
    ['Gain two electrons to form a -2 ion', 'Be chemically inert', 'Form covalent bonds exclusively'])

add(89,'Chemistry','Chemical Bonding','Easy',
    'A metallic bond can best be described as:',
    "Positive metal ions held together by a 'sea' of delocalized electrons",
    ['A bond formed by complete electron transfer', 'A bond formed by sharing electron pairs equally', 'A weak intermolecular attraction only'])
add(90,'Chemistry','Chemical Bonding','Medium',
    'According to VSEPR theory, a molecule such as methane (CH4), with four bonding pairs and no lone pairs on the central atom, has a molecular shape described as:',
    'Tetrahedral', ['Trigonal pyramidal', 'Bent', 'Trigonal planar'])
add(91,'Chemistry','Chemical Bonding','Medium',
    'HCl is a polar molecule mainly because:',
    'Chlorine is more electronegative than hydrogen, creating an uneven distribution of electron density',
    ['Hydrogen and chlorine have very similar electronegativities', 'The molecule has a symmetrical shape', 'It contains no covalent bond'])
add(92,'Chemistry','Chemical Bonding','Hard',
    'Ice is less dense than liquid water mainly because:',
    'Hydrogen bonding in the solid state arranges water molecules into an open lattice structure',
    ['Water molecules pack more tightly as a solid', 'Ice contains fewer water molecules per unit volume through evaporation', 'Ice has stronger covalent bonds than liquid water'])
add(125,'Chemistry','Chemical Bonding','Easy',
    'A single covalent bond between two atoms involves the sharing of:',
    'One pair of electrons', ['Two pairs of electrons', 'Three pairs of electrons', 'No electrons'])

add(93,'Chemistry','States of Matter','Easy',
    'The change of state from gas directly to solid, without passing through the liquid phase, is called:',
    'Deposition', ['Sublimation', 'Condensation', 'Freezing'])
add(94,'Chemistry','States of Matter','Medium',
    "A gas occupies 10.0 L at 1.0 atm. What volume will it occupy at 5.0 atm, assuming constant temperature (Boyle's Law)?",
    '2.0 L', ['50.0 L', '5.0 L', '10.0 L'])
add(95,'Chemistry','States of Matter','Hard',
    "A fixed mass of gas at 4 atm and 400 K is cooled at constant volume until its pressure drops to 2 atm. What is the new temperature (Gay-Lussac's Law)?",
    '200 K', ['800 K', '100 K', '400 K'])

add(96,'Chemistry','Stoichiometry','Easy',
    'The molar mass of ammonia (NH3) is approximately:',
    '17 g/mol', ['14 g/mol', '16 g/mol', '34 g/mol'])
add(97,'Chemistry','Stoichiometry','Medium',
    'How many moles are present in 24 g of magnesium (molar mass 24 g/mol)?',
    '1 mol', ['0.5 mol', '2 mol', '24 mol'])
add(98,'Chemistry','Stoichiometry','Hard',
    'A 200 mL solution contains 0.05 mole of Na2CO3. What is the molarity of this solution?',
    '0.25 M', ['0.1 M', '0.05 M', '4 M'])
add(99,'Chemistry','Stoichiometry','Medium',
    'In the balanced equation CaCO3 -> CaO + CO2, how many moles of CO2 are produced from the complete decomposition of 4 moles of CaCO3?',
    '4', ['2', '8', '1'])

add(100,'Chemistry','Thermochemistry','Easy',
    'A reaction that absorbs heat from its surroundings is classified as:',
    'Endothermic', ['Exothermic', 'Isobaric', 'Isochoric'])
add(101,'Chemistry','Thermochemistry','Medium',
    'The standard enthalpy of combustion of a substance is always:',
    'Negative (exothermic), since combustion releases heat',
    ['Positive (endothermic)', 'Equal to zero', 'Undefined for organic compounds'])

add(102,'Chemistry','Chemical Equilibrium','Medium',
    'For the equilibrium 2NO2(g) <-> N2O4(g), decreasing the temperature (an exothermic forward reaction) will shift the equilibrium:',
    'Toward the product (N2O4)', ['Toward the reactants (NO2)', 'Not at all', 'Completely to the reactant side'])
add(103,'Chemistry','Chemical Equilibrium','Hard',
    "According to Le Chatelier's principle, removing product from an equilibrium mixture as it forms will:",
    'Shift the equilibrium toward the products, favoring further forward reaction',
    ['Shift the equilibrium toward the reactants', 'Have no effect on the equilibrium', 'Stop the reaction entirely'])

add(104,'Chemistry','Reaction Kinetics','Easy',
    'Increasing the surface area of a solid reactant generally increases reaction rate mainly because:',
    'It exposes more particles at the surface, increasing the frequency of effective collisions',
    ['It decreases the number of particle collisions', 'It lowers the temperature of the reaction', 'It decreases the concentration of reactants'])
add(105,'Chemistry','Reaction Kinetics','Medium',
    'A reaction is zero order with respect to a reactant. Doubling the concentration of that reactant will:',
    'Have no effect on the rate', ['Double the rate', 'Quadruple the rate', 'Halve the rate'])

add(106,'Chemistry','Electrochemistry','Medium',
    'In an electrolytic cell, an external power source is used to:',
    'Drive a non-spontaneous redox reaction',
    ['Generate electricity spontaneously', 'Prevent any reaction from occurring', 'Measure the pH of a solution'])
add(107,'Chemistry','Electrochemistry','Hard',
    'In the reaction Fe + CuSO4 -> FeSO4 + Cu, iron is oxidized while copper ion (Cu2+) is:',
    'Reduced, gaining electrons to form solid copper', ['Oxidized', 'Unchanged', 'Acting as a catalyst'])

add(108,'Chemistry','Acids & Bases','Easy',
    'According to the Bronsted-Lowry definition, an acid is a substance that:',
    'Donates a proton (H+)', ['Accepts a proton (H+)', 'Accepts a pair of electrons', 'Donates a hydroxide ion'])
add(109,'Chemistry','Acids & Bases','Medium',
    'A solution has [H+] = 1x10^-4 M. What is its pH?',
    '4', ['10', '-4', '0.4'])
add(110,'Chemistry','Acids & Bases','Medium',
    'The graph shows the pH curve as NaOH is added to a weak acid (acetic acid) solution. Based on the shape of the curve, the pH at the equivalence point is expected to be:',
    'Slightly greater than 7, because the resulting salt solution is weakly basic',
    ['Exactly 7.0', 'Slightly less than 7', 'Extremely low, near pH 1'],
    image='images/q5_titration_curve_weak_acid.png')
add(111,'Chemistry','Acids & Bases','Hard',
    "A solution's buffering capacity is greatest when:",
    'The concentrations of the weak acid and its conjugate base are roughly equal',
    ['The concentrations of the weak acid and its conjugate base are very different', 'Only a strong acid is present', 'No equilibrium exists in solution'])

add(112,'Chemistry','Organic Chemistry','Easy',
    'The functional group -OH attached to a carbon chain (not part of a carboxyl group) characterizes a class of compounds called:',
    'Alcohols', ['Ethers', 'Aldehydes', 'Esters'])
add(113,'Chemistry','Organic Chemistry','Medium',
    'Alkanes are generally less reactive than alkenes mainly because alkanes:',
    'Contain only strong, relatively unreactive single (sigma) bonds, lacking the reactive pi bond of a double bond',
    ['Contain highly reactive triple bonds', 'Have no carbon-hydrogen bonds', 'Are always found as gases'])
add(114,'Chemistry','Organic Chemistry','Medium',
    'An ether functional group is characterized by an oxygen atom:',
    'Bonded to two separate carbon-containing groups',
    ['Double-bonded to a single carbon', 'Bonded to a hydrogen and a carbon (as in -OH)', 'Bonded to nitrogen'])
add(115,'Chemistry','Organic Chemistry','Hard',
    'In addition polymerization, monomers with a carbon-carbon double bond join together mainly by:',
    'The double bond opening up, allowing monomers to bond directly to one another without any byproduct',
    ['Releasing a small molecule such as water at each linkage', 'Hydrolysis of an ester linkage', 'Losing a halogen atom at each step'])
add(116,'Chemistry','Organic Chemistry','Medium',
    'Saponification refers to the reaction of a fat or oil with a strong base to produce:',
    'Soap (a fatty acid salt) and glycerol', ['An ester and water', 'A polymer', 'Only carbon dioxide and water'])
add(117,'Chemistry','Organic Chemistry','Easy',
    'Optical isomers (enantiomers) are non-superimposable mirror images of each other that arise due to the presence of a:',
    'Chiral (asymmetric) carbon', ['Double bond', 'Benzene ring', 'Halogen substituent'])

add(118,'Chemistry','Inorganic Chemistry','Medium',
    'Group 1 (alkali metal) hydroxides, such as NaOH, are generally:',
    'Strong bases that fully dissociate in water', ['Weak bases', 'Neutral compounds', 'Strong acids'])
add(119,'Chemistry','Inorganic Chemistry','Medium',
    'Noble gases are generally unreactive mainly because they:',
    'Already possess a complete (stable) outer electron shell',
    ['Have incomplete outer electron shells', 'Have very small atomic radii only', 'Are strongly electronegative'])
add(120,'Chemistry','Inorganic Chemistry','Hard',
    "In the reaction 2Na + Cl2 -> 2NaCl, sodium's oxidation state changes from:",
    '0 to +1 (oxidation)', ['0 to -1', '+1 to 0', 'No change occurs'])

add(121,'Chemistry','Physical Chemistry','Medium',
    'Mole fraction of a component in a mixture is defined as:',
    'Moles of that component divided by total moles of all components in the mixture',
    ['Grams of that component per liter of solution', 'Moles of that component per kilogram of solvent', 'Volume of that component divided by total volume'])
add(122,'Chemistry','Physical Chemistry','Hard',
    '15 mL of 0.4 M H2SO4 is required to exactly neutralize 30 mL of NaOH solution (H2SO4 + 2NaOH -> Na2SO4 + 2H2O). What is the molarity of the NaOH solution?',
    '0.4 M', ['0.2 M', '0.8 M', '0.1 M'])

add(123,'Chemistry','Environmental Chemistry','Easy',
    'Which of the following is considered a renewable energy source?',
    'Solar energy', ['Coal', 'Natural gas', 'Petroleum'])
add(124,'Chemistry','Environmental Chemistry','Medium',
    'Eutrophication of a water body is primarily triggered by:',
    'Excessive nutrient input (such as nitrates and phosphates), causing algal blooms and subsequent oxygen depletion',
    ['Excess dissolved oxygen', 'A decrease in water temperature', 'High salinity alone'])

# ============================================================
# PHYSICS (36) - id 127-162
# ============================================================
add(127,'Physics','Kinematics','Easy',
    "A car travels 150 km in 3 hours at constant velocity. What is the car's average speed?",
    '50 km/h', ['450 km/h', '45 km/h', '3 km/h'])
add(128,'Physics','Kinematics','Medium',
    'A cyclist accelerates uniformly from 4 m/s to 12 m/s over 4 seconds. What is the acceleration?',
    '2 m/s^2', ['4 m/s^2', '8 m/s^2', '3 m/s^2'])
add(129,'Physics','Kinematics','Hard',
    'A stone is thrown vertically upward with an initial velocity of 30 m/s (g = 10 m/s^2). How long does it take to reach its maximum height?',
    '3 s', ['1 s', '6 s', '30 s'])

add(130,'Physics','Dynamics','Easy',
    'The property of an object that resists changes to its state of motion is called:',
    'Inertia', ['Momentum', 'Velocity', 'Acceleration'])
add(131,'Physics','Dynamics','Medium',
    'A 6 kg object accelerates at 2.5 m/s^2 due to an applied net force. What is the magnitude of this force?',
    '15 N', ['2.4 N', '8.5 N', '3.5 N'])
add(132,'Physics','Dynamics','Medium',
    "Momentum is defined as the product of an object's:",
    'Mass and velocity', ['Mass and acceleration', 'Force and time', 'Velocity and time'])
add(133,'Physics','Dynamics','Hard',
    "A 6 kg block is pushed horizontally with a 42 N force across a surface with a coefficient of kinetic friction of 0.3 (g = 10 m/s^2). What is the block's acceleration?",
    '4 m/s^2', ['2 m/s^2', '7 m/s^2', '1 m/s^2'])

add(134,'Physics','Work, Energy & Power','Easy',
    'Power is defined as the rate at which:',
    'Work is done, or energy is transferred, per unit time',
    ['Force is applied', 'Distance is covered', 'Mass changes over time'])
add(135,'Physics','Work, Energy & Power','Medium',
    'A 6 kg object is raised to a height of 3 m (g = 10 m/s^2). What is its gravitational potential energy at that height?',
    '180 J', ['18 J', '30 J', '60 J'])
add(136,'Physics','Work, Energy & Power','Medium',
    'A 4 kg object moving at 3 m/s has a kinetic energy of:',
    '18 J', ['12 J', '24 J', '36 J'])
add(137,'Physics','Work, Energy & Power','Hard',
    'An elevator motor lifts a 600 kg cabin to a height of 15 m in 20 seconds (g = 10 m/s^2). What is the power output of the motor?',
    '4500 W', ['450 W', '90000 W', '9000 W'])

add(138,'Physics','Circular Motion & Gravitation','Easy',
    'The force that keeps a satellite in circular orbit around a planet is provided by:',
    'Gravitational attraction between the satellite and the planet',
    ['Friction', 'Air resistance', "The satellite's own thrust continuously"])
add(139,'Physics','Circular Motion & Gravitation','Medium',
    'If the mass of one of two objects is doubled while the distance between them stays the same, the gravitational force between them becomes:',
    'Twice as large', ['Half as large', 'Four times as large', 'Unchanged'])
add(140,'Physics','Circular Motion & Gravitation','Hard',
    "According to Kepler's third law, the square of a planet's orbital period is proportional to:",
    'The cube of its average distance from the Sun',
    ["The planet's mass", "The planet's radius only", 'The eccentricity of its orbit'])

add(141,'Physics','Fluid Mechanics','Easy',
    "According to Pascal's principle, pressure applied to an enclosed, incompressible fluid is:",
    'Transmitted equally in all directions throughout the fluid',
    ['Absorbed entirely at the point of application', 'Lost as heat', 'Reduced as it moves through the fluid'])
add(142,'Physics','Fluid Mechanics','Medium',
    'An object floats partially submerged in a fluid when:',
    'Its weight equals the buoyant force exerted by the displaced fluid',
    ['Its density is greater than the fluid\'s density', 'It has zero weight', 'The fluid has no density'])
add(143,'Physics','Fluid Mechanics','Hard',
    'A hydraulic lift uses a small-area piston to generate a large force on a larger-area piston, according to:',
    'Pascal\'s principle, since pressure is transmitted equally throughout the fluid',
    ["Bernoulli's principle", 'The continuity equation', "Archimedes' principle"])

add(144,'Physics','Oscillations & Waves','Easy',
    'The distance between two consecutive crests (or troughs) of a wave is called its:',
    'Wavelength', ['Amplitude', 'Frequency', 'Period'])
add(145,'Physics','Oscillations & Waves','Medium',
    'The speed of a wave is related to its frequency and wavelength by the equation:',
    'v = f x lambda', ['v = f / lambda', 'v = f + lambda', 'v = lambda / f^2'])
add(146,'Physics','Oscillations & Waves','Medium',
    'A wave travels at 340 m/s and has a wavelength of 0.68 m. What is its frequency?',
    '500 Hz', ['231 Hz', '5 Hz', '50 Hz'])
add(147,'Physics','Oscillations & Waves','Hard',
    'Resonance occurs when a system is driven at a frequency that matches its:',
    'Natural (or fundamental) frequency, causing a large increase in amplitude',
    ['Amplitude', 'Wavelength only', 'Damping coefficient'])

add(148,'Physics','Thermodynamics','Easy',
    'Specific heat capacity is defined as the amount of heat required to raise the temperature of:',
    'A unit mass of a substance by one degree (Celsius or Kelvin)',
    ['Any amount of a substance by any temperature change', 'A substance until it boils', 'A gas at constant volume only'])
add(149,'Physics','Thermodynamics','Medium',
    'According to the second law of thermodynamics, in any spontaneous process, the total entropy of an isolated system:',
    'Always increases or remains constant',
    ['Always decreases', 'Always remains exactly constant', 'Is unrelated to spontaneity'])
add(150,'Physics','Thermodynamics','Hard',
    'In an adiabatic process, a gas expands and does work on its surroundings without any heat exchange. The internal energy of the gas will:',
    'Decrease', ['Increase', 'Remain exactly constant', 'Become infinite'])

add(151,'Physics','Electrostatics','Easy',
    'The SI unit of electric charge is the:',
    'Coulomb', ['Volt', 'Ampere', 'Ohm'])
add(152,'Physics','Electrostatics','Medium',
    'Two point charges of the same sign, when brought near each other, will experience a force that is:',
    'Repulsive', ['Attractive', 'Zero', 'Dependent only on their mass'])

add(153,'Physics','Current Electricity','Easy',
    "Ohm's law relates voltage, current, and resistance according to the equation:",
    'V = I x R', ['V = I / R', 'V = I + R', 'V = R / I'])
add(154,'Physics','Current Electricity','Medium',
    'In the circuit shown, R1 (4 ohm) and R2 (4 ohm) are connected in parallel, and this parallel combination is connected in series with R3 (3 ohm). What is the total resistance of the circuit?',
    '5 ohm', ['8 ohm', '2 ohm', '11 ohm'],
    image='images/q5_circuit_diagram_r1r2r3.png')
add(155,'Physics','Current Electricity','Hard',
    'Four resistors of 10 ohm each are connected in series. What is their total resistance?',
    '40 ohm', ['2.5 ohm', '10 ohm', '100 ohm'])
add(156,'Physics','Current Electricity','Medium',
    'A device draws a current of 5 A when connected to a 100 V supply. What is its resistance?',
    '20 ohm', ['500 ohm', '0.05 ohm', '105 ohm'])

add(157,'Physics','Electromagnetism','Medium',
    'A current-carrying wire placed within an external magnetic field experiences a force that is:',
    'Perpendicular to both the current direction and the magnetic field, as given by the right-hand rule',
    ['Parallel to the current direction always', "Independent of the current's direction", 'Zero regardless of orientation'])
add(158,'Physics','Electromagnetism','Hard',
    "According to Faraday's law of electromagnetic induction, an EMF is induced in a coil whenever:",
    'The magnetic flux through the coil changes over time',
    ['The coil is stationary in a constant magnetic field', 'No current flows through the coil', 'The coil has zero resistance'])

add(159,'Physics','Modern Physics','Easy',
    'Isotopes of the same element have the same number of protons but a different number of:',
    'Neutrons', ['Electrons', 'Valence electrons', 'Energy levels'])
add(160,'Physics','Modern Physics','Medium',
    'During alpha decay, a nucleus emits a particle consisting of:',
    '2 protons and 2 neutrons (a helium nucleus)',
    ['A single electron', 'A single proton only', 'High-energy electromagnetic radiation only'])
add(161,'Physics','Modern Physics','Hard',
    'A radioactive isotope has a half-life of 5 days. Approximately what fraction of the original sample remains after 20 days?',
    '1/16', ['1/2', '1/4', '1/8'])

add(162,'Physics','Optics','Medium',
    'The ray diagram shows an object placed exactly at the focal point (F) of a converging (convex) lens. Based on the diagram, the rays emerging from the lens are:',
    'Parallel to each other, so no real image forms on a screen at any finite distance',
    ['Converging to form a small real image close to the lens', 'Diverging as though from a virtual image behind the lens', 'Converging exactly at the lens itself'],
    image='images/q5_lens_diagram_object_at_f.png')

# ============================================================
# ENGLISH (9) - id 163-171
# ============================================================
add(163,'English','Synonyms','Easy',
    "Choose the word most nearly similar in meaning to 'CANDID':",
    'Frank', ['Deceptive', 'Secretive', 'Timid'])
add(164,'English','Antonyms','Easy',
    "Choose the word most nearly opposite in meaning to 'RETAIN':",
    'Discard', ['Keep', 'Preserve', 'Maintain'])
add(165,'English','Grammar','Easy',
    'Choose the grammatically correct sentence:',
    "She doesn't like coffee.", ["She don't like coffee.", "She doesn't likes coffee.", 'She not like coffee.'])
add(166,'English','Grammar','Medium',
    'Choose the correct sentence:',
    'If I had known, I would have come.',
    ['If I would have known, I would have come.', 'If I know, I would have come.', 'If I had known, I will come.'])
add(167,'English','Sentence Correction','Medium',
    'Identify the sentence that follows correct subject-verb agreement:',
    'The team of scientists is conducting the experiment.',
    ['The team of scientists are conducting the experiment.', 'The teams of scientist is conducting the experiment.', 'The team of scientists were conducting the experiment, is it?'])
add(168,'English','Vocabulary','Medium',
    "Choose the word that best completes the sentence: 'Her ______ remarks during the meeting offended several colleagues.'",
    'Blunt', ['Tactful', 'Courteous', 'Diplomatic'])
add(169,'English','Idioms','Medium',
    "Choose the meaning closest to the idiom 'to hit the nail on the head':",
    'To describe something exactly right',
    ['To make a costly mistake', 'To finish a task quickly', 'To argue unnecessarily'])
add(170,'English','Sentence Correction','Hard',
    "Choose the option that best corrects the sentence: 'Everyone must bring their own lunch to the picnic.'",
    'Everyone must bring his or her own lunch to the picnic.',
    ['Everyone must bring their own lunches to the picnic.', 'Everyone must bring his own lunches to the picnic.', 'Everybody must bring their own lunch to the picnics.'])
add(171,'English','Prepositions','Hard',
    "Choose the correct preposition to complete the sentence: 'The scientist is known ______ her groundbreaking research.'",
    'for', ['on', 'at', 'with'])

# ============================================================
# LOGICAL REASONING (9) - id 172-180
# ============================================================
add(172,'Logical Reasoning','Number Series','Easy',
    'Find the next number in the series: 7, 14, 28, 56, ?',
    '112', ['84', '98', '70'])
add(173,'Logical Reasoning','Number Series','Easy',
    'Find the missing number: 3, 8, 13, 18, ?',
    '23', ['20', '22', '25'])
add(174,'Logical Reasoning','Analogies','Easy',
    'Pen is to Write as Knife is to:',
    'Cut', ['Sharp', 'Kitchen', 'Blade'])
add(175,'Logical Reasoning','Analogies','Medium',
    'Fish is to Water as Bird is to:',
    'Sky', ['Nest', 'Feather', 'Beak'])
add(176,'Logical Reasoning','Blood Relations','Medium',
    "Sara said, 'His mother is the only daughter of my grandmother.' How is the man related to Sara?",
    'Brother', ['Cousin', 'Father', 'Uncle'])
add(177,'Logical Reasoning','Coding-Decoding','Medium',
    'If in a certain code, CHAIR is written as DIBJS, how is TABLE written in the same code?',
    'UBCMF', ['UACMF', 'UBDMG', 'VBCMF'])
add(178,'Logical Reasoning','Syllogism','Hard',
    'All mammals are warm-blooded. All cats are mammals. Which conclusion logically follows?',
    'All cats are warm-blooded',
    ['All warm-blooded animals are cats', 'No cats are warm-blooded', 'Some mammals are not warm-blooded'])
add(179,'Logical Reasoning','Pattern Recognition','Hard',
    'Find the next term in the series: 3, 6, 11, 18, 27, ?',
    '38', ['36', '40', '34'])
add(180,'Logical Reasoning','Direction Sense','Medium',
    'A man walks 8 km east, then turns south and walks 15 km. How far is he from his starting point?',
    '17 km', ['23 km', '7 km', '21 km'])

# ============================================================
# Assign balanced option letters (shuffled, no long runs) and
# build final QUESTIONS list
# ============================================================
random.seed(7331)

LETTERS = ['A', 'B', 'C', 'D']
n = len(RAW)
base = n // 4
rem = n % 4
pool = []
for idx, L in enumerate(LETTERS):
    cnt = base + (1 if idx < rem else 0)
    pool.extend([L] * cnt)

def shuffled_no_long_runs(pool, max_run=2, tries=2000):
    for _ in range(tries):
        random.shuffle(pool)
        ok = True
        run = 1
        for i in range(1, len(pool)):
            if pool[i] == pool[i-1]:
                run += 1
                if run > max_run:
                    ok = False
                    break
            else:
                run = 1
        if ok:
            return pool[:]
    return pool[:]

letter_sequence = shuffled_no_long_runs(pool)

RAW_sorted = sorted(RAW, key=lambda r: r["id"])

QUESTIONS = []
for i, r in enumerate(RAW_sorted):
    correct_letter = letter_sequence[i]
    slot_order = [correct_letter] + [l for l in LETTERS if l != correct_letter]
    values = [r['correct']] + r['distractors']
    options = {}
    for letter, val in zip(slot_order, values):
        options[letter] = val
    options = {L: options[L] for L in LETTERS}
    q = {
        "id": r["id"], "subject": r["subject"], "topic": r["topic"], "difficulty": r["difficulty"],
        "question": r["question"], "options": options, "answer": correct_letter
    }
    if r["image"]:
        q["image"] = r["image"]
    QUESTIONS.append(q)

# ------------------------------------------------------------
# Sanity checks
# ------------------------------------------------------------
from collections import Counter
assert len(QUESTIONS) == 180, len(QUESTIONS)
ids = [q["id"] for q in QUESTIONS]
assert len(set(ids)) == 180, "duplicate ids"
assert ids == list(range(1, 181)), "ids not sequential 1-180"
subj = Counter(q["subject"] for q in QUESTIONS)
assert subj == {"Biology": 81, "Chemistry": 45, "Physics": 36, "English": 9, "Logical Reasoning": 9}, subj
ans = Counter(q["answer"] for q in QUESTIONS)
diff = Counter(q["difficulty"] for q in QUESTIONS)
qtext = [q["question"] for q in QUESTIONS]
assert len(set(qtext)) == 180, "duplicate question text"
images = [q for q in QUESTIONS if "image" in q]
for q in QUESTIONS:
    assert set(q["options"].keys()) == {"A", "B", "C", "D"}
    assert q["answer"] in q["options"]

print("Subject counts:", dict(subj))
print("Answer letter counts:", dict(ans))
print("Difficulty counts:", dict(diff))
print("Image questions:", len(images))
for q in images:
    print(" ", q["id"], q["subject"], q["image"])

with open("mock5_data.json", "w") as f:
    json.dump(QUESTIONS, f, indent=2)

print("\nOK - all checks passed. Data written to mock5_data.json")