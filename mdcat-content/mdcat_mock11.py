"""
MDCAT Mock Test 11
==================
Full-length mock test: 180 MCQs
Weightage: Biology 81 | Chemistry 45 | Physics 36 | English 9 | Logical Reasoning 9
Difficulty mix (approx): 30% Easy / 50% Medium / 20% Hard, distributed throughout.

Includes 5 image/diagram-based questions (2 Biology, 1 Chemistry, 2 Physics).
Each such question has an "image" key giving a relative path to a PNG diagram
that must be viewed alongside the question (images/ subfolder, shipped alongside
this file). Diagrams: a cell caught in metaphase of mitosis, a labeled nephron
cross-section, a solid/liquid/gas phase diagram showing the triple point, a
parallel-then-series resistor circuit, and a concave-mirror ray diagram (object
beyond C).

Each question is a dict:
    id, subject, topic, difficulty, question, [image], options (A-D), answer (correct letter)

Run this file directly to print a summary / sanity-check the paper.
"""

QUESTIONS = [

# ============================================================
# BIOLOGY (81) - id 1-81
# ============================================================

{"id":1,"subject":'Biology',"topic":'Biomolecules',"difficulty":'Easy',
 "question":'Which of the following is a polymer of amino acids?',
 "options":{"A":'Protein', "B":'Starch', "C":'Cellulose', "D":'DNA'},"answer":'A'},

{"id":2,"subject":'Biology',"topic":'Biomolecules',"difficulty":'Easy',
 "question":'The building blocks of nucleic acids are:',
 "options":{"A":'Nucleotides', "B":'Amino acids', "C":'Monosaccharides', "D":'Fatty acids'},"answer":'A'},

{"id":3,"subject":'Biology',"topic":'Biomolecules',"difficulty":'Medium',
 "question":'Denatured proteins lose their biological function mainly because:',
 "options":{"A":'Their primary amino acid sequence changes', "B":'They gain additional amino acids', "C":'Their three-dimensional shape is disrupted, even though the amino acid sequence stays the same', "D":'They convert into carbohydrates'},"answer":'C'},

{"id":4,"subject":'Biology',"topic":'Biomolecules',"difficulty":'Medium',
 "question":'A wax, commonly found on leaf surfaces and animal fur, is chemically similar to a triglyceride but differs in that a wax:',
 "options":{"A":'Contains glycerol esterified with three fatty acids', "B":'Is a type of carbohydrate', "C":'Is made entirely of amino acids', "D":'Consists of a long-chain fatty acid esterified with a long-chain alcohol, not glycerol'},"answer":'D'},

{"id":5,"subject":'Biology',"topic":'Biomolecules',"difficulty":'Hard',
 "question":'A single strand of DNA and a single strand of RNA could theoretically base-pair with each other (as in a DNA-RNA hybrid) because:',
 "options":{"A":'Both use complementary base pairing rules, with adenine pairing to uracil (in RNA) as it would to thymine (in DNA)', "B":'They share no common bases', "C":'RNA has no nitrogenous bases', "D":'DNA and RNA never interact directly'},"answer":'A'},

{"id":6,"subject":'Biology',"topic":'Enzymes',"difficulty":'Easy',
 "question":'Enzymes are typically named by adding which suffix to the name of their substrate or the reaction they catalyze?',
 "options":{"A":'-ose', "B":'-ase', "C":'-ide', "D":'-ol'},"answer":'B'},

{"id":7,"subject":'Biology',"topic":'Enzymes',"difficulty":'Medium',
 "question":"An enzyme's active site is highly specific to its substrate mainly due to:",
 "options":{"A":'Random chance', "B":'The enzyme constantly changing its amino acid sequence', "C":'The precise three-dimensional shape and chemical properties of the active site, which complement the substrate', "D":'All enzymes having identical active sites'},"answer":'C'},

{"id":8,"subject":'Biology',"topic":'Enzymes',"difficulty":'Medium',
 "question":'A vitamin-derived organic molecule that binds loosely to an enzyme and assists in catalysis is called a:',
 "options":{"A":'Prosthetic group', "B":'Holoenzyme', "C":'Apoenzyme', "D":'Coenzyme'},"answer":'D'},

{"id":9,"subject":'Biology',"topic":'Enzymes',"difficulty":'Hard',
 "question":"If an enzyme's Vmax remains unchanged but its apparent Km increases in the presence of an inhibitor, this is characteristic of:",
 "options":{"A":'Competitive inhibition', "B":'Non-competitive inhibition', "C":'Irreversible inhibition', "D":'No inhibition at all'},"answer":'A'},

{"id":10,"subject":'Biology',"topic":'Cell Biology',"difficulty":'Easy',
 "question":'The jelly-like fluid found inside the nucleus, surrounding the chromatin, is called:',
 "options":{"A":'Cytoplasm', "B":'Nucleoplasm', "C":'Cytosol', "D":'Matrix'},"answer":'B'},

{"id":11,"subject":'Biology',"topic":'Cell Biology',"difficulty":'Easy',
 "question":'Which structure is responsible for photosynthesis in plant cells?',
 "options":{"A":'Mitochondrion', "B":'Golgi apparatus', "C":'Chloroplast', "D":'Vacuole'},"answer":'C'},

{"id":12,"subject":'Biology',"topic":'Cell Biology',"difficulty":'Medium',
 "question":'The primary function of the rough endoplasmic reticulum is to:',
 "options":{"A":'Synthesize lipids', "B":'Generate ATP', "C":'Store water and ions', "D":'Synthesize and process proteins destined for secretion or membranes, using attached ribosomes'},"answer":'D'},

{"id":13,"subject":'Biology',"topic":'Cell Biology',"difficulty":'Medium',
 "question":'Centrosomes, containing a pair of centrioles in animal cells, primarily function to:',
 "options":{"A":'Organize microtubules and form the mitotic spindle during cell division', "B":'Store genetic information', "C":'Digest cellular waste', "D":'Produce lipids'},"answer":'A'},

{"id":14,"subject":'Biology',"topic":'Cell Biology',"difficulty":'Medium',
 "question":"The plasma membrane's phospholipid bilayer is described as 'fluid' mainly because:",
 "options":{"A":'Phospholipids are rigidly fixed in place', "B":'Individual phospholipid molecules can move laterally within their layer', "C":'The membrane is composed entirely of water', "D":'Phospholipids dissolve completely in the cytoplasm'},"answer":'B'},

{"id":15,"subject":'Biology',"topic":'Cell Biology',"difficulty":'Medium',
 "question":'Which of the following is a key structural difference between plant and animal cells?',
 "options":{"A":'Only animal cells have mitochondria', "B":'Only plant cells have ribosomes', "C":'Plant cells have a cell wall and typically a large central vacuole, which animal cells generally lack', "D":'Animal cells have chloroplasts while plant cells do not'},"answer":'C'},

{"id":16,"subject":'Biology',"topic":'Cell Biology',"difficulty":'Hard',
 "question":'A cell with a mutation preventing the Golgi apparatus from properly modifying proteins would most likely show defects in:',
 "options":{"A":'DNA replication', "B":'Transcription of genes', "C":'ATP synthesis', "D":'Protein glycosylation and proper sorting to their final destinations'},"answer":'D'},

{"id":17,"subject":'Biology',"topic":'Cell Membrane & Transport',"difficulty":'Easy',
 "question":'The movement of ions such as Na+ or K+ across a membrane against their concentration gradient, requiring ATP, is called:',
 "options":{"A":'Active transport', "B":'Diffusion', "C":'Osmosis', "D":'Facilitated diffusion'},"answer":'A'},

{"id":18,"subject":'Biology',"topic":'Cell Membrane & Transport',"difficulty":'Medium',
 "question":'A cell that is turgid (firm and swollen with water) is most likely a plant cell placed in a:',
 "options":{"A":'Hypertonic solution', "B":'Hypotonic solution', "C":'Isotonic solution', "D":'Solution with no water at all'},"answer":'B'},

{"id":19,"subject":'Biology',"topic":'Cell Membrane & Transport',"difficulty":'Medium',
 "question":'Exocytosis and endocytosis both require energy mainly because they involve:',
 "options":{"A":'Passive diffusion of ions', "B":'Osmosis alone', "C":'Vesicle formation and fusion with the plasma membrane, processes that require ATP', "D":'No cellular structures at all'},"answer":'C'},

{"id":20,"subject":'Biology',"topic":'Cell Membrane & Transport',"difficulty":'Hard',
 "question":'The rate of simple diffusion across a membrane is affected by all of the following EXCEPT:',
 "options":{"A":'The steepness of the concentration gradient', "B":'The temperature of the system', "C":'The surface area of the membrane', "D":'The presence of ATP, since simple diffusion does not require it'},"answer":'D'},

{"id":21,"subject":'Biology',"topic":'Cell Membrane & Transport',"difficulty":'Easy',
 "question":'Which of the following best describes osmosis?',
 "options":{"A":'The movement of water across a selectively permeable membrane from high to low water potential', "B":'The movement of solute particles across a membrane', "C":'The active transport of water using ATP', "D":'The engulfment of large particles by a cell'},"answer":'A'},

{"id":22,"subject":'Biology',"topic":'Cell Cycle & Division',"difficulty":'Easy',
 "question":'The cell cycle phase in which a cell prepares for division by synthesizing proteins and organelles, before DNA replication, is:',
 "options":{"A":'S phase', "B":'G1 phase', "C":'G2 phase', "D":'M phase'},"answer":'B'},

{"id":23,"subject":'Biology',"topic":'Cell Cycle & Division',"difficulty":'Easy',
 "question":'The diagram shows a dividing cell with chromosomes aligned singly along the center of the cell, attached to spindle fibers from both poles. Which phase of mitosis is shown?',
 "image":'images/q_mitosis_metaphase_stage.png',
 "options":{"A":'Prophase', "B":'Anaphase', "C":'Metaphase', "D":'Telophase'},"answer":'C'},

{"id":24,"subject":'Biology',"topic":'Cell Cycle & Division',"difficulty":'Medium',
 "question":'The primary purpose of crossing over during meiosis I is to:',
 "options":{"A":'Reduce chromosome number', "B":'Duplicate chromosomes exactly', "C":'Prevent any genetic variation', "D":'Generate new combinations of alleles on homologous chromosomes, increasing genetic variation'},"answer":'D'},

{"id":25,"subject":'Biology',"topic":'Cell Cycle & Division',"difficulty":'Medium',
 "question":'A cell with a diploid chromosome number of 2n = 46 completes meiosis I. How many chromosomes are present in each resulting cell at this point?',
 "options":{"A":'23, each consisting of two sister chromatids', "B":'46, each consisting of two sister chromatids', "C":'46, each consisting of a single chromatid', "D":'92, each consisting of one chromatid'},"answer":'A'},

{"id":26,"subject":'Biology',"topic":'Cell Cycle & Division',"difficulty":'Hard',
 "question":'Mitotic cell division in a multicellular organism is tightly regulated mainly to:',
 "options":{"A":'Ensure random, uncontrolled growth', "B":'Maintain proper tissue growth and repair, and prevent conditions such as cancer', "C":'Prevent any cell division from occurring', "D":'Only occur during embryonic development'},"answer":'B'},

{"id":27,"subject":'Biology',"topic":'Cell Cycle & Division',"difficulty":'Medium',
 "question":'A cell that fails to properly complete cytokinesis after mitosis would most likely result in:',
 "options":{"A":'Two normal daughter cells', "B":'Complete destruction of the cell', "C":'A single cell with two nuclei (a binucleate cell)', "D":'No effect at all'},"answer":'C'},

{"id":28,"subject":'Biology',"topic":'Genetics',"difficulty":'Easy',
 "question":'In pea plants, tall stem height (T) is dominant over short (t). A cross between two true-breeding tall plants (TT x TT) will produce offspring that are:',
 "options":{"A":'1 tall : 1 short', "B":'All short', "C":'3 tall : 1 short', "D":'All tall'},"answer":'D'},

{"id":29,"subject":'Biology',"topic":'Genetics',"difficulty":'Medium',
 "question":'A heterozygous tall pea plant (Tt) is crossed with a short pea plant (tt). What proportion of offspring is expected to be tall?',
 "options":{"A":'50%', "B":'75%', "C":'100%', "D":'25%'},"answer":'A'},

{"id":30,"subject":'Biology',"topic":'Genetics',"difficulty":'Medium',
 "question":"A particular disorder is inherited in an autosomal recessive pattern. Two unaffected parents, both carriers, have an affected child. What is the genotype of the affected child, using 'a' for the recessive allele?",
 "options":{"A":'Aa', "B":'aa', "C":'AA', "D":'Cannot be determined'},"answer":'B'},

{"id":31,"subject":'Biology',"topic":'Genetics',"difficulty":'Hard',
 "question":'In a trihybrid cross AaBbCc x AaBbCc, what fraction of offspring is expected to show the dominant phenotype for all three traits?',
 "options":{"A":'1/64', "B":'9/64', "C":'27/64', "D":'1/8'},"answer":'C'},

{"id":32,"subject":'Biology',"topic":'Genetics',"difficulty":'Medium',
 "question":'A woman with blood type AB and a man with blood type O have children. What blood types are possible among their offspring?',
 "options":{"A":'AB and O only', "B":'Only O', "C":'A, B, and AB', "D":'A and B only'},"answer":'D'},

{"id":33,"subject":'Biology',"topic":'Genetics',"difficulty":'Hard',
 "question":'A certain disorder appears only in individuals who inherit the recessive allele from both an affected father and an unaffected carrier mother, and is seen equally in males and females across generations, sometimes skipping a generation entirely. This is most consistent with:',
 "options":{"A":'Autosomal recessive inheritance', "B":'X-linked dominant inheritance', "C":'Y-linked inheritance', "D":'Autosomal dominant inheritance'},"answer":'A'},

{"id":34,"subject":'Biology',"topic":'Genetics',"difficulty":'Medium',
 "question":"In a certain species of chicken, crossing a black-feathered bird with a white-feathered bird produces offspring with a blue-gray, or 'andalusian', feather color, an intermediate blend. This is an example of:",
 "options":{"A":'Codominance', "B":'Incomplete dominance', "C":'Epistasis', "D":'Pleiotropy'},"answer":'B'},

{"id":35,"subject":'Biology',"topic":'Molecular Biology',"difficulty":'Easy',
 "question":"A DNA molecule's two strands are held together primarily by:",
 "options":{"A":'Covalent bonds between bases', "B":'Ionic bonds between sugars', "C":'Hydrogen bonds between complementary base pairs', "D":'Peptide bonds'},"answer":'C'},

{"id":36,"subject":'Biology',"topic":'Molecular Biology',"difficulty":'Easy',
 "question":'The enzyme responsible for synthesizing new DNA strands during replication is:',
 "options":{"A":'RNA polymerase', "B":'Ligase', "C":'Helicase', "D":'DNA polymerase'},"answer":'D'},

{"id":37,"subject":'Biology',"topic":'Molecular Biology',"difficulty":'Medium',
 "question":'The origin of replication is best described as:',
 "options":{"A":'A specific sequence on the DNA molecule where replication begins', "B":'The point where DNA replication ends', "C":'A protein that synthesizes RNA primers', "D":'The location where proteins are translated'},"answer":'A'},

{"id":38,"subject":'Biology',"topic":'Molecular Biology',"difficulty":'Medium',
 "question":'During translation, the ribosome moves along the mRNA, reading codons and forming a growing polypeptide chain until it encounters a:',
 "options":{"A":'Start codon', "B":'Stop codon', "C":'Promoter sequence', "D":'TATA box'},"answer":'B'},

{"id":39,"subject":'Biology',"topic":'Molecular Biology',"difficulty":'Medium',
 "question":"A mutation resulting from the insertion of three additional nucleotides (a multiple of three) into a gene's coding sequence would most likely:",
 "options":{"A":'Cause a complete frameshift, altering the entire downstream protein', "B":'Have no effect whatsoever on the DNA', "C":'Add one additional amino acid to the protein without shifting the reading frame', "D":'Immediately terminate translation'},"answer":'C'},

{"id":40,"subject":'Biology',"topic":'Molecular Biology',"difficulty":'Hard',
 "question":'Which of the following best describes the difference between a gene and an allele?',
 "options":{"A":'A gene and an allele are identical terms', "B":'A gene exists only in prokaryotes', "C":'An allele is always dominant, while a gene is always recessive', "D":'A gene is a segment of DNA coding for a trait, while an allele is one of the possible variant forms of that gene'},"answer":'D'},

{"id":41,"subject":'Biology',"topic":'Molecular Biology',"difficulty":'Hard',
 "question":'The process by which some bacteria take up free DNA fragments from their environment and incorporate them into their genome is called:',
 "options":{"A":'Transformation', "B":'Conjugation', "C":'Transduction', "D":'Replication'},"answer":'A'},

{"id":42,"subject":'Biology',"topic":'Molecular Biology',"difficulty":'Medium',
 "question":'Which of the following enzymes is responsible for unwinding the DNA double helix ahead of the replication fork?',
 "options":{"A":'DNA polymerase', "B":'Helicase', "C":'Ligase', "D":'Primase'},"answer":'B'},

{"id":43,"subject":'Biology',"topic":'Molecular Biology',"difficulty":'Medium',
 "question":'A gene expressed only in certain cell types (e.g., insulin only in pancreatic beta cells), despite being present in the DNA of nearly all body cells, illustrates the concept of:',
 "options":{"A":'Gene mutation', "B":'Chromosomal deletion', "C":'Differential (selective) gene expression', "D":'Random gene loss'},"answer":'C'},

{"id":44,"subject":'Biology',"topic":'Molecular Biology',"difficulty":'Easy',
 "question":'The complete set of genetic material within an organism is referred to as its:',
 "options":{"A":'Phenotype', "B":'Karyotype', "C":'Proteome', "D":'Genome'},"answer":'D'},

{"id":45,"subject":'Biology',"topic":'Evolution',"difficulty":'Easy',
 "question":'The process by which better-adapted individuals are more likely to survive and reproduce, passing on their advantageous traits, is called:',
 "options":{"A":'Natural selection', "B":'Genetic drift', "C":'Gene flow', "D":'Mutation'},"answer":'A'},

{"id":46,"subject":'Biology',"topic":'Evolution',"difficulty":'Medium',
 "question":'Divergent evolution occurs when:',
 "options":{"A":'Two unrelated species independently evolve similar traits', "B":'A single ancestral species evolves into two or more distinct species, adapted to different environments', "C":'Two species merge into one', "D":'A species remains completely unchanged over time'},"answer":'B'},

{"id":47,"subject":'Biology',"topic":'Evolution',"difficulty":'Medium',
 "question":'Gene flow between two populations tends to:',
 "options":{"A":'Increase genetic differences between the populations', "B":"Have no effect on either population's gene pool", "C":'Decrease genetic differences between the populations by mixing their gene pools', "D":'Cause immediate speciation'},"answer":'C'},

{"id":48,"subject":'Biology',"topic":'Evolution',"difficulty":'Hard',
 "question":'In a population at Hardy-Weinberg equilibrium, 640 out of 1000 individuals show the dominant phenotype for a trait with two alleles. What is the frequency of the recessive allele?',
 "options":{"A":'0.36', "B":'0.64', "C":'0.4', "D":'0.6'},"answer":'D'},

{"id":49,"subject":'Biology',"topic":'Classification & Diversity',"difficulty":'Easy',
 "question":'The correct order of taxonomic ranks, from broadest to most specific, is:',
 "options":{"A":'Kingdom, Phylum, Class, Order, Family, Genus, Species', "B":'Species, Genus, Family, Order, Class, Phylum, Kingdom', "C":'Phylum, Kingdom, Class, Family, Order, Genus, Species', "D":'Genus, Species, Family, Order, Class, Phylum, Kingdom'},"answer":'A'},

{"id":50,"subject":'Biology',"topic":'Classification & Diversity',"difficulty":'Easy',
 "question":'Members of kingdom Monera (bacteria and archaea in older classification systems) are unified by being:',
 "options":{"A":'Multicellular eukaryotes', "B":'Unicellular prokaryotes lacking a membrane-bound nucleus', "C":'Photosynthetic organisms only', "D":'Always harmful to humans'},"answer":'B'},

{"id":51,"subject":'Biology',"topic":'Classification & Diversity',"difficulty":'Medium',
 "question":'A biologist discovers a new unicellular organism with a membrane-bound nucleus that is not classified as a plant, animal, or fungus. This organism would most likely be placed in kingdom:',
 "options":{"A":'Monera', "B":'Plantae', "C":'Protista', "D":'Fungi'},"answer":'C'},

{"id":52,"subject":'Biology',"topic":'Classification & Diversity',"difficulty":'Medium',
 "question":'Which characteristic distinguishes phylum Platyhelminthes (flatworms) from phylum Nematoda (roundworms)?',
 "options":{"A":'Flatworms have jointed appendages', "B":'Flatworms are always parasitic while roundworms never are', "C":'Roundworms lack any digestive system', "D":'Flatworms have a flattened, unsegmented body and no true body cavity, while roundworms have a cylindrical body with a pseudocoelom'},"answer":'D'},

{"id":53,"subject":'Biology',"topic":'Classification & Diversity',"difficulty":'Easy',
 "question":'Which taxonomic rank is more specific than Order but broader than Genus?',
 "options":{"A":'Family', "B":'Class', "C":'Phylum', "D":'Kingdom'},"answer":'A'},

{"id":54,"subject":'Biology',"topic":'Classification & Diversity',"difficulty":'Medium',
 "question":'The class of vertebrates characterized by having feathers, a four-chambered heart, and being endothermic (warm-blooded) is:',
 "options":{"A":'Reptilia', "B":'Aves', "C":'Amphibia', "D":'Mammalia'},"answer":'B'},

{"id":55,"subject":'Biology',"topic":'Plant Biology',"difficulty":'Easy',
 "question":'The tiny pores on the surface of a leaf, mainly on the underside, through which gas exchange occurs, are called:',
 "options":{"A":'Lenticels', "B":'Trichomes', "C":'Stomata', "D":'Cuticles'},"answer":'C'},

{"id":56,"subject":'Biology',"topic":'Plant Biology',"difficulty":'Medium',
 "question":'In the Calvin cycle, ATP and NADPH generated during the light reactions are used mainly to:',
 "options":{"A":'Split water molecules', "B":'Transport electrons through the electron transport chain', "C":'Directly produce oxygen gas', "D":'Reduce fixed carbon dioxide into glyceraldehyde-3-phosphate (G3P), which can form glucose'},"answer":'D'},

{"id":57,"subject":'Biology',"topic":'Plant Biology',"difficulty":'Medium',
 "question":'The waxy layer covering the outer surface of leaves and stems, which helps prevent excessive water loss, is called the:',
 "options":{"A":'Cuticle', "B":'Epidermis', "C":'Cortex', "D":'Mesophyll'},"answer":'A'},

{"id":58,"subject":'Biology',"topic":'Plant Biology',"difficulty":'Hard',
 "question":'A plant grown in low-light conditions typically develops taller stems and larger, thinner leaves than the same species grown in bright light. This adaptive response is an example of:',
 "options":{"A":'Genetic mutation', "B":'Phenotypic plasticity, allowing the plant to adjust its growth pattern to its environment', "C":'Random variation with no adaptive value', "D":'Chromosomal rearrangement'},"answer":'B'},

{"id":59,"subject":'Biology',"topic":'Plant Biology',"difficulty":'Medium',
 "question":'Cytokinins, a class of plant hormones, are primarily known for promoting:',
 "options":{"A":'Root elongation only', "B":'Stomatal closure exclusively', "C":'Cell division (cytokinesis) and delaying leaf senescence', "D":'Fruit ripening'},"answer":'C'},

{"id":60,"subject":'Biology',"topic":'Plant Biology',"difficulty":'Easy',
 "question":'A seed contains an embryo, a food reserve, and a protective outer layer called the:',
 "options":{"A":'Endosperm', "B":'Radicle', "C":'Cotyledon', "D":'Seed coat'},"answer":'D'},

{"id":61,"subject":'Biology',"topic":'Human Physiology - Digestion',"difficulty":'Easy',
 "question":'The muscular, ring-shaped valve that controls the passage of food from the esophagus into the stomach is the:',
 "options":{"A":'Cardiac (esophageal) sphincter', "B":'Pyloric sphincter', "C":'Ileocecal valve', "D":'Anal sphincter'},"answer":'A'},

{"id":62,"subject":'Biology',"topic":'Human Physiology - Digestion',"difficulty":'Medium',
 "question":'Trypsin and chymotrypsin, secreted by the pancreas in inactive forms, function to digest:',
 "options":{"A":'Carbohydrates', "B":'Proteins into smaller peptides', "C":'Lipids into fatty acids', "D":'Nucleic acids'},"answer":'B'},

{"id":63,"subject":'Biology',"topic":'Human Physiology - Digestion',"difficulty":'Medium',
 "question":'The primary function of the large intestine, beyond housing beneficial bacteria, is to:',
 "options":{"A":'Complete protein digestion', "B":'Absorb most nutrients from food', "C":'Absorb water and electrolytes from indigestible food matter, forming feces', "D":'Produce digestive enzymes'},"answer":'C'},

{"id":64,"subject":'Biology',"topic":'Human Physiology - Digestion',"difficulty":'Hard',
 "question":'A blockage of the common bile duct would most directly interfere with:',
 "options":{"A":'Carbohydrate digestion in the mouth', "B":'Water absorption in the large intestine', "C":'Protein digestion in the stomach', "D":'Fat digestion, since bile would be unable to reach the small intestine to emulsify fats'},"answer":'D'},

{"id":65,"subject":'Biology',"topic":'Human Physiology - Circulation',"difficulty":'Easy',
 "question":'The chamber of the heart that receives deoxygenated blood from the body via the vena cava is the:',
 "options":{"A":'Right atrium', "B":'Left atrium', "C":'Left ventricle', "D":'Right ventricle'},"answer":'A'},

{"id":66,"subject":'Biology',"topic":'Human Physiology - Circulation',"difficulty":'Medium',
 "question":'Capillary beds are the site of:',
 "options":{"A":'Pumping blood at high pressure', "B":'Exchange of gases, nutrients, and wastes between blood and body tissues', "C":'Blood cell production', "D":'Storage of oxygen'},"answer":'B'},

{"id":67,"subject":'Biology',"topic":'Human Physiology - Circulation',"difficulty":'Medium',
 "question":'Plasma, the liquid component of blood, is composed mostly of:',
 "options":{"A":'Red blood cells', "B":'White blood cells', "C":'Water, along with dissolved proteins, salts, and other solutes', "D":'Platelets'},"answer":'C'},

{"id":68,"subject":'Biology',"topic":'Human Physiology - Circulation',"difficulty":'Hard',
 "question":"The pulmonary circuit is unique among the body's circulatory pathways because it carries:",
 "options":{"A":'Oxygenated blood in its arteries and deoxygenated blood in its veins, like the systemic circuit', "B":'Only white blood cells', "C":'No blood at all, only lymph', "D":'Deoxygenated blood in its arteries and oxygenated blood in its veins, reversed compared to systemic vessels'},"answer":'D'},

{"id":69,"subject":'Biology',"topic":'Human Physiology - Respiration',"difficulty":'Easy',
 "question":'Gas exchange between air and blood in the lungs occurs by simple diffusion across the walls of the:',
 "options":{"A":'Alveoli', "B":'Bronchi', "C":'Trachea', "D":'Larynx'},"answer":'A'},

{"id":70,"subject":'Biology',"topic":'Human Physiology - Respiration',"difficulty":'Medium',
 "question":'During forced exhalation, in addition to the relaxation of inspiratory muscles, which muscles actively contract to further decrease thoracic volume?',
 "options":{"A":'The diaphragm only', "B":'The internal intercostal and abdominal muscles', "C":'The external intercostal muscles only', "D":'No muscles are involved in forced exhalation'},"answer":'B'},

{"id":71,"subject":'Biology',"topic":'Human Physiology - Respiration',"difficulty":'Medium',
 "question":"Hemoglobin's oxygen-binding curve shifts to the right (releasing oxygen more readily) in tissues with:",
 "options":{"A":'Low carbon dioxide and high pH', "B":'No metabolic activity at all', "C":'High carbon dioxide, low pH, and higher temperature (the Bohr effect)', "D":'Very high oxygen concentration'},"answer":'C'},

{"id":72,"subject":'Biology',"topic":'Human Physiology - Excretion',"difficulty":'Medium',
 "question":"The diagram shows a nephron with structures labeled 1-5: afferent arteriole, glomerulus, Bowman's capsule, proximal convoluted tubule, and loop of Henle. Which labeled structure is the site of blood filtration under pressure?",
 "image":'images/q_nephron_diagram.png',
 "options":{"A":'Structure 1 (afferent arteriole)', "B":'Structure 5 (loop of Henle)', "C":'Structure 4 (proximal convoluted tubule)', "D":'Structure 2 (glomerulus)'},"answer":'D'},

{"id":73,"subject":'Biology',"topic":'Human Physiology - Excretion',"difficulty":'Medium',
 "question":'The distal convoluted tubule of the nephron is primarily involved in:',
 "options":{"A":'Fine-tuning reabsorption and secretion, regulated by hormones such as aldosterone', "B":'Initial filtration of blood', "C":'Producing urine-related hormones', "D":'Storing urine before excretion'},"answer":'A'},

{"id":74,"subject":'Biology',"topic":'Human Physiology - Excretion',"difficulty":'Hard',
 "question":'A person taking a diuretic medication, which inhibits sodium (and therefore water) reabsorption in the nephron, would be expected to experience:',
 "options":{"A":'Decreased urine volume', "B":'Increased urine volume, due to reduced water reabsorption', "C":'No change in urine volume', "D":'Complete kidney failure'},"answer":'B'},

{"id":75,"subject":'Biology',"topic":'Human Physiology - Nervous & Endocrine',"difficulty":'Easy',
 "question":'The part of the brainstem that regulates vital involuntary functions such as heart rate and breathing is the:',
 "options":{"A":'Cerebrum', "B":'Cerebellum', "C":'Medulla oblongata', "D":'Corpus callosum'},"answer":'C'},

{"id":76,"subject":'Biology',"topic":'Human Physiology - Nervous & Endocrine',"difficulty":'Medium',
 "question":'An action potential is propagated along a myelinated axon via saltatory conduction, in which the electrical impulse:',
 "options":{"A":'Travels continuously along the entire membrane', "B":'Moves more slowly than in unmyelinated axons', "C":'Cannot travel at all along myelinated axons', "D":"'Jumps' between the nodes of Ranvier, increasing conduction speed"},"answer":'D'},

{"id":77,"subject":'Biology',"topic":'Human Physiology - Nervous & Endocrine',"difficulty":'Medium',
 "question":'The hormone melatonin, secreted by the pineal gland, primarily regulates:',
 "options":{"A":'The sleep-wake cycle (circadian rhythm)', "B":'Blood glucose levels', "C":'Growth of long bones', "D":'Blood calcium levels'},"answer":'A'},

{"id":78,"subject":'Biology',"topic":'Human Physiology - Nervous & Endocrine',"difficulty":'Hard',
 "question":"Damage to Broca's area in the brain would most likely result in difficulty with:",
 "options":{"A":'Understanding spoken language', "B":'Producing fluent, coherent speech, despite intact comprehension', "C":'Regulating heart rate', "D":'Maintaining balance'},"answer":'B'},

{"id":79,"subject":'Biology',"topic":'Human Physiology - Reproduction',"difficulty":'Easy',
 "question":'The structure that produces both eggs and the hormones estrogen and progesterone in females is the:',
 "options":{"A":'Uterus', "B":'Fallopian tube', "C":'Ovary', "D":'Vagina'},"answer":'C'},

{"id":80,"subject":'Biology',"topic":'Human Physiology - Reproduction',"difficulty":'Medium',
 "question":'LH (luteinizing hormone) triggers ovulation and then stimulates the remaining follicle to transform into the:',
 "options":{"A":'Graafian follicle', "B":'Endometrium', "C":'Corpus albicans directly', "D":'Corpus luteum, which secretes progesterone'},"answer":'D'},

{"id":81,"subject":'Biology',"topic":'Ecology',"difficulty":'Medium',
 "question":'The gradual, predictable change in species composition of a community over time, following a disturbance such as a fire, is called:',
 "options":{"A":'Ecological succession', "B":'Symbiosis', "C":'Competitive exclusion', "D":'Biomagnification'},"answer":'A'},

# ============================================================
# CHEMISTRY (45) - id 82-126
# ============================================================

{"id":82,"subject":'Chemistry',"topic":'Atomic Structure',"difficulty":'Easy',
 "question":'The number of electrons an atom can hold in its outermost (valence) shell is directly related to its:',
 "options":{"A":'Mass number only', "B":'Chemical reactivity and bonding behavior', "C":'Number of neutrons', "D":'Isotope classification'},"answer":'B'},

{"id":83,"subject":'Chemistry',"topic":'Atomic Structure',"difficulty":'Medium',
 "question":'An atom of phosphorus-31 (atomic number 15) contains how many neutrons?',
 "options":{"A":'15', "B":'31', "C":'16', "D":'46'},"answer":'C'},

{"id":84,"subject":'Chemistry',"topic":'Atomic Structure',"difficulty":'Medium',
 "question":'The electron configuration of a neutral neon atom (Z = 10) is:',
 "options":{"A":'1s2 2s1 2p7', "B":'1s2 2s2 2p5', "C":'1s2 2s2 2p4', "D":'1s2 2s2 2p6'},"answer":'D'},

{"id":85,"subject":'Chemistry',"topic":'Atomic Structure',"difficulty":'Hard',
 "question":'An ion has 26 protons and 24 electrons. What is its charge?',
 "options":{"A":'+2', "B":'-2', "C":'+26', "D":'-26'},"answer":'A'},

{"id":86,"subject":'Chemistry',"topic":'Periodic Table',"difficulty":'Easy',
 "question":'Elements in Group 1 of the periodic table (excluding hydrogen) are called:',
 "options":{"A":'Halogens', "B":'Alkali metals', "C":'Alkaline earth metals', "D":'Noble gases'},"answer":'B'},

{"id":87,"subject":'Chemistry',"topic":'Periodic Table',"difficulty":'Medium',
 "question":'Electron affinity generally becomes more negative (indicating a greater tendency to gain electrons) across a period from left to right mainly because:',
 "options":{"A":'Shielding increases dramatically', "B":'Atomic radius increases significantly', "C":'Nuclear charge increases, more strongly attracting an added electron', "D":'Electrons become harder to add'},"answer":'C'},

{"id":88,"subject":'Chemistry',"topic":'Periodic Table',"difficulty":'Medium',
 "question":'Which of the following elements would most likely form a 2- ion by gaining two electrons?',
 "options":{"A":'Sodium', "B":'Calcium', "C":'Aluminum', "D":'Oxygen'},"answer":'D'},

{"id":89,"subject":'Chemistry',"topic":'Chemical Bonding',"difficulty":'Easy',
 "question":'A bond in which one atom contributes both electrons to a shared pair, while the other atom contributes none, is called a:',
 "options":{"A":'Coordinate (dative) covalent bond', "B":'Ionic bond', "C":'Metallic bond', "D":'Van der Waals interaction'},"answer":'A'},

{"id":90,"subject":'Chemistry',"topic":'Chemical Bonding',"difficulty":'Medium',
 "question":'According to VSEPR theory, a molecule with six bonding pairs and no lone pairs on the central atom (e.g., SF6) has a molecular shape described as:',
 "options":{"A":'Trigonal bipyramidal', "B":'Octahedral', "C":'Tetrahedral', "D":'Square planar'},"answer":'B'},

{"id":91,"subject":'Chemistry',"topic":'Chemical Bonding',"difficulty":'Medium',
 "question":'Which of the following molecules would be expected to be nonpolar overall, despite containing polar bonds?',
 "options":{"A":'H2O', "B":'NH3', "C":'CO2', "D":'HCl'},"answer":'C'},

{"id":92,"subject":'Chemistry',"topic":'Chemical Bonding',"difficulty":'Hard',
 "question":'Ionic compounds tend to be brittle mainly because:',
 "options":{"A":'Their bonds are extremely weak', "B":'They are always liquids at room temperature', "C":'They contain no charged particles', "D":'When struck, layers of ions shift, bringing like-charged ions into close proximity, causing repulsion and fracture'},"answer":'D'},

{"id":93,"subject":'Chemistry',"topic":'States of Matter',"difficulty":'Easy',
 "question":'The phase diagram shows regions of solid, liquid, and gas plotted against temperature and pressure, with the triple point and critical point marked. Based on the diagram, at the triple point, the substance exists as:',
 "image":'images/q_phase_diagram_triple_point.png',
 "options":{"A":'Solid, liquid, and gas simultaneously in equilibrium', "B":'Only a liquid', "C":'Only a solid', "D":'Only a gas'},"answer":'A'},

{"id":94,"subject":'Chemistry',"topic":'States of Matter',"difficulty":'Medium',
 "question":'A gas occupies 12.0 L at a pressure of 2.0 atm. What pressure would be required to compress it to 4.0 L, assuming constant temperature?',
 "options":{"A":'0.67 atm', "B":'6.0 atm', "C":'3.0 atm', "D":'8.0 atm'},"answer":'B'},

{"id":95,"subject":'Chemistry',"topic":'States of Matter',"difficulty":'Hard',
 "question":'A weather balloon contains 500 L of gas at 1 atm and 280 K at ground level. As it rises, the pressure drops to 0.5 atm and the temperature drops to 240 K. What is the new volume of gas in the balloon?',
 "options":{"A":'500 L', "B":'1000 L', "C":'857 L', "D":'250 L'},"answer":'C'},

{"id":96,"subject":'Chemistry',"topic":'Stoichiometry',"difficulty":'Easy',
 "question":'The molar mass of glucose (C6H12O6) is approximately:',
 "options":{"A":'342 g/mol', "B":'90 g/mol', "C":'120 g/mol', "D":'180 g/mol'},"answer":'D'},

{"id":97,"subject":'Chemistry',"topic":'Stoichiometry',"difficulty":'Medium',
 "question":'How many moles of nitrogen atoms are present in 3 moles of (NH4)2SO4?',
 "options":{"A":'6', "B":'3', "C":'2', "D":'9'},"answer":'A'},

{"id":98,"subject":'Chemistry',"topic":'Stoichiometry',"difficulty":'Hard',
 "question":'A 750 mL solution contains 1.5 moles of KNO3. What is the molarity of the solution?',
 "options":{"A":'1.0 M', "B":'2.0 M', "C":'0.5 M', "D":'1.5 M'},"answer":'B'},

{"id":99,"subject":'Chemistry',"topic":'Stoichiometry',"difficulty":'Medium',
 "question":'In the reaction 2C2H6 + 7O2 -> 4CO2 + 6H2O, how many moles of water are produced when 4 moles of ethane (C2H6) react completely with excess O2?',
 "options":{"A":'6', "B":'8', "C":'12', "D":'4'},"answer":'C'},

{"id":100,"subject":'Chemistry',"topic":'Thermochemistry',"difficulty":'Easy',
 "question":'The specific heat capacity of a substance is defined as the amount of energy required to raise the temperature of:',
 "options":{"A":'One gram of the substance by 100 degrees', "B":'One mole of the substance by 10 degrees', "C":'The entire substance by one degree, regardless of mass', "D":'One gram (or unit mass) of the substance by one degree'},"answer":'D'},

{"id":101,"subject":'Chemistry',"topic":'Thermochemistry',"difficulty":'Medium',
 "question":'Bond breaking in a chemical reaction:',
 "options":{"A":'Always requires an input of energy', "B":'Always releases energy', "C":'Never involves any energy change', "D":'Only occurs in exothermic reactions'},"answer":'A'},

{"id":102,"subject":'Chemistry',"topic":'Chemical Equilibrium',"difficulty":'Medium',
 "question":'For the equilibrium PCl5(g) <-> PCl3(g) + Cl2(g), increasing the container volume (decreasing pressure) will shift the equilibrium:',
 "options":{"A":'Toward PCl5, the side with fewer moles of gas', "B":'Toward the products, PCl3 and Cl2, the side with more moles of gas', "C":'Not at all', "D":'Completely toward PCl5'},"answer":'B'},

{"id":103,"subject":'Chemistry',"topic":'Chemical Equilibrium',"difficulty":'Hard',
 "question":'If the concentration of a product is increased in a reaction at equilibrium, the reaction will shift to:',
 "options":{"A":'Produce more product', "B":'Have no effect on the equilibrium', "C":'Consume some of the added product, favoring the reverse reaction', "D":'Immediately stop the reaction entirely'},"answer":'C'},

{"id":104,"subject":'Chemistry',"topic":'Reaction Kinetics',"difficulty":'Easy',
 "question":'Which of the following would most likely increase the rate of a reaction between a solid and a liquid?',
 "options":{"A":'Using a larger, solid chunk of the reactant', "B":'Diluting the liquid reactant significantly', "C":'Decreasing the temperature', "D":'Grinding the solid reactant into a fine powder, increasing surface area'},"answer":'D'},

{"id":105,"subject":'Chemistry',"topic":'Reaction Kinetics',"difficulty":'Medium',
 "question":'The activation energy of a reaction is best described as:',
 "options":{"A":'The minimum energy required for reactant particles to successfully react upon collision', "B":'The total energy released by the reaction', "C":'The energy difference between reactants and products at equilibrium', "D":'Always equal to zero for spontaneous reactions'},"answer":'A'},

{"id":106,"subject":'Chemistry',"topic":'Electrochemistry',"difficulty":'Medium',
 "question":'A battery (galvanic cell) generates electricity through:',
 "options":{"A":'A non-spontaneous reaction requiring external energy', "B":'A spontaneous redox reaction that releases energy as electrical current', "C":'Physical rotation of magnets', "D":'Heating of the electrodes'},"answer":'B'},

{"id":107,"subject":'Chemistry',"topic":'Electrochemistry',"difficulty":'Hard',
 "question":'In the reaction Cu(s) + 2AgNO3(aq) -> Cu(NO3)2(aq) + 2Ag(s), the silver ion is:',
 "options":{"A":'Oxidized', "B":'Unchanged', "C":'Reduced', "D":'Acting as a catalyst'},"answer":'C'},

{"id":108,"subject":'Chemistry',"topic":'Acids & Bases',"difficulty":'Easy',
 "question":'A solution with a pH between 0 and 6 is generally classified as:',
 "options":{"A":'Basic', "B":'Amphoteric', "C":'Neutral', "D":'Acidic'},"answer":'D'},

{"id":109,"subject":'Chemistry',"topic":'Acids & Bases',"difficulty":'Medium',
 "question":'A solution has a hydroxide ion concentration [OH-] of 1x10^-2 M. What is its pOH?',
 "options":{"A":'2', "B":'12', "C":'14', "D":'1x10^-2'},"answer":'A'},

{"id":110,"subject":'Chemistry',"topic":'Acids & Bases',"difficulty":'Medium',
 "question":'A strong acid, when dissolved in water, is characterized by:',
 "options":{"A":'Only partial dissociation into ions', "B":'Complete (or nearly complete) dissociation into its constituent ions', "C":'No dissociation at all', "D":'A pH consistently above 7'},"answer":'B'},

{"id":111,"subject":'Chemistry',"topic":'Acids & Bases',"difficulty":'Hard',
 "question":'Titrating a strong acid with a strong base produces a titration curve where the pH at the equivalence point is approximately:',
 "options":{"A":'Less than 7', "B":'Greater than 7', "C":'Exactly 7', "D":'Undefined'},"answer":'C'},

{"id":112,"subject":'Chemistry',"topic":'Organic Chemistry',"difficulty":'Easy',
 "question":'A hydrocarbon containing at least one carbon-carbon triple bond belongs to which homologous series?',
 "options":{"A":'Alkanes', "B":'Alkenes', "C":'Cycloalkanes', "D":'Alkynes'},"answer":'D'},

{"id":113,"subject":'Chemistry',"topic":'Organic Chemistry',"difficulty":'Medium',
 "question":'Which of the following best describes an addition reaction, typical of alkenes?',
 "options":{"A":'Two smaller molecules combine to form one larger molecule, with no atoms lost', "B":'One atom in a molecule is replaced by another', "C":'A single molecule breaks apart into two smaller ones', "D":'Water is lost from a molecule'},"answer":'A'},

{"id":114,"subject":'Chemistry',"topic":'Organic Chemistry',"difficulty":'Medium',
 "question":'A tertiary alcohol is one in which the carbon bearing the -OH group is bonded to:',
 "options":{"A":'One other carbon atom', "B":'Three other carbon atoms', "C":'Two other carbon atoms', "D":'No other carbon atoms'},"answer":'B'},

{"id":115,"subject":'Chemistry',"topic":'Organic Chemistry',"difficulty":'Hard',
 "question":'In electrophilic addition to an alkene, the first step typically involves:',
 "options":{"A":'Attack of a nucleophile on the electron-poor double bond', "B":'Homolytic bond cleavage forming radicals', "C":'Attack of an electrophile on the electron-rich pi bond of the alkene, forming a carbocation intermediate', "D":'Direct substitution with no intermediate'},"answer":'C'},

{"id":116,"subject":'Chemistry',"topic":'Organic Chemistry',"difficulty":'Medium',
 "question":'Amino acids contain both an amino group and a carboxylic acid group, allowing them to act as:',
 "options":{"A":'Only acids', "B":'Only bases', "C":'Neither acids nor bases', "D":'Amphoteric molecules, able to act as both acids and bases'},"answer":'D'},

{"id":117,"subject":'Chemistry',"topic":'Organic Chemistry',"difficulty":'Easy',
 "question":'A compound containing the functional group -X (where X is a halogen such as Cl, Br, or I) attached to a carbon chain is called a(n):',
 "options":{"A":'Haloalkane (alkyl halide)', "B":'Alcohol', "C":'Ether', "D":'Amine'},"answer":'A'},

{"id":118,"subject":'Chemistry',"topic":'Inorganic Chemistry',"difficulty":'Medium',
 "question":'Which of the following best explains why transition metals can act as catalysts in many industrial reactions?',
 "options":{"A":'They are chemically inert and unreactive', "B":'Their variable oxidation states and ability to form complexes allow them to facilitate electron transfer and bond formation/breaking', "C":'They have very low melting points', "D":'They never form compounds'},"answer":'B'},

{"id":119,"subject":'Chemistry',"topic":'Inorganic Chemistry',"difficulty":'Medium',
 "question":'The general trend in reactivity of Group 1 metals (alkali metals) with water is that reactivity:',
 "options":{"A":'Decreases down the group', "B":'Remains constant throughout the group', "C":'Increases down the group, as the outer electron becomes easier to lose', "D":'Is unrelated to their position in the group'},"answer":'C'},

{"id":120,"subject":'Chemistry',"topic":'Inorganic Chemistry',"difficulty":'Hard',
 "question":'In the reaction SO2 + 2H2S -> 3S + 2H2O, sulfur in SO2 undergoes a change in oxidation state from:',
 "options":{"A":"No change in SO2's sulfur", "B":'-2 to 0 (oxidation)', "C":'0 to +4', "D":'+4 to 0 (reduction)'},"answer":'D'},

{"id":121,"subject":'Chemistry',"topic":'Physical Chemistry',"difficulty":'Medium',
 "question":'Osmotic pressure of a solution depends primarily on:',
 "options":{"A":'The molar concentration of dissolved solute particles', "B":'The identity of the solute only', "C":'The color of the solution', "D":"The solvent's boiling point alone"},"answer":'A'},

{"id":122,"subject":'Chemistry',"topic":'Physical Chemistry',"difficulty":'Hard',
 "question":'25 mL of an unknown NaOH solution is exactly neutralized by 40 mL of 0.25 M HCl. What is the molarity of the NaOH solution?',
 "options":{"A":'0.16 M', "B":'0.4 M', "C":'0.25 M', "D":'0.156 M'},"answer":'B'},

{"id":123,"subject":'Chemistry',"topic":'Environmental Chemistry',"difficulty":'Easy',
 "question":'Which of the following is a primary source of nitrogen oxide (NOx) pollutants in urban areas?',
 "options":{"A":'Photosynthesis', "B":'Ocean evaporation', "C":'Combustion in vehicle engines and power plants', "D":'Decomposition of organic matter alone'},"answer":'C'},

{"id":124,"subject":'Chemistry',"topic":'Environmental Chemistry',"difficulty":'Medium',
 "question":'Bioaccumulation refers to the process by which:',
 "options":{"A":'Toxic substances are rapidly broken down and eliminated by organisms', "B":'Toxins have no effect on living organisms', "C":'Organisms rapidly adapt to eliminate all toxins', "D":'Toxic substances build up in the tissues of an organism over time, often becoming more concentrated at higher trophic levels (biomagnification)'},"answer":'D'},

{"id":125,"subject":'Chemistry',"topic":'Chemical Bonding',"difficulty":'Easy',
 "question":'A molecule with a symmetrical shape and identical atoms bonded to a central atom (such as CH4) is typically:',
 "options":{"A":'Nonpolar', "B":'Polar', "C":'Ionic', "D":'Radioactive'},"answer":'A'},

{"id":126,"subject":'Chemistry',"topic":'Atomic Structure',"difficulty":'Easy',
 "question":'Isotopes of the same element have the same chemical properties mainly because they have identical numbers of:',
 "options":{"A":'Neutrons', "B":'Protons and electrons', "C":'Mass numbers', "D":'Total nucleons'},"answer":'B'},

# ============================================================
# PHYSICS (36) - id 127-162
# ============================================================

{"id":127,"subject":'Physics',"topic":'Kinematics',"difficulty":'Easy',
 "question":'A bus covers 240 km in 4 hours at constant speed. What is its speed?',
 "options":{"A":'40 km/h', "B":'960 km/h', "C":'60 km/h', "D":'6 km/h'},"answer":'C'},

{"id":128,"subject":'Physics',"topic":'Kinematics',"difficulty":'Medium',
 "question":'An object accelerates uniformly from 8 m/s to 28 m/s over 4 seconds. What is its acceleration?',
 "options":{"A":'4 m/s^2', "B":'7 m/s^2', "C":'9 m/s^2', "D":'5 m/s^2'},"answer":'D'},

{"id":129,"subject":'Physics',"topic":'Kinematics',"difficulty":'Hard',
 "question":'A car travels at a constant 20 m/s for 10 seconds, then decelerates uniformly to rest over the next 5 seconds. What is the total distance traveled during the entire 15 seconds?',
 "options":{"A":'250 m', "B":'200 m', "C":'300 m', "D":'150 m'},"answer":'A'},

{"id":130,"subject":'Physics',"topic":'Dynamics',"difficulty":'Easy',
 "question":'A rocket expels exhaust gases downward and is propelled upward. This is best explained by:',
 "options":{"A":"Newton's first law", "B":"Newton's third law", "C":"Newton's second law", "D":'The law of conservation of mass'},"answer":'B'},

{"id":131,"subject":'Physics',"topic":'Dynamics',"difficulty":'Medium',
 "question":"A net force of 60 N produces an acceleration of 5 m/s^2 in an object. What is the object's mass?",
 "options":{"A":'65 kg', "B":'300 kg', "C":'12 kg', "D":'55 kg'},"answer":'C'},

{"id":132,"subject":'Physics',"topic":'Dynamics',"difficulty":'Medium',
 "question":'The weight of an object is calculated as the product of its mass and:',
 "options":{"A":'Velocity', "B":'Its momentum', "C":'Its acceleration alone, regardless of gravity', "D":'The acceleration due to gravity'},"answer":'D'},

{"id":133,"subject":'Physics',"topic":'Dynamics',"difficulty":'Hard',
 "question":'A 6 kg object moving at 4 m/s to the right collides head-on with a stationary 2 kg object, and after the collision they move together. What is their combined velocity?',
 "options":{"A":'3 m/s', "B":'2 m/s', "C":'4 m/s', "D":'1 m/s'},"answer":'A'},

{"id":134,"subject":'Physics',"topic":'Work, Energy & Power',"difficulty":'Easy',
 "question":'If no displacement occurs in the direction of an applied force, the work done by that force is:',
 "options":{"A":'Maximum', "B":'Zero', "C":'Negative', "D":'Equal to the force squared'},"answer":'B'},

{"id":135,"subject":'Physics',"topic":'Work, Energy & Power',"difficulty":'Medium',
 "question":'A 3 kg object falls from rest and reaches a speed of 6 m/s. What is its kinetic energy at that point?',
 "options":{"A":'18 J', "B":'108 J', "C":'54 J', "D":'9 J'},"answer":'C'},

{"id":136,"subject":'Physics',"topic":'Work, Energy & Power',"difficulty":'Medium',
 "question":'A compressed spring, when released, converts its stored elastic potential energy primarily into:',
 "options":{"A":'Chemical energy', "B":'No other form of energy', "C":'Nuclear energy', "D":'Kinetic energy of the object it propels'},"answer":'D'},

{"id":137,"subject":'Physics',"topic":'Work, Energy & Power',"difficulty":'Hard',
 "question":"A crane does 24000 J of work lifting a load in 8 seconds. What is the crane's power output?",
 "options":{"A":'3000 W', "B":'192000 W', "C":'300 W', "D":'30000 W'},"answer":'A'},

{"id":138,"subject":'Physics',"topic":'Circular Motion & Gravitation',"difficulty":'Easy',
 "question":'An object moving in a circle at constant speed experiences a net force directed:',
 "options":{"A":'Tangentially', "B":'Toward the center', "C":'Away from the center', "D":'In no particular direction'},"answer":'B'},

{"id":139,"subject":'Physics',"topic":'Circular Motion & Gravitation',"difficulty":'Medium',
 "question":'If the mass of both objects in a gravitational system is halved, while the distance remains unchanged, the gravitational force between them becomes:',
 "options":{"A":'Double the original', "B":'Half of the original', "C":'One quarter of the original', "D":'Four times the original'},"answer":'C'},

{"id":140,"subject":'Physics',"topic":'Circular Motion & Gravitation',"difficulty":'Hard',
 "question":"A satellite orbits Earth at a certain altitude with orbital speed v. If the satellite's orbital radius were increased, its required orbital speed to maintain a stable circular orbit would:",
 "options":{"A":'Increase', "B":'Become zero', "C":'Remain exactly the same', "D":'Decrease'},"answer":'D'},

{"id":141,"subject":'Physics',"topic":'Fluid Mechanics',"difficulty":'Easy',
 "question":'Pressure in a fluid at rest increases with increasing:',
 "options":{"A":'Depth', "B":'Surface area', "C":'Temperature only', "D":'Fluid color'},"answer":'A'},

{"id":142,"subject":'Physics',"topic":'Fluid Mechanics',"difficulty":'Medium',
 "question":'An object will sink in a fluid if its average density is:',
 "options":{"A":"Less than the fluid's density", "B":"Greater than the fluid's density", "C":"Exactly equal to the fluid's density", "D":'Zero'},"answer":'B'},

{"id":143,"subject":'Physics',"topic":'Fluid Mechanics',"difficulty":'Hard',
 "question":'A venturi meter, used to measure fluid flow rate, works based on the principle that as a fluid passes through a constricted section of pipe, its speed increases and its pressure:',
 "options":{"A":'Increases proportionally', "B":'Remains completely unchanged', "C":"Decreases, as described by Bernoulli's principle", "D":'Becomes infinite'},"answer":'C'},

{"id":144,"subject":'Physics',"topic":'Oscillations & Waves',"difficulty":'Easy',
 "question":'The number of oscillations completed per unit time is called the:',
 "options":{"A":'Period', "B":'Wavelength', "C":'Amplitude', "D":'Frequency'},"answer":'D'},

{"id":145,"subject":'Physics',"topic":'Oscillations & Waves',"difficulty":'Medium',
 "question":'For a mass oscillating on a spring, increasing the mass while keeping the spring constant the same will cause the period to:',
 "options":{"A":'Increase', "B":'Decrease', "C":'Remain unchanged', "D":'Become zero'},"answer":'A'},

{"id":146,"subject":'Physics',"topic":'Oscillations & Waves',"difficulty":'Medium',
 "question":'A wave has a period of 0.5 seconds and a wavelength of 4 m. What is its speed?',
 "options":{"A":'2 m/s', "B":'8 m/s', "C":'0.125 m/s', "D":'4.5 m/s'},"answer":'B'},

{"id":147,"subject":'Physics',"topic":'Oscillations & Waves',"difficulty":'Hard',
 "question":'Standing waves are produced when two waves of the same frequency and amplitude travel:',
 "options":{"A":'In the same direction and never interact', "B":'At right angles to each other', "C":'In opposite directions and interfere, creating fixed nodes and antinodes', "D":'At completely different frequencies'},"answer":'C'},

{"id":148,"subject":'Physics',"topic":'Thermodynamics',"difficulty":'Easy',
 "question":'The natural tendency of heat to flow from hot to cold objects, never spontaneously the reverse, is described by the:',
 "options":{"A":'First law of thermodynamics', "B":'Law of conservation of mass', "C":'Zeroth law of thermodynamics', "D":'Second law of thermodynamics'},"answer":'D'},

{"id":149,"subject":'Physics',"topic":'Thermodynamics',"difficulty":'Medium',
 "question":'In a cyclic process, where a system returns to its initial state after a series of changes, the net change in internal energy of the system is:',
 "options":{"A":'Zero', "B":'Always negative', "C":'Always positive', "D":'Equal to the total heat absorbed'},"answer":'A'},

{"id":150,"subject":'Physics',"topic":'Thermodynamics',"difficulty":'Hard',
 "question":'A refrigerator removes 300 J of heat from its interior while the compressor does 100 J of work. How much heat is expelled into the surrounding room?',
 "options":{"A":'200 J', "B":'400 J', "C":'300 J', "D":'100 J'},"answer":'B'},

{"id":151,"subject":'Physics',"topic":'Electrostatics',"difficulty":'Easy',
 "question":'The SI unit used to measure electric potential (voltage) is the:',
 "options":{"A":'Ampere', "B":'Ohm', "C":'Volt', "D":'Coulomb'},"answer":'C'},

{"id":152,"subject":'Physics',"topic":'Electrostatics',"difficulty":'Medium',
 "question":'Grounding an electrically charged object typically causes it to:',
 "options":{"A":'Become more highly charged', "B":'Reverse its charge', "C":'Explode', "D":'Lose its excess charge by transferring it to the Earth'},"answer":'D'},

{"id":153,"subject":'Physics',"topic":'Current Electricity',"difficulty":'Easy',
 "question":'The reciprocal of resistance is called:',
 "options":{"A":'Conductance', "B":'Capacitance', "C":'Inductance', "D":'Reactance'},"answer":'A'},

{"id":154,"subject":'Physics',"topic":'Current Electricity',"difficulty":'Medium',
 "question":'In the circuit shown, resistor R1 (4 ohm) is connected in parallel with resistor R2 (12 ohm), and this combination is connected in series with R3 (1 ohm). What is the total resistance of the circuit?',
 "image":'images/q_circuit_r1r2_parallel_r3_series_v2.png',
 "options":{"A":'3 ohm', "B":'4 ohm', "C":'17 ohm', "D":'6 ohm'},"answer":'B'},

{"id":155,"subject":'Physics',"topic":'Current Electricity',"difficulty":'Hard',
 "question":'Three identical 9 ohm resistors are connected in series. What is the equivalent resistance?',
 "options":{"A":'3 ohm', "B":'9 ohm', "C":'27 ohm', "D":'18 ohm'},"answer":'C'},

{"id":156,"subject":'Physics',"topic":'Current Electricity',"difficulty":'Medium',
 "question":'A device consumes 720 J of energy in 60 seconds while operating at 6 A. What is the voltage across the device?',
 "options":{"A":'4320 V', "B":'12 V', "C":'120 V', "D":'2 V'},"answer":'D'},

{"id":157,"subject":'Physics',"topic":'Electromagnetism',"difficulty":'Medium',
 "question":'A galvanometer can be converted into an ammeter (for measuring larger currents) by connecting a:',
 "options":{"A":'Low resistance (shunt) in parallel', "B":'High resistance in series', "C":'Capacitor in series', "D":'Nothing; a galvanometer cannot be modified this way'},"answer":'A'},

{"id":158,"subject":'Physics',"topic":'Electromagnetism',"difficulty":'Hard',
 "question":'Eddy currents, induced in a conductor moving through a magnetic field, tend to:',
 "options":{"A":"Increase the conductor's motion", "B":"Oppose the motion that created them, according to Lenz's law, resulting in a braking effect", "C":'Have no effect on the conductor', "D":'Only occur in insulators'},"answer":'B'},

{"id":159,"subject":'Physics',"topic":'Modern Physics',"difficulty":'Easy',
 "question":'The number of electrons in a neutral atom is always equal to its:',
 "options":{"A":'Mass number', "B":'Number of neutrons', "C":'Number of protons', "D":'Number of isotopes'},"answer":'C'},

{"id":160,"subject":'Physics',"topic":'Modern Physics',"difficulty":'Medium',
 "question":'Nuclear fusion, the process powering the Sun, involves:',
 "options":{"A":'The splitting of heavy nuclei into lighter ones', "B":'A purely chemical process', "C":'The complete destruction of matter with no energy release', "D":'The combining of light nuclei (such as hydrogen) into a heavier nucleus, releasing energy'},"answer":'D'},

{"id":161,"subject":'Physics',"topic":'Modern Physics',"difficulty":'Hard',
 "question":'A radioactive isotope decays to 1/16 of its original amount after 40 minutes. What is its half-life?',
 "options":{"A":'10 minutes', "B":'8 minutes', "C":'5 minutes', "D":'20 minutes'},"answer":'A'},

{"id":162,"subject":'Physics',"topic":'Optics',"difficulty":'Medium',
 "question":'The ray diagram shows an object placed beyond the center of curvature (C) of a concave mirror, with two reflected rays converging to form the image. Based on the diagram, where is the image formed, and what are its characteristics?',
 "image":'images/q_concave_mirror_beyond_c_ray_diagram.png',
 "options":{"A":'Between the pole and F; virtual, upright, and magnified', "B":'Between F and C; real, inverted, and diminished', "C":'At C; real, inverted, and the same size as the object', "D":'Beyond C; real, inverted, and magnified'},"answer":'B'},

# ============================================================
# ENGLISH (9) - id 163-171
# ============================================================

{"id":163,"subject":'English',"topic":'Synonyms',"difficulty":'Easy',
 "question":"Choose the word most nearly similar in meaning to 'PRUDENT':",
 "options":{"A":'Reckless', "B":'Careless', "C":'Wise and cautious', "D":'Impulsive'},"answer":'C'},

{"id":164,"subject":'English',"topic":'Antonyms',"difficulty":'Easy',
 "question":"Choose the word most nearly opposite in meaning to 'OPTIMISTIC':",
 "options":{"A":'Hopeful', "B":'Positive', "C":'Cheerful', "D":'Pessimistic'},"answer":'D'},

{"id":165,"subject":'English',"topic":'Grammar',"difficulty":'Easy',
 "question":'Choose the grammatically correct sentence:',
 "options":{"A":'Neither the coach nor the players were happy with the result.', "B":'Neither the coach nor the players was happy with the result.', "C":'Neither the coach or the players were happy with the result.', "D":'Neither the coach nor the player were happy with the result.'},"answer":'A'},

{"id":166,"subject":'English',"topic":'Grammar',"difficulty":'Medium',
 "question":'Choose the correct sentence:',
 "options":{"A":'If I knew, I would have come earlier.', "B":'If I had known, I would have come earlier.', "C":'If I had known, I would come earlier.', "D":'If I have known, I would have come earlier.'},"answer":'B'},

{"id":167,"subject":'English',"topic":'Sentence Correction',"difficulty":'Medium',
 "question":'Choose the sentence that is grammatically correct:',
 "options":{"A":'One of the players are injured.', "B":'One of the player is injured.', "C":'One of the players is injured.', "D":'One of the players have been injured.'},"answer":'C'},

{"id":168,"subject":'English',"topic":'Vocabulary',"difficulty":'Medium',
 "question":"Choose the word that best completes the sentence: 'The company's profits have shown a ______ increase over the past five years.'",
 "options":{"A":'Negligible', "B":'Erratic', "C":'Declining', "D":'Steady'},"answer":'D'},

{"id":169,"subject":'English',"topic":'Idioms',"difficulty":'Medium',
 "question":"Choose the meaning closest to the idiom 'to be on the same page':",
 "options":{"A":'To have the same understanding or agreement about something', "B":'To read the same book', "C":'To be located in the same place', "D":'To argue about the same topic'},"answer":'A'},

{"id":170,"subject":'English',"topic":'Sentence Correction',"difficulty":'Hard',
 "question":"Choose the option that best corrects the sentence: 'The teacher explained the students the new topic.'",
 "options":{"A":'The teacher explained to the students the new topic.', "B":'Both A and D are correct.', "C":'The teacher explain the students the new topic.', "D":'The teacher explained the new topic to the students.'},"answer":'B'},

{"id":171,"subject":'English',"topic":'Prepositions',"difficulty":'Hard',
 "question":"Choose the correct preposition: 'The new policy will come ______ effect starting next month.'",
 "options":{"A":'in', "B":'with', "C":'into', "D":'at'},"answer":'C'},

# ============================================================
# LOGICAL REASONING (9) - id 172-180
# ============================================================

{"id":172,"subject":'Logical Reasoning',"topic":'Number Series',"difficulty":'Easy',
 "question":'Find the next number in the series: 3, 9, 27, 81, ?',
 "options":{"A":'162', "B":'324', "C":'200', "D":'243'},"answer":'D'},

{"id":173,"subject":'Logical Reasoning',"topic":'Number Series',"difficulty":'Easy',
 "question":'Find the missing number: 100, 91, 82, 73, ?',
 "options":{"A":'64', "B":'60', "C":'65', "D":'63'},"answer":'A'},

{"id":174,"subject":'Logical Reasoning',"topic":'Analogies',"difficulty":'Easy',
 "question":'Carpenter is to Wood as Tailor is to:',
 "options":{"A":'Needle', "B":'Cloth', "C":'Scissors', "D":'Shop'},"answer":'B'},

{"id":175,"subject":'Logical Reasoning',"topic":'Analogies',"difficulty":'Medium',
 "question":'Book is to Chapter as Building is to:',
 "options":{"A":'Wall', "B":'Roof', "C":'Floor', "D":'Door'},"answer":'C'},

{"id":176,"subject":'Logical Reasoning',"topic":'Blood Relations',"difficulty":'Medium',
 "question":"A woman introduces a boy as 'the son of my husband's sister.' How is the boy related to the woman?",
 "options":{"A":'Son', "B":'Cousin', "C":'Brother', "D":'Nephew'},"answer":'D'},

{"id":177,"subject":'Logical Reasoning',"topic":'Coding-Decoding',"difficulty":'Medium',
 "question":'If in a certain code, FLOWER is written as GMPXFS, how is GARDEN written in the same code?',
 "options":{"A":'HBSEFN', "B":'HBSEFO', "C":'HASEFO', "D":'GBSEFO'},"answer":'B'},

{"id":178,"subject":'Logical Reasoning',"topic":'Syllogism',"difficulty":'Hard',
 "question":'All fish live in water. No mammals live in water. Which conclusion logically follows?',
 "options":{"A":'All mammals are fish', "B":'No fish are mammals', "C":'Some fish are mammals', "D":'All water-dwelling creatures are fish'},"answer":'B'},

{"id":179,"subject":'Logical Reasoning',"topic":'Pattern Recognition',"difficulty":'Hard',
 "question":'Find the next term in the series: 1, 1, 2, 3, 5, 8, ?',
 "options":{"A":'11', "B":'12', "C":'13', "D":'14'},"answer":'C'},

{"id":180,"subject":'Logical Reasoning',"topic":'Direction Sense',"difficulty":'Medium',
 "question":'A girl walks 6 km east, then turns south and walks 8 km. How far is she from her starting point?',
 "options":{"A":'14 km', "B":'48 km', "C":'2 km', "D":'10 km'},"answer":'D'},

]


# ------------------------------------------------------------
# Sanity-check / summary utility
# ------------------------------------------------------------
def summarize(questions):
    from collections import Counter
    subj = Counter(q["subject"] for q in questions)
    diff = Counter(q["difficulty"] for q in questions)
    ans = Counter(q["answer"] for q in questions)
    ids = [q["id"] for q in questions]
    dup_ids = [i for i in set(ids) if ids.count(i) > 1]
    dup_q = [q["question"] for q in questions]
    dup_questions = [t for t in set(dup_q) if dup_q.count(t) > 1]
    images = [q for q in questions if "image" in q]

    print(f"Total questions: {len(questions)}")
    print("\nBy subject:")
    for s, c in subj.items():
        print(f"  {s}: {c}")
    print("\nBy difficulty:")
    for d, c in diff.items():
        print(f"  {d}: {c}")
    print("\nBy correct-answer letter (should be roughly balanced):")
    for L in ["A", "B", "C", "D"]:
        print(f"  {L}: {ans[L]}")
    print(f"\nDuplicate IDs: {dup_ids if dup_ids else 'None'}")
    print(f"Duplicate question text: {dup_questions if dup_questions else 'None'}")
    print(f"\nImage-based questions ({len(images)}):")
    for q in images:
        print(f"  Q{q['id']} [{q['subject']}] -> {q['image']}")

    for q in questions:
        assert set(q["options"].keys()) == {"A", "B", "C", "D"}, f"Q{q['id']} missing an option"
        assert q["answer"] in q["options"], f"Q{q['id']} answer key invalid"
    print("\nAll questions have exactly 4 options (A-D) and a valid answer key. OK.")


def print_answer_key(questions):
    print("\nANSWER KEY")
    print("-" * 40)
    for q in questions:
        print(f"{q['id']:>3}. {q['answer']}", end="   ")
        if q["id"] % 10 == 0:
            print()
    print()


if __name__ == "__main__":
    summarize(QUESTIONS)
    print_answer_key(QUESTIONS)