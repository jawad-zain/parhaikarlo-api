import json
from pathlib import Path

OUT = Path(__file__).parent / "mock18_explanations_biology_2.json"

def I(po): return po + 7944

E = []

def add(po, short, long, trick, a, b, c, d):
    E.append({
        "id": I(po), "short": short, "long": long, "trick": trick,
        "options": {"a": a, "b": b, "c": c, "d": d}
    })

add(42, "DNA ligase seals nicks between Okazaki fragments, joining the lagging strand into a continuous piece.",
    "DNA polymerase synthesizes the lagging strand discontinuously as short Okazaki fragments (since replication only proceeds 5'->3'); DNA ligase then forms the phosphodiester bonds that seal the remaining gaps/nicks between these fragments into one continuous strand.",
    "Primase lays down RNA primers; ligase seals fragments together at the end — don't mix up the enzyme that starts fragments versus the one that joins them.",
    "Incorrect — primase synthesizes the RNA primers that initiate each fragment, but does not join fragments together.",
    "Correct — DNA ligase seals the nicks between Okazaki fragments, joining the lagging strand.",
    "Incorrect — helicase unwinds the double helix ahead of the replication fork; it doesn't join fragments.",
    "Incorrect — topoisomerase relieves supercoiling tension ahead of the fork; it doesn't join Okazaki fragments.")

add(43, "An enhancer is a regulatory DNA sequence that boosts transcription even from a distance.",
    "Enhancers are regulatory elements that can be located far upstream, downstream, or even within introns of a gene, yet still increase its transcription rate by looping DNA to bring bound activator proteins close to the promoter/RNA polymerase complex.",
    "Promoters sit right at the transcription start site; enhancers can act from far away — that 'action at a distance' is the enhancer's signature feature.",
    "Incorrect — a promoter is located directly at the transcription start site, not able to act from far away.",
    "Incorrect — a terminator signals the END of transcription, unrelated to boosting it from a distance.",
    "Correct — enhancers are defined by their ability to increase transcription even when located far from the gene.",
    "Incorrect — an exon is a protein-coding segment of a gene itself, not a distant regulatory sequence.")

add(44, "A codon is made of exactly 3 nucleotide bases, coding for one amino acid (or a stop signal).",
    "The genetic code is read in triplets: each group of 3 consecutive mRNA nucleotides forms one codon, specifying either a particular amino acid or a stop signal — this triplet nature is what allows 4 bases to encode 20 amino acids (4^3 = 64 possible codons).",
    "Memorize: codon = 3 bases. This triplet size is why insertions/deletions of non-multiples of 3 cause damaging frameshift mutations.",
    "Incorrect — a single base cannot specify one of 20 amino acids (only 4 possibilities); it's insufficient.",
    "Incorrect — two bases would give only 16 (4^2) combinations, still not enough to code for all 20 amino acids reliably.",
    "Incorrect — four bases would be more than needed and doesn't match the actual codon structure used by the genetic code.",
    "Correct — a codon consists of exactly 3 nucleotide bases.")

add(45, "Natural selection acts on heritable variation that affects an organism's survival and reproductive success.",
    "For natural selection to work, variation must be genetically heritable (passed to offspring) and must influence fitness (survival/reproduction) — traits acquired during a lifetime (like a built muscle) are not passed on genetically and so aren't subject to selection.",
    "Only HERITABLE variation matters for natural selection — acquired traits (exercise, injuries) are a classic wrong-answer trap since Lamarckian inheritance is not how it actually works.",
    "Correct — natural selection specifically requires heritable variation affecting survival/reproduction.",
    "Incorrect — traits acquired during a lifetime are not passed to offspring genetically, so selection can't act on them.",
    "Incorrect — for selection to act, mutations must actually affect fitness; ones with zero fitness effect aren't selected for or against.",
    "Incorrect — selection can act on any heritable trait affecting fitness, not only visible appearance (e.g. biochemical/physiological traits too).")

add(46, "Stabilizing selection favors the average phenotype, reducing variation at both extremes of a trait.",
    "This selection type removes individuals with extreme trait values (too small, too large) while favoring intermediate individuals — e.g. human birth weight, where both very low and very high birth weights have reduced survival, keeping the population clustered near the average.",
    "Stabilizing = narrows toward the average; directional = shifts the whole curve one way; disruptive = favors both extremes over the middle — three distinct selection shapes to distinguish.",
    "Incorrect — favoring extremes over the average describes disruptive selection, not stabilizing selection.",
    "Correct — stabilizing selection favors the average/intermediate phenotype and reduces variation at both extremes.",
    "Incorrect — stabilizing selection does actively narrow the phenotype distribution; it's not a no-effect scenario.",
    "Incorrect — creating two distinct groups describes disruptive selection, the opposite pattern from stabilizing.")

add(47, "Convergent evolution is when unrelated species independently evolve similar traits due to similar environmental pressures.",
    "Classic examples include the wing of a bat and the wing of an insect, or the streamlined body shape of sharks (fish) and dolphins (mammals) — unrelated lineages arriving at similar solutions (analogous structures) because they face similar selective pressures, not because of shared ancestry.",
    "Convergent evolution produces analogous structures (similar function, different evolutionary origin) — contrast this with homologous structures, which share ancestry (divergent evolution).",
    "Incorrect — two closely related species evolving different traits describes divergent evolution, not convergent.",
    "Incorrect — one species splitting into many describes speciation/adaptive radiation, not convergent evolution.",
    "Correct — unrelated species independently evolving similar traits under similar pressures is the definition of convergent evolution.",
    "Incorrect — extinction is the disappearance of a species, unrelated to the convergent-evolution concept.")

add(48, "With 16% recessive phenotype (q^2 = 0.16), the recessive allele frequency q = sqrt(0.16) = 0.4.",
    "Under Hardy-Weinberg equilibrium, the recessive phenotype frequency equals q^2 (both alleles recessive). Given q^2 = 0.16, taking the square root gives q = 0.4 — the frequency of the recessive allele in the population.",
    "Always take the SQUARE ROOT of the recessive phenotype frequency to get q, not the phenotype frequency itself or a simple fraction of it.",
    "Incorrect — 0.16 is q^2 (the phenotype frequency), not q itself; you must take its square root.",
    "Incorrect — 0.6 does not satisfy q^2 = 0.16 (0.6^2 = 0.36, not 0.16).",
    "Incorrect — 0.84 is p (1 - q = 1 - 0.4), the dominant allele frequency, not q.",
    "Correct — sqrt(0.16) = 0.4, the recessive allele frequency.")

add(49, "Binomial nomenclature is the standardized two-part (genus + species) naming system for organisms.",
    "Devised by Linnaeus, binomial nomenclature gives every species a unique two-part Latin name (Genus species, e.g. Homo sapiens), avoiding the confusion of common names that vary by language/region.",
    "'Binomial' literally means 'two names' — genus first (capitalized), species second (lowercase), both italicized.",
    "Correct — binomial nomenclature is precisely the genus + species two-part naming convention.",
    "Incorrect — cladistics is a method of classifying organisms by evolutionary relationships (clades), not a naming system.",
    "Incorrect — taxonomy is the broader science of classification; binomial nomenclature is specifically its naming convention, a narrower term.",
    "Incorrect — phylogeny refers to the evolutionary history/relationships of organisms, not their naming system.")

add(50, "Fungi are absorptive heterotrophs: they secrete digestive enzymes externally, then absorb the digested nutrients.",
    "Unlike animals (which ingest food internally) or plants (which photosynthesize), fungi secrete extracellular enzymes onto their food source, break it down externally, and then absorb the resulting small organic molecules through their cell walls/membranes.",
    "Fungi digest OUTSIDE the body first, then absorb — the reverse order from animals, who ingest first and digest internally.",
    "Incorrect — fungi lack chlorophyll and cannot photosynthesize; they are heterotrophs, not autotrophs.",
    "Correct — secreting enzymes externally and then absorbing digested nutrients defines fungal (absorptive heterotrophic) nutrition.",
    "Incorrect — ingesting prey internally describes animal-style (holozoic) nutrition, not typical fungal nutrition.",
    "Incorrect — chemosynthesis (using inorganic chemical energy) is used by certain bacteria, not by fungi.")

add(51, "Both Bacteria and Archaea are prokaryotic, single-celled domains.",
    "Despite major biochemical differences between them (e.g. membrane lipids, RNA polymerase structure), both Bacteria and Archaea share the defining prokaryotic features: no membrane-bound nucleus or organelles, and typically unicellular organization — distinguishing them from the eukaryotic domain Eukarya.",
    "Domain-level split: Bacteria and Archaea = prokaryotic; Eukarya = eukaryotic (includes protists, fungi, plants, animals) — the three-domain system's most basic distinction.",
    "Incorrect — both domains are prokaryotic and typically unicellular, not eukaryotic/multicellular.",
    "Incorrect — while some Archaea are extremophiles, both domains also include organisms in ordinary, non-extreme environments.",
    "Correct — being prokaryotic and unicellular is the shared defining feature of both domains.",
    "Incorrect — many bacteria and archaea are not photosynthetic; this isn't a universal domain-defining trait.")

add(52, "A segmented body, jointed appendages, and a chitin exoskeleton are hallmark features of phylum Arthropoda.",
    "Arthropods (insects, crustaceans, arachnids, myriapods) are defined by body segmentation (often grouped into regions), jointed limbs allowing flexible movement, and a rigid chitinous exoskeleton that must be periodically molted for growth.",
    "'Jointed appendages' + 'exoskeleton' + 'segmented body' together point specifically to Arthropoda — the most diverse animal phylum.",
    "Incorrect — echinoderms (like starfish) have an internal calcareous endoskeleton and radial symmetry, not a chitin exoskeleton.",
    "Incorrect — annelids (segmented worms) are segmented but lack jointed appendages and a hard exoskeleton.",
    "Incorrect — mollusks (like snails, clams) typically have a soft body, often with a calcium carbonate shell, not a chitin exoskeleton or jointed limbs.",
    "Correct — segmentation + jointed appendages + chitin exoskeleton together define phylum Arthropoda.")

add(53, "Genus is the taxonomic rank more specific than Family but less specific than Species.",
    "The standard taxonomic hierarchy from broad to narrow is: Kingdom, Phylum, Class, Order, Family, Genus, Species. Genus sits directly between Family (broader) and Species (narrower/most specific).",
    "Memorize the hierarchy order (e.g. 'King Philip Came Over For Good Soup') to quickly place any rank relative to another.",
    "Correct — Genus is exactly the rank sitting between Family and Species in the taxonomic hierarchy.",
    "Incorrect — Order is broader than Family, so it sits further from Species, not between Family and Species.",
    "Incorrect — Class is broader still (above Order), even further from Species than Family is.",
    "Incorrect — Phylum is one of the broadest ranks, far above Family in the hierarchy.")

add(54, "Class Aves is characterized by feathers, endothermy (warm-bloodedness), and typically flight capability.",
    "Birds (Aves) are defined by feathers (used for insulation and flight), a four-chambered heart supporting a high, warm-blooded metabolism (endothermy), and lightweight/hollow bones adapted for most species' powered flight.",
    "Feathers are unique to birds among living animals — the single most reliable identifying feature of class Aves.",
    "Incorrect — gills and cold-bloodedness describe fish (or amphibian larvae), not birds, which are warm-blooded and breathe with lungs.",
    "Correct — feathers, endothermy, and typically flight are the defining characteristics of class Aves.",
    "Incorrect — mammary glands are a defining feature of Class Mammalia, not Aves.",
    "Incorrect — moist, permeable skin for gas exchange is characteristic of amphibians, not birds (which have dry, feathered skin).")

add(55, "Xylem transports water and dissolved minerals from roots up to the leaves.",
    "Xylem is composed of dead, hollow, lignified cells (tracheids and vessel elements) that form continuous tubes; water moves upward largely via transpiration pull (cohesion-tension) combined with root pressure and capillary action.",
    "Xylem carries water UPWARD (roots to leaves) only; phloem carries sugars in either direction (source to sink) — a fundamental plant-transport distinction.",
    "Incorrect — phloem transports sugars (organic nutrients like sucrose), not water and minerals, and can move bidirectionally.",
    "Incorrect — the epidermis is the outer protective cell layer, not a long-distance transport tissue.",
    "Correct — xylem is the tissue specialized for transporting water and dissolved minerals from roots to leaves.",
    "Incorrect — cork cambium produces protective cork tissue in woody stems/roots; it isn't a water-transport tissue.")

add(56, "The light-dependent reactions of photosynthesis occur across the thylakoid membrane.",
    "Chlorophyll and the photosystems embedded in the thylakoid membrane absorb light energy, splitting water and generating ATP and NADPH, which are then used by the light-independent reactions (Calvin cycle) occurring in the stroma.",
    "Light reactions = thylakoid membrane; Calvin cycle (dark/light-independent reactions) = stroma — a very commonly tested location pairing.",
    "Incorrect — the cytoplasm is outside the chloroplast entirely; photosynthesis occurs within chloroplast compartments.",
    "Incorrect — the stroma hosts the light-INDEPENDENT reactions (Calvin cycle), not the light-dependent reactions.",
    "Incorrect — the mitochondrial matrix hosts the Krebs cycle (respiration), an entirely different organelle and process.",
    "Correct — the thylakoid membrane is specifically where the light-dependent reactions take place.")

add(57, "A shoot growing toward light is phototropism — a directional growth response to a light stimulus.",
    "Tropisms are directional plant growth responses to external stimuli; phototropism specifically responds to light direction (shoots typically grow toward light, positively phototropic), driven by auxin redistribution causing differential cell elongation.",
    "Match the stimulus to the tropism name: photo = light, gravi = gravity, thigmo = touch, hydro = water — the prefix tells you the trigger.",
    "Correct — growth toward a light source is precisely what phototropism means.",
    "Incorrect — gravitropism is growth in response to gravity, not light.",
    "Incorrect — thigmotropism is growth in response to touch/contact (e.g. a vine's tendril coiling around a support).",
    "Incorrect — hydrotropism is growth in response to a water gradient (mainly seen in roots), not light.")

add(58, "Mycorrhizal fungi increase a root's effective surface area for water/mineral uptake, trading that for sugars from the plant.",
    "This mutualistic symbiosis benefits both partners: fungal hyphae vastly extend the root system's absorptive surface area (especially for phosphate and water), while the plant supplies the fungus with photosynthetically produced sugars — a win-win relationship, not one-sided harm.",
    "Mycorrhizae are MUTUALISTIC (both partners benefit), not parasitic — don't mistake this relationship for one that only harms the plant.",
    "Incorrect — mycorrhizal fungi provide a clear benefit (better water/mineral absorption), not harm, in this mutualistic relationship.",
    "Correct — expanding root surface area for absorption, in exchange for plant sugars, is exactly how this mutualism works.",
    "Incorrect — fungi cannot photosynthesize and produce no light energy for the plant.",
    "Incorrect — this relationship enhances, rather than prevents, water uptake by the plant.")

add(59, "Auxin primarily promotes cell elongation and drives tropic (phototropic/gravitropic) growth responses.",
    "Auxin, produced mainly in shoot tips, diffuses to the shaded/lower side of a stem, stimulating those cells to elongate more than the lit/upper side cells — bending the shoot toward light (phototropism) or against gravity (negative gravitropism in shoots).",
    "Auxin's headline function is cell elongation — many of its other listed effects (fruit ripening = ethylene, dormancy = ABA) belong to different plant hormones, a classic hormone mix-up trap.",
    "Incorrect — fruit ripening is primarily driven by ethylene, not auxin.",
    "Incorrect — auxin actually generally inhibits, rather than exclusively promotes, leaf abscission at normal levels.",
    "Correct — cell elongation underlying phototropic and gravitropic bending is auxin's defining role.",
    "Incorrect — seed dormancy is mainly regulated by abscisic acid (ABA), not auxin.")

add(60, "The stamen is a flower's male reproductive structure, producing pollen.",
    "Each stamen consists of a filament supporting an anther, where meiosis produces pollen grains containing male gametes — the flower's counterpart to the female pistil (which contains the ovary/ovules).",
    "Stamen = male (produces pollen); Pistil/carpel = female (contains ovules) — the two core reproductive flower parts to keep straight.",
    "Incorrect — the pistil is the female reproductive structure (containing the ovary), not the pollen-producing structure.",
    "Incorrect — petals are non-reproductive, typically colorful structures that attract pollinators.",
    "Incorrect — sepals are protective, leaf-like structures enclosing the flower bud, not reproductive organs.",
    "Correct — the stamen (anther + filament) is the male structure that produces pollen.")

add(61, "Salivary amylase in the mouth begins chemical digestion of starch into shorter sugar chains.",
    "Saliva contains salivary amylase, which starts breaking down starch (a polysaccharide) into smaller polysaccharide fragments and maltose while food is still being chewed, even before it reaches the stomach.",
    "Salivary amylase acts on CARBOHYDRATES (starch) specifically, in the mouth — don't confuse it with pepsin (protein, stomach) or lipase (fat, small intestine).",
    "Incorrect — pepsin is a protein-digesting enzyme active in the stomach, not the mouth, and doesn't act on starch.",
    "Correct — salivary amylase is the enzyme that begins starch digestion in the mouth.",
    "Incorrect — lipase digests fats, mainly in the small intestine, and plays no role in starch digestion.",
    "Incorrect — trypsin is a protein-digesting enzyme secreted by the pancreas into the small intestine, unrelated to starch.")

add(62, "Pepsin, active in the acidic stomach, breaks down proteins into smaller polypeptides.",
    "Pepsin is secreted as inactive pepsinogen by stomach chief cells and activated by the stomach's strongly acidic environment (HCl from parietal cells); it cleaves peptide bonds in dietary proteins, beginning protein digestion.",
    "Pepsin works specifically on PROTEINS and needs an ACIDIC environment (the stomach) — it would actually be inactivated in the near-neutral/alkaline small intestine.",
    "Incorrect — carbohydrate digestion is mainly carried out by amylase (salivary and pancreatic), not pepsin.",
    "Correct — pepsin specifically breaks down proteins in the stomach's acidic environment.",
    "Incorrect — lipid digestion is carried out by lipase, not pepsin.",
    "Incorrect — pepsin is not specific to nucleic acids; nucleases handle those, in the small intestine.")

add(63, "Bile emulsifies fats into smaller droplets, increasing surface area for lipase to act on.",
    "Bile (produced by the liver, stored in the gallbladder) contains bile salts that act like a detergent, breaking large fat globules into many tiny droplets (emulsification) — this dramatically increases the surface area available for pancreatic lipase to chemically digest the fats into fatty acids and glycerol.",
    "Bile itself is not an enzyme and doesn't chemically break bonds — it's a physical/mechanical emulsifier that helps lipase (the actual enzyme) work more efficiently.",
    "Incorrect — bile does not chemically break fat molecules apart itself; that's the enzymatic job of lipase.",
    "Incorrect — bile is not lipase itself; it's produced by the liver and works alongside pancreatic lipase.",
    "Correct — emulsifying fat into small droplets to increase surface area for lipase is bile's specific role.",
    "Incorrect — bile aids digestion of fats, not their direct absorption into the bloodstream.")

add(64, "Removing the gallbladder most directly affects the storage and timed release of bile for fat digestion.",
    "The gallbladder's job is to store and concentrate bile (made continuously by the liver) between meals, then release it in a controlled burst when fatty food enters the small intestine. Without a gallbladder, bile still reaches the intestine from the liver, but more continuously/less concentrated, somewhat impairing efficient fat digestion, especially of large fatty meals.",
    "The LIVER makes bile; the GALLBLADDER stores/releases it — removing the gallbladder affects storage/timing, not bile production itself.",
    "Incorrect — protein digestion in the stomach (via pepsin) is unrelated to bile or the gallbladder.",
    "Incorrect — water absorption in the large intestine does not depend on gallbladder function.",
    "Incorrect — starch digestion begins in the mouth via salivary amylase, unrelated to the gallbladder.",
    "Correct — the gallbladder specifically stores bile and releases it in a timed manner to aid fat digestion; removing it disrupts this storage/release function.")

add(65, "The left ventricle pumps oxygenated blood out to the entire body via the aorta.",
    "Oxygenated blood returns from the lungs to the left atrium, passes into the left ventricle, which has the thickest muscular wall (to generate high pressure), and is pumped out through the aorta to systemic circulation supplying the whole body.",
    "Left side of the heart = oxygenated blood/systemic circuit; right side = deoxygenated blood/pulmonary circuit — and it's always the ventricles (not atria) that do the actual pumping out.",
    "Correct — the left ventricle's powerful contraction pumps oxygenated blood into the aorta and out to the body.",
    "Incorrect — the right atrium receives deoxygenated blood returning from the body; it doesn't pump blood out to the body.",
    "Incorrect — the right ventricle pumps deoxygenated blood to the lungs (pulmonary circulation), not to the body.",
    "Incorrect — the left atrium receives oxygenated blood from the lungs but passes it to the left ventricle rather than pumping it to the whole body itself.")

add(66, "Pulmonary circulation carries blood between the heart and the lungs for gas exchange.",
    "The right ventricle pumps deoxygenated blood through the pulmonary artery to the lungs, where CO2 is released and O2 is picked up; oxygenated blood then returns via the pulmonary veins to the left atrium — this closed loop is pulmonary circulation.",
    "'Pulmonary' always refers to the LUNGS specifically — pulmonary circulation is the heart-lungs loop, distinct from systemic circulation (heart-to-rest-of-body).",
    "Incorrect — the heart-to-rest-of-body loop is systemic circulation, not pulmonary circulation.",
    "Correct — pulmonary circulation specifically connects the heart and lungs for gas exchange.",
    "Incorrect — the kidneys receive blood via the renal circulation (part of systemic circulation), not the pulmonary circuit.",
    "Incorrect — the liver receives blood via hepatic/portal circulation (part of systemic circulation), not the pulmonary circuit.")

add(67, "Blood clotting relies on platelets working together with clotting factors (a cascade of plasma proteins).",
    "When a blood vessel is injured, platelets adhere to the exposed collagen and aggregate at the site, while a cascade of clotting factors (many synthesized in the liver) converts fibrinogen into fibrin, forming a mesh that stabilizes the platelet plug into a clot.",
    "Clotting needs BOTH platelets (cells) AND clotting factors (plasma proteins) working together — neither alone completes the process.",
    "Incorrect — red blood cells carry oxygen; they are not the primary cellular component of clot formation.",
    "Incorrect — clotting factors (plasma proteins) alone aren't sufficient; platelets are essential cellular participants too.",
    "Correct — platelets, working alongside clotting factors, are the key cellular component of coagulation.",
    "Incorrect — white blood cells are involved in immune defense, not primarily in the clotting process.")

add(68, "During intense exercise, heart rate rises mainly to increase cardiac output, delivering more oxygen and nutrients to active muscles.",
    "Cardiac output = heart rate x stroke volume. As muscles work harder and demand more oxygen/glucose (and produce more CO2/waste), heart rate increases to pump blood faster, boosting delivery of oxygen and nutrients and faster removal of metabolic waste.",
    "Exercise increases, not decreases, oxygen delivery and blood flow to active tissues — options describing a decrease or stoppage are the opposite of what actually happens.",
    "Incorrect — exercise increases, not decreases, oxygen delivery to meet higher tissue demand.",
    "Incorrect — blood flow to muscles increases during exercise; it certainly doesn't stop.",
    "Incorrect — blood pressure typically rises somewhat during exercise, not drops to zero (which would be catastrophic).",
    "Correct — raising cardiac output to deliver more oxygen/nutrients to active tissues is the main purpose of the exercise-induced heart rate increase.")

add(69, "Gas exchange in the lungs occurs across the thin walls of the alveoli.",
    "Alveoli are tiny, thin-walled, richly capillary-surrounded air sacs that maximize surface area for efficient diffusion of O2 into the blood and CO2 out of the blood, the actual site of gas exchange in the respiratory system.",
    "The bronchi/trachea/larynx are airway passages that conduct air; only the alveoli, at the very end of the airway tree, are thin and vascularized enough for actual gas exchange.",
    "Correct — alveoli are the specialized, thin-walled structures where gas exchange with the bloodstream actually occurs.",
    "Incorrect — bronchi are larger conducting airways; their walls are too thick for efficient gas exchange.",
    "Incorrect — the trachea is the windpipe, a conducting airway, not a gas-exchange surface.",
    "Incorrect — the larynx (voice box) is part of the upper airway, unrelated to gas exchange.")

add(70, "During inhalation, the diaphragm contracts and moves downward, increasing thoracic volume so air flows in.",
    "Diaphragm contraction flattens its dome shape and moves it downward, expanding the chest cavity's volume; this drop in internal pressure (per Boyle's law) draws air into the lungs from the higher-pressure atmosphere.",
    "Diaphragm CONTRACTS to increase volume during INHALATION (breathing in); it RELAXES during exhalation — a very commonly reversed detail.",
    "Incorrect — this describes what happens during exhalation (diaphragm relaxing, moving up, decreasing volume), not inhalation.",
    "Correct — diaphragm contraction and downward movement increases thoracic volume, drawing air in during inhalation.",
    "Incorrect — the diaphragm plays a central, essential role in breathing, not none.",
    "Incorrect — a contracting diaphragm draws air IN (inhalation); forcing air OUT happens on relaxation (during exhalation), not contraction.")

add(71, "Asthma's airway inflammation and constriction cause difficulty breathing due to narrowed airways.",
    "In asthma, chronic inflammation makes airway linings swell and airway smooth muscle constricts (bronchospasm), narrowing the passage for airflow and often triggering wheezing, coughing, and shortness of breath, especially during an asthma attack.",
    "Narrower airways = HARDER breathing, more resistance to airflow — this is the direct physical consequence of the described inflammation/constriction.",
    "Incorrect — narrowed, inflamed airways make breathing harder, not easier — 'improved airflow' is the opposite of what actually happens.",
    "Incorrect — inflammation and constriction do have a significant, often severe, effect on breathing.",
    "Correct — narrowed airways from inflammation/constriction directly cause difficulty breathing, the hallmark symptom of asthma.",
    "Incorrect — asthma reduces, rather than increases, effective airflow/lung capacity during an attack.")

add(72, "Structure 1 in the diagram, the glomerulus, is the capillary tuft where blood filtration begins in the nephron.",
    "The glomerulus is a dense knot of capillaries inside Bowman's capsule; blood pressure forces water, ions, glucose, and small molecules out of the blood and into the capsule (filtration), the very first step of urine formation, before fluid moves on through the tubule system.",
    "Filtration happens at the GLOMERULUS specifically (structure 1); Bowman's capsule (structure 2) just collects the filtrate that results — don't mix up the filter itself with the cup that catches the filtrate.",
    "Incorrect — Structure 4, the loop of Henle, functions in reabsorption/concentration further along the nephron, not initial filtration.",
    "Incorrect — Structure 2, Bowman's capsule, collects the filtrate produced by the glomerulus; it isn't the capillary tuft itself.",
    "Incorrect — Structure 3, the proximal convoluted tubule, reabsorbs substances from the filtrate; it isn't where filtration begins.",
    "Correct — Structure 1, the glomerulus, is the capillary tuft where blood filtration into the nephron begins.")

add(73, "Beyond the proximal convoluted tubule, most remaining water reabsorption occurs at the loop of Henle and collecting duct.",
    "The proximal convoluted tubule reabsorbs the bulk (~65%) of filtered water and solutes; the loop of Henle (via the countercurrent multiplier) and the collecting duct (under ADH control) then fine-tune and reabsorb most of the remaining water, concentrating the final urine.",
    "Water reabsorption is distributed along multiple nephron segments (PCT, loop of Henle, collecting duct) — not concentrated in a single non-tubule structure like the renal artery, ureter, or bladder.",
    "Correct — the loop of Henle and collecting duct handle most of the remaining water reabsorption after the PCT.",
    "Incorrect — the renal artery simply delivers blood to the kidney; it doesn't reabsorb water from filtrate.",
    "Incorrect — the ureter transports already-formed urine to the bladder; it isn't a major site of water reabsorption.",
    "Incorrect — the bladder stores urine; it is not a significant site of water reabsorption.")

add(74, "ADH increases water reabsorption by making the collecting duct more permeable to water.",
    "ADH (vasopressin), released from the posterior pituitary in response to low blood volume/high blood osmolarity, inserts aquaporin water channels into the collecting duct's cell membranes, allowing more water to be reabsorbed back into the blood, concentrating the urine and raising blood volume.",
    "ADH acts specifically on the COLLECTING DUCT's water PERMEABILITY (via aquaporins) — it does not act on the glomerulus/filtration step at all.",
    "Incorrect — ADH is released specifically to counteract low blood volume by promoting water retention, not to intentionally decrease blood volume further.",
    "Correct — increasing collecting duct permeability to water (via aquaporin insertion) is exactly how ADH boosts reabsorption.",
    "Incorrect — ADH does not act on the glomerulus or block filtration; its target is the collecting duct.",
    "Incorrect — ADH decreases urine volume (by promoting water reabsorption), the opposite of increasing it.")

add(75, "Dendrites are the parts of a neuron that receive signals from other neurons.",
    "Dendrites are branched extensions from the cell body that receive neurotransmitter signals at synapses and convert them into electrical signals (graded potentials) that travel toward the cell body, and then, if strong enough, trigger an action potential down the axon.",
    "Dendrites RECEIVE signals (input); the axon SENDS signals away (output) toward the next neuron/synapse — the two ends of information flow through a neuron.",
    "Incorrect — the cell body integrates signals and contains the nucleus, but the dendrites specifically are the receiving branches.",
    "Incorrect — the axon carries signals AWAY from the cell body toward the synapse, not the receiving end.",
    "Correct — dendrites are specifically the receiving structures of a neuron.",
    "Incorrect — the myelin sheath insulates the axon to speed conduction; it doesn't receive signals.")

add(76, "Neurotransmitters are stored in synaptic vesicles within the presynaptic neuron before release.",
    "The presynaptic neuron's axon terminal contains membrane-bound synaptic vesicles packed with neurotransmitter molecules; an arriving action potential triggers calcium influx, causing these vesicles to fuse with the presynaptic membrane and release their contents into the synaptic cleft.",
    "Neurotransmitters are stored PRESYNAPTICALLY (in vesicles, before release) — the postsynaptic neuron only receives them afterward via receptors, it doesn't store them.",
    "Incorrect — mitochondria supply ATP for the process, but neurotransmitters themselves are stored in vesicles, and this is presynaptic, not postsynaptic.",
    "Incorrect — the postsynaptic neuron's nucleus is unrelated to neurotransmitter storage; that occurs in the presynaptic terminal.",
    "Incorrect — the myelin sheath insulates axons; it plays no role in neurotransmitter storage.",
    "Correct — synaptic vesicles in the presynaptic neuron's terminal are where neurotransmitters are stored before release.")

add(77, "The thyroid gland's hormones primarily regulate the body's metabolic rate.",
    "Thyroid hormones (T3/T4) increase basal metabolic rate, influencing oxygen consumption, heat production, and overall energy use in nearly all body tissues; imbalances cause conditions like hypothyroidism (low metabolism) or hyperthyroidism (high metabolism).",
    "Thyroid = metabolic rate; pancreas (insulin/glucagon) = blood glucose; parathyroid = blood calcium; adrenal medulla = fight-or-flight — don't mix up which gland regulates which system.",
    "Correct — regulating overall metabolic rate is the thyroid gland's primary, defining hormonal role.",
    "Incorrect — blood glucose regulation is primarily the job of the pancreas (insulin and glucagon), not the thyroid.",
    "Incorrect — blood calcium regulation is primarily controlled by the parathyroid glands (parathyroid hormone), not the thyroid.",
    "Incorrect — the fight-or-flight response is driven mainly by the adrenal medulla (adrenaline), not the thyroid.")

add(78, "Negative feedback maintains hormone levels within a stable range by inhibiting further release once levels are sufficient.",
    "In negative feedback loops (like thyroid hormone regulation via the hypothalamus-pituitary-thyroid axis), rising hormone levels signal back to suppress further release, preventing overproduction and keeping levels within a healthy homeostatic range — the dominant regulatory pattern in the endocrine system.",
    "Negative feedback = self-limiting/stabilizing (the more common pattern); positive feedback = self-amplifying (rarer, e.g. childbirth contractions) — don't confuse the two.",
    "Incorrect — negative feedback specifically prevents unlimited increase; it self-limits hormone levels rather than continuously raising them.",
    "Correct — inhibiting further hormone release once levels are adequate, to maintain a stable range, is exactly how negative feedback works.",
    "Incorrect — negative feedback is a major, active regulatory mechanism throughout the endocrine system, not something with no effect.",
    "Incorrect — negative feedback regulates many hormones (thyroid, cortisol, sex hormones, etc.), not only insulin.")

add(79, "Fertilization in females typically occurs in the fallopian tube (oviduct).",
    "After ovulation, the egg travels into the fallopian tube, where sperm (having traveled up from the vagina, through the uterus) typically meet and fertilize it; the resulting zygote then continues moving toward the uterus for implantation.",
    "Fertilization happens in the fallopian TUBE, not the uterus (that's where implantation occurs afterward) — a commonly confused pair of locations.",
    "Incorrect — the uterus is where the resulting embryo implants afterward, not typically where fertilization itself occurs.",
    "Incorrect — the ovary is where the egg is released from (ovulation), not where sperm typically meets and fertilizes it.",
    "Correct — the fallopian tube (oviduct) is the typical site of fertilization.",
    "Incorrect — the vagina is the site of sperm deposition/entry, well before sperm travels up to the fallopian tube where fertilization occurs.")

add(80, "Progesterone maintains the uterine lining, preparing for and sustaining pregnancy.",
    "Secreted mainly by the corpus luteum (and later the placenta), progesterone thickens and maintains the endometrium (uterine lining), suppresses further ovulation, and supports pregnancy; falling progesterone levels (if no pregnancy occurs) trigger menstruation.",
    "Progesterone MAINTAINS the lining (supports pregnancy); its drop (not itself) triggers menstruation — a subtle but important distinction.",
    "Incorrect — a surge in LH (not progesterone) triggers ovulation.",
    "Incorrect — menstruation is triggered by a DROP in progesterone (and estrogen), not by progesterone acting to cause it.",
    "Incorrect — sperm production (spermatogenesis) is regulated by testosterone/FSH/LH in males, unrelated to progesterone's role.",
    "Correct — maintaining the uterine lining for and during pregnancy is progesterone's key function.")

add(81, "On average, only about 10% of energy transfers from one trophic level to the next in an ecosystem.",
    "Following the '10% rule' (an approximation), most energy at each trophic level is lost as heat through metabolism, movement, and incomplete consumption, so only roughly 10% of the energy is available to the next level up — explaining why food chains rarely extend beyond 4-5 levels and why higher trophic levels support far less biomass.",
    "This '10% rule' is a very frequently tested ecology figure — energy transfer efficiency between trophic levels is low, not anywhere near 50% or higher.",
    "Correct — approximately 10% is the standard estimate for energy transfer efficiency between successive trophic levels.",
    "Incorrect — 50% dramatically overstates real trophic transfer efficiency, which is much lower due to heat/metabolic losses.",
    "Incorrect — 90% would mean almost no energy is lost, wildly inconsistent with the actual inefficiency of trophic energy transfer.",
    "Incorrect — 100% would mean no energy loss at all between levels, which never happens due to respiration, movement, and incomplete consumption.")

data = E
print(f"Batch 2: {len(data)} entries, ids {data[0]['id']}-{data[-1]['id']}")
assert len(data) == 40
OUT.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
print("wrote", OUT)
