"""
MDCAT Mock Test 18
==================
Full-length mock test: 180 MCQs
Weightage: Biology 81 | Chemistry 45 | Physics 36 | English 9 | Logical Reasoning 9
Difficulty mix (approx): 30% Easy / 50% Medium / 20% Hard, distributed throughout.

Includes 5 image/diagram-based questions (2 Biology, 1 Chemistry, 2 Physics).
Each such question has an "image" key giving a relative path to a PNG diagram
that must be viewed alongside the question (images/ subfolder, shipped alongside
this file). Diagrams: a labeled mitochondrion cross-section, a labeled nephron
identifying the glomerulus, an acid-base titration curve identifying the
equivalence point, a series-then-parallel resistor circuit, and a convex-lens
ray diagram (object beyond 2F).

Each question is a dict:
    id, subject, topic, difficulty, question, [image], options (A-D), answer (correct letter)

Run this file directly to print a summary / sanity-check the paper.
"""

QUESTIONS = [

# ============================================================
# BIOLOGY (81) - id 1-81
# ============================================================

{"id":1,"subject":'Biology',"topic":'Biomolecules',"difficulty":'Easy',
 "question":'Which of the following is a disaccharide?',
 "options":{"A":'Sucrose', "B":'Glucose', "C":'Ribose', "D":'Glycerol'},"answer":'A'},

{"id":2,"subject":'Biology',"topic":'Biomolecules',"difficulty":'Easy',
 "question":'The building blocks that link together to form proteins are:',
 "options":{"A":'Amino acids', "B":'Fatty acids', "C":'Nucleotides', "D":'Monosaccharides'},"answer":'A'},

{"id":3,"subject":'Biology',"topic":'Biomolecules',"difficulty":'Medium',
 "question":'Secondary protein structure (alpha helices and beta sheets) is stabilized mainly by:',
 "options":{"A":'Disulfide bridges exclusively', "B":'Ionic bonds between side chains only', "C":'Hydrogen bonds between backbone atoms of the polypeptide', "D":'Hydrophobic interactions between distant amino acids'},"answer":'C'},

{"id":4,"subject":'Biology',"topic":'Biomolecules',"difficulty":'Medium',
 "question":'Triglycerides function primarily in the body as:',
 "options":{"A":'Genetic material', "B":'Structural components of ribosomes', "C":'Enzymes', "D":'Long-term energy storage molecules'},"answer":'D'},

{"id":5,"subject":'Biology',"topic":'Biomolecules',"difficulty":'Hard',
 "question":'Denaturation of a protein disrupts its function primarily because it:',
 "options":{"A":'Disrupts the higher-order folding and shape without necessarily breaking peptide bonds', "B":'Breaks peptide bonds in the primary structure', "C":'Converts the protein into a carbohydrate', "D":"Has no effect on the protein's three-dimensional shape"},"answer":'A'},

{"id":6,"subject":'Biology',"topic":'Enzymes',"difficulty":'Easy',
 "question":'Enzymes are best described as:',
 "options":{"A":'Biological catalysts that speed up reactions without being consumed', "B":'Substrates that are consumed in reactions', "C":'Products formed only during respiration', "D":'Structural proteins with no catalytic role'},"answer":'A'},

{"id":7,"subject":'Biology',"topic":'Enzymes',"difficulty":'Medium',
 "question":'Competitive inhibitors reduce enzyme activity by:',
 "options":{"A":'Binding an allosteric site far from the active site', "B":"Permanently destroying the enzyme's structure", "C":'Binding the active site, resembling the substrate, and physically blocking it', "D":'Increasing the effective enzyme concentration'},"answer":'C'},

{"id":8,"subject":'Biology',"topic":'Enzymes',"difficulty":'Medium',
 "question":"At temperatures well above an enzyme's optimum, enzyme activity typically:",
 "options":{"A":'Increases indefinitely with temperature', "B":'Doubles with every one-degree rise', "C":'Stays exactly constant', "D":'Decreases sharply because the enzyme denatures'},"answer":'D'},

{"id":9,"subject":'Biology',"topic":'Enzymes',"difficulty":'Hard',
 "question":'A non-competitive inhibitor decreases enzyme activity by:',
 "options":{"A":'Binding a site other than the active site, altering enzyme shape so it can no longer bind substrate effectively', "B":'Competing directly with substrate at the active site', "C":"Increasing the enzyme's affinity for its substrate", "D":'Only affecting enzymes that lack cofactors'},"answer":'A'},

{"id":10,"subject":'Biology',"topic":'Cell Biology',"difficulty":'Easy',
 "question":'Ribosomes are the cellular site of:',
 "options":{"A":'Lipid digestion', "B":'Protein synthesis', "C":'DNA replication', "D":'ATP breakdown exclusively'},"answer":'B'},

{"id":11,"subject":'Biology',"topic":'Cell Biology',"difficulty":'Easy',
 "question":'The Golgi apparatus mainly functions to:',
 "options":{"A":'Store genetic material', "B":'Produce ATP through respiration', "C":'Modify, sort, and package proteins for secretion or delivery', "D":'Carry out photosynthesis'},"answer":'C'},

{"id":12,"subject":'Biology',"topic":'Cell Biology',"difficulty":'Medium',
 "question":'The diagram shows a cross-section of a mitochondrion with structures labeled W, X, Y, and Z (the outer membrane, the folded inner membrane forming cristae, the matrix, and the intermembrane space). Which labeled structure is folded into cristae to increase surface area for ATP synthesis?',
 "image":'images/q_mitochondrion_crosssection_diagram.png',
 "options":{"A":'Structure W (outer membrane)', "B":'Structure Z (intermembrane space)', "C":'Structure Y (matrix)', "D":'Structure X (inner membrane / cristae)'},"answer":'D'},

{"id":13,"subject":'Biology',"topic":'Cell Biology',"difficulty":'Medium',
 "question":'Centrioles in animal cells are primarily associated with:',
 "options":{"A":'Organizing spindle fibers during cell division', "B":'Carrying out photosynthesis', "C":'Producing ribosomal RNA', "D":'Storing lipid droplets'},"answer":'A'},

{"id":14,"subject":'Biology',"topic":'Cell Biology',"difficulty":'Medium',
 "question":'Pores in the nuclear envelope function to:',
 "options":{"A":'Prevent all molecules from entering or leaving the nucleus', "B":'Regulate the passage of molecules such as RNA and proteins between the nucleus and cytoplasm', "C":'Allow only water molecules through', "D":'Serve no functional role'},"answer":'B'},

{"id":15,"subject":'Biology',"topic":'Cell Biology',"difficulty":'Hard',
 "question":'A cell containing an unusually large number of mitochondria is most likely:',
 "options":{"A":'A skin cell with low energy demands', "B":'A mature red blood cell', "C":'A muscle or liver cell with high energy demands', "D":'A cell that does not carry out respiration'},"answer":'C'},

{"id":16,"subject":'Biology',"topic":'Cell Membrane & Transport',"difficulty":'Easy',
 "question":'Osmosis refers specifically to the diffusion of:',
 "options":{"A":'Gases only', "B":'Proteins across a membrane', "C":'Ions against their concentration gradient', "D":'Water across a selectively permeable membrane'},"answer":'D'},

{"id":17,"subject":'Biology',"topic":'Cell Membrane & Transport',"difficulty":'Medium',
 "question":'Active transport differs from passive transport mainly in that it:',
 "options":{"A":'Requires ATP to move substances against their concentration gradient', "B":'Never requires a carrier protein', "C":'Always moves substances down their concentration gradient', "D":'Occurs only in plant cells'},"answer":'A'},

{"id":18,"subject":'Biology',"topic":'Cell Membrane & Transport',"difficulty":'Medium',
 "question":'A plant cell placed in a hypertonic solution will most likely undergo:',
 "options":{"A":'An increase in turgor pressure', "B":'Plasmolysis, as the cell membrane pulls away from the cell wall', "C":'Bursting of the cell', "D":'No change whatsoever'},"answer":'B'},

{"id":19,"subject":'Biology',"topic":'Cell Membrane & Transport',"difficulty":'Hard',
 "question":'During each cycle, the sodium-potassium pump uses ATP to move:',
 "options":{"A":'Equal numbers of Na+ and K+ in the same direction', "B":'2 Na+ out of the cell and 3 K+ into the cell', "C":'3 Na+ out of the cell and 2 K+ into the cell', "D":'Only Na+ ions, with no K+ movement'},"answer":'C'},

{"id":20,"subject":'Biology',"topic":'Cell Membrane & Transport',"difficulty":'Easy',
 "question":'Which transport process requires a carrier protein but no ATP?',
 "options":{"A":'Endocytosis', "B":'Active transport', "C":'Exocytosis', "D":'Facilitated diffusion'},"answer":'D'},

{"id":21,"subject":'Biology',"topic":'Cell Cycle & Division',"difficulty":'Easy',
 "question":'Interphase includes which of the following sub-phases?',
 "options":{"A":'G1, S, and G2', "B":'Only mitosis', "C":'Only cytokinesis', "D":'Prophase and metaphase only'},"answer":'A'},

{"id":22,"subject":'Biology',"topic":'Cell Cycle & Division',"difficulty":'Easy',
 "question":'Sister chromatids separate and move toward opposite poles during:',
 "options":{"A":'Prophase', "B":'Anaphase', "C":'Metaphase', "D":'Interphase'},"answer":'B'},

{"id":23,"subject":'Biology',"topic":'Cell Cycle & Division',"difficulty":'Medium',
 "question":'Compared to mitosis, meiosis produces:',
 "options":{"A":'Two diploid daughter cells identical to the parent', "B":'One diploid and one haploid cell', "C":'Four genetically distinct haploid daughter cells', "D":'No new cells at all'},"answer":'C'},

{"id":24,"subject":'Biology',"topic":'Cell Cycle & Division',"difficulty":'Medium',
 "question":'A diploid organism has 2n = 24. How many chromosomes are present in each gamete produced by meiosis?',
 "options":{"A":'24', "B":'6', "C":'48', "D":'12'},"answer":'D'},

{"id":25,"subject":'Biology',"topic":'Cell Cycle & Division',"difficulty":'Hard',
 "question":'The spindle assembly checkpoint during mitosis ensures that:',
 "options":{"A":'All chromosomes are properly attached to spindle fibers before anaphase begins', "B":'DNA has been fully replicated before S phase', "C":'The cell has enough nutrients to divide', "D":'Cytokinesis occurs before mitosis'},"answer":'A'},

{"id":26,"subject":'Biology',"topic":'Cell Cycle & Division',"difficulty":'Medium',
 "question":'Apoptosis is best described as:',
 "options":{"A":'Uncontrolled, unregulated cell division', "B":'A programmed, regulated process of cell death', "C":'A specific type of mitosis', "D":'A form of meiosis'},"answer":'B'},

{"id":27,"subject":'Biology',"topic":'Genetics',"difficulty":'Easy',
 "question":'In pea plants, tall (T) is dominant over short (t). A cross of Tt x tt is expected to produce offspring in what ratio?',
 "options":{"A":'All tall', "B":'3 tall : 1 short', "C":'1 tall : 1 short', "D":'All short'},"answer":'C'},

{"id":28,"subject":'Biology',"topic":'Genetics',"difficulty":'Medium',
 "question":'A cross between two heterozygous individuals for a single gene (Aa x Aa) is expected to produce what genotype ratio?',
 "options":{"A":'3 AA : 1 aa', "B":'All Aa', "C":'1 AA : 1 aa', "D":'1 AA : 2 Aa : 1 aa'},"answer":'D'},

{"id":29,"subject":'Biology',"topic":'Genetics',"difficulty":'Medium',
 "question":'X-linked recessive disorders are more common in males than females mainly because:',
 "options":{"A":'Males have only one X chromosome, so a single recessive allele is expressed', "B":'Males have two X chromosomes', "C":'Females cannot carry the allele at all', "D":'The disorder cannot affect males'},"answer":'A'},

{"id":30,"subject":'Biology',"topic":'Genetics',"difficulty":'Hard',
 "question":'In a dihybrid cross AaBb x AaBb, what fraction of offspring is expected to be homozygous recessive for both traits (aabb)?',
 "options":{"A":'9/16', "B":'1/16', "C":'3/16', "D":'1/4'},"answer":'B'},

{"id":31,"subject":'Biology',"topic":'Genetics',"difficulty":'Medium',
 "question":'A man with blood type AB and a woman with blood type O have children. What blood type(s) are possible in their offspring?',
 "options":{"A":'Only AB', "B":'Only O', "C":'Only A or B (never AB or O)', "D":'A, B, AB, and O are all possible'},"answer":'C'},

{"id":32,"subject":'Biology',"topic":'Genetics',"difficulty":'Hard',
 "question":'A trait that skips generations and appears only in children of two unaffected carrier parents is most consistent with:',
 "options":{"A":'Autosomal dominant inheritance', "B":'Codominant inheritance', "C":'Y-linked inheritance', "D":'Autosomal recessive inheritance'},"answer":'D'},

{"id":33,"subject":'Biology',"topic":'Genetics',"difficulty":'Medium',
 "question":'In snapdragons, crossing a red-flowered (RR) plant with a white-flowered (WW) plant produces all pink-flowered (RW) offspring. This pattern is best described as:',
 "options":{"A":'Incomplete dominance', "B":'Codominance', "C":'Epistasis', "D":'Complete dominance'},"answer":'A'},

{"id":34,"subject":'Biology',"topic":'Genetics',"difficulty":'Easy',
 "question":"The physical, observable expression of an organism's genotype, such as eye color, is called its:",
 "options":{"A":'Genotype', "B":'Phenotype', "C":'Allele', "D":'Locus'},"answer":'B'},

{"id":35,"subject":'Biology',"topic":'Molecular Biology',"difficulty":'Easy',
 "question":'In DNA base pairing, adenine pairs with:',
 "options":{"A":'Guanine', "B":'Cytosine', "C":'Thymine', "D":'Uracil'},"answer":'C'},

{"id":36,"subject":'Biology',"topic":'Molecular Biology',"difficulty":'Easy',
 "question":'RNA differs from DNA in that RNA contains the sugar:',
 "options":{"A":'Deoxyribose', "B":'Galactose', "C":'Glucose', "D":'Ribose'},"answer":'D'},

{"id":37,"subject":'Biology',"topic":'Molecular Biology',"difficulty":'Medium',
 "question":'DNA replication is described as semi-conservative because:',
 "options":{"A":'Each new DNA molecule contains one original strand and one newly synthesized strand', "B":'Both new strands are entirely newly synthesized', "C":'Both new strands come from the original molecule unchanged', "D":'No new strands are formed during replication'},"answer":'A'},

{"id":38,"subject":'Biology',"topic":'Molecular Biology',"difficulty":'Medium',
 "question":'The process of converting mRNA codons into a chain of amino acids at the ribosome is called:',
 "options":{"A":'Transcription', "B":'Translation', "C":'Replication', "D":'Splicing'},"answer":'B'},

{"id":39,"subject":'Biology',"topic":'Molecular Biology',"difficulty":'Medium',
 "question":'A mutation that changes one amino acid to a different one in the resulting protein is called a:',
 "options":{"A":'Silent mutation', "B":'Nonsense mutation', "C":'Missense mutation', "D":'Frameshift mutation'},"answer":'C'},

{"id":40,"subject":'Biology',"topic":'Molecular Biology',"difficulty":'Hard',
 "question":"Insertion of a single nucleotide into a gene's coding sequence would most likely cause:",
 "options":{"A":'No change in the resulting protein', "B":"An increase in the protein's stability", "C":'A silent mutation only', "D":'A frameshift, altering every codon downstream of the insertion'},"answer":'D'},

{"id":41,"subject":'Biology',"topic":'Molecular Biology',"difficulty":'Hard',
 "question":'A retrovirus, such as HIV, uses which enzyme to convert its RNA genome into DNA inside a host cell?',
 "options":{"A":'Reverse transcriptase', "B":'DNA polymerase', "C":'RNA polymerase', "D":'Ligase'},"answer":'A'},

{"id":42,"subject":'Biology',"topic":'Molecular Biology',"difficulty":'Medium',
 "question":'The enzyme responsible for joining Okazaki fragments on the lagging strand during DNA replication is:',
 "options":{"A":'Primase', "B":'DNA ligase', "C":'Helicase', "D":'Topoisomerase'},"answer":'B'},

{"id":43,"subject":'Biology',"topic":'Molecular Biology',"difficulty":'Medium',
 "question":'A regulatory DNA sequence that can increase transcription of a gene even when located far from it is called a(n):',
 "options":{"A":'Promoter', "B":'Terminator', "C":'Enhancer', "D":'Exon'},"answer":'C'},

{"id":44,"subject":'Biology',"topic":'Molecular Biology',"difficulty":'Easy',
 "question":'How many nucleotide bases make up a single codon?',
 "options":{"A":'1', "B":'2', "C":'4', "D":'3'},"answer":'D'},

{"id":45,"subject":'Biology',"topic":'Evolution',"difficulty":'Easy',
 "question":'Natural selection acts on:',
 "options":{"A":'Heritable variation that affects survival and reproduction', "B":"Traits acquired during an organism's lifetime", "C":'Random mutations that have no effect on fitness', "D":"Only an organism's physical appearance"},"answer":'A'},

{"id":46,"subject":'Biology',"topic":'Evolution',"difficulty":'Medium',
 "question":'Stabilizing selection tends to:',
 "options":{"A":'Favor extreme phenotypes over the average', "B":'Favor the average phenotype, reducing variation at both extremes', "C":'Have no effect on phenotype distribution', "D":'Always create two distinct phenotype groups'},"answer":'B'},

{"id":47,"subject":'Biology',"topic":'Evolution',"difficulty":'Medium',
 "question":'Convergent evolution describes:',
 "options":{"A":'Two closely related species evolving very different traits', "B":'One species splitting into many species', "C":'Unrelated species independently evolving similar traits due to similar environmental pressures', "D":'A species going extinct'},"answer":'C'},

{"id":48,"subject":'Biology',"topic":'Evolution',"difficulty":'Hard',
 "question":'In a population at Hardy-Weinberg equilibrium, 16% of individuals show the recessive phenotype. What is the frequency of the recessive allele (q)?',
 "options":{"A":'0.16', "B":'0.6', "C":'0.84', "D":'0.4'},"answer":'D'},

{"id":49,"subject":'Biology',"topic":'Classification & Diversity',"difficulty":'Easy',
 "question":'The two-part naming system for species (genus + species) is called:',
 "options":{"A":'Binomial nomenclature', "B":'Cladistics', "C":'Taxonomy alone', "D":'Phylogeny'},"answer":'A'},

{"id":50,"subject":'Biology',"topic":'Classification & Diversity',"difficulty":'Easy',
 "question":'Members of kingdom Fungi obtain nutrition by:',
 "options":{"A":'Photosynthesis', "B":'Absorptive heterotrophy, secreting enzymes to digest food externally', "C":'Ingesting prey internally', "D":'Chemosynthesis exclusively'},"answer":'B'},

{"id":51,"subject":'Biology',"topic":'Classification & Diversity',"difficulty":'Medium',
 "question":'Domain Bacteria and Domain Archaea both consist of organisms that are:',
 "options":{"A":'Eukaryotic and multicellular', "B":'Found only in extreme environments', "C":'Prokaryotic and unicellular', "D":'Photosynthetic exclusively'},"answer":'C'},

{"id":52,"subject":'Biology',"topic":'Classification & Diversity',"difficulty":'Medium',
 "question":'An organism with a segmented body, jointed appendages, and a chitin exoskeleton most likely belongs to phylum:',
 "options":{"A":'Echinodermata', "B":'Annelida', "C":'Mollusca', "D":'Arthropoda'},"answer":'D'},

{"id":53,"subject":'Biology',"topic":'Classification & Diversity',"difficulty":'Easy',
 "question":'Which taxonomic rank is more specific than Family but less specific than Species?',
 "options":{"A":'Genus', "B":'Order', "C":'Class', "D":'Phylum'},"answer":'A'},

{"id":54,"subject":'Biology',"topic":'Classification & Diversity',"difficulty":'Medium',
 "question":'Class Aves (birds) is characterized by:',
 "options":{"A":'Gills and cold-bloodedness', "B":'Feathers, endothermy, and typically the ability to fly', "C":'Mammary glands', "D":'Moist, permeable skin used for respiration'},"answer":'B'},

{"id":55,"subject":'Biology',"topic":'Plant Biology',"difficulty":'Easy',
 "question":'Water and dissolved minerals are transported from roots to leaves through:',
 "options":{"A":'Phloem', "B":'Epidermis', "C":'Xylem', "D":'Cork cambium'},"answer":'C'},

{"id":56,"subject":'Biology',"topic":'Plant Biology',"difficulty":'Medium',
 "question":'The light-dependent reactions of photosynthesis take place in the:',
 "options":{"A":'Cytoplasm', "B":'Stroma', "C":'Mitochondrial matrix', "D":'Thylakoid membrane'},"answer":'D'},

{"id":57,"subject":'Biology',"topic":'Plant Biology',"difficulty":'Medium',
 "question":"A plant's shoot growing toward a light source is an example of:",
 "options":{"A":'Phototropism', "B":'Gravitropism', "C":'Thigmotropism', "D":'Hydrotropism'},"answer":'A'},

{"id":58,"subject":'Biology',"topic":'Plant Biology',"difficulty":'Hard',
 "question":'Mycorrhizal fungi form a mutualistic relationship with plant roots mainly by:',
 "options":{"A":"Only harming the plant's root system", "B":"Increasing the root's effective surface area for water and mineral absorption, in exchange for sugars from the plant", "C":'Producing light energy for the plant', "D":'Preventing water uptake entirely'},"answer":'B'},

{"id":59,"subject":'Biology',"topic":'Plant Biology',"difficulty":'Medium',
 "question":'Auxin, a plant hormone, primarily promotes:',
 "options":{"A":'Fruit ripening', "B":'Leaf abscission only', "C":'Cell elongation and phototropic/gravitropic responses', "D":'Seed dormancy'},"answer":'C'},

{"id":60,"subject":'Biology',"topic":'Plant Biology',"difficulty":'Easy',
 "question":'The male reproductive structure of a flower, which produces pollen, is the:',
 "options":{"A":'Pistil', "B":'Petal', "C":'Sepal', "D":'Stamen'},"answer":'D'},

{"id":61,"subject":'Biology',"topic":'Human Physiology - Digestion',"difficulty":'Easy',
 "question":'Chemical digestion of starch begins in the mouth due to the enzyme:',
 "options":{"A":'Pepsin', "B":'Salivary amylase', "C":'Lipase', "D":'Trypsin'},"answer":'B'},

{"id":62,"subject":'Biology',"topic":'Human Physiology - Digestion',"difficulty":'Medium',
 "question":'The enzyme pepsin, active in the stomach, functions to break down:',
 "options":{"A":'Carbohydrates', "B":'Proteins', "C":'Lipids', "D":'Nucleic acids exclusively'},"answer":'B'},

{"id":63,"subject":'Biology',"topic":'Human Physiology - Digestion',"difficulty":'Medium',
 "question":'Bile, produced by the liver, aids in fat digestion mainly by:',
 "options":{"A":'Chemically breaking fat molecules into fatty acids directly', "B":'Producing lipase itself', "C":'Emulsifying fats into smaller droplets, increasing surface area for lipase action', "D":'Absorbing fats directly into the bloodstream'},"answer":'C'},

{"id":64,"subject":'Biology',"topic":'Human Physiology - Digestion',"difficulty":'Hard',
 "question":'Removal of the gallbladder would most directly affect:',
 "options":{"A":'Protein digestion in the stomach', "B":'Absorption of water in the large intestine', "C":'Starch digestion in the mouth', "D":'The storage and timed release of bile for fat digestion'},"answer":'D'},

{"id":65,"subject":'Biology',"topic":'Human Physiology - Circulation',"difficulty":'Easy',
 "question":'The chamber of the heart that pumps oxygenated blood out to the entire body is the:',
 "options":{"A":'Left ventricle', "B":'Right atrium', "C":'Right ventricle', "D":'Left atrium'},"answer":'A'},

{"id":66,"subject":'Biology',"topic":'Human Physiology - Circulation',"difficulty":'Medium',
 "question":'Pulmonary circulation carries blood between the heart and the:',
 "options":{"A":'Rest of the body', "B":'Lungs, for gas exchange', "C":'Kidneys only', "D":'Liver only'},"answer":'B'},

{"id":67,"subject":'Biology',"topic":'Human Physiology - Circulation',"difficulty":'Medium',
 "question":'Blood clotting (coagulation) primarily involves which blood component along with clotting factors?',
 "options":{"A":'Red blood cells', "B":'Plasma proteins alone, with no cells involved', "C":'Platelets', "D":'White blood cells exclusively'},"answer":'C'},

{"id":68,"subject":'Biology',"topic":'Human Physiology - Circulation',"difficulty":'Hard',
 "question":'During intense exercise, heart rate increases mainly to:',
 "options":{"A":'Decrease oxygen delivery to tissues', "B":'Stop blood flow to the muscles', "C":'Reduce blood pressure to zero', "D":'Increase cardiac output, delivering more oxygen and nutrients to active tissues'},"answer":'D'},

{"id":69,"subject":'Biology',"topic":'Human Physiology - Respiration',"difficulty":'Easy',
 "question":'Gas exchange in the lungs occurs across the walls of the:',
 "options":{"A":'Alveoli', "B":'Bronchi', "C":'Trachea', "D":'Larynx'},"answer":'A'},

{"id":70,"subject":'Biology',"topic":'Human Physiology - Respiration',"difficulty":'Medium',
 "question":'During inhalation, the diaphragm:',
 "options":{"A":'Relaxes and moves upward, decreasing thoracic volume', "B":'Contracts and moves downward, increasing thoracic volume and allowing air to flow in', "C":'Has no role in breathing', "D":'Contracts to force air out'},"answer":'B'},

{"id":71,"subject":'Biology',"topic":'Human Physiology - Respiration',"difficulty":'Medium',
 "question":'Asthma is a condition in which airway inflammation and constriction primarily result in:',
 "options":{"A":'Improved airflow', "B":'No effect on breathing', "C":'Difficulty breathing due to narrowed airways', "D":'Increased lung capacity'},"answer":'C'},

{"id":72,"subject":'Biology',"topic":'Human Physiology - Excretion',"difficulty":'Easy',
 "question":"The diagram shows a nephron with structures labeled 1-4 (the glomerulus, Bowman's capsule, the proximal convoluted tubule, and the loop of Henle). Which labeled structure is the tuft of capillaries where blood filtration begins?",
 "image":'images/q_nephron_glomerulus_diagram.png',
 "options":{"A":'Structure 4 (loop of Henle)', "B":"Structure 2 (Bowman's capsule)", "C":'Structure 3 (proximal convoluted tubule)', "D":'Structure 1 (glomerulus)'},"answer":'D'},

{"id":73,"subject":'Biology',"topic":'Human Physiology - Excretion',"difficulty":'Medium',
 "question":'Besides the proximal convoluted tubule, most of the remaining water reabsorption occurs at the:',
 "options":{"A":'Loop of Henle and collecting duct', "B":'Renal artery', "C":'Ureter', "D":'Bladder wall only'},"answer":'A'},

{"id":74,"subject":'Biology',"topic":'Human Physiology - Excretion',"difficulty":'Hard',
 "question":'Antidiuretic hormone (ADH) increases water reabsorption mainly by:',
 "options":{"A":'Decreasing blood volume intentionally', "B":'Increasing the permeability of the collecting duct to water', "C":'Blocking filtration in the glomerulus', "D":'Increasing urine volume'},"answer":'B'},

{"id":75,"subject":'Biology',"topic":'Human Physiology - Nervous & Endocrine',"difficulty":'Easy',
 "question":'The part of a neuron that receives signals from other neurons is the:',
 "options":{"A":'Cell body only', "B":'Axon', "C":'Dendrite', "D":'Myelin sheath'},"answer":'C'},

{"id":76,"subject":'Biology',"topic":'Human Physiology - Nervous & Endocrine',"difficulty":'Medium',
 "question":'Neurotransmitters released at a synapse are stored, prior to release, in:',
 "options":{"A":'Mitochondria of the postsynaptic neuron only', "B":'The nucleus of the postsynaptic neuron', "C":'The myelin sheath', "D":'Synaptic vesicles in the presynaptic neuron'},"answer":'D'},

{"id":77,"subject":'Biology',"topic":'Human Physiology - Nervous & Endocrine',"difficulty":'Medium',
 "question":'The thyroid gland secretes hormones that primarily regulate:',
 "options":{"A":'Metabolic rate', "B":'Blood glucose levels', "C":'Blood calcium levels exclusively', "D":'The fight-or-flight response'},"answer":'A'},

{"id":78,"subject":'Biology',"topic":'Human Physiology - Nervous & Endocrine',"difficulty":'Hard',
 "question":'Negative feedback in the endocrine system, such as thyroid hormone regulation, functions to:',
 "options":{"A":'Continuously increase hormone levels without limit', "B":'Maintain hormone levels within a stable range by inhibiting further release once levels are sufficient', "C":'Have no regulatory effect at all', "D":'Only apply to insulin regulation'},"answer":'B'},

{"id":79,"subject":'Biology',"topic":'Human Physiology - Reproduction',"difficulty":'Easy',
 "question":'In females, fertilization typically occurs in the:',
 "options":{"A":'Uterus', "B":'Ovary', "C":'Fallopian tube (oviduct)', "D":'Vagina'},"answer":'C'},

{"id":80,"subject":'Biology',"topic":'Human Physiology - Reproduction',"difficulty":'Medium',
 "question":'Progesterone, secreted mainly by the corpus luteum, functions to:',
 "options":{"A":'Trigger ovulation', "B":'Cause menstruation', "C":'Stimulate sperm production', "D":'Maintain the uterine lining in preparation for and during pregnancy'},"answer":'D'},

{"id":81,"subject":'Biology',"topic":'Ecology',"difficulty":'Medium',
 "question":'The transfer of energy from one trophic level to the next in an ecosystem is typically inefficient, with roughly what percentage of energy passing to the next level?',
 "options":{"A":'10%', "B":'50%', "C":'90%', "D":'100%'},"answer":'A'},

# ============================================================
# CHEMISTRY (45) - id 82-126
# ============================================================

{"id":82,"subject":'Chemistry',"topic":'Atomic Structure',"difficulty":'Easy',
 "question":'Electrons in an atom are located:',
 "options":{"A":'In the nucleus', "B":'In an electron cloud surrounding the nucleus', "C":'Nowhere in the atom', "D":'Only in the innermost shell'},"answer":'B'},

{"id":83,"subject":'Chemistry',"topic":'Atomic Structure',"difficulty":'Medium',
 "question":'An atom of chlorine-35 (atomic number 17) contains how many neutrons?',
 "options":{"A":'17', "B":'35', "C":'18', "D":'52'},"answer":'C'},

{"id":84,"subject":'Chemistry',"topic":'Atomic Structure',"difficulty":'Medium',
 "question":'The electron configuration of a neutral phosphorus atom (Z = 15) is:',
 "options":{"A":'1s2 2s2 2p6 3s1 3p4', "B":'1s2 2s2 2p6 3s2 3p2', "C":'1s2 2s2 2p5 3s2 3p4', "D":'1s2 2s2 2p6 3s2 3p3'},"answer":'D'},

{"id":85,"subject":'Chemistry',"topic":'Atomic Structure',"difficulty":'Hard',
 "question":'An ion has 20 protons and 18 electrons. What is its charge?',
 "options":{"A":'+2', "B":'-2', "C":'+20', "D":'-18'},"answer":'A'},

{"id":86,"subject":'Chemistry',"topic":'Atomic Structure',"difficulty":'Easy',
 "question":'Isotopes of an element differ in their number of:',
 "options":{"A":'Protons', "B":'Neutrons', "C":'Electrons', "D":'Their atomic number'},"answer":'B'},

{"id":87,"subject":'Chemistry',"topic":'Periodic Table',"difficulty":'Easy',
 "question":'The vertical columns of the periodic table are called:',
 "options":{"A":'Periods', "B":'Blocks', "C":'Groups', "D":'Series'},"answer":'C'},

{"id":88,"subject":'Chemistry',"topic":'Periodic Table',"difficulty":'Medium',
 "question":'Atomic radius generally changes going down a group in that it:',
 "options":{"A":'Decreases', "B":'Becomes negative', "C":'Stays exactly the same', "D":'Increases, as more electron shells are added'},"answer":'D'},

{"id":89,"subject":'Chemistry',"topic":'Periodic Table',"difficulty":'Medium',
 "question":'An element with high electron affinity and a strong tendency to gain one electron would most likely be found:',
 "options":{"A":'In Group 17, near the right side of the periodic table', "B":'In Group 1, on the far left', "C":'Among the noble gases', "D":'Among the transition metals'},"answer":'A'},

{"id":90,"subject":'Chemistry',"topic":'Chemical Bonding',"difficulty":'Easy',
 "question":'A bond formed by the sharing of electron pairs between atoms is a:',
 "options":{"A":'Ionic bond', "B":'Covalent bond', "C":'Metallic bond', "D":'Van der Waals interaction'},"answer":'B'},

{"id":91,"subject":'Chemistry',"topic":'Chemical Bonding',"difficulty":'Medium',
 "question":'According to VSEPR theory, a molecule with three bonding pairs and one lone pair on the central atom (like NH3) has a molecular geometry of:',
 "options":{"A":'Trigonal planar', "B":'Linear', "C":'Trigonal pyramidal', "D":'Tetrahedral'},"answer":'C'},

{"id":92,"subject":'Chemistry',"topic":'Chemical Bonding',"difficulty":'Medium',
 "question":'Water (H2O) is polar overall mainly because:',
 "options":{"A":'It has a linear molecular shape', "B":'Oxygen and hydrogen have identical electronegativities', "C":'It contains no polar bonds', "D":'Its bent molecular geometry prevents the individual bond dipoles from canceling out'},"answer":'D'},

{"id":93,"subject":'Chemistry',"topic":'Chemical Bonding',"difficulty":'Hard',
 "question":"Metallic bonding, characterized by a 'sea' of delocalized electrons, explains why metals are typically:",
 "options":{"A":'Malleable, ductile, and good electrical conductors', "B":'Brittle and poor conductors of electricity', "C":'Transparent and non-conductive', "D":'Highly volatile at room temperature'},"answer":'A'},

{"id":94,"subject":'Chemistry',"topic":'Chemical Bonding',"difficulty":'Easy',
 "question":'A hydrogen bond between two water molecules forms between:',
 "options":{"A":'Two oxygen atoms directly', "B":'A hydrogen atom on one molecule and an oxygen lone pair on a neighboring molecule', "C":'Two hydrogen atoms directly', "D":'Atoms only within a single water molecule'},"answer":'B'},

{"id":95,"subject":'Chemistry',"topic":'States of Matter',"difficulty":'Easy',
 "question":'Which state of matter has neither a definite shape nor a definite volume?',
 "options":{"A":'Solid', "B":'Liquid', "C":'Gas', "D":'Crystal'},"answer":'C'},

{"id":96,"subject":'Chemistry',"topic":'States of Matter',"difficulty":'Medium',
 "question":'A gas occupies 8.0 L at a pressure of 2.0 atm. What volume will it occupy at 4.0 atm, assuming constant temperature?',
 "options":{"A":'16 L', "B":'32 L', "C":'2.0 L', "D":'4.0 L'},"answer":'D'},

{"id":97,"subject":'Chemistry',"topic":'States of Matter',"difficulty":'Hard',
 "question":'A gas has a volume of 6 L at 300 K and 1 atm. What volume will it occupy at 600 K and 2 atm?',
 "options":{"A":'6 L', "B":'3 L', "C":'12 L', "D":'24 L'},"answer":'A'},

{"id":98,"subject":'Chemistry',"topic":'Stoichiometry',"difficulty":'Easy',
 "question":'The molar mass of calcium carbonate (CaCO3) is approximately:',
 "options":{"A":'56 g/mol', "B":'100 g/mol', "C":'78 g/mol', "D":'44 g/mol'},"answer":'B'},

{"id":99,"subject":'Chemistry',"topic":'Stoichiometry',"difficulty":'Medium',
 "question":'How many moles of hydrogen atoms are present in 3 moles of Al(OH)3?',
 "options":{"A":'3', "B":'6', "C":'9', "D":'12'},"answer":'C'},

{"id":100,"subject":'Chemistry',"topic":'Stoichiometry',"difficulty":'Hard',
 "question":'A 500 mL solution contains 2.0 moles of NaOH. What is the molarity of the solution?',
 "options":{"A":'0.25 M', "B":'1.0 M', "C":'2.0 M', "D":'4.0 M'},"answer":'D'},

{"id":101,"subject":'Chemistry',"topic":'Stoichiometry',"difficulty":'Medium',
 "question":'In the reaction 2H2 + O2 -> 2H2O, how many moles of O2 are needed to react completely with 8 moles of H2?',
 "options":{"A":'4', "B":'2', "C":'8', "D":'16'},"answer":'A'},

{"id":102,"subject":'Chemistry',"topic":'Thermochemistry',"difficulty":'Easy',
 "question":'In an endothermic reaction, the products have _____ energy than the reactants.',
 "options":{"A":'Lower', "B":'Higher', "C":'The same', "D":'Zero'},"answer":'B'},

{"id":103,"subject":'Chemistry',"topic":'Thermochemistry',"difficulty":'Medium',
 "question":"Hess's law relies on the principle that enthalpy is a state function, meaning:",
 "options":{"A":'Enthalpy change can never be calculated indirectly', "B":'Enthalpy depends heavily on the specific reaction pathway used', "C":'The total enthalpy change depends only on the initial and final states, not the pathway taken', "D":'Enthalpy changes are always zero'},"answer":'C'},

{"id":104,"subject":'Chemistry',"topic":'Chemical Equilibrium',"difficulty":'Medium',
 "question":'For the reaction N2(g) + 3H2(g) <-> 2NH3(g), decreasing the volume (increasing pressure) shifts the equilibrium toward:',
 "options":{"A":'The reactants (4 moles of gas)', "B":'Complete depletion of the reactants', "C":'No shift at all', "D":'The products (2 moles of gas), the side with fewer gas moles'},"answer":'D'},

{"id":105,"subject":'Chemistry',"topic":'Chemical Equilibrium',"difficulty":'Hard',
 "question":'If the temperature is increased for an endothermic reaction at equilibrium, the equilibrium will shift:',
 "options":{"A":'Toward the products, increasing yield', "B":'Toward the reactants, decreasing yield', "C":'Not at all', "D":'To stop the reaction entirely'},"answer":'A'},

{"id":106,"subject":'Chemistry',"topic":'Reaction Kinetics',"difficulty":'Easy',
 "question":'Raising the temperature of a reaction generally increases its rate mainly because:',
 "options":{"A":'Molecules move slower', "B":'Molecules collide more frequently and with greater energy', "C":'The reaction becomes less thermodynamically favorable', "D":'Activation energy increases'},"answer":'B'},

{"id":107,"subject":'Chemistry',"topic":'Reaction Kinetics',"difficulty":'Medium',
 "question":'A catalyst increases reaction rate by:',
 "options":{"A":'Increasing the activation energy required', "B":'Changing the products of the reaction', "C":'Providing an alternative pathway with lower activation energy', "D":'Being permanently consumed in the reaction'},"answer":'C'},

{"id":108,"subject":'Chemistry',"topic":'Electrochemistry',"difficulty":'Medium',
 "question":'In an electrochemical cell, oxidation always occurs at the:',
 "options":{"A":'Cathode', "B":'Voltmeter', "C":'Salt bridge', "D":'Anode'},"answer":'D'},

{"id":109,"subject":'Chemistry',"topic":'Electrochemistry',"difficulty":'Hard',
 "question":'In the reaction Zn(s) + Cu2+(aq) -> Zn2+(aq) + Cu(s), the copper ions are:',
 "options":{"A":'Reduced', "B":'Oxidized', "C":'Unchanged', "D":'Acting as a catalyst'},"answer":'A'},

{"id":110,"subject":'Chemistry',"topic":'Acids & Bases',"difficulty":'Easy',
 "question":'A solution with a pH of 2 is:',
 "options":{"A":'Weakly basic', "B":'Strongly acidic', "C":'Strongly basic', "D":'Neutral'},"answer":'B'},

{"id":111,"subject":'Chemistry',"topic":'Acids & Bases',"difficulty":'Medium',
 "question":'The graph shows a titration curve of pH versus volume of base added to an acid, with a steep rise in pH near the midpoint of the curve. The point on the curve where the moles of acid exactly equal the moles of base added is called the:',
 "image":'images/q_titration_curve_equivalence_point.png',
 "options":{"A":'Buffer region', "B":'Half-life point', "C":'Equivalence point', "D":'Saturation point'},"answer":'C'},

{"id":112,"subject":'Chemistry',"topic":'Acids & Bases',"difficulty":'Medium',
 "question":'According to the Bronsted-Lowry theory, a base is a substance that:',
 "options":{"A":'Donates a proton (H+)', "B":'Releases hydroxide ions exclusively', "C":'Donates a pair of electrons only', "D":'Accepts a proton (H+)'},"answer":'D'},

{"id":113,"subject":'Chemistry',"topic":'Acids & Bases',"difficulty":'Hard',
 "question":'A buffer made of ammonia and ammonium chloride resists a large pH change when a small amount of strong acid is added because:',
 "options":{"A":'The ammonia component reacts with and neutralizes the added acid', "B":'The ammonium chloride reacts with the acid instead', "C":'The buffer has no capacity to resist pH change', "D":'The pH always drops sharply regardless'},"answer":'A'},

{"id":114,"subject":'Chemistry',"topic":'Organic Chemistry',"difficulty":'Easy',
 "question":'The functional group -OH characterizes which class of organic compounds?',
 "options":{"A":'Aldehydes', "B":'Alcohols', "C":'Ketones', "D":'Esters'},"answer":'B'},

{"id":115,"subject":'Chemistry',"topic":'Organic Chemistry',"difficulty":'Medium',
 "question":'Alkanes primarily undergo which type of reaction, in which a hydrogen atom is replaced by another atom or group?',
 "options":{"A":'Addition', "B":'Elimination', "C":'Substitution', "D":'Condensation'},"answer":'C'},

{"id":116,"subject":'Chemistry',"topic":'Organic Chemistry',"difficulty":'Medium',
 "question":'A secondary alcohol has its -OH bearing carbon bonded to how many other carbon atoms?',
 "options":{"A":'One', "B":'Zero', "C":'Three', "D":'Two'},"answer":'D'},

{"id":117,"subject":'Chemistry',"topic":'Organic Chemistry',"difficulty":'Hard',
 "question":'Which of the following best describes an SN1 reaction mechanism?',
 "options":{"A":'A two-step reaction proceeding through a stable carbocation intermediate', "B":'A one-step concerted reaction with simultaneous bond breaking and forming', "C":'A reaction that never involves a leaving group', "D":'A reaction exclusive to alkenes'},"answer":'A'},

{"id":118,"subject":'Chemistry',"topic":'Organic Chemistry',"difficulty":'Medium',
 "question":'Esters are formed through condensation reactions between carboxylic acids and alcohols, releasing which byproduct?',
 "options":{"A":'Carbon dioxide', "B":'Water', "C":'Ammonia', "D":'Hydrogen gas'},"answer":'B'},

{"id":119,"subject":'Chemistry',"topic":'Organic Chemistry',"difficulty":'Easy',
 "question":'A carbonyl group (C=O) located between two carbon chains, rather than at the end of the chain, characterizes:',
 "options":{"A":'An aldehyde', "B":'A carboxylic acid', "C":'A ketone', "D":'An amine'},"answer":'C'},

{"id":120,"subject":'Chemistry',"topic":'Inorganic Chemistry',"difficulty":'Medium',
 "question":'The general unreactivity of Group 18 elements (noble gases) is best explained by:',
 "options":{"A":'Their small atomic size', "B":'Their tendency to form multiple bonds readily', "C":'Very high nuclear charge', "D":'A complete valence electron shell, providing high stability'},"answer":'D'},

{"id":121,"subject":'Chemistry',"topic":'Inorganic Chemistry',"difficulty":'Medium',
 "question":'Alkali metals (Group 1) react with water more vigorously than alkaline earth metals (Group 2) of the same period mainly because:',
 "options":{"A":'They have lower ionization energy, losing their single valence electron more easily', "B":'They have higher ionization energy', "C":'They do not react with water at all', "D":'They have smaller atomic radii'},"answer":'A'},

{"id":122,"subject":'Chemistry',"topic":'Inorganic Chemistry',"difficulty":'Hard',
 "question":"In the reaction Fe2O3 + 3CO -> 2Fe + 3CO2, iron's oxidation state changes from:",
 "options":{"A":'0 to +3', "B":'+3 to 0 (reduction)', "C":'+2 to +3', "D":'No change occurs'},"answer":'B'},

{"id":123,"subject":'Chemistry',"topic":'Physical Chemistry',"difficulty":'Medium',
 "question":'Boiling point elevation, a colligative property, occurs when a non-volatile solute is added to a solvent because the solute:',
 "options":{"A":'Has no effect on the boiling point', "B":'Increases the vapor pressure of the solvent', "C":'Lowers the vapor pressure of the solvent, requiring a higher temperature to reach boiling', "D":"Only affects the solvent's density"},"answer":'C'},

{"id":124,"subject":'Chemistry',"topic":'Physical Chemistry',"difficulty":'Hard',
 "question":'20 mL of 0.4 M H2SO4 is required to completely neutralize 40 mL of KOH solution (H2SO4 + 2KOH -> K2SO4 + 2H2O). What is the molarity of the KOH solution?',
 "options":{"A":'0.1 M', "B":'0.2 M', "C":'0.8 M', "D":'0.4 M'},"answer":'D'},

{"id":125,"subject":'Chemistry',"topic":'Environmental Chemistry',"difficulty":'Easy',
 "question":'The depletion of the ozone layer is primarily caused by:',
 "options":{"A":'Chlorofluorocarbons (CFCs) and related halogenated compounds', "B":'Increased carbon dioxide emissions', "C":'Excess oxygen production', "D":'Volcanic ash exclusively'},"answer":'A'},

{"id":126,"subject":'Chemistry',"topic":'Environmental Chemistry',"difficulty":'Medium',
 "question":'Which of the following practices would most directly help reduce acid rain formation?',
 "options":{"A":'Increasing coal combustion without emission controls', "B":'Reducing sulfur dioxide and nitrogen oxide emissions from industrial processes and vehicles', "C":'Removing catalytic converters from cars', "D":'Increasing fossil fuel subsidies'},"answer":'B'},

# ============================================================
# PHYSICS (36) - id 127-162
# ============================================================

{"id":127,"subject":'Physics',"topic":'Kinematics',"difficulty":'Easy',
 "question":"A cyclist covers 30 km in 3 hours at constant speed. What is the cyclist's speed?",
 "options":{"A":'90 km/h', "B":'15 km/h', "C":'10 km/h', "D":'3.3 km/h'},"answer":'C'},

{"id":128,"subject":'Physics',"topic":'Kinematics',"difficulty":'Medium',
 "question":'A car accelerates uniformly from 10 m/s to 25 m/s in 5 seconds. What is its acceleration?',
 "options":{"A":'2 m/s^2', "B":'5 m/s^2', "C":'7.5 m/s^2', "D":'3 m/s^2'},"answer":'D'},

{"id":129,"subject":'Physics',"topic":'Kinematics',"difficulty":'Hard',
 "question":'A ball is dropped from rest and falls for 4 seconds before hitting the ground (g = 10 m/s^2, ignoring air resistance). What is its velocity just before impact?',
 "options":{"A":'40 m/s', "B":'20 m/s', "C":'80 m/s', "D":'10 m/s'},"answer":'A'},

{"id":130,"subject":'Physics',"topic":'Dynamics',"difficulty":'Easy',
 "question":"A stationary object experiences zero net force. According to Newton's first law, it will:",
 "options":{"A":'Immediately start moving', "B":'Remain at rest', "C":'Accelerate randomly', "D":'Gain mass'},"answer":'B'},

{"id":131,"subject":'Physics',"topic":'Dynamics',"difficulty":'Medium',
 "question":'A net force of 20 N produces an acceleration of 4 m/s^2 in an object. What is the mass of the object?',
 "options":{"A":'16 kg', "B":'80 kg', "C":'5 kg', "D":'24 kg'},"answer":'C'},

{"id":132,"subject":'Physics',"topic":'Dynamics',"difficulty":'Medium',
 "question":"Which of the following is a correct statement of Newton's second law?",
 "options":{"A":'An object at rest stays at rest unless acted upon by a force', "B":'Momentum is always conserved in an isolated system', "C":'For every action force, there is an equal and opposite reaction force', "D":'Force equals mass multiplied by acceleration (F = ma)'},"answer":'D'},

{"id":133,"subject":'Physics',"topic":'Dynamics',"difficulty":'Hard',
 "question":"A 4 kg object is pushed with a horizontal force of 22 N across a surface with a coefficient of kinetic friction of 0.25 (g = 10 m/s^2). What is the object's acceleration?",
 "options":{"A":'3 m/s^2', "B":'5.5 m/s^2', "C":'2 m/s^2', "D":'4 m/s^2'},"answer":'A'},

{"id":134,"subject":'Physics',"topic":'Work, Energy & Power',"difficulty":'Easy',
 "question":"If a force acts parallel to the direction of an object's motion, the work done by that force is:",
 "options":{"A":'Zero', "B":'Maximum for that magnitude of force and displacement', "C":'Always negative', "D":'Undefined'},"answer":'B'},

{"id":135,"subject":'Physics',"topic":'Work, Energy & Power',"difficulty":'Medium',
 "question":'A 4 kg object is raised to a height of 5 m (g = 10 m/s^2). What is its gravitational potential energy?',
 "options":{"A":'20 J', "B":'50 J', "C":'200 J', "D":'9 J'},"answer":'C'},

{"id":136,"subject":'Physics',"topic":'Work, Energy & Power',"difficulty":'Medium',
 "question":'A 4 kg object moving at 5 m/s has a kinetic energy of:',
 "options":{"A":'20 J', "B":'10 J', "C":'100 J', "D":'50 J'},"answer":'D'},

{"id":137,"subject":'Physics',"topic":'Work, Energy & Power',"difficulty":'Hard',
 "question":'A motor produces 24000 J of energy in 40 seconds. What is its power output?',
 "options":{"A":'600 W', "B":'960000 W', "C":'60 W', "D":'6000 W'},"answer":'A'},

{"id":138,"subject":'Physics',"topic":'Circular Motion & Gravitation',"difficulty":'Easy',
 "question":'The direction of centripetal force in uniform circular motion always points:',
 "options":{"A":'Tangent to the circular path', "B":'Toward the center of the circle', "C":'Away from the center', "D":"In the direction of the object's velocity"},"answer":'B'},

{"id":139,"subject":'Physics',"topic":'Circular Motion & Gravitation',"difficulty":'Medium',
 "question":'If the distance between two masses is tripled while both masses remain unchanged, the gravitational force between them becomes:',
 "options":{"A":'3 times the original', "B":'1/3 of the original', "C":'1/9 of the original', "D":'9 times the original'},"answer":'C'},

{"id":140,"subject":'Physics',"topic":'Circular Motion & Gravitation',"difficulty":'Hard',
 "question":"If Earth's radius were to double while its mass stayed the same, the acceleration due to gravity at its surface would:",
 "options":{"A":'Stay the same', "B":'Double', "C":'Quadruple', "D":'Be reduced to 1/4 of its original value'},"answer":'D'},

{"id":141,"subject":'Physics',"topic":'Fluid Mechanics',"difficulty":'Easy',
 "question":'An object sinks in a fluid when the buoyant force acting on it is:',
 "options":{"A":'Less than its weight', "B":'Greater than its weight', "C":'Equal to its weight', "D":'Twice its weight'},"answer":'A'},

{"id":142,"subject":'Physics',"topic":'Fluid Mechanics',"difficulty":'Medium',
 "question":"Pascal's principle states that pressure applied to an enclosed fluid is:",
 "options":{"A":'Absorbed entirely at the point of application', "B":'Transmitted undiminished throughout the fluid in all directions', "C":'Lost as the fluid moves away from the source', "D":'Only transmitted in the direction of application'},"answer":'B'},

{"id":143,"subject":'Physics',"topic":'Fluid Mechanics',"difficulty":'Hard',
 "question":"According to Bernoulli's principle, as the speed of a flowing fluid increases, its pressure:",
 "options":{"A":'Increases', "B":'Stays exactly constant', "C":'Decreases', "D":'Becomes zero'},"answer":'C'},

{"id":144,"subject":'Physics',"topic":'Oscillations & Waves',"difficulty":'Easy',
 "question":'The lowest point of a transverse wave is called the:',
 "options":{"A":'Crest', "B":'Amplitude', "C":'Node', "D":'Trough'},"answer":'D'},

{"id":145,"subject":'Physics',"topic":'Oscillations & Waves',"difficulty":'Medium',
 "question":"A pendulum's period depends on its length such that a shorter pendulum has:",
 "options":{"A":'A shorter period (higher frequency)', "B":'A longer period', "C":'The same period regardless of length', "D":'No defined period'},"answer":'A'},

{"id":146,"subject":'Physics',"topic":'Oscillations & Waves',"difficulty":'Medium',
 "question":'A wave has a frequency of 20 Hz and a wavelength of 15 m. What is its speed?',
 "options":{"A":'0.75 m/s', "B":'300 m/s', "C":'35 m/s', "D":'1.33 m/s'},"answer":'B'},

{"id":147,"subject":'Physics',"topic":'Oscillations & Waves',"difficulty":'Hard',
 "question":'Destructive interference occurs when two waves meet:',
 "options":{"A":'In phase, amplifying each other', "B":'At a 45-degree angle only', "C":'Completely out of phase, with crest meeting trough, reducing or canceling amplitude', "D":'With identical frequencies and phases always'},"answer":'C'},

{"id":148,"subject":'Physics',"topic":'Thermodynamics',"difficulty":'Easy',
 "question":'Conduction is a method of heat transfer that occurs primarily through:',
 "options":{"A":'Only in gases', "B":'The bulk movement of fluid', "C":'Electromagnetic waves through a vacuum', "D":'Direct contact between particles, especially in solids'},"answer":'D'},

{"id":149,"subject":'Physics',"topic":'Thermodynamics',"difficulty":'Medium',
 "question":'An isothermal process, by definition, involves:',
 "options":{"A":'Constant temperature throughout the process', "B":'No heat exchange with the surroundings', "C":'Constant volume', "D":'Constant pressure'},"answer":'A'},

{"id":150,"subject":'Physics',"topic":'Thermodynamics',"difficulty":'Hard',
 "question":'A gas at constant pressure absorbs 600 J of heat and does 200 J of work on its surroundings. What is the change in internal energy of the gas?',
 "options":{"A":'800 J', "B":'400 J', "C":'-400 J', "D":'200 J'},"answer":'B'},

{"id":151,"subject":'Physics',"topic":'Electrostatics',"difficulty":'Easy',
 "question":'Two objects with like electric charges will:',
 "options":{"A":'Attract each other', "B":'Have no interaction', "C":'Repel each other', "D":"Neutralize each other's charge"},"answer":'C'},

{"id":152,"subject":'Physics',"topic":'Electrostatics',"difficulty":'Medium',
 "question":"According to Coulomb's law, the force between two point charges is directly proportional to:",
 "options":{"A":'The distance between them', "B":'The temperature of the surrounding medium', "C":'The square of the distance between them', "D":'The product of the magnitudes of the two charges'},"answer":'D'},

{"id":153,"subject":'Physics',"topic":'Current Electricity',"difficulty":'Easy',
 "question":"Ohm's law states that current equals voltage divided by:",
 "options":{"A":'Resistance', "B":'Power', "C":'Time', "D":'Energy'},"answer":'A'},

{"id":154,"subject":'Physics',"topic":'Current Electricity',"difficulty":'Medium',
 "question":'The diagram shows a circuit where resistors R1 (3 ohm) and R2 (3 ohm) are connected in series, and this series combination is connected in parallel with R3 (6 ohm). What is the total resistance of the circuit?',
 "image":'images/q_circuit_series_then_parallel_v2.png',
 "options":{"A":'6 ohm', "B":'3 ohm', "C":'12 ohm', "D":'1.5 ohm'},"answer":'B'},

{"id":155,"subject":'Physics',"topic":'Current Electricity',"difficulty":'Hard',
 "question":'Two resistors of 20 ohm and 5 ohm are connected in parallel. What is their equivalent resistance?',
 "options":{"A":'25 ohm', "B":'15 ohm', "C":'4 ohm', "D":'100 ohm'},"answer":'C'},

{"id":156,"subject":'Physics',"topic":'Current Electricity',"difficulty":'Medium',
 "question":'A 500 W appliance operates at 250 V. What current does it draw?',
 "options":{"A":'5 A', "B":'0.5 A', "C":'125000 A', "D":'2 A'},"answer":'D'},

{"id":157,"subject":'Physics',"topic":'Electromagnetism',"difficulty":'Medium',
 "question":'The strength of the magnetic field around a straight current-carrying wire:',
 "options":{"A":'Decreases with increasing distance from the wire', "B":'Increases with distance from the wire', "C":'Is unaffected by distance from the wire', "D":'Is zero at all points around the wire'},"answer":'A'},

{"id":158,"subject":'Physics',"topic":'Electromagnetism',"difficulty":'Hard',
 "question":"According to Lenz's law, an induced current always flows in a direction that:",
 "options":{"A":'Reinforces the change in magnetic flux that caused it', "B":'Opposes the change in magnetic flux that caused it', "C":'Has no relationship to the original flux change', "D":'Is fixed regardless of the flux change'},"answer":'B'},

{"id":159,"subject":'Physics',"topic":'Modern Physics',"difficulty":'Easy',
 "question":'The overall electric charge of a neutron is:',
 "options":{"A":'Positive', "B":'Negative', "C":'Neutral (zero)', "D":'Variable, depending on the atom'},"answer":'C'},

{"id":160,"subject":'Physics',"topic":'Modern Physics',"difficulty":'Medium',
 "question":'In alpha decay, an unstable nucleus emits:',
 "options":{"A":'An electron and an antineutrino', "B":'A positron', "C":'A photon only', "D":'A helium nucleus (2 protons and 2 neutrons)'},"answer":'D'},

{"id":161,"subject":'Physics',"topic":'Modern Physics',"difficulty":'Hard',
 "question":'A radioactive isotope has a half-life of 3 hours. Starting with 400 g, how much remains after 12 hours?',
 "options":{"A":'25 g', "B":'50 g', "C":'12.5 g', "D":'100 g'},"answer":'A'},

{"id":162,"subject":'Physics',"topic":'Optics',"difficulty":'Medium',
 "question":'The ray diagram shows a convex lens with an object placed beyond twice the focal length (2F). Based on the diagram, the image formed is:',
 "image":'images/q_convex_lens_object_beyond_2f.png',
 "options":{"A":'Virtual, upright, and magnified', "B":'Real, inverted, and diminished, formed between F and 2F on the other side of the lens', "C":'Real, upright, and magnified', "D":'Virtual, inverted, and diminished'},"answer":'B'},

# ============================================================
# ENGLISH (9) - id 163-171
# ============================================================

{"id":163,"subject":'English',"topic":'Synonyms',"difficulty":'Easy',
 "question":"Choose the word most nearly similar in meaning to 'BENEVOLENT':",
 "options":{"A":'Indifferent', "B":'Cruel', "C":'Kind', "D":'Selfish'},"answer":'C'},

{"id":164,"subject":'English',"topic":'Antonyms',"difficulty":'Easy',
 "question":"Choose the word most nearly opposite in meaning to 'TRANSPARENT':",
 "options":{"A":'Obvious', "B":'Clear', "C":'Visible', "D":'Opaque'},"answer":'D'},

{"id":165,"subject":'English',"topic":'Grammar',"difficulty":'Easy',
 "question":'Choose the grammatically correct sentence:',
 "options":{"A":"He doesn't know the answer.", "B":"He don't know the answer.", "C":'He not knows the answer.', "D":"He doesn't knows the answer."},"answer":'A'},

{"id":166,"subject":'English',"topic":'Grammar',"difficulty":'Medium',
 "question":'Choose the correct sentence:',
 "options":{"A":'It is essential that he attends the meeting on time.', "B":'It is essential that he attend the meeting on time.', "C":'It is essential that he attends to the meeting.', "D":'It is essential he will attend the meeting.'},"answer":'B'},

{"id":167,"subject":'English',"topic":'Sentence Correction',"difficulty":'Medium',
 "question":'Choose the sentence that is grammatically correct:',
 "options":{"A":'Neither of the answer are correct.', "B":'Neither of the answers are correct.', "C":'Neither of the answers is correct.', "D":'Neither of the answers were correct.'},"answer":'C'},

{"id":168,"subject":'English',"topic":'Vocabulary',"difficulty":'Medium',
 "question":"Choose the word that best completes the sentence: 'The negotiations reached a(n) ______ that satisfied both parties.'",
 "options":{"A":'Impasse', "B":'Conflict', "C":'Deadlock', "D":'Compromise'},"answer":'D'},

{"id":169,"subject":'English',"topic":'Idioms',"difficulty":'Medium',
 "question":"Choose the meaning closest to the idiom 'to bite the bullet':",
 "options":{"A":'To avoid a difficult situation entirely', "B":'To face a difficult or unpleasant situation with courage', "C":'To cause harm to someone else', "D":'To celebrate a victory'},"answer":'B'},

{"id":170,"subject":'English',"topic":'Sentence Correction',"difficulty":'Hard',
 "question":"Choose the option that best corrects the sentence: 'Neither the teacher nor the students was aware of the schedule change.'",
 "options":{"A":'Neither the teacher nor the students was aware about the schedule change.', "B":'Neither the teacher nor the students were aware of the schedule change.', "C":'Neither the teachers nor the student were aware of the schedule change.', "D":'No correction needed.'},"answer":'B'},

{"id":171,"subject":'English',"topic":'Prepositions',"difficulty":'Hard',
 "question":"Choose the correct preposition: 'She has been interested ______ astronomy since childhood.'",
 "options":{"A":'on', "B":'at', "C":'in', "D":'for'},"answer":'C'},

# ============================================================
# LOGICAL REASONING (9) - id 172-180
# ============================================================

{"id":172,"subject":'Logical Reasoning',"topic":'Number Series',"difficulty":'Easy',
 "question":'Find the next number in the series: 5, 10, 15, 20, ?',
 "options":{"A":'22', "B":'24', "C":'30', "D":'25'},"answer":'D'},

{"id":173,"subject":'Logical Reasoning',"topic":'Number Series',"difficulty":'Easy',
 "question":'Find the missing number: 2, 5, 10, 17, ?',
 "options":{"A":'26', "B":'24', "C":'28', "D":'30'},"answer":'A'},

{"id":174,"subject":'Logical Reasoning',"topic":'Analogies',"difficulty":'Easy',
 "question":'Bird is to Nest as Bee is to:',
 "options":{"A":'Flower', "B":'Hive', "C":'Honey', "D":'Wing'},"answer":'B'},

{"id":175,"subject":'Logical Reasoning',"topic":'Analogies',"difficulty":'Medium',
 "question":'Doctor is to Hospital as Teacher is to:',
 "options":{"A":'Student', "B":'Book', "C":'School', "D":'Classroom exam'},"answer":'C'},

{"id":176,"subject":'Logical Reasoning',"topic":'Blood Relations',"difficulty":'Medium',
 "question":"Pointing to a photograph, a man said, 'She is the daughter of my grandfather's only son.' How is the woman related to the man, if the man has no siblings other than possibly her?",
 "options":{"A":'Niece', "B":'Cousin', "C":'Aunt', "D":'Sister'},"answer":'D'},

{"id":177,"subject":'Logical Reasoning',"topic":'Coding-Decoding',"difficulty":'Medium',
 "question":'If in a certain code, APPLE is written as BQQMF, how is MANGO written in the same code?',
 "options":{"A":'NBOHP', "B":'NBOHQ', "C":'MBOHP', "D":'NBPHP'},"answer":'A'},

{"id":178,"subject":'Logical Reasoning',"topic":'Syllogism',"difficulty":'Hard',
 "question":'All doctors are educated. No educated people are illiterate. Which conclusion logically follows?',
 "options":{"A":'Some doctors are illiterate', "B":'No doctors are illiterate', "C":'All illiterate people are doctors', "D":'Some educated people are doctors'},"answer":'B'},

{"id":179,"subject":'Logical Reasoning',"topic":'Pattern Recognition',"difficulty":'Hard',
 "question":'Find the next term in the series: 3, 6, 11, 18, 27, ?',
 "options":{"A":'40', "B":'36', "C":'38', "D":'34'},"answer":'C'},

{"id":180,"subject":'Logical Reasoning',"topic":'Direction Sense',"difficulty":'Medium',
 "question":'A man walks 6 km east, then turns north and walks 8 km. How far is he from his starting point?',
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