"""
MDCAT Physics-Only Mock Test
=============================
Full-length Physics-only mock test: 200 MCQs
Covers: Measurements & Units, Vectors & Equilibrium, Kinematics, Dynamics,
Work/Energy/Power, Circular Motion & Gravitation, Fluid Mechanics,
Oscillations (SHM), Waves & Sound, Thermodynamics, Electrostatics,
Current Electricity, Electromagnetism, Electromagnetic Induction & AC,
Electronics, Modern Physics (Atomic), Nuclear Physics, and Optics.

Difficulty mix (approx): 30% Easy / 50% Medium / 20% Hard, distributed throughout.

Includes 5 image/diagram-based questions. Each such question has an "image" key
giving a relative path to a PNG diagram that must be viewed alongside the
question (images/ subfolder, shipped alongside this file). Diagrams: a vector
drawn on a coordinate grid with its components labeled, a series-then-parallel
resistor circuit, a current-carrying wire in a uniform magnetic field, a
step-up transformer with labeled primary/secondary coils, and a concave-mirror
ray diagram (object between F and the mirror).

Each question is a dict:
    id, subject, topic, difficulty, question, [image], options (A-D), answer (correct letter)

Run this file directly to print a summary / sanity-check the paper.
"""

QUESTIONS = [
# ============================================================
# MEASUREMENTS & UNITS (10 questions) - id 1-10
# ============================================================

{"id":1,"subject":"Physics","topic":"Measurements & Units","difficulty":"Easy",
 "question":"The SI unit of electric current is the:",
 "options":{"A":"Volt","B":"Ampere","C":"Ohm","D":"Coulomb"},"answer":"B"},
{"id":2,"subject":"Physics","topic":"Measurements & Units","difficulty":"Easy",
 "question":"Which of the following is a fundamental (base) quantity?",
 "options":{"A":"Force","B":"Velocity","C":"Energy","D":"Mass"},"answer":"D"},
{"id":3,"subject":"Physics","topic":"Measurements & Units","difficulty":"Easy",
 "question":"The number of significant figures in the measurement 0.00420 is:",
 "options":{"A":"2","B":"5","C":"3","D":"6"},"answer":"C"},
{"id":4,"subject":"Physics","topic":"Measurements & Units","difficulty":"Medium",
 "question":"The dimensional formula of force is:",
 "options":{"A":"[MLT^-1]","B":"[ML^2T^-2]","C":"[ML^-1T^-2]","D":"[MLT^-2]"},"answer":"D"},
{"id":5,"subject":"Physics","topic":"Measurements & Units","difficulty":"Medium",
 "question":"Which pair of physical quantities has the same dimensions?",
 "options":{"A":"Work and Power","B":"Force and Pressure","C":"Work and Torque","D":"Momentum and Force"},"answer":"C"},
{"id":6,"subject":"Physics","topic":"Measurements & Units","difficulty":"Easy",
 "question":"The instrument used to measure very small lengths, such as the diameter of a thin wire, with high precision is the:",
 "options":{"A":"Meter rule","B":"Measuring tape","C":"Screw gauge","D":"Protractor"},"answer":"C"},
{"id":7,"subject":"Physics","topic":"Measurements & Units","difficulty":"Medium",
 "question":"A vernier caliper has 20 divisions on its vernier scale matching 19 main scale divisions of 1 mm each. What is its least count?",
 "options":{"A":"0.05 mm","B":"0.01 mm","C":"0.1 mm","D":"1 mm"},"answer":"A"},
{"id":8,"subject":"Physics","topic":"Measurements & Units","difficulty":"Hard",
 "question":"A physical quantity Q is calculated as Q = A^2 * B / C^3. If the percentage errors in A, B, and C are 2%, 3%, and 1% respectively, what is the approximate percentage error in Q?",
 "options":{"A":"10%","B":"6%","C":"8%","D":"12%"},"answer":"A"},
{"id":9,"subject":"Physics","topic":"Measurements & Units","difficulty":"Easy",
 "question":"Which of the following is a derived unit?",
 "options":{"A":"Meter","B":"Newton","C":"Kilogram","D":"Second"},"answer":"B"},
{"id":10,"subject":"Physics","topic":"Measurements & Units","difficulty":"Medium",
 "question":"The order of magnitude of Avogadro's number (6.022 x 10^23) is:",
 "options":{"A":"10^23","B":"10^20","C":"10^22","D":"10^24"},"answer":"A"},

# ============================================================
# VECTORS & EQUILIBRIUM (10 questions) - id 11-20
# ============================================================

{"id":11,"subject":"Physics","topic":"Vectors & Equilibrium","difficulty":"Easy",
 "question":"A vector quantity has:",
 "options":{"A":"Magnitude only","B":"Direction only","C":"Both magnitude and direction","D":"Neither magnitude nor direction"},"answer":"C"},
{"id":12,"subject":"Physics","topic":"Vectors & Equilibrium","difficulty":"Easy",
 "question":"Which of the following is a scalar quantity?",
 "options":{"A":"Velocity","B":"Displacement","C":"Acceleration","D":"Speed"},"answer":"D"},
{"id":13,"subject":"Physics","topic":"Vectors & Equilibrium","difficulty":"Medium",
 "question":"The resultant of two vectors of magnitude 3 N and 4 N acting at right angles to each other is:",
 "options":{"A":"1 N","B":"7 N","C":"5 N","D":"12 N"},"answer":"C"},
{"id":14,"subject":"Physics","topic":"Vectors & Equilibrium","difficulty":"Medium",
 "question":"Two forces of equal magnitude F act on a point at an angle of 120 degrees to each other. The magnitude of their resultant is:",
 "options":{"A":"2F","B":"F","C":"F/2","D":"0"},"answer":"B"},
{"id":15,"subject":"Physics","topic":"Vectors & Equilibrium","difficulty":"Hard",
 "question":"The dot product of two non-zero vectors A and B is zero. This means the vectors are:",
 "options":{"A":"Parallel","B":"Anti-parallel","C":"Equal in magnitude","D":"Perpendicular"},"answer":"D"},
{"id":16,"subject":"Physics","topic":"Vectors & Equilibrium","difficulty":"Medium",
 "question":"The cross product of two parallel vectors is:",
 "options":{"A":"Maximum","B":"Equal to their dot product","C":"Undefined","D":"Zero"},"answer":"D"},
{"id":17,"subject":"Physics","topic":"Vectors & Equilibrium","difficulty":"Easy",
 "question":"A rigid body is in complete equilibrium when:",
 "options":{"A":"The net force and net torque acting on it are both zero","B":"It is always at rest","C":"It is moving with increasing speed","D":"Only the net force is zero, regardless of torque"},"answer":"A"},
{"id":18,"subject":"Physics","topic":"Vectors & Equilibrium","difficulty":"Medium",
 "question":"Three concurrent forces of 3 N, 4 N, and 5 N act on a body such that it remains in equilibrium. These forces must:",
 "options":{"A":"Be parallel to each other","B":"All act in exactly the same direction","C":"Form a closed triangle when added head-to-tail","D":"Have no relationship to each other"},"answer":"C"},
{"id":19,"subject":"Physics","topic":"Vectors & Equilibrium","difficulty":"Hard",
 "question":"The diagram shows a vector A drawn on a coordinate grid, with its components labeled Ax = 6 and Ay = 8 along the horizontal and vertical axes. Based on the diagram, what is the magnitude of vector A and its angle from the x-axis?",
 "image":"images/q_vector_components_diagram.png",
 "options":{"A":"10, 53.1 degrees","B":"14, 45 degrees","C":"10, 36.9 degrees","D":"2, 53.1 degrees"},"answer":"A"},
{"id":20,"subject":"Physics","topic":"Vectors & Equilibrium","difficulty":"Medium",
 "question":"The component of a force of 10 N along a direction making a 60-degree angle with the force is:",
 "options":{"A":"5 N","B":"10 N","C":"8.66 N","D":"0 N"},"answer":"A"},

# ============================================================
# KINEMATICS (14 questions) - id 21-34
# ============================================================

{"id":21,"subject":"Physics","topic":"Kinematics","difficulty":"Easy",
 "question":"A car covers 40 km in 2 hours at constant speed. What is its speed?",
 "options":{"A":"10 km/h","B":"80 km/h","C":"5 km/h","D":"20 km/h"},"answer":"D"},
{"id":22,"subject":"Physics","topic":"Kinematics","difficulty":"Easy",
 "question":"Displacement is best defined as:",
 "options":{"A":"The shortest straight-line distance between initial and final position, with direction","B":"The total path length traveled","C":"Speed multiplied by time","D":"A scalar quantity only"},"answer":"A"},
{"id":23,"subject":"Physics","topic":"Kinematics","difficulty":"Medium",
 "question":"A car accelerates uniformly from 15 m/s to 35 m/s in 4 seconds. What is its acceleration?",
 "options":{"A":"5 m/s^2","B":"8.75 m/s^2","C":"20 m/s^2","D":"4 m/s^2"},"answer":"A"},
{"id":24,"subject":"Physics","topic":"Kinematics","difficulty":"Medium",
 "question":"An object starts from rest and accelerates uniformly at 3 m/s^2. How far does it travel in 5 seconds?",
 "options":{"A":"15 m","B":"7.5 m","C":"37.5 m","D":"75 m"},"answer":"C"},
{"id":25,"subject":"Physics","topic":"Kinematics","difficulty":"Hard",
 "question":"A ball is thrown vertically upward with an initial velocity of 20 m/s (g = 10 m/s^2). How long does it take to return to its starting point?",
 "options":{"A":"2 s","B":"1 s","C":"10 s","D":"4 s"},"answer":"D"},
{"id":26,"subject":"Physics","topic":"Kinematics","difficulty":"Hard",
 "question":"A projectile is launched at 30 m/s at an angle of 30 degrees above the horizontal (g = 10 m/s^2). What is its maximum height?",
 "options":{"A":"15 m","B":"22.5 m","C":"45 m","D":"11.25 m"},"answer":"D"},
{"id":27,"subject":"Physics","topic":"Kinematics","difficulty":"Easy",
 "question":"Which of the following is a vector quantity?",
 "options":{"A":"Velocity","B":"Speed","C":"Distance","D":"Time"},"answer":"A"},
{"id":28,"subject":"Physics","topic":"Kinematics","difficulty":"Medium",
 "question":"A car travels at 20 m/s for 10 s, then decelerates uniformly to rest in 5 s. What is the total distance traveled?",
 "options":{"A":"200 m","B":"150 m","C":"250 m","D":"300 m"},"answer":"C"},
{"id":29,"subject":"Physics","topic":"Kinematics","difficulty":"Medium",
 "question":"The slope of a velocity-time graph represents:",
 "options":{"A":"Acceleration","B":"Displacement","C":"Speed","D":"Distance"},"answer":"A"},
{"id":30,"subject":"Physics","topic":"Kinematics","difficulty":"Easy",
 "question":"The area under a velocity-time graph represents:",
 "options":{"A":"Force","B":"Acceleration","C":"Jerk","D":"Displacement"},"answer":"D"},
{"id":31,"subject":"Physics","topic":"Kinematics","difficulty":"Hard",
 "question":"A stone is dropped from a tower and takes 5 seconds to reach the ground (g = 10 m/s^2). What is the height of the tower?",
 "options":{"A":"125 m","B":"50 m","C":"25 m","D":"250 m"},"answer":"A"},
{"id":32,"subject":"Physics","topic":"Kinematics","difficulty":"Medium",
 "question":"Two cars A and B start from the same point at the same time; A moves at a constant 20 m/s while B starts from rest with acceleration 4 m/s^2. After how many seconds will B catch up to A?",
 "options":{"A":"5 s","B":"8 s","C":"10 s","D":"4 s"},"answer":"C"},
{"id":33,"subject":"Physics","topic":"Kinematics","difficulty":"Easy",
 "question":"For an object moving with uniform velocity, its acceleration is:",
 "options":{"A":"Zero","B":"Increasing","C":"Constant but non-zero","D":"Negative"},"answer":"A"},
{"id":34,"subject":"Physics","topic":"Kinematics","difficulty":"Hard",
 "question":"A particle moves along a straight line with position x = 2t^2 - 3t + 1 (x in meters, t in seconds). What is its velocity at t = 2 s?",
 "options":{"A":"5 m/s","B":"8 m/s","C":"4 m/s","D":"1 m/s"},"answer":"A"},

# ============================================================
# DYNAMICS (14 questions) - id 35-48
# ============================================================

{"id":35,"subject":"Physics","topic":"Dynamics","difficulty":"Easy",
 "question":"Newton's first law is also known as the law of:",
 "options":{"A":"Action and reaction","B":"Conservation of momentum","C":"Gravitation","D":"Inertia"},"answer":"D"},
{"id":36,"subject":"Physics","topic":"Dynamics","difficulty":"Medium",
 "question":"A net force of 15 N acts on a 3 kg object. What is its acceleration?",
 "options":{"A":"45 m/s^2","B":"5 m/s^2","C":"0.2 m/s^2","D":"18 m/s^2"},"answer":"B"},
{"id":37,"subject":"Physics","topic":"Dynamics","difficulty":"Easy",
 "question":"According to Newton's third law, when object A exerts a force on object B, object B:",
 "options":{"A":"Remains stationary","B":"Exerts an equal and opposite force on A","C":"Exerts a smaller force back on A","D":"Exerts no force on A"},"answer":"B"},
{"id":38,"subject":"Physics","topic":"Dynamics","difficulty":"Medium",
 "question":"The momentum of a 5 kg object moving at 4 m/s is:",
 "options":{"A":"1.25 kg m/s","B":"9 kg m/s","C":"0.8 kg m/s","D":"20 kg m/s"},"answer":"D"},
{"id":39,"subject":"Physics","topic":"Dynamics","difficulty":"Medium",
 "question":"According to the law of conservation of momentum, in a closed system with no external forces, the total momentum:",
 "options":{"A":"Remains constant","B":"Increases over time","C":"Decreases over time","D":"Becomes zero"},"answer":"A"},
{"id":40,"subject":"Physics","topic":"Dynamics","difficulty":"Hard",
 "question":"A 2 kg ball moving at 6 m/s collides head-on with a stationary 4 kg ball and sticks to it. What is their common velocity immediately after the collision?",
 "options":{"A":"1 m/s","B":"3 m/s","C":"4 m/s","D":"2 m/s"},"answer":"D"},
{"id":41,"subject":"Physics","topic":"Dynamics","difficulty":"Easy",
 "question":"Friction that opposes the start of motion between two surfaces in contact is called:",
 "options":{"A":"Kinetic friction","B":"Rolling friction","C":"Fluid friction","D":"Static friction"},"answer":"D"},
{"id":42,"subject":"Physics","topic":"Dynamics","difficulty":"Medium",
 "question":"A 5 kg block on a horizontal surface experiences a friction force of 10 N when a horizontal force of 25 N is applied. What is the block's acceleration?",
 "options":{"A":"5 m/s^2","B":"3 m/s^2","C":"2 m/s^2","D":"7 m/s^2"},"answer":"B"},
{"id":43,"subject":"Physics","topic":"Dynamics","difficulty":"Hard",
 "question":"A 6 kg block is pushed with a horizontal force of 30 N across a surface with a coefficient of kinetic friction of 0.2 (g = 10 m/s^2). What is the block's acceleration?",
 "options":{"A":"3 m/s^2","B":"5 m/s^2","C":"1 m/s^2","D":"2 m/s^2"},"answer":"A"},
{"id":44,"subject":"Physics","topic":"Dynamics","difficulty":"Medium",
 "question":"The impulse experienced by an object equals:",
 "options":{"A":"Its mass times velocity","B":"Its weight times time","C":"The change in its momentum","D":"Its kinetic energy"},"answer":"C"},
{"id":45,"subject":"Physics","topic":"Dynamics","difficulty":"Easy",
 "question":"Weight is defined as:",
 "options":{"A":"The amount of matter in an object","B":"A measure of an object's inertia","C":"The same as mass in all cases","D":"The gravitational force acting on an object's mass"},"answer":"D"},
{"id":46,"subject":"Physics","topic":"Dynamics","difficulty":"Medium",
 "question":"A rocket expels gas backward to propel itself forward. This is best explained by:",
 "options":{"A":"Newton's first law","B":"Newton's third law and conservation of momentum","C":"Newton's law of gravitation","D":"Archimedes' principle"},"answer":"B"},
{"id":47,"subject":"Physics","topic":"Dynamics","difficulty":"Hard",
 "question":"Two objects of mass 3 kg and 2 kg are connected by a string over a frictionless pulley (an Atwood machine). What is the acceleration of the system (g = 10 m/s^2)?",
 "options":{"A":"10 m/s^2","B":"5 m/s^2","C":"2 m/s^2","D":"1 m/s^2"},"answer":"C"},
{"id":48,"subject":"Physics","topic":"Dynamics","difficulty":"Medium",
 "question":"The centripetal force acting on a car turning a corner on a flat road is provided by:",
 "options":{"A":"The engine's power alone","B":"Air resistance","C":"Friction between the tires and the road","D":"The car's weight"},"answer":"C"},

# ============================================================
# WORK, ENERGY & POWER (12 questions) - id 49-60
# ============================================================

{"id":49,"subject":"Physics","topic":"Work, Energy & Power","difficulty":"Easy",
 "question":"Work done by a force is defined as:",
 "options":{"A":"Force multiplied by time","B":"Force multiplied by displacement in the direction of the force","C":"Mass multiplied by acceleration","D":"Force multiplied by velocity"},"answer":"B"},
{"id":50,"subject":"Physics","topic":"Work, Energy & Power","difficulty":"Medium",
 "question":"A force of 20 N moves an object 5 m in the direction of the force. How much work is done?",
 "options":{"A":"4 J","B":"25 J","C":"100 J","D":"0.25 J"},"answer":"C"},
{"id":51,"subject":"Physics","topic":"Work, Energy & Power","difficulty":"Medium",
 "question":"A 2 kg object moving at 6 m/s has a kinetic energy of:",
 "options":{"A":"12 J","B":"18 J","C":"36 J","D":"6 J"},"answer":"C"},
{"id":52,"subject":"Physics","topic":"Work, Energy & Power","difficulty":"Easy",
 "question":"The SI unit of power is the:",
 "options":{"A":"Joule","B":"Watt","C":"Newton","D":"Pascal"},"answer":"B"},
{"id":53,"subject":"Physics","topic":"Work, Energy & Power","difficulty":"Medium",
 "question":"How much work does a 500 W motor do in 20 seconds?",
 "options":{"A":"25 J","B":"500 J","C":"10000 J","D":"2500 J"},"answer":"C"},
{"id":54,"subject":"Physics","topic":"Work, Energy & Power","difficulty":"Hard",
 "question":"A pendulum bob of mass 0.5 kg swings from a height of 0.2 m above its lowest point. What is its speed at the lowest point (g = 10 m/s^2, ignoring air resistance)?",
 "options":{"A":"1 m/s","B":"4 m/s","C":"2 m/s","D":"0.5 m/s"},"answer":"C"},
{"id":55,"subject":"Physics","topic":"Work, Energy & Power","difficulty":"Easy",
 "question":"According to the law of conservation of energy, energy:",
 "options":{"A":"Can neither be created nor destroyed, only transformed","B":"Can be created but not destroyed","C":"Can be destroyed but not created","D":"Is always lost as heat"},"answer":"A"},
{"id":56,"subject":"Physics","topic":"Work, Energy & Power","difficulty":"Medium",
 "question":"A spring with spring constant 200 N/m is compressed by 0.1 m. What is the elastic potential energy stored?",
 "options":{"A":"1 J","B":"2 J","C":"20 J","D":"0.5 J"},"answer":"A"},
{"id":57,"subject":"Physics","topic":"Work, Energy & Power","difficulty":"Medium",
 "question":"Which of the following is an example of a (nearly) elastic collision?",
 "options":{"A":"Two cars colliding and sticking together","B":"A lump of clay hitting a wall and sticking","C":"A bullet embedding itself in a wooden block","D":"A ball bouncing back to nearly its original height off a rigid surface, with little energy loss"},"answer":"D"},
{"id":58,"subject":"Physics","topic":"Work, Energy & Power","difficulty":"Hard",
 "question":"A 1000 kg car moving at 20 m/s brakes and comes to rest over a distance of 50 m. What is the average braking force?",
 "options":{"A":"2000 N","B":"8000 N","C":"400 N","D":"4000 N"},"answer":"D"},
{"id":59,"subject":"Physics","topic":"Work, Energy & Power","difficulty":"Easy",
 "question":"A machine's mechanical efficiency is defined as the ratio of:",
 "options":{"A":"Output (useful) energy to input energy","B":"Input energy to output energy","C":"Power to time","D":"Force to distance"},"answer":"A"},
{"id":60,"subject":"Physics","topic":"Work, Energy & Power","difficulty":"Medium",
 "question":"A crane lifts a 200 kg load to a height of 10 m in 20 seconds (g = 10 m/s^2). What power does it deliver?",
 "options":{"A":"100 W","B":"1000 W","C":"2000 W","D":"20000 W"},"answer":"B"},

# ============================================================
# CIRCULAR MOTION & GRAVITATION (12 questions) - id 61-72
# ============================================================

{"id":61,"subject":"Physics","topic":"Circular Motion & Gravitation","difficulty":"Easy",
 "question":"Centripetal acceleration in uniform circular motion is directed:",
 "options":{"A":"Tangent to the circular path","B":"Away from the center","C":"Toward the center of the circle","D":"Along the object's velocity"},"answer":"C"},
{"id":62,"subject":"Physics","topic":"Circular Motion & Gravitation","difficulty":"Medium",
 "question":"A car of mass 1000 kg moves in a circle of radius 50 m at a constant speed of 10 m/s. What is the centripetal force acting on it?",
 "options":{"A":"2000 N","B":"200 N","C":"20000 N","D":"100 N"},"answer":"A"},
{"id":63,"subject":"Physics","topic":"Circular Motion & Gravitation","difficulty":"Medium",
 "question":"According to Kepler's third law, the square of a planet's orbital period is proportional to:",
 "options":{"A":"The planet's radius","B":"The planet's mass","C":"The square of its orbital speed","D":"The cube of the semi-major axis of its orbit"},"answer":"D"},
{"id":64,"subject":"Physics","topic":"Circular Motion & Gravitation","difficulty":"Hard",
 "question":"Two satellites orbit Earth at radii R and 4R. What is the ratio of their orbital periods (period at 4R divided by period at R)?",
 "options":{"A":"2","B":"4","C":"16","D":"8"},"answer":"D"},
{"id":65,"subject":"Physics","topic":"Circular Motion & Gravitation","difficulty":"Easy",
 "question":"The value of acceleration due to gravity (g) at the surface of the Earth is approximately:",
 "options":{"A":"5 m/s^2","B":"15 m/s^2","C":"9.8 m/s^2","D":"3.5 m/s^2"},"answer":"C"},
{"id":66,"subject":"Physics","topic":"Circular Motion & Gravitation","difficulty":"Medium",
 "question":"If a planet has the same mass as Earth but a radius half of Earth's, the acceleration due to gravity at its surface would be:",
 "options":{"A":"Half of Earth's","B":"Four times that of Earth","C":"The same as Earth's","D":"Twice that of Earth"},"answer":"B"},
{"id":67,"subject":"Physics","topic":"Circular Motion & Gravitation","difficulty":"Medium",
 "question":"The minimum speed needed for an object to permanently escape a planet's gravitational field is called:",
 "options":{"A":"Orbital velocity","B":"Terminal velocity","C":"Escape velocity","D":"Angular velocity"},"answer":"C"},
{"id":68,"subject":"Physics","topic":"Circular Motion & Gravitation","difficulty":"Hard",
 "question":"A satellite orbits Earth with a period equal to Earth's rotational period (24 hours), staying above the same point on Earth's surface. This type of orbit is called:",
 "options":{"A":"Geostationary orbit","B":"Low Earth orbit","C":"Polar orbit","D":"Elliptical orbit"},"answer":"A"},
{"id":69,"subject":"Physics","topic":"Circular Motion & Gravitation","difficulty":"Easy",
 "question":"Angular velocity is measured in units of:",
 "options":{"A":"Radians per second","B":"Meters per second","C":"Newtons","D":"Meters"},"answer":"A"},
{"id":70,"subject":"Physics","topic":"Circular Motion & Gravitation","difficulty":"Medium",
 "question":"A wheel completes 5 revolutions in 2 seconds. What is its angular velocity?",
 "options":{"A":"10*pi rad/s","B":"2.5*pi rad/s","C":"15.7 rad/s","D":"5*pi rad/s"},"answer":"D"},
{"id":71,"subject":"Physics","topic":"Circular Motion & Gravitation","difficulty":"Hard",
 "question":"An astronaut in a satellite orbiting Earth appears to be weightless mainly because:",
 "options":{"A":"There is no gravity in space at that altitude","B":"The satellite blocks the effect of gravity","C":"The astronaut and satellite are both in continuous free-fall around Earth","D":"The astronaut has zero mass in orbit"},"answer":"C"},
{"id":72,"subject":"Physics","topic":"Circular Motion & Gravitation","difficulty":"Medium",
 "question":"Centrifugal force, as experienced by an object in a rotating reference frame, is best described as:",
 "options":{"A":"A real force pushing objects outward","B":"The same as centripetal force","C":"A force that only exists in space","D":"A fictitious (pseudo) force that appears to act outward in a rotating frame"},"answer":"D"},

# ============================================================
# FLUID MECHANICS (10 questions) - id 73-82
# ============================================================

{"id":73,"subject":"Physics","topic":"Fluid Mechanics","difficulty":"Easy",
 "question":"Pressure is defined as force per unit:",
 "options":{"A":"Volume","B":"Area","C":"Length","D":"Mass"},"answer":"B"},
{"id":74,"subject":"Physics","topic":"Fluid Mechanics","difficulty":"Medium",
 "question":"According to Pascal's principle, pressure applied to an enclosed fluid is:",
 "options":{"A":"Absorbed entirely at the point of application","B":"Transmitted undiminished throughout the fluid in all directions","C":"Lost as it moves through the fluid","D":"Only transmitted downward"},"answer":"B"},
{"id":75,"subject":"Physics","topic":"Fluid Mechanics","difficulty":"Medium",
 "question":"A hydraulic lift has a small piston of area 0.01 m^2 and a large piston of area 0.5 m^2. If a force of 100 N is applied to the small piston, what force is exerted by the large piston?",
 "options":{"A":"2 N","B":"500 N","C":"50 N","D":"5000 N"},"answer":"D"},
{"id":76,"subject":"Physics","topic":"Fluid Mechanics","difficulty":"Hard",
 "question":"According to Archimedes' principle, the buoyant force on a submerged object equals:",
 "options":{"A":"The weight of the fluid displaced by the object","B":"The object's own weight","C":"The density of the fluid","D":"Zero, for any submerged object"},"answer":"A"},
{"id":77,"subject":"Physics","topic":"Fluid Mechanics","difficulty":"Easy",
 "question":"An object floats when the buoyant force acting on it is:",
 "options":{"A":"Less than its weight","B":"Zero","C":"Equal to its weight","D":"Greater than twice its weight"},"answer":"C"},
{"id":78,"subject":"Physics","topic":"Fluid Mechanics","difficulty":"Medium",
 "question":"According to the continuity equation, as a fluid flows through a narrowing section of pipe, its speed:",
 "options":{"A":"Decreases","B":"Increases","C":"Stays constant","D":"Becomes zero"},"answer":"B"},
{"id":79,"subject":"Physics","topic":"Fluid Mechanics","difficulty":"Medium",
 "question":"According to Bernoulli's principle, in a horizontal pipe, as fluid speed increases, its pressure:",
 "options":{"A":"Increases","B":"Decreases","C":"Stays constant","D":"Becomes negative"},"answer":"B"},
{"id":80,"subject":"Physics","topic":"Fluid Mechanics","difficulty":"Hard",
 "question":"An airplane wing generates lift mainly because:",
 "options":{"A":"Air moves slower over the top surface than the bottom","B":"The wing has no interaction with the airflow","C":"Gravity pulls the wing upward","D":"Air moves faster over the curved top surface, lowering pressure there relative to the bottom, per Bernoulli's principle"},"answer":"D"},
{"id":81,"subject":"Physics","topic":"Fluid Mechanics","difficulty":"Easy",
 "question":"The property of a fluid that describes its internal resistance to flow is called:",
 "options":{"A":"Density","B":"Viscosity","C":"Pressure","D":"Buoyancy"},"answer":"B"},
{"id":82,"subject":"Physics","topic":"Fluid Mechanics","difficulty":"Medium",
 "question":"Surface tension in a liquid arises due to:",
 "options":{"A":"Repulsive forces between surface molecules","B":"Gravitational forces alone","C":"Cohesive forces between liquid molecules at the surface, pulling them inward","D":"Air pressure acting on the liquid surface"},"answer":"C"},

# ============================================================
# OSCILLATIONS (SHM) (10 questions) - id 83-92
# ============================================================

{"id":83,"subject":"Physics","topic":"Oscillations (SHM)","difficulty":"Easy",
 "question":"Simple harmonic motion is characterized by a restoring force that is:",
 "options":{"A":"Constant, regardless of displacement","B":"Independent of displacement","C":"Directly proportional to displacement and directed opposite to it","D":"Directed in the same direction as displacement"},"answer":"C"},
{"id":84,"subject":"Physics","topic":"Oscillations (SHM)","difficulty":"Medium",
 "question":"The time period of a simple pendulum depends on:",
 "options":{"A":"Its mass and length","B":"Its amplitude only","C":"Its length and the local acceleration due to gravity","D":"Its mass only"},"answer":"C"},
{"id":85,"subject":"Physics","topic":"Oscillations (SHM)","difficulty":"Medium",
 "question":"A simple pendulum has a length of 1 m. Using T = 2*pi*sqrt(L/g) with g = 10 m/s^2, what is its approximate period?",
 "options":{"A":"1 s","B":"0.5 s","C":"2 s","D":"4 s"},"answer":"C"},
{"id":86,"subject":"Physics","topic":"Oscillations (SHM)","difficulty":"Hard",
 "question":"If the length of a simple pendulum is quadrupled, its period will:",
 "options":{"A":"Double","B":"Quadruple","C":"Be halved","D":"Stay the same"},"answer":"A"},
{"id":87,"subject":"Physics","topic":"Oscillations (SHM)","difficulty":"Easy",
 "question":"The maximum displacement of an oscillating object from its equilibrium position is called its:",
 "options":{"A":"Amplitude","B":"Frequency","C":"Period","D":"Phase"},"answer":"A"},
{"id":88,"subject":"Physics","topic":"Oscillations (SHM)","difficulty":"Medium",
 "question":"The frequency of oscillation is related to the period by:",
 "options":{"A":"f = T","B":"f = 2T","C":"f = 1/T","D":"f = T^2"},"answer":"C"},
{"id":89,"subject":"Physics","topic":"Oscillations (SHM)","difficulty":"Medium",
 "question":"In simple harmonic motion, the velocity of the oscillating object is maximum:",
 "options":{"A":"At the extreme positions","B":"Halfway between the mean and extreme positions","C":"At the equilibrium (mean) position","D":"It never changes"},"answer":"C"},
{"id":90,"subject":"Physics","topic":"Oscillations (SHM)","difficulty":"Hard",
 "question":"A mass-spring system has spring constant k and mass m. If the mass is doubled while k stays the same, the period of oscillation will:",
 "options":{"A":"Double","B":"Stay the same","C":"Be halved","D":"Increase by a factor of sqrt(2)"},"answer":"D"},
{"id":91,"subject":"Physics","topic":"Oscillations (SHM)","difficulty":"Easy",
 "question":"Damped oscillations occur when:",
 "options":{"A":"No energy is lost from the system","B":"Energy is gradually lost from the system, usually due to friction or resistance","C":"The amplitude increases over time","D":"The system oscillates forever without any loss"},"answer":"B"},
{"id":92,"subject":"Physics","topic":"Oscillations (SHM)","difficulty":"Medium",
 "question":"Resonance occurs when a system is driven at a frequency that:",
 "options":{"A":"Is much lower than its natural frequency","B":"Matches its natural frequency, causing a large increase in amplitude","C":"Has no relation to its natural frequency","D":"Always dampens the oscillations"},"answer":"B"},

# ============================================================
# WAVES & SOUND (12 questions) - id 93-104
# ============================================================

{"id":93,"subject":"Physics","topic":"Waves & Sound","difficulty":"Easy",
 "question":"A wave that requires a medium in order to travel is called a:",
 "options":{"A":"Electromagnetic wave","B":"Light wave","C":"Mechanical wave","D":"Radio wave"},"answer":"C"},
{"id":94,"subject":"Physics","topic":"Waves & Sound","difficulty":"Medium",
 "question":"Sound waves are classified as:",
 "options":{"A":"Transverse waves","B":"Electromagnetic waves","C":"Longitudinal waves","D":"Standing waves only"},"answer":"C"},
{"id":95,"subject":"Physics","topic":"Waves & Sound","difficulty":"Medium",
 "question":"A wave has a frequency of 25 Hz and travels at 100 m/s. What is its wavelength?",
 "options":{"A":"0.25 m","B":"2500 m","C":"125 m","D":"4 m"},"answer":"D"},
{"id":96,"subject":"Physics","topic":"Waves & Sound","difficulty":"Easy",
 "question":"The speed of sound is generally fastest in:",
 "options":{"A":"A vacuum","B":"Solids","C":"Gases","D":"Liquids"},"answer":"B"},
{"id":97,"subject":"Physics","topic":"Waves & Sound","difficulty":"Medium",
 "question":"The Doppler effect describes the apparent change in:",
 "options":{"A":"The frequency (and pitch) of a wave due to relative motion between source and observer","B":"The amplitude of a wave due to relative motion","C":"The speed of light","D":"The wavelength of a stationary source only"},"answer":"A"},
{"id":98,"subject":"Physics","topic":"Waves & Sound","difficulty":"Hard",
 "question":"A car horn emits sound at 500 Hz. As the car approaches a stationary listener, the listener hears a frequency that is:",
 "options":{"A":"Lower than 500 Hz","B":"Exactly 500 Hz","C":"Zero","D":"Higher than 500 Hz"},"answer":"D"},
{"id":99,"subject":"Physics","topic":"Waves & Sound","difficulty":"Medium",
 "question":"Two sound waves of slightly different frequencies produce a periodic variation in loudness called:",
 "options":{"A":"Resonance","B":"The Doppler effect","C":"Beats","D":"Interference cancellation only"},"answer":"C"},
{"id":100,"subject":"Physics","topic":"Waves & Sound","difficulty":"Easy",
 "question":"Which property of a sound wave determines its loudness?",
 "options":{"A":"Frequency","B":"Amplitude","C":"Wavelength","D":"Speed"},"answer":"B"},
{"id":101,"subject":"Physics","topic":"Waves & Sound","difficulty":"Medium",
 "question":"Which property of a sound wave determines its pitch?",
 "options":{"A":"Amplitude","B":"Speed","C":"Phase","D":"Frequency"},"answer":"D"},
{"id":102,"subject":"Physics","topic":"Waves & Sound","difficulty":"Hard",
 "question":"A stretched string fixed at both ends vibrates in its fundamental mode with a frequency of 100 Hz. What is the frequency of the second harmonic (first overtone)?",
 "options":{"A":"200 Hz","B":"50 Hz","C":"100 Hz","D":"300 Hz"},"answer":"A"},
{"id":103,"subject":"Physics","topic":"Waves & Sound","difficulty":"Medium",
 "question":"Standing waves are formed when:",
 "options":{"A":"Two identical waves travel in opposite directions and interfere","B":"Two waves of the same frequency travel in the same direction","C":"A single wave travels through a vacuum","D":"Waves have different frequencies and cancel entirely"},"answer":"A"},
{"id":104,"subject":"Physics","topic":"Waves & Sound","difficulty":"Medium",
 "question":"Ultrasonic waves have frequencies that are:",
 "options":{"A":"Below the range of human hearing","B":"Exactly equal to the human hearing range","C":"In the visible light spectrum","D":"Above the range of human hearing (above about 20,000 Hz)"},"answer":"D"},

# ============================================================
# THERMODYNAMICS (12 questions) - id 105-116
# ============================================================

{"id":105,"subject":"Physics","topic":"Thermodynamics","difficulty":"Easy",
 "question":"Heat naturally flows from a body of:",
 "options":{"A":"Lower temperature to higher temperature","B":"Higher temperature to lower temperature, until thermal equilibrium is reached","C":"Equal temperature to unequal temperature","D":"Higher pressure to lower pressure only"},"answer":"B"},
{"id":106,"subject":"Physics","topic":"Thermodynamics","difficulty":"Medium",
 "question":"The zeroth law of thermodynamics establishes the concept of:",
 "options":{"A":"Energy conservation","B":"Temperature and thermal equilibrium","C":"Entropy","D":"Absolute zero"},"answer":"B"},
{"id":107,"subject":"Physics","topic":"Thermodynamics","difficulty":"Medium",
 "question":"According to the first law of thermodynamics, the change in internal energy of a system equals:",
 "options":{"A":"Heat added plus work done by the system","B":"Only the heat added","C":"Heat added minus work done by the system","D":"Only the work done"},"answer":"C"},
{"id":108,"subject":"Physics","topic":"Thermodynamics","difficulty":"Hard",
 "question":"A gas absorbs 500 J of heat and does 150 J of work on its surroundings. What is the change in its internal energy?",
 "options":{"A":"650 J","B":"-350 J","C":"350 J","D":"150 J"},"answer":"C"},
{"id":109,"subject":"Physics","topic":"Thermodynamics","difficulty":"Easy",
 "question":"Which method of heat transfer occurs through direct particle-to-particle contact, especially in solids?",
 "options":{"A":"Convection","B":"Radiation","C":"Evaporation","D":"Conduction"},"answer":"D"},
{"id":110,"subject":"Physics","topic":"Thermodynamics","difficulty":"Medium",
 "question":"Convection primarily transfers heat through:",
 "options":{"A":"Direct molecular contact in solids","B":"Electromagnetic waves through a vacuum","C":"The bulk movement of a fluid","D":"Sound waves"},"answer":"C"},
{"id":111,"subject":"Physics","topic":"Thermodynamics","difficulty":"Medium",
 "question":"The second law of thermodynamics implies that in any energy transfer, the entropy of an isolated system:",
 "options":{"A":"Always decreases","B":"Always remains exactly constant","C":"Becomes zero","D":"Always increases or stays the same"},"answer":"D"},
{"id":112,"subject":"Physics","topic":"Thermodynamics","difficulty":"Hard",
 "question":"A heat engine operates between a hot reservoir at 500 K and a cold reservoir at 300 K. What is its maximum possible (Carnot) efficiency?",
 "options":{"A":"20%","B":"60%","C":"40%","D":"80%"},"answer":"C"},
{"id":113,"subject":"Physics","topic":"Thermodynamics","difficulty":"Easy",
 "question":"An isobaric process occurs at constant:",
 "options":{"A":"Pressure","B":"Volume","C":"Temperature","D":"Entropy"},"answer":"A"},
{"id":114,"subject":"Physics","topic":"Thermodynamics","difficulty":"Medium",
 "question":"An isochoric (isovolumetric) process occurs at constant:",
 "options":{"A":"Volume","B":"Pressure","C":"Temperature","D":"Entropy"},"answer":"A"},
{"id":115,"subject":"Physics","topic":"Thermodynamics","difficulty":"Medium",
 "question":"Specific heat capacity is defined as the amount of heat required to raise the temperature of:",
 "options":{"A":"Any mass of a substance by any temperature","B":"1 g of water only","C":"A substance to its melting point","D":"1 kg of a substance by 1 degree Celsius"},"answer":"D"},
{"id":116,"subject":"Physics","topic":"Thermodynamics","difficulty":"Hard",
 "question":"How much heat is required to raise the temperature of 2 kg of water by 10 degrees Celsius (specific heat of water = 4200 J/kg degreeC)?",
 "options":{"A":"8400 J","B":"42000 J","C":"84000 J","D":"420000 J"},"answer":"C"},

# ============================================================
# ELECTROSTATICS (12 questions) - id 117-128
# ============================================================

{"id":117,"subject":"Physics","topic":"Electrostatics","difficulty":"Easy",
 "question":"Like electric charges:",
 "options":{"A":"Attract each other","B":"Have no interaction","C":"Repel each other","D":"Cancel each other out"},"answer":"C"},
{"id":118,"subject":"Physics","topic":"Electrostatics","difficulty":"Medium",
 "question":"According to Coulomb's law, the electric force between two point charges is inversely proportional to:",
 "options":{"A":"The product of the charges","B":"The sum of the charges","C":"The square of the distance between them","D":"The medium's temperature"},"answer":"C"},
{"id":119,"subject":"Physics","topic":"Electrostatics","difficulty":"Medium",
 "question":"Two point charges of 2 x 10^-6 C and 3 x 10^-6 C are separated by 0.1 m in vacuum (k = 9 x 10^9 Nm^2/C^2). What is the force between them?",
 "options":{"A":"0.54 N","B":"54 N","C":"5.4 N","D":"0.054 N"},"answer":"C"},
{"id":120,"subject":"Physics","topic":"Electrostatics","difficulty":"Easy",
 "question":"Electric field lines around a positive point charge point:",
 "options":{"A":"Away from the charge, radially outward","B":"Toward the charge","C":"In circles around the charge","D":"Randomly in all directions with no pattern"},"answer":"A"},
{"id":121,"subject":"Physics","topic":"Electrostatics","difficulty":"Medium",
 "question":"Electric potential at a point is defined as:",
 "options":{"A":"Electric field per unit charge","B":"Work done per unit charge in moving a test charge from infinity to that point","C":"Force per unit area","D":"Charge per unit volume"},"answer":"B"},
{"id":122,"subject":"Physics","topic":"Electrostatics","difficulty":"Hard",
 "question":"Two identical conducting spheres carrying charges of +6 microC and -2 microC are brought into contact and then separated. What is the charge on each sphere afterward?",
 "options":{"A":"+4 microC each","B":"+2 microC each","C":"+3 microC each","D":"-2 microC each"},"answer":"B"},
{"id":123,"subject":"Physics","topic":"Electrostatics","difficulty":"Medium",
 "question":"A capacitor stores electrical energy by:",
 "options":{"A":"Accumulating and separating positive and negative charge on its plates","B":"Converting electrical energy into heat permanently","C":"Generating a magnetic field","D":"Storing kinetic energy"},"answer":"A"},
{"id":124,"subject":"Physics","topic":"Electrostatics","difficulty":"Medium",
 "question":"The capacitance of a parallel plate capacitor increases when:",
 "options":{"A":"The plate separation increases","B":"The plate area increases","C":"The plate area decreases","D":"The dielectric constant decreases"},"answer":"B"},
{"id":125,"subject":"Physics","topic":"Electrostatics","difficulty":"Easy",
 "question":"The SI unit of electric charge is the:",
 "options":{"A":"Volt","B":"Ampere","C":"Farad","D":"Coulomb"},"answer":"D"},
{"id":126,"subject":"Physics","topic":"Electrostatics","difficulty":"Hard",
 "question":"Three capacitors of 2 microF, 3 microF, and 6 microF are connected in parallel. What is their total capacitance?",
 "options":{"A":"1 microF","B":"6 microF","C":"11 microF","D":"0.9 microF"},"answer":"C"},
{"id":127,"subject":"Physics","topic":"Electrostatics","difficulty":"Medium",
 "question":"The electric field inside a charged conductor in electrostatic equilibrium is:",
 "options":{"A":"Maximum","B":"Zero","C":"Equal to the field outside","D":"Infinite"},"answer":"B"},
{"id":128,"subject":"Physics","topic":"Electrostatics","difficulty":"Medium",
 "question":"Grounding a charged conductor:",
 "options":{"A":"Increases its charge","B":"Allows excess charge to flow to or from the Earth, neutralizing it","C":"Has no effect on its charge","D":"Converts it into an insulator"},"answer":"B"},

# ============================================================
# CURRENT ELECTRICITY (14 questions) - id 129-142
# ============================================================

{"id":129,"subject":"Physics","topic":"Current Electricity","difficulty":"Easy",
 "question":"Electric current is defined as the rate of flow of:",
 "options":{"A":"Energy","B":"Electric charge","C":"Voltage","D":"Resistance"},"answer":"B"},
{"id":130,"subject":"Physics","topic":"Current Electricity","difficulty":"Easy",
 "question":"Ohm's law relates voltage, current, and:",
 "options":{"A":"Power","B":"Resistance","C":"Charge","D":"Capacitance"},"answer":"B"},
{"id":131,"subject":"Physics","topic":"Current Electricity","difficulty":"Medium",
 "question":"A circuit has a voltage of 12 V and a resistance of 4 ohm. What current flows through it?",
 "options":{"A":"48 A","B":"3 A","C":"0.33 A","D":"8 A"},"answer":"B"},
{"id":132,"subject":"Physics","topic":"Current Electricity","difficulty":"Medium",
 "question":"Two resistors of 6 ohm and 3 ohm are connected in series. What is the total resistance?",
 "options":{"A":"9 ohm","B":"2 ohm","C":"18 ohm","D":"3 ohm"},"answer":"A"},
{"id":133,"subject":"Physics","topic":"Current Electricity","difficulty":"Medium",
 "question":"Two resistors of 6 ohm and 3 ohm are connected in parallel. What is the total resistance?",
 "options":{"A":"9 ohm","B":"2 ohm","C":"4.5 ohm","D":"18 ohm"},"answer":"B"},
{"id":134,"subject":"Physics","topic":"Current Electricity","difficulty":"Hard",
 "question":"The diagram shows a circuit in which resistors R1 (5 ohm) and R2 (5 ohm) are connected in series, and this series combination is connected in parallel with R3 (10 ohm). What is the total resistance of the circuit?",
 "image":"images/q_circuit_series_parallel_physics200.png",
 "options":{"A":"10 ohm","B":"20 ohm","C":"5 ohm","D":"2.5 ohm"},"answer":"C"},
{"id":135,"subject":"Physics","topic":"Current Electricity","difficulty":"Medium",
 "question":"Electrical power dissipated in a resistor can be found using P = I^2 R. A current of 2 A flows through a 10 ohm resistor. What power is dissipated?",
 "options":{"A":"5 W","B":"20 W","C":"200 W","D":"40 W"},"answer":"D"},
{"id":136,"subject":"Physics","topic":"Current Electricity","difficulty":"Medium",
 "question":"A 60 W bulb operates at 120 V. What current does it draw?",
 "options":{"A":"2 A","B":"7200 A","C":"60 A","D":"0.5 A"},"answer":"D"},
{"id":137,"subject":"Physics","topic":"Current Electricity","difficulty":"Easy",
 "question":"Materials that allow electric current to flow easily are called:",
 "options":{"A":"Conductors","B":"Insulators","C":"Semiconductors","D":"Superconductors only"},"answer":"A"},
{"id":138,"subject":"Physics","topic":"Current Electricity","difficulty":"Medium",
 "question":"The resistivity of a typical conducting metal, as temperature increases, generally:",
 "options":{"A":"Decreases","B":"Stays exactly the same","C":"Becomes zero","D":"Increases"},"answer":"D"},
{"id":139,"subject":"Physics","topic":"Current Electricity","difficulty":"Hard",
 "question":"A wire of resistance 8 ohm is stretched to twice its original length, with its volume kept constant. What is its new resistance?",
 "options":{"A":"16 ohm","B":"4 ohm","C":"32 ohm","D":"8 ohm"},"answer":"C"},
{"id":140,"subject":"Physics","topic":"Current Electricity","difficulty":"Medium",
 "question":"The terminal voltage of a battery connected in a circuit is generally _____ its EMF, due to internal resistance.",
 "options":{"A":"Equal to","B":"Less than","C":"Greater than","D":"Unrelated to"},"answer":"B"},
{"id":141,"subject":"Physics","topic":"Current Electricity","difficulty":"Medium",
 "question":"Kirchhoff's current law (junction rule) states that:",
 "options":{"A":"Voltage is conserved around any loop","B":"The sum of currents entering a junction equals the sum of currents leaving it","C":"Current is always the same in every branch of a circuit","D":"Resistance in a circuit is always constant"},"answer":"B"},
{"id":142,"subject":"Physics","topic":"Current Electricity","difficulty":"Hard",
 "question":"A battery with EMF 12 V and internal resistance 1 ohm is connected to an external resistor of 5 ohm. What is the current in the circuit?",
 "options":{"A":"2.4 A","B":"12 A","C":"1.7 A","D":"2 A"},"answer":"D"},

# ============================================================
# ELECTROMAGNETISM (10 questions) - id 143-152
# ============================================================

{"id":143,"subject":"Physics","topic":"Electromagnetism","difficulty":"Easy",
 "question":"A current-carrying wire produces a magnetic field that circles around it, as described by:",
 "options":{"A":"The right-hand rule (Ampere's law)","B":"Faraday's law","C":"Coulomb's law","D":"Ohm's law"},"answer":"A"},
{"id":144,"subject":"Physics","topic":"Electromagnetism","difficulty":"Medium",
 "question":"The magnetic force on a moving charge is given by F = qvB*sin(theta), where theta is the angle between velocity and the field. This force is maximum when theta equals:",
 "options":{"A":"90 degrees","B":"0 degrees","C":"180 degrees","D":"45 degrees"},"answer":"A"},
{"id":145,"subject":"Physics","topic":"Electromagnetism","difficulty":"Medium",
 "question":"A charged particle moving parallel to a magnetic field experiences:",
 "options":{"A":"Maximum magnetic force","B":"No magnetic force","C":"A force perpendicular to the field","D":"A force equal to its weight"},"answer":"B"},
{"id":146,"subject":"Physics","topic":"Electromagnetism","difficulty":"Hard",
 "question":"The diagram shows a straight wire carrying a current of 5 A, placed perpendicular to a uniform magnetic field of 0.2 T, with 0.5 m of the wire's length inside the field. Based on the diagram, what is the magnitude of the force on the wire?",
 "image":"images/q_wire_in_magnetic_field_diagram.png",
 "options":{"A":"5 N","B":"0.5 N","C":"1 N","D":"0.05 N"},"answer":"B"},
{"id":147,"subject":"Physics","topic":"Electromagnetism","difficulty":"Easy",
 "question":"The strength of the magnetic field inside a solenoid is increased by:",
 "options":{"A":"Decreasing the number of turns","B":"Removing the core material","C":"Increasing the current or the number of turns per unit length","D":"Decreasing the current"},"answer":"C"},
{"id":148,"subject":"Physics","topic":"Electromagnetism","difficulty":"Medium",
 "question":"A solenoid with a soft iron core has a stronger magnetic field than an air-core solenoid mainly because:",
 "options":{"A":"Iron has high magnetic permeability, which strengthens the field","B":"Iron increases the resistance of the wire","C":"Iron blocks the magnetic field","D":"Iron increases the current"},"answer":"A"},
{"id":149,"subject":"Physics","topic":"Electromagnetism","difficulty":"Medium",
 "question":"The force between two parallel wires carrying current in the same direction is:",
 "options":{"A":"Repulsive","B":"Attractive","C":"Zero","D":"Perpendicular to both wires"},"answer":"B"},
{"id":150,"subject":"Physics","topic":"Electromagnetism","difficulty":"Hard",
 "question":"A charged particle moves in a circular path within a uniform magnetic field. The magnetic force provides:",
 "options":{"A":"Centripetal force, keeping it in circular motion at constant speed","B":"Tangential acceleration, increasing its speed","C":"No net effect on its motion","D":"A force in the direction of motion"},"answer":"A"},
{"id":151,"subject":"Physics","topic":"Electromagnetism","difficulty":"Easy",
 "question":"A magnetic compass needle aligns with Earth's magnetic field because:",
 "options":{"A":"It is attracted directly to Earth's core","B":"It has no interaction with Earth's magnetic field","C":"It experiences a torque aligning it with the local magnetic field direction","D":"It is repelled by all magnetic fields"},"answer":"C"},
{"id":152,"subject":"Physics","topic":"Electromagnetism","difficulty":"Medium",
 "question":"The magnetic field at the center of a current-carrying circular loop is:",
 "options":{"A":"Zero","B":"Parallel to the plane of the loop","C":"Maximum, perpendicular to the plane of the loop","D":"Equal to the field far from the loop"},"answer":"C"},

# ============================================================
# ELECTROMAGNETIC INDUCTION & AC (10 questions) - id 153-162
# ============================================================

{"id":153,"subject":"Physics","topic":"Electromagnetic Induction & AC","difficulty":"Easy",
 "question":"Electromagnetic induction refers to the generation of an EMF due to:",
 "options":{"A":"A changing magnetic flux through a circuit","B":"A constant magnetic field","C":"Direct current flow only","D":"Static electric charge"},"answer":"A"},
{"id":154,"subject":"Physics","topic":"Electromagnetic Induction & AC","difficulty":"Medium",
 "question":"Faraday's law of electromagnetic induction states that the induced EMF is proportional to:",
 "options":{"A":"The magnetic field strength alone","B":"The rate of change of magnetic flux","C":"The resistance of the circuit","D":"The current already flowing"},"answer":"B"},
{"id":155,"subject":"Physics","topic":"Electromagnetic Induction & AC","difficulty":"Medium",
 "question":"Lenz's law states that the direction of an induced current:",
 "options":{"A":"Reinforces the change in flux that caused it","B":"Opposes the change in flux that caused it, consistent with conservation of energy","C":"Has no defined direction","D":"Is always clockwise"},"answer":"B"},
{"id":156,"subject":"Physics","topic":"Electromagnetic Induction & AC","difficulty":"Hard",
 "question":"A coil with 100 turns experiences a change in magnetic flux of 0.02 Wb over 0.1 s. What is the magnitude of the induced EMF?",
 "options":{"A":"2 V","B":"20 V","C":"0.2 V","D":"200 V"},"answer":"B"},
{"id":157,"subject":"Physics","topic":"Electromagnetic Induction & AC","difficulty":"Easy",
 "question":"A transformer is used to:",
 "options":{"A":"Change the voltage level of an alternating current","B":"Convert AC to DC","C":"Generate current from nothing","D":"Store electrical energy"},"answer":"A"},
{"id":158,"subject":"Physics","topic":"Electromagnetic Induction & AC","difficulty":"Medium",
 "question":"The diagram shows a step-up transformer with 100 turns on the primary coil and 400 turns on the secondary coil, connected to a 20 V AC source on the primary side. Based on the diagram, what is the secondary voltage?",
 "image":"images/q_transformer_primary_secondary_diagram.png",
 "options":{"A":"5 V","B":"80 V","C":"400 V","D":"20 V"},"answer":"B"},
{"id":159,"subject":"Physics","topic":"Electromagnetic Induction & AC","difficulty":"Medium",
 "question":"An AC generator converts:",
 "options":{"A":"Electrical energy into mechanical energy","B":"Chemical energy into electrical energy","C":"Nuclear energy into mechanical energy","D":"Mechanical energy into electrical energy, typically via electromagnetic induction"},"answer":"D"},
{"id":160,"subject":"Physics","topic":"Electromagnetic Induction & AC","difficulty":"Hard",
 "question":"An AC voltage has a peak value of 170 V. What is its approximate RMS (root-mean-square) value?",
 "options":{"A":"85 V","B":"170 V","C":"240 V","D":"120 V"},"answer":"D"},
{"id":161,"subject":"Physics","topic":"Electromagnetic Induction & AC","difficulty":"Medium",
 "question":"Eddy currents are:",
 "options":{"A":"Currents that only flow in insulators","B":"Currents induced in a conductor due to a changing magnetic flux, often causing energy loss as heat","C":"Always beneficial with no drawbacks","D":"Currents that flow only in DC circuits"},"answer":"B"},
{"id":162,"subject":"Physics","topic":"Electromagnetic Induction & AC","difficulty":"Medium",
 "question":"Self-inductance of a coil opposes:",
 "options":{"A":"The current flowing in a neighboring coil only","B":"Direct current exclusively","C":"Static magnetic fields","D":"Any change in the current flowing through it"},"answer":"D"},

# ============================================================
# ELECTRONICS (8 questions) - id 163-170
# ============================================================

{"id":163,"subject":"Physics","topic":"Electronics","difficulty":"Easy",
 "question":"A semiconductor's electrical conductivity lies between that of:",
 "options":{"A":"A conductor and an insulator","B":"Two different conductors","C":"Two different insulators","D":"A superconductor and vacuum"},"answer":"A"},
{"id":164,"subject":"Physics","topic":"Electronics","difficulty":"Medium",
 "question":"Doping a semiconductor with an element having five valence electrons (such as phosphorus in silicon) creates a(n):",
 "options":{"A":"P-type semiconductor","B":"Intrinsic semiconductor","C":"Insulator","D":"N-type semiconductor, with excess free electrons"},"answer":"D"},
{"id":165,"subject":"Physics","topic":"Electronics","difficulty":"Medium",
 "question":"A P-N junction diode allows current to flow easily when it is:",
 "options":{"A":"Reverse biased","B":"Forward biased, with the p-side connected to the positive terminal","C":"Not connected to any voltage source","D":"Short-circuited"},"answer":"B"},
{"id":166,"subject":"Physics","topic":"Electronics","difficulty":"Hard",
 "question":"A diode is used as a rectifier mainly because it:",
 "options":{"A":"Allows current to flow in both directions equally","B":"Amplifies voltage signals","C":"Stores electrical charge like a capacitor","D":"Allows current to flow predominantly in one direction, converting AC to pulsating DC"},"answer":"D"},
{"id":167,"subject":"Physics","topic":"Electronics","difficulty":"Medium",
 "question":"A transistor can act as an amplifier because:",
 "options":{"A":"A small change in base current produces a much larger change in collector current","B":"A change in collector current causes a large change in base current","C":"Emitter voltage has no effect on the circuit","D":"Resistance causes voltage to disappear"},"answer":"A"},
{"id":168,"subject":"Physics","topic":"Electronics","difficulty":"Easy",
 "question":"The three terminals of a bipolar junction transistor are the:",
 "options":{"A":"Emitter, base, and collector","B":"Anode, cathode, and gate","C":"Source, drain, and gate","D":"Positive, negative, and neutral"},"answer":"A"},
{"id":169,"subject":"Physics","topic":"Electronics","difficulty":"Medium",
 "question":"Logic gates form the basic building blocks of:",
 "options":{"A":"Analog radio circuits only","B":"Digital electronic circuits and computers","C":"Mechanical systems","D":"Optical fibers"},"answer":"B"},
{"id":170,"subject":"Physics","topic":"Electronics","difficulty":"Medium",
 "question":"An AND logic gate produces a high (1) output only when:",
 "options":{"A":"At least one input is high","B":"All inputs are low","C":"Exactly one input is high","D":"All inputs are high"},"answer":"D"},

# ============================================================
# MODERN PHYSICS / ATOMIC (12 questions) - id 171-182
# ============================================================

{"id":171,"subject":"Physics","topic":"Modern Physics","difficulty":"Easy",
 "question":"According to Bohr's model of the atom, electrons orbit the nucleus in:",
 "options":{"A":"Random paths with no fixed pattern","B":"A continuous range of any possible orbit","C":"Specific, quantized energy levels or orbits","D":"Orbits identical to planetary orbits, with no quantum restriction"},"answer":"C"},
{"id":172,"subject":"Physics","topic":"Modern Physics","difficulty":"Medium",
 "question":"When an electron transitions from a higher energy level to a lower one, the atom:",
 "options":{"A":"Absorbs a photon","B":"Emits a photon with energy equal to the difference between the two levels","C":"Gains mass","D":"Loses an electron entirely"},"answer":"B"},
{"id":173,"subject":"Physics","topic":"Modern Physics","difficulty":"Medium",
 "question":"The photoelectric effect demonstrates that light behaves as:",
 "options":{"A":"A continuous wave only, with no particle nature","B":"A purely mechanical wave","C":"A stream of discrete energy packets called photons","D":"A form of matter with rest mass"},"answer":"C"},
{"id":174,"subject":"Physics","topic":"Modern Physics","difficulty":"Hard",
 "question":"In the photoelectric effect, increasing the intensity of light at a fixed frequency (above the threshold frequency) increases:",
 "options":{"A":"The maximum kinetic energy of the emitted electrons","B":"The work function of the metal","C":"The threshold frequency","D":"The number of photoelectrons emitted per second, not their maximum kinetic energy"},"answer":"D"},
{"id":175,"subject":"Physics","topic":"Modern Physics","difficulty":"Medium",
 "question":"The work function of a metal is defined as:",
 "options":{"A":"The total energy of an incoming photon","B":"The kinetic energy of an emitted electron","C":"The frequency of incoming light","D":"The minimum energy needed to remove an electron from the metal's surface"},"answer":"D"},
{"id":176,"subject":"Physics","topic":"Modern Physics","difficulty":"Easy",
 "question":"X-rays are a form of:",
 "options":{"A":"Sound waves","B":"Electromagnetic radiation with high energy and short wavelength","C":"Mechanical waves requiring a medium","D":"Particles with significant rest mass"},"answer":"B"},
{"id":177,"subject":"Physics","topic":"Modern Physics","difficulty":"Medium",
 "question":"According to de Broglie's hypothesis, particles such as electrons exhibit:",
 "options":{"A":"Only particle-like behavior","B":"No wave characteristics at all","C":"Wave-particle duality, with an associated wavelength related to their momentum","D":"Infinite wavelength regardless of momentum"},"answer":"C"},
{"id":178,"subject":"Physics","topic":"Modern Physics","difficulty":"Hard",
 "question":"According to Heisenberg's uncertainty principle, it is fundamentally impossible to simultaneously know with perfect precision a particle's:",
 "options":{"A":"Charge and mass","B":"Energy and charge","C":"Temperature and volume","D":"Position and momentum"},"answer":"D"},
{"id":179,"subject":"Physics","topic":"Modern Physics","difficulty":"Medium",
 "question":"The emission spectrum of hydrogen consists of discrete spectral lines because:",
 "options":{"A":"Electrons move in continuous orbits at any energy","B":"Hydrogen atoms contain no electrons","C":"Light is absorbed uniformly at all wavelengths","D":"Electrons can occupy only specific, quantized energy levels"},"answer":"D"},
{"id":180,"subject":"Physics","topic":"Modern Physics","difficulty":"Medium",
 "question":"Photons of light with higher frequency carry:",
 "options":{"A":"Less energy","B":"The same energy regardless of frequency","C":"More energy, according to E = hf","D":"No energy at all"},"answer":"C"},
{"id":181,"subject":"Physics","topic":"Modern Physics","difficulty":"Easy",
 "question":"The Planck constant relates a photon's energy to its:",
 "options":{"A":"Mass","B":"Wavelength inversely and frequency directly","C":"Charge","D":"Speed only"},"answer":"B"},
{"id":182,"subject":"Physics","topic":"Modern Physics","difficulty":"Hard",
 "question":"Light of frequency 6 x 10^14 Hz strikes a metal with a work function of 2 x 10^-19 J. Using E = hf (h = 6.6 x 10^-34 Js), what is the approximate maximum kinetic energy of the emitted photoelectrons?",
 "options":{"A":"3.96 x 10^-19 J","B":"1.96 x 10^-19 J","C":"5.96 x 10^-19 J","D":"0 J"},"answer":"B"},

# ============================================================
# NUCLEAR PHYSICS (8 questions) - id 183-190
# ============================================================

{"id":183,"subject":"Physics","topic":"Nuclear Physics","difficulty":"Easy",
 "question":"The nucleus of an atom consists of:",
 "options":{"A":"Protons and neutrons","B":"Protons and electrons","C":"Electrons and neutrons","D":"Only protons"},"answer":"A"},
{"id":184,"subject":"Physics","topic":"Nuclear Physics","difficulty":"Medium",
 "question":"In beta-minus decay, a neutron in the nucleus transforms into a proton, emitting:",
 "options":{"A":"An electron and an antineutrino","B":"An alpha particle","C":"A gamma ray only","D":"A positron"},"answer":"A"},
{"id":185,"subject":"Physics","topic":"Nuclear Physics","difficulty":"Medium",
 "question":"Gamma decay involves the emission of:",
 "options":{"A":"High-energy electromagnetic radiation, with no change in atomic or mass number","B":"A helium nucleus","C":"An electron","D":"A neutron"},"answer":"A"},
{"id":186,"subject":"Physics","topic":"Nuclear Physics","difficulty":"Hard",
 "question":"A radioactive sample has a half-life of 6 hours. Starting with 800 g, how much remains after 18 hours?",
 "options":{"A":"200 g","B":"400 g","C":"100 g","D":"50 g"},"answer":"C"},
{"id":187,"subject":"Physics","topic":"Nuclear Physics","difficulty":"Medium",
 "question":"Nuclear fission involves:",
 "options":{"A":"The decay of a single proton","B":"The fusion of two light nuclei into a heavier one","C":"The absorption of a neutron with no further effect","D":"The splitting of a heavy nucleus into two lighter nuclei, releasing energy"},"answer":"D"},
{"id":188,"subject":"Physics","topic":"Nuclear Physics","difficulty":"Medium",
 "question":"Nuclear fusion, the process powering the Sun, involves:",
 "options":{"A":"Light nuclei combining to form a heavier nucleus, releasing energy","B":"The splitting of heavy nuclei","C":"The emission of alpha particles only","D":"No change in mass or energy"},"answer":"A"},
{"id":189,"subject":"Physics","topic":"Nuclear Physics","difficulty":"Hard",
 "question":"According to Einstein's mass-energy equivalence (E = mc^2), a small amount of mass converted entirely into energy would release:",
 "options":{"A":"A negligible amount of energy","B":"Exactly zero energy","C":"An enormous amount of energy, since c^2 is very large","D":"Only thermal energy"},"answer":"C"},
{"id":190,"subject":"Physics","topic":"Nuclear Physics","difficulty":"Medium",
 "question":"The binding energy of a nucleus represents:",
 "options":{"A":"The kinetic energy of the nucleus","B":"The charge of the nucleus","C":"The mass of a single proton","D":"The energy required to completely separate all its nucleons"},"answer":"D"},

# ============================================================
# OPTICS (10 questions) - id 191-200
# ============================================================

{"id":191,"subject":"Physics","topic":"Optics","difficulty":"Easy",
 "question":"The image formed by a plane mirror is:",
 "options":{"A":"Virtual, upright, and the same size as the object","B":"Real and inverted","C":"Real, upright, and magnified","D":"Virtual and diminished"},"answer":"A"},
{"id":192,"subject":"Physics","topic":"Optics","difficulty":"Medium",
 "question":"A concave mirror can form a real image when the object is placed:",
 "options":{"A":"Between the pole and the focal point","B":"Only at infinity","C":"Never; concave mirrors only form virtual images","D":"Beyond the focal point"},"answer":"D"},
{"id":193,"subject":"Physics","topic":"Optics","difficulty":"Medium",
 "question":"According to the law of refraction (Snell's law), light bends toward the normal when it passes:",
 "options":{"A":"From a less dense medium into a denser medium","B":"From a denser medium to a less dense medium","C":"Through a vacuum only","D":"Along the normal itself"},"answer":"A"},
{"id":194,"subject":"Physics","topic":"Optics","difficulty":"Hard",
 "question":"The ray diagram shows a concave mirror with an object placed between the focal point (F) and the mirror's surface. Based on the diagram, the image formed is:",
 "image":"images/q_concave_mirror_object_between_f_and_mirror.png",
 "options":{"A":"Real, inverted, and diminished","B":"Virtual, upright, and magnified, formed behind the mirror","C":"Real, upright, and the same size","D":"Virtual, inverted, and diminished"},"answer":"B"},
{"id":195,"subject":"Physics","topic":"Optics","difficulty":"Easy",
 "question":"The bending of light as it passes from one transparent medium to another of different density is called:",
 "options":{"A":"Reflection","B":"Refraction","C":"Diffraction","D":"Polarization"},"answer":"B"},
{"id":196,"subject":"Physics","topic":"Optics","difficulty":"Medium",
 "question":"The refractive index of a medium is defined as the ratio of:",
 "options":{"A":"The speed of light in that medium to the speed of light in vacuum","B":"The speed of light in vacuum to the speed of light in that medium","C":"The wavelength in vacuum to the frequency in the medium","D":"The angle of incidence to the angle of reflection"},"answer":"B"},
{"id":197,"subject":"Physics","topic":"Optics","difficulty":"Medium",
 "question":"Total internal reflection occurs when light traveling in a denser medium strikes the boundary with a less dense medium at an angle:",
 "options":{"A":"Less than the critical angle","B":"Exactly 0 degrees","C":"Equal to 90 degrees only","D":"Greater than the critical angle"},"answer":"D"},
{"id":198,"subject":"Physics","topic":"Optics","difficulty":"Hard",
 "question":"A convex lens has a focal length of 20 cm. An object is placed 40 cm from the lens. Using 1/f = 1/v - 1/u (with sign convention u = -40 cm, f = +20 cm), what is the image distance v?",
 "options":{"A":"40 cm","B":"13.3 cm","C":"-40 cm","D":"20 cm"},"answer":"A"},
{"id":199,"subject":"Physics","topic":"Optics","difficulty":"Medium",
 "question":"Dispersion of white light through a prism occurs because:",
 "options":{"A":"Different wavelengths of light travel at different speeds within the prism, refracting by different amounts","B":"All wavelengths refract by exactly the same amount","C":"The prism absorbs all colors except white","D":"Light does not interact with the prism material"},"answer":"A"},
{"id":200,"subject":"Physics","topic":"Optics","difficulty":"Medium",
 "question":"Which type of lens is used to correct myopia (nearsightedness)?",
 "options":{"A":"Convex (converging) lens","B":"A flat lens with no curvature","C":"A cylindrical lens only","D":"Concave (diverging) lens"},"answer":"D"},
]


# ------------------------------------------------------------
# Sanity-check / summary utility
# ------------------------------------------------------------
def summarize(questions):
    from collections import Counter
    subj = Counter(q["subject"] for q in questions)
    topic = Counter(q["topic"] for q in questions)
    diff = Counter(q["difficulty"] for q in questions)
    ans = Counter(q["answer"] for q in questions)
    ids = [q["id"] for q in questions]
    dup_ids = [i for i in set(ids) if ids.count(i) > 1]
    dup_q = [q["question"] for q in questions]
    dup_questions = [t for t in set(dup_q) if dup_q.count(t) > 1]
    images = [q for q in questions if "image" in q]

    print(f"Total questions: {len(questions)}")
    print("\nBy subject:")
    for s, c in subj.items():
        print(f"  {s}: {c}")
    print("\nBy topic:")
    for t, c in topic.items():
        print(f"  {t}: {c}")
    print("\nBy difficulty:")
    for d, c in diff.items():
        print(f"  {d}: {c}")
    print("\nBy correct-answer letter (should be roughly balanced):")
    for L in ["A", "B", "C", "D"]:
        print(f"  {L}: {ans[L]}")
    print(f"\nDuplicate IDs: {dup_ids if dup_ids else 'None'}")
    print(f"Duplicate question text: {dup_questions if dup_questions else 'None'}")
    print(f"\nImage-based questions ({len(images)}):")
    for q in images:
        print(f"  Q{q['id']} [{q['topic']}] -> {q['image']}")

    for q in questions:
        assert set(q["options"].keys()) == {"A", "B", "C", "D"}, f"Q{q['id']} missing an option"
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