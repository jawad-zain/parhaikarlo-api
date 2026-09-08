import json
from pathlib import Path

EXPL = {
8345: dict(
    short="A terminator sequence signals RNA polymerase to release the newly made RNA, ending transcription.",
    long="The terminator sequence marks the end of a gene's transcribed region. When RNA polymerase reaches it, transcription stops and the completed RNA transcript is released from the DNA template.",
    trick="Don't confuse a terminator (ends transcription) with a promoter (INITIATES transcription by recruiting RNA polymerase) — these are opposite-function regulatory sequences.",
    options=dict(a="Correct — a terminator sequence signals the end of transcription, releasing the RNA.",
                 b="Initiating transcription is the promoter's role, not the terminator's.",
                 c="Binding ribosomes during translation is unrelated to a DNA terminator sequence's function.",
                 d="Splicing introns is carried out by the spliceosome after transcription, not by the terminator sequence itself.")
),
8346: dict(
    short="AUG is the start codon, also coding for methionine.",
    long="AUG serves the dual role of being the near-universal start codon (signaling the ribosome where to begin translation) while also coding for the amino acid methionine.",
    trick="UAA, UAG, and UGA are all STOP codons (they don't code for any amino acid) — don't confuse these with the START codon AUG.",
    options=dict(a="UAA is a stop codon, not the start codon.",
                 b="Correct — AUG is the start codon, also coding for methionine.",
                 c="UAG is a stop codon, not the start codon.",
                 d="UGA is a stop codon, not the start codon.")
),
8347: dict(
    short="PCR rapidly amplifies a specific DNA segment into many copies.",
    long="Polymerase chain reaction (PCR) uses repeated cycles of heating and cooling with DNA polymerase, primers, and nucleotides to exponentially amplify a targeted DNA segment, producing millions of copies from a tiny starting sample.",
    trick="PCR is specifically about AMPLIFYING (copying) a known/targeted DNA segment — it doesn't sequence an entire genome by itself, nor translate mRNA, nor destroy DNA.",
    options=dict(a="Sequencing an entire genome directly is a separate technique (genome sequencing), not PCR's primary purpose.",
                 b="Translating mRNA into protein in vitro describes an entirely different process (in vitro translation), not PCR.",
                 c="Correct — PCR rapidly amplifies a specific DNA segment into many copies.",
                 d="PCR amplifies (multiplies) DNA; it doesn't destroy DNA samples.")
),
8348: dict(
    short="Natural selection requires a trait to be heritable and affect reproductive success.",
    long="For evolution by natural selection to occur, there must be heritable variation in a population, and that variation must affect differential survival/reproduction — traits that improve reproductive success become more common over generations.",
    trick="Don't think mutations or environmental stability are PREREQUISITES that must be absent — quite the opposite, mutations are actually a key SOURCE of the heritable variation natural selection acts upon.",
    options=dict(a="Mutations must NOT be absent — they're actually a key source of the heritable variation natural selection relies on.",
                 b="Genetic identity across all individuals would eliminate the variation natural selection needs to act on.",
                 c="Environments DO change, and this can actually be what drives shifting selection pressures — it's not a requirement that they stay static.",
                 d="Correct — a heritable trait affecting reproductive success is required for natural selection to act.")
),
8349: dict(
    short="Disruptive selection favors both phenotypic extremes over the intermediate, potentially splitting the population.",
    long="Disruptive (diversifying) selection favors individuals at both extremes of a trait's range while selecting against the intermediate phenotype, which can eventually lead to two distinct phenotype groups (and potentially speciation over time).",
    trick="Don't confuse disruptive selection (favors BOTH extremes) with stabilizing selection (favors the AVERAGE/intermediate, the opposite pattern) or directional selection (favors ONE extreme only).",
    options=dict(a="Correct — disruptive selection favors both extremes over the intermediate phenotype.",
                 b="Favoring the average phenotype describes STABILIZING selection, the opposite of disruptive selection.",
                 c="Disruptive selection very much affects phenotype distribution — it's not a 'no effect' scenario.",
                 d="Disruptive selection favors BOTH extremes, not just one — favoring only one extreme describes directional selection instead.")
),
8350: dict(
    short="Homologous structures (like forelimbs across species) reflect common ancestry with structures modified for different functions.",
    long="Homologous structures share a common underlying anatomical/developmental origin (inherited from a shared ancestor) but have been modified over evolutionary time to serve different functions in different descendant species — this is strong evidence for common ancestry.",
    trick="Don't confuse homologous structures (similar origin, DIFFERENT function, evidence of common ancestry) with analogous structures (different origin, SIMILAR function, evidence of convergent evolution, e.g., a bird wing and an insect wing).",
    options=dict(a="Convergent evolution from UNRELATED ancestors is what analogous (not homologous) structures demonstrate.",
                 b="Correct — homologous structures reflect common ancestry, modified over time for different functions.",
                 c="Homologous structures are direct evidence FOR an evolutionary relationship, not against one.",
                 d="These structures actually serve DIFFERENT functions (e.g. walking, swimming, flying) despite their shared origin — 'identical function' doesn't fit.")
),
8351: dict(
    short="q^2=0.09, so q=0.3, and p=1-q=0.7.",
    long="Using the Hardy-Weinberg equation p^2+2pq+q^2=1, where q^2 is the recessive phenotype frequency: q^2=0.09, so q=sqrt(0.09)=0.3. Since p+q=1, p=1-0.3=0.7.",
    trick="Always take the SQUARE ROOT of the recessive phenotype frequency to get q, then use p=1-q — a common error is forgetting the square root step and using 0.09 directly as q.",
    options=dict(a="0.3 is q (the recessive allele frequency), not p (the dominant allele frequency) being asked for.",
                 b="0.09 is q^2 (the recessive PHENOTYPE frequency), not the dominant allele frequency p.",
                 c="Correct — p = 1-q = 1-0.3 = 0.7.",
                 d="0.91 doesn't correctly follow from p=1-q with q=0.3.")
),
8352: dict(
    short="Family is the taxonomic rank directly above genus.",
    long="The standard taxonomic hierarchy from broad to specific is: Domain, Kingdom, Phylum, Class, Order, Family, Genus, Species. Family sits directly above genus.",
    trick="Memorize the full hierarchy in order (often via a mnemonic like 'Dear King Philip Came Over For Good Soup') to correctly identify which rank is immediately above or below another.",
    options=dict(a="Class is several ranks above genus (Class > Order > Family > Genus), not directly above it.",
                 b="Species is BELOW genus in the hierarchy, not above it.",
                 c="Order is one rank above family, so it's two steps above genus, not directly above.",
                 d="Correct — Family is the rank directly above genus.")
),
8353: dict(
    short="Bacteria and Archaea are both prokaryotic, lacking a membrane-bound nucleus.",
    long="Domains Bacteria and Archaea consist of prokaryotic organisms — single-celled with no membrane-bound nucleus or other membrane-bound organelles, distinguishing them from the eukaryotic Domain Eukarya.",
    trick="Don't confuse these two prokaryotic domains with Domain Eukarya (which includes eukaryotic, often multicellular organisms with a true nucleus) — Bacteria and Archaea are both prokaryotic despite their biochemical differences from each other.",
    options=dict(a="Correct — both Bacteria and Archaea are prokaryotic, lacking a membrane-bound nucleus.",
                 b="Eukaryotic and multicellular describes Domain Eukarya organisms, not Bacteria/Archaea.",
                 c="Not all bacteria/archaea are photosynthetic — many have other modes of nutrition (e.g., chemosynthesis, heterotrophy).",
                 d="Not all bacteria/archaea are parasitic; many are free-living, and some are even beneficial symbionts.")
),
8354: dict(
    short="Animals are generally heterotrophic and lack cell walls, unlike plants.",
    long="A defining distinction: plants are autotrophic (make their own food via photosynthesis) and have cellulose cell walls, while animals are heterotrophic (must consume other organisms for food) and lack cell walls around their cells.",
    trick="Don't mix up which kingdom has the cell wall — PLANTS have cellulose cell walls; ANIMALS lack cell walls entirely (their cells are bounded only by the plasma membrane).",
    options=dict(a="Autotrophic and having cellulose cell walls describes PLANTS, not animals.",
                 b="Correct — animals are heterotrophic and lack cell walls.",
                 c="Most animals ARE capable of movement (locomotion), one of their defining features.",
                 d="Animal cells are eukaryotic, not prokaryotic.")
),
8355: dict(
    short="Radial symmetry, cnidocytes, and a sac-like body plan indicate phylum Cnidaria.",
    long="Phylum Cnidaria (jellyfish, sea anemones, corals, hydra) is characterized by radial symmetry, specialized stinging cells called cnidocytes (containing nematocysts), and a simple sac-like body with a single opening (gastrovascular cavity).",
    trick="Cnidocytes (stinging cells) are the single most distinctive, memorable identifying feature of Cnidaria — no other major phylum has this exact structure.",
    options=dict(a="Chordata (vertebrates and close relatives) is characterized by a notochord/spinal structure, not cnidocytes or radial symmetry.",
                 b="Arthropoda is characterized by jointed appendages and an exoskeleton, not cnidocytes.",
                 c="Correct — radial symmetry, cnidocytes, and a sac-like body identify phylum Cnidaria.",
                 d="Mollusca is characterized by a soft body often with a shell, unrelated to cnidocytes.")
),
8356: dict(
    short="Class groups together several related orders.",
    long="In the taxonomic hierarchy (Domain > Kingdom > Phylum > Class > Order > Family > Genus > Species), class is positioned directly above order, grouping several related orders together.",
    trick="Work from the hierarchy directly: since Order sits below Class, 'grouping several orders' points specifically to the rank immediately above order — Class.",
    options=dict(a="Species is the most specific rank, far below order, not grouping multiple orders.",
                 b="Family sits BELOW order in the hierarchy, so it doesn't group orders together.",
                 c="Genus is even more specific than family, well below order.",
                 d="Correct — Class groups together several related orders.")
),
8357: dict(
    short="Amphibians typically undergo metamorphosis, with aquatic gilled larvae and lunged, moist-skinned adults.",
    long="Class Amphibia (frogs, toads, salamanders) is characterized by a life cycle that often includes metamorphosis: aquatic, gill-breathing larvae (like tadpoles) transforming into terrestrial, lung-breathing adults with moist, permeable skin used for supplemental gas exchange.",
    trick="Moist, permeable skin (used for cutaneous respiration) is a hallmark amphibian trait — don't confuse it with reptiles' dry, scaly skin (which reduces water loss for a fully terrestrial life).",
    options=dict(a="Correct — amphibians typically undergo metamorphosis with aquatic larvae and lunged, moist-skinned adults.",
                 b="Dry, scaly skin and land-only shelled eggs describe REPTILES, not amphibians.",
                 c="Feathers and endothermy describe BIRDS, not amphibians.",
                 d="Mammary glands are a defining MAMMAL trait, not an amphibian one.")
),
8358: dict(
    short="Phloem transports sugars (products of photosynthesis) from leaves to other plant parts.",
    long="Phloem tissue conducts organic nutrients, primarily sugars made during photosynthesis, from source tissues (like leaves) to sink tissues (like roots, fruits, and growing regions) throughout the plant.",
    trick="Don't confuse phloem (transports SUGARS, can move in various directions depending on source/sink) with xylem (transports WATER/minerals, generally upward from roots).",
    options=dict(a="Xylem transports water and minerals (generally upward from roots), not sugars.",
                 b="Correct — phloem transports photosynthetic sugars from leaves to other plant parts.",
                 c="The epidermis is the plant's outer protective layer, not a transport tissue.",
                 d="Meristem is actively dividing growth tissue, not a sugar-transport tissue.")
),
8359: dict(
    short="Stomata regulate gas exchange (CO2/O2) and water vapor loss (transpiration).",
    long="Stomata are small pores, primarily on leaf undersides, flanked by guard cells that open/close to regulate the exchange of CO2 (for photosynthesis) and O2, as well as water vapor loss through transpiration.",
    trick="Stomata handle GAS exchange and water VAPOR loss (transpiration) — they are not involved in absorbing liquid water from soil (that's the root's job) or transporting sugars (phloem's job).",
    options=dict(a="Absorbing water from soil is the root system's (and root hairs') job, not stomata's.",
                 b="Transporting sugars throughout the plant is phloem's function, not stomata's.",
                 c="Correct — stomata regulate gas exchange and water vapor loss via transpiration.",
                 d="Anchoring the plant is the root system's structural role, unrelated to stomatal function.")
),
8360: dict(
    short="A tendril coiling around a support in response to touch is thigmotropism.",
    long="Thigmotropism is a plant's directional growth response to physical touch/contact — as seen when a climbing vine's tendril coils around a support structure it contacts.",
    trick="Match the tropism to its stimulus: photo-=light, hydro-=water, gravi-=gravity, thigmo-=touch — the touch-triggered coiling response specifically points to thigmotropism.",
    options=dict(a="Phototropism is a growth response to LIGHT, not physical touch.",
                 b="Hydrotropism is a growth response to WATER, not touch.",
                 c="Gravitropism is a growth response to GRAVITY, not touch.",
                 d="Correct — thigmotropism is the touch-triggered coiling response described here.")
),
8361: dict(
    short="Root hairs increase absorption mainly by increasing the root's surface area in contact with soil.",
    long="Root hairs are thin, hair-like extensions of root epidermal cells that dramatically increase the total surface area in contact with soil, greatly enhancing the root's capacity to absorb water and dissolved minerals.",
    trick="The mechanism is purely about SURFACE AREA increase (more contact points with soil), not about producing chlorophyll (roots typically lack chlorophyll and don't photosynthesize) or reducing length.",
    options=dict(a="Correct — root hairs increase the root's surface area in contact with soil, boosting absorption.",
                 b="Roots generally lack chlorophyll and don't carry out photosynthesis — that's leaves' role.",
                 c="Root hairs facilitate (not prevent) water uptake — this option states the opposite effect.",
                 d="Root hairs don't reduce the root's length; they extend outward, increasing surface area without shortening the root.")
),
8362: dict(
    short="Abscisic acid promotes seed dormancy and stomatal closure during water stress.",
    long="Abscisic acid (ABA) is a plant stress hormone that promotes and maintains seed dormancy (preventing premature germination) and triggers stomatal closure during drought/water stress to reduce water loss.",
    trick="Don't confuse ABA (a growth-INHIBITING, stress-response hormone) with growth-promoting hormones like auxins or gibberellins, which drive cell elongation and stem growth — ABA generally does the opposite.",
    options=dict(a="Rapid cell elongation and growth is more characteristic of hormones like auxins or gibberellins, not ABA.",
                 b="Correct — ABA promotes seed dormancy and stomatal closure during water stress.",
                 c="Fruit ripening is primarily promoted by ethylene, not ABA exclusively.",
                 d="Stem elongation is promoted by hormones like gibberellins, not ABA (which tends to inhibit growth under stress).")
),
8363: dict(
    short="The pistil (carpel), including stigma, style, and ovary, is the flower's female reproductive structure.",
    long="The pistil (or carpel) is the female reproductive part of a flower, consisting of the stigma (receives pollen), style (connects stigma to ovary), and ovary (contains ovules, develops into fruit after fertilization).",
    trick="Don't confuse the pistil (female: stigma/style/ovary) with the stamen (male: anther/filament, produces pollen) — these are the two main reproductive structures of a flower.",
    options=dict(a="The stamen is the MALE reproductive structure (anther and filament), not the female one being described.",
                 b="Petals are the often colorful/showy parts attracting pollinators, not the reproductive structure itself.",
                 c="Correct — the pistil (carpel), comprising stigma, style, and ovary, is the female reproductive structure.",
                 d="Sepals are the protective outer leaf-like parts of a flower bud, not the reproductive structure.")
),
8364: dict(
    short="Bile, aiding fat digestion, is produced by the liver.",
    long="The liver produces bile, which is then stored and concentrated in the gallbladder before being released into the small intestine to emulsify fats, aiding their digestion.",
    trick="Don't confuse where bile is PRODUCED (the liver) with where it's STORED (the gallbladder) — a very common source of confusion in digestion questions.",
    options=dict(a="The stomach produces gastric juices (like pepsin and HCl), not bile.",
                 b="The gallbladder STORES and concentrates bile but does not produce it — the liver does.",
                 c="The pancreas produces digestive enzymes and bicarbonate, not bile.",
                 d="Correct — the liver produces bile.")
),
8365: dict(
    short="Amylase breaks down starch into simpler sugars.",
    long="Amylase (found in saliva and pancreatic secretions) hydrolyzes starch (a polysaccharide) into smaller sugar units like maltose, beginning carbohydrate digestion.",
    trick="Match each enzyme to its substrate: amylase=carbohydrates/starch, protease=proteins, lipase=lipids — amylase is specifically a carbohydrate-digesting enzyme.",
    options=dict(a="Correct — amylase breaks down starch (carbohydrates) into simpler sugars.",
                 b="Proteins are broken down by proteases (like pepsin/trypsin), not amylase.",
                 c="Lipids are broken down by lipase, not amylase.",
                 d="Nucleic acids are broken down by nucleases, not amylase.")
),
8366: dict(
    short="The large intestine's main role is absorbing water/electrolytes from indigestible matter, forming feces.",
    long="The large intestine (colon) primarily reabsorbs water and electrolytes from the remaining indigestible food material, compacting it into feces for elimination — it doesn't perform major nutrient digestion.",
    trick="Don't confuse the large intestine's water-absorption role with the small intestine's role (main site of NUTRIENT digestion/absorption) — the large intestine mainly handles water reclamation.",
    options=dict(a="Pepsin-based protein digestion occurs in the STOMACH, not the large intestine.",
                 b="Correct — the large intestine mainly absorbs water/electrolytes, forming feces.",
                 c="Bile is produced by the liver, not the large intestine.",
                 d="Insulin is secreted by the pancreas, not the large intestine.")
),
8367: dict(
    short="A blocked common bile duct would impair bile delivery to the small intestine, hurting fat digestion.",
    long="The common bile duct carries bile from the liver/gallbladder to the small intestine (duodenum). A blockage prevents bile from reaching the intestine, directly impairing the emulsification and digestion of dietary fats.",
    trick="Trace the specific ANATOMICAL PATHWAY affected by a blockage — the common bile duct's job is delivering bile for FAT digestion specifically, not starch digestion (mouth) or water absorption (large intestine).",
    options=dict(a="Starch digestion in the mouth (via salivary amylase) doesn't depend on the bile duct.",
                 b="Protein digestion in the stomach (via pepsin) doesn't depend on the bile duct.",
                 c="Correct — a blocked bile duct impairs bile delivery for fat digestion in the small intestine.",
                 d="Water absorption in the large intestine is a separate process, not dependent on the bile duct.")
),
8368: dict(
    short="Arteries carry blood away from the heart.",
    long="By definition, arteries are the blood vessels that carry blood AWAY from the heart (regardless of oxygen content), while veins carry blood back TOWARD the heart.",
    trick="Remember: the artery/vein distinction is about DIRECTION relative to the heart, not oxygenation — this is why the pulmonary artery (carrying deoxygenated blood, but AWAY from the heart) is still classified as an artery.",
    options=dict(a="Veins carry blood TOWARD the heart, the opposite direction from arteries.",
                 b="Venules are small vessels that merge into veins, also carrying blood toward the heart.",
                 c="Capillaries are the tiny vessels where exchange occurs, not the main away-from-heart vessels.",
                 d="Correct — arteries carry blood away from the heart.")
),
8369: dict(
    short="Vessel W (the pulmonary artery) is the only artery carrying deoxygenated blood.",
    long="The pulmonary artery is unique among arteries: it carries deoxygenated blood from the heart's right ventricle to the lungs for oxygenation — the general rule is arteries carry oxygenated blood, but this vessel is the well-known exception (paired with the pulmonary vein, which is the exception on the venous side, carrying oxygenated blood).",
    trick="Remember the two classic exceptions to the 'arteries=oxygenated, veins=deoxygenated' rule: the pulmonary ARTERY carries DEoxygenated blood, and the pulmonary VEIN carries OXYGENATED blood — opposite to systemic vessels.",
    options=dict(a="Correct — the pulmonary artery (W) is the only artery carrying deoxygenated blood.",
                 b="The pulmonary vein (X) carries oxygenated blood, and as a vein isn't even classified as an artery.",
                 c="The vena cava (Y) is a vein carrying deoxygenated blood, not an artery.",
                 d="The aorta (Z) is an artery, but it carries oxygenated blood, not deoxygenated.")
),
8370: dict(
    short="White blood cells (leukocytes) defend the body against infection and foreign invaders.",
    long="Leukocytes are the immune system's cellular defenders — they identify, target, and destroy pathogens (bacteria, viruses) and other foreign substances, as well as playing roles in inflammation and immune memory.",
    trick="Don't confuse leukocytes (immune defense) with erythrocytes/red blood cells (oxygen transport) or platelets (clotting) — each blood cell type has a distinct primary role.",
    options=dict(a="Transporting oxygen is the role of red blood cells (erythrocytes), not white blood cells.",
                 b="Correct — white blood cells defend the body against infection and foreign invaders.",
                 c="Carrying nutrients is primarily a function of blood plasma, not white blood cells specifically.",
                 d="Forming blood clots is primarily the role of platelets, not white blood cells.")
),
8371: dict(
    short="Increased blood viscosity increases resistance to flow, making the heart work harder.",
    long="Higher blood viscosity (thickness), such as from dehydration, increases the frictional resistance blood experiences as it flows through vessels, requiring the heart to work harder (generate more pressure) to maintain adequate circulation.",
    trick="Think of viscosity like pouring honey versus water through a tube — the thicker (more viscous) fluid meets more resistance, directly analogous to how thicker blood strains the circulatory system.",
    options=dict(a="Increased viscosity increases (not decreases) resistance to flow.",
                 b="Blood pressure IS affected (typically increased) by higher viscosity, not left unaffected.",
                 c="Correct — increased viscosity raises resistance to flow, making the heart work harder.",
                 d="Blood flow doesn't stop completely from moderately increased viscosity; it becomes more strained/difficult, not halted.")
),
8372: dict(
    short="The trachea carries air from the throat toward the lungs, branching into the bronchi.",
    long="The trachea (windpipe) is the tube connecting the throat/larynx to the bronchi, which then branch further into the lungs, carrying air along the respiratory pathway.",
    trick="Don't confuse the trachea (air passage) with the esophagus (food passage, located just behind the trachea) — they're adjacent but carry very different substances.",
    options=dict(a="The esophagus carries food/liquid to the stomach, a separate passage from the air pathway.",
                 b="The larynx (voice box) sits above the trachea and contains the vocal cords, but the tube branching into the bronchi is specifically the trachea.",
                 c="The pharynx is a shared passage for both air and food before they split into separate tracts, not the tube branching into bronchi itself.",
                 d="Correct — the trachea carries air toward the lungs, branching into the bronchi.")
),
8373: dict(
    short="During exhalation, the diaphragm relaxes and moves upward, decreasing thoracic volume.",
    long="During normal exhalation, the diaphragm (previously contracted and flattened downward during inhalation) relaxes and returns to its dome-shaped upward position, decreasing thoracic cavity volume and increasing pressure, pushing air out of the lungs.",
    trick="Remember: diaphragm CONTRACTS and moves DOWN during INHALATION (increasing volume, drawing air in); it RELAXES and moves UP during EXHALATION (decreasing volume, pushing air out) — the two phases are opposite movements.",
    options=dict(a="Correct — during exhalation, the diaphragm relaxes and moves upward, decreasing thoracic volume.",
                 b="Contracting and moving downward describes INHALATION, not exhalation.",
                 c="The diaphragm plays a central role in normal breathing, not 'no role'.",
                 d="Contracting to pull air in describes inhalation, the opposite phase from what's being asked (exhalation).")
),
8374: dict(
    short="Most CO2 is transported in blood as bicarbonate ions (HCO3-) after reacting with water in red blood cells.",
    long="The majority of CO2 produced by tissues is converted (inside red blood cells, via carbonic anhydrase) into bicarbonate ions (HCO3-) plus H+, which then dissolve in the plasma for transport to the lungs, where the reaction reverses to release CO2 for exhalation.",
    trick="Only a small fraction of CO2 travels as dissolved gas or bound to hemoglobin — the DOMINANT transport form is as bicarbonate ions, a key detail often tested.",
    options=dict(a="Only a small fraction of CO2 is transported as simple dissolved gas — most is converted to bicarbonate.",
                 b="Correct — most CO2 is transported as bicarbonate ions after reacting with water in red blood cells.",
                 c="CO2 is a gas, not transported as solid carbon particles.",
                 d="CO2 does bind hemoglobin to some extent (as carbaminohemoglobin) but is readily released at the lungs — it's not bound 'permanently'.")
),
8375: dict(
    short="Urine travels from the kidneys to the bladder through the ureter.",
    long="Each kidney connects to the bladder via a ureter, a muscular tube that transports urine formed in the kidney down to the bladder for storage until urination.",
    trick="Don't confuse the ureter (kidney-to-bladder) with the urethra (bladder-to-outside-the-body, used during urination) — these sound similar but serve different segments of the urinary pathway.",
    options=dict(a="The urethra carries urine OUT of the bladder during urination, not from kidney to bladder.",
                 b="The renal vein carries blood (not urine) away from the kidney.",
                 c="Correct — the ureter carries urine from the kidney to the bladder.",
                 d="The renal artery carries blood (not urine) INTO the kidney.")
),
8376: dict(
    short="Substances like excess H+ and drugs are added to filtrate during tubular secretion.",
    long="Tubular secretion is the process by which substances (like excess hydrogen ions, potassium, and certain drugs) are actively transported FROM the blood INTO the tubule fluid (filtrate) along the nephron, supplementing what was already filtered at the glomerulus.",
    trick="Distinguish the three main nephron processes: filtration (blood -> filtrate at glomerulus), reabsorption (filtrate -> blood, reclaiming useful substances), and secretion (blood -> filtrate, ADDING substances like H+ and drugs) — this question specifically describes secretion.",
    options=dict(a="Filtration at the glomerulus is the initial, relatively nonselective process forming the filtrate, not the selective addition of specific substances described here.",
                 b="Storage in the bladder occurs after urine is already formed, unrelated to adding substances to filtrate.",
                 c="Reabsorption moves substances FROM filtrate INTO blood (the opposite direction from what's described here).",
                 d="Correct — tubular secretion adds substances like H+ and drugs to the filtrate along the nephron tubules.")
),
8377: dict(
    short="Kidney failure leads to accumulation of urea and other nitrogenous wastes in the blood.",
    long="The kidneys normally filter and excrete nitrogenous waste products (like urea, a byproduct of protein metabolism) from the blood. If kidney function fails, these wastes accumulate in the bloodstream, a condition called uremia/azotemia.",
    trick="Focus on what the kidneys NORMALLY REMOVE — since kidney failure impairs removal, the substance that builds up is exactly what's normally filtered out: nitrogenous wastes like urea.",
    options=dict(a="Correct — untreated kidney failure leads to accumulation of urea and nitrogenous wastes in the blood.",
                 b="Kidney failure doesn't directly cause oxygen accumulation; oxygen levels relate more to respiratory/circulatory function.",
                 c="Digestive enzymes are produced by digestive organs, unrelated to kidney filtration function.",
                 d="Kidney failure can actually cause anemia (reduced red blood cells due to lowered erythropoietin), not an excess of red blood cells.")
),
8378: dict(
    short="The axon transmits electrical impulses away from the neuron's cell body.",
    long="The axon is the long, thin projection of a neuron responsible for conducting electrical impulses (action potentials) away from the cell body toward the axon terminals, where they can be passed to the next cell via a synapse.",
    trick="Don't confuse the axon (impulses OUT/away) with dendrites (receive/carry impulses TOWARD the cell body) — these are the two main types of neuronal projections, transmitting signals in opposite directions relative to the cell body.",
    options=dict(a="Dendrites carry impulses TOWARD the cell body, the opposite direction from what's described.",
                 b="Correct — the axon transmits impulses away from the cell body.",
                 c="The cell body (soma) contains the nucleus and organelles; it isn't the long extension carrying impulses away.",
                 d="The nucleus contains genetic material; it isn't the impulse-conducting extension being described.")
),
8379: dict(
    short="Myelin sheaths increase nerve impulse speed via saltatory conduction.",
    long="Myelin is an insulating layer around certain axons, with gaps called Nodes of Ranvier. This structure allows the electrical impulse to 'jump' from node to node (saltatory conduction), greatly increasing conduction speed compared to unmyelinated axons.",
    trick="Myelin SPEEDS UP conduction (not slows it) — myelinated axons can conduct impulses much faster than unmyelinated ones, which is exactly why conditions damaging myelin (like MS) cause slowed/impaired nerve function.",
    options=dict(a="Myelin sheaths increase (not slow down) the speed of nerve impulse transmission.",
                 b="Producing neurotransmitters is a function of the axon terminal/synaptic vesicles, not the myelin sheath.",
                 c="Correct — myelin sheaths increase conduction speed via saltatory conduction.",
                 d="Digesting old neurons is a function of glial/immune cells' clean-up processes, not the myelin sheath's role in healthy signaling.")
),
8380: dict(
    short="Adrenaline prepares the body for 'fight-or-flight' by raising heart rate and blood glucose.",
    long="Adrenaline (epinephrine), released by the adrenal medulla during stress, triggers the 'fight-or-flight' response: increasing heart rate, dilating airways, and raising blood glucose availability to prepare the body for rapid physical action.",
    trick="Adrenaline's effects are broadly the OPPOSITE of a calm/resting state — it doesn't slow the heart or promote digestion (that's more the parasympathetic 'rest and digest' response); it activates an urgent, energy-mobilizing response instead.",
    options=dict(a="Slowing the heart rate and promoting digestion describes the calming parasympathetic response, the opposite of adrenaline's fight-or-flight effect.",
                 b="Adrenaline has substantial, well-documented physiological effects — 'no effect' is incorrect.",
                 c="Adrenaline typically RAISES blood pressure (as part of the fight-or-flight response), not lowers it.",
                 d="Correct — adrenaline prepares for fight-or-flight by raising heart rate and blood glucose availability.")
),
8381: dict(
    short="Insulin lowers blood glucose, which then reduces further insulin release — classic negative feedback.",
    long="High blood glucose triggers insulin release from the pancreas. Insulin promotes glucose uptake by cells, lowering blood glucose levels. As glucose falls back toward normal, the stimulus for insulin release diminishes, reducing further insulin secretion — a self-correcting negative feedback loop.",
    trick="Negative feedback loops work by counteracting the original stimulus (high glucose triggers a response that LOWERS glucose) — don't confuse this with a positive feedback loop, which would amplify the original change instead.",
    options=dict(a="Correct — insulin lowers blood glucose, reducing the stimulus for further insulin release (negative feedback).",
                 b="Insulin LOWERS (not raises) blood glucose — raising it further would be a positive feedback loop, not the typical negative feedback described here.",
                 c="Insulin's glucose-lowering effect DOES influence (reduce) subsequent insulin release, so 'no effect' is incorrect.",
                 d="This loop specifically concerns blood glucose regulation, not calcium (a separate hormonal system, e.g., parathyroid hormone).")
),
8382: dict(
    short="The ovary is where egg (ovum) production and maturation occur in females.",
    long="The ovaries are the female gonads responsible for producing and maturing eggs (ova) through the process of oogenesis, as well as secreting reproductive hormones like estrogen and progesterone.",
    trick="Don't confuse the ovary (egg production site) with the uterus (site of embryo implantation/development) or the fallopian tube (site of fertilization and egg transport, not egg production itself).",
    options=dict(a="The uterus is where a fertilized egg implants and develops, not where eggs are produced.",
                 b="Correct — the ovary is the site of egg production and maturation.",
                 c="The fallopian tube transports the egg and is typically the site of fertilization, not egg production.",
                 d="The vagina is the birth canal/copulatory organ, unrelated to egg production.")
),
8383: dict(
    short="Estrogen stimulates uterine lining development and secondary sexual characteristics.",
    long="Estrogen, secreted mainly by the ovarian follicles, promotes growth of the uterine lining (endometrium) in preparation for potential pregnancy, and drives the development of female secondary sexual characteristics during puberty.",
    trick="Don't confuse estrogen's building-up/growth-promoting role with progesterone's maintenance role, or assume it triggers menstruation directly — menstruation actually occurs when estrogen/progesterone levels DROP if no pregnancy occurs.",
    options=dict(a="Estrogen doesn't trigger insulin release; that's a pancreatic function unrelated to estrogen's main reproductive roles.",
                 b="Estrogen doesn't cause 'immediate' menstruation — menstruation actually follows a DROP in estrogen/progesterone when pregnancy doesn't occur.",
                 c="Correct — estrogen stimulates uterine lining development and secondary sexual characteristics.",
                 d="Estrogen actually contributes to triggering ovulation (via the LH surge) rather than permanently preventing it.")
),
8384: dict(
    short="Heterotrophs obtain energy by consuming other organisms.",
    long="Heterotrophs cannot produce their own food and must obtain organic nutrients/energy by consuming other organisms (plants, animals, or their remains), unlike autotrophs (producers), which make their own food via photosynthesis or chemosynthesis.",
    trick="Don't confuse heterotrophs (consumers, eating other organisms) with autotrophs/producers (make their own food) — decomposers are actually a SPECIFIC TYPE of heterotroph (feeding on dead matter), not a separate category from heterotrophs overall.",
    options=dict(a="Autotrophs make their own food (e.g., via photosynthesis); they don't consume other organisms for energy.",
                 b="Decomposers are actually a specific subset of heterotrophs (feeding on dead organic matter), not an exclusive separate category.",
                 c="Producers are synonymous with autotrophs, which make their own food rather than consuming others.",
                 d="Correct — heterotrophs obtain energy by consuming other organisms.")
),
8385: dict(
    short="Photosynthesis is how plants remove atmospheric CO2 and incorporate it into organic molecules.",
    long="In the carbon cycle, photosynthesis is the key process by which plants (and other autotrophs) capture atmospheric carbon dioxide and use it to build organic molecules (like glucose), fixing inorganic carbon into biological, organic form.",
    trick="Photosynthesis REMOVES CO2 from the atmosphere; respiration, combustion, and decomposition all instead RELEASE CO2 back into the atmosphere — this question specifically asks about the CO2-removing process.",
    options=dict(a="Correct — photosynthesis removes atmospheric CO2, incorporating it into organic molecules.",
                 b="Respiration RELEASES CO2 back into the atmosphere, the opposite of what's described.",
                 c="Combustion also RELEASES CO2 (burning organic material), not removing it.",
                 d="Decomposition also releases CO2 as organic matter is broken down, not the CO2-fixing process described.")
),
}

def main():
    root = Path(__file__).parent.parent
    out = []
    for qid, e in EXPL.items():
        out.append({
            "id": qid,
            "short": e["short"],
            "long": e["long"],
            "trick": e["trick"],
            "options": e["options"],
        })
    out_path = root / "scripts" / "mock20_explanations_biology_2.json"
    out_path.write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Wrote {len(out)} explanations to {out_path}")

if __name__ == "__main__":
    main()
