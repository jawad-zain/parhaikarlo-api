import json
from pathlib import Path

OUT = Path(__file__).parent / "mock18_explanations_physics.json"

def I(po): return po + 7944

E = []

def add(po, short, long, trick, a, b, c, d):
    E.append({
        "id": I(po), "short": short, "long": long, "trick": trick,
        "options": {"a": a, "b": b, "c": c, "d": d}
    })

add(127, "Speed = distance/time = 30 km / 3 h = 10 km/h.",
    "For constant speed, speed = total distance / total time. Here, 30 km / 3 h = 10 km/h.",
    "A quick sanity check: 10 km/h x 3 h = 30 km, confirming the answer matches the given distance.",
    "Incorrect — 90 km/h would result from multiplying (30 x 3) instead of dividing.",
    "Incorrect — 15 km/h doesn't match 30/3; it would require a different distance or time.",
    "Correct — 30 km divided by 3 h gives 10 km/h.",
    "Incorrect — 3.3 km/h would result from an inverted calculation (3/30 instead of 30/3).")

add(128, "Acceleration = change in velocity / time = (25 - 10) / 5 = 3 m/s^2.",
    "Acceleration a = (v_final - v_initial) / t = (25 m/s - 10 m/s) / 5 s = 15/5 = 3 m/s^2.",
    "Always subtract initial from final velocity FIRST, then divide by the time interval — don't divide each velocity separately.",
    "Incorrect — 2 m/s^2 doesn't match (25-10)/5; check the subtraction and division again.",
    "Incorrect — 5 m/s^2 would result from an arithmetic slip, not matching the correct 15/5 calculation.",
    "Incorrect — 7.5 m/s^2 doesn't correspond to the correct values given.",
    "Correct — (25 - 10) / 5 = 15 / 5 = 3 m/s^2.")

add(129, "For a ball dropped from rest, v = gt = 10 x 4 = 40 m/s after 4 seconds.",
    "Starting from rest (initial velocity = 0), under constant gravitational acceleration g = 10 m/s^2, velocity after time t is simply v = gt = 10 x 4 = 40 m/s (ignoring air resistance).",
    "'Dropped from rest' means initial velocity = 0, so v = gt directly — no need for a more complex kinematics equation here.",
    "Correct — v = g x t = 10 x 4 = 40 m/s.",
    "Incorrect — 20 m/s would result from using only half the actual fall time or a factor-of-2 error.",
    "Incorrect — 80 m/s would double the correct answer, perhaps from doubling g or t incorrectly.",
    "Incorrect — 10 m/s is just g itself (the acceleration value), not the velocity after 4 seconds of falling.")

add(130, "By Newton's first law, an object with zero net force stays at rest if it was already at rest (inertia).",
    "Newton's first law (law of inertia) states an object at rest remains at rest, and an object in motion continues in motion at constant velocity, unless acted upon by a net external force. With zero net force, a stationary object simply stays stationary.",
    "Newton's first law is fundamentally about resisting CHANGE in motion state — 'zero net force' means 'no change', so a resting object stays resting.",
    "Incorrect — with zero net force, there's no reason for a stationary object to spontaneously start moving.",
    "Correct — zero net force on a stationary object means it remains at rest, per Newton's first law.",
    "Incorrect — 'random acceleration' would require a net force, which contradicts the zero-net-force condition given.",
    "Incorrect — mass doesn't change simply because net force is zero; these are unrelated concepts.")

add(131, "By Newton's second law, mass = force / acceleration = 20 N / 4 m/s^2 = 5 kg.",
    "Newton's second law states F = ma, so rearranged, m = F/a = 20 N / 4 m/s^2 = 5 kg.",
    "Rearrange F=ma to solve for whichever variable is missing — here it's mass, so divide force by acceleration.",
    "Incorrect — 16 kg doesn't result from correctly dividing 20 by 4.",
    "Incorrect — 80 kg would result from multiplying (20 x 4) instead of dividing.",
    "Correct — 20 N / 4 m/s^2 = 5 kg.",
    "Incorrect — 24 kg doesn't match the correct division of the given values.")

add(132, "Newton's second law is precisely F = ma (force equals mass times acceleration).",
    "F = ma is the mathematical statement of Newton's second law, relating the net force on an object to its mass and resulting acceleration — the other listed statements describe Newton's first law (inertia), the law of conservation of momentum, and Newton's third law (action-reaction) respectively.",
    "Match each classic statement to its correct law: 'stays at rest unless forced' = 1st law; 'F=ma' = 2nd law; 'equal and opposite reaction' = 3rd law — a common exam mix-up to avoid.",
    "Incorrect — this statement describes Newton's FIRST law (inertia), not the second law.",
    "Incorrect — conservation of momentum is a related but separate principle from Newton's second law's F=ma formula.",
    "Incorrect — this statement describes Newton's THIRD law (action-reaction pairs), not the second law.",
    "Correct — F = ma is exactly Newton's second law.")

add(133, "Net force = 22 N - friction (10 N) = 12 N; acceleration = 12 N / 4 kg = 3 m/s^2.",
    "Friction force = mu x Normal force = 0.25 x (4 kg x 10 m/s^2) = 0.25 x 40 N = 10 N. Net force = applied force - friction = 22 - 10 = 12 N. Acceleration = net force / mass = 12 / 4 = 3 m/s^2.",
    "Always subtract friction from the applied force to get NET force before dividing by mass — forgetting friction is a very common mistake in these problems.",
    "Correct — after subtracting 10 N of friction from the 22 N applied force, net force 12 N divided by 4 kg gives 3 m/s^2.",
    "Incorrect — 5.5 m/s^2 would result from using the applied force (22 N) directly without subtracting friction (22/4=5.5), ignoring friction entirely.",
    "Incorrect — 2 m/s^2 doesn't match the correct friction and net-force calculation here.",
    "Incorrect — 4 m/s^2 doesn't correspond to the correctly computed 12 N net force divided by 4 kg.")

add(134, "Work done by a force parallel to the direction of motion is maximum for that force/displacement magnitude.",
    "Work = F x d x cos(theta), where theta is the angle between force and displacement. When force is parallel to motion (theta=0deg), cos(0)=1, giving the maximum possible work for that force magnitude and displacement — any other angle would produce less work (theta=90deg gives zero work).",
    "W = Fd cos(theta): parallel (theta=0) maximizes work; perpendicular (theta=90) gives zero work — remember these two special cases.",
    "Incorrect — zero work would occur if the force were perpendicular to motion, not parallel to it.",
    "Correct — a parallel force (cos 0deg = 1) produces the maximum possible work for that force and displacement.",
    "Incorrect — work would only be negative if the force opposed the direction of motion (theta=180deg), not when it's parallel/aligned with it.",
    "Incorrect — work is a well-defined, calculable quantity (W = Fd cos theta) in this scenario, not undefined.")

add(135, "Gravitational PE = mgh = 4 kg x 10 m/s^2 x 5 m = 200 J.",
    "Gravitational potential energy formula: PE = mgh, where m is mass, g is gravitational acceleration, and h is height. Substituting: PE = 4 x 10 x 5 = 200 J.",
    "Multiply all three values together (mass, g, height) — a common error is forgetting one of the three factors.",
    "Incorrect — 20 J would result from omitting one of the three factors (e.g. forgetting height or g).",
    "Incorrect — 50 J doesn't match the full m x g x h calculation with these values.",
    "Correct — 4 x 10 x 5 = 200 J.",
    "Incorrect — 9 J is far too small and doesn't reflect the correct multiplication of mass, g, and height.")

add(136, "Kinetic energy = (1/2)mv^2 = 0.5 x 4 x 5^2 = 0.5 x 4 x 25 = 50 J.",
    "KE = (1/2)mv^2. With m=4 kg and v=5 m/s: KE = 0.5 x 4 x 25 = 50 J.",
    "Remember velocity is SQUARED in the kinetic energy formula — squaring v before multiplying by (1/2)m is a common step to miss.",
    "Incorrect — 20 J would result from forgetting to square the velocity (using v instead of v^2).",
    "Incorrect — 10 J is too small and doesn't match the correct formula's result.",
    "Incorrect — 100 J would result from omitting the 1/2 factor in the KE formula.",
    "Correct — 0.5 x 4 x 5^2 = 0.5 x 4 x 25 = 50 J.")

add(137, "Power = energy / time = 24000 J / 40 s = 600 W.",
    "Power is the rate of energy transfer: P = W/t = 24000 J / 40 s = 600 W (watts).",
    "Power = energy divided by TIME — make sure to use the correct time value (40 s here, not some other number) in the denominator.",
    "Correct — 24000 / 40 = 600 W.",
    "Incorrect — 960000 W would result from multiplying (24000 x 40) instead of dividing.",
    "Incorrect — 60 W is off by a factor of 10 from the correct division.",
    "Incorrect — 6000 W is off by a factor of 10 from the correct answer.")

add(138, "Centripetal force in uniform circular motion always points toward the center of the circular path.",
    "Centripetal force is the net inward force needed to continuously redirect an object's velocity toward the center, keeping it moving along a circular path rather than flying off in a straight line (per Newton's first law) — it always points radially inward, toward the center, never outward or tangentially.",
    "'Centripetal' literally means 'center-seeking' — the force always points toward the center, a very frequently tested direction fact.",
    "Incorrect — tangent to the path describes the object's instantaneous velocity direction, not the centripetal force direction.",
    "Correct — centripetal force always points toward the center of the circular path.",
    "Incorrect — pointing away from the center would be centrifugal (an apparent, not real, force in a rotating reference frame), not centripetal.",
    "Incorrect — the object's velocity direction is tangential, not the same as the (radially inward) centripetal force direction.")

add(139, "By Newton's law of gravitation (F ∝ 1/r^2), tripling the distance reduces the force to 1/9 of the original.",
    "Gravitational force follows an inverse-square law: F = Gm1m2/r^2. If r is tripled (3r), the new force = Gm1m2/(3r)^2 = Gm1m2/(9r^2) = (1/9) of the original force.",
    "Whenever distance changes by a factor, the FORCE changes by the inverse of that factor SQUARED — tripling distance means dividing force by 3^2=9, not just by 3.",
    "Incorrect — 3 times the original force would apply if force were directly (not inversely) proportional to distance.",
    "Incorrect — 1/3 forgets to square the distance factor; the inverse-square law requires squaring, giving 1/9, not 1/3.",
    "Correct — tripling the distance means dividing the force by 3^2 = 9, giving 1/9 of the original.",
    "Incorrect — 9 times the original force would be the case if force increased (not decreased) with distance, the opposite of gravity's actual inverse relationship.")

add(140, "If Earth's radius doubled with mass unchanged, surface gravity would drop to 1/4 of its original value.",
    "Surface gravitational acceleration g = GM/r^2. Since g is inversely proportional to r^2, doubling r (with M constant) gives g_new = GM/(2r)^2 = GM/(4r^2) = (1/4) of the original g.",
    "Same inverse-square logic as gravitational force between two masses applies here to surface gravity — doubling radius means g drops by a factor of 2^2 = 4, not just 2.",
    "Incorrect — g would stay the same only if radius didn't actually change, contrary to the question's premise.",
    "Incorrect — doubling g would require radius to HALVE (not double), the opposite direction of change described.",
    "Incorrect — quadrupling g would require the radius to halve, again the wrong direction for this scenario.",
    "Correct — the inverse-square relationship means doubling the radius reduces g to 1/4 of its original value.")

add(141, "An object sinks when the buoyant force on it is less than its weight.",
    "By Archimedes' principle, an object floats or sinks based on comparing its weight to the buoyant force (equal to the weight of fluid displaced). If buoyant force < weight, the net force is downward, and the object sinks; if buoyant force >= weight, it floats or is neutrally buoyant.",
    "Sinks: buoyancy < weight. Floats: buoyancy >= weight — compare the two forces directly to predict sinking vs floating.",
    "Correct — an object sinks precisely when the buoyant force acting on it is less than its weight.",
    "Incorrect — a buoyant force greater than weight would push the object upward, causing it to float or rise, not sink.",
    "Incorrect — buoyant force exactly equal to weight would result in the object being neutrally buoyant (suspended), not actively sinking.",
    "Incorrect — a buoyant force twice the weight would strongly push the object upward, the opposite of sinking.")

add(142, "Pascal's principle: pressure applied to an enclosed fluid is transmitted undiminished throughout the fluid in all directions.",
    "This principle underlies hydraulic systems: a pressure applied at any point in a confined, incompressible fluid is transmitted equally to every other point in the fluid and to the walls of its container, allowing a small force over a small area to generate a much larger force over a larger area (hydraulic lift/brake systems).",
    "'Undiminished' and 'in all directions' are the two key phrases in Pascal's principle — pressure isn't lost or limited to one direction within the enclosed fluid.",
    "Incorrect — the pressure is transmitted throughout the fluid, not simply absorbed at just the point of application.",
    "Correct — undiminished, all-direction transmission of pressure through the enclosed fluid is precisely Pascal's principle.",
    "Incorrect — the whole point of Pascal's principle is that pressure is NOT lost as it moves through the fluid.",
    "Incorrect — pressure is transmitted in ALL directions through an enclosed fluid, not restricted only to the direction it was applied.")

add(143, "By Bernoulli's principle, faster-flowing fluid has lower pressure.",
    "Bernoulli's equation relates fluid speed and pressure along a streamline: as flow speed increases, pressure (in that flow) decreases, assuming height and energy losses are constant — this inverse relationship explains phenomena like airplane lift and the Venturi effect.",
    "Bernoulli's principle: FASTER flow = LOWER pressure (and vice versa) — an inverse, not direct, relationship between speed and pressure.",
    "Incorrect — pressure decreases (not increases) as fluid speed increases, per Bernoulli's principle.",
    "Incorrect — pressure changes measurably with flow speed; it does not stay constant.",
    "Correct — as fluid speed increases, its pressure decreases, per Bernoulli's principle.",
    "Incorrect — pressure decreases but doesn't necessarily drop all the way to zero; this overstates the effect.")

add(144, "The lowest point of a transverse wave is called the trough.",
    "In a transverse wave, the highest point is the crest and the lowest point is the trough; amplitude is the maximum displacement from the equilibrium (rest) position, and a node is a point of zero displacement (seen in standing waves).",
    "Crest = highest point; Trough = lowest point; Amplitude = height of displacement (a measurement, not a location); Node = zero-displacement point in a standing wave.",
    "Incorrect — the crest is the HIGHEST point of a transverse wave, the opposite of what's being asked.",
    "Incorrect — amplitude is a measurement of maximum displacement, not a specific point on the wave itself.",
    "Incorrect — a node is a point of zero displacement, typically discussed in standing waves, not the lowest point of a traveling wave.",
    "Correct — the trough is specifically the lowest point of a transverse wave.")

add(145, "A shorter pendulum has a shorter period, meaning a higher frequency of oscillation.",
    "Pendulum period T = 2*pi*sqrt(L/g), so period depends on the square root of length L (and gravity g, held constant here). A shorter length L gives a smaller T (shorter period), which corresponds to a higher oscillation frequency (since frequency = 1/T).",
    "Period increases with the SQUARE ROOT of length — shorter pendulums swing faster (shorter period, higher frequency), a frequently tested inverse relationship.",
    "Correct — a shorter pendulum has a shorter period (and thus higher frequency), per T = 2*pi*sqrt(L/g).",
    "Incorrect — a longer period would apply to a LONGER pendulum, not a shorter one.",
    "Incorrect — pendulum period clearly depends on length (via the square root relationship); it is not independent of length.",
    "Incorrect — pendulum period is a well-defined, calculable quantity (via the formula above), not undefined.")

add(146, "Wave speed = frequency x wavelength = 20 Hz x 15 m = 300 m/s.",
    "The universal wave equation is v = f x lambda (speed = frequency x wavelength). Substituting: v = 20 x 15 = 300 m/s.",
    "Always multiply frequency and wavelength directly (v=f*lambda) — a common slip is dividing instead of multiplying.",
    "Incorrect — 0.75 m/s would result from dividing frequency by wavelength instead of multiplying.",
    "Correct — 20 Hz x 15 m = 300 m/s.",
    "Incorrect — 35 m/s would result from adding frequency and wavelength instead of multiplying them.",
    "Incorrect — 1.33 m/s would result from an inverted division (15/20 rather than the correct 20 x 15).")

add(147, "Destructive interference occurs when two waves meet completely out of phase (crest meets trough), reducing or canceling amplitude.",
    "When two waves overlap such that the crest of one aligns with the trough of the other (a phase difference of 180 degrees / half a wavelength), their displacements subtract, partially or fully canceling the resultant wave's amplitude — the opposite of constructive interference, where in-phase waves add together.",
    "In-phase waves (crest meets crest) -> constructive interference (amplifies); out-of-phase waves (crest meets trough) -> destructive interference (cancels) — the two fundamental interference outcomes.",
    "Incorrect — in-phase waves meeting and amplifying each other describes constructive, not destructive, interference.",
    "Incorrect — the specific angle isn't what defines destructive interference; it's about the phase relationship (specifically, opposite phase) between the waves.",
    "Correct — waves meeting completely out of phase (crest-trough) is exactly the condition for destructive interference.",
    "Incorrect — identical frequencies and phases (fully in phase) describes constructive interference, the opposite of destructive.")

add(148, "Conduction transfers heat primarily through direct contact between particles, especially effective in solids.",
    "In conduction, faster-vibrating (hotter) particles transfer kinetic energy to neighboring, slower particles through direct collisions/contact, without the particles themselves moving from place to place — this is especially efficient in solids, where particles are tightly packed and fixed in relative position.",
    "Conduction = direct particle contact (best in solids); Convection = bulk fluid movement (liquids/gases); Radiation = electromagnetic waves (works even through a vacuum) — the three distinct heat transfer mechanisms.",
    "Incorrect — conduction occurs in solids, liquids, and gases (though most efficiently in solids), not exclusively in gases.",
    "Incorrect — bulk fluid movement describes convection, not conduction.",
    "Incorrect — electromagnetic waves through a vacuum describes radiation, not conduction (which actually requires a physical medium/direct contact).",
    "Correct — direct particle-to-particle contact, most effective in solids, is exactly how conduction transfers heat.")

add(149, "An isothermal process occurs at constant temperature throughout.",
    "'Iso-' means 'same/constant' and 'thermal' refers to temperature, so an isothermal process is, by definition, one where temperature remains unchanged even as other variables (pressure, volume) may change — distinct from adiabatic (no heat exchange), isochoric (constant volume), or isobaric (constant pressure) processes.",
    "Match each 'iso-' process name to its constant variable: isothermal=temperature, isobaric=pressure, isochoric=volume — and note adiabatic is a separate concept (zero heat exchange, not a constant-quantity name).",
    "Correct — constant temperature throughout is the literal definition of an isothermal process.",
    "Incorrect — no heat exchange with surroundings describes an adiabatic process, not isothermal.",
    "Incorrect — constant volume describes an isochoric (or isovolumetric) process, not isothermal.",
    "Incorrect — constant pressure describes an isobaric process, not isothermal.")

add(150, "By the first law of thermodynamics, ΔU = Q - W = 600 J - 200 J = 400 J.",
    "The first law of thermodynamics states ΔU = Q - W, where Q is heat added to the system and W is work done BY the system on its surroundings. Here, Q=600 J absorbed and W=200 J done by the gas, so ΔU = 600 - 200 = 400 J.",
    "Remember the sign convention: heat ADDED to the system is positive Q; work done BY the system (expansion) is subtracted — ΔU = Q - W, not Q + W.",
    "Incorrect — 800 J would result from adding Q and W instead of subtracting.",
    "Correct — 600 J (heat in) minus 200 J (work done by the gas) equals 400 J change in internal energy.",
    "Incorrect — -400 J has the wrong sign; since more heat was absorbed than work done, internal energy should increase (positive), not decrease.",
    "Incorrect — 200 J would just be the work value alone, without properly subtracting it from the heat absorbed.")

add(151, "Like electric charges repel each other.",
    "Coulomb's law describes the force between charges: same-sign (like) charges experience a repulsive force pushing them apart, while opposite-sign charges experience an attractive force pulling them together.",
    "Like charges REPEL, opposite charges ATTRACT — the most fundamental rule of electrostatics, analogous to (but opposite from) magnetic pole behavior naming conventions.",
    "Incorrect — attraction occurs between OPPOSITE charges, not like (same-sign) charges.",
    "Incorrect — like charges definitely interact (via repulsion); they don't simply have no interaction.",
    "Correct — like electric charges repel each other, a fundamental electrostatic principle.",
    "Incorrect — charges don't spontaneously neutralize each other just by being near one another; they exert a repulsive or attractive force instead.")

add(152, "Coulomb's law: force is directly proportional to the product of the two charges' magnitudes.",
    "Coulomb's law: F = k(q1*q2)/r^2. The force is directly proportional to the product of the charge magnitudes (q1 x q2) and inversely proportional to the square of the distance between them (1/r^2) — larger charges produce a stronger force; greater separation weakens it.",
    "Coulomb's law has TWO separate relationships: force is proportional to charge PRODUCT (direct) and inversely proportional to distance SQUARED — don't confuse the distance and charge dependencies.",
    "Incorrect — force is inversely (not directly) proportional to distance, and even then it's the SQUARE of distance, not distance alone.",
    "Incorrect — temperature of the surrounding medium isn't a factor in the basic Coulomb's law formula.",
    "Incorrect — force is inversely proportional to the square of distance, not directly proportional to it — this option describes the wrong relationship entirely.",
    "Correct — the product of the two charges' magnitudes is what force is directly proportional to in Coulomb's law.")

add(153, "Ohm's law: current equals voltage divided by resistance (I = V/R).",
    "Ohm's law relates voltage (V), current (I), and resistance (R) in a simple linear relationship: V = IR, which rearranges to I = V/R — current increases with voltage and decreases with resistance.",
    "Remember the Ohm's law triangle (V on top, I and R on the bottom) to quickly rearrange for whichever variable you need to solve for.",
    "Correct — I = V/R is the correct rearrangement of Ohm's law for current.",
    "Incorrect — power (P=IV or I^2R) is a related but different quantity from resistance in this formula.",
    "Incorrect — time doesn't appear in the basic Ohm's law relationship between current, voltage, and resistance.",
    "Incorrect — energy is a different quantity altogether, not what current is divided by in Ohm's law.")

add(154, "R1 (3 ohm) + R2 (3 ohm) in series = 6 ohm; that combination in parallel with R3 (6 ohm) gives (6x6)/(6+6) = 3 ohm total.",
    "First combine the series branch: R1+R2 = 3+3 = 6 ohm. Then combine this 6 ohm branch in parallel with R3 (6 ohm): 1/Rtotal = 1/6 + 1/6 = 2/6 = 1/3, so Rtotal = 3 ohm — matching the diagram's two equal parallel branches.",
    "Always simplify series combinations FIRST, then apply the parallel formula to the simplified branches — solving multi-step circuits one stage at a time avoids errors.",
    "Incorrect — 6 ohm is the resistance of the series branch alone (R1+R2), before combining it in parallel with R3.",
    "Correct — combining the 6 ohm series branch in parallel with R3 (also 6 ohm) gives (6x6)/(6+6)=3 ohm total.",
    "Incorrect — 12 ohm would result from simply adding R1+R2+R3 in series, ignoring that R3 is actually in parallel with the R1+R2 branch.",
    "Incorrect — 1.5 ohm doesn't match the correct parallel-combination calculation for two equal 6 ohm branches.")

add(155, "Two resistors (20 ohm, 5 ohm) in parallel: 1/Req = 1/20 + 1/5 = 5/20, so Req = 4 ohm.",
    "For resistors in parallel, 1/Req = 1/R1 + 1/R2 = 1/20 + 1/5 = 1/20 + 4/20 = 5/20 = 1/4, so Req = 4 ohm — always less than the smallest individual resistor in the parallel combination.",
    "A useful check: the equivalent resistance of a parallel combination is always SMALLER than the smallest individual resistor — here 4 ohm is indeed less than 5 ohm.",
    "Incorrect — 25 ohm would result from simply adding the two resistances (as if they were in series), not combining them in parallel.",
    "Incorrect — 15 ohm doesn't match the correct parallel-resistance formula for these two values.",
    "Correct — 1/20 + 1/5 = 5/20 = 1/4, so Req = 4 ohm.",
    "Incorrect — 100 ohm would result from multiplying (20 x 5) without dividing by the sum, skipping the actual parallel formula.")

add(156, "Current = Power / Voltage = 500 W / 250 V = 2 A.",
    "Electrical power relates to voltage and current via P = VI, so rearranged, I = P/V = 500/250 = 2 A.",
    "P=VI rearranges to I=P/V — make sure to divide power by voltage, not the reverse.",
    "Incorrect — 5 A doesn't match dividing 500 by 250 correctly.",
    "Incorrect — 0.5 A would result from an inverted calculation (250/500) rather than the correct 500/250.",
    "Incorrect — 125000 A would result from multiplying (500 x 250) instead of dividing, a huge and unrealistic overestimate.",
    "Correct — 500 W / 250 V = 2 A.")

add(157, "The magnetic field strength around a straight current-carrying wire decreases with increasing distance from the wire.",
    "The magnetic field around a long straight wire follows B = (mu0*I)/(2*pi*r), so field strength is inversely proportional to distance r from the wire — closer to the wire, the field is stronger; farther away, it weakens.",
    "Field strength around a wire follows an inverse relationship with distance (B ∝ 1/r) — similar in spirit to other 'weaker further away' field patterns in physics, though not inverse-square like gravity/Coulomb's law.",
    "Correct — magnetic field strength around a straight wire decreases as distance from the wire increases.",
    "Incorrect — field strength decreases (not increases) with greater distance from the wire, the opposite of this statement.",
    "Incorrect — field strength is clearly distance-dependent (via B ∝ 1/r), not unaffected by distance.",
    "Incorrect — the field is nonzero everywhere around the wire (just weaker farther away); it isn't zero at all points.")

add(158, "By Lenz's law, an induced current always flows in a direction that opposes the change in magnetic flux that caused it.",
    "Lenz's law is essentially a statement of energy conservation applied to electromagnetic induction: the induced current creates its own magnetic field that opposes whatever change (increase or decrease in flux) originally induced it, preventing the effect from reinforcing its own cause indefinitely.",
    "Lenz's law = OPPOSES the change (not reinforces it) — this 'opposing' direction is what keeps electromagnetic induction consistent with energy conservation.",
    "Incorrect — reinforcing the flux change would violate energy conservation; Lenz's law specifically describes opposition, not reinforcement.",
    "Correct — an induced current flows in a direction that opposes the change in magnetic flux, per Lenz's law.",
    "Incorrect — Lenz's law specifically DOES relate the induced current's direction to the original flux change (in an opposing sense), not with no relationship at all.",
    "Incorrect — the induced current direction depends on (and opposes) the flux change; it's not fixed independent of that change.")

add(159, "A neutron carries no net electric charge (it's electrically neutral).",
    "As the name suggests, neutrons are one of the three main subatomic particles (alongside positively charged protons and negatively charged electrons) and carry zero net electric charge, despite having internal quark structure with partial charges that cancel out overall.",
    "Proton = positive; Electron = negative; Neutron = neutral (zero charge) — the fundamental charges of the three basic subatomic particles.",
    "Incorrect — a positive charge describes the proton, not the neutron.",
    "Incorrect — a negative charge describes the electron, not the neutron.",
    "Correct — the neutron's overall electric charge is neutral (zero), consistent with its name.",
    "Incorrect — a neutron's charge is always neutral; it doesn't vary depending on which atom it's part of.")

add(160, "In alpha decay, an unstable nucleus emits an alpha particle: a helium nucleus (2 protons and 2 neutrons).",
    "Alpha decay reduces a nucleus's mass number by 4 and its atomic number by 2, as it ejects an alpha particle — identical in composition to a helium-4 nucleus (2 protons, 2 neutrons) — a relatively large, slow-moving, and easily-shielded form of radiation compared to beta or gamma emission.",
    "Alpha particle = helium nucleus (2p+2n); Beta particle = high-speed electron (or positron); Gamma = high-energy photon — the three classic types of radioactive decay emission.",
    "Incorrect — an electron and antineutrino describes beta-minus decay, not alpha decay.",
    "Incorrect — a positron describes beta-plus decay, not alpha decay.",
    "Incorrect — gamma decay involves emission of a high-energy photon alone, typically accompanying (not defining) alpha or beta decay, and doesn't itself define alpha decay.",
    "Correct — an alpha particle, equivalent to a helium nucleus (2 protons + 2 neutrons), is exactly what's emitted in alpha decay.")

add(161, "With a 3-hour half-life, 12 hours = 4 half-lives, so 400 g reduces to 400 x (1/2)^4 = 25 g.",
    "Number of half-lives elapsed = total time / half-life = 12 / 3 = 4. Remaining amount = initial amount x (1/2)^(number of half-lives) = 400 x (1/2)^4 = 400 / 16 = 25 g.",
    "Always compute the NUMBER of half-lives first (total time / half-life period), then apply (1/2) raised to that power — don't just halve the amount once regardless of how many half-lives have passed.",
    "Correct — after 4 half-lives (12 h / 3 h per half-life), 400 g reduces to 400/16 = 25 g.",
    "Incorrect — 50 g would correspond to only 3 half-lives elapsed (400/8=50), not the full 4 half-lives in 12 hours.",
    "Incorrect — 12.5 g would correspond to 5 half-lives, one more than the actual 4 half-lives elapsed in 12 hours.",
    "Incorrect — 100 g would correspond to only 2 half-lives elapsed, undercounting the actual 4 half-lives in the given 12-hour period.")

add(162, "For a convex lens with the object beyond 2F, the image forms real, inverted, and diminished, between F and 2F on the far side.",
    "Using the thin-lens equation 1/v = 1/f - 1/u, an object placed farther than 2f from a converging lens produces a real image that is smaller than the object (diminished), inverted, and located between F and 2F on the opposite side of the lens — as shown and computed (u=6, f=2, giving v=3, between F=2 and 2F=4) in the diagram.",
    "Object position vs image outcome for a convex lens: beyond 2F -> real/inverted/diminished (between F and 2F); at 2F -> real/inverted/same-size; between F and 2F -> real/inverted/magnified (beyond 2F); at F -> image at infinity; within F -> virtual/upright/magnified.",
    "Incorrect — a virtual, upright, magnified image occurs when the object is placed WITHIN the focal length, not beyond 2F.",
    "Correct — an object beyond 2F produces a real, inverted, diminished image located between F and 2F, exactly as computed and drawn in the diagram.",
    "Incorrect — a real, upright image is physically impossible for a simple single convex lens forming a real image; real images from a single converging lens are always inverted.",
    "Incorrect — a virtual image would form only if the object were placed within the focal length; an object beyond 2F always produces a real image, not virtual.")

data = E
print(f"Physics batch: {len(data)} entries, ids {data[0]['id']}-{data[-1]['id']}")
assert len(data) == 36
OUT.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
print("wrote", OUT)
