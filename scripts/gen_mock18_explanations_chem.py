import json
from pathlib import Path

OUT = Path(__file__).parent / "mock18_explanations_chemistry.json"

def I(po): return po + 7944

E = []

def add(po, short, long, trick, a, b, c, d):
    E.append({
        "id": I(po), "short": short, "long": long, "trick": trick,
        "options": {"a": a, "b": b, "c": c, "d": d}
    })

add(82, "Electrons occupy the electron cloud (orbitals) surrounding the nucleus, not the nucleus itself.",
    "The modern quantum-mechanical model describes electrons as existing in probability regions (orbitals) around the nucleus, rather than fixed orbits; the nucleus itself contains only protons and neutrons.",
    "Nucleus = protons + neutrons; electron cloud = electrons — never place electrons 'in' the nucleus.",
    "Incorrect — the nucleus contains protons and neutrons, not electrons.",
    "Correct — electrons occupy the surrounding electron cloud/orbitals, not the nucleus.",
    "Incorrect — electrons are present throughout the atom's occupied orbitals, not absent.",
    "Incorrect — electrons occupy multiple shells/orbitals as needed, not only the innermost one.")

add(83, "Chlorine-35 (Z=17) has 35 - 17 = 18 neutrons.",
    "Mass number (35) = protons + neutrons. Atomic number (17) = number of protons. So neutrons = mass number - atomic number = 35 - 17 = 18.",
    "Neutrons = Mass number - Atomic number — a simple subtraction many students rush and get wrong.",
    "Incorrect — 17 is the atomic number (proton count), not the neutron count.",
    "Incorrect — 35 is the mass number (protons + neutrons combined), not just the neutron count.",
    "Correct — 35 - 17 = 18 neutrons.",
    "Incorrect — 52 would result from adding (not subtracting) 35 and 17, which isn't the correct calculation.")

add(84, "Phosphorus (Z=15) has electron configuration 1s2 2s2 2p6 3s2 3p3.",
    "Filling orbitals in order of increasing energy for 15 electrons: 1s2 (2) + 2s2 (2) + 2p6 (6) + 3s2 (2) + 3p3 (3) = 2+2+6+2+3 = 15 total electrons, matching phosphorus's atomic number.",
    "Always add up the superscripts to check they total the atomic number — a fast way to catch a wrong configuration.",
    "Incorrect — this totals 2+2+6+1+4=15 electrons but violates filling order (3s should fill completely before 3p starts).",
    "Incorrect — this totals only 2+2+6+2+2=14 electrons, one short of phosphorus's 15.",
    "Incorrect — this configuration has an incomplete 2p subshell (2p5) alongside a partially filled 3p4, which is not phosphorus's ground-state configuration.",
    "Correct — 1s2 2s2 2p6 3s2 3p3 correctly totals 15 electrons in the proper filling order.")

add(85, "An ion with 20 protons and 18 electrons has a net charge of +2 (2 more protons than electrons).",
    "Charge = protons - electrons (in units of elementary charge). With 20 protons and 18 electrons, charge = 20 - 18 = +2 — this matches Ca2+, calcium having lost 2 electrons.",
    "More protons than electrons means a net POSITIVE charge (a cation); more electrons than protons means NEGATIVE (an anion) — don't flip the sign.",
    "Correct — 20 protons minus 18 electrons gives a net charge of +2.",
    "Incorrect — this would require more electrons than protons, the opposite of the given numbers.",
    "Incorrect — +20 would be the charge only if there were zero electrons at all, not 18.",
    "Incorrect — -18 both has the wrong sign and ignores the proton count entirely.")

add(86, "Isotopes of an element have the same number of protons but differ in neutron number.",
    "By definition, isotopes are atoms of the same element (same protons, hence same atomic number) with different numbers of neutrons, giving them different mass numbers while retaining the same chemical properties.",
    "Same protons = same element (always); different neutrons = different isotope — atomic number never changes between isotopes of one element.",
    "Incorrect — isotopes of the same element always share the same proton number by definition.",
    "Correct — isotopes differ specifically in their number of neutrons.",
    "Incorrect — a neutral atom's electron count matches its proton count, which is the same across isotopes.",
    "Incorrect — atomic number equals proton count, which is identical for all isotopes of one element.")

add(87, "The vertical columns of the periodic table are called groups.",
    "Groups (or families) are the 18 vertical columns; elements in the same group share the same number of valence electrons and therefore similar chemical properties. Horizontal rows are called periods.",
    "Groups = vertical (up-down, similar chemistry); Periods = horizontal (left-right, same number of shells) — a foundational periodic-table vocabulary distinction.",
    "Incorrect — periods are the horizontal rows, not the vertical columns.",
    "Incorrect — 'blocks' (s, p, d, f) refer to which subshell is being filled, a different grouping concept from columns.",
    "Correct — vertical columns are called groups.",
    "Incorrect — 'series' is not the standard term for the periodic table's vertical columns (it's sometimes used loosely for the lanthanide/actinide rows instead).")

add(88, "Atomic radius increases going down a group as additional electron shells are added.",
    "Each successive period adds a new principal energy level (shell) further from the nucleus, so atomic radius increases down a group despite the also-increasing nuclear charge, because the added shells dominate the size trend.",
    "Down a group: radius INCREASES (more shells). Across a period (left to right): radius DECREASES (increasing nuclear pull on the same shell) — two opposite periodic trends to keep straight.",
    "Incorrect — radius increases, not decreases, going down a group.",
    "Incorrect — atomic radius is a physical size, always a positive value; it can never become negative.",
    "Incorrect — radius changes substantially down a group; it does not stay constant.",
    "Correct — additional electron shells added at each period down a group make atomic radius increase.")

add(89, "High electron affinity (strong tendency to gain an electron) is typical of Group 17 (halogens), near the periodic table's right side.",
    "Halogens (Group 17) are one electron short of a stable noble-gas configuration, giving them a very strong pull for gaining one additional electron to complete their outer shell, making them highly reactive nonmetals with high electron affinities.",
    "High electron affinity clusters toward the top-right of the periodic table (excluding noble gases, which are already stable and don't 'want' electrons) — halogens are the textbook example.",
    "Correct — Group 17 (halogens) elements have the strongest tendency among common elements to gain a single electron.",
    "Incorrect — Group 1 (alkali metals) elements tend to LOSE an electron, not gain one; they have low electron affinity in this sense.",
    "Incorrect — noble gases already have a complete valence shell and have essentially no tendency to gain electrons.",
    "Incorrect — transition metals don't typically show the strongest single-electron-gaining tendency compared to halogens.")

add(90, "A covalent bond forms through the sharing of electron pairs between atoms.",
    "In covalent bonding, two (typically nonmetal) atoms each contribute electrons to a shared pair, held between both nuclei by mutual electrostatic attraction — distinct from ionic bonding (electron transfer) or metallic bonding (a 'sea' of delocalized electrons).",
    "Covalent = SHARING electrons; Ionic = TRANSFERRING electrons (forming charged ions) — the single most basic bonding-type distinction.",
    "Incorrect — an ionic bond involves the transfer (not sharing) of electrons between atoms, forming oppositely charged ions.",
    "Correct — sharing electron pairs between atoms is precisely the definition of a covalent bond.",
    "Incorrect — metallic bonding involves a delocalized 'sea' of electrons shared among many metal cations, a different arrangement from discrete shared pairs.",
    "Incorrect — van der Waals forces are weak intermolecular attractions, not a true chemical bond formed by shared electron pairs.")

add(91, "NH3's 3 bonding pairs + 1 lone pair on the central N atom give it a trigonal pyramidal molecular geometry.",
    "VSEPR predicts electron-pair geometry from all 4 electron domains (tetrahedral arrangement), but the observed MOLECULAR shape only counts atom positions — with one domain being a lone pair (which pushes bonding pairs slightly closer together), the 3 N-H bonds arrange into a trigonal pyramidal shape, like a tripod.",
    "Don't confuse electron-pair geometry (tetrahedral, counting the lone pair) with molecular geometry (trigonal pyramidal, counting only atoms) — VSEPR questions often test exactly this distinction.",
    "Incorrect — trigonal planar describes 3 bonding pairs with NO lone pair (like BF3), not NH3's case with a lone pair present.",
    "Incorrect — linear geometry applies to only 2 electron domains (like BeCl2 or CO2), not 4 domains as in NH3.",
    "Correct — 3 bonding pairs plus 1 lone pair on the central atom gives the trigonal pyramidal molecular shape characteristic of NH3.",
    "Incorrect — tetrahedral describes the underlying electron-pair geometry (or a molecule with 4 bonding pairs and no lone pairs, like CH4), not NH3's molecular shape once the lone pair's non-atom position is excluded.")

add(92, "Water is polar overall because its bent molecular geometry prevents the two O-H bond dipoles from canceling out.",
    "Oxygen is more electronegative than hydrogen, creating two polar O-H bonds; because water's shape is bent (not linear) due to oxygen's two lone pairs, these bond dipoles don't point in exactly opposite directions and so don't cancel, giving the whole molecule a net dipole moment (polarity).",
    "Shape matters as much as bond polarity for overall molecular polarity — a molecule with polar bonds can still be nonpolar overall if its geometry is symmetric enough to cancel the dipoles (e.g. linear CO2).",
    "Incorrect — a linear shape (like in CO2) would allow opposite bond dipoles to cancel, making the molecule nonpolar — water is NOT linear.",
    "Incorrect — oxygen and hydrogen have quite different electronegativities, which is exactly why the O-H bonds are polar in the first place.",
    "Incorrect — water does contain polar O-H bonds (unequal electronegativity between O and H creates genuine bond dipoles).",
    "Correct — water's bent shape prevents the two O-H bond dipoles from canceling out, giving the whole molecule a net dipole (polarity).")

add(93, "Metallic bonding's 'sea' of delocalized electrons explains why metals are malleable, ductile, and good conductors.",
    "Because valence electrons in a metal are delocalized (not tied to specific atoms), metal cations can slide past each other without breaking bonds (giving malleability/ductility), and the mobile electron sea readily carries electric current (giving high conductivity).",
    "Delocalized electrons are the key to BOTH mechanical properties (bendable, not brittle) and electrical conductivity of metals — one shared cause explaining two different behaviors.",
    "Correct — the delocalized electron sea directly explains metals' malleability, ductility, and electrical conductivity.",
    "Incorrect — this describes ionic/covalent network solids (brittle, poor conductors), the opposite of typical metallic behavior.",
    "Incorrect — metals are opaque and lustrous, not transparent, and are excellent (not poor) conductors.",
    "Incorrect — most metals have high melting/boiling points and are not typically volatile at room temperature.")

add(94, "A hydrogen bond between water molecules forms between a hydrogen atom on one molecule and an oxygen lone pair on a neighboring molecule.",
    "Because O-H bonds are highly polar, the partially positive hydrogen on one water molecule is strongly attracted to a partially negative oxygen lone pair on an adjacent water molecule — this intermolecular attraction (hydrogen bonding) explains water's unusually high boiling point, surface tension, and other anomalous properties.",
    "Hydrogen bonds are INTERmolecular (between separate molecules), not intramolecular (within one molecule) — the question specifically distinguishes 'between two water molecules'.",
    "Incorrect — a direct oxygen-oxygen attraction isn't what defines a hydrogen bond; it specifically involves a hydrogen atom and an electronegative atom's lone pair.",
    "Correct — a hydrogen bond connects a hydrogen atom on one water molecule to an oxygen lone pair on a neighboring molecule.",
    "Incorrect — hydrogen-hydrogen 'bonds' aren't how hydrogen bonding works; it requires one hydrogen and one electronegative lone-pair atom.",
    "Incorrect — the question specifically asks about a bond BETWEEN two separate water molecules, not within a single molecule.")

add(95, "Gases have neither a definite shape nor a definite volume, expanding to fill their container.",
    "Gas particles are far apart with weak intermolecular forces, moving freely and expanding to fill whatever container they occupy, taking on both its shape and its entire volume — unlike solids (fixed shape/volume) or liquids (fixed volume, variable shape).",
    "Solid: fixed shape + fixed volume. Liquid: fixed volume + variable shape. Gas: variable shape AND variable volume — the three-state comparison table worth memorizing.",
    "Incorrect — solids have both a definite shape and definite volume, the opposite of the question's description.",
    "Incorrect — liquids have a definite volume (though variable shape), so this doesn't match 'neither' shape nor volume being definite.",
    "Correct — gases have neither a fixed shape nor a fixed volume, expanding to fill their container.",
    "Incorrect — 'crystal' describes an ordered solid structure, which has both definite shape and volume.")

add(96, "By Boyle's law (P1V1 = P2V2), doubling pressure from 2.0 to 4.0 atm halves the volume from 8.0 L to 4.0 L.",
    "At constant temperature, pressure and volume are inversely proportional: P1V1 = P2V2. Here, 2.0 atm x 8.0 L = 4.0 atm x V2, so V2 = 16 / 4.0 = 4.0 L.",
    "Boyle's law: as pressure goes UP, volume goes DOWN proportionally (inverse relationship) — doubling pressure should halve volume, a quick sanity check.",
    "Incorrect — 16 L would result from doubling (not halving) the volume, the opposite direction Boyle's law predicts when pressure increases.",
    "Incorrect — 32 L is far too large and doesn't satisfy P1V1 = P2V2 for these values.",
    "Incorrect — 2.0 L would require quadrupling the pressure ratio beyond what's given (2.0 to 4.0 atm is only a doubling).",
    "Correct — 2.0 atm x 8.0 L = 4.0 atm x 4.0 L = 16 L·atm on both sides, satisfying Boyle's law.")

add(97, "Using the combined gas law, 6 L at 300 K/1 atm becomes 6 L at 600 K/2 atm (the changes exactly offset).",
    "Combined gas law: P1V1/T1 = P2V2/T2. Plugging in: (1)(6)/300 = (2)(V2)/600, so 0.02 = V2/300, giving V2 = 6 L. Doubling both temperature (which would double volume alone) and pressure (which would halve volume alone) exactly cancel out, leaving volume unchanged.",
    "When both pressure and temperature double simultaneously, their individual effects on volume (double vs halve) cancel out — a useful pattern-recognition shortcut for combined gas law problems.",
    "Correct — with P1V1/T1 = P2V2/T2, the doubled temperature and doubled pressure exactly cancel, leaving the volume unchanged at 6 L.",
    "Incorrect — 3 L would result only from the pressure-doubling effect alone, ignoring the offsetting temperature increase.",
    "Incorrect — 12 L would result only from the temperature-doubling effect alone, ignoring the offsetting pressure increase.",
    "Incorrect — 24 L doesn't satisfy the combined gas law equation for these given values.")

add(98, "Calcium carbonate (CaCO3) has a molar mass of approximately 100 g/mol (40 + 12 + 48).",
    "Adding atomic masses: Ca (~40) + C (~12) + 3xO (~16 each = 48) = 40 + 12 + 48 = 100 g/mol, a commonly used approximate value in stoichiometry problems.",
    "Break CaCO3 into its three elements and add their atomic masses individually — a reliable way to double-check any molar mass calculation.",
    "Incorrect — 56 g/mol is too low and doesn't match the sum of Ca + C + 3O.",
    "Correct — 40 (Ca) + 12 (C) + 48 (3 x O) = 100 g/mol.",
    "Incorrect — 78 g/mol doesn't correspond to the correct atomic mass sum for CaCO3.",
    "Incorrect — 44 g/mol is actually close to CO2's molar mass, not CaCO3's, and is far too low here.")

add(99, "3 moles of Al(OH)3 contain 3 x 3 = 9 moles of hydrogen atoms (3 OH groups per formula unit).",
    "Each Al(OH)3 formula unit contains 3 hydroxide (OH) groups, so 3 hydrogen atoms per molecule; with 3 moles of Al(OH)3, total H atoms = 3 moles x 3 H/molecule = 9 moles of H atoms.",
    "Count subscripts carefully within the formula (3 OH groups = 3 H atoms per unit) before multiplying by the given number of moles.",
    "Incorrect — 3 moles would only account for 1 H atom per formula unit, undercounting the 3 OH groups actually present.",
    "Incorrect — 6 moles would correspond to only 2 H atoms per formula unit, still undercounting.",
    "Correct — 3 moles of Al(OH)3 x 3 H atoms per unit = 9 moles of H atoms.",
    "Incorrect — 12 moles would overcount, implying 4 H atoms per formula unit rather than the actual 3.")

add(100, "500 mL solution with 2.0 mol NaOH has molarity = 2.0 mol / 0.500 L = 4.0 M.",
    "Molarity = moles of solute / liters of solution. Converting 500 mL to 0.500 L: molarity = 2.0 mol / 0.500 L = 4.0 mol/L (M).",
    "Always convert mL to L (divide by 1000) before dividing moles by volume — a very common unit-conversion slip in molarity problems.",
    "Incorrect — 0.25 M would result from dividing 0.5 by 2.0 (an inverted calculation), not moles by volume.",
    "Incorrect — 1.0 M doesn't match dividing 2.0 mol by 0.5 L correctly.",
    "Incorrect — 2.0 M would result from forgetting to convert 500 mL to 0.5 L (treating volume as 1 L instead).",
    "Correct — 2.0 mol divided by 0.500 L gives 4.0 M.")

add(101, "For 2H2 + O2 -> 2H2O, 8 moles of H2 require 4 moles of O2 (a 2:1 mole ratio).",
    "The balanced equation shows a 2:1 mole ratio of H2 to O2. Using that ratio: 8 mol H2 x (1 mol O2 / 2 mol H2) = 4 mol O2 needed for complete reaction.",
    "Always use the coefficients from the BALANCED equation as your mole ratio — here 2 mol H2 pairs with exactly 1 mol O2.",
    "Correct — 8 mol H2 x (1 O2 / 2 H2) = 4 mol O2, matching the balanced 2:1 ratio.",
    "Incorrect — 2 mol would result from an inverted or miscalculated ratio, not matching 8 mol H2 correctly.",
    "Incorrect — 8 mol would assume a 1:1 ratio, but the balanced equation actually requires half as much O2 as H2.",
    "Incorrect — 16 mol would double the required amount, the opposite of the actual 2:1 (H2:O2) stoichiometric relationship.")

add(102, "In an endothermic reaction, products end up at higher energy than the reactants (energy absorbed from surroundings).",
    "Endothermic reactions absorb heat from the surroundings to proceed, so the products end up storing more potential/chemical energy than the reactants did — the reverse of an exothermic reaction, where products release energy and end up lower.",
    "Endo = energy IN (absorbed), products end HIGHER in energy. Exo = energy OUT (released), products end LOWER — a core thermochemistry pairing.",
    "Incorrect — lower product energy describes an exothermic, not endothermic, reaction.",
    "Correct — in an endothermic reaction, products have higher energy than reactants, since energy was absorbed.",
    "Incorrect — the whole point of endothermic/exothermic classification is that reactant and product energies DIFFER, not stay the same.",
    "Incorrect — a genuine chemical reaction with an energy change cannot have zero energy difference between reactants and products.")

add(103, "Hess's law works because enthalpy is a state function: total enthalpy change depends only on initial and final states, not the path taken.",
    "Because enthalpy (H) is a state function, the overall enthalpy change for a reaction is the same whether it happens in one step or through several intermediate steps — this allows chemists to add/subtract known reaction enthalpies (Hess's law) to find an otherwise hard-to-measure enthalpy change.",
    "'State function' means path-independence — this is the whole basis for why Hess's law-style addition of reactions is mathematically valid.",
    "Incorrect — Hess's law is specifically a method for calculating enthalpy change indirectly, by combining known steps.",
    "Incorrect — being a state function means enthalpy change does NOT depend on pathway, the opposite of this statement.",
    "Correct — a state function's value depends only on initial and final states, not the specific path, which is the basis of Hess's law.",
    "Incorrect — enthalpy changes are generally nonzero for real reactions; being a state function doesn't imply they're always zero.")

add(104, "Decreasing volume (raising pressure) shifts N2+3H2<->2NH3 toward the products side, which has fewer gas moles (2 vs 4).",
    "By Le Chatelier's principle, increasing pressure (compressing volume) shifts equilibrium toward the side with fewer total gas moles, to partially counteract the pressure increase. Here, reactants total 1+3=4 moles of gas versus products' 2 moles, so the equilibrium shifts toward the products (more NH3 forms) — the basis of the industrial Haber process's high-pressure conditions.",
    "'Increase pressure -> shift toward fewer gas moles' is the key Le Chatelier rule for pressure/volume changes — count total gas moles on each side to apply it.",
    "Incorrect — the reactant side has MORE gas moles (4), so increased pressure shifts AWAY from, not toward, the reactants.",
    "Incorrect — Le Chatelier's principle shifts the position of equilibrium; it does not completely deplete reactants.",
    "Incorrect — pressure changes do cause a real shift in gas-phase equilibria when the mole counts differ between sides, as they do here.",
    "Correct — the product side (2 moles of gas) is favored when pressure increases/volume decreases, since it's the side with fewer gas moles.")

add(105, "Raising temperature for an endothermic reaction at equilibrium shifts it toward products, increasing yield.",
    "Since heat can be treated as a 'reactant' in an endothermic reaction, adding more heat (raising temperature) shifts equilibrium toward the products (which absorb that extra heat), per Le Chatelier's principle — increasing product yield.",
    "For an ENDOTHERMIC reaction, more heat = more product (shift right); for an EXOTHERMIC reaction, more heat would instead shift equilibrium back toward reactants (shift left) — opposite responses depending on reaction type.",
    "Correct — for an endothermic reaction, raising temperature shifts equilibrium toward products, increasing yield.",
    "Incorrect — shifting toward reactants (decreasing yield) is what would happen for an EXOTHERMIC reaction upon heating, not an endothermic one.",
    "Incorrect — temperature changes do meaningfully shift equilibrium position when a reaction has a nonzero enthalpy change, as here.",
    "Incorrect — a temperature increase shifts equilibrium; it does not stop the reaction from occurring.")

add(106, "Raising temperature increases reaction rate mainly because molecules collide more frequently and with greater kinetic energy.",
    "According to collision theory, higher temperature means faster-moving molecules, leading to both more frequent collisions and a greater proportion of those collisions having enough energy to exceed the activation energy barrier — both effects combine to speed up the reaction.",
    "Collision theory's two ingredients for a successful, rate-boosting collision: enough FREQUENCY and enough ENERGY — heat increases both simultaneously.",
    "Incorrect — higher temperature makes molecules move faster, not slower.",
    "Correct — more frequent, higher-energy collisions from increased temperature is exactly why reaction rate rises.",
    "Incorrect — temperature doesn't change whether a reaction is thermodynamically favorable (that's about ΔG, unrelated to rate/kinetics here).",
    "Incorrect — activation energy is a fixed property of the reaction pathway; it doesn't increase with temperature (though more molecules can now surpass it).")

add(107, "A catalyst speeds up a reaction by providing an alternative pathway with lower activation energy.",
    "Catalysts (without being consumed) bind reactants and stabilize a lower-energy transition state, opening up a reaction pathway with a smaller activation energy barrier — this lets more collisions succeed per unit time, increasing rate without altering the reaction's thermodynamics (products, ΔH) at all.",
    "Catalysts change the RATE (kinetics) of a reaction, never the identity of the products or the reaction's overall energy change (thermodynamics) — a very frequently tested distinction.",
    "Incorrect — a catalyst LOWERS, not raises, the required activation energy.",
    "Incorrect — a catalyst never changes what products form; it only affects how fast the existing reaction proceeds.",
    "Correct — offering a lower-activation-energy alternative pathway is precisely how a catalyst increases reaction rate.",
    "Incorrect — by definition, a true catalyst is regenerated and not permanently consumed in the reaction.")

add(108, "In an electrochemical cell, oxidation (loss of electrons) always occurs at the anode.",
    "By convention, the anode is defined as the electrode where oxidation occurs (electrons are released into the external circuit), while the cathode is where reduction occurs (electrons are gained) — true in both galvanic and electrolytic cells.",
    "Remember 'AN OX, RED CAT': ANode = OXidation, REDuction = CAThode — a classic mnemonic for electrochemistry.",
    "Incorrect — the cathode is where reduction, not oxidation, occurs.",
    "Incorrect — a voltmeter measures voltage; it isn't an electrode where a redox half-reaction occurs.",
    "Incorrect — the salt bridge maintains charge balance between half-cells; it isn't the site of oxidation.",
    "Correct — oxidation, by definition, always occurs at the anode in an electrochemical cell.")

add(109, "In Zn(s) + Cu2+(aq) -> Zn2+(aq) + Cu(s), Cu2+ gains electrons and is reduced to Cu(s).",
    "Zinc metal loses 2 electrons (is oxidized) to become Zn2+, while those electrons are transferred to Cu2+ ions, which gain them (are reduced) to form solid copper metal — a classic single-replacement redox reaction and the basis of the Daniell cell.",
    "Look at oxidation state changes: Cu goes from +2 (in Cu2+) to 0 (in Cu metal) — a DECREASE in oxidation number always signals reduction (gain of electrons).",
    "Correct — copper ions gain electrons, going from Cu2+ to Cu(s), which is reduction.",
    "Incorrect — zinc, not copper, is the species that loses electrons (is oxidized) in this reaction.",
    "Incorrect — copper's oxidation state clearly changes (+2 to 0), so it is not unchanged.",
    "Incorrect — copper ions are a reactant being consumed/transformed here, not acting as an unchanged catalyst.")

add(110, "A pH of 2 indicates a strongly acidic solution (far below neutral pH 7).",
    "The pH scale runs roughly 0 (strongly acidic) to 14 (strongly basic), with 7 as neutral. A pH of 2 is well below 7, corresponding to a high H+ concentration and strong acidity — similar in acidity to stomach acid or lemon juice.",
    "Lower pH numbers = more acidic; higher pH numbers = more basic; 7 = neutral — the fundamental pH scale orientation.",
    "Incorrect — a weakly basic solution would have a pH somewhat above 7, not as low as 2.",
    "Correct — a pH of 2 is far below neutral (7), indicating strong acidity.",
    "Incorrect — strongly basic solutions have pH values well above 7 (closer to 14), the opposite end of the scale from pH 2.",
    "Incorrect — neutral solutions have pH 7, not 2.")

add(111, "The equivalence point on a titration curve is where moles of acid exactly equal moles of base added, marked by the curve's steepest point.",
    "As base is gradually added to an acid, pH rises slowly at first, then shoots up sharply near the point of exact stoichiometric neutralization (equivalence point) — visible as the steep, near-vertical section of the titration curve, before leveling off again in excess base.",
    "The equivalence point is a stoichiometric concept (moles acid = moles base); the visually steepest part of the graph is where it sits — don't confuse it with the flatter buffer region earlier on the curve.",
    "Incorrect — the buffer region is the relatively flat portion of the curve well before the equivalence point, resisting pH change.",
    "Incorrect — 'half-life point' is a radioactive decay/kinetics term, not a titration curve feature.",
    "Correct — the equivalence point, where acid and base moles are exactly equal, is marked by the curve's steep rise.",
    "Incorrect — 'saturation point' describes when a solution can dissolve no more solute, an unrelated solubility concept, not a titration curve feature.")

add(112, "By the Bronsted-Lowry definition, a base accepts a proton (H+).",
    "Bronsted-Lowry theory defines acids as proton (H+) donors and bases as proton (H+) acceptors — a broader definition than the Arrhenius theory, since it doesn't require the base to release hydroxide ions directly (e.g. ammonia, NH3, acts as a Bronsted-Lowry base by accepting H+ without containing OH- itself).",
    "Bronsted-Lowry: Acid = donates H+; Base = accepts H+ — remember it's about proton transfer, not necessarily hydroxide ions.",
    "Incorrect — donating a proton describes a Bronsted-Lowry ACID, the opposite role from a base.",
    "Incorrect — this is closer to the narrower Arrhenius definition of a base; Bronsted-Lowry bases don't need to contain/release hydroxide themselves (e.g. NH3).",
    "Incorrect — donating an electron pair describes a Lewis base, a related but distinct (broader) definition from Bronsted-Lowry.",
    "Correct — accepting a proton (H+) is the defining feature of a Bronsted-Lowry base.")

add(113, "The ammonia/ammonium chloride buffer resists pH drop because ammonia (the weak base component) neutralizes added strong acid.",
    "A buffer pairs a weak base (NH3) with its conjugate acid (NH4+, from NH4Cl); when strong acid (H+) is added, the ammonia component reacts with and consumes it (NH3 + H+ -> NH4+), preventing a large drop in pH, while the ammonium component would similarly neutralize any added strong base.",
    "In a buffer, the WEAK BASE component neutralizes added ACID, and the WEAK ACID (conjugate) component neutralizes added BASE — match each buffer half to the stress it counters.",
    "Correct — the ammonia (weak base) component reacts with and neutralizes added strong acid, resisting a sharp pH drop.",
    "Incorrect — ammonium chloride (the conjugate acid component) would instead react with added base, not with added acid.",
    "Incorrect — a properly formed buffer does have significant capacity to resist pH change, contrary to this statement.",
    "Incorrect — the whole point of a buffer is to prevent a sharp pH drop when acid is added, not let it happen anyway.")

add(114, "The -OH functional group defines the alcohol class of organic compounds.",
    "An alcohol is characterized by a hydroxyl (-OH) group attached to a saturated carbon; this differs from a carboxylic acid's -COOH group, an aldehyde's terminal -CHO, or a ketone's internal C=O.",
    "-OH = alcohol; -CHO = aldehyde; C=O (internal) = ketone; -COOH = carboxylic acid — matching functional groups to compound classes is a core organic chemistry skill.",
    "Incorrect — aldehydes are characterized by a terminal -CHO group, not -OH.",
    "Correct — the -OH (hydroxyl) group is the defining feature of alcohols.",
    "Incorrect — ketones are characterized by an internal carbonyl (C=O) group, not -OH.",
    "Incorrect — esters are characterized by a -COO- linkage, not a simple -OH group.")

add(115, "Alkanes mainly undergo substitution reactions, where a hydrogen atom is replaced by another atom or group.",
    "Because alkanes are saturated (only single C-C and C-H bonds, no double/triple bonds to add across), they can't undergo addition reactions easily; instead, under conditions like UV light with a halogen, a hydrogen atom is substituted (replaced) by another atom (e.g. halogenation: CH4 + Cl2 -> CH3Cl + HCl).",
    "Alkanes (saturated) -> substitution; alkenes/alkynes (unsaturated, have double/triple bonds) -> addition — matching hydrocarbon saturation to reaction type.",
    "Incorrect — addition reactions are characteristic of unsaturated hydrocarbons (alkenes/alkynes), not saturated alkanes.",
    "Incorrect — elimination reactions remove atoms to form a double bond (e.g. from alcohols/alkyl halides), a different reaction type than typical alkane chemistry.",
    "Correct — substitution, replacing a hydrogen with another atom/group, is the characteristic reaction type for saturated alkanes.",
    "Incorrect — condensation reactions join two molecules with loss of a small molecule (like water), not the typical alkane reaction pattern.")

add(116, "A secondary alcohol has its -OH-bearing carbon bonded to exactly two other carbon atoms.",
    "Alcohols are classified by how many carbon atoms are attached to the carbon bearing the -OH group: primary (1 carbon attached), secondary (2 carbons attached), tertiary (3 carbons attached). A secondary alcohol's -OH carbon sits between exactly two other carbon chains.",
    "Primary=1 carbon attached, Secondary=2, Tertiary=3 — count the carbons attached to the -OH-bearing carbon, not the total carbons in the whole molecule.",
    "Incorrect — one attached carbon describes a primary alcohol, not secondary.",
    "Incorrect — zero attached carbons would mean it's not actually classified this way (essentially just methanol, a special minimal case).",
    "Incorrect — three attached carbons describes a tertiary alcohol, not secondary.",
    "Correct — exactly two carbon atoms attached to the -OH-bearing carbon defines a secondary alcohol.")

add(117, "SN1 mechanisms proceed in two steps through a relatively stable carbocation intermediate.",
    "In an SN1 (unimolecular nucleophilic substitution) reaction, the leaving group departs first, forming a carbocation intermediate (rate-determining step), which the nucleophile then attacks in a second, fast step — favored by tertiary substrates whose carbocations are more stabilized.",
    "SN1 = 2 steps, carbocation intermediate, rate depends only on substrate concentration. SN2 = 1 step, concerted, backside attack, rate depends on both substrate and nucleophile — the two classic substitution mechanisms to contrast.",
    "Correct — a two-step mechanism proceeding through a carbocation intermediate is the defining feature of SN1.",
    "Incorrect — a one-step concerted mechanism with simultaneous bond breaking/forming describes SN2, not SN1.",
    "Incorrect — SN1 (like SN2) requires a leaving group to depart; leaving groups are essential to both substitution mechanisms.",
    "Incorrect — SN1 mechanisms are associated with alkyl halides/similar substrates, not specifically restricted to alkenes.")

add(118, "Esters form from carboxylic acids and alcohols via condensation, releasing water as the byproduct.",
    "In Fischer esterification, a carboxylic acid's -OH and an alcohol's -OH combine (typically acid-catalyzed), losing a water molecule as the ester (-COO-) linkage forms between them — a classic condensation (dehydration synthesis) reaction.",
    "Ester formation is a CONDENSATION reaction, always releasing WATER — the reverse process (ester hydrolysis) adds water back to break the ester apart.",
    "Incorrect — carbon dioxide isn't the byproduct of esterification; that's more associated with reactions like carbonate decomposition.",
    "Correct — water is the small molecule released when a carboxylic acid and alcohol condense to form an ester.",
    "Incorrect — ammonia isn't produced in standard ester-forming reactions between a carboxylic acid and alcohol.",
    "Incorrect — hydrogen gas isn't released during esterification; that's more typical of reactions like a metal reacting with an acid.")

add(119, "A carbonyl group (C=O) located between two carbon chains (not at a chain end) defines a ketone.",
    "Ketones have their carbonyl carbon bonded to two other carbon-containing groups on both sides (internal position), whereas aldehydes have the carbonyl at the very end of the chain, bonded to at least one hydrogen.",
    "Carbonyl at the END of the chain (with an H) = aldehyde; carbonyl INSIDE the chain (between two carbons) = ketone — positioning is the key distinguishing feature.",
    "Incorrect — an aldehyde has its carbonyl group at the end of the carbon chain, not positioned internally between two chains.",
    "Incorrect — a carboxylic acid has a -COOH group (carbonyl plus -OH) at the chain's end, not an internal carbonyl alone.",
    "Correct — an internally positioned carbonyl group, between two carbon chains, is precisely what defines a ketone.",
    "Incorrect — an amine is characterized by a nitrogen-containing -NH2 (or similar) group, unrelated to a carbonyl.")

add(120, "Noble gases (Group 18) are largely unreactive because they already have a complete, stable valence electron shell.",
    "With a full outer electron shell (octet, or duet for helium), noble gases have little thermodynamic drive to gain, lose, or share electrons, making them chemically inert under most conditions (though a few heavier noble gases can form compounds under extreme conditions).",
    "'Complete valence shell = stable = unreactive' is the single biggest organizing idea in explaining periodic reactivity trends, and noble gases are the textbook example.",
    "Incorrect — small atomic size alone doesn't explain unreactivity; several small atoms (like fluorine) are actually highly reactive.",
    "Incorrect — noble gases have essentially no tendency to form multiple bonds; this is the opposite of their actual chemical behavior.",
    "Incorrect — nuclear charge alone doesn't determine reactivity; it's the resulting stable electron configuration that matters most.",
    "Correct — a complete, stable valence electron shell is the fundamental reason noble gases are so unreactive.")

add(121, "Alkali metals react with water more vigorously than alkaline earth metals of the same period because they have lower ionization energy and lose their single valence electron more easily.",
    "Group 1 (alkali) metals have only one valence electron to lose and generally lower ionization energies than the corresponding Group 2 (alkaline earth) metals of the same period, making them react faster and more violently with water (e.g. sodium fizzing/igniting vs magnesium reacting only slowly with cold water).",
    "Lower ionization energy = electron given up more easily = more vigorous/faster reactivity — a recurring theme across many reactivity comparisons in the periodic table.",
    "Correct — lower ionization energy, letting them lose their single valence electron more readily, explains alkali metals' greater reactivity with water.",
    "Incorrect — higher ionization energy would make a metal LESS reactive/slower to lose electrons, the opposite of the actual trend.",
    "Incorrect — alkali metals famously do react with water, often vigorously (sometimes explosively for heavier ones).",
    "Incorrect — alkali metals actually have LARGER atomic radii than alkaline earth metals of the same period, not smaller — and radius isn't the main reason here anyway.")

add(122, "In Fe2O3 + 3CO -> 2Fe + 3CO2, iron's oxidation state changes from +3 to 0, which is reduction.",
    "In Fe2O3, iron is in the +3 oxidation state (bonded to oxygen); in elemental Fe metal (the product), iron's oxidation state is 0. A decrease in oxidation number (+3 to 0) means iron gained electrons, i.e. it was reduced, while CO is simultaneously oxidized to CO2 (this is the blast furnace iron-extraction reaction).",
    "A drop in oxidation number = reduction (gain of electrons); a rise = oxidation (loss of electrons) — check the sign of the change to classify a redox process correctly.",
    "Incorrect — this reverses the actual direction; iron starts at +3 (in the oxide) and ends at 0 (as metal), not the other way around.",
    "Correct — iron's oxidation state drops from +3 to 0, which is reduction (gain of electrons).",
    "Incorrect — iron's actual starting oxidation state in Fe2O3 is +3, not +2, and its ending state is 0, not +3.",
    "Incorrect — iron's oxidation state clearly does change here (from +3 in the ore to 0 in the metal), a defining feature of this redox reaction.")

add(123, "Boiling point elevation happens because a dissolved non-volatile solute lowers the solvent's vapor pressure, requiring a higher temperature to reach boiling.",
    "Colligative properties depend only on the number of dissolved solute particles, not their identity. A non-volatile solute occupies some of the solvent surface, reducing the rate of solvent evaporation (lowering vapor pressure); since boiling occurs when vapor pressure equals atmospheric pressure, a higher temperature is now needed to reach that point.",
    "Colligative properties (boiling point elevation, freezing point depression, vapor pressure lowering) all trace back to one cause: more dissolved particles reducing the solvent's escaping tendency (vapor pressure).",
    "Incorrect — a non-volatile solute does have a measurable effect on boiling point; that's the whole basis of this colligative property.",
    "Incorrect — a non-volatile solute LOWERS, not increases, the solvent's vapor pressure.",
    "Correct — lowering the solvent's vapor pressure, which then requires a higher temperature to reach boiling, is exactly why boiling point elevation occurs.",
    "Incorrect — the key colligative effect here concerns vapor pressure/boiling point, not primarily the solution's density.")

add(124, "0.4 M KOH: neutralizing 20 mL of 0.4 M H2SO4 requires 0.016 mol KOH, giving 0.4 M when dissolved in 40 mL.",
    "Moles of H2SO4 = 0.020 L x 0.4 M = 0.008 mol. From H2SO4 + 2KOH -> K2SO4 + 2H2O, moles of KOH needed = 2 x 0.008 = 0.016 mol. Molarity of KOH = 0.016 mol / 0.040 L = 0.4 M.",
    "Watch the 1:2 mole ratio in the balanced equation (1 H2SO4 reacts with 2 KOH) — forgetting to double the moles of KOH is a very common error in this type of titration problem.",
    "Incorrect — 0.1 M would result from skipping the 1:2 mole ratio and/or a volume conversion error.",
    "Incorrect — 0.2 M would result from using the acid's mole count directly for KOH without doubling for the 1:2 stoichiometric ratio.",
    "Incorrect — 0.8 M would overcorrect, doubling the actual correct concentration.",
    "Correct — applying the 1:2 mole ratio and the given volumes correctly gives 0.4 M KOH.")

add(125, "Ozone layer depletion is primarily caused by chlorofluorocarbons (CFCs) and related halogenated compounds.",
    "CFCs, once widely used in refrigerants and aerosols, release chlorine atoms in the stratosphere under UV light; these chlorine atoms catalytically destroy ozone (O3) molecules in a repeating chain reaction, thinning the protective ozone layer — leading to international bans like the Montreal Protocol.",
    "CFCs are the textbook cause of ozone depletion — don't confuse this with the separate issue of greenhouse gases (like CO2) driving global warming/climate change.",
    "Correct — CFCs and similar halogenated compounds are the primary drivers of stratospheric ozone depletion.",
    "Incorrect — increased CO2 emissions are primarily linked to global warming/the greenhouse effect, a separate environmental issue from ozone depletion.",
    "Incorrect — 'excess oxygen production' is not a recognized cause of ozone depletion; if anything, ozone (O3) is a form of oxygen being destroyed, not overproduced.",
    "Incorrect — volcanic ash is not the primary driver of ozone-layer depletion; CFCs are the dominant, well-established cause.")

add(126, "Reducing sulfur dioxide and nitrogen oxide emissions from industry/vehicles most directly helps reduce acid rain.",
    "Acid rain forms when SO2 and NOx (mainly from burning fossil fuels in power plants and vehicles) react with atmospheric water vapor to form sulfuric and nitric acids; cutting these emissions (e.g. via scrubbers, catalytic converters, cleaner fuels) directly reduces the acid-forming pollutants entering the atmosphere.",
    "Acid rain's two main culprit gases are SO2 and NOx — any answer that INCREASES fossil fuel combustion or REMOVES pollution-control devices (like catalytic converters) makes acid rain worse, not better.",
    "Incorrect — increasing coal combustion without emission controls would worsen, not reduce, acid rain.",
    "Correct — directly reducing SO2 and NOx emissions is the most effective way to reduce acid rain formation.",
    "Incorrect — removing catalytic converters would increase, not decrease, harmful vehicle emissions contributing to acid rain.",
    "Incorrect — increasing fossil fuel subsidies would likely increase fossil fuel use and associated emissions, worsening acid rain, not helping.")

data = E
print(f"Chemistry batch: {len(data)} entries, ids {data[0]['id']}-{data[-1]['id']}")
assert len(data) == 45
OUT.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
print("wrote", OUT)
