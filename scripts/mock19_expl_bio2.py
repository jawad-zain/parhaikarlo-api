import json
from pathlib import Path

EXPL = {
8165: dict(
    short="A promoter is the DNA site where RNA polymerase binds to start transcription.",
    long="A promoter is a specific DNA sequence located upstream of a gene that RNA polymerase (with associated factors) recognizes and binds to, positioning it correctly to initiate transcription.",
    trick="A promoter does not code for protein itself — it's a regulatory/binding sequence, not a coding sequence.",
    options=dict(a="Correct — the promoter is RNA polymerase's binding site to start transcription.",
                 b="Coding for a specific protein describes an exon/gene's coding sequence, not the promoter.",
                 c="Splicing introns is done by the spliceosome on pre-mRNA, unrelated to the promoter.",
                 d="A terminator sequence ends transcription; the promoter starts it.")
),
8166: dict(
    short="AUG is a start codon, not a stop codon.",
    long="The three stop codons in the standard genetic code are UAA, UAG, and UGA. AUG is actually the START codon (coding for methionine), not a stop codon.",
    trick="AUG is a very common distractor in 'which is NOT a stop codon' questions specifically because it's the START codon — an easy trap if you just recognize it as 'a codon' without checking its role.",
    options=dict(a="Correct — AUG is the START codon (Met), not one of the three stop codons.",
                 b="UAA is indeed one of the three standard stop codons.",
                 c="UAG is indeed one of the three standard stop codons.",
                 d="UGA is indeed one of the three standard stop codons.")
),
8167: dict(
    short="Restriction enzymes cut DNA at specific sequences, creating defined-end fragments.",
    long="Restriction enzymes (restriction endonucleases) recognize specific short DNA sequences and cleave the DNA there, producing fragments with defined ends (often 'sticky ends') — essential tools for cloning and genetic engineering.",
    trick="Ligase (not restriction enzymes) is what JOINS DNA fragments — don't mix up the cutting and joining tools of genetic engineering.",
    options=dict(a="Joining DNA fragments is the role of DNA ligase, not restriction enzymes.",
                 b="Correct — restriction enzymes cut DNA at specific recognition sequences.",
                 c="Synthesizing new DNA strands is the role of DNA polymerase.",
                 d="Translating mRNA into protein is done by ribosomes, unrelated to restriction enzymes.")
),
8168: dict(
    short="Natural selection requires heritable variation among individuals.",
    long="For natural selection to act, a population must have heritable variation in traits; individuals with advantageous heritable traits are more likely to survive and reproduce, passing those traits on.",
    trick="Acquired traits (things gained during an individual's lifetime, like a bodybuilder's muscles) are NOT heritable and are not passed to offspring — a classic Lamarckian misconception ruled out by modern evolutionary theory.",
    options=dict(a="Acquired traits are not passed genetically to offspring — this contradicts how natural selection actually works.",
                 b="A constant environment with no selective pressures would not drive selection at all.",
                 c="Correct — heritable variation is essential; selection acts on it.",
                 d="Identical genotypes across all individuals would leave nothing for selection to act upon.")
),
8169: dict(
    short="Directional selection shifts the population toward one phenotypic extreme.",
    long="Directional selection favors individuals at one extreme of a trait's distribution (e.g., larger beak size), causing the population's average trait value to shift in that direction over generations.",
    trick="Don't confuse this with stabilizing selection (favors the average/middle, reduces variation) or disruptive selection (favors both extremes, creating two distinct groups).",
    options=dict(a="Favoring the average phenotype describes stabilizing selection, not directional selection.",
                 b="Correct — directional selection favors and shifts the population toward one extreme.",
                 c="Selection by definition changes allele frequencies, so 'no effect' is wrong.",
                 d="Creating two distinct extreme groups describes disruptive selection, not directional selection.")
),
8170: dict(
    short="Analogous structures (like insect vs bird wings) arise from convergent evolution, not shared ancestry.",
    long="Analogous structures perform similar functions but evolved independently in unrelated lineages facing similar environmental/selective pressures (convergent evolution) — they do not indicate a recent common ancestor, unlike homologous structures.",
    trick="Don't confuse analogous (similar function, independent origin — like insect and bird wings) with homologous (similar structure/origin from a common ancestor, like a bat wing and human arm).",
    options=dict(a="Correct — convergent evolution under similar pressures, without shared ancestry, produces analogous structures.",
                 b="They arise from different genetic pathways in unrelated lineages, not identical ones.",
                 c="Divergent evolution from a common ancestor would make structures homologous, not analogous.",
                 d="Common ancestry is the hallmark of homologous, not analogous, structures.")
),
8171: dict(
    short="With q=0.3, Hardy-Weinberg gives 2pq = 42% heterozygotes.",
    long="Hardy-Weinberg: p + q = 1, so p = 1 - 0.3 = 0.7. Heterozygote frequency = 2pq = 2 × 0.7 × 0.3 = 0.42, i.e. 42% of the population.",
    trick="Don't just square q (that gives homozygous recessive frequency, 9%) or forget the factor of 2 in 2pq — both are common calculation slips.",
    options=dict(a="Correct — 2pq = 2 × 0.7 × 0.3 = 0.42 = 42%.",
                 b="49% would be p² (0.7² = 0.49), the homozygous dominant frequency, not heterozygous.",
                 c="30% is just q itself, not the heterozygote calculation.",
                 d="9% is q² (0.3² = 0.09), the homozygous recessive frequency, not heterozygous.")
),
8172: dict(
    short="Binomial nomenclature gives every species a two-part Latin name.",
    long="Binomial nomenclature (established by Linnaeus) assigns each species a two-part name: genus + species epithet (e.g., Homo sapiens), providing a standardized universal naming system.",
    trick="Cladistics and phylogenetics are about evolutionary relationships/classification methods, not the naming convention itself — don't conflate naming with classification methodology.",
    options=dict(a="Cladistics is a method of classification based on shared derived traits, not the naming system itself.",
                 b="Dichotomous keying is an identification tool using paired choices, not the naming system.",
                 c="Phylogenetics studies evolutionary relationships, not the specific two-part naming convention.",
                 d="Correct — binomial nomenclature is the two-part Latin naming system.")
),
8173: dict(
    short="Protists are a diverse group of mostly unicellular eukaryotes.",
    long="Kingdom Protista is a highly diverse (and somewhat catch-all) group of mostly unicellular eukaryotic organisms, including protozoans, algae, and slime molds — not defined by a single mode of nutrition or cell organization.",
    trick="Protists are NOT exclusively parasitic, exclusively photosynthetic, or multicellular as a rule — the group is defined more by what it isn't (not animal/plant/fungus/bacterium) than one shared trait.",
    options=dict(a="Protists aren't exclusively parasitic; many are free-living, photosynthetic, or otherwise.",
                 b="Protists aren't exclusively multicellular or exclusively photosynthetic; most are unicellular and diverse in nutrition.",
                 c="Correct — Protista is a diverse group of mostly unicellular eukaryotes.",
                 d="Protists are eukaryotic (have a nucleus), not prokaryotic.")
),
8174: dict(
    short="Eukarya are defined by having a true nucleus and membrane-bound organelles.",
    long="The defining feature separating domain Eukarya from Bacteria and Archaea is the presence of a true, membrane-bound nucleus and other membrane-bound organelles (mitochondria, ER, etc.) — Bacteria and Archaea are prokaryotic and lack these.",
    trick="Eukaryotes can be unicellular or multicellular — 'always unicellular' is wrong, and clearly Eukarya are NOT prokaryotic (that description fits Bacteria/Archaea).",
    options=dict(a="Eukaryotes include many multicellular organisms (plants, animals, fungi), not just unicellular ones.",
                 b="Eukarya are NOT prokaryotic — that describes Bacteria and Archaea.",
                 c="This describes Bacteria/Archaea (prokaryotes), the opposite of Eukarya's defining trait.",
                 d="Correct — a true nucleus and membrane-bound organelles define Eukarya.")
),
8175: dict(
    short="Soft body, muscular foot, and often a shell describes phylum Mollusca.",
    long="Phylum Mollusca (snails, clams, octopuses, etc.) is characterized by a soft body typically with a muscular foot for movement, and in many groups a protective calcium carbonate shell.",
    trick="Arthropods have jointed exoskeletons (not soft bodies), and annelids are segmented worms without a shell — the specific combination of 'soft body + muscular foot + shell' points to molluscs.",
    options=dict(a="Arthropods have a hard jointed exoskeleton, the opposite of a soft body.",
                 b="Annelids are segmented worms, typically without a shell or a distinct muscular foot like this.",
                 c="Cnidarians (jellyfish, corals) lack a muscular foot and calcium carbonate shell.",
                 d="Correct — soft body, muscular foot, and often a shell describes Mollusca.")
),
8176: dict(
    short="Phylum is broader than Class but narrower than Kingdom.",
    long="The standard taxonomic hierarchy from broadest to narrowest is: Kingdom > Phylum > Class > Order > Family > Genus > Species. So Phylum sits directly below Kingdom and directly above Class.",
    trick="Memorize the full hierarchy order (King Phillip Came Over For Good Soup) to avoid mixing up which ranks are broader/narrower than which.",
    options=dict(a="Genus is much narrower than Class, near the bottom of the hierarchy.",
                 b="Correct — Phylum sits between Kingdom (broader) and Class (narrower).",
                 c="Order is narrower than Class, not broader.",
                 d="Family is narrower than Class, not broader.")
),
8177: dict(
    short="Mammalia is defined by hair/fur, mammary glands, and typically live birth.",
    long="Class Mammalia is characterized by the presence of hair or fur, mammary glands that produce milk to feed young, and (in most mammals) live birth rather than egg-laying.",
    trick="Feathers and egg-laying describe birds (Aves), and gills/moist-skin respiration describe fish/amphibians — don't mix up the class-defining traits across vertebrate groups.",
    options=dict(a="Gills throughout life describes fish, not mammals.",
                 b="Feathers and universal egg-laying describe birds (Aves), not mammals.",
                 c="Correct — hair/fur, mammary glands, and typically live birth define Mammalia.",
                 d="Moist skin for respiration describes amphibians, not mammals.")
),
8178: dict(
    short="Photosynthetic sugars are transported through the phloem.",
    long="The phloem is the vascular tissue responsible for translocating sugars (like sucrose) produced during photosynthesis from source tissues (leaves) to sink tissues (roots, fruits, growing regions) throughout the plant.",
    trick="Don't confuse phloem (sugar transport, bidirectional) with xylem (water/mineral transport, one-way upward from roots) — a very common MDCAT mix-up.",
    options=dict(a="Correct — phloem transports the sugars made during photosynthesis.",
                 b="The cortex is a tissue layer, not a specialized transport vessel for sugars.",
                 c="The epidermis is the outer protective layer, not a transport tissue.",
                 d="Xylem transports water and minerals upward, not photosynthetic sugars.")
),
8179: dict(
    short="The Calvin cycle occurs in the stroma of the chloroplast.",
    long="The light-independent reactions (Calvin cycle), which fix CO2 into sugars using ATP and NADPH from the light reactions, take place in the stroma — the fluid-filled space surrounding the thylakoids inside the chloroplast.",
    trick="The light-DEPENDENT reactions happen at the thylakoid membrane; the light-INDEPENDENT Calvin cycle happens in the stroma — keep the two locations straight.",
    options=dict(a="The nucleus has no role in the Calvin cycle.",
                 b="The thylakoid membrane is where the light-dependent reactions occur, not the Calvin cycle.",
                 c="Correct — the Calvin cycle (light-independent reactions) occurs in the stroma.",
                 d="The mitochondrial matrix is where the Krebs cycle occurs (cellular respiration), unrelated to photosynthesis.")
),
8180: dict(
    short="A root growing downward due to gravity shows positive gravitropism.",
    long="Gravitropism (geotropism) is a plant's growth response to gravity. Roots growing toward (down, in the direction of) gravity show positive gravitropism, while shoots typically grow away from gravity (negative gravitropism).",
    trick="Don't confuse gravitropism (response to gravity) with phototropism (response to light) — the stimulus here is explicitly gravity, not light.",
    options=dict(a="Correct — growth toward the direction of gravity (downward) is positive gravitropism.",
                 b="Phototropism is a response to light, not gravity, so it's the wrong stimulus category.",
                 c="Thigmotropism is a response to touch/contact, unrelated to gravity.",
                 d="Positive phototropism (toward light) is also the wrong stimulus category — this is about gravity.")
),
8181: dict(
    short="Root-nodule bacteria fix atmospheric nitrogen into a usable (ammonia) form for the plant.",
    long="Nitrogen-fixing bacteria (like Rhizobium) in legume root nodules convert atmospheric N2 (which plants can't use directly) into ammonia (NH3/NH4+), which the plant can incorporate into amino acids and proteins — a mutualistic relationship.",
    trick="These bacteria do NOT photosynthesize for the plant or damage its structure — their specific mutualistic contribution is nitrogen fixation, a distinct chemical process from photosynthesis.",
    options=dict(a="These bacteria form a mutualistic (not damaging) relationship; they don't break down cell walls.",
                 b="Correct — nitrogen fixation converts atmospheric N2 into usable ammonia for the plant.",
                 c="The bacteria don't photosynthesize for the plant; their contribution is nitrogen fixation, a separate process.",
                 d="They don't prevent water absorption; their role is unrelated to water uptake.")
),
8182: dict(
    short="Gibberellins promote stem elongation and seed germination.",
    long="Gibberellins are plant hormones best known for promoting stem/internode elongation and breaking seed dormancy to trigger germination (e.g., by inducing enzymes that mobilize seed food reserves).",
    trick="Don't confuse gibberellins (elongation/germination) with abscisic acid (dormancy, stomatal closure) or ethylene (abscission/ripening) — different hormones have distinct, specific roles.",
    options=dict(a="Root formation is more associated with auxins, not gibberellins specifically.",
                 b="Stomatal closure is a role of abscisic acid, not gibberellins.",
                 c="Leaf abscission is primarily driven by ethylene, not gibberellins.",
                 d="Correct — gibberellins promote stem elongation and stimulate seed germination.")
),
8183: dict(
    short="The stigma is the sticky part of the flower that receives pollen.",
    long="The stigma, at the top of the pistil (female reproductive structure), is typically sticky or feathery to capture and retain pollen grains, allowing pollen tube growth down to the ovary.",
    trick="The anther (male structure, on the stamen) is where pollen is PRODUCED, not received — don't mix up male and female flower parts.",
    options=dict(a="The anther is the male structure that produces pollen, not the receiving structure.",
                 b="Correct — the stigma is the sticky pollen-receiving surface of the pistil.",
                 c="The filament is the stalk supporting the anther, part of the male stamen.",
                 d="The sepal is a protective outer floral leaf, unrelated to receiving pollen.")
),
8184: dict(
    short="Protein digestion begins in the stomach via pepsin.",
    long="While chewing/mechanical digestion starts in the mouth, chemical PROTEIN digestion specifically begins in the stomach, where pepsin (activated from pepsinogen by stomach acid) starts breaking peptide bonds.",
    trick="The mouth digests some carbohydrates (via salivary amylase) but not proteins — protein digestion is stomach-specific in its start, a frequent MDCAT trap.",
    options=dict(a="The large intestine mainly absorbs water; it's not where protein digestion begins.",
                 b="Correct — pepsin in the acidic stomach environment begins protein digestion.",
                 c="The small intestine continues/completes protein digestion (via trypsin etc.), but doesn't begin it.",
                 d="The mouth handles some carbohydrate digestion (amylase), not protein digestion.")
),
8185: dict(
    short="Trypsin (from the pancreas) breaks down proteins in the small intestine.",
    long="Trypsin is a pancreatic protease secreted into the small intestine (as inactive trypsinogen, then activated) that continues protein digestion by cleaving peptide bonds into smaller peptides.",
    trick="Don't confuse trypsin (protein-digesting) with lipase (fat-digesting) or amylase (starch-digesting) — each pancreatic enzyme targets a specific macronutrient.",
    options=dict(a="Correct — trypsin specifically breaks down proteins.",
                 b="Lipids are broken down by lipase, not trypsin.",
                 c="Nucleic acids are broken down by nucleases, not trypsin.",
                 d="Carbohydrates are broken down by amylase, not trypsin.")
),
8186: dict(
    short="Villi and microvilli increase surface area for nutrient absorption.",
    long="The small intestine's lining is folded extensively into villi (finger-like projections) and further into microvilli on each villus cell, dramatically increasing the surface area available for absorbing digested nutrients into the blood/lymph.",
    trick="This is purely about maximizing ABSORPTION surface area — it has nothing to do with acid production (that's the stomach) or slowing digestion.",
    options=dict(a="Correct — villi/microvilli massively increase the absorptive surface area.",
                 b="Stomach acid is produced by gastric glands in the stomach, not intestinal villi.",
                 c="Villi are for absorption, not storage of undigested food.",
                 d="Increasing surface area speeds up absorption; it doesn't slow digestion.")
),
8187: dict(
    short="Lactase deficiency causes difficulty digesting lactose (milk sugar).",
    long="Lactase is the enzyme that breaks down lactose (milk sugar) into glucose and galactose. Insufficient lactase leads to undigested lactose reaching the colon, causing bloating/gas/diarrhea — lactose intolerance.",
    trick="Lactase acts specifically on the disaccharide lactose — not on proteins, fats, or the polysaccharide starch, which require entirely different enzymes.",
    options=dict(a="Protein digestion relies on proteases (pepsin, trypsin), not lactase.",
                 b="Fat digestion relies on lipase, not lactase.",
                 c="Starch digestion relies on amylase, not lactase.",
                 d="Correct — lactase deficiency specifically impairs lactose digestion, causing lactose intolerance.")
),
8188: dict(
    short="The right atrium receives deoxygenated blood returning from the body.",
    long="Deoxygenated blood from the body (via the superior and inferior vena cavae) enters the heart's right atrium first, then passes to the right ventricle, which pumps it to the lungs.",
    trick="Don't confuse the RIGHT side (deoxygenated blood, body → heart → lungs) with the LEFT side (oxygenated blood, lungs → heart → body) — this is one of the most tested heart-anatomy distinctions.",
    options=dict(a="The right ventricle receives blood from the right atrium next, but doesn't directly receive blood from the body itself.",
                 b="The left atrium receives OXYGENATED blood from the lungs, not deoxygenated blood from the body.",
                 c="Correct — the right atrium is the first chamber to receive deoxygenated blood from the body.",
                 d="The left ventricle pumps oxygenated blood to the body; it doesn't receive blood from the body.")
),
8189: dict(
    short="The aorta (structure 4) carries oxygenated blood from the left ventricle to the body.",
    long="The aorta is the largest artery in the body, arising from the left ventricle and carrying freshly oxygenated blood out to systemic circulation. In the labeled diagram, structure 4 is the aorta; structures 1, 2, and 3 are the right atrium, right ventricle, and left atrium respectively.",
    trick="Don't be misled into picking an atrium or the right ventricle just because they're heart chambers too — only the aorta (a great artery, not a chamber) carries oxygenated blood OUT to the whole body.",
    options=dict(a="Correct — Structure 4, the aorta, carries oxygenated blood from the left ventricle to the body.",
                 b="Structure 1, the right atrium, receives deoxygenated blood; it doesn't distribute oxygenated blood to the body.",
                 c="Structure 2, the right ventricle, pumps deoxygenated blood to the lungs, not oxygenated blood to the body.",
                 d="Structure 3, the left atrium, receives oxygenated blood from the lungs but doesn't distribute it to the body directly.")
),
8190: dict(
    short="Systemic circulation carries oxygenated blood to body tissues, returning deoxygenated blood.",
    long="Systemic circulation is the loop that carries oxygenated blood from the left ventricle through the aorta to all body tissues, where gas exchange occurs, and returns deoxygenated blood via the venae cavae to the right atrium.",
    trick="Pulmonary circulation (heart <-> lungs) is the OTHER loop — don't confuse the two circuits; systemic circulation is specifically heart <-> rest of the body.",
    options=dict(a="Carrying blood to the lungs for gas exchange describes pulmonary, not systemic, circulation.",
                 b="Correct — systemic circulation supplies the body's tissues and returns deoxygenated blood.",
                 c="Systemic circulation supplies the WHOLE body, not just the kidneys.",
                 d="Systemic circulation supplies the whole body, not only the brain.")
),
8191: dict(
    short="Lacking a nucleus maximizes internal space in RBCs for hemoglobin, boosting O2 capacity.",
    long="Mammalian red blood cells expel their nucleus during maturation, freeing up internal volume that is instead packed with hemoglobin, maximizing the cell's oxygen-carrying capacity — a specific evolutionary adaptation.",
    trick="This is a functional, purposeful adaptation (more room for hemoglobin), not a random or disadvantageous quirk — don't pick a 'no significance' or 'can't carry oxygen' option.",
    options=dict(a="This has clear functional significance for oxygen transport, not 'no significance.'",
                 b="It doesn't prevent oxygen carrying — the opposite is true; it maximizes hemoglobin space.",
                 c="Correct — more internal space for hemoglobin increases oxygen-carrying capacity.",
                 d="Lacking a nucleus actually prevents RBCs from dividing (no DNA), not allows rapid division.")
),
8192: dict(
    short="The diaphragm changes thoracic cavity volume during breathing.",
    long="The diaphragm, a dome-shaped muscle beneath the lungs, contracts (flattens) to increase thoracic cavity volume during inhalation and relaxes (domes upward) to decrease volume during exhalation, driven by pressure changes per Boyle's law.",
    trick="The bicep and tongue muscles are unrelated to ventilation mechanics — cardiac muscle only pumps the heart, not the lungs' volume changes.",
    options=dict(a="The bicep is an arm muscle, unrelated to breathing mechanics.",
                 b="Correct — the diaphragm's contraction/relaxation changes thoracic cavity volume for breathing.",
                 c="Cardiac muscle powers the heart's pumping, not lung ventilation.",
                 d="The tongue muscle is involved in speech/swallowing, not thoracic volume changes.")
),
8193: dict(
    short="O2 diffuses from alveoli to blood because alveolar O2 concentration is higher.",
    long="Gas exchange in the lungs follows simple diffusion: oxygen concentration (partial pressure) is higher in the alveolar air than in the deoxygenated blood arriving at the lungs, so O2 diffuses down its gradient into the blood.",
    trick="This is passive diffusion, NOT active transport — no ATP pump is needed; the concentration gradient alone drives gas exchange.",
    options=dict(a="There IS a concentration gradient — that's precisely what drives the diffusion.",
                 b="Correct — higher O2 concentration in alveoli than blood drives diffusion into the blood.",
                 c="This reverses the actual gradient direction; alveolar O2 is higher, not lower, than in the blood.",
                 d="Gas exchange here is passive diffusion, not active transport requiring pumps.")
),
8194: dict(
    short="COPD/emphysema damages alveoli, reducing gas-exchange surface area.",
    long="Emphysema (a form of COPD) destroys alveolar walls, merging small alveoli into larger, fewer air sacs. This drastically reduces the total surface area available for gas exchange, impairing oxygen uptake and CO2 removal.",
    trick="COPD makes breathing HARDER by reducing elasticity and surface area — options claiming it 'strengthens' or 'has no impact' are the opposite of the actual pathology.",
    options=dict(a="Correct — alveolar damage in emphysema reduces the gas-exchange surface area.",
                 b="COPD/emphysema actually decreases lung elasticity, not increases it.",
                 c="COPD very much impairs gas exchange; 'no impact' contradicts the disease's core effect.",
                 d="COPD weakens/destroys alveolar walls, it doesn't strengthen them.")
),
8195: dict(
    short="The nephron is the kidney's functional filtering unit.",
    long="The nephron is the structural and functional unit of the kidney, responsible for filtering blood (at the glomerulus/Bowman's capsule) and processing the filtrate through tubules to form urine.",
    trick="Don't confuse nephron (kidney) with neuron (nerve cell) — they sound similar but are completely different structures in different organ systems.",
    options=dict(a="A villus is an intestinal absorptive structure, unrelated to kidney filtration.",
                 b="Correct — the nephron is the kidney's functional filtering/urine-forming unit.",
                 c="A neuron is a nerve cell, easily confused by name with 'nephron' but functionally unrelated.",
                 d="An alveolus is a lung gas-exchange sac, unrelated to kidney function.")
),
8196: dict(
    short="Filtered glucose is normally completely reabsorbed at the proximal convoluted tubule.",
    long="Under normal conditions, all glucose filtered at the glomerulus is actively reabsorbed back into the blood at the proximal convoluted tubule via specific transporters, so healthy urine contains no glucose. (Glucose appears in urine only when blood glucose exceeds the tubule's reabsorption capacity, as in diabetes.)",
    trick="Glucose in urine (glycosuria) is ABNORMAL — under normal physiology it should be virtually 100% reabsorbed, not partially excreted.",
    options=dict(a="Glucose isn't converted to urea; urea comes from amino acid/protein metabolism (deamination), a separate pathway.",
                 b="Glucose is normally NOT excreted in urine at all under healthy conditions.",
                 c="Correct — under normal conditions, filtered glucose is fully reabsorbed at the PCT.",
                 d="Glucose IS freely filtered at the glomerulus (small enough to pass); it's the subsequent reabsorption that recovers it.")
),
8197: dict(
    short="More ADH means more water reabsorption -> concentrated urine, reduced volume.",
    long="Antidiuretic hormone (ADH/vasopressin) increases the permeability of the collecting duct to water, promoting more water reabsorption back into the blood. This results in smaller volumes of more concentrated urine — the body's response to conserve water during dehydration.",
    trick="More ADH means LESS urine (not more) and MORE concentrated urine (not diluted) — the name 'antidiuretic' literally means 'against urine production.'",
    options=dict(a="ADH doesn't completely stop urine formation, just reduces its volume and increases concentration.",
                 b="Increased ADH does change urine concentration significantly (increases it), not 'no change.'",
                 c="This is the opposite effect — more ADH means less dilute urine and LOWER volume, not more.",
                 d="Correct — more ADH causes more water reabsorption, giving concentrated urine and reduced volume.")
),
8198: dict(
    short="The gap between neurons where neurotransmitters are released is the synapse.",
    long="The synapse is the junction between two neurons (or a neuron and effector) where the presynaptic neuron releases neurotransmitters into the synaptic cleft to signal the postsynaptic cell.",
    trick="The myelin sheath insulates the axon for faster conduction; it has nothing to do with the neuron-to-neuron communication gap — don't mix up structural (myelin/dendrite) and functional (synapse) terms.",
    options=dict(a="The myelin sheath insulates the axon; it's not the site of neurotransmitter release.",
                 b="The axon terminal is where neurotransmitter vesicles are stored/released FROM, but the gap itself (junction) is the synapse.",
                 c="Correct — the synapse is the gap/junction where neurotransmitters cross between neurons.",
                 d="Dendrites receive signals; they aren't the gap itself.")
),
8199: dict(
    short="Depolarization is driven by Na+ ions rushing into the neuron.",
    long="During an action potential, voltage-gated sodium channels open in response to a stimulus, allowing Na+ to rush into the neuron down its electrochemical gradient, making the inside more positive (depolarization).",
    trick="Repolarization (the NEXT phase) is driven by K+ ions rushing OUT — don't mix up which ion movement corresponds to which phase of the action potential.",
    options=dict(a="Calcium ion movement is more associated with neurotransmitter release at synapses, not the depolarization phase itself.",
                 b="There IS significant ion movement (Na+ influx) during depolarization; 'no movement' is incorrect.",
                 c="Potassium efflux drives repolarization (the phase AFTER depolarization), not depolarization itself.",
                 d="Correct — Na+ influx through voltage-gated channels causes depolarization.")
),
8200: dict(
    short="Insulin lowers blood glucose by promoting cellular uptake/storage.",
    long="Insulin, secreted by pancreatic beta cells, lowers blood glucose levels by stimulating body cells (especially liver, muscle, fat) to take up glucose from the blood and store it (as glycogen or fat).",
    trick="Glucagon (not insulin) is the hormone that RAISES blood glucose — don't mix up these two antagonistic pancreatic hormones.",
    options=dict(a="The fight-or-flight response is triggered by adrenaline (epinephrine), not insulin.",
                 b="Increasing blood glucose is glucagon's role, the opposite hormone to insulin.",
                 c="Correct — insulin lowers blood glucose by promoting cellular uptake and storage.",
                 d="Calcium regulation is primarily controlled by parathyroid hormone/calcitonin, not insulin.")
),
8201: dict(
    short="Type 1 diabetes results from autoimmune destruction of pancreatic beta cells.",
    long="In Type 1 diabetes, the immune system mistakenly attacks and destroys the insulin-producing beta cells of the pancreas, leading to little or no insulin production and resulting high blood glucose.",
    trick="Type 1 is about a lack of insulin PRODUCTION (autoimmune beta-cell destruction); Type 2 is about insulin RESISTANCE despite normal/high insulin — don't conflate the two types' mechanisms.",
    options=dict(a="Excess salt consumption isn't the cause of Type 1 diabetes.",
                 b="The liver doesn't produce insulin at all (that's the pancreas's job); this option misattributes the source organ.",
                 c="Blood glucose is actually elevated (not low) in untreated Type 1 diabetes, due to insufficient insulin.",
                 d="Correct — autoimmune destruction of pancreatic beta cells is the hallmark cause of Type 1 diabetes.")
),
8202: dict(
    short="Sperm are produced within the seminiferous tubules of the testes.",
    long="Spermatogenesis (sperm production) occurs within the seminiferous tubules inside the testes, where germ cells undergo meiosis to form mature sperm cells.",
    trick="The epididymis STORES and matures sperm after production, and the prostate contributes seminal fluid — neither is the actual site of sperm PRODUCTION, which is the seminiferous tubules.",
    options=dict(a="Correct — sperm are produced within the testes' seminiferous tubules.",
                 b="The prostate gland contributes fluid to semen; it doesn't produce sperm.",
                 c="The epididymis stores and matures sperm after production, it isn't the production site.",
                 d="The urethra is simply the exit duct for sperm/urine, not a production site.")
),
8203: dict(
    short="The LH surge at mid-cycle triggers ovulation.",
    long="A sharp surge in luteinizing hormone (LH) around day 14 of a typical menstrual cycle triggers ovulation — the release of a mature egg from the dominant ovarian follicle.",
    trick="Implantation and placenta formation happen much LATER, only if fertilization occurs — the LH surge's immediate, direct trigger is specifically ovulation, not these downstream pregnancy-related events.",
    options=dict(a="Implantation happens later, only if fertilization occurs, not as a direct LH-surge trigger.",
                 b="Placenta formation is a much later pregnancy event, not triggered directly by the LH surge.",
                 c="Menstruation results from a drop in hormones (if no pregnancy occurs), not the LH surge itself.",
                 d="Correct — the LH surge is the direct trigger for ovulation.")
),
8204: dict(
    short="Organisms making their own organic molecules (e.g. via photosynthesis) are autotrophs.",
    long="Autotrophs (like plants, algae, and photosynthetic bacteria) synthesize their own organic molecules from inorganic sources (like CO2 and water, using light energy), forming the base of most food chains.",
    trick="Heterotrophs (consumers, decomposers) must obtain organic molecules from other organisms — don't confuse them with self-sufficient autotrophs.",
    options=dict(a="Decomposers are a specific type of heterotroph (break down dead matter); this doesn't describe self-nourishing autotrophs.",
                 b="Consumers are heterotrophs that eat other organisms, the opposite of autotrophs.",
                 c="Heterotrophs must obtain organic molecules from external sources, unlike self-sufficient autotrophs.",
                 d="Correct — autotrophs manufacture their own organic molecules from inorganic sources.")
),
8205: dict(
    short="Decreasing energy/biomass at each trophic level is depicted as an ecological pyramid.",
    long="An ecological pyramid (of energy, biomass, or numbers) visually represents how the amount of energy or biomass available typically decreases at each successive trophic level, due to energy loss (as heat, metabolism) between levels (~10% rule).",
    trick="The nitrogen and carbon cycles describe elemental cycling through ecosystems, not the trophic-level energy decrease — and a food web just shows feeding CONNECTIONS, not the quantitative decrease itself.",
    options=dict(a="The nitrogen cycle describes nitrogen's movement through the ecosystem, unrelated to trophic-level energy decline.",
                 b="The carbon cycle describes carbon's movement through the ecosystem, unrelated to trophic-level energy decline.",
                 c="Correct — an ecological pyramid visually depicts the trophic-level decrease in energy/biomass.",
                 d="A food web shows feeding relationships/connections, not specifically the quantitative decrease per level.")
),
}

def main():
    root = Path(__file__).parent.parent
    out = []
    for qid, e in EXPL.items():
        out.append({"id": qid, "short": e["short"], "long": e["long"], "trick": e["trick"], "options": e["options"]})
    out_path = root / "scripts" / "mock19_explanations_biology_2.json"
    out_path.write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Wrote {len(out)} explanations to {out_path}")

if __name__ == "__main__":
    main()
