import json
from pathlib import Path

OUT = Path(__file__).parent / "mock18_explanations_biology_1.json"

# id = paper_order + 7944
def I(po): return po + 7944

E = []

def add(po, short, long, trick, a, b, c, d):
    E.append({
        "id": I(po), "short": short, "long": long, "trick": trick,
        "options": {"a": a, "b": b, "c": c, "d": d}
    })

add(1, "Sucrose is a disaccharide (glucose + fructose); the others are monosaccharides or a lipid component.",
    "Disaccharides form when two monosaccharides join via a glycosidic bond with loss of water. Sucrose = glucose + fructose. Glucose and ribose are monosaccharides (single sugar units), and glycerol is a lipid-building alcohol, not a sugar at all.",
    "Watch for monosaccharide names that sound similar (glucose, ribose) — only a compound sugar built from two units counts as a disaccharide.",
    "Correct — sucrose is glucose + fructose joined by a glycosidic bond, the classic disaccharide.",
    "Incorrect — glucose is a single monosaccharide, not a disaccharide.",
    "Incorrect — ribose is a monosaccharide (a 5-carbon sugar in RNA/ATP).",
    "Incorrect — glycerol is a 3-carbon alcohol, the backbone of lipids, not a sugar at all.")

add(2, "Amino acids are the monomers that polymerize (via peptide bonds) to form proteins.",
    "Proteins are polymers of amino acids linked by peptide bonds formed between the carboxyl group of one amino acid and the amino group of the next, with loss of water (condensation/dehydration synthesis).",
    "Don't mix up monomer-polymer pairs: amino acids->proteins, nucleotides->nucleic acids, monosaccharides->polysaccharides, fatty acids(+glycerol)->lipids.",
    "Correct — amino acids link via peptide bonds to build polypeptide chains (proteins).",
    "Incorrect — fatty acids are lipid building blocks, not protein building blocks.",
    "Incorrect — nucleotides are the monomers of nucleic acids (DNA/RNA), not proteins.",
    "Incorrect — monosaccharides are the monomers of carbohydrates (polysaccharides), not proteins.")

add(3, "Secondary structure (helices/sheets) is stabilized by hydrogen bonds along the polypeptide backbone.",
    "Alpha helices and beta sheets form when hydrogen bonds arise between the backbone C=O and N-H groups of the polypeptide chain at regular intervals, independent of the specific side chains present. Side-chain (R-group) interactions like disulfide bridges, ionic bonds, and hydrophobic interactions instead stabilize tertiary structure.",
    "Backbone H-bonds = secondary structure; R-group (side chain) interactions = tertiary structure — a very common exam distinction.",
    "Incorrect — disulfide bridges (between cysteine side chains) mainly stabilize tertiary/quaternary structure, and are not the exclusive stabilizer even there.",
    "Incorrect — ionic bonds between side chains contribute to tertiary structure, not the backbone H-bonding pattern of secondary structure.",
    "Correct — regular backbone hydrogen bonding is exactly what forms and stabilizes alpha helices and beta sheets.",
    "Incorrect — hydrophobic interactions between side chains (which can be far apart in sequence) drive tertiary folding, not secondary structure.")

add(4, "Triglycerides are the body's main long-term, energy-dense storage molecules.",
    "Triglycerides (three fatty acids esterified to glycerol) store roughly twice the energy per gram of carbohydrates, making them the body's primary long-term fuel reserve, stored mainly in adipose tissue.",
    "Don't confuse triglycerides (energy storage) with phospholipids (membrane structure) — both are lipids but serve very different roles.",
    "Incorrect — genetic material is DNA/RNA (nucleic acids), not lipids.",
    "Incorrect — ribosomes are built from rRNA and protein, not triglycerides.",
    "Incorrect — enzymes are proteins; triglycerides have no catalytic function.",
    "Correct — triglycerides are energy-dense molecules stored long-term in fat (adipose) tissue.")

add(5, "Denaturation unfolds a protein's higher-order structure (breaking weak bonds) without necessarily breaking the peptide-bond backbone.",
    "Heat, pH extremes, or chemicals disrupt the hydrogen bonds, ionic bonds, and hydrophobic interactions that hold a protein's secondary/tertiary/quaternary shape — destroying its specific 3D conformation and thus its function — while the primary sequence (peptide bonds) typically remains intact.",
    "Denaturation is about losing SHAPE, not about breaking the amino acid chain itself (that would require hydrolysis, a different process).",
    "Correct — denaturation disrupts folding/shape (secondary/tertiary/quaternary bonds), not necessarily the primary peptide backbone.",
    "Incorrect — breaking peptide bonds describes hydrolysis/digestion, not denaturation.",
    "Incorrect — denaturation does not change a protein's chemical class into a carbohydrate.",
    "Incorrect — denaturation specifically destroys the 3D shape, which is the whole basis of losing function.")

add(6, "Enzymes are biological catalysts: they speed up reactions and are not consumed or permanently changed.",
    "Enzymes lower the activation energy of a reaction by stabilizing the transition state, dramatically increasing reaction rate, while emerging chemically unchanged at the end — allowing them to be reused repeatedly.",
    "A catalyst (enzyme) is never consumed like a substrate — if an answer choice implies the enzyme is 'used up', it's wrong.",
    "Correct — enzymes catalyze reactions without being permanently altered or consumed.",
    "Incorrect — substrates, not enzymes, are consumed and converted into products.",
    "Incorrect — enzymes are not simply respiration products; most are proteins synthesized via gene expression.",
    "Incorrect — enzymes are defined by their catalytic role, the opposite of this statement.")

add(7, "Competitive inhibitors resemble the substrate and physically occupy the active site, blocking substrate binding.",
    "Because competitive inhibitors have a shape similar to the natural substrate, they can bind the active site directly, 'competing' with substrate for that site. Increasing substrate concentration can outcompete/overcome this type of inhibition.",
    "Competitive = active site + substrate-like shape; non-competitive = a different (allosteric) site entirely — don't mix the two mechanisms up.",
    "Incorrect — binding an allosteric site describes non-competitive inhibition, not competitive.",
    "Incorrect — competitive inhibition is typically reversible; it doesn't destroy the enzyme.",
    "Correct — resembling the substrate and physically blocking the active site is the defining feature of competitive inhibition.",
    "Incorrect — inhibitors reduce, not increase, effective enzyme activity.")

add(8, "Well above the optimum temperature, enzymes denature and activity drops sharply.",
    "Enzyme activity rises with temperature only up to an optimum (more frequent, higher-energy collisions); beyond that point, heat disrupts the enzyme's tertiary structure (denaturation), rapidly destroying its active site and causing a sharp drop in activity.",
    "The enzyme-activity-vs-temperature curve is a rise-then-sharp-fall shape, not an endless increase — the fall is denaturation, not just 'slowing down'.",
    "Incorrect — activity does not increase indefinitely; it collapses past the optimum due to denaturation.",
    "Incorrect — there's no fixed 'doubling per degree' rule, and this ignores denaturation entirely.",
    "Incorrect — activity changes dramatically with temperature; it is not constant.",
    "Correct — excessive heat denatures the enzyme's active site, sharply decreasing activity.")

add(9, "Non-competitive inhibitors bind elsewhere (not the active site) and change the enzyme's shape so substrate no longer fits well.",
    "Unlike competitive inhibitors, non-competitive inhibitors bind an allosteric (different) site, inducing a conformational change that distorts the active site, reducing catalytic efficiency even if substrate is still present in excess.",
    "Increasing substrate concentration overcomes competitive inhibition but NOT non-competitive inhibition, since the active site itself is distorted.",
    "Correct — binding elsewhere and reshaping the enzyme (including its active site) is exactly how non-competitive inhibition works.",
    "Incorrect — competing directly at the active site describes competitive, not non-competitive, inhibition.",
    "Incorrect — inhibitors decrease, not increase, an enzyme's effective affinity/activity.",
    "Incorrect — non-competitive inhibition is a general mechanism, not limited to cofactor-lacking enzymes.")

add(10, "Ribosomes are the cellular machinery for protein synthesis (translation).",
    "Ribosomes, made of rRNA and protein, read mRNA codons and assemble the corresponding amino acid sequence into a polypeptide chain — this process is called translation.",
    "Don't confuse ribosomes (protein synthesis) with the nucleus (DNA replication) or mitochondria (ATP production).",
    "Incorrect — lipid digestion involves lipase enzymes, unrelated to ribosome function.",
    "Correct — ribosomes translate mRNA into protein, their defining cellular role.",
    "Incorrect — DNA replication occurs in the nucleus, carried out by DNA polymerase, not ribosomes.",
    "Incorrect — ATP breakdown/production is mainly a mitochondrial function, not a ribosomal one.")

add(11, "The Golgi apparatus modifies, sorts, and packages proteins for secretion or delivery to their destination.",
    "Proteins arriving from the rough ER are chemically modified (e.g. glycosylation) in the Golgi's cisternae, then sorted into vesicles and directed to the plasma membrane, lysosomes, or for secretion outside the cell.",
    "Rough ER makes/folds proteins; Golgi apparatus modifies/packages/ships them — a frequently tested two-step pathway.",
    "Incorrect — the nucleus, not the Golgi, stores genetic material (DNA).",
    "Incorrect — ATP production via respiration occurs mainly in mitochondria.",
    "Correct — modifying, sorting, and packaging proteins for secretion/delivery is the Golgi's defining role.",
    "Incorrect — photosynthesis occurs in chloroplasts, an entirely different organelle.")

add(12, "The diagram's structure X (the inner membrane) is folded into cristae to expand surface area for ATP synthesis.",
    "In a mitochondrion, W = smooth outer membrane, Z = the narrow intermembrane space, Y = the matrix (interior fluid), and X = the inner membrane, which folds inward into cristae — increasing surface area to host more electron transport chain complexes and ATP synthase, boosting ATP output.",
    "Only the INNER membrane folds into cristae; the outer membrane (W) stays smooth — don't mix up which membrane the question is describing.",
    "Incorrect — Structure W is the smooth outer membrane; it does not fold into cristae.",
    "Incorrect — Structure Z, the intermembrane space, is a thin fluid-filled gap, not a folded membrane.",
    "Incorrect — Structure Y, the matrix, is the interior compartment enclosed by the inner membrane, not the membrane itself.",
    "Correct — Structure X, the inner membrane, folds into cristae to maximize surface area for ATP synthase and the electron transport chain.")

add(13, "Centrioles organize the mitotic spindle fibers that pull chromosomes apart during cell division.",
    "Centrioles form the centrosome, which nucleates microtubules that make up the spindle apparatus, guiding chromosome movement during mitosis and meiosis.",
    "Centrioles are found in animal cells (mostly absent in higher plants) and relate specifically to spindle organization, not photosynthesis or RNA synthesis.",
    "Correct — organizing spindle fibers for chromosome separation is the centrioles' primary role in cell division.",
    "Incorrect — photosynthesis occurs in chloroplasts (in plants/algae), unrelated to centrioles.",
    "Incorrect — ribosomal RNA is produced in the nucleolus, not by centrioles.",
    "Incorrect — lipid droplet storage is unrelated to centriole function.")

add(14, "Nuclear pores regulate selective passage of molecules like RNA and proteins between nucleus and cytoplasm.",
    "The nuclear envelope is studded with pore complexes that allow controlled, selective transport — e.g. mRNA and ribosomal subunits exit to the cytoplasm, while regulatory proteins and nucleotides enter the nucleus — rather than blocking or allowing everything indiscriminately.",
    "Nuclear pores are selective gates, not simple open holes or total barriers — both extremes ('block everything' / 'only water') are wrong.",
    "Incorrect — pores allow selective passage; they don't block all molecules.",
    "Correct — nuclear pores regulate the controlled exchange of molecules like RNA and proteins across the nuclear envelope.",
    "Incorrect — pores pass far more than just water; they are essential for macromolecule traffic.",
    "Incorrect — nuclear pores have a critical, well-defined transport function.")

add(15, "Cells with high energy demands (like muscle or liver cells) contain unusually large numbers of mitochondria.",
    "Since mitochondria are the primary site of ATP production via aerobic respiration, cells that need large, continuous amounts of energy (muscle contraction, liver metabolism) pack in many more mitochondria than low-energy-demand cells.",
    "Mature red blood cells actually lack mitochondria and nuclei entirely (to maximize oxygen-carrying space) — a classic trick option to rule out.",
    "Incorrect — a low-energy-demand skin cell would need fewer, not more, mitochondria.",
    "Incorrect — mature red blood cells lack mitochondria (and a nucleus) entirely.",
    "Correct — muscle and liver cells have high, continuous energy needs, matched by a high mitochondria count.",
    "Incorrect — a cell that doesn't respire would have no functional need for mitochondria at all.")

add(16, "Osmosis is specifically the diffusion of water across a selectively permeable membrane.",
    "Osmosis is a special case of diffusion limited to water molecules, moving from a region of higher water potential (lower solute concentration) to lower water potential (higher solute concentration) across a membrane that is permeable to water but restricts solutes.",
    "General 'diffusion' can apply to gases, ions, or any particle; 'osmosis' is reserved specifically for water movement — precise vocabulary matters here.",
    "Incorrect — osmosis refers to water, not gases.",
    "Incorrect — protein movement across membranes is typically active/vesicular transport, not osmosis.",
    "Incorrect — ion movement against a gradient describes active transport, not osmosis.",
    "Correct — osmosis is, by definition, the diffusion of water across a selectively permeable membrane.")

add(17, "Active transport requires ATP to move substances against their concentration gradient.",
    "Passive transport (diffusion, facilitated diffusion, osmosis) moves substances down their gradient with no energy input; active transport pumps substances the 'uphill' direction (low to high concentration), which requires ATP hydrolysis to power carrier proteins like the sodium-potassium pump.",
    "'Against the gradient' + 'requires ATP' are the two hallmark, always-paired features of active transport.",
    "Correct — moving substances against their gradient always costs ATP, the defining feature of active transport.",
    "Incorrect — many active transport pumps (e.g. Na+/K+ pump) absolutely require carrier proteins.",
    "Incorrect — moving down a gradient describes passive transport, the opposite of active transport.",
    "Incorrect — active transport occurs in animal cells too (e.g. neurons, kidney cells), not only plant cells.")

add(18, "In a hypertonic external solution, a plant cell loses water and undergoes plasmolysis.",
    "A hypertonic solution has a higher solute concentration outside than inside the cell, so water leaves the cell by osmosis; the protoplast (cell membrane + cytoplasm) shrinks and pulls away from the rigid cell wall — this is plasmolysis.",
    "Turgor pressure rises in a HYPOtonic solution (water enters); plasmolysis happens in a HYPERtonic one (water leaves) — don't flip the prefixes.",
    "Incorrect — turgor pressure increases in a hypotonic (not hypertonic) solution, as water enters the cell.",
    "Correct — water leaving the cell in a hypertonic solution causes the membrane to pull away from the wall (plasmolysis).",
    "Incorrect — bursting (lysis) would occur in a very hypotonic solution in a cell lacking a wall, not here.",
    "Incorrect — a hypertonic environment does cause a clear, measurable change (water loss/plasmolysis).")

add(19, "The Na+/K+ pump moves 3 Na+ out of the cell and 2 K+ into the cell per ATP cycle.",
    "This electrogenic pump uses the energy of one ATP hydrolysis to export 3 sodium ions and import 2 potassium ions each cycle, maintaining the resting membrane potential and the concentration gradients neurons and other cells depend on.",
    "The classic ratio to memorize is 3 Na+ out : 2 K+ in — reversing these numbers is a very common wrong-answer trap.",
    "Incorrect — the pump does not move equal numbers of each ion, nor in the same direction.",
    "Incorrect — this reverses the correct ratio; it's 3 Na+ out and 2 K+ in, not 2 out/3 in.",
    "Correct — 3 Na+ pumped out and 2 K+ pumped in per ATP cycle is the defining stoichiometry of this pump.",
    "Incorrect — the pump moves both Na+ and K+, not Na+ alone.")

add(20, "Facilitated diffusion uses a carrier/channel protein but needs no ATP, since it still moves substances down their gradient.",
    "Facilitated diffusion is passive: molecules that can't cross the membrane unaided (like glucose or ions) move through specific carrier or channel proteins, but always down their concentration gradient, so no cellular energy is spent.",
    "'Carrier protein' does not automatically mean 'active transport' — check the direction of movement (down gradient = passive/no ATP; against gradient = active/needs ATP).",
    "Incorrect — endocytosis is vesicle-based bulk transport requiring ATP, not a simple carrier-protein process.",
    "Incorrect — active transport requires ATP by definition.",
    "Incorrect — exocytosis is vesicle-based and requires ATP.",
    "Correct — facilitated diffusion uses carrier/channel proteins but moves substances down their gradient, needing no ATP.")

add(21, "Interphase is made up of the G1, S, and G2 sub-phases (cell growth and DNA replication, no division yet).",
    "Interphase, the longest part of the cell cycle, includes G1 (growth, organelle duplication), S phase (DNA replication), and G2 (further growth and preparation for mitosis) — mitosis and cytokinesis follow afterward as separate phases.",
    "Interphase is everything BEFORE mitosis (G1-S-G2); don't confuse it with the M phase (mitosis + cytokinesis) itself.",
    "Correct — G1, S, and G2 together make up interphase, the cell's growth and DNA-replication period.",
    "Incorrect — mitosis is the phase that FOLLOWS interphase, not part of it.",
    "Incorrect — cytokinesis is the final division of the cytoplasm, occurring after mitosis, not during interphase.",
    "Incorrect — prophase and metaphase are stages of mitosis, not interphase.")

add(22, "Sister chromatids separate and move to opposite poles during anaphase.",
    "In anaphase, the centromere splits and spindle fibers shorten, pulling each pair of sister chromatids apart toward opposite spindle poles — ensuring each daughter cell receives a complete chromosome set.",
    "Order to remember: Prophase (condense) -> Metaphase (align) -> Anaphase (separate/pull apart) -> Telophase (reform nuclei).",
    "Incorrect — in prophase, chromosomes condense but sister chromatids are still joined, not yet separating.",
    "Correct — anaphase is specifically defined by sister chromatid separation toward opposite poles.",
    "Incorrect — in metaphase, chromosomes align at the cell's equator but have not yet separated.",
    "Incorrect — interphase precedes mitosis entirely; no chromosome separation occurs here.")

add(23, "Meiosis produces four genetically distinct haploid daughter cells, unlike mitosis.",
    "Mitosis produces two genetically identical diploid cells for growth/repair. Meiosis involves two divisions (I and II) with crossing-over and independent assortment, yielding four haploid cells that are genetically distinct from each other and the parent cell — essential for sexual reproduction.",
    "Mitosis: 2 diploid, identical. Meiosis: 4 haploid, genetically varied. Keep these two outcomes clearly separated.",
    "Incorrect — this describes a typical mitotic outcome (identical diploid cells), not meiosis.",
    "Incorrect — meiosis does not stop at one diploid + one haploid cell; it fully halves chromosome number across all four products.",
    "Correct — meiosis yields four genetically distinct haploid cells, the basis of gametes.",
    "Incorrect — meiosis definitely produces new (four) daughter cells.")

add(24, "With 2n = 24, each haploid gamete produced by meiosis carries n = 12 chromosomes.",
    "Meiosis halves the chromosome number: starting from a diploid (2n) cell, each of the four resulting gametes is haploid (n). Since 2n = 24, n = 24 / 2 = 12.",
    "2n refers to the diploid (body cell) number; gametes are always haploid (n), i.e. exactly half — a very common calculation trap is forgetting to divide by 2.",
    "Incorrect — 24 is the diploid (2n) number, describing the parent cell, not the haploid gamete.",
    "Incorrect — 6 would be a quarter of 24, not the correct half.",
    "Incorrect — 48 would be double 24 (as if 2n were doubled again), the opposite of what meiosis does.",
    "Correct — 24 / 2 = 12, the haploid chromosome number carried by each gamete.")

add(25, "The spindle assembly checkpoint ensures all chromosomes are properly attached to spindle fibers before anaphase can begin.",
    "This checkpoint monitors kinetochore-spindle fiber attachment at each chromosome; if any chromosome is unattached or improperly attached, the cell cycle halts before anaphase, preventing chromosome mis-segregation (a source of aneuploidy).",
    "This checkpoint acts right before ANAPHASE (M-phase), not at S-phase entry or based on nutrient availability — those are different checkpoints (G1/G2).",
    "Correct — verifying complete spindle attachment before allowing anaphase to proceed is exactly this checkpoint's role.",
    "Incorrect — checking DNA replication is complete is the role of the G2 checkpoint, not the spindle assembly checkpoint.",
    "Incorrect — nutrient/growth-factor checks happen at the G1 checkpoint (restriction point), not the spindle assembly checkpoint.",
    "Incorrect — cytokinesis follows mitosis; this checkpoint concerns chromosome attachment, not division timing relative to cytokinesis.")

add(26, "Apoptosis is a programmed, tightly regulated process of cell death, not accidental or uncontrolled.",
    "Unlike necrosis (accidental, damage-triggered cell death causing inflammation), apoptosis is an orderly, genetically programmed process — cells shrink, DNA fragments, and the cell is cleanly broken into membrane-bound bodies removed by phagocytes, important in development and tissue homeostasis.",
    "Apoptosis is deliberate and controlled ('cell suicide'), distinct from cell division (mitosis/meiosis) or accidental death (necrosis).",
    "Incorrect — apoptosis is precisely the opposite: a tightly regulated, controlled process, not uncontrolled division.",
    "Correct — apoptosis is defined as programmed, regulated cell death.",
    "Incorrect — apoptosis is cell death, not a type of cell division like mitosis.",
    "Incorrect — meiosis produces gametes; it is unrelated to programmed cell death.")

add(27, "A Tt x tt cross (testcross) yields offspring in a 1 tall : 1 short ratio.",
    "Tt produces gametes T and t in equal proportion; tt produces only t gametes. Combining: Tt (tall) and tt (short) offspring occur in a 1:1 ratio — this is the classic testcross pattern used to reveal an unknown genotype.",
    "A cross against a homozygous recessive (tt) is called a testcross, and it always splits the heterozygous parent's gametes 1:1 into the offspring phenotypes.",
    "Incorrect — 'all tall' would only happen if the cross were TT x tt, not Tt x tt.",
    "Incorrect — 3:1 is the ratio from a heterozygous x heterozygous (Tt x Tt) cross, not a testcross.",
    "Correct — Tt x tt (a testcross) produces a 1 tall : 1 short ratio.",
    "Incorrect — 'all short' would require both parents to be tt, but one parent here (Tt) still carries the dominant T allele.")

add(28, "Aa x Aa produces offspring in a 1 AA : 2 Aa : 1 aa genotype ratio.",
    "Each Aa parent produces A and a gametes in equal (1:1) proportion. A Punnett square combining A/a x A/a gives genotypes AA, Aa, Aa, aa — i.e. 1 AA : 2 Aa : 1 aa (the classic monohybrid genotype ratio, corresponding to a 3:1 phenotype ratio if A is dominant).",
    "Don't confuse the GENOTYPE ratio (1:2:1) with the PHENOTYPE ratio (3:1) from the same Aa x Aa cross — this question specifically asks for genotype.",
    "Incorrect — 3 AA : 1 aa isn't a valid outcome of this cross; heterozygotes (Aa) are the most common genotype, not absent.",
    "Incorrect — 'All Aa' would only occur from a cross like AA x aa, not Aa x Aa.",
    "Incorrect — 1 AA : 1 aa omits the heterozygous (Aa) offspring, which actually make up half the total.",
    "Correct — the standard monohybrid cross genotype ratio is 1 AA : 2 Aa : 1 aa.")

add(29, "X-linked recessive disorders show up more in males because they have only one X chromosome, so one recessive allele is enough to be expressed (no second X to mask it).",
    "Males are XY, so any recessive allele on their single X chromosome is automatically expressed (hemizygous), with no second X to potentially carry a dominant, masking allele. Females (XX) need the recessive allele on both X chromosomes to show the trait, making them far more likely to be unaffected carriers.",
    "The key word is 'hemizygous' — males have only ONE copy of X-linked genes, so recessive alleles there can't be 'hidden' the way they can in females.",
    "Correct — having only one X chromosome means males express any recessive allele present there, with no second copy to mask it.",
    "Incorrect — males have only ONE X chromosome (plus a Y), not two — this is factually backward.",
    "Incorrect — females can and do carry the recessive allele, typically without expressing the disorder (if heterozygous).",
    "Incorrect — X-linked recessive disorders clearly can and do affect males; this is why they're more common in males, not absent.")

add(30, "In an AaBb x AaBb dihybrid cross, 1/16 of offspring are expected to be homozygous recessive for both traits (aabb).",
    "A dihybrid cross yields the classic 9:3:3:1 phenotype ratio out of 16 total combinations. Each single-gene aa or bb outcome alone has probability 1/4; combined (independent assortment), aabb = 1/4 x 1/4 = 1/16.",
    "For any dihybrid AaBb x AaBb cross, memorize the 9:3:3:1 out of 16 pattern — the fully recessive class (aabb) is always the smallest, 1/16 slice.",
    "Incorrect — 9/16 is the fraction showing BOTH dominant traits (A_B_), the largest class, not the double-recessive class.",
    "Correct — 1/4 (aa) x 1/4 (bb) = 1/16 is the fraction of offspring homozygous recessive for both genes.",
    "Incorrect — 3/16 corresponds to one of the single-dominant/single-recessive combination classes (e.g. A_bb), not aabb.",
    "Incorrect — 1/4 would be the probability for a single gene's recessive class alone, not both genes combined.")

add(31, "AB x O parents can only produce type A or type B children (never AB or O).",
    "Type AB parent contributes either the IA or IB allele; type O parent contributes only the recessive i allele. Possible offspring genotypes are IAi (type A) or IBi (type B) — never both alleles from the AB parent together (that needs another IA or IB donor for AB), and never ii (O) since the AB parent never contributes an i allele.",
    "An AB parent can never have an O child, and an O parent can never have an AB child — remember these two impossible combinations for ABO genetics questions.",
    "Incorrect — 'only AB' is impossible, since the O parent never contributes an IA or IB allele.",
    "Incorrect — 'only O' is impossible, since the AB parent never contributes the recessive i allele.",
    "Correct — offspring can only be genotype IAi (type A) or IBi (type B); AB and O outcomes are both excluded for this parent combination.",
    "Incorrect — AB and O are specifically the two blood types that CANNOT result from this particular cross.")

add(32, "A trait appearing only in children of two unaffected carrier parents, skipping generations, is classic autosomal recessive inheritance.",
    "If both parents are unaffected but heterozygous carriers (Aa), they can still have an affected child (aa) with 1/4 probability, even though neither parent shows the trait — this 'skipping a generation' pattern, unlinked to sex, is the hallmark of autosomal recessive inheritance.",
    "'Two unaffected parents having an affected child' is essentially only possible with recessive inheritance — dominant traits, by contrast, virtually always show up in at least one parent.",
    "Incorrect — autosomal DOMINANT traits show up in at least one parent every generation; they don't skip.",
    "Incorrect — codominant traits produce a blended/mixed phenotype visible in heterozygotes (like AB blood type), not hidden carriers.",
    "Incorrect — Y-linked traits pass only from father to son and would never appear via two unaffected carrier parents this way.",
    "Correct — unaffected carrier parents (Aa x Aa) having an affected (aa) child is the signature pattern of autosomal recessive inheritance.")

add(33, "RR (red) x WW (white) giving all pink (RW) offspring is incomplete dominance — a blended intermediate phenotype.",
    "In incomplete dominance, neither allele is fully dominant, so the heterozygote shows a blended, intermediate phenotype (pink) rather than fully resembling one parent (as in complete dominance) or showing both colors distinctly side-by-side (as in codominance, e.g. spotted).",
    "Incomplete dominance = a BLENDED intermediate look (pink); codominance = BOTH parental traits shown together/distinctly (e.g. roan coat, AB blood type) — don't mix up these two non-Mendelian patterns.",
    "Correct — a single blended intermediate color (pink) between red and white is the defining signature of incomplete dominance.",
    "Incorrect — codominance would show both red and white simultaneously and distinctly (e.g. spotted/streaked), not a uniform blended pink.",
    "Incorrect — epistasis involves one gene masking the expression of a different gene, not a color blend from a single gene.",
    "Incorrect — complete dominance would produce all-red (or all-white) offspring, not an intermediate pink.")

add(34, "Phenotype is the observable physical expression of an organism's genotype.",
    "Genotype is the genetic makeup (allele combination, e.g. Bb); phenotype is how that genotype is actually expressed and observed, such as eye color, height, or blood type.",
    "Genotype = the genetic code itself; phenotype = what you can actually SEE/observe/measure as a result.",
    "Incorrect — genotype is the underlying allele combination, not the observable trait itself.",
    "Correct — phenotype is precisely defined as the observable expression of the genotype.",
    "Incorrect — an allele is one version of a gene, a component of genotype, not the observable trait.",
    "Incorrect — locus refers to a gene's physical position on a chromosome, unrelated to observable traits.")

add(35, "In DNA, adenine (A) pairs with thymine (T) via two hydrogen bonds.",
    "DNA base pairing follows strict complementary rules: A pairs with T (2 H-bonds), and G pairs with C (3 H-bonds). Uracil replaces thymine only in RNA, where it pairs with adenine instead.",
    "In DNA specifically it's A-T (not A-U) — uracil only appears in RNA, replacing thymine there.",
    "Incorrect — guanine pairs with cytosine, not adenine.",
    "Incorrect — cytosine pairs with guanine, not adenine.",
    "Correct — in DNA, adenine specifically pairs with thymine.",
    "Incorrect — uracil is an RNA-only base and replaces thymine there; DNA does not use uracil.")

add(36, "RNA's sugar is ribose, whereas DNA uses deoxyribose (which lacks one oxygen at the 2' carbon).",
    "The 'ribo-' in ribonucleic acid (RNA) directly names its sugar, ribose, which has a hydroxyl (-OH) group at the 2' carbon. DNA's sugar, deoxyribose, lacks that oxygen at the same position (hence 'deoxy-').",
    "Match the name to the sugar: ribonucleic acid -> ribose; deoxyribonucleic acid -> deoxyribose.",
    "Incorrect — deoxyribose is DNA's sugar, not RNA's.",
    "Incorrect — galactose is a hexose sugar unrelated to nucleic acid backbones.",
    "Incorrect — glucose is a hexose sugar, not the pentose sugar found in nucleic acids.",
    "Correct — ribose is the five-carbon sugar found in RNA's backbone.")

add(37, "DNA replication is semi-conservative: each new molecule keeps one original (parental) strand and one newly made strand.",
    "During replication, the double helix unwinds and each original strand serves as a template for building a new complementary strand. The result: two daughter DNA molecules, each a hybrid of one old and one new strand — proven experimentally by the Meselson-Stahl experiment.",
    "'Semi-conservative' literally means half (semi) of the original molecule is conserved (retained) in each daughter molecule — one old strand + one new strand each.",
    "Correct — each daughter DNA molecule contains exactly one original (template) strand and one newly synthesized strand.",
    "Incorrect — this would describe a 'conservative' replication model (both strands new), which is not how replication actually works.",
    "Incorrect — this would describe fully conserving the original molecule intact, contradicting semi-conservative replication.",
    "Incorrect — replication does form two new strands (one per daughter molecule); it does not skip strand synthesis.")

add(38, "Translation is the process of building an amino acid chain (protein) from mRNA codons at the ribosome.",
    "During translation, tRNA molecules bring specific amino acids matching each mRNA codon (via anticodon pairing) to the ribosome, which links them into a growing polypeptide chain in the sequence dictated by the mRNA.",
    "Transcription = DNA -> mRNA (in the nucleus); Translation = mRNA -> protein (at the ribosome) — keep these two steps and their locations straight.",
    "Incorrect — transcription is the DNA-to-mRNA step, which happens in the nucleus, not at the ribosome.",
    "Correct — translation is specifically the mRNA-codon-to-amino-acid-chain process occurring at the ribosome.",
    "Incorrect — replication copies DNA itself; it does not involve building a protein from codons.",
    "Incorrect — splicing removes introns from pre-mRNA during RNA processing, before translation even begins.")

add(39, "A mutation swapping one amino acid for another in the final protein is a missense mutation.",
    "A missense mutation is a point mutation that changes a codon so it now specifies a different amino acid, potentially altering protein structure/function — as opposed to a silent mutation (same amino acid, due to codon redundancy) or a nonsense mutation (a premature stop codon).",
    "Silent = no amino acid change; Missense = different amino acid; Nonsense = new stop codon (truncated protein) — three distinct point-mutation outcomes to keep separate.",
    "Incorrect — a silent mutation changes the codon but NOT the resulting amino acid (due to genetic code redundancy).",
    "Incorrect — a nonsense mutation creates a premature stop codon, truncating the protein, not simply substituting one amino acid.",
    "Correct — changing to a different amino acid at one position is precisely what defines a missense mutation.",
    "Incorrect — a frameshift mutation results from insertions/deletions that are not multiples of three, shifting the entire reading frame, not a single-codon substitution.")

add(40, "Inserting a single nucleotide shifts the reading frame, altering every codon downstream of the insertion — a frameshift mutation.",
    "Since codons are read in fixed groups of three, adding (or removing) one nucleotide (not a multiple of three) shifts how all subsequent nucleotides are grouped into codons, typically scrambling the entire downstream amino acid sequence and often introducing a premature stop codon.",
    "Insertions/deletions of a NON-multiple of three cause frameshifts; insertions/deletions of exactly three nucleotides just add/remove one amino acid without shifting the frame.",
    "Incorrect — a single-nucleotide insertion drastically changes the protein by shifting the whole downstream reading frame.",
    "Incorrect — a frameshift typically disrupts, rather than stabilizes, protein structure and function.",
    "Incorrect — a frameshift is the opposite of 'silent' — it usually scrambles many codons, not none.",
    "Correct — a single-nucleotide insertion shifts the reading frame, altering every downstream codon.")

add(41, "HIV, a retrovirus, uses reverse transcriptase to convert its RNA genome into DNA inside the host cell.",
    "Retroviruses carry RNA genomes but must integrate into host DNA to replicate; reverse transcriptase catalyzes synthesis of complementary DNA (cDNA) from the viral RNA template, reversing the usual DNA-to-RNA direction of the central dogma.",
    "'Retro' signals reverse transcription: RNA -> DNA, the opposite direction of normal transcription (DNA -> RNA) — a defining, testable feature of retroviruses like HIV.",
    "Correct — reverse transcriptase is the defining enzyme retroviruses like HIV use to make DNA from their RNA genome.",
    "Incorrect — DNA polymerase copies DNA from a DNA template; it can't use an RNA template the way reverse transcriptase does.",
    "Incorrect — RNA polymerase makes RNA from DNA (normal transcription), the opposite direction needed here.",
    "Incorrect — ligase joins DNA fragments together; it doesn't synthesize DNA from an RNA template.")

data = E
print(f"Batch 1: {len(data)} entries, ids {data[0]['id']}-{data[-1]['id']}")
assert len(data) == 41
OUT.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
print("wrote", OUT)
