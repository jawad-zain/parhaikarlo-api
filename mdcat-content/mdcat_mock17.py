"""
MDCAT Mock Test 17
==================
Full-length mock test: 180 MCQs
Weightage: Biology 81 | Chemistry 45 | Physics 36 | English 9 | Logical Reasoning 9
Difficulty mix (approx): 30% Easy / 50% Medium / 20% Hard, distributed throughout.

Includes 5 image/diagram-based questions (2 Biology, 1 Chemistry, 2 Physics).
Each such question has an "image" key giving a relative path to a PNG diagram
that must be viewed alongside the question (images/ subfolder, shipped alongside
this file). Diagrams: a labeled plasma-membrane cross-section, a labeled heart
cross-section identifying the tricuspid valve, a reaction energy-profile
diagram, a parallel-then-series resistor circuit, and a concave-mirror ray
diagram (object at C).

Each question is a dict:
    id, subject, topic, difficulty, question, [image], options (A-D), answer (correct letter)

Run this file directly to print a summary / sanity-check the paper.
"""

QUESTIONS = [

# ============================================================
# BIOLOGY (81) - id 1-81
# ============================================================

{"id":1,"subject":'Biology',"topic":'Biomolecules',"difficulty":'Easy',
 "question":'Which of the following is a simple sugar (monosaccharide)?',
 "options":{"A":'Fructose', "B":'Sucrose', "C":'Maltose', "D":'Starch'},"answer":'A'},

{"id":2,"subject":'Biology',"topic":'Biomolecules',"difficulty":'Easy',
 "question":'The monomers that make up nucleic acids, consisting of a sugar, phosphate, and nitrogenous base, are called:',
 "options":{"A":'Amino acids', "B":'Nucleotides', "C":'Fatty acids', "D":'Monosaccharides'},"answer":'B'},

{"id":3,"subject":'Biology',"topic":'Biomolecules',"difficulty":'Medium',
 "question":'Tertiary protein structure is stabilized by interactions between:',
 "options":{"A":'Adjacent amino acids in the primary sequence only', "B":'Two separate polypeptide chains', "C":'The side chains (R-groups) of amino acids, including hydrogen bonds, ionic bonds, and hydrophobic interactions', "D":'DNA and protein'},"answer":'C'},

{"id":4,"subject":'Biology',"topic":'Biomolecules',"difficulty":'Medium',
 "question":'A key function of phospholipids in a cell is to:',
 "options":{"A":'Store long-term energy exclusively', "B":'Carry genetic information', "C":'Catalyze biochemical reactions', "D":'Form the structural basis of cell membranes due to their amphipathic nature'},"answer":'D'},

{"id":5,"subject":'Biology',"topic":'Biomolecules',"difficulty":'Hard',
 "question":"The specific sequence of nucleotides in DNA ultimately determines an organism's traits because this sequence:",
 "options":{"A":'Codes for the specific amino acid sequences of proteins, which perform most cellular functions', "B":'Directly forms the physical structures of the body', "C":'Has no relationship to protein structure', "D":'Only affects the color of the organism'},"answer":'A'},

{"id":6,"subject":'Biology',"topic":'Enzymes',"difficulty":'Easy',
 "question":'Enzymes lower the activation energy of a reaction, which:',
 "options":{"A":'Makes the reaction less likely to occur', "B":'Increases the rate at which the reaction proceeds', "C":'Changes the products of the reaction', "D":'Has no effect on reaction rate'},"answer":'B'},

{"id":7,"subject":'Biology',"topic":'Enzymes',"difficulty":'Medium',
 "question":'Which statement about enzyme cofactors and coenzymes is correct?',
 "options":{"A":'Cofactors are always organic molecules while coenzymes are always inorganic', "B":'Coenzymes are never required for enzyme function', "C":'Cofactors can be either inorganic ions or organic molecules; coenzymes are a specific type of organic cofactor', "D":'Cofactors and coenzymes are identical terms with no distinction'},"answer":'C'},

{"id":8,"subject":'Biology',"topic":'Enzymes',"difficulty":'Medium',
 "question":'An enzyme that catalyzes the same type of reaction across many different substrates, but is optimized for one substrate in particular, demonstrates a degree of:',
 "options":{"A":'Absolute specificity only', "B":'Complete non-selectivity', "C":'No specificity at all', "D":'Relative specificity'},"answer":'D'},

{"id":9,"subject":'Biology',"topic":'Enzymes',"difficulty":'Hard',
 "question":'In allosteric enzyme regulation, binding of a regulatory molecule at a site distinct from the active site can:',
 "options":{"A":'Either activate or inhibit the enzyme, depending on the specific regulatory molecule', "B":'Only ever activate the enzyme', "C":'Have no effect on enzyme shape', "D":'Directly destroy the enzyme'},"answer":'A'},

{"id":10,"subject":'Biology',"topic":'Cell Biology',"difficulty":'Easy',
 "question":'The site of ATP production in a cell through aerobic respiration is the:',
 "options":{"A":'Nucleus', "B":'Mitochondrion', "C":'Ribosome', "D":'Golgi apparatus'},"answer":'B'},

{"id":11,"subject":'Biology',"topic":'Cell Biology',"difficulty":'Easy',
 "question":'Chloroplasts, found in plant cells, are the site of:',
 "options":{"A":'Cellular respiration', "B":'Protein synthesis exclusively', "C":'Photosynthesis', "D":'DNA replication only'},"answer":'C'},

{"id":12,"subject":'Biology',"topic":'Cell Biology',"difficulty":'Medium',
 "question":'The diagram shows a cross-section of the plasma membrane with structures labeled W, X, Y, and Z (the phospholipid bilayer, an integral protein spanning the membrane, a peripheral protein on the surface, and a cholesterol molecule embedded within the bilayer). Which labeled structure represents the integral membrane protein spanning the entire width of the membrane?',
 "image":'images/q_membrane_crosssection_diagram.png',
 "options":{"A":'Structure W', "B":'Structure Z', "C":'Structure Y', "D":'Structure X (the integral/transmembrane protein)'},"answer":'D'},

{"id":13,"subject":'Biology',"topic":'Cell Biology',"difficulty":'Medium',
 "question":'Which of the following best describes the function of vacuoles in plant cells?',
 "options":{"A":'They store water, ions, and waste products, and help maintain turgor pressure', "B":'They synthesize proteins', "C":'They produce ATP through respiration', "D":'They replicate DNA'},"answer":'A'},

{"id":14,"subject":'Biology',"topic":'Cell Biology',"difficulty":'Medium',
 "question":'Lysosomal enzymes function optimally in an acidic environment mainly to:',
 "options":{"A":'Match the pH of the cytoplasm exactly', "B":'Ensure the enzymes remain inactive if accidentally released into the more neutral cytoplasm, protecting the cell', "C":'Allow the enzymes to function outside the cell', "D":'Prevent the enzymes from ever being active'},"answer":'B'},

{"id":15,"subject":'Biology',"topic":'Cell Biology',"difficulty":'Medium',
 "question":'Which structure would be found in a prokaryotic cell but is generally absent from a eukaryotic cell in the same form?',
 "options":{"A":'Ribosomes', "B":'A plasma membrane', "C":'A single circular chromosome free in the cytoplasm, without a nuclear envelope', "D":'Cytoplasm'},"answer":'C'},

{"id":16,"subject":'Biology',"topic":'Cell Biology',"difficulty":'Hard',
 "question":'A cell biologist observes that a cell has an unusually extensive smooth endoplasmic reticulum. This cell is most likely specialized for:',
 "options":{"A":'Extensive protein secretion', "B":'Cellulose production', "C":'Photosynthesis', "D":'Lipid synthesis and/or detoxification of drugs and toxins'},"answer":'D'},

{"id":17,"subject":'Biology',"topic":'Cell Membrane & Transport',"difficulty":'Easy',
 "question":'The movement of molecules from an area of high concentration to low concentration is generally described as moving:',
 "options":{"A":'Down the concentration gradient', "B":'Against the concentration gradient', "C":'Perpendicular to the concentration gradient', "D":'In no particular direction relative to concentration'},"answer":'A'},

{"id":18,"subject":'Biology',"topic":'Cell Membrane & Transport',"difficulty":'Medium',
 "question":'Water potential is influenced by both solute concentration and:',
 "options":{"A":'Temperature exclusively', "B":'Pressure (pressure potential)', "C":'The color of the solution', "D":'The presence of enzymes'},"answer":'B'},

{"id":19,"subject":'Biology',"topic":'Cell Membrane & Transport',"difficulty":'Medium',
 "question":'Bulk transport processes, such as endocytosis and exocytosis, are used mainly for moving:',
 "options":{"A":'Small ions across the membrane', "B":'Only water molecules', "C":'Large molecules or particles that cannot cross via channels or carriers', "D":'Only gases'},"answer":'C'},

{"id":20,"subject":'Biology',"topic":'Cell Membrane & Transport',"difficulty":'Hard',
 "question":'A red blood cell placed in a solution of unknown tonicity swells slightly but does not burst, then reaches a stable size. This solution is most likely:',
 "options":{"A":'Strongly hypertonic', "B":'Exactly isotonic', "C":'Strongly hypotonic', "D":'Mildly hypotonic'},"answer":'D'},

{"id":21,"subject":'Biology',"topic":'Cell Membrane & Transport',"difficulty":'Easy',
 "question":'Facilitated diffusion is similar to simple diffusion in that both processes:',
 "options":{"A":'Move substances down their concentration gradient', "B":'Require ATP', "C":'Require a carrier protein', "D":'Move substances against their concentration gradient'},"answer":'A'},

{"id":22,"subject":'Biology',"topic":'Cell Cycle & Division',"difficulty":'Easy',
 "question":'DNA replication must be completed before a cell can proceed to:',
 "options":{"A":'G1 phase', "B":'Mitosis (M phase)', "C":'The resting G0 phase', "D":'Fertilization'},"answer":'B'},

{"id":23,"subject":'Biology',"topic":'Cell Cycle & Division',"difficulty":'Easy',
 "question":'The stage of mitosis characterized by the alignment of chromosomes along the metaphase plate is:',
 "options":{"A":'Prophase', "B":'Anaphase', "C":'Metaphase', "D":'Telophase'},"answer":'C'},

{"id":24,"subject":'Biology',"topic":'Cell Cycle & Division',"difficulty":'Medium',
 "question":'The primary genetic consequence of meiosis, compared to mitosis, is:',
 "options":{"A":'Identical daughter cells with the same chromosome number as the parent', "B":'Formation of only diploid cells', "C":'No change in chromosome number', "D":'Genetically varied haploid cells, due to crossing over and independent assortment'},"answer":'D'},

{"id":25,"subject":'Biology',"topic":'Cell Cycle & Division',"difficulty":'Medium',
 "question":'A diploid cell begins meiosis with 2n = 16 chromosomes. How many chromosomes are present in each cell after meiosis II is complete?',
 "options":{"A":'8', "B":'16', "C":'32', "D":'4'},"answer":'A'},

{"id":26,"subject":'Biology',"topic":'Cell Cycle & Division',"difficulty":'Hard',
 "question":'The restriction point (R point) in the G1 phase of the mammalian cell cycle serves to:',
 "options":{"A":'Ensure DNA has been replicated correctly', "B":'Determine whether the cell has adequate resources and signals to commit to dividing', "C":'Check for proper chromosome attachment to the spindle', "D":'Trigger cytokinesis'},"answer":'B'},

{"id":27,"subject":'Biology',"topic":'Cell Cycle & Division',"difficulty":'Medium',
 "question":'Uncontrolled cellular proliferation, often resulting from mutations affecting cell cycle checkpoints, characterizes:',
 "options":{"A":'Normal tissue repair', "B":'Apoptosis', "C":'Cancer', "D":'Meiosis'},"answer":'C'},

{"id":28,"subject":'Biology',"topic":'Genetics',"difficulty":'Easy',
 "question":'In pea plants, yellow seed color (Y) is dominant over green (y). A cross between two heterozygous plants (Yy x Yy) produces offspring in what phenotypic ratio?',
 "options":{"A":'All yellow', "B":'All green', "C":'1 yellow : 1 green', "D":'3 yellow : 1 green'},"answer":'D'},

{"id":29,"subject":'Biology',"topic":'Genetics',"difficulty":'Medium',
 "question":'A cross between a homozygous dominant plant (YY) and a heterozygous plant (Yy) produces offspring with what expected phenotype distribution?',
 "options":{"A":'All yellow', "B":'All green', "C":'1 yellow : 1 green', "D":'3 yellow : 1 green'},"answer":'A'},

{"id":30,"subject":'Biology',"topic":'Genetics',"difficulty":'Medium',
 "question":'A disorder is inherited in an X-linked recessive pattern. A carrier mother and an affected father have children. What proportion of daughters is expected to be affected?',
 "options":{"A":'0%', "B":'50%', "C":'25%', "D":'100%'},"answer":'B'},

{"id":31,"subject":'Biology',"topic":'Genetics',"difficulty":'Hard',
 "question":'In a trihybrid cross AaBbCc x aabbcc (a complete test cross), what fraction of offspring is expected to show the recessive phenotype for all three traits?',
 "options":{"A":'1/64', "B":'1/16', "C":'1/8', "D":'1/4'},"answer":'C'},

{"id":32,"subject":'Biology',"topic":'Genetics',"difficulty":'Medium',
 "question":'A father with blood type A (heterozygous, IAi) and a mother with blood type A (heterozygous, IAi) have children. What is the probability a child will have blood type O?',
 "options":{"A":'0%', "B":'100%', "C":'50%', "D":'25%'},"answer":'D'},

{"id":33,"subject":'Biology',"topic":'Genetics',"difficulty":'Hard',
 "question":'A genetic disorder appears in every generation of a family, with affected individuals always having at least one affected parent, and males and females are affected in roughly equal numbers. This pattern is most consistent with:',
 "options":{"A":'Autosomal dominant inheritance', "B":'Autosomal recessive inheritance', "C":'X-linked recessive inheritance', "D":'Mitochondrial inheritance'},"answer":'A'},

{"id":34,"subject":'Biology',"topic":'Genetics',"difficulty":'Medium',
 "question":"In certain cattle, crossing a red-coated (RR) bull with a white-coated (WW) cow produces offspring with a 'roan' coat consisting of both red and white hairs intermixed, rather than pink coloring. This pattern is best described as:",
 "options":{"A":'Incomplete dominance', "B":'Codominance', "C":'Epistasis', "D":'Complete dominance'},"answer":'B'},

{"id":35,"subject":'Biology',"topic":'Molecular Biology',"difficulty":'Easy',
 "question":'DNA is composed of two strands twisted into a:',
 "options":{"A":'Single helix', "B":'Triple helix', "C":'Double helix', "D":'Flat ladder shape'},"answer":'C'},

{"id":36,"subject":'Biology',"topic":'Molecular Biology',"difficulty":'Easy',
 "question":'The sugar found in DNA nucleotides is:',
 "options":{"A":'Ribose', "B":'Fructose', "C":'Glucose', "D":'Deoxyribose'},"answer":'D'},

{"id":37,"subject":'Biology',"topic":'Molecular Biology',"difficulty":'Medium',
 "question":'RNA polymerase, unlike DNA polymerase, does not require:',
 "options":{"A":'A primer to begin synthesis', "B":'A DNA template', "C":'Nucleotides', "D":'Energy'},"answer":'A'},

{"id":38,"subject":'Biology',"topic":'Molecular Biology',"difficulty":'Medium',
 "question":'The process by which a pre-mRNA molecule is modified by removing introns and joining exons together is called:',
 "options":{"A":'Transcription', "B":'Splicing', "C":'Translation', "D":'Replication'},"answer":'B'},

{"id":39,"subject":'Biology',"topic":'Molecular Biology',"difficulty":'Medium',
 "question":"A mutation that adds a stop codon prematurely within a gene's coding sequence, truncating the resulting protein, is called a:",
 "options":{"A":'Silent mutation', "B":'Missense mutation', "C":'Nonsense mutation', "D":'Frameshift mutation caused by substitution'},"answer":'C'},

{"id":40,"subject":'Biology',"topic":'Molecular Biology',"difficulty":'Hard',
 "question":"Which of the following mutations would most likely have the LEAST impact on a protein's overall function?",
 "options":{"A":'A nonsense mutation near the beginning of the gene', "B":'A frameshift mutation near the beginning of the gene', "C":'A large deletion spanning most of the gene', "D":'A silent mutation'},"answer":'D'},

{"id":41,"subject":'Biology',"topic":'Molecular Biology',"difficulty":'Hard',
 "question":'A bacteriophage injecting its DNA into a bacterial cell and using the bacterial machinery to replicate is an example of:',
 "options":{"A":'Viral infection and replication', "B":'Transformation', "C":'Conjugation', "D":'Binary fission'},"answer":'A'},

{"id":42,"subject":'Biology',"topic":'Molecular Biology',"difficulty":'Medium',
 "question":'Which of the following enzymes synthesizes the RNA primer needed to initiate DNA replication?',
 "options":{"A":'DNA polymerase', "B":'Primase', "C":'Ligase', "D":'Topoisomerase'},"answer":'B'},

{"id":43,"subject":'Biology',"topic":'Molecular Biology',"difficulty":'Medium',
 "question":'A cis-regulatory element located directly adjacent to a gene, providing a binding site for RNA polymerase, is the:',
 "options":{"A":'Enhancer', "B":'Terminator', "C":'Promoter', "D":'Intron'},"answer":'C'},

{"id":44,"subject":'Biology',"topic":'Molecular Biology',"difficulty":'Easy',
 "question":'The number of possible codons, given four different nucleotide bases arranged in groups of three, is:',
 "options":{"A":'4', "B":'16', "C":'256', "D":'64'},"answer":'D'},

{"id":45,"subject":'Biology',"topic":'Evolution',"difficulty":'Easy',
 "question":'Adaptations are inherited traits that:',
 "options":{"A":"Increase an organism's fitness in its environment, improving survival and/or reproduction", "B":"Decrease an organism's chance of survival", "C":'Have no effect on survival or reproduction', "D":"Are acquired during an organism's lifetime and then inherited"},"answer":'A'},

{"id":46,"subject":'Biology',"topic":'Evolution',"difficulty":'Medium',
 "question":'Which of the following best illustrates directional selection?',
 "options":{"A":'Extreme phenotypes on both ends of a distribution are favored equally', "B":"One extreme phenotype is consistently favored, shifting the population's average trait value over generations", "C":'The average phenotype in a population is favored over both extremes', "D":'All phenotypes are equally favored regardless of extremity'},"answer":'B'},

{"id":47,"subject":'Biology',"topic":'Evolution',"difficulty":'Medium',
 "question":'Adaptive radiation refers to:',
 "options":{"A":'The extinction of a single widespread species', "B":'The complete stagnation of species over time', "C":'The relatively rapid diversification of a single ancestral species into many new species, each adapted to a different ecological niche', "D":'The merging of multiple species into one'},"answer":'C'},

{"id":48,"subject":'Biology',"topic":'Evolution',"difficulty":'Hard',
 "question":'In a population, 84% of individuals display the dominant phenotype for a trait controlled by one gene with two alleles. Assuming Hardy-Weinberg equilibrium, what is the frequency of the dominant allele (p)?',
 "options":{"A":'0.4', "B":'0.16', "C":'0.84', "D":'0.6'},"answer":'D'},

{"id":49,"subject":'Biology',"topic":'Classification & Diversity',"difficulty":'Easy',
 "question":'The scientific classification system organizes living things into a hierarchy of nested categories, from broad to specific, primarily to:',
 "options":{"A":'Reflect evolutionary relationships and organize the diversity of life in a systematic way', "B":'Make memorization more difficult', "C":'Randomly group unrelated organisms', "D":'Eliminate the need for further study'},"answer":'A'},

{"id":50,"subject":'Biology',"topic":'Classification & Diversity',"difficulty":'Easy',
 "question":'Kingdom Plantae is characterized by organisms that are:',
 "options":{"A":'Heterotrophic and lack cell walls', "B":'Multicellular, photosynthetic autotrophs with cellulose cell walls', "C":'Unicellular and prokaryotic', "D":'Decomposers lacking chlorophyll'},"answer":'B'},

{"id":51,"subject":'Biology',"topic":'Classification & Diversity',"difficulty":'Medium',
 "question":'The domain Eukarya includes which of the following kingdoms?',
 "options":{"A":'Only Animalia', "B":'Only Monera', "C":'Protista, Fungi, Plantae, and Animalia', "D":'Only Protista'},"answer":'C'},

{"id":52,"subject":'Biology',"topic":'Classification & Diversity',"difficulty":'Medium',
 "question":'An organism characterized by a soft body, a muscular foot, and (in many species) a hard calcium carbonate shell most likely belongs to phylum:',
 "options":{"A":'Porifera', "B":'Arthropoda', "C":'Cnidaria', "D":'Mollusca'},"answer":'D'},

{"id":53,"subject":'Biology',"topic":'Classification & Diversity',"difficulty":'Easy',
 "question":'Which taxonomic rank sits directly below Kingdom and above Class?',
 "options":{"A":'Phylum', "B":'Order', "C":'Family', "D":'Genus'},"answer":'A'},

{"id":54,"subject":'Biology',"topic":'Classification & Diversity',"difficulty":'Medium',
 "question":'Members of class Reptilia are characterized by having:',
 "options":{"A":'Feathers and warm-bloodedness', "B":'Dry, scaly skin, amniotic eggs, and ectothermy (cold-bloodedness)', "C":'Gills and an aquatic-only lifestyle', "D":'Mammary glands'},"answer":'B'},

{"id":55,"subject":'Biology',"topic":'Plant Biology',"difficulty":'Easy',
 "question":'The tissue responsible for transporting sugars produced during photosynthesis to other parts of the plant is:',
 "options":{"A":'Xylem', "B":'Epidermis', "C":'Phloem', "D":'Cork cambium'},"answer":'C'},

{"id":56,"subject":'Biology',"topic":'Plant Biology',"difficulty":'Medium',
 "question":'The Calvin cycle uses ATP and NADPH from the light reactions to fix carbon dioxide into:',
 "options":{"A":'Oxygen gas', "B":'Nitrogen compounds', "C":'Water', "D":'Organic sugar molecules (such as G3P, which can form glucose)'},"answer":'D'},

{"id":57,"subject":'Biology',"topic":'Plant Biology',"difficulty":'Medium',
 "question":"A plant's response to gravity, causing roots to grow downward and shoots to grow upward, is called:",
 "options":{"A":'Gravitropism (geotropism)', "B":'Phototropism', "C":'Thigmotropism', "D":'Hydrotropism'},"answer":'A'},

{"id":58,"subject":'Biology',"topic":'Plant Biology',"difficulty":'Hard',
 "question":'Nitrogen-fixing bacteria living in root nodules of legume plants provide a mutual benefit because they:',
 "options":{"A":'Only harm the plant by consuming its nutrients', "B":'Convert atmospheric nitrogen gas into a usable form (such as ammonia) for the plant, while receiving carbohydrates from the plant', "C":'Convert sunlight into chemical energy for the plant', "D":'Have no functional relationship with the plant'},"answer":'B'},

{"id":59,"subject":'Biology',"topic":'Plant Biology',"difficulty":'Medium',
 "question":'Ethylene, a gaseous plant hormone, is primarily responsible for:',
 "options":{"A":'Stem elongation', "B":'Root hair formation', "C":'Fruit ripening and leaf abscission', "D":'Seed dormancy maintenance'},"answer":'C'},

{"id":60,"subject":'Biology',"topic":'Plant Biology',"difficulty":'Easy',
 "question":'The structure of a flower that receives pollen and allows pollen tube growth toward the ovary is the:',
 "options":{"A":'Anther', "B":'Filament', "C":'Sepal', "D":'Stigma'},"answer":'D'},

{"id":61,"subject":'Biology',"topic":'Human Physiology - Digestion',"difficulty":'Easy',
 "question":'Mechanical digestion of food, including chewing, begins in the:',
 "options":{"A":'Mouth', "B":'Stomach', "C":'Small intestine', "D":'Esophagus'},"answer":'A'},

{"id":62,"subject":'Biology',"topic":'Human Physiology - Digestion',"difficulty":'Medium',
 "question":'Gastric juice, secreted by the stomach lining, contains hydrochloric acid and the enzyme:',
 "options":{"A":'Amylase', "B":'Pepsin', "C":'Lipase', "D":'Trypsin'},"answer":'B'},

{"id":63,"subject":'Biology',"topic":'Human Physiology - Digestion',"difficulty":'Medium',
 "question":'The primary role of the gallbladder in digestion is to:',
 "options":{"A":'Produce bile', "B":'Digest fats directly', "C":'Store and concentrate bile before its release into the small intestine', "D":'Absorb nutrients'},"answer":'C'},

{"id":64,"subject":'Biology',"topic":'Human Physiology - Digestion',"difficulty":'Hard',
 "question":'A person whose stomach fails to produce sufficient hydrochloric acid would most likely experience impaired:',
 "options":{"A":'Peristalsis in the esophagus', "B":'Absorption of water in the large intestine', "C":'Bile production by the liver', "D":'Activation of pepsinogen into pepsin, reducing protein digestion'},"answer":'D'},

{"id":65,"subject":'Biology',"topic":'Human Physiology - Circulation',"difficulty":'Easy',
 "question":'The diagram shows a cross-section of the heart with valves labeled 1-4. Which labeled valve is located between the right atrium and the right ventricle?',
 "image":'images/q_heart_tricuspid_valve_diagram.png',
 "options":{"A":'Valve 1 (tricuspid valve)', "B":'Valve 2 (bicuspid/mitral valve)', "C":'Valve 3 (aortic valve)', "D":'Valve 4 (pulmonary valve)'},"answer":'A'},

{"id":66,"subject":'Biology',"topic":'Human Physiology - Circulation',"difficulty":'Medium',
 "question":'Systemic circulation refers to the pathway of blood:',
 "options":{"A":'Between the heart and the lungs', "B":'Between the heart and the rest of the body (excluding the lungs)', "C":'Only within the heart itself', "D":'Only within the brain'},"answer":'B'},

{"id":67,"subject":'Biology',"topic":'Human Physiology - Circulation',"difficulty":'Medium',
 "question":'Anemia, a condition characterized by a reduced ability of the blood to carry oxygen, is often caused by:',
 "options":{"A":'An excess of red blood cells', "B":'An excess of platelets', "C":'A deficiency in red blood cells or hemoglobin', "D":'A deficiency in white blood cells only'},"answer":'C'},

{"id":68,"subject":'Biology',"topic":'Human Physiology - Circulation',"difficulty":'Hard',
 "question":'During exercise, blood flow to skeletal muscles increases mainly due to:',
 "options":{"A":'Vasoconstriction of blood vessels supplying the muscles', "B":'A decrease in heart rate', "C":'Complete cessation of blood flow to the muscles', "D":'Vasodilation of blood vessels supplying the muscles, increasing blood flow to meet higher oxygen demand'},"answer":'D'},

{"id":69,"subject":'Biology',"topic":'Human Physiology - Respiration',"difficulty":'Easy',
 "question":'The primary muscle responsible for changing the volume of the thoracic cavity during breathing is the:',
 "options":{"A":'Diaphragm', "B":'Bicep', "C":'Trapezius', "D":'Cardiac muscle'},"answer":'A'},

{"id":70,"subject":'Biology',"topic":'Human Physiology - Respiration',"difficulty":'Medium',
 "question":'The partial pressure of oxygen is higher in the alveoli than in the pulmonary capillary blood, causing oxygen to:',
 "options":{"A":'Diffuse from the blood into the alveoli', "B":'Diffuse from the alveoli into the blood', "C":'Remain unchanged between the two', "D":'Be actively transported using ATP'},"answer":'B'},

{"id":71,"subject":'Biology',"topic":'Human Physiology - Respiration',"difficulty":'Medium',
 "question":'Chronic obstructive pulmonary disease (COPD), often caused by long-term smoking, typically results in:',
 "options":{"A":'Improved lung elasticity and airflow', "B":'No change in respiratory function', "C":'Damage to lung tissue and airways, reducing airflow and gas exchange efficiency', "D":'Enhanced oxygen absorption'},"answer":'C'},

{"id":72,"subject":'Biology',"topic":'Human Physiology - Excretion',"difficulty":'Easy',
 "question":"The kidney's basic structural and functional unit, responsible for filtering blood and forming urine, is the:",
 "options":{"A":'Villus', "B":'Neuron', "C":'Alveolus', "D":'Nephron'},"answer":'D'},

{"id":73,"subject":'Biology',"topic":'Human Physiology - Excretion',"difficulty":'Medium',
 "question":'Glucose is normally completely reabsorbed from the filtrate back into the blood in the:',
 "options":{"A":'Proximal convoluted tubule', "B":'Loop of Henle', "C":'Collecting duct', "D":'Ureter'},"answer":'A'},

{"id":74,"subject":'Biology',"topic":'Human Physiology - Excretion',"difficulty":'Hard',
 "question":'In uncontrolled diabetes mellitus, glucose appears in the urine mainly because:',
 "options":{"A":'The kidneys intentionally excrete excess glucose as a protective mechanism', "B":'Blood glucose levels exceed the renal threshold, overwhelming the transporters responsible for glucose reabsorption', "C":'The kidneys stop filtering blood entirely', "D":'Insulin causes glucose to be actively secreted into urine'},"answer":'B'},

{"id":75,"subject":'Biology',"topic":'Human Physiology - Nervous & Endocrine',"difficulty":'Easy',
 "question":'The basic functional unit of the nervous system, responsible for transmitting electrical and chemical signals, is the:',
 "options":{"A":'Nephron', "B":'Osteocyte', "C":'Neuron', "D":'Erythrocyte'},"answer":'C'},

{"id":76,"subject":'Biology',"topic":'Human Physiology - Nervous & Endocrine',"difficulty":'Medium',
 "question":'The synaptic cleft is the small gap between:',
 "options":{"A":'The brain and spinal cord', "B":'The nucleus and cytoplasm of a neuron', "C":'Two adjacent muscle fibers only', "D":'Two adjacent neurons, across which neurotransmitters diffuse'},"answer":'D'},

{"id":77,"subject":'Biology',"topic":'Human Physiology - Nervous & Endocrine',"difficulty":'Medium',
 "question":'The pancreas functions as both an exocrine and endocrine gland; its endocrine function includes secreting:',
 "options":{"A":'Insulin and glucagon directly into the bloodstream', "B":'Digestive enzymes into the small intestine', "C":'Bile into the gallbladder', "D":'Hydrochloric acid into the stomach'},"answer":'A'},

{"id":78,"subject":'Biology',"topic":'Human Physiology - Nervous & Endocrine',"difficulty":'Hard',
 "question":'Damage to the hypothalamus, which links the nervous and endocrine systems, could disrupt:',
 "options":{"A":'Vision processing only', "B":"Regulation of body temperature, hunger, thirst, and control of the pituitary gland's hormone release", "C":'Hearing only', "D":'Voluntary muscle movement exclusively'},"answer":'B'},

{"id":79,"subject":'Biology',"topic":'Human Physiology - Reproduction',"difficulty":'Easy',
 "question":'The structure in males where sperm mature and are stored before ejaculation is the:',
 "options":{"A":'Seminiferous tubules', "B":'Vas deferens', "C":'Epididymis', "D":'Prostate gland'},"answer":'C'},

{"id":80,"subject":'Biology',"topic":'Human Physiology - Reproduction',"difficulty":'Medium',
 "question":'A surge in luteinizing hormone (LH) at approximately the midpoint of the menstrual cycle directly triggers:',
 "options":{"A":'Menstruation', "B":'The onset of puberty', "C":'Implantation', "D":'Ovulation, the release of a mature egg from the ovary'},"answer":'D'},

{"id":81,"subject":'Biology',"topic":'Ecology',"difficulty":'Medium',
 "question":'The total amount of chemical energy produced by primary producers in an ecosystem, minus the energy they use in respiration, is called:',
 "options":{"A":'Net primary productivity', "B":'Gross primary productivity', "C":'Secondary productivity', "D":'Biomass'},"answer":'A'},

# ============================================================
# CHEMISTRY (45) - id 82-126
# ============================================================

{"id":82,"subject":'Chemistry',"topic":'Atomic Structure',"difficulty":'Easy',
 "question":'Protons and neutrons are located in which part of the atom?',
 "options":{"A":'The electron cloud', "B":'The nucleus', "C":'The valence shell', "D":'Outside the atom entirely'},"answer":'B'},

{"id":83,"subject":'Chemistry',"topic":'Atomic Structure',"difficulty":'Medium',
 "question":'An atom of iron-56 (atomic number 26) contains how many neutrons?',
 "options":{"A":'26', "B":'56', "C":'30', "D":'82'},"answer":'C'},

{"id":84,"subject":'Chemistry',"topic":'Atomic Structure',"difficulty":'Medium',
 "question":'The electron configuration of a neutral aluminum atom (Z = 13) is:',
 "options":{"A":'1s2 2s2 2p6 3s2 3p2', "B":'1s2 2s2 2p6 3s1 3p2', "C":'1s2 2s2 2p5 3s2 3p2', "D":'1s2 2s2 2p6 3s2 3p1'},"answer":'D'},

{"id":85,"subject":'Chemistry',"topic":'Atomic Structure',"difficulty":'Hard',
 "question":'An ion has 34 protons and 36 electrons. What is its charge?',
 "options":{"A":'-2', "B":'+2', "C":'+34', "D":'-36'},"answer":'A'},

{"id":86,"subject":'Chemistry',"topic":'Periodic Table',"difficulty":'Easy',
 "question":'The horizontal rows of the periodic table are called:',
 "options":{"A":'Groups', "B":'Periods', "C":'Families', "D":'Blocks'},"answer":'B'},

{"id":87,"subject":'Chemistry',"topic":'Periodic Table',"difficulty":'Medium',
 "question":'Which of the following correctly describes the general trend in nonmetallic character across a period, from left to right?',
 "options":{"A":'Nonmetallic character generally decreases', "B":'Nonmetallic character remains constant', "C":'Nonmetallic character generally increases', "D":'Nonmetallic character becomes negative'},"answer":'C'},

{"id":88,"subject":'Chemistry',"topic":'Periodic Table',"difficulty":'Medium',
 "question":'An element with low ionization energy and a strong tendency to lose one electron easily would most likely be located:',
 "options":{"A":'On the far right of the periodic table', "B":'In the middle of the transition metals', "C":'Among the noble gases', "D":'In Group 1, on the far left of the periodic table'},"answer":'D'},

{"id":89,"subject":'Chemistry',"topic":'Chemical Bonding',"difficulty":'Easy',
 "question":'The attraction between oppositely charged ions in a crystal lattice is characteristic of a(n):',
 "options":{"A":'Ionic bond', "B":'Covalent bond', "C":'Metallic bond', "D":'Hydrogen bond'},"answer":'A'},

{"id":90,"subject":'Chemistry',"topic":'Chemical Bonding',"difficulty":'Medium',
 "question":'According to VSEPR theory, a molecule with four bonding pairs and no lone pairs on a central atom has a bond angle of approximately:',
 "options":{"A":'90 degrees', "B":'109.5 degrees', "C":'120 degrees', "D":'180 degrees'},"answer":'B'},

{"id":91,"subject":'Chemistry',"topic":'Chemical Bonding',"difficulty":'Medium',
 "question":'Carbon tetrachloride (CCl4) is nonpolar overall, despite having polar C-Cl bonds, mainly because:',
 "options":{"A":'Chlorine and carbon have identical electronegativities', "B":'It contains no polar bonds at all', "C":'Its symmetrical tetrahedral geometry causes the bond dipoles to cancel out', "D":'It has a lone pair on carbon'},"answer":'C'},

{"id":92,"subject":'Chemistry',"topic":'Chemical Bonding',"difficulty":'Hard',
 "question":'Network covalent solids, such as diamond and quartz, tend to have extremely high melting points mainly because:',
 "options":{"A":'They are held together by weak intermolecular forces only', "B":'They have very low densities', "C":'They contain ionic bonds exclusively', "D":'Every atom is covalently bonded to several neighboring atoms in a continuous three-dimensional network'},"answer":'D'},

{"id":93,"subject":'Chemistry',"topic":'States of Matter',"difficulty":'Easy',
 "question":'Which state of matter has a definite volume but takes the shape of its container?',
 "options":{"A":'Liquid', "B":'Solid', "C":'Gas', "D":'Plasma'},"answer":'A'},

{"id":94,"subject":'Chemistry',"topic":'States of Matter',"difficulty":'Medium',
 "question":'A gas occupies 6.0 L at a pressure of 3.0 atm. What volume will it occupy at 2.0 atm, assuming constant temperature?',
 "options":{"A":'4.0 L', "B":'9.0 L', "C":'6.0 L', "D":'2.0 L'},"answer":'B'},

{"id":95,"subject":'Chemistry',"topic":'States of Matter',"difficulty":'Hard',
 "question":'A gas sample has a volume of 4 L at 27 degrees C (300 K) and 1 atm. What volume will it occupy at 127 degrees C (400 K) and 2 atm?',
 "options":{"A":'8 L', "B":'5.33 L', "C":'2.67 L', "D":'3 L'},"answer":'C'},

{"id":96,"subject":'Chemistry',"topic":'Stoichiometry',"difficulty":'Easy',
 "question":'The molar mass of sodium chloride (NaCl) is approximately:',
 "options":{"A":'23 g/mol', "B":'35.5 g/mol', "C":'40 g/mol', "D":'58.5 g/mol'},"answer":'D'},

{"id":97,"subject":'Chemistry',"topic":'Stoichiometry',"difficulty":'Medium',
 "question":'How many moles of oxygen atoms are present in 2 moles of Ca(NO3)2?',
 "options":{"A":'12', "B":'6', "C":'2', "D":'4'},"answer":'A'},

{"id":98,"subject":'Chemistry',"topic":'Stoichiometry',"difficulty":'Hard',
 "question":'A 300 mL solution contains 0.6 mole of HCl. What is the molarity of this solution?',
 "options":{"A":'0.2 M', "B":'2.0 M', "C":'0.5 M', "D":'1.8 M'},"answer":'B'},

{"id":99,"subject":'Chemistry',"topic":'Stoichiometry',"difficulty":'Medium',
 "question":'In the reaction N2 + 3H2 -> 2NH3, how many moles of H2 are required to react completely with 5 moles of N2?',
 "options":{"A":'5', "B":'10', "C":'15', "D":'20'},"answer":'C'},

{"id":100,"subject":'Chemistry',"topic":'Thermochemistry',"difficulty":'Easy',
 "question":'The graph shows the energy profile of a chemical reaction, plotting potential energy against reaction progress, with the activation energy (Ea) and overall energy change (delta H) both marked. Since the products have lower energy than the reactants in this diagram, the reaction shown is:',
 "image":'images/q_energy_profile_diagram.png',
 "options":{"A":'Endothermic', "B":'Non-spontaneous', "C":'At equilibrium', "D":'Exothermic'},"answer":'D'},

{"id":101,"subject":'Chemistry',"topic":'Thermochemistry',"difficulty":'Medium',
 "question":"Hess's law is useful for calculating the enthalpy change of a reaction that:",
 "options":{"A":'Cannot be measured directly, by adding the enthalpy changes of a series of other reactions', "B":'Has already been measured directly with no need for further calculation', "C":'Always has zero enthalpy change', "D":'Occurs only in living organisms'},"answer":'A'},

{"id":102,"subject":'Chemistry',"topic":'Chemical Equilibrium',"difficulty":'Medium',
 "question":'For the reaction 4NH3(g) + 5O2(g) <-> 4NO(g) + 6H2O(g), increasing the pressure by decreasing volume will shift the equilibrium:',
 "options":{"A":'Toward the products, the side with more moles of gas (10 moles)', "B":'Toward the reactants, the side with fewer moles of gas (9 moles)', "C":'Not at all', "D":'Completely to the products'},"answer":'B'},

{"id":103,"subject":'Chemistry',"topic":'Chemical Equilibrium',"difficulty":'Hard',
 "question":'If the temperature of an exothermic reaction at equilibrium is decreased, the equilibrium will shift:',
 "options":{"A":'Toward the reactants, decreasing yield', "B":'Not at all', "C":'Toward the products, increasing yield, since the system responds to counteract the temperature decrease by releasing more heat', "D":'The reaction stops completely'},"answer":'C'},

{"id":104,"subject":'Chemistry',"topic":'Reaction Kinetics',"difficulty":'Easy',
 "question":'An increase in the concentration of reactants generally results in:',
 "options":{"A":'A decreased reaction rate', "B":"A change in the reaction's products", "C":'No change in reaction rate', "D":'An increased reaction rate, due to more frequent collisions'},"answer":'D'},

{"id":105,"subject":'Chemistry',"topic":'Reaction Kinetics',"difficulty":'Medium',
 "question":'A catalyst increases reaction rate without altering the equilibrium position because it:',
 "options":{"A":'Speeds up both the forward and reverse reactions equally', "B":'Only speeds up the forward reaction', "C":'Only speeds up the reverse reaction', "D":"Changes the reaction's overall enthalpy"},"answer":'A'},

{"id":106,"subject":'Chemistry',"topic":'Electrochemistry',"difficulty":'Medium',
 "question":'In an electrochemical cell, reduction always occurs at the:',
 "options":{"A":'Anode', "B":'Cathode', "C":'Salt bridge', "D":'External wire'},"answer":'B'},

{"id":107,"subject":'Chemistry',"topic":'Electrochemistry',"difficulty":'Hard',
 "question":'In the reaction Mg(s) + Zn2+(aq) -> Mg2+(aq) + Zn(s), magnesium is:',
 "options":{"A":'Reduced', "B":'Unchanged', "C":'Oxidized', "D":'Acting as a catalyst'},"answer":'C'},

{"id":108,"subject":'Chemistry',"topic":'Acids & Bases',"difficulty":'Easy',
 "question":'A solution with a pH of 12 is:',
 "options":{"A":'Strongly acidic', "B":'Weakly acidic', "C":'Neutral', "D":'Strongly basic'},"answer":'D'},

{"id":109,"subject":'Chemistry',"topic":'Acids & Bases',"difficulty":'Medium',
 "question":'A solution has a hydrogen ion concentration of 1x10^-8 M. What is its pH?',
 "options":{"A":'8', "B":'6', "C":'-8', "D":'1x10^8'},"answer":'A'},

{"id":110,"subject":'Chemistry',"topic":'Acids & Bases',"difficulty":'Medium',
 "question":'According to the Arrhenius theory, an acid is a substance that:',
 "options":{"A":'Releases hydroxide ions in water', "B":'Releases hydrogen ions (H+) in water', "C":'Accepts a pair of electrons', "D":'Donates a pair of electrons'},"answer":'B'},

{"id":111,"subject":'Chemistry',"topic":'Acids & Bases',"difficulty":'Hard',
 "question":'A buffer solution is prepared using acetic acid and sodium acetate. If a small amount of strong base is added, the acetic acid component of the buffer will:',
 "options":{"A":'Convert entirely into sodium acetate immediately, causing a large pH spike', "B":'Have no effect on the added base', "C":'React with and neutralize the added base, minimizing the pH change', "D":'Cause the pH to decrease sharply'},"answer":'C'},

{"id":112,"subject":'Chemistry',"topic":'Organic Chemistry',"difficulty":'Easy',
 "question":'The functional group -COOH characterizes which class of organic compounds?',
 "options":{"A":'Aldehydes', "B":'Alcohols', "C":'Ethers', "D":'Carboxylic acids'},"answer":'D'},

{"id":113,"subject":'Chemistry',"topic":'Organic Chemistry',"difficulty":'Medium',
 "question":'Which type of reaction is typical of alkenes, involving the breaking of the pi bond to add new atoms across the double bond?',
 "options":{"A":'Addition reaction', "B":'Substitution reaction', "C":'Elimination reaction', "D":'Condensation reaction'},"answer":'A'},

{"id":114,"subject":'Chemistry',"topic":'Organic Chemistry',"difficulty":'Medium',
 "question":'A primary alcohol is one in which the carbon bearing the -OH group is bonded to how many other carbon atoms?',
 "options":{"A":'Zero', "B":'One', "C":'Two', "D":'Three'},"answer":'B'},

{"id":115,"subject":'Chemistry',"topic":'Organic Chemistry',"difficulty":'Hard',
 "question":'Which of the following best describes an E2 elimination reaction?',
 "options":{"A":'A reaction that only adds atoms to a molecule', "B":'A two-step reaction involving a stable carbocation intermediate', "C":'A one-step reaction where a base removes a proton and a leaving group departs simultaneously, forming a double bond', "D":'A reaction that occurs only in the absence of any base'},"answer":'C'},

{"id":116,"subject":'Chemistry',"topic":'Organic Chemistry',"difficulty":'Medium',
 "question":'Polypeptides are formed through condensation polymerization of amino acids, releasing which byproduct?',
 "options":{"A":'Carbon dioxide', "B":'Hydrogen gas', "C":'Ammonia', "D":'Water'},"answer":'D'},

{"id":117,"subject":'Chemistry',"topic":'Organic Chemistry',"difficulty":'Easy',
 "question":'The functional group C=O situated at the end of a carbon chain (bonded to at least one hydrogen) characterizes:',
 "options":{"A":'An aldehyde', "B":'A ketone', "C":'A carboxylic acid', "D":'An ether'},"answer":'A'},

{"id":118,"subject":'Chemistry',"topic":'Inorganic Chemistry',"difficulty":'Medium',
 "question":'Which of the following best explains the general unreactivity of Group 18 elements (noble gases)?',
 "options":{"A":'They have very small atomic radii', "B":'Their complete outer electron shell provides high stability, making them reluctant to gain, lose, or share electrons', "C":'They have very low nuclear charge', "D":'They readily form multiple types of bonds'},"answer":'B'},

{"id":119,"subject":'Chemistry',"topic":'Inorganic Chemistry',"difficulty":'Medium',
 "question":'Alkaline earth metals (Group 2) generally react with water:',
 "options":{"A":'More vigorously than alkali metals (Group 1) of the same period', "B":'Not at all, under any circumstances', "C":'Less vigorously than alkali metals (Group 1) of the same period, due to their higher ionization energy', "D":'Only when exposed to extreme cold'},"answer":'C'},

{"id":120,"subject":'Chemistry',"topic":'Inorganic Chemistry',"difficulty":'Hard',
 "question":"In the reaction 2CuO + C -> 2Cu + CO2, copper's oxidation state changes from:",
 "options":{"A":'No change occurs', "B":'0 to +2 (oxidation)', "C":'+4 to +2', "D":'+2 to 0 (reduction)'},"answer":'D'},

{"id":121,"subject":'Chemistry',"topic":'Physical Chemistry',"difficulty":'Medium',
 "question":'Freezing point depression, a colligative property, occurs when a solute is added to a solvent because the solute:',
 "options":{"A":"Disrupts the solvent's ability to form an ordered solid structure, lowering the temperature at which freezing occurs", "B":"Increases the solvent's boiling point only", "C":'Has no effect on freezing point', "D":"Only affects the solvent's color"},"answer":'A'},

{"id":122,"subject":'Chemistry',"topic":'Physical Chemistry',"difficulty":'Hard',
 "question":'10 mL of 0.5 M H2SO4 is required to neutralize 20 mL of NaOH solution (H2SO4 + 2NaOH -> Na2SO4 + 2H2O). What is the molarity of the NaOH solution?',
 "options":{"A":'0.25 M', "B":'0.5 M', "C":'1.0 M', "D":'0.125 M'},"answer":'B'},

{"id":123,"subject":'Chemistry',"topic":'Environmental Chemistry',"difficulty":'Easy',
 "question":'The primary cause of global warming, according to the scientific consensus, is:',
 "options":{"A":'Natural solar cycles alone', "B":'Volcanic eruptions alone', "C":'Increased atmospheric concentrations of greenhouse gases (like CO2) from human activities', "D":'Ocean currents alone'},"answer":'C'},

{"id":124,"subject":'Chemistry',"topic":'Environmental Chemistry',"difficulty":'Medium',
 "question":'Which of the following practices would most directly help reduce plastic pollution in oceans?',
 "options":{"A":'Increasing single-use plastic production', "B":'Banning all forms of recycling', "C":'Dumping more waste directly into rivers', "D":'Reducing plastic waste, improving recycling, and proper waste management'},"answer":'D'},

{"id":125,"subject":'Chemistry',"topic":'Chemical Bonding',"difficulty":'Easy',
 "question":'A hydrogen bond is best described as:',
 "options":{"A":'A relatively weak intermolecular attraction between a hydrogen atom bonded to an electronegative atom and a lone pair on a nearby electronegative atom', "B":'A strong covalent bond between hydrogen and oxygen within the same molecule', "C":'The strongest type of chemical bond', "D":'A bond found only in metals'},"answer":'A'},

{"id":126,"subject":'Chemistry',"topic":'Atomic Structure',"difficulty":'Easy',
 "question":'Two atoms of the same element with different numbers of neutrons are called:',
 "options":{"A":'Ions', "B":'Isotopes', "C":'Isomers', "D":'Allotropes'},"answer":'B'},

# ============================================================
# PHYSICS (36) - id 127-162
# ============================================================

{"id":127,"subject":'Physics',"topic":'Kinematics',"difficulty":'Easy',
 "question":"A jogger covers 12 km in 2 hours at constant speed. What is the jogger's speed?",
 "options":{"A":'4 km/h', "B":'24 km/h', "C":'6 km/h', "D":'0.6 km/h'},"answer":'C'},

{"id":128,"subject":'Physics',"topic":'Kinematics',"difficulty":'Medium',
 "question":'A car accelerates uniformly from 12 m/s to 32 m/s in 5 seconds. What is its acceleration?',
 "options":{"A":'2.4 m/s^2', "B":'6.4 m/s^2', "C":'20 m/s^2', "D":'4 m/s^2'},"answer":'D'},

{"id":129,"subject":'Physics',"topic":'Kinematics',"difficulty":'Hard',
 "question":'A ball is dropped from rest and falls for 3 seconds before hitting the ground (g = 10 m/s^2, ignoring air resistance). What is its velocity just before impact?',
 "options":{"A":'30 m/s', "B":'15 m/s', "C":'45 m/s', "D":'10 m/s'},"answer":'A'},

{"id":130,"subject":'Physics',"topic":'Dynamics',"difficulty":'Easy',
 "question":'A book remains stationary on a table because the net force acting on it is:',
 "options":{"A":'Very large', "B":'Zero', "C":'Directed downward only', "D":'Directed upward only'},"answer":'B'},

{"id":131,"subject":'Physics',"topic":'Dynamics',"difficulty":'Medium',
 "question":'A net force of 36 N produces an acceleration of 4 m/s^2 in an object. What is the mass of the object?',
 "options":{"A":'32 kg', "B":'144 kg', "C":'9 kg', "D":'40 kg'},"answer":'C'},

{"id":132,"subject":'Physics',"topic":'Dynamics',"difficulty":'Medium',
 "question":"Which of the following is a correct statement of Newton's third law?",
 "options":{"A":'An object at rest stays at rest unless acted upon by a force', "B":'Objects in motion tend to stay in motion', "C":'Force equals mass times acceleration', "D":'For every action force, there is an equal and opposite reaction force'},"answer":'D'},

{"id":133,"subject":'Physics',"topic":'Dynamics',"difficulty":'Hard',
 "question":"A 3 kg object is pushed with a horizontal force of 18 N across a surface with a coefficient of kinetic friction of 0.2 (g = 10 m/s^2). What is the object's acceleration?",
 "options":{"A":'4 m/s^2', "B":'6 m/s^2', "C":'2 m/s^2', "D":'8 m/s^2'},"answer":'A'},

{"id":134,"subject":'Physics',"topic":'Work, Energy & Power',"difficulty":'Easy',
 "question":'If an object moves in a direction perpendicular to the applied force, the work done by that force is:',
 "options":{"A":'Maximum', "B":'Zero', "C":'Negative', "D":'Equal to the force times distance'},"answer":'B'},

{"id":135,"subject":'Physics',"topic":'Work, Energy & Power',"difficulty":'Medium',
 "question":'A 6 kg object is raised to a height of 5 m (g = 10 m/s^2). What is its gravitational potential energy?',
 "options":{"A":'30 J', "B":'50 J', "C":'300 J', "D":'11 J'},"answer":'C'},

{"id":136,"subject":'Physics',"topic":'Work, Energy & Power',"difficulty":'Medium',
 "question":'A 5 kg object moving at 4 m/s has a kinetic energy of:',
 "options":{"A":'20 J', "B":'100 J', "C":'80 J', "D":'40 J'},"answer":'D'},

{"id":137,"subject":'Physics',"topic":'Work, Energy & Power',"difficulty":'Hard',
 "question":'A generator produces 18000 J of energy in 30 seconds. What is its power output?',
 "options":{"A":'600 W', "B":'540000 W', "C":'60 W', "D":'6000 W'},"answer":'A'},

{"id":138,"subject":'Physics',"topic":'Circular Motion & Gravitation',"difficulty":'Easy',
 "question":'The direction of centripetal acceleration for an object in uniform circular motion is:',
 "options":{"A":'Tangent to the circular path', "B":'Toward the center of the circle', "C":'Away from the center', "D":"In the direction of the object's velocity"},"answer":'B'},

{"id":139,"subject":'Physics',"topic":'Circular Motion & Gravitation',"difficulty":'Medium',
 "question":'If the distance between two masses is increased by a factor of 5, while both masses remain unchanged, the gravitational force between them becomes:',
 "options":{"A":'5 times the original', "B":'1/5 of the original', "C":'1/25 of the original', "D":'25 times the original'},"answer":'C'},

{"id":140,"subject":'Physics',"topic":'Circular Motion & Gravitation',"difficulty":'Hard',
 "question":"If Earth's mass were to double while its radius stayed the same, the acceleration due to gravity at its surface would:",
 "options":{"A":'Stay the same', "B":'Quadruple', "C":'Be halved', "D":'Double'},"answer":'D'},

{"id":141,"subject":'Physics',"topic":'Fluid Mechanics',"difficulty":'Easy',
 "question":'An object will float in a fluid when the buoyant force acting on it:',
 "options":{"A":'Equals its weight', "B":'Is less than its weight', "C":'Is zero', "D":'Exceeds twice its weight'},"answer":'A'},

{"id":142,"subject":'Physics',"topic":'Fluid Mechanics',"difficulty":'Medium',
 "question":"According to Archimedes' principle, an object submerged in a fluid experiences an upward buoyant force equal to:",
 "options":{"A":'Its own weight', "B":'The weight of the fluid it displaces', "C":'The weight of the container', "D":'Zero, if fully submerged'},"answer":'B'},

{"id":143,"subject":'Physics',"topic":'Fluid Mechanics',"difficulty":'Hard',
 "question":'A syringe uses a plunger to create a pressure difference that draws fluid into the barrel. This is best explained by:',
 "options":{"A":"Bernoulli's principle exclusively", "B":"Archimedes' principle", "C":"Pascal's principle, since pressure changes are transmitted throughout the enclosed fluid", "D":"Newton's third law only"},"answer":'C'},

{"id":144,"subject":'Physics',"topic":'Oscillations & Waves',"difficulty":'Easy',
 "question":'The point of maximum displacement above the equilibrium position in a transverse wave is called the:',
 "options":{"A":'Trough', "B":'Wavelength', "C":'Node', "D":'Crest'},"answer":'D'},

{"id":145,"subject":'Physics',"topic":'Oscillations & Waves',"difficulty":'Medium',
 "question":"The frequency of a simple pendulum's oscillation is related to its length such that a longer pendulum has:",
 "options":{"A":'A lower frequency (longer period)', "B":'A higher frequency', "C":'The same frequency, regardless of length', "D":'No defined frequency'},"answer":'A'},

{"id":146,"subject":'Physics',"topic":'Oscillations & Waves',"difficulty":'Medium',
 "question":'A wave has a frequency of 50 Hz and travels at 200 m/s. What is its wavelength?',
 "options":{"A":'0.25 m', "B":'4 m', "C":'10000 m', "D":'250 m'},"answer":'B'},

{"id":147,"subject":'Physics',"topic":'Oscillations & Waves',"difficulty":'Hard',
 "question":'Constructive interference occurs when two waves meet:',
 "options":{"A":'Completely out of phase, canceling each other', "B":'At a 90-degree angle only', "C":'In phase, with their crests and troughs aligning, resulting in a larger combined amplitude', "D":'With completely different frequencies'},"answer":'C'},

{"id":148,"subject":'Physics',"topic":'Thermodynamics',"difficulty":'Easy',
 "question":'Convection is a method of heat transfer that occurs primarily in:',
 "options":{"A":'Solids only', "B":'Only in metals', "C":'A vacuum only', "D":'Fluids (liquids and gases), through the bulk movement of the fluid'},"answer":'D'},

{"id":149,"subject":'Physics',"topic":'Thermodynamics',"difficulty":'Medium',
 "question":'An adiabatic process, by definition, involves:',
 "options":{"A":'No heat exchange with the surroundings', "B":'Constant temperature', "C":'Constant volume', "D":'Constant internal energy'},"answer":'A'},

{"id":150,"subject":'Physics',"topic":'Thermodynamics',"difficulty":'Hard',
 "question":'A gas at constant pressure absorbs 800 J of heat and expands, doing 300 J of work on its surroundings. What is the change in internal energy of the gas?',
 "options":{"A":'1100 J', "B":'500 J', "C":'-500 J', "D":'300 J'},"answer":'B'},

{"id":151,"subject":'Physics',"topic":'Electrostatics',"difficulty":'Easy',
 "question":'Two objects with opposite electric charges will:',
 "options":{"A":'Repel each other', "B":'Have no interaction', "C":'Attract each other', "D":'Immediately combine into a neutral object'},"answer":'C'},

{"id":152,"subject":'Physics',"topic":'Electrostatics',"difficulty":'Medium',
 "question":"The force between two point charges, according to Coulomb's law, is inversely proportional to:",
 "options":{"A":'The product of the charges', "B":'The temperature of the surroundings', "C":'The sum of the charges', "D":'The square of the distance between them'},"answer":'D'},

{"id":153,"subject":'Physics',"topic":'Current Electricity',"difficulty":'Easy',
 "question":"Ohm's law states that voltage equals the product of current and:",
 "options":{"A":'Resistance', "B":'Power', "C":'Energy', "D":'Time'},"answer":'A'},

{"id":154,"subject":'Physics',"topic":'Current Electricity',"difficulty":'Medium',
 "question":'In the circuit shown, resistors R1 (6 ohm) and R2 (3 ohm) are connected in parallel, and this parallel combination is connected in series with R3 (4 ohm). What is the total resistance of the circuit?',
 "image":'images/q_circuit_r1r2_parallel_r3_series_v3.png',
 "options":{"A":'13 ohm', "B":'6 ohm', "C":'2 ohm', "D":'9 ohm'},"answer":'B'},

{"id":155,"subject":'Physics',"topic":'Current Electricity',"difficulty":'Hard',
 "question":'Two resistors of 15 ohm and 10 ohm are connected in parallel. What is their equivalent resistance?',
 "options":{"A":'25 ohm', "B":'5 ohm', "C":'6 ohm', "D":'150 ohm'},"answer":'C'},

{"id":156,"subject":'Physics',"topic":'Current Electricity',"difficulty":'Medium',
 "question":'A 1000 W heater operates at 250 V. What current does it draw?',
 "options":{"A":'2.5 A', "B":'0.25 A', "C":'250000 A', "D":'4 A'},"answer":'D'},

{"id":157,"subject":'Physics',"topic":'Electromagnetism',"difficulty":'Medium',
 "question":'The magnetic field produced by a current-carrying loop of wire is strongest:',
 "options":{"A":'At the center of the loop', "B":'Far from the loop', "C":'Outside the loop only', "D":'Nowhere; loops produce no magnetic field'},"answer":'A'},

{"id":158,"subject":'Physics',"topic":'Electromagnetism',"difficulty":'Hard',
 "question":"Lenz's law states that the direction of an induced current is such that it:",
 "options":{"A":'Aids the change in magnetic flux that produced it', "B":'Opposes the change in magnetic flux that produced it', "C":'Has no relation to the change in flux', "D":'Is always in a fixed, predetermined direction'},"answer":'B'},

{"id":159,"subject":'Physics',"topic":'Modern Physics',"difficulty":'Easy',
 "question":'The overall electric charge of a proton is:',
 "options":{"A":'Negative', "B":'Neutral', "C":'Positive', "D":'Variable, depending on the atom'},"answer":'C'},

{"id":160,"subject":'Physics',"topic":'Modern Physics',"difficulty":'Medium',
 "question":'In beta-minus decay, a neutron in the nucleus transforms into a proton, emitting:',
 "options":{"A":'An alpha particle', "B":'A positron', "C":'A gamma ray only', "D":'An electron (beta particle) and an antineutrino'},"answer":'D'},

{"id":161,"subject":'Physics',"topic":'Modern Physics',"difficulty":'Hard',
 "question":'A radioactive isotope has a half-life of 4 hours. Starting with 320 g, how much remains after 20 hours?',
 "options":{"A":'10 g', "B":'20 g', "C":'40 g', "D":'5 g'},"answer":'A'},

{"id":162,"subject":'Physics',"topic":'Optics',"difficulty":'Medium',
 "question":'The ray diagram shows an object placed exactly at the center of curvature (C) of a concave mirror. Based on the diagram, the image formed is:',
 "image":'images/q_concave_mirror_object_at_c.png',
 "options":{"A":'Virtual, upright, and magnified', "B":'Real, inverted, and the same size as the object, formed at C', "C":'Real, inverted, and magnified, formed beyond C', "D":'Virtual, inverted, and diminished'},"answer":'B'},

# ============================================================
# ENGLISH (9) - id 163-171
# ============================================================

{"id":163,"subject":'English',"topic":'Synonyms',"difficulty":'Easy',
 "question":"Choose the word most nearly similar in meaning to 'CANDID':",
 "options":{"A":'Evasive', "B":'Deceptive', "C":'Frank', "D":'Secretive'},"answer":'C'},

{"id":164,"subject":'English',"topic":'Antonyms',"difficulty":'Easy',
 "question":"Choose the word most nearly opposite in meaning to 'ABUNDANT':",
 "options":{"A":'Sufficient', "B":'Plentiful', "C":'Ample', "D":'Scarce'},"answer":'D'},

{"id":165,"subject":'English',"topic":'Grammar',"difficulty":'Easy',
 "question":'Choose the grammatically correct sentence:',
 "options":{"A":"She doesn't like spicy food.", "B":"She don't like spicy food.", "C":'She not like spicy food.', "D":"She doesn't likes spicy food."},"answer":'A'},

{"id":166,"subject":'English',"topic":'Grammar',"difficulty":'Medium',
 "question":'Choose the correct sentence:',
 "options":{"A":'He suggested that she should go early.', "B":'He suggested that she go early.', "C":'He suggested that she goes early.', "D":'He suggested she will go early.'},"answer":'B'},

{"id":167,"subject":'English',"topic":'Sentence Correction',"difficulty":'Medium',
 "question":'Choose the sentence that is grammatically correct:',
 "options":{"A":'Each of the students have their own laptop.', "B":'Each of the student has their own laptop.', "C":'Each of the students has his or her own laptop.', "D":'Each of the students have his own laptop.'},"answer":'C'},

{"id":168,"subject":'English',"topic":'Vocabulary',"difficulty":'Medium',
 "question":"Choose the word that best completes the sentence: 'Despite the criticism, the artist remained ______ in her unique creative vision.'",
 "options":{"A":'Wavering', "B":'Indifferent', "C":'Uncertain', "D":'Steadfast'},"answer":'D'},

{"id":169,"subject":'English',"topic":'Idioms',"difficulty":'Medium',
 "question":"Choose the meaning closest to the idiom 'to add fuel to the fire':",
 "options":{"A":'To make an already difficult situation worse', "B":'To calm down a tense situation', "C":'To start a literal fire', "D":'To ignore a problem entirely'},"answer":'A'},

{"id":170,"subject":'English',"topic":'Sentence Correction',"difficulty":'Hard',
 "question":"Choose the option that best corrects the sentence: 'The manager, as well as his employees, were present at the meeting.'",
 "options":{"A":'The manager, as well as his employees, were present in the meeting.', "B":'The manager, as well as his employees, was present at the meeting.', "C":'The managers, as well as his employee, was present at the meeting.', "D":'No correction needed.'},"answer":'B'},

{"id":171,"subject":'English',"topic":'Prepositions',"difficulty":'Hard',
 "question":"Choose the correct preposition: 'The success of the project depends largely ______ effective teamwork.'",
 "options":{"A":'of', "B":'for', "C":'on', "D":'with'},"answer":'C'},

# ============================================================
# LOGICAL REASONING (9) - id 172-180
# ============================================================

{"id":172,"subject":'Logical Reasoning',"topic":'Number Series',"difficulty":'Easy',
 "question":'Find the next number in the series: 8, 16, 24, 32, ?',
 "options":{"A":'36', "B":'48', "C":'42', "D":'40'},"answer":'D'},

{"id":173,"subject":'Logical Reasoning',"topic":'Number Series',"difficulty":'Easy',
 "question":'Find the missing number: 1, 3, 6, 10, ?',
 "options":{"A":'15', "B":'14', "C":'12', "D":'16'},"answer":'A'},

{"id":174,"subject":'Logical Reasoning',"topic":'Analogies',"difficulty":'Easy',
 "question":'Fish is to Gills as Human is to:',
 "options":{"A":'Heart', "B":'Lungs', "C":'Skin', "D":'Blood'},"answer":'B'},

{"id":175,"subject":'Logical Reasoning',"topic":'Analogies',"difficulty":'Medium',
 "question":'Umbrella is to Rain as Sunscreen is to:',
 "options":{"A":'Summer', "B":'Skin', "C":'Sun', "D":'Heat'},"answer":'C'},

{"id":176,"subject":'Logical Reasoning',"topic":'Blood Relations',"difficulty":'Medium',
 "question":"A man said, 'This woman's husband is the only brother of my wife.' How is the man related to the woman's husband?",
 "options":{"A":'Uncle', "B":'Father-in-law', "C":'Cousin', "D":'Brother-in-law'},"answer":'D'},

{"id":177,"subject":'Logical Reasoning',"topic":'Coding-Decoding',"difficulty":'Medium',
 "question":'If in a certain code, LEMON is written as MFNPO, how is ORANGE written in the same code?',
 "options":{"A":'PSBOHF', "B":'PSBOGF', "C":'OSBOHF', "D":'PSBOHE'},"answer":'A'},

{"id":178,"subject":'Logical Reasoning',"topic":'Syllogism',"difficulty":'Hard',
 "question":'All pilots are trained professionals. No trained professionals are careless. Which conclusion logically follows?',
 "options":{"A":'Some pilots are careless', "B":'No pilots are careless', "C":'All careless people are pilots', "D":'Some trained professionals are pilots'},"answer":'B'},

{"id":179,"subject":'Logical Reasoning',"topic":'Pattern Recognition',"difficulty":'Hard',
 "question":'Find the next term in the series: 2, 4, 8, 14, 22, ?',
 "options":{"A":'30', "B":'34', "C":'32', "D":'36'},"answer":'C'},

{"id":180,"subject":'Logical Reasoning',"topic":'Direction Sense',"difficulty":'Medium',
 "question":'A woman walks 9 km north, then turns east and walks 12 km. How far is she from her starting point?',
 "options":{"A":'21 km', "B":'108 km', "C":'3 km', "D":'15 km'},"answer":'D'},

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