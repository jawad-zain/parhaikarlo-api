import json
from pathlib import Path

EXPL = {
8386: dict(
    short="Protons carry a positive electric charge.",
    long="Protons are subatomic particles found in the nucleus that carry a positive (+1) electric charge, balancing the negative charge of electrons in a neutral atom.",
    trick="Don't confuse protons (positive) with electrons (negative) or neutrons (no charge) — this is one of the most basic atomic structure facts.",
    options=dict(a="Negative charge describes electrons, not protons.",
                 b="Correct — protons carry positive charge.",
                 c="Neutral (no charge) describes neutrons, not protons.",
                 d="Proton charge is fixed (+1), not variable.")
),
8387: dict(
    short="Neutrons = mass number - atomic number = 14 - 6 = 8.",
    long="Carbon-14 has a mass number of 14 and an atomic number (proton count) of 6. Neutrons = mass number − atomic number = 14 − 6 = 8.",
    trick="Don't confuse mass number (protons+neutrons) with atomic number (protons only) — subtract the two correctly to isolate the neutron count.",
    options=dict(a="6 is the atomic number (proton count), not the neutron count.",
                 b="14 is the mass number itself, not the neutron count alone.",
                 c="Correct — 14-6=8 neutrons.",
                 d="20 would come from adding instead of subtracting (14+6).")
),
8388: dict(
    short="Mg (Z=12): 1s2 2s2 2p6 3s2 is the correct ground-state electron configuration.",
    long="Magnesium has 12 electrons, filling in order: 1s2(2) 2s2(2) 2p6(6) 3s2(2) = 2+2+6+2 = 12 electrons total, matching the Aufbau principle.",
    trick="Check that the total electron count in a configuration sums to the atomic number — options with only 11 or 13 electrons total are immediately wrong regardless of orbital order.",
    options=dict(a="This configuration has 2p5 (only 5 electrons in 2p, should be full at 6) and totals only 11 electrons — one short.",
                 b="This has only 2p6 then 3s1 — totaling 11 electrons, one short of magnesium's 12.",
                 c="This adds an extra 3p1 electron, totaling 13 — one too many for magnesium.",
                 d="Correct — 1s2 2s2 2p6 3s2 sums to exactly 12 electrons, matching Mg's atomic number.")
),
8389: dict(
    short="Charge = protons - electrons = 8 - 10 = -2.",
    long="An ion's charge equals the number of protons minus the number of electrons. With 8 protons and 10 electrons: charge = 8 - 10 = -2.",
    trick="More electrons than protons always gives a NEGATIVE ion (anion) — don't flip the subtraction order, which would incorrectly give a positive result.",
    options=dict(a="Correct — 8 protons minus 10 electrons gives a -2 charge.",
                 b="+2 would result from reversing the subtraction (10-8) but with the wrong sign for this case.",
                 c="+8 mistakes the proton count itself for the ion's charge.",
                 d="-10 mistakes the electron count itself for the ion's charge.")
),
8390: dict(
    short="The atomic number equals the number of protons in the nucleus.",
    long="By definition, an element's atomic number is the count of protons in the nucleus of its atoms — this uniquely identifies the element.",
    trick="Mass number (total nucleons = protons+neutrons) is a different quantity from atomic number — don't confuse the two.",
    options=dict(a="Outermost-shell electrons relate to valence electrons/group number, not atomic number.",
                 b="Correct — atomic number = number of protons in the nucleus.",
                 c="Total nucleons (protons+neutrons) is the mass number, not the atomic number.",
                 d="Neutron count alone is not the atomic number; it's part of the mass number.")
),
8391: dict(
    short="Elements in the same periodic-table group share the same number of valence electrons.",
    long="Elements in a group (vertical column) have the same number of valence (outermost-shell) electrons, which is why they show similar chemical properties and bonding behavior.",
    trick="Atomic mass and number of energy levels (shells) both vary DOWN a group — only the valence electron count stays consistent within a group.",
    options=dict(a="Atomic mass increases down a group; it isn't shared/similar.",
                 b="Neutron count varies between elements even within the same group.",
                 c="Correct — same-group elements share the same number of valence electrons.",
                 d="The number of energy levels (shells) increases down a group, so it's not shared.")
),
8392: dict(
    short="Electronegativity decreases down a group as atomic radius increases and nuclear pull on bonding electrons weakens.",
    long="Down a group, additional electron shells increase atomic radius and add shielding, weakening the nucleus's pull on the outer (bonding) electrons — so electronegativity decreases going down a group.",
    trick="This is opposite to the trend ACROSS a period (where electronegativity increases left to right) — make sure you know which direction (group vs period) is being asked about.",
    options=dict(a="Electronegativity does not increase down a group; it decreases.",
                 b="Electronegativity is a relative scale value, not literally a 'negative' charge value.",
                 c="Electronegativity is not constant down a group; it changes noticeably.",
                 d="Correct — electronegativity decreases down a group as atomic radius grows and nuclear attraction weakens.")
),
8393: dict(
    short="Small, highly electronegative nonmetals (upper right of the periodic table) tend to gain electrons to form anions.",
    long="Elements with small atomic radius and high electronegativity (like nonmetals near fluorine/oxygen, excluding noble gases) have a strong pull for additional electrons, readily gaining them to achieve a stable octet and forming negatively charged anions.",
    trick="Don't confuse this behavior with metals (large radius, low electronegativity), which instead readily LOSE electrons to form cations — the two trends are opposite ends of the periodic table.",
    options=dict(a="Correct — such elements readily gain electrons to form anions.",
                 b="Losing electrons to form cations is typical of metals (large radius, low electronegativity), not this description.",
                 c="Such elements are typically quite reactive, readily forming bonds, not avoiding them.",
                 d="These elements very much do form compounds/ions; they don't remain inert like noble gases.")
),
8394: dict(
    short="Unequal electron sharing due to an electronegativity difference defines a polar covalent bond.",
    long="A polar covalent bond forms when two bonded atoms share electrons unequally because one atom is more electronegative than the other, creating partial positive and negative charges (a dipole).",
    trick="A NONpolar covalent bond has EQUAL sharing (same or very similar electronegativity), while an ionic bond involves a full electron transfer, not sharing — polar covalent sits between these two extremes.",
    options=dict(a="A nonpolar covalent bond has EQUAL sharing, the opposite of what's described.",
                 b="Correct — unequal sharing due to electronegativity difference defines a polar covalent bond.",
                 c="An ionic bond involves electron TRANSFER, not sharing at all.",
                 d="A metallic bond involves a 'sea of electrons' among metal atoms, unrelated to this unequal-sharing description.")
),
8395: dict(
    short="Two bonding pairs + two lone pairs on the central atom gives a bent (angular) shape, as in water.",
    long="VSEPR theory: with 4 total electron domains (2 bonding, 2 lone pairs) arranged tetrahedrally, but only the 2 bonded atoms define the observed molecular shape — which comes out bent (angular), as seen in H2O.",
    trick="Don't confuse the underlying ELECTRON geometry (tetrahedral, counting lone pairs) with the observed MOLECULAR geometry (bent, based only on atom positions) — lone pairs affect shape but aren't 'seen' in the final geometry name.",
    options=dict(a="Linear geometry would occur with no lone pairs and 2 bonding pairs (like CO2), not this case.",
                 b="Tetrahedral describes the electron-domain geometry (or a molecule with 4 bonding pairs, 0 lone pairs, like CH4), not the molecular shape here.",
                 c="Correct — with 2 bonding + 2 lone pairs, the molecular shape is bent (angular), as in water.",
                 d="Trigonal pyramidal occurs with 3 bonding pairs and 1 lone pair (like NH3), not 2 and 2.")
),
8396: dict(
    short="NH3's trigonal pyramidal shape prevents the individual bond dipoles from canceling, making it polar overall.",
    long="Ammonia has 3 N-H polar bonds plus a lone pair on nitrogen, giving it a trigonal pyramidal (not symmetric) shape. Because the shape is asymmetric, the individual bond dipole moments don't cancel out, leaving a net molecular dipole (polar molecule).",
    trick="A molecule can have polar BONDS but still be nonpolar overall if its geometry is symmetric enough for the dipoles to cancel (like CO2) — NH3's asymmetric pyramidal shape is why it stays polar.",
    options=dict(a="NH3 is NOT symmetrical/tetrahedral in the sense that would cancel dipoles — it's pyramidal due to the lone pair.",
                 b="Nitrogen and hydrogen do NOT have identical electronegativities; that difference is exactly what creates the bond dipoles.",
                 c="NH3 does contain polar N-H bonds due to the electronegativity difference.",
                 d="Correct — the pyramidal shape prevents the bond dipoles from canceling, keeping NH3 polar overall.")
),
8397: dict(
    short="Ionic compounds have high melting points due to strong electrostatic attraction throughout the crystal lattice.",
    long="In an ionic solid, oppositely charged ions are held together by strong electrostatic (Coulombic) forces extending throughout the entire crystal lattice, requiring a large amount of energy (high temperature) to overcome and melt.",
    trick="Don't confuse ionic bonding's strong lattice-wide attraction with the much weaker intermolecular forces (like Van der Waals) found in many molecular covalent compounds, which is why those tend to have much lower melting points.",
    options=dict(a="Correct — strong electrostatic attraction throughout the lattice explains high melting points.",
                 b="Van der Waals forces are much weaker and are NOT what holds ionic lattices together.",
                 c="Ionic compounds do contain charged particles (ions) — that's the whole basis of ionic bonding.",
                 d="Ionic bonds are actually quite strong and are NOT easily broken at room temperature (hence high melting points).")
),
8398: dict(
    short="Hydrogen bonding gives water its relatively high boiling point compared to similarly sized molecules.",
    long="Water molecules form hydrogen bonds with each other due to the highly polar O-H bonds. These extra intermolecular attractions require more energy to break, giving water an unusually high boiling point compared to similarly sized nonpolar or weakly polar molecules.",
    trick="Compare water (boiling at 100°C) to a similarly-sized nonpolar molecule like methane (boiling around -161°C) — the huge difference highlights just how significant hydrogen bonding is.",
    options=dict(a="Water is very much polar, not nonpolar — that's a prerequisite for hydrogen bonding.",
                 b="Correct — hydrogen bonding explains water's unusually high boiling point for its size.",
                 c="Water is actually an excellent solvent for many ionic compounds (the 'universal solvent'), not unable to dissolve them.",
                 d="Water actually has relatively HIGH surface tension due to hydrogen bonding, not low.")
),
8399: dict(
    short="A solid has both a fixed shape and a fixed volume.",
    long="Solids have strongly bonded, closely packed particles in fixed positions, giving them both a definite shape and a definite volume — unlike liquids (fixed volume, variable shape) or gases (variable shape and volume).",
    trick="Liquids have a fixed volume but take the shape of their container; gases have neither fixed shape nor fixed volume — only solids have both properties fixed.",
    options=dict(a="Gas has neither fixed shape nor fixed volume.",
                 b="Liquid has a fixed volume but NOT a fixed shape (it takes the container's shape).",
                 c="Correct — a solid has both a fixed shape and a fixed volume.",
                 d="Plasma, like gas, has neither a fixed shape nor a fixed volume.")
),
8400: dict(
    short="Boyle's law: P1V1=P2V2, so V2 = (1.5x10)/3.0 = 5.0 L.",
    long="At constant temperature, Boyle's law states P1V1 = P2V2. Solving for V2: V2 = P1V1/P2 = (1.5 atm x 10 L) / 3.0 atm = 15/3.0 = 5.0 L.",
    trick="Since pressure doubled (1.5 to 3.0 atm), volume must HALVE (inverse relationship) — 10 L halved is 5.0 L, a quick sanity check against the full calculation.",
    options=dict(a="20 L would result if volume increased with pressure, but Boyle's law is an inverse relationship.",
                 b="7.5 L doesn't match the correct halving relationship.",
                 c="15 L is simply P1V1, without dividing by the new pressure.",
                 d="Correct — (1.5x10)/3.0=5.0 L.")
),
8401: dict(
    short="Combined gas law: P1V1/T1 = P2V2/T2, giving V2 = 12 L.",
    long="Using the combined gas law: (P1V1)/T1 = (P2V2)/T2. Plugging in: (4x3)/200 = (2xV2)/400. So 12/200 = 2V2/400, giving 2V2 = (12/200)x400 = 24, so V2 = 12 L.",
    trick="Work through the combined gas law systematically (cross-multiply carefully) rather than trying to reason about pressure and temperature changes separately — errors often creep in when handling two variables changing at once.",
    options=dict(a="Correct — solving the combined gas law equation gives V2=12 L.",
                 b="6 L would result from an arithmetic slip in the cross-multiplication.",
                 c="3 L (unchanged) ignores that both pressure and temperature changed.",
                 d="24 L overshoots the correct answer, likely from a doubling error.")
),
8402: dict(
    short="Molar mass of glucose C6H12O6 = 6(12)+12(1)+6(16) = 72+12+96 = 180 g/mol.",
    long="Summing atomic masses: Carbon 6x12=72, Hydrogen 12x1=12, Oxygen 6x16=96. Total = 72+12+96 = 180 g/mol.",
    trick="Make sure to multiply each element's atomic mass by its correct subscript count in the formula (6, 12, and 6 respectively) before summing.",
    options=dict(a="120 g/mol would result from omitting one of the element contributions.",
                 b="Correct — 72+12+96=180 g/mol.",
                 c="342 g/mol is actually the molar mass of sucrose (C12H22O11), not glucose.",
                 d="90 g/mol is roughly half the correct value, suggesting a halving error somewhere.")
),
8403: dict(
    short="NH3 has 3 hydrogen atoms; 4 moles of NH3 contain 4x3=12 moles of H atoms.",
    long="Each molecule of NH3 (ammonia) contains 1 nitrogen and 3 hydrogen atoms. In 4 moles of NH3, there are 4 x 3 = 12 moles of hydrogen atoms.",
    trick="Multiply the number of moles of the compound by the SUBSCRIPT of the atom in question (3 for H in NH3) — don't just restate the mole count of the compound itself.",
    options=dict(a="4 would just restate the moles of NH3 itself, ignoring the 3 hydrogens per molecule.",
                 b="8 doesn't match 4x3=12.",
                 c="Correct — 4 moles NH3 x 3 H atoms each = 12 moles H.",
                 d="16 overshoots the correct value (would need 4 H per molecule, but NH3 only has 3).")
),
8404: dict(
    short="Molarity = moles/volume(L) = 0.4/0.2 = 2.0 M.",
    long="Molarity is moles of solute divided by volume of solution in liters: 0.4 mol / 0.2 L (200 mL converted to L) = 2.0 M.",
    trick="Always convert volume to LITERS before dividing — using 200 (mL) directly instead of 0.2 (L) gives a very different, wrong answer.",
    options=dict(a="0.5 M would come from an incorrect inverse calculation.",
                 b="1.25 M doesn't match the correct division.",
                 c="0.8 M doesn't match 0.4/0.2.",
                 d="Correct — 0.4 mol / 0.2 L = 2.0 M.")
),
8405: dict(
    short="Balanced equation shows a 1:2 mole ratio of CH4:O2, so 6 moles CH4 needs 12 moles O2.",
    long="From the balanced equation CH4 + 2O2 -> CO2 + 2H2O, 1 mole of CH4 reacts with 2 moles of O2. For 6 moles of CH4: 6 x 2 = 12 moles of O2 required.",
    trick="Always use the coefficients from the BALANCED equation as your mole ratio — using a 1:1 ratio (ignoring the '2' in front of O2) would give a wrong, smaller answer.",
    options=dict(a="Correct — 6 moles CH4 x (2 mol O2 / 1 mol CH4) = 12 moles O2.",
                 b="6 would result from an incorrect 1:1 ratio, ignoring the O2 coefficient of 2.",
                 c="3 doesn't match the correct stoichiometric ratio at all.",
                 d="18 overshoots — that would require a 1:3 ratio, which isn't what the balanced equation shows.")
),
8406: dict(
    short="The heat absorbed/released at constant pressure is called the enthalpy change (ΔH).",
    long="Enthalpy change (ΔH) is defined as the heat absorbed or released by a reaction occurring at constant pressure — a widely used thermodynamic quantity for chemical reactions run in open, atmospheric-pressure conditions.",
    trick="Don't confuse enthalpy (heat at constant pressure) with entropy (a measure of disorder) or activation energy (the energy barrier to start a reaction) — these are related but distinct thermodynamic concepts.",
    options=dict(a="Kinetic energy is the energy of motion, not the constant-pressure heat of reaction.",
                 b="Correct — enthalpy change is the heat absorbed/released at constant pressure.",
                 c="Entropy measures disorder/randomness, a different thermodynamic quantity.",
                 d="Activation energy is the energy barrier needed to start the reaction, not the overall heat change.")
),
8407: dict(
    short="Hess's law: sum the steps. X->Y (+40) + Y->Z (-90) = X->Z (-50 kJ).",
    long="By Hess's law, the overall enthalpy change for a multi-step process equals the sum of the individual steps' enthalpy changes: ΔH(X->Z) = ΔH(X->Y) + ΔH(Y->Z) = (+40) + (-90) = -50 kJ.",
    trick="Keep track of signs carefully — absorbing energy is positive (+40), releasing energy is negative (-90); a sign error here easily flips the final answer.",
    options=dict(a="+130 kJ would result from adding the magnitudes without respecting the release step's negative sign.",
                 b="-130 kJ would result from treating both steps as negative instead of one positive, one negative.",
                 c="Correct — (+40)+(-90) = -50 kJ.",
                 d="+50 kJ has the right magnitude but the wrong sign.")
),
8408: dict(
    short="Decreasing volume (increasing pressure) shifts equilibrium toward the side with fewer gas moles — here, N2O4 (1 mole).",
    long="By Le Chatelier's principle, increasing pressure (decreasing volume) favors the side of the reaction with FEWER total moles of gas, since that side takes up less volume. For 2NO2 (2 mol gas) <-> N2O4 (1 mol gas), higher pressure shifts equilibrium toward N2O4 (the products).",
    trick="Count the total moles of GAS on each side of the equation carefully — the equilibrium always shifts toward the side with fewer gas moles when pressure increases (volume decreases), not the side with more.",
    options=dict(a="The reactant side (2NO2) has MORE gas moles (2), so increased pressure shifts AWAY from it, not toward it.",
                 b="A shift toward products doesn't mean total depletion of one side — equilibrium is still maintained, just shifted.",
                 c="There is a definite, predictable shift according to Le Chatelier's principle; it's not 'no shift'.",
                 d="Correct — the product side (N2O4, 1 mole of gas) is favored when pressure increases/volume decreases.")
),
8409: dict(
    short="Continuously removing a reactant shifts equilibrium toward the products, to help replace it.",
    long="By Le Chatelier's principle, if a reactant is continuously removed from an equilibrium system, the equilibrium shifts in the direction that would replace some of that reactant — i.e., toward the reverse reaction that regenerates it, but in the context of forward/reverse balance, this manifests as the reaction shifting to try to restore the removed reactant, ultimately driving more product formation as reactant keeps being pulled away.",
    trick="Removing a substance shifts equilibrium AWAY from the side it was removed from (in the sense of the system trying to counteract the change) — don't assume removing a reactant simply halts the reaction; it actually drives it forward as consumed reactant is replenished.",
    options=dict(a="Correct — continuous removal of a reactant drives the equilibrium to keep shifting toward the products.",
                 b="A shift purely toward reactants would occur if a PRODUCT were removed, not a reactant.",
                 c="The system does respond to the disturbance — it isn't unaffected.",
                 d="The reaction doesn't simply stop; the equilibrium position shifts in response to the disturbance.")
),
8410: dict(
    short="Increasing surface area increases collision frequency between reactant particles, speeding up the reaction.",
    long="Grinding a solid into powder increases its total surface area exposed to the other reactant, allowing more particle collisions to occur per unit time, which increases the reaction rate.",
    trick="Don't confuse this with lowering activation energy (which is what a catalyst does) — increasing surface area works purely by increasing the FREQUENCY of collisions, not by making each collision more likely to succeed.",
    options=dict(a="Increased surface area increases (not decreases) the number of effective collisions.",
                 b="Correct — more exposed surface area means more particle collisions, increasing reaction rate.",
                 c="Surface area changes don't inherently lower temperature.",
                 d="Activation energy is unaffected by surface area; only a catalyst can lower it.")
),
8411: dict(
    short="Activation energy is the minimum energy needed for a successful, reaction-producing collision.",
    long="Activation energy is the energy barrier that reacting particles must overcome for a collision to successfully result in a chemical reaction (bond breaking/forming), rather than just an ineffective bounce-off.",
    trick="Don't confuse activation energy with the overall energy released by the reaction (that's related to enthalpy change), nor assume it's always zero for spontaneous reactions — even exothermic, spontaneous reactions typically still require some activation energy to get started.",
    options=dict(a="Total energy released describes the reaction's enthalpy change, not activation energy.",
                 b="Product energy alone doesn't define the activation energy barrier.",
                 c="Correct — activation energy is the minimum energy needed for particles to react upon collision.",
                 d="Spontaneous reactions can still have a nonzero activation energy; spontaneity relates to overall energy change (thermodynamics), not the kinetic barrier.")
),
8412: dict(
    short="In a galvanic cell, electrons flow externally from the anode (oxidation site) to the cathode (reduction site).",
    long="In a galvanic (voltaic) cell, oxidation occurs at the anode, releasing electrons that travel through the external circuit to the cathode, where reduction occurs. So electron flow in the external wire is anode -> cathode.",
    trick="Don't confuse electron flow (through the external wire, anode to cathode) with ion flow (through the salt bridge, maintaining charge balance) — these are separate parts of the same circuit.",
    options=dict(a="This reverses the actual direction; electrons flow FROM the anode TO the cathode, not the other way.",
                 b="Electrons flow through the external wire, not through the salt bridge (which carries ion flow).",
                 c="The salt bridge carries ions, not electrons, and doesn't connect directly to the anode this way.",
                 d="Correct — electrons flow externally from the anode to the cathode.")
),
8413: dict(
    short="Al loses electrons (0 -> +3), so it is oxidized in this reaction.",
    long="In 2Al + 3Cu2+ -> 2Al3+ + 3Cu, aluminum goes from oxidation state 0 (as a free element) to +3 (as Al3+), meaning it LOSES 3 electrons per atom — this is oxidation.",
    trick="Remember 'OIL RIG': Oxidation Is Loss (of electrons), Reduction Is Gain — Al going from 0 to +3 is a loss of electrons, hence oxidation.",
    options=dict(a="Correct — aluminum loses electrons (0 to +3), meaning it is oxidized.",
                 b="Reduction would mean gaining electrons (a more negative oxidation state), the opposite of what happens to Al here.",
                 c="Aluminum's oxidation state clearly changes from 0 to +3, so it is not unchanged.",
                 d="Aluminum is a reactant being consumed and transformed here, not merely a catalyst.")
),
8414: dict(
    short="A pH of 7 is considered neutral.",
    long="On the pH scale (0-14), a pH of 7 represents neutral (neither acidic nor basic), corresponding to pure water at 25°C where [H+] = [OH-].",
    trick="Values below 7 are acidic, above 7 are basic/alkaline — pH 7 specifically is the neutral midpoint, not itself extreme in either direction.",
    options=dict(a="Strongly acidic would correspond to a pH well below 7, not exactly 7.",
                 b="Correct — pH 7 is neutral.",
                 c="Strongly basic would correspond to a pH well above 7, not exactly 7.",
                 d="A neutral pH of 7 is not inherently 'highly corrosive' — that describes strong acids/bases at the extremes.")
),
8415: dict(
    short="Lewis acid definition: a substance that accepts a pair of electrons.",
    long="The Lewis theory broadens the acid-base concept beyond protons: a Lewis acid is an electron-pair ACCEPTOR, while a Lewis base is an electron-pair DONOR — this includes species that don't even contain H+ (like BF3).",
    trick="Don't confuse this with the Bronsted-Lowry definition (acid = proton donor) — the Lewis definition is specifically about electron pairs, and 'donates a pair of electrons' actually describes a Lewis BASE, not an acid.",
    options=dict(a="Donating a pair of electrons describes a Lewis BASE, not an acid.",
                 b="Donating a proton is the Bronsted-Lowry definition of an acid, not the Lewis definition being asked about here.",
                 c="Correct — a Lewis acid accepts a pair of electrons.",
                 d="Increasing OH- concentration describes an Arrhenius base, unrelated to the Lewis acid definition.")
),
8416: dict(
    short="Titration determines an unknown acid/base concentration by reacting it with a solution of known concentration.",
    long="Titration is a quantitative analytical technique: a solution of known concentration (the titrant) is added incrementally to a solution of unknown concentration until the reaction reaches its endpoint (often signaled by an indicator), allowing calculation of the unknown concentration.",
    trick="Titration is fundamentally about concentration determination via a controlled chemical reaction — temperature, boiling point, and indicator color changes are related observations/tools, not the core purpose itself.",
    options=dict(a="Temperature measurement is not titration's purpose.",
                 b="Boiling point determination is unrelated to titration.",
                 c="The indicator's color change is just a visual signal used during titration, not titration's overall purpose.",
                 d="Correct — titration determines an unknown acid/base concentration via reaction with a known-concentration solution.")
),
8417: dict(
    short="A carbonic acid/bicarbonate buffer resists pH change by interconverting between its two components when acid or base is added.",
    long="A buffer contains a weak acid (carbonic acid, H2CO3) and its conjugate base (bicarbonate, HCO3-). Added acid is neutralized by bicarbonate (converting to carbonic acid); added base is neutralized by carbonic acid (converting to bicarbonate) — this interconversion keeps pH relatively stable.",
    trick="A buffer works in BOTH directions (against added acids AND added bases) — an option claiming it reacts with only one type is a common trap in buffer questions.",
    options=dict(a="Correct — the buffer neutralizes added acids/bases through interconversion between carbonic acid and bicarbonate.",
                 b="Buffers specifically DO have significant capacity to resist pH changes — that's their defining function.",
                 c="A buffer resists change; it doesn't 'permanently increase' pH regardless of input.",
                 d="A buffer reacts with BOTH added acids and added bases, not strong bases exclusively.")
),
8418: dict(
    short="The -NH2 functional group characterizes amines.",
    long="Amines are organic compounds characterized by the amino functional group -NH2 (or its substituted forms), derived conceptually from ammonia (NH3) with one or more hydrogens replaced by carbon groups.",
    trick="Don't confuse -NH2 (amine) with -OH (alcohol), C=O in a chain (ketone), or -COO- (ester) — each functional group has its own distinct characteristic atoms.",
    options=dict(a="Alcohols are characterized by the -OH group, not -NH2.",
                 b="Correct — amines are characterized by the -NH2 functional group.",
                 c="Ketones are characterized by a carbonyl group (C=O) within a carbon chain, not -NH2.",
                 d="Esters are characterized by a -COO- linkage, not -NH2.")
),
8419: dict(
    short="Alkynes contain at least one carbon-carbon triple bond.",
    long="Alkynes are hydrocarbons characterized by at least one C≡C triple bond, distinguishing them from alkanes (all single bonds) and alkenes (double bonds).",
    trick="Remember the naming/bonding pattern: alkanes = single bonds only, alkenes = double bond(s), alkynes = triple bond(s) — don't mix these three hydrocarbon classes up.",
    options=dict(a="Only single bonds describes alkanes, not alkynes.",
                 b="A benzene ring describes aromatic compounds, a separate structural class.",
                 c="Correct — alkynes have at least one carbon-carbon triple bond.",
                 d="Alkynes still have carbon-hydrogen bonds; only some carbon positions lack extra hydrogens due to the triple bond's geometry.")
),
8420: dict(
    short="A primary alcohol's -OH carbon is bonded to zero or one other carbon atom.",
    long="Alcohols are classified by how many carbon atoms are attached to the carbon bearing the -OH group: primary (0 or 1 other carbon), secondary (2 other carbons), tertiary (3 other carbons).",
    trick="Don't confuse this with 'primary' referring to position in a chain generally — it specifically counts carbon attachments to the -OH-bearing carbon itself.",
    options=dict(a="Four carbon attachments isn't even possible on a carbon also bonded to -OH (would exceed carbon's 4 total bonds).",
                 b="Two carbon attachments describes a SECONDARY alcohol, not primary.",
                 c="Three carbon attachments describes a TERTIARY alcohol, not primary.",
                 d="Correct — a primary alcohol's -OH carbon is bonded to zero or one other carbon (e.g., methanol has zero, ethanol has one).")
),
8421: dict(
    short="A tertiary substrate (stable carbocation) favors SN1 over SN2.",
    long="SN1 reactions proceed through a carbocation intermediate, so substrates that form STABLE carbocations (tertiary > secondary > primary, due to hyperconjugation/inductive stabilization by alkyl groups) favor the SN1 pathway.",
    trick="SN2 favors the OPPOSITE conditions: primary/unhindered substrates, strong nucleophiles, and polar APROTIC solvents — if you see these conditions instead, think SN2, not SN1.",
    options=dict(a="Correct — a tertiary substrate forming a stable carbocation favors SN1.",
                 b="A primary, unhindered substrate favors SN2 (backside attack is easy), not SN1.",
                 c="A strong nucleophile in high concentration favors SN2, which depends on nucleophile strength/concentration; SN1 doesn't.",
                 d="A polar APROTIC solvent favors SN2; SN1 is favored by polar PROTIC solvents that stabilize the carbocation and leaving group.")
),
8422: dict(
    short="Ethylene forming polyethylene is addition polymerization (monomers simply add together, no byproduct).",
    long="Addition polymerization involves small unsaturated monomers (like ethylene, containing a C=C double bond) adding together directly, opening their double bonds to form long chains, without losing any atoms/byproducts — unlike condensation polymerization, which releases a small molecule (often water) per bond formed.",
    trick="If a small molecule like water is released as monomers join, that's CONDENSATION polymerization — addition polymerization (like polyethylene formation) releases nothing extra.",
    options=dict(a="Hydrolysis is a bond-breaking reaction using water, the opposite process from forming a polymer.",
                 b="Correct — ethylene forming polyethylene is a classic example of addition polymerization.",
                 c="Condensation polymerization releases water as a byproduct; addition polymerization (like this case) does not.",
                 d="Combustion is a burning/oxidation reaction, unrelated to polymer chain formation.")
),
8423: dict(
    short="An -O- linkage between two carbon chains with no carbonyl group defines an ether.",
    long="Ethers have the general structure R-O-R', an oxygen atom bridging two carbon-containing groups, with no carbonyl (C=O) group present — distinguishing them from esters (which do have a carbonyl adjacent to the -O-).",
    trick="The presence or absence of a carbonyl (C=O) group is the key distinguishing feature between an ether (-O- only) and an ester (-C(=O)-O-) — don't classify purely by the presence of oxygen.",
    options=dict(a="An ester has a carbonyl group adjacent to the -O- linkage; this compound explicitly has NO carbonyl group.",
                 b="An aldehyde is characterized by a terminal -CHO carbonyl group, not an -O- bridge between chains.",
                 c="Correct — an -O- linkage between carbon chains with no carbonyl group is an ether.",
                 d="An amide contains a carbonyl group bonded to nitrogen (-C(=O)-N-), not an -O- linkage like this.")
),
8424: dict(
    short="Transition metals' closely-spaced d-electron energies allow multiple oxidation states.",
    long="Transition metals have (n-1)d and ns electrons that are relatively close in energy, so varying numbers of electrons can be involved in bonding depending on conditions, resulting in the characteristic multiple oxidation states seen across transition metal chemistry.",
    trick="Don't think transition metals 'lack' d electrons or bonding capability — quite the opposite, it's the AVAILABILITY and close energy spacing of their d electrons that enables this variable bonding behavior.",
    options=dict(a="Transition metals DO have d electrons available for bonding — that's central to their chemistry.",
                 b="Transition metals absolutely have electron configurations; this option is factually false.",
                 c="Transition metals readily form ions (that's how they achieve different oxidation states).",
                 d="Correct — closely-spaced d-electron energies allow variable involvement in bonding, producing multiple oxidation states.")
),
8425: dict(
    short="Halogens are highly reactive because they strongly tend to gain one electron to complete a stable octet.",
    long="Halogens (Group 17) have 7 valence electrons, just one short of a stable noble-gas octet. This creates a strong drive to gain one more electron (forming a -1 anion), making them highly reactive nonmetals.",
    trick="Don't confuse halogen reactivity (electron-GAINING tendency) with alkali-metal reactivity (electron-LOSING tendency) — they achieve stability via opposite mechanisms.",
    options=dict(a="Correct — halogens strongly tend to gain one electron to complete a stable octet.",
                 b="Halogens tend to GAIN electrons, not lose them, to reach stability.",
                 c="Halogens react vigorously with metals (e.g., forming salts like NaCl), the opposite of not reacting.",
                 d="Halogens do NOT have a complete valence shell already — they're one electron short, which drives their reactivity.")
),
8426: dict(
    short="Mg goes from oxidation state 0 (element) to +2 in MgO — this is oxidation.",
    long="In 2Mg + O2 -> 2MgO, elemental magnesium (oxidation state 0) loses 2 electrons to become Mg2+ in the ionic compound MgO, an increase in oxidation state from 0 to +2 — this is oxidation.",
    trick="Remember 'OIL RIG': Oxidation Is Loss of electrons (increase in oxidation number) — Mg going from 0 to +2 fits oxidation, not reduction.",
    options=dict(a="This reverses the direction; Mg actually goes from 0 to +2, not +2 to 0.",
                 b="Correct — Mg goes from 0 to +2, which is oxidation (loss of electrons).",
                 c="Mg's oxidation state increases (to +2, positive), not decreases to a negative value.",
                 d="Mg's oxidation state clearly changes (0 to +2) as it forms the ionic compound MgO.")
),
8427: dict(
    short="Osmotic pressure depends on the concentration (number) of solute particles, not their identity.",
    long="Osmotic pressure is a colligative property, meaning it depends on the NUMBER of dissolved solute particles per unit volume, regardless of what those particles chemically are (as long as they don't dissociate differently).",
    trick="Colligative properties (osmotic pressure, boiling point elevation, freezing point depression, vapor pressure lowering) all share this defining trait: they depend on particle COUNT/concentration, not particle identity.",
    options=dict(a="Colligative properties, by definition, do NOT depend on the specific identity of the solute.",
                 b="Color is a physical/optical property unrelated to osmotic pressure.",
                 c="Correct — osmotic pressure depends on the concentration (number) of solute particles.",
                 d="The solvent's boiling point alone doesn't define osmotic pressure of a solution.")
),
8428: dict(
    short="Above the critical point, a substance exists as a supercritical fluid with no distinct liquid-gas boundary.",
    long="Beyond the critical temperature and pressure, the distinction between liquid and gas phases disappears — the substance becomes a single, continuous supercritical fluid phase with properties intermediate between a liquid and a gas.",
    trick="Don't confuse the critical point region with the triple point (where solid, liquid, and gas all coexist at LOW pressure/temperature) — the critical point is at HIGH pressure/temperature, marking the END of the distinct liquid-gas boundary.",
    options=dict(a="A solid-only state would not occur at high pressure/temperature conditions beyond the critical point.",
                 b="A clear liquid-gas boundary is exactly what DISAPPEARS beyond the critical point — this option describes the opposite.",
                 c="Plasma requires much more extreme conditions (ionization of atoms) than simply crossing the critical point on a standard phase diagram.",
                 d="Correct — beyond the critical point, the substance exists as a supercritical fluid with no distinct liquid-gas boundary.")
),
8429: dict(
    short="Acid rain forms when SO2 and NOx react with atmospheric water vapor to form acidic compounds.",
    long="Sulfur dioxide and nitrogen oxides released into the atmosphere react with water vapor (and oxygen) to form sulfuric acid and nitric acid, which fall as acid rain, lowering the pH of precipitation.",
    trick="Don't confuse this mechanism with ozone depletion (a separate atmospheric chemistry issue involving CFCs) — acid rain specifically involves SO2/NOx reacting with water to form acids.",
    options=dict(a="Correct — SO2 and NOx react with atmospheric water vapor to form acidic compounds, causing acid rain.",
                 b="Reaction with carbon dioxide exclusively is not the standard acid rain formation pathway.",
                 c="Reaction with ozone to form 'harmless products' does not describe acid rain formation; ozone depletion is a different (though related) atmospheric issue.",
                 d="Reaction with oxygen gas to form water doesn't describe the acid-forming chemistry involved in acid rain.")
),
8430: dict(
    short="Phasing out ozone-depleting substances like CFCs helps mitigate ozone layer depletion.",
    long="Chlorofluorocarbons (CFCs) catalytically destroy stratospheric ozone. Reducing/eliminating their use (replacing them with ozone-safe alternatives, as done under the Montreal Protocol) directly helps the ozone layer recover.",
    trick="Increasing CFC or halon production would make ozone depletion WORSE, not better — make sure you're identifying the mitigating action, not an aggravating one.",
    options=dict(a="Increasing CFC use would worsen ozone depletion, not help mitigate it.",
                 b="Correct — phasing out CFCs in favor of safer alternatives directly helps address ozone depletion.",
                 c="Removing pollution regulations would likely worsen environmental harm, not help.",
                 d="Increasing halon production (halons also deplete ozone) would worsen the problem, not mitigate it.")
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
    out_path = root / "scripts" / "mock20_explanations_chemistry.json"
    out_path.write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Wrote {len(out)} explanations to {out_path}")

if __name__ == "__main__":
    main()
