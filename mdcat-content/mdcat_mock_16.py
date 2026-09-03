"""
MDCAT Mock Test 14
==================
Full-length mock test: 180 MCQs
Weightage: Biology 81 | Chemistry 45 | Physics 36 | English 9 | Logical Reasoning 9
Difficulty mix (approx): 30% Easy / 50% Medium / 20% Hard, distributed throughout.

Includes 5 image/diagram-based questions (2 Biology, 1 Chemistry, 2 Physics).
Each such question has an "image" key giving a relative path to a PNG diagram
that must be viewed alongside the question (images/ subfolder, shipped alongside
this file). Diagrams: the endomembrane system secretory pathway, an
autosomal-recessive pedigree chart, a solubility-vs-temperature curve, a
series-then-parallel resistor circuit, and a convex-lens diagram showing
parallel rays converging at the principal focus.

Each question is a dict:
    id, subject, topic, difficulty, question, [image], options (A-D), answer (correct letter)

Run this file directly to print a summary / sanity-check the paper.
"""

QUESTIONS = [

# ============================================================
# BIOLOGY (81) - id 1-81
# ============================================================

{"id":1,"subject":'Biology',"topic":'Biomolecules',"difficulty":'Easy',
 "question":'Which of the following is a nucleic acid?',
 "options":{"A":'RNA', "B":'Cellulose', "C":'Hemoglobin', "D":'Glycogen'},"answer":'A'},

{"id":2,"subject":'Biology',"topic":'Biomolecules',"difficulty":'Easy',
 "question":'Amino acids are linked together to form proteins through:',
 "options":{"A":'Glycosidic bonds', "B":'Peptide bonds', "C":'Ester bonds', "D":'Hydrogen bonds only'},"answer":'B'},

{"id":3,"subject":'Biology',"topic":'Biomolecules',"difficulty":'Medium',
 "question":'Which bond primarily stabilizes the alpha helix, a common secondary structure in proteins?',
 "options":{"A":'Disulfide bridges only', "B":'Ionic bonds between R-groups', "C":'Hydrogen bonds between backbone N-H and C=O groups', "D":'Peptide bonds between R-groups'},"answer":'C'},

{"id":4,"subject":'Biology',"topic":'Biomolecules',"difficulty":'Medium',
 "question":'A key structural difference between starch and glycogen is that glycogen is:',
 "options":{"A":'Made of fructose units', "B":'Composed of amino acids', "C":'Found only in plants', "D":'More highly branched than starch, allowing faster glucose release'},"answer":'D'},

{"id":5,"subject":'Biology',"topic":'Biomolecules',"difficulty":'Hard',
 "question":'The specific three-dimensional shape of an enzyme, essential for its function, is primarily determined by its:',
 "options":{"A":'Primary sequence of amino acids, which dictates folding', "B":'Random environmental factors alone', "C":"The organism's diet", "D":'Its molecular weight only'},"answer":'A'},

{"id":6,"subject":'Biology',"topic":'Enzymes',"difficulty":'Easy',
 "question":'A substance that speeds up a chemical reaction without being permanently changed itself is called a(n):',
 "options":{"A":'Substrate', "B":'Catalyst', "C":'Product', "D":'Reactant'},"answer":'B'},

{"id":7,"subject":'Biology',"topic":'Enzymes',"difficulty":'Medium',
 "question":"The 'induced fit' model of enzyme action proposes that:",
 "options":{"A":"The enzyme's active site is a rigid, unchanging shape that perfectly matches the substrate", "B":'Enzymes never interact with their substrates directly', "C":'The active site changes shape slightly as it binds the substrate, improving the fit', "D":'Substrates change shape to match a rigid enzyme'},"answer":'C'},

{"id":8,"subject":'Biology',"topic":'Enzymes',"difficulty":'Medium',
 "question":'Which factor would most likely decrease the rate of an enzyme-catalyzed reaction, all else being equal?',
 "options":{"A":'Increasing substrate concentration below saturation', "B":'Adding more enzyme', "C":'Raising temperature slightly toward the optimum', "D":"Decreasing pH far below the enzyme's optimum"},"answer":'D'},

{"id":9,"subject":'Biology',"topic":'Enzymes',"difficulty":'Hard',
 "question":'A researcher observes that adding excess substrate does not overcome the inhibitory effect of a particular inhibitor. This finding is most consistent with:',
 "options":{"A":'Non-competitive inhibition', "B":'Competitive inhibition', "C":'No inhibition occurring at all', "D":'The inhibitor not binding the enzyme at all'},"answer":'A'},

{"id":10,"subject":'Biology',"topic":'Cell Biology',"difficulty":'Easy',
 "question":'Which structure is found in both plant and animal cells and is the primary site of protein synthesis?',
 "options":{"A":'Chloroplast', "B":'Ribosome', "C":'Cell wall', "D":'Central vacuole'},"answer":'B'},

{"id":11,"subject":'Biology',"topic":'Cell Biology',"difficulty":'Easy',
 "question":"The membrane-bound organelle containing the cell's genetic material is the:",
 "options":{"A":'Mitochondrion', "B":'Ribosome', "C":'Nucleus', "D":'Lysosome'},"answer":'C'},

{"id":12,"subject":'Biology',"topic":'Cell Biology',"difficulty":'Medium',
 "question":'The diagram shows the endomembrane system with structures labeled 1-4 (nuclear envelope/rough ER, Golgi apparatus, secretory vesicle, and plasma membrane), connected by arrows showing the pathway of a secreted protein. Based on the diagram, in which order does the protein correctly pass through these structures?',
 "image":'images/q_endomembrane_system_diagram.png',
 "options":{"A":'4 -> 3 -> 2 -> 1', "B":'3 -> 4 -> 1 -> 2', "C":'2 -> 1 -> 4 -> 3', "D":'1 -> 2 -> 3 -> 4'},"answer":'D'},

{"id":13,"subject":'Biology',"topic":'Cell Biology',"difficulty":'Medium',
 "question":'Which organelle is responsible for converting light energy into chemical energy stored in glucose?',
 "options":{"A":'Chloroplast', "B":'Mitochondrion', "C":'Nucleus', "D":'Lysosome'},"answer":'A'},

{"id":14,"subject":'Biology',"topic":'Cell Biology',"difficulty":'Medium',
 "question":'A cell lacking a functional Golgi apparatus would most likely have difficulty:',
 "options":{"A":'Replicating its DNA', "B":'Properly modifying, sorting, and packaging proteins for secretion', "C":'Performing glycolysis', "D":'Transcribing genes'},"answer":'B'},

{"id":15,"subject":'Biology',"topic":'Cell Biology',"difficulty":'Medium',
 "question":'Cell theory states that all living organisms are composed of cells, and that:',
 "options":{"A":'Cells arise spontaneously from non-living matter', "B":'Cells have no common origin', "C":'All cells arise from pre-existing cells', "D":'Only animal cells follow cell theory'},"answer":'C'},

{"id":16,"subject":'Biology',"topic":'Cell Biology',"difficulty":'Hard',
 "question":'A cell that has an unusually high number of ribosomes, both free and attached to rough ER, is most likely a cell that:',
 "options":{"A":'Has a very low rate of protein synthesis', "B":'Is undergoing apoptosis', "C":'Cannot synthesize any proteins', "D":'Actively synthesizes large quantities of protein'},"answer":'D'},

{"id":17,"subject":'Biology',"topic":'Cell Membrane & Transport',"difficulty":'Easy',
 "question":'The plasma membrane is composed mainly of a bilayer of:',
 "options":{"A":'Phospholipids', "B":'Proteins', "C":'Carbohydrates', "D":'Nucleic acids'},"answer":'A'},

{"id":18,"subject":'Biology',"topic":'Cell Membrane & Transport',"difficulty":'Medium',
 "question":'Which type of transport requires a carrier protein but does not require ATP?',
 "options":{"A":'Active transport', "B":'Facilitated diffusion', "C":'Endocytosis', "D":'Exocytosis'},"answer":'B'},

{"id":19,"subject":'Biology',"topic":'Cell Membrane & Transport',"difficulty":'Medium',
 "question":"A cell membrane's selective permeability allows it to:",
 "options":{"A":'Let all substances pass through equally', "B":'Prevent any substance from crossing', "C":'Control which substances enter and exit the cell, based on size, charge, and polarity', "D":'Only allow water to cross'},"answer":'C'},

{"id":20,"subject":'Biology',"topic":'Cell Membrane & Transport',"difficulty":'Hard',
 "question":"Aquaporins increase a cell's permeability to water far beyond what would occur through the lipid bilayer alone, primarily because:",
 "options":{"A":'They actively pump water using ATP', "B":'They convert water into a different molecule', "C":'They dissolve the lipid bilayer', "D":'They form dedicated channels that allow rapid, selective passage of water molecules'},"answer":'D'},

{"id":21,"subject":'Biology',"topic":'Cell Membrane & Transport',"difficulty":'Easy',
 "question":'The process by which a cell engulfs extracellular fluid and dissolved substances is specifically called:',
 "options":{"A":'Pinocytosis', "B":'Phagocytosis', "C":'Exocytosis', "D":'Facilitated diffusion'},"answer":'A'},

{"id":22,"subject":'Biology',"topic":'Cell Cycle & Division',"difficulty":'Easy',
 "question":'Which of the following correctly lists the four phases of mitosis in order?',
 "options":{"A":'Metaphase, Prophase, Anaphase, Telophase', "B":'Prophase, Metaphase, Anaphase, Telophase', "C":'Anaphase, Telophase, Prophase, Metaphase', "D":'Telophase, Anaphase, Metaphase, Prophase'},"answer":'B'},

{"id":23,"subject":'Biology',"topic":'Cell Cycle & Division',"difficulty":'Easy',
 "question":'During telophase, chromosomes:',
 "options":{"A":'Condense further and align at the equator', "B":'Separate and move to opposite poles', "C":'Begin decondensing as new nuclear envelopes form around each set', "D":'Attach to spindle fibers for the first time'},"answer":'C'},

{"id":24,"subject":'Biology',"topic":'Cell Cycle & Division',"difficulty":'Medium',
 "question":'Meiosis II is similar to mitosis in that meiosis II involves:',
 "options":{"A":'The pairing of homologous chromosomes', "B":'Crossing over between chromatids', "C":'A reduction in chromosome number from diploid to haploid', "D":'The separation of sister chromatids'},"answer":'D'},

{"id":25,"subject":'Biology',"topic":'Cell Cycle & Division',"difficulty":'Medium',
 "question":'If a diploid cell has 2n = 12 chromosomes, how many chromatids are present in the cell just before mitosis begins (after S phase)?',
 "options":{"A":'24', "B":'12', "C":'6', "D":'48'},"answer":'A'},

{"id":26,"subject":'Biology',"topic":'Cell Cycle & Division',"difficulty":'Hard',
 "question":'The G0 phase refers to a state in which a cell:',
 "options":{"A":'Is actively dividing rapidly', "B":'Has exited the active cell cycle and is not preparing to divide, often permanently or temporarily', "C":'Is in the middle of mitosis', "D":'Has just completed cytokinesis'},"answer":'B'},

{"id":27,"subject":'Biology',"topic":'Cell Cycle & Division',"difficulty":'Medium',
 "question":'A benign tumor differs from a malignant tumor mainly in that a benign tumor:',
 "options":{"A":'Spreads to other parts of the body (metastasizes)', "B":'Is always fatal', "C":'Remains localized and does not invade surrounding tissue or spread to distant sites', "D":'Never involves abnormal cell growth'},"answer":'C'},

{"id":28,"subject":'Biology',"topic":'Genetics',"difficulty":'Easy',
 "question":'In pea plants, purple flowers (P) are dominant over white (p). Crossing two white-flowered plants (pp x pp) will produce offspring that are:',
 "options":{"A":'All purple', "B":'1 purple : 1 white', "C":'3 purple : 1 white', "D":'All white'},"answer":'D'},

{"id":29,"subject":'Biology',"topic":'Genetics',"difficulty":'Medium',
 "question":'If a plant with genotype Pp is self-pollinated, what proportion of the offspring is expected to be white-flowered (pp)?',
 "options":{"A":'25%', "B":'0%', "C":'50%', "D":'75%'},"answer":'A'},

{"id":30,"subject":'Biology',"topic":'Genetics',"difficulty":'Medium',
 "question":'A woman who is a carrier for an X-linked recessive disorder (XAXa) has children with an unaffected man (XAY). What proportion of her sons is expected to be affected?',
 "options":{"A":'0%', "B":'50%', "C":'25%', "D":'100%'},"answer":'B'},

{"id":31,"subject":'Biology',"topic":'Genetics',"difficulty":'Hard',
 "question":'In a dihybrid cross between AaBb and aaBb, assuming independent assortment, what fraction of offspring is expected to be Aabb?',
 "options":{"A":'1/4', "B":'1/16', "C":'1/8', "D":'3/8'},"answer":'C'},

{"id":32,"subject":'Biology',"topic":'Genetics',"difficulty":'Medium',
 "question":'A child has blood type O. Which of the following parental blood type combinations would be IMPOSSIBLE for this child?',
 "options":{"A":'A and B', "B":'A and O', "C":'O and O', "D":'AB and AB'},"answer":'D'},

{"id":33,"subject":'Biology',"topic":'Genetics',"difficulty":'Hard',
 "question":'The pedigree chart shows a trait that skips generations, appears in both males and females equally, and occurs in children of two unaffected parents who must both be carriers. Based on this autosomal recessive pattern, what is the expected proportion of affected children when two carrier (heterozygous) individuals shown in the pedigree have children together?',
 "image":'images/q_pedigree_autosomal_recessive.png',
 "options":{"A":'25%', "B":'0%', "C":'50%', "D":'100%'},"answer":'A'},

{"id":34,"subject":'Biology',"topic":'Genetics',"difficulty":'Medium',
 "question":'In snapdragons, a cross between a red-flowered (RR) and white-flowered (WW) plant produces all pink-flowered (RW) offspring, with intermediate color rather than a blend of spots. This is an example of:',
 "options":{"A":'Codominance', "B":'Incomplete dominance', "C":'Epistasis', "D":'Complete dominance'},"answer":'B'},

{"id":35,"subject":'Biology',"topic":'Molecular Biology',"difficulty":'Easy',
 "question":'The sequence of bases along a DNA molecule ultimately determines the sequence of:',
 "options":{"A":'Lipids in a membrane', "B":'Carbohydrates in a cell wall', "C":'Amino acids in a protein', "D":'Water molecules in a cell'},"answer":'C'},

{"id":36,"subject":'Biology',"topic":'Molecular Biology',"difficulty":'Easy',
 "question":'In DNA replication, the enzyme that joins Okazaki fragments together is:',
 "options":{"A":'DNA polymerase', "B":'Primase', "C":'Helicase', "D":'DNA ligase'},"answer":'D'},

{"id":37,"subject":'Biology',"topic":'Molecular Biology',"difficulty":'Medium',
 "question":'Which of the following correctly describes the direction of mRNA synthesis relative to its DNA template strand?',
 "options":{"A":"mRNA is synthesized 5' to 3', antiparallel to the 3' to 5' template strand", "B":"mRNA is synthesized 3' to 5', parallel to the template strand", "C":'mRNA synthesis direction is random', "D":'mRNA is synthesized in both directions simultaneously'},"answer":'A'},

{"id":38,"subject":'Biology',"topic":'Molecular Biology',"difficulty":'Medium',
 "question":'The process by which mature mRNA leaves the nucleus to be translated in the cytoplasm requires passage through:',
 "options":{"A":'The Golgi apparatus', "B":'Nuclear pores in the nuclear envelope', "C":'The cell wall', "D":'The plasma membrane directly'},"answer":'B'},

{"id":39,"subject":'Biology',"topic":'Molecular Biology',"difficulty":'Medium',
 "question":'A large-scale chromosomal mutation in which an entire chromosome segment is lost is called a:',
 "options":{"A":'Duplication', "B":'Inversion', "C":'Deletion', "D":'Translocation'},"answer":'C'},

{"id":40,"subject":'Biology',"topic":'Molecular Biology',"difficulty":'Hard',
 "question":'A chromosomal mutation in which a segment of one chromosome breaks off and attaches to a different, non-homologous chromosome is called a:',
 "options":{"A":'Deletion', "B":'Duplication', "C":'Inversion', "D":'Translocation'},"answer":'D'},

{"id":41,"subject":'Biology',"topic":'Molecular Biology',"difficulty":'Hard',
 "question":'Operons, such as the lac operon in bacteria, allow for:',
 "options":{"A":'Coordinated regulation of multiple genes involved in a related metabolic pathway, transcribed together as a single mRNA', "B":'Individual regulation of each gene completely independently', "C":'No regulation of gene expression at all', "D":'Regulation only in eukaryotic cells'},"answer":'A'},

{"id":42,"subject":'Biology',"topic":'Molecular Biology',"difficulty":'Medium',
 "question":'Which of the following bases is found in RNA but not in DNA?',
 "options":{"A":'Adenine', "B":'Uracil', "C":'Guanine', "D":'Cytosine'},"answer":'B'},

{"id":43,"subject":'Biology',"topic":'Molecular Biology',"difficulty":'Medium',
 "question":'A silencer, in the context of gene regulation, is a DNA sequence that, when bound by specific proteins:',
 "options":{"A":'Increases the rate of transcription', "B":'Has no effect on transcription', "C":'Decreases or represses the rate of transcription', "D":'Codes for a repressor protein directly'},"answer":'C'},

{"id":44,"subject":'Biology',"topic":'Molecular Biology',"difficulty":'Easy',
 "question":"What is the complementary strand (written 5' to 3') for the DNA sequence 5'-ATGC-3'?",
 "options":{"A":"5'-TACG-3'", "B":"5'-ATGC-3'", "C":"5'-CGAT-3'", "D":"5'-GCAT-3'"},"answer":'D'},

{"id":45,"subject":'Biology',"topic":'Evolution',"difficulty":'Easy',
 "question":"Descent with modification, the core idea behind Darwin's theory, refers to the concept that:",
 "options":{"A":'Species change over time and are descended from common ancestors', "B":'Species remain unchanged across generations', "C":'All species were created independently and simultaneously', "D":'Only humans undergo evolutionary change'},"answer":'A'},

{"id":46,"subject":'Biology',"topic":'Evolution',"difficulty":'Medium',
 "question":'Sexual selection, a specific form of natural selection, occurs when:',
 "options":{"A":'Traits that increase survival are favored regardless of reproduction', "B":"Certain traits increase an individual's chances of attracting mates or competing for them, even if the traits don't directly aid survival", "C":'All individuals in a population have equal reproductive success', "D":'Mutation is the only source of variation'},"answer":'B'},

{"id":47,"subject":'Biology',"topic":'Evolution',"difficulty":'Medium',
 "question":'The founder effect occurs when:',
 "options":{"A":'A large, established population undergoes significant genetic change', "B":'Two populations merge into one with increased diversity', "C":"A small group of individuals establishes a new population, carrying only a subset of the original population's genetic variation", "D":'No genetic change occurs in a new population'},"answer":'C'},

{"id":48,"subject":'Biology',"topic":'Evolution',"difficulty":'Hard',
 "question":'In a population, the frequency of a recessive allele (q) is 0.1. Assuming Hardy-Weinberg equilibrium, what percentage of the population is expected to be heterozygous carriers?',
 "options":{"A":'1%', "B":'10%', "C":'81%', "D":'18%'},"answer":'D'},

{"id":49,"subject":'Biology',"topic":'Classification & Diversity',"difficulty":'Easy',
 "question":'The kingdom that includes multicellular, heterotrophic organisms with cell walls made of chitin is:',
 "options":{"A":'Fungi', "B":'Plantae', "C":'Animalia', "D":'Protista'},"answer":'A'},

{"id":50,"subject":'Biology',"topic":'Classification & Diversity',"difficulty":'Easy',
 "question":'A dichotomous key uses paired statements to help identify an organism based on:',
 "options":{"A":'Its exact age', "B":'Observable physical characteristics', "C":'Its genome sequence only', "D":'Its geographic location alone'},"answer":'B'},

{"id":51,"subject":'Biology',"topic":'Classification & Diversity',"difficulty":'Medium',
 "question":'Which of the following best describes the relationship between domain and kingdom in modern classification?',
 "options":{"A":'Kingdom is a broader category that contains domains', "B":'Domain and kingdom are identical categories', "C":'Domain is the broadest taxonomic category, containing one or more kingdoms', "D":'Domain applies only to bacteria'},"answer":'C'},

{"id":52,"subject":'Biology',"topic":'Classification & Diversity',"difficulty":'Medium',
 "question":'An organism with a segmented body, a hard exoskeleton made of chitin, and jointed appendages most likely belongs to phylum:',
 "options":{"A":'Annelida', "B":'Echinodermata', "C":'Mollusca', "D":'Arthropoda'},"answer":'D'},

{"id":53,"subject":'Biology',"topic":'Classification & Diversity',"difficulty":'Easy',
 "question":'Which taxonomic category is the most specific and narrowest in scope?',
 "options":{"A":'Species', "B":'Genus', "C":'Family', "D":'Order'},"answer":'A'},

{"id":54,"subject":'Biology',"topic":'Classification & Diversity',"difficulty":'Medium',
 "question":'Members of class Mammalia are characterized by having:',
 "options":{"A":'Feathers and a beak', "B":'Mammary glands, hair, and (typically) live birth', "C":'Scales and cold-bloodedness', "D":'Gills throughout their entire life'},"answer":'B'},

{"id":55,"subject":'Biology',"topic":'Plant Biology',"difficulty":'Easy',
 "question":'The process by which plants convert light energy into chemical energy stored in glucose is called:',
 "options":{"A":'Respiration', "B":'Transpiration', "C":'Photosynthesis', "D":'Germination'},"answer":'C'},

{"id":56,"subject":'Biology',"topic":'Plant Biology',"difficulty":'Medium',
 "question":'The overall equation for photosynthesis shows that plants use carbon dioxide and water to produce glucose and:',
 "options":{"A":'Nitrogen gas', "B":'Methane', "C":'Carbon monoxide', "D":'Oxygen gas'},"answer":'D'},

{"id":57,"subject":'Biology',"topic":'Plant Biology',"difficulty":'Medium',
 "question":"Root hairs increase a root's surface area, allowing for greater absorption of:",
 "options":{"A":'Water and dissolved minerals from the soil', "B":'Sunlight', "C":'Carbon dioxide', "D":'Oxygen from the air'},"answer":'A'},

{"id":58,"subject":'Biology',"topic":'Plant Biology',"difficulty":'Hard',
 "question":'Which of the following best explains why C3 plants are generally more efficient than C4 plants in cool, moist climates with normal atmospheric CO2 levels?',
 "options":{"A":'C3 plants require less water and sunlight overall', "B":'C4 photosynthesis has additional energy costs that are only advantageous in hot, dry, high-light conditions where photorespiration is otherwise a major problem', "C":'C4 plants cannot survive in cool climates at all', "D":'C3 plants lack chlorophyll'},"answer":'B'},

{"id":59,"subject":'Biology',"topic":'Plant Biology',"difficulty":'Medium',
 "question":'Abscisic acid (ABA), a plant hormone, plays a key role in:',
 "options":{"A":'Promoting rapid cell division', "B":'Stimulating fruit ripening exclusively', "C":'Inducing stomatal closure during water stress and maintaining seed dormancy', "D":'Promoting stem elongation'},"answer":'C'},

{"id":60,"subject":'Biology',"topic":'Plant Biology',"difficulty":'Easy',
 "question":'The process by which a plant loses excess water vapor through its stomata is called:',
 "options":{"A":'Photosynthesis', "B":'Guttation', "C":'Respiration', "D":'Transpiration'},"answer":'D'},

{"id":61,"subject":'Biology',"topic":'Human Physiology - Digestion',"difficulty":'Easy',
 "question":'Chemical digestion of proteins begins in the:',
 "options":{"A":'Stomach', "B":'Mouth', "C":'Small intestine', "D":'Esophagus'},"answer":'A'},

{"id":62,"subject":'Biology',"topic":'Human Physiology - Digestion',"difficulty":'Medium',
 "question":'The enzyme lactase, found in the small intestine, is responsible for breaking down:',
 "options":{"A":'Sucrose', "B":'Lactose into glucose and galactose', "C":'Starch into maltose', "D":'Proteins into amino acids'},"answer":'B'},

{"id":63,"subject":'Biology',"topic":'Human Physiology - Digestion',"difficulty":'Medium',
 "question":'Which of the following best describes the function of the epiglottis during swallowing?',
 "options":{"A":'It absorbs nutrients', "B":'It digests carbohydrates', "C":'It closes off the trachea, directing food into the esophagus and preventing aspiration', "D":'It produces saliva'},"answer":'C'},

{"id":64,"subject":'Biology',"topic":'Human Physiology - Digestion',"difficulty":'Hard',
 "question":"Malabsorption of nutrients, such as in celiac disease where the small intestine's villi are damaged, would most directly result in:",
 "options":{"A":'Improved nutrient absorption', "B":'No noticeable effect on digestion', "C":'Increased bile production', "D":'Reduced surface area for absorption, leading to nutrient deficiencies'},"answer":'D'},

{"id":65,"subject":'Biology',"topic":'Human Physiology - Circulation',"difficulty":'Easy',
 "question":'Which blood vessels have valves to prevent the backflow of blood, especially important in the limbs where blood must flow against gravity?',
 "options":{"A":'Veins', "B":'Arteries', "C":'Capillaries', "D":'Arterioles'},"answer":'A'},

{"id":66,"subject":'Biology',"topic":'Human Physiology - Circulation',"difficulty":'Medium',
 "question":'The pulmonary vein is unique among veins in that it carries:',
 "options":{"A":'Deoxygenated blood, as all veins do', "B":'Oxygenated blood, from the lungs to the heart', "C":'No blood at all, only lymph', "D":'Blood only during exercise'},"answer":'B'},

{"id":67,"subject":'Biology',"topic":'Human Physiology - Circulation',"difficulty":'Medium',
 "question":'Platelets are formed from fragments of large cells in the bone marrow called:',
 "options":{"A":'Erythrocytes', "B":'Lymphocytes', "C":'Megakaryocytes', "D":'Neutrophils'},"answer":'C'},

{"id":68,"subject":'Biology',"topic":'Human Physiology - Circulation',"difficulty":'Hard',
 "question":"The 'lub-dub' sound of a heartbeat, heard through a stethoscope, is caused mainly by:",
 "options":{"A":"Blood flowing through the heart's chambers", "B":"The opening of the heart's valves", "C":'The contraction of cardiac muscle fibers directly', "D":"The closing of the heart's valves (AV valves for 'lub,' semilunar valves for 'dub')"},"answer":'D'},

{"id":69,"subject":'Biology',"topic":'Human Physiology - Respiration',"difficulty":'Easy',
 "question":'Which structure prevents food and liquids from entering the trachea during swallowing?',
 "options":{"A":'Epiglottis', "B":'Larynx', "C":'Alveoli', "D":'Bronchioles'},"answer":'A'},

{"id":70,"subject":'Biology',"topic":'Human Physiology - Respiration',"difficulty":'Medium',
 "question":'The diaphragm and external intercostal muscles contract during:',
 "options":{"A":'Passive exhalation', "B":'Inhalation, increasing the volume of the thoracic cavity', "C":"Holding one's breath only", "D":'Coughing exclusively'},"answer":'B'},

{"id":71,"subject":'Biology',"topic":'Human Physiology - Respiration',"difficulty":'Medium',
 "question":'Residual volume refers to:',
 "options":{"A":'The total volume of air the lungs can hold', "B":'The volume of air in a normal breath', "C":'The volume of air that remains in the lungs even after a maximal exhalation', "D":'The maximum volume that can be inhaled'},"answer":'C'},

{"id":72,"subject":'Biology',"topic":'Human Physiology - Excretion',"difficulty":'Easy',
 "question":"The structures within the kidney where blood filtration occurs, consisting of a glomerulus surrounded by Bowman's capsule, are called:",
 "options":{"A":'Villi', "B":'Alveoli', "C":'Neurons', "D":'Nephrons'},"answer":'D'},

{"id":73,"subject":'Biology',"topic":'Human Physiology - Excretion',"difficulty":'Medium',
 "question":'Which hormone increases the reabsorption of sodium ions (and consequently water) in the distal convoluted tubule and collecting duct?',
 "options":{"A":'Aldosterone', "B":'Insulin', "C":'Glucagon', "D":'Thyroid hormone'},"answer":'A'},

{"id":74,"subject":'Biology',"topic":'Human Physiology - Excretion',"difficulty":'Hard',
 "question":'Kidney stones can form when substances such as calcium oxalate crystallize within the urinary tract mainly due to:',
 "options":{"A":'Excessive water intake diluting the urine', "B":'Supersaturation of certain minerals in urine, allowing crystals to form and aggregate', "C":'Complete absence of minerals in the diet', "D":'Overactive bladder muscles'},"answer":'B'},

{"id":75,"subject":'Biology',"topic":'Human Physiology - Nervous & Endocrine',"difficulty":'Easy',
 "question":'The nervous system division that includes the brain and spinal cord is the:',
 "options":{"A":'Peripheral nervous system', "B":'Autonomic nervous system', "C":'Central nervous system', "D":'Somatic nervous system'},"answer":'C'},

{"id":76,"subject":'Biology',"topic":'Human Physiology - Nervous & Endocrine',"difficulty":'Medium',
 "question":'A reflex arc typically involves signal transmission through which basic pathway?',
 "options":{"A":'Sensory neuron directly to muscle, bypassing the spinal cord entirely', "B":'Brain to muscle only, with no spinal cord involvement', "C":'Motor neuron to sensory neuron only', "D":'Sensory neuron to spinal cord (often via an interneuron) to motor neuron to effector'},"answer":'D'},

{"id":77,"subject":'Biology',"topic":'Human Physiology - Nervous & Endocrine',"difficulty":'Medium',
 "question":'The hormone prolactin, secreted by the anterior pituitary, primarily stimulates:',
 "options":{"A":'Milk production in the mammary glands', "B":'Uterine contractions', "C":'Growth of bones', "D":'Regulation of blood pressure'},"answer":'A'},

{"id":78,"subject":'Biology',"topic":'Human Physiology - Nervous & Endocrine',"difficulty":'Hard',
 "question":'A tumor on the anterior pituitary gland that causes excessive growth hormone secretion in an adult (after growth plates have fused) would most likely result in a condition called:',
 "options":{"A":'Gigantism', "B":'Acromegaly, characterized by enlargement of extremities and facial features', "C":'Dwarfism', "D":'Diabetes insipidus'},"answer":'B'},

{"id":79,"subject":'Biology',"topic":'Human Physiology - Reproduction',"difficulty":'Easy',
 "question":'The male gonads, responsible for producing sperm and testosterone, are the:',
 "options":{"A":'Ovaries', "B":'Epididymis', "C":'Testes', "D":'Prostate gland'},"answer":'C'},

{"id":80,"subject":'Biology',"topic":'Human Physiology - Reproduction',"difficulty":'Medium',
 "question":'During the luteal phase of the menstrual cycle, the corpus luteum primarily secretes:',
 "options":{"A":'FSH', "B":'GnRH', "C":'LH', "D":'Progesterone, which maintains the uterine lining'},"answer":'D'},

{"id":81,"subject":'Biology',"topic":'Ecology',"difficulty":'Medium',
 "question":'Two species that both rely on the same limited food source, but one is more efficient at exploiting it, may eventually lead to the less efficient species being:',
 "options":{"A":'Competitively excluded from that niche', "B":'Unaffected entirely', "C":'Immediately extinct everywhere', "D":'More successful over time'},"answer":'A'},

# ============================================================
# CHEMISTRY (45) - id 82-126
# ============================================================

{"id":82,"subject":'Chemistry',"topic":'Atomic Structure',"difficulty":'Easy',
 "question":'The nucleus of an atom contains:',
 "options":{"A":'Protons and electrons', "B":'Protons and neutrons', "C":'Electrons and neutrons', "D":'Only electrons'},"answer":'B'},

{"id":83,"subject":'Chemistry',"topic":'Atomic Structure',"difficulty":'Medium',
 "question":'An atom of calcium-40 (atomic number 20) contains how many neutrons?',
 "options":{"A":'60', "B":'40', "C":'20', "D":'10'},"answer":'C'},

{"id":84,"subject":'Chemistry',"topic":'Atomic Structure',"difficulty":'Medium',
 "question":'The maximum number of electrons that can occupy a single s orbital is:',
 "options":{"A":'14', "B":'6', "C":'10', "D":'2'},"answer":'D'},

{"id":85,"subject":'Chemistry',"topic":'Atomic Structure',"difficulty":'Hard',
 "question":'An atom has 15 protons and forms an ion with a -3 charge. How many electrons does this ion have?',
 "options":{"A":'18', "B":'15', "C":'12', "D":'3'},"answer":'A'},

{"id":86,"subject":'Chemistry',"topic":'Periodic Table',"difficulty":'Easy',
 "question":'Elements in Group 17 of the periodic table are called:',
 "options":{"A":'Alkali metals', "B":'Halogens', "C":'Noble gases', "D":'Alkaline earth metals'},"answer":'B'},

{"id":87,"subject":'Chemistry',"topic":'Periodic Table',"difficulty":'Medium',
 "question":'Which of the following correctly describes the trend in atomic radius down a group of the periodic table?',
 "options":{"A":'Atomic radius generally decreases', "B":'Atomic radius remains constant', "C":'Atomic radius generally increases, due to additional electron shells', "D":'Atomic radius becomes negative'},"answer":'C'},

{"id":88,"subject":'Chemistry',"topic":'Periodic Table',"difficulty":'Medium',
 "question":'An element with a very high ionization energy and a strong tendency to gain (rather than lose) electrons would most likely be located:',
 "options":{"A":'On the far left of the periodic table', "B":'At the bottom of any group', "C":'In the middle of the periodic table (transition metals)', "D":'On the far right of the periodic table (excluding noble gases)'},"answer":'D'},

{"id":89,"subject":'Chemistry',"topic":'Chemical Bonding',"difficulty":'Easy',
 "question":'The type of bond formed between two nonmetal atoms that share electrons is called a(n):',
 "options":{"A":'Covalent bond', "B":'Ionic bond', "C":'Metallic bond', "D":'Hydrogen bond'},"answer":'A'},

{"id":90,"subject":'Chemistry',"topic":'Chemical Bonding',"difficulty":'Medium',
 "question":'According to VSEPR theory, a molecule with three bonding pairs and one lone pair on the central atom (e.g., NH3) has an electron geometry of tetrahedral but a molecular shape of:',
 "options":{"A":'Tetrahedral', "B":'Trigonal pyramidal', "C":'Trigonal planar', "D":'Linear'},"answer":'B'},

{"id":91,"subject":'Chemistry',"topic":'Chemical Bonding',"difficulty":'Medium',
 "question":'Which of the following best explains why methane (CH4) is a nonpolar molecule?',
 "options":{"A":'It contains ionic bonds', "B":'It has no bonds at all', "C":'Its symmetrical tetrahedral shape causes the four polar C-H bond dipoles to cancel out', "D":'Carbon and hydrogen have identical electronegativities'},"answer":'C'},

{"id":92,"subject":'Chemistry',"topic":'Chemical Bonding',"difficulty":'Hard',
 "question":'The strength of a covalent bond is generally related to:',
 "options":{"A":'Bond length alone, with no relation to bond order', "B":'The state of matter of the compound', "C":'The color of the compound', "D":'Bond order, with triple bonds generally being stronger and shorter than double or single bonds between the same two atoms'},"answer":'D'},

{"id":93,"subject":'Chemistry',"topic":'States of Matter',"difficulty":'Easy',
 "question":'According to the kinetic molecular theory, particles in a gas:',
 "options":{"A":'Move rapidly and randomly, with large distances between particles compared to their size', "B":'Are tightly packed and vibrate in fixed positions', "C":'Do not move at all', "D":'Are arranged in a fixed, orderly lattice'},"answer":'A'},

{"id":94,"subject":'Chemistry',"topic":'States of Matter',"difficulty":'Medium',
 "question":'A gas occupies 10.0 L at a pressure of 1.0 atm. What volume will it occupy at 4.0 atm, assuming constant temperature?',
 "options":{"A":'40.0 L', "B":'2.5 L', "C":'10.0 L', "D":'4.0 L'},"answer":'B'},

{"id":95,"subject":'Chemistry',"topic":'States of Matter',"difficulty":'Hard',
 "question":"A sealed container holds gas at 3 atm and 350 K. If the container's volume is halved and the temperature is raised to 700 K, what is the new pressure?",
 "options":{"A":'3 atm', "B":'6 atm', "C":'12 atm', "D":'1.5 atm'},"answer":'C'},

{"id":96,"subject":'Chemistry',"topic":'Stoichiometry',"difficulty":'Easy',
 "question":'The molar mass of calcium carbonate (CaCO3) is approximately:',
 "options":{"A":'60 g/mol', "B":'116 g/mol', "C":'78 g/mol', "D":'100 g/mol'},"answer":'D'},

{"id":97,"subject":'Chemistry',"topic":'Stoichiometry',"difficulty":'Medium',
 "question":'How many moles of chlorine atoms are present in 4 moles of CaCl2?',
 "options":{"A":'8', "B":'4', "C":'2', "D":'6'},"answer":'A'},

{"id":98,"subject":'Chemistry',"topic":'Stoichiometry',"difficulty":'Hard',
 "question":'A 600 mL solution contains 18 g of NaCl (molar mass 58.5 g/mol). What is the approximate molarity of the solution?',
 "options":{"A":'0.31 M', "B":'0.51 M', "C":'0.18 M', "D":'1.03 M'},"answer":'B'},

{"id":99,"subject":'Chemistry',"topic":'Stoichiometry',"difficulty":'Medium',
 "question":'In the reaction 2H2O2 -> 2H2O + O2, how many moles of O2 gas are produced from the decomposition of 6 moles of H2O2?',
 "options":{"A":'6', "B":'12', "C":'3', "D":'2'},"answer":'C'},

{"id":100,"subject":'Chemistry',"topic":'Thermochemistry',"difficulty":'Easy',
 "question":'An endothermic reaction is one that:',
 "options":{"A":'Releases heat to the surroundings', "B":'Only occurs at very low temperatures', "C":'Involves no energy change at all', "D":'Absorbs heat from the surroundings'},"answer":'D'},

{"id":101,"subject":'Chemistry',"topic":'Thermochemistry',"difficulty":'Medium',
 "question":'The enthalpy change (delta H) of a reaction is calculated as:',
 "options":{"A":'The enthalpy of the products minus the enthalpy of the reactants', "B":'The enthalpy of the reactants minus the enthalpy of the products', "C":'The sum of the enthalpies of both reactants and products', "D":'Always a positive number regardless of reaction type'},"answer":'A'},

{"id":102,"subject":'Chemistry',"topic":'Chemical Equilibrium',"difficulty":'Medium',
 "question":'For the equilibrium reaction CO(g) + H2O(g) <-> CO2(g) + H2(g), which has equal moles of gas on both sides, changing pressure by changing volume will:',
 "options":{"A":'Strongly shift equilibrium toward products', "B":'Have essentially no effect on the equilibrium position', "C":'Strongly shift equilibrium toward reactants', "D":'Completely stop the reaction'},"answer":'B'},

{"id":103,"subject":'Chemistry',"topic":'Chemical Equilibrium',"difficulty":'Hard',
 "question":'A reaction has Keq = 1 at a given temperature. This indicates that at equilibrium:',
 "options":{"A":'The reaction strongly favors products', "B":'The reaction strongly favors reactants', "C":'The concentrations of products and reactants are comparable, in a ratio reflecting the stoichiometry', "D":'No reaction is occurring'},"answer":'C'},

{"id":104,"subject":'Chemistry',"topic":'Reaction Kinetics',"difficulty":'Easy',
 "question":'A reaction proceeds faster in the presence of a catalyst mainly because the catalyst:',
 "options":{"A":'Increases the temperature of the reaction', "B":'Removes reactants from the system', "C":'Increases the concentration of reactants', "D":'Provides an alternative reaction pathway with a lower activation energy'},"answer":'D'},

{"id":105,"subject":'Chemistry',"topic":'Reaction Kinetics',"difficulty":'Medium',
 "question":'The half-life of a first-order reaction is:',
 "options":{"A":'Constant, independent of the initial concentration of reactant', "B":'Dependent on the initial concentration of reactant', "C":'Always equal to zero', "D":'Always increasing over time'},"answer":'A'},

{"id":106,"subject":'Chemistry',"topic":'Electrochemistry',"difficulty":'Medium',
 "question":'In a galvanic cell, the electrode where oxidation takes place is called the:',
 "options":{"A":'Cathode', "B":'Anode', "C":'Salt bridge', "D":'Reference electrode'},"answer":'B'},

{"id":107,"subject":'Chemistry',"topic":'Electrochemistry',"difficulty":'Hard',
 "question":'In the reaction Fe(s) + 2HCl(aq) -> FeCl2(aq) + H2(g), iron is:',
 "options":{"A":'Reduced', "B":'Neither oxidized nor reduced', "C":'Oxidized', "D":'Acting only as a catalyst'},"answer":'C'},

{"id":108,"subject":'Chemistry',"topic":'Acids & Bases',"difficulty":'Easy',
 "question":'A solution with a pH greater than 7 is classified as:',
 "options":{"A":'Acidic', "B":'Amphoteric', "C":'Neutral', "D":'Basic'},"answer":'D'},

{"id":109,"subject":'Chemistry',"topic":'Acids & Bases',"difficulty":'Medium',
 "question":'A solution has a pH of 5. What is its hydrogen ion concentration, [H+]?',
 "options":{"A":'1x10^-5 M', "B":'5 M', "C":'1x10^5 M', "D":'0.5 M'},"answer":'A'},

{"id":110,"subject":'Chemistry',"topic":'Acids & Bases',"difficulty":'Medium',
 "question":'The conjugate base of a Bronsted-Lowry acid is formed when the acid:',
 "options":{"A":'Gains a proton', "B":'Loses a proton (H+)', "C":'Gains an electron pair', "D":'Loses an electron pair'},"answer":'B'},

{"id":111,"subject":'Chemistry',"topic":'Acids & Bases',"difficulty":'Hard',
 "question":'A solution containing a weak acid and its conjugate base (a buffer) has its greatest buffering capacity when:',
 "options":{"A":'The concentrations of the weak acid and conjugate base are very different', "B":'Only the weak acid is present, with no conjugate base', "C":'The concentrations of the weak acid and conjugate base are approximately equal', "D":'The solution is diluted to near-zero concentration'},"answer":'C'},

{"id":112,"subject":'Chemistry',"topic":'Organic Chemistry',"difficulty":'Easy',
 "question":'The simplest alkane, containing only one carbon atom, is:',
 "options":{"A":'Ethane', "B":'Butane', "C":'Propane', "D":'Methane'},"answer":'D'},

{"id":113,"subject":'Chemistry',"topic":'Organic Chemistry',"difficulty":'Medium',
 "question":'Which of the following reactions is typical of alkanes, involving the replacement of a hydrogen atom with another atom or group?',
 "options":{"A":'Substitution reaction', "B":'Addition reaction', "C":'Elimination reaction', "D":'Polymerization reaction'},"answer":'A'},

{"id":114,"subject":'Chemistry',"topic":'Organic Chemistry',"difficulty":'Medium',
 "question":'A secondary amine has its nitrogen atom bonded to how many carbon-containing groups?',
 "options":{"A":'One', "B":'Two', "C":'Three', "D":'Zero'},"answer":'B'},

{"id":115,"subject":'Chemistry',"topic":'Organic Chemistry',"difficulty":'Hard',
 "question":'Which factor most strongly favors an SN1 mechanism over an SN2 mechanism in a nucleophilic substitution reaction?',
 "options":{"A":'A primary substrate with a strong nucleophile', "B":'A polar protic solvent has no effect on the mechanism', "C":'A tertiary substrate, which forms a relatively stable carbocation intermediate', "D":'The absence of any leaving group'},"answer":'C'},

{"id":116,"subject":'Chemistry',"topic":'Organic Chemistry',"difficulty":'Medium',
 "question":'Which functional group, when present in a molecule, characterizes an amide?',
 "options":{"A":'-COOH', "B":'-OH', "C":'-CHO', "D":'-CONH2'},"answer":'D'},

{"id":117,"subject":'Chemistry',"topic":'Organic Chemistry',"difficulty":'Easy',
 "question":'Two compounds with the same molecular formula but different structural arrangements are called:',
 "options":{"A":'Isomers', "B":'Allotropes', "C":'Isotopes', "D":'Ions'},"answer":'A'},

{"id":118,"subject":'Chemistry',"topic":'Inorganic Chemistry',"difficulty":'Medium',
 "question":'Which of the following best explains why noble gases are placed in Group 18 of the periodic table?',
 "options":{"A":'They have only one valence electron', "B":'They have a full valence electron shell, making them largely chemically unreactive', "C":'They readily form ionic bonds', "D":'They are highly reactive metals'},"answer":'B'},

{"id":119,"subject":'Chemistry',"topic":'Inorganic Chemistry',"difficulty":'Medium',
 "question":'The general reactivity trend of halogens (Group 17) with metals is that reactivity:',
 "options":{"A":'Increases down the group', "B":'Remains constant throughout the group', "C":'Decreases down the group, as atomic radius increases and electron affinity becomes less favorable', "D":'Is unrelated to atomic radius'},"answer":'C'},

{"id":120,"subject":'Chemistry',"topic":'Inorganic Chemistry',"difficulty":'Hard',
 "question":"In the reaction 2Na + 2H2O -> 2NaOH + H2, hydrogen's oxidation state changes from:",
 "options":{"A":'No change occurs', "B":'0 to +1 (oxidation)', "C":'-1 to +1', "D":'+1 to 0 (reduction)'},"answer":'D'},

{"id":121,"subject":'Chemistry',"topic":'Physical Chemistry',"difficulty":'Medium',
 "question":'The graph shows the solubility (in grams per 100 mL of water) of a solid salt plotted against temperature. Based on the graph, as temperature increases, the solubility of this salt:',
 "image":'images/q_solubility_curve_graph.png',
 "options":{"A":'Increases', "B":'Decreases', "C":'Remains constant', "D":'Cannot be determined from a solubility curve'},"answer":'A'},

{"id":122,"subject":'Chemistry',"topic":'Physical Chemistry',"difficulty":'Hard',
 "question":'50 mL of 0.2 M H2SO4 is required to neutralize 25 mL of a NaOH solution (H2SO4 + 2NaOH -> Na2SO4 + 2H2O). What is the molarity of the NaOH solution?',
 "options":{"A":'0.4 M', "B":'0.8 M', "C":'0.2 M', "D":'1.6 M'},"answer":'B'},

{"id":123,"subject":'Chemistry',"topic":'Environmental Chemistry',"difficulty":'Easy',
 "question":'Which of the following gases contributes to acid rain when it reacts with atmospheric water vapor?',
 "options":{"A":'Nitrogen', "B":'Oxygen', "C":'Sulfur dioxide', "D":'Argon'},"answer":'C'},

{"id":124,"subject":'Chemistry',"topic":'Environmental Chemistry',"difficulty":'Medium',
 "question":'Which of the following would most effectively help reduce the buildup of atmospheric carbon dioxide?',
 "options":{"A":'Increased deforestation', "B":'Reduced use of public transportation', "C":'Increased fossil fuel combustion', "D":'Reforestation and afforestation programs'},"answer":'D'},

{"id":125,"subject":'Chemistry',"topic":'Chemical Bonding',"difficulty":'Easy',
 "question":'Molecules held together primarily by weak, temporary attractions due to fluctuating electron distributions exhibit:',
 "options":{"A":'London dispersion forces (a type of van der Waals force)', "B":'Ionic bonding', "C":'Covalent bonding exclusively', "D":'Metallic bonding'},"answer":'A'},

{"id":126,"subject":'Chemistry',"topic":'Atomic Structure',"difficulty":'Easy',
 "question":'The atomic mass of an element, as shown on the periodic table, represents the weighted average mass of:',
 "options":{"A":'Only the most common isotope', "B":'All naturally occurring isotopes of that element, weighted by their abundance', "C":'Only the lightest isotope', "D":'The mass of a single proton'},"answer":'B'},

# ============================================================
# PHYSICS (36) - id 127-162
# ============================================================

{"id":127,"subject":'Physics',"topic":'Kinematics',"difficulty":'Easy',
 "question":'A train covers 150 km in 3 hours at constant speed. What is its speed?',
 "options":{"A":'45 km/h', "B":'450 km/h', "C":'50 km/h', "D":'5 km/h'},"answer":'C'},

{"id":128,"subject":'Physics',"topic":'Kinematics',"difficulty":'Medium',
 "question":'An object decelerates uniformly from 50 m/s to 20 m/s over 6 seconds. What is its deceleration?',
 "options":{"A":'3.3 m/s^2', "B":'30 m/s^2', "C":'8.3 m/s^2', "D":'5 m/s^2'},"answer":'D'},

{"id":129,"subject":'Physics',"topic":'Kinematics',"difficulty":'Hard',
 "question":'A ball is thrown vertically upward with an initial velocity of 25 m/s (g = 10 m/s^2, ignoring air resistance). What is its velocity after 2 seconds?',
 "options":{"A":'5 m/s upward', "B":'15 m/s upward', "C":'20 m/s upward', "D":'45 m/s upward'},"answer":'A'},

{"id":130,"subject":'Physics',"topic":'Dynamics',"difficulty":'Easy',
 "question":'An object remains at rest or continues moving at constant velocity unless acted upon by a net external force. This describes:',
 "options":{"A":"Newton's second law", "B":"Newton's first law", "C":"Newton's third law", "D":'The law of conservation of momentum'},"answer":'B'},

{"id":131,"subject":'Physics',"topic":'Dynamics',"difficulty":'Medium',
 "question":'A 7 kg object experiences a net force of 21 N. What is its resulting acceleration?',
 "options":{"A":'21 m/s^2', "B":'7 m/s^2', "C":'3 m/s^2', "D":'147 m/s^2'},"answer":'C'},

{"id":132,"subject":'Physics',"topic":'Dynamics',"difficulty":'Medium',
 "question":'If the net force on an object is zero, the object is said to be in:',
 "options":{"A":'Uniform acceleration', "B":'Circular motion', "C":'Free fall', "D":'Equilibrium'},"answer":'D'},

{"id":133,"subject":'Physics',"topic":'Dynamics',"difficulty":'Hard',
 "question":"A 4 kg block is pulled with a horizontal force of 20 N across a surface with a coefficient of kinetic friction of 0.25 (g = 10 m/s^2). What is the block's acceleration?",
 "options":{"A":'2.5 m/s^2', "B":'5 m/s^2', "C":'1.5 m/s^2', "D":'10 m/s^2'},"answer":'A'},

{"id":134,"subject":'Physics',"topic":'Work, Energy & Power',"difficulty":'Easy',
 "question":'The joule, the SI unit of work and energy, is equivalent to:',
 "options":{"A":'One newton per meter', "B":'One newton times one meter', "C":'One kilogram per second', "D":'One watt per second'},"answer":'B'},

{"id":135,"subject":'Physics',"topic":'Work, Energy & Power',"difficulty":'Medium',
 "question":'A 5 kg object is raised to a height of 6 m (g = 10 m/s^2). What is its gravitational potential energy?',
 "options":{"A":'30 J', "B":'60 J', "C":'300 J', "D":'11 J'},"answer":'C'},

{"id":136,"subject":'Physics',"topic":'Work, Energy & Power',"difficulty":'Medium',
 "question":'A 2 kg object moving at 8 m/s has a kinetic energy of:',
 "options":{"A":'16 J', "B":'128 J', "C":'32 J', "D":'64 J'},"answer":'D'},

{"id":137,"subject":'Physics',"topic":'Work, Energy & Power',"difficulty":'Hard',
 "question":'A machine performs 15000 J of work in 30 seconds. What is its power output?',
 "options":{"A":'500 W', "B":'450000 W', "C":'45000 W', "D":'50 W'},"answer":'A'},

{"id":138,"subject":'Physics',"topic":'Circular Motion & Gravitation',"difficulty":'Easy',
 "question":'In circular motion, the force that continuously pulls an object toward the center of its circular path is called the:',
 "options":{"A":'Gravitational force', "B":'Centripetal force', "C":'Normal force', "D":'Applied force'},"answer":'B'},

{"id":139,"subject":'Physics',"topic":'Circular Motion & Gravitation',"difficulty":'Medium',
 "question":"According to Newton's law of gravitation, if the distance between two objects is halved while both masses remain the same, the gravitational force between them becomes:",
 "options":{"A":'Half the original', "B":'Double the original', "C":'Four times the original', "D":'One quarter of the original'},"answer":'C'},

{"id":140,"subject":'Physics',"topic":'Circular Motion & Gravitation',"difficulty":'Hard',
 "question":'Two planets have the same radius, but Planet X has twice the mass of Planet Y. Compared to Planet Y, the surface gravity on Planet X is:',
 "options":{"A":'The same as Planet Y', "B":"Half of Planet Y's", "C":"Four times Planet Y's", "D":"Twice Planet Y's"},"answer":'D'},

{"id":141,"subject":'Physics',"topic":'Fluid Mechanics',"difficulty":'Easy',
 "question":'The buoyant force acting on a fully submerged object is equal to the weight of the:',
 "options":{"A":'Fluid displaced by the object', "B":'Object itself', "C":'Container holding the fluid', "D":'Air above the fluid'},"answer":'A'},

{"id":142,"subject":'Physics',"topic":'Fluid Mechanics',"difficulty":'Medium',
 "question":"Pascal's principle states that pressure exerted on a confined, incompressible fluid is:",
 "options":{"A":'Concentrated only near the point where it is applied', "B":'Transmitted equally throughout the fluid in all directions', "C":'Lost as heat within the fluid', "D":'Only transmitted in the direction of gravity'},"answer":'B'},

{"id":143,"subject":'Physics',"topic":'Fluid Mechanics',"difficulty":'Hard',
 "question":"In a hydraulic press, a small force is applied to a small piston (area A1), and a much larger force is generated on a larger piston (area A2). According to Pascal's principle, the relationship between the forces and areas is:",
 "options":{"A":'F1/A2 = F2/A1', "B":'F1*A1 = F2*A2', "C":'F1/A1 = F2/A2', "D":'F1 = F2 regardless of area'},"answer":'C'},

{"id":144,"subject":'Physics',"topic":'Oscillations & Waves',"difficulty":'Easy',
 "question":'The maximum displacement of a wave from its equilibrium (rest) position is called its:',
 "options":{"A":'Wavelength', "B":'Frequency', "C":'Period', "D":'Amplitude'},"answer":'D'},

{"id":145,"subject":'Physics',"topic":'Oscillations & Waves',"difficulty":'Medium',
 "question":'The period of a wave is related to its frequency by the equation:',
 "options":{"A":'T = 1/f', "B":'T = f', "C":'T = f^2', "D":'T = 2f'},"answer":'A'},

{"id":146,"subject":'Physics',"topic":'Oscillations & Waves',"difficulty":'Medium',
 "question":'A wave has a wavelength of 6 m and a period of 3 seconds. What is its speed?',
 "options":{"A":'18 m/s', "B":'2 m/s', "C":'0.5 m/s', "D":'9 m/s'},"answer":'B'},

{"id":147,"subject":'Physics',"topic":'Oscillations & Waves',"difficulty":'Hard',
 "question":'When a moving sound source approaches a stationary observer, the observed frequency of the sound:',
 "options":{"A":'Decreases, due to the Doppler effect', "B":'Remains completely unchanged', "C":'Increases, due to the Doppler effect, as sound waves are compressed in front of the source', "D":'Becomes zero'},"answer":'C'},

{"id":148,"subject":'Physics',"topic":'Thermodynamics',"difficulty":'Easy',
 "question":'Heat transfer that occurs without any physical contact between objects, such as warmth from the sun, is called:',
 "options":{"A":'Conduction', "B":'Convection', "C":'Insulation', "D":'Radiation'},"answer":'D'},

{"id":149,"subject":'Physics',"topic":'Thermodynamics',"difficulty":'Medium',
 "question":'According to the first law of thermodynamics, the change in internal energy of a system equals:',
 "options":{"A":'Heat added to the system minus work done by the system', "B":'Heat added to the system plus work done by the system, regardless of sign convention used', "C":'Only the work done on the system', "D":'Zero, always'},"answer":'A'},

{"id":150,"subject":'Physics',"topic":'Thermodynamics',"difficulty":'Hard',
 "question":'A gas undergoes a process at constant pressure, expanding from 2 L to 5 L against a constant external pressure of 100 kPa. How much work is done BY the gas?',
 "options":{"A":'500 J', "B":'300 J', "C":'200 J', "D":'700 J'},"answer":'B'},

{"id":151,"subject":'Physics',"topic":'Electrostatics',"difficulty":'Easy',
 "question":'Objects with like charges (both positive or both negative) will:',
 "options":{"A":'Attract each other', "B":'Have no interaction', "C":'Repel each other', "D":'Instantly neutralize'},"answer":'C'},

{"id":152,"subject":'Physics',"topic":'Electrostatics',"difficulty":'Medium',
 "question":'The strength of the electric field around a point charge decreases with:',
 "options":{"A":"The charge's mass", "B":'The distance from the charge, becoming stronger farther away', "C":'Time, regardless of distance', "D":'The square of the distance from the charge, becoming weaker farther away'},"answer":'D'},

{"id":153,"subject":'Physics',"topic":'Current Electricity',"difficulty":'Easy',
 "question":'The unit used to measure electric current is the:',
 "options":{"A":'Ampere', "B":'Volt', "C":'Ohm', "D":'Watt'},"answer":'A'},

{"id":154,"subject":'Physics',"topic":'Current Electricity',"difficulty":'Medium',
 "question":'In the circuit shown, R1 (3 ohm) is connected in series with R2 (5 ohm), and this series combination is connected in parallel with R3 (8 ohm). What is the total resistance of the circuit?',
 "image":'images/q_circuit_r1r2_series_r3_parallel.png',
 "options":{"A":'8 ohm', "B":'4 ohm', "C":'16 ohm', "D":'2 ohm'},"answer":'B'},

{"id":155,"subject":'Physics',"topic":'Current Electricity',"difficulty":'Hard',
 "question":'Two resistors, 12 ohm and 4 ohm, are connected in parallel. What is their equivalent resistance?',
 "options":{"A":'16 ohm', "B":'8 ohm', "C":'3 ohm', "D":'6 ohm'},"answer":'C'},

{"id":156,"subject":'Physics',"topic":'Current Electricity',"difficulty":'Medium',
 "question":'A circuit has a total resistance of 5 ohm and carries a current of 4 A. What is the voltage across the circuit?',
 "options":{"A":'1.25 V', "B":'9 V', "C":'80 V', "D":'20 V'},"answer":'D'},

{"id":157,"subject":'Physics',"topic":'Electromagnetism',"difficulty":'Medium',
 "question":'The strength of the magnetic field inside a solenoid can be increased by:',
 "options":{"A":'Increasing the current flowing through the coil', "B":'Decreasing the number of turns in the coil', "C":'Removing the core material', "D":'Decreasing the current'},"answer":'A'},

{"id":158,"subject":'Physics',"topic":'Electromagnetism',"difficulty":'Hard',
 "question":'A transformer works based on the principle of:',
 "options":{"A":'Static electric charge', "B":'Mutual electromagnetic induction between two coils sharing a changing magnetic flux', "C":'Direct current flow only', "D":'Gravitational attraction between coils'},"answer":'B'},

{"id":159,"subject":'Physics',"topic":'Modern Physics',"difficulty":'Easy',
 "question":'The central, dense part of an atom, containing protons and neutrons, is called the:',
 "options":{"A":'Electron cloud', "B":'Valence shell', "C":'Nucleus', "D":'Orbital'},"answer":'C'},

{"id":160,"subject":'Physics',"topic":'Modern Physics',"difficulty":'Medium',
 "question":'Gamma radiation, emitted during certain types of radioactive decay, consists of:',
 "options":{"A":'Helium nuclei', "B":'Neutrons only', "C":'Fast-moving electrons', "D":'High-energy electromagnetic photons'},"answer":'D'},

{"id":161,"subject":'Physics',"topic":'Modern Physics',"difficulty":'Hard',
 "question":'A radioactive sample decays such that 87.5% of the original sample has decayed after 30 minutes. What is the half-life of this sample?',
 "options":{"A":'10 minutes', "B":'15 minutes', "C":'20 minutes', "D":'30 minutes'},"answer":'A'},

{"id":162,"subject":'Physics',"topic":'Optics',"difficulty":'Medium',
 "question":'The ray diagram shows parallel light rays striking a convex lens and converging at a single point after passing through the lens. Based on the diagram, this point of convergence is called the:',
 "image":'images/q_convex_lens_parallel_rays_focus.png',
 "options":{"A":'Center of curvature', "B":'Principal focus (focal point)', "C":'Pole of the lens', "D":'Optical center'},"answer":'B'},

# ============================================================
# ENGLISH (9) - id 163-171
# ============================================================

{"id":163,"subject":'English',"topic":'Synonyms',"difficulty":'Easy',
 "question":"Choose the word most nearly similar in meaning to 'TENACIOUS':",
 "options":{"A":'Indifferent', "B":'Weak', "C":'Persistent', "D":'Fragile'},"answer":'C'},

{"id":164,"subject":'English',"topic":'Antonyms',"difficulty":'Easy',
 "question":"Choose the word most nearly opposite in meaning to 'VERBOSE':",
 "options":{"A":'Wordy', "B":'Talkative', "C":'Lengthy', "D":'Concise'},"answer":'D'},

{"id":165,"subject":'English',"topic":'Grammar',"difficulty":'Easy',
 "question":'Choose the grammatically correct sentence:',
 "options":{"A":'Everybody has to submit their forms by Friday.', "B":'Everybody have to submit their forms by Friday.', "C":'Everybody have to submit his form by Friday.', "D":'Everybody has to submit their form by Fridays.'},"answer":'A'},

{"id":166,"subject":'English',"topic":'Grammar',"difficulty":'Medium',
 "question":'Choose the correct sentence:',
 "options":{"A":'I wish I was taller.', "B":'I wish I were taller.', "C":'I wish I am taller.', "D":'I wish I will be taller.'},"answer":'B'},

{"id":167,"subject":'English',"topic":'Sentence Correction',"difficulty":'Medium',
 "question":'Choose the sentence that is grammatically correct:',
 "options":{"A":'Statistic show that crime rate is declining.', "B":'Statistics shows that crime rate is declining.', "C":'Statistics show that crime rate is declining.', "D":'Statistics shows that crime rates are declining, individually.'},"answer":'C'},

{"id":168,"subject":'English',"topic":'Vocabulary',"difficulty":'Medium',
 "question":"Choose the word that best completes the sentence: 'The lawyer presented ______ evidence that left no doubt about the defendant's innocence.'",
 "options":{"A":'Ambiguous', "B":'Circumstantial', "C":'Flimsy', "D":'Conclusive'},"answer":'D'},

{"id":169,"subject":'English',"topic":'Idioms',"difficulty":'Medium',
 "question":"Choose the meaning closest to the idiom 'to jump on the bandwagon':",
 "options":{"A":'To join a popular activity or trend that others are already doing', "B":'To start a new trend independently', "C":'To criticize a popular idea', "D":'To avoid participating in a group activity'},"answer":'A'},

{"id":170,"subject":'English',"topic":'Sentence Correction',"difficulty":'Hard',
 "question":"Choose the option that best corrects the sentence: 'Being tired, the couch was where she decided to sleep.'",
 "options":{"A":'Being tired, the couch decided she should sleep.', "B":'Being tired, she decided to sleep on the couch.', "C":'The couch, being tired, was where she decided to sleep.', "D":'No correction is needed.'},"answer":'B'},

{"id":171,"subject":'English',"topic":'Prepositions',"difficulty":'Hard',
 "question":"Choose the correct preposition: 'The results of the experiment were consistent ______ the researchers' initial hypothesis.'",
 "options":{"A":'to', "B":'for', "C":'with', "D":'about'},"answer":'C'},

# ============================================================
# LOGICAL REASONING (9) - id 172-180
# ============================================================

{"id":172,"subject":'Logical Reasoning',"topic":'Number Series',"difficulty":'Easy',
 "question":'Find the next number in the series: 2, 5, 10, 17, ?',
 "options":{"A":'24', "B":'28', "C":'25', "D":'26'},"answer":'D'},

{"id":173,"subject":'Logical Reasoning',"topic":'Number Series',"difficulty":'Easy',
 "question":'Find the missing number: 200, 100, 50, 25, ?',
 "options":{"A":'12.5', "B":'15', "C":'10', "D":'5'},"answer":'A'},

{"id":174,"subject":'Logical Reasoning',"topic":'Analogies',"difficulty":'Easy',
 "question":'Painter is to Canvas as Writer is to:',
 "options":{"A":'Pen', "B":'Paper', "C":'Book', "D":'Story'},"answer":'B'},

{"id":175,"subject":'Logical Reasoning',"topic":'Analogies',"difficulty":'Medium',
 "question":'Engine is to Car as Heart is to:',
 "options":{"A":'Blood', "B":'Lungs', "C":'Body', "D":'Brain'},"answer":'C'},

{"id":176,"subject":'Logical Reasoning',"topic":'Blood Relations',"difficulty":'Medium',
 "question":"Pointing to a man, a woman said, 'His son is my son's father.' How is the man related to the woman?",
 "options":{"A":'Brother', "B":'Grandfather', "C":'Husband', "D":'Father-in-law'},"answer":'D'},

{"id":177,"subject":'Logical Reasoning',"topic":'Coding-Decoding',"difficulty":'Medium',
 "question":'If in a certain code, PLANET is written as QMBOFU, how is JUPITER written in the same code?',
 "options":{"A":'KVQJUFS', "B":'KVQJUFR', "C":'JVQJUFS', "D":'KVQIUFS'},"answer":'A'},

{"id":178,"subject":'Logical Reasoning',"topic":'Syllogism',"difficulty":'Hard',
 "question":'All athletes are fit. Some fit people are fast runners. Which conclusion logically follows?',
 "options":{"A":'All athletes are fast runners', "B":'No definite conclusion can be drawn about athletes being fast runners', "C":'Some athletes are fast runners', "D":'No athletes are fast runners'},"answer":'B'},

{"id":179,"subject":'Logical Reasoning',"topic":'Pattern Recognition',"difficulty":'Hard',
 "question":'Find the next term in the series: 4, 9, 16, 25, 36, ?',
 "options":{"A":'42', "B":'47', "C":'49', "D":'45'},"answer":'C'},

{"id":180,"subject":'Logical Reasoning',"topic":'Direction Sense',"difficulty":'Medium',
 "question":'A man walks 12 km south, then turns west and walks 5 km. How far is he from his starting point?',
 "options":{"A":'17 km', "B":'7 km', "C":'60 km', "D":'13 km'},"answer":'D'},

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