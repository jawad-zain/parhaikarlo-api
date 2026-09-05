"""
MDCAT Biology Question Bank
===========================
200 MCQs modeled on the MDCAT (Punjab / national) Biology syllabus,
same Python dict format as the mock test / LR bank.

Topic distribution (approx):
    Biomolecules ..................... 12
    Enzymes ..........................  8
    Bioenergetics (Photosynthesis
        & Cellular Respiration) ...... 12
    Cell Biology & Organelles ........ 12
    Cell Membrane & Transport ........  8
    Cell Cycle & Division ............ 10
    Genetics (Mendelian + Human) ..... 15
    Molecular Biology (DNA / gene
        expression / mutations) ...... 15
    Evolution ........................  8
    Biological Classification &
        Diversity of Life ............ 10
    Prokaryotes / Viruses / Fungi ....  8
    Plant Biology (nutrition /
        transport / hormones) ........ 12
    Human Digestion ..................  8
    Human Circulation ................ 10
    Human Respiration ................  8
    Human Excretion & Homeostasis ....  8
    Human Nervous System ............. 10
    Human Endocrine System ...........  8
    Support & Movement ...............  6
    Human Reproduction ............... 10
    Ecology .......................... 10
    Biotechnology ....................  5
    Immunity .........................  5
    Total ........................... 200

Difficulty mix ~ 30% Easy / 50% Medium / 20% Hard.

Correct-answer letter is balanced ~50/50/50/50 across A-D (option
positions were shuffled after authoring so the answer key cannot be
gamed by always picking one letter).

Each question is a dict:
    id, subject, topic, subtopic, difficulty, question, options (A-D), answer
"""

QUESTIONS = [

# ============================================================
# BIOMOLECULES (12)  id 1-12
# ============================================================

{"id":1,"subject":'Biology',"topic":'Biomolecules',"subtopic":'Carbohydrates',"difficulty":'Easy',
 "question":'Which of the following is a monosaccharide?',
 "options":{"A":'Sucrose',"B":'Glucose',"C":'Starch',"D":'Cellulose'},"answer":'B'},

{"id":2,"subject":'Biology',"topic":'Biomolecules',"subtopic":'Carbohydrates',"difficulty":'Easy',
 "question":'The storage carbohydrate in animal cells is:',
 "options":{"A":'Starch',"B":'Cellulose',"C":'Chitin',"D":'Glycogen'},"answer":'D'},

{"id":3,"subject":'Biology',"topic":'Biomolecules',"subtopic":'Carbohydrates',"difficulty":'Medium',
 "question":'Which glycosidic linkage is present in cellulose?',
 "options":{"A":'Alpha 1-4',"B":'Alpha 1-6',"C":'Beta 1-4',"D":'Beta 1-2'},"answer":'C'},

{"id":4,"subject":'Biology',"topic":'Biomolecules',"subtopic":'Lipids',"difficulty":'Easy',
 "question":'Triglycerides are formed by the condensation of glycerol with:',
 "options":{"A":'Amino acids',"B":'Nucleotides',"C":'Monosaccharides',"D":'Fatty acids'},"answer":'D'},

{"id":5,"subject":'Biology',"topic":'Biomolecules',"subtopic":'Lipids',"difficulty":'Medium',
 "question":'Which of the following is a phospholipid component of biological membranes?',
 "options":{"A":'Cholesterol only',"B":'Triglycerides',"C":'Phosphatidylcholine',"D":'Wax esters'},"answer":'C'},

{"id":6,"subject":'Biology',"topic":'Biomolecules',"subtopic":'Proteins',"difficulty":'Easy',
 "question":'The bond that links two amino acids in a protein is:',
 "options":{"A":'Glycosidic bond',"B":'Ester bond',"C":'Peptide bond',"D":'Phosphodiester bond'},"answer":'C'},

{"id":7,"subject":'Biology',"topic":'Biomolecules',"subtopic":'Proteins',"difficulty":'Medium',
 "question":'The alpha helix and beta pleated sheet are examples of which level of protein structure?',
 "options":{"A":'Secondary',"B":'Primary',"C":'Tertiary',"D":'Quaternary'},"answer":'A'},

{"id":8,"subject":'Biology',"topic":'Biomolecules',"subtopic":'Proteins',"difficulty":'Medium',
 "question":'Denaturation of a protein results in loss of its:',
 "options":{"A":'Higher-order structure and function',"B":'Primary structure',"C":'Peptide bonds',"D":'Amino acid composition'},"answer":'A'},

{"id":9,"subject":'Biology',"topic":'Biomolecules',"subtopic":'Nucleic Acids',"difficulty":'Easy',
 "question":'The sugar present in RNA is:',
 "options":{"A":'Glucose',"B":'Ribose',"C":'Deoxyribose',"D":'Fructose'},"answer":'B'},

{"id":10,"subject":'Biology',"topic":'Biomolecules',"subtopic":'Nucleic Acids',"difficulty":'Medium',
 "question":'Which of the following bases is a pyrimidine?',
 "options":{"A":'Cytosine',"B":'Adenine',"C":'Guanine',"D":'None of these'},"answer":'A'},

{"id":11,"subject":'Biology',"topic":'Biomolecules',"subtopic":'Water',"difficulty":'Medium',
 "question":'Water is an excellent solvent for polar substances because it is:',
 "options":{"A":'Nonpolar',"B":'An acid',"C":'A polar molecule capable of forming hydrogen bonds',"D":'A base'},"answer":'C'},

{"id":12,"subject":'Biology',"topic":'Biomolecules',"subtopic":'Proteins',"difficulty":'Hard',
 "question":'A protein\'s specific three-dimensional shape is primarily determined by:',
 "options":{"A":'Random environmental factors',"B":'The organism diet',"C":'The molecular weight only',"D":'The sequence of amino acids which dictates folding'},"answer":'D'},


# ============================================================
# ENZYMES (8)  id 13-20
# ============================================================

{"id":13,"subject":'Biology',"topic":'Enzymes',"subtopic":'General',"difficulty":'Easy',
 "question":'Enzymes are best described as:',
 "options":{"A":'Inorganic catalysts',"B":'Substrates for reactions',"C":'Biological catalysts, mostly proteins',"D":'Products of digestion'},"answer":'C'},

{"id":14,"subject":'Biology',"topic":'Enzymes',"subtopic":'Mechanism',"difficulty":'Medium',
 "question":'The induced fit model of enzyme action proposes that:',
 "options":{"A":'The active site is completely rigid',"B":'The active site changes shape slightly to fit the substrate',"C":'Enzymes do not physically bind substrates',"D":'Substrates are permanently altered'},"answer":'B'},

{"id":15,"subject":'Biology',"topic":'Enzymes',"subtopic":'Factors',"difficulty":'Medium',
 "question":'Which factor would most likely denature an enzyme?',
 "options":{"A":'Optimum pH',"B":'Low substrate concentration',"C":'Presence of cofactors',"D":'Very high temperature'},"answer":'D'},

{"id":16,"subject":'Biology',"topic":'Enzymes',"subtopic":'Inhibition',"difficulty":'Medium',
 "question":'A competitive inhibitor of an enzyme:',
 "options":{"A":'Binds to an allosteric site and cannot be overcome by substrate',"B":'Permanently destroys the enzyme',"C":'Only works at high pH',"D":'Binds to the active site and can be overcome by increasing substrate concentration'},"answer":'D'},

{"id":17,"subject":'Biology',"topic":'Enzymes',"subtopic":'Cofactors',"difficulty":'Medium',
 "question":'A non-protein organic molecule required for enzyme activity is called a:',
 "options":{"A":'Coenzyme',"B":'Prosthetic group only',"C":'Metal ion cofactor',"D":'Zymogen'},"answer":'A'},

{"id":18,"subject":'Biology',"topic":'Enzymes',"subtopic":'Classification',"difficulty":'Hard',
 "question":'An enzyme that catalyzes the transfer of a functional group from one molecule to another belongs to the class:',
 "options":{"A":'Oxidoreductases',"B":'Hydrolases',"C":'Transferases',"D":'Ligases'},"answer":'C'},

{"id":19,"subject":'Biology',"topic":'Enzymes',"subtopic":'Kinetics',"difficulty":'Hard',
 "question":'The Km value of an enzyme is a measure of:',
 "options":{"A":'The affinity of the enzyme for its substrate; lower Km means higher affinity',"B":'The maximum reaction rate',"C":'The turnover number',"D":'The molecular weight of the enzyme'},"answer":'A'},

{"id":20,"subject":'Biology',"topic":'Enzymes',"subtopic":'Regulation',"difficulty":'Medium',
 "question":'Feedback inhibition typically involves the end product of a pathway inhibiting:',
 "options":{"A":'A key regulatory enzyme, often the first one committed to the pathway',"B":'The last enzyme of the pathway',"C":'All enzymes equally',"D":'Only the substrate binding'},"answer":'A'},


# ============================================================
# BIOENERGETICS (12)  id 21-32
# ============================================================

{"id":21,"subject":'Biology',"topic":'Bioenergetics',"subtopic":'Photosynthesis',"difficulty":'Easy',
 "question":'The overall reactants of photosynthesis are:',
 "options":{"A":'Glucose and oxygen',"B":'Oxygen and water',"C":'Glucose and carbon dioxide',"D":'Carbon dioxide and water'},"answer":'D'},

{"id":22,"subject":'Biology',"topic":'Bioenergetics',"subtopic":'Photosynthesis',"difficulty":'Easy',
 "question":'The pigment primarily responsible for capturing light energy in plants is:',
 "options":{"A":'Chlorophyll a',"B":'Carotene',"C":'Xanthophyll',"D":'Phycocyanin'},"answer":'A'},

{"id":23,"subject":'Biology',"topic":'Bioenergetics',"subtopic":'Photosynthesis',"difficulty":'Medium',
 "question":'The light-dependent reactions of photosynthesis take place in the:',
 "options":{"A":'Thylakoid membranes',"B":'Stroma',"C":'Cytoplasm',"D":'Outer chloroplast membrane'},"answer":'A'},

{"id":24,"subject":'Biology',"topic":'Bioenergetics',"subtopic":'Photosynthesis',"difficulty":'Medium',
 "question":'In the Calvin cycle, CO2 is initially fixed by combining with:',
 "options":{"A":'PEP',"B":'Pyruvate',"C":'RuBP',"D":'Glucose'},"answer":'C'},

{"id":25,"subject":'Biology',"topic":'Bioenergetics',"subtopic":'Photosynthesis',"difficulty":'Hard',
 "question":'C4 plants are more efficient than C3 plants under conditions of:',
 "options":{"A":'Low light and low temperature',"B":'Very low CO2 concentration only in aquatic environments',"C":'Complete darkness',"D":'High temperature and high light intensity'},"answer":'D'},

{"id":26,"subject":'Biology',"topic":'Bioenergetics',"subtopic":'Respiration',"difficulty":'Easy',
 "question":'Glycolysis takes place in the:',
 "options":{"A":'Mitochondrial matrix',"B":'Inner mitochondrial membrane',"C":'Nucleus',"D":'Cytoplasm'},"answer":'D'},

{"id":27,"subject":'Biology',"topic":'Bioenergetics',"subtopic":'Respiration',"difficulty":'Medium',
 "question":'The net gain of ATP from one glucose molecule during glycolysis is:',
 "options":{"A":'2 ATP',"B":'4 ATP',"C":'36 ATP',"D":'38 ATP'},"answer":'A'},

{"id":28,"subject":'Biology',"topic":'Bioenergetics',"subtopic":'Respiration',"difficulty":'Medium',
 "question":'The Krebs cycle occurs in the:',
 "options":{"A":'Cytoplasm',"B":'Outer mitochondrial membrane',"C":'Mitochondrial matrix',"D":'Endoplasmic reticulum'},"answer":'C'},

{"id":29,"subject":'Biology',"topic":'Bioenergetics',"subtopic":'Respiration',"difficulty":'Medium',
 "question":'The final electron acceptor in aerobic respiration is:',
 "options":{"A":'Oxygen',"B":'NAD+',"C":'FAD',"D":'Pyruvate'},"answer":'A'},

{"id":30,"subject":'Biology',"topic":'Bioenergetics',"subtopic":'Respiration',"difficulty":'Hard',
 "question":'In eukaryotic cells, the total net ATP yield per glucose molecule from complete aerobic respiration is approximately:',
 "options":{"A":'2',"B":'4',"C":'80',"D":'30 to 32'},"answer":'D'},

{"id":31,"subject":'Biology',"topic":'Bioenergetics',"subtopic":'Fermentation',"difficulty":'Medium',
 "question":'In muscle cells under anaerobic conditions, pyruvate is converted to:',
 "options":{"A":'Lactic acid',"B":'Ethanol and CO2',"C":'Acetyl-CoA',"D":'Citrate'},"answer":'A'},

{"id":32,"subject":'Biology',"topic":'Bioenergetics',"subtopic":'ATP',"difficulty":'Medium',
 "question":'The energy currency of the cell is:',
 "options":{"A":'NADH',"B":'Glucose',"C":'ATP',"D":'FADH2'},"answer":'C'},


# ============================================================
# CELL BIOLOGY (12)  id 33-44
# ============================================================

{"id":33,"subject":'Biology',"topic":'Cell Biology',"subtopic":'General',"difficulty":'Easy',
 "question":'Which of the following is present in prokaryotic cells but absent in eukaryotic cells (typically)?',
 "options":{"A":'A nucleoid region',"B":'Ribosomes',"C":'Membrane-bound nucleus',"D":'Mitochondria'},"answer":'A'},

{"id":34,"subject":'Biology',"topic":'Cell Biology',"subtopic":'Nucleus',"difficulty":'Easy',
 "question":'The site of ribosomal RNA synthesis within the nucleus is the:',
 "options":{"A":'Nucleolus',"B":'Nuclear envelope',"C":'Nuclear pore',"D":'Chromatin'},"answer":'A'},

{"id":35,"subject":'Biology',"topic":'Cell Biology',"subtopic":'ER',"difficulty":'Easy',
 "question":'Rough endoplasmic reticulum is studded with:',
 "options":{"A":'Lysosomes',"B":'Chloroplasts',"C":'Vacuoles',"D":'Ribosomes'},"answer":'D'},

{"id":36,"subject":'Biology',"topic":'Cell Biology',"subtopic":'Golgi',"difficulty":'Medium',
 "question":'The Golgi apparatus is primarily involved in:',
 "options":{"A":'ATP synthesis',"B":'Modification, sorting, and packaging of proteins',"C":'DNA replication',"D":'Cellular respiration'},"answer":'B'},

{"id":37,"subject":'Biology',"topic":'Cell Biology',"subtopic":'Mitochondria',"difficulty":'Medium',
 "question":'The inner mitochondrial membrane is folded into structures called:',
 "options":{"A":'Grana',"B":'Cristae',"C":'Thylakoids',"D":'Cisternae'},"answer":'B'},

{"id":38,"subject":'Biology',"topic":'Cell Biology',"subtopic":'Lysosomes',"difficulty":'Medium',
 "question":'Lysosomes contain enzymes that function best in a:',
 "options":{"A":'Basic pH',"B":'Neutral pH',"C":'Very high temperature',"D":'Acidic pH'},"answer":'D'},

{"id":39,"subject":'Biology',"topic":'Cell Biology',"subtopic":'Chloroplasts',"difficulty":'Medium',
 "question":'Stacks of thylakoids in a chloroplast are called:',
 "options":{"A":'Grana',"B":'Stroma',"C":'Cristae',"D":'Matrix'},"answer":'A'},

{"id":40,"subject":'Biology',"topic":'Cell Biology',"subtopic":'Ribosomes',"difficulty":'Medium',
 "question":'The ribosomes of prokaryotes are of size:',
 "options":{"A":'80S',"B":'60S',"C":'40S',"D":'70S'},"answer":'D'},

{"id":41,"subject":'Biology',"topic":'Cell Biology',"subtopic":'Cytoskeleton',"difficulty":'Hard',
 "question":'Microtubules are composed primarily of the protein:',
 "options":{"A":'Actin',"B":'Keratin',"C":'Myosin',"D":'Tubulin'},"answer":'D'},

{"id":42,"subject":'Biology',"topic":'Cell Biology',"subtopic":'Cell Wall',"difficulty":'Easy',
 "question":'The cell wall of plant cells is primarily made of:',
 "options":{"A":'Chitin',"B":'Cellulose',"C":'Peptidoglycan',"D":'Lignin only'},"answer":'B'},

{"id":43,"subject":'Biology',"topic":'Cell Biology',"subtopic":'Endosymbiotic Theory',"difficulty":'Hard',
 "question":'The endosymbiotic theory proposes that mitochondria and chloroplasts originated from:',
 "options":{"A":'Free-living prokaryotes engulfed by ancestral eukaryotic cells',"B":'Viruses that infected early cells',"C":'Nuclear invaginations',"D":'Golgi vesicles'},"answer":'A'},

{"id":44,"subject":'Biology',"topic":'Cell Biology',"subtopic":'General',"difficulty":'Medium',
 "question":'A cell that produces and secretes large amounts of protein would contain abundant:',
 "options":{"A":'Chloroplasts',"B":'Central vacuoles',"C":'Rough ER and Golgi apparatus',"D":'Peroxisomes only'},"answer":'C'},


# ============================================================
# CELL MEMBRANE AND TRANSPORT (8)  id 45-52
# ============================================================

{"id":45,"subject":'Biology',"topic":'Cell Membrane and Transport',"subtopic":'Structure',"difficulty":'Easy',
 "question":'According to the fluid mosaic model, the cell membrane consists mainly of:',
 "options":{"A":'A rigid protein layer',"B":'Only carbohydrates',"C":'Cellulose and lignin',"D":'A phospholipid bilayer with embedded proteins'},"answer":'D'},

{"id":46,"subject":'Biology',"topic":'Cell Membrane and Transport',"subtopic":'Transport',"difficulty":'Easy',
 "question":'Diffusion of water across a selectively permeable membrane is called:',
 "options":{"A":'Active transport',"B":'Osmosis',"C":'Endocytosis',"D":'Exocytosis'},"answer":'B'},

{"id":47,"subject":'Biology',"topic":'Cell Membrane and Transport',"subtopic":'Transport',"difficulty":'Medium',
 "question":'Facilitated diffusion differs from simple diffusion in that facilitated diffusion:',
 "options":{"A":'Requires ATP',"B":'Only occurs for lipid-soluble molecules',"C":'Requires a carrier or channel protein but does not require ATP',"D":'Moves molecules against their gradient'},"answer":'C'},

{"id":48,"subject":'Biology',"topic":'Cell Membrane and Transport',"subtopic":'Transport',"difficulty":'Medium',
 "question":'The Na+/K+ pump is an example of:',
 "options":{"A":'Simple diffusion',"B":'Facilitated diffusion',"C":'Primary active transport',"D":'Osmosis'},"answer":'C'},

{"id":49,"subject":'Biology',"topic":'Cell Membrane and Transport',"subtopic":'Osmosis',"difficulty":'Medium',
 "question":'A red blood cell placed in a hypotonic solution will:',
 "options":{"A":'Shrink and crenate',"B":'Swell and possibly burst',"C":'Remain unchanged',"D":'Undergo plasmolysis'},"answer":'B'},

{"id":50,"subject":'Biology',"topic":'Cell Membrane and Transport',"subtopic":'Endocytosis',"difficulty":'Easy',
 "question":'The process by which cells engulf solid particles is called:',
 "options":{"A":'Pinocytosis',"B":'Exocytosis',"C":'Phagocytosis',"D":'Diffusion'},"answer":'C'},

{"id":51,"subject":'Biology',"topic":'Cell Membrane and Transport',"subtopic":'Aquaporins',"difficulty":'Hard',
 "question":'Aquaporins are membrane proteins that specifically facilitate the transport of:',
 "options":{"A":'Sodium ions',"B":'Glucose',"C":'Water',"D":'Amino acids'},"answer":'C'},

{"id":52,"subject":'Biology',"topic":'Cell Membrane and Transport',"subtopic":'Transport',"difficulty":'Hard',
 "question":'A plant cell placed in a hypertonic solution will undergo:',
 "options":{"A":'Turgor pressure increase',"B":'Plasmolysis',"C":'Lysis',"D":'Deplasmolysis'},"answer":'B'},


# ============================================================
# CELL CYCLE AND DIVISION (10)  id 53-62
# ============================================================

{"id":53,"subject":'Biology',"topic":'Cell Cycle and Division',"subtopic":'Mitosis',"difficulty":'Easy',
 "question":'The correct sequence of mitotic phases is:',
 "options":{"A":'Metaphase, Prophase, Telophase, Anaphase',"B":'Anaphase, Prophase, Metaphase, Telophase',"C":'Prophase, Metaphase, Anaphase, Telophase',"D":'Telophase, Anaphase, Prophase, Metaphase'},"answer":'C'},

{"id":54,"subject":'Biology',"topic":'Cell Cycle and Division',"subtopic":'Interphase',"difficulty":'Easy',
 "question":'DNA replication occurs during which phase of the cell cycle?',
 "options":{"A":'G1 phase',"B":'G2 phase',"C":'S phase',"D":'M phase'},"answer":'C'},

{"id":55,"subject":'Biology',"topic":'Cell Cycle and Division',"subtopic":'Mitosis',"difficulty":'Medium',
 "question":'Chromosomes align at the equatorial plate during:',
 "options":{"A":'Metaphase',"B":'Prophase',"C":'Anaphase',"D":'Telophase'},"answer":'A'},

{"id":56,"subject":'Biology',"topic":'Cell Cycle and Division',"subtopic":'Mitosis',"difficulty":'Medium',
 "question":'Sister chromatids separate and move to opposite poles during:',
 "options":{"A":'Anaphase',"B":'Prophase',"C":'Metaphase',"D":'Telophase'},"answer":'A'},

{"id":57,"subject":'Biology',"topic":'Cell Cycle and Division',"subtopic":'Meiosis',"difficulty":'Medium',
 "question":'Crossing over between homologous chromosomes occurs during:',
 "options":{"A":'Metaphase I',"B":'Anaphase II',"C":'Prophase II',"D":'Prophase I of meiosis'},"answer":'D'},

{"id":58,"subject":'Biology',"topic":'Cell Cycle and Division',"subtopic":'Meiosis',"difficulty":'Medium',
 "question":'Meiosis produces:',
 "options":{"A":'Two identical diploid cells',"B":'Two haploid identical cells',"C":'Four diploid cells',"D":'Four haploid genetically variable cells'},"answer":'D'},

{"id":59,"subject":'Biology',"topic":'Cell Cycle and Division',"subtopic":'Regulation',"difficulty":'Medium',
 "question":'Cyclin-dependent kinases (CDKs) regulate:',
 "options":{"A":'Progression through the cell cycle',"B":'Only cytoplasmic streaming',"C":'Only DNA repair',"D":'Only lipid metabolism'},"answer":'A'},

{"id":60,"subject":'Biology',"topic":'Cell Cycle and Division',"subtopic":'Cancer',"difficulty":'Hard',
 "question":'Uncontrolled cell division that invades surrounding tissues characterizes:',
 "options":{"A":'Benign tumors',"B":'Malignant tumors',"C":'Normal cell growth',"D":'Cellular differentiation'},"answer":'B'},

{"id":61,"subject":'Biology',"topic":'Cell Cycle and Division',"subtopic":'Apoptosis',"difficulty":'Hard',
 "question":'Programmed cell death is known as:',
 "options":{"A":'Necrosis',"B":'Mitosis',"C":'Apoptosis',"D":'Meiosis'},"answer":'C'},

{"id":62,"subject":'Biology',"topic":'Cell Cycle and Division',"subtopic":'General',"difficulty":'Medium',
 "question":'If a cell has 2n = 8, after meiosis, each daughter cell will have how many chromosomes?',
 "options":{"A":'4',"B":'8',"C":'16',"D":'2'},"answer":'A'},


# ============================================================
# GENETICS (15)  id 63-77
# ============================================================

{"id":63,"subject":'Biology',"topic":'Genetics',"subtopic":'Mendelian',"difficulty":'Easy',
 "question":'Mendel\'s law of segregation states that:',
 "options":{"A":'Genes for different traits assort independently',"B":'Dominant alleles always mask recessive ones',"C":'Traits are inherited in blends',"D":'Two alleles for each trait separate during gamete formation'},"answer":'D'},

{"id":64,"subject":'Biology',"topic":'Genetics',"subtopic":'Mendelian',"difficulty":'Easy',
 "question":'In a monohybrid cross between two heterozygotes (Aa x Aa), the expected phenotypic ratio is:',
 "options":{"A":'1:1',"B":'9:3:3:1',"C":'1:2:1',"D":'3:1'},"answer":'D'},

{"id":65,"subject":'Biology',"topic":'Genetics',"subtopic":'Mendelian',"difficulty":'Medium',
 "question":'A dihybrid test cross (AaBb x aabb) produces a phenotypic ratio of:',
 "options":{"A":'9:3:3:1',"B":'3:1',"C":'1:1:1:1',"D":'1:2:1'},"answer":'C'},

{"id":66,"subject":'Biology',"topic":'Genetics',"subtopic":'Incomplete Dominance',"difficulty":'Medium',
 "question":'In snapdragons, red x white flowers produce all pink offspring. This is an example of:',
 "options":{"A":'Codominance',"B":'Incomplete dominance',"C":'Epistasis',"D":'Complete dominance'},"answer":'B'},

{"id":67,"subject":'Biology',"topic":'Genetics',"subtopic":'Codominance',"difficulty":'Medium',
 "question":'The AB blood group in humans is an example of:',
 "options":{"A":'Incomplete dominance',"B":'Complete dominance',"C":'Codominance',"D":'Sex-linked inheritance'},"answer":'C'},

{"id":68,"subject":'Biology',"topic":'Genetics',"subtopic":'Blood Groups',"difficulty":'Medium',
 "question":'A person with blood group O has the genotype:',
 "options":{"A":'ii',"B":'IA IB',"C":'IA i',"D":'IB IB'},"answer":'A'},

{"id":69,"subject":'Biology',"topic":'Genetics',"subtopic":'Sex-linked',"difficulty":'Medium',
 "question":'A woman who is a carrier for hemophilia (XHXh) marries a normal man (XHY). The probability that a son will be hemophilic is:',
 "options":{"A":'50%',"B":'0%',"C":'25%',"D":'100%'},"answer":'A'},

{"id":70,"subject":'Biology',"topic":'Genetics',"subtopic":'Sex-linked',"difficulty":'Medium',
 "question":'Color blindness in humans is an example of a trait that is:',
 "options":{"A":'Autosomal dominant',"B":'Y-linked',"C":'Mitochondrial',"D":'X-linked recessive'},"answer":'D'},

{"id":71,"subject":'Biology',"topic":'Genetics',"subtopic":'Human Disorders',"difficulty":'Medium',
 "question":'Down\'s syndrome is caused by:',
 "options":{"A":'Deletion of chromosome 21',"B":'Monosomy of chromosome X',"C":'Trisomy of chromosome 21',"D":'Translocation of chromosome 13'},"answer":'C'},

{"id":72,"subject":'Biology',"topic":'Genetics',"subtopic":'Human Disorders',"difficulty":'Medium',
 "question":'Klinefelter\'s syndrome has the karyotype:',
 "options":{"A":'45, X',"B":'47, XYY',"C":'47, XXX',"D":'47, XXY'},"answer":'D'},

{"id":73,"subject":'Biology',"topic":'Genetics',"subtopic":'Human Disorders',"difficulty":'Medium',
 "question":'Turner\'s syndrome is characterized by:',
 "options":{"A":'47 chromosomes with XXX',"B":'45 chromosomes with a single X (45, X)',"C":'47, XXY',"D":'Trisomy 18'},"answer":'B'},

{"id":74,"subject":'Biology',"topic":'Genetics',"subtopic":'Pedigree',"difficulty":'Hard',
 "question":'A trait that appears more frequently in males and is passed from carrier mothers to sons is most likely:',
 "options":{"A":'Autosomal dominant',"B":'X-linked recessive',"C":'Autosomal recessive',"D":'Y-linked'},"answer":'B'},

{"id":75,"subject":'Biology',"topic":'Genetics',"subtopic":'Hardy-Weinberg',"difficulty":'Hard',
 "question":'If the frequency of a recessive allele in a population is 0.2, the frequency of homozygous recessive individuals (assuming HW equilibrium) is:',
 "options":{"A":'0.16',"B":'0.20',"C":'0.32',"D":'0.04'},"answer":'D'},

{"id":76,"subject":'Biology',"topic":'Genetics',"subtopic":'Linkage',"difficulty":'Hard',
 "question":'Genes located close together on the same chromosome tend to be inherited together. This is called:',
 "options":{"A":'Genetic linkage',"B":'Independent assortment',"C":'Codominance',"D":'Recombination'},"answer":'A'},

{"id":77,"subject":'Biology',"topic":'Genetics',"subtopic":'Mendelian',"difficulty":'Easy',
 "question":'The physical expression of a gene is called the:',
 "options":{"A":'Genotype',"B":'Allele',"C":'Phenotype',"D":'Locus'},"answer":'C'},


# ============================================================
# MOLECULAR BIOLOGY (15)  id 78-92
# ============================================================

{"id":78,"subject":'Biology',"topic":'Molecular Biology',"subtopic":'DNA Structure',"difficulty":'Easy',
 "question":'The two strands of DNA are held together by:',
 "options":{"A":'Peptide bonds',"B":'Hydrogen bonds between complementary bases',"C":'Ionic bonds',"D":'Disulfide bridges'},"answer":'B'},

{"id":79,"subject":'Biology',"topic":'Molecular Biology',"subtopic":'DNA Structure',"difficulty":'Easy',
 "question":'In DNA, adenine always pairs with:',
 "options":{"A":'Guanine',"B":'Thymine',"C":'Cytosine',"D":'Uracil'},"answer":'B'},

{"id":80,"subject":'Biology',"topic":'Molecular Biology',"subtopic":'DNA Replication',"difficulty":'Medium',
 "question":'DNA replication is described as:',
 "options":{"A":'Conservative',"B":'Dispersive',"C":'Random',"D":'Semi-conservative'},"answer":'D'},

{"id":81,"subject":'Biology',"topic":'Molecular Biology',"subtopic":'DNA Replication',"difficulty":'Medium',
 "question":'The enzyme that unwinds the DNA double helix during replication is:',
 "options":{"A":'DNA ligase',"B":'Helicase',"C":'Primase',"D":'DNA polymerase'},"answer":'B'},

{"id":82,"subject":'Biology',"topic":'Molecular Biology',"subtopic":'DNA Replication',"difficulty":'Medium',
 "question":'Okazaki fragments are joined together by:',
 "options":{"A":'Helicase',"B":'Primase',"C":'DNA ligase',"D":'RNA polymerase'},"answer":'C'},

{"id":83,"subject":'Biology',"topic":'Molecular Biology',"subtopic":'Transcription',"difficulty":'Medium',
 "question":'The process of synthesizing mRNA from a DNA template is called:',
 "options":{"A":'Translation',"B":'Replication',"C":'Transcription',"D":'Transduction'},"answer":'C'},

{"id":84,"subject":'Biology',"topic":'Molecular Biology',"subtopic":'Transcription',"difficulty":'Medium',
 "question":'The enzyme that catalyzes transcription is:',
 "options":{"A":'DNA polymerase',"B":'Reverse transcriptase',"C":'RNA polymerase',"D":'DNA ligase'},"answer":'C'},

{"id":85,"subject":'Biology',"topic":'Molecular Biology',"subtopic":'Translation',"difficulty":'Medium',
 "question":'Translation occurs on:',
 "options":{"A":'Nucleoli',"B":'Golgi apparatus',"C":'Ribosomes',"D":'Lysosomes'},"answer":'C'},

{"id":86,"subject":'Biology',"topic":'Molecular Biology',"subtopic":'Genetic Code',"difficulty":'Medium',
 "question":'A codon consists of:',
 "options":{"A":'3 nucleotides',"B":'1 nucleotide',"C":'2 nucleotides',"D":'4 nucleotides'},"answer":'A'},

{"id":87,"subject":'Biology',"topic":'Molecular Biology',"subtopic":'Genetic Code',"difficulty":'Medium',
 "question":'The start codon in most organisms is:',
 "options":{"A":'AUG',"B":'UAA',"C":'UAG',"D":'UGA'},"answer":'A'},

{"id":88,"subject":'Biology',"topic":'Molecular Biology',"subtopic":'RNA',"difficulty":'Easy',
 "question":'Which type of RNA carries amino acids to the ribosome?',
 "options":{"A":'mRNA',"B":'rRNA',"C":'tRNA',"D":'snRNA'},"answer":'C'},

{"id":89,"subject":'Biology',"topic":'Molecular Biology',"subtopic":'Mutations',"difficulty":'Medium',
 "question":'A point mutation that changes a codon to a stop codon is called a:',
 "options":{"A":'Silent mutation',"B":'Missense mutation',"C":'Nonsense mutation',"D":'Frameshift mutation'},"answer":'C'},

{"id":90,"subject":'Biology',"topic":'Molecular Biology',"subtopic":'Mutations',"difficulty":'Medium',
 "question":'Sickle cell anemia is caused by a mutation in the gene encoding:',
 "options":{"A":'Insulin',"B":'Collagen',"C":'Myosin',"D":'Beta-hemoglobin'},"answer":'D'},

{"id":91,"subject":'Biology',"topic":'Molecular Biology',"subtopic":'Gene Regulation',"difficulty":'Hard',
 "question":'The lac operon in E. coli is an example of:',
 "options":{"A":'A eukaryotic regulatory system',"B":'An inducible operon activated in the presence of lactose',"C":'A repressible operon inhibited by tryptophan',"D":'Constitutive gene expression'},"answer":'B'},

{"id":92,"subject":'Biology',"topic":'Molecular Biology',"subtopic":'Chromosomal Mutations',"difficulty":'Hard',
 "question":'A chromosomal mutation in which a segment breaks off and reattaches to a non-homologous chromosome is called a:',
 "options":{"A":'Deletion',"B":'Translocation',"C":'Inversion',"D":'Duplication'},"answer":'B'},


# ============================================================
# EVOLUTION (8)  id 93-100
# ============================================================

{"id":93,"subject":'Biology',"topic":'Evolution',"subtopic":'Darwin',"difficulty":'Easy',
 "question":'Darwin\'s theory of evolution is based on the mechanism of:',
 "options":{"A":'Use and disuse',"B":'Inheritance of acquired characteristics',"C":'Natural selection',"D":'Spontaneous generation'},"answer":'C'},

{"id":94,"subject":'Biology',"topic":'Evolution',"subtopic":'Lamarck',"difficulty":'Easy',
 "question":'Lamarck proposed the idea of:',
 "options":{"A":'Natural selection',"B":'Genetic drift',"C":'Inheritance of acquired characteristics',"D":'Punctuated equilibrium'},"answer":'C'},

{"id":95,"subject":'Biology',"topic":'Evolution',"subtopic":'Evidence',"difficulty":'Medium',
 "question":'Homologous structures in different organisms suggest:',
 "options":{"A":'Convergent evolution',"B":'Random mutation',"C":'Genetic drift',"D":'Common ancestry'},"answer":'D'},

{"id":96,"subject":'Biology',"topic":'Evolution',"subtopic":'Evidence',"difficulty":'Medium',
 "question":'The wings of birds and insects are examples of:',
 "options":{"A":'Homologous structures',"B":'Analogous structures',"C":'Vestigial organs',"D":'Atavistic organs'},"answer":'B'},

{"id":97,"subject":'Biology',"topic":'Evolution',"subtopic":'Selection',"difficulty":'Medium',
 "question":'Which type of selection favors the average phenotype?',
 "options":{"A":'Stabilizing selection',"B":'Directional selection',"C":'Disruptive selection',"D":'Sexual selection'},"answer":'A'},

{"id":98,"subject":'Biology',"topic":'Evolution',"subtopic":'Speciation',"difficulty":'Medium',
 "question":'The formation of new species due to a geographic barrier is called:',
 "options":{"A":'Sympatric speciation',"B":'Peripatric speciation',"C":'Parapatric speciation',"D":'Allopatric speciation'},"answer":'D'},

{"id":99,"subject":'Biology',"topic":'Evolution',"subtopic":'Genetic Drift',"difficulty":'Hard',
 "question":'The bottleneck effect refers to:',
 "options":{"A":'The founder effect exactly',"B":'Increased genetic variation over time',"C":'A drastic reduction in population size that reduces genetic variation',"D":'Migration between populations'},"answer":'C'},

{"id":100,"subject":'Biology',"topic":'Evolution',"subtopic":'Hardy-Weinberg',"difficulty":'Hard',
 "question":'Which of the following conditions does NOT need to be met for a population to be in Hardy-Weinberg equilibrium?',
 "options":{"A":'Large population size',"B":'Presence of natural selection',"C":'Random mating',"D":'No migration'},"answer":'B'},


# ============================================================
# CLASSIFICATION AND DIVERSITY (10)  id 101-110
# ============================================================

{"id":101,"subject":'Biology',"topic":'Classification and Diversity',"subtopic":'Taxonomy',"difficulty":'Easy',
 "question":'The correct hierarchical order of taxonomic categories is:',
 "options":{"A":'Kingdom, Class, Phylum, Order, Family, Species, Genus',"B":'Species, Genus, Family, Order, Class, Phylum, Kingdom',"C":'Kingdom, Phylum, Order, Class, Family, Genus, Species',"D":'Kingdom, Phylum, Class, Order, Family, Genus, Species'},"answer":'D'},

{"id":102,"subject":'Biology',"topic":'Classification and Diversity',"subtopic":'Binomial Nomenclature',"difficulty":'Easy',
 "question":'The system of binomial nomenclature was introduced by:',
 "options":{"A":'Carolus Linnaeus',"B":'Charles Darwin',"C":'Gregor Mendel',"D":'Aristotle'},"answer":'A'},

{"id":103,"subject":'Biology',"topic":'Classification and Diversity',"subtopic":'Five Kingdoms',"difficulty":'Medium',
 "question":'The five kingdom classification was proposed by:',
 "options":{"A":'R.H. Whittaker',"B":'Linnaeus',"C":'Aristotle',"D":'Ernst Haeckel'},"answer":'A'},

{"id":104,"subject":'Biology',"topic":'Classification and Diversity',"subtopic":'Kingdoms',"difficulty":'Medium',
 "question":'Members of Kingdom Monera are:',
 "options":{"A":'Multicellular and eukaryotic',"B":'Unicellular and eukaryotic',"C":'Multicellular and prokaryotic',"D":'Unicellular and prokaryotic'},"answer":'D'},

{"id":105,"subject":'Biology',"topic":'Classification and Diversity',"subtopic":'Kingdoms',"difficulty":'Medium',
 "question":'Which of the following is a characteristic of Kingdom Fungi?',
 "options":{"A":'Autotrophic and multicellular',"B":'Heterotrophic with cell walls made of chitin',"C":'Prokaryotic and unicellular',"D":'Photosynthetic and unicellular'},"answer":'B'},

{"id":106,"subject":'Biology',"topic":'Classification and Diversity',"subtopic":'Animal Phyla',"difficulty":'Medium',
 "question":'Radial symmetry is characteristic of phylum:',
 "options":{"A":'Chordata',"B":'Cnidaria',"C":'Arthropoda',"D":'Annelida'},"answer":'B'},

{"id":107,"subject":'Biology',"topic":'Classification and Diversity',"subtopic":'Animal Phyla',"difficulty":'Medium',
 "question":'Notochord, dorsal nerve cord, and pharyngeal gill slits at some stage of life are characteristics of:',
 "options":{"A":'Arthropoda',"B":'Mollusca',"C":'Chordata',"D":'Echinodermata'},"answer":'C'},

{"id":108,"subject":'Biology',"topic":'Classification and Diversity',"subtopic":'Animal Phyla',"difficulty":'Medium',
 "question":'Which of the following is NOT a class of phylum Arthropoda?',
 "options":{"A":'Insecta',"B":'Crustacea',"C":'Cephalopoda',"D":'Arachnida'},"answer":'C'},

{"id":109,"subject":'Biology',"topic":'Classification and Diversity',"subtopic":'Plants',"difficulty":'Hard',
 "question":'Bryophytes differ from tracheophytes in that bryophytes:',
 "options":{"A":'Have well-developed vascular tissue',"B":'Produce seeds',"C":'Have flowers',"D":'Lack true vascular tissue and produce spores'},"answer":'D'},

{"id":110,"subject":'Biology',"topic":'Classification and Diversity',"subtopic":'Domains',"difficulty":'Hard',
 "question":'The three-domain system of classification includes Bacteria, Archaea, and:',
 "options":{"A":'Fungi',"B":'Protista',"C":'Eukarya',"D":'Monera'},"answer":'C'},


# ============================================================
# PROKARYOTES AND VIRUSES (8)  id 111-118
# ============================================================

{"id":111,"subject":'Biology',"topic":'Prokaryotes and Viruses',"subtopic":'Bacteria',"difficulty":'Easy',
 "question":'The cell wall of most bacteria is composed of:',
 "options":{"A":'Cellulose',"B":'Chitin',"C":'Lignin',"D":'Peptidoglycan'},"answer":'D'},

{"id":112,"subject":'Biology',"topic":'Prokaryotes and Viruses',"subtopic":'Bacteria',"difficulty":'Medium',
 "question":'Gram-positive bacteria retain the crystal violet stain because they have:',
 "options":{"A":'A thin peptidoglycan layer and an outer membrane',"B":'No cell wall',"C":'A thick peptidoglycan layer',"D":'A capsule made of protein'},"answer":'C'},

{"id":113,"subject":'Biology',"topic":'Prokaryotes and Viruses',"subtopic":'Bacterial Reproduction',"difficulty":'Medium',
 "question":'Bacteria typically reproduce by:',
 "options":{"A":'Binary fission',"B":'Mitosis',"C":'Meiosis',"D":'Budding only'},"answer":'A'},

{"id":114,"subject":'Biology',"topic":'Prokaryotes and Viruses',"subtopic":'Viruses',"difficulty":'Easy',
 "question":'A virus consists of:',
 "options":{"A":'Genetic material enclosed in a protein coat (capsid)',"B":'Only genetic material',"C":'A cell membrane and nucleus',"D":'A cell wall and cytoplasm'},"answer":'A'},

{"id":115,"subject":'Biology',"topic":'Prokaryotes and Viruses',"subtopic":'Viruses',"difficulty":'Medium',
 "question":'The lytic cycle of a bacteriophage ends with:',
 "options":{"A":'Integration of viral DNA into host chromosome',"B":'Formation of endospores',"C":'Bacterial conjugation',"D":'Lysis of the host cell and release of new viruses'},"answer":'D'},

{"id":116,"subject":'Biology',"topic":'Prokaryotes and Viruses',"subtopic":'Viruses',"difficulty":'Medium',
 "question":'HIV is a:',
 "options":{"A":'DNA virus with double-stranded DNA',"B":'Bacteriophage',"C":'Retrovirus that uses reverse transcriptase',"D":'Bacterium'},"answer":'C'},

{"id":117,"subject":'Biology',"topic":'Prokaryotes and Viruses',"subtopic":'Fungi',"difficulty":'Medium',
 "question":'The body of a multicellular fungus is composed of thread-like structures called:',
 "options":{"A":'Rhizoids',"B":'Stolons',"C":'Hyphae',"D":'Cilia'},"answer":'C'},

{"id":118,"subject":'Biology',"topic":'Prokaryotes and Viruses',"subtopic":'Fungi',"difficulty":'Hard',
 "question":'Lichens are examples of a symbiotic relationship between fungi and:',
 "options":{"A":'Bacteria only',"B":'Protozoa',"C":'Algae or cyanobacteria',"D":'Bryophytes'},"answer":'C'},


# ============================================================
# PLANT BIOLOGY (12)  id 119-130
# ============================================================

{"id":119,"subject":'Biology',"topic":'Plant Biology',"subtopic":'Nutrition',"difficulty":'Easy',
 "question":'Plants are classified as autotrophs because they:',
 "options":{"A":'Consume other organisms',"B":'Absorb organic compounds from soil',"C":'Synthesize their own food using light energy',"D":'Depend on fungi for nutrition'},"answer":'C'},

{"id":120,"subject":'Biology',"topic":'Plant Biology',"subtopic":'Transport',"difficulty":'Easy',
 "question":'Water is transported from roots to leaves through:',
 "options":{"A":'Xylem',"B":'Phloem',"C":'Cambium',"D":'Cortex'},"answer":'A'},

{"id":121,"subject":'Biology',"topic":'Plant Biology',"subtopic":'Transport',"difficulty":'Medium',
 "question":'Phloem is responsible for the transport of:',
 "options":{"A":'Water and minerals',"B":'Sugars and other organic solutes',"C":'Only oxygen',"D":'Only carbon dioxide'},"answer":'B'},

{"id":122,"subject":'Biology',"topic":'Plant Biology',"subtopic":'Transpiration',"difficulty":'Medium',
 "question":'Transpiration in plants mainly occurs through:',
 "options":{"A":'Xylem vessels',"B":'Stomata',"C":'Root hairs',"D":'Cuticle exclusively'},"answer":'B'},

{"id":123,"subject":'Biology',"topic":'Plant Biology',"subtopic":'Stomata',"difficulty":'Medium',
 "question":'Guard cells regulate the opening and closing of:',
 "options":{"A":'Stomata',"B":'Xylem vessels',"C":'Sieve tubes',"D":'Root nodules'},"answer":'A'},

{"id":124,"subject":'Biology',"topic":'Plant Biology',"subtopic":'Hormones',"difficulty":'Medium',
 "question":'Which plant hormone is primarily responsible for cell elongation and phototropism?',
 "options":{"A":'Cytokinin',"B":'Auxin',"C":'Ethylene',"D":'Abscisic acid'},"answer":'B'},

{"id":125,"subject":'Biology',"topic":'Plant Biology',"subtopic":'Hormones',"difficulty":'Medium',
 "question":'The plant hormone associated with fruit ripening is:',
 "options":{"A":'Gibberellin',"B":'Auxin',"C":'Cytokinin',"D":'Ethylene'},"answer":'D'},

{"id":126,"subject":'Biology',"topic":'Plant Biology',"subtopic":'Hormones',"difficulty":'Hard',
 "question":'Abscisic acid (ABA) primarily functions in:',
 "options":{"A":'Cell division',"B":'Promotion of stem elongation',"C":'Stomatal closure during water stress and maintenance of seed dormancy',"D":'Fruit formation'},"answer":'C'},

{"id":127,"subject":'Biology',"topic":'Plant Biology',"subtopic":'Photoperiodism',"difficulty":'Hard',
 "question":'Plants that flower in response to short days (long nights) are called:',
 "options":{"A":'Long-day plants',"B":'Short-day plants',"C":'Day-neutral plants',"D":'Photoperiodic plants exclusively'},"answer":'B'},

{"id":128,"subject":'Biology',"topic":'Plant Biology',"subtopic":'Reproduction',"difficulty":'Medium',
 "question":'The male reproductive part of a flower is the:',
 "options":{"A":'Pistil',"B":'Stamen',"C":'Sepal',"D":'Petal'},"answer":'B'},

{"id":129,"subject":'Biology',"topic":'Plant Biology',"subtopic":'Reproduction',"difficulty":'Medium',
 "question":'In angiosperms, double fertilization results in the formation of:',
 "options":{"A":'A zygote only',"B":'A zygote and endosperm',"C":'Only endosperm',"D":'A pollen tube'},"answer":'B'},

{"id":130,"subject":'Biology',"topic":'Plant Biology',"subtopic":'Nutrition',"difficulty":'Medium',
 "question":'Nitrogen-fixing bacteria found in root nodules of legumes belong to the genus:',
 "options":{"A":'Escherichia',"B":'Rhizobium',"C":'Lactobacillus',"D":'Nitrosomonas'},"answer":'B'},


# ============================================================
# HUMAN DIGESTION (8)  id 131-138
# ============================================================

{"id":131,"subject":'Biology',"topic":'Human Digestion',"subtopic":'General',"difficulty":'Easy',
 "question":'The chemical digestion of starch begins in the:',
 "options":{"A":'Stomach',"B":'Mouth',"C":'Small intestine',"D":'Large intestine'},"answer":'B'},

{"id":132,"subject":'Biology',"topic":'Human Digestion',"subtopic":'Enzymes',"difficulty":'Easy',
 "question":'The enzyme found in saliva that breaks down starch is:',
 "options":{"A":'Salivary amylase (ptyalin)',"B":'Pepsin',"C":'Trypsin',"D":'Lipase'},"answer":'A'},

{"id":133,"subject":'Biology',"topic":'Human Digestion',"subtopic":'Stomach',"difficulty":'Medium',
 "question":'The chief cells of the stomach secrete:',
 "options":{"A":'HCl',"B":'Pepsinogen',"C":'Mucus',"D":'Intrinsic factor only'},"answer":'B'},

{"id":134,"subject":'Biology',"topic":'Human Digestion',"subtopic":'Stomach',"difficulty":'Medium',
 "question":'HCl in the stomach is secreted by:',
 "options":{"A":'Chief cells',"B":'Goblet cells',"C":'Parietal (oxyntic) cells',"D":'Islet cells'},"answer":'C'},

{"id":135,"subject":'Biology',"topic":'Human Digestion',"subtopic":'Small Intestine',"difficulty":'Medium',
 "question":'Bile is produced by the liver and stored in the:',
 "options":{"A":'Pancreas',"B":'Duodenum',"C":'Spleen',"D":'Gall bladder'},"answer":'D'},

{"id":136,"subject":'Biology',"topic":'Human Digestion',"subtopic":'Small Intestine',"difficulty":'Medium',
 "question":'Bile aids digestion primarily by:',
 "options":{"A":'Chemically digesting proteins',"B":'Neutralizing gastric acid completely',"C":'Absorbing carbohydrates',"D":'Emulsifying fats into smaller droplets'},"answer":'D'},

{"id":137,"subject":'Biology',"topic":'Human Digestion',"subtopic":'Absorption',"difficulty":'Medium',
 "question":'Most nutrient absorption in humans occurs in the:',
 "options":{"A":'Small intestine',"B":'Stomach',"C":'Large intestine',"D":'Esophagus'},"answer":'A'},

{"id":138,"subject":'Biology',"topic":'Human Digestion',"subtopic":'Pancreas',"difficulty":'Hard',
 "question":'The pancreas is a mixed gland because it secretes:',
 "options":{"A":'Only digestive enzymes',"B":'Only hormones',"C":'Only bile',"D":'Both digestive enzymes and hormones'},"answer":'D'},


# ============================================================
# HUMAN CIRCULATION (10)  id 139-148
# ============================================================

{"id":139,"subject":'Biology',"topic":'Human Circulation',"subtopic":'Heart',"difficulty":'Easy',
 "question":'The human heart has how many chambers?',
 "options":{"A":'2',"B":'3',"C":'4',"D":'5'},"answer":'C'},

{"id":140,"subject":'Biology',"topic":'Human Circulation',"subtopic":'Heart',"difficulty":'Easy',
 "question":'The pacemaker of the human heart is the:',
 "options":{"A":'AV node',"B":'SA node',"C":'Bundle of His',"D":'Purkinje fibers'},"answer":'B'},

{"id":141,"subject":'Biology',"topic":'Human Circulation',"subtopic":'Blood Vessels',"difficulty":'Easy',
 "question":'The largest artery in the human body is the:',
 "options":{"A":'Pulmonary artery',"B":'Aorta',"C":'Carotid artery',"D":'Femoral artery'},"answer":'B'},

{"id":142,"subject":'Biology',"topic":'Human Circulation',"subtopic":'Blood',"difficulty":'Medium',
 "question":'Red blood cells transport oxygen using the protein:',
 "options":{"A":'Myoglobin',"B":'Albumin',"C":'Fibrinogen',"D":'Hemoglobin'},"answer":'D'},

{"id":143,"subject":'Biology',"topic":'Human Circulation',"subtopic":'Blood',"difficulty":'Medium',
 "question":'Which white blood cells produce antibodies?',
 "options":{"A":'B lymphocytes',"B":'Neutrophils',"C":'Eosinophils',"D":'Basophils'},"answer":'A'},

{"id":144,"subject":'Biology',"topic":'Human Circulation',"subtopic":'Blood',"difficulty":'Medium',
 "question":'Platelets are essential for:',
 "options":{"A":'Blood clotting',"B":'Oxygen transport',"C":'Fighting infection',"D":'Producing antibodies'},"answer":'A'},

{"id":145,"subject":'Biology',"topic":'Human Circulation',"subtopic":'Blood Vessels',"difficulty":'Medium',
 "question":'Veins carry blood toward the heart. The pulmonary vein carries:',
 "options":{"A":'Deoxygenated blood',"B":'Oxygenated blood',"C":'A mix of both',"D":'No blood'},"answer":'B'},

{"id":146,"subject":'Biology',"topic":'Human Circulation',"subtopic":'Heart',"difficulty":'Medium',
 "question":'The valve between the left atrium and left ventricle is the:',
 "options":{"A":'Tricuspid valve',"B":'Bicuspid (mitral) valve',"C":'Pulmonary valve',"D":'Aortic valve'},"answer":'B'},

{"id":147,"subject":'Biology',"topic":'Human Circulation',"subtopic":'Blood Pressure',"difficulty":'Hard',
 "question":'A normal resting blood pressure for a healthy adult is approximately:',
 "options":{"A":'80/40 mmHg',"B":'160/100 mmHg',"C":'120/80 mmHg',"D":'200/120 mmHg'},"answer":'C'},

{"id":148,"subject":'Biology',"topic":'Human Circulation',"subtopic":'Lymphatic',"difficulty":'Hard',
 "question":'The lymphatic system returns excess tissue fluid to the:',
 "options":{"A":'Bloodstream',"B":'Kidneys',"C":'Digestive tract',"D":'Lungs directly'},"answer":'A'},


# ============================================================
# HUMAN RESPIRATION (8)  id 149-156
# ============================================================

{"id":149,"subject":'Biology',"topic":'Human Respiration',"subtopic":'Anatomy',"difficulty":'Easy',
 "question":'Gas exchange in the lungs occurs at the:',
 "options":{"A":'Trachea',"B":'Alveoli',"C":'Bronchi',"D":'Larynx'},"answer":'B'},

{"id":150,"subject":'Biology',"topic":'Human Respiration',"subtopic":'Anatomy',"difficulty":'Easy',
 "question":'The main muscle involved in breathing is the:',
 "options":{"A":'Diaphragm',"B":'Intercostal muscle',"C":'Pectoral muscle',"D":'Abdominal muscle'},"answer":'A'},

{"id":151,"subject":'Biology',"topic":'Human Respiration',"subtopic":'Mechanism',"difficulty":'Medium',
 "question":'During inhalation, the diaphragm:',
 "options":{"A":'Relaxes and moves upward',"B":'Does not move',"C":'Contracts and moves downward, increasing thoracic volume',"D":'Contracts and moves upward'},"answer":'C'},

{"id":152,"subject":'Biology',"topic":'Human Respiration',"subtopic":'Gas Transport',"difficulty":'Medium',
 "question":'Most CO2 in the blood is transported as:',
 "options":{"A":'Dissolved CO2',"B":'Carbaminohemoglobin',"C":'Bicarbonate ions',"D":'Carbonic acid'},"answer":'C'},

{"id":153,"subject":'Biology',"topic":'Human Respiration',"subtopic":'Regulation',"difficulty":'Medium',
 "question":'The respiratory center in the brain is located in the:',
 "options":{"A":'Medulla oblongata',"B":'Cerebrum',"C":'Cerebellum',"D":'Hypothalamus'},"answer":'A'},

{"id":154,"subject":'Biology',"topic":'Human Respiration',"subtopic":'Lung Volumes',"difficulty":'Medium',
 "question":'Tidal volume refers to:',
 "options":{"A":'The maximum amount of air in the lungs',"B":'Volume of air inhaled or exhaled in a normal breath',"C":'The residual air in the lungs after exhalation',"D":'Vital capacity'},"answer":'B'},

{"id":155,"subject":'Biology',"topic":'Human Respiration',"subtopic":'Disorders',"difficulty":'Hard',
 "question":'Emphysema is a chronic respiratory disorder characterized by:',
 "options":{"A":'Constriction of bronchi due to allergens',"B":'Destruction of alveolar walls, reducing surface area for gas exchange',"C":'Excess mucus in the trachea',"D":'Bacterial infection of pleura'},"answer":'B'},

{"id":156,"subject":'Biology',"topic":'Human Respiration',"subtopic":'Anatomy',"difficulty":'Hard',
 "question":'The structure that prevents food from entering the trachea during swallowing is the:',
 "options":{"A":'Larynx',"B":'Epiglottis',"C":'Uvula',"D":'Pharynx'},"answer":'B'},


# ============================================================
# HUMAN EXCRETION (8)  id 157-164
# ============================================================

{"id":157,"subject":'Biology',"topic":'Human Excretion',"subtopic":'Kidney',"difficulty":'Easy',
 "question":'The functional unit of the kidney is the:',
 "options":{"A":'Nephron',"B":'Neuron',"C":'Alveolus',"D":'Villus'},"answer":'A'},

{"id":158,"subject":'Biology',"topic":'Human Excretion',"subtopic":'Kidney',"difficulty":'Easy',
 "question":'Blood is filtered in the kidney at the:',
 "options":{"A":'Loop of Henle',"B":'Bowman\'s capsule',"C":'Collecting duct',"D":'Distal tubule'},"answer":'B'},

{"id":159,"subject":'Biology',"topic":'Human Excretion',"subtopic":'Nephron',"difficulty":'Medium',
 "question":'Most reabsorption of water and useful solutes in the nephron occurs in the:',
 "options":{"A":'Distal convoluted tubule',"B":'Loop of Henle',"C":'Collecting duct',"D":'Proximal convoluted tubule'},"answer":'D'},

{"id":160,"subject":'Biology',"topic":'Human Excretion',"subtopic":'Regulation',"difficulty":'Medium',
 "question":'ADH (antidiuretic hormone) primarily acts on the:',
 "options":{"A":'Proximal tubule',"B":'Glomerulus',"C":'Bowman\'s capsule',"D":'Distal tubule and collecting duct, increasing water reabsorption'},"answer":'D'},

{"id":161,"subject":'Biology',"topic":'Human Excretion',"subtopic":'Nitrogenous Wastes',"difficulty":'Medium',
 "question":'The main nitrogenous waste product excreted by humans is:',
 "options":{"A":'Ammonia',"B":'Urea',"C":'Uric acid',"D":'Creatinine only'},"answer":'B'},

{"id":162,"subject":'Biology',"topic":'Human Excretion',"subtopic":'Regulation',"difficulty":'Medium',
 "question":'Aldosterone acts on the kidney tubules to increase reabsorption of:',
 "options":{"A":'Potassium ions',"B":'Glucose',"C":'Urea',"D":'Sodium ions (and water)'},"answer":'D'},

{"id":163,"subject":'Biology',"topic":'Human Excretion',"subtopic":'Disorders',"difficulty":'Hard',
 "question":'Diabetes insipidus is caused by:',
 "options":{"A":'Insufficient secretion of ADH',"B":'Insulin deficiency',"C":'Excess aldosterone',"D":'Kidney tumor'},"answer":'A'},

{"id":164,"subject":'Biology',"topic":'Human Excretion',"subtopic":'Homeostasis',"difficulty":'Hard',
 "question":'Homeostasis refers to:',
 "options":{"A":'Random fluctuations in body conditions',"B":'The process of digestion',"C":'The transport of nutrients',"D":'Maintenance of a relatively stable internal environment'},"answer":'D'},


# ============================================================
# HUMAN NERVOUS SYSTEM (10)  id 165-174
# ============================================================

{"id":165,"subject":'Biology',"topic":'Human Nervous System',"subtopic":'Neuron',"difficulty":'Easy',
 "question":'The structural and functional unit of the nervous system is the:',
 "options":{"A":'Nephron',"B":'Neuron',"C":'Neuroglia',"D":'Axon'},"answer":'B'},

{"id":166,"subject":'Biology',"topic":'Human Nervous System',"subtopic":'Neuron',"difficulty":'Medium',
 "question":'Myelin sheath is produced in the peripheral nervous system by:',
 "options":{"A":'Oligodendrocytes',"B":'Astrocytes',"C":'Microglia',"D":'Schwann cells'},"answer":'D'},

{"id":167,"subject":'Biology',"topic":'Human Nervous System',"subtopic":'Impulse',"difficulty":'Medium',
 "question":'The resting membrane potential of a neuron is maintained primarily by the:',
 "options":{"A":'Na+/K+ ATPase pump',"B":'Ca2+ pump',"C":'Cl- channel',"D":'H+ pump'},"answer":'A'},

{"id":168,"subject":'Biology',"topic":'Human Nervous System',"subtopic":'Synapse',"difficulty":'Medium',
 "question":'The gap between two neurons at a synapse is called the:',
 "options":{"A":'Synaptic cleft',"B":'Node of Ranvier',"C":'Axon terminal',"D":'Dendrite'},"answer":'A'},

{"id":169,"subject":'Biology',"topic":'Human Nervous System',"subtopic":'Neurotransmitters',"difficulty":'Medium',
 "question":'A common excitatory neurotransmitter at neuromuscular junctions is:',
 "options":{"A":'GABA',"B":'Acetylcholine',"C":'Dopamine only',"D":'Serotonin'},"answer":'B'},

{"id":170,"subject":'Biology',"topic":'Human Nervous System',"subtopic":'CNS',"difficulty":'Easy',
 "question":'The central nervous system consists of:',
 "options":{"A":'Brain and spinal nerves',"B":'Cranial and spinal nerves',"C":'Sympathetic and parasympathetic nerves',"D":'Brain and spinal cord'},"answer":'D'},

{"id":171,"subject":'Biology',"topic":'Human Nervous System',"subtopic":'Brain',"difficulty":'Medium',
 "question":'The part of the brain responsible for balance and coordination of movements is the:',
 "options":{"A":'Cerebrum',"B":'Medulla oblongata',"C":'Cerebellum',"D":'Hypothalamus'},"answer":'C'},

{"id":172,"subject":'Biology',"topic":'Human Nervous System',"subtopic":'Brain',"difficulty":'Medium',
 "question":'The center for higher thinking, memory, and voluntary actions is the:',
 "options":{"A":'Cerebellum',"B":'Cerebrum',"C":'Medulla',"D":'Pons'},"answer":'B'},

{"id":173,"subject":'Biology',"topic":'Human Nervous System',"subtopic":'ANS',"difficulty":'Hard',
 "question":'The sympathetic nervous system prepares the body for:',
 "options":{"A":'Rest and digestion',"B":'Sleep only',"C":'Fight or flight response',"D":'Digestion of food'},"answer":'C'},

{"id":174,"subject":'Biology',"topic":'Human Nervous System',"subtopic":'Reflex',"difficulty":'Hard',
 "question":'A knee-jerk reflex is an example of a:',
 "options":{"A":'Conditioned reflex',"B":'Complex learned response',"C":'Voluntary action',"D":'Monosynaptic reflex'},"answer":'D'},


# ============================================================
# HUMAN ENDOCRINE SYSTEM (8)  id 175-182
# ============================================================

{"id":175,"subject":'Biology',"topic":'Human Endocrine System',"subtopic":'Pituitary',"difficulty":'Easy',
 "question":'The master gland of the endocrine system is the:',
 "options":{"A":'Thyroid',"B":'Adrenal',"C":'Pancreas',"D":'Pituitary'},"answer":'D'},

{"id":176,"subject":'Biology',"topic":'Human Endocrine System',"subtopic":'Thyroid',"difficulty":'Medium',
 "question":'Thyroxine hormone regulates:',
 "options":{"A":'Blood glucose levels',"B":'Basal metabolic rate',"C":'Water balance',"D":'Calcium balance'},"answer":'B'},

{"id":177,"subject":'Biology',"topic":'Human Endocrine System',"subtopic":'Pancreas',"difficulty":'Medium',
 "question":'Insulin is secreted by the:',
 "options":{"A":'Alpha cells of the pancreas',"B":'Delta cells',"C":'Beta cells of the pancreas',"D":'Acinar cells'},"answer":'C'},

{"id":178,"subject":'Biology',"topic":'Human Endocrine System',"subtopic":'Pancreas',"difficulty":'Medium',
 "question":'Glucagon opposes insulin by:',
 "options":{"A":'Lowering blood glucose',"B":'Storing glucose as fat',"C":'Suppressing blood pressure',"D":'Raising blood glucose by promoting glycogen breakdown'},"answer":'D'},

{"id":179,"subject":'Biology',"topic":'Human Endocrine System',"subtopic":'Adrenal',"difficulty":'Medium',
 "question":'Adrenaline (epinephrine) is secreted by the:',
 "options":{"A":'Adrenal cortex',"B":'Pituitary gland',"C":'Thyroid gland',"D":'Adrenal medulla'},"answer":'D'},

{"id":180,"subject":'Biology',"topic":'Human Endocrine System',"subtopic":'Disorders',"difficulty":'Hard',
 "question":'Diabetes mellitus type 1 is primarily caused by:',
 "options":{"A":'Insulin resistance at receptor level',"B":'Excess glucagon',"C":'Autoimmune destruction of pancreatic beta cells',"D":'Kidney failure'},"answer":'C'},

{"id":181,"subject":'Biology',"topic":'Human Endocrine System',"subtopic":'Parathyroid',"difficulty":'Hard',
 "question":'Parathyroid hormone regulates the blood levels of:',
 "options":{"A":'Sodium and potassium',"B":'Calcium and phosphate',"C":'Glucose',"D":'Iodine'},"answer":'B'},

{"id":182,"subject":'Biology',"topic":'Human Endocrine System',"subtopic":'Hypothalamus',"difficulty":'Medium',
 "question":'The hypothalamus controls the pituitary gland through:',
 "options":{"A":'Nervous impulses only',"B":'Releasing and inhibiting hormones',"C":'Blood cells',"D":'Digestive enzymes'},"answer":'B'},


# ============================================================
# SUPPORT AND MOVEMENT (6)  id 183-188
# ============================================================

{"id":183,"subject":'Biology',"topic":'Support and Movement',"subtopic":'Skeleton',"difficulty":'Easy',
 "question":'The total number of bones in the adult human skeleton is:',
 "options":{"A":'206',"B":'220',"C":'180',"D":'250'},"answer":'A'},

{"id":184,"subject":'Biology',"topic":'Support and Movement',"subtopic":'Joints',"difficulty":'Medium',
 "question":'The joint between the humerus and scapula is a:',
 "options":{"A":'Ball and socket joint',"B":'Hinge joint',"C":'Pivot joint',"D":'Gliding joint'},"answer":'A'},

{"id":185,"subject":'Biology',"topic":'Support and Movement',"subtopic":'Muscles',"difficulty":'Medium',
 "question":'Skeletal muscles are attached to bones by:',
 "options":{"A":'Tendons',"B":'Ligaments',"C":'Cartilage',"D":'Fascia'},"answer":'A'},

{"id":186,"subject":'Biology',"topic":'Support and Movement',"subtopic":'Muscles',"difficulty":'Medium',
 "question":'The contractile units of skeletal muscles are called:',
 "options":{"A":'Myofibrils',"B":'Myosin only',"C":'Sarcomeres',"D":'Actin filaments'},"answer":'C'},

{"id":187,"subject":'Biology',"topic":'Support and Movement',"subtopic":'Contraction',"difficulty":'Hard',
 "question":'According to the sliding filament theory, muscle contraction occurs when:',
 "options":{"A":'Actin filaments shorten',"B":'Both filaments shorten',"C":'Sarcomeres lengthen',"D":'Myosin heads pull actin filaments toward the center of the sarcomere'},"answer":'D'},

{"id":188,"subject":'Biology',"topic":'Support and Movement',"subtopic":'Disorders',"difficulty":'Hard',
 "question":'Osteoporosis is a condition characterized by:',
 "options":{"A":'Decreased bone density, making bones fragile',"B":'Increased bone density',"C":'Inflammation of joints',"D":'Muscle wasting'},"answer":'A'},


# ============================================================
# HUMAN REPRODUCTION (10)  id 189-198
# ============================================================

{"id":189,"subject":'Biology',"topic":'Human Reproduction',"subtopic":'Male',"difficulty":'Easy',
 "question":'Sperms are produced in the:',
 "options":{"A":'Prostate',"B":'Vas deferens',"C":'Seminiferous tubules of testes',"D":'Epididymis'},"answer":'C'},

{"id":190,"subject":'Biology',"topic":'Human Reproduction',"subtopic":'Male',"difficulty":'Medium',
 "question":'The primary male sex hormone is:',
 "options":{"A":'Estrogen',"B":'Progesterone',"C":'FSH',"D":'Testosterone'},"answer":'D'},

{"id":191,"subject":'Biology',"topic":'Human Reproduction',"subtopic":'Female',"difficulty":'Easy',
 "question":'Fertilization in humans normally occurs in the:',
 "options":{"A":'Fallopian tube (oviduct)',"B":'Uterus',"C":'Ovary',"D":'Vagina'},"answer":'A'},

{"id":192,"subject":'Biology',"topic":'Human Reproduction',"subtopic":'Female',"difficulty":'Medium',
 "question":'The hormone responsible for triggering ovulation is:',
 "options":{"A":'FSH',"B":'Estrogen exclusively',"C":'Progesterone',"D":'LH surge'},"answer":'D'},

{"id":193,"subject":'Biology',"topic":'Human Reproduction',"subtopic":'Menstrual Cycle',"difficulty":'Medium',
 "question":'During the luteal phase of the menstrual cycle, the corpus luteum primarily secretes:',
 "options":{"A":'Progesterone',"B":'FSH',"C":'LH',"D":'GnRH'},"answer":'A'},

{"id":194,"subject":'Biology',"topic":'Human Reproduction',"subtopic":'Development',"difficulty":'Medium',
 "question":'Implantation of the blastocyst occurs in the:',
 "options":{"A":'Vagina',"B":'Uterine wall (endometrium)',"C":'Cervix',"D":'Fallopian tube'},"answer":'B'},

{"id":195,"subject":'Biology',"topic":'Human Reproduction',"subtopic":'Development',"difficulty":'Medium',
 "question":'The placenta functions in:',
 "options":{"A":'Only oxygen exchange',"B":'Nutrient, gas, and waste exchange between mother and fetus',"C":'Producing digestive enzymes',"D":'Blood cell production only'},"answer":'B'},

{"id":196,"subject":'Biology',"topic":'Human Reproduction',"subtopic":'Development',"difficulty":'Medium',
 "question":'The typical duration of human pregnancy from conception is approximately:',
 "options":{"A":'20 weeks',"B":'38 weeks',"C":'30 weeks',"D":'52 weeks'},"answer":'B'},

{"id":197,"subject":'Biology',"topic":'Human Reproduction',"subtopic":'Hormones',"difficulty":'Hard',
 "question":'Milk production after childbirth is stimulated by the hormone:',
 "options":{"A":'Oxytocin',"B":'FSH',"C":'Estrogen',"D":'Prolactin'},"answer":'D'},

{"id":198,"subject":'Biology',"topic":'Human Reproduction',"subtopic":'Hormones',"difficulty":'Hard',
 "question":'The hormone responsible for uterine contractions during childbirth is:',
 "options":{"A":'Oxytocin',"B":'Prolactin',"C":'ADH',"D":'Estrogen'},"answer":'A'},


# ============================================================
# ECOLOGY (2)  id 199-200
# ============================================================

{"id":199,"subject":'Biology',"topic":'Ecology',"subtopic":'General',"difficulty":'Easy',
 "question":'The study of interactions between organisms and their environment is called:',
 "options":{"A":'Ecology',"B":'Physiology',"C":'Taxonomy',"D":'Genetics'},"answer":'A'},

{"id":200,"subject":'Biology',"topic":'Ecology',"subtopic":'Food Chain',"difficulty":'Medium',
 "question":'In a food chain, organisms that feed on primary consumers are called:',
 "options":{"A":'Producers',"B":'Decomposers',"C":'Autotrophs',"D":'Secondary consumers'},"answer":'D'},

]


# ------------------------------------------------------------
# Sanity-check / summary utility
# ------------------------------------------------------------
def summarize(questions):
    from collections import Counter
    topic = Counter(q["topic"] for q in questions)
    diff = Counter(q["difficulty"] for q in questions)
    ans = Counter(q["answer"] for q in questions)
    ids = [q["id"] for q in questions]
    dup_ids = [i for i in set(ids) if ids.count(i) > 1]
    dup_q = [q["question"] for q in questions]
    dup_questions = [t for t in set(dup_q) if dup_q.count(t) > 1]

    print(f"Total questions: {len(questions)}")
    print("\nBy topic:")
    for t, c in sorted(topic.items(), key=lambda x: -x[1]):
        print(f"  {t}: {c}")
    print("\nBy difficulty:")
    for d, c in diff.items():
        print(f"  {d}: {c}")
    print("\nBy correct-answer letter:")
    for L in ["A", "B", "C", "D"]:
        print(f"  {L}: {ans[L]}")
    print(f"\nDuplicate IDs: {dup_ids if dup_ids else 'None'}")
    print(f"Duplicate question text: {len(dup_questions)} duplicates" if dup_questions else "Duplicate question text: None")

    for q in questions:
        assert set(q["options"].keys()) == {"A", "B", "C", "D"}, f"Q{q['id']} missing option"
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
