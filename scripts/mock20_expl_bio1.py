import json
from pathlib import Path

EXPL = {
8305: dict(
    short="Glycogen is a polysaccharide (a polymer of many glucose units).",
    long="A polysaccharide is a large carbohydrate polymer made of many monosaccharide units joined together. Glycogen (animal storage carbohydrate) fits this, while glucose and fructose are monosaccharides and sucrose is a disaccharide.",
    trick="Don't be fooled by sucrose sounding complex — it's only two sugar units joined (a disaccharide), not a full polysaccharide.",
    options=dict(a="Fructose is a monosaccharide, not a polysaccharide.",
                 b="Correct — glycogen is a polysaccharide made of many glucose units.",
                 c="Glucose is a single monosaccharide unit.",
                 d="Sucrose is a disaccharide (two units), not a polysaccharide.")
),
8306: dict(
    short="Nucleic acids (DNA/RNA) are built from repeating nucleotide units.",
    long="Nucleotides — each made of a sugar, phosphate, and nitrogenous base — are the monomer building blocks that polymerize to form DNA and RNA.",
    trick="Don't confuse this with the building blocks of proteins (amino acids) or carbohydrates (monosaccharides) — nucleic acids specifically use nucleotides.",
    options=dict(a="Amino acids are the building blocks of proteins, not nucleic acids.",
                 b="Correct — nucleotides are the basic building blocks of nucleic acids.",
                 c="Monosaccharides build carbohydrates, not nucleic acids.",
                 d="Fatty acids are components of lipids, not nucleic acids.")
),
8307: dict(
    short="Primary structure = the linear amino acid sequence joined by peptide bonds.",
    long="A protein's primary structure is simply its sequence of amino acids linked by peptide bonds — the most basic level of protein structure, which then folds into secondary, tertiary, and sometimes quaternary structures.",
    trick="Don't confuse this with tertiary structure (3D shape) or quaternary structure (multiple subunits) — primary structure is purely about the linear sequence.",
    options=dict(a="Overall 3D shape describes tertiary structure, not primary.",
                 b="Interactions between multiple subunits describes quaternary structure, not primary.",
                 c="Correct — primary structure is the linear amino acid sequence.",
                 d="Hydrogen-bonding patterns forming helices describes secondary structure, not primary.")
),
8308: dict(
    short="Unsaturated fatty acids have one or more C=C double bonds, which cause kinks in the chain.",
    long="Unsaturated fatty acids contain at least one carbon-carbon double bond, which introduces a kink/bend in the hydrocarbon chain — this prevents tight packing, making unsaturated fats typically liquid at room temperature (unlike saturated fats).",
    trick="The 'kink' from the double bond is the key structural reason unsaturated fats behave differently (e.g., lower melting points) from saturated fats — remember this cause-and-effect link.",
    options=dict(a="Fatty acids definitely contain carbon atoms — this option is factually wrong.",
                 b="Fatty acid chains contain hydrogen atoms throughout, just fewer at the double-bond positions.",
                 c="Only single bonds throughout describes SATURATED fatty acids, the opposite of unsaturated.",
                 d="Correct — one or more C=C double bonds cause kinks, defining unsaturated fatty acids.")
),
8309: dict(
    short="Chaperone proteins help other proteins fold correctly into their 3D shape.",
    long="Molecular chaperones assist newly synthesized (or stress-denatured) polypeptides in folding into their correct, functional three-dimensional conformation, often preventing improper aggregation during the folding process.",
    trick="Chaperones don't directly power translation or destroy misfolded proteins — that's the job of ribosomes and the proteasome/lysosome system respectively; chaperones specifically assist FOLDING.",
    options=dict(a="Correct — chaperones help polypeptides fold into their correct 3D shape.",
                 b="Providing energy for translation is the ribosome/GTP's role, not chaperones' main function.",
                 c="Permanently inactivating misfolded proteins describes degradation pathways (e.g. proteasome), not chaperone function.",
                 d="Catalyzing peptide bond hydrolysis describes proteases, not chaperones.")
),
8310: dict(
    short="The substrate binds to an enzyme's active site.",
    long="The active site is the specific region of an enzyme's tertiary structure where the substrate binds and the catalyzed reaction occurs.",
    trick="Don't confuse the active site (where substrate binds) with the allosteric site (a separate regulatory binding site for other molecules).",
    options=dict(a="The allosteric site is a separate regulatory binding location, not where substrate binds for catalysis.",
                 b="Correct — the active site is where the substrate binds.",
                 c="'Coenzyme site' isn't the standard term for the substrate-binding region.",
                 d="'Zymogen site' isn't a standard enzyme structural term; zymogens are inactive enzyme precursors.")
),
8311: dict(
    short="pH far below optimum denatures the enzyme, reducing its activity.",
    long="Extreme pH shifts disrupt the ionic and hydrogen bonds maintaining an enzyme's precise 3D shape, denaturing it and destroying (or severely reducing) its catalytic activity.",
    trick="Don't assume 'lower pH' always means 'more acid, more reaction' — enzymes have an OPTIMAL pH range, and moving far outside it in either direction impairs function.",
    options=dict(a="Activity does not increase indefinitely; extreme pH harms enzyme structure and function.",
                 b="Extreme pH DOES affect enzyme structure — that's precisely the mechanism of denaturation.",
                 c="Correct — extreme low pH denatures the enzyme, reducing activity.",
                 d="Extreme pH does not 'double the rate' — it impairs the enzyme instead.")
),
8312: dict(
    short="A coenzyme is a small organic molecule (often from a vitamin) that assists enzyme catalysis.",
    long="Coenzymes are non-protein organic molecules (frequently derived from vitamins, like NAD+ from niacin) that bind to enzymes and assist their catalytic function, often by transferring specific chemical groups.",
    trick="Don't confuse coenzymes (organic, vitamin-derived helper molecules) with cofactors in general (which can include inorganic metal ions) or with the substrate itself.",
    options=dict(a="Enzymes catalyzing independently describes the enzyme itself, not the coenzyme helper molecule.",
                 b="A substrate is the molecule the enzyme acts ON, a completely different role from a coenzyme.",
                 c="Metal ions are a type of INORGANIC cofactor, distinct from organic coenzymes.",
                 d="Correct — a coenzyme is a small organic molecule, often vitamin-derived, assisting enzyme activity.")
),
8313: dict(
    short="Feedback inhibition: the pathway's final product inhibits an earlier enzyme, regulating the pathway.",
    long="In feedback (end-product) inhibition, the final product of a metabolic pathway binds to and inhibits an enzyme earlier in the same pathway, preventing overproduction — a classic form of metabolic self-regulation.",
    trick="Don't confuse this with the reverse (substrate activating the pathway) — feedback inhibition specifically involves the END PRODUCT looping back to slow down an EARLIER step.",
    options=dict(a="Correct — the final product inhibits an earlier enzyme in the pathway, a self-regulating feedback loop.",
                 b="This describes the opposite relationship (substrate activating), not feedback inhibition.",
                 c="Enzymes are typically reused many times (as catalysts), not destroyed after one use.",
                 d="Substrate concentration does affect reaction rate in real enzyme kinetics; this option is incorrect.")
),
8314: dict(
    short="The Golgi apparatus packages and modifies proteins from the ER before shipping them onward.",
    long="The Golgi apparatus receives proteins from the endoplasmic reticulum, further modifies them (e.g. adding sugar groups), sorts them, and packages them into vesicles for transport to their final destinations.",
    trick="Don't confuse the Golgi (packaging/modifying/shipping hub) with the lysosome (digestive organelle) or the ER (initial protein synthesis/folding site) — each has a distinct, specific role.",
    options=dict(a="The lysosome is a digestive organelle, not the packaging/shipping hub described here.",
                 b="Correct — the Golgi apparatus packages and modifies proteins before shipping them onward.",
                 c="Peroxisomes break down fatty acids/toxins, unrelated to this packaging role.",
                 d="The vacuole primarily stores substances/water, not the protein-processing role described here.")
),
8315: dict(
    short="Smooth ER is involved in lipid synthesis and detoxification of drugs.",
    long="Smooth endoplasmic reticulum lacks ribosomes and specializes in lipid (including steroid) synthesis and detoxifying drugs/toxins, especially prominent in liver cells.",
    trick="Don't confuse smooth ER (lipid synthesis/detoxification) with rough ER (protein synthesis, studded with ribosomes) — the 'smooth' vs 'rough' distinction directly maps to these different functions.",
    options=dict(a="Protein synthesis is the role of ROUGH ER (with ribosomes), not smooth ER.",
                 b="ATP production is primarily the mitochondria's role, not the ER's.",
                 c="Correct — smooth ER handles lipid synthesis and drug detoxification.",
                 d="Photosynthesis occurs in chloroplasts (plant cells), unrelated to the ER's function.")
),
8316: dict(
    short="Structure M (the central vacuole) maintains turgor pressure by storing water.",
    long="The large central vacuole in plant cells stores water and dissolved substances; the pressure it exerts against the cell wall (turgor pressure) keeps the cell rigid and supports the plant structurally.",
    trick="Don't confuse the vacuole's water-storage/pressure role with the cell wall's role (providing rigid structural support itself, but not by storing water) — they work together but perform different specific functions.",
    options=dict(a="The nucleus (J) controls cell activities/genetics; it doesn't store water for turgor pressure.",
                 b="The cell wall (K) provides structural rigidity itself, but doesn't store water to create turgor pressure — the vacuole does.",
                 c="Chloroplasts (L) carry out photosynthesis, unrelated to turgor pressure.",
                 d="Correct — the central vacuole (M) stores water, creating turgor pressure that keeps the cell rigid.")
),
8317: dict(
    short="Peroxisomes break down fatty acids and detoxify substances via oxidative reactions.",
    long="Peroxisomes contain oxidative enzymes that break down fatty acids (via beta-oxidation) and detoxify harmful substances (like alcohol), often producing and then neutralizing hydrogen peroxide as a byproduct.",
    trick="Don't confuse peroxisomes with mitochondria (main ATP production via aerobic respiration) or the nucleus (genetic storage) — peroxisomes specifically handle oxidative fatty-acid breakdown and detox.",
    options=dict(a="Correct — peroxisomes break down fatty acids and detoxify substances via oxidative reactions.",
                 b="ATP synthesis via glycolysis occurs in the cytoplasm, not specifically in peroxisomes.",
                 c="Storing genetic material is the nucleus's role, not the peroxisome's.",
                 d="Producing ribosomal subunits is the nucleolus's role, not the peroxisome's.")
),
8318: dict(
    short="Loss of cell cycle checkpoint control can lead to cancerous, uncontrolled cell division.",
    long="Cell cycle checkpoints normally ensure DNA is undamaged/correctly replicated before division proceeds. If a cell loses this regulatory control, it can divide uncontrollably, becoming cancerous.",
    trick="Don't assume checkpoint loss simply stops division — quite the opposite, it often REMOVES the brakes, allowing runaway division (cancer), not a halt to division.",
    options=dict(a="A normal, healthy cell would still have functioning checkpoints — losing them is abnormal.",
                 b="Correct — loss of checkpoint regulation can lead to uncontrolled (cancerous) division.",
                 c="Losing checkpoints tends to REMOVE restraints on division, not prevent division entirely.",
                 d="Cancerous cells remain metabolically active (often highly so), not inactive.")
),
8319: dict(
    short="Exocytosis: a cell expels materials by fusing a vesicle with the plasma membrane.",
    long="Exocytosis is the process by which cells release materials (proteins, waste, etc.) to the outside by fusing a membrane-bound vesicle with the plasma membrane, releasing its contents.",
    trick="Don't confuse exocytosis (materials going OUT via vesicle fusion) with endocytosis (materials coming IN via membrane engulfment) — they're the reverse of each other.",
    options=dict(a="Endocytosis is the reverse process (bringing materials INTO the cell), not exocytosis.",
                 b="Osmosis is the passive movement of water across a membrane, unrelated to vesicle fusion/expulsion.",
                 c="Correct — exocytosis expels materials via vesicle fusion with the plasma membrane.",
                 d="Facilitated diffusion moves specific molecules through membrane proteins, not via vesicle fusion.")
),
8320: dict(
    short="Aquaporins allow rapid, passive movement of water across the membrane.",
    long="Aquaporins are specialized channel proteins that greatly increase the membrane's permeability to water, allowing it to move passively (down its concentration/osmotic gradient) much faster than by simple diffusion through the lipid bilayer alone.",
    trick="Aquaporins are PASSIVE channels (no ATP needed) — don't confuse them with active ion pumps, which do use ATP to move substances against their gradient.",
    options=dict(a="Aquaporins facilitate passive water movement; they don't actively pump ions using ATP.",
                 b="Transmitting electrical signals is the role of ion channels along neurons, not aquaporins specifically.",
                 c="Digesting macromolecules is the role of enzymes (e.g., in lysosomes), not aquaporins.",
                 d="Correct — aquaporins allow rapid, passive movement of water across the membrane.")
),
8321: dict(
    short="In a hypotonic solution, a red blood cell takes in water and may swell/burst (hemolysis).",
    long="A hypotonic solution has a lower solute concentration outside the cell than inside, so water moves INTO the cell by osmosis, causing it to swell and potentially rupture (hemolysis) since animal cells lack a rigid cell wall to resist this expansion.",
    trick="Don't confuse hypotonic (cell swells, water moves IN) with hypertonic (cell shrinks, water moves OUT) — remember 'hypo' = less solute outside = water rushes in.",
    options=dict(a="Correct — in a hypotonic solution, the cell swells and may undergo hemolysis.",
                 b="Shrinking due to water loss would occur in a HYPERTONIC solution, not hypotonic.",
                 c="The cell definitely changes (swells) in a hypotonic solution; it doesn't remain unchanged.",
                 d="Plasmolysis (shrinking due to water loss) is a PLANT cell phenomenon in a hypertonic solution, not what happens to an animal cell here.")
),
8322: dict(
    short="Symport and antiport are both forms of secondary active transport.",
    long="Secondary active transport uses the energy stored in one substance's electrochemical gradient (established by primary active transport) to move another substance against its own gradient — symport moves both substances the same direction, antiport moves them in opposite directions.",
    trick="Don't confuse this with simple diffusion or passive transport — both symport and antiport actively move at least one substance against its gradient, using the coupled energy from another substance's movement.",
    options=dict(a="Simple diffusion involves no carrier proteins or coupled transport, unlike symport/antiport.",
                 b="Correct — symport and antiport are both types of secondary active transport.",
                 c="Osmosis specifically refers to water movement, not the coupled solute transport described by symport/antiport.",
                 d="Both symport and antiport DO require specific transport proteins, so 'passive transport requiring no protein' doesn't fit.")
),
8323: dict(
    short="Cholesterol helps regulate membrane fluidity across a range of temperatures.",
    long="Cholesterol embeds within the phospholipid bilayer and moderates membrane fluidity — preventing it from becoming too rigid at low temperatures and too fluid/permeable at high temperatures.",
    trick="Don't think cholesterol simply 'increases permeability to everything' — its actual role is more nuanced fluidity regulation, helping maintain an optimal, stable membrane state across temperature changes.",
    options=dict(a="Cholesterol doesn't uniformly increase permeability to all molecules; its role is fluidity regulation.",
                 b="Cholesterol is one component among many (phospholipids, proteins, etc.), not the sole component of the membrane.",
                 c="Correct — cholesterol helps regulate membrane fluidity across a range of temperatures.",
                 d="Cholesterol doesn't prevent protein embedding; membrane proteins coexist with cholesterol in the bilayer.")
),
8324: dict(
    short="G1 is the growth phase before DNA replication (S phase).",
    long="The cell cycle's interphase consists of G1 (growth, normal metabolic activity, before DNA replication), S (DNA synthesis/replication), and G2 (further growth/preparation before mitosis).",
    trick="Don't confuse G1 (before replication) with G2 (after replication, before mitosis) — the 'G' phases sandwich the S phase, with G1 coming first.",
    options=dict(a="Mitosis is the division phase itself, occurring after G1, S, and G2.",
                 b="S phase is specifically when DNA replication occurs, not the growth phase before it.",
                 c="G2 occurs AFTER DNA replication (S phase), preparing for mitosis — not before replication.",
                 d="Correct — G1 is the growth phase before DNA replication.")
),
8325: dict(
    short="Chromosomes become visible as condensed structures during prophase.",
    long="During prophase (the first stage of mitosis), chromatin condenses into visible, distinct duplicated chromosomes (each made of two sister chromatids), and the nuclear envelope begins to break down.",
    trick="Don't confuse prophase (condensation begins) with metaphase (chromosomes ALIGNED at the equator) — condensation happens first, in prophase, before alignment.",
    options=dict(a="Correct — chromosomes become visible/condensed during prophase.",
                 b="Metaphase is when chromosomes are ALIGNED at the equator, not when they first become visible.",
                 c="Anaphase is when sister chromatids SEPARATE, a later stage.",
                 d="Telophase is the final stage, when chromosomes decondense as new nuclei form.")
),
8326: dict(
    short="Independent assortment randomly orients homologous pairs at the metaphase plate, distributing maternal/paternal chromosomes independently.",
    long="During meiosis I, homologous chromosome pairs line up randomly at the metaphase plate. Which pole each maternal vs. paternal chromosome goes to is independent of how other pairs orient, generating many possible allele combinations in gametes — a major source of genetic variation.",
    trick="Don't confuse independent assortment (random orientation of DIFFERENT chromosome pairs) with crossing over (exchange of segments WITHIN a homologous pair) — both increase variation but through different mechanisms.",
    options=dict(a="Independent assortment causes VARIED, not identical, chromosome distribution to gametes.",
                 b="Correct — random orientation of homologous pairs leads to independent distribution of maternal/paternal chromosomes.",
                 c="Independent assortment specifically occurs in MEIOSIS (I), not mitosis.",
                 d="Independent assortment doesn't prevent chromosome separation; separation still occurs, just with varied combinations.")
),
8327: dict(
    short="After meiosis I, 2n=8 becomes n=4 (chromosome number halves; count is chromosomes, not chromatids).",
    long="Meiosis I separates homologous chromosome pairs, halving the chromosome number from diploid (2n=8) to haploid (n=4). Each of these 4 chromosomes still has two sister chromatids at this point (not yet separated — that happens in meiosis II), but by convention we count chromosomes, not chromatids.",
    trick="Don't double-count sister chromatids as separate chromosomes — after meiosis I, the CHROMOSOME number is n=4, even though each chromosome still has 2 chromatids joined at a centromere.",
    options=dict(a="8 would be the original diploid number, unchanged — but meiosis I halves this.",
                 b="16 would represent doubling, the opposite of meiosis I's halving effect.",
                 c="Correct — meiosis I halves 2n=8 to n=4 chromosomes.",
                 d="2 is too small; that would represent further halving beyond what meiosis I alone produces.")
),
8328: dict(
    short="Nondisjunction (failed chromosome separation) can produce gametes with an abnormal chromosome number (e.g. trisomy).",
    long="If homologous chromosomes (or sister chromatids) fail to separate properly during meiosis, some resulting gametes get an extra chromosome and others get one too few. Fertilization involving such a gamete can lead to conditions like trisomy (e.g. Down syndrome, trisomy 21).",
    trick="Don't assume errors always mean 'no DNA at all' — nondisjunction typically produces gametes with ONE EXTRA or one FEWER chromosome, not a complete absence of genetic material.",
    options=dict(a="Nondisjunction specifically produces an ABNORMAL (not normal/balanced) chromosome number.",
                 b="Gametes still contain genetic material overall — just an incorrect (extra or missing) chromosome count, not none at all.",
                 c="The DNA content isn't always exactly half in nondisjunction cases — that's precisely the abnormality being described.",
                 d="Correct — nondisjunction can produce gametes with an abnormal chromosome number, potentially leading to trisomy.")
),
8329: dict(
    short="Telomeres protect chromosome ends from degradation and prevent fusion with other chromosomes.",
    long="Telomeres are repetitive DNA sequences capping the ends of linear chromosomes, protecting them from degradation, preventing chromosome ends from being mistaken for DNA damage, and preventing chromosomes from fusing end-to-end with each other.",
    trick="Don't confuse telomeres (protective end caps) with centromeres (the attachment point for spindle fibers during division) — these are distinct chromosomal structures with different roles.",
    options=dict(a="Correct — telomeres protect chromosome ends from degradation and prevent fusion.",
                 b="Telomeres consist of repetitive, generally non-coding sequences, not protein-coding genes.",
                 c="The centromere (not the telomere) serves as the spindle attachment site.",
                 d="Telomeres don't actively promote division; they protect chromosome integrity, and their shortening is actually linked to cellular aging/senescence.")
),
8330: dict(
    short="Rr x Rr monohybrid cross gives a classic 3:1 phenotype ratio (3 round : 1 wrinkled).",
    long="Crossing two heterozygotes (Rr x Rr) for a simple dominant/recessive trait produces genotypes in a 1 RR : 2 Rr : 1 rr ratio. Since RR and Rr both show the dominant (round) phenotype, the phenotype ratio is 3 round : 1 wrinkled.",
    trick="Don't confuse the GENOTYPE ratio (1:2:1) with the simpler PHENOTYPE ratio (3:1) that results when one allele is fully dominant — questions often ask specifically about phenotype.",
    options=dict(a="All round would only occur if at least one parent were homozygous dominant (RR), not heterozygous (Rr).",
                 b="Correct — Rr x Rr gives the classic 3 round : 1 wrinkled phenotype ratio.",
                 c="1:1 would result from a testcross (Rr x rr), not an Rr x Rr cross.",
                 d="All wrinkled would only occur if both parents were homozygous recessive (rr).")
),
8331: dict(
    short="AA x aa cross produces all heterozygous (Aa) offspring.",
    long="Crossing a homozygous dominant parent (AA) with a homozygous recessive parent (aa): every offspring receives one A allele from one parent and one a allele from the other, giving 100% Aa (heterozygous) offspring, all showing the dominant phenotype.",
    trick="Don't assume a 1:1 or other split ratio — a homozygous x homozygous cross (AA x aa) is special in that it produces uniformly heterozygous offspring, with no genetic variation among them.",
    options=dict(a="All homozygous dominant (AA) would require BOTH parents to contribute an A allele, but the aa parent can only contribute 'a'.",
                 b="A 1:1 dominant:recessive split would occur in a testcross like Aa x aa, not AA x aa.",
                 c="Correct — AA x aa produces all heterozygous (Aa) offspring.",
                 d="All homozygous recessive (aa) would require both parents to contribute 'a', but the AA parent can only contribute 'A'.")
),
8332: dict(
    short="Hemophilia (X-linked recessive): carrier mother x unaffected father, sons have 50% chance of being affected.",
    long="The mother is a carrier (Xh X). She passes either the Xh (affected) or X (normal) allele to a son with 50% probability each. Since the father contributes Y to sons regardless, sons get either XhY (affected, 50%) or XY (unaffected, 50%).",
    trick="For X-linked recessive traits, sons only need ONE copy of the recessive allele (since they only have one X) to be affected — this is why the carrier mother's genotype alone determines the 50% son-affected probability here.",
    options=dict(a="0% would be wrong since the mother, as a carrier, can pass the affected X allele.",
                 b="25% would apply to a different scenario (e.g., calculating affected DAUGHTERS from two carrier-type parents), not this direct case.",
                 c="100% would only apply if the mother were affected (XhXh) herself, not just a carrier.",
                 d="Correct — a carrier mother gives a 50% chance of an affected son.")
),
8333: dict(
    short="Dihybrid cross AaBb x AaBb: 9/16 show the dominant phenotype for BOTH traits.",
    long="A dihybrid cross of two double heterozygotes produces the classic 9:3:3:1 phenotype ratio. The 9/16 portion represents offspring showing the dominant phenotype for both traits (A_B_).",
    trick="Remember the full 9:3:3:1 breakdown: 9 (both dominant), 3 (dominant A, recessive b), 3 (recessive a, dominant B), 1 (both recessive) — 'both dominant' is always the largest (9/16) group.",
    options=dict(a="Correct — 9/16 is the fraction showing dominant phenotype for both traits in a dihybrid cross.",
                 b="3/16 represents one of the single-trait-dominant categories (e.g. dominant A, recessive b), not both dominant.",
                 c="1/16 represents the double-recessive category, the opposite of what's being asked.",
                 d="1/4 doesn't match the correct dihybrid ratio fraction (9/16).")
),
8334: dict(
    short="IAi x IBi parents can produce A, B, AB, and O offspring — all four blood types possible.",
    long="Parent gametes: IAi contributes IA or i; IBi contributes IB or i. Combinations: IAIB (AB), IAi (A), IBi (B), ii (O) — all four blood types are possible outcomes.",
    trick="Don't assume heterozygous A and B parents can only produce A/B/AB types — the hidden recessive 'i' alleles from BOTH parents can combine to make an O-type (ii) child too.",
    options=dict(a="Only A and B misses that AB and O are also genuinely possible combinations here.",
                 b="Correct — all four blood types (A, B, AB, O) are possible from this cross.",
                 c="Only AB ignores that A, B, and O types are also possible from the available allele combinations.",
                 d="Only O ignores that A, B, and AB types are also possible.")
),
8335: dict(
    short="A trait appearing only with two recessive alleles, more common among unaffected carriers' children, is autosomal recessive.",
    long="Autosomal recessive inheritance requires two copies of the recessive allele (homozygous recessive) for the trait to be expressed. Unaffected heterozygous carrier parents can each pass on the recessive allele, producing affected (homozygous recessive) children despite neither parent showing the trait.",
    trick="Don't confuse this pattern with dominant inheritance (where just one copy is enough to show the trait, so it typically appears every generation) — recessive traits can 'skip' generations exactly as described here.",
    options=dict(a="Autosomal dominant traits need only ONE copy to show and typically don't 'hide' in unaffected carrier parents this way.",
                 b="Y-linked inheritance would be transmitted father-to-son only, and wouldn't fit the two-recessive-allele/carrier-parent description.",
                 c="Correct — this describes classic autosomal recessive inheritance.",
                 d="Incomplete dominance produces a blended intermediate phenotype in heterozygotes, not a hidden trait needing two recessive alleles.")
),
8336: dict(
    short="RR x WW giving all pink (RW) intermediate offspring is incomplete dominance.",
    long="Incomplete dominance occurs when the heterozygous phenotype is an intermediate BLEND of the two homozygous parental phenotypes — as with red x white four o'clocks producing pink offspring, rather than one color completely masking the other.",
    trick="Don't confuse incomplete dominance (blended intermediate phenotype) with codominance (BOTH parental phenotypes show up distinctly and separately, like in AB blood type or roan cattle coat color) — pink flowers are a blend, not a mix of distinct red and white patches.",
    options=dict(a="Codominance would show BOTH red and white distinctly (like spots or patches), not a blended pink.",
                 b="Complete dominance would produce all-red or all-white offspring, not an intermediate blend.",
                 c="Epistasis involves one gene masking/affecting the expression of another gene, unrelated to this single-gene blending scenario.",
                 d="Correct — the blended pink intermediate phenotype is a classic example of incomplete dominance.")
),
8337: dict(
    short="An organism's complete set of alleles for all genes is its genotype.",
    long="Genotype refers to the specific genetic makeup (all the allele combinations) an organism carries, as distinct from phenotype (the observable physical/biochemical traits resulting from that genotype interacting with the environment).",
    trick="Don't confuse genotype (the genetic 'blueprint', i.e. alleles) with phenotype (the observable outcome) — the question specifically asks about the underlying set of alleles.",
    options=dict(a="Correct — genotype is the complete set of alleles an organism carries.",
                 b="Phenotype refers to the observable traits resulting from the genotype, not the alleles themselves.",
                 c="Karyotype refers to the number/appearance of chromosomes, not the full allele set.",
                 d="Proteome refers to the full set of proteins expressed, a downstream product of gene expression, not the allele set itself.")
),
8338: dict(
    short="In RNA, adenine pairs with uracil (not thymine, which is DNA-specific).",
    long="RNA uses uracil in place of DNA's thymine. Base pairing rules in RNA: adenine pairs with uracil (A-U), and cytosine pairs with guanine (C-G).",
    trick="Thymine is exclusive to DNA — RNA replaces it with uracil, so 'adenine pairs with thymine' would only be correct in a DNA context, not RNA.",
    options=dict(a="Thymine doesn't exist in RNA (it's DNA-specific) — RNA uses uracil instead.",
                 b="Correct — in RNA, adenine pairs with uracil.",
                 c="Cytosine pairs with guanine, not adenine.",
                 d="Guanine pairs with cytosine, not adenine.")
),
8339: dict(
    short="DNA's sugar is deoxyribose (RNA's is ribose).",
    long="DNA (deoxyribonucleic acid) contains the sugar deoxyribose, which lacks an oxygen atom on the 2' carbon compared to ribose, the sugar found in RNA.",
    trick="Remember the naming clue: 'deoxyribonucleic acid' literally contains 'deoxyribose' — a helpful way to recall which sugar belongs to DNA vs. RNA (ribose).",
    options=dict(a="Ribose is the sugar found in RNA, not DNA.",
                 b="Glucose is a simple sugar used in metabolism/energy, not part of DNA's backbone.",
                 c="Correct — deoxyribose is the sugar found in DNA.",
                 d="Fructose is a simple sugar found in fruit, unrelated to DNA's structural sugar.")
),
8340: dict(
    short="tRNA delivers amino acids by recognizing an mRNA codon via a complementary anticodon.",
    long="Each tRNA molecule carries a specific amino acid and has an anticodon sequence that base-pairs (complementary) with a specific mRNA codon at the ribosome, ensuring the correct amino acid is added to the growing polypeptide chain in the right order.",
    trick="Don't say tRNA reads DNA directly — it interacts with mRNA (the intermediate messenger already transcribed from DNA) during translation, specifically via codon-anticodon pairing.",
    options=dict(a="tRNA interacts with mRNA (via codon-anticodon pairing), not the DNA template strand directly.",
                 b="Delivery is NOT random — it's precisely directed by codon-anticodon complementary base pairing.",
                 c="tRNA recognizes ALL codons corresponding to its specific anticodon, not exclusively the start codon.",
                 d="Correct — tRNA recognizes a specific mRNA codon via a complementary anticodon.")
),
8341: dict(
    short="A mutation that changes a codon but still codes for the same amino acid is a silent mutation.",
    long="Due to the redundancy (degeneracy) of the genetic code — multiple codons can specify the same amino acid — some point mutations change the codon sequence without changing the resulting amino acid, having no effect on the protein. This is called a silent mutation.",
    trick="Don't confuse silent mutations (no amino acid change) with missense mutations (DIFFERENT amino acid, potentially changing protein function) or nonsense mutations (premature stop codon).",
    options=dict(a="Correct — a silent mutation changes the codon but not the resulting amino acid, due to code redundancy.",
                 b="A nonsense mutation creates a premature STOP codon, a different (and often more harmful) outcome.",
                 c="A missense mutation changes the codon to specify a DIFFERENT amino acid, unlike a silent mutation.",
                 d="A frameshift mutation involves insertion/deletion disrupting the reading frame, a structurally different type of mutation.")
),
8342: dict(
    short="Alternative splicing lets one primary transcript produce multiple distinct protein products.",
    long="Alternative splicing allows different combinations of exons from the same pre-mRNA transcript to be joined together, producing multiple distinct mature mRNAs (and therefore different protein products) from a single gene.",
    trick="Don't confuse alternative splicing (varying which exons are included) with basic transcription or replication — it specifically explains how ONE gene can code for MULTIPLE different proteins.",
    options=dict(a="Reverse transcription converts RNA back into DNA (used by retroviruses), unrelated to producing multiple protein variants from one transcript.",
                 b="Correct — alternative splicing produces multiple distinct proteins from a single primary transcript.",
                 c="Semi-conservative replication describes how DNA is copied, unrelated to producing protein variety from a transcript.",
                 d="Transcription termination is simply the end of RNA synthesis, unrelated to generating multiple protein products.")
),
8343: dict(
    short="Inserting 2 nucleotides causes a frameshift, altering every downstream codon.",
    long="Since the genetic code is read in triplets (codons), inserting a number of nucleotides not divisible by 3 (like 2) shifts the reading frame for every codon downstream of the insertion point, typically producing a completely different (and usually nonfunctional) protein from that point onward.",
    trick="Insertions/deletions of exactly 3 nucleotides (or multiples of 3) preserve the reading frame (adding/removing whole codons) — but 1 or 2 nucleotides (as here) cause a disruptive frameshift.",
    options=dict(a="A 2-nucleotide insertion is NOT a 'no change' event — it disrupts the reading frame significantly.",
                 b="This is far more severe than a single silent mutation — it's a frameshift affecting many codons, not just one.",
                 c="Correct — inserting 2 nucleotides (not a multiple of 3) causes a frameshift, altering all downstream codons.",
                 d="There's no guarantee of increased protein stability — frameshift mutations typically produce a garbled, often nonfunctional protein.")
),
8344: dict(
    short="Primase synthesizes a short RNA primer for DNA polymerase to extend from.",
    long="DNA polymerase cannot start synthesizing a new strand from scratch — it needs a free 3'-OH end to extend. Primase solves this by synthesizing a short RNA primer, giving DNA polymerase a starting point to begin adding DNA nucleotides.",
    trick="Don't confuse primase (makes the RNA primer) with helicase (unwinds the double helix) or DNA polymerase's own proofreading function — each replication enzyme has a distinct, specific job.",
    options=dict(a="Unwinding the double helix is helicase's job, not primase's.",
                 b="Proofreading and removing incorrect nucleotides is largely DNA polymerase's own function (and other repair enzymes), not primase's.",
                 c="Joining Okazaki fragments is DNA ligase's job, not primase's.",
                 d="Correct — primase synthesizes a short RNA primer for DNA polymerase to extend from.")
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
    out_path = root / "scripts" / "mock20_explanations_biology_1.json"
    out_path.write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Wrote {len(out)} explanations to {out_path}")

if __name__ == "__main__":
    main()
