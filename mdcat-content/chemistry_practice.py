"""
MDCAT Chemistry Question Bank
=============================
200 MCQs modeled on the MDCAT (Punjab / national) Chemistry syllabus
(pmdc_mdcat_syllabus.json), same id/subject/topic/subtopic/difficulty/
question/options/answer dict shape as biology_practice.py.

Topic distribution (approx):
    Fundamental Concepts of Chemistry ......... 10
    Atomic Structure ........................... 14
    Gases ....................................... 10
    Liquids ......................................  8
    Solids .......................................  8
    Chemical Equilibrium ........................ 12
    Reaction Kinetics ........................... 10
    Thermochemistry and Energetics .............. 12
    Electrochemistry ............................ 10
    Chemical Bonding ............................ 14
    s and p Block Elements ...................... 12
    Transition Elements ..........................  6
    Fundamental Principles of Organic Chemistry ..  8
    Chemistry of Hydrocarbons ................... 18
    Alkyl Halides .................................  8
    Alcohols and Phenols ........................ 10
    Aldehydes and Ketones ....................... 10
    Carboxylic Acids ..............................  8
    Macromolecules .................................6
    Industrial Chemistry ...........................6
    Total ....................................... 200

Difficulty mix ~ 30% Easy / 50% Medium / 20% Hard.

Unlike biology_practice.py (options hand-shuffled after authoring), this
file is written as a small builder: each item in RAW carries the correct
answer's TEXT plus its distractors, and the module-level code below
assigns the correct answer to a rotating A/B/C/D slot (round robin over
the 200 items -> an exact 50/50/50/50 split) so the key can't be gamed
by always picking one letter. QUESTIONS (the list other scripts import)
is built once, at import time, from RAW.

Each question in QUESTIONS is a dict:
    id, subject, topic, subtopic, difficulty, question, options (A-D), answer
"""

# Each RAW entry: (id, topic, subtopic, difficulty, question, correct, [distractor1, distractor2, distractor3])
RAW = []


def add(id, topic, subtopic, difficulty, question, correct, distractors):
    RAW.append((id, topic, subtopic, difficulty, question, correct, distractors))


# ============================================================
# FUNDAMENTAL CONCEPTS OF CHEMISTRY (10)  id 1-10
# ============================================================

add(1, 'Fundamental Concepts of Chemistry', "Moles and Avogadro's Number", 'Easy',
    'One mole of any substance contains how many particles?',
    '6.022 x 10^23', ['6.022 x 10^22', '3.011 x 10^23', '1.000 x 10^23'])

add(2, 'Fundamental Concepts of Chemistry', "Moles and Avogadro's Number", 'Easy',
    'The number of moles in 44 g of CO2 (molar mass 44 g/mol) is:',
    '1 mole', ['0.5 mole', '2 moles', '4 moles'])

add(3, 'Fundamental Concepts of Chemistry', "Moles and Avogadro's Number", 'Medium',
    'The number of atoms present in 0.5 mole of oxygen gas (O2) is:',
    '6.022 x 10^23', ['3.011 x 10^23', '1.204 x 10^24', '6.022 x 10^22'])

add(4, 'Fundamental Concepts of Chemistry', 'Limiting and Excess Reactants', 'Medium',
    'In a reaction, the reactant that is completely consumed and determines the amount of product formed is called the:',
    'Limiting reactant', ['Excess reactant', 'Catalyst', 'Intermediate'])

add(5, 'Fundamental Concepts of Chemistry', 'Limiting and Excess Reactants', 'Hard',
    'If 2 mol H2 reacts with 2 mol O2 in the reaction 2H2 + O2 -> 2H2O, the limiting reactant is:',
    'H2', ['O2', 'Both are limiting', 'Neither, reaction is complete'])

add(6, 'Fundamental Concepts of Chemistry', 'Yield (Theoretical, Actual, Percentage)', 'Easy',
    'The maximum amount of product that can be formed from given reactants, calculated from stoichiometry, is called the:',
    'Theoretical yield', ['Actual yield', 'Percentage yield', 'Excess yield'])

add(7, 'Fundamental Concepts of Chemistry', 'Yield (Theoretical, Actual, Percentage)', 'Medium',
    'If the theoretical yield of a reaction is 20 g and the actual yield obtained is 15 g, the percentage yield is:',
    '75%', ['80%', '60%', '133%'])

add(8, 'Fundamental Concepts of Chemistry', "Moles and Avogadro's Number", 'Medium',
    'The mass of one mole of water (H2O) molecules is approximately:',
    '18 g', ['16 g', '9 g', '36 g'])

add(9, 'Fundamental Concepts of Chemistry', 'Limiting and Excess Reactants', 'Medium',
    'The reactant left over after a reaction has gone to completion is called the:',
    'Excess reactant', ['Limiting reactant', 'Byproduct', 'Catalyst'])

add(10, 'Fundamental Concepts of Chemistry', 'Yield (Theoretical, Actual, Percentage)', 'Hard',
    'A low percentage yield in an experiment is most likely explained by:',
    'Side reactions and loss of product during purification/transfer',
    ['Using too much limiting reactant', 'An error in the mole concept', 'Excess catalyst being present'])


# ============================================================
# ATOMIC STRUCTURE (14)  id 11-24
# ============================================================

add(11, 'Atomic Structure', 'Discovery of Proton', 'Easy',
    'The proton was discovered by:',
    'Goldstein', ['J.J. Thomson', 'Rutherford', 'Chadwick'])

add(12, 'Atomic Structure', 'Discovery of Proton', 'Medium',
    'Positively charged particles observed in a discharge tube experiment with perforated cathode were called:',
    'Canal rays', ['Cathode rays', 'Beta rays', 'X-rays'])

add(13, 'Atomic Structure', "Planck's Quantum Theory", 'Medium',
    "According to Planck's quantum theory, energy is emitted or absorbed:",
    'In discrete packets called quanta', ['Continuously in any amount', 'Only as heat', 'Only in the form of protons'])

add(14, 'Atomic Structure', "Planck's Quantum Theory", 'Medium',
    'The energy of a photon is given by the equation:',
    'E = h nu', ['E = mc^2', 'E = mv^2', 'E = h/nu'])

add(15, 'Atomic Structure', 'Quantum Numbers', 'Easy',
    'The principal quantum number (n) describes the:',
    'Main energy level (shell) of an electron', ['Shape of the orbital', 'Orientation of the orbital', 'Spin of the electron'])

add(16, 'Atomic Structure', 'Quantum Numbers', 'Medium',
    'The azimuthal (angular momentum) quantum number "l" determines the:',
    'Shape of the orbital (subshell)', ['Energy level (shell)', 'Orientation of the orbital in space', 'Spin direction of the electron'])

add(17, 'Atomic Structure', 'Quantum Numbers', 'Medium',
    'The magnetic quantum number (m) describes the:',
    'Orientation of the orbital in space', ['Shape of the orbital', 'Energy level of the electron', 'Spin of the electron'])

add(18, 'Atomic Structure', 'Quantum Numbers', 'Hard',
    'For n = 3, the possible values of the azimuthal quantum number "l" are:',
    '0, 1, 2', ['0, 1', '1, 2, 3', '0, 1, 2, 3'])

add(19, 'Atomic Structure', 'Shapes of Orbitals', 'Easy',
    'The shape of an s-orbital is:',
    'Spherical', ['Dumbbell-shaped', 'Cloverleaf-shaped', 'Doughnut-shaped'])

add(20, 'Atomic Structure', 'Shapes of Orbitals', 'Medium',
    'A p-orbital has which characteristic shape?',
    'Dumbbell-shaped with two lobes', ['Spherical', 'Cloverleaf-shaped', 'Cubic'])

add(21, 'Atomic Structure', 'Spectrum of Hydrogen', 'Medium',
    'The Balmer series in the hydrogen spectrum results from electron transitions to which energy level?',
    'n = 2', ['n = 1', 'n = 3', 'n = 4'])

add(22, 'Atomic Structure', 'Spectrum of Hydrogen', 'Hard',
    'The Lyman series of the hydrogen spectrum lies in which region of the electromagnetic spectrum?',
    'Ultraviolet', ['Visible', 'Infrared', 'Microwave'])

add(23, 'Atomic Structure', 'Electronic Configuration', 'Easy',
    'The electronic configuration of Sodium (Z = 11) is:',
    '2, 8, 1', ['2, 8, 2', '2, 9', '8, 2, 1'])

add(24, 'Atomic Structure', 'Electronic Configuration', 'Medium',
    'According to the Aufbau principle, electrons fill orbitals:',
    'In order of increasing energy', ['In order of decreasing energy', 'Randomly', 'Only in the outermost shell first'])


# ============================================================
# GASES (10)  id 25-34
# ============================================================

add(25, 'Gases', 'Kinetic Molecular Theory', 'Easy',
    'According to the kinetic molecular theory, gas particles are considered to be:',
    'In constant, random motion', ['Stationary', 'Arranged in a fixed lattice', 'Attracted strongly to each other'])

add(26, 'Gases', 'Standard Temperature and Pressure', 'Easy',
    'Standard temperature and pressure (STP) is defined as:',
    '0 degrees C (273 K) and 1 atm', ['25 degrees C and 1 atm', '0 degrees C and 2 atm', '100 degrees C and 1 atm'])

add(27, 'Gases', "Boyle's Law", 'Medium',
    "Boyle's law states that at constant temperature, the volume of a fixed mass of gas is:",
    'Inversely proportional to its pressure', ['Directly proportional to its pressure', 'Independent of pressure', 'Directly proportional to the square of pressure'])

add(28, 'Gases', "Charles's Law", 'Medium',
    "Charles's law states that at constant pressure, the volume of a fixed mass of gas is:",
    'Directly proportional to its absolute temperature', ['Inversely proportional to its absolute temperature', 'Independent of temperature', 'Directly proportional to pressure'])

add(29, 'Gases', 'Absolute Zero', 'Medium',
    'Absolute zero, the temperature at which an ideal gas would theoretically have zero volume, is:',
    '-273.15 degrees C (0 K)', ['0 degrees C', '-100 degrees C', '-373 degrees C'])

add(30, 'Gases', 'Ideal Gas Equation', 'Medium',
    'The ideal gas equation is expressed as:',
    'PV = nRT', ['PV = nT/R', 'P/V = nRT', 'PVT = nR'])

add(31, 'Gases', 'Ideal Gas Constant (R)', 'Hard',
    'The value of the universal gas constant R in SI units is approximately:',
    '8.314 J/(mol K)', ['0.0821 J/(mol K)', '1.987 J/(mol K)', '22.4 J/(mol K)'])

add(32, 'Gases', 'Real and Ideal Gases', 'Medium',
    'Real gases deviate most from ideal behavior under conditions of:',
    'High pressure and low temperature', ['Low pressure and high temperature', 'Standard temperature and pressure', 'High temperature and high pressure'])

add(33, 'Gases', 'Ideal Gas Equation', 'Hard',
    'At constant volume, if the temperature of an ideal gas is doubled, its pressure will:',
    'Double', ['Remain the same', 'Be halved', 'Quadruple'])

add(34, 'Gases', 'Kinetic Molecular Theory', 'Hard',
    'According to kinetic molecular theory, an increase in temperature causes gas molecules to:',
    'Move faster, increasing their average kinetic energy', ['Move slower', 'Stop moving', 'Decrease in kinetic energy'])


# ============================================================
# LIQUIDS (8)  id 35-42
# ============================================================

add(35, 'Liquids', 'Properties of Liquids (Kinetic Theory)', 'Easy',
    'Compared to gases, liquids have:',
    'Definite volume but no definite shape', ['Definite shape and definite volume', 'No definite shape and no definite volume', 'Definite shape but no definite volume'])

add(36, 'Liquids', 'Evaporation, Boiling Point, Vapor Pressure', 'Medium',
    'A liquid boils when its vapor pressure becomes equal to:',
    'The external (atmospheric) pressure', ['Zero', 'Twice the atmospheric pressure', 'Its critical pressure'])

add(37, 'Liquids', 'Evaporation, Boiling Point, Vapor Pressure', 'Medium',
    'Evaporation of a liquid causes cooling of its surroundings because:',
    'Higher-energy molecules escape, lowering the average kinetic energy left behind', ['Lower-energy molecules escape first', 'The liquid absorbs heat from itself only', 'Evaporation releases heat'])

add(38, 'Liquids', 'Hydrogen Bonding', 'Medium',
    'Hydrogen bonding occurs when hydrogen is covalently bonded to a small, highly electronegative atom such as:',
    'F, O, or N', ['C, S, or P', 'Cl, Br, or I', 'Any nonmetal'])

add(39, 'Liquids', 'Anomalous Behavior of Water', 'Hard',
    'Water shows anomalous behavior because it is:',
    'Denser as a liquid at 4 degrees C than as ice', ['Denser as a solid than as a liquid at all temperatures', 'Less dense as a liquid than as a gas', 'Non-polar unlike other liquids'])

add(40, 'Liquids', 'Hydrogen Bonding', 'Medium',
    'The unusually high boiling point of water compared to other hydrides of Group VI elements is due to:',
    'Extensive hydrogen bonding between water molecules', ['Its low molecular mass', 'Weak van der Waals forces', 'Its covalent network structure'])

add(41, 'Liquids', 'Properties of Liquids (Kinetic Theory)', 'Easy',
    'The property of a liquid surface that allows small insects to walk on water is called:',
    'Surface tension', ['Viscosity', 'Vapor pressure', 'Capillarity'])

add(42, 'Liquids', 'Evaporation, Boiling Point, Vapor Pressure', 'Hard',
    'As the temperature of a liquid increases, its vapor pressure:',
    'Increases', ['Decreases', 'Remains constant', 'Becomes zero'])


# ============================================================
# SOLIDS (8)  id 43-50
# ============================================================

add(43, 'Solids', 'Crystalline Solids', 'Easy',
    'A solid with a highly ordered, repeating internal arrangement of particles is called a:',
    'Crystalline solid', ['Amorphous solid', 'Colloid', 'Liquid crystal'])

add(44, 'Solids', 'Crystalline Solids', 'Medium',
    'Amorphous solids differ from crystalline solids in that amorphous solids:',
    'Lack a long-range ordered particle arrangement', ['Have a sharp, definite melting point', 'Have a highly ordered lattice', 'Are always ionic in nature'])

add(45, 'Solids', 'Ionic vs Molecular Crystals', 'Medium',
    'Ionic crystals such as NaCl typically have:',
    'High melting points due to strong electrostatic forces', ['Low melting points due to weak van der Waals forces', 'No definite geometric shape', 'High electrical conductivity in solid state'])

add(46, 'Solids', 'Ionic vs Molecular Crystals', 'Medium',
    'Molecular crystals, such as solid CO2 (dry ice), are held together primarily by:',
    'Weak van der Waals / intermolecular forces', ['Strong ionic bonds', 'Metallic bonds', 'Covalent network bonds throughout the lattice'])

add(47, 'Solids', 'Crystal Lattice', 'Medium',
    'The smallest repeating three-dimensional arrangement of particles in a crystal is called the:',
    'Unit cell', ['Molecule', 'Isomer', 'Allotrope'])

add(48, 'Solids', 'Lattice Energy', 'Hard',
    'Lattice energy is defined as the energy released when:',
    'Gaseous ions combine to form one mole of a solid ionic crystal', ['A solid melts into a liquid', 'A solid sublimes directly into a gas', 'Covalent bonds are broken in a molecule'])

add(49, 'Solids', 'Factors Affecting Shape of Ionic Crystals', 'Hard',
    'The shape and structure of an ionic crystal is most directly influenced by:',
    'The relative sizes (radius ratio) of the cation and anion', ['The color of the compound', 'The temperature of formation only', 'The state of matter at room temperature'])

add(50, 'Solids', 'Crystalline Solids', 'Medium',
    'Which of the following is an example of an amorphous solid?',
    'Glass', ['Sodium chloride', 'Diamond', 'Quartz'])


# ============================================================
# CHEMICAL EQUILIBRIUM (12)  id 51-62
# ============================================================

add(51, 'Chemical Equilibrium', 'Chemical Equilibrium (Reversible Reactions)', 'Easy',
    'A state in which the rates of the forward and reverse reactions are equal is called:',
    'Chemical equilibrium', ['Completion of reaction', 'Activation state', 'Steady combustion'])

add(52, 'Chemical Equilibrium', 'Chemical Equilibrium (Reversible Reactions)', 'Medium',
    'At chemical equilibrium, the concentrations of reactants and products:',
    'Remain constant over time (though reactions continue)', ['Become exactly equal to each other', 'Both reach zero', 'Increase continuously'])

add(53, 'Chemical Equilibrium', "Le Chatelier's Principle", 'Medium',
    "Le Chatelier's principle states that if a system at equilibrium is disturbed, it will:",
    'Shift to counteract the disturbance and restore a new equilibrium', ['Immediately stop reacting', 'Shift in the direction favoring the disturbance', 'Remain completely unaffected'])

add(54, 'Chemical Equilibrium', "Le Chatelier's Principle", 'Medium',
    'Increasing the pressure on a gaseous equilibrium system will shift the equilibrium toward the side with:',
    'Fewer moles of gas', ['More moles of gas', 'Equal moles of gas on both sides always', 'No effect regardless of moles'])

add(55, 'Chemical Equilibrium', 'Solubility Products', 'Medium',
    'The solubility product (Ksp) of a sparingly soluble salt is:',
    'The product of the molar concentrations of its ions at saturation, each raised to its stoichiometric power', ['The total mass of salt dissolved per liter', 'Always equal to 1', 'The rate at which the salt dissolves'])

add(56, 'Chemical Equilibrium', 'Common Ion Effect', 'Medium',
    'The common ion effect refers to the:',
    'Decrease in solubility of a salt when a solution already contains one of its constituent ions', ['Increase in solubility when a common ion is added', 'Effect of temperature on solubility', 'Effect of pressure on gas solubility'])

add(57, 'Chemical Equilibrium', 'Buffer Solutions', 'Medium',
    'A buffer solution resists changes in pH when small amounts of acid or base are added because it contains:',
    'A weak acid/base and its conjugate salt', ['Only a strong acid', 'Only pure water', 'Only a strong base'])

add(58, 'Chemical Equilibrium', 'Buffer Solutions', 'Hard',
    'An acidic buffer can be prepared by mixing:',
    'A weak acid with its conjugate base salt (e.g., CH3COOH and CH3COONa)', ['A strong acid with a strong base', 'Two strong acids', 'Pure water with a strong base'])

add(59, 'Chemical Equilibrium', "Haber's Process", 'Medium',
    "The Haber's process is industrially used for the manufacture of:",
    'Ammonia (NH3) from nitrogen and hydrogen', ['Sulfuric acid', 'Nitric acid', 'Sodium carbonate'])

add(60, 'Chemical Equilibrium', "Haber's Process", 'Hard',
    "In the Haber's process, the forward reaction (N2 + 3H2 <-> 2NH3) is exothermic, so according to Le Chatelier's principle, high temperature:",
    'Favors the reverse reaction, lowering ammonia yield', ['Always increases ammonia yield', 'Has no effect on equilibrium position', 'Only affects the rate, not the yield'])

add(61, 'Chemical Equilibrium', 'Chemical Equilibrium (Reversible Reactions)', 'Hard',
    'A large value of the equilibrium constant (Keq) indicates that at equilibrium:',
    'Products are strongly favored over reactants', ['Reactants are strongly favored over products', 'The reaction has not started', 'The reaction is at STP'])

add(62, 'Chemical Equilibrium', 'Solubility Products', 'Hard',
    'If the ionic product of a salt in solution exceeds its Ksp, the solution is:',
    'Supersaturated, and precipitation will occur', ['Unsaturated, more salt can dissolve', 'Exactly saturated with no further change', 'Undergoing dilution'])


# ============================================================
# REACTION KINETICS (10)  id 63-72
# ============================================================

add(63, 'Reaction Kinetics', 'Rate of Reaction and Rate Equation', 'Easy',
    'The rate of a chemical reaction is defined as the:',
    'Change in concentration of reactants or products per unit time', ['Total amount of reactant used', 'Time taken for the reaction to start', 'Energy released during the reaction'])

add(64, 'Reaction Kinetics', 'Factors Affecting Rate of Reaction', 'Easy',
    'Which of the following generally increases the rate of a chemical reaction?',
    'Increasing temperature', ['Decreasing temperature', 'Decreasing surface area of reactants', 'Removing the catalyst'])

add(65, 'Reaction Kinetics', 'Factors Affecting Rate of Reaction', 'Medium',
    'A catalyst increases the rate of a reaction by:',
    'Providing an alternative pathway with lower activation energy', ['Increasing the activation energy', 'Being consumed in the reaction', 'Shifting the equilibrium position'])

add(66, 'Reaction Kinetics', 'Order of Reaction', 'Medium',
    'The order of a reaction is determined by:',
    'The experimentally observed dependence of rate on reactant concentrations', ['The stoichiometric coefficients in the balanced equation alone', 'The number of reactant molecules only', 'The temperature at which the reaction occurs'])

add(67, 'Reaction Kinetics', 'Order of Reaction', 'Medium',
    'For a reaction that is first order overall, doubling the concentration of the reactant will:',
    'Double the rate of reaction', ['Quadruple the rate of reaction', 'Have no effect on the rate', 'Halve the rate of reaction'])

add(68, 'Reaction Kinetics', 'Activation Energy and Activated Complex', 'Medium',
    'The minimum energy required for reactant molecules to react upon collision is called:',
    'Activation energy', ['Bond energy', 'Lattice energy', 'Ionization energy'])

add(69, 'Reaction Kinetics', 'Activation Energy and Activated Complex', 'Hard',
    'The unstable, high-energy species formed momentarily during a reaction, between reactants and products, is called the:',
    'Activated complex (transition state)', ['Catalyst', 'Intermediate product', 'Free radical'])

add(70, 'Reaction Kinetics', 'Rate Constant', 'Medium',
    'In the rate equation Rate = k[A]^m[B]^n, the term "k" represents the:',
    'Rate constant', ['Order of reaction', 'Equilibrium constant', 'Activation energy'])

add(71, 'Reaction Kinetics', 'Rate Constant', 'Hard',
    'The rate constant (k) of a reaction is affected mainly by:',
    'Temperature and the presence of a catalyst', ['Only the initial concentration of reactants', 'The volume of the container only', 'The color of the reactants'])

add(72, 'Reaction Kinetics', 'Factors Affecting Rate of Reaction', 'Medium',
    'Increasing the surface area of a solid reactant increases the reaction rate because it:',
    'Exposes more particles for collision with the other reactant', ['Decreases the number of effective collisions', 'Lowers the temperature of the system', 'Increases the activation energy'])


# ============================================================
# THERMOCHEMISTRY AND ENERGETICS (12)  id 73-84
# ============================================================

add(73, 'Thermochemistry and Energetics', 'Thermodynamics (Definition)', 'Easy',
    'Thermodynamics is the branch of science that deals with:',
    'Heat, work, and energy changes accompanying physical and chemical processes', ['Only the rate of chemical reactions', 'Only the structure of atoms', 'Only electrical phenomena'])

add(74, 'Thermochemistry and Energetics', 'Exothermic and Endothermic Reactions', 'Easy',
    'A reaction that releases heat to the surroundings is called:',
    'Exothermic', ['Endothermic', 'Isothermic', 'Adiabatic'])

add(75, 'Thermochemistry and Energetics', 'Exothermic and Endothermic Reactions', 'Medium',
    'In an endothermic reaction, the enthalpy change (delta H) is:',
    'Positive', ['Negative', 'Zero', 'Undefined'])

add(76, 'Thermochemistry and Energetics', 'System, Surroundings, State Functions', 'Medium',
    'The part of the universe under study, separated from everything else, is called the:',
    'System', ['Surroundings', 'Universe', 'Boundary'])

add(77, 'Thermochemistry and Energetics', 'System, Surroundings, State Functions', 'Medium',
    'A property that depends only on the initial and final states of a system, not on the path taken, is called a:',
    'State function', ['Path function', 'Extensive property only', 'Kinetic property'])

add(78, 'Thermochemistry and Energetics', 'Internal Energy', 'Medium',
    'The internal energy of a system is the sum of:',
    'The kinetic and potential energies of all particles in the system', ['Only the kinetic energy of the system', 'Only the potential energy of the system', 'The heat released by the system'])

add(79, 'Thermochemistry and Energetics', 'First Law of Thermodynamics', 'Medium',
    'The first law of thermodynamics is a statement of the conservation of:',
    'Energy', ['Mass only', 'Momentum', 'Charge'])

add(80, 'Thermochemistry and Energetics', 'First Law of Thermodynamics', 'Hard',
    'According to the first law of thermodynamics, delta U = q + w. If a system absorbs heat and has work done on it, its internal energy will:',
    'Increase', ['Decrease', 'Remain constant', 'Become zero'])

add(81, 'Thermochemistry and Energetics', "Hess's Law", 'Medium',
    "Hess's law states that the total enthalpy change for a reaction is:",
    'The same whether the reaction occurs in one step or several steps', ['Different depending on the number of steps', 'Always zero for exothermic reactions', 'Dependent only on the catalyst used'])

add(82, 'Thermochemistry and Energetics', 'Enthalpy of Reaction', 'Medium',
    'The enthalpy of combustion is the heat change when one mole of a substance is:',
    'Completely burned in excess oxygen', ['Dissolved in water', 'Formed from its elements', 'Neutralized by an acid'])

add(83, 'Thermochemistry and Energetics', 'Enthalpy of Reaction', 'Hard',
    'The standard enthalpy of formation of an element in its most stable state is defined as:',
    'Zero', ['Always positive', 'Always negative', 'Equal to its atomic mass'])

add(84, 'Thermochemistry and Energetics', "Hess's Law", 'Hard',
    "Hess's law is a direct consequence of the fact that enthalpy is a:",
    'State function', ['Path function', 'Kinetic quantity', 'Non-conserved quantity'])


# ============================================================
# ELECTROCHEMISTRY (10)  id 85-94
# ============================================================

add(85, 'Electrochemistry', 'Redox Reactions', 'Easy',
    'A reaction in which both oxidation and reduction occur simultaneously is called a:',
    'Redox reaction', ['Neutralization reaction', 'Precipitation reaction', 'Hydrolysis reaction'])

add(86, 'Electrochemistry', 'Oxidation and Reduction', 'Easy',
    'Oxidation is best defined as the:',
    'Loss of electrons', ['Gain of electrons', 'Loss of protons', 'Gain of protons'])

add(87, 'Electrochemistry', 'Oxidation and Reduction', 'Easy',
    'Reduction is best defined as the:',
    'Gain of electrons', ['Loss of electrons', 'Gain of protons', 'Loss of protons'])

add(88, 'Electrochemistry', 'Oxidation and Reduction', 'Medium',
    'In the reaction Zn + Cu2+ -> Zn2+ + Cu, the species that is oxidized is:',
    'Zn', ['Cu2+', 'Zn2+', 'Cu'])

add(89, 'Electrochemistry', 'Oxidation and Reduction', 'Medium',
    'The oxidizing agent in a redox reaction is the species that:',
    'Gets reduced (gains electrons) while oxidizing another species', ['Gets oxidized (loses electrons)', 'Remains unchanged throughout', 'Acts only as a catalyst'])

add(90, 'Electrochemistry', 'Balancing Redox Equations', 'Medium',
    'When balancing redox equations by the oxidation number method, electrons lost in oxidation must:',
    'Equal electrons gained in reduction', ['Always exceed electrons gained', 'Always be fewer than electrons gained', 'Be ignored'])

add(91, 'Electrochemistry', 'Balancing Redox Equations', 'Hard',
    'In balancing a redox equation in acidic medium using the ion-electron method, oxygen atoms are typically balanced by adding:',
    'Water molecules (H2O)', ['Hydroxide ions (OH-) only', 'Extra oxygen gas', 'Hydrogen peroxide'])

add(92, 'Electrochemistry', 'Standard Hydrogen Electrode (SHE)', 'Medium',
    'The standard hydrogen electrode (SHE) is assigned a standard reduction potential of:',
    '0.00 V', ['1.00 V', '-1.00 V', '2.00 V'])

add(93, 'Electrochemistry', 'Standard Hydrogen Electrode (SHE)', 'Hard',
    'The standard hydrogen electrode is used as a reference to measure the:',
    'Standard reduction potentials of other electrodes', ['Rate of a redox reaction', 'Concentration of an acid', 'Solubility product of a salt'])

add(94, 'Electrochemistry', 'Redox Reactions', 'Medium',
    'In the reaction 2Na + Cl2 -> 2NaCl, sodium is:',
    'Oxidized, losing an electron to chlorine', ['Reduced, gaining an electron', 'Neither oxidized nor reduced', 'Acting as an oxidizing agent'])


# ============================================================
# CHEMICAL BONDING (14)  id 95-108
# ============================================================

add(95, 'Chemical Bonding', 'VSEPR Theory', 'Medium',
    'VSEPR theory predicts molecular shape based on:',
    'Minimizing repulsion between electron pairs around the central atom', ['The atomic mass of the central atom', 'The color of the compound', 'The boiling point of the compound'])

add(96, 'Chemical Bonding', 'VSEPR Theory', 'Medium',
    'According to VSEPR theory, a molecule with 4 bonding pairs and no lone pairs on the central atom (e.g., CH4) has a:',
    'Tetrahedral shape', ['Linear shape', 'Trigonal planar shape', 'Octahedral shape'])

add(97, 'Chemical Bonding', 'Sigma and Pi Bonds', 'Easy',
    'A sigma (sigma) bond is formed by:',
    'Head-on (axial) overlap of atomic orbitals', ['Sideways (lateral) overlap of atomic orbitals', 'Transfer of electrons between atoms', 'Overlap of d-orbitals only'])

add(98, 'Chemical Bonding', 'Sigma and Pi Bonds', 'Medium',
    'A pi (pi) bond is formed by:',
    'Sideways (lateral) overlap of parallel unhybridized p-orbitals', ['Head-on overlap of orbitals', 'Complete transfer of an electron', 'Overlap of s-orbitals only'])

add(99, 'Chemical Bonding', 'Sigma and Pi Bonds', 'Medium',
    'A carbon-carbon triple bond (as in alkynes) consists of:',
    'One sigma bond and two pi bonds', ['Three sigma bonds', 'Two sigma bonds and one pi bond', 'Three pi bonds'])

add(100, 'Chemical Bonding', 'Hybridization', 'Medium',
    'The hybridization of carbon in methane (CH4) is:',
    'sp3', ['sp2', 'sp', 'sp3d'])

add(101, 'Chemical Bonding', 'Hybridization', 'Medium',
    'The hybridization of carbon in ethene (C2H4), which has a double bond, is:',
    'sp2', ['sp3', 'sp', 'sp3d2'])

add(102, 'Chemical Bonding', 'Hybridization', 'Medium',
    'The hybridization of carbon in ethyne (C2H2), which has a triple bond, is:',
    'sp', ['sp2', 'sp3', 'sp3d'])

add(103, 'Chemical Bonding', 'Molecular Shapes (VSEPR Application)', 'Medium',
    'The molecular shape of ammonia (NH3), which has one lone pair on nitrogen, is:',
    'Trigonal pyramidal', ['Tetrahedral', 'Trigonal planar', 'Linear'])

add(104, 'Chemical Bonding', 'Molecular Shapes (VSEPR Application)', 'Medium',
    'The molecular shape of water (H2O), which has two lone pairs on oxygen, is:',
    'Bent (angular)', ['Linear', 'Tetrahedral', 'Trigonal pyramidal'])

add(105, 'Chemical Bonding', 'Dipole Moment', 'Medium',
    'A molecule has a net dipole moment when it has:',
    'Polar bonds that do not cancel out due to molecular geometry', ['Only nonpolar bonds', 'A perfectly symmetric shape with polar bonds that cancel', 'No charge separation at all'])

add(106, 'Chemical Bonding', 'Dipole Moment', 'Hard',
    'Carbon dioxide (CO2) is a nonpolar molecule overall, even though each C=O bond is polar, because:',
    'The molecule is linear, so the two bond dipoles cancel each other', ['Oxygen and carbon have identical electronegativities', 'It has no double bonds', 'It has a bent geometry'])

add(107, 'Chemical Bonding', 'Ionic Character of Covalent Bond', 'Medium',
    'A covalent bond gains partial ionic character when there is a difference in the:',
    'Electronegativities of the bonded atoms', ['Atomic masses of the bonded atoms', 'Number of neutrons in the bonded atoms', 'Physical states of the bonded atoms'])

add(108, 'Chemical Bonding', 'Bond Energy', 'Hard',
    'Bond energy is defined as the energy required to:',
    'Break one mole of a specific bond in the gaseous state', ['Form one mole of ionic crystal', 'Vaporize one mole of a liquid', 'Melt one mole of a solid'])


# ============================================================
# S AND P BLOCK ELEMENTS (12)  id 109-120
# ============================================================

add(109, 's and p Block Elements', 'Periodic Trends (Radii, IE, EA, Electronegativity)', 'Easy',
    'Atomic radius generally decreases across a period from left to right because:',
    'Nuclear charge increases while electrons are added to the same shell', ['Nuclear charge decreases across the period', 'The number of shells increases', 'Shielding effect increases sharply'])

add(110, 's and p Block Elements', 'Periodic Trends (Radii, IE, EA, Electronegativity)', 'Medium',
    'Ionization energy generally increases across a period because:',
    'Increasing nuclear charge holds valence electrons more tightly', ['Atomic size increases across the period', 'Electron shielding increases significantly', 'Electron affinity decreases'])

add(111, 's and p Block Elements', 'Periodic Trends (Radii, IE, EA, Electronegativity)', 'Medium',
    'Electronegativity generally increases across a period and decreases down a group; the most electronegative element is:',
    'Fluorine', ['Oxygen', 'Chlorine', 'Nitrogen'])

add(112, 's and p Block Elements', 's, p, d, f Block Demarcation', 'Medium',
    'Elements in which the last electron enters an s or p orbital of the outermost shell are classified as:',
    's and p block elements', ['d block elements', 'f block elements', 'Noble gases only'])

add(113, 's and p Block Elements', 's, p, d, f Block Demarcation', 'Medium',
    'The f-block elements are also known as the:',
    'Inner transition elements (lanthanides and actinides)', ['Alkali metals', 'Alkaline earth metals', 'Halogens'])

add(114, 's and p Block Elements', 'Group I Reactions', 'Easy',
    'Group I elements (alkali metals) react with water to form:',
    'A metal hydroxide and hydrogen gas', ['A metal oxide and oxygen gas', 'A metal chloride and chlorine gas', 'A metal carbonate and carbon dioxide'])

add(115, 's and p Block Elements', 'Group I Reactions', 'Medium',
    'Alkali metals are stored under kerosene oil because they:',
    'React vigorously with moisture and oxygen in air', ['Are radioactive', 'Sublime readily at room temperature', 'Are extremely dense'])

add(116, 's and p Block Elements', 'Group II Reactions', 'Medium',
    'Group II elements (alkaline earth metals) generally form ions with a charge of:',
    '+2', ['+1', '+3', '-2'])

add(117, 's and p Block Elements', 'Group II Reactions', 'Medium',
    'Magnesium reacts with dilute hydrochloric acid to produce:',
    'Magnesium chloride and hydrogen gas', ['Magnesium oxide and water', 'Magnesium hydroxide only', 'Magnesium carbonate and carbon dioxide'])

add(118, 's and p Block Elements', 'Group IV Reactions', 'Medium',
    'Down Group IV, the character of the elements changes from:',
    'Nonmetallic (carbon) to metallic (lead)', ['Metallic to nonmetallic', 'Metalloid to nonmetallic only', 'Gas to metal directly'])

add(119, 's and p Block Elements', 'Group IV Reactions', 'Hard',
    'Carbon, the first member of Group IV, differs from other group members mainly due to its:',
    'Small atomic size and ability to form strong pi-bonds (catenation)', ['Large atomic size', 'Metallic luster', 'Low ionization energy'])

add(120, 's and p Block Elements', 'Periodic Trends (Radii, IE, EA, Electronegativity)', 'Hard',
    'Electron affinity is generally defined as the energy change when:',
    'An isolated gaseous atom gains an electron to form a negative ion', ['An atom loses an electron to form a cation', 'Two atoms share electrons in a bond', 'A molecule absorbs a photon'])


# ============================================================
# TRANSITION ELEMENTS (6)  id 121-126
# ============================================================

add(121, 'Transition Elements', 'Electronic Structure of d-block', 'Easy',
    'Transition elements are characterized by having a partially filled:',
    'd subshell', ['s subshell', 'p subshell', 'f subshell'])

add(122, 'Transition Elements', 'Electronic Structure of d-block', 'Medium',
    'Transition metals commonly show variable oxidation states because:',
    'The energies of their (n-1)d and ns electrons are very close, allowing several to be lost', ['They have only one valence electron', 'They lack d-orbitals entirely', 'Their outer shell is always full'])

add(123, 'Transition Elements', 'Electronic Structure of d-block', 'Medium',
    'Transition metals and their compounds are often colored because of:',
    'd-d electronic transitions within partially filled d-orbitals', ['Complete absence of d-electrons', 's-orbital transitions only', 'Their high melting points'])

add(124, 'Transition Elements', 'Electronic Structure of d-block', 'Medium',
    'Many transition metals act as good catalysts mainly because of their ability to:',
    'Show variable oxidation states and form intermediate complexes', ['Remain chemically inert', 'Have very low melting points', 'Form only ionic compounds'])

add(125, 'Transition Elements', 'Electronic Structure of d-block', 'Hard',
    'Zinc is generally NOT classified as a true transition element because:',
    'Its d-subshell is completely filled (d10) in both the atom and its common ions', ['It has no d electrons at all', 'It is a nonmetal', 'It never forms colored compounds by exception'])

add(126, 'Transition Elements', 'Electronic Structure of d-block', 'Medium',
    'Transition metals typically form complex ions because their ions:',
    'Are small and highly charged with empty d-orbitals available to accept electron pairs', ['Are very large and weakly charged', 'Cannot accept any electron pairs', 'Have no vacant orbitals'])


# ============================================================
# FUNDAMENTAL PRINCIPLES OF ORGANIC CHEMISTRY (8)  id 127-134
# ============================================================

add(127, 'Fundamental Principles of Organic Chemistry', 'Definition and Classification of Organic Compounds', 'Easy',
    'Organic chemistry is generally defined as the study of compounds containing:',
    'Carbon (mainly bonded with hydrogen)', ['Only metals', 'Only ionic salts', 'Only inorganic acids'])

add(128, 'Fundamental Principles of Organic Chemistry', 'Definition and Classification of Organic Compounds', 'Medium',
    'Organic compounds made up of only carbon and hydrogen are called:',
    'Hydrocarbons', ['Carbohydrates', 'Alcohols', 'Carboxylic acids'])

add(129, 'Fundamental Principles of Organic Chemistry', 'Functional Groups', 'Easy',
    'A specific group of atoms within a molecule responsible for its characteristic chemical reactions is called a:',
    'Functional group', ['Homologous series', 'Isomer', 'Reaction mechanism'])

add(130, 'Fundamental Principles of Organic Chemistry', 'Functional Groups', 'Medium',
    'The functional group -OH, characteristic of alcohols, is called the:',
    'Hydroxyl group', ['Carbonyl group', 'Carboxyl group', 'Amino group'])

add(131, 'Fundamental Principles of Organic Chemistry', 'Functional Groups', 'Medium',
    'The functional group -COOH is characteristic of:',
    'Carboxylic acids', ['Aldehydes', 'Ketones', 'Alcohols'])

add(132, 'Fundamental Principles of Organic Chemistry', 'Isomerism (Stereoisomerism)', 'Medium',
    'Compounds with the same molecular formula but different structural arrangements are called:',
    'Isomers', ['Homologs', 'Allotropes', 'Polymers'])

add(133, 'Fundamental Principles of Organic Chemistry', 'Isomerism (Stereoisomerism)', 'Hard',
    'Stereoisomers are compounds that have the same structural formula but differ in:',
    'The spatial arrangement of their atoms', ['Their molecular formula', 'Their functional groups', 'The type of bonds present'])

add(134, 'Fundamental Principles of Organic Chemistry', 'Isomerism (Stereoisomerism)', 'Hard',
    'Cis-trans (geometric) isomerism arises in alkenes due to:',
    'Restricted rotation around the carbon-carbon double bond', ['Free rotation around a single bond', 'The presence of a triple bond', 'Ring formation only'])


# ============================================================
# CHEMISTRY OF HYDROCARBONS (18)  id 135-152
# ============================================================

add(135, 'Chemistry of Hydrocarbons', 'Nomenclature of Alkanes', 'Easy',
    'Alkanes are hydrocarbons characterized by having:',
    'Only single (sigma) carbon-carbon bonds', ['At least one carbon-carbon double bond', 'At least one carbon-carbon triple bond', 'A benzene ring'])

add(136, 'Chemistry of Hydrocarbons', 'Nomenclature of Alkanes', 'Medium',
    'The IUPAC name of the alkane with 5 carbon atoms (C5H12) is:',
    'Pentane', ['Butane', 'Hexane', 'Propane'])

add(137, 'Chemistry of Hydrocarbons', 'Free Radical Mechanism', 'Medium',
    'The halogenation of alkanes proceeds via a mechanism that is:',
    'Free radical substitution', ['Nucleophilic substitution', 'Electrophilic addition', 'Nucleophilic addition'])

add(138, 'Chemistry of Hydrocarbons', 'Free Radical Mechanism', 'Hard',
    'The first step in the free radical halogenation of methane, in which a halogen molecule splits into two atoms under UV light, is called:',
    'Initiation', ['Propagation', 'Termination', 'Substitution'])

add(139, 'Chemistry of Hydrocarbons', 'Preparation of Alkanes', 'Medium',
    'Alkanes can be prepared in the laboratory by the reduction of alkyl halides, or by the Wurtz reaction, which involves:',
    'Sodium metal reacting with an alkyl halide', ['Oxidation of an alcohol', 'Hydration of an alkene', 'Addition of hydrogen halide to an alkyne'])

add(140, 'Chemistry of Hydrocarbons', 'Nomenclature of Alkenes', 'Easy',
    'Alkenes are hydrocarbons that contain at least one:',
    'Carbon-carbon double bond', ['Carbon-carbon triple bond', 'Benzene ring', 'Only single bonds'])

add(141, 'Chemistry of Hydrocarbons', 'Shapes of Alkenes (Sigma/Pi Bonds)', 'Medium',
    'The carbon atoms of a carbon-carbon double bond in an alkene, along with the atoms directly attached to them, lie in a:',
    'Single plane (planar arrangement)', ['Tetrahedral arrangement', 'Linear arrangement', 'Pyramidal arrangement'])

add(142, 'Chemistry of Hydrocarbons', 'Structure and Reactivity of Alkenes', 'Medium',
    'Alkenes are generally more reactive than alkanes because of:',
    'The presence of a pi bond, which is weaker and more easily broken', ['Their higher molecular mass', 'Their lack of hydrogen atoms', 'Their higher boiling points'])

add(143, 'Chemistry of Hydrocarbons', 'Structure and Reactivity of Alkenes', 'Medium',
    'Alkenes characteristically undergo which type of reaction with reagents like Br2 or HBr?',
    'Electrophilic addition', ['Nucleophilic substitution', 'Free radical substitution', 'Elimination'])

add(144, 'Chemistry of Hydrocarbons', "MOT of Benzene, Resonance, Resonance Energy", 'Hard',
    'According to molecular orbital theory, the extra stability of benzene arises from:',
    'Delocalization of pi electrons over all six carbon atoms of the ring', ['Localized double bonds fixed between alternating carbons', 'The presence of only sigma bonds', 'Its high molecular mass'])

add(145, 'Chemistry of Hydrocarbons', "MOT of Benzene, Resonance, Resonance Energy", 'Medium',
    'The resonance energy of benzene is the extra stability it possesses compared to a hypothetical structure with:',
    'Three fixed, alternating (localized) double bonds', ['Three single bonds only', 'No pi electrons at all', 'A non-planar ring structure'])

add(146, 'Chemistry of Hydrocarbons', 'Reactivity of Benzene', 'Medium',
    'Unlike alkenes, benzene characteristically undergoes which type of reaction to preserve its aromatic stability?',
    'Electrophilic substitution', ['Electrophilic addition', 'Free radical addition', 'Nucleophilic addition'])

add(147, 'Chemistry of Hydrocarbons', 'Chemical Reactions of Benzene', 'Medium',
    'The reaction of benzene with an alkyl halide in the presence of anhydrous AlCl3 is called:',
    'Friedel-Crafts alkylation', ['Friedel-Crafts acylation', 'Nitration', 'Sulfonation'])

add(148, 'Chemistry of Hydrocarbons', 'Effect of Substituents on Benzene', 'Hard',
    'An -OH group attached to a benzene ring is an activating group that directs an incoming electrophile to the:',
    'Ortho and para positions', ['Meta position only', 'Ipso position only', 'No specific position (random)'])

add(149, 'Chemistry of Hydrocarbons', 'Nomenclature of Alkynes', 'Easy',
    'Alkynes are hydrocarbons that contain at least one:',
    'Carbon-carbon triple bond', ['Carbon-carbon double bond', 'Benzene ring', 'Only single bonds'])

add(150, 'Chemistry of Hydrocarbons', 'Acidity of Alkynes', 'Hard',
    'Terminal alkynes (with a hydrogen directly on the triple-bonded carbon) show weak acidic character because:',
    'The sp-hybridized carbon holds the bonding electrons closer, stabilizing the resulting carbanion', ['The triple bond is very weak and breaks easily', 'They contain oxygen atoms', 'They are highly polar molecules'])

add(151, 'Chemistry of Hydrocarbons', 'Preparation of Alkynes', 'Medium',
    'Ethyne (acetylene) can be prepared in the laboratory by treating calcium carbide with:',
    'Water', ['Dilute hydrochloric acid', 'Sodium hydroxide', 'Concentrated sulfuric acid'])

add(152, 'Chemistry of Hydrocarbons', 'Substitution vs Addition Reactions', 'Hard',
    'The key structural reason alkanes undergo substitution reactions while alkenes/alkynes undergo addition reactions is that:',
    'Alkanes have only strong sigma bonds while alkenes/alkynes have reactive, breakable pi bonds', ['Alkanes contain more carbon atoms', 'Alkenes/alkynes have no hydrogen atoms to substitute', 'Alkanes are always liquids'])


# ============================================================
# ALKYL HALIDES (8)  id 153-160
# ============================================================

add(153, 'Alkyl Halides', 'Nomenclature, Structure, Reactivity', 'Easy',
    'Alkyl halides are organic compounds in which a halogen atom is bonded to a(n):',
    'sp3-hybridized (alkyl) carbon atom', ['Aromatic ring carbon directly', 'Carbonyl carbon', 'Carboxylic acid carbon'])

add(154, 'Alkyl Halides', 'Nomenclature, Structure, Reactivity', 'Medium',
    'A tertiary alkyl halide is one in which the halogen-bearing carbon is attached to:',
    'Three other carbon atoms', ['One other carbon atom', 'Two other carbon atoms', 'No other carbon atoms'])

add(155, 'Alkyl Halides', 'Nucleophilic Substitution Mechanisms', 'Medium',
    'In an SN2 (bimolecular nucleophilic substitution) reaction, the nucleophile attacks the substrate:',
    'From the side opposite to the leaving group, in a single concerted step', ['From the same side as the leaving group', 'After the leaving group has fully departed', 'Only after forming a stable carbocation'])

add(156, 'Alkyl Halides', 'Nucleophilic Substitution Mechanisms', 'Hard',
    'An SN1 (unimolecular nucleophilic substitution) reaction proceeds via the formation of a:',
    'Carbocation intermediate', ['Concerted transition state with no intermediate', 'Free radical intermediate', 'Carbanion intermediate'])

add(157, 'Alkyl Halides', 'Nucleophilic Substitution Mechanisms', 'Hard',
    'Tertiary alkyl halides typically react via the SN1 mechanism rather than SN2 mainly because:',
    'Steric hindrance disfavors backside attack, while the resulting tertiary carbocation is relatively stable', ['They have no leaving group', 'They lack a carbon skeleton', 'Primary carbocations are more stable than tertiary'])

add(158, 'Alkyl Halides', 'Elimination Mechanisms', 'Medium',
    'An E2 elimination reaction removes a hydrogen and a leaving group from adjacent carbons in a:',
    'Single concerted step, forming an alkene', ['Two separate, unrelated steps', 'Process that never forms a double bond', 'Reaction that requires no base'])

add(159, 'Alkyl Halides', 'Elimination Mechanisms', 'Hard',
    'An E1 elimination reaction proceeds through the same type of intermediate as which substitution mechanism?',
    'SN1 (a carbocation intermediate)', ['SN2 (a concerted transition state)', 'Free radical substitution', 'Electrophilic addition'])

add(160, 'Alkyl Halides', 'Nomenclature, Structure, Reactivity', 'Medium',
    'Alkyl halides are generally more reactive than the corresponding alkanes because of the:',
    'Polar carbon-halogen bond, making the carbon electrophilic', ['Absence of hydrogen atoms', 'Nonpolar carbon-carbon bonds present', 'Very high boiling points of alkyl halides'])


# ============================================================
# ALCOHOLS AND PHENOLS (10)  id 161-170
# ============================================================

add(161, 'Alcohols and Phenols', 'Nomenclature, Structure, Reactivity of Alcohols', 'Easy',
    'Alcohols are organic compounds containing a hydroxyl (-OH) group attached to a(n):',
    'sp3-hybridized (alkyl) carbon atom', ['Aromatic ring carbon directly', 'Carbonyl carbon', 'Alkyne carbon'])

add(162, 'Alcohols and Phenols', 'Nomenclature, Structure, Reactivity of Alcohols', 'Medium',
    'A secondary alcohol is one in which the -OH bearing carbon is attached to:',
    'Two other carbon atoms', ['One other carbon atom', 'Three other carbon atoms', 'No other carbon atom'])

add(163, 'Alcohols and Phenols', 'Chemistry of Alcohols (Ethers, Esters)', 'Medium',
    'The reaction of an alcohol with a carboxylic acid in the presence of an acid catalyst, forming an ester and water, is called:',
    'Esterification', ['Saponification', 'Hydrolysis', 'Oxidation'])

add(164, 'Alcohols and Phenols', 'Chemistry of Alcohols (Ethers, Esters)', 'Medium',
    'Two alcohol molecules can be dehydrated (in presence of concentrated H2SO4 at a lower temperature) to form:',
    'An ether', ['An alkene', 'An aldehyde', 'A carboxylic acid'])

add(165, 'Alcohols and Phenols', 'Nomenclature, Structure, Reactivity of Phenols', 'Easy',
    'Phenols are organic compounds in which a hydroxyl (-OH) group is directly attached to a(n):',
    'Aromatic (benzene) ring carbon', ['sp3-hybridized alkyl carbon', 'Carbonyl carbon', 'Alkyne carbon'])

add(166, 'Alcohols and Phenols', 'Electrophilic Aromatic Substitution in Phenols', 'Medium',
    "Phenol reacts more readily than benzene in electrophilic aromatic substitution because the -OH group:",
    'Donates electron density into the ring through resonance, activating it', ['Withdraws electron density strongly, deactivating the ring', 'Has no effect on the ring electron density', 'Blocks all substitution positions'])

add(167, 'Alcohols and Phenols', 'Alcohol vs Phenol', 'Medium',
    'Phenol is a stronger acid than a typical aliphatic alcohol mainly because:',
    'Its conjugate base (phenoxide ion) is stabilized by resonance delocalization into the ring', ['It contains more carbon atoms', 'Its O-H bond is weaker due to hydrogen bonding alone', 'Alcohols are always basic, not acidic'])

add(168, 'Alcohols and Phenols', 'Alcohol vs Phenol', 'Medium',
    'Unlike simple alcohols, phenol reacts with aqueous sodium hydroxide (NaOH) because phenol is:',
    'Acidic enough to be neutralized by a strong base', ['Basic in nature', 'Completely inert to bases', 'Only soluble in nonpolar solvents'])

add(169, 'Alcohols and Phenols', 'Nomenclature, Structure, Reactivity of Alcohols', 'Medium',
    'Primary alcohols are oxidized by an oxidizing agent like acidified potassium dichromate first to an aldehyde, and then further to a:',
    'Carboxylic acid', ['Ketone', 'Ether', 'Alkane'])

add(170, 'Alcohols and Phenols', 'Chemistry of Alcohols (Ethers, Esters)', 'Hard',
    'Secondary alcohols, upon oxidation with an oxidizing agent, are converted to:',
    'Ketones', ['Carboxylic acids directly', 'Aldehydes', 'Ethers'])


# ============================================================
# ALDEHYDES AND KETONES (10)  id 171-180
# ============================================================

add(171, 'Aldehydes and Ketones', 'Nomenclature and Structure', 'Easy',
    'The functional group common to both aldehydes and ketones is the:',
    'Carbonyl group (C=O)', ['Hydroxyl group (-OH)', 'Carboxyl group (-COOH)', 'Amino group (-NH2)'])

add(172, 'Aldehydes and Ketones', 'Nomenclature and Structure', 'Medium',
    'In an aldehyde, the carbonyl carbon is bonded to at least one:',
    'Hydrogen atom', ['Halogen atom always', 'Second carbonyl group', 'Nitrogen atom'])

add(173, 'Aldehydes and Ketones', 'Preparation', 'Medium',
    'Aldehydes can be prepared by the controlled oxidation of:',
    'Primary alcohols', ['Secondary alcohols', 'Tertiary alcohols', 'Carboxylic acids'])

add(174, 'Aldehydes and Ketones', 'Preparation', 'Medium',
    'Ketones can be prepared by the oxidation of:',
    'Secondary alcohols', ['Primary alcohols', 'Tertiary alcohols', 'Alkanes'])

add(175, 'Aldehydes and Ketones', 'Reactivity of Aldehydes and Ketones', 'Medium',
    'Aldehydes are generally more reactive toward nucleophilic addition than ketones mainly because:',
    'Aldehydes have less steric hindrance and a more electrophilic carbonyl carbon', ['Ketones have no carbonyl carbon', 'Aldehydes have two alkyl groups shielding the carbonyl', 'Ketones are more polar than aldehydes'])

add(176, 'Aldehydes and Ketones', 'Nucleophilic Addition Reactions', 'Medium',
    'The characteristic reaction type of the carbonyl group in aldehydes and ketones is:',
    'Nucleophilic addition', ['Electrophilic addition', 'Free radical substitution', 'Electrophilic substitution'])

add(177, 'Aldehydes and Ketones', 'Reduction to Alcohols', 'Medium',
    'Reduction of an aldehyde (e.g., using NaBH4) produces a:',
    'Primary alcohol', ['Secondary alcohol', 'Tertiary alcohol', 'Carboxylic acid'])

add(178, 'Aldehydes and Ketones', 'Reduction to Alcohols', 'Medium',
    'Reduction of a ketone produces a:',
    'Secondary alcohol', ['Primary alcohol', 'Tertiary alcohol', 'Aldehyde'])

add(179, 'Aldehydes and Ketones', 'Oxidation Reactions', 'Medium',
    "Tollens' reagent (ammoniacal silver nitrate) is used to distinguish aldehydes from ketones because aldehydes:",
    'Are easily oxidized, reducing Ag+ to metallic silver (a silver mirror)', ['Cannot be oxidized at all', 'Reduce ketones instead', 'Do not react with any oxidizing agent'])

add(180, 'Aldehydes and Ketones', 'Oxidation Reactions', 'Hard',
    "Ketones generally do NOT give a positive test with Tollens' or Fehling's reagent because they:",
    'Lack the easily oxidizable hydrogen present on the carbonyl carbon of aldehydes', ['Have no carbonyl group', 'Are always more reactive than aldehydes', 'React explosively with mild oxidizing agents instead'])


# ============================================================
# CARBOXYLIC ACIDS (8)  id 181-188
# ============================================================

add(181, 'Carboxylic Acids', 'Nomenclature, Structure, Preparation', 'Easy',
    'Carboxylic acids contain the functional group:',
    '-COOH (carboxyl group)', ['-OH (hydroxyl group)', '-CHO (aldehyde group)', '-NH2 (amino group)'])

add(182, 'Carboxylic Acids', 'Nomenclature, Structure, Preparation', 'Medium',
    'Carboxylic acids can be prepared by the oxidation of:',
    'Primary alcohols or aldehydes', ['Secondary alcohols only', 'Tertiary alcohols only', 'Ketones'])

add(183, 'Carboxylic Acids', 'Reactivity of Carboxylic Acids', 'Medium',
    'Carboxylic acids are acidic mainly because their conjugate base, the carboxylate ion, is stabilized by:',
    'Resonance delocalization of the negative charge over two oxygen atoms', ['A very strong O-H bond', 'The presence of an alkyl group only', 'Hydrogen bonding with water alone'])

add(184, 'Carboxylic Acids', 'Reactivity of Carboxylic Acids', 'Medium',
    'Carboxylic acids react with sodium bicarbonate (NaHCO3) to release:',
    'Carbon dioxide gas', ['Hydrogen gas', 'Oxygen gas', 'Chlorine gas'])

add(185, 'Carboxylic Acids', 'Conversion to Derivatives (Acyl Halides, Anhydrides, Esters)', 'Medium',
    'Treating a carboxylic acid with thionyl chloride (SOCl2) converts it into a(n):',
    'Acyl (acid) chloride', ['Ester', 'Anhydride', 'Amide only, never a chloride'])

add(186, 'Carboxylic Acids', 'Conversion to Derivatives (Acyl Halides, Anhydrides, Esters)', 'Medium',
    'Two carboxylic acid molecules can be dehydrated to form a(n):',
    'Acid (carboxylic) anhydride', ['Acyl chloride', 'Ether', 'Ketone'])

add(187, 'Carboxylic Acids', 'Conversion to Derivatives (Acyl Halides, Anhydrides, Esters)', 'Medium',
    'The reaction of a carboxylic acid with an alcohol, catalyzed by an acid, to form an ester is called:',
    'Esterification', ['Saponification', 'Hydrolysis', 'Decarboxylation'])

add(188, 'Carboxylic Acids', 'Nomenclature, Structure, Preparation', 'Hard',
    'Carboxylic acids generally have higher boiling points than alcohols of comparable molecular mass because carboxylic acids:',
    'Form stronger, more extensive hydrogen-bonded dimers', ['Have weaker intermolecular forces', 'Are always nonpolar', 'Have a lower molecular mass'])


# ============================================================
# MACROMOLECULES (6)  id 189-194
# ============================================================

add(189, 'Macromolecules', 'Classification and Structure of Proteins', 'Easy',
    'Proteins are macromolecules built from monomer units called:',
    'Amino acids', ['Monosaccharides', 'Nucleotides', 'Fatty acids'])

add(190, 'Macromolecules', 'Classification and Structure of Proteins', 'Medium',
    'Amino acids are linked together in a protein chain by:',
    'Peptide bonds', ['Glycosidic bonds', 'Ester bonds', 'Phosphodiester bonds'])

add(191, 'Macromolecules', 'Classification and Structure of Proteins', 'Medium',
    'The specific sequence of amino acids in a protein chain defines its:',
    'Primary structure', ['Secondary structure', 'Tertiary structure', 'Quaternary structure'])

add(192, 'Macromolecules', 'Importance of Proteins', 'Easy',
    'Proteins in the human body perform important roles including acting as:',
    'Enzymes, structural components, and transport molecules', ['Only as an energy-storage molecule', 'Only as genetic material', 'Only as a solvent'])

add(193, 'Macromolecules', 'Enzymes as Biocatalysts', 'Medium',
    'Enzymes are biological catalysts that are chemically:',
    'Mostly globular proteins', ['Always carbohydrates', 'Always lipids', 'Always nucleic acids'])

add(194, 'Macromolecules', 'Enzymes as Biocatalysts', 'Hard',
    'Enzymes increase the rate of biochemical reactions by:',
    'Lowering the activation energy of the reaction via a specific active site', ['Increasing the activation energy needed', 'Being permanently consumed in the reaction', 'Shifting the reaction equilibrium constant'])


# ============================================================
# INDUSTRIAL CHEMISTRY (6)  id 195-200
# ============================================================

add(195, 'Industrial Chemistry', 'Adhesives', 'Easy',
    'Adhesives are substances used industrially to:',
    'Bond two surfaces together', ['Dissolve other chemicals', 'Bleach fabrics', 'Conduct electricity'])

add(196, 'Industrial Chemistry', 'Dyes', 'Medium',
    'A dye is a colored substance that has an affinity for a substrate (like fabric) and, chemically, typically contains a:',
    'Chromophore group responsible for its color', ['Carboxyl group only', 'Noble gas core', 'Metallic lattice structure'])

add(197, 'Industrial Chemistry', 'Polymers (Condensation and Addition)', 'Medium',
    'Polymers formed by the repeated joining of monomer units with no small molecule (like water) released are called:',
    'Addition polymers', ['Condensation polymers', 'Natural polymers only', 'Inorganic polymers'])

add(198, 'Industrial Chemistry', 'Polymers (Condensation and Addition)', 'Medium',
    'Polymers formed by the joining of monomers with the elimination of a small molecule such as water at each step are called:',
    'Condensation polymers', ['Addition polymers', 'Elastomers exclusively', 'Monomeric polymers'])

add(199, 'Industrial Chemistry', 'Polymers (Condensation and Addition)', 'Medium',
    'Polyethylene, formed from the repeated addition of ethene monomers, is an example of a(n):',
    'Addition polymer', ['Condensation polymer', 'Natural protein polymer', 'Inorganic ceramic'])

add(200, 'Industrial Chemistry', 'Dyes', 'Hard',
    'Azo dyes, a major class of synthetic dyes, are characterized by the presence of the functional linkage:',
    '-N=N- (azo group) connecting two aromatic rings', ['-COOH (carboxyl group)', '-OH (hydroxyl group) alone', '-CHO (aldehyde group)'])


# ------------------------------------------------------------
# Build QUESTIONS from RAW with a balanced, shuffled answer key
# (a plain round-robin A,B,C,D,A,B,C,D... is itself a gameable pattern,
# so the 50/50/50/50 assignment is shuffled with a fixed seed instead)
# ------------------------------------------------------------
import random as _random

_LETTERS = ['A', 'B', 'C', 'D']
_letter_pool = _LETTERS * (len(RAW) // 4)
_random.Random(42).shuffle(_letter_pool)

QUESTIONS = []
for idx, (qid, topic, subtopic, difficulty, question, correct, distractors) in enumerate(RAW):
    correct_letter = _letter_pool[idx]
    texts = list(distractors)
    texts.insert(_LETTERS.index(correct_letter), correct)
    options = {letter: text for letter, text in zip(_LETTERS, texts)}
    QUESTIONS.append({
        "id": qid,
        "subject": 'Chemistry',
        "topic": topic,
        "subtopic": subtopic,
        "difficulty": difficulty,
        "question": question,
        "options": options,
        "answer": correct_letter,
    })


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
