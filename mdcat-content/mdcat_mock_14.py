"""
MDCAT Mock Test 14
===================
Full-length mock test: 180 MCQs
Weightage: Biology 81 | Chemistry 45 | Physics 36 | English 9 | Logical Reasoning 9
Difficulty mix (approx): 30% Easy / 50% Medium / 20% Hard, distributed throughout.

Includes 5 image/diagram-based questions (2 Biology, 1 Chemistry, 2 Physics).
Each such question has an "image" key giving a relative path to a PNG diagram
that must be viewed alongside the question (images/ subfolder, shipped alongside
this file). Diagrams: an enzyme activity vs temperature curve, a labeled
neuron diagram, a strong-acid/strong-base titration curve, a projectile-motion
trajectory diagram, and a converging-lens ray diagram.

Each question is a dict:
    id, subject, topic, difficulty, question, [image], options (A-D), answer (correct letter)

Run this file directly to print a summary / sanity-check the paper.
"""

QUESTIONS = [

# ============================================================
# BIOLOGY (81) - id 1-81
# ============================================================

{"id":1,"subject":'Biology',"topic":'Biomolecules',"difficulty":'Easy',
 "question":'Which of the following is a monosaccharide?',
 "options":{"A":'Glucose', "B":'Maltose', "C":'Sucrose', "D":'Lactose'},"answer":'A'},

{"id":2,"subject":'Biology',"topic":'Biomolecules',"difficulty":'Easy',
 "question":'The bond that joins two amino acids together in a protein is called a:',
 "options":{"A":'Peptide bond', "B":'Glycosidic bond', "C":'Ester bond', "D":'Phosphodiester bond'},"answer":'A'},

{"id":3,"subject":'Biology',"topic":'Biomolecules',"difficulty":'Medium',
 "question":'Saturated fatty acids differ from unsaturated fatty acids in that saturated fatty acids:',
 "options":{"A":'Contain one or more carbon-carbon double bonds', "B":'Are always liquid at room temperature', "C":'Contain only carbon-carbon single bonds in their hydrocarbon tail', "D":'Contain a phosphate group'},"answer":'C'},

{"id":4,"subject":'Biology',"topic":'Biomolecules',"difficulty":'Medium',
 "question":'Which of the following most accurately describes the primary structure of a protein?',
 "options":{"A":'The three-dimensional folding of the polypeptide', "B":'Alpha helices and beta sheets stabilized by hydrogen bonds', "C":'The association of multiple polypeptide subunits', "D":'The specific linear sequence of amino acids linked by peptide bonds'},"answer":'D'},

{"id":5,"subject":'Biology',"topic":'Biomolecules',"difficulty":'Hard',
 "question":"Chargaff's rules of base pairing in DNA state that:",
 "options":{"A":'The amount of adenine equals thymine, and the amount of guanine equals cytosine', "B":'The amount of purines always exceeds pyrimidines', "C":'Adenine only pairs with cytosine', "D":'All four bases occur in equal amounts in every organism'},"answer":'A'},

{"id":6,"subject":'Biology',"topic":'Enzymes',"difficulty":'Easy',
 "question":'The specific region of an enzyme where the substrate binds is called the:',
 "options":{"A":'Active site', "B":'Allosteric site', "C":'Binding site for cofactors', "D":'Regulatory site'},"answer":'A'},

{"id":7,"subject":'Biology',"topic":'Enzymes',"difficulty":'Medium',
 "question":'A competitive inhibitor slows an enzyme-catalyzed reaction by:',
 "options":{"A":'Binding only at low substrate concentrations', "B":'Permanently destroying the enzyme structure', "C":'Binding to the active site and preventing substrate binding', "D":'Increasing the enzyme concentration'},"answer":'C'},

{"id":8,"subject":'Biology',"topic":'Enzymes',"difficulty":'Medium',
 "question":'The graph shows enzyme activity plotted against temperature. Activity rises to a maximum near 37 degrees C and then falls sharply. The sharp decrease above 40 degrees C is best explained by:',
 "image":'images/q14_enzyme_temperature_curve.png',
 "options":{"A":'Increased substrate concentration', "B":'A decrease in kinetic energy of molecules', "C":'Formation of more active sites at high temperature', "D":'Denaturation of the enzyme, disrupting its three-dimensional shape'},"answer":'D'},

{"id":9,"subject":'Biology',"topic":'Enzymes',"difficulty":'Hard',
 "question":'A non-competitive inhibitor differs from a competitive inhibitor in that a non-competitive inhibitor:',
 "options":{"A":'Binds at a site other than the active site, changing the enzyme shape so the substrate cannot react effectively', "B":'Can be overcome by increasing substrate concentration', "C":'Binds only at the active site', "D":'Increases the maximum reaction rate (Vmax)'},"answer":'A'},

{"id":10,"subject":'Biology',"topic":'Cell Biology',"difficulty":'Easy',
 "question":'Which organelle is often called the "powerhouse of the cell" because it produces ATP through aerobic respiration?',
 "options":{"A":'Ribosome', "B":'Mitochondrion', "C":'Nucleus', "D":'Lysosome'},"answer":'B'},

{"id":11,"subject":'Biology',"topic":'Cell Biology',"difficulty":'Easy',
 "question":'The primary function of lysosomes in animal cells is:',
 "options":{"A":'Photosynthesis', "B":'Protein synthesis', "C":'Intracellular digestion of macromolecules and worn-out organelles', "D":'Storage of genetic information'},"answer":'C'},

{"id":12,"subject":'Biology',"topic":'Cell Biology',"difficulty":'Medium',
 "question":'Ribosomes bound to the endoplasmic reticulum primarily synthesize proteins that will be:',
 "options":{"A":'Used within the cytosol', "B":'Stored permanently in the nucleus', "C":'Broken down immediately in lysosomes', "D":'Secreted from the cell or inserted into membranes'},"answer":'D'},

{"id":13,"subject":'Biology',"topic":'Cell Biology',"difficulty":'Medium',
 "question":'Which of the following is NOT a component of a prokaryotic cell?',
 "options":{"A":'Membrane-bound nucleus', "B":'Ribosomes', "C":'Plasma membrane', "D":'Cell wall'},"answer":'A'},

{"id":14,"subject":'Biology',"topic":'Cell Biology',"difficulty":'Medium',
 "question":'The Golgi apparatus primarily functions to:',
 "options":{"A":'Generate ATP through oxidative phosphorylation', "B":'Modify, sort, and package proteins and lipids for secretion or delivery to other organelles', "C":'Synthesize DNA during replication', "D":'Break down fatty acids into acetyl-CoA'},"answer":'B'},

{"id":15,"subject":'Biology',"topic":'Cell Biology',"difficulty":'Medium',
 "question":'Which of the following structures is found in plant cells but NOT in typical animal cells?',
 "options":{"A":'Mitochondrion', "B":'Nucleus', "C":'Cell wall made of cellulose', "D":'Ribosome'},"answer":'C'},

{"id":16,"subject":'Biology',"topic":'Cell Biology',"difficulty":'Hard',
 "question":'The endosymbiotic theory proposes that mitochondria and chloroplasts originated from:',
 "options":{"A":'Invaginations of the plasma membrane of ancestral cells', "B":'Sections of the nuclear membrane that broke away', "C":'Viral particles that entered eukaryotic cells', "D":'Free-living prokaryotes that were engulfed by ancestral eukaryotic cells and lived symbiotically'},"answer":'D'},

{"id":17,"subject":'Biology',"topic":'Cell Membrane & Transport',"difficulty":'Easy',
 "question":'The fluid mosaic model describes the plasma membrane as consisting mainly of:',
 "options":{"A":'A phospholipid bilayer with embedded proteins that can move laterally', "B":'A rigid layer of carbohydrates', "C":'A solid single layer of proteins', "D":'A network of cellulose fibers'},"answer":'A'},

{"id":18,"subject":'Biology',"topic":'Cell Membrane & Transport',"difficulty":'Medium',
 "question":'A red blood cell placed in a hypotonic solution will:',
 "options":{"A":'Shrink due to water loss', "B":'Swell and possibly burst (hemolysis) due to water entering the cell', "C":'Remain the same size', "D":'Actively pump ions outward'},"answer":'B'},

{"id":19,"subject":'Biology',"topic":'Cell Membrane & Transport',"difficulty":'Medium',
 "question":'Facilitated diffusion differs from simple diffusion in that facilitated diffusion:',
 "options":{"A":'Requires ATP hydrolysis', "B":'Moves substances against their concentration gradient', "C":'Requires specific membrane transport proteins but does not require energy input', "D":'Only occurs across the nuclear membrane'},"answer":'C'},

{"id":20,"subject":'Biology',"topic":'Cell Membrane & Transport',"difficulty":'Hard',
 "question":'Secondary active transport is characterized by:',
 "options":{"A":'Directly using ATP to move ions across the membrane', "B":'Endocytosis of large particles', "C":'Passive diffusion of gases', "D":'Using the electrochemical gradient of one substance (established by primary active transport) to drive the transport of another substance'},"answer":'D'},

{"id":21,"subject":'Biology',"topic":'Cell Membrane & Transport',"difficulty":'Easy',
 "question":'The process by which a cell engulfs a large solid particle, such as a bacterium, is called:',
 "options":{"A":'Phagocytosis', "B":'Pinocytosis', "C":'Exocytosis', "D":'Osmosis'},"answer":'A'},

{"id":22,"subject":'Biology',"topic":'Cell Cycle & Division',"difficulty":'Easy',
 "question":'The longest phase of the cell cycle, during which the cell grows and DNA is replicated, is:',
 "options":{"A":'Mitosis', "B":'Interphase', "C":'Cytokinesis', "D":'Prophase'},"answer":'B'},

{"id":23,"subject":'Biology',"topic":'Cell Cycle & Division',"difficulty":'Easy',
 "question":'During which stage of mitosis do chromosomes line up along the equatorial plate of the cell?',
 "options":{"A":'Prophase', "B":'Anaphase', "C":'Metaphase', "D":'Telophase'},"answer":'C'},

{"id":24,"subject":'Biology',"topic":'Cell Cycle & Division',"difficulty":'Medium',
 "question":'Crossing over between homologous chromosomes occurs during which phase of meiosis?',
 "options":{"A":'Telophase II', "B":'Metaphase II', "C":'Anaphase I', "D":'Prophase I'},"answer":'D'},

{"id":25,"subject":'Biology',"topic":'Cell Cycle & Division',"difficulty":'Medium',
 "question":'A human cell has 46 chromosomes. After meiosis, each resulting daughter (gamete) cell will contain:',
 "options":{"A":'23 chromosomes', "B":'46 chromosomes', "C":'92 chromosomes', "D":'12 chromosomes'},"answer":'A'},

{"id":26,"subject":'Biology',"topic":'Cell Cycle & Division',"difficulty":'Medium',
 "question":'Uncontrolled cell division, resulting from failure of cell cycle regulation, is a defining feature of:',
 "options":{"A":'Apoptosis', "B":'Cancer', "C":'Differentiation', "D":'Meiosis'},"answer":'B'},

{"id":27,"subject":'Biology',"topic":'Cell Cycle & Division',"difficulty":'Hard',
 "question":'The M-phase (spindle assembly) checkpoint prevents the cell from proceeding into anaphase until:',
 "options":{"A":'DNA replication is complete', "B":'The cell has doubled in size', "C":'All chromosomes are properly attached to spindle fibers at their kinetochores', "D":'All mRNA has been transcribed'},"answer":'C'},

{"id":28,"subject":'Biology',"topic":'Genetics',"difficulty":'Easy',
 "question":'An individual with two identical alleles for a particular gene is said to be:',
 "options":{"A":'Heterozygous', "B":'Dominant', "C":'Recessive', "D":'Homozygous'},"answer":'D'},

{"id":29,"subject":'Biology',"topic":'Genetics',"difficulty":'Medium',
 "question":'In a dihybrid cross between two individuals heterozygous for both traits (AaBb x AaBb), what is the expected phenotypic ratio in the offspring, assuming both traits show complete dominance and independent assortment?',
 "options":{"A":'9:3:3:1', "B":'1:1:1:1', "C":'3:1', "D":'1:2:1'},"answer":'A'},

{"id":30,"subject":'Biology',"topic":'Genetics',"difficulty":'Medium',
 "question":'Color blindness is an X-linked recessive trait. If a color-blind father and a homozygous unaffected mother have children, what proportion of their daughters will be carriers?',
 "options":{"A":'0%', "B":'100%', "C":'50%', "D":'25%'},"answer":'B'},

{"id":31,"subject":'Biology',"topic":'Genetics',"difficulty":'Hard',
 "question":'In snapdragons, red flower color (R) is incompletely dominant over white (r), producing pink heterozygotes. A cross between two pink-flowered plants (Rr x Rr) is expected to produce offspring in what phenotypic ratio?',
 "options":{"A":'3 red : 1 white', "B":'All pink', "C":'1 red : 2 pink : 1 white', "D":'1 red : 1 white'},"answer":'C'},

{"id":32,"subject":'Biology',"topic":'Genetics',"difficulty":'Medium',
 "question":'A man with blood type AB marries a woman with blood type O. Which blood types are possible in their children?',
 "options":{"A":'Only AB', "B":'Only O', "C":'A, B, AB, and O', "D":'A and B only'},"answer":'D'},

{"id":33,"subject":'Biology',"topic":'Genetics',"difficulty":'Hard',
 "question":'A test cross is performed by crossing an individual of unknown genotype with an individual that is:',
 "options":{"A":'Homozygous recessive', "B":'Homozygous dominant', "C":'Heterozygous', "D":'Of the same phenotype only'},"answer":'A'},

{"id":34,"subject":'Biology',"topic":'Genetics',"difficulty":'Medium',
 "question":'A trait controlled by many genes, each with a small additive effect, resulting in a continuous range of phenotypes (such as human skin color or height), is best described as showing:',
 "options":{"A":'Codominance', "B":'Polygenic inheritance', "C":'Incomplete dominance', "D":'Sex linkage'},"answer":'B'},

{"id":35,"subject":'Biology',"topic":'Molecular Biology',"difficulty":'Easy',
 "question":'The complementary base of adenine in a DNA molecule is:',
 "options":{"A":'Cytosine', "B":'Guanine', "C":'Thymine', "D":'Uracil'},"answer":'C'},

{"id":36,"subject":'Biology',"topic":'Molecular Biology',"difficulty":'Easy',
 "question":'DNA replication is described as semi-conservative because each daughter DNA molecule consists of:',
 "options":{"A":'Two newly synthesized strands', "B":'Two original parental strands', "C":'Only RNA nucleotides', "D":'One original (parental) strand and one newly synthesized strand'},"answer":'D'},

{"id":37,"subject":'Biology',"topic":'Molecular Biology',"difficulty":'Medium',
 "question":'During translation, transfer RNA (tRNA) molecules function to:',
 "options":{"A":'Carry specific amino acids to the ribosome and match them to mRNA codons via their anticodons', "B":'Serve as the template for protein synthesis', "C":'Catalyze peptide bond formation', "D":'Splice introns from pre-mRNA'},"answer":'A'},

{"id":38,"subject":'Biology',"topic":'Molecular Biology',"difficulty":'Medium',
 "question":'The stop codons in the standard genetic code are:',
 "options":{"A":'AUG, AUA, AUC', "B":'UAA, UAG, UGA', "C":'GGG, CCC, AAA', "D":'AUG only'},"answer":'B'},

{"id":39,"subject":'Biology',"topic":'Molecular Biology',"difficulty":'Medium',
 "question":'A mutation that changes a codon specifying an amino acid into a stop codon, prematurely terminating translation, is called a:',
 "options":{"A":'Silent mutation', "B":'Missense mutation', "C":'Nonsense mutation', "D":'Frameshift mutation'},"answer":'C'},

{"id":40,"subject":'Biology',"topic":'Molecular Biology',"difficulty":'Hard',
 "question":'A single-nucleotide insertion near the beginning of a protein-coding gene would most likely produce a:',
 "options":{"A":'Silent mutation with no effect on the protein', "B":'Missense mutation changing only one amino acid', "C":'Duplication of the entire chromosome', "D":'Frameshift mutation altering all amino acids downstream of the insertion'},"answer":'D'},

{"id":41,"subject":'Biology',"topic":'Molecular Biology',"difficulty":'Hard',
 "question":'In the lac operon, when lactose is present in the cell, its metabolite (allolactose) acts as an inducer by:',
 "options":{"A":'Binding to the repressor protein, causing it to release the operator and allowing transcription', "B":'Binding to RNA polymerase and blocking transcription', "C":'Directly activating the structural genes', "D":'Degrading the operon DNA'},"answer":'A'},

{"id":42,"subject":'Biology',"topic":'Molecular Biology',"difficulty":'Medium',
 "question":'The removal of non-coding intron sequences from pre-mRNA and joining of the exons is called:',
 "options":{"A":'Transcription', "B":'RNA splicing', "C":'Translation', "D":'Replication'},"answer":'B'},

{"id":43,"subject":'Biology',"topic":'Molecular Biology',"difficulty":'Medium',
 "question":'Which of the following is a key structural difference between DNA and RNA?',
 "options":{"A":'DNA contains ribose while RNA contains deoxyribose', "B":'DNA contains uracil while RNA contains thymine', "C":'DNA is typically double-stranded while RNA is typically single-stranded', "D":'DNA has no phosphate backbone'},"answer":'C'},

{"id":44,"subject":'Biology',"topic":'Molecular Biology',"difficulty":'Easy',
 "question":'The enzyme that unwinds the DNA double helix during replication is:',
 "options":{"A":'DNA polymerase', "B":'RNA polymerase', "C":'Ligase', "D":'Helicase'},"answer":'D'},

{"id":45,"subject":'Biology',"topic":'Evolution',"difficulty":'Easy',
 "question":'The forelimbs of humans, whales, and bats have similar bone structures despite serving very different functions. Such structures are described as:',
 "options":{"A":'Homologous structures', "B":'Analogous structures', "C":'Vestigial structures', "D":'Convergent structures'},"answer":'A'},

{"id":46,"subject":'Biology',"topic":'Evolution',"difficulty":'Medium',
 "question":'Genetic drift has the greatest effect on the allele frequencies of:',
 "options":{"A":'Very large populations with high gene flow', "B":'Small populations, where random events can significantly change allele frequencies', "C":'Populations with high mutation rates only', "D":'Only populations that are extinct'},"answer":'B'},

{"id":47,"subject":'Biology',"topic":'Evolution',"difficulty":'Medium',
 "question":'Two populations of the same species become geographically separated by a mountain range and eventually accumulate enough genetic differences that they can no longer interbreed. This is an example of:',
 "options":{"A":'Sympatric speciation', "B":'Convergent evolution', "C":'Allopatric speciation', "D":'Coevolution'},"answer":'C'},

{"id":48,"subject":'Biology',"topic":'Evolution',"difficulty":'Hard',
 "question":'In a Hardy-Weinberg population, the frequency of the dominant allele (p) is 0.7. What is the expected frequency of heterozygous individuals in the population?',
 "options":{"A":'0.09', "B":'0.21', "C":'0.49', "D":'0.42'},"answer":'D'},

{"id":49,"subject":'Biology',"topic":'Classification & Diversity',"difficulty":'Easy',
 "question":'Which of the following is the correct sequence of taxonomic categories, from most inclusive to least inclusive?',
 "options":{"A":'Kingdom, Phylum, Class, Order, Family, Genus, Species', "B":'Species, Genus, Family, Order, Class, Phylum, Kingdom', "C":'Kingdom, Class, Phylum, Order, Genus, Family, Species', "D":'Phylum, Kingdom, Class, Family, Order, Genus, Species'},"answer":'A'},

{"id":50,"subject":'Biology',"topic":'Classification & Diversity',"difficulty":'Easy',
 "question":'A key characteristic that distinguishes kingdom Fungi from kingdom Plantae is that fungi:',
 "options":{"A":'Are autotrophic', "B":'Have cell walls made of chitin and are heterotrophic (absorptive)', "C":'Have chloroplasts for photosynthesis', "D":'Are always unicellular'},"answer":'B'},

{"id":51,"subject":'Biology',"topic":'Classification & Diversity',"difficulty":'Medium',
 "question":'Viruses are generally not classified in any of the traditional kingdoms of life mainly because they:',
 "options":{"A":'Are too large to observe', "B":'Contain no genetic material', "C":'Lack cellular structure and cannot reproduce or carry out metabolism outside a host cell', "D":'Are exclusively found in soil'},"answer":'C'},

{"id":52,"subject":'Biology',"topic":'Classification & Diversity',"difficulty":'Medium',
 "question":'Members of phylum Arthropoda are characterized by having:',
 "options":{"A":'Radial symmetry and stinging cells', "B":'Soft, unsegmented bodies with a mantle', "C":'A notochord at some stage of development', "D":'A segmented body, jointed appendages, and an exoskeleton made of chitin'},"answer":'D'},

{"id":53,"subject":'Biology',"topic":'Classification & Diversity',"difficulty":'Easy',
 "question":'Which of the following is a defining feature of chordates?',
 "options":{"A":'Presence of a notochord at some stage of development', "B":'External shell of calcium carbonate', "C":'Radial symmetry', "D":'Absence of a nervous system'},"answer":'A'},

{"id":54,"subject":'Biology',"topic":'Classification & Diversity',"difficulty":'Medium',
 "question":'Cnidarians, such as jellyfish and hydra, possess specialized stinging cells used for defense and prey capture called:',
 "options":{"A":'Chloroplasts', "B":'Cnidocytes (containing nematocysts)', "C":'Ribosomes', "D":'Sarcomeres'},"answer":'B'},

{"id":55,"subject":'Biology',"topic":'Plant Biology',"difficulty":'Easy',
 "question":'Xylem tissue in plants is primarily responsible for:',
 "options":{"A":'Transporting sugars from leaves to other parts of the plant', "B":'Producing food through photosynthesis', "C":'Conducting water and dissolved minerals from roots to leaves', "D":'Storing starch reserves'},"answer":'C'},

{"id":56,"subject":'Biology',"topic":'Plant Biology',"difficulty":'Medium',
 "question":'Guard cells regulate the opening and closing of stomata primarily to:',
 "options":{"A":'Absorb sunlight for photosynthesis', "B":'Anchor the plant to the soil', "C":'Transport sugars in phloem', "D":'Control gas exchange and water loss through transpiration'},"answer":'D'},

{"id":57,"subject":'Biology',"topic":'Plant Biology',"difficulty":'Medium',
 "question":'The overall balanced equation for photosynthesis is best represented as:',
 "options":{"A":'6CO2 + 6H2O + light energy -> C6H12O6 + 6O2', "B":'C6H12O6 + 6O2 -> 6CO2 + 6H2O + energy', "C":'6O2 + 6H2O -> C6H12O6 + 6CO2', "D":'C6H12O6 -> 2C2H5OH + 2CO2'},"answer":'A'},

{"id":58,"subject":'Biology',"topic":'Plant Biology',"difficulty":'Hard',
 "question":'C4 plants have an adaptation that allows them to photosynthesize efficiently at high temperatures and low CO2 concentrations. This adaptation involves:',
 "options":{"A":'Fixing CO2 only at night', "B":'Fixing CO2 initially in mesophyll cells using PEP carboxylase, then transferring the fixed carbon to bundle-sheath cells where the Calvin cycle occurs', "C":'Lacking chloroplasts entirely', "D":'Using oxygen instead of carbon dioxide as their carbon source'},"answer":'B'},

{"id":59,"subject":'Biology',"topic":'Plant Biology',"difficulty":'Medium',
 "question":'Auxin, a plant growth hormone, is primarily associated with:',
 "options":{"A":'Causing leaves to abscise (fall off)', "B":'Inducing seed dormancy', "C":'Promoting cell elongation and phototropism (growth toward light)', "D":'Preventing all cell division'},"answer":'C'},

{"id":60,"subject":'Biology',"topic":'Plant Biology',"difficulty":'Easy',
 "question":'In flowering plants, pollen grains are produced within which structure of the flower?',
 "options":{"A":'Ovary', "B":'Stigma', "C":'Sepal', "D":'Anther'},"answer":'D'},

{"id":61,"subject":'Biology',"topic":'Human Physiology - Digestion',"difficulty":'Easy',
 "question":'The enzyme salivary amylase, secreted in the mouth, begins the digestion of:',
 "options":{"A":'Starch (carbohydrates)', "B":'Lipids', "C":'Proteins', "D":'Nucleic acids'},"answer":'A'},

{"id":62,"subject":'Biology',"topic":'Human Physiology - Digestion',"difficulty":'Medium',
 "question":'Bile, produced by the liver and stored in the gallbladder, aids fat digestion mainly by:',
 "options":{"A":'Chemically breaking down fats into glycerol', "B":'Emulsifying fats into smaller droplets, greatly increasing the surface area available for lipase action', "C":'Neutralizing stomach acid entirely', "D":'Absorbing fats directly into the bloodstream'},"answer":'B'},

{"id":63,"subject":'Biology',"topic":'Human Physiology - Digestion',"difficulty":'Medium',
 "question":'Most nutrient absorption in the human digestive system occurs in the:',
 "options":{"A":'Stomach', "B":'Large intestine (colon)', "C":'Small intestine', "D":'Esophagus'},"answer":'C'},

{"id":64,"subject":'Biology',"topic":'Human Physiology - Digestion',"difficulty":'Hard',
 "question":'The villi and microvilli of the small intestine primarily enhance digestion and absorption by:',
 "options":{"A":'Producing hydrochloric acid', "B":'Secreting the majority of digestive enzymes', "C":'Storing bile', "D":'Increasing the surface area available for nutrient absorption'},"answer":'D'},

{"id":65,"subject":'Biology',"topic":'Human Physiology - Circulation',"difficulty":'Easy',
 "question":'Which of the following blood vessels carries oxygenated blood from the lungs back to the heart?',
 "options":{"A":'Pulmonary vein', "B":'Pulmonary artery', "C":'Vena cava', "D":'Aorta'},"answer":'A'},

{"id":66,"subject":'Biology',"topic":'Human Physiology - Circulation',"difficulty":'Medium',
 "question":'The natural pacemaker of the heart, which initiates each heartbeat, is the:',
 "options":{"A":'Atrioventricular (AV) node', "B":'Sinoatrial (SA) node', "C":'Bundle of His', "D":'Purkinje fibers'},"answer":'B'},

{"id":67,"subject":'Biology',"topic":'Human Physiology - Circulation',"difficulty":'Medium',
 "question":'Red blood cells (erythrocytes) are specialized to transport oxygen because they:',
 "options":{"A":'Contain a large nucleus with many chromosomes', "B":'Have many mitochondria for ATP production', "C":'Lack a nucleus and are packed with hemoglobin, which binds oxygen', "D":'Are the largest cells in the blood'},"answer":'C'},

{"id":68,"subject":'Biology',"topic":'Human Physiology - Circulation',"difficulty":'Hard',
 "question":'The Bohr effect describes how, in actively respiring tissues, increased CO2 and lower pH cause hemoglobin to:',
 "options":{"A":'Bind oxygen more tightly, holding onto it longer', "B":'Stop binding oxygen at all in the lungs', "C":'Denature completely', "D":'Release oxygen more readily to the tissues that need it'},"answer":'D'},

{"id":69,"subject":'Biology',"topic":'Human Physiology - Respiration',"difficulty":'Easy',
 "question":'Gas exchange between air and blood in the lungs takes place in the:',
 "options":{"A":'Alveoli', "B":'Bronchi', "C":'Trachea', "D":'Pleura'},"answer":'A'},

{"id":70,"subject":'Biology',"topic":'Human Physiology - Respiration',"difficulty":'Medium',
 "question":'During inhalation (inspiration), the diaphragm:',
 "options":{"A":'Relaxes and moves upward, decreasing thoracic volume', "B":'Contracts and flattens, increasing thoracic volume and decreasing pressure in the lungs', "C":'Remains completely stationary', "D":'Contracts and moves upward'},"answer":'B'},

{"id":71,"subject":'Biology',"topic":'Human Physiology - Respiration',"difficulty":'Medium',
 "question":'The majority of carbon dioxide is transported in the blood in the form of:',
 "options":{"A":'Dissolved CO2 gas in plasma', "B":'Bound to hemoglobin as carbaminohemoglobin only', "C":'Bicarbonate ions (HCO3-)', "D":'Solid carbonate crystals'},"answer":'C'},

{"id":72,"subject":'Biology',"topic":'Human Physiology - Excretion',"difficulty":'Easy',
 "question":'The functional unit of the kidney, responsible for filtering blood and forming urine, is the:',
 "options":{"A":'Alveolus', "B":'Sarcomere', "C":'Neuron', "D":'Nephron'},"answer":'D'},

{"id":73,"subject":'Biology',"topic":'Human Physiology - Excretion',"difficulty":'Medium',
 "question":'Ultrafiltration of blood in the kidney occurs specifically in the:',
 "options":{"A":"Glomerulus within the Bowman's capsule", "B":'Loop of Henle', "C":'Collecting duct', "D":'Renal pelvis'},"answer":'A'},

{"id":74,"subject":'Biology',"topic":'Human Physiology - Excretion',"difficulty":'Hard',
 "question":'The loop of Henle in the kidney primarily functions to:',
 "options":{"A":'Filter blood at the initial site', "B":'Establish a concentration gradient in the medulla that enables the production of concentrated urine', "C":'Store urine before it is excreted', "D":'Produce erythropoietin'},"answer":'B'},

{"id":75,"subject":'Biology',"topic":'Human Physiology - Nervous & Endocrine',"difficulty":'Easy',
 "question":'The small gap between two neurons across which neurotransmitters diffuse is called the:',
 "options":{"A":'Node of Ranvier', "B":'Axon hillock', "C":'Synaptic cleft', "D":'Myelin sheath'},"answer":'C'},

{"id":76,"subject":'Biology',"topic":'Human Physiology - Nervous & Endocrine',"difficulty":'Medium',
 "question":'The labeled diagram shows a neuron. Structure X is a long, thin extension that carries the action potential from the cell body toward other neurons or effector cells. Structure X is the:',
 "image":'images/q14_neuron_diagram_labeled.png',
 "options":{"A":'Dendrite', "B":'Nucleus', "C":'Node of Ranvier', "D":'Axon'},"answer":'D'},

{"id":77,"subject":'Biology',"topic":'Human Physiology - Nervous & Endocrine',"difficulty":'Medium',
 "question":'Insulin, secreted by the beta cells of the pancreas, primarily acts to:',
 "options":{"A":'Lower blood glucose levels by promoting cellular glucose uptake and glycogen synthesis in the liver', "B":'Increase blood glucose levels by stimulating glycogen breakdown', "C":'Stimulate the release of adrenaline', "D":'Increase urine output'},"answer":'A'},

{"id":78,"subject":'Biology',"topic":'Human Physiology - Nervous & Endocrine',"difficulty":'Hard',
 "question":"During the depolarization phase of a neuron's action potential, the membrane potential rapidly becomes more positive primarily because:",
 "options":{"A":'Potassium ions rush out of the cell', "B":'Sodium ion channels open and Na+ ions rush into the cell down their electrochemical gradient', "C":'Chloride ions enter the cell', "D":'The sodium-potassium pump reverses direction'},"answer":'B'},

{"id":79,"subject":'Biology',"topic":'Human Physiology - Reproduction',"difficulty":'Easy',
 "question":'Fertilization in humans normally occurs in the:',
 "options":{"A":'Vagina', "B":'Ovary', "C":'Fallopian tube (oviduct)', "D":'Uterus'},"answer":'C'},

{"id":80,"subject":'Biology',"topic":'Human Physiology - Reproduction',"difficulty":'Medium',
 "question":'The luteinizing hormone (LH) surge during the menstrual cycle directly triggers:',
 "options":{"A":'Menstruation', "B":'Fertilization', "C":'Implantation of the embryo', "D":'Ovulation (release of the egg from the ovary)'},"answer":'D'},

{"id":81,"subject":'Biology',"topic":'Ecology',"difficulty":'Medium',
 "question":'In an ecological food chain, organisms at higher trophic levels typically:',
 "options":{"A":'Receive only about 10% of the energy available at the trophic level below them, due to energy losses at each transfer', "B":'Have access to more total energy than producers', "C":'Do not depend on other organisms for energy', "D":'Include only decomposers'},"answer":'A'},

# ============================================================
# CHEMISTRY (45) - id 82-126
# ============================================================

{"id":82,"subject":'Chemistry',"topic":'Atomic Structure',"difficulty":'Easy',
 "question":'The subatomic particle with a positive charge, located in the nucleus, is the:',
 "options":{"A":'Electron', "B":'Proton', "C":'Neutron', "D":'Positron'},"answer":'B'},

{"id":83,"subject":'Chemistry',"topic":'Atomic Structure',"difficulty":'Medium',
 "question":'The number of orbitals in the 3d subshell is:',
 "options":{"A":'1', "B":'3', "C":'5', "D":'7'},"answer":'C'},

{"id":84,"subject":'Chemistry',"topic":'Atomic Structure',"difficulty":'Medium',
 "question":'The electron configuration of a neutral sodium atom (Z = 11) is:',
 "options":{"A":'1s2 2s2 2p6 3s2', "B":'1s2 2s2 2p6', "C":'1s2 2s2 2p5 3s2', "D":'1s2 2s2 2p6 3s1'},"answer":'D'},

{"id":85,"subject":'Chemistry',"topic":'Atomic Structure',"difficulty":'Hard',
 "question":'A neutral atom of magnesium (Z = 12) loses 2 electrons. The resulting ion has an electron configuration identical to that of:',
 "options":{"A":'Neon', "B":'Sodium', "C":'Argon', "D":'Helium'},"answer":'A'},

{"id":86,"subject":'Chemistry',"topic":'Periodic Table',"difficulty":'Easy',
 "question":'The elements of Group 1 in the periodic table are commonly known as:',
 "options":{"A":'Halogens', "B":'Alkali metals', "C":'Noble gases', "D":'Alkaline earth metals'},"answer":'B'},

{"id":87,"subject":'Chemistry',"topic":'Periodic Table',"difficulty":'Medium',
 "question":'Ionization energy generally increases across a period from left to right primarily because:',
 "options":{"A":'Atomic radius increases across a period', "B":'The number of electron shells increases dramatically', "C":'Nuclear charge increases while electrons enter the same principal shell, so valence electrons are held more tightly', "D":'Shielding effect increases greatly'},"answer":'C'},

{"id":88,"subject":'Chemistry',"topic":'Periodic Table',"difficulty":'Medium',
 "question":'Which of the following elements has the highest electronegativity?',
 "options":{"A":'Chlorine', "B":'Oxygen', "C":'Nitrogen', "D":'Fluorine'},"answer":'D'},

{"id":89,"subject":'Chemistry',"topic":'Chemical Bonding',"difficulty":'Easy',
 "question":'A covalent bond forms when two atoms:',
 "options":{"A":'Share one or more pairs of electrons', "B":'Completely transfer electrons from one to the other', "C":'Attract each other through gravitational forces', "D":'Ionize to form charged particles'},"answer":'A'},

{"id":90,"subject":'Chemistry',"topic":'Chemical Bonding',"difficulty":'Medium',
 "question":'According to VSEPR theory, a water molecule (H2O), with two bonding pairs and two lone pairs on the central oxygen, has a molecular shape described as:',
 "options":{"A":'Linear', "B":'Bent (angular)', "C":'Tetrahedral', "D":'Trigonal planar'},"answer":'B'},

{"id":91,"subject":'Chemistry',"topic":'Chemical Bonding',"difficulty":'Medium',
 "question":'Carbon dioxide (CO2) is a nonpolar molecule despite having polar C=O bonds because:',
 "options":{"A":'Oxygen and carbon have identical electronegativities', "B":'It contains no lone pairs on the central atom', "C":'Its linear geometry causes the two bond dipoles to cancel each other out exactly', "D":'It has hydrogen bonding that neutralizes the dipoles'},"answer":'C'},

{"id":92,"subject":'Chemistry',"topic":'Chemical Bonding',"difficulty":'Hard',
 "question":'Hydrogen bonding is much stronger than typical van der Waals forces because it involves:',
 "options":{"A":'The complete transfer of electrons between molecules', "B":'The sharing of electrons within a single covalent bond', "C":'Only temporary induced dipoles between nonpolar molecules', "D":'An attraction between a hydrogen atom bonded to a highly electronegative atom (N, O, or F) and a lone pair on another electronegative atom'},"answer":'D'},

{"id":93,"subject":'Chemistry',"topic":'States of Matter',"difficulty":'Easy',
 "question":'At the same temperature and pressure, gas molecules have significantly higher kinetic energy and much greater freedom of motion than particles in liquids and solids because gases:',
 "options":{"A":'Have very weak intermolecular forces and their molecules are far apart', "B":'Have very strong intermolecular forces', "C":'Contain only heavy molecules', "D":'Do not obey any physical laws'},"answer":'A'},

{"id":94,"subject":'Chemistry',"topic":'States of Matter',"difficulty":'Medium',
 "question":"A sample of gas has a volume of 3.0 L at 300 K and 1.0 atm. What will its volume be at 600 K if the pressure remains constant (Charles's Law)?",
 "options":{"A":'1.5 L', "B":'6.0 L', "C":'3.0 L', "D":'9.0 L'},"answer":'B'},

{"id":95,"subject":'Chemistry',"topic":'States of Matter',"difficulty":'Hard',
 "question":'How many moles of an ideal gas are contained in a 22.4 L vessel at standard temperature and pressure (STP: 0 degrees C, 1 atm)?',
 "options":{"A":'0.5 mol', "B":'2 mol', "C":'1 mol', "D":'22.4 mol'},"answer":'C'},

{"id":96,"subject":'Chemistry',"topic":'Stoichiometry',"difficulty":'Easy',
 "question":'The molar mass of water (H2O) is approximately:',
 "options":{"A":'10 g/mol', "B":'16 g/mol', "C":'32 g/mol', "D":'18 g/mol'},"answer":'D'},

{"id":97,"subject":'Chemistry',"topic":'Stoichiometry',"difficulty":'Medium',
 "question":'How many moles are present in 22 g of carbon dioxide (CO2, molar mass 44 g/mol)?',
 "options":{"A":'0.5 mol', "B":'1 mol', "C":'2 mol', "D":'22 mol'},"answer":'A'},

{"id":98,"subject":'Chemistry',"topic":'Stoichiometry',"difficulty":'Hard',
 "question":'What mass of NaCl (molar mass 58.5 g/mol) is required to prepare 500 mL of a 0.2 M solution?',
 "options":{"A":'11.7 g', "B":'5.85 g', "C":'58.5 g', "D":'2.925 g'},"answer":'B'},

{"id":99,"subject":'Chemistry',"topic":'Stoichiometry',"difficulty":'Medium',
 "question":'In the balanced equation 2H2 + O2 -> 2H2O, how many moles of water are produced when 4 moles of hydrogen react completely with excess oxygen?',
 "options":{"A":'2 mol', "B":'8 mol', "C":'4 mol', "D":'1 mol'},"answer":'C'},

{"id":100,"subject":'Chemistry',"topic":'Thermochemistry',"difficulty":'Easy',
 "question":'An endothermic reaction is one in which:',
 "options":{"A":'Heat is released to the surroundings', "B":'Only light energy is exchanged', "C":'No heat change occurs', "D":'Heat is absorbed from the surroundings'},"answer":'D'},

{"id":101,"subject":'Chemistry',"topic":'Thermochemistry',"difficulty":'Medium',
 "question":'The standard enthalpy of formation of an element in its most stable form at standard conditions is defined as:',
 "options":{"A":'Zero, by convention', "B":'The energy required to ionize the element', "C":'Equal to its atomic mass', "D":'Equal to its bond energy'},"answer":'A'},

{"id":102,"subject":'Chemistry',"topic":'Chemical Equilibrium',"difficulty":'Medium',
 "question":"Le Chatelier's principle predicts that if the pressure on an equilibrium mixture of gases is increased, the equilibrium will shift toward:",
 "options":{"A":'The side with the greater number of moles of gas', "B":'The side with the fewer number of moles of gas, reducing the pressure', "C":'Neither side, since pressure has no effect', "D":'The side with the highest temperature'},"answer":'B'},

{"id":103,"subject":'Chemistry',"topic":'Chemical Equilibrium',"difficulty":'Hard',
 "question":'For a reaction with Keq >> 1, at equilibrium the reaction mixture will contain:',
 "options":{"A":'Predominantly reactants, with very few products', "B":'Exactly equal amounts of reactants and products', "C":'Predominantly products, with very few reactants', "D":'No reactants and no products'},"answer":'C'},

{"id":104,"subject":'Chemistry',"topic":'Reaction Kinetics',"difficulty":'Easy',
 "question":'Increasing the temperature of a chemical reaction generally increases the reaction rate mainly because:',
 "options":{"A":'The activation energy of the reaction decreases', "B":'The concentration of reactants increases', "C":'The catalyst becomes more effective only at high temperature', "D":'The kinetic energy of the reactant molecules increases, so more molecules have enough energy to overcome the activation barrier'},"answer":'D'},

{"id":105,"subject":'Chemistry',"topic":'Reaction Kinetics',"difficulty":'Medium',
 "question":'For a reaction with rate law rate = k[A]^2, if the concentration of A is doubled, the reaction rate will:',
 "options":{"A":'Quadruple (increase fourfold)', "B":'Double', "C":'Remain unchanged', "D":'Be cut in half'},"answer":'A'},

{"id":106,"subject":'Chemistry',"topic":'Electrochemistry',"difficulty":'Medium',
 "question":'In a galvanic (voltaic) cell, the anode is the electrode at which:',
 "options":{"A":'Reduction takes place and electrons are gained', "B":'Oxidation takes place and electrons are released into the external circuit', "C":'No chemical reaction takes place', "D":'Water is decomposed'},"answer":'B'},

{"id":107,"subject":'Chemistry',"topic":'Electrochemistry',"difficulty":'Hard',
 "question":'The purpose of a salt bridge in an electrochemical cell is to:',
 "options":{"A":'Provide a path for electrons to flow between the electrodes', "B":'Speed up the reaction by heating the solutions', "C":'Maintain electrical neutrality in the two half-cells by allowing ion migration between them', "D":'Prevent any current from flowing'},"answer":'C'},

{"id":108,"subject":'Chemistry',"topic":'Acids & Bases',"difficulty":'Easy',
 "question":'According to the Bronsted-Lowry definition, an acid is a substance that:',
 "options":{"A":'Accepts a proton (H+)', "B":'Donates a pair of electrons', "C":'Accepts a pair of electrons', "D":'Donates a proton (H+)'},"answer":'D'},

{"id":109,"subject":'Chemistry',"topic":'Acids & Bases',"difficulty":'Medium',
 "question":'A solution with a pH of 4 is:',
 "options":{"A":'Acidic and 100 times more acidic than a solution with a pH of 6', "B":'Basic and 100 times more basic than a solution with a pH of 6', "C":'Neutral', "D":'Basic and 10 times more basic than a solution with a pH of 6'},"answer":'A'},

{"id":110,"subject":'Chemistry',"topic":'Acids & Bases',"difficulty":'Medium',
 "question":'The graph shows the pH curve for the titration of a strong acid (HCl) with a strong base (NaOH). At the equivalence point, the pH is expected to be:',
 "image":'images/q14_titration_strong_acid_strong_base.png',
 "options":{"A":'Less than 7, because the resulting salt is acidic', "B":'Exactly 7, since the salt formed (NaCl) does not undergo hydrolysis', "C":'Greater than 7, because the resulting salt is basic', "D":'Extremely low, near pH 1'},"answer":'B'},

{"id":111,"subject":'Chemistry',"topic":'Acids & Bases',"difficulty":'Hard',
 "question":'A buffer solution is best described as a solution that:',
 "options":{"A":'Has a pH of exactly 7 at all times', "B":'Contains only a strong acid and a strong base', "C":'Resists changes in pH when small amounts of acid or base are added, typically containing a weak acid and its conjugate base (or a weak base and its conjugate acid)', "D":'Cannot be diluted with water'},"answer":'C'},

{"id":112,"subject":'Chemistry',"topic":'Organic Chemistry',"difficulty":'Easy',
 "question":'The general molecular formula for alkanes is:',
 "options":{"A":'CnH2n', "B":'CnHn', "C":'CnH2n-2', "D":'CnH2n+2'},"answer":'D'},

{"id":113,"subject":'Chemistry',"topic":'Organic Chemistry',"difficulty":'Medium',
 "question":'Which of the following is a characteristic reaction of alkenes?',
 "options":{"A":'Addition reactions across the carbon-carbon double bond, such as addition of hydrogen or bromine', "B":'Substitution reactions with halogens under normal conditions', "C":'Combustion reactions only', "D":'Polymerization is impossible for alkenes'},"answer":'A'},

{"id":114,"subject":'Chemistry',"topic":'Organic Chemistry',"difficulty":'Medium',
 "question":'The functional group -COOH is characteristic of:',
 "options":{"A":'Alcohols', "B":'Carboxylic acids', "C":'Ketones', "D":'Aldehydes'},"answer":'B'},

{"id":115,"subject":'Chemistry',"topic":'Organic Chemistry',"difficulty":'Hard',
 "question":'Benzene undergoes electrophilic substitution rather than addition reactions because:',
 "options":{"A":'It has a very unreactive single bond', "B":'Benzene contains no double bonds at all', "C":'Substitution preserves the stable delocalized pi-electron system of the aromatic ring, while addition would disrupt it', "D":'Its molecules are too large to react by addition'},"answer":'C'},

{"id":116,"subject":'Chemistry',"topic":'Organic Chemistry',"difficulty":'Medium',
 "question":'Esters are typically formed by the reaction of a carboxylic acid and an alcohol, catalyzed by a small amount of concentrated acid. This process is called:',
 "options":{"A":'Saponification', "B":'Hydrolysis', "C":'Halogenation', "D":'Esterification (a condensation reaction that releases water)'},"answer":'D'},

{"id":117,"subject":'Chemistry',"topic":'Organic Chemistry',"difficulty":'Easy',
 "question":'Two compounds with the same molecular formula but different structural arrangements of atoms are called:',
 "options":{"A":'Structural (constitutional) isomers', "B":'Isotopes', "C":'Allotropes', "D":'Polymers'},"answer":'A'},

{"id":118,"subject":'Chemistry',"topic":'Inorganic Chemistry',"difficulty":'Medium',
 "question":'Which of the following halogens is the most reactive?',
 "options":{"A":'Chlorine', "B":'Fluorine', "C":'Bromine', "D":'Iodine'},"answer":'B'},

{"id":119,"subject":'Chemistry',"topic":'Inorganic Chemistry',"difficulty":'Medium',
 "question":'Transition metals often form colored compounds mainly because of:',
 "options":{"A":'The absence of any d-electrons', "B":'Ionic bonding in the compound', "C":'d-d electronic transitions in which visible light is absorbed by the metal ion, promoting electrons between split d-orbitals', "D":'Their large atomic mass'},"answer":'C'},

{"id":120,"subject":'Chemistry',"topic":'Inorganic Chemistry',"difficulty":'Hard',
 "question":'In the reaction 2Na + Cl2 -> 2NaCl, sodium is oxidized. This means sodium:',
 "options":{"A":'Gains electrons and its oxidation number decreases', "B":'Only shares electrons with chlorine', "C":'Does not change its oxidation state', "D":'Loses electrons and its oxidation number increases from 0 to +1'},"answer":'D'},

{"id":121,"subject":'Chemistry',"topic":'Physical Chemistry',"difficulty":'Medium',
 "question":'The vapor pressure of a solvent is lowered when a non-volatile solute is dissolved in it. This is an example of a:',
 "options":{"A":'Colligative property, which depends on the number of solute particles, not their identity', "B":'Property that depends only on the mass of the solute', "C":'Chemical reaction between solvent and solute', "D":'Property that only applies to gases'},"answer":'A'},

{"id":122,"subject":'Chemistry',"topic":'Physical Chemistry',"difficulty":'Hard',
 "question":'25 mL of 0.1 M NaOH exactly neutralizes 50 mL of an HCl solution (NaOH + HCl -> NaCl + H2O). What is the molarity of the HCl solution?',
 "options":{"A":'0.10 M', "B":'0.05 M', "C":'0.20 M', "D":'0.025 M'},"answer":'B'},

{"id":123,"subject":'Chemistry',"topic":'Environmental Chemistry',"difficulty":'Easy',
 "question":'Acid rain is primarily caused by atmospheric pollutants such as:',
 "options":{"A":'Oxygen and nitrogen', "B":'Carbon dioxide only', "C":'Sulfur dioxide (SO2) and nitrogen oxides (NOx), which react with water in the atmosphere to form sulfuric and nitric acids', "D":'Methane and helium'},"answer":'C'},

{"id":124,"subject":'Chemistry',"topic":'Environmental Chemistry',"difficulty":'Medium',
 "question":'The depletion of the ozone layer in the upper atmosphere has been linked mainly to the release of:',
 "options":{"A":'Carbon dioxide from respiration', "B":'Molecular nitrogen from the atmosphere', "C":'Water vapor', "D":'Chlorofluorocarbons (CFCs), whose chlorine atoms catalyze the destruction of ozone molecules'},"answer":'D'},

{"id":125,"subject":'Chemistry',"topic":'Chemical Bonding',"difficulty":'Easy',
 "question":'Which of the following molecules contains a triple bond?',
 "options":{"A":'N2', "B":'O2', "C":'H2O', "D":'CH4'},"answer":'A'},

{"id":126,"subject":'Chemistry',"topic":'Atomic Structure',"difficulty":'Easy',
 "question":'The maximum number of electrons that can occupy a single atomic orbital is:',
 "options":{"A":'1', "B":'2', "C":'4', "D":'8'},"answer":'B'},

# ============================================================
# PHYSICS (36) - id 127-162
# ============================================================

{"id":127,"subject":'Physics',"topic":'Kinematics',"difficulty":'Easy',
 "question":'A car travels 150 km in 3 hours at constant velocity. What is its average speed?',
 "options":{"A":'500 km/h', "B":'45 km/h', "C":'50 km/h', "D":'15 km/h'},"answer":'C'},

{"id":128,"subject":'Physics',"topic":'Kinematics',"difficulty":'Medium',
 "question":'A cyclist accelerates uniformly from rest to 20 m/s in 5 seconds. What is the magnitude of the acceleration?',
 "options":{"A":'2 m/s^2', "B":'100 m/s^2', "C":'25 m/s^2', "D":'4 m/s^2'},"answer":'D'},

{"id":129,"subject":'Physics',"topic":'Kinematics',"difficulty":'Hard',
 "question":"The diagram shows the trajectory of a projectile launched from the ground at an angle to the horizontal, ignoring air resistance. At the highest point of the trajectory, the projectile's:",
 "image":'images/q14_projectile_trajectory_diagram.png',
 "options":{"A":'Vertical velocity component is zero, while its horizontal velocity component remains constant', "B":'Vertical and horizontal velocity components are both zero', "C":'Acceleration is zero', "D":'Horizontal velocity component is zero while vertical velocity remains constant'},"answer":'A'},

{"id":130,"subject":'Physics',"topic":'Dynamics',"difficulty":'Easy',
 "question":"According to Newton's third law of motion, for every action there is:",
 "options":{"A":'A greater reaction force', "B":'An equal and opposite reaction force', "C":'No reaction force at all', "D":'A parallel reaction force in the same direction'},"answer":'B'},

{"id":131,"subject":'Physics',"topic":'Dynamics',"difficulty":'Medium',
 "question":'A net force of 20 N acts on a 5 kg object. What is the resulting acceleration of the object?',
 "options":{"A":'100 m/s^2', "B":'25 m/s^2', "C":'4 m/s^2', "D":'0.25 m/s^2'},"answer":'C'},

{"id":132,"subject":'Physics',"topic":'Dynamics',"difficulty":'Medium',
 "question":'Momentum is defined as:',
 "options":{"A":'The sum of kinetic and potential energy', "B":'The product of mass and acceleration', "C":'The product of force and time only', "D":'The product of mass and velocity'},"answer":'D'},

{"id":133,"subject":'Physics',"topic":'Dynamics',"difficulty":'Hard',
 "question":'Two objects of masses 3 kg and 5 kg are moving toward each other with speeds of 4 m/s and 2 m/s respectively. If they undergo a perfectly inelastic collision, what is the speed of the combined object immediately after collision?',
 "options":{"A":'0.25 m/s', "B":'1.0 m/s', "C":'2.0 m/s', "D":'6.0 m/s'},"answer":'A'},

{"id":134,"subject":'Physics',"topic":'Work, Energy & Power',"difficulty":'Easy',
 "question":'The SI unit of work and energy is the:',
 "options":{"A":'Pascal', "B":'Joule', "C":'Newton', "D":'Watt'},"answer":'B'},

{"id":135,"subject":'Physics',"topic":'Work, Energy & Power',"difficulty":'Medium',
 "question":'How much work is done when a force of 50 N moves an object a distance of 4 m in the direction of the force?',
 "options":{"A":'12.5 J', "B":'54 J', "C":'200 J', "D":'2000 J'},"answer":'C'},

{"id":136,"subject":'Physics',"topic":'Work, Energy & Power',"difficulty":'Medium',
 "question":'A 2 kg object is moving at 10 m/s. Its kinetic energy is:',
 "options":{"A":'20 J', "B":'400 J', "C":'200 J', "D":'100 J'},"answer":'D'},

{"id":137,"subject":'Physics',"topic":'Work, Energy & Power',"difficulty":'Hard',
 "question":'An electric motor lifts a 100 kg mass through a height of 10 m in 20 seconds (g = 10 m/s^2). What is the average power output of the motor?',
 "options":{"A":'500 W', "B":'50 W', "C":'1000 W', "D":'5000 W'},"answer":'A'},

{"id":138,"subject":'Physics',"topic":'Circular Motion & Gravitation',"difficulty":'Easy',
 "question":'The force required to keep an object moving in a circular path, directed toward the center of the circle, is called the:',
 "options":{"A":'Centrifugal force', "B":'Centripetal force', "C":'Gravitational force only', "D":'Frictional force'},"answer":'B'},

{"id":139,"subject":'Physics',"topic":'Circular Motion & Gravitation',"difficulty":'Medium',
 "question":"According to Newton's law of universal gravitation, if the mass of one of two objects is doubled while all other factors remain constant, the gravitational force between them will:",
 "options":{"A":'Remain the same', "B":'Be halved', "C":'Double', "D":'Quadruple'},"answer":'C'},

{"id":140,"subject":'Physics',"topic":'Circular Motion & Gravitation',"difficulty":'Hard',
 "question":'An object in a geostationary orbit around Earth has an orbital period equal to:',
 "options":{"A":'1 hour', "B":'12 hours', "C":'365 days', "D":'24 hours (one sidereal day)'},"answer":'D'},

{"id":141,"subject":'Physics',"topic":'Fluid Mechanics',"difficulty":'Easy',
 "question":'The pressure exerted by a fluid at a given depth depends on:',
 "options":{"A":'The density of the fluid, the depth, and the gravitational acceleration', "B":'The shape of the container only', "C":'The color of the fluid', "D":'The volume of the container'},"answer":'A'},

{"id":142,"subject":'Physics',"topic":'Fluid Mechanics',"difficulty":'Medium',
 "question":'An object floats in a fluid when:',
 "options":{"A":'Its density is greater than the density of the fluid', "B":'Its density is less than or equal to the density of the fluid, so buoyant force equals or exceeds its weight', "C":'It has zero mass', "D":'The fluid is completely still'},"answer":'B'},

{"id":143,"subject":'Physics',"topic":'Fluid Mechanics',"difficulty":'Hard',
 "question":'The equation of continuity for an incompressible fluid flowing in a pipe (A1v1 = A2v2) implies that if the cross-sectional area of the pipe decreases, the fluid speed:',
 "options":{"A":'Decreases proportionally', "B":'Remains constant', "C":'Increases proportionally', "D":'Becomes zero'},"answer":'C'},

{"id":144,"subject":'Physics',"topic":'Oscillations & Waves',"difficulty":'Easy',
 "question":'A transverse wave is one in which the particle displacement is:',
 "options":{"A":'Parallel to the direction of wave propagation', "B":'Zero at all times', "C":'At a 45-degree angle to the direction of propagation', "D":'Perpendicular to the direction of wave propagation'},"answer":'D'},

{"id":145,"subject":'Physics',"topic":'Oscillations & Waves',"difficulty":'Medium',
 "question":'The period of a simple pendulum of length L is approximately (for small oscillations):',
 "options":{"A":'T = 2 pi sqrt(L/g)', "B":'T = 2 pi sqrt(g/L)', "C":'T = 2 pi L g', "D":'T = 1 / (2 pi sqrt(L g))'},"answer":'A'},

{"id":146,"subject":'Physics',"topic":'Oscillations & Waves',"difficulty":'Medium',
 "question":'A wave has a frequency of 500 Hz and a wavelength of 0.6 m. What is its speed?',
 "options":{"A":'833 m/s', "B":'300 m/s', "C":'0.0012 m/s', "D":'3000 m/s'},"answer":'B'},

{"id":147,"subject":'Physics',"topic":'Oscillations & Waves',"difficulty":'Hard',
 "question":'The Doppler effect describes the change in observed frequency of a wave when:',
 "options":{"A":'The wave amplitude changes', "B":'The wave passes through different media', "C":'The source or observer is moving relative to the medium', "D":'The wave is reflected off a stationary surface only'},"answer":'C'},

{"id":148,"subject":'Physics',"topic":'Thermodynamics',"difficulty":'Easy',
 "question":'The first law of thermodynamics is essentially a statement of the:',
 "options":{"A":'Conservation of charge', "B":'Conservation of mass', "C":'Conservation of momentum', "D":'Conservation of energy'},"answer":'D'},

{"id":149,"subject":'Physics',"topic":'Thermodynamics',"difficulty":'Medium',
 "question":'The second law of thermodynamics states that in any spontaneous process, the total entropy of an isolated system:',
 "options":{"A":'Increases or remains constant', "B":'Decreases', "C":'Always remains constant', "D":'Approaches zero'},"answer":'A'},

{"id":150,"subject":'Physics',"topic":'Thermodynamics',"difficulty":'Hard',
 "question":'A heat engine operates between a hot reservoir at 400 K and a cold reservoir at 300 K. What is its maximum theoretical (Carnot) efficiency?',
 "options":{"A":'33%', "B":'25%', "C":'75%', "D":'100%'},"answer":'B'},

{"id":151,"subject":'Physics',"topic":'Electrostatics',"difficulty":'Easy',
 "question":"Coulomb's law describes the force between two point charges. The force is:",
 "options":{"A":'Directly proportional to the square of the distance between the charges', "B":'Independent of distance between the charges', "C":'Directly proportional to the product of the charges and inversely proportional to the square of the distance between them', "D":'Independent of the magnitude of the charges'},"answer":'C'},

{"id":152,"subject":'Physics',"topic":'Electrostatics',"difficulty":'Medium',
 "question":'The capacitance of a parallel-plate capacitor is increased when:',
 "options":{"A":'The distance between the plates is increased', "B":'The applied voltage is decreased', "C":'The area of the plates is decreased', "D":'A dielectric material with higher permittivity is inserted between the plates'},"answer":'D'},

{"id":153,"subject":'Physics',"topic":'Current Electricity',"difficulty":'Easy',
 "question":"Ohm's law states that the voltage across a conductor is:",
 "options":{"A":'Directly proportional to the current through it, at constant temperature', "B":'Inversely proportional to the current through it', "C":'Independent of the current', "D":'Equal to the square of the current'},"answer":'A'},

{"id":154,"subject":'Physics',"topic":'Current Electricity',"difficulty":'Medium',
 "question":'The circuit diagram shows a converging lens with an object placed beyond twice the focal length (2F). Based on the ray diagram, the image formed is:',
 "image":'images/q14_converging_lens_ray_diagram.png',
 "options":{"A":'Virtual, upright, and magnified', "B":'Real, inverted, and diminished, located between F and 2F on the other side of the lens', "C":'Real, upright, and the same size as the object', "D":'Virtual, inverted, and diminished'},"answer":'B'},

{"id":155,"subject":'Physics',"topic":'Current Electricity',"difficulty":'Hard',
 "question":'Three resistors of 6 ohm each are connected in parallel. What is the equivalent resistance of the combination?',
 "options":{"A":'18 ohm', "B":'6 ohm', "C":'2 ohm', "D":'0.5 ohm'},"answer":'C'},

{"id":156,"subject":'Physics',"topic":'Current Electricity',"difficulty":'Medium',
 "question":'A 60 W light bulb operates at 120 V. What is the current through the bulb?',
 "options":{"A":'7200 A', "B":'2 A', "C":'60 A', "D":'0.5 A'},"answer":'D'},

{"id":157,"subject":'Physics',"topic":'Electromagnetism',"difficulty":'Medium',
 "question":'A current-carrying wire produces a magnetic field around it whose direction can be determined by:',
 "options":{"A":'The right-hand grip rule (thumb points in the direction of current, fingers curl in the direction of the magnetic field)', "B":"Newton's first law of motion", "C":'The left-hand slap rule for gravity', "D":'The inverse-square law only'},"answer":'A'},

{"id":158,"subject":'Physics',"topic":'Electromagnetism',"difficulty":'Hard',
 "question":'A transformer with 200 turns in the primary coil and 1000 turns in the secondary coil is supplied with 240 V AC on the primary. Assuming ideal behavior, the secondary voltage is:',
 "options":{"A":'48 V', "B":'1200 V', "C":'240 V', "D":'2000 V'},"answer":'B'},

{"id":159,"subject":'Physics',"topic":'Modern Physics',"difficulty":'Easy',
 "question":'The photoelectric effect provides strong evidence that light behaves as:',
 "options":{"A":'A continuous wave only', "B":'A stream of positively charged particles', "C":'Discrete packets of energy called photons', "D":'A gravitational wave'},"answer":'C'},

{"id":160,"subject":'Physics',"topic":'Modern Physics',"difficulty":'Medium',
 "question":'When a uranium-238 nucleus undergoes alpha decay, it releases an alpha particle and transforms into a nucleus with:',
 "options":{"A":'The same atomic number but a smaller mass number', "B":'A larger atomic number and the same mass number', "C":'A larger atomic number and larger mass number', "D":'An atomic number that is 2 less and a mass number that is 4 less than uranium-238'},"answer":'D'},

{"id":161,"subject":'Physics',"topic":'Modern Physics',"difficulty":'Hard',
 "question":'A sample containing 800 g of a radioactive isotope with a half-life of 5 years will contain approximately how much of the original isotope after 20 years?',
 "options":{"A":'50 g', "B":'200 g', "C":'400 g', "D":'25 g'},"answer":'A'},

{"id":162,"subject":'Physics',"topic":'Optics',"difficulty":'Medium',
 "question":'The phenomenon of total internal reflection can occur when light travels:',
 "options":{"A":'From a less dense medium to a more dense medium at any angle', "B":'From a more dense (optically denser) medium to a less dense medium, at an angle greater than the critical angle', "C":'Through a vacuum at any angle', "D":'From a medium to itself'},"answer":'B'},

# ============================================================
# ENGLISH (9) - id 163-171
# ============================================================

{"id":163,"subject":'English',"topic":'Synonyms',"difficulty":'Easy',
 "question":"Choose the word most nearly similar in meaning to 'BENEVOLENT':",
 "options":{"A":'Hostile', "B":'Cruel', "C":'Kind', "D":'Selfish'},"answer":'C'},

{"id":164,"subject":'English',"topic":'Antonyms',"difficulty":'Easy',
 "question":"Choose the word most nearly opposite in meaning to 'ABUNDANT':",
 "options":{"A":'Ample', "B":'Plentiful', "C":'Numerous', "D":'Scarce'},"answer":'D'},

{"id":165,"subject":'English',"topic":'Grammar',"difficulty":'Easy',
 "question":'Choose the grammatically correct sentence:',
 "options":{"A":'Each of the students has submitted his or her assignment.', "B":'Each of the students have submitted their assignments.', "C":'Each of the student have submitted their assignment.', "D":'Each of the students have submitted his assignment.'},"answer":'A'},

{"id":166,"subject":'English',"topic":'Grammar',"difficulty":'Medium',
 "question":'Choose the correct sentence:',
 "options":{"A":'If I would have known, I would have come earlier.', "B":'If I had known, I would have come earlier.', "C":'If I knew, I would have come earlier.', "D":'If I have known, I would have come earlier.'},"answer":'B'},

{"id":167,"subject":'English',"topic":'Sentence Correction',"difficulty":'Medium',
 "question":'Identify the sentence with correct use of the article:',
 "options":{"A":'She is a honest person.', "B":'She is the honest person.', "C":'She is an honest person.', "D":'She is honest person.'},"answer":'C'},

{"id":168,"subject":'English',"topic":'Vocabulary',"difficulty":'Medium',
 "question":"Choose the word that best completes the sentence: 'The negotiations broke down because the two sides could not reach a ______.'",
 "options":{"A":'contradiction', "B":'confusion', "C":'conflict', "D":'consensus'},"answer":'D'},

{"id":169,"subject":'English',"topic":'Idioms',"difficulty":'Medium',
 "question":"Choose the meaning closest to the idiom 'to bite the bullet':",
 "options":{"A":'To eat something quickly', "B":'To face a difficult or unpleasant situation with courage', "C":'To lose a fight', "D":'To make a foolish decision'},"answer":'B'},

{"id":170,"subject":'English',"topic":'Sentence Correction',"difficulty":'Hard',
 "question":"Choose the option that best corrects the sentence: 'Neither of the two proposals were accepted by the committee.'",
 "options":{"A":'Neither of the two proposal were accepted by the committee.', "B":'Neither of the two proposals was accepted by the committee.', "C":'Neither of the two proposals are accepted by the committee.', "D":'Neither of the two proposals have been accepted by the committee.'},"answer":'B'},

{"id":171,"subject":'English',"topic":'Prepositions',"difficulty":'Hard',
 "question":"Choose the correct preposition to complete the sentence: 'The results of the experiment differ significantly ______ our earlier findings.'",
 "options":{"A":'than', "B":'to', "C":'from', "D":'with'},"answer":'C'},

# ============================================================
# LOGICAL REASONING (9) - id 172-180
# ============================================================

{"id":172,"subject":'Logical Reasoning',"topic":'Number Series',"difficulty":'Easy',
 "question":'Find the next number in the series: 3, 6, 12, 24, ?',
 "options":{"A":'42', "B":'36', "C":'30', "D":'48'},"answer":'D'},

{"id":173,"subject":'Logical Reasoning',"topic":'Number Series',"difficulty":'Easy',
 "question":'Find the missing number: 5, 10, 15, 20, ?',
 "options":{"A":'23', "B":'25', "C":'22', "D":'30'},"answer":'B'},

{"id":174,"subject":'Logical Reasoning',"topic":'Analogies',"difficulty":'Easy',
 "question":'Author is to Book as Composer is to:',
 "options":{"A":'Piano', "B":'Symphony', "C":'Orchestra', "D":'Concert'},"answer":'B'},

{"id":175,"subject":'Logical Reasoning',"topic":'Analogies',"difficulty":'Medium',
 "question":'Fish is to Water as Bird is to:',
 "options":{"A":'Beak', "B":'Feather', "C":'Air', "D":'Nest'},"answer":'C'},

{"id":176,"subject":'Logical Reasoning',"topic":'Blood Relations',"difficulty":'Medium',
 "question":"Pointing at a photograph, Sara said, 'She is the daughter of my grandfather's only son.' How is the girl in the photograph related to Sara?",
 "options":{"A":'Cousin', "B":'Aunt', "C":'Niece', "D":'Sister'},"answer":'D'},

{"id":177,"subject":'Logical Reasoning',"topic":'Coding-Decoding',"difficulty":'Medium',
 "question":'If in a certain code, CAT is written as DBU, how is DOG written in the same code?',
 "options":{"A":'EPH', "B":'DPH', "C":'EPG', "D":'FPH'},"answer":'A'},

{"id":178,"subject":'Logical Reasoning',"topic":'Syllogism',"difficulty":'Hard',
 "question":'All roses are flowers. Some flowers fade quickly. Which conclusion logically follows?',
 "options":{"A":'All roses fade quickly', "B":'None of the given conclusions logically follows', "C":'No roses fade quickly', "D":'Some roses fade quickly'},"answer":'B'},

{"id":179,"subject":'Logical Reasoning',"topic":'Pattern Recognition',"difficulty":'Hard',
 "question":'Find the next term in the series: 1, 4, 9, 16, 25, ?',
 "options":{"A":'35', "B":'30', "C":'36', "D":'49'},"answer":'C'},

{"id":180,"subject":'Logical Reasoning',"topic":'Direction Sense',"difficulty":'Medium',
 "question":'A man walks 5 km north, then turns east and walks 12 km. How far is he from his starting point (straight-line distance)?',
 "options":{"A":'7 km', "B":'60 km', "C":'17 km', "D":'13 km'},"answer":'D'},

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