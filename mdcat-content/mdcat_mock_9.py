# -*- coding: utf-8 -*-
"""
Builder for MDCAT Mock Test 9.
Raw question data (question, correct answer, 3 distractors) is defined below;
this script assigns option letters in a shuffled, balanced rotation so correct
answers are evenly spread across A/B/C/D, then writes the final mock9.py file
in the same format as the earlier mocks.
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
    'Starch and glycogen are both polysaccharides that function mainly as:',
    'Energy storage molecules in plants and animals respectively',
    ['Structural components of cell walls', 'Genetic material', 'Enzymes'])
add(2,'Biology','Biomolecules','Easy',
    'Amino acids are joined together to form proteins primarily through:',
    'Peptide bonds', ['Glycosidic bonds', 'Ester bonds', 'Hydrogen bonds'])
add(3,'Biology','Biomolecules','Medium',
    'Which of the following best describes an unsaturated fatty acid?',
    'It contains one or more carbon-carbon double bonds, reducing the number of hydrogen atoms compared to a saturated fatty acid',
    ['It contains no carbon-hydrogen bonds', 'It is always solid at room temperature', 'It cannot be metabolized by the body'])
add(4,'Biology','Biomolecules','Medium',
    'Which bond is primarily responsible for holding the two strands of a DNA double helix together?',
    'Hydrogen bonds between complementary bases',
    ['Peptide bonds', 'Phosphodiester bonds within a single strand', 'Ionic bonds between phosphate groups'])
add(5,'Biology','Biomolecules','Hard',
    "A protein's function is critically dependent on its three-dimensional shape. Sickle cell hemoglobin differs from normal hemoglobin by a single amino acid substitution, which illustrates that:",
    "Even a single amino acid change in primary structure can significantly alter a protein's structure and function",
    ['Primary structure changes rarely affect overall protein function', "Only quaternary structure affects protein function", 'Amino acid sequence has no bearing on protein shape'])

add(6,'Biology','Enzymes','Easy',
    'Enzymes speed up biochemical reactions mainly by:',
    'Lowering the activation energy required for the reaction to proceed',
    ['Increasing the temperature of the reaction', 'Being permanently altered during the reaction', 'Increasing the amount of product formed beyond the equilibrium point'])
add(7,'Biology','Enzymes','Medium',
    'A cofactor that is a non-protein organic molecule, often derived from a vitamin, is more specifically called a:',
    'Coenzyme', ['Apoenzyme', 'Holoenzyme', 'Zymogen'])
add(8,'Biology','Enzymes','Medium',
    'The graph shows the initial reaction rate of an enzyme-catalyzed reaction plotted against increasing enzyme concentration, with substrate held in constant excess. The rate increases proportionally as shown. This linear relationship is best explained by:',
    'More enzyme molecules being available to bind substrate simultaneously, as substrate is not limiting',
    ['Substrate becoming the limiting factor', 'The enzyme becoming denatured', "A decrease in the reaction's activation energy over time"],
    image='images/q9_enzyme_concentration_graph.png')
add(9,'Biology','Enzymes','Hard',
    'Feedback inhibition in a metabolic pathway typically occurs when:',
    'The final product of a pathway binds to and inhibits an earlier enzyme in the same pathway, often allosterically',
    ['The first enzyme in a pathway is activated by an early substrate', 'Every enzyme in the pathway is inhibited simultaneously by an external toxin', 'Substrate concentration has no effect on pathway regulation'])

add(10,'Biology','Cell Biology','Easy',
    'The jelly-like fluid within a cell, in which organelles are suspended, is called the:',
    'Cytoplasm', ['Nucleoplasm', 'Extracellular matrix', 'Cytoskeleton'])
add(11,'Biology','Cell Biology','Easy',
    'Which organelle is responsible for the intracellular digestion of worn-out organelles and macromolecules using hydrolytic enzymes?',
    'Lysosome', ['Peroxisome', 'Golgi apparatus', 'Ribosome'])
add(12,'Biology','Cell Biology','Medium',
    'Which structure is present in plant cells but typically absent in animal cells?',
    'Chloroplast', ['Mitochondrion', 'Ribosome', 'Nucleus'])
add(13,'Biology','Cell Biology','Medium',
    'Microvilli, tiny finger-like projections on certain cell surfaces (such as intestinal epithelial cells), primarily function to:',
    'Increase surface area for absorption',
    ['Propel the cell through fluid', 'Anchor chromosomes during division', 'Synthesize lipids'])
add(14,'Biology','Cell Biology','Medium',
    'The diagram shows an animal cell with structures labeled W, X, Y, and Z. Structure Z is a membrane-bound vesicle containing hydrolytic enzymes used to break down waste materials and worn-out organelles. Which structure is Z?',
    'Structure Z (lysosome)',
    ['Structure W (nucleus)', 'Structure X (mitochondrion)', 'Structure Y (Golgi apparatus)'],
    image='images/q9_cell_diagram_wxyz.png')
add(15,'Biology','Cell Biology','Medium',
    'Ribosomes, whether free in the cytoplasm or attached to the rough ER, are composed of:',
    'rRNA and proteins', ['DNA and proteins', 'mRNA only', 'Lipids and carbohydrates'])
add(16,'Biology','Cell Biology','Hard',
    'A cell exposed to a chemical that specifically inhibits ATP synthase would most directly experience a reduced ability to:',
    'Generate ATP via oxidative phosphorylation',
    ['Replicate its DNA', 'Synthesize proteins directly', 'Transcribe mRNA'])

add(17,'Biology','Cell Membrane & Transport','Easy',
    'The process by which a cell expends energy to move substances against their concentration gradient is called:',
    'Active transport', ['Diffusion', 'Osmosis', 'Facilitated diffusion'])
add(18,'Biology','Cell Membrane & Transport','Medium',
    'Plasmolysis occurs in plant cells when they are placed in a strongly hypertonic solution, causing:',
    'The cell membrane to pull away from the cell wall as water leaves the cell',
    ['The cell wall to rupture', 'The cell to swell and burst', 'No change in cell shape'])
add(19,'Biology','Cell Membrane & Transport','Medium',
    'Pinocytosis is a form of endocytosis in which a cell:',
    'Takes in dissolved substances and extracellular fluid via small vesicles',
    ['Engulfs large solid particles', 'Releases digestive enzymes', 'Actively pumps out excess water'])
add(20,'Biology','Cell Membrane & Transport','Hard',
    'Aquaporins are specialized channel proteins that primarily facilitate the rapid movement of:',
    'Water molecules across the plasma membrane',
    ['Glucose molecules', 'Sodium ions against their gradient', 'Large proteins'])
add(21,'Biology','Cell Membrane & Transport','Easy',
    'Glycoproteins on the outer surface of the plasma membrane primarily function in:',
    'Cell recognition and signaling',
    ['Generating ATP', 'Replicating DNA', 'Breaking down worn-out organelles'])

add(22,'Biology','Cell Cycle & Division','Easy',
    'During which phase of interphase does a cell primarily synthesize proteins and organelles in preparation for DNA replication?',
    'G1 phase', ['S phase', 'G2 phase', 'M phase'])
add(23,'Biology','Cell Cycle & Division','Easy',
    'During telophase of mitosis, which of the following occurs?',
    'Two new nuclear envelopes begin to form around each set of chromosomes',
    ['Chromosomes condense for the first time', 'Chromosomes align at the equator', 'Sister chromatids separate and move to opposite poles'])
add(24,'Biology','Cell Cycle & Division','Medium',
    'Which of the following best distinguishes meiosis I from meiosis II?',
    'Meiosis I separates homologous chromosomes, while meiosis II separates sister chromatids',
    ['Meiosis I separates sister chromatids, while meiosis II separates homologous chromosomes', 'Both meiosis I and II separate sister chromatids identically', 'DNA replication occurs before both meiosis I and meiosis II'])
add(25,'Biology','Cell Cycle & Division','Medium',
    'A human somatic cell has 46 chromosomes. After completing mitosis, how many chromosomes will each of the two daughter cells contain?',
    '46', ['23', '92', '12'])
add(26,'Biology','Cell Cycle & Division','Medium',
    'The synaptonemal complex forms during prophase I of meiosis to facilitate:',
    'Pairing of homologous chromosomes, enabling crossing over',
    ['Random assortment of chromosomes', 'Separation of sister chromatids', 'Cell membrane pinching'])
add(27,'Biology','Cell Cycle & Division','Hard',
    'Telomeres, the repetitive DNA sequences at the ends of chromosomes, primarily function to:',
    'Protect chromosome ends from degradation and prevent loss of important genetic information during replication',
    ['Code for essential proteins', 'Serve as the site of crossing over', 'Anchor the chromosome to the nuclear envelope permanently'])

add(28,'Biology','Genetics','Easy',
    'In fruit flies, long wings (L) are dominant over vestigial wings (l). A cross between two heterozygous long-winged flies (Ll x Ll) produces offspring with what phenotypic ratio?',
    '3 long : 1 vestigial', ['1 long : 1 vestigial', 'All long', 'All vestigial'])
add(29,'Biology','Genetics','Medium',
    'A dihybrid cross between two individuals heterozygous for two independently assorting traits (AaBb x AaBb): what fraction of offspring is expected to show both dominant phenotypes?',
    '9/16', ['1/16', '3/16', '1/4'])
add(30,'Biology','Genetics','Medium',
    'Duchenne muscular dystrophy is X-linked recessive. If a carrier mother and an affected father have children, what proportion of their daughters is expected to be affected?',
    '50%', ['0%', '25%', '100%'])
add(31,'Biology','Genetics','Hard',
    'In a cross AaBb x aabb (a test cross for two genes), assuming independent assortment, what fraction of offspring is expected to display the recessive phenotype for both traits?',
    '1/4', ['1/2', '1/8', '1/16'])
add(32,'Biology','Genetics','Medium',
    'Two parents, both with blood type AB, have children. Which blood types are possible among their offspring?',
    'A, B, and AB only', ['Only AB', 'A, B, AB, and O', 'Only A and B'])
add(33,'Biology','Genetics','Hard',
    'A pedigree shows a trait appearing more frequently in males than females, with affected males always inheriting the trait from their mothers (who are typically unaffected carriers), and affected fathers never passing the trait to their sons. This pattern is most consistent with:',
    'X-linked recessive inheritance',
    ['Autosomal dominant inheritance', 'Y-linked inheritance', 'Mitochondrial inheritance'])
add(34,'Biology','Genetics','Medium',
    'Human skin color is influenced by multiple genes, each contributing a small additive effect, resulting in a continuous range of phenotypes rather than distinct categories. This is an example of:',
    'Polygenic inheritance', ['Codominance', 'Incomplete dominance', 'Epistasis'])

add(35,'Biology','Molecular Biology','Easy',
    'Thymine in DNA is replaced by which base in RNA?',
    'Uracil', ['Cytosine', 'Guanine', 'Adenine'])
add(36,'Biology','Molecular Biology','Easy',
    'The synthesis of an mRNA molecule from a DNA template, occurring in the nucleus, is called:',
    'Transcription', ['Translation', 'Replication', 'Splicing'])
add(37,'Biology','Molecular Biology','Medium',
    'The lagging strand during DNA replication requires which enzyme, in addition to DNA polymerase and ligase, to initiate synthesis of each Okazaki fragment?',
    'Primase, to lay down short RNA primers', ['Helicase', 'Topoisomerase', 'Ligase alone'])
add(38,'Biology','Molecular Biology','Medium',
    'The ribosome is composed of two subunits, a large and a small subunit, which come together on the mRNA mainly during:',
    'Initiation of translation', ['DNA replication', 'Transcription termination', 'RNA splicing'])
add(39,'Biology','Molecular Biology','Medium',
    'A mutation that changes a normal codon into a premature stop codon typically results in:',
    'A truncated (shortened), likely nonfunctional protein',
    ['A longer-than-normal protein', 'No change in protein length', 'Enhanced protein function'])
add(40,'Biology','Molecular Biology','Hard',
    "Which type of mutation would most likely have NO effect on the resulting protein's amino acid sequence?",
    'A silent mutation, due to the degeneracy of the genetic code',
    ['A frameshift mutation', 'A nonsense mutation', 'A large deletion spanning multiple codons'])
add(41,'Biology','Molecular Biology','Hard',
    'In the tryptophan (trp) operon, when tryptophan levels are high, tryptophan acts as a corepressor by:',
    'Binding to the inactive repressor protein, activating it so it can bind the operator and block transcription',
    ['Preventing the repressor protein from binding the operator', 'Directly binding to RNA polymerase', 'Increasing transcription of the trp genes'])
add(42,'Biology','Molecular Biology','Medium',
    'Which of the following correctly lists the general order of protein synthesis stages?',
    'Transcription in the nucleus, followed by translation at the ribosome',
    ['Translation, then transcription', 'Replication, then translation, then transcription', 'Splicing, then replication'])
add(43,'Biology','Molecular Biology','Medium',
    'A gene that has undergone alternative splicing to skip a particular exon will produce an mRNA and resulting protein that:',
    'Lacks the amino acid sequence normally encoded by that exon',
    ['Is identical to the standard version', 'Cannot be translated at all', 'Contains extra introns'])
add(44,'Biology','Molecular Biology','Easy',
    'Which of the following best describes the relationship between a gene and a codon?',
    'A gene is typically composed of many codons, each specifying one amino acid',
    ['A gene is a single codon', 'A codon contains many genes', 'Genes and codons are unrelated'])

add(45,'Biology','Evolution','Easy',
    'Which of the following is considered a mechanism that can introduce new genetic variation into a population?',
    'Mutation', ['Natural selection', 'Genetic drift', 'Gene flow from an identical population'])
add(46,'Biology','Evolution','Medium',
    'Artificial selection, as practiced by dog breeders, differs from natural selection mainly in that artificial selection:',
    'Involves humans intentionally choosing which traits are favored for breeding, rather than the environment selecting them',
    ['Cannot produce noticeable changes in a population', 'Never involves heritable traits', 'Always reduces genetic diversity to zero'])
add(47,'Biology','Evolution','Medium',
    'Which of the following would violate the assumption of random mating required for Hardy-Weinberg equilibrium?',
    'Individuals preferentially mate with those of similar phenotype (assortative mating)',
    ['Individuals mate entirely by chance', 'The population is infinitely large', 'No selection is occurring'])
add(48,'Biology','Evolution','Hard',
    'In a population in Hardy-Weinberg equilibrium, 9% of individuals show the recessive phenotype. What is the frequency of the heterozygous genotype?',
    '0.42', ['0.09', '0.49', '0.21'])

add(49,'Biology','Classification & Diversity','Easy',
    'Which of the following represents the correct order of the taxonomic hierarchy, from broadest to most specific?',
    'Domain, Kingdom, Phylum, Class, Order, Family, Genus, Species',
    ['Species, Genus, Family, Order, Class, Phylum, Kingdom, Domain', 'Kingdom, Domain, Class, Phylum, Order, Family, Genus, Species', 'Domain, Phylum, Kingdom, Class, Order, Family, Genus, Species'])
add(50,'Biology','Classification & Diversity','Easy',
    'Members of kingdom Protista are generally described as:',
    "A diverse group of mostly unicellular eukaryotes that don't fit neatly into the other kingdoms",
    ['Multicellular photosynthetic autotrophs only', 'Prokaryotic organisms with peptidoglycan cell walls', 'Heterotrophic decomposers with chitin cell walls only'])
add(51,'Biology','Classification & Diversity','Medium',
    'Phylogenetic trees constructed using molecular data (such as DNA sequences) are considered more reliable than those based solely on physical appearance mainly because:',
    'Molecular data can reveal evolutionary relationships that convergent physical similarities might obscure',
    ['Physical appearance is always more accurate', 'DNA sequences never change over time', 'Appearance-based trees require no evidence at all'])
add(52,'Biology','Classification & Diversity','Medium',
    'An organism is a unicellular eukaryote with a rigid cell wall containing cellulose and is capable of photosynthesis, but lacks the complex tissue differentiation of true plants. It most likely belongs to:',
    'Kingdom Protista (such as algae)', ['Kingdom Fungi', 'Kingdom Monera', 'Kingdom Animalia'])
add(53,'Biology','Classification & Diversity','Easy',
    'Which of the following taxonomic ranks includes multiple different orders?',
    'Class', ['Family', 'Genus', 'Species'])
add(54,'Biology','Classification & Diversity','Medium',
    'Members of phylum Echinodermata, such as starfish, are characterized primarily by:',
    'Radial symmetry as adults and a unique water vascular system used for movement',
    ['Bilateral symmetry only, with no water vascular system', 'A rigid exoskeleton made of chitin', 'A well-developed brain and centralized nervous system'])

add(55,'Biology','Plant Biology','Easy',
    'The tiny pores on the underside of leaves that allow for gas exchange are called:',
    'Stomata', ['Lenticels', 'Trichomes', 'Nodes'])
add(56,'Biology','Plant Biology','Medium',
    'During the light-dependent reactions of photosynthesis, the electron transport chain in the thylakoid membrane ultimately generates:',
    'ATP and NADPH, which are used to power the Calvin cycle',
    ['Glucose directly', 'Carbon dioxide', 'Only oxygen, with no other products'])
add(57,'Biology','Plant Biology','Medium',
    'Photosystem I and Photosystem II differ mainly in:',
    'The type of chlorophyll and the specific wavelength of light each absorbs most efficiently, and their role in the electron transport chain',
    ['Photosystem I splitting water, while Photosystem II does not', 'Neither photosystem being involved in ATP production', 'Being located in different organisms entirely'])
add(58,'Biology','Plant Biology','Hard',
    'Which of the following is a key anatomical adaptation shared by C4 plants that helps minimize photorespiration?',
    'Kranz anatomy, in which bundle-sheath cells surrounding the vascular tissue carry out the Calvin cycle, separate from the mesophyll cells that perform initial CO2 fixation',
    ['Absence of mesophyll cells', 'Complete lack of stomata', 'Performing the Calvin cycle exclusively at night'])
add(59,'Biology','Plant Biology','Medium',
    'Gibberellins, a class of plant hormones, are primarily associated with:',
    'Promoting stem elongation and breaking seed dormancy',
    ['Closing stomata during water stress', 'Triggering leaf abscission exclusively', 'Inhibiting all plant growth'])
add(60,'Biology','Plant Biology','Easy',
    'The male reproductive part of a flower, which produces pollen, is called the:',
    'Stamen', ['Pistil', 'Sepal', 'Ovary'])

add(61,'Biology','Human Physiology - Digestion','Easy',
    'The wave-like muscular contractions that propel food through the esophagus and intestines are called:',
    'Peristalsis', ['Segmentation', 'Emulsification', 'Absorption'])
add(62,'Biology','Human Physiology - Digestion','Medium',
    'Intrinsic factor, secreted by the stomach, is essential for the absorption of:',
    'Vitamin B12 in the small intestine', ['Iron', 'Calcium', 'Vitamin C'])
add(63,'Biology','Human Physiology - Digestion','Medium',
    'Which enzyme in saliva begins the chemical digestion of starch even before food reaches the stomach?',
    'Salivary amylase', ['Pepsin', 'Lipase', 'Trypsin'])
add(64,'Biology','Human Physiology - Digestion','Hard',
    'Damage to the ileum (the final section of the small intestine) would most directly impair the absorption of:',
    'Vitamin B12 and bile salts, which are specifically absorbed there',
    ['Simple sugars only', 'Water exclusively', 'Nothing, since absorption occurs earlier'])

add(65,'Biology','Human Physiology - Circulation','Easy',
    'Which blood vessel carries blood away from the heart to the rest of the body under high pressure?',
    'Artery', ['Vein', 'Capillary', 'Venule'])
add(66,'Biology','Human Physiology - Circulation','Medium',
    'The coronary arteries primarily function to:',
    'Supply oxygenated blood directly to the heart muscle itself',
    ['Carry blood from the heart to the lungs', 'Drain deoxygenated blood from the brain', 'Carry blood to the kidneys for filtration'])
add(67,'Biology','Human Physiology - Circulation','Medium',
    'Lymphatic vessels play an important role in circulation by:',
    'Returning excess interstitial fluid and proteins to the bloodstream',
    ['Pumping blood directly to the heart', 'Producing red blood cells', 'Filtering urine'])
add(68,'Biology','Human Physiology - Circulation','Hard',
    "During the cardiac cycle, the 'lub' heart sound is produced mainly by:",
    'The closing of the atrioventricular (mitral and tricuspid) valves at the start of ventricular contraction',
    ['The closing of the semilunar (aortic and pulmonary) valves', 'Blood flowing through open valves silently', 'The SA node firing'])

add(69,'Biology','Human Physiology - Respiration','Easy',
    'The two main bronchi branch off from the trachea and lead directly into the:',
    'Lungs', ['Alveoli', 'Larynx', 'Pharynx'])
add(70,'Biology','Human Physiology - Respiration','Medium',
    "Hemoglobin's affinity for oxygen decreases in tissues with lower pH and higher CO2 (the Bohr effect), which mainly helps to:",
    'Promote the release of oxygen to actively respiring tissues that need it most',
    ['Prevent oxygen from ever being released', 'Increase oxygen binding in the lungs only', 'Have no functional significance'])
add(71,'Biology','Human Physiology - Respiration','Medium',
    'Which of the following best describes the role of the epiglottis?',
    'It covers the trachea during swallowing, preventing food from entering the airway',
    ['It filters air entering the nose', 'It produces mucus in the bronchi', 'It regulates the rate of breathing'])

add(72,'Biology','Human Physiology - Excretion','Easy',
    'The tube that carries urine from each kidney to the urinary bladder is called the:',
    'Ureter', ['Urethra', 'Nephron', 'Renal vein'])
add(73,'Biology','Human Physiology - Excretion','Medium',
    'Aldosterone, a hormone released by the adrenal cortex, primarily regulates kidney function by:',
    'Increasing sodium reabsorption (and consequently water reabsorption) in the distal nephron',
    ['Decreasing sodium reabsorption', 'Blocking ADH action entirely', 'Preventing all filtration'])
add(74,'Biology','Human Physiology - Excretion','Hard',
    'A person on a very high-protein diet would be expected to produce urine containing higher-than-normal levels of:',
    'Urea, a nitrogenous waste product from amino acid breakdown',
    ['Glucose', 'Red blood cells', 'Bile pigments'])

add(75,'Biology','Human Physiology - Nervous & Endocrine','Easy',
    'The part of the brain primarily responsible for coordinating balance and fine motor control is the:',
    'Cerebellum', ['Cerebrum', 'Medulla oblongata', 'Hypothalamus'])
add(76,'Biology','Human Physiology - Nervous & Endocrine','Medium',
    'A reflex arc, such as the knee-jerk reflex, allows for a rapid response mainly because it:',
    'Involves a direct pathway through the spinal cord, often bypassing the brain for immediate action',
    ['Requires conscious processing in the cerebrum before acting', 'Never involves sensory neurons', 'Only functions during sleep'])
add(77,'Biology','Human Physiology - Nervous & Endocrine','Medium',
    'Growth hormone, secreted by the anterior pituitary gland, primarily promotes:',
    'Growth of bones and tissues, and regulation of metabolism',
    ['Suppression of protein synthesis', 'Immediate blood glucose reduction only', 'Water reabsorption in the kidneys'])
add(78,'Biology','Human Physiology - Nervous & Endocrine','Hard',
    "In a negative feedback loop regulating hormone levels, a rise in a hormone's concentration typically:",
    'Inhibits further release of that hormone, helping maintain homeostasis',
    ['Further stimulates its own release, creating a runaway increase', 'Has no effect on the gland that produced it', 'Only affects hormones from a different gland'])

add(79,'Biology','Human Physiology - Reproduction','Easy',
    'In males, sperm cells mature and are stored primarily in the:',
    'Epididymis', ['Seminiferous tubules', 'Prostate gland', 'Urethra'])
add(80,'Biology','Human Physiology - Reproduction','Medium',
    'During the menstrual cycle, a surge in luteinizing hormone (LH) directly triggers:',
    'Ovulation, the release of the mature egg from the ovary',
    ['Menstruation', 'Implantation', 'Formation of the placenta'])

add(81,'Biology','Ecology','Medium',
    'A keystone species is one that:',
    "Has a disproportionately large effect on its ecosystem's structure and stability relative to its abundance",
    ['Has the largest population size in its ecosystem', 'Is always a top predator', 'Has no significant ecological role'])

# ============================================================
# CHEMISTRY (45) - id 82-126
# ============================================================
add(82,'Chemistry','Atomic Structure','Easy',
    'The overall electrical charge of a neutral atom is:',
    'Zero, since protons and electrons balance', ['Positive', 'Negative', 'Always variable'])
add(83,'Chemistry','Atomic Structure','Medium',
    'An atom of carbon-14 (atomic number 6) contains how many neutrons?',
    '8', ['6', '14', '20'])
add(84,'Chemistry','Atomic Structure','Medium',
    'The electron configuration of a neutral aluminum atom (Z = 13) is:',
    '1s2 2s2 2p6 3s2 3p1', ['1s2 2s2 2p6 3s1', '1s2 2s2 2p6 3s2 3p2', '1s2 2s2 2p5'])
add(85,'Chemistry','Atomic Structure','Hard',
    'An ion formed from a neutral atom with 20 protons that has lost 2 electrons carries a charge of:',
    '+2', ['-2', '+1', '-1'])
add(126,'Chemistry','Atomic Structure','Easy',
    'Which of the following particles has a mass approximately 1836 times greater than that of an electron?',
    'Proton', ['Neutron', 'Positron', 'Photon'])

add(86,'Chemistry','Periodic Table','Easy',
    'The modern periodic table arranges elements primarily in order of increasing:',
    'Atomic number', ['Atomic mass only', 'Number of neutrons', 'Melting point'])
add(87,'Chemistry','Periodic Table','Medium',
    'Which trend correctly describes how metallic character changes across the periodic table?',
    'It decreases across a period left to right and increases down a group',
    ['It increases across a period left to right and decreases down a group', 'It remains constant throughout the table', 'It increases in both directions simultaneously'])
add(88,'Chemistry','Periodic Table','Medium',
    'An element with electron configuration [Xe]6s2 would most likely:',
    'Lose two electrons to form a +2 ion',
    ['Gain six electrons to form a -6 ion', 'Be chemically inert like a noble gas', 'Form only covalent bonds with metals'])

add(89,'Chemistry','Chemical Bonding','Easy',
    'Which type of bond is typically formed between two nonmetal atoms with similar electronegativities?',
    'Covalent bond', ['Ionic bond', 'Metallic bond', 'Hydrogen bond only'])
add(90,'Chemistry','Chemical Bonding','Medium',
    'According to VSEPR theory, a molecule such as PCl5, with five bonding pairs and no lone pairs on the central atom, has a molecular shape described as:',
    'Trigonal bipyramidal', ['Octahedral', 'Square planar', 'Tetrahedral'])
add(91,'Chemistry','Chemical Bonding','Medium',
    'CCl4 is a nonpolar molecule overall, despite having polar C-Cl bonds, mainly because:',
    'Its symmetrical tetrahedral geometry causes the four bond dipoles to cancel',
    ['Chlorine has no electronegativity', 'Carbon carries a lone pair balancing the dipoles', 'It contains no covalent bonds'])
add(92,'Chemistry','Chemical Bonding','Hard',
    'Sodium chloride (NaCl) has a high melting point mainly because:',
    'Strong electrostatic forces exist between oppositely charged ions throughout the crystal lattice',
    ['It consists of individual, weakly bonded molecules', 'It is held together by weak van der Waals forces only', 'It contains no charged particles'])
add(125,'Chemistry','Chemical Bonding','Easy',
    'The number of electron pairs shared in a triple covalent bond is:',
    'Three', ['One', 'Two', 'Four'])

add(93,'Chemistry','States of Matter','Easy',
    'Which of the following best describes the arrangement of particles in a liquid, compared to a gas and a solid?',
    'Particles are close together but can move past one another, unlike the fixed positions in a solid',
    ['Particles are tightly packed in a fixed, rigid arrangement, like a solid', 'Particles are far apart and move freely and randomly, like a gas', 'Particles do not move at all'])
add(94,'Chemistry','States of Matter','Medium',
    "A gas occupies 12.0 L at 3.0 atm. What volume will it occupy at 4.0 atm, assuming constant temperature (Boyle's Law)?",
    '9.0 L', ['16.0 L', '4.0 L', '36.0 L'])
add(95,'Chemistry','States of Matter','Hard',
    "A fixed mass of gas at 1 atm and 300 K is heated at constant volume until its pressure reaches 3 atm. What is the new temperature (Gay-Lussac's Law)?",
    '900 K', ['100 K', '300 K', '600 K'])

add(96,'Chemistry','Stoichiometry','Easy',
    'The molar mass of glucose (C6H12O6) is approximately:',
    '180 g/mol', ['90 g/mol', '120 g/mol', '342 g/mol'])
add(97,'Chemistry','Stoichiometry','Medium',
    'How many moles are present in 4.6 g of sodium (molar mass 23 g/mol)?',
    '0.2 mol', ['0.1 mol', '2 mol', '46 mol'])
add(98,'Chemistry','Stoichiometry','Hard',
    'A 250 mL solution contains 0.05 mole of glucose. What is the molarity of this solution?',
    '0.2 M', ['0.05 M', '0.125 M', '0.0125 M'])
add(99,'Chemistry','Stoichiometry','Medium',
    'In the balanced equation Fe2O3 + 3CO -> 2Fe + 3CO2, how many moles of Fe are produced from the complete reaction of 4 moles of Fe2O3 with excess CO?',
    '8', ['4', '2', '12'])

add(100,'Chemistry','Thermochemistry','Easy',
    'The energy required to start a chemical reaction, overcoming the initial energy barrier, is called the:',
    'Activation energy', ['Enthalpy of reaction', 'Free energy', 'Entropy'])
add(101,'Chemistry','Thermochemistry','Medium',
    'During an exothermic reaction, the total energy of the products compared to the reactants is:',
    'Lower than the reactants, with the difference released as heat',
    ['Higher than the reactants', 'Exactly equal to the reactants', 'Impossible to determine'])

add(102,'Chemistry','Chemical Equilibrium','Medium',
    'For the equilibrium CO(g) + H2O(g) <-> CO2(g) + H2(g), since the number of moles of gas is equal on both sides, changing the pressure by changing volume will:',
    'Have essentially no effect on the position of equilibrium',
    ['Strongly shift the equilibrium toward products', 'Strongly shift the equilibrium toward reactants', 'Stop the reaction completely'])
add(103,'Chemistry','Chemical Equilibrium','Hard',
    'Which of the following changes would increase the value of Keq for an exothermic reaction?',
    'Decreasing the temperature', ['Increasing the temperature', 'Adding a catalyst', 'Increasing the pressure'])

add(104,'Chemistry','Reaction Kinetics','Easy',
    'The collision theory of reaction rates states that for a reaction to occur, particles must collide with:',
    'Sufficient energy and proper orientation',
    ['Any amount of energy, regardless of orientation', 'Only proper orientation, energy is irrelevant', 'No energy at all'])
add(105,'Chemistry','Reaction Kinetics','Medium',
    "A reaction's rate law is given as rate = k[A]^2[B]. What is the overall order of this reaction?",
    '3', ['2', '1', '4'])

add(106,'Chemistry','Electrochemistry','Medium',
    'A salt bridge in a galvanic cell primarily functions to:',
    'Maintain electrical neutrality by allowing ion flow between the two half-cells',
    ['Generate the electric current', 'Prevent any reaction from occurring', "Increase the cell's voltage directly"])
add(107,'Chemistry','Electrochemistry','Hard',
    'In the reaction 2Ag+ + Cu -> 2Ag + Cu2+, silver ion (Ag+) gains electrons and is therefore the:',
    'Oxidizing agent', ['Reducing agent', 'Neither oxidized nor reduced', 'Catalyst'])

add(108,'Chemistry','Acids & Bases','Easy',
    'A solution with a pH of 9 is:',
    'Basic', ['Strongly acidic', 'Neutral', 'Not possible at 25°C'])
add(109,'Chemistry','Acids & Bases','Medium',
    'A solution has [OH-] = 1x10^-2 M. What is its pH (at 25°C)?',
    '12', ['2', '14', '7'])
add(110,'Chemistry','Acids & Bases','Medium',
    'The graph shows the pH curve for the titration of a strong acid (HCl) with a strong base (NaOH). Based on the shape of the curve, the pH at the equivalence point is expected to be:',
    'Exactly 7.0, since the resulting salt is neutral',
    ['Significantly less than 7', 'Significantly greater than 7', 'Negative'],
    image='images/q9_titration_strong_acid_strong_base.png')
add(111,'Chemistry','Acids & Bases','Hard',
    'Which of the following pairs would form an effective buffer solution?',
    'Acetic acid (CH3COOH) and sodium acetate (CH3COONa)',
    ['HCl and NaCl', 'NaOH and NaCl', 'HCl and NaOH in equal amounts'])

add(112,'Chemistry','Organic Chemistry','Easy',
    'A nitrile functional group contains a carbon atom:',
    'Triple-bonded to nitrogen', ['Singly bonded to nitrogen', 'Double-bonded to oxygen', 'Bonded to two oxygen atoms'])
add(113,'Chemistry','Organic Chemistry','Medium',
    'Alcohols are classified as primary, secondary, or tertiary based on:',
    'The number of carbon atoms directly bonded to the carbon bearing the -OH group',
    ['Their molecular weight', 'The number of oxygen atoms present', 'Whether they are liquids or solids'])
add(114,'Chemistry','Organic Chemistry','Medium',
    'Which functional group characterizes an amine?',
    '-NH2', ['-COOH', '-OH', '-CHO'])
add(115,'Chemistry','Organic Chemistry','Hard',
    'During an E2 elimination reaction, a strong base removes a proton while the leaving group departs simultaneously, resulting in:',
    'Formation of a new carbon-carbon double bond in a single concerted step',
    ['Formation of a carbocation intermediate', 'No structural change to the molecule', 'Addition of a new substituent to the molecule'])
add(116,'Chemistry','Organic Chemistry','Medium',
    'Hydrolysis of an ester in the presence of water and an acid catalyst produces:',
    'A carboxylic acid and an alcohol', ['A polymer', 'Only carbon dioxide and water', 'An amine and an alcohol'])
add(117,'Chemistry','Organic Chemistry','Easy',
    'Which of the following pairs represents positional isomers, differing only in the location of a functional group on the same carbon skeleton?',
    '1-propanol and 2-propanol',
    ['Ethanol and dimethyl ether', 'Butane and isobutane', 'Two enantiomers of the same molecule'])

add(118,'Chemistry','Inorganic Chemistry','Medium',
    'Which of the following best explains why transition metal ions often form complex ions with ligands?',
    'Transition metals have empty or partially filled d orbitals that can accept electron pairs from ligands',
    ['Transition metals have no available orbitals for bonding', 'Transition metals cannot form ionic bonds', 'Ligands are always negatively charged only'])
add(119,'Chemistry','Inorganic Chemistry','Medium',
    'Which of the following elements is classified as a metalloid, exhibiting properties intermediate between metals and nonmetals?',
    'Silicon', ['Sodium', 'Oxygen', 'Calcium'])
add(120,'Chemistry','Inorganic Chemistry','Hard',
    'In the reaction Cl2 + 2KBr -> 2KCl + Br2, chlorine is reduced while bromide ion (Br-) is:',
    'Oxidized, losing electrons to form Br2', ['Reduced', 'Unchanged', 'Acting as a catalyst'])

add(121,'Chemistry','Physical Chemistry','Medium',
    "Raoult's law describes the relationship between:",
    'The vapor pressure of a solution and the mole fraction of its components',
    ['The boiling point of a pure solvent and its molar mass', 'The rate of a chemical reaction and temperature', 'The pH of a solution and its concentration'])
add(122,'Chemistry','Physical Chemistry','Hard',
    '12.5 mL of 0.2 M NaOH is required to exactly neutralize 25 mL of HCl solution (NaOH + HCl -> NaCl + H2O). What is the molarity of the HCl solution?',
    '0.1 M', ['0.05 M', '0.2 M', '0.4 M'])

add(123,'Chemistry','Environmental Chemistry','Easy',
    "Which of the following best describes 'greenhouse gases'?",
    'Gases that trap heat in the atmosphere by absorbing and re-emitting infrared radiation',
    ['Gases that block all sunlight from reaching Earth', 'Gases found only in polluted urban areas', "Gases that have no effect on Earth's temperature"])
add(124,'Chemistry','Environmental Chemistry','Medium',
    'Photochemical smog, common in sunny urban areas with heavy traffic, forms primarily through reactions involving:',
    'Nitrogen oxides and volatile organic compounds reacting in the presence of sunlight',
    ['Carbon dioxide and water vapor only', 'Sulfur dioxide and rainwater alone', 'Ozone depletion in the stratosphere'])

# ============================================================
# PHYSICS (36) - id 127-162
# ============================================================
add(127,'Physics','Kinematics','Easy',
    "A swimmer covers 200 m in 40 seconds at constant velocity. What is the swimmer's speed?",
    '5 m/s', ['8 m/s', '160 m/s', '0.2 m/s'])
add(128,'Physics','Kinematics','Medium',
    'A motorcycle accelerates uniformly from 5 m/s to 25 m/s over 5 seconds. What is its acceleration?',
    '4 m/s^2', ['5 m/s^2', '6 m/s^2', '1 m/s^2'])
add(129,'Physics','Kinematics','Hard',
    'A ball is dropped from rest and falls for 5 seconds before hitting the ground (g = 10 m/s^2, ignoring air resistance). From what height was it dropped?',
    '125 m', ['50 m', '100 m', '250 m'])

add(130,'Physics','Dynamics','Easy',
    'The SI unit of force is the:',
    'Newton', ['Joule', 'Watt', 'Pascal'])
add(131,'Physics','Dynamics','Medium',
    'A 4 kg object accelerates at 3.5 m/s^2 due to an applied net force. What is the magnitude of this force?',
    '14 N', ['1.14 N', '7.5 N', '0.875 N'])
add(132,'Physics','Dynamics','Medium',
    'If the net force acting on a moving object is zero, the object will:',
    'Continue moving at constant velocity',
    ['Immediately come to rest', 'Accelerate uniformly', 'Reverse its direction of motion'])
add(133,'Physics','Dynamics','Hard',
    "A 8 kg block is pushed horizontally with a 36 N force across a surface with a coefficient of kinetic friction of 0.25 (g = 10 m/s^2). What is the block's acceleration?",
    '2 m/s^2', ['1.5 m/s^2', '4.5 m/s^2', '0.5 m/s^2'])

add(134,'Physics','Work, Energy & Power','Easy',
    'When a force is applied to an object and causes it to move in the same direction as the force, the work done is considered:',
    'Positive', ['Zero', 'Negative', 'Undefined'])
add(135,'Physics','Work, Energy & Power','Medium',
    'A 10 kg object is raised to a height of 4 m (g = 10 m/s^2). What is its gravitational potential energy at that height?',
    '400 J', ['40 J', '100 J', '250 J'])
add(136,'Physics','Work, Energy & Power','Medium',
    'A 5 kg object moving at 6 m/s has a kinetic energy of:',
    '90 J', ['30 J', '150 J', '15 J'])
add(137,'Physics','Work, Energy & Power','Hard',
    'A crane lifts a 300 kg load to a height of 20 m in 15 seconds (g = 10 m/s^2). What is the power output of the crane?',
    '4000 W', ['400 W', '60000 W', '6000 W'])

add(138,'Physics','Circular Motion & Gravitation','Easy',
    'An object moving in a circle at constant speed has an acceleration that is:',
    'Directed toward the center of the circle',
    ['Zero, since speed is constant', 'Directed away from the center of the circle', 'Directed tangentially, in the direction of motion'])
add(139,'Physics','Circular Motion & Gravitation','Medium',
    'If the mass of one object is halved while the distance between two objects stays the same, the gravitational force between them becomes:',
    'Half as large', ['Twice as large', 'Four times as large', 'Unchanged'])
add(140,'Physics','Circular Motion & Gravitation','Hard',
    "The escape velocity needed for an object to break free of a planet's gravitational pull depends on:",
    "The planet's mass and radius", ["The object's own mass only", "The object's color", "The object's temperature"])

add(141,'Physics','Fluid Mechanics','Easy',
    'Density is defined as:',
    'Mass per unit volume', ['Weight per unit area', 'Volume per unit mass', 'Force per unit area'])
add(142,'Physics','Fluid Mechanics','Medium',
    'A block of wood floats in water with part of it above the surface mainly because:',
    "Wood is less dense than water, so it displaces a volume of water whose weight equals the wood's weight before being fully submerged",
    ['Wood has zero density', 'Water has no buoyant force', 'The block has no weight'])
add(143,'Physics','Fluid Mechanics','Hard',
    "According to the continuity equation for an incompressible fluid, if a pipe narrows to half its original cross-sectional area, the fluid's speed at the narrow section will:",
    'Double', ['Halve', 'Remain the same', 'Quadruple'])

add(144,'Physics','Oscillations & Waves','Easy',
    "A wave's frequency is measured in units of:",
    'Hertz', ['Meters', 'Seconds', 'Newtons'])
add(145,'Physics','Oscillations & Waves','Medium',
    'For a mass-spring system undergoing simple harmonic motion, increasing the spring constant (making the spring stiffer), while keeping the mass constant, will:',
    'Decrease the period of oscillation',
    ['Increase the period of oscillation', 'Have no effect on the period', 'Stop the oscillation entirely'])
add(146,'Physics','Oscillations & Waves','Medium',
    'A wave has a period of 0.005 seconds. What is its frequency?',
    '200 Hz', ['5 Hz', '50 Hz', '2000 Hz'])
add(147,'Physics','Oscillations & Waves','Hard',
    'Standing waves are formed when two waves of the same frequency and amplitude travel:',
    'In opposite directions and interfere, creating fixed nodes and antinodes',
    ['In the same direction only', 'Through completely different media simultaneously', 'With no interference at all'])

add(148,'Physics','Thermodynamics','Easy',
    'Which of the following best describes an isolated system in thermodynamics?',
    'It exchanges neither matter nor energy with its surroundings',
    ['It exchanges both matter and energy with its surroundings', 'It exchanges only matter, not energy', 'It exchanges only energy, not matter'])
add(149,'Physics','Thermodynamics','Medium',
    'During a phase change, such as ice melting into water at 0°C, the temperature of the substance:',
    'Remains constant, as the added heat is used to break intermolecular bonds rather than raise temperature',
    ['Increases steadily', 'Decreases', 'Rises to the boiling point immediately'])
add(150,'Physics','Thermodynamics','Hard',
    'A gas undergoes a process at constant volume, absorbing 400 J of heat. Since no work is done (constant volume), the change in internal energy is:',
    '400 J', ['0 J', '-400 J', '800 J'])

add(151,'Physics','Electrostatics','Easy',
    'Electric potential difference (voltage) between two points is measured in units of:',
    'Volts', ['Amperes', 'Ohms', 'Coulombs'])
add(152,'Physics','Electrostatics','Medium',
    'The electric field between two oppositely charged parallel plates is:',
    'Uniform in strength and direction between the plates',
    ['Zero everywhere', 'Strongest at the edges only', 'Directed randomly'])

add(153,'Physics','Current Electricity','Easy',
    'In a series circuit, the current flowing through each component is:',
    'The same throughout the circuit', ['Different at each point', 'Always zero', 'Dependent only on voltage'])
add(154,'Physics','Current Electricity','Medium',
    'In the circuit shown, R1 (10 ohm) and R2 (15 ohm) are connected in parallel, and this parallel combination is connected in series with R3 (2 ohm). What is the total resistance of the circuit?',
    '8 ohm', ['6 ohm', '27 ohm', '10 ohm'],
    image='images/q9_circuit_diagram_r1r2r3.png')
add(155,'Physics','Current Electricity','Hard',
    'Three resistors of 4 ohm, 4 ohm, and 4 ohm are connected in parallel. What is their equivalent resistance?',
    '1.33 ohm', ['12 ohm', '4 ohm', '8 ohm'])
add(156,'Physics','Current Electricity','Medium',
    'A circuit has a resistance of 25 ohm and carries a current of 4 A. What is the voltage across it?',
    '100 V', ['6.25 V', '29 V', '21 V'])

add(157,'Physics','Electromagnetism','Medium',
    'A transformer works on the principle of:',
    'Electromagnetic induction, using a changing magnetic field to induce voltage in a secondary coil',
    ['Direct current flow only', 'Static electricity', 'Nuclear reactions'])
add(158,'Physics','Electromagnetism','Hard',
    'Increasing the speed at which a magnet is moved through a coil of wire will:',
    'Increase the induced EMF, since flux changes more rapidly',
    ['Decrease the induced EMF', 'Have no effect on the induced EMF', 'Reverse the polarity only, without changing magnitude'])

add(159,'Physics','Modern Physics','Easy',
    'The phenomenon in which electrons are emitted from a metal surface when light of sufficient frequency strikes it is called:',
    'The photoelectric effect', ['Nuclear fission', 'Radioactive decay', 'Electromagnetic induction'])
add(160,'Physics','Modern Physics','Medium',
    'Nuclear fusion, the process that powers the Sun, involves:',
    'The combining of light nuclei into a heavier nucleus, releasing energy',
    ['The splitting of heavy nuclei into lighter ones', 'No change in nuclear composition', 'The emission of a single photon only'])
add(161,'Physics','Modern Physics','Hard',
    'A radioactive sample initially contains 240 g of a substance with a half-life of 6 hours. How much of the substance remains after 18 hours?',
    '30 g', ['120 g', '60 g', '15 g'])

add(162,'Physics','Optics','Medium',
    'The ray diagram shows an object placed in front of a convex (diverging) mirror. Based on the diagram, the image formed behind the mirror is:',
    'Virtual, upright, and diminished',
    ['Real, inverted, and magnified', 'Real, upright, and the same size', 'Virtual, inverted, and magnified'],
    image='images/q9_convex_mirror_diagram.png')

# ============================================================
# ENGLISH (9) - id 163-171
# ============================================================
add(163,'English','Synonyms','Easy',
    "Choose the word most nearly similar in meaning to 'ELOQUENT':",
    'Articulate', ['Clumsy', 'Silent', 'Confusing'])
add(164,'English','Antonyms','Easy',
    "Choose the word most nearly opposite in meaning to 'GENUINE':",
    'Fake', ['Authentic', 'Sincere', 'Real'])
add(165,'English','Grammar','Easy',
    'Choose the grammatically correct sentence:',
    'They were going to the market.',
    ['They was going to the market.', 'They is going to the market.', 'They be going to the market.'])
add(166,'English','Grammar','Medium',
    'Choose the correct sentence:',
    'She has gone to the store already.',
    ['She has went to the store already.', 'She have gone to the store already.', "She had went to the store already, hasn't she."])
add(167,'English','Sentence Correction','Medium',
    'Identify the sentence that follows correct subject-verb agreement:',
    'A number of students were absent today.',
    ['A number of students was absent today.', 'The number of student were absent today.', 'A number of student was absent today.'])
add(168,'English','Vocabulary','Medium',
    "Choose the word that best completes the sentence: 'The manager's ______ approach to leadership earned the trust and respect of the entire team.'",
    'Collaborative', ['Autocratic', 'Dismissive', 'Erratic'])
add(169,'English','Idioms','Medium',
    "Choose the meaning closest to the idiom 'to spill the beans':",
    'To reveal a secret, often unintentionally',
    ['To make a mess', 'To argue loudly', 'To finish a meal quickly'])
add(170,'English','Sentence Correction','Hard',
    "Choose the option that best corrects the sentence: 'Each of the applicants have to submit their resume by Monday.'",
    'Each of the applicants has to submit his or her resume by Monday.',
    ['Each of the applicants have to submit his resume by Monday.', 'Each of the applicant has to submit their resumes by Monday.', 'Each of the applicants has to submit their resumes by Monday.'])
add(171,'English','Prepositions','Hard',
    "Choose the correct preposition to complete the sentence: 'The students were divided ______ four separate groups for the project.'",
    'into', ['in', 'at', 'with'])

# ============================================================
# LOGICAL REASONING (9) - id 172-180
# ============================================================
add(172,'Logical Reasoning','Number Series','Easy',
    'Find the next number in the series: 4, 9, 19, 39, ?',
    '79', ['59', '69', '89'])
add(173,'Logical Reasoning','Number Series','Easy',
    'Find the missing number: 81, 27, 9, 3, ?',
    '1', ['0', '2', '-1'])
add(174,'Logical Reasoning','Analogies','Easy',
    'Hammer is to Nail as Screwdriver is to:',
    'Screw', ['Wood', 'Toolbox', 'Drill'])
add(175,'Logical Reasoning','Analogies','Medium',
    'Author is to Novel as Composer is to:',
    'Symphony', ['Instrument', 'Orchestra', 'Concert Hall'])
add(176,'Logical Reasoning','Blood Relations','Medium',
    "Pointing to a photograph, Amna said, 'This boy's father is my father's son, but I have no brothers.' How is the boy related to Amna?",
    'Son', ['Nephew', 'Brother', 'Cousin'])
add(177,'Logical Reasoning','Coding-Decoding','Medium',
    'If in a certain code, FLOWER is written as GMPXFS, how is GARDEN written in the same code?',
    'HBSEFO', ['HBSEFP', 'HBSDEO', 'IBSEFO'])
add(178,'Logical Reasoning','Syllogism','Hard',
    'All birds can fly. Penguins are birds. Which conclusion, if the first premise is taken as strictly true, logically follows?',
    'Penguins can fly', ['Penguins cannot fly', 'Some birds are not penguins', 'No conclusion is possible'])
add(179,'Logical Reasoning','Pattern Recognition','Hard',
    'Find the next term in the series: 5, 10, 20, 35, 55, ?',
    '80', ['70', '75', '85'])
add(180,'Logical Reasoning','Direction Sense','Medium',
    'A boy walks 10 km north, then turns east and walks 24 km. How far is he from his starting point?',
    '26 km', ['34 km', '14 km', '24 km'])

# ============================================================
# Assign balanced option letters (shuffled, no long runs) and
# build final QUESTIONS list
# ============================================================
random.seed(4471)

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

with open("mock9_data.json", "w") as f:
    json.dump(QUESTIONS, f, indent=2)

print("\nOK - all checks passed. Data written to mock9_data.json")