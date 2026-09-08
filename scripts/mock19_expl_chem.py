import json
from pathlib import Path

EXPL = {
8206: dict(
    short="The nucleus contains protons and neutrons.",
    long="The atomic nucleus is composed of protons (positive charge) and neutrons (no charge), collectively called nucleons. Electrons orbit outside the nucleus in electron shells/orbitals.",
    trick="Electrons are NOT in the nucleus — a very basic but sometimes-tested distinction between nuclear and extranuclear particles.",
    options=dict(a="Electrons alone would leave out the actual nuclear particles (protons/neutrons).",
                 b="Electrons are outside the nucleus, not inside it with protons.",
                 c="Electrons are outside the nucleus; neutrons are correct but electrons don't belong here.",
                 d="Correct — protons and neutrons (nucleons) make up the nucleus.")
),
8207: dict(
    short="K-39 has 19 protons (atomic number) and 39-19=20 neutrons.",
    long="Mass number (39) = protons + neutrons. Since atomic number (protons) = 19, neutrons = 39 - 19 = 20.",
    trick="Don't confuse mass number (39) itself with the neutron count — you must subtract the atomic number first.",
    options=dict(a="39 is the mass number itself, not the neutron count.",
                 b="Correct — 39 (mass number) minus 19 (protons) = 20 neutrons.",
                 c="19 is the atomic number/proton count, not the neutron count.",
                 d="58 would be an incorrect sum, not the actual neutron count.")
),
8208: dict(
    short="Sulfur (Z=16): 1s2 2s2 2p6 3s2 3p4.",
    long="Filling orbitals in order for 16 electrons: 1s2 (2) + 2s2 (2) + 2p6 (6) + 3s2 (2) + 3p4 (4) = 16 total electrons, matching sulfur's atomic number.",
    trick="Watch the 3p subshell electron count carefully — 3p4 (not 3p2 or 3p6) is what correctly totals to 16 electrons for sulfur.",
    options=dict(a="Correct — this configuration correctly totals 16 electrons for sulfur (Z=16).",
                 b="3p2 would only total 14 electrons, undercounting sulfur's actual electron number.",
                 c="3p6 would total 18 electrons — that's the configuration for argon, not sulfur.",
                 d="This configuration (3s1 3p5) is non-standard and doesn't represent sulfur's ground state.")
),
8209: dict(
    short="16 protons, 18 electrons -> charge = +16 + (-18) = -2.",
    long="Charge = (number of protons) - (number of electrons) in terms of net charge magnitude: with more electrons (18) than protons (16), there are 2 extra negative charges, giving an overall charge of -2.",
    trick="More electrons than protons means a NEGATIVE ion (anion) — don't flip the sign by mistake.",
    options=dict(a="Correct — 2 more electrons than protons gives a net charge of -2.",
                 b="+16 would ignore the electrons entirely; charge depends on the proton-electron difference.",
                 c="-18 would be wrong; it's the electron-proton DIFFERENCE (2), not the electron count itself.",
                 d="+2 has the correct magnitude but the wrong sign — more electrons than protons means negative, not positive.")
),
8210: dict(
    short="Mass number = protons + neutrons.",
    long="By definition, the mass number (nucleon number) of an atom equals the total count of protons plus neutrons in its nucleus (electrons contribute negligible mass and aren't counted).",
    trick="Don't include electrons in the mass number — their mass is negligible and they aren't nucleons.",
    options=dict(a="Protons alone would just give the atomic number, not the mass number.",
                 b="Electrons have negligible mass and aren't part of mass number.",
                 c="Correct — mass number is the sum of protons and neutrons.",
                 d="Neutrons and electrons together excludes protons, which are essential to mass number.")
),
8211: dict(
    short="Horizontal rows of the periodic table are called periods.",
    long="The periodic table's horizontal rows are periods (numbered 1-7), while vertical columns are groups (or families). Elements in the same period have the same number of electron shells.",
    trick="Don't swap 'periods' (rows) and 'groups' (columns) — a very commonly confused pair of terms.",
    options=dict(a="Blocks (s, p, d, f) refer to which subshell is being filled, not rows.",
                 b="Correct — horizontal rows are called periods.",
                 c="Groups are the vertical columns, not horizontal rows.",
                 d="Families is another name for groups (columns), not rows.")
),
8212: dict(
    short="Ionization energy increases across a period as nuclear charge rises and radius shrinks.",
    long="Moving left to right across a period, protons (nuclear charge) increase while electrons are added to the same shell, pulling electrons closer (smaller atomic radius) and making them harder to remove — hence ionization energy generally increases.",
    trick="This is a general trend with some exceptions (e.g., Be to B, N to O), but the overall/expected trend tested here is a steady increase.",
    options=dict(a="Correct — increasing nuclear charge and decreasing radius raise ionization energy across a period.",
                 b="Ionization energy is not constant; it clearly trends with atomic structure changes.",
                 c="Ionization energy stays positive (energy required to remove an electron), it doesn't become negative.",
                 d="This is the opposite of the actual trend — ionization energy increases, not decreases, across a period.")
),
8213: dict(
    short="Low ionization energy + tendency to lose one electron -> Group 1 (alkali metals).",
    long="Group 1 elements (alkali metals) have exactly one valence electron, held loosely due to low ionization energy and large atomic radius, making them highly likely to lose that one electron to form a +1 ion.",
    trick="Noble gases (Group 18) have very HIGH ionization energy (stable, don't lose electrons) — the opposite of what's described here.",
    options=dict(a="Noble gases have very high ionization energy and don't readily lose electrons.",
                 b="Halogens (Group 17) tend to GAIN an electron (high electron affinity), not lose one.",
                 c="Correct — Group 1 alkali metals have low ionization energy and lose one electron readily.",
                 d="Group 17 (halogens) tends to gain electrons, not lose one, contradicting the description.")
),
8214: dict(
    short="Complete electron transfer between atoms forms an ionic bond.",
    long="An ionic bond forms when one atom (typically a metal) completely transfers one or more electrons to another atom (typically a nonmetal), creating oppositely charged ions that attract each other electrostatically.",
    trick="Covalent bonds involve SHARING electrons, not complete transfer — make sure 'transfer' vs 'sharing' language matches ionic vs covalent bonding respectively.",
    options=dict(a="Metallic bonding involves a 'sea' of delocalized electrons among metal atoms, not simple transfer between two atoms.",
                 b="Hydrogen bonds are weak intermolecular attractions, not a complete electron-transfer bond.",
                 c="Covalent bonds involve SHARING electrons, not complete transfer.",
                 d="Correct — complete electron transfer between atoms defines an ionic bond.")
),
8215: dict(
    short="Four bonding pairs, no lone pairs (like CH4) gives a tetrahedral geometry.",
    long="According to VSEPR theory, four electron domains (all bonding pairs, no lone pairs) around a central atom arrange themselves as far apart as possible in 3D space, forming a tetrahedral geometry with ~109.5° bond angles — the classic CH4 shape.",
    trick="Lone pairs would distort this geometry (e.g., bent for 2 bonding pairs + 2 lone pairs, as in water) — but with ZERO lone pairs and 4 bonding pairs, it's simply tetrahedral.",
    options=dict(a="Bent geometry arises with lone pairs present (like in water), not with four bonding pairs and none.",
                 b="Trigonal planar arises from three bonding domains, not four.",
                 c="Correct — four bonding pairs with no lone pairs gives tetrahedral geometry.",
                 d="Linear geometry arises from two bonding domains (or two bonding + no lone pairs), not four.")
),
8216: dict(
    short="CO2's linear geometry makes the two C=O bond dipoles cancel, giving a nonpolar molecule.",
    long="Even though each individual C=O bond is polar (oxygen more electronegative), CO2's linear molecular geometry places the two bond dipoles exactly opposite each other, so they cancel out vectorially, making the overall molecule nonpolar.",
    trick="A molecule can have polar bonds yet be nonpolar overall if its geometry causes the bond dipoles to cancel — always check the molecular shape, not just bond polarity, when determining overall molecular polarity.",
    options=dict(a="Correct — the linear shape causes the two bond dipoles to cancel out.",
                 b="Carbon and oxygen actually have quite different electronegativities; that's why each individual C=O bond IS polar.",
                 c="CO2 does contain polar bonds (C=O); the nonpolarity comes from geometry, not an absence of polar bonds.",
                 d="CO2 is actually linear, not bent — a bent shape (like water) would NOT cancel the dipoles.")
),
8217: dict(
    short="Covalent network solids (like diamond) have very high melting points and hardness.",
    long="In a covalent network solid, every atom is joined to its neighbors via strong covalent bonds throughout a continuous 3D network (as in diamond's carbon lattice), requiring enormous energy to break, resulting in very high melting points and hardness.",
    trick="Diamond is famously an electrical INSULATOR (not conductor) since all electrons are tied up in localized covalent bonds — don't assume high melting point implies high conductivity.",
    options=dict(a="Diamond has a very HIGH melting point, and it's an electrical insulator, not a conductor.",
                 b="Correct — covalent network solids have very high melting points and hardness due to the strong bonded network.",
                 c="Diamond is a solid at room temperature, not a liquid.",
                 d="Covalent network solids are known for excellent thermal STABILITY, not poor stability.")
),
8218: dict(
    short="H-bonds form between H (on N/O/F) and a lone pair on a nearby electronegative atom.",
    long="A hydrogen bond is a special, relatively strong intermolecular attraction that occurs when a hydrogen atom is covalently bonded to a highly electronegative atom (N, O, or F), creating a partial positive charge on H that then attracts a lone pair on a nearby electronegative atom.",
    trick="Hydrogen bonding requires BOTH the specific N/O/F-H bond AND a nearby electronegative atom with a lone pair — a hydrogen bonded to carbon (in a nonpolar molecule) doesn't qualify.",
    options=dict(a="Hydrogen bonded to another hydrogen (H-H) has no significant electronegativity difference to create hydrogen bonding.",
                 b="Noble gases don't typically form covalent bonds with hydrogen in this context.",
                 c="A hydrogen on a nonpolar carbon (C-H in a nonpolar molecule) isn't electronegative enough to hydrogen-bond.",
                 d="Correct — H bonded to N/O/F, attracted to a lone pair on a nearby electronegative atom, defines hydrogen bonding.")
),
8219: dict(
    short="A liquid has definite volume but takes the shape of its container.",
    long="Liquids have a fixed volume (molecules are closely packed, incompressible) but flow to take the shape of whatever container holds them, unlike solids (fixed shape AND volume) or gases (neither fixed shape nor volume).",
    trick="Don't confuse this with a gas (no fixed volume OR shape) or a solid (fixed shape AND volume) — the specific combo of 'fixed volume, variable shape' points uniquely to liquid.",
    options=dict(a="A gas has neither fixed volume nor fixed shape.",
                 b="Plasma is a highly energetic ionized gas-like state, without a definite volume.",
                 c="A solid has BOTH definite shape and volume, not just definite volume with variable shape.",
                 d="Correct — a liquid has definite volume but conforms to its container's shape.")
),
8220: dict(
    short="Boyle's law: P1V1 = P2V2 -> (3)(6) = (2)(V2), so V2 = 9.0 L.",
    long="At constant temperature, Boyle's Law states P1V1 = P2V2. Here, 3.0 atm × 6.0 L = 2.0 atm × V2, so V2 = 18/2 = 9.0 L.",
    trick="Make sure to keep units consistent and correctly identify which value is unknown — a common error is inverting the ratio (multiplying instead of dividing).",
    options=dict(a="12 L would result from an incorrect calculation, not matching P1V1=P2V2.",
                 b="2.0 L doesn't satisfy P1V1=P2V2 with these given values.",
                 c="4.0 L doesn't satisfy the Boyle's law equation here.",
                 d="Correct — 3.0×6.0 = 2.0×V2 gives V2 = 9.0 L.")
),
8221: dict(
    short="Combined gas law: P1V1/T1 = P2V2/T2 -> V2 = 16 L.",
    long="Using the combined gas law: (2 atm × 4 L)/250 K = (1 atm × V2)/500 K. Cross-multiplying: 8/250 = V2/500, so V2 = 8 × 500/250 = 16 L.",
    trick="Always use absolute temperature (Kelvin) in gas law calculations, and carefully track which quantities change together.",
    options=dict(a="4 L would imply no change at all, ignoring the pressure/temperature changes.",
                 b="8 L doesn't correctly balance both the pressure decrease and temperature increase together.",
                 c="Correct — applying the combined gas law correctly gives V2 = 16 L.",
                 d="2 L would result from an inverted or miscalculated ratio.")
),
8222: dict(
    short="NaCl molar mass ≈ 23 (Na) + 35.5 (Cl) = 58.5 g/mol.",
    long="Sodium's atomic mass is approximately 23 g/mol, and chlorine's is approximately 35.5 g/mol. Adding these for the ionic compound NaCl gives a molar mass of about 58.5 g/mol.",
    trick="Don't just use one element's atomic mass alone (23 or 35.5) — you must add BOTH elements' contributions for the compound's molar mass.",
    options=dict(a="78 g/mol doesn't match the sum of Na and Cl atomic masses.",
                 b="Correct — 23 (Na) + 35.5 (Cl) = 58.5 g/mol.",
                 c="35.5 g/mol is just chlorine's atomic mass alone, not the full compound.",
                 d="23 g/mol is just sodium's atomic mass alone, not the full compound.")
),
8223: dict(
    short="Ca(NO3)2 has 6 O atoms per formula unit; 2 moles gives 12 moles of O atoms.",
    long="Each NO3- ion has 3 oxygen atoms, and Ca(NO3)2 has 2 nitrate ions, so 1 formula unit has 3×2=6 oxygen atoms. For 2 moles of Ca(NO3)2, total oxygen = 2 × 6 = 12 moles.",
    trick="Don't forget to multiply by BOTH the number of nitrate groups per formula unit (2) AND the oxygens per nitrate (3) AND the number of moles given (2) — a triple multiplication is needed.",
    options=dict(a="4 moles undercounts; it misses one of the required multiplication steps.",
                 b="Correct — 2 mol × 2 NO3- × 3 O = 12 moles of oxygen atoms.",
                 c="2 moles vastly undercounts the oxygen atoms present.",
                 d="6 moles would be the oxygen count in just ONE mole of Ca(NO3)2, not two moles.")
),
8224: dict(
    short="Molarity = moles/volume(L) = 0.5 mol / 0.25 L = 2.0 M.",
    long="Molarity is defined as moles of solute per liter of solution. Converting 250 mL to 0.25 L, molarity = 0.5 mol / 0.25 L = 2.0 M.",
    trick="Always convert volume to liters before dividing — a common mistake is dividing by 250 (mL) directly, which would give a very different (wrong) number.",
    options=dict(a="1.0 M would result from using an incorrect volume (like 0.5 L) in the calculation.",
                 b="Correct — 0.5 mol divided by 0.25 L gives 2.0 M.",
                 c="0.25 M inverts the calculation incorrectly (dividing volume by moles instead of the reverse).",
                 d="0.5 M would just restate the moles value without proper unit conversion/division.")
),
8225: dict(
    short="N2 + 3H2 -> 2NH3: 5 mol N2 needs 5×3 = 15 mol H2 by stoichiometry.",
    long="The balanced equation shows a 1:3 mole ratio between N2 and H2. For 5 moles of N2, the required H2 is 5 × 3 = 15 moles.",
    trick="Always use the balanced equation's mole ratio directly — don't just multiply by the wrong coefficient or forget to scale by the given amount of N2.",
    options=dict(a="10 moles doesn't match the 1:3 ratio scaled to 5 moles of N2.",
                 b="Correct — 5 × 3 = 15 moles of H2 needed, from the 1:3 N2:H2 ratio.",
                 c="20 moles overshoots the correct stoichiometric ratio.",
                 d="5 moles would be a 1:1 ratio, but the balanced equation requires a 1:3 ratio.")
),
8226: dict(
    short="Exothermic reactions release energy, so products have LOWER energy than reactants.",
    long="In an exothermic reaction, energy is released to the surroundings (often as heat), meaning the products end up at a lower energy state than the reactants — the difference in energy is what's released.",
    trick="Don't confuse 'exothermic releases energy' with 'products have higher energy' — releasing energy means the products end up LOWER in energy, not higher.",
    options=dict(a="A zero energy difference would mean no reaction occurred (not exothermic).",
                 b="Correct — exothermic reactions release energy, leaving products at lower energy than reactants.",
                 c="Higher product energy would describe an endothermic reaction, the opposite case.",
                 d="If energy were the same, no net energy would be released, contradicting 'exothermic.'")
),
8227: dict(
    short="Hess's law: sum the enthalpy changes: -100 + (-50) = -150 kJ.",
    long="Hess's law states that the overall enthalpy change for a reaction is the sum of the enthalpy changes of the individual steps, regardless of pathway. Here, -100 kJ (releasing) + -50 kJ (releasing) = -150 kJ overall.",
    trick="'Releases 100 kJ' means ΔH = -100 kJ (exothermic, negative sign) — don't accidentally use positive values for energy-releasing steps.",
    options=dict(a="+150 kJ would incorrectly treat both steps as endothermic (positive), when both actually release energy.",
                 b="Correct — summing -100 kJ and -50 kJ (both exothermic, releasing energy) gives -150 kJ overall.",
                 c="-50 kJ only accounts for one of the two steps, not their sum.",
                 d="+50 kJ has both an incorrect sign and an incomplete sum of the two steps.")
),
8228: dict(
    short="Increasing pressure shifts equilibrium toward the side with fewer gas moles (products, 2 mol).",
    long="For 2SO2(g) + O2(g) <-> 2SO3(g), the reactant side has 3 total moles of gas (2 SO2 + 1 O2) while the product side has 2 moles (2 SO3). Increasing pressure (decreasing volume) shifts equilibrium toward the side with fewer gas moles — the products — per Le Chatelier's principle.",
    trick="Count total gas moles on each side carefully (3 vs 2) — the equilibrium shift always favors the side with FEWER moles of gas when pressure increases.",
    options=dict(a="Increasing pressure shifts equilibrium toward products, not toward completely depleting reactants (which would require going to completion, not equilibrium shift).",
                 b="The reactant side actually has MORE gas moles (3), so pressure increase favors the other side, not this one.",
                 c="Correct — the product side (2 moles gas, fewer) is favored when pressure increases.",
                 d="Le Chatelier's principle predicts a definite shift with unequal mole counts on each side, not 'no shift.'")
),
8229: dict(
    short="Decreasing temperature for an exothermic reaction shifts equilibrium toward products.",
    long="For an exothermic reaction, heat can be treated as a product. Lowering temperature (removing heat/'product') shifts the equilibrium forward toward the products, per Le Chatelier's principle, increasing yield.",
    trick="This is opposite for endothermic reactions (where lowering temperature shifts toward reactants) — always identify whether the reaction is exo- or endothermic before predicting the temperature-shift direction.",
    options=dict(a="Correct — for an exothermic reaction, lower temperature favors the forward (product-forming) direction.",
                 b="This is the effect for an ENDOTHERMIC reaction, not an exothermic one.",
                 c="Temperature changes do shift equilibrium for reactions involving heat release/absorption; 'not at all' is incorrect.",
                 d="Decreasing temperature doesn't stop the reaction entirely; it shifts equilibrium position.")
),
8230: dict(
    short="Higher concentration increases collision frequency, raising effective-collision rate.",
    long="According to collision theory, increasing reactant concentration increases the number of reactant particles per unit volume, leading to more frequent collisions and, correspondingly, more successful (effective) collisions per unit time, raising the reaction rate.",
    trick="Concentration doesn't lower the activation energy (that's what a catalyst does) — it simply increases how often molecules meet, raising the chance of reaching that same activation energy via more frequent collisions.",
    options=dict(a="Higher concentration means MORE, not less frequent collisions.",
                 b="Correct — more frequent collisions from higher concentration raise the reaction rate.",
                 c="Concentration changes don't alter activation energy; only a catalyst does that.",
                 d="Increasing concentration doesn't make a reaction non-spontaneous; spontaneity relates to thermodynamics, not kinetics.")
),
8231: dict(
    short="A catalyst speeds up reaching equilibrium without shifting its position.",
    long="A catalyst provides an alternate reaction pathway with lower activation energy, speeding up both the forward and reverse reactions equally. This means equilibrium is reached faster, but the equilibrium position (concentrations at equilibrium) is unchanged.",
    trick="A catalyst affects RATE (kinetics), not the equilibrium POSITION (thermodynamics/K value) — a very commonly tested distinction.",
    options=dict(a="A catalyst DOES affect reaction rate — that's its primary defined function.",
                 b="A catalyst does not shift equilibrium toward products; it accelerates both directions equally.",
                 c="Correct — a catalyst speeds up reaching equilibrium without changing its final position.",
                 d="A catalyst does not shift equilibrium toward reactants either; the position stays the same.")
),
8232: dict(
    short="Reduction (gain of electrons) always occurs at the cathode.",
    long="In electrochemistry (both electrolytic and galvanic cells), by convention, reduction always occurs at the cathode (gain of electrons) and oxidation always occurs at the anode (loss of electrons) — remembered by 'RedCat, AnOx.'",
    trick="This rule holds for BOTH galvanic and electrolytic cells even though which electrode is + or - flips between the two cell types — always tie reduction to 'cathode' regardless of cell type.",
    options=dict(a="The salt bridge maintains ionic balance/charge neutrality; it isn't where reduction occurs.",
                 b="Correct — reduction (gain of electrons) always occurs at the cathode.",
                 c="Oxidation (loss of electrons), not reduction, occurs at the anode.",
                 d="The external wire simply carries electron flow between electrodes; it isn't itself an electrode where reduction happens.")
),
8233: dict(
    short="Mg loses electrons (is oxidized) reacting with HCl: Mg -> Mg2+ + 2e-.",
    long="In Mg(s) + 2HCl(aq) -> MgCl2(aq) + H2(g), magnesium goes from a neutral 0 oxidation state to +2 in MgCl2, meaning it loses 2 electrons — it is oxidized. (Correspondingly, H+ is reduced to H2 gas.)",
    trick="The metal reacting with acid is oxidized (loses electrons) while the H+ ions are reduced (to H2 gas) — a classic single-displacement redox reaction.",
    options=dict(a="Magnesium's oxidation state clearly changes (0 to +2), so it is NOT unchanged.",
                 b="A catalyst is consumed/unchanged and speeds reactions; Mg is a reactant that's chemically transformed here.",
                 c="Magnesium loses electrons (oxidation), the opposite of being reduced.",
                 d="Correct — magnesium is oxidized, going from 0 to +2 oxidation state by losing 2 electrons.")
),
8234: dict(
    short="pH 12 is strongly basic (well above the neutral pH of 7).",
    long="The pH scale runs 0-14, with 7 being neutral. A pH of 12 is significantly above 7, in the strongly basic (alkaline) range.",
    trick="Higher pH = more basic, lower pH = more acidic — pH 12 is far from neutral (7) on the basic side, so 'weakly acidic' or 'neutral' are both clearly wrong.",
    options=dict(a="pH 12 is far too high (basic) to be described as weakly acidic.",
                 b="Correct — a pH of 12 is strongly basic.",
                 c="Neutral would be pH 7; pH 12 is well above that, in the basic range.",
                 d="pH 12 is basic, the opposite of acidic; 'strongly acidic' would be a very low pH (like 1-2).")
),
8235: dict(
    short="Arrhenius acid: increases [H+] in aqueous solution.",
    long="The Arrhenius definition specifically states that an acid is a substance that, when dissolved in water, increases the concentration of hydrogen ions (H+) in solution.",
    trick="An Arrhenius BASE increases [OH-], and accepting protons/donating electron pairs describe Brønsted-Lowry and Lewis definitions respectively — make sure to match the correct theory to the correct definition when asked specifically about 'Arrhenius.'",
    options=dict(a="Increasing OH- concentration describes an Arrhenius BASE, not an acid.",
                 b="Accepting protons describes a Brønsted-Lowry base, not an Arrhenius acid.",
                 c="Donating electron pairs describes a Lewis base, not an Arrhenius acid.",
                 d="Correct — the Arrhenius definition of an acid is increasing [H+] in aqueous solution.")
),
8236: dict(
    short="A buffer resists pH change by containing a weak acid/base pair with its conjugate.",
    long="A buffer solution contains significant amounts of both a weak acid and its conjugate base (or a weak base and its conjugate acid). This allows it to neutralize small additions of either strong acid or strong base, minimizing pH change.",
    trick="Pure water or a solution of only a strong acid has NO buffering capacity — the defining feature of a buffer is having BOTH members of a weak conjugate acid-base pair present together.",
    options=dict(a="Correct — a weak acid/conjugate base pair (or weak base/conjugate acid) is what gives buffering capacity.",
                 b="Pure water has essentially no buffering capacity against pH changes.",
                 c="A buffer specifically needs dissociable ions (the conjugate pair) to function.",
                 d="A strong acid alone, with no conjugate base reserve, cannot buffer against added base effectively.")
),
8237: dict(
    short="Acetic acid neutralizes added strong base, keeping pH nearly stable.",
    long="In an acetic acid/sodium acetate buffer, adding a small amount of strong base is neutralized by the weak acid component (acetic acid reacts with OH- to form acetate and water), preventing a large pH swing.",
    trick="It's the ACID component of the buffer pair that reacts with added BASE (and the conjugate BASE component that reacts with added acid) — match the right buffer component to the right added species.",
    options=dict(a="A buffer specifically DOES have capacity to resist pH change — that's its defining property.",
                 b="The pH does NOT rise sharply in a properly functioning buffer; that's the whole point of buffering.",
                 c="Correct — the acetic acid component reacts with (neutralizes) the added base.",
                 d="It's the acid (acetic acid), not the conjugate base (sodium acetate), that neutralizes added base.")
),
8238: dict(
    short="-COOH is the carboxylic acid functional group.",
    long="The carboxyl group (-COOH), combining a carbonyl (C=O) and hydroxyl (-OH) on the same carbon, is the defining functional group of carboxylic acids (e.g., acetic acid, CH3COOH).",
    trick="Don't confuse -COOH (carboxylic acid) with a plain -OH (alcohol) or a plain C=O (aldehyde/ketone) — the carboxyl group combines both features together into one distinct functional group.",
    options=dict(a="Amines are characterized by an -NH2 (or substituted nitrogen) group, not -COOH.",
                 b="Aldehydes have a terminal C=O with an H attached, not the full -COOH combination.",
                 c="Correct — the -COOH group specifically defines carboxylic acids.",
                 d="Alcohols are characterized by a plain -OH group, not the combined carboxyl -COOH.")
),
8239: dict(
    short="Alkenes undergo addition reactions across their C=C double bond.",
    long="Alkenes readily undergo addition reactions, where atoms (like H2, X2, or HX) add across the double bond, converting it to a single bond — this reflects the double bond's relatively high reactivity compared to single bonds.",
    trick="Alkanes (saturated, single bonds only) undergo substitution reactions instead, since they have no double bond to add across — match reaction type to the specific functional group/bond type involved.",
    options=dict(a="Substitution reactions are more typical of saturated alkanes, not alkenes' characteristic reaction.",
                 b="Correct — addition reactions across the C=C double bond are the hallmark reaction of alkenes.",
                 c="Elimination reactions typically FORM double bonds (e.g., from alcohols or haloalkanes), the reverse of addition.",
                 d="Condensation reactions involve joining two molecules with loss of a small molecule (like water), a different reaction class.")
),
8240: dict(
    short="A tertiary alcohol's -OH carbon is bonded to 3 other carbons.",
    long="Alcohols are classified by how many carbon atoms are attached to the carbon bearing the -OH group: primary (1 carbon), secondary (2 carbons), tertiary (3 carbons).",
    trick="Don't confuse this classification scheme with primary/secondary/tertiary amines (which count nitrogen-attached carbons differently) — for alcohols, it's specifically about the -OH-bearing carbon's OTHER carbon attachments.",
    options=dict(a="One carbon attachment would define a primary alcohol, not tertiary.",
                 b="Two carbon attachments would define a secondary alcohol, not tertiary.",
                 c="Correct — three carbon attachments define a tertiary alcohol.",
                 d="Zero carbon attachments would mean it's just methanol, with no classification as tertiary.")
),
8241: dict(
    short="SN2 is a one-step concerted reaction with simultaneous nucleophile attack and leaving-group departure.",
    long="In an SN2 (bimolecular nucleophilic substitution) mechanism, the nucleophile attacks the electrophilic carbon from the opposite side of the leaving group in a single, concerted step, with bond-breaking and bond-forming happening simultaneously (inverting stereochemistry, like an umbrella flipping inside out).",
    trick="SN1 (not SN2) proceeds through a two-step mechanism with a carbocation intermediate — don't mix up the number of steps and reaction order between the two substitution mechanisms.",
    options=dict(a="A two-step mechanism through a carbocation intermediate describes SN1, not SN2.",
                 b="Correct — SN2 is a single concerted step with simultaneous attack and departure.",
                 c="SN2 does involve a leaving group being displaced; it's the same-carbon attack of the nucleophile that's distinct.",
                 d="SN2 mechanisms occur at aliphatic (sp3) carbons, not exclusively in aromatic systems.")
),
8242: dict(
    short="Amide formation from carboxylic acid + amine releases water.",
    long="When a carboxylic acid reacts with an amine in a condensation reaction, the -OH of the acid and an H from the amine's -NH combine to form water, while the remaining fragments join to form the amide bond.",
    trick="This is a classic condensation reaction — recognize the general pattern of two molecules joining with loss of a small molecule (here, water), similar to ester or peptide bond formation.",
    options=dict(a="Correct — water is released as the condensation byproduct when amides form.",
                 b="Ammonia isn't the typical byproduct of this specific condensation (it would be if excess amine reacted differently).",
                 c="Hydrogen gas isn't released in this type of condensation reaction.",
                 d="Carbon dioxide isn't the byproduct here (that would be more typical of a decarboxylation reaction).")
),
8243: dict(
    short="A carbonyl at the chain end with an attached H characterizes an aldehyde.",
    long="Aldehydes have the general structure R-CHO: a carbonyl group (C=O) located at the terminal position of the carbon chain, with a hydrogen atom also attached to that same carbon.",
    trick="Ketones ALSO have a C=O, but positioned WITHIN the chain (between two carbon groups, not terminal with an H) — the terminal position + attached H is what specifically distinguishes an aldehyde.",
    options=dict(a="Correct — a terminal carbonyl bonded to at least one H defines an aldehyde.",
                 b="A carboxylic acid needs the full -COOH (carbonyl PLUS hydroxyl), not just a plain terminal carbonyl.",
                 c="Ethers have a C-O-C linkage, with no carbonyl group at all.",
                 d="A ketone's carbonyl is located WITHIN the chain (between two carbons), not at a terminal position with an H.")
),
8244: dict(
    short="Noble gases are unreactive due to their stable, complete valence shell.",
    long="Group 18 (noble gases) have a full valence electron shell (an octet, or duet for helium), making them exceptionally stable and generally unreactive, since they have little tendency to gain, lose, or share electrons.",
    trick="Don't confuse 'stable full valence shell' (the real reason for unreactivity) with unrelated factors like atomic size or nuclear charge, which don't by themselves explain noble gas inertness.",
    options=dict(a="Noble gases are notably UNREACTIVE, so a tendency to readily form ionic bonds is the opposite of their behavior.",
                 b="Atomic size alone doesn't explain unreactivity; it's the complete valence configuration that matters.",
                 c="Correct — a stable, complete valence electron configuration explains noble gas unreactivity.",
                 d="Noble gases don't have unusually low nuclear charge; their inertness comes from valence shell stability, not nuclear charge.")
),
8245: dict(
    short="Group 2 metals are less reactive with water than Group 1 due to higher ionization energy.",
    long="Alkaline earth metals (Group 2) have a higher nuclear charge (more protons) than the alkali metal in the same period, holding their two valence electrons more tightly (higher ionization energy), making them somewhat less reactive with water than Group 1 metals.",
    trick="Larger atomic radius alone doesn't determine reactivity trend here — Group 2 atoms are actually SMALLER than the Group 1 element in the same period (more protons pull electrons closer), which is directly tied to their higher ionization energy.",
    options=dict(a="Group 2 elements actually have SMALLER atomic radii than the same-period Group 1 element, not larger.",
                 b="Correct — higher ionization energy (tighter-held valence electrons) makes Group 2 less reactive than Group 1.",
                 c="Group 2 elements have HIGHER, not lower, ionization energy compared to same-period Group 1.",
                 d="Group 2 metals do react with water (though less vigorously than Group 1), so 'not at all' is incorrect.")
),
8246: dict(
    short="Cu goes from +2 (in CuO) to 0 (as Cu metal) — reduction.",
    long="In CuO + H2 -> Cu + H2O, copper starts as Cu2+ (in CuO) and ends as elemental Cu (oxidation state 0), a decrease in oxidation state — this is reduction (gain of electrons). Correspondingly, hydrogen is oxidized (0 to +1).",
    trick="Copper's oxidation state DECREASES here (reduction), while hydrogen's INCREASES (oxidation) — make sure you're tracking the correct element's oxidation state change as asked.",
    options=dict(a="This reverses the direction; copper goes FROM +2 TO 0, not the other way around.",
                 b="Correct — copper's oxidation state decreases from +2 to 0, which is reduction.",
                 c="+1 to +2 doesn't match copper's actual oxidation states in CuO (+2) and Cu metal (0).",
                 d="Copper's oxidation state clearly changes (from +2 to 0); 'no change' is incorrect.")
),
8247: dict(
    short="A solute disrupts the solvent's ordered solid lattice, lowering the freezing point.",
    long="Freezing point depression is a colligative property: dissolved solute particles interfere with the solvent molecules' ability to arrange into an ordered crystalline (solid) lattice, so a lower temperature is needed to achieve freezing compared to the pure solvent.",
    trick="This is a colligative property — it depends on the NUMBER of solute particles, not their chemical identity — and it LOWERS (not raises) the freezing point.",
    options=dict(a="A non-volatile solute clearly does affect the freezing point (that's the entire phenomenon described).",
                 b="Freezing point depression is specifically about lattice disruption, not primarily a viscosity effect.",
                 c="Correct — disrupting the ordered lattice formation is why the solute lowers the freezing point.",
                 d="The solute LOWERS the freezing point, it does not increase it.")
),
8248: dict(
    short="Cooling a saturated solution at fixed concentration makes it supersaturated; excess solute precipitates.",
    long="Since solubility of this solid solute increases with temperature, a solution saturated at a high temperature holds more dissolved solute than the (lower) solubility limit at a cooler temperature. Cooling it while keeping the same concentration pushes it above the new (lower) solubility curve value — supersaturated — and the excess solute tends to crystallize/precipitate out until the solution is once again just saturated at the new temperature.",
    trick="Don't assume cooling just makes it 'unsaturated' — since solubility DROPS as temperature drops (for this typical solid), holding the same concentration while cooling actually pushes the solution ABOVE the (now lower) saturation limit.",
    options=dict(a="Cooling would need to REDUCE concentration to become unsaturated; here concentration is held constant while the solubility limit itself drops, so it becomes supersaturated, not unsaturated.",
                 b="Correct — cooling while holding concentration constant pushes it above the (now lower) solubility limit, causing excess solute to precipitate as it re-saturates.",
                 c="Cooling doesn't dilute anything by itself; the amount of solute and solvent doesn't change.",
                 d="The solution IS affected — since solubility depends on temperature, cooling definitely changes its saturation state.")
),
8249: dict(
    short="Greenhouse gas buildup (CO2, methane) causes global warming via the enhanced greenhouse effect.",
    long="Greenhouse gases like CO2 and methane trap outgoing infrared radiation in the atmosphere, and their increasing concentration enhances this natural greenhouse effect, leading to a gradual rise in global average temperatures — global warming.",
    trick="Don't confuse the greenhouse effect/global warming with ozone depletion (a separate issue, mainly caused by CFCs) or acid rain (mainly caused by SO2/NOx) — each environmental problem has its own specific primary cause.",
    options=dict(a="Greenhouse gases don't directly decrease atmospheric pressure; that's not their documented primary effect.",
                 b="Ozone depletion is mainly caused by CFCs, a separate issue from the general greenhouse effect described here.",
                 c="Correct — CO2/methane buildup enhances the greenhouse effect, driving global warming.",
                 d="Acid rain is mainly caused by SO2/NOx emissions, not specifically CO2/methane buildup.")
),
8250: dict(
    short="Shifting to renewables and reducing fossil fuel use most directly reduces atmospheric CO2 buildup.",
    long="Since fossil fuel combustion is a major source of atmospheric CO2, transitioning to renewable energy sources (solar, wind, hydro) and burning less fossil fuel directly reduces new CO2 emissions entering the atmosphere.",
    trick="Deforestation and increasing fossil fuel use/subsidies would WORSEN CO2 buildup, not reduce it — watch for these clearly counterproductive distractors.",
    options=dict(a="Deforestation reduces the number of trees absorbing CO2, worsening the problem, not helping.",
                 b="Correct — renewable energy adoption and reduced fossil fuel combustion directly cuts CO2 emissions.",
                 c="Removing carbon capture technology would worsen, not help, CO2 buildup.",
                 d="Increasing fossil fuel subsidies would encourage more fossil fuel use, worsening CO2 emissions.")
),
}

def main():
    root = Path(__file__).parent.parent
    out = []
    for qid, e in EXPL.items():
        out.append({"id": qid, "short": e["short"], "long": e["long"], "trick": e["trick"], "options": e["options"]})
    out_path = root / "scripts" / "mock19_explanations_chemistry.json"
    out_path.write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Wrote {len(out)} explanations to {out_path}")

if __name__ == "__main__":
    main()
