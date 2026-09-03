"""
MDCAT Mock Test 15
===================
Full-length mock test: 180 MCQs
Weightage: Biology 81 | Chemistry 45 | Physics 36 | English 9 | Logical Reasoning 9
Difficulty mix (approx): 30% Easy / 50% Medium / 20% Hard, distributed throughout.

Includes 5 image/diagram-based questions (2 Biology, 1 Chemistry, 2 Physics).
Each such question has an "image" key giving a relative path to a PNG diagram
that must be viewed alongside the question (images/ subfolder, shipped alongside
this file). Diagrams: a labeled diagram of a mitochondrion, a phylogenetic tree
of vertebrates, an energy profile diagram for a catalyzed vs uncatalyzed
reaction, a free-body diagram of a block on an inclined plane, and a diagram
of parallel current-carrying wires with magnetic field lines.

Each question is a dict:
    id, subject, topic, difficulty, question, [image], options (A-D), answer (correct letter)

Run this file directly to print a summary / sanity-check the paper.
"""

QUESTIONS = [

# ============================================================
# BIOLOGY (81) - id 1-81
# ============================================================

{"id":1,"subject":'Biology',"topic":'Biomolecules',"difficulty":'Easy',
 "question":'The building blocks (monomers) of nucleic acids are called:',
 "options":{"A":'Nucleotides', "B":'Amino acids', "C":'Fatty acids', "D":'Monosaccharides'},"answer":'A'},

{"id":2,"subject":'Biology',"topic":'Biomolecules',"difficulty":'Easy',
 "question":'Glycogen is a storage polysaccharide found mainly in:',
 "options":{"A":'Plant leaves', "B":'Animal liver and muscle cells', "C":'Bacterial cell walls', "D":'Fungal spores'},"answer":'B'},

{"id":3,"subject":'Biology',"topic":'Biomolecules',"difficulty":'Medium',
 "question":'Which type of chemical bond stabilizes the alpha-helical secondary structure of proteins?',
 "options":{"A":'Peptide bonds between adjacent helices', "B":'Ionic bonds between distant side chains', "C":'Hydrogen bonds between the backbone C=O and N-H groups four residues apart', "D":'Disulfide bridges between cysteine residues'},"answer":'C'},

{"id":4,"subject":'Biology',"topic":'Biomolecules',"difficulty":'Medium',
 "question":'Triglycerides consist of:',
 "options":{"A":'Three glycerol molecules and one fatty acid', "B":'A steroid ring and three amino acids', "C":'A phosphate group linked to two fatty acids', "D":'One glycerol molecule and three fatty acids joined by ester bonds'},"answer":'D'},

{"id":5,"subject":'Biology',"topic":'Biomolecules',"difficulty":'Hard',
 "question":"The complementary DNA strand for the sequence 5'-ATGCCA-3' is:",
 "options":{"A":"5'-TGGCAT-3'", "B":"5'-TACGGT-3'", "C":"5'-UACGGU-3'", "D":"5'-ATGCCA-3'"},"answer":'A'},

{"id":6,"subject":'Biology',"topic":'Enzymes',"difficulty":'Easy',
 "question":'The "lock and key" model of enzyme action describes:',
 "options":{"A":'The random collision of enzymes with substrates', "B":'The general precise complementary fit between the substrate and the active site', "C":'The requirement of ATP for every enzyme', "D":'The denaturation of enzymes at high pH'},"answer":'B'},

{"id":7,"subject":'Biology',"topic":'Enzymes',"difficulty":'Medium',
 "question":'The graph shows an energy profile diagram for a chemical reaction with and without an enzyme. The enzyme increases the reaction rate by:',
 "image":'images/q15_enzyme_energy_profile.png',
 "options":{"A":'Increasing the enthalpy change of the reaction', "B":'Increasing the temperature of the reactants', "C":'Lowering the activation energy of the reaction', "D":'Changing the overall products formed'},"answer":'C'},

{"id":8,"subject":'Biology',"topic":'Enzymes',"difficulty":'Medium',
 "question":'A cofactor is best described as:',
 "options":{"A":'The substrate molecule of an enzyme reaction', "B":'The product formed by the enzyme', "C":'A protein that inhibits enzyme activity', "D":"A non-protein chemical (often a metal ion or organic molecule) required for an enzyme's activity"},"answer":'D'},

{"id":9,"subject":'Biology',"topic":'Enzymes',"difficulty":'Hard',
 "question":'Feedback inhibition of a metabolic pathway typically occurs when:',
 "options":{"A":'The end-product of the pathway allosterically inhibits an enzyme catalyzing an early step, shutting down the pathway when the product is abundant', "B":'The substrate of the first enzyme is depleted', "C":'The enzyme is destroyed by high temperature', "D":'The pH becomes strongly basic'},"answer":'A'},

{"id":10,"subject":'Biology',"topic":'Cell Biology',"difficulty":'Easy',
 "question":'The diagram shows a mitochondrion. The inner folded membranes labeled X, which greatly increase surface area for the electron transport chain, are called:',
 "image":'images/q15_mitochondrion_labeled.png',
 "options":{"A":'Grana', "B":'Cristae', "C":'Thylakoids', "D":'Ribosomes'},"answer":'B'},

{"id":11,"subject":'Biology',"topic":'Cell Biology',"difficulty":'Easy',
 "question":'The cell wall of a plant cell is primarily composed of:',
 "options":{"A":'Chitin', "B":'Peptidoglycan', "C":'Cellulose', "D":'Phospholipids'},"answer":'C'},

{"id":12,"subject":'Biology',"topic":'Cell Biology',"difficulty":'Medium',
 "question":'Peroxisomes primarily function in the cell to:',
 "options":{"A":'Synthesize proteins for secretion', "B":'Produce ATP through the citric acid cycle', "C":'Store genetic information', "D":'Break down fatty acids and detoxify harmful substances such as hydrogen peroxide'},"answer":'D'},

{"id":13,"subject":'Biology',"topic":'Cell Biology',"difficulty":'Medium',
 "question":'The nucleolus, a dense structure within the nucleus, is primarily the site of:',
 "options":{"A":'Ribosomal RNA (rRNA) synthesis and ribosome subunit assembly', "B":'RNA splicing', "C":'DNA replication', "D":'Protein degradation'},"answer":'A'},

{"id":14,"subject":'Biology',"topic":'Cell Biology',"difficulty":'Medium',
 "question":'Which of the following is a difference between the rough and smooth endoplasmic reticulum?',
 "options":{"A":'Rough ER lacks ribosomes; smooth ER has many ribosomes', "B":'Rough ER has ribosomes attached and is involved in protein synthesis; smooth ER lacks ribosomes and functions in lipid synthesis and detoxification', "C":'Rough ER is found only in plant cells; smooth ER only in animal cells', "D":'Rough ER produces DNA; smooth ER produces RNA'},"answer":'B'},

{"id":15,"subject":'Biology',"topic":'Cell Biology',"difficulty":'Medium',
 "question":'The large central vacuole of a mature plant cell primarily functions in:',
 "options":{"A":'Photosynthesis', "B":'ATP production', "C":'Maintaining cell turgor pressure and storing water, ions, and waste products', "D":'Protein synthesis'},"answer":'C'},

{"id":16,"subject":'Biology',"topic":'Cell Biology',"difficulty":'Hard',
 "question":'A drug that inhibits ATP synthase in mitochondria would most directly affect:',
 "options":{"A":'DNA replication in the nucleus', "B":'The transport of proteins into the Golgi apparatus', "C":'The translation of mRNA on cytosolic ribosomes', "D":'The production of ATP during oxidative phosphorylation'},"answer":'D'},

{"id":17,"subject":'Biology',"topic":'Cell Membrane & Transport',"difficulty":'Easy',
 "question":'Osmosis is best described as the:',
 "options":{"A":'Movement of water across a semipermeable membrane from a region of higher water concentration to lower water concentration', "B":'Movement of solutes across a semipermeable membrane', "C":'Active transport of ions against a concentration gradient', "D":'Endocytosis of large molecules'},"answer":'A'},

{"id":18,"subject":'Biology',"topic":'Cell Membrane & Transport',"difficulty":'Medium',
 "question":'A plant cell placed in a hypertonic solution will undergo:',
 "options":{"A":'Cytolysis, bursting due to water intake', "B":'Plasmolysis, where the protoplast shrinks away from the cell wall due to water loss', "C":'No change in volume', "D":'Active uptake of solutes'},"answer":'B'},

{"id":19,"subject":'Biology',"topic":'Cell Membrane & Transport',"difficulty":'Medium',
 "question":'Which of the following is an example of active transport?',
 "options":{"A":'Diffusion of oxygen into red blood cells', "B":'Osmosis of water across a membrane', "C":'The sodium-potassium pump moving Na+ out and K+ into cells against their gradients', "D":'Simple diffusion of carbon dioxide out of a cell'},"answer":'C'},

{"id":20,"subject":'Biology',"topic":'Cell Membrane & Transport',"difficulty":'Hard',
 "question":'Aquaporins are membrane proteins that specifically:',
 "options":{"A":'Actively pump ions against their gradients', "B":'Break down waste products in the cell', "C":'Transport large proteins by endocytosis', "D":'Form channels that allow rapid passage of water molecules across the plasma membrane'},"answer":'D'},

{"id":21,"subject":'Biology',"topic":'Cell Membrane & Transport',"difficulty":'Easy',
 "question":'Exocytosis is the process by which cells:',
 "options":{"A":'Release materials from vesicles that fuse with the plasma membrane and expel their contents outside the cell', "B":'Take in solid particles via vesicles', "C":'Absorb dissolved solutes through channels', "D":'Divide their cytoplasm during mitosis'},"answer":'A'},

{"id":22,"subject":'Biology',"topic":'Cell Cycle & Division',"difficulty":'Easy',
 "question":'DNA replication occurs during which phase of the cell cycle?',
 "options":{"A":'M phase', "B":'S phase (synthesis phase)', "C":'G2 phase', "D":'G1 phase'},"answer":'B'},

{"id":23,"subject":'Biology',"topic":'Cell Cycle & Division',"difficulty":'Easy',
 "question":'During prophase of mitosis, which of the following events occurs?',
 "options":{"A":'Chromosomes align at the equator of the cell', "B":'Sister chromatids are pulled to opposite poles', "C":'Chromatin condenses into visible chromosomes and the nuclear envelope begins to break down', "D":'Cytokinesis is completed'},"answer":'C'},

{"id":24,"subject":'Biology',"topic":'Cell Cycle & Division',"difficulty":'Medium',
 "question":'A cell undergoing meiosis produces:',
 "options":{"A":'Two genetically identical diploid daughter cells', "B":'Two haploid daughter cells with unchanged chromosomes', "C":'Four identical diploid daughter cells', "D":'Four genetically diverse haploid daughter cells'},"answer":'D'},

{"id":25,"subject":'Biology',"topic":'Cell Cycle & Division',"difficulty":'Medium',
 "question":'In animal cells, cytokinesis is achieved primarily by:',
 "options":{"A":'A cleavage furrow formed by a contractile ring of actin filaments that pinches the cell in two', "B":'The formation of a cell plate in the middle of the cell', "C":'The rupture of the nuclear envelope', "D":'The synthesis of a new cell wall between the daughter cells'},"answer":'A'},

{"id":26,"subject":'Biology',"topic":'Cell Cycle & Division',"difficulty":'Medium',
 "question":'Nondisjunction during meiosis can result in:',
 "options":{"A":'Gametes with the correct chromosome number', "B":'Gametes with an abnormal number of chromosomes, potentially leading to conditions such as Down syndrome (trisomy 21)', "C":'Identical twins in every case', "D":'The complete failure of meiosis to occur'},"answer":'B'},

{"id":27,"subject":'Biology',"topic":'Cell Cycle & Division',"difficulty":'Hard',
 "question":'The protein p53 is often called the "guardian of the genome" because it:',
 "options":{"A":'Directly copies DNA during replication', "B":'Serves as the primary receptor for insulin', "C":'Detects DNA damage and can halt the cell cycle for repair, or trigger apoptosis if damage is too severe', "D":'Forms the spindle fibers during mitosis'},"answer":'C'},

{"id":28,"subject":'Biology',"topic":'Genetics',"difficulty":'Easy',
 "question":'Which of the following describes a phenotype?',
 "options":{"A":'The specific combination of alleles an individual carries for a gene', "B":'The number of chromosomes in a gamete', "C":'The exact DNA sequence of a chromosome', "D":'The observable physical or biochemical characteristics of an organism'},"answer":'D'},

{"id":29,"subject":'Biology',"topic":'Genetics',"difficulty":'Medium',
 "question":'In pea plants, tall (T) is dominant over short (t). What is the probability of obtaining a short offspring from a cross between two heterozygous tall plants (Tt x Tt)?',
 "options":{"A":'25%', "B":'0%', "C":'50%', "D":'75%'},"answer":'A'},

{"id":30,"subject":'Biology',"topic":'Genetics',"difficulty":'Medium',
 "question":'In humans, the sex of a child is determined by:',
 "options":{"A":'The X chromosome contributed by the mother', "B":'The sex chromosome (X or Y) contributed by the father in the sperm', "C":'The number of autosomes present', "D":'Environmental factors during pregnancy'},"answer":'B'},

{"id":31,"subject":'Biology',"topic":'Genetics',"difficulty":'Hard',
 "question":'A woman who is a carrier of hemophilia (X-linked recessive) marries an unaffected man. What is the probability that any given son will be affected with hemophilia?',
 "options":{"A":'0%', "B":'25%', "C":'50%', "D":'100%'},"answer":'C'},

{"id":32,"subject":'Biology',"topic":'Genetics',"difficulty":'Medium',
 "question":'Which of the following blood types is considered the universal donor for red blood cells?',
 "options":{"A":'Type A', "B":'Type B', "C":'Type AB', "D":'Type O negative'},"answer":'D'},

{"id":33,"subject":'Biology',"topic":'Genetics',"difficulty":'Hard',
 "question":'Two genes located far apart on the same chromosome tend to:',
 "options":{"A":'Assort more independently, with recombination frequency approaching that seen for genes on different chromosomes', "B":'Always be inherited together with no recombination', "C":'Undergo no crossing over ever', "D":'Always produce identical offspring'},"answer":'A'},

{"id":34,"subject":'Biology',"topic":'Genetics',"difficulty":'Medium',
 "question":'A pedigree in which an affected trait appears in every generation and is passed from affected parents to roughly half of their children of both sexes most likely represents:',
 "options":{"A":'An autosomal recessive trait', "B":'An autosomal dominant trait', "C":'An X-linked recessive trait', "D":'A mitochondrial trait'},"answer":'B'},

{"id":35,"subject":'Biology',"topic":'Molecular Biology',"difficulty":'Easy',
 "question":'A codon consists of a sequence of how many bases on an mRNA molecule?',
 "options":{"A":'One base', "B":'Two bases', "C":'Three bases', "D":'Four bases'},"answer":'C'},

{"id":36,"subject":'Biology',"topic":'Molecular Biology',"difficulty":'Easy',
 "question":'The process of copying information from DNA into a complementary strand of mRNA is called:',
 "options":{"A":'Translation', "B":'Splicing', "C":'Replication', "D":'Transcription'},"answer":'D'},

{"id":37,"subject":'Biology',"topic":'Molecular Biology',"difficulty":'Medium',
 "question":'The start codon in the standard genetic code, which specifies the amino acid methionine, is:',
 "options":{"A":'AUG', "B":'UAG', "C":'UAA', "D":'GCA'},"answer":'A'},

{"id":38,"subject":'Biology',"topic":'Molecular Biology',"difficulty":'Medium',
 "question":'Which of the following enzymes joins Okazaki fragments together on the lagging strand during DNA replication?',
 "options":{"A":'Helicase', "B":'DNA ligase', "C":'RNA polymerase', "D":'Reverse transcriptase'},"answer":'B'},

{"id":39,"subject":'Biology',"topic":'Molecular Biology',"difficulty":'Medium',
 "question":'A silent mutation is one in which:',
 "options":{"A":'A stop codon is introduced early in the gene', "B":'The entire gene is deleted', "C":'A single base substitution results in a codon that specifies the same amino acid as before, so the protein sequence is unchanged', "D":'A frameshift alters all downstream amino acids'},"answer":'C'},

{"id":40,"subject":'Biology',"topic":'Molecular Biology',"difficulty":'Hard',
 "question":'Reverse transcriptase, an enzyme found in retroviruses such as HIV, catalyzes the synthesis of:',
 "options":{"A":'RNA from a DNA template', "B":'DNA from a protein template', "C":'Protein from an mRNA template', "D":'DNA from an RNA template'},"answer":'D'},

{"id":41,"subject":'Biology',"topic":'Molecular Biology',"difficulty":'Hard',
 "question":'In eukaryotic gene expression, enhancer sequences function to:',
 "options":{"A":'Bind transcription factors and increase the rate of transcription of a target gene, sometimes from a distance', "B":'Terminate transcription at specific sites', "C":'Break down mRNA in the cytoplasm', "D":'Directly code for amino acid sequences'},"answer":'A'},

{"id":42,"subject":'Biology',"topic":'Molecular Biology',"difficulty":'Medium',
 "question":"The 5' cap and poly-A tail added during mRNA processing in eukaryotes primarily function to:",
 "options":{"A":'Provide the coding sequence for the protein', "B":'Protect the mRNA from degradation and aid in ribosome recognition and export from the nucleus', "C":'Splice out introns', "D":'Anneal the mRNA back to DNA'},"answer":'B'},

{"id":43,"subject":'Biology',"topic":'Molecular Biology',"difficulty":'Medium',
 "question":'Which of the following statements about DNA and RNA is correct?',
 "options":{"A":'Both are typically double-stranded and contain deoxyribose', "B":'RNA is stored in the nucleus and DNA is found in the cytoplasm', "C":'DNA contains thymine and deoxyribose, while RNA contains uracil and ribose', "D":'Both contain the same set of nitrogenous bases'},"answer":'C'},

{"id":44,"subject":'Biology',"topic":'Molecular Biology',"difficulty":'Easy',
 "question":'The A site, P site, and E site are functional regions of the:',
 "options":{"A":'Nucleus', "B":'Mitochondrion', "C":'Golgi apparatus', "D":'Ribosome, involved in translation'},"answer":'D'},

{"id":45,"subject":'Biology',"topic":'Evolution',"difficulty":'Easy',
 "question":'Natural selection acts directly on:',
 "options":{"A":'The phenotype of individuals, favoring those best suited to their environment', "B":'The genotype of individuals', "C":'The DNA sequence directly', "D":'Only the environment'},"answer":'A'},

{"id":46,"subject":'Biology',"topic":'Evolution',"difficulty":'Medium',
 "question":'Analogous structures, such as the wings of insects and the wings of birds, arise through:',
 "options":{"A":'Common descent from a recent common ancestor', "B":'Convergent evolution, in which unrelated species evolve similar features in response to similar environmental pressures', "C":'Genetic drift alone', "D":'A shared genetic mutation'},"answer":'B'},

{"id":47,"subject":'Biology',"topic":'Evolution',"difficulty":'Medium',
 "question":'The bottleneck effect describes a form of genetic drift that occurs when:',
 "options":{"A":'A small population expands rapidly', "B":'Two populations interbreed extensively', "C":"A population's size is drastically reduced by a random event, causing a change in allele frequencies that may not represent the original gene pool", "D":'A mutation spreads through a large population'},"answer":'C'},

{"id":48,"subject":'Biology',"topic":'Evolution',"difficulty":'Hard',
 "question":'In a Hardy-Weinberg population, if the frequency of a homozygous recessive genotype (q^2) is 0.04, what is the frequency of the recessive allele (q)?',
 "options":{"A":'0.02', "B":'0.16', "C":'0.4', "D":'0.2'},"answer":'D'},

{"id":49,"subject":'Biology',"topic":'Classification & Diversity',"difficulty":'Easy',
 "question":'The diagram shows a phylogenetic tree of several vertebrate groups. Two species that share the most recent common ancestor are said to be:',
 "image":'images/q15_phylogenetic_tree_vertebrates.png',
 "options":{"A":'The most closely related evolutionarily', "B":'Most distantly related evolutionarily', "C":'Unrelated', "D":'Members of different kingdoms'},"answer":'A'},

{"id":50,"subject":'Biology',"topic":'Classification & Diversity',"difficulty":'Easy',
 "question":'Which of the following is a defining characteristic of mammals?',
 "options":{"A":'Laying of leathery eggs on land only', "B":'Presence of mammary glands and body hair', "C":'Absence of a backbone', "D":'External fertilization in water'},"answer":'B'},

{"id":51,"subject":'Biology',"topic":'Classification & Diversity',"difficulty":'Medium',
 "question":'Bacteria are classified in domain Bacteria; another domain of unicellular prokaryotes that often inhabit extreme environments is:',
 "options":{"A":'Eukarya', "B":'Protista', "C":'Archaea', "D":'Fungi'},"answer":'C'},

{"id":52,"subject":'Biology',"topic":'Classification & Diversity',"difficulty":'Medium',
 "question":'An organism has a body plan featuring a mantle, a muscular foot, and often a calcareous shell. It most likely belongs to phylum:',
 "options":{"A":'Annelida', "B":'Porifera', "C":'Echinodermata', "D":'Mollusca'},"answer":'D'},

{"id":53,"subject":'Biology',"topic":'Classification & Diversity',"difficulty":'Easy',
 "question":'Which of the following taxonomic ranks is the most inclusive?',
 "options":{"A":'Domain', "B":'Family', "C":'Order', "D":'Genus'},"answer":'A'},

{"id":54,"subject":'Biology',"topic":'Classification & Diversity',"difficulty":'Medium',
 "question":'Members of phylum Echinodermata are characterized by having:',
 "options":{"A":'Bilateral symmetry, an exoskeleton, and jointed legs', "B":'A radially symmetrical body plan (as adults), a water vascular system, and a calcareous endoskeleton', "C":'A soft body covered by a mantle', "D":'Segmented body with setae'},"answer":'B'},

{"id":55,"subject":'Biology',"topic":'Plant Biology',"difficulty":'Easy',
 "question":'Phloem tissue in plants is primarily responsible for:',
 "options":{"A":'Transporting water from roots to leaves', "B":'Anchoring the plant to the soil', "C":'Transporting sugars (mainly sucrose) produced in the leaves to other parts of the plant', "D":'Absorbing minerals from the soil'},"answer":'C'},

{"id":56,"subject":'Biology',"topic":'Plant Biology',"difficulty":'Medium',
 "question":'Transpiration is the process by which:',
 "options":{"A":'Water enters the roots by osmosis', "B":'Sugars are transported through the phloem', "C":'Carbon dioxide is fixed into organic molecules', "D":'Water vapor is lost from the aerial parts of the plant, mainly through stomata in the leaves'},"answer":'D'},

{"id":57,"subject":'Biology',"topic":'Plant Biology',"difficulty":'Medium',
 "question":'The main product(s) of the light-dependent reactions of photosynthesis include:',
 "options":{"A":'ATP, NADPH, and oxygen', "B":'Glucose and oxygen only', "C":'Carbon dioxide and water', "D":'Amino acids and DNA'},"answer":'A'},

{"id":58,"subject":'Biology',"topic":'Plant Biology',"difficulty":'Hard',
 "question":'The Calvin cycle uses ATP and NADPH from the light reactions to:',
 "options":{"A":'Split water molecules and release oxygen', "B":'Fix CO2 and produce a three-carbon sugar (G3P), which is used to synthesize glucose and other organic compounds', "C":'Absorb light energy directly', "D":'Break down glucose to release ATP'},"answer":'B'},

{"id":59,"subject":'Biology',"topic":'Plant Biology',"difficulty":'Medium',
 "question":'Gibberellins are plant hormones that primarily promote:',
 "options":{"A":'Stomatal closure during drought', "B":'Fruit ripening only', "C":'Stem elongation, seed germination, and flowering in some plants', "D":'The abscission of leaves'},"answer":'C'},

{"id":60,"subject":'Biology',"topic":'Plant Biology',"difficulty":'Easy',
 "question":'The female reproductive part of a flower, which contains the ovary, style, and stigma, is called the:',
 "options":{"A":'Stamen', "B":'Anther', "C":'Filament', "D":'Carpel (pistil)'},"answer":'D'},

{"id":61,"subject":'Biology',"topic":'Human Physiology - Digestion',"difficulty":'Easy',
 "question":'Hydrochloric acid in the stomach primarily functions to:',
 "options":{"A":'Activate pepsinogen into pepsin and kill many ingested microorganisms', "B":'Neutralize bile', "C":'Digest carbohydrates completely', "D":'Absorb nutrients into the bloodstream'},"answer":'A'},

{"id":62,"subject":'Biology',"topic":'Human Physiology - Digestion',"difficulty":'Medium',
 "question":'The pancreas contributes to digestion by secreting:',
 "options":{"A":'Bile that emulsifies fats', "B":'Digestive enzymes (such as trypsin, lipase, and amylase) and bicarbonate into the small intestine', "C":'Hydrochloric acid into the stomach', "D":'Only insulin, which digests glucose in the small intestine'},"answer":'B'},

{"id":63,"subject":'Biology',"topic":'Human Physiology - Digestion',"difficulty":'Medium',
 "question":'Peristalsis in the digestive system refers to:',
 "options":{"A":'The mixing of food with digestive enzymes only', "B":'The absorption of nutrients into the blood', "C":'Wave-like muscular contractions that propel food along the alimentary canal', "D":'The secretion of hormones by the gut'},"answer":'C'},

{"id":64,"subject":'Biology',"topic":'Human Physiology - Digestion',"difficulty":'Hard',
 "question":'The large intestine (colon) primarily functions to:',
 "options":{"A":'Digest proteins with pepsin', "B":'Produce bile for fat digestion', "C":'Absorb most nutrients from digested food', "D":'Absorb water and electrolytes from the remaining undigested material, forming feces'},"answer":'D'},

{"id":65,"subject":'Biology',"topic":'Human Physiology - Circulation',"difficulty":'Easy',
 "question":'Which of the following blood vessels carries deoxygenated blood from the heart to the lungs?',
 "options":{"A":'Pulmonary artery', "B":'Aorta', "C":'Pulmonary vein', "D":'Superior vena cava'},"answer":'A'},

{"id":66,"subject":'Biology',"topic":'Human Physiology - Circulation',"difficulty":'Medium',
 "question":'Capillaries are well suited for exchange between blood and tissues mainly because they:',
 "options":{"A":'Have thick muscular walls', "B":'Have walls only one cell thick and are numerous, providing a very large surface area for exchange', "C":'Contain valves to prevent backflow', "D":'Only carry oxygenated blood'},"answer":'B'},

{"id":67,"subject":'Biology',"topic":'Human Physiology - Circulation',"difficulty":'Medium',
 "question":'Platelets play a key role in:',
 "options":{"A":'Transporting oxygen', "B":'Fighting infection as part of the immune system', "C":'Blood clotting at sites of vessel injury', "D":'Producing red blood cells in the bone marrow'},"answer":'C'},

{"id":68,"subject":'Biology',"topic":'Human Physiology - Circulation',"difficulty":'Hard',
 "question":'Systolic blood pressure represents:',
 "options":{"A":'The average pressure throughout the entire cardiac cycle', "B":'The pressure in the arteries between heartbeats, when the heart is relaxed', "C":'The pressure inside the atria only', "D":'The pressure in the arteries when the ventricles contract and pump blood out'},"answer":'D'},

{"id":69,"subject":'Biology',"topic":'Human Physiology - Respiration',"difficulty":'Easy',
 "question":'The correct pathway of air during inhalation is:',
 "options":{"A":'Nasal cavity → pharynx → larynx → trachea → bronchi → bronchioles → alveoli', "B":'Alveoli → bronchi → trachea → nasal cavity', "C":'Trachea → larynx → pharynx → nasal cavity → alveoli', "D":'Nasal cavity → trachea → pharynx → bronchi → alveoli'},"answer":'A'},

{"id":70,"subject":'Biology',"topic":'Human Physiology - Respiration',"difficulty":'Medium',
 "question":'Alveoli are ideally suited for gas exchange because they:',
 "options":{"A":'Have thick walls that slow the diffusion of gases', "B":'Are numerous, thin-walled, and surrounded by a dense network of capillaries, providing a very large surface area for diffusion', "C":'Contain many mitochondria that consume oxygen', "D":'Are made of cartilage that keeps them rigid'},"answer":'B'},

{"id":71,"subject":'Biology',"topic":'Human Physiology - Respiration',"difficulty":'Medium',
 "question":'The main respiratory control center that regulates the rate and depth of breathing is located in the:',
 "options":{"A":'Cerebellum', "B":'Frontal lobe of the cerebrum', "C":'Medulla oblongata of the brainstem', "D":'Spinal cord only'},"answer":'C'},

{"id":72,"subject":'Biology',"topic":'Human Physiology - Excretion',"difficulty":'Easy',
 "question":'The main nitrogenous waste product excreted in the urine of humans is:',
 "options":{"A":'Ammonia', "B":'Uric acid', "C":'Creatine', "D":'Urea'},"answer":'D'},

{"id":73,"subject":'Biology',"topic":'Human Physiology - Excretion',"difficulty":'Medium',
 "question":'Tubular reabsorption in the nephron is primarily responsible for:',
 "options":{"A":'Returning useful substances such as water, glucose, and ions from the filtrate back into the blood', "B":'Filtering blood at the glomerulus', "C":'Secreting drugs and excess ions into the filtrate', "D":'Producing erythropoietin'},"answer":'A'},

{"id":74,"subject":'Biology',"topic":'Human Physiology - Excretion',"difficulty":'Hard',
 "question":'Aldosterone, a hormone released by the adrenal cortex, primarily acts on the kidneys to:',
 "options":{"A":'Increase excretion of sodium and reduce blood pressure', "B":'Increase reabsorption of sodium (and thus water) from the filtrate, raising blood volume and pressure', "C":'Increase glucose reabsorption', "D":'Decrease water reabsorption and increase urine volume'},"answer":'B'},

{"id":75,"subject":'Biology',"topic":'Human Physiology - Nervous & Endocrine',"difficulty":'Easy',
 "question":'The central nervous system consists of the:',
 "options":{"A":'Autonomic ganglia', "B":'Cranial nerves and spinal nerves only', "C":'Brain and spinal cord', "D":'Sensory receptors in the skin'},"answer":'C'},

{"id":76,"subject":'Biology',"topic":'Human Physiology - Nervous & Endocrine',"difficulty":'Medium',
 "question":'A reflex arc typically involves the following pathway:',
 "options":{"A":'Motor neuron → sensory neuron → effector → receptor', "B":'Receptor → motor neuron → sensory neuron → interneuron → effector', "C":'Effector → motor neuron → receptor → sensory neuron', "D":'Receptor → sensory neuron → interneuron (in spinal cord) → motor neuron → effector'},"answer":'D'},

{"id":77,"subject":'Biology',"topic":'Human Physiology - Nervous & Endocrine',"difficulty":'Medium',
 "question":'Glucagon, secreted by the alpha cells of the pancreas, primarily acts to:',
 "options":{"A":'Raise blood glucose levels by promoting the breakdown of glycogen in the liver into glucose', "B":'Lower blood glucose by stimulating glucose uptake', "C":'Store glucose as fat in adipose tissue', "D":'Stimulate insulin release from beta cells'},"answer":'A'},

{"id":78,"subject":'Biology',"topic":'Human Physiology - Nervous & Endocrine',"difficulty":'Hard',
 "question":'Myelinated axons conduct nerve impulses faster than unmyelinated axons because:',
 "options":{"A":'Action potentials propagate continuously along the entire axon', "B":'The action potential "jumps" between nodes of Ranvier in a process called saltatory conduction', "C":'Myelin generates additional action potentials', "D":'Myelin increases the diameter of the axon significantly'},"answer":'B'},

{"id":79,"subject":'Biology',"topic":'Human Physiology - Reproduction',"difficulty":'Easy',
 "question":'The main male sex hormone, produced primarily by the testes, is:',
 "options":{"A":'Estrogen', "B":'Progesterone', "C":'Testosterone', "D":'Oxytocin'},"answer":'C'},

{"id":80,"subject":'Biology',"topic":'Human Physiology - Reproduction',"difficulty":'Medium',
 "question":'The placenta primarily functions to:',
 "options":{"A":'Cushion the fetus from mechanical shock', "B":'Trigger the onset of menstruation', "C":'Store milk for the newborn', "D":'Enable exchange of nutrients, gases, and wastes between the mother and the developing fetus, and produce hormones supporting pregnancy'},"answer":'D'},

{"id":81,"subject":'Biology',"topic":'Ecology',"difficulty":'Medium',
 "question":'Secondary succession occurs in an area where:',
 "options":{"A":'A previously established community has been disturbed but soil and some organisms remain, allowing recolonization', "B":'Life has never existed before, such as newly cooled lava', "C":'Only aquatic organisms are found', "D":'A population is at carrying capacity and stable'},"answer":'A'},

# ============================================================
# CHEMISTRY (45) - id 82-126
# ============================================================

{"id":82,"subject":'Chemistry',"topic":'Atomic Structure',"difficulty":'Easy',
 "question":'The atomic number of an element is defined as the number of:',
 "options":{"A":'Electrons in the outermost shell', "B":'Protons in the nucleus', "C":'Neutrons in the nucleus', "D":'Nucleons in the atom'},"answer":'B'},

{"id":83,"subject":'Chemistry',"topic":'Atomic Structure',"difficulty":'Medium',
 "question":'According to the Aufbau principle, electrons occupy orbitals in the order of:',
 "options":{"A":'Decreasing energy, from the highest energy orbitals downward', "B":'A random order determined by nuclear charge', "C":'Increasing energy, from the lowest energy orbitals upward', "D":'The alphabetical order of the orbitals'},"answer":'C'},

{"id":84,"subject":'Chemistry',"topic":'Atomic Structure',"difficulty":'Medium',
 "question":'Two atoms are considered isotopes of the same element if they have:',
 "options":{"A":'The same number of neutrons but different numbers of protons', "B":'The same mass number but different atomic numbers', "C":'Different numbers of protons', "D":'The same atomic number but different mass numbers (different numbers of neutrons)'},"answer":'D'},

{"id":85,"subject":'Chemistry',"topic":'Atomic Structure',"difficulty":'Hard',
 "question":'A neutral chlorine atom (Z = 17) gains one electron. The resulting ion has a charge of:',
 "options":{"A":'-1', "B":'+1', "C":'0', "D":'-2'},"answer":'A'},

{"id":86,"subject":'Chemistry',"topic":'Periodic Table',"difficulty":'Easy',
 "question":'The elements of Group 17 in the periodic table are commonly known as:',
 "options":{"A":'Noble gases', "B":'Halogens', "C":'Alkali metals', "D":'Transition metals'},"answer":'B'},

{"id":87,"subject":'Chemistry',"topic":'Periodic Table',"difficulty":'Medium',
 "question":'Which of the following elements is expected to have the largest atomic radius?',
 "options":{"A":'Fluorine (F)', "B":'Chlorine (Cl)', "C":'Iodine (I)', "D":'Bromine (Br)'},"answer":'C'},

{"id":88,"subject":'Chemistry',"topic":'Periodic Table',"difficulty":'Medium',
 "question":'Electron affinity generally becomes more negative (i.e., more energy is released when a neutral atom gains an electron) as you move:',
 "options":{"A":'Down a group', "B":'Left across a period', "C":'From right to left across the periodic table', "D":'Right across a period (toward the halogens)'},"answer":'D'},

{"id":89,"subject":'Chemistry',"topic":'Chemical Bonding',"difficulty":'Easy',
 "question":'A metallic bond is best described as:',
 "options":{"A":'The attraction between positively charged metal ions and a "sea" of delocalized valence electrons', "B":'The sharing of a specific pair of electrons between two atoms', "C":'The complete transfer of electrons between a metal and a nonmetal', "D":'A weak intermolecular force between neutral molecules'},"answer":'A'},

{"id":90,"subject":'Chemistry',"topic":'Chemical Bonding',"difficulty":'Medium',
 "question":'According to VSEPR theory, a methane molecule (CH4), with four bonding pairs and no lone pairs on the central carbon, has a molecular shape that is:',
 "options":{"A":'Linear', "B":'Tetrahedral', "C":'Trigonal planar', "D":'Bent'},"answer":'B'},

{"id":91,"subject":'Chemistry',"topic":'Chemical Bonding',"difficulty":'Medium',
 "question":'Which of the following molecules is expected to be polar?',
 "options":{"A":'CO2', "B":'CH4', "C":'H2O', "D":'N2'},"answer":'C'},

{"id":92,"subject":'Chemistry',"topic":'Chemical Bonding',"difficulty":'Hard',
 "question":'The unusually high boiling point of water compared to other hydrides of Group 16 elements (such as H2S) is best explained by:',
 "options":{"A":'The very heavy molecular mass of water', "B":'The nonpolar nature of water molecules', "C":'The presence of ionic bonds within water molecules', "D":'Strong hydrogen bonding between water molecules, which requires significant energy to overcome'},"answer":'D'},

{"id":93,"subject":'Chemistry',"topic":'States of Matter',"difficulty":'Easy',
 "question":'Which of the following statements about an ideal gas is correct?',
 "options":{"A":'Ideal gas particles have negligible volume and no intermolecular forces (except during collisions)', "B":'Ideal gas particles exert strong intermolecular attractions on each other', "C":'Ideal gas particles have significant volume compared to the container', "D":'Ideal gases cannot be compressed'},"answer":'A'},

{"id":94,"subject":'Chemistry',"topic":'States of Matter',"difficulty":'Medium',
 "question":"A gas has a pressure of 2.0 atm at 300 K. What will its pressure be at 600 K if the volume is kept constant (Gay-Lussac's Law)?",
 "options":{"A":'1.0 atm', "B":'4.0 atm', "C":'2.0 atm', "D":'6.0 atm'},"answer":'B'},

{"id":95,"subject":'Chemistry',"topic":'States of Matter',"difficulty":'Hard',
 "question":'Real gases deviate most from ideal gas behavior at:',
 "options":{"A":'High temperature and low pressure', "B":'Standard temperature and pressure only', "C":'Low temperature and high pressure, where intermolecular forces and molecular volume become significant', "D":'Any condition equally'},"answer":'C'},

{"id":96,"subject":'Chemistry',"topic":'Stoichiometry',"difficulty":'Easy',
 "question":'The molar mass of oxygen gas (O2) is approximately:',
 "options":{"A":'16 g/mol', "B":'18 g/mol', "C":'44 g/mol', "D":'32 g/mol'},"answer":'D'},

{"id":97,"subject":'Chemistry',"topic":'Stoichiometry',"difficulty":'Medium',
 "question":'How many atoms are present in 0.5 moles of iron (Fe)?',
 "options":{"A":'0.5 x 6.022 x 10^23', "B":'6.022 x 10^23', "C":'2 x 6.022 x 10^23', "D":'55.85 x 6.022 x 10^23'},"answer":'A'},

{"id":98,"subject":'Chemistry',"topic":'Stoichiometry',"difficulty":'Hard',
 "question":'In the reaction 2H2 + O2 -> 2H2O, if 4 moles of H2 react with 3 moles of O2, which is the limiting reactant?',
 "options":{"A":'H2, because there is not enough of it', "B":'H2, because O2 is in excess based on the 2:1 stoichiometry', "C":'O2, because there is not enough of it', "D":'Neither is limiting; they are in perfect ratio'},"answer":'B'},

{"id":99,"subject":'Chemistry',"topic":'Stoichiometry',"difficulty":'Medium',
 "question":'What is the percentage by mass of oxygen in water (H2O)? (H = 1, O = 16)',
 "options":{"A":'11.1%', "B":'50.0%', "C":'88.9%', "D":'16.0%'},"answer":'C'},

{"id":100,"subject":'Chemistry',"topic":'Thermochemistry',"difficulty":'Easy',
 "question":'The heat energy released or absorbed at constant pressure during a chemical reaction is called the:',
 "options":{"A":'Entropy change', "B":'Activation energy', "C":'Free energy change', "D":'Enthalpy change (ΔH)'},"answer":'D'},

{"id":101,"subject":'Chemistry',"topic":'Thermochemistry',"difficulty":'Medium',
 "question":"Hess's law states that the enthalpy change for a reaction is:",
 "options":{"A":'Independent of the pathway and depends only on the initial and final states', "B":'Dependent on the pathway taken from reactants to products', "C":'Always positive for exothermic reactions', "D":'Zero for all reactions'},"answer":'A'},

{"id":102,"subject":'Chemistry',"topic":'Chemical Equilibrium',"difficulty":'Medium',
 "question":'For the equilibrium 2SO2(g) + O2(g) <-> 2SO3(g), which change would shift the equilibrium to the right (toward more SO3)?',
 "options":{"A":'Increasing the volume of the container', "B":'Removing SO3 from the system as it forms', "C":'Adding a catalyst', "D":'Decreasing the concentration of SO2'},"answer":'B'},

{"id":103,"subject":'Chemistry',"topic":'Chemical Equilibrium',"difficulty":'Hard',
 "question":'Adding a catalyst to a chemical reaction at equilibrium will:',
 "options":{"A":'Shift the equilibrium toward the products', "B":'Shift the equilibrium toward the reactants', "C":'Have no effect on the position of the equilibrium but will speed up the attainment of equilibrium', "D":'Change the value of the equilibrium constant Keq'},"answer":'C'},

{"id":104,"subject":'Chemistry',"topic":'Reaction Kinetics',"difficulty":'Easy',
 "question":'The activation energy of a reaction is:',
 "options":{"A":'The energy released by the products', "B":'The energy of activation that catalysts increase', "C":'The total energy of the reactants', "D":'The minimum energy required for reactant molecules to react and form products'},"answer":'D'},

{"id":105,"subject":'Chemistry',"topic":'Reaction Kinetics',"difficulty":'Medium',
 "question":'The rate of a reaction generally increases with concentration of reactants because:',
 "options":{"A":'The frequency of effective collisions between reactant molecules increases', "B":'The activation energy of the reaction decreases', "C":'The temperature of the system rises automatically', "D":'The products are removed faster'},"answer":'A'},

{"id":106,"subject":'Chemistry',"topic":'Electrochemistry',"difficulty":'Medium',
 "question":'In the electrolysis of molten sodium chloride (NaCl), the product formed at the cathode is:',
 "options":{"A":'Chlorine gas', "B":'Sodium metal, formed by reduction of Na+ ions', "C":'Hydrogen gas', "D":'Oxygen gas'},"answer":'B'},

{"id":107,"subject":'Chemistry',"topic":'Electrochemistry',"difficulty":'Hard',
 "question":'Which of the following metals will displace copper (Cu) from a solution of copper sulfate (CuSO4)?',
 "options":{"A":'Silver (Ag), because it is less reactive than copper', "B":'Gold (Au), because it is a noble metal', "C":'Zinc (Zn), because it is more reactive than copper in the reactivity series', "D":'None, because copper cannot be displaced'},"answer":'C'},

{"id":108,"subject":'Chemistry',"topic":'Acids & Bases',"difficulty":'Easy',
 "question":'A solution with a pH of 7 at 25 degrees C is:',
 "options":{"A":'Strongly acidic', "B":'Weakly acidic', "C":'Strongly basic', "D":'Neutral'},"answer":'D'},

{"id":109,"subject":'Chemistry',"topic":'Acids & Bases',"difficulty":'Medium',
 "question":'The pH of a solution with a hydroxide ion concentration [OH-] of 1 x 10^-3 M at 25 degrees C is:',
 "options":{"A":'11', "B":'7', "C":'3', "D":'14'},"answer":'A'},

{"id":110,"subject":'Chemistry',"topic":'Acids & Bases',"difficulty":'Medium',
 "question":'Which of the following pairs would form the best buffer solution?',
 "options":{"A":'HCl and NaCl', "B":'Acetic acid (CH3COOH) and sodium acetate (CH3COONa)', "C":'NaOH and NaCl', "D":'HCl and NaOH'},"answer":'B'},

{"id":111,"subject":'Chemistry',"topic":'Acids & Bases',"difficulty":'Hard',
 "question":'The conjugate acid of ammonia (NH3) is:',
 "options":{"A":'NH2-', "B":'NH3+', "C":'NH4+', "D":'N2H4'},"answer":'C'},

{"id":112,"subject":'Chemistry',"topic":'Organic Chemistry',"difficulty":'Easy',
 "question":'The functional group -OH is characteristic of:',
 "options":{"A":'Carboxylic acids', "B":'Aldehydes', "C":'Ketones', "D":'Alcohols'},"answer":'D'},

{"id":113,"subject":'Chemistry',"topic":'Organic Chemistry',"difficulty":'Medium',
 "question":'Which of the following is an addition reaction?',
 "options":{"A":'C2H4 + Br2 -> C2H4Br2', "B":'CH4 + Cl2 -> CH3Cl + HCl', "C":'CH3COOH + NaOH -> CH3COONa + H2O', "D":'2H2O -> 2H2 + O2'},"answer":'A'},

{"id":114,"subject":'Chemistry',"topic":'Organic Chemistry',"difficulty":'Medium',
 "question":'The IUPAC name of the compound CH3-CH2-CH2-OH is:',
 "options":{"A":'Ethanol', "B":'Propan-1-ol', "C":'Propan-2-ol', "D":'Butan-1-ol'},"answer":'B'},

{"id":115,"subject":'Chemistry',"topic":'Organic Chemistry',"difficulty":'Hard',
 "question":'SN2 reactions (bimolecular nucleophilic substitution) are typically fastest with:',
 "options":{"A":'Tertiary alkyl halides, which have the most substituents around the central carbon', "B":'Aromatic compounds', "C":'Primary alkyl halides, because the central carbon is least sterically hindered', "D":'Alkenes, which have double bonds'},"answer":'C'},

{"id":116,"subject":'Chemistry',"topic":'Organic Chemistry',"difficulty":'Medium',
 "question":'Polymerization of ethylene (C2H4) molecules produces:',
 "options":{"A":'Polystyrene', "B":'Nylon', "C":'Rubber', "D":'Polyethylene, formed by repeated addition of ethylene monomers'},"answer":'D'},

{"id":117,"subject":'Chemistry',"topic":'Organic Chemistry',"difficulty":'Easy',
 "question":'Two compounds with the same molecular and structural formula but different spatial arrangements of atoms are called:',
 "options":{"A":'Stereoisomers', "B":'Structural isomers', "C":'Isotopes', "D":'Allotropes'},"answer":'A'},

{"id":118,"subject":'Chemistry',"topic":'Inorganic Chemistry',"difficulty":'Medium',
 "question":'Which of the following is a property of transition metals?',
 "options":{"A":'They are typically nonmetallic and dull in appearance', "B":'They exhibit variable oxidation states and often form colored compounds', "C":'They have very low melting points, like noble gases', "D":'They never form complexes with ligands'},"answer":'B'},

{"id":119,"subject":'Chemistry',"topic":'Inorganic Chemistry',"difficulty":'Medium',
 "question":'Diamond and graphite are two allotropes of carbon that differ in physical properties because:',
 "options":{"A":'They contain different elements', "B":'Diamond contains carbon and graphite contains silicon', "C":'Their carbon atoms are arranged in different structural patterns (tetrahedral network in diamond; layers of hexagons in graphite)', "D":'They have different atomic numbers'},"answer":'C'},

{"id":120,"subject":'Chemistry',"topic":'Inorganic Chemistry',"difficulty":'Hard',
 "question":'In the reaction Fe2O3 + 3CO -> 2Fe + 3CO2, the substance that is oxidized is:',
 "options":{"A":'Fe2O3', "B":'CO2', "C":'Fe', "D":'CO (carbon monoxide), because its carbon changes from +2 to +4 oxidation state'},"answer":'D'},

{"id":121,"subject":'Chemistry',"topic":'Physical Chemistry',"difficulty":'Medium',
 "question":'The freezing point of a solvent is lowered when a non-volatile solute is dissolved in it. This is known as:',
 "options":{"A":'Freezing point depression, a colligative property', "B":'Boiling point elevation', "C":'Vapor pressure elevation', "D":'Osmotic dilution'},"answer":'A'},

{"id":122,"subject":'Chemistry',"topic":'Physical Chemistry',"difficulty":'Hard',
 "question":'A solution is prepared by dissolving 4 g of NaOH (molar mass 40 g/mol) in enough water to make 500 mL. What is its molarity?',
 "options":{"A":'0.1 M', "B":'0.2 M', "C":'0.4 M', "D":'0.8 M'},"answer":'B'},

{"id":123,"subject":'Chemistry',"topic":'Environmental Chemistry',"difficulty":'Easy',
 "question":'Which of the following is a greenhouse gas contributing to global warming?',
 "options":{"A":'Nitrogen (N2)', "B":'Argon (Ar)', "C":'Carbon dioxide (CO2)', "D":'Neon (Ne)'},"answer":'C'},

{"id":124,"subject":'Chemistry',"topic":'Environmental Chemistry',"difficulty":'Medium',
 "question":'Photochemical smog, common in sunlit urban areas, is primarily formed by reactions involving:',
 "options":{"A":'Molecular nitrogen and helium', "B":'Carbon dioxide and water vapor only', "C":'Only chlorofluorocarbons in the atmosphere', "D":'Nitrogen oxides (NOx) and volatile organic compounds (VOCs) in the presence of sunlight'},"answer":'D'},

{"id":125,"subject":'Chemistry',"topic":'Chemical Bonding',"difficulty":'Easy',
 "question":'Ionic compounds typically have:',
 "options":{"A":'High melting points and conduct electricity when molten or dissolved in water', "B":'Low melting points and are gases at room temperature', "C":'No structural regularity in the solid state', "D":'No electrostatic forces between their ions'},"answer":'A'},

{"id":126,"subject":'Chemistry',"topic":'Atomic Structure',"difficulty":'Easy',
 "question":'Which of the following orbitals has a spherical shape?',
 "options":{"A":'p orbital', "B":'s orbital', "C":'f orbital', "D":'d orbital'},"answer":'B'},

# ============================================================
# PHYSICS (36) - id 127-162
# ============================================================

{"id":127,"subject":'Physics',"topic":'Kinematics',"difficulty":'Easy',
 "question":'Which of the following is a vector quantity?',
 "options":{"A":'Speed', "B":'Mass', "C":'Velocity', "D":'Temperature'},"answer":'C'},

{"id":128,"subject":'Physics',"topic":'Kinematics',"difficulty":'Medium',
 "question":'A stone is dropped from rest from the top of a cliff. Ignoring air resistance and taking g = 10 m/s^2, how far does the stone fall in the first 3 seconds?',
 "options":{"A":'15 m', "B":'30 m', "C":'90 m', "D":'45 m'},"answer":'D'},

{"id":129,"subject":'Physics',"topic":'Kinematics',"difficulty":'Hard',
 "question":'A car accelerates from rest at 3 m/s^2 for 8 seconds. How far does the car travel during this time?',
 "options":{"A":'96 m', "B":'48 m', "C":'24 m', "D":'192 m'},"answer":'A'},

{"id":130,"subject":'Physics',"topic":'Dynamics',"difficulty":'Easy',
 "question":'The tendency of an object to resist changes in its state of motion is called:',
 "options":{"A":'Acceleration', "B":'Inertia', "C":'Momentum', "D":'Friction'},"answer":'B'},

{"id":131,"subject":'Physics',"topic":'Dynamics',"difficulty":'Medium',
 "question":"The free-body diagram shows a block of mass 10 kg resting on a frictionless inclined plane at 30 degrees to the horizontal (g = 10 m/s^2). The component of the block's weight parallel to the incline is:",
 "image":'images/q15_inclined_plane_freebody.png',
 "options":{"A":'100 N', "B":'86.6 N', "C":'50 N', "D":'25 N'},"answer":'C'},

{"id":132,"subject":'Physics',"topic":'Dynamics',"difficulty":'Medium',
 "question":'The impulse experienced by an object is equal to:',
 "options":{"A":'The velocity of the object divided by time', "B":"The change in the object's kinetic energy", "C":'The mass of the object multiplied by its displacement', "D":"The change in the object's momentum"},"answer":'D'},

{"id":133,"subject":'Physics',"topic":'Dynamics',"difficulty":'Hard',
 "question":'A 2 kg ball moving at 6 m/s to the right collides elastically with a stationary 2 kg ball. Immediately after the collision:',
 "options":{"A":'The first ball stops and the second ball moves at 6 m/s to the right', "B":'Both balls move to the right at 3 m/s', "C":'Both balls stop', "D":'The first ball rebounds at 6 m/s to the left'},"answer":'A'},

{"id":134,"subject":'Physics',"topic":'Work, Energy & Power',"difficulty":'Easy',
 "question":'When an object is lifted vertically at constant velocity, the work done on the object by the lifting force is:',
 "options":{"A":'Negative', "B":'Positive and stored as gravitational potential energy', "C":'Zero', "D":'Always converted entirely to kinetic energy'},"answer":'B'},

{"id":135,"subject":'Physics',"topic":'Work, Energy & Power',"difficulty":'Medium',
 "question":'A spring of spring constant k = 200 N/m is compressed by 0.1 m. The elastic potential energy stored in the spring is:',
 "options":{"A":'0.5 J', "B":'2 J', "C":'1 J', "D":'20 J'},"answer":'C'},

{"id":136,"subject":'Physics',"topic":'Work, Energy & Power',"difficulty":'Medium',
 "question":'The principle of conservation of energy states that in an isolated system:',
 "options":{"A":'Energy is created continuously by moving objects', "B":'Total energy is destroyed during collisions', "C":'Kinetic energy always increases with time', "D":'Total energy remains constant; it can be transformed from one form to another but never created or destroyed'},"answer":'D'},

{"id":137,"subject":'Physics',"topic":'Work, Energy & Power',"difficulty":'Hard',
 "question":'A pump lifts 500 kg of water through a height of 20 m in 25 seconds (g = 10 m/s^2). The average power output of the pump is:',
 "options":{"A":'4000 W', "B":'2500 W', "C":'400 W', "D":'10000 W'},"answer":'A'},

{"id":138,"subject":'Physics',"topic":'Circular Motion & Gravitation',"difficulty":'Easy',
 "question":'An object moving in a circle at constant speed:',
 "options":{"A":'Has zero acceleration', "B":'Has an acceleration directed toward the center of the circle', "C":'Has an acceleration directed tangent to the circle', "D":'Has an acceleration directed outward from the center'},"answer":'B'},

{"id":139,"subject":'Physics',"topic":'Circular Motion & Gravitation',"difficulty":'Medium',
 "question":'A car of mass 1000 kg moves in a circular track of radius 50 m at a constant speed of 10 m/s. What is the centripetal force acting on the car?',
 "options":{"A":'200 N', "B":'500 N', "C":'2000 N', "D":'5000 N'},"answer":'C'},

{"id":140,"subject":'Physics',"topic":'Circular Motion & Gravitation',"difficulty":'Hard',
 "question":"Kepler's third law states that for planets orbiting the sun:",
 "options":{"A":'The orbital period is independent of the distance from the sun', "B":'The orbital period is proportional to the mass of the planet', "C":'All planets have the same orbital period', "D":'The square of the orbital period is proportional to the cube of the semi-major axis of the orbit'},"answer":'D'},

{"id":141,"subject":'Physics',"topic":'Fluid Mechanics',"difficulty":'Easy',
 "question":'Which of the following units is commonly used to measure pressure?',
 "options":{"A":'Pascal (Pa)', "B":'Newton (N)', "C":'Joule (J)', "D":'Watt (W)'},"answer":'A'},

{"id":142,"subject":'Physics',"topic":'Fluid Mechanics',"difficulty":'Medium',
 "question":"Pascal's principle states that when pressure is applied to an enclosed fluid, it:",
 "options":{"A":'Only acts in the direction of the applied force', "B":'Is transmitted undiminished throughout the fluid to all points and to the walls of the container', "C":'Is completely absorbed by the container walls', "D":'Decreases with distance from the point of application'},"answer":'B'},

{"id":143,"subject":'Physics',"topic":'Fluid Mechanics',"difficulty":'Hard',
 "question":'A hydraulic press has an input piston of area 2 cm^2 and an output piston of area 100 cm^2. If a force of 50 N is applied to the input piston, the force exerted by the output piston is:',
 "options":{"A":'1 N', "B":'50 N', "C":'2500 N', "D":'500 N'},"answer":'C'},

{"id":144,"subject":'Physics',"topic":'Oscillations & Waves',"difficulty":'Easy',
 "question":'Sound waves are examples of:',
 "options":{"A":'Transverse waves', "B":'Standing waves only', "C":'Electromagnetic waves', "D":'Longitudinal (compression) waves'},"answer":'D'},

{"id":145,"subject":'Physics',"topic":'Oscillations & Waves',"difficulty":'Medium',
 "question":'The amplitude of a wave is a measure of:',
 "options":{"A":"The maximum displacement of a particle from its equilibrium position, related to the wave's energy", "B":'The distance between two consecutive crests', "C":'The number of cycles per second', "D":'The speed of the wave'},"answer":'A'},

{"id":146,"subject":'Physics',"topic":'Oscillations & Waves',"difficulty":'Medium',
 "question":'A stretched string of length 1 m produces a fundamental frequency of 200 Hz. What is the speed of the transverse wave on the string?',
 "options":{"A":'100 m/s', "B":'400 m/s', "C":'200 m/s', "D":'800 m/s'},"answer":'B'},

{"id":147,"subject":'Physics',"topic":'Oscillations & Waves',"difficulty":'Hard',
 "question":'Destructive interference between two waves of equal amplitude occurs when the waves meet:',
 "options":{"A":'In phase, producing a wave of larger amplitude', "B":'At a 90-degree phase difference', "C":'Exactly out of phase (180 degrees), so their displacements cancel and produce a wave of zero amplitude', "D":'Traveling in the same direction with the same frequency'},"answer":'C'},

{"id":148,"subject":'Physics',"topic":'Thermodynamics',"difficulty":'Easy',
 "question":'The transfer of heat through direct contact between materials is called:',
 "options":{"A":'Convection', "B":'Radiation', "C":'Evaporation', "D":'Conduction'},"answer":'D'},

{"id":149,"subject":'Physics',"topic":'Thermodynamics',"difficulty":'Medium',
 "question":'An isothermal process is one that takes place at:',
 "options":{"A":'Constant temperature', "B":'Constant pressure', "C":'Constant volume', "D":'Constant entropy'},"answer":'A'},

{"id":150,"subject":'Physics',"topic":'Thermodynamics',"difficulty":'Hard',
 "question":'The efficiency of an ideal Carnot engine operating between hot reservoir T_h and cold reservoir T_c is given by:',
 "options":{"A":'(T_h + T_c) / T_h', "B":'1 - (T_c / T_h)', "C":'(T_h - T_c) / T_c', "D":'T_c / T_h'},"answer":'B'},

{"id":151,"subject":'Physics',"topic":'Electrostatics',"difficulty":'Easy',
 "question":'Like charges:',
 "options":{"A":'Attract each other', "B":'Have no interaction', "C":'Repel each other', "D":'Combine to form neutral particles'},"answer":'C'},

{"id":152,"subject":'Physics',"topic":'Electrostatics',"difficulty":'Medium',
 "question":'The electric field at a point in space is defined as:',
 "options":{"A":'The voltage per unit length', "B":'The potential energy per unit mass', "C":'The current per unit area', "D":'The force per unit positive test charge placed at that point'},"answer":'D'},

{"id":153,"subject":'Physics',"topic":'Current Electricity',"difficulty":'Easy',
 "question":'The direction of conventional current is defined as:',
 "options":{"A":'The direction of flow of positive charges (opposite to electron flow)', "B":'The direction opposite to the flow of positive charges', "C":'The direction of motion of electrons', "D":'Perpendicular to the flow of electrons'},"answer":'A'},

{"id":154,"subject":'Physics',"topic":'Current Electricity',"difficulty":'Medium',
 "question":'Two resistors of 4 ohm each are connected in series. What is the total resistance of the combination?',
 "options":{"A":'2 ohm', "B":'8 ohm', "C":'6 ohm', "D":'4 ohm'},"answer":'B'},

{"id":155,"subject":'Physics',"topic":'Current Electricity',"difficulty":'Hard',
 "question":'A 12 V battery is connected across a resistor and drives a current of 4 A. The power dissipated in the resistor is:',
 "options":{"A":'3 W', "B":'16 W', "C":'48 W', "D":'144 W'},"answer":'C'},

{"id":156,"subject":'Physics',"topic":'Current Electricity',"difficulty":'Medium',
 "question":"Kirchhoff's current law (junction rule) states that at any junction in a circuit:",
 "options":{"A":'The resistance is always zero', "B":'The sum of voltages around a closed loop is zero', "C":'The current is always constant', "D":'The sum of currents entering the junction equals the sum of currents leaving it'},"answer":'D'},

{"id":157,"subject":'Physics',"topic":'Electromagnetism',"difficulty":'Medium',
 "question":'The diagram shows two parallel wires carrying current in the same direction. According to the right-hand rule for magnetic fields, the two wires will:',
 "image":'images/q15_parallel_wires_magnetic_field.png',
 "options":{"A":'Attract each other', "B":'Repel each other', "C":'Exert no force on each other', "D":'Twist around each other'},"answer":'A'},

{"id":158,"subject":'Physics',"topic":'Electromagnetism',"difficulty":'Hard',
 "question":"Faraday's law of electromagnetic induction states that the induced EMF in a coil is:",
 "options":{"A":'Independent of the number of turns in the coil', "B":'Proportional to the rate of change of magnetic flux through the coil', "C":'Equal to the resistance of the coil', "D":'Directly proportional to the current in the coil'},"answer":'B'},

{"id":159,"subject":'Physics',"topic":'Modern Physics',"difficulty":'Easy',
 "question":'The wave nature of matter (matter waves), such as electrons behaving as waves, is a central concept of:',
 "options":{"A":'Classical Newtonian mechanics', "B":'Thermodynamics', "C":'Quantum mechanics (de Broglie hypothesis)', "D":'Fluid mechanics'},"answer":'C'},

{"id":160,"subject":'Physics',"topic":'Modern Physics',"difficulty":'Medium',
 "question":"In Einstein's special theory of relativity, the mass-energy equivalence is expressed by:",
 "options":{"A":'F = ma', "B":'p = mv', "C":'PV = nRT', "D":'E = mc^2'},"answer":'D'},

{"id":161,"subject":'Physics',"topic":'Modern Physics',"difficulty":'Hard',
 "question":'In nuclear fission, a heavy nucleus (such as uranium-235) splits into:',
 "options":{"A":'Two smaller nuclei along with the release of several neutrons and a large amount of energy', "B":'A single heavier nucleus after absorbing a neutron', "C":'Only alpha particles and gamma rays', "D":'Two identical nuclei with no release of energy'},"answer":'A'},

{"id":162,"subject":'Physics',"topic":'Optics',"difficulty":'Medium',
 "question":'When light passes from air into a denser medium such as glass, the light ray:',
 "options":{"A":'Bends away from the normal to the surface', "B":'Bends toward the normal to the surface, since the speed of light decreases in the denser medium', "C":'Continues without any change in direction', "D":'Is completely absorbed'},"answer":'B'},

# ============================================================
# ENGLISH (9) - id 163-171
# ============================================================

{"id":163,"subject":'English',"topic":'Synonyms',"difficulty":'Easy',
 "question":"Choose the word most nearly similar in meaning to 'CANDID':",
 "options":{"A":'Deceitful', "B":'Reserved', "C":'Frank', "D":'Vague'},"answer":'C'},

{"id":164,"subject":'English',"topic":'Antonyms',"difficulty":'Easy',
 "question":"Choose the word most nearly opposite in meaning to 'TRIVIAL':",
 "options":{"A":'Insignificant', "B":'Petty', "C":'Minor', "D":'Important'},"answer":'D'},

{"id":165,"subject":'English',"topic":'Grammar',"difficulty":'Easy',
 "question":'Choose the grammatically correct sentence:',
 "options":{"A":'The number of applicants has increased significantly.', "B":'The number of applicants have increased significantly.', "C":'The number of applicant have increased significantly.', "D":'The number of applicants are increased significantly.'},"answer":'A'},

{"id":166,"subject":'English',"topic":'Grammar',"difficulty":'Medium',
 "question":'Choose the correct sentence:',
 "options":{"A":'He is one of those students who always works hard.', "B":'He is one of those students who always work hard.', "C":'He is one of those student who always work hard.', "D":'He is one of those students whom always work hard.'},"answer":'B'},

{"id":167,"subject":'English',"topic":'Sentence Correction',"difficulty":'Medium',
 "question":'Identify the sentence with correct use of tense:',
 "options":{"A":'She has visited Paris last summer.', "B":'She had been visiting Paris last summer.', "C":'She visited Paris last summer.', "D":'She is visiting Paris last summer.'},"answer":'C'},

{"id":168,"subject":'English',"topic":'Vocabulary',"difficulty":'Medium',
 "question":"Choose the word that best completes the sentence: 'His arguments were so ______ that even his critics were persuaded.'",
 "options":{"A":'weak', "B":'irrelevant', "C":'confusing', "D":'compelling'},"answer":'D'},

{"id":169,"subject":'English',"topic":'Idioms',"difficulty":'Medium',
 "question":"Choose the meaning closest to the idiom 'once in a blue moon':",
 "options":{"A":'Very rarely', "B":'On a monthly basis', "C":'Very often', "D":'At sunset only'},"answer":'A'},

{"id":170,"subject":'English',"topic":'Sentence Correction',"difficulty":'Hard',
 "question":"Choose the option that best corrects the sentence: 'Between you and I, this plan will never work.'",
 "options":{"A":'Between yourself and me, this plan will never work.', "B":'Between you and me, this plan will never work.', "C":'Between I and you, this plan will never work.', "D":'Among you and I, this plan will never work.'},"answer":'B'},

{"id":171,"subject":'English',"topic":'Prepositions',"difficulty":'Hard',
 "question":"Choose the correct preposition to complete the sentence: 'She has been suffering ______ a severe headache since morning.'",
 "options":{"A":'with', "B":'of', "C":'from', "D":'in'},"answer":'C'},

# ============================================================
# LOGICAL REASONING (9) - id 172-180
# ============================================================

{"id":172,"subject":'Logical Reasoning',"topic":'Number Series',"difficulty":'Easy',
 "question":'Find the next number in the series: 2, 4, 8, 16, ?',
 "options":{"A":'20', "B":'24', "C":'64', "D":'32'},"answer":'D'},

{"id":173,"subject":'Logical Reasoning',"topic":'Number Series',"difficulty":'Easy',
 "question":'Find the missing number: 1, 4, 9, 16, ?, 36',
 "options":{"A":'25', "B":'23', "C":'20', "D":'30'},"answer":'A'},

{"id":174,"subject":'Logical Reasoning',"topic":'Analogies',"difficulty":'Easy',
 "question":'Doctor is to Patient as Lawyer is to:',
 "options":{"A":'Judge', "B":'Client', "C":'Court', "D":'Law'},"answer":'B'},

{"id":175,"subject":'Logical Reasoning',"topic":'Analogies',"difficulty":'Medium',
 "question":'Glove is to Hand as Sock is to:',
 "options":{"A":'Shoe', "B":'Leg', "C":'Foot', "D":'Toe'},"answer":'C'},

{"id":176,"subject":'Logical Reasoning',"topic":'Blood Relations',"difficulty":'Medium',
 "question":"Introducing a man, Salma said, 'His mother is the only daughter of my mother.' How is the man related to Salma?",
 "options":{"A":'Brother', "B":'Uncle', "C":'Cousin', "D":'Son'},"answer":'D'},

{"id":177,"subject":'Logical Reasoning',"topic":'Coding-Decoding',"difficulty":'Medium',
 "question":'If in a certain code, BOOK is written as CPPL, how is DESK written in the same code?',
 "options":{"A":'EFTL', "B":'EDTL', "C":'CFTL', "D":'FETL'},"answer":'A'},

{"id":178,"subject":'Logical Reasoning',"topic":'Syllogism',"difficulty":'Hard',
 "question":'All students in the class passed the exam. Ali is a student in the class. Which conclusion logically follows?',
 "options":{"A":'Ali may or may not have passed the exam', "B":'Ali passed the exam', "C":'Ali failed the exam', "D":'None of the given conclusions logically follows'},"answer":'B'},

{"id":179,"subject":'Logical Reasoning',"topic":'Pattern Recognition',"difficulty":'Hard',
 "question":'Find the next term in the series: 1, 3, 7, 15, 31, ?',
 "options":{"A":'47', "B":'55', "C":'63', "D":'62'},"answer":'C'},

{"id":180,"subject":'Logical Reasoning',"topic":'Direction Sense',"difficulty":'Medium',
 "question":'A boy walks 8 km east, then 6 km north. How far is he from his starting point (straight-line distance)?',
 "options":{"A":'2 km', "B":'48 km', "C":'14 km', "D":'10 km'},"answer":'D'},

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