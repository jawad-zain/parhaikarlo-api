import json
from pathlib import Path

EXPL = {
8125: dict(
    short="Glucose is the monosaccharide; the others are di-/polysaccharides.",
    long="A monosaccharide is the simplest carbohydrate unit that cannot be hydrolyzed further (e.g. glucose, fructose). Sucrose is a disaccharide (glucose+fructose), while starch and cellulose are polysaccharides built from many glucose units.",
    trick="Don't be misled just because starch and cellulose are 'made of glucose' — being a polymer of a monosaccharide is not the same as being one.",
    options=dict(a="Sucrose is a disaccharide (glucose + fructose), not a monosaccharide.",
                 b="Correct — glucose is a single simple sugar unit, a monosaccharide.",
                 c="Starch is a polysaccharide (many glucose units joined together).",
                 d="Cellulose is a structural polysaccharide of glucose units.")
),
8126: dict(
    short="Nucleic acids are polymers of nucleotides.",
    long="DNA and RNA are built from repeating monomer units called nucleotides, each consisting of a sugar, a phosphate group, and a nitrogenous base.",
    trick="Amino acids build proteins, not nucleic acids — don't mix up the two monomer/polymer pairs.",
    options=dict(a="Correct — nucleotides are the repeating units of DNA/RNA.",
                 b="Amino acids are the monomers of proteins, not nucleic acids.",
                 c="Fatty acids are components of lipids.",
                 d="Monosaccharides are the units of carbohydrates.")
),
8127: dict(
    short="Tertiary structure is stabilized by R-group (side chain) interactions.",
    long="A protein's tertiary structure — its overall 3D folded shape — arises from interactions between amino acid side chains (R groups): hydrogen bonds, ionic bonds, disulfide bridges, and hydrophobic interactions.",
    trick="Don't confuse this with primary structure (backbone sequence) or secondary structure (backbone H-bonding into helices/sheets) — tertiary structure is specifically about side-chain interactions.",
    options=dict(a="Nucleotide bases pair in nucleic acids, not protein folding.",
                 b="Adjacent DNA strands relates to nucleic acid structure, not protein tertiary structure.",
                 c="The backbone alone determines primary/secondary structure, not full tertiary folding.",
                 d="Correct — R-group interactions (H-bonds, ionic bonds, hydrophobic effects) stabilize tertiary structure.")
),
8128: dict(
    short="Phospholipids form a bilayer with hydrophilic heads out, hydrophobic tails in.",
    long="Phospholipids are amphipathic — they have a polar (hydrophilic) phosphate head and nonpolar (hydrophobic) fatty acid tails. In water, they spontaneously arrange into a bilayer with heads facing the aqueous environment on both sides and tails buried inside, forming the basis of all cell membranes.",
    trick="They are NOT entirely hydrophobic or freely water-soluble — their amphipathic nature is exactly what drives bilayer self-assembly.",
    options=dict(a="They do not dissolve freely in water; their tails are hydrophobic.",
                 b="They do contain fatty acid (hydrophobic tail) chains.",
                 c="Correct — the amphipathic bilayer arrangement is the basis of membrane structure.",
                 d="They are amphipathic (part hydrophilic, part hydrophobic), not entirely hydrophobic.")
),
8129: dict(
    short="Substrate specificity comes from the 3D shape-complementarity of the active site.",
    long="Enzymes are highly specific because their active site has a precise three-dimensional shape (and chemical environment) complementary to a particular substrate, much like a lock and key (or induced fit).",
    trick="Random collision alone can't explain specificity — many molecules could 'collide' with an enzyme, but only the shape-complementary one binds productively.",
    options=dict(a="Correct — active-site shape complementary to the substrate underlies specificity.",
                 b="Random collision happens with many molecules, but only the matching one binds/reacts.",
                 c="Size alone doesn't guarantee correct chemical fit.",
                 d="Temperature affects rate, not which substrate the enzyme recognizes.")
),
8130: dict(
    short="The substance an enzyme acts on is called the substrate.",
    long="In enzyme kinetics, the substrate is the reactant molecule that binds to the enzyme's active site and is converted into product.",
    trick="Don't confuse substrate (reactant) with product (result) or cofactor/coenzyme (helper molecules).",
    options=dict(a="Correct — the substrate is what the enzyme acts upon.",
                 b="A coenzyme is a helper molecule, not what's acted upon.",
                 c="The product is the result of the reaction, not the starting substance.",
                 d="A cofactor is a non-protein helper (often a metal ion), not the substrate.")
),
8131: dict(
    short="Rate increases with substrate concentration until all active sites are saturated.",
    long="As substrate concentration rises, more enzyme-substrate complexes form, increasing rate — but once every active site is occupied (saturation), rate plateaus regardless of further substrate increase (this is the basis of Michaelis-Menten kinetics and Vmax).",
    trick="A common wrong assumption is that rate increases indefinitely — it always levels off once active sites are saturated.",
    options=dict(a="Correct — saturation of active sites caps the maximum reaction rate (Vmax).",
                 b="The enzyme isn't destroyed by more substrate.",
                 c="The reaction doesn't reverse just from more substrate.",
                 d="Temperature isn't what's changing here; only substrate concentration is varied.")
),
8132: dict(
    short="A non-protein metal-ion helper is called a cofactor.",
    long="Cofactors are non-protein components (often metal ions like Zn²⁺, Fe²⁺, Mg²⁺) required by some enzymes for proper catalytic function. Coenzymes are organic (often vitamin-derived) cofactors, but a specifically metal-ion helper is best termed a cofactor.",
    trick="Coenzymes are a subset of cofactors that are organic molecules — a metal ion is a cofactor, not a coenzyme in the strict sense used here.",
    options=dict(a="A zymogen is an inactive enzyme precursor, unrelated to metal-ion helpers.",
                 b="'Prosthetic sugar' is not a standard term for a metal-ion helper.",
                 c="Coenzymes are typically organic molecules, not metal ions.",
                 d="Correct — a non-protein metal ion required for function is a cofactor.")
),
8133: dict(
    short="Allosteric regulators bind a site other than the active site.",
    long="Allosteric regulation involves a regulatory molecule binding at an allosteric site (distinct from the active site), causing a conformational change that alters the enzyme's activity (either enhancing or inhibiting catalysis).",
    trick="Don't confuse this with competitive inhibition, where the inhibitor DOES bind the active site directly.",
    options=dict(a="Correct — binding elsewhere causes a shape change that affects the active site's function.",
                 b="Binding the active site directly describes competitive inhibition, not allosteric regulation.",
                 c="Allosteric effects are typically reversible and functional, not simple irreversible denaturation.",
                 d="Allosteric regulators bind the enzyme, not the substrate itself.")
),
8134: dict(
    short="The lysosome breaks down worn-out components using digestive enzymes.",
    long="Lysosomes are membrane-bound organelles containing hydrolytic (digestive) enzymes that break down worn-out organelles, macromolecules, and engulfed foreign material (autophagy and phagocytosis).",
    trick="Peroxisomes also contain enzymes, but their role is oxidative reactions (breaking down fatty acids, detoxifying) — lysosomes are the digestive 'clean-up crew.'",
    options=dict(a="Peroxisomes handle oxidative reactions like fatty-acid breakdown and detoxification, not general digestion.",
                 b="Ribosomes synthesize proteins, they don't digest material.",
                 c="Centrioles function in cell division/microtubule organization.",
                 d="Correct — lysosomes contain digestive enzymes for breaking down cellular debris.")
),
8135: dict(
    short="Rough ER (with ribosomes) makes proteins for secretion.",
    long="The rough endoplasmic reticulum is studded with ribosomes on its cytoplasmic surface, which synthesize proteins destined for secretion, the membrane, or organelles — the ER then folds and processes them.",
    trick="Smooth ER (no ribosomes) handles lipid synthesis and detoxification — don't mix the two ER types up.",
    options=dict(a="Lipid synthesis is mainly a smooth ER function.",
                 b="Correct — ribosome-studded rough ER synthesizes and processes secretory/membrane proteins.",
                 c="ATP production occurs in mitochondria.",
                 d="Photosynthesis occurs in chloroplasts, not the ER.")
),
8136: dict(
    short="The granum (stacked thylakoids), structure Q, is where the light reactions occur.",
    long="The light-dependent reactions of photosynthesis take place across the thylakoid membranes, which are stacked into structures called grana. In the labeled diagram, Q is the granum. P is the outer membrane, S is the inner membrane, and R is the stroma (site of the Calvin cycle, the light-independent reactions).",
    trick="Don't confuse the stroma (light-independent/Calvin cycle site) with the granum/thylakoids (light-dependent reaction site) — they're adjacent but do different jobs.",
    options=dict(a="Structure S, the inner membrane, is just a boundary layer, not the site of light reactions.",
                 b="Structure P, the outer membrane, is the outer boundary, not where light reactions occur.",
                 c="Correct — Structure Q, the granum (stacked thylakoids), houses the light-dependent reactions.",
                 d="Structure R, the stroma, is where the light-INDEPENDENT reactions (Calvin cycle) occur.")
),
8137: dict(
    short="Actin filaments are central to muscle contraction and cell shape.",
    long="Actin microfilaments are a major cytoskeletal component; besides maintaining/changing cell shape and enabling cell movement, they interact with myosin to drive muscle contraction.",
    trick="The cytoskeleton isn't just structural scaffolding — actin's role in active contraction (with myosin) is a key MDCAT point.",
    options=dict(a="Actin filaments aren't involved in ATP synthesis.",
                 b="Correct — actin is central to both muscle contraction and shaping/supporting the cell.",
                 c="Photosynthesis has nothing to do with the cytoskeleton.",
                 d="DNA replication occurs in the nucleus, unrelated to actin filaments.")
),
8138: dict(
    short="Protein-secreting cells have extensive rough ER and Golgi apparatus.",
    long="Cells specialized for secreting large amounts of protein (like hormone-secreting endocrine cells) need extensive rough ER (synthesis/folding) and Golgi apparatus (modification, packaging, and secretion via vesicles).",
    trick="A 'no organelles' or 'peroxisome only' option is an easy giveaway wrong answer — heavy secretory activity always implies well-developed ER + Golgi.",
    options=dict(a="A cell actively secreting protein needs organelles, not an absence of them.",
                 b="Smooth ER is more associated with lipid synthesis/detox, not protein secretion pathways.",
                 c="Correct — rough ER (synthesis) and Golgi (packaging/secretion) are both needed for heavy protein secretion.",
                 d="Peroxisomes handle oxidative metabolism, not the secretory pathway.")
),
8139: dict(
    short="Diffusion moves particles from high to low concentration, down the gradient.",
    long="Diffusion is the passive net movement of particles from a region of higher concentration to one of lower concentration, driven by random thermal motion, until equilibrium is reached.",
    trick="Watch for options that reverse the direction (low-to-high) — that's active transport, not diffusion.",
    options=dict(a="Diffusion isn't restricted to living cells; it's a general physical process.",
                 b="This reverses the correct direction — that would require active transport, not diffusion.",
                 c="Correct — diffusion moves particles down their concentration gradient, high to low.",
                 d="Diffusion can occur directly through membranes too, not only via carrier proteins.")
),
8140: dict(
    short="Endocytosis is engulfing material into a membrane-derived vesicle.",
    long="Endocytosis is the process by which a cell takes in large particles, fluid, or molecules by having the plasma membrane invaginate and pinch off to form an internal vesicle.",
    trick="Exocytosis (the reverse — releasing material via vesicle fusion with the membrane) is a common distractor; make sure you have the direction right.",
    options=dict(a="Active ion pumping via ATP describes active transport of ions, not endocytosis.",
                 b="Free diffusion of gases doesn't require any membrane engulfing process.",
                 c="Releasing material via vesicle fusion describes exocytosis, the reverse process.",
                 d="Correct — endocytosis takes material INTO the cell via a membrane-derived vesicle.")
),
8141: dict(
    short="Animal cells in hypotonic solution swell and can burst (lyse), lacking a wall.",
    long="In a hypotonic solution (lower solute concentration outside than inside), water moves into the cell by osmosis. Without a rigid cell wall to resist expansion, an animal cell can swell and potentially lyse (burst).",
    trick="Plasmolysis and crenation happen in HYPERtonic solutions, and only plant cells with walls resist bursting in hypotonic solutions — animal cells have no such protection.",
    options=dict(a="The cell does change — water moves in via osmosis, so it isn't unchanged.",
                 b="Plasmolysis (shrinking of the plant cell membrane away from the wall) occurs in hypertonic, not hypotonic, solutions.",
                 c="Shrinking/crenation happens in a hypertonic solution, the opposite condition.",
                 d="Correct — without a wall, water influx in a hypotonic solution can cause the cell to swell and lyse.")
),
8142: dict(
    short="Facilitated diffusion uses channel/carrier proteins, still moving down the gradient.",
    long="Facilitated diffusion is passive (no ATP) but requires specific membrane transport proteins (channels or carriers) to move substances (like glucose or ions) down their concentration gradient, unlike simple diffusion through the lipid bilayer directly.",
    trick="Facilitated diffusion is still passive — it does NOT use ATP and does NOT move against the gradient (that would be active transport).",
    options=dict(a="Correct — it specifically requires channel/carrier proteins, unlike simple diffusion.",
                 b="It occurs in eukaryotic cells too, not exclusively prokaryotes.",
                 c="It does not require ATP — that would make it active transport.",
                 d="It moves substances DOWN their gradient, not against it.")
),
8143: dict(
    short="The fluid mosaic model: a flexible phospholipid bilayer with mobile embedded proteins.",
    long="The fluid mosaic model describes the membrane as a fluid (dynamic) phospholipid bilayer within which proteins are embedded and can move laterally, giving both fluidity and a 'mosaic' pattern of different components.",
    trick="The model emphasizes fluidity/movement — 'rigid' or 'unchanging' descriptions directly contradict the concept.",
    options=dict(a="Cholesterol is only one embedded component, not the entire model.",
                 b="The model specifically emphasizes fluidity/mobility, not rigidity.",
                 c="Correct — fluid bilayer plus mobile embedded proteins is exactly the fluid mosaic model.",
                 d="Cellulose walls belong to plant cell walls, not the fluid membrane model.")
),
8144: dict(
    short="DNA replication occurs during S phase of interphase.",
    long="The cell cycle's interphase is divided into G1 (growth), S (DNA synthesis/replication), and G2 (further growth/preparation) before mitosis. DNA is duplicated specifically during S phase.",
    trick="Mitosis is where the ALREADY-replicated DNA is separated, not where replication itself happens.",
    options=dict(a="Mitosis is chromosome segregation, occurring after DNA has already been replicated.",
                 b="G1 is a growth phase before DNA synthesis begins.",
                 c="Correct — S phase (Synthesis phase) is specifically when DNA replication occurs.",
                 d="G2 is a preparatory growth phase after replication, before mitosis.")
),
8145: dict(
    short="Chromosomes align at the equatorial plate during metaphase.",
    long="During mitosis, metaphase is defined by chromosomes lining up along the metaphase (equatorial) plate, attached to spindle fibers from opposite poles, prior to separation in anaphase.",
    trick="Anaphase is when chromosomes are pulled APART toward poles — a common mix-up with metaphase's alignment stage.",
    options=dict(a="Anaphase is when sister chromatids separate and move to opposite poles.",
                 b="Telophase is when nuclear envelopes reform and chromosomes decondense.",
                 c="Prophase is when chromosomes condense and the spindle begins forming.",
                 d="Correct — metaphase is defined by chromosome alignment at the equatorial plate.")
),
8146: dict(
    short="Crossing over occurs in prophase I of meiosis, between homologous chromosomes.",
    long="Crossing over — the exchange of genetic material between non-sister chromatids of homologous chromosomes — occurs during prophase I of meiosis, generating genetic variation via recombination.",
    trick="Crossing over is a MEIOSIS-specific event (not mitosis), and specifically happens in prophase I, not later phases.",
    options=dict(a="Interphase of mitosis has no crossing over — that's a meiotic process.",
                 b="Mitosis produces genetically identical cells; it doesn't include crossing over.",
                 c="Correct — homologous chromosomes exchange segments during prophase I of meiosis.",
                 d="Anaphase of mitosis just separates sister chromatids, no crossing over involved.")
),
8147: dict(
    short="After telophase of mitosis, each daughter cell has 46 chromosomes (same as parent).",
    long="Mitosis produces two genetically identical daughter cells, each with the same chromosome number as the parent cell (2n=46 in humans) — mitosis does not reduce chromosome number, unlike meiosis.",
    trick="Don't halve the number as you would for meiosis (which gives n=23) — mitosis conserves the full diploid number.",
    options=dict(a="23 would be the haploid number produced by meiosis, not mitosis.",
                 b="Correct — mitosis preserves the diploid chromosome number (46) in each daughter cell.",
                 c="92 would be double, as if DNA had been replicated but chromosomes not yet separated.",
                 d="12 has no basis in this scenario.")
),
8148: dict(
    short="Cancer arises from mutations in proto-oncogenes and tumor suppressor genes.",
    long="Cell cycle control genes fall into two broad classes: proto-oncogenes (which normally promote division, and become oncogenes when mutated to overactive forms) and tumor suppressor genes (which normally restrain division, and lose function when mutated). Mutations disrupting either class can cause uncontrolled cell division — cancer.",
    trick="A common distractor tries to link cancer to genes with no cell-cycle role — always tie cancer specifically to these two gene classes.",
    options=dict(a="Cancer specifically involves genes that DO regulate the cell cycle, not unrelated genes.",
                 b="Eye-color genes are unrelated to cell cycle regulation.",
                 c="Correct — mutated proto-oncogenes/tumor suppressor genes are the classic cause of cancer.",
                 d="Hemoglobin genes are unrelated to cell cycle control.")
),
8149: dict(
    short="Animal cell cytokinesis uses a contractile ring that pinches the cell in two.",
    long="In animal cells, cytokinesis (physical division of the cytoplasm) occurs via a contractile ring of actin and myosin filaments that constricts at the cell's equator, pinching it into two daughter cells (cleavage furrow).",
    trick="A cell PLATE is the plant-cell method of cytokinesis (since plants can't pinch through a rigid wall) — don't mix up plant vs animal cytokinesis mechanisms.",
    options=dict(a="A cell plate is how PLANT cells divide (building a new wall), not animal cells.",
                 b="Correct — the actin-myosin contractile ring pinches animal cells into two.",
                 c="A cellulose wall is a plant cell structure, irrelevant to animal cytokinesis.",
                 d="Spindle fibers segregate chromosomes but don't by themselves physically divide the cytoplasm.")
),
8150: dict(
    short="YY x yy cross gives all Yy offspring — all yellow (dominant phenotype).",
    long="Crossing a homozygous dominant (YY) with a homozygous recessive (yy) parent produces all heterozygous (Yy) offspring. Since yellow (Y) is dominant, all offspring display the yellow phenotype, even though genotypically they are all Yy.",
    trick="Don't confuse this monohybrid cross (YY x yy, all Yy, all dominant phenotype) with a heterozygous x heterozygous cross (Yy x Yy, which gives the classic 3:1 ratio).",
    options=dict(a="Correct — every offspring is Yy, and since yellow is dominant, all appear yellow.",
                 b="Green would only appear if offspring were homozygous recessive (yy), which none are here.",
                 c="A 1:1 ratio would arise from a testcross (Yy x yy), not YY x yy.",
                 d="3:1 is the classic ratio from a heterozygous x heterozygous cross (Yy x Yy), not this cross.")
),
8151: dict(
    short="A test cross reveals if a dominant-phenotype organism is homozygous or heterozygous.",
    long="A test cross crosses an organism showing the dominant phenotype (genotype unknown — could be homozygous dominant or heterozygous) with a homozygous recessive individual. If all offspring show the dominant trait, the unknown parent is homozygous dominant; if about half show the recessive trait, it's heterozygous.",
    trick="Test crosses are specifically used to resolve genotype ambiguity in DOMINANT-phenotype individuals — not for determining age or sex.",
    options=dict(a="A test cross has nothing to do with determining an organism's age.",
                 b="A test cross doesn't determine sex of offspring; that's unrelated to its purpose.",
                 c="If it were already known to be homozygous dominant, there'd be no ambiguity to test for.",
                 d="Correct — a test cross distinguishes homozygous dominant from heterozygous individuals.")
),
8152: dict(
    short="Aa x Aa cross gives 3/4 unaffected (dominant phenotype), 1/4 affected.",
    long="Two carriers (Aa x Aa) for a recessive disorder produce offspring in a 1 AA : 2 Aa : 1 aa genotypic ratio. Since AA and Aa are both phenotypically unaffected (normal, as the disorder is recessive), 3 out of 4 (75%) of offspring are unaffected, and only aa (25%) is affected.",
    trick="Remember affected requires TWO recessive alleles (aa) — since 3/4 of offspring carry at least one dominant allele, 75% (not 50%) are unaffected.",
    options=dict(a="25% is the probability of being AFFECTED (aa), not unaffected.",
                 b="50% isn't the standard Aa x Aa ratio for either phenotype category.",
                 c="Correct — 3/4 (AA + Aa) are phenotypically unaffected in an Aa x Aa cross.",
                 d="100% would mean no offspring are ever affected, which is false for a 25% aa outcome.")
),
8153: dict(
    short="AaBb x aabb testcross gives 1/4 offspring showing both dominant traits.",
    long="In a dihybrid testcross (AaBb x aabb), each gene segregates independently in a simple 1:1 ratio (Aa:aa and Bb:bb), so the combined probability of getting both dominant traits (AaBb-phenotype, i.e., A_B_) is 1/2 × 1/2 = 1/4.",
    trick="Don't apply the classic 9:16 ratio here — that's for a full dihybrid CROSS (AaBb x AaBb), not a TESTcross against a double-recessive.",
    options=dict(a="3/4 doesn't match the simple 1/2 × 1/2 testcross calculation for double-dominant phenotype.",
                 b="9/16 is the ratio for a full AaBb x AaBb dihybrid cross, not this testcross.",
                 c="Correct — 1/2 (A_) × 1/2 (B_) = 1/4 for the double-dominant phenotype in a testcross.",
                 d="1/16 would be the double-recessive fraction in a full dihybrid cross, not applicable here.")
),
8154: dict(
    short="Color-blind father x homozygous normal mother → 0% color-blind daughters.",
    long="For an X-linked recessive trait, daughters get one X from their color-blind father (X^cb) and one X from their homozygous normal mother (X^N X^N), so every daughter is X^N X^cb — a carrier, but phenotypically normal (not color-blind) since they have one normal dominant allele.",
    trick="Daughters of an affected father are always CARRIERS (not affected) if the mother is homozygous normal — a very common MDCAT X-linked inheritance trap.",
    options=dict(a="50% would apply if we were asking about SONS getting the trait from their mother (not the case for daughters here).",
                 b="100% would be wrong since every daughter gets a normal X from the homozygous normal mother.",
                 c="Correct — daughters are all carriers (X^N X^cb), 0% show the color-blind phenotype.",
                 d="25% doesn't match this simple X-linked cross outcome.")
),
8155: dict(
    short="Appearing every generation in ~half of offspring fits autosomal dominant inheritance.",
    long="A trait showing up in every generation (no skipping) in roughly 50% of offspring of an affected x unaffected cross is the classic signature of autosomal dominant inheritance (e.g., Aa x aa gives ~1:1 affected:unaffected).",
    trick="Recessive traits typically SKIP generations (appearing only when both parents are carriers) — the 'every generation, ~50%' pattern is diagnostic of dominant inheritance.",
    options=dict(a="Codominance describes both alleles being expressed together, not this every-generation-half pattern.",
                 b="Autosomal recessive traits typically skip generations, unlike what's described here.",
                 c="Correct — appearing every generation in about half the offspring fits autosomal dominant inheritance.",
                 d="Y-linked inheritance would only affect males (father-to-son), not roughly half of a mixed-sex offspring group generally.")
),
8156: dict(
    short="Roan coat color (both colors visible together) is an example of codominance.",
    long="Codominance occurs when both alleles are fully and separately expressed in the heterozygote, rather than blending. A roan coat (both red and white hairs distinctly present, side by side) is the classic codominance example, unlike incomplete dominance which would blend into a uniform intermediate color (like pink).",
    trick="Don't confuse codominance (both traits visibly separate, like red AND white hairs) with incomplete dominance (a blended intermediate, like uniform pink) — the key clue is 'mix of red and white hairs' (distinct, not blended).",
    options=dict(a="Correct — both alleles are separately and fully expressed (distinct red and white hairs), which is codominance.",
                 b="Epistasis involves one gene masking another's expression, unrelated to this simple coat-color scenario.",
                 c="Complete dominance would mean only one color (say, all red) appears, not a mix.",
                 d="Incomplete dominance would blend into a uniform intermediate color (like solid pink), not a mix of distinct red/white hairs.")
),
8157: dict(
    short="An organism's complete set of genetic instructions is its genome.",
    long="The genome is the entirety of an organism's genetic material (all genes and non-coding DNA), distinct from phenotype (observable traits), karyotype (chromosome number/appearance), or allele (a specific gene variant).",
    trick="Don't confuse genome (the whole genetic content) with genotype (the specific allele combination at particular loci) — genome is broader.",
    options=dict(a="A karyotype is the chromosome complement's visual arrangement, not the full genetic instruction set.",
                 b="Phenotype is the observable expression of traits, not the underlying genetic code itself.",
                 c="Correct — genome refers to the organism's complete genetic instructions.",
                 d="An allele is just one variant form of a single gene, a tiny fraction of the genome.")
),
8158: dict(
    short="Guanine always pairs with cytosine (G-C) in DNA.",
    long="DNA base pairing follows strict complementary rules: adenine (A) pairs with thymine (T), and guanine (G) pairs with cytosine (C), held together by hydrogen bonds (2 for A-T, 3 for G-C).",
    trick="Uracil replaces thymine in RNA, not DNA — since this question specifies DNA, uracil is not a valid pairing partner here.",
    options=dict(a="Thymine pairs with adenine, not guanine.",
                 b="Correct — guanine pairs with cytosine via three hydrogen bonds.",
                 c="Uracil is found in RNA, not DNA, so it's not a DNA base-pairing partner.",
                 d="Adenine pairs with thymine, not guanine.")
),
8159: dict(
    short="The antiparallel template strand is used to synthesize mRNA.",
    long="During transcription, RNA polymerase reads one strand of the DNA double helix (the template/antisense strand, running 3'->5') and synthesizes a complementary mRNA strand running 5'->3', antiparallel to the template.",
    trick="It's not truly 'random' which strand is used — for a given gene, one specific strand (the template strand) is consistently transcribed, based on promoter orientation.",
    options=dict(a="Correct — the specific antiparallel template strand directs synthesis of the complementary mRNA.",
                 b="The sense (coding) strand has the same sequence as the mRNA (except T/U) — it is NOT the one directly read/templated.",
                 c="It's not random; a specific template strand is used for each gene.",
                 d="The newly synthesized strand is the mRNA product itself, not the template used to make it.")
),
8160: dict(
    short="Transcription copies a DNA sequence into complementary mRNA.",
    long="Transcription is the process where RNA polymerase synthesizes a complementary mRNA strand using one strand of DNA as a template, essentially copying the genetic information from DNA into a mobile RNA form.",
    trick="Don't confuse transcription (DNA -> mRNA) with translation (mRNA -> protein) or replication (DNA -> DNA) — three related but distinct processes.",
    options=dict(a="Making two identical DNA molecules describes replication, not transcription.",
                 b="mRNA degradation is a separate regulatory process, not transcription itself.",
                 c="Joining amino acids into a polypeptide describes translation, not transcription.",
                 d="Correct — transcription copies DNA sequence into complementary mRNA.")
),
8161: dict(
    short="A mutation creating a premature stop codon is a nonsense mutation.",
    long="A nonsense mutation changes a codon that specified an amino acid into one of the three stop codons (UAA, UAG, UGA), causing translation to terminate early and producing a truncated (usually non-functional) protein.",
    trick="A missense mutation changes one amino acid for another (protein usually still full-length) — nonsense specifically means an early STOP, truncating the protein.",
    options=dict(a="A missense mutation changes to a different amino acid, not a stop signal.",
                 b="Correct — a nonsense mutation converts a codon into a premature stop, truncating the protein.",
                 c="A frameshift mutation results from insertion/deletion (not a multiple of 3), shifting the whole reading frame.",
                 d="A silent mutation doesn't change the amino acid at all (due to codon redundancy).")
),
8162: dict(
    short="RNA splicing removes introns and joins exons in the primary transcript.",
    long="After transcription, the primary (pre-mRNA) transcript undergoes RNA splicing: non-coding introns are removed and the coding exons are joined together to form the mature mRNA that will be translated.",
    trick="Splicing happens AFTER transcription (on the pre-mRNA), so don't confuse it with transcription initiation itself.",
    options=dict(a="Correct — splicing removes introns and joins exons to produce mature mRNA.",
                 b="Replication duplicates DNA, unrelated to intron/exon processing.",
                 c="Transcription initiation is the start of RNA synthesis, a separate earlier step.",
                 d="Translation is protein synthesis from mRNA, a later and separate process.")
),
8163: dict(
    short="Deleting 3 nucleotides removes/adds one amino acid without a frameshift.",
    long="Since the genetic code is read in triplets (codons), deleting exactly 3 consecutive nucleotides removes exactly one codon (one amino acid) while keeping the reading frame intact for all remaining codons — unlike deletions/insertions not in multiples of 3, which cause a frameshift.",
    trick="The key insight is that 3 is a multiple of the codon length — any deletion/insertion NOT a multiple of 3 causes a frameshift, but exact multiples of 3 preserve the frame.",
    options=dict(a="Removing 3 nucleotides does remove a codon, so it's not 'no change at all.'",
                 b="This isn't necessarily about the start codon specifically; it just removes whichever codon those 3 nucleotides span.",
                 c="A 3-nucleotide deletion does NOT cause a frameshift, since 3 is an exact multiple of the codon length.",
                 d="Correct — losing exactly one codon (3 nucleotides) removes one amino acid without shifting the frame.")
),
8164: dict(
    short="Helicase unwinds the DNA double helix ahead of the replication fork.",
    long="During DNA replication, the enzyme helicase breaks the hydrogen bonds between base pairs, unwinding and separating the two DNA strands ahead of the replication fork so that other enzymes (primase, DNA polymerase) can act on the single strands.",
    trick="Ligase seals nicks in the sugar-phosphate backbone (joining Okazaki fragments), and DNA polymerase synthesizes new strands — neither of those unwinds the helix; that's helicase's specific job.",
    options=dict(a="Correct — helicase unwinds the double helix at the replication fork.",
                 b="Ligase joins DNA fragments (like Okazaki fragments), it doesn't unwind the helix.",
                 c="Primase synthesizes short RNA primers, it doesn't unwind DNA.",
                 d="DNA polymerase synthesizes new DNA strands, it doesn't unwind the helix itself.")
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
    out_path = root / "scripts" / "mock19_explanations_biology_1.json"
    out_path.write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Wrote {len(out)} explanations to {out_path}")

if __name__ == "__main__":
    main()
