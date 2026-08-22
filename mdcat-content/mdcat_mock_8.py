"""
MDCAT Mock Test 8
==================
Full-length mock test: 180 MCQs
Weightage: Biology 81 | Chemistry 45 | Physics 36 | English 9 | Logical Reasoning 9
Difficulty mix (approx): 30% Easy / 50% Medium / 20% Hard, distributed throughout.

Includes 5 image/diagram-based questions (2 Biology, 1 Chemistry, 2 Physics).
Each such question has an "image" key giving a relative path to a PNG diagram
that must be viewed alongside the question (images/ subfolder, shipped alongside
this file). Diagrams: labeled mitochondrion cross-section, an autosomal-dominant
pedigree chart, a strong-acid/strong-base titration curve, a series-parallel
resistor circuit, and a convex-lens ray diagram (object at F).

Each question is a dict:
    id, subject, topic, difficulty, question, [image], options (A-D), answer (correct letter)

Run this file directly to print a summary / sanity-check the paper.
"""

QUESTIONS = [

# ============================================================
# BIOLOGY (81) - id 1-81
# ============================================================

{"id":1,"subject":'Biology',"topic":'Biomolecules',"difficulty":'Easy',
 "question":'Which of the following is a disaccharide formed from glucose and fructose?',
 "options":{"A":'Sucrose', "B":'Maltose', "C":'Lactose', "D":'Glycogen'},"answer":'A'},

{"id":2,"subject":'Biology',"topic":'Biomolecules',"difficulty":'Easy',
 "question":'The monomer units that make up proteins are:',
 "options":{"A":'Amino acids', "B":'Nucleotides', "C":'Monosaccharides', "D":'Fatty acids'},"answer":'A'},

{"id":3,"subject":'Biology',"topic":'Biomolecules',"difficulty":'Medium',
 "question":'Quaternary protein structure refers to:',
 "options":{"A":'The linear sequence of amino acids', "B":'Folding of a single polypeptide into helices or sheets', "C":'The arrangement of two or more polypeptide subunits into a single functional protein complex', "D":'The bonding of a protein to a carbohydrate group'},"answer":'C'},

{"id":4,"subject":'Biology',"topic":'Biomolecules',"difficulty":'Medium',
 "question":'Phospholipids are amphipathic molecules that spontaneously form a bilayer in water mainly because:',
 "options":{"A":'They are entirely hydrophobic', "B":'They dissolve completely in water', "C":'They are entirely hydrophilic', "D":'Their hydrophilic phosphate heads face the water while their hydrophobic tails face each other, away from water'},"answer":'D'},

{"id":5,"subject":'Biology',"topic":'Biomolecules',"difficulty":'Hard',
 "question":'Which of the following correctly ranks the four levels of protein structure from most basic to most complex?',
 "options":{"A":'Primary, secondary, tertiary, quaternary', "B":'Quaternary, tertiary, secondary, primary', "C":'Secondary, primary, quaternary, tertiary', "D":'Tertiary, primary, secondary, quaternary'},"answer":'A'},

{"id":6,"subject":'Biology',"topic":'Enzymes',"difficulty":'Easy',
 "question":'An enzyme is best described chemically as a:',
 "options":{"A":'Biological catalyst, usually a protein', "B":'Carbohydrate', "C":'Lipid', "D":'Nucleic acid that never changes shape'},"answer":'A'},

{"id":7,"subject":'Biology',"topic":'Enzymes',"difficulty":'Medium',
 "question":'Enzyme specificity for a particular substrate is mainly explained by:',
 "options":{"A":'Random binding of any molecule to the enzyme', "B":'Enzymes reacting equally with all molecules', "C":'The complementary shape and chemical properties between the active site and the substrate', "D":'The enzyme permanently changing its own structure after each reaction'},"answer":'C'},

{"id":8,"subject":'Biology',"topic":'Enzymes',"difficulty":'Medium',
 "question":'Irreversible inhibition of an enzyme occurs when an inhibitor:',
 "options":{"A":'Competes reversibly with the substrate for the active site', "B":'Only slows the reaction temporarily', "C":'Has no lasting effect on enzyme activity', "D":'Forms a permanent covalent bond with the enzyme, permanently inactivating it'},"answer":'D'},

{"id":9,"subject":'Biology',"topic":'Enzymes',"difficulty":'Hard',
 "question":'Two enzymes that catalyze the same reaction but differ slightly in amino acid sequence, often expressed in different tissues, are called:',
 "options":{"A":'Isoenzymes (isozymes)', "B":'Coenzymes', "C":'Apoenzymes', "D":'Zymogens'},"answer":'A'},

{"id":10,"subject":'Biology',"topic":'Cell Biology',"difficulty":'Easy',
 "question":'The gel-like substance filling the interior of a cell, in which organelles are suspended, is called the:',
 "options":{"A":'Nucleoplasm', "B":'Cytoplasm', "C":'Extracellular matrix', "D":'Cell wall'},"answer":'B'},

{"id":11,"subject":'Biology',"topic":'Cell Biology',"difficulty":'Easy',
 "question":'Chloroplasts are found in:',
 "options":{"A":'All plant and animal cells', "B":'Only animal cells', "C":'Photosynthetic cells of plants and some protists', "D":'Only bacterial cells'},"answer":'C'},

{"id":12,"subject":'Biology',"topic":'Cell Biology',"difficulty":'Medium',
 "question":'The diagram shows a mitochondrion with three structures labeled P, Q, and R. Which labeled structure represents the folded inner membrane that houses the electron transport chain proteins?',
 "image":'images/q_mitochondrion_diagram.png',
 "options":{"A":'Structure P (outer membrane)', "B":'None of the labeled structures', "C":'Structure R (matrix)', "D":'Structure Q (cristae, the folded inner membrane)'},"answer":'D'},

{"id":13,"subject":'Biology',"topic":'Cell Biology',"difficulty":'Medium',
 "question":'Which of the following best explains why the inner mitochondrial membrane is highly folded into cristae?',
 "options":{"A":'To increase the surface area for electron transport chain proteins and ATP synthase, boosting ATP production', "B":'To reduce the surface area available for ATP synthesis', "C":'To prevent any chemical reactions from occurring', "D":'To store genetic material'},"answer":'A'},

{"id":14,"subject":'Biology',"topic":'Cell Biology',"difficulty":'Medium',
 "question":'Free ribosomes (not attached to the ER) in the cytoplasm typically synthesize proteins that:',
 "options":{"A":'Are always secreted outside the cell', "B":'Function within the cytosol itself, rather than being secreted or membrane-bound', "C":'Are found exclusively within the nucleus', "D":'Are immediately digested by lysosomes'},"answer":'B'},

{"id":15,"subject":'Biology',"topic":'Cell Biology',"difficulty":'Medium',
 "question":'Which of the following organelles is unique to plant cells and not typically found in animal cells?',
 "options":{"A":'Mitochondrion', "B":'Ribosome', "C":'Chloroplast', "D":'Golgi apparatus'},"answer":'C'},

{"id":16,"subject":'Biology',"topic":'Cell Biology',"difficulty":'Hard',
 "question":'A researcher observes a cell containing an unusually large number of mitochondria. This cell most likely:',
 "options":{"A":'Has a very low energy demand', "B":'Is a mature red blood cell', "C":'Does not perform cellular respiration', "D":'Has a high energy demand, such as a muscle or liver cell'},"answer":'D'},

{"id":17,"subject":'Biology',"topic":'Cell Membrane & Transport',"difficulty":'Easy',
 "question":'A membrane that allows some substances to pass through while restricting others is described as:',
 "options":{"A":'Selectively (semi-) permeable', "B":'Fully permeable', "C":'Impermeable', "D":'Rigid'},"answer":'A'},

{"id":18,"subject":'Biology',"topic":'Cell Membrane & Transport',"difficulty":'Medium',
 "question":'When two solutions have identical solute concentrations, they are described as:',
 "options":{"A":'Hypertonic to each other', "B":'Isotonic to each other', "C":'Hypotonic to each other', "D":'Saturated'},"answer":'B'},

{"id":19,"subject":'Biology',"topic":'Cell Membrane & Transport',"difficulty":'Medium',
 "question":'Ion channels that open or close in response to a change in membrane voltage are called:',
 "options":{"A":'Ligand-gated channels', "B":'Mechanically-gated channels', "C":'Voltage-gated channels', "D":'Leak channels'},"answer":'C'},

{"id":20,"subject":'Biology',"topic":'Cell Membrane & Transport',"difficulty":'Hard',
 "question":'A membrane pump actively moves three Na+ ions out of a cell for every two K+ ions moved in, using one ATP molecule per cycle. This describes the action of the:',
 "options":{"A":'Calcium pump', "B":'Glucose transporter', "C":'Proton pump', "D":'Sodium-potassium pump'},"answer":'D'},

{"id":21,"subject":'Biology',"topic":'Cell Membrane & Transport',"difficulty":'Easy',
 "question":'Receptor proteins embedded in the plasma membrane primarily function to:',
 "options":{"A":'Bind specific signaling molecules and trigger a response inside the cell', "B":'Transport water across the membrane', "C":'Provide structural support to the cytoskeleton only', "D":'Synthesize ATP'},"answer":'A'},

{"id":22,"subject":'Biology',"topic":'Cell Cycle & Division',"difficulty":'Easy',
 "question":'Interphase is divided into which three sub-stages, in order?',
 "options":{"A":'M, G1, S', "B":'G1, S, G2', "C":'S, G2, M', "D":'G2, G1, S'},"answer":'B'},

{"id":23,"subject":'Biology',"topic":'Cell Cycle & Division',"difficulty":'Easy',
 "question":'During which stage of mitosis do chromosomes begin to condense and become visible, while the spindle apparatus starts to form?',
 "options":{"A":'Anaphase', "B":'Metaphase', "C":'Prophase', "D":'Telophase'},"answer":'C'},

{"id":24,"subject":'Biology',"topic":'Cell Cycle & Division',"difficulty":'Medium',
 "question":'In meiosis, the separation of homologous chromosomes (rather than sister chromatids) occurs during:',
 "options":{"A":'Telophase II', "B":'Anaphase II', "C":'Metaphase I', "D":'Anaphase I'},"answer":'D'},

{"id":25,"subject":'Biology',"topic":'Cell Cycle & Division',"difficulty":'Medium',
 "question":'A diploid organism has 2n = 24 chromosomes. How many chromosomes will be present in each of its gametes?',
 "options":{"A":'12', "B":'24', "C":'48', "D":'6'},"answer":'A'},

{"id":26,"subject":'Biology',"topic":'Cell Cycle & Division',"difficulty":'Hard',
 "question":'Cyclins and cyclin-dependent kinases (CDKs) regulate the cell cycle mainly by:',
 "options":{"A":'Directly replicating DNA', "B":'Forming complexes that phosphorylate target proteins, driving the cell through checkpoints and cycle transitions', "C":'Permanently breaking down the nuclear envelope', "D":'Having no functional role in cycle progression'},"answer":'B'},

{"id":27,"subject":'Biology',"topic":'Cell Cycle & Division',"difficulty":'Medium',
 "question":'A tumor suppressor gene, such as p53, normally functions to:',
 "options":{"A":'Promote uncontrolled cell division', "B":'Directly cause cancer when functioning normally', "C":'Halt the cell cycle or trigger apoptosis in cells with damaged DNA', "D":'Have no role in the cell cycle whatsoever'},"answer":'C'},

{"id":28,"subject":'Biology',"topic":'Genetics',"difficulty":'Easy',
 "question":'In a monohybrid cross between a homozygous dominant (AA) and a homozygous recessive (aa) individual, all offspring will be:',
 "options":{"A":'AA', "B":'A mix of AA and aa', "C":'aa', "D":'Aa'},"answer":'D'},

{"id":29,"subject":'Biology',"topic":'Genetics',"difficulty":'Medium',
 "question":'A test cross is performed mainly to determine:',
 "options":{"A":'Whether an organism showing a dominant phenotype is homozygous or heterozygous for that trait', "B":'The sex of an organism', "C":'The exact chromosome number of an organism', "D":'Whether a mutation is present'},"answer":'A'},

{"id":30,"subject":'Biology',"topic":'Genetics',"difficulty":'Medium',
 "question":'Hemophilia A is X-linked recessive. If an affected man and a homozygous unaffected woman have children, what is expected?',
 "options":{"A":'All sons will be affected', "B":'All daughters will be carriers, and no children will be affected', "C":'All daughters will be affected', "D":'Half of the sons will be affected'},"answer":'B'},

{"id":31,"subject":'Biology',"topic":'Genetics',"difficulty":'Hard',
 "question":'In a dihybrid cross AaBb x AaBb, what fraction of the offspring is expected to show the dominant phenotype for at least one of the two traits?',
 "options":{"A":'9/16', "B":'3/16', "C":'15/16', "D":'1/16'},"answer":'C'},

{"id":32,"subject":'Biology',"topic":'Genetics',"difficulty":'Medium',
 "question":'A father with blood type A and a mother with blood type A have a child with blood type O. This outcome is possible if:',
 "options":{"A":'Both parents are homozygous IAIA', "B":'One parent must actually be blood type O', "C":"The child's blood type must have been mislabeled, since this is impossible", "D":'Both parents are heterozygous IAi'},"answer":'D'},

{"id":33,"subject":'Biology',"topic":'Genetics',"difficulty":'Hard',
 "question":'The pedigree chart shows an autosomal dominant trait passed through three generations, appearing in every generation. Based on this pedigree, which statement must be true about any unaffected individual shown?',
 "image":'images/q_pedigree_autosomal_dominant.png',
 "options":{"A":'They cannot pass the trait to their offspring, since they lack the dominant allele required to show or transmit it', "B":'They must be a carrier who could still pass on the trait', "C":'They will definitely become affected later in life', "D":'This cannot be determined from a pedigree chart'},"answer":'A'},

{"id":34,"subject":'Biology',"topic":'Genetics',"difficulty":'Medium',
 "question":"In four-o'clock plants, crossing a red-flowered plant with a white-flowered plant produces all pink-flowered offspring. This is an example of:",
 "options":{"A":'Codominance', "B":'Incomplete dominance', "C":'Epistasis', "D":'Complete dominance'},"answer":'B'},

{"id":35,"subject":'Biology',"topic":'Molecular Biology',"difficulty":'Easy',
 "question":'The two strands of the DNA double helix run in:',
 "options":{"A":'The same direction (parallel)', "B":'Random, unrelated directions', "C":'Opposite directions (antiparallel)', "D":'Only one strand has a defined direction'},"answer":'C'},

{"id":36,"subject":'Biology',"topic":'Molecular Biology',"difficulty":'Easy',
 "question":'A nucleotide consists of a nitrogenous base, a sugar, and:',
 "options":{"A":'An amino acid', "B":'A glycerol molecule', "C":'A fatty acid chain', "D":'A phosphate group'},"answer":'D'},

{"id":37,"subject":'Biology',"topic":'Molecular Biology',"difficulty":'Medium',
 "question":'Okazaki fragments are formed during DNA replication on the:',
 "options":{"A":'Lagging strand, synthesized discontinuously in short segments', "B":'Leading strand, synthesized continuously', "C":'Template strand only, never on the newly made strand', "D":'mRNA molecule during transcription'},"answer":'A'},

{"id":38,"subject":'Biology',"topic":'Molecular Biology',"difficulty":'Medium',
 "question":'Which enzyme joins together the Okazaki fragments on the lagging strand during DNA replication?',
 "options":{"A":'Primase', "B":'DNA ligase', "C":'Helicase', "D":'Topoisomerase'},"answer":'B'},

{"id":39,"subject":'Biology',"topic":'Molecular Biology',"difficulty":'Medium',
 "question":"An insertion of one nucleotide into the middle of a gene's coding sequence typically causes:",
 "options":{"A":'No effect on the resulting protein', "B":'A silent mutation only', "C":'A frameshift mutation, altering the amino acid sequence from that point onward', "D":'Deletion of the entire gene'},"answer":'C'},

{"id":40,"subject":'Biology',"topic":'Molecular Biology',"difficulty":'Hard',
 "question":'A mutation that changes a single codon so that it now specifies a different amino acid, while the protein is still produced, is called a:',
 "options":{"A":'Silent mutation', "B":'Frameshift mutation', "C":'Nonsense mutation', "D":'Missense mutation'},"answer":'D'},

{"id":41,"subject":'Biology',"topic":'Molecular Biology',"difficulty":'Hard',
 "question":'Alternative splicing of pre-mRNA allows a single gene to:',
 "options":{"A":'Produce multiple different protein variants by combining exons in different ways', "B":'Produce only one possible protein', "C":'Never be transcribed at all', "D":'Skip translation entirely'},"answer":'A'},

{"id":42,"subject":'Biology',"topic":'Molecular Biology',"difficulty":'Medium',
 "question":'A ribosome moves along the mRNA in which direction during translation?',
 "options":{"A":"3' to 5'", "B":"5' to 3'", "C":'Randomly in either direction', "D":'It does not move along the mRNA at all'},"answer":'B'},

{"id":43,"subject":'Biology',"topic":'Molecular Biology',"difficulty":'Medium',
 "question":'Which of the following is a purine base?',
 "options":{"A":'Cytosine', "B":'Thymine', "C":'Adenine', "D":'Uracil'},"answer":'C'},

{"id":44,"subject":'Biology',"topic":'Molecular Biology',"difficulty":'Easy',
 "question":'The process of converting the information in an mRNA sequence into a sequence of amino acids is called:',
 "options":{"A":'Transcription', "B":'Splicing', "C":'Replication', "D":'Translation'},"answer":'D'},

{"id":45,"subject":'Biology',"topic":'Evolution',"difficulty":'Easy',
 "question":'Individuals of a species that become geographically separated and no longer interbreed may eventually diverge into separate species through:',
 "options":{"A":'Allopatric speciation', "B":'Genetic drift alone', "C":'Codominance', "D":'Meiosis'},"answer":'A'},

{"id":46,"subject":'Biology',"topic":'Evolution',"difficulty":'Medium',
 "question":'Convergent evolution explains why unrelated species, such as sharks and dolphins, have similar streamlined body shapes mainly because:',
 "options":{"A":'They share a very recent common ancestor', "B":'They independently evolved similar adaptations in response to similar environmental pressures', "C":'They belong to the same species', "D":'One species evolved directly from the other'},"answer":'B'},

{"id":47,"subject":'Biology',"topic":'Evolution',"difficulty":'Medium',
 "question":'Which of the following is an assumption required for a population to remain in Hardy-Weinberg equilibrium?',
 "options":{"A":'Natural selection is actively occurring', "B":'The population is very small', "C":'No mutation, migration, genetic drift, or selection is occurring, and mating is random', "D":'Non-random mating occurs'},"answer":'C'},

{"id":48,"subject":'Biology',"topic":'Evolution',"difficulty":'Hard',
 "question":'In a population, 16% of individuals show a recessive phenotype. Assuming Hardy-Weinberg equilibrium, what is the frequency of the dominant allele?',
 "options":{"A":'0.4', "B":'0.84', "C":'0.16', "D":'0.6'},"answer":'D'},

{"id":49,"subject":'Biology',"topic":'Classification & Diversity',"difficulty":'Easy',
 "question":'The most inclusive (broadest) taxonomic category, ranking above Kingdom, is:',
 "options":{"A":'Domain', "B":'Phylum', "C":'Class', "D":'Family'},"answer":'A'},

{"id":50,"subject":'Biology',"topic":'Classification & Diversity',"difficulty":'Easy',
 "question":'Members of kingdom Fungi obtain nutrients mainly by:',
 "options":{"A":'Photosynthesis', "B":'Absorbing nutrients after secreting digestive enzymes onto their food', "C":'Ingesting prey directly', "D":'Chemosynthesis'},"answer":'B'},

{"id":51,"subject":'Biology',"topic":'Classification & Diversity',"difficulty":'Medium',
 "question":'The three-domain system of classification (Bacteria, Archaea, Eukarya) is based mainly on differences in:',
 "options":{"A":'Body size', "B":'Habitat alone', "C":'Molecular and genetic differences, such as rRNA sequence', "D":'Method of locomotion'},"answer":'C'},

{"id":52,"subject":'Biology',"topic":'Classification & Diversity',"difficulty":'Medium',
 "question":'A biologist identifies an organism as multicellular, eukaryotic, capable of photosynthesis, and possessing cellulose cell walls. This organism belongs to kingdom:',
 "options":{"A":'Animalia', "B":'Monera', "C":'Fungi', "D":'Plantae'},"answer":'D'},

{"id":53,"subject":'Biology',"topic":'Classification & Diversity',"difficulty":'Easy',
 "question":'Which taxonomic rank lies directly between Class and Family?',
 "options":{"A":'Order', "B":'Phylum', "C":'Genus', "D":'Kingdom'},"answer":'A'},

{"id":54,"subject":'Biology',"topic":'Classification & Diversity',"difficulty":'Medium',
 "question":'Members of phylum Nematoda (roundworms) are characterized by:',
 "options":{"A":'A segmented body and jointed legs', "B":'A pseudocoelom and a tube-within-a-tube body plan', "C":'Radial symmetry and stinging cells', "D":'A calcium carbonate shell'},"answer":'B'},

{"id":55,"subject":'Biology',"topic":'Plant Biology',"difficulty":'Easy',
 "question":'The vascular tissue responsible for transporting water and dissolved minerals upward from the roots is:',
 "options":{"A":'Phloem', "B":'Epidermis', "C":'Xylem', "D":'Cortex'},"answer":'C'},

{"id":56,"subject":'Biology',"topic":'Plant Biology',"difficulty":'Medium',
 "question":'Photosystem II in the thylakoid membrane primarily functions to:',
 "options":{"A":'Produce ATP directly without needing light', "B":'Transport sugars from the leaf to the roots', "C":'Fix carbon dioxide into sugar', "D":'Absorb light energy and split water molecules, releasing oxygen and electrons'},"answer":'D'},

{"id":57,"subject":'Biology',"topic":'Plant Biology',"difficulty":'Medium',
 "question":'RuBisCO, the enzyme that fixes CO2 in the Calvin cycle, is considered relatively inefficient partly because it:',
 "options":{"A":'Can also bind O2 instead of CO2, leading to photorespiration and reduced sugar yield', "B":'Works only in complete darkness', "C":'Requires no cofactors at all', "D":'Directly produces ATP'},"answer":'A'},

{"id":58,"subject":'Biology',"topic":'Plant Biology',"difficulty":'Hard',
 "question":'In C4 plants, the enzyme PEP carboxylase is advantageous over RuBisCO for initial carbon fixation mainly because PEP carboxylase:',
 "options":{"A":'Has a much lower affinity for CO2 than RuBisCO', "B":'Has a very high affinity for CO2 and does not bind O2, minimizing photorespiration', "C":'Only works in the complete absence of light', "D":'Fixes atmospheric nitrogen instead of carbon'},"answer":'B'},

{"id":59,"subject":'Biology',"topic":'Plant Biology',"difficulty":'Medium',
 "question":'Auxin, a plant hormone, is primarily responsible for:',
 "options":{"A":'Promoting leaf senescence only', "B":'Triggering seed dormancy', "C":'Promoting cell elongation and phototropic bending of shoots toward light', "D":'Causing stomatal closure exclusively'},"answer":'C'},

{"id":60,"subject":'Biology',"topic":'Plant Biology',"difficulty":'Easy',
 "question":'The fusion of a sperm nucleus with an egg nucleus in a flowering plant, forming a diploid zygote, is called:',
 "options":{"A":'Pollination', "B":'Dispersal', "C":'Germination', "D":'Fertilization'},"answer":'D'},

{"id":61,"subject":'Biology',"topic":'Human Physiology - Digestion',"difficulty":'Easy',
 "question":'The muscular tube connecting the throat to the stomach, through which food passes, is the:',
 "options":{"A":'Esophagus', "B":'Trachea', "C":'Pharynx', "D":'Larynx'},"answer":'A'},

{"id":62,"subject":'Biology',"topic":'Human Physiology - Digestion',"difficulty":'Medium',
 "question":'The enzyme amylase, found in both saliva and pancreatic secretions, functions to digest:',
 "options":{"A":'Proteins', "B":'Starch into maltose', "C":'Fats into fatty acids', "D":'Nucleic acids'},"answer":'B'},

{"id":63,"subject":'Biology',"topic":'Human Physiology - Digestion',"difficulty":'Medium',
 "question":'Which of the following best describes the function of the pyloric sphincter?',
 "options":{"A":'It absorbs nutrients directly into the blood', "B":'It regulates food entry into the esophagus', "C":'It regulates the release of partially digested food (chyme) from the stomach into the small intestine', "D":'It produces digestive enzymes'},"answer":'C'},

{"id":64,"subject":'Biology',"topic":'Human Physiology - Digestion',"difficulty":'Hard',
 "question":'A person with damage to the exocrine (digestive enzyme-producing) function of the pancreas would most likely experience difficulty digesting:',
 "options":{"A":'Only water', "B":'Nothing, since the stomach compensates fully', "C":'Only vitamins', "D":'Proteins, fats, and carbohydrates, since pancreatic enzymes are needed for all three'},"answer":'D'},

{"id":65,"subject":'Biology',"topic":'Human Physiology - Circulation',"difficulty":'Easy',
 "question":'The chamber of the heart that pumps oxygenated blood into the aorta and out to the body is the:',
 "options":{"A":'Left ventricle', "B":'Right atrium', "C":'Right ventricle', "D":'Left atrium'},"answer":'A'},

{"id":66,"subject":'Biology',"topic":'Human Physiology - Circulation',"difficulty":'Medium',
 "question":'Blood pressure is typically highest in the:',
 "options":{"A":'Veins', "B":'Arteries, particularly near the heart', "C":'Capillaries', "D":'Venules'},"answer":'B'},

{"id":67,"subject":'Biology',"topic":'Human Physiology - Circulation',"difficulty":'Medium',
 "question":'White blood cells (leukocytes) primarily function to:',
 "options":{"A":'Transport oxygen throughout the body', "B":'Carry nutrients to tissues', "C":'Defend the body against pathogens and infection', "D":'Form blood clots'},"answer":'C'},

{"id":68,"subject":'Biology',"topic":'Human Physiology - Circulation',"difficulty":'Hard',
 "question":'During ventricular systole (contraction), pressure inside the ventricles rises until it exceeds the pressure in the:',
 "options":{"A":'Atria only, causing the AV valves to open', "B":'Coronary arteries only', "C":'Vena cava, causing backflow', "D":'Aorta and pulmonary artery, causing the semilunar valves to open and blood to be ejected'},"answer":'D'},

{"id":69,"subject":'Biology',"topic":'Human Physiology - Respiration',"difficulty":'Easy',
 "question":'The flap of cartilage that prevents food from entering the trachea during swallowing is the:',
 "options":{"A":'Epiglottis', "B":'Larynx', "C":'Pharynx', "D":'Bronchiole'},"answer":'A'},

{"id":70,"subject":'Biology',"topic":'Human Physiology - Respiration',"difficulty":'Medium',
 "question":'The elastic recoil of the lungs together with relaxation of the diaphragm and rib muscles during quiet breathing is primarily responsible for:',
 "options":{"A":'Inhalation', "B":'Exhalation', "C":'Gas exchange in the alveoli', "D":'Production of surfactant'},"answer":'B'},

{"id":71,"subject":'Biology',"topic":'Human Physiology - Respiration',"difficulty":'Medium',
 "question":'Surfactant, produced by cells in the alveoli, functions mainly to:',
 "options":{"A":'Increase surface tension, helping alveoli stay collapsed', "B":'Transport oxygen directly into the blood', "C":'Reduce surface tension within the alveoli, preventing their collapse', "D":'Filter incoming air'},"answer":'C'},

{"id":72,"subject":'Biology',"topic":'Human Physiology - Excretion',"difficulty":'Easy',
 "question":'The tube that carries urine from each kidney to the urinary bladder is the:',
 "options":{"A":'Urethra', "B":'Renal artery', "C":'Renal vein', "D":'Ureter'},"answer":'D'},

{"id":73,"subject":'Biology',"topic":'Human Physiology - Excretion',"difficulty":'Medium',
 "question":'The loop of Henle in the nephron is primarily responsible for:',
 "options":{"A":'Establishing a concentration gradient in the kidney medulla, enabling water reabsorption', "B":'Filtering blood directly', "C":'Producing urine-related hormones', "D":'Storing urine before excretion'},"answer":'A'},

{"id":74,"subject":'Biology',"topic":'Human Physiology - Excretion',"difficulty":'Hard',
 "question":"A drug that blocks aldosterone's action on the kidney would most likely result in:",
 "options":{"A":'Increased sodium reabsorption and decreased urine volume', "B":'Decreased sodium reabsorption in the distal tubule, leading to increased sodium and water loss in urine', "C":'No change in electrolyte balance', "D":'Complete kidney failure'},"answer":'B'},

{"id":75,"subject":'Biology',"topic":'Human Physiology - Nervous & Endocrine',"difficulty":'Easy',
 "question":'The largest and most complex part of the human brain, responsible for higher functions such as reasoning and voluntary movement, is the:',
 "options":{"A":'Cerebellum', "B":'Medulla oblongata', "C":'Cerebrum', "D":'Hypothalamus'},"answer":'C'},

{"id":76,"subject":'Biology',"topic":'Human Physiology - Nervous & Endocrine',"difficulty":'Medium',
 "question":'The refractory period following an action potential mainly ensures that:',
 "options":{"A":'The neuron can fire again immediately in the same direction', "B":'Neurotransmitters are permanently depleted', "C":'The neuron never fires again', "D":'The action potential travels in one direction only and the neuron cannot immediately fire again'},"answer":'D'},

{"id":77,"subject":'Biology',"topic":'Human Physiology - Nervous & Endocrine',"difficulty":'Medium',
 "question":'Antidiuretic hormone (ADH) is produced by the hypothalamus and released into the blood from the:',
 "options":{"A":'Posterior pituitary', "B":'Anterior pituitary', "C":'Thyroid gland', "D":'Adrenal medulla'},"answer":'A'},

{"id":78,"subject":'Biology',"topic":'Human Physiology - Nervous & Endocrine',"difficulty":'Hard',
 "question":'In response to low blood calcium levels, the parathyroid glands release parathyroid hormone (PTH), which acts to:',
 "options":{"A":'Decrease blood calcium levels further', "B":'Increase blood calcium by stimulating bone resorption, kidney reabsorption, and vitamin D activation', "C":'Have no effect on blood calcium levels', "D":'Directly convert calcium into phosphate'},"answer":'B'},

{"id":79,"subject":'Biology',"topic":'Human Physiology - Reproduction',"difficulty":'Easy',
 "question":'The process by which a fertilized egg (zygote) attaches to the uterine wall is called:',
 "options":{"A":'Ovulation', "B":'Fertilization', "C":'Implantation', "D":'Menstruation'},"answer":'C'},

{"id":80,"subject":'Biology',"topic":'Human Physiology - Reproduction',"difficulty":'Medium',
 "question":'FSH (follicle-stimulating hormone) in females primarily functions to:',
 "options":{"A":'Stimulate milk production', "B":'Trigger ovulation directly', "C":'Maintain the uterine lining after implantation', "D":'Stimulate the growth and maturation of ovarian follicles'},"answer":'D'},

{"id":81,"subject":'Biology',"topic":'Ecology',"difficulty":'Medium',
 "question":'Two species competing for exactly the same limited resource in the same habitat may, over time, experience:',
 "options":{"A":'Competitive exclusion, where one species outcompetes and displaces the other', "B":'Mutual benefit with no consequence to either species', "C":'Immediate extinction of both species', "D":'No interaction between the species at all'},"answer":'A'},

# ============================================================
# CHEMISTRY (45) - id 82-126
# ============================================================

{"id":82,"subject":'Chemistry',"topic":'Atomic Structure',"difficulty":'Easy',
 "question":'The atomic number of an atom represents the number of:',
 "options":{"A":'Neutrons only', "B":'Protons in the nucleus', "C":'Total nucleons', "D":'Valence electrons only'},"answer":'B'},

{"id":83,"subject":'Chemistry',"topic":'Atomic Structure',"difficulty":'Medium',
 "question":'A neutral atom of sulfur-32 (atomic number 16) contains how many electrons?',
 "options":{"A":'32', "B":'48', "C":'16', "D":'8'},"answer":'C'},

{"id":84,"subject":'Chemistry',"topic":'Atomic Structure',"difficulty":'Medium',
 "question":'The maximum number of electrons that can occupy the second principal energy shell (n=2) is:',
 "options":{"A":'2', "B":'32', "C":'18', "D":'8'},"answer":'D'},

{"id":85,"subject":'Chemistry',"topic":'Atomic Structure',"difficulty":'Hard',
 "question":'An atom in its ground state has the electron configuration 1s2 2s2 2p6 3s2 3p4. This element most likely belongs to which group of the periodic table?',
 "options":{"A":'Group 16', "B":'Group 15', "C":'Group 14', "D":'Group 17'},"answer":'A'},

{"id":86,"subject":'Chemistry',"topic":'Periodic Table',"difficulty":'Easy',
 "question":'Elements in the same vertical column of the periodic table are called a:',
 "options":{"A":'Period', "B":'Group', "C":'Series', "D":'Row'},"answer":'B'},

{"id":87,"subject":'Chemistry',"topic":'Periodic Table',"difficulty":'Medium',
 "question":'Atomic radius generally decreases across a period from left to right mainly because:',
 "options":{"A":'Electron shielding increases significantly across the period', "B":'Additional electron shells are added across the period', "C":'Increasing nuclear charge pulls the valence electrons closer, while shielding stays roughly constant', "D":'The number of protons decreases across the period'},"answer":'C'},

{"id":88,"subject":'Chemistry',"topic":'Periodic Table',"difficulty":'Medium',
 "question":'Which of the following elements would be expected to have the highest electronegativity?',
 "options":{"A":'Sodium', "B":'Magnesium', "C":'Aluminum', "D":'Chlorine'},"answer":'D'},

{"id":89,"subject":'Chemistry',"topic":'Chemical Bonding',"difficulty":'Easy',
 "question":'When two atoms of the same element bond together, such as in O2, the bond formed is:',
 "options":{"A":'Purely covalent (nonpolar)', "B":'Ionic', "C":'Metallic', "D":'Hydrogen bonding'},"answer":'A'},

{"id":90,"subject":'Chemistry',"topic":'Chemical Bonding',"difficulty":'Medium',
 "question":'According to VSEPR theory, a molecule with three bonding pairs and no lone pairs on the central atom (e.g., BF3) has a molecular shape described as:',
 "options":{"A":'Tetrahedral', "B":'Trigonal planar', "C":'Bent', "D":'Trigonal pyramidal'},"answer":'B'},

{"id":91,"subject":'Chemistry',"topic":'Chemical Bonding',"difficulty":'Medium',
 "question":'Which of the following molecules is polar overall, due to an asymmetrical distribution of bond dipoles?',
 "options":{"A":'CO2', "B":'CH4', "C":'H2O', "D":'CCl4'},"answer":'C'},

{"id":92,"subject":'Chemistry',"topic":'Chemical Bonding',"difficulty":'Hard',
 "question":'Van der Waals (London dispersion) forces exist between all molecules, including nonpolar ones, mainly because:',
 "options":{"A":'All molecules carry a permanent net charge', "B":'They are ionic in nature', "C":'They contain hydrogen bonded directly to oxygen', "D":'Temporary, instantaneous dipoles arise from fluctuations in electron distribution'},"answer":'D'},

{"id":93,"subject":'Chemistry',"topic":'States of Matter',"difficulty":'Easy',
 "question":'The change of state from gas to liquid is called:',
 "options":{"A":'Condensation', "B":'Evaporation', "C":'Sublimation', "D":'Melting'},"answer":'A'},

{"id":94,"subject":'Chemistry',"topic":'States of Matter',"difficulty":'Medium',
 "question":"A gas occupies 5.0 L at 4.0 atm. What volume will it occupy at 2.0 atm, assuming constant temperature (Boyle's Law)?",
 "options":{"A":'2.5 L', "B":'10.0 L', "C":'20.0 L', "D":'1.0 L'},"answer":'B'},

{"id":95,"subject":'Chemistry',"topic":'States of Matter',"difficulty":'Hard',
 "question":'A gas sample at 350 K and 2 atm has a volume of 10 L. What would its volume be at STP (273 K, 1 atm), assuming ideal behavior?',
 "options":{"A":'Approximately 20 L', "B":'Approximately 12.8 L', "C":'Approximately 15.6 L', "D":'Approximately 5 L'},"answer":'C'},

{"id":96,"subject":'Chemistry',"topic":'Stoichiometry',"difficulty":'Easy',
 "question":'One mole of any substance contains approximately how many particles?',
 "options":{"A":'22.4 x 10^23', "B":'3.14 x 10^23', "C":'1.0 x 10^23', "D":'6.02 x 10^23'},"answer":'D'},

{"id":97,"subject":'Chemistry',"topic":'Stoichiometry',"difficulty":'Medium',
 "question":'How many moles of NaOH (molar mass 40 g/mol) are present in 20 g of NaOH?',
 "options":{"A":'0.5 mol', "B":'0.2 mol', "C":'2 mol', "D":'5 mol'},"answer":'A'},

{"id":98,"subject":'Chemistry',"topic":'Stoichiometry',"difficulty":'Hard',
 "question":'A 100 mL solution contains 0.05 mole of HCl. What is the molarity of the solution?',
 "options":{"A":'0.05 M', "B":'0.5 M', "C":'5 M', "D":'0.005 M'},"answer":'B'},

{"id":99,"subject":'Chemistry',"topic":'Stoichiometry',"difficulty":'Medium',
 "question":'In the reaction 4Fe + 3O2 -> 2Fe2O3, how many moles of Fe2O3 are produced when 8 moles of Fe react completely with excess O2?',
 "options":{"A":'2', "B":'6', "C":'4', "D":'8'},"answer":'C'},

{"id":100,"subject":'Chemistry',"topic":'Thermochemistry',"difficulty":'Easy',
 "question":'The formation of a new chemical bond generally:',
 "options":{"A":'Requires an input of energy in every case', "B":'Only occurs at absolute zero temperature', "C":'Has no effect on the energy of the system', "D":'Releases energy, since bond formation is generally an exothermic process'},"answer":'D'},

{"id":101,"subject":'Chemistry',"topic":'Thermochemistry',"difficulty":'Medium',
 "question":'An exothermic reaction has a negative enthalpy change (delta H). This means:',
 "options":{"A":'The products have lower energy than the reactants, and energy is released to the surroundings', "B":'The products have higher energy than the reactants', "C":'No energy change occurs during the reaction', "D":'Energy is absorbed from the surroundings'},"answer":'A'},

{"id":102,"subject":'Chemistry',"topic":'Chemical Equilibrium',"difficulty":'Medium',
 "question":'For the equilibrium N2O4(g) <-> 2NO2(g), where the forward reaction is endothermic, increasing the temperature will shift the equilibrium:',
 "options":{"A":'Toward the reactant, N2O4', "B":'Toward the product, NO2, increasing its concentration', "C":'Not at all, since temperature has no effect on equilibrium', "D":'Completely to N2O4, stopping the reverse reaction'},"answer":'B'},

{"id":103,"subject":'Chemistry',"topic":'Chemical Equilibrium',"difficulty":'Hard',
 "question":'At chemical equilibrium, the rate of the forward reaction and the rate of the reverse reaction are:',
 "options":{"A":'Both exactly zero', "B":'The forward rate is always greater than the reverse rate', "C":'Equal to each other, though not necessarily zero', "D":'The reverse rate is always greater than the forward rate'},"answer":'C'},

{"id":104,"subject":'Chemistry',"topic":'Reaction Kinetics',"difficulty":'Easy',
 "question":'A catalyst speeds up a chemical reaction without being:',
 "options":{"A":'Involved in the reaction mechanism at all', "B":'Present in significant amounts', "C":'Able to lower the activation energy', "D":'Consumed or permanently changed by the overall reaction'},"answer":'D'},

{"id":105,"subject":'Chemistry',"topic":'Reaction Kinetics',"difficulty":'Medium',
 "question":'The order of a reaction with respect to a given reactant is determined:',
 "options":{"A":'Experimentally, by observing how the rate changes with concentration', "B":'Directly from the coefficients in the balanced chemical equation', "C":"From the reaction's overall enthalpy change", "D":'Solely from the temperature of the reaction'},"answer":'A'},

{"id":106,"subject":'Chemistry',"topic":'Electrochemistry',"difficulty":'Medium',
 "question":'In electrolysis, the electrode at which reduction occurs is the:',
 "options":{"A":'Anode', "B":'Cathode', "C":'Salt bridge', "D":'External circuit'},"answer":'B'},

{"id":107,"subject":'Chemistry',"topic":'Electrochemistry',"difficulty":'Hard',
 "question":'In the reaction Pb(s) + 2AgNO3(aq) -> Pb(NO3)2(aq) + 2Ag(s), lead (Pb) undergoes:',
 "options":{"A":'Reduction, gaining electrons', "B":'No change in oxidation state', "C":'Oxidation, losing electrons', "D":'Neither oxidation nor reduction'},"answer":'C'},

{"id":108,"subject":'Chemistry',"topic":'Acids & Bases',"difficulty":'Easy',
 "question":'A solution with pH = 9 is:',
 "options":{"A":'Strongly acidic', "B":'Weakly acidic', "C":'Perfectly neutral', "D":'Basic'},"answer":'D'},

{"id":109,"subject":'Chemistry',"topic":'Acids & Bases',"difficulty":'Medium',
 "question":'A solution has [H+] = 1x10^-6 M. What is its pH?',
 "options":{"A":'6', "B":'8', "C":'-6', "D":'1x10^6'},"answer":'A'},

{"id":110,"subject":'Chemistry',"topic":'Acids & Bases',"difficulty":'Medium',
 "question":'The graph shows the change in pH as a strong base is added to a strong acid. Based on the steep, near-vertical jump near the midpoint of the curve, this feature indicates:',
 "image":'images/q_strong_acid_strong_base_curve.png',
 "options":{"A":'A gradual, slow change in pH throughout the titration', "B":'The equivalence point, where pH changes very rapidly with only a small addition of titrant', "C":'That no chemical reaction is occurring', "D":'That the acid being titrated is actually a weak acid'},"answer":'B'},

{"id":111,"subject":'Chemistry',"topic":'Acids & Bases',"difficulty":'Hard',
 "question":'A solution of a strong acid and a solution of a weak acid have the same molar concentration. Compared to the weak acid solution, the strong acid solution will have:',
 "options":{"A":'A higher pH (less acidic)', "B":'Exactly the same pH', "C":'A lower pH (more acidic), since it dissociates completely', "D":'No H+ ions present at all'},"answer":'C'},

{"id":112,"subject":'Chemistry',"topic":'Organic Chemistry',"difficulty":'Easy',
 "question":'The functional group -OH attached to a non-aromatic carbon chain characterizes:',
 "options":{"A":'Aldehydes', "B":'Esters', "C":'Ethers', "D":'Alcohols'},"answer":'D'},

{"id":113,"subject":'Chemistry',"topic":'Organic Chemistry',"difficulty":'Medium',
 "question":'Aromatic compounds, such as benzene, are characterized by:',
 "options":{"A":'A ring of alternating single and double bonds with delocalized pi electrons, giving special stability', "B":'A single, isolated carbon-carbon double bond', "C":'The complete absence of carbon atoms', "D":'Only single bonds throughout the molecule'},"answer":'A'},

{"id":114,"subject":'Chemistry',"topic":'Organic Chemistry',"difficulty":'Medium',
 "question":'The reaction of a haloalkane with aqueous KOH to form an alcohol proceeds through:',
 "options":{"A":'An addition reaction', "B":'A nucleophilic substitution reaction, in which OH- replaces the halide', "C":'A combustion reaction', "D":'A polymerization reaction'},"answer":'B'},

{"id":115,"subject":'Chemistry',"topic":'Organic Chemistry',"difficulty":'Hard',
 "question":'In a condensation polymerization reaction forming a polyester, the monomers join together with the release of:',
 "options":{"A":'Hydrogen gas', "B":'Carbon dioxide only', "C":'A small molecule, such as water', "D":'No byproduct at all'},"answer":'C'},

{"id":116,"subject":'Chemistry',"topic":'Organic Chemistry',"difficulty":'Medium',
 "question":'The oxidation of a primary alcohol using a suitable oxidizing agent typically produces first a(n):',
 "options":{"A":'Ketone', "B":'Alkene', "C":'Ether', "D":'Aldehyde, which can be further oxidized to a carboxylic acid'},"answer":'D'},

{"id":117,"subject":'Chemistry',"topic":'Organic Chemistry',"difficulty":'Easy',
 "question":'Which functional group is characteristic of an amide?',
 "options":{"A":'-CONH2', "B":'-COOH', "C":'-OH', "D":'-CHO'},"answer":'A'},

{"id":118,"subject":'Chemistry',"topic":'Inorganic Chemistry',"difficulty":'Medium',
 "question":'Group 17 elements (halogens) exist as diatomic molecules (e.g., Cl2, Br2) mainly because:',
 "options":{"A":'They already have a full outer electron shell', "B":'Sharing one electron pair between two halogen atoms allows both to achieve a stable octet', "C":'They cannot bond with any other element', "D":'They are all radioactive'},"answer":'B'},

{"id":119,"subject":'Chemistry',"topic":'Inorganic Chemistry',"difficulty":'Medium',
 "question":'Which of the following correctly ranks these elements in order of increasing atomic radius: F, Cl, Br?',
 "options":{"A":'Br < Cl < F', "B":'Cl < F < Br', "C":'F < Cl < Br', "D":'They are all equal in atomic radius'},"answer":'C'},

{"id":120,"subject":'Chemistry',"topic":'Inorganic Chemistry',"difficulty":'Hard',
 "question":"In the reaction 2FeCl2 + Cl2 -> 2FeCl3, iron's oxidation state changes from:",
 "options":{"A":'No change occurs', "B":'+3 to +2 (reduction)', "C":'0 to +2', "D":'+2 to +3 (oxidation)'},"answer":'D'},

{"id":121,"subject":'Chemistry',"topic":'Physical Chemistry',"difficulty":'Medium',
 "question":'Colligative properties of a solution, such as boiling point elevation, depend primarily on:',
 "options":{"A":'The number (concentration) of solute particles present, regardless of their identity', "B":'The specific chemical identity of the solute', "C":'The color of the solute', "D":"The solvent's boiling point alone"},"answer":'A'},

{"id":122,"subject":'Chemistry',"topic":'Physical Chemistry',"difficulty":'Hard',
 "question":'30 mL of 0.5 M H2SO4 is required to completely neutralize a NaOH solution of unknown volume with a concentration of 0.6 M (H2SO4 + 2NaOH -> Na2SO4 + 2H2O). What volume of NaOH solution was used?',
 "options":{"A":'25 mL', "B":'50 mL', "C":'30 mL', "D":'60 mL'},"answer":'B'},

{"id":123,"subject":'Chemistry',"topic":'Environmental Chemistry',"difficulty":'Easy',
 "question":'Which of the following is considered a renewable source of energy, in contrast to fossil fuels?',
 "options":{"A":'Coal', "B":'Natural gas', "C":'Solar energy', "D":'Petroleum'},"answer":'C'},

{"id":124,"subject":'Chemistry',"topic":'Environmental Chemistry',"difficulty":'Medium',
 "question":'The main cause of ocean acidification is:',
 "options":{"A":'Increased salinity from evaporation', "B":'Increased water temperature alone', "C":'Oil spills', "D":'Absorption of excess atmospheric CO2 by seawater, forming carbonic acid'},"answer":'D'},

{"id":125,"subject":'Chemistry',"topic":'Chemical Bonding',"difficulty":'Easy',
 "question":'The bond formed by the complete transfer of one or more electrons from a metal atom to a nonmetal atom is called a(n):',
 "options":{"A":'Ionic bond', "B":'Covalent bond', "C":'Metallic bond', "D":'Hydrogen bond'},"answer":'A'},

{"id":126,"subject":'Chemistry',"topic":'Atomic Structure',"difficulty":'Easy',
 "question":'An isotope of an element differs from the standard atom mainly in its number of:',
 "options":{"A":'Protons', "B":'Neutrons', "C":'Electrons', "D":'Valence shells'},"answer":'B'},

# ============================================================
# PHYSICS (36) - id 127-162
# ============================================================

{"id":127,"subject":'Physics',"topic":'Kinematics',"difficulty":'Easy',
 "question":'A train travels 300 km in 5 hours at constant speed. What is its speed?',
 "options":{"A":'50 km/h', "B":'1500 km/h', "C":'60 km/h', "D":'6 km/h'},"answer":'C'},

{"id":128,"subject":'Physics',"topic":'Kinematics',"difficulty":'Medium',
 "question":'A car accelerates uniformly at 3 m/s^2 from an initial velocity of 5 m/s. What is its velocity after 6 seconds?',
 "options":{"A":'18 m/s', "B":'30 m/s', "C":'11 m/s', "D":'23 m/s'},"answer":'D'},

{"id":129,"subject":'Physics',"topic":'Kinematics',"difficulty":'Hard',
 "question":'A ball is thrown horizontally from a height of 20 m with an initial horizontal speed of 15 m/s (g = 10 m/s^2, ignoring air resistance). How long does it take to hit the ground?',
 "options":{"A":'1 s', "B":'2 s', "C":'3 s', "D":'4 s'},"answer":'B'},

{"id":130,"subject":'Physics',"topic":'Dynamics',"difficulty":'Easy',
 "question":'The property of matter that resists changes in its state of motion is called:',
 "options":{"A":'Weight', "B":'Inertia', "C":'Momentum', "D":'Acceleration'},"answer":'B'},

{"id":131,"subject":'Physics',"topic":'Dynamics',"difficulty":'Medium',
 "question":'A 5 kg object experiences a net force of 15 N. What is its resulting acceleration?',
 "options":{"A":'75 m/s^2', "B":'0.33 m/s^2', "C":'3 m/s^2', "D":'20 m/s^2'},"answer":'C'},

{"id":132,"subject":'Physics',"topic":'Dynamics',"difficulty":'Medium',
 "question":"According to Newton's second law, for a constant net force, doubling an object's mass will:",
 "options":{"A":'Double its acceleration', "B":'Quadruple its acceleration', "C":'Leave its acceleration unchanged', "D":'Halve its acceleration'},"answer":'D'},

{"id":133,"subject":'Physics',"topic":'Dynamics',"difficulty":'Hard',
 "question":'A 3 kg block slides down a frictionless incline at 30 degrees to the horizontal (g = 10 m/s^2). What is its acceleration along the incline?',
 "options":{"A":'5 m/s^2', "B":'10 m/s^2', "C":'8.7 m/s^2', "D":'3 m/s^2'},"answer":'A'},

{"id":134,"subject":'Physics',"topic":'Work, Energy & Power',"difficulty":'Easy',
 "question":'Power is defined as the rate at which:',
 "options":{"A":'Force is applied', "B":'Work is done (energy is transferred)', "C":'Mass changes', "D":'Velocity changes'},"answer":'B'},

{"id":135,"subject":'Physics',"topic":'Work, Energy & Power',"difficulty":'Medium',
 "question":'A 6 kg object moving at 5 m/s has a kinetic energy of:',
 "options":{"A":'30 J', "B":'150 J', "C":'75 J', "D":'15 J'},"answer":'C'},

{"id":136,"subject":'Physics',"topic":'Work, Energy & Power',"difficulty":'Medium',
 "question":'An object falls freely from rest under gravity, with air resistance ignored. As it falls, its total mechanical energy:',
 "options":{"A":'Increases continuously', "B":'Decreases continuously', "C":'Is zero at all times', "D":'Remains constant, as potential energy converts into kinetic energy'},"answer":'D'},

{"id":137,"subject":'Physics',"topic":'Work, Energy & Power',"difficulty":'Hard',
 "question":'A pump raises 300 kg of water to a height of 15 m in 25 seconds (g = 10 m/s^2). What is the power output of the pump?',
 "options":{"A":'1800 W', "B":'4500 W', "C":'180 W', "D":'450 W'},"answer":'A'},

{"id":138,"subject":'Physics',"topic":'Circular Motion & Gravitation',"difficulty":'Easy',
 "question":'For an object undergoing uniform circular motion, its speed remains constant, but its:',
 "options":{"A":'Acceleration is always zero', "B":'Velocity is constantly changing direction, so it does accelerate', "C":'Mass changes continuously', "D":'Radius changes constantly'},"answer":'B'},

{"id":139,"subject":'Physics',"topic":'Circular Motion & Gravitation',"difficulty":'Medium',
 "question":"According to Newton's law of gravitation, if both masses of two objects are doubled while the distance between them remains constant, the gravitational force between them becomes:",
 "options":{"A":'Double the original', "B":'Half the original', "C":'Four times the original', "D":'Unchanged'},"answer":'C'},

{"id":140,"subject":'Physics',"topic":'Circular Motion & Gravitation',"difficulty":'Hard',
 "question":'An astronaut on the Moon, where gravity is about 1/6 that of Earth, would find that their mass:',
 "options":{"A":'Decreases to 1/6 of its Earth value', "B":'Becomes zero on the Moon', "C":'Increases on the Moon', "D":'Remains exactly the same as on Earth, while their weight decreases to about 1/6'},"answer":'D'},

{"id":141,"subject":'Physics',"topic":'Fluid Mechanics',"difficulty":'Easy',
 "question":'The upward force exerted by a fluid on a submerged or floating object is called:',
 "options":{"A":'Buoyant force', "B":'Gravitational force', "C":'Normal force', "D":'Frictional force'},"answer":'A'},

{"id":142,"subject":'Physics',"topic":'Fluid Mechanics',"difficulty":'Medium',
 "question":"According to the continuity equation for an incompressible fluid flowing through a pipe of varying cross-section, when the cross-sectional area decreases, the fluid's speed:",
 "options":{"A":'Decreases', "B":'Increases', "C":'Stays the same', "D":'Becomes zero'},"answer":'B'},

{"id":143,"subject":'Physics',"topic":'Fluid Mechanics',"difficulty":'Hard',
 "question":"A perfume atomizer sprays liquid by blowing air rapidly across the top of a narrow tube dipped in the liquid. This works because, according to Bernoulli's principle, the fast-moving air:",
 "options":{"A":'Creates a region of high pressure that pushes liquid up the tube', "B":'Has no effect on the pressure at the tube opening', "C":'Creates a region of low pressure above the tube, allowing atmospheric pressure to push the liquid up', "D":'Cools the liquid, causing it to rise'},"answer":'C'},

{"id":144,"subject":'Physics',"topic":'Oscillations & Waves',"difficulty":'Easy',
 "question":"The number of complete wave cycles passing a fixed point per second is the wave's:",
 "options":{"A":'Wavelength', "B":'Speed', "C":'Amplitude', "D":'Frequency'},"answer":'D'},

{"id":145,"subject":'Physics',"topic":'Oscillations & Waves',"difficulty":'Medium',
 "question":'In simple harmonic motion, the restoring force acting on the oscillating object is:',
 "options":{"A":'Proportional to the displacement from equilibrium and directed toward equilibrium', "B":'Constant in magnitude and direction at all times', "C":'Always directed away from equilibrium', "D":'Zero everywhere except at equilibrium'},"answer":'A'},

{"id":146,"subject":'Physics',"topic":'Oscillations & Waves',"difficulty":'Medium',
 "question":'A wave traveling at 300 m/s has a frequency of 60 Hz. What is its wavelength?',
 "options":{"A":'18000 m', "B":'5 m', "C":'0.2 m', "D":'360 m'},"answer":'B'},

{"id":147,"subject":'Physics',"topic":'Oscillations & Waves',"difficulty":'Hard',
 "question":'Two sound waves of slightly different frequencies, when heard together, produce a periodic variation in loudness known as:',
 "options":{"A":'Resonance', "B":'The Doppler effect', "C":'Beats', "D":'Interference cancellation only'},"answer":'C'},

{"id":148,"subject":'Physics',"topic":'Thermodynamics',"difficulty":'Easy',
 "question":'The transfer of heat through direct molecular collisions within a solid is called:',
 "options":{"A":'Convection', "B":'Evaporation', "C":'Radiation', "D":'Conduction'},"answer":'D'},

{"id":149,"subject":'Physics',"topic":'Thermodynamics',"difficulty":'Medium',
 "question":'An adiabatic process is one in which:',
 "options":{"A":'No heat is exchanged between the system and its surroundings', "B":'Temperature is held constant', "C":'Pressure is held constant', "D":'Volume is held constant'},"answer":'A'},

{"id":150,"subject":'Physics',"topic":'Thermodynamics',"difficulty":'Hard',
 "question":'A gas is compressed, and 400 J of work is done ON the gas, while the gas simultaneously releases 150 J of heat to its surroundings. What is the change in internal energy of the gas?',
 "options":{"A":'550 J', "B":'250 J', "C":'-250 J', "D":'-550 J'},"answer":'B'},

{"id":151,"subject":'Physics',"topic":'Electrostatics',"difficulty":'Easy',
 "question":'Electric field lines around a single, isolated positive point charge point:',
 "options":{"A":'Toward the charge', "B":'In circles around the charge', "C":'Away from the charge, radially outward', "D":'There is no field around a point charge'},"answer":'C'},

{"id":152,"subject":'Physics',"topic":'Electrostatics',"difficulty":'Medium',
 "question":'The electric potential energy between two point charges depends on:',
 "options":{"A":'Neither the charges nor the distance between them', "B":'Only the distance between them, not the charges', "C":'Only the magnitude of one of the charges', "D":'The magnitude of both charges and the distance between them'},"answer":'D'},

{"id":153,"subject":'Physics',"topic":'Current Electricity',"difficulty":'Easy',
 "question":'A voltmeter is connected across a component in a circuit to measure:',
 "options":{"A":'Potential difference (voltage)', "B":'Current', "C":'Resistance directly', "D":'Power only'},"answer":'A'},

{"id":154,"subject":'Physics',"topic":'Current Electricity',"difficulty":'Medium',
 "question":'In the circuit shown, R1 (6 ohm) is connected in series with a parallel combination of R2 (4 ohm) and R3 (4 ohm). What is the total resistance of the circuit?',
 "image":'images/q_circuit_r1_series_r2r3_parallel.png',
 "options":{"A":'10 ohm', "B":'8 ohm', "C":'14 ohm', "D":'2 ohm'},"answer":'B'},

{"id":155,"subject":'Physics',"topic":'Current Electricity',"difficulty":'Hard',
 "question":'Four identical 8 ohm resistors are connected in parallel. What is their equivalent resistance?',
 "options":{"A":'32 ohm', "B":'8 ohm', "C":'2 ohm', "D":'4 ohm'},"answer":'C'},

{"id":156,"subject":'Physics',"topic":'Current Electricity',"difficulty":'Medium',
 "question":'A heater draws 5 A of current when connected to a 240 V supply. What is its power rating?',
 "options":{"A":'48 W', "B":'245 W', "C":'235 W', "D":'1200 W'},"answer":'D'},

{"id":157,"subject":'Physics',"topic":'Electromagnetism',"difficulty":'Medium',
 "question":'The right-hand rule is commonly used to determine:',
 "options":{"A":'The direction of the magnetic field around a current-carrying wire', "B":'The direction of gravitational force', "C":'The wavelength of a wave', "D":'The frequency of oscillation'},"answer":'A'},

{"id":158,"subject":'Physics',"topic":'Electromagnetism',"difficulty":'Hard',
 "question":'An electric generator converts:',
 "options":{"A":'Chemical energy directly into electrical energy', "B":'Mechanical energy into electrical energy, via electromagnetic induction', "C":'Electrical energy into mechanical energy', "D":'Heat energy directly into light'},"answer":'B'},

{"id":159,"subject":'Physics',"topic":'Modern Physics',"difficulty":'Easy',
 "question":'The mass number of an atom represents:',
 "options":{"A":'The number of protons only', "B":'The number of electrons only', "C":'The total number of protons and neutrons in the nucleus', "D":'The atomic number'},"answer":'C'},

{"id":160,"subject":'Physics',"topic":'Modern Physics',"difficulty":'Medium',
 "question":'In beta-plus (positron) decay, a proton in the nucleus is converted into a neutron with the emission of:',
 "options":{"A":'An electron and an antineutrino', "B":'A gamma ray only', "C":'An alpha particle', "D":'A positron and a neutrino'},"answer":'D'},

{"id":161,"subject":'Physics',"topic":'Modern Physics',"difficulty":'Hard',
 "question":'A radioactive sample initially has a mass of 240 g. After three half-lives, how much of the original sample remains?',
 "options":{"A":'30 g', "B":'60 g', "C":'120 g', "D":'15 g'},"answer":'A'},

{"id":162,"subject":'Physics',"topic":'Optics',"difficulty":'Medium',
 "question":'The ray diagram shows an object placed exactly at the focal point (F) of a converging (convex) lens. Based on the diagram, the rays emerging from the lens are:',
 "image":'images/q_convex_lens_object_at_f.png',
 "options":{"A":'Converging to form a real image at a finite distance', "B":'Parallel to each other, so no real image forms (image at infinity)', "C":'Diverging, as if from a virtual image behind the lens', "D":'Reflected back toward the object'},"answer":'B'},

# ============================================================
# ENGLISH (9) - id 163-171
# ============================================================

{"id":163,"subject":'English',"topic":'Synonyms',"difficulty":'Easy',
 "question":"Choose the word most nearly similar in meaning to 'RETICENT':",
 "options":{"A":'Talkative', "B":'Aggressive', "C":'Reserved', "D":'Curious'},"answer":'C'},

{"id":164,"subject":'English',"topic":'Antonyms',"difficulty":'Easy',
 "question":"Choose the word most nearly opposite in meaning to 'ABUNDANT':",
 "options":{"A":'Vast', "B":'Plentiful', "C":'Generous', "D":'Scarce'},"answer":'D'},

{"id":165,"subject":'English',"topic":'Grammar',"difficulty":'Easy',
 "question":'Choose the grammatically correct sentence:',
 "options":{"A":'The books are on the table.', "B":'The books is on the table.', "C":'The books was on the table.', "D":'The book are on the table.'},"answer":'A'},

{"id":166,"subject":'English',"topic":'Grammar',"difficulty":'Medium',
 "question":'Choose the correct sentence:',
 "options":{"A":'I have seen him yesterday.', "B":'I saw him yesterday.', "C":'I have saw him yesterday.', "D":'I was seeing him yesterday.'},"answer":'B'},

{"id":167,"subject":'English',"topic":'Sentence Correction',"difficulty":'Medium',
 "question":'Choose the sentence that is grammatically correct:',
 "options":{"A":'Neither of the answers are correct.', "B":'Neither of the answer is correct.', "C":'Neither of the answers is correct.', "D":'Neither of the answers were correct.'},"answer":'C'},

{"id":168,"subject":'English',"topic":'Vocabulary',"difficulty":'Medium',
 "question":"Choose the word that best completes the sentence: 'The manager's ______ approach to leadership earned the respect of the entire team.'",
 "options":{"A":'Callous', "B":'Careless', "C":'Erratic', "D":'Fair'},"answer":'D'},

{"id":169,"subject":'English',"topic":'Idioms',"difficulty":'Medium',
 "question":"Choose the meaning closest to the idiom 'to burn the midnight oil':",
 "options":{"A":'To waste time carelessly', "B":'To work or study late into the night', "C":'To start a fire accidentally', "D":'To relax after a long day'},"answer":'B'},

{"id":170,"subject":'English',"topic":'Sentence Correction',"difficulty":'Hard',
 "question":"Choose the option that best corrects the sentence: 'Having finished the exam, the classroom was left by the students.'",
 "options":{"A":'Having finished the exam, the classroom left the students.', "B":'Having finished the exam, the students left the classroom.', "C":'The classroom was left, having finished the exam by the students.', "D":'No correction is needed.'},"answer":'B'},

{"id":171,"subject":'English',"topic":'Prepositions',"difficulty":'Hard',
 "question":"Choose the correct preposition: 'The scientist's discovery contributed greatly ______ our understanding of the disease.'",
 "options":{"A":'for', "B":'with', "C":'to', "D":'at'},"answer":'C'},

# ============================================================
# LOGICAL REASONING (9) - id 172-180
# ============================================================

{"id":172,"subject":'Logical Reasoning',"topic":'Number Series',"difficulty":'Easy',
 "question":'Find the next number in the series: 4, 8, 16, 32, ?',
 "options":{"A":'48', "B":'56', "C":'40', "D":'64'},"answer":'D'},

{"id":173,"subject":'Logical Reasoning',"topic":'Number Series',"difficulty":'Easy',
 "question":'Find the missing number: 3, 9, 27, 81, ?',
 "options":{"A":'243', "B":'200', "C":'162', "D":'100'},"answer":'A'},

{"id":174,"subject":'Logical Reasoning',"topic":'Analogies',"difficulty":'Easy',
 "question":'Hammer is to Nail as Screwdriver is to:',
 "options":{"A":'Wood', "B":'Screw', "C":'Tool', "D":'Handle'},"answer":'B'},

{"id":175,"subject":'Logical Reasoning',"topic":'Analogies',"difficulty":'Medium',
 "question":'Ocean is to Water as Desert is to:',
 "options":{"A":'Cactus', "B":'Heat', "C":'Sand', "D":'Camel'},"answer":'C'},

{"id":176,"subject":'Logical Reasoning',"topic":'Blood Relations',"difficulty":'Medium',
 "question":"A man said, 'This girl is the wife of my only brother's son.' How is the girl related to the man?",
 "options":{"A":'Daughter', "B":'Granddaughter', "C":'Sister', "D":"Daughter-in-law of his brother (his niece's husband's... i.e., his brother's daughter-in-law)"},"answer":'D'},

{"id":177,"subject":'Logical Reasoning',"topic":'Coding-Decoding',"difficulty":'Medium',
 "question":'If in a certain code, HOUSE is written as GNTRD, how is TABLE written in the same code?',
 "options":{"A":'SZAKD', "B":'UBCMF', "C":'SZAKF', "D":'SBAKD'},"answer":'A'},

{"id":178,"subject":'Logical Reasoning',"topic":'Syllogism',"difficulty":'Hard',
 "question":'No reptiles are mammals. All snakes are reptiles. Which conclusion logically follows?',
 "options":{"A":'Some snakes are mammals', "B":'No snakes are mammals', "C":'All mammals are snakes', "D":'All reptiles are snakes'},"answer":'B'},

{"id":179,"subject":'Logical Reasoning',"topic":'Pattern Recognition',"difficulty":'Hard',
 "question":'Find the next term in the series: 100, 96, 89, 79, 66, ?',
 "options":{"A":'55', "B":'52', "C":'50', "D":'48'},"answer":'C'},

{"id":180,"subject":'Logical Reasoning',"topic":'Direction Sense',"difficulty":'Medium',
 "question":'A girl walks 5 km north, then turns left and walks 5 km, then turns left again and walks 5 km, then turns left again and walks 5 km. How far is she from her starting point?',
 "options":{"A":'20 km', "B":'10 km', "C":'5 km', "D":'0 km'},"answer":'D'},

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