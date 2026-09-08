"""
MDCAT Mock Test 20
==================
Full-length mock test: 180 MCQs
Weightage: Biology 81 | Chemistry 45 | Physics 36 | English 9 | Logical Reasoning 9
Difficulty mix (approx): 30% Easy / 50% Medium / 20% Hard, distributed throughout.

Includes 5 image/diagram-based questions (2 Biology, 1 Chemistry, 2 Physics).
Each such question has an "image" key giving a relative path to a PNG diagram
that must be viewed alongside the question (images/ subfolder, shipped alongside
this file). Diagrams: a labeled plant cell identifying the central vacuole, a
simplified circulatory pathway identifying the pulmonary artery, a phase diagram
showing the triple point and critical region, a three-resistor parallel circuit,
and a convex-lens ray diagram (object placed at the focal point F).

Each question is a dict:
    id, subject, topic, difficulty, question, [image], options (A-D), answer (correct letter)

Run this file directly to print a summary / sanity-check the paper.
"""

QUESTIONS = [

# ============================================================
# BIOLOGY (81) - id 1-81
# ============================================================

{"id":1,"subject":'Biology',"topic":'Biomolecules',"difficulty":'Easy',
 "question":'Which of the following is a polysaccharide?',
 "options":{"A":'Fructose', "B":'Glycogen', "C":'Glucose', "D":'Sucrose'},"answer":'B'},

{"id":2,"subject":'Biology',"topic":'Biomolecules',"difficulty":'Easy',
 "question":'The basic building blocks of nucleic acids are:',
 "options":{"A":'Amino acids', "B":'Nucleotides', "C":'Monosaccharides', "D":'Fatty acids'},"answer":'B'},

{"id":3,"subject":'Biology',"topic":'Biomolecules',"difficulty":'Medium',
 "question":'The primary structure of a protein refers to:',
 "options":{"A":'Its overall three-dimensional shape', "B":'Interactions between multiple polypeptide subunits', "C":'The linear sequence of amino acids joined by peptide bonds', "D":'Hydrogen bonding patterns forming helices'},"answer":'C'},

{"id":4,"subject":'Biology',"topic":'Biomolecules',"difficulty":'Medium',
 "question":'Unsaturated fatty acids differ from saturated fatty acids in that they contain:',
 "options":{"A":'No carbon atoms', "B":'No hydrogen atoms', "C":'Only single bonds throughout', "D":'One or more carbon-carbon double bonds, causing kinks in the chain'},"answer":'D'},

{"id":5,"subject":'Biology',"topic":'Biomolecules',"difficulty":'Hard',
 "question":'Chaperone proteins assist other proteins mainly by:',
 "options":{"A":'Helping newly synthesized polypeptides fold into their correct three-dimensional shape', "B":'Directly providing energy for translation', "C":'Permanently binding to and inactivating misfolded proteins', "D":'Catalyzing peptide bond hydrolysis exclusively'},"answer":'A'},

{"id":6,"subject":'Biology',"topic":'Enzymes',"difficulty":'Easy',
 "question":'The region of an enzyme where the substrate binds is called the:',
 "options":{"A":'Allosteric site', "B":'Active site', "C":'Coenzyme site', "D":'Zymogen site'},"answer":'B'},

{"id":7,"subject":'Biology',"topic":'Enzymes',"difficulty":'Medium',
 "question":"Lowering the pH far below an enzyme's optimum typically:",
 "options":{"A":'Increases enzyme activity indefinitely', "B":'Has no effect on enzyme structure', "C":'Denatures the enzyme and reduces its activity', "D":'Always doubles the reaction rate'},"answer":'C'},

{"id":8,"subject":'Biology',"topic":'Enzymes',"difficulty":'Medium',
 "question":'A coenzyme differs from an enzyme in that a coenzyme is:',
 "options":{"A":'A protein that catalyzes reactions independently', "B":'The same as a substrate', "C":'Always a metal ion', "D":"A small organic molecule that assists an enzyme's catalytic activity, often derived from a vitamin"},"answer":'D'},

{"id":9,"subject":'Biology',"topic":'Enzymes',"difficulty":'Hard',
 "question":'Feedback inhibition in a metabolic pathway typically occurs when:',
 "options":{"A":'The final product of a pathway binds to and inhibits an earlier enzyme in the same pathway', "B":'The initial substrate activates the final enzyme', "C":'An enzyme is permanently destroyed after one use', "D":'Substrate concentration has no effect on pathway regulation'},"answer":'A'},

{"id":10,"subject":'Biology',"topic":'Cell Biology',"difficulty":'Easy',
 "question":'The organelle that packages and modifies proteins received from the endoplasmic reticulum before shipping them to their destination is the:',
 "options":{"A":'Lysosome', "B":'Golgi apparatus', "C":'Peroxisome', "D":'Vacuole'},"answer":'B'},

{"id":11,"subject":'Biology',"topic":'Cell Biology',"difficulty":'Easy',
 "question":'Smooth endoplasmic reticulum is primarily involved in:',
 "options":{"A":'Protein synthesis', "B":'ATP production', "C":'Lipid synthesis and detoxification of drugs', "D":'Photosynthesis'},"answer":'C'},

{"id":12,"subject":'Biology',"topic":'Cell Biology',"difficulty":'Medium',
 "question":'The diagram shows a plant cell with structures labeled J, K, L, and M (the central vacuole, the cell wall, the chloroplast, and the nucleus). Which labeled structure maintains turgor pressure by storing water and helping keep the cell rigid?',
 "image":'images/q_plant_cell_vacuole_diagram.png',
 "options":{"A":'Structure M (nucleus)', "B":'Structure K (cell wall)', "C":'Structure L (chloroplast)', "D":'Structure J (central vacuole)'},"answer":'D'},

{"id":13,"subject":'Biology',"topic":'Cell Biology',"difficulty":'Medium',
 "question":'Peroxisomes function mainly in cells by:',
 "options":{"A":'Breaking down fatty acids and detoxifying harmful substances using oxidative reactions', "B":'Synthesizing ATP through glycolysis', "C":'Storing genetic material', "D":'Producing ribosomal subunits'},"answer":'A'},

{"id":14,"subject":'Biology',"topic":'Cell Biology',"difficulty":'Hard',
 "question":'A cell that has lost the ability to regulate its cell cycle checkpoints may develop into a:',
 "options":{"A":'Normal, healthy differentiated cell', "B":'Cancerous cell that divides uncontrollably', "C":'Cell incapable of any division', "D":'Cell with no metabolic activity'},"answer":'B'},

{"id":15,"subject":'Biology',"topic":'Cell Membrane & Transport',"difficulty":'Easy',
 "question":'The process by which a cell expels materials to the outside by fusing a vesicle with the plasma membrane is called:',
 "options":{"A":'Endocytosis', "B":'Osmosis', "C":'Exocytosis', "D":'Facilitated diffusion'},"answer":'C'},

{"id":16,"subject":'Biology',"topic":'Cell Membrane & Transport',"difficulty":'Medium',
 "question":'Aquaporins are membrane proteins that primarily function to:',
 "options":{"A":'Actively pump ions across the membrane using ATP', "B":'Transmit electrical signals along neurons', "C":'Digest large macromolecules', "D":'Allow rapid, passive movement of water molecules across the membrane'},"answer":'D'},

{"id":17,"subject":'Biology',"topic":'Cell Membrane & Transport',"difficulty":'Medium',
 "question":'A red blood cell placed in a hypotonic solution will most likely:',
 "options":{"A":'Swell and potentially undergo hemolysis (bursting)', "B":'Shrink due to water loss', "C":'Remain completely unchanged', "D":'Undergo plasmolysis'},"answer":'A'},

{"id":18,"subject":'Biology',"topic":'Cell Membrane & Transport',"difficulty":'Hard',
 "question":'Symport and antiport are both types of:',
 "options":{"A":'Simple diffusion', "B":'Secondary active transport, in which the movement of one substance down its gradient drives the movement of another substance', "C":'Osmosis exclusively', "D":'Passive transport requiring no protein'},"answer":'B'},

{"id":19,"subject":'Biology',"topic":'Cell Membrane & Transport',"difficulty":'Easy',
 "question":'Cholesterol embedded within the phospholipid bilayer of animal cell membranes primarily functions to:',
 "options":{"A":'Increase membrane permeability to all molecules', "B":'Act as the sole component of the membrane', "C":'Help regulate membrane fluidity across a range of temperatures', "D":'Prevent any protein from being embedded in the membrane'},"answer":'C'},

{"id":20,"subject":'Biology',"topic":'Cell Cycle & Division',"difficulty":'Easy',
 "question":'The phase of the cell cycle in which the cell grows and carries out its normal metabolic functions before DNA replication is:',
 "options":{"A":'Mitosis', "B":'S phase', "C":'G2', "D":'G1'},"answer":'D'},

{"id":21,"subject":'Biology',"topic":'Cell Cycle & Division',"difficulty":'Easy',
 "question":'Chromosomes become visible as condensed, duplicated structures during which phase of mitosis?',
 "options":{"A":'Prophase', "B":'Metaphase', "C":'Anaphase', "D":'Telophase'},"answer":'A'},

{"id":22,"subject":'Biology',"topic":'Cell Cycle & Division',"difficulty":'Medium',
 "question":'Independent assortment during meiosis I contributes to genetic variation by:',
 "options":{"A":'Causing identical chromosome distribution to every gamete', "B":'Randomly orienting homologous chromosome pairs at the metaphase plate, so maternal and paternal chromosomes are distributed independently to gametes', "C":'Occurring only in mitosis', "D":'Preventing any chromosome separation'},"answer":'B'},

{"id":23,"subject":'Biology',"topic":'Cell Cycle & Division',"difficulty":'Medium',
 "question":'A diploid organism has 2n = 8. How many chromosomes are present in each cell after meiosis I is complete (prior to meiosis II)?',
 "options":{"A":'8', "B":'16', "C":'4', "D":'2'},"answer":'C'},

{"id":24,"subject":'Biology',"topic":'Cell Cycle & Division',"difficulty":'Hard',
 "question":'Nondisjunction during meiosis, in which homologous chromosomes fail to separate properly, can result in gametes with:',
 "options":{"A":'A normal, balanced chromosome number', "B":'No genetic material at all', "C":'Exactly half the normal DNA content, always', "D":'An abnormal chromosome number, potentially leading to conditions such as trisomy'},"answer":'D'},

{"id":25,"subject":'Biology',"topic":'Cell Cycle & Division',"difficulty":'Medium',
 "question":'Telomeres, located at the ends of chromosomes, function mainly to:',
 "options":{"A":'Protect chromosome ends from degradation and prevent them from fusing with other chromosomes', "B":'Code for essential proteins', "C":'Serve as the site of centromere attachment', "D":'Actively promote cell division'},"answer":'A'},

{"id":26,"subject":'Biology',"topic":'Genetics',"difficulty":'Easy',
 "question":'In pea plants, if round seed shape (R) is dominant over wrinkled (r), a cross of Rr x Rr is expected to produce offspring in what phenotype ratio?',
 "options":{"A":'All round', "B":'3 round : 1 wrinkled', "C":'1 round : 1 wrinkled', "D":'All wrinkled'},"answer":'B'},

{"id":27,"subject":'Biology',"topic":'Genetics',"difficulty":'Medium',
 "question":'A cross between a homozygous dominant individual (AA) and a homozygous recessive individual (aa) produces offspring that are:',
 "options":{"A":'All homozygous dominant', "B":'1:1 dominant to recessive phenotype', "C":'All heterozygous', "D":'All homozygous recessive'},"answer":'C'},

{"id":28,"subject":'Biology',"topic":'Genetics',"difficulty":'Medium',
 "question":'Hemophilia is an X-linked recessive disorder. If a carrier mother (unaffected) and an unaffected father have a son, what is the probability the son will have hemophilia?',
 "options":{"A":'0%', "B":'25%', "C":'100%', "D":'50%'},"answer":'D'},

{"id":29,"subject":'Biology',"topic":'Genetics',"difficulty":'Hard',
 "question":'In a dihybrid cross AaBb x AaBb, what fraction of offspring is expected to show the dominant phenotype for both traits?',
 "options":{"A":'9/16', "B":'3/16', "C":'1/16', "D":'1/4'},"answer":'A'},

{"id":30,"subject":'Biology',"topic":'Genetics',"difficulty":'Medium',
 "question":'A man with blood type A (heterozygous, IAi) and a woman with blood type B (heterozygous, IBi) have children. Which blood types are possible in their offspring?',
 "options":{"A":'Only A and B', "B":'A, B, AB, and O are all possible', "C":'Only AB', "D":'Only O'},"answer":'B'},

{"id":31,"subject":'Biology',"topic":'Genetics',"difficulty":'Hard',
 "question":'A trait that appears only when an individual inherits two recessive alleles, and is more common among children of unaffected carrier parents, follows a pattern of:',
 "options":{"A":'Autosomal dominant inheritance', "B":'Y-linked inheritance', "C":'Autosomal recessive inheritance', "D":'Incomplete dominance'},"answer":'C'},

{"id":32,"subject":'Biology',"topic":'Genetics',"difficulty":'Medium',
 "question":"In four o'clock plants, crossing a red-flowered (RR) plant with a white-flowered (WW) plant produces all pink-flowered (RW) offspring, an intermediate blend of the two parental colors. This is an example of:",
 "options":{"A":'Codominance', "B":'Complete dominance', "C":'Epistasis', "D":'Incomplete dominance'},"answer":'D'},

{"id":33,"subject":'Biology',"topic":'Genetics',"difficulty":'Easy',
 "question":"An organism's complete set of alleles for all its genes is referred to as its:",
 "options":{"A":'Genotype', "B":'Phenotype', "C":'Karyotype', "D":'Proteome'},"answer":'A'},

{"id":34,"subject":'Biology',"topic":'Molecular Biology',"difficulty":'Easy',
 "question":'In RNA, adenine pairs with:',
 "options":{"A":'Thymine', "B":'Uracil', "C":'Cytosine', "D":'Guanine'},"answer":'B'},

{"id":35,"subject":'Biology',"topic":'Molecular Biology',"difficulty":'Easy',
 "question":'The sugar found in DNA is:',
 "options":{"A":'Ribose', "B":'Glucose', "C":'Deoxyribose', "D":'Fructose'},"answer":'C'},

{"id":36,"subject":'Biology',"topic":'Molecular Biology',"difficulty":'Medium',
 "question":'During translation, tRNA molecules deliver amino acids to the ribosome by recognizing:',
 "options":{"A":'The DNA template strand directly', "B":'Nothing in particular; delivery is random', "C":'Only the start codon', "D":'A specific mRNA codon via a complementary anticodon'},"answer":'D'},

{"id":37,"subject":'Biology',"topic":'Molecular Biology',"difficulty":'Medium',
 "question":'A mutation that changes a codon but still codes for the same amino acid (due to the redundancy of the genetic code) is called a:',
 "options":{"A":'Silent mutation', "B":'Nonsense mutation', "C":'Missense mutation', "D":'Frameshift mutation'},"answer":'A'},

{"id":38,"subject":'Biology',"topic":'Molecular Biology',"difficulty":'Medium',
 "question":'The process by which a single primary mRNA transcript can be spliced in different ways to produce multiple distinct protein products is called:',
 "options":{"A":'Reverse transcription', "B":'Alternative splicing', "C":'Semi-conservative replication', "D":'Transcription termination'},"answer":'B'},

{"id":39,"subject":'Biology',"topic":'Molecular Biology',"difficulty":'Hard',
 "question":"Insertion of two nucleotides within a gene's coding sequence would most likely cause:",
 "options":{"A":'No change in the protein at all', "B":'Only a silent mutation', "C":'A frameshift, altering every codon downstream of the insertion', "D":'An increase in protein stability with certainty'},"answer":'C'},

{"id":40,"subject":'Biology',"topic":'Molecular Biology',"difficulty":'Hard',
 "question":'The enzyme primase functions during DNA replication to:',
 "options":{"A":'Unwind the DNA double helix', "B":'Proofread and remove incorrect nucleotides', "C":'Join Okazaki fragments together', "D":'Synthesize a short RNA primer to which DNA polymerase can add nucleotides'},"answer":'D'},

{"id":41,"subject":'Biology',"topic":'Molecular Biology',"difficulty":'Medium',
 "question":'A terminator sequence in a gene functions to:',
 "options":{"A":'Signal the end of transcription, causing RNA polymerase to release the newly made RNA', "B":'Initiate transcription', "C":'Bind ribosomes during translation', "D":'Splice introns from the primary transcript'},"answer":'A'},

{"id":42,"subject":'Biology',"topic":'Molecular Biology',"difficulty":'Easy',
 "question":'Which of the following is the start codon that also codes for methionine in most organisms?',
 "options":{"A":'UAA', "B":'AUG', "C":'UAG', "D":'UGA'},"answer":'B'},

{"id":43,"subject":'Biology',"topic":'Molecular Biology',"difficulty":'Hard',
 "question":'The polymerase chain reaction (PCR) is a laboratory technique used primarily to:',
 "options":{"A":'Sequence an entire genome directly', "B":'Translate mRNA into protein in vitro', "C":'Rapidly amplify a specific segment of DNA into many copies', "D":'Permanently destroy DNA samples'},"answer":'C'},

{"id":44,"subject":'Biology',"topic":'Evolution',"difficulty":'Easy',
 "question":'Which of the following is required for evolution by natural selection to occur in a population?',
 "options":{"A":'Mutations must never occur', "B":'All individuals must be genetically identical', "C":'The environment must never change', "D":'A trait must be heritable and affect reproductive success'},"answer":'D'},

{"id":45,"subject":'Biology',"topic":'Evolution',"difficulty":'Medium',
 "question":'Disruptive selection tends to:',
 "options":{"A":'Favor both phenotypic extremes over the intermediate form, potentially splitting a population into two distinct groups', "B":'Favor the average phenotype', "C":'Have no effect on phenotype distribution', "D":'Only ever produce one extreme phenotype'},"answer":'A'},

{"id":46,"subject":'Biology',"topic":'Evolution',"difficulty":'Medium',
 "question":'Homologous structures, such as the forelimbs of humans, whales, and bats, provide evidence for:',
 "options":{"A":'Convergent evolution from unrelated ancestors', "B":'Common ancestry, with the structures being modified over time for different functions', "C":'No evolutionary relationship at all', "D":'Identical function despite different structure'},"answer":'B'},

{"id":47,"subject":'Biology',"topic":'Evolution',"difficulty":'Hard',
 "question":'In a population at Hardy-Weinberg equilibrium, 9% of individuals show the recessive phenotype. What is the frequency of the dominant allele (p)?',
 "options":{"A":'0.3', "B":'0.09', "C":'0.7', "D":'0.91'},"answer":'C'},

{"id":48,"subject":'Biology',"topic":'Classification & Diversity',"difficulty":'Easy',
 "question":'The rank in taxonomy directly above genus is:',
 "options":{"A":'Class', "B":'Species', "C":'Order', "D":'Family'},"answer":'D'},

{"id":49,"subject":'Biology',"topic":'Classification & Diversity',"difficulty":'Easy',
 "question":'Members of Domains Bacteria and Archaea are characterized by being:',
 "options":{"A":'Prokaryotic, lacking a membrane-bound nucleus', "B":'Eukaryotic and multicellular', "C":'Exclusively photosynthetic', "D":'Always parasitic'},"answer":'A'},

{"id":50,"subject":'Biology',"topic":'Classification & Diversity',"difficulty":'Medium',
 "question":'A defining feature distinguishing kingdom Animalia from kingdom Plantae is that animals are generally:',
 "options":{"A":'Autotrophic and possess cell walls made of cellulose', "B":'Heterotrophic and lack cell walls', "C":'Incapable of movement', "D":'Composed of prokaryotic cells'},"answer":'B'},

{"id":51,"subject":'Biology',"topic":'Classification & Diversity',"difficulty":'Medium',
 "question":'An organism with radial symmetry, stinging cells (cnidocytes), and a simple sac-like body plan most likely belongs to phylum:',
 "options":{"A":'Chordata', "B":'Arthropoda', "C":'Cnidaria', "D":'Mollusca'},"answer":'C'},

{"id":52,"subject":'Biology',"topic":'Classification & Diversity',"difficulty":'Easy',
 "question":'Which taxonomic rank groups together several related orders?',
 "options":{"A":'Species', "B":'Family', "C":'Genus', "D":'Class'},"answer":'D'},

{"id":53,"subject":'Biology',"topic":'Classification & Diversity',"difficulty":'Medium',
 "question":'Class Amphibia is characterized by organisms that typically:',
 "options":{"A":'Undergo metamorphosis, having gilled aquatic larvae and lungs as adults, with moist permeable skin', "B":'Have dry, scaly skin and lay shelled eggs on land only', "C":'Have feathers and are endothermic', "D":'Possess mammary glands'},"answer":'A'},

{"id":54,"subject":'Biology',"topic":'Plant Biology',"difficulty":'Easy',
 "question":'The tissue responsible for transporting sugars produced by photosynthesis from leaves to other parts of the plant is the:',
 "options":{"A":'Xylem', "B":'Phloem', "C":'Epidermis', "D":'Meristem'},"answer":'B'},

{"id":55,"subject":'Biology',"topic":'Plant Biology',"difficulty":'Medium',
 "question":'Stomata, small pores mainly on the underside of leaves, primarily function to:',
 "options":{"A":'Absorb water directly from the soil', "B":'Transport sugars throughout the plant', "C":'Regulate gas exchange (CO2 and O2) and water vapor loss through transpiration', "D":'Anchor the plant in soil'},"answer":'C'},

{"id":56,"subject":'Biology',"topic":'Plant Biology',"difficulty":'Medium',
 "question":"A vine's tendrils coiling around a support structure upon contact is an example of:",
 "options":{"A":'Phototropism', "B":'Hydrotropism', "C":'Gravitropism', "D":'Thigmotropism'},"answer":'D'},

{"id":57,"subject":'Biology',"topic":'Plant Biology',"difficulty":'Hard',
 "question":"Root hairs greatly increase a plant's ability to absorb water and minerals mainly by:",
 "options":{"A":'Increasing the surface area of the root in contact with soil', "B":'Producing chlorophyll for photosynthesis', "C":'Preventing water uptake entirely', "D":"Reducing the root's overall length"},"answer":'A'},

{"id":58,"subject":'Biology',"topic":'Plant Biology',"difficulty":'Medium',
 "question":'Abscisic acid, a plant hormone, primarily promotes:',
 "options":{"A":'Rapid cell elongation and growth', "B":'Seed dormancy and stomatal closure during water stress', "C":'Fruit ripening exclusively', "D":'Stem elongation'},"answer":'B'},

{"id":59,"subject":'Biology',"topic":'Plant Biology',"difficulty":'Easy',
 "question":'The female reproductive structure of a flower, which includes the stigma, style, and ovary, is the:',
 "options":{"A":'Stamen', "B":'Petal', "C":'Pistil (carpel)', "D":'Sepal'},"answer":'C'},

{"id":60,"subject":'Biology',"topic":'Human Physiology - Digestion',"difficulty":'Easy',
 "question":'Bile, which aids in fat digestion, is produced by the:',
 "options":{"A":'Stomach', "B":'Gallbladder', "C":'Pancreas', "D":'Liver'},"answer":'D'},

{"id":61,"subject":'Biology',"topic":'Human Physiology - Digestion',"difficulty":'Medium',
 "question":'Amylase enzymes function to break down:',
 "options":{"A":'Starch (carbohydrates) into simpler sugars', "B":'Proteins', "C":'Lipids', "D":'Nucleic acids exclusively'},"answer":'A'},

{"id":62,"subject":'Biology',"topic":'Human Physiology - Digestion',"difficulty":'Medium',
 "question":"The large intestine's primary function is to:",
 "options":{"A":'Digest proteins using pepsin', "B":'Absorb water and electrolytes from indigestible food matter, forming feces', "C":'Produce bile', "D":'Secrete insulin'},"answer":'B'},

{"id":63,"subject":'Biology',"topic":'Human Physiology - Digestion',"difficulty":'Hard',
 "question":'A blockage of the common bile duct would most directly impair:',
 "options":{"A":'Starch digestion in the mouth', "B":'Protein digestion in the stomach', "C":'The delivery of bile to the small intestine for fat digestion', "D":'Water absorption in the large intestine'},"answer":'C'},

{"id":64,"subject":'Biology',"topic":'Human Physiology - Circulation',"difficulty":'Easy',
 "question":'The blood vessels that carry blood away from the heart are called:',
 "options":{"A":'Veins', "B":'Venules', "C":'Capillaries', "D":'Arteries'},"answer":'D'},

{"id":65,"subject":'Biology',"topic":'Human Physiology - Circulation',"difficulty":'Medium',
 "question":'The diagram shows a simplified circulatory pathway with labeled vessels W, X, Y, and Z (the pulmonary artery carrying deoxygenated blood to the lungs, the pulmonary vein carrying oxygenated blood from the lungs, the vena cava, and the aorta). Which labeled vessel is the only artery in the body that carries deoxygenated blood?',
 "image":'images/q_circulatory_pathway_pulmonary_artery_diagram.png',
 "options":{"A":'Vessel W (pulmonary artery)', "B":'Vessel X (pulmonary vein)', "C":'Vessel Y (vena cava)', "D":'Vessel Z (aorta)'},"answer":'A'},

{"id":66,"subject":'Biology',"topic":'Human Physiology - Circulation',"difficulty":'Medium',
 "question":'White blood cells (leukocytes) primarily function in the body to:',
 "options":{"A":'Transport oxygen throughout the body', "B":'Defend the body against infection and foreign invaders', "C":'Carry nutrients exclusively', "D":'Form blood clots'},"answer":'B'},

{"id":67,"subject":'Biology',"topic":'Human Physiology - Circulation',"difficulty":'Hard',
 "question":'An increase in blood viscosity (thickness), such as from dehydration, would most likely:',
 "options":{"A":'Decrease the resistance to blood flow', "B":'Have no effect on blood pressure', "C":'Increase the resistance to blood flow, making the heart work harder to maintain circulation', "D":'Stop blood flow completely'},"answer":'C'},

{"id":68,"subject":'Biology',"topic":'Human Physiology - Respiration',"difficulty":'Easy',
 "question":'The tube that carries air from the throat toward the lungs, branching into the bronchi, is the:',
 "options":{"A":'Esophagus', "B":'Larynx', "C":'Pharynx', "D":'Trachea'},"answer":'D'},

{"id":69,"subject":'Biology',"topic":'Human Physiology - Respiration',"difficulty":'Medium',
 "question":'During exhalation at rest, the diaphragm:',
 "options":{"A":'Relaxes and moves upward, decreasing thoracic volume and pushing air out', "B":'Contracts and moves downward', "C":'Has no role in the process', "D":'Contracts to pull air in'},"answer":'A'},

{"id":70,"subject":'Biology',"topic":'Human Physiology - Respiration',"difficulty":'Hard',
 "question":'Carbon dioxide is transported in the blood mostly in the form of:',
 "options":{"A":'Dissolved CO2 gas only', "B":'Bicarbonate ions (HCO3-) after reacting with water in red blood cells', "C":'Solid carbon particles', "D":'Bound tightly and permanently to hemoglobin, never released'},"answer":'B'},

{"id":71,"subject":'Biology',"topic":'Human Physiology - Excretion',"difficulty":'Easy',
 "question":'Urine formed by the kidneys is transported to the bladder through the:',
 "options":{"A":'Urethra', "B":'Renal vein', "C":'Ureter', "D":'Renal artery'},"answer":'C'},

{"id":72,"subject":'Biology',"topic":'Human Physiology - Excretion',"difficulty":'Medium',
 "question":'Substances such as excess H+ ions and certain drugs are added to the filtrate from the blood mainly during:',
 "options":{"A":'Filtration at the glomerulus', "B":'Storage in the bladder', "C":'Reabsorption only', "D":'Tubular secretion, occurring along the nephron tubules'},"answer":'D'},

{"id":73,"subject":'Biology',"topic":'Human Physiology - Excretion',"difficulty":'Hard',
 "question":'A person with untreated kidney failure would be expected to accumulate excess:',
 "options":{"A":'Urea and other nitrogenous wastes in the blood', "B":'Oxygen in the blood', "C":'Digestive enzymes', "D":'Red blood cells'},"answer":'A'},

{"id":74,"subject":'Biology',"topic":'Human Physiology - Nervous & Endocrine',"difficulty":'Easy',
 "question":'The long, thin extension of a neuron that transmits electrical impulses away from the cell body is the:',
 "options":{"A":'Dendrite', "B":'Axon', "C":'Cell body', "D":'Nucleus'},"answer":'B'},

{"id":75,"subject":'Biology',"topic":'Human Physiology - Nervous & Endocrine',"difficulty":'Medium',
 "question":'Myelin sheaths surrounding certain axons function mainly to:',
 "options":{"A":'Slow down the speed of nerve impulse transmission', "B":'Produce neurotransmitters', "C":'Increase the speed of nerve impulse transmission via saltatory conduction', "D":'Digest old neurons'},"answer":'C'},

{"id":76,"subject":'Biology',"topic":'Human Physiology - Nervous & Endocrine',"difficulty":'Medium',
 "question":'The adrenal glands secrete adrenaline (epinephrine) mainly in response to stress, which functions to:',
 "options":{"A":'Slow the heart rate and promote digestion', "B":'Have no effect on the body', "C":'Lower blood pressure exclusively', "D":"Prepare the body for a 'fight-or-flight' response by increasing heart rate and blood glucose availability"},"answer":'D'},

{"id":77,"subject":'Biology',"topic":'Human Physiology - Nervous & Endocrine',"difficulty":'Hard',
 "question":'In a classic negative feedback loop regulating blood glucose, high blood glucose levels trigger insulin release, which then:',
 "options":{"A":'Lowers blood glucose levels, which in turn reduces further insulin release', "B":'Further raises blood glucose levels', "C":'Has no effect on subsequent insulin release', "D":'Only affects blood calcium'},"answer":'A'},

{"id":78,"subject":'Biology',"topic":'Human Physiology - Reproduction',"difficulty":'Easy',
 "question":'In females, the site of egg (ovum) production and maturation is the:',
 "options":{"A":'Uterus', "B":'Ovary', "C":'Fallopian tube', "D":'Vagina'},"answer":'B'},

{"id":79,"subject":'Biology',"topic":'Human Physiology - Reproduction',"difficulty":'Medium',
 "question":'Estrogen, secreted mainly by the ovarian follicles, functions to:',
 "options":{"A":'Trigger the release of insulin', "B":'Cause immediate menstruation', "C":'Stimulate development of the uterine lining and secondary sexual characteristics', "D":'Prevent ovulation permanently'},"answer":'C'},

{"id":80,"subject":'Biology',"topic":'Ecology',"difficulty":'Easy',
 "question":'Organisms that obtain energy by consuming other organisms are called:',
 "options":{"A":'Autotrophs', "B":'Decomposers exclusively', "C":'Producers', "D":'Heterotrophs'},"answer":'D'},

{"id":81,"subject":'Biology',"topic":'Ecology',"difficulty":'Medium',
 "question":'In the carbon cycle, the process by which plants remove carbon dioxide from the atmosphere and incorporate it into organic molecules is:',
 "options":{"A":'Photosynthesis', "B":'Respiration', "C":'Combustion', "D":'Decomposition'},"answer":'A'},

# ============================================================
# CHEMISTRY (45) - id 82-126
# ============================================================

{"id":82,"subject":'Chemistry',"topic":'Atomic Structure',"difficulty":'Easy',
 "question":'Protons carry what type of electric charge?',
 "options":{"A":'Negative', "B":'Positive', "C":'Neutral', "D":'Variable'},"answer":'B'},

{"id":83,"subject":'Chemistry',"topic":'Atomic Structure',"difficulty":'Medium',
 "question":'An atom of carbon-14 (atomic number 6) contains how many neutrons?',
 "options":{"A":'6', "B":'14', "C":'8', "D":'20'},"answer":'C'},

{"id":84,"subject":'Chemistry',"topic":'Atomic Structure',"difficulty":'Medium',
 "question":'The electron configuration of a neutral magnesium atom (Z = 12) is:',
 "options":{"A":'1s2 2s2 2p5 3s2', "B":'1s2 2s2 2p6 3s1', "C":'1s2 2s2 2p6 3s2 3p1', "D":'1s2 2s2 2p6 3s2'},"answer":'D'},

{"id":85,"subject":'Chemistry',"topic":'Atomic Structure',"difficulty":'Hard',
 "question":'An ion has 8 protons and 10 electrons. What is its charge?',
 "options":{"A":'-2', "B":'+2', "C":'+8', "D":'-10'},"answer":'A'},

{"id":86,"subject":'Chemistry',"topic":'Atomic Structure',"difficulty":'Easy',
 "question":'The atomic number of an element is defined as the number of:',
 "options":{"A":'Electrons in the outermost shell only', "B":'Protons in the nucleus', "C":'Total nucleons', "D":'Neutrons in the nucleus'},"answer":'B'},

{"id":87,"subject":'Chemistry',"topic":'Periodic Table',"difficulty":'Easy',
 "question":'Elements in the same group of the periodic table generally have similar:',
 "options":{"A":'Atomic mass', "B":'Number of neutrons', "C":'Number of valence electrons', "D":'Number of energy levels'},"answer":'C'},

{"id":88,"subject":'Chemistry',"topic":'Periodic Table',"difficulty":'Medium',
 "question":'Electronegativity generally changes going down a group in that it:',
 "options":{"A":'Increases', "B":'Becomes negative', "C":'Stays exactly constant', "D":"Decreases, as atomic radius increases and the nucleus's pull on bonding electrons weakens"},"answer":'D'},

{"id":89,"subject":'Chemistry',"topic":'Periodic Table',"difficulty":'Medium',
 "question":'An element with a very small atomic radius and high electronegativity, found in the upper right of the periodic table (excluding noble gases), would be expected to:',
 "options":{"A":'Readily gain electrons to form an anion', "B":'Readily lose electrons to form a cation', "C":'Never form any bonds', "D":'Only exist as a neutral atom'},"answer":'A'},

{"id":90,"subject":'Chemistry',"topic":'Chemical Bonding',"difficulty":'Easy',
 "question":'A bond in which electrons are shared unequally due to a difference in electronegativity is called a:',
 "options":{"A":'Nonpolar covalent bond', "B":'Polar covalent bond', "C":'Ionic bond exclusively', "D":'Metallic bond'},"answer":'B'},

{"id":91,"subject":'Chemistry',"topic":'Chemical Bonding',"difficulty":'Medium',
 "question":'According to VSEPR theory, a molecule with two bonding pairs and two lone pairs on the central atom (like H2O) has a molecular geometry of:',
 "options":{"A":'Linear', "B":'Tetrahedral', "C":'Bent (angular)', "D":'Trigonal pyramidal'},"answer":'C'},

{"id":92,"subject":'Chemistry',"topic":'Chemical Bonding',"difficulty":'Medium',
 "question":'Ammonia (NH3) is polar overall mainly because:',
 "options":{"A":'It has a perfectly symmetrical tetrahedral shape', "B":'Nitrogen and hydrogen have identical electronegativities', "C":'It contains no polar bonds', "D":'Its trigonal pyramidal shape prevents the bond dipoles from canceling'},"answer":'D'},

{"id":93,"subject":'Chemistry',"topic":'Chemical Bonding',"difficulty":'Hard',
 "question":'Ionic compounds typically have high melting points mainly because:',
 "options":{"A":'Strong electrostatic attractions exist between oppositely charged ions throughout the crystal lattice', "B":'They are held together by weak Van der Waals forces', "C":'They contain no charged particles', "D":'Their bonds are easily broken at room temperature'},"answer":'A'},

{"id":94,"subject":'Chemistry',"topic":'Chemical Bonding',"difficulty":'Easy',
 "question":"Hydrogen bonding between water molecules is responsible for water's:",
 "options":{"A":'Complete lack of polarity', "B":'Relatively high boiling point compared to similarly sized molecules', "C":'Inability to dissolve ionic compounds', "D":'Low surface tension'},"answer":'B'},

{"id":95,"subject":'Chemistry',"topic":'States of Matter',"difficulty":'Easy',
 "question":'Which state of matter has a fixed shape and a fixed volume?',
 "options":{"A":'Gas', "B":'Liquid', "C":'Solid', "D":'Plasma'},"answer":'C'},

{"id":96,"subject":'Chemistry',"topic":'States of Matter',"difficulty":'Medium',
 "question":'A gas occupies 10 L at a pressure of 1.5 atm. What volume will it occupy at 3.0 atm, assuming constant temperature?',
 "options":{"A":'20 L', "B":'7.5 L', "C":'15 L', "D":'5.0 L'},"answer":'D'},

{"id":97,"subject":'Chemistry',"topic":'States of Matter',"difficulty":'Hard',
 "question":'A gas has a volume of 3 L at 200 K and 4 atm. What volume will it occupy at 400 K and 2 atm?',
 "options":{"A":'12 L', "B":'6 L', "C":'3 L', "D":'24 L'},"answer":'A'},

{"id":98,"subject":'Chemistry',"topic":'Stoichiometry',"difficulty":'Easy',
 "question":'The molar mass of glucose (C6H12O6) is approximately:',
 "options":{"A":'120 g/mol', "B":'180 g/mol', "C":'342 g/mol', "D":'90 g/mol'},"answer":'B'},

{"id":99,"subject":'Chemistry',"topic":'Stoichiometry',"difficulty":'Medium',
 "question":'How many moles of hydrogen atoms are present in 4 moles of NH3?',
 "options":{"A":'4', "B":'8', "C":'12', "D":'16'},"answer":'C'},

{"id":100,"subject":'Chemistry',"topic":'Stoichiometry',"difficulty":'Hard',
 "question":'A 200 mL solution contains 0.4 moles of KOH. What is the molarity of the solution?',
 "options":{"A":'0.5 M', "B":'1.25 M', "C":'0.8 M', "D":'2.0 M'},"answer":'D'},

{"id":101,"subject":'Chemistry',"topic":'Stoichiometry',"difficulty":'Medium',
 "question":'In the reaction CH4 + 2O2 -> CO2 + 2H2O, how many moles of O2 are required to completely react with 6 moles of CH4?',
 "options":{"A":'12', "B":'6', "C":'3', "D":'18'},"answer":'A'},

{"id":102,"subject":'Chemistry',"topic":'Thermochemistry',"difficulty":'Easy',
 "question":'The energy released or absorbed during a chemical reaction at constant pressure is called the:',
 "options":{"A":'Kinetic energy', "B":'Enthalpy change', "C":'Entropy', "D":'Activation energy'},"answer":'B'},

{"id":103,"subject":'Chemistry',"topic":'Thermochemistry',"difficulty":'Medium',
 "question":"If reaction X -> Y absorbs 40 kJ and reaction Y -> Z releases 90 kJ, what is the overall enthalpy change for reaction X -> Z (using Hess's law)?",
 "options":{"A":'+130 kJ', "B":'-130 kJ', "C":'-50 kJ', "D":'+50 kJ'},"answer":'C'},

{"id":104,"subject":'Chemistry',"topic":'Chemical Equilibrium',"difficulty":'Medium',
 "question":'For the reaction 2NO2(g) <-> N2O4(g), decreasing the volume of the container (increasing pressure) shifts the equilibrium toward:',
 "options":{"A":'The reactants (2 moles of gas)', "B":'Complete depletion of the products', "C":'No shift at all', "D":'The products (1 mole of gas), the side with fewer gas moles'},"answer":'D'},

{"id":105,"subject":'Chemistry',"topic":'Chemical Equilibrium',"difficulty":'Hard',
 "question":'If a reactant is continuously removed from a reaction at equilibrium, the equilibrium will shift:',
 "options":{"A":'Toward the products, to help replace the removed reactant', "B":'Toward the reactants only', "C":'Not at all', "D":'To stop the reaction entirely'},"answer":'A'},

{"id":106,"subject":'Chemistry',"topic":'Reaction Kinetics',"difficulty":'Easy',
 "question":'Increasing the surface area of a solid reactant (e.g. by grinding it into powder) generally increases reaction rate mainly because:',
 "options":{"A":'It decreases the number of particle collisions', "B":'It exposes more particles to the other reactant, increasing the frequency of collisions', "C":'It lowers the temperature of the reaction', "D":'It removes the need for activation energy entirely'},"answer":'B'},

{"id":107,"subject":'Chemistry',"topic":'Reaction Kinetics',"difficulty":'Medium',
 "question":'The activation energy of a reaction represents:',
 "options":{"A":'The total energy released by the reaction', "B":'The energy of the products only', "C":'The minimum energy required for reactant particles to successfully collide and react', "D":'A quantity that is always zero for spontaneous reactions'},"answer":'C'},

{"id":108,"subject":'Chemistry',"topic":'Electrochemistry',"difficulty":'Medium',
 "question":'In a galvanic (voltaic) cell, electrons flow through the external circuit from the:',
 "options":{"A":'Cathode to the anode', "B":'Cathode to the salt bridge', "C":'Salt bridge to the anode', "D":'Anode to the cathode'},"answer":'D'},

{"id":109,"subject":'Chemistry',"topic":'Electrochemistry',"difficulty":'Hard',
 "question":'In the reaction 2Al(s) + 3Cu2+(aq) -> 2Al3+(aq) + 3Cu(s), aluminum is:',
 "options":{"A":'Oxidized, losing electrons', "B":'Reduced', "C":'Unchanged', "D":'Acting as a catalyst'},"answer":'A'},

{"id":110,"subject":'Chemistry',"topic":'Acids & Bases',"difficulty":'Easy',
 "question":'A solution with a pH of 7 is considered:',
 "options":{"A":'Strongly acidic', "B":'Neutral', "C":'Strongly basic', "D":'Highly corrosive'},"answer":'B'},

{"id":111,"subject":'Chemistry',"topic":'Acids & Bases',"difficulty":'Medium',
 "question":'According to the Lewis theory, an acid is defined as a substance that:',
 "options":{"A":'Donates a pair of electrons', "B":'Donates a proton only', "C":'Accepts a pair of electrons', "D":'Increases OH- concentration'},"answer":'C'},

{"id":112,"subject":'Chemistry',"topic":'Acids & Bases',"difficulty":'Medium',
 "question":'Titration is a technique used to determine:',
 "options":{"A":'The temperature of a solution', "B":'The boiling point of a solution', "C":'The color of an indicator only', "D":'The unknown concentration of an acid or base by reacting it with a solution of known concentration'},"answer":'D'},

{"id":113,"subject":'Chemistry',"topic":'Acids & Bases',"difficulty":'Hard',
 "question":'A buffer made of carbonic acid and bicarbonate helps maintain blood pH by:',
 "options":{"A":'Neutralizing added acids and bases through interconversion between the two buffer components', "B":'Having no capacity to resist pH changes', "C":'Permanently increasing blood pH regardless of what is added', "D":'Reacting only with strong bases, never acids'},"answer":'A'},

{"id":114,"subject":'Chemistry',"topic":'Organic Chemistry',"difficulty":'Easy',
 "question":'The functional group -NH2 characterizes which class of organic compounds?',
 "options":{"A":'Alcohols', "B":'Amines', "C":'Ketones', "D":'Esters'},"answer":'B'},

{"id":115,"subject":'Chemistry',"topic":'Organic Chemistry',"difficulty":'Medium',
 "question":'Alkynes are characterized by having:',
 "options":{"A":'Only single bonds between carbon atoms', "B":'A benzene ring', "C":'At least one carbon-carbon triple bond', "D":'No carbon-hydrogen bonds'},"answer":'C'},

{"id":116,"subject":'Chemistry',"topic":'Organic Chemistry',"difficulty":'Medium',
 "question":'A primary alcohol has its -OH bearing carbon bonded to how many other carbon atoms?',
 "options":{"A":'Four', "B":'Two', "C":'Three', "D":'Zero or one'},"answer":'D'},

{"id":117,"subject":'Chemistry',"topic":'Organic Chemistry',"difficulty":'Hard',
 "question":'Which factor most favors an SN1 reaction mechanism over SN2?',
 "options":{"A":'A tertiary substrate capable of forming a stable carbocation intermediate', "B":'A primary substrate with an unhindered carbon', "C":'A strong nucleophile in high concentration', "D":'A polar aprotic solvent only'},"answer":'A'},

{"id":118,"subject":'Chemistry',"topic":'Organic Chemistry',"difficulty":'Medium',
 "question":'Polymerization of many small monomer units, such as ethylene forming polyethylene, is an example of:',
 "options":{"A":'Hydrolysis', "B":'Addition polymerization', "C":'Condensation with water release', "D":'Combustion'},"answer":'B'},

{"id":119,"subject":'Chemistry',"topic":'Organic Chemistry',"difficulty":'Easy',
 "question":'An organic compound containing the functional group -O- between two carbon chains, with no carbonyl group, is classified as a(n):',
 "options":{"A":'Ester', "B":'Aldehyde', "C":'Ether', "D":'Amide'},"answer":'C'},

{"id":120,"subject":'Chemistry',"topic":'Inorganic Chemistry',"difficulty":'Medium',
 "question":'Transition metals commonly exhibit multiple oxidation states mainly because:',
 "options":{"A":'They have no d electrons available for bonding', "B":'They lack an electron configuration entirely', "C":'They never form ions', "D":'Their d electrons are close in energy and can be involved in bonding to varying degrees'},"answer":'D'},

{"id":121,"subject":'Chemistry',"topic":'Inorganic Chemistry',"difficulty":'Medium',
 "question":'Halogens (Group 17) are highly reactive nonmetals mainly because they:',
 "options":{"A":'Have a strong tendency to gain one electron to achieve a stable octet', "B":'Readily lose electrons to form cations', "C":'Do not react with metals', "D":'Have a complete valence shell already'},"answer":'A'},

{"id":122,"subject":'Chemistry',"topic":'Inorganic Chemistry',"difficulty":'Hard',
 "question":"In the reaction 2Mg + O2 -> 2MgO, magnesium's oxidation state changes from:",
 "options":{"A":'+2 to 0', "B":'0 to +2 (oxidation)', "C":'0 to -2', "D":'No change occurs'},"answer":'B'},

{"id":123,"subject":'Chemistry',"topic":'Physical Chemistry',"difficulty":'Medium',
 "question":'Osmotic pressure, a colligative property, depends primarily on:',
 "options":{"A":'The identity of the solute particles', "B":'The color of the solution', "C":'The concentration (number) of solute particles dissolved in the solution', "D":"The solvent's boiling point alone"},"answer":'C'},

{"id":124,"subject":'Chemistry',"topic":'Physical Chemistry',"difficulty":'Hard',
 "question":'The graph shows a phase diagram of a pure substance with pressure plotted against temperature, showing the solid, liquid, and gas regions along with the triple point where all three phases coexist in equilibrium. Based on the diagram, at pressures and temperatures above the critical point, the substance exists as a:',
 "image":'images/q_mock20_phase_diagram_triple_point.png',
 "options":{"A":'Solid only', "B":'Distinct liquid and gas phases with a clear boundary', "C":'Plasma', "D":'Supercritical fluid, with no distinct liquid-gas boundary'},"answer":'D'},

{"id":125,"subject":'Chemistry',"topic":'Environmental Chemistry',"difficulty":'Easy',
 "question":'Acid rain is primarily formed when sulfur dioxide and nitrogen oxides react with:',
 "options":{"A":'Atmospheric water vapor to form acidic compounds', "B":'Carbon dioxide exclusively', "C":'Ozone to form harmless products', "D":'Oxygen gas to form water'},"answer":'A'},

{"id":126,"subject":'Chemistry',"topic":'Environmental Chemistry',"difficulty":'Medium',
 "question":'Which of the following would most directly help mitigate ozone layer depletion?',
 "options":{"A":'Increasing the use of chlorofluorocarbons (CFCs)', "B":'Phasing out ozone-depleting substances like CFCs in favor of safer alternatives', "C":'Removing all pollution regulations', "D":'Increasing halon production'},"answer":'B'},

# ============================================================
# PHYSICS (36) - id 127-162
# ============================================================

{"id":127,"subject":'Physics',"topic":'Kinematics',"difficulty":'Easy',
 "question":"A car travels 150 km in 3 hours at constant speed. What is the car's speed?",
 "options":{"A":'30 km/h', "B":'450 km/h', "C":'50 km/h', "D":'0.02 km/h'},"answer":'C'},

{"id":128,"subject":'Physics',"topic":'Kinematics',"difficulty":'Medium',
 "question":'An object accelerates uniformly from 8 m/s to 20 m/s in 4 seconds. What is its acceleration?',
 "options":{"A":'2 m/s^2', "B":'5 m/s^2', "C":'4 m/s^2', "D":'3 m/s^2'},"answer":'D'},

{"id":129,"subject":'Physics',"topic":'Kinematics',"difficulty":'Hard',
 "question":'A ball is thrown straight up and takes 2 seconds to reach its highest point (g = 10 m/s^2, ignoring air resistance). What was its initial upward velocity?',
 "options":{"A":'20 m/s', "B":'10 m/s', "C":'5 m/s', "D":'40 m/s'},"answer":'A'},

{"id":130,"subject":'Physics',"topic":'Dynamics',"difficulty":'Easy',
 "question":"According to Newton's first law, an object in motion will continue moving at constant velocity unless acted upon by a(n):",
 "options":{"A":'Balanced force', "B":'Unbalanced (net) force', "C":'Internal force only', "D":'Frictionless surface'},"answer":'B'},

{"id":131,"subject":'Physics',"topic":'Dynamics',"difficulty":'Medium',
 "question":'A net force of 30 N produces an acceleration of 5 m/s^2 in an object. What is the mass of the object?',
 "options":{"A":'25 kg', "B":'150 kg', "C":'6 kg', "D":'35 kg'},"answer":'C'},

{"id":132,"subject":'Physics',"topic":'Dynamics',"difficulty":'Medium',
 "question":"Momentum is defined as the product of an object's:",
 "options":{"A":'Mass and displacement', "B":'Mass and acceleration', "C":'Force and time', "D":'Mass and velocity'},"answer":'D'},

{"id":133,"subject":'Physics',"topic":'Dynamics',"difficulty":'Hard',
 "question":"A 6 kg object is pushed with a horizontal force of 30 N across a surface with a coefficient of kinetic friction of 0.3 (g = 10 m/s^2). What is the object's acceleration?",
 "options":{"A":'2 m/s^2', "B":'5 m/s^2', "C":'3 m/s^2', "D":'1 m/s^2'},"answer":'A'},

{"id":134,"subject":'Physics',"topic":'Work, Energy & Power',"difficulty":'Easy',
 "question":'The SI unit of work and energy is the:',
 "options":{"A":'Joule', "B":'Newton', "C":'Pascal', "D":'Watt'},"answer":'A'},

{"id":135,"subject":'Physics',"topic":'Work, Energy & Power',"difficulty":'Medium',
 "question":'A 3 kg object is raised to a height of 6 m (g = 10 m/s^2). What is its gravitational potential energy?',
 "options":{"A":'18 J', "B":'30 J', "C":'180 J', "D":'60 J'},"answer":'C'},

{"id":136,"subject":'Physics',"topic":'Work, Energy & Power',"difficulty":'Medium',
 "question":'A 2 kg object moving at 10 m/s has a kinetic energy of:',
 "options":{"A":'20 J', "B":'10 J', "C":'200 J', "D":'100 J'},"answer":'D'},

{"id":137,"subject":'Physics',"topic":'Work, Energy & Power',"difficulty":'Hard',
 "question":'A machine does 5000 J of work in 25 seconds. What is its power output?',
 "options":{"A":'200 W', "B":'125000 W', "C":'20 W', "D":'2000 W'},"answer":'A'},

{"id":138,"subject":'Physics',"topic":'Circular Motion & Gravitation',"difficulty":'Easy',
 "question":'An object undergoing uniform circular motion has a velocity vector that is constantly:',
 "options":{"A":'Increasing in magnitude', "B":'Changing direction, always tangent to the circle', "C":'Pointing toward the center', "D":'Zero at all times'},"answer":'B'},

{"id":139,"subject":'Physics',"topic":'Circular Motion & Gravitation',"difficulty":'Medium',
 "question":'If the mass of one of two objects is doubled while distance remains constant, the gravitational force between them becomes:',
 "options":{"A":'Half the original', "B":'Four times the original', "C":'Twice the original', "D":'Unchanged'},"answer":'C'},

{"id":140,"subject":'Physics',"topic":'Circular Motion & Gravitation',"difficulty":'Hard',
 "question":"An astronaut's weight on the Moon is less than on Earth mainly because the Moon has:",
 "options":{"A":'A larger radius than Earth', "B":'The same mass as Earth', "C":'No gravitational field at all', "D":'A smaller mass than Earth, resulting in weaker surface gravity'},"answer":'D'},

{"id":141,"subject":'Physics',"topic":'Fluid Mechanics',"difficulty":'Easy',
 "question":"The pressure exerted by a fluid at a given depth depends on the fluid's density and the:",
 "options":{"A":'Depth below the surface', "B":'Shape of the container only', "C":'Color of the fluid', "D":'Temperature exclusively'},"answer":'A'},

{"id":142,"subject":'Physics',"topic":'Fluid Mechanics',"difficulty":'Medium',
 "question":"A hydraulic lift uses Pascal's principle to allow a small input force to lift a much larger load mainly because:",
 "options":{"A":'Fluids can create force from nothing', "B":'Pressure is transmitted equally throughout the fluid, and a larger piston area experiences a proportionally larger force', "C":'The load has no weight', "D":'The input force is amplified by friction alone'},"answer":'B'},

{"id":143,"subject":'Physics',"topic":'Fluid Mechanics',"difficulty":'Hard',
 "question":'Two identical objects, one made of a denser material than the other, are submerged in the same fluid. Compared to the less dense object, the denser object experiences:',
 "options":{"A":'A greater buoyant force, because it is denser', "B":'No buoyant force at all', "C":"The same buoyant force, since buoyant force depends on displaced fluid volume, not the object's density", "D":'A buoyant force that always exceeds its weight'},"answer":'C'},

{"id":144,"subject":'Physics',"topic":'Oscillations & Waves',"difficulty":'Easy',
 "question":'The distance between two consecutive crests of a wave is called its:',
 "options":{"A":'Amplitude', "B":'Period', "C":'Frequency', "D":'Wavelength'},"answer":'D'},

{"id":145,"subject":'Physics',"topic":'Oscillations & Waves',"difficulty":'Medium',
 "question":'Increasing the amplitude of a sound wave primarily affects its perceived:',
 "options":{"A":'Loudness (volume)', "B":'Pitch', "C":'Speed of travel', "D":'Wavelength only'},"answer":'A'},

{"id":146,"subject":'Physics',"topic":'Oscillations & Waves',"difficulty":'Medium',
 "question":'A wave travels at 340 m/s and has a wavelength of 0.5 m. What is its frequency?',
 "options":{"A":'0.68 Hz', "B":'680 Hz', "C":'340 Hz', "D":'170 Hz'},"answer":'B'},

{"id":147,"subject":'Physics',"topic":'Oscillations & Waves',"difficulty":'Hard',
 "question":'Standing waves are formed when two waves of the same frequency and amplitude travel:',
 "options":{"A":'At vastly different frequencies', "B":'Perpendicular to each other only', "C":'In opposite directions and interfere, creating fixed nodes and antinodes', "D":'In the same direction only'},"answer":'C'},

{"id":148,"subject":'Physics',"topic":'Thermodynamics',"difficulty":'Easy',
 "question":'Radiation, as a method of heat transfer, occurs through:',
 "options":{"A":'Direct particle contact', "B":'The bulk movement of fluid', "C":'Conduction through solids only', "D":'Electromagnetic waves, which can travel through a vacuum'},"answer":'D'},

{"id":149,"subject":'Physics',"topic":'Thermodynamics',"difficulty":'Medium',
 "question":'An isochoric (constant volume) process involves a gas doing:',
 "options":{"A":'No work on its surroundings, since work requires a volume change', "B":'Maximum work on its surroundings', "C":'Work equal to the heat absorbed', "D":'Negative work always'},"answer":'A'},

{"id":150,"subject":'Physics',"topic":'Thermodynamics',"difficulty":'Hard',
 "question":'A gas releases 500 J of heat while 200 J of work is done on the gas by its surroundings. What is the change in internal energy of the gas?',
 "options":{"A":'700 J', "B":'-300 J', "C":'-700 J', "D":'300 J'},"answer":'B'},

{"id":151,"subject":'Physics',"topic":'Electrostatics',"difficulty":'Easy',
 "question":'An object that has gained extra electrons compared to protons carries a net:',
 "options":{"A":'Positive charge', "B":'Neutral charge', "C":'Negative charge', "D":'Charge that constantly changes'},"answer":'C'},

{"id":152,"subject":'Physics',"topic":'Electrostatics',"difficulty":'Medium',
 "question":'Electric field lines around an isolated positive point charge point:',
 "options":{"A":'Toward the charge', "B":'In no particular direction', "C":'In a circular pattern around the charge', "D":'Radially outward, away from the charge'},"answer":'D'},

{"id":153,"subject":'Physics',"topic":'Current Electricity',"difficulty":'Easy',
 "question":'Electrical resistance is measured in units of:',
 "options":{"A":'Ohms', "B":'Amperes', "C":'Volts', "D":'Watts'},"answer":'A'},

{"id":154,"subject":'Physics',"topic":'Current Electricity',"difficulty":'Medium',
 "question":'The diagram shows a circuit where three identical resistors, each of 6 ohm, are all connected in parallel with each other. What is the total resistance of the circuit?',
 "image":'images/q_circuit_three_parallel_resistors.png',
 "options":{"A":'18 ohm', "B":'2 ohm', "C":'6 ohm', "D":'3 ohm'},"answer":'B'},

{"id":155,"subject":'Physics',"topic":'Current Electricity',"difficulty":'Hard',
 "question":'Three resistors of 2 ohm, 3 ohm, and 5 ohm are connected in series. What is their total resistance?',
 "options":{"A":'5 ohm', "B":'30 ohm', "C":'10 ohm', "D":'0.97 ohm'},"answer":'C'},

{"id":156,"subject":'Physics',"topic":'Current Electricity',"difficulty":'Medium',
 "question":'A 60 W light bulb operates at 120 V. What current does it draw?',
 "options":{"A":'5 A', "B":'2 A', "C":'7200 A', "D":'0.5 A'},"answer":'D'},

{"id":157,"subject":'Physics',"topic":'Electromagnetism',"difficulty":'Medium',
 "question":'A current-carrying wire placed in an external magnetic field experiences a force whose direction can be determined using:',
 "options":{"A":'The right-hand rule (or left-hand rule, depending on convention)', "B":"Ohm's law", "C":"Coulomb's law", "D":'The law of conservation of energy'},"answer":'A'},

{"id":158,"subject":'Physics',"topic":'Electromagnetism',"difficulty":'Hard',
 "question":'A transformer increases voltage from the primary to the secondary coil (a step-up transformer) when the secondary coil has:',
 "options":{"A":'Fewer turns than the primary coil', "B":'More turns than the primary coil', "C":'The exact same number of turns as the primary coil', "D":'No turns at all'},"answer":'B'},

{"id":159,"subject":'Physics',"topic":'Modern Physics',"difficulty":'Easy',
 "question":'The particle with a negative electric charge that orbits the nucleus of an atom is the:',
 "options":{"A":'Proton', "B":'Neutron', "C":'Electron', "D":'Positron'},"answer":'C'},

{"id":160,"subject":'Physics',"topic":'Modern Physics',"difficulty":'Medium',
 "question":'In gamma decay, an excited nucleus emits:',
 "options":{"A":'A helium nucleus', "B":'An electron', "C":'A neutron', "D":'A high-energy photon, with no change in atomic or mass number'},"answer":'D'},

{"id":161,"subject":'Physics',"topic":'Modern Physics',"difficulty":'Hard',
 "question":'A radioactive sample has a half-life of 5 days. Starting with 800 g, approximately how much remains after 20 days?',
 "options":{"A":'50 g', "B":'100 g', "C":'25 g', "D":'200 g'},"answer":'A'},

{"id":162,"subject":'Physics',"topic":'Optics',"difficulty":'Medium',
 "question":'The ray diagram shows a convex lens with an object placed exactly at the focal point (F). Based on the diagram, the image formed is:',
 "image":'images/q_mock20_convex_lens_object_at_f.png',
 "options":{"A":'Real and formed at 2F on the other side', "B":'No clear image is formed, as the refracted rays emerge parallel to each other', "C":'Virtual and located on the same side as the object', "D":'Real, inverted, and diminished, formed very close to the lens'},"answer":'B'},

# ============================================================
# ENGLISH (9) - id 163-171
# ============================================================

{"id":163,"subject":'English',"topic":'Synonyms',"difficulty":'Easy',
 "question":"Choose the word most nearly similar in meaning to 'METICULOUS':",
 "options":{"A":'Impulsive', "B":'Lazy', "C":'Careful and precise', "D":'Careless'},"answer":'C'},

{"id":164,"subject":'English',"topic":'Antonyms',"difficulty":'Easy',
 "question":"Choose the word most nearly opposite in meaning to 'GENEROUS':",
 "options":{"A":'Charitable', "B":'Giving', "C":'Kind', "D":'Stingy'},"answer":'D'},

{"id":165,"subject":'English',"topic":'Grammar',"difficulty":'Easy',
 "question":'Choose the grammatically correct sentence:',
 "options":{"A":'They were going to the market.', "B":'They was going to the market.', "C":'They is going to the market.', "D":'They be going to the market.'},"answer":'A'},

{"id":166,"subject":'English',"topic":'Grammar',"difficulty":'Medium',
 "question":'Choose the correct sentence:',
 "options":{"A":'If I will be you, I would apologize.', "B":'If I were you, I would apologize.', "C":'If I am you, I would apologize.', "D":'If I was you, I would apologize.'},"answer":'B'},

{"id":167,"subject":'English',"topic":'Sentence Correction',"difficulty":'Medium',
 "question":'Choose the sentence that is grammatically correct:',
 "options":{"A":'Everyone of the players have arrived.', "B":'Everyone of the player have arrived.', "C":'Everyone of the players has arrived.', "D":'Everyone of the players were arrived.'},"answer":'C'},

{"id":168,"subject":'English',"topic":'Vocabulary',"difficulty":'Medium',
 "question":"Choose the word that best completes the sentence: 'The committee's decision was ______ and could not be appealed.'",
 "options":{"A":'Tentative', "B":'Uncertain', "C":'Negotiable', "D":'Final'},"answer":'D'},

{"id":169,"subject":'English',"topic":'Idioms',"difficulty":'Medium',
 "question":"Choose the meaning closest to the idiom 'to hit the nail on the head':",
 "options":{"A":'To describe exactly what is causing a situation or problem', "B":'To make a careless mistake', "C":'To avoid a difficult task', "D":'To argue without reason'},"answer":'A'},

{"id":170,"subject":'English',"topic":'Sentence Correction',"difficulty":'Hard',
 "question":"Choose the option that best corrects the sentence: 'Neither of the two options were acceptable to the committee.'",
 "options":{"A":'Neither of the two option were acceptable to the committee.', "B":'Neither of the two options was acceptable to the committee.', "C":'Neither of the two options are acceptable to the committee.', "D":'No correction needed.'},"answer":'B'},

{"id":171,"subject":'English',"topic":'Prepositions',"difficulty":'Hard',
 "question":"Choose the correct preposition: 'The company is known ______ its excellent customer service.'",
 "options":{"A":'with', "B":'at', "C":'for', "D":'about'},"answer":'C'},

# ============================================================
# LOGICAL REASONING (9) - id 172-180
# ============================================================

{"id":172,"subject":'Logical Reasoning',"topic":'Number Series',"difficulty":'Easy',
 "question":'Find the next number in the series: 7, 14, 21, 28, ?',
 "options":{"A":'32', "B":'30', "C":'42', "D":'35'},"answer":'D'},

{"id":173,"subject":'Logical Reasoning',"topic":'Number Series',"difficulty":'Easy',
 "question":'Find the missing number: 1, 4, 9, 16, ?',
 "options":{"A":'25', "B":'24', "C":'20', "D":'36'},"answer":'A'},

{"id":174,"subject":'Logical Reasoning',"topic":'Analogies',"difficulty":'Easy',
 "question":'Pen is to Write as Knife is to:',
 "options":{"A":'Metal', "B":'Cut', "C":'Kitchen', "D":'Sharp'},"answer":'B'},

{"id":175,"subject":'Logical Reasoning',"topic":'Analogies',"difficulty":'Medium',
 "question":'Painter is to Canvas as Sculptor is to:',
 "options":{"A":'Brush', "B":'Gallery', "C":'Marble', "D":'Museum'},"answer":'C'},

{"id":176,"subject":'Logical Reasoning',"topic":'Blood Relations',"difficulty":'Medium',
 "question":"Pointing to a man, a woman said, 'His mother is the only sister of my father.' How is the man related to the woman?",
 "options":{"A":'Brother', "B":'Nephew', "C":'Uncle', "D":'Cousin'},"answer":'D'},

{"id":177,"subject":'Logical Reasoning',"topic":'Coding-Decoding',"difficulty":'Medium',
 "question":'If in a certain code, DOG is written as EPH, how is CAT written in the same code?',
 "options":{"A":'DBU', "B":'DBV', "C":'CBU', "D":'DBS'},"answer":'A'},

{"id":178,"subject":'Logical Reasoning',"topic":'Syllogism',"difficulty":'Hard',
 "question":'All roses are flowers. Some flowers fade quickly. Which conclusion logically follows?',
 "options":{"A":'All flowers are roses', "B":'No valid conclusion about roses fading can be drawn from these statements', "C":'Some flowers are roses', "D":'All roses fade quickly'},"answer":'B'},

{"id":179,"subject":'Logical Reasoning',"topic":'Pattern Recognition',"difficulty":'Hard',
 "question":'Find the next term in the series: 1, 2, 4, 7, 11, ?',
 "options":{"A":'14', "B":'15', "C":'16', "D":'18'},"answer":'C'},

{"id":180,"subject":'Logical Reasoning',"topic":'Direction Sense',"difficulty":'Medium',
 "question":'A man walks 8 km west, then turns south and walks 15 km. How far is he from his starting point?',
 "options":{"A":'23 km', "B":'120 km', "C":'7 km', "D":'17 km'},"answer":'D'},

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