"""
MDCAT Physics Question Bank
===========================
200 MCQs modeled on the MDCAT (Punjab / PMDC) Physics syllabus.
Answer letters rebalanced 2026-09-05 to an exact 50/50/50/50 A/B/C/D
split (seed 42) prior to DB import -- content/correctness unchanged,
only which lettered slot holds the correct option was reshuffled.

Each question is a dict:
    id, subject, topic, subtopic, difficulty, question, options (A-D), answer
"""

QUESTIONS = [
{"id":1,"subject":'Physics',"topic":'Measurement',"subtopic":'SI Units',"difficulty":'Easy',
 "question":'The SI unit of electric current is the:',
 "options":{"A":'Ohm',"B":'Ampere',"C":'Coulomb',"D":'Volt'},"answer":'B'},

{"id":2,"subject":'Physics',"topic":'Measurement',"subtopic":'Base Quantities',"difficulty":'Easy',
 "question":'Which of the following is NOT a base quantity in the SI system?',
 "options":{"A":'Mass',"B":'Time',"C":'Temperature',"D":'Force'},"answer":'D'},

{"id":3,"subject":'Physics',"topic":'Measurement',"subtopic":'Dimensions',"difficulty":'Medium',
 "question":'The dimensions of pressure are:',
 "options":{"A":'[M L T^-2]',"B":'[M L^-2 T^-1]',"C":'[M L^-1 T^-2]',"D":'[M L^2 T^-2]'},"answer":'C'},

{"id":4,"subject":'Physics',"topic":'Measurement',"subtopic":'Significant Figures',"difficulty":'Medium',
 "question":'The number 0.004560 has how many significant figures?',
 "options":{"A":'3',"B":'7',"C":'5',"D":'4'},"answer":'D'},

{"id":5,"subject":'Physics',"topic":'Measurement',"subtopic":'Errors',"difficulty":'Medium',
 "question":'The least count of a vernier caliper with 10 vernier divisions coinciding with 9 main-scale divisions of 1 mm each is:',
 "options":{"A":'0.001 mm',"B":'1 mm',"C":'0.1 mm',"D":'0.01 mm'},"answer":'C'},

{"id":6,"subject":'Physics',"topic":'Measurement',"subtopic":'Dimensions',"difficulty":'Hard',
 "question":'Which pair of quantities has the same dimensions?',
 "options":{"A":'Force and momentum',"B":'Pressure and force',"C":'Torque and energy',"D":'Work and power'},"answer":'C'},

{"id":7,"subject":'Physics',"topic":'Vectors and Equilibrium',"subtopic":'Vectors',"difficulty":'Easy',
 "question":'Which of the following is a scalar quantity?',
 "options":{"A":'Speed',"B":'Displacement',"C":'Velocity',"D":'Acceleration'},"answer":'A'},

{"id":8,"subject":'Physics',"topic":'Vectors and Equilibrium',"subtopic":'Vector Addition',"difficulty":'Easy',
 "question":'Two forces of 3 N and 4 N act at right angles to each other. Their resultant is:',
 "options":{"A":'5 N',"B":'7 N',"C":'1 N',"D":'12 N'},"answer":'A'},

{"id":9,"subject":'Physics',"topic":'Vectors and Equilibrium',"subtopic":'Dot Product',"difficulty":'Medium',
 "question":'The scalar product of two perpendicular vectors is:',
 "options":{"A":'Equal to their magnitudes',"B":'Zero',"C":'Maximum',"D":'Negative'},"answer":'B'},

{"id":10,"subject":'Physics',"topic":'Vectors and Equilibrium',"subtopic":'Cross Product',"difficulty":'Medium',
 "question":'The direction of the vector product A x B is given by:',
 "options":{"A":'Right-hand rule, perpendicular to the plane of A and B',"B":'Parallel to B',"C":'Along the resultant of A and B',"D":'Parallel to A'},"answer":'A'},

{"id":11,"subject":'Physics',"topic":'Vectors and Equilibrium',"subtopic":'Equilibrium',"difficulty":'Medium',
 "question":'A body is in complete equilibrium if:',
 "options":{"A":'Net torque on it is zero only',"B":'Net force on it is zero only',"C":'Both net force and net torque are zero',"D":'It is at rest'},"answer":'C'},

{"id":12,"subject":'Physics',"topic":'Vectors and Equilibrium',"subtopic":'Torque',"difficulty":'Medium',
 "question":'Torque is the vector product of:',
 "options":{"A":'Force and velocity',"B":'Momentum and velocity',"C":'Force and displacement',"D":'Position vector and force'},"answer":'D'},

{"id":13,"subject":'Physics',"topic":'Vectors and Equilibrium',"subtopic":'Vector Components',"difficulty":'Hard',
 "question":'A vector of magnitude 10 makes an angle of 60 degrees with the x-axis. Its x-component is:',
 "options":{"A":'5 sqrt(3)',"B":'10',"C":'5',"D":'8.66'},"answer":'C'},

{"id":14,"subject":'Physics',"topic":'Vectors and Equilibrium',"subtopic":'Equilibrium',"difficulty":'Hard',
 "question":'Three coplanar forces acting on a point are in equilibrium. They can be represented in magnitude and direction by the three sides of a:',
 "options":{"A":'Rectangle',"B":'Triangle taken in order',"C":'Circle',"D":'Square taken in order'},"answer":'B'},

{"id":15,"subject":'Physics',"topic":'Motion and Force',"subtopic":'Kinematics',"difficulty":'Easy',
 "question":'The area under a velocity-time graph represents:',
 "options":{"A":'Acceleration',"B":'Force',"C":'Speed',"D":'Displacement'},"answer":'D'},

{"id":16,"subject":'Physics',"topic":'Motion and Force',"subtopic":'Kinematics',"difficulty":'Easy',
 "question":'The slope of a displacement-time graph gives:',
 "options":{"A":'Force',"B":'Displacement',"C":'Acceleration',"D":'Velocity'},"answer":'D'},

{"id":17,"subject":'Physics',"topic":'Motion and Force',"subtopic":"Newton's Laws","difficulty":'Easy',
 "question":"Newton's second law of motion states that force equals:",
 "options":{"A":'Mass times acceleration',"B":'Mass times velocity',"C":'Mass divided by acceleration',"D":'Weight divided by mass'},"answer":'A'},

{"id":18,"subject":'Physics',"topic":'Motion and Force',"subtopic":"Newton's Laws","difficulty":'Easy',
 "question":'The law of inertia is:',
 "options":{"A":'Law of gravitation',"B":"Newton's third law","C":"Newton's first law","D":"Newton's second law"},"answer":'C'},

{"id":19,"subject":'Physics',"topic":'Motion and Force',"subtopic":'Momentum',"difficulty":'Easy',
 "question":'The SI unit of linear momentum is:',
 "options":{"A":'kg m/s',"B":'kg m/s^2',"C":'N',"D":'J'},"answer":'A'},

{"id":20,"subject":'Physics',"topic":'Motion and Force',"subtopic":'Kinematics',"difficulty":'Medium',
 "question":'A body starting from rest accelerates uniformly at 2 m/s^2. Its velocity after 5 s is:',
 "options":{"A":'10 m/s',"B":'20 m/s',"C":'25 m/s',"D":'5 m/s'},"answer":'A'},

{"id":21,"subject":'Physics',"topic":'Motion and Force',"subtopic":'Kinematics',"difficulty":'Medium',
 "question":'A car travelling at 20 m/s decelerates uniformly at 4 m/s^2. The distance covered before it stops is:',
 "options":{"A":'25 m',"B":'80 m',"C":'100 m',"D":'50 m'},"answer":'D'},

{"id":22,"subject":'Physics',"topic":'Motion and Force',"subtopic":'Projectile',"difficulty":'Medium',
 "question":'The horizontal range of a projectile is maximum when the angle of projection is:',
 "options":{"A":'45 degrees',"B":'30 degrees',"C":'90 degrees',"D":'60 degrees'},"answer":'A'},

{"id":23,"subject":'Physics',"topic":'Motion and Force',"subtopic":'Projectile',"difficulty":'Medium',
 "question":'For a projectile, the vertical component of velocity at the highest point is:',
 "options":{"A":'Zero',"B":'Maximum',"C":'Equal to initial velocity',"D":'Equal to horizontal component'},"answer":'A'},

{"id":24,"subject":'Physics',"topic":'Motion and Force',"subtopic":'Projectile',"difficulty":'Medium',
 "question":'A ball is projected with velocity 20 m/s at 30 degrees. Its horizontal component of velocity is (approx):',
 "options":{"A":'20 m/s',"B":'10 m/s',"C":'17.3 m/s',"D":'5 m/s'},"answer":'C'},

{"id":25,"subject":'Physics',"topic":'Motion and Force',"subtopic":"Newton's Laws","difficulty":'Medium',
 "question":'A force of 10 N acts on a 2 kg body. Its acceleration is:',
 "options":{"A":'10 m/s^2',"B":'2 m/s^2',"C":'20 m/s^2',"D":'5 m/s^2'},"answer":'D'},

{"id":26,"subject":'Physics',"topic":'Motion and Force',"subtopic":'Momentum',"difficulty":'Medium',
 "question":'The rate of change of momentum of a body is equal to:',
 "options":{"A":'Power',"B":'Impulse',"C":'Kinetic energy',"D":'Applied force'},"answer":'D'},

{"id":27,"subject":'Physics',"topic":'Motion and Force',"subtopic":'Impulse',"difficulty":'Medium',
 "question":'Impulse is defined as:',
 "options":{"A":'Force multiplied by time of action',"B":'Force divided by time',"C":'Rate of change of force',"D":'Momentum divided by force'},"answer":'A'},

{"id":28,"subject":'Physics',"topic":'Motion and Force',"subtopic":'Collisions',"difficulty":'Hard',
 "question":'In an elastic collision between two bodies, which quantity is conserved besides momentum?',
 "options":{"A":'Only velocity',"B":'Angular momentum only',"C":'Kinetic energy',"D":'Only mass'},"answer":'C'},

{"id":29,"subject":'Physics',"topic":'Motion and Force',"subtopic":'Collisions',"difficulty":'Hard',
 "question":'A body of mass m collides elastically head-on with an identical stationary body. After collision:',
 "options":{"A":'Moving body stops and stationary body moves with the initial velocity of moving body',"B":'Both stop',"C":'They move together with half the initial velocity',"D":'Both move with equal velocities'},"answer":'A'},

{"id":30,"subject":'Physics',"topic":'Motion and Force',"subtopic":"Newton's Laws","difficulty":'Hard',
 "question":'A rocket propels forward because of:',
 "options":{"A":"Newton's first law","B":'Conservation of energy',"C":'Bernoulli principle',"D":"Newton's third law (action-reaction of exhaust gases)"},"answer":'D'},

{"id":31,"subject":'Physics',"topic":'Motion and Force',"subtopic":'Free Fall',"difficulty":'Medium',
 "question":'A body freely falls from rest. The distance covered in the first 3 seconds (g = 10 m/s^2) is:',
 "options":{"A":'45 m',"B":'90 m',"C":'30 m',"D":'15 m'},"answer":'A'},

{"id":32,"subject":'Physics',"topic":'Motion and Force',"subtopic":'Projectile',"difficulty":'Hard',
 "question":'Two projectiles are fired with the same speed at angles 30 and 60 degrees. Their horizontal ranges are:',
 "options":{"A":'In ratio 1:3',"B":'In ratio 2:1',"C":'Equal',"D":'In ratio 1:2'},"answer":'C'},

{"id":33,"subject":'Physics',"topic":'Work, Energy & Power',"subtopic":'Work',"difficulty":'Easy',
 "question":'The SI unit of work is:',
 "options":{"A":'Joule',"B":'Pascal',"C":'Watt',"D":'Newton'},"answer":'A'},

{"id":34,"subject":'Physics',"topic":'Work, Energy & Power',"subtopic":'Work',"difficulty":'Easy',
 "question":'Work done by a force is zero when the angle between force and displacement is:',
 "options":{"A":'90 degrees',"B":'180 degrees',"C":'45 degrees',"D":'0 degrees'},"answer":'A'},

{"id":35,"subject":'Physics',"topic":'Work, Energy & Power',"subtopic":'Kinetic Energy',"difficulty":'Medium',
 "question":'If the velocity of a body is doubled, its kinetic energy becomes:',
 "options":{"A":'Half',"B":'Double',"C":'Unchanged',"D":'Four times'},"answer":'D'},

{"id":36,"subject":'Physics',"topic":'Work, Energy & Power',"subtopic":'Power',"difficulty":'Easy',
 "question":'The SI unit of power is:',
 "options":{"A":'Newton',"B":'Watt',"C":'Horsepower',"D":'Joule'},"answer":'B'},

{"id":37,"subject":'Physics',"topic":'Work, Energy & Power',"subtopic":'Power',"difficulty":'Medium',
 "question":'A machine lifts a 100 kg load to a height of 10 m in 20 s. The power (g = 10 m/s^2) is:',
 "options":{"A":'250 W',"B":'500 W',"C":'1000 W',"D":'50 W'},"answer":'B'},

{"id":38,"subject":'Physics',"topic":'Work, Energy & Power',"subtopic":'Conservation',"difficulty":'Medium',
 "question":'The law of conservation of energy states that energy:',
 "options":{"A":'Is constant only in mechanical systems',"B":'Can be destroyed but not created',"C":'Can be created but not destroyed',"D":'Can neither be created nor destroyed, only transformed'},"answer":'D'},

{"id":39,"subject":'Physics',"topic":'Work, Energy & Power',"subtopic":'Potential Energy',"difficulty":'Medium',
 "question":'The gravitational PE of a 2 kg body at height 5 m (g = 10 m/s^2) is:',
 "options":{"A":'100 J',"B":'10 J',"C":'50 J',"D":'25 J'},"answer":'A'},

{"id":40,"subject":'Physics',"topic":'Work, Energy & Power',"subtopic":'Work-Energy Theorem',"difficulty":'Medium',
 "question":'The work-energy theorem states that work done by the net force equals:',
 "options":{"A":'Change in power',"B":'Change in potential energy',"C":'Change in momentum',"D":'Change in kinetic energy'},"answer":'D'},

{"id":41,"subject":'Physics',"topic":'Work, Energy & Power',"subtopic":'Efficiency',"difficulty":'Hard',
 "question":'A machine uses 500 J of energy to do 400 J of useful work. Its efficiency is:',
 "options":{"A":'40%',"B":'100%',"C":'20%',"D":'80%'},"answer":'D'},

{"id":42,"subject":'Physics',"topic":'Work, Energy & Power',"subtopic":'Escape Velocity',"difficulty":'Hard',
 "question":'The escape velocity from the surface of Earth is approximately:',
 "options":{"A":'2.4 km/s',"B":'11.2 km/s',"C":'8 km/s',"D":'22.4 km/s'},"answer":'B'},

{"id":43,"subject":'Physics',"topic":'Circular Motion',"subtopic":'Angular Quantities',"difficulty":'Easy',
 "question":'The SI unit of angular velocity is:',
 "options":{"A":'rad/s',"B":'m/s',"C":'m/s^2',"D":'rev/s'},"answer":'A'},

{"id":44,"subject":'Physics',"topic":'Circular Motion',"subtopic":'Centripetal',"difficulty":'Easy',
 "question":'In uniform circular motion, the centripetal acceleration is directed:',
 "options":{"A":'Tangent to the circle',"B":'Along the velocity vector',"C":'Radially inward toward the center',"D":'Radially outward'},"answer":'C'},

{"id":45,"subject":'Physics',"topic":'Circular Motion',"subtopic":'Centripetal',"difficulty":'Medium',
 "question":'The centripetal force required to move a 2 kg body in a circle of radius 1 m at 3 m/s is:',
 "options":{"A":'6 N',"B":'12 N',"C":'9 N',"D":'18 N'},"answer":'D'},

{"id":46,"subject":'Physics',"topic":'Circular Motion',"subtopic":'Angular Quantities',"difficulty":'Medium',
 "question":'The relation between linear velocity v, radius r, and angular velocity omega is:',
 "options":{"A":'v = r / omega',"B":'v = r * omega',"C":'v = omega^2 * r',"D":'v = omega / r'},"answer":'B'},

{"id":47,"subject":'Physics',"topic":'Circular Motion',"subtopic":'Moment of Inertia',"difficulty":'Medium',
 "question":'Moment of inertia depends on:',
 "options":{"A":'Only the axis chosen',"B":'Only the mass of the body',"C":'Mass and the distribution of mass about the axis',"D":'Only angular velocity'},"answer":'C'},

{"id":48,"subject":'Physics',"topic":'Circular Motion',"subtopic":'Angular Momentum',"difficulty":'Medium',
 "question":'Angular momentum is defined as:',
 "options":{"A":'Torque times angular velocity',"B":'Force times radius',"C":'Moment of inertia times angular velocity',"D":'Moment of inertia divided by angular velocity'},"answer":'C'},

{"id":49,"subject":'Physics',"topic":'Circular Motion',"subtopic":'Satellite',"difficulty":'Hard',
 "question":'A geostationary satellite has an orbital period of:',
 "options":{"A":'1 hour',"B":'24 hours',"C":'12 hours',"D":'48 hours'},"answer":'B'},

{"id":50,"subject":'Physics',"topic":'Circular Motion',"subtopic":'Banking',"difficulty":'Hard',
 "question":'The banking of a road on a curve is done to:',
 "options":{"A":'Reduce the weight of the vehicle',"B":'Increase speed',"C":'Provide the necessary centripetal force without relying entirely on friction',"D":'Increase friction'},"answer":'C'},

{"id":51,"subject":'Physics',"topic":'Gravitation',"subtopic":"Newton's Law","difficulty":'Easy',
 "question":"Newton's law of universal gravitation states that the gravitational force between two masses is:",
 "options":{"A":'Directly proportional to the square of the distance',"B":'Inversely proportional to the product of masses',"C":'Directly proportional to product of masses and inversely proportional to square of distance',"D":'Independent of distance'},"answer":'C'},

{"id":52,"subject":'Physics',"topic":'Gravitation',"subtopic":'g',"difficulty":'Medium',
 "question":'The value of g on the surface of Earth is approximately:',
 "options":{"A":'0.98 m/s^2',"B":'9.8 m/s^2',"C":'98 m/s^2',"D":'980 m/s'},"answer":'B'},

{"id":53,"subject":'Physics',"topic":'Gravitation',"subtopic":'Variation of g',"difficulty":'Medium',
 "question":'The value of g at the center of Earth is:',
 "options":{"A":'Same as at the surface',"B":'Infinity',"C":'Zero',"D":'Maximum'},"answer":'C'},

{"id":54,"subject":'Physics',"topic":'Gravitation',"subtopic":'Orbital Velocity',"difficulty":'Hard',
 "question":'The orbital velocity of a satellite close to Earth surface is approximately:',
 "options":{"A":'11.2 km/s',"B":'22 km/s',"C":'8 km/s',"D":'3 km/s'},"answer":'C'},

{"id":55,"subject":'Physics',"topic":'Oscillations',"subtopic":'SHM',"difficulty":'Easy',
 "question":'In simple harmonic motion, the acceleration is:',
 "options":{"A":'Directly proportional to displacement and directed toward mean position',"B":'Directed away from mean position',"C":'Constant',"D":'Zero at the extreme position'},"answer":'A'},

{"id":56,"subject":'Physics',"topic":'Oscillations',"subtopic":'SHM',"difficulty":'Easy',
 "question":'In SHM, the velocity is maximum at the:',
 "options":{"A":'Mean position',"B":'Quarter position',"C":'Extreme position',"D":'It is always constant'},"answer":'A'},

{"id":57,"subject":'Physics',"topic":'Oscillations',"subtopic":'Pendulum',"difficulty":'Medium',
 "question":'The time period of a simple pendulum depends on:',
 "options":{"A":'Material of the bob',"B":'Mass of the bob',"C":'Amplitude (for large angles only)',"D":'Length and acceleration due to gravity'},"answer":'D'},

{"id":58,"subject":'Physics',"topic":'Oscillations',"subtopic":'Pendulum',"difficulty":'Medium',
 "question":'The time period of a simple pendulum of length 1 m (g = pi^2 m/s^2) is:',
 "options":{"A":'pi s',"B":'1 s',"C":'2 pi s',"D":'2 s'},"answer":'D'},

{"id":59,"subject":'Physics',"topic":'Oscillations',"subtopic":'Spring',"difficulty":'Medium',
 "question":'The time period of a mass m attached to a spring of force constant k is:',
 "options":{"A":'2 pi sqrt(m/k)',"B":'2 pi (m k)',"C":'2 pi sqrt(k/m)',"D":'sqrt(k/m)'},"answer":'A'},

{"id":60,"subject":'Physics',"topic":'Oscillations',"subtopic":'Energy in SHM',"difficulty":'Medium',
 "question":'In SHM, at the mean position, the energy is entirely:',
 "options":{"A":'Half kinetic half potential',"B":'Kinetic',"C":'Potential',"D":'Zero'},"answer":'B'},

{"id":61,"subject":'Physics',"topic":'Oscillations',"subtopic":'Resonance',"difficulty":'Hard',
 "question":'Resonance occurs when:',
 "options":{"A":'Damping is maximum',"B":'Frequency is very high',"C":'The frequency of the driving force equals the natural frequency of the system',"D":'Amplitude is zero'},"answer":'C'},

{"id":62,"subject":'Physics',"topic":'Oscillations',"subtopic":'SHM',"difficulty":'Hard',
 "question":'The phase difference between displacement and acceleration in SHM is:',
 "options":{"A":'pi',"B":'2 pi',"C":'0',"D":'pi/2'},"answer":'A'},

{"id":63,"subject":'Physics',"topic":'Waves',"subtopic":'Types',"difficulty":'Easy',
 "question":'A wave in which particles vibrate perpendicular to the direction of propagation is:',
 "options":{"A":'Longitudinal',"B":'Stationary',"C":'Matter wave',"D":'Transverse'},"answer":'D'},

{"id":64,"subject":'Physics',"topic":'Waves',"subtopic":'Wave Equation',"difficulty":'Easy',
 "question":'The relation between wave speed v, frequency f, and wavelength lambda is:',
 "options":{"A":'v = f / lambda',"B":'v = lambda / f',"C":'v = f + lambda',"D":'v = f * lambda'},"answer":'D'},

{"id":65,"subject":'Physics',"topic":'Waves',"subtopic":'Wave Speed',"difficulty":'Medium',
 "question":'The speed of a wave of frequency 200 Hz and wavelength 0.5 m is:',
 "options":{"A":'400 m/s',"B":'50 m/s',"C":'100 m/s',"D":'200 m/s'},"answer":'C'},

{"id":66,"subject":'Physics',"topic":'Waves',"subtopic":'Superposition',"difficulty":'Medium',
 "question":'When two waves of the same frequency superpose in phase, the result is:',
 "options":{"A":'Destructive interference',"B":'Constructive interference',"C":'Diffraction',"D":'Polarization'},"answer":'B'},

{"id":67,"subject":'Physics',"topic":'Waves',"subtopic":'Stationary',"difficulty":'Medium',
 "question":'The distance between two consecutive nodes in a stationary wave is:',
 "options":{"A":'lambda',"B":'2 lambda',"C":'lambda / 2',"D":'lambda / 4'},"answer":'C'},

{"id":68,"subject":'Physics',"topic":'Waves',"subtopic":'Beats',"difficulty":'Medium',
 "question":'Two tuning forks of frequencies 256 Hz and 260 Hz produce beats of frequency:',
 "options":{"A":'4 Hz',"B":'256 Hz',"C":'516 Hz',"D":'2 Hz'},"answer":'A'},

{"id":69,"subject":'Physics',"topic":'Waves',"subtopic":'String',"difficulty":'Hard',
 "question":'The speed of a transverse wave on a stretched string depends on:',
 "options":{"A":'Tension and linear mass density of the string',"B":'Wavelength only',"C":'Frequency of the wave',"D":'Amplitude of the wave'},"answer":'A'},

{"id":70,"subject":'Physics',"topic":'Waves',"subtopic":'Doppler',"difficulty":'Hard',
 "question":'The Doppler effect refers to:',
 "options":{"A":'Reflection of sound',"B":'Superposition of two waves',"C":'Bending of light around obstacles',"D":'Apparent change in frequency due to relative motion between source and observer'},"answer":'D'},

{"id":71,"subject":'Physics',"topic":'Waves',"subtopic":'Types',"difficulty":'Easy',
 "question":'Sound waves in air are:',
 "options":{"A":'Transverse',"B":'Electromagnetic',"C":'Longitudinal',"D":'Matter waves'},"answer":'C'},

{"id":72,"subject":'Physics',"topic":'Waves',"subtopic":'Stationary',"difficulty":'Medium',
 "question":'In a stationary wave, at the antinode:',
 "options":{"A":'Particles are at rest',"B":'Pressure is maximum',"C":'Displacement is always zero',"D":'Displacement varies between maximum values'},"answer":'D'},

{"id":73,"subject":'Physics',"topic":'Sound',"subtopic":'Speed',"difficulty":'Easy',
 "question":'The speed of sound in air at 0 degrees C is approximately:',
 "options":{"A":'1000 m/s',"B":'332 m/s',"C":'3 x 10^8 m/s',"D":'150 m/s'},"answer":'B'},

{"id":74,"subject":'Physics',"topic":'Sound',"subtopic":'Frequency Range',"difficulty":'Easy',
 "question":'The audible frequency range for a normal human ear is approximately:',
 "options":{"A":'0 Hz to 100 Hz',"B":'20 Hz to 20,000 Hz',"C":'Above 100 kHz',"D":'20,000 Hz to 200,000 Hz'},"answer":'B'},

{"id":75,"subject":'Physics',"topic":'Sound',"subtopic":'Intensity',"difficulty":'Medium',
 "question":'The intensity level of sound is measured in:',
 "options":{"A":'Watt',"B":'Newton',"C":'Hertz',"D":'Decibel (dB)'},"answer":'D'},

{"id":76,"subject":'Physics',"topic":'Sound',"subtopic":'Speed',"difficulty":'Medium',
 "question":'The speed of sound in air increases with:',
 "options":{"A":'Increase in temperature',"B":'Decrease in temperature',"C":'Decrease in humidity',"D":'Increase in pressure only'},"answer":'A'},

{"id":77,"subject":'Physics',"topic":'Sound',"subtopic":'Ultrasonics',"difficulty":'Medium',
 "question":'Ultrasonic waves are sound waves with frequency:',
 "options":{"A":'Between 20 and 20000 Hz',"B":'Below 20 Hz',"C":'Above 20,000 Hz',"D":'Exactly 20 kHz'},"answer":'C'},

{"id":78,"subject":'Physics',"topic":'Sound',"subtopic":'Organ Pipes',"difficulty":'Hard',
 "question":'The fundamental frequency of an open organ pipe of length L is (v = speed of sound):',
 "options":{"A":'v / (4L)',"B":'v / (2L)',"C":'v / L',"D":'2 v / L'},"answer":'B'},

{"id":79,"subject":'Physics',"topic":'Thermodynamics',"subtopic":'Temperature',"difficulty":'Easy',
 "question":'Absolute zero corresponds to:',
 "options":{"A":'100 degrees C',"B":'-273 degrees C',"C":'0 degrees C',"D":'273 degrees C'},"answer":'B'},

{"id":80,"subject":'Physics',"topic":'Thermodynamics',"subtopic":'Heat',"difficulty":'Easy',
 "question":'The SI unit of heat is:',
 "options":{"A":'Kelvin',"B":'Watt',"C":'Calorie',"D":'Joule'},"answer":'D'},

{"id":81,"subject":'Physics',"topic":'Thermodynamics',"subtopic":'Specific Heat',"difficulty":'Medium',
 "question":'The specific heat capacity of water is approximately:',
 "options":{"A":'400 J/kg/K',"B":'4200 J/kg/K',"C":'100 J/kg/K',"D":'2100 J/kg/K'},"answer":'B'},

{"id":82,"subject":'Physics',"topic":'Thermodynamics',"subtopic":'Gas Laws',"difficulty":'Medium',
 "question":"Boyle's law relates:",
 "options":{"A":'Pressure and temperature at constant volume',"B":'Volume and temperature at constant pressure',"C":'Pressure and volume of a gas at constant temperature',"D":'Volume and mass'},"answer":'C'},

{"id":83,"subject":'Physics',"topic":'Thermodynamics',"subtopic":'Gas Laws',"difficulty":'Medium',
 "question":"Charles's law states that at constant pressure, the volume of a gas is:",
 "options":{"A":'Inversely proportional to absolute temperature',"B":'Proportional to pressure',"C":'Directly proportional to absolute temperature',"D":'Independent of temperature'},"answer":'C'},

{"id":84,"subject":'Physics',"topic":'Thermodynamics',"subtopic":'First Law',"difficulty":'Medium',
 "question":'The first law of thermodynamics is a statement of conservation of:',
 "options":{"A":'Charge',"B":'Momentum',"C":'Energy',"D":'Mass'},"answer":'C'},

{"id":85,"subject":'Physics',"topic":'Thermodynamics',"subtopic":'Isothermal',"difficulty":'Medium',
 "question":'In an isothermal process:',
 "options":{"A":'Pressure is constant',"B":'Volume is constant',"C":'Temperature is constant and dU = 0',"D":'Heat is zero'},"answer":'C'},

{"id":86,"subject":'Physics',"topic":'Thermodynamics',"subtopic":'Adiabatic',"difficulty":'Medium',
 "question":'In an adiabatic process:',
 "options":{"A":'No heat is exchanged with surroundings',"B":'Internal energy is zero',"C":'Pressure is constant',"D":'Temperature is constant'},"answer":'A'},

{"id":87,"subject":'Physics',"topic":'Thermodynamics',"subtopic":'Second Law',"difficulty":'Hard',
 "question":'The second law of thermodynamics implies that:',
 "options":{"A":'Entropy of an isolated system tends to increase',"B":'Heat flows spontaneously from cold to hot',"C":'Energy can be created',"D":'All heat can be converted to work'},"answer":'A'},

{"id":88,"subject":'Physics',"topic":'Thermodynamics',"subtopic":'Carnot Engine',"difficulty":'Hard',
 "question":'The efficiency of a Carnot engine operating between temperatures T1 (hot) and T2 (cold) is:',
 "options":{"A":'T1 / T2',"B":'T2 / T1',"C":'1 - T2 / T1',"D":'T1 - T2'},"answer":'C'},

{"id":89,"subject":'Physics',"topic":'Thermodynamics',"subtopic":'Ideal Gas',"difficulty":'Medium',
 "question":'The ideal gas equation is:',
 "options":{"A":'PVT = nR',"B":'P/V = nRT',"C":'PV = nRT',"D":'PV = mRT'},"answer":'C'},

{"id":90,"subject":'Physics',"topic":'Thermodynamics',"subtopic":'Heat Transfer',"difficulty":'Easy',
 "question":'The transfer of heat through a solid without movement of particles is:',
 "options":{"A":'Advection',"B":'Convection',"C":'Radiation',"D":'Conduction'},"answer":'D'},

{"id":91,"subject":'Physics',"topic":'Thermodynamics',"subtopic":'Latent Heat',"difficulty":'Medium',
 "question":'Latent heat of fusion is the heat required to:',
 "options":{"A":'Break molecular bonds completely',"B":'Change unit mass of a solid to liquid at its melting point without change in temperature',"C":'Convert liquid to vapor',"D":'Raise the temperature of a substance by 1 K'},"answer":'B'},

{"id":92,"subject":'Physics',"topic":'Thermodynamics',"subtopic":'Kinetic Theory',"difficulty":'Hard',
 "question":'The average kinetic energy of gas molecules is directly proportional to:',
 "options":{"A":'Mass of the molecule',"B":'Absolute temperature',"C":'Pressure only',"D":'Volume'},"answer":'B'},

{"id":93,"subject":'Physics',"topic":'Fluid Dynamics',"subtopic":'Continuity',"difficulty":'Easy',
 "question":'The equation of continuity for an incompressible fluid states that:',
 "options":{"A":'A1 + v1 = A2 + v2',"B":'A1 / v1 = A2 / v2',"C":'A1 v1 = A2 v2 (mass flow rate is constant)',"D":'P1 + v1 = P2 + v2'},"answer":'C'},

{"id":94,"subject":'Physics',"topic":'Fluid Dynamics',"subtopic":'Pressure',"difficulty":'Easy',
 "question":'The SI unit of pressure is:',
 "options":{"A":'Newton',"B":'Joule',"C":'Pascal',"D":'Watt'},"answer":'C'},

{"id":95,"subject":'Physics',"topic":'Fluid Dynamics',"subtopic":'Bernoulli',"difficulty":'Medium',
 "question":"Bernoulli's principle states that in a streamlined flow, an increase in fluid speed corresponds to:",
 "options":{"A":'Constant pressure',"B":'Increase in pressure',"C":'Increase in density',"D":'Decrease in pressure'},"answer":'D'},

{"id":96,"subject":'Physics',"topic":'Fluid Dynamics',"subtopic":'Viscosity',"difficulty":'Medium',
 "question":'Viscosity of a liquid is due to:',
 "options":{"A":'Surface tension only',"B":'Internal friction between adjacent fluid layers',"C":'Gravity',"D":'Elasticity'},"answer":'B'},

{"id":97,"subject":'Physics',"topic":'Fluid Dynamics',"subtopic":'Stokes',"difficulty":'Hard',
 "question":"Stokes' law gives the viscous drag on a sphere of radius r moving with velocity v in a fluid of viscosity eta as:",
 "options":{"A":'6 pi eta r v',"B":'2 pi eta r^2',"C":'4 pi eta r v',"D":'eta v / r'},"answer":'A'},

{"id":98,"subject":'Physics',"topic":'Fluid Dynamics',"subtopic":'Terminal Velocity',"difficulty":'Hard',
 "question":'The terminal velocity of a body falling through a viscous fluid is reached when:',
 "options":{"A":'Velocity is zero',"B":'Weight is zero',"C":'Buoyant force is zero',"D":'Weight equals viscous drag plus buoyant force'},"answer":'D'},

{"id":99,"subject":'Physics',"topic":'Deformation of Solids',"subtopic":"Hooke's Law","difficulty":'Easy',
 "question":"Hooke's law is valid:",
 "options":{"A":'Only for gases',"B":'For all stresses',"C":'Within the elastic limit',"D":'Only for plastic materials'},"answer":'C'},

{"id":100,"subject":'Physics',"topic":'Deformation of Solids',"subtopic":'Stress',"difficulty":'Medium',
 "question":'Stress is defined as:',
 "options":{"A":'Work done per unit volume',"B":'Force per unit area',"C":'Change in length per unit length',"D":'Force per unit length'},"answer":'B'},

{"id":101,"subject":'Physics',"topic":'Deformation of Solids',"subtopic":"Young's Modulus","difficulty":'Medium',
 "question":"Young's modulus is defined as the ratio of:",
 "options":{"A":'Force to area',"B":'Volume stress to volume strain',"C":'Shear stress to shear strain',"D":'Tensile stress to tensile strain'},"answer":'D'},

{"id":102,"subject":'Physics',"topic":'Deformation of Solids',"subtopic":'Elastic Limit',"difficulty":'Hard',
 "question":'The elastic limit of a material is the maximum stress beyond which:',
 "options":{"A":'The material does not return to its original shape after removal of the stress',"B":'The material becomes perfectly elastic',"C":'The material breaks immediately',"D":'Stress becomes zero'},"answer":'A'},

{"id":103,"subject":'Physics',"topic":'Electrostatics',"subtopic":"Coulomb's Law","difficulty":'Easy',
 "question":"Coulomb's force between two point charges is inversely proportional to:",
 "options":{"A":'Square of the distance between them',"B":'Product of charges',"C":'Distance between them',"D":'Cube of the distance'},"answer":'A'},

{"id":104,"subject":'Physics',"topic":'Electrostatics',"subtopic":'Charge',"difficulty":'Easy',
 "question":'The SI unit of electric charge is:',
 "options":{"A":'Volt',"B":'Ampere',"C":'Farad',"D":'Coulomb'},"answer":'D'},

{"id":105,"subject":'Physics',"topic":'Electrostatics',"subtopic":'Electric Field',"difficulty":'Easy',
 "question":'The electric field due to a point charge Q at distance r is:',
 "options":{"A":'kQ^2 / r',"B":'kQ / r^2',"C":'kQ / r',"D":'kQ * r'},"answer":'B'},

{"id":106,"subject":'Physics',"topic":'Electrostatics',"subtopic":'Potential',"difficulty":'Medium',
 "question":'The electric potential at a point due to a point charge Q at distance r is:',
 "options":{"A":'kQ / r^2',"B":'kQ / r',"C":'kQ * r^2',"D":'kQ * r'},"answer":'B'},

{"id":107,"subject":'Physics',"topic":'Electrostatics',"subtopic":'Potential',"difficulty":'Medium',
 "question":'The SI unit of electric potential is:',
 "options":{"A":'Farad',"B":'Coulomb',"C":'Volt',"D":'Ohm'},"answer":'C'},

{"id":108,"subject":'Physics',"topic":'Electrostatics',"subtopic":'Capacitance',"difficulty":'Medium',
 "question":'The SI unit of capacitance is:',
 "options":{"A":'Coulomb',"B":'Ohm',"C":'Farad',"D":'Volt'},"answer":'C'},

{"id":109,"subject":'Physics',"topic":'Electrostatics',"subtopic":'Capacitance',"difficulty":'Medium',
 "question":'The capacitance of a parallel-plate capacitor:',
 "options":{"A":'Does not depend on the medium',"B":'Increases as the distance between plates increases',"C":'Decreases as the area of plates increases',"D":'Increases when a dielectric is inserted between the plates'},"answer":'D'},

{"id":110,"subject":'Physics',"topic":'Electrostatics',"subtopic":'Combination',"difficulty":'Medium',
 "question":'Two capacitors of 2 uF and 3 uF are connected in parallel. The equivalent capacitance is:',
 "options":{"A":'6 uF',"B":'0.6 uF',"C":'5 uF',"D":'1.2 uF'},"answer":'C'},

{"id":111,"subject":'Physics',"topic":'Electrostatics',"subtopic":'Combination',"difficulty":'Medium',
 "question":'Two capacitors of 2 uF and 3 uF are connected in series. The equivalent capacitance is:',
 "options":{"A":'5 uF',"B":'6 uF',"C":'0.5 uF',"D":'1.2 uF'},"answer":'D'},

{"id":112,"subject":'Physics',"topic":'Electrostatics',"subtopic":'Energy',"difficulty":'Hard',
 "question":'The energy stored in a capacitor of capacitance C charged to potential V is:',
 "options":{"A":'C V^2',"B":'C V',"C":'(1/2) C V^2',"D":'(1/2) C^2 V'},"answer":'C'},

{"id":113,"subject":'Physics',"topic":'Electrostatics',"subtopic":'Field Lines',"difficulty":'Medium',
 "question":'Electric field lines:',
 "options":{"A":'Start on positive and end on negative charges',"B":'Form closed loops',"C":'Cross each other',"D":'Start on negative and end on positive charges'},"answer":'A'},

{"id":114,"subject":'Physics',"topic":'Electrostatics',"subtopic":"Gauss's Law","difficulty":'Hard',
 "question":"Gauss's law relates the electric flux through a closed surface to the:",
 "options":{"A":'Total charge inside the surface divided by permittivity',"B":'Distance from the source charge',"C":'Charge outside the surface',"D":'Volume enclosed'},"answer":'A'},

{"id":115,"subject":'Physics',"topic":'Electrostatics',"subtopic":'Conductor',"difficulty":'Hard',
 "question":'Inside a hollow charged conductor in electrostatic equilibrium, the electric field is:',
 "options":{"A":'Infinite',"B":'Maximum at the center',"C":'Equal to that at the surface',"D":'Zero'},"answer":'D'},

{"id":116,"subject":'Physics',"topic":'Electrostatics',"subtopic":'Electron Volt',"difficulty":'Easy',
 "question":'One electron-volt (eV) is equal to:',
 "options":{"A":'6.02 x 10^23 J',"B":'1.6 x 10^19 J',"C":'1.6 x 10^-19 J',"D":'9.1 x 10^-31 J'},"answer":'C'},

{"id":117,"subject":'Physics',"topic":'Current Electricity',"subtopic":"Ohm's Law","difficulty":'Easy',
 "question":"Ohm's law states that:",
 "options":{"A":'V is inversely proportional to I',"B":'R = V + I',"C":'V = I * R at constant temperature',"D":'I = V * R'},"answer":'C'},

{"id":118,"subject":'Physics',"topic":'Current Electricity',"subtopic":'Resistance',"difficulty":'Easy',
 "question":'The SI unit of resistance is:',
 "options":{"A":'Volt',"B":'Watt',"C":'Ohm',"D":'Ampere'},"answer":'C'},

{"id":119,"subject":'Physics',"topic":'Current Electricity',"subtopic":'Resistivity',"difficulty":'Medium',
 "question":'The resistance of a conductor of length L, area A, and resistivity rho is:',
 "options":{"A":'rho * L * A',"B":'L * A / rho',"C":'rho * L / A',"D":'rho * A / L'},"answer":'C'},

{"id":120,"subject":'Physics',"topic":'Current Electricity',"subtopic":'Combination',"difficulty":'Medium',
 "question":'Three resistors of 2 ohm, 3 ohm, and 5 ohm are connected in series. The equivalent resistance is:',
 "options":{"A":'10 ohm',"B":'2 ohm',"C":'5 ohm',"D":'0.97 ohm'},"answer":'A'},

{"id":121,"subject":'Physics',"topic":'Current Electricity',"subtopic":'Combination',"difficulty":'Medium',
 "question":'Two resistors of 4 ohm and 6 ohm are connected in parallel. The equivalent resistance is:',
 "options":{"A":'10 ohm',"B":'2.4 ohm',"C":'0.24 ohm',"D":'5 ohm'},"answer":'B'},

{"id":122,"subject":'Physics',"topic":'Current Electricity',"subtopic":'Power',"difficulty":'Medium',
 "question":'The electrical power dissipated in a resistor R carrying current I is:',
 "options":{"A":'I / R',"B":'I^2 R',"C":'I R',"D":'V R'},"answer":'B'},

{"id":123,"subject":'Physics',"topic":'Current Electricity',"subtopic":'EMF',"difficulty":'Medium',
 "question":'The terminal voltage of a battery of EMF E and internal resistance r delivering current I is:',
 "options":{"A":'E - I r',"B":'E + I r',"C":'E / (I r)',"D":'E * I r'},"answer":'A'},

{"id":124,"subject":'Physics',"topic":'Current Electricity',"subtopic":'Kirchhoff',"difficulty":'Medium',
 "question":"Kirchhoff's current law is based on the conservation of:",
 "options":{"A":'Energy',"B":'Charge',"C":'Momentum',"D":'Mass'},"answer":'B'},

{"id":125,"subject":'Physics',"topic":'Current Electricity',"subtopic":'Kirchhoff',"difficulty":'Medium',
 "question":"Kirchhoff's voltage law is based on the conservation of:",
 "options":{"A":'Charge',"B":'Momentum',"C":'Mass',"D":'Energy'},"answer":'D'},

{"id":126,"subject":'Physics',"topic":'Current Electricity',"subtopic":'Wheatstone',"difficulty":'Hard',
 "question":'The Wheatstone bridge is balanced when:',
 "options":{"A":'P + Q = R + S',"B":'P - Q = R - S',"C":'P / Q = R / S',"D":'P Q = R S'},"answer":'C'},

{"id":127,"subject":'Physics',"topic":'Current Electricity',"subtopic":'Temperature',"difficulty":'Hard',
 "question":'The resistance of a metallic conductor with increase in temperature:',
 "options":{"A":'First decreases then increases',"B":'Increases',"C":'Decreases',"D":'Remains unchanged'},"answer":'B'},

{"id":128,"subject":'Physics',"topic":'Current Electricity',"subtopic":'Current',"difficulty":'Easy',
 "question":'Electric current is defined as:',
 "options":{"A":'Charge per unit length',"B":'Charge per unit time (dQ/dt)',"C":'Time per unit charge',"D":'Voltage per resistance times time'},"answer":'B'},

{"id":129,"subject":'Physics',"topic":'Current Electricity',"subtopic":'Drift Velocity',"difficulty":'Hard',
 "question":'Drift velocity of electrons in a conductor is:',
 "options":{"A":'Zero always',"B":'Very small average velocity due to applied electric field',"C":'Random thermal velocity',"D":'Speed of light'},"answer":'B'},

{"id":130,"subject":'Physics',"topic":'Current Electricity',"subtopic":'Power',"difficulty":'Easy',
 "question":'A 100 W bulb operating at 200 V draws current:',
 "options":{"A":'2 A',"B":'0.5 A',"C":'20 A',"D":'0.05 A'},"answer":'B'},

{"id":131,"subject":'Physics',"topic":'Magnetism',"subtopic":'Magnetic Field',"difficulty":'Easy',
 "question":'The SI unit of magnetic flux density (magnetic field) is:',
 "options":{"A":'Weber',"B":'Tesla',"C":'Gauss',"D":'Henry'},"answer":'B'},

{"id":132,"subject":'Physics',"topic":'Magnetism',"subtopic":'Force on Charge',"difficulty":'Easy',
 "question":'The magnetic force on a charge q moving with velocity v in a magnetic field B is:',
 "options":{"A":'q v B (perpendicular to v)',"B":'q B / v',"C":'q + v + B',"D":'q v / B'},"answer":'A'},

{"id":133,"subject":'Physics',"topic":'Magnetism',"subtopic":'Force on Wire',"difficulty":'Medium',
 "question":'The force on a current-carrying wire of length L in magnetic field B is:',
 "options":{"A":'B I L^2',"B":'B I L sin(theta)',"C":'B I / L',"D":'B + I + L'},"answer":'B'},

{"id":134,"subject":'Physics',"topic":'Magnetism',"subtopic":'Field of Wire',"difficulty":'Medium',
 "question":'The magnetic field at a distance r from a long straight current-carrying wire (current I) is:',
 "options":{"A":'I / (mu0 r)',"B":'mu0 I r',"C":'mu0 I / (2 pi r)',"D":'mu0 I / r^2'},"answer":'C'},

{"id":135,"subject":'Physics',"topic":'Magnetism',"subtopic":'Solenoid',"difficulty":'Medium',
 "question":'The magnetic field inside a long solenoid of n turns per unit length carrying current I is:',
 "options":{"A":'mu0 I / n',"B":'mu0 n / I',"C":'n I / mu0',"D":'mu0 n I'},"answer":'D'},

{"id":136,"subject":'Physics',"topic":'Magnetism',"subtopic":'Motion in Field',"difficulty":'Hard',
 "question":'A charged particle moving perpendicular to a uniform magnetic field follows a:',
 "options":{"A":'Parabola',"B":'Helical path always',"C":'Straight line',"D":'Circular path'},"answer":'D'},

{"id":137,"subject":'Physics',"topic":'Magnetism',"subtopic":'Materials',"difficulty":'Medium',
 "question":'Which material is strongly attracted by a magnet?',
 "options":{"A":'Ferromagnetic',"B":'Diamagnetic',"C":'Non-magnetic',"D":'Paramagnetic'},"answer":'A'},

{"id":138,"subject":'Physics',"topic":'Magnetism',"subtopic":'Materials',"difficulty":'Hard',
 "question":'Above the Curie temperature, a ferromagnetic material becomes:',
 "options":{"A":'Superconducting',"B":'Non-magnetic (dielectric)',"C":'Diamagnetic',"D":'Paramagnetic'},"answer":'D'},

{"id":139,"subject":'Physics',"topic":'Magnetism',"subtopic":'e/m',"difficulty":'Hard',
 "question":'The specific charge (e/m) of the electron was first measured by:',
 "options":{"A":'Millikan',"B":'Rutherford',"C":'J.J. Thomson',"D":'Bohr'},"answer":'C'},

{"id":140,"subject":'Physics',"topic":'Magnetism',"subtopic":'Torque on Loop',"difficulty":'Medium',
 "question":'The torque on a current loop of area A carrying current I in a magnetic field B is (theta between normal and B):',
 "options":{"A":'B I / A',"B":'B I A sin(theta)',"C":'B I A cos(theta)',"D":'B I A^2'},"answer":'B'},

{"id":141,"subject":'Physics',"topic":'Magnetism',"subtopic":'Galvanometer',"difficulty":'Medium',
 "question":'A galvanometer can be converted into an ammeter by connecting:',
 "options":{"A":'A high resistance in series',"B":'A low resistance (shunt) in parallel',"C":'A capacitor in parallel',"D":'An inductor in series'},"answer":'B'},

{"id":142,"subject":'Physics',"topic":'Magnetism',"subtopic":'Voltmeter',"difficulty":'Medium',
 "question":'A galvanometer can be converted into a voltmeter by connecting:',
 "options":{"A":'A low resistance in parallel',"B":'A capacitor in series',"C":'A shunt in parallel',"D":'A high resistance in series'},"answer":'D'},

{"id":143,"subject":'Physics',"topic":'EM Induction and AC',"subtopic":'Faraday',"difficulty":'Easy',
 "question":"Faraday's law of electromagnetic induction states that induced EMF is equal to:",
 "options":{"A":'Rate of change of magnetic flux (with negative sign)',"B":'Magnetic flux times time',"C":'Magnetic field times area',"D":'Current times resistance'},"answer":'A'},

{"id":144,"subject":'Physics',"topic":'EM Induction and AC',"subtopic":'Lenz',"difficulty":'Easy',
 "question":"Lenz's law is a consequence of the conservation of:",
 "options":{"A":'Energy',"B":'Momentum',"C":'Mass',"D":'Charge'},"answer":'A'},

{"id":145,"subject":'Physics',"topic":'EM Induction and AC',"subtopic":'Inductance',"difficulty":'Medium',
 "question":'The SI unit of inductance is:',
 "options":{"A":'Weber',"B":'Henry',"C":'Farad',"D":'Ohm'},"answer":'B'},

{"id":146,"subject":'Physics',"topic":'EM Induction and AC',"subtopic":'AC',"difficulty":'Medium',
 "question":'The rms value of an alternating current of peak value I0 is:',
 "options":{"A":'I0 * sqrt(2)',"B":'I0 / sqrt(2)',"C":'I0',"D":'2 I0'},"answer":'B'},

{"id":147,"subject":'Physics',"topic":'EM Induction and AC',"subtopic":'Transformer',"difficulty":'Medium',
 "question":'A step-up transformer:',
 "options":{"A":'Decreases both voltage and current',"B":'Increases both voltage and current',"C":'Increases voltage and decreases current',"D":'Decreases voltage and increases current'},"answer":'C'},

{"id":148,"subject":'Physics',"topic":'EM Induction and AC',"subtopic":'Transformer',"difficulty":'Medium',
 "question":'A transformer works on the principle of:',
 "options":{"A":'Mutual induction',"B":'Self-induction',"C":'Electrostatic induction',"D":'Motional EMF only'},"answer":'A'},

{"id":149,"subject":'Physics',"topic":'EM Induction and AC',"subtopic":'Reactance',"difficulty":'Hard',
 "question":'The inductive reactance of an inductor L at angular frequency omega is:',
 "options":{"A":'omega / L',"B":'omega L',"C":'1 / (omega L)',"D":'L / omega'},"answer":'B'},

{"id":150,"subject":'Physics',"topic":'EM Induction and AC',"subtopic":'Reactance',"difficulty":'Hard',
 "question":'The capacitive reactance of a capacitor C at angular frequency omega is:',
 "options":{"A":'1 / (omega C)',"B":'omega C',"C":'C / omega',"D":'omega / C'},"answer":'A'},

{"id":151,"subject":'Physics',"topic":'EM Induction and AC',"subtopic":'Resonance',"difficulty":'Hard',
 "question":'The condition for resonance in a series LCR circuit is:',
 "options":{"A":'omega = 0',"B":'X_L = R',"C":'X_L = X_C',"D":'X_C = R'},"answer":'C'},

{"id":152,"subject":'Physics',"topic":'EM Induction and AC',"subtopic":'Power Factor',"difficulty":'Medium',
 "question":'The power factor of a purely inductive circuit is:',
 "options":{"A":'1',"B":'Infinity',"C":'0',"D":'0.5'},"answer":'C'},

{"id":153,"subject":'Physics',"topic":'Physical Optics',"subtopic":'Nature of Light',"difficulty":'Easy',
 "question":'The phenomenon of interference confirms that light behaves as a:',
 "options":{"A":'Wave',"B":'Neither wave nor particle',"C":'Ray only',"D":'Particle'},"answer":'A'},

{"id":154,"subject":'Physics',"topic":'Physical Optics',"subtopic":"Young's Experiment","difficulty":'Medium',
 "question":"In Young's double-slit experiment, the fringe width beta is given by (D = distance to screen, d = slit separation):",
 "options":{"A":'beta = d D / lambda',"B":'beta = lambda D / d',"C":'beta = lambda / (D d)',"D":'beta = D / (lambda d)'},"answer":'B'},

{"id":155,"subject":'Physics',"topic":'Physical Optics',"subtopic":'Diffraction',"difficulty":'Medium',
 "question":'Diffraction is more pronounced when the size of the obstacle is:',
 "options":{"A":'Very large compared to wavelength',"B":'Comparable to the wavelength of the wave',"C":'Infinite',"D":'Zero'},"answer":'B'},

{"id":156,"subject":'Physics',"topic":'Physical Optics',"subtopic":'Polarization',"difficulty":'Medium',
 "question":'Polarization confirms that light is a:',
 "options":{"A":'Stationary wave',"B":'Transverse wave',"C":'Longitudinal wave',"D":'Mechanical wave'},"answer":'B'},

{"id":157,"subject":'Physics',"topic":'Physical Optics',"subtopic":'Interference',"difficulty":'Medium',
 "question":'For constructive interference, the path difference between two waves should be:',
 "options":{"A":'n lambda where n is an integer',"B":'(n + 1/2) lambda',"C":'n lambda / 2',"D":'lambda / 4'},"answer":'A'},

{"id":158,"subject":'Physics',"topic":'Physical Optics',"subtopic":'Diffraction Grating',"difficulty":'Hard',
 "question":'The condition for the principal maxima of a diffraction grating (d = grating spacing) is:',
 "options":{"A":'d cos(theta) = n lambda',"B":'d sin(theta) = n lambda',"C":'d sin(theta) = (n+1/2) lambda',"D":'sin(theta) = n d lambda'},"answer":'B'},

{"id":159,"subject":'Physics',"topic":'Physical Optics',"subtopic":'Brewster',"difficulty":'Hard',
 "question":"At Brewster's angle, the reflected light is:",
 "options":{"A":'Partially polarized elliptically',"B":'Unpolarized',"C":'Circularly polarized',"D":'Completely plane-polarized'},"answer":'D'},

{"id":160,"subject":'Physics',"topic":'Physical Optics',"subtopic":'Interference',"difficulty":'Easy',
 "question":'Two sources of light are coherent if they have:',
 "options":{"A":'The same amplitude only',"B":'Different phases each moment',"C":'Different frequencies',"D":'The same frequency and a constant phase difference'},"answer":'D'},

{"id":161,"subject":'Physics',"topic":'Dawn of Modern Physics',"subtopic":'Photoelectric',"difficulty":'Easy',
 "question":'The photoelectric effect established that light behaves like:',
 "options":{"A":'An electric field only',"B":'A stream of particles (photons)',"C":'Nothing definite',"D":'A pure wave only'},"answer":'B'},

{"id":162,"subject":'Physics',"topic":'Dawn of Modern Physics',"subtopic":'Photoelectric',"difficulty":'Medium',
 "question":'The threshold frequency for a metal is the minimum frequency of light:',
 "options":{"A":'That causes ionization',"B":'Above which no photoelectrons are emitted',"C":'At which resistance is minimum',"D":'Below which no photoelectrons are emitted from the metal'},"answer":'D'},

{"id":163,"subject":'Physics',"topic":'Dawn of Modern Physics',"subtopic":'Photon',"difficulty":'Medium',
 "question":"The energy of a photon of frequency f is (h = Planck's constant):",
 "options":{"A":'h f',"B":'h f^2',"C":'f / h',"D":'h / f'},"answer":'A'},

{"id":164,"subject":'Physics',"topic":'Dawn of Modern Physics',"subtopic":'Compton',"difficulty":'Medium',
 "question":'The Compton effect involves:',
 "options":{"A":'Emission of electrons from a metal surface',"B":'Nuclear disintegration',"C":'Absorption of X-rays by atoms',"D":'Scattering of X-rays (or photons) by electrons with change in wavelength'},"answer":'D'},

{"id":165,"subject":'Physics',"topic":'Dawn of Modern Physics',"subtopic":'de Broglie',"difficulty":'Medium',
 "question":'The de Broglie wavelength of a particle of momentum p is:',
 "options":{"A":'p / h',"B":'h / p',"C":'h^2 / p',"D":'h * p'},"answer":'B'},

{"id":166,"subject":'Physics',"topic":'Dawn of Modern Physics',"subtopic":'Uncertainty',"difficulty":'Hard',
 "question":"Heisenberg's uncertainty principle states that:",
 "options":{"A":'Mass equals energy',"B":'Position and momentum can both be measured exactly',"C":'Energy is always conserved',"D":'The product of uncertainties in position and momentum has a minimum value on the order of h'},"answer":'D'},

{"id":167,"subject":'Physics',"topic":'Dawn of Modern Physics',"subtopic":'Relativity',"difficulty":'Hard',
 "question":"According to Einstein's special theory of relativity, the mass-energy equivalence is:",
 "options":{"A":'E = m c^2',"B":'E = m c',"C":'E = m / c^2',"D":'E = (1/2) m c^2'},"answer":'A'},

{"id":168,"subject":'Physics',"topic":'Dawn of Modern Physics',"subtopic":'Photoelectric',"difficulty":'Medium',
 "question":"According to Einstein's photoelectric equation, the maximum KE of photoelectron is:",
 "options":{"A":'h f - phi (work function)',"B":'phi - h f',"C":'h f + phi',"D":'phi / (h f)'},"answer":'A'},

{"id":169,"subject":'Physics',"topic":'Dawn of Modern Physics',"subtopic":'X-rays',"difficulty":'Medium',
 "question":'X-rays are:',
 "options":{"A":'High-energy electrons',"B":'Electromagnetic radiation of very short wavelength',"C":'Sound waves of high frequency',"D":'Charged particles from the nucleus'},"answer":'B'},

{"id":170,"subject":'Physics',"topic":'Dawn of Modern Physics',"subtopic":'Photoelectric',"difficulty":'Hard',
 "question":'When the intensity of incident light (above threshold) is increased, the:',
 "options":{"A":'Maximum KE of photoelectrons increases',"B":'Work function increases',"C":'Threshold frequency decreases',"D":'Number of photoelectrons emitted per second increases'},"answer":'D'},

{"id":171,"subject":'Physics',"topic":'Atomic Spectra',"subtopic":'Bohr Model',"difficulty":'Easy',
 "question":'According to Bohr, electrons in an atom revolve in:',
 "options":{"A":'Straight lines',"B":'Elliptical continuous orbits at any radius',"C":'Discrete stationary orbits with quantized angular momentum',"D":'Random paths'},"answer":'C'},

{"id":172,"subject":'Physics',"topic":'Atomic Spectra',"subtopic":'Bohr Model',"difficulty":'Medium',
 "question":'The angular momentum of an electron in the nth Bohr orbit is:',
 "options":{"A":'h / n',"B":'n h / (2 pi)',"C":'n h',"D":'n^2 h'},"answer":'B'},

{"id":173,"subject":'Physics',"topic":'Atomic Spectra',"subtopic":'Hydrogen',"difficulty":'Medium',
 "question":'The ground state energy of a hydrogen atom is approximately:',
 "options":{"A":'-3.4 eV',"B":'-1.6 eV',"C":'-13.6 eV',"D":'+13.6 eV'},"answer":'C'},

{"id":174,"subject":'Physics',"topic":'Atomic Spectra',"subtopic":'Series',"difficulty":'Medium',
 "question":'The Balmer series of hydrogen atoms lies in which region of the electromagnetic spectrum?',
 "options":{"A":'Infrared',"B":'X-ray',"C":'Ultraviolet',"D":'Visible'},"answer":'D'},

{"id":175,"subject":'Physics',"topic":'Atomic Spectra',"subtopic":'Series',"difficulty":'Medium',
 "question":'The Lyman series of hydrogen atom lies in the:',
 "options":{"A":'Visible region',"B":'Infrared region',"C":'Microwave region',"D":'Ultraviolet region'},"answer":'D'},

{"id":176,"subject":'Physics',"topic":'Atomic Spectra',"subtopic":'Emission',"difficulty":'Medium',
 "question":'An electron in an atom emits radiation when it:',
 "options":{"A":'Moves within the same orbit',"B":'Jumps from a higher to a lower energy level',"C":'Absorbs a photon',"D":'Jumps from a lower to a higher energy level'},"answer":'B'},

{"id":177,"subject":'Physics',"topic":'Atomic Spectra',"subtopic":'Laser',"difficulty":'Hard',
 "question":'LASER stands for:',
 "options":{"A":'Light Absorption in Stationary Electric Rings',"B":'Long Amplitude Simple Emission Ray',"C":'Light Amplification by Stimulated Emission of Radiation',"D":'Light Absorption by Simple Emission of Radio'},"answer":'C'},

{"id":178,"subject":'Physics',"topic":'Atomic Spectra',"subtopic":'Laser',"difficulty":'Hard',
 "question":'A LASER produces a beam of light which is:',
 "options":{"A":'Only visible white light',"B":'Random in frequency',"C":'Unpolarized and incoherent',"D":'Highly monochromatic, coherent, and directional'},"answer":'D'},

{"id":179,"subject":'Physics',"topic":'Nuclear Physics',"subtopic":'Nucleus',"difficulty":'Easy',
 "question":'The nucleus of an atom contains:',
 "options":{"A":'Protons and electrons',"B":'Only neutrons',"C":'Only protons',"D":'Protons and neutrons'},"answer":'D'},

{"id":180,"subject":'Physics',"topic":'Nuclear Physics',"subtopic":'Isotopes',"difficulty":'Easy',
 "question":'Isotopes of an element have:',
 "options":{"A":'Same mass number, different atomic number',"B":'Same number of neutrons',"C":'Same atomic number, different mass number',"D":'Different atomic and mass number'},"answer":'C'},

{"id":181,"subject":'Physics',"topic":'Nuclear Physics',"subtopic":'Radioactivity',"difficulty":'Medium',
 "question":'Alpha particles are:',
 "options":{"A":'High-energy electrons',"B":'Helium nuclei (2 protons + 2 neutrons)',"C":'Electromagnetic waves',"D":'Neutrons only'},"answer":'B'},

{"id":182,"subject":'Physics',"topic":'Nuclear Physics',"subtopic":'Radioactivity',"difficulty":'Medium',
 "question":'Beta particles are:',
 "options":{"A":'Protons',"B":'Fast-moving electrons emitted from the nucleus',"C":'Electromagnetic waves',"D":'Helium nuclei'},"answer":'B'},

{"id":183,"subject":'Physics',"topic":'Nuclear Physics',"subtopic":'Radioactivity',"difficulty":'Medium',
 "question":'Gamma rays are:',
 "options":{"A":'Electromagnetic radiation of very short wavelength',"B":'High-energy electrons',"C":'Sound waves',"D":'Positively charged particles'},"answer":'A'},

{"id":184,"subject":'Physics',"topic":'Nuclear Physics',"subtopic":'Half-Life',"difficulty":'Medium',
 "question":'The half-life of a radioactive substance is the time in which:',
 "options":{"A":'Half of the original atoms decay',"B":'Nucleus becomes stable',"C":'Mass doubles',"D":'All atoms decay'},"answer":'A'},

{"id":185,"subject":'Physics',"topic":'Nuclear Physics',"subtopic":'Half-Life',"difficulty":'Medium',
 "question":'A radioactive sample has half-life 10 years. After 30 years, the fraction remaining is:',
 "options":{"A":'1/8',"B":'1/2',"C":'1/4',"D":'1/16'},"answer":'A'},

{"id":186,"subject":'Physics',"topic":'Nuclear Physics',"subtopic":'Binding Energy',"difficulty":'Hard',
 "question":'Nuclear binding energy per nucleon is greatest for elements around mass number:',
 "options":{"A":'238',"B":'2',"C":'56 (iron region)',"D":'400'},"answer":'C'},

{"id":187,"subject":'Physics',"topic":'Nuclear Physics',"subtopic":'Fission',"difficulty":'Hard',
 "question":'Nuclear fission of U-235 is initiated by:',
 "options":{"A":'Alpha particles only',"B":'Fast protons only',"C":'Gamma rays',"D":'Slow (thermal) neutrons'},"answer":'D'},

{"id":188,"subject":'Physics',"topic":'Nuclear Physics',"subtopic":'Fusion',"difficulty":'Hard',
 "question":'The energy source of the Sun is primarily:',
 "options":{"A":'Nuclear fusion of hydrogen into helium',"B":'Gravitational collapse',"C":'Nuclear fission',"D":'Chemical burning'},"answer":'A'},

{"id":189,"subject":'Physics',"topic":'Electronics',"subtopic":'Semiconductors',"difficulty":'Easy',
 "question":'A semiconductor doped with pentavalent impurity becomes:',
 "options":{"A":'Insulator',"B":'Intrinsic',"C":'n-type',"D":'p-type'},"answer":'C'},

{"id":190,"subject":'Physics',"topic":'Electronics',"subtopic":'Semiconductors',"difficulty":'Easy',
 "question":'In a p-type semiconductor, the majority charge carriers are:',
 "options":{"A":'Electrons',"B":'Neutrons',"C":'Protons',"D":'Holes'},"answer":'D'},

{"id":191,"subject":'Physics',"topic":'Electronics',"subtopic":'PN Junction',"difficulty":'Medium',
 "question":'A pn-junction diode allows current to flow easily when:',
 "options":{"A":'Forward biased',"B":'Not biased',"C":'Reverse biased',"D":'Zero temperature'},"answer":'A'},

{"id":192,"subject":'Physics',"topic":'Electronics',"subtopic":'Rectifier',"difficulty":'Medium',
 "question":'The main function of a rectifier is to convert:',
 "options":{"A":'Low voltage into high voltage',"B":'Current into voltage',"C":'DC into AC',"D":'AC into DC'},"answer":'D'},

{"id":193,"subject":'Physics',"topic":'Electronics',"subtopic":'Transistor',"difficulty":'Medium',
 "question":'A transistor has three terminals: emitter, base, and:',
 "options":{"A":'Collector',"B":'Gate',"C":'Cathode',"D":'Anode'},"answer":'A'},

{"id":194,"subject":'Physics',"topic":'Electronics',"subtopic":'Logic Gates',"difficulty":'Medium',
 "question":'A logic gate whose output is 1 only when both inputs are 1 is:',
 "options":{"A":'NOT',"B":'AND',"C":'OR',"D":'NAND'},"answer":'B'},

{"id":195,"subject":'Physics',"topic":'Electronics',"subtopic":'Logic Gates',"difficulty":'Hard',
 "question":'The output of an XOR gate is 1 when:',
 "options":{"A":'Both inputs are 0',"B":'The two inputs are different',"C":'Both inputs are 1',"D":'Both inputs are the same'},"answer":'B'},

{"id":196,"subject":'Physics',"topic":'Electronics',"subtopic":'Op-Amp',"difficulty":'Hard',
 "question":'An ideal operational amplifier has:',
 "options":{"A":'Finite input impedance and finite output impedance',"B":'Infinite input impedance and zero output impedance',"C":'Zero gain',"D":'Zero input impedance and infinite output impedance'},"answer":'B'},

{"id":197,"subject":'Physics',"topic":'Electronics',"subtopic":'Semiconductors',"difficulty":'Medium',
 "question":'The forbidden energy gap of a semiconductor is typically:',
 "options":{"A":'Zero',"B":'More than 100 eV',"C":'About 10 eV',"D":'About 1 eV'},"answer":'D'},

{"id":198,"subject":'Physics',"topic":'Waves',"subtopic":'EM Spectrum',"difficulty":'Easy',
 "question":'The speed of electromagnetic waves in vacuum is approximately:',
 "options":{"A":'3 x 10^8 m/s',"B":'3 x 10^6 m/s',"C":'3 x 10^5 m/s',"D":'3 x 10^10 m/s'},"answer":'A'},

{"id":199,"subject":'Physics',"topic":'Nuclear Physics',"subtopic":'Mass Defect',"difficulty":'Hard',
 "question":'Mass defect in a nucleus is:',
 "options":{"A":'Difference between mass of nucleus and total mass of its constituent nucleons',"B":'Mass of alpha particle emitted',"C":'Extra mass created during fusion',"D":'Mass of electrons removed'},"answer":'A'},

{"id":200,"subject":'Physics',"topic":'Current Electricity',"subtopic":'Energy',"difficulty":'Medium',
 "question":'One kilowatt-hour (kWh) is equal to:',
 "options":{"A":'1.6 x 10^-19 J',"B":'1000 J',"C":'3600 J',"D":'3.6 x 10^6 J'},"answer":'D'},

]