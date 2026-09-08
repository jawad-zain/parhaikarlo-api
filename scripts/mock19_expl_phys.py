import json
from pathlib import Path

EXPL = {
8251: dict(
    short="Speed = distance/time = 100 m / 20 s = 5 m/s.",
    long="Constant speed is simply total distance divided by total time: 100 m ÷ 20 s = 5 m/s.",
    trick="Make sure units are consistent (meters and seconds) before dividing — a simple but essential step.",
    options=dict(a="Correct — 100 m / 20 s = 5 m/s.",
                 b="20 m/s would result from dividing the wrong way (time/distance inverted, or a slip).",
                 c="2000 m/s would come from multiplying instead of dividing.",
                 d="0.2 m/s inverts the actual division (20/100 instead of 100/20).")
),
8252: dict(
    short="Acceleration = Δv/Δt = (20-5)/3 = 5 m/s².",
    long="Acceleration is the change in velocity over time: (20 m/s - 5 m/s) / 3 s = 15/3 = 5 m/s².",
    trick="Don't forget to take the DIFFERENCE in velocity (final minus initial), not just divide the final velocity by time.",
    options=dict(a="Correct — (20-5)/3 = 5 m/s².",
                 b="15 m/s² is just the velocity difference itself, without dividing by time.",
                 c="25 m/s² would come from adding instead of subtracting velocities.",
                 d="3 m/s² doesn't match the actual calculation of Δv/Δt here.")
),
8253: dict(
    short="v = gt = 10 × 3 = 30 m/s (free fall from rest).",
    long="For an object dropped from rest under gravity, final velocity v = gt (since initial velocity = 0). With g=10 m/s² and t=3 s, v = 10 × 3 = 30 m/s.",
    trick="Don't forget the object starts from rest (u=0) — this simplifies v=u+gt to just v=gt.",
    options=dict(a="10 m/s would just be the value of g itself, not the actual final velocity.",
                 b="Correct — v = gt = 10 × 3 = 30 m/s.",
                 c="15 m/s doesn't match g×t for these given values.",
                 d="60 m/s would come from doubling the correct answer, an arithmetic slip.")
),
8254: dict(
    short="Constant velocity means zero net force (Newton's first law).",
    long="By Newton's first law, an object moving at constant velocity (no acceleration) has zero net force acting on it — any unbalanced force would cause it to accelerate (speed up, slow down, or change direction).",
    trick="'Constant velocity' specifically means no acceleration, which by F=ma directly implies F_net=0 — don't assume constant motion requires an ongoing force to sustain it (a common Aristotelian misconception).",
    options=dict(a="An increasing net force would cause changing (non-constant) acceleration, contradicting constant velocity.",
                 b="Correct — constant velocity means zero acceleration, hence zero net force.",
                 c="A decreasing force would still imply some acceleration, not constant velocity.",
                 d="A net force is not always positive; and more fundamentally, constant velocity requires the net force to be exactly zero.")
),
8255: dict(
    short="Mass = Force/acceleration = 15 N / 3 m/s² = 5 kg.",
    long="From Newton's second law, F = ma, so m = F/a = 15 N / 3 m/s² = 5 kg.",
    trick="Make sure to divide force by acceleration (not the reverse) to solve for mass — a common mix-up when rearranging F=ma.",
    options=dict(a="Correct — m = F/a = 15/3 = 5 kg.",
                 b="45 kg would come from multiplying instead of dividing (15 × 3).",
                 c="12 kg doesn't match the correct F/a calculation.",
                 d="18 kg doesn't match the correct F/a calculation.")
),
8256: dict(
    short="Newton's third law: every action force has an equal, opposite reaction force.",
    long="Newton's third law states that forces occur in pairs: whenever object A exerts a force on object B, object B exerts an equal-magnitude, opposite-direction force back on object A.",
    trick="Don't confuse the three Newton's laws — momentum conservation is a consequence often linked with the third law but is a distinct statement; inertia is the first law; F=ma is the second law.",
    options=dict(a="Momentum conservation, while related, is a separate principle, not the direct statement of the third law.",
                 b="An object in motion staying in motion (inertia) is Newton's FIRST law.",
                 c="Force equals mass times acceleration is Newton's SECOND law.",
                 d="Correct — equal and opposite action-reaction force pairs describe Newton's third law.")
),
8257: dict(
    short="a = (F - friction)/m = (25 - 0.2×5×10)/5 = 15/5 = 3 m/s².",
    long="Friction force = μmg = 0.2 × 5 kg × 10 m/s² = 10 N. Net force = applied force - friction = 25 N - 10 N = 15 N. Acceleration = net force / mass = 15/5 = 3 m/s².",
    trick="Don't forget to subtract the friction force from the applied force BEFORE dividing by mass to get acceleration — using the applied force alone (25/5=5) is a common shortcut error.",
    options=dict(a="Correct — after subtracting friction (10 N) from the applied force (25 N), net force 15 N gives a=3 m/s².",
                 b="5 m/s² would result from ignoring friction entirely (25/5), which is incorrect.",
                 c="1 m/s² doesn't match the correct net-force calculation.",
                 d="2 m/s² doesn't match the correct net-force calculation.")
),
8258: dict(
    short="Work done by a perpendicular force is zero (W = Fd·cosθ, cos90°=0).",
    long="Work is defined as W = Fd·cos(θ), where θ is the angle between force and displacement. When the force is perpendicular to displacement (θ=90°), cos(90°)=0, so no work is done by that force, regardless of its magnitude.",
    trick="A force can be large and still do zero work if it's perpendicular to motion — classic example: the normal force or centripetal force in circular motion do no work on the moving object.",
    options=dict(a="Correct — cos(90°)=0 makes the work done by a perpendicular force zero.",
                 b="The work isn't 'always negative'; it's specifically zero at exactly 90°, not negative.",
                 c="Work is well-defined (via the cosine formula) even at 90°, not undefined.",
                 d="Maximum work (W=Fd) happens when the force is PARALLEL (0°) to displacement, not perpendicular.")
),
8259: dict(
    short="PE = mgh = 5 × 10 × 4 = 200 J.",
    long="Gravitational potential energy is calculated as PE = mgh: 5 kg × 10 m/s² × 4 m = 200 J.",
    trick="Make sure to multiply all three quantities (mass, g, height) together — a common slip is forgetting one factor.",
    options=dict(a="40 J would result from omitting a factor (like using g=2 or omitting mass).",
                 b="9 J doesn't correspond to any straightforward combination of the given values.",
                 c="20 J would result from omitting the mass factor (just g×h=40, still not matching either).",
                 d="Correct — mgh = 5×10×4 = 200 J.")
),
8260: dict(
    short="KE = ½mv² = ½ × 6 × 4² = 48 J.",
    long="Kinetic energy formula: KE = ½mv² = 0.5 × 6 kg × (4 m/s)² = 0.5 × 6 × 16 = 48 J.",
    trick="Remember to SQUARE the velocity before multiplying — forgetting to square it (using v instead of v²) is a very common kinetic-energy mistake.",
    options=dict(a="96 J would result from forgetting the ½ factor (doubling the correct answer).",
                 b="Correct — ½ × 6 × 16 = 48 J.",
                 c="24 J would result from an incomplete calculation, like using v instead of v² somewhere.",
                 d="12 J doesn't match the full ½mv² calculation with these values.")
),
8261: dict(
    short="Power = Energy/time = 18000 J / 30 s = 600 W.",
    long="Power is defined as the rate of energy transfer: P = E/t = 18000 J / 30 s = 600 W.",
    trick="Make sure to divide (not multiply) energy by time to get power — a common slip is multiplying the two values instead.",
    options=dict(a="540000 W would result from multiplying instead of dividing.",
                 b="60 W doesn't match the correct division (an order-of-magnitude slip).",
                 c="6000 W would result from a decimal-point error in the division.",
                 d="Correct — 18000/30 = 600 W.")
),
8262: dict(
    short="Centripetal acceleration always points toward the center of the circular path.",
    long="In uniform circular motion, the centripetal acceleration (and corresponding centripetal force) is always directed toward the center of the circle, constantly changing the direction of velocity to keep the object moving in a circular path (even though speed stays constant).",
    trick="Centripetal means 'center-seeking' — don't confuse it with centrifugal (an apparent outward effect in a rotating, non-inertial reference frame) or with the tangential velocity direction.",
    options=dict(a="Pointing away from the center describes a (fictitious) centrifugal effect, not real centripetal acceleration.",
                 b="The direction of velocity is tangent to the circle, perpendicular to the centripetal acceleration, not the same direction.",
                 c="Tangent to the path describes the velocity direction, not the acceleration direction in uniform circular motion.",
                 d="Correct — centripetal acceleration always points toward the center of the circular path.")
),
8263: dict(
    short="Doubling distance reduces gravitational force to 1/4 (inverse-square law).",
    long="Newton's law of gravitation states F = Gm1m2/r². Since force is inversely proportional to the SQUARE of distance, doubling r (r->2r) makes the force F -> F/(2²) = F/4 — one-quarter of the original.",
    trick="Don't apply a simple inverse relationship (which would give 1/2) — gravity follows an INVERSE-SQUARE law, so doubling distance quarters the force, not halves it.",
    options=dict(a="Correct — doubling distance in an inverse-square law reduces force to 1/4.",
                 b="4 times the original would result from an incorrect direct-square relationship, not inverse-square.",
                 c="2 times the original doesn't match the inverse-square relationship at all.",
                 d="1/2 of the original would result from an incorrect simple inverse (not inverse-SQUARE) relationship.")
),
8264: dict(
    short="Doubling mass (radius fixed) doubles surface gravity (g = GM/R²).",
    long="Surface gravity is given by g = GM/R². If mass M doubles while radius R stays the same, g simply doubles proportionally (since g is directly proportional to M when R is constant).",
    trick="Don't confuse this with the RADIUS-dependence (inverse-square) — here it's the MASS that's changing, and g is directly (not inversely) proportional to mass.",
    options=dict(a="Halving g would be incorrect; doubling mass increases (not decreases) surface gravity.",
                 b="Quadrupling would apply if mass quadrupled, or misapplies a squared relationship that doesn't exist for mass here.",
                 c="g would only stay the same if mass were unchanged, but here mass is explicitly doubled.",
                 d="Correct — g is directly proportional to mass (with R fixed), so doubling mass doubles g.")
),
8265: dict(
    short="An object floats when buoyant force equals (or exceeds, at max displacement) its weight.",
    long="An object floats in equilibrium when the upward buoyant force exactly balances its downward weight (Archimedes' principle) — for a floating object at rest, buoyant force = weight (it displaces just enough fluid to support itself).",
    trick="For a floating (not sinking or rising) object, buoyant force must be at least equal to weight — if buoyant force capacity is available but the object displaces exactly enough water, it settles into floating equilibrium with buoyant force = weight.",
    options=dict(a="Correct — floating equilibrium occurs when the buoyant force is (at least) equal to the object's weight.",
                 b="If buoyant force were less than weight, the object would sink, not float.",
                 c="Buoyant force is never simply 'always zero' for an object in a fluid — it depends on displaced fluid volume.",
                 d="Twice the weight would cause the object to accelerate upward/be pushed out of the fluid, not sit in floating equilibrium.")
),
8266: dict(
    short="Archimedes' principle: buoyant force = weight of fluid displaced.",
    long="Archimedes' principle states that the buoyant force on a submerged (or floating) object equals the weight of the fluid that the object displaces, regardless of the object's own weight or density directly.",
    trick="Buoyant force depends on the DISPLACED FLUID's weight, not the object's own weight or the surface pressure directly — a common wording trap.",
    options=dict(a="The object's own weight is a separate quantity from the buoyant force it experiences.",
                 b="Correct — buoyant force equals the weight of the fluid displaced.",
                 c="Object density alone doesn't directly give the buoyant force value (though it affects whether the object floats or sinks).",
                 d="Surface pressure isn't the direct basis of Archimedes' principle; displaced fluid weight is.")
),
8267: dict(
    short="Continuity equation: fluid speeds up in a narrower pipe section (A1v1=A2v2).",
    long="The continuity equation (A1v1 = A2v2) reflects conservation of mass flow rate for an incompressible fluid: as cross-sectional area decreases (narrower pipe), velocity must increase proportionally to keep the flow rate constant.",
    trick="Don't reverse the relationship — area and velocity are INVERSELY related (smaller area, higher speed), a common point of confusion.",
    options=dict(a="Speed actually increases (not decreases) in the narrower section, per the continuity equation.",
                 b="Correct — flow rate conservation (A1v1=A2v2) means velocity increases as area decreases.",
                 c="Speed does NOT stay the same; it must change to conserve the flow rate as area changes.",
                 d="Speed doesn't become zero; it increases (doesn't stop) in the narrower section.")
),
8268: dict(
    short="The highest point of a transverse wave is the crest.",
    long="In a transverse wave, the crest is the highest point (maximum positive displacement) of the wave, while the trough is the lowest point (maximum negative displacement).",
    trick="Don't confuse crest/trough (wave height extremes) with node (a point of zero displacement in a standing wave) or wavelength (the distance between repeating points).",
    options=dict(a="Correct — the crest is the wave's highest point.",
                 b="The trough is the LOWEST point, the opposite of what's asked.",
                 c="A node is a point of zero displacement (in standing waves), not the highest point.",
                 d="Wavelength is a distance measurement between repeating points, not a point on the wave itself.")
),
8269: dict(
    short="A longer pendulum has a longer period (lower frequency).",
    long="A simple pendulum's period is T = 2π√(L/g), which increases with the square root of its length L. So a longer pendulum swings more slowly, taking a longer time per swing (longer period, lower frequency).",
    trick="Don't assume period is independent of length (that's true for amplitude in small-angle approximation, but NOT for length) — length is a primary factor determining a pendulum's period.",
    options=dict(a="A pendulum's period IS well-defined by the formula T=2π√(L/g); it's not undefined.",
                 b="A longer pendulum has a LONGER period, not a shorter one.",
                 c="Correct — longer length gives a longer period (lower frequency), per T=2π√(L/g).",
                 d="Period does depend on length (via the square-root relationship), so it's not independent of length.")
),
8270: dict(
    short="Wave speed = f × λ = 25 × 12 = 300 m/s.",
    long="The wave speed equation is v = fλ (frequency × wavelength): 25 Hz × 12 m = 300 m/s.",
    trick="Make sure to multiply (not divide) frequency and wavelength — a common slip is dividing one by the other instead.",
    options=dict(a="Correct — v = fλ = 25 × 12 = 300 m/s.",
                 b="0.48 m/s would result from an incorrect division (12/25) rather than multiplication.",
                 c="37 m/s doesn't match the fλ multiplication.",
                 d="2.08 m/s would result from an incorrect division (25/12) rather than multiplication.")
),
8271: dict(
    short="Constructive interference occurs when waves are in phase, amplifying amplitude.",
    long="Constructive interference happens when two waves meet in phase (crest aligns with crest, trough with trough), so their amplitudes add together, producing a larger resultant wave amplitude.",
    trick="Destructive interference (the opposite — waves out of phase, amplitudes cancel) is a common confusable pairing — always check whether the waves described are 'in phase' (constructive) or 'out of phase' (destructive).",
    options=dict(a="A specific 90-degree angle isn't the defining condition; it's about wave PHASE relationship, not spatial angle.",
                 b="A defined phase relationship (in phase) IS required for constructive interference, not an arbitrary/random relationship.",
                 c="Completely out of phase describes DESTRUCTIVE interference, the opposite effect.",
                 d="Correct — in-phase waves (crest meets crest) add amplitudes, giving constructive interference.")
),
8272: dict(
    short="Convection transfers heat via bulk movement of a heated fluid.",
    long="Convection is heat transfer through the actual physical movement (bulk flow) of a heated fluid (liquid or gas), as warmer, less dense fluid rises and cooler, denser fluid sinks, creating convection currents.",
    trick="Conduction (direct particle-to-particle contact, mainly in solids) and radiation (electromagnetic waves, works even through a vacuum) are the OTHER two heat transfer methods — don't mix up which mechanism belongs to which name.",
    options=dict(a="Correct — convection specifically involves bulk fluid movement carrying heat.",
                 b="Direct particle-to-particle contact in solids describes conduction, not convection.",
                 c="Electromagnetic waves through a vacuum describes radiation, not convection.",
                 d="Convection specifically requires a fluid (liquid/gas) that can flow; it doesn't occur 'only within solids.'")
),
8273: dict(
    short="An adiabatic process involves no heat exchange with the surroundings.",
    long="By definition, an adiabatic process is one in which no heat (Q) is transferred into or out of the system — any internal energy change comes entirely from work done on/by the system (ΔU = -W for adiabatic, per the first law).",
    trick="Don't confuse adiabatic (no heat transfer, Q=0) with isothermal (constant temperature), isochoric (constant volume), or isobaric (constant pressure) — each thermodynamic process type has a distinct defining condition.",
    options=dict(a="Constant temperature describes an ISOTHERMAL process, not adiabatic.",
                 b="Constant volume describes an ISOCHORIC process, not adiabatic.",
                 c="Constant pressure describes an ISOBARIC process, not adiabatic.",
                 d="Correct — 'no heat exchange with the surroundings' is the defining condition of an adiabatic process.")
),
8274: dict(
    short="First law: ΔU = Q - W = 800 - 300 = 500 J.",
    long="The first law of thermodynamics states ΔU = Q - W, where Q is heat absorbed by the system and W is work done BY the system on the surroundings. Here, ΔU = 800 J - 300 J = 500 J.",
    trick="Sign convention matters — make sure you're using Q absorbed (positive) minus W done BY the gas (positive, since it does work outward), not accidentally adding them.",
    options=dict(a="Correct — ΔU = 800 - 300 = 500 J.",
                 b="1100 J would result from adding instead of subtracting the two values.",
                 c="-500 J has the correct magnitude but wrong sign (would occur with reversed sign convention/mislabeled work).",
                 d="300 J is just the work value alone, not the actual change in internal energy.")
),
8275: dict(
    short="Opposite charges attract each other.",
    long="Coulomb's law describes that like charges (both positive or both negative) repel, while opposite charges (one positive, one negative) attract each other via the electrostatic force.",
    trick="Don't mix up 'like charges repel, opposite charges attract' — a very basic but essential electrostatics rule.",
    options=dict(a="Correct — opposite charges attract each other.",
                 b="Repulsion occurs between LIKE (same-sign) charges, not opposite charges.",
                 c="Opposite charges do interact (attract); 'no interaction' is incorrect.",
                 d="Charges don't spontaneously neutralize just from proximity/interaction; they simply exert forces on each other.")
),
8276: dict(
    short="Coulomb's law: force is inversely proportional to the square of the distance.",
    long="Coulomb's law: F = kq1q2/r². The force between two point charges is directly proportional to the product of the charges and inversely proportional to the SQUARE of the distance between them (an inverse-square law, analogous to gravity).",
    trick="Don't confuse 'inversely proportional to distance' (a simple inverse) with 'inversely proportional to distance SQUARED' (inverse-square) — Coulomb's law is specifically inverse-square.",
    options=dict(a="The force is DIRECTLY (not inversely) proportional to the product of the charges.",
                 b="Correct — Coulomb's law force is inversely proportional to the square of the distance.",
                 c="Medium temperature isn't part of the basic Coulomb's law formula (that's more a material/dielectric consideration).",
                 d="The sum of the charges isn't the relevant quantity; it's the PRODUCT of the charges that matters (and directly, not inversely).")
),
8277: dict(
    short="Ohm's law: V = IR (voltage = current × resistance).",
    long="Ohm's law states that voltage across a conductor equals the current flowing through it multiplied by its resistance: V = IR.",
    trick="Don't confuse Ohm's law (V=IR) with the power formula (P=IV) — both involve voltage and current, but relate to different quantities (resistance vs. power).",
    options=dict(a="Time isn't part of Ohm's law's basic V=IR relationship.",
                 b="Energy isn't the multiplying factor in Ohm's law; that's a separate quantity (related via P and t).",
                 c="Power is a related but distinct quantity (P=IV), not what current is multiplied by in Ohm's law itself.",
                 d="Correct — Ohm's law states V = I × R (current × resistance).")
),
8278: dict(
    short="R1(4)∥R2(4)=2Ω, then +R3(2Ω) in series = 4Ω total.",
    long="R1 and R2 (both 4Ω) in parallel combine as (4×4)/(4+4) = 16/8 = 2Ω. This parallel combination is then in series with R3 (2Ω), so total resistance = 2Ω + 2Ω = 4Ω.",
    trick="Always resolve the parallel section into its single equivalent resistance FIRST, then simply add the series resistance — don't try to combine series and parallel resistors in one step.",
    options=dict(a="10 ohm doesn't match the correct parallel-then-series calculation.",
                 b="6 ohm would result from a calculation error, like adding R1+R2+R3 directly as if all in series.",
                 c="Correct — R1∥R2 (2Ω) + R3 (2Ω) in series = 4Ω total.",
                 d="2 ohm is just the parallel combination alone, forgetting to add R3 in series.")
),
8279: dict(
    short="10Ω and 15Ω in parallel: (10×15)/(10+15) = 150/25 = 6Ω.",
    long="Parallel resistance formula: R_eq = (R1×R2)/(R1+R2) = (10×15)/25 = 150/25 = 6 ohm.",
    trick="Remember that parallel combined resistance is always LESS than the smallest individual resistor (6Ω < 10Ω here) — a good sanity check on your answer.",
    options=dict(a="150 ohm is just the numerator of the parallel formula, without dividing by the sum.",
                 b="25 ohm is just the sum (10+15), not the actual parallel combination.",
                 c="Correct — (10×15)/(10+15) = 6 ohm.",
                 d="5 ohm doesn't match the correct parallel resistance calculation.")
),
8280: dict(
    short="Current = Power/Voltage = 1000 W / 200 V = 5 A.",
    long="From P = IV, current I = P/V = 1000 W / 200 V = 5 A.",
    trick="Make sure to divide power by voltage (not the reverse) to solve for current — a common algebra slip when rearranging P=IV.",
    options=dict(a="Correct — I = P/V = 1000/200 = 5 A.",
                 b="0.2 A would result from inverting the division (200/1000).",
                 c="200000 A would result from multiplying instead of dividing.",
                 d="20 A doesn't match the correct P/V calculation.")
),
8281: dict(
    short="Solenoid field strength increases with more turns per length or more current.",
    long="The magnetic field inside a solenoid is given by B = μ₀nI, where n is turns per unit length and I is current. Increasing either the number of turns per unit length or the current increases the field strength.",
    trick="Removing the iron core actually DECREASES field strength (an iron core, being ferromagnetic, greatly amplifies the field) — a common opposite-direction trap.",
    options=dict(a="Removing the iron core would DECREASE, not increase, the field strength, since iron amplifies magnetic fields.",
                 b="Decreasing turns would decrease, not increase, field strength.",
                 c="Decreasing current would decrease, not increase, field strength.",
                 d="Correct — more turns per length or more current increases the solenoid's magnetic field strength.")
),
8282: dict(
    short="Induced EMF depends on the rate of change of magnetic flux (Faraday's law).",
    long="Faraday's law states that the magnitude of induced EMF equals the rate of change of magnetic flux through a circuit: EMF = -dΦ/dt. A faster-changing flux induces a larger EMF.",
    trick="It's specifically the RATE OF CHANGE of flux that matters — a constant (unchanging) flux, no matter how large, induces zero EMF.",
    options=dict(a="Wire color has no physical relevance to electromagnetic induction.",
                 b="Magnet temperature isn't the determining factor in Faraday's law (unless it demagnetizes the magnet, which is a separate, extreme effect).",
                 c="Induced EMF specifically DOES depend on flux change; 'independent of flux change' directly contradicts Faraday's law.",
                 d="Correct — Faraday's law ties induced EMF directly to the rate of change of magnetic flux.")
),
8283: dict(
    short="A proton carries a positive electric charge.",
    long="Protons are one of the fundamental nucleon particles, carrying a fixed positive elementary charge (+1e), balancing the negative charge of electrons in a neutral atom.",
    trick="Don't confuse proton (positive) with electron (negative) or neutron (neutral, no charge) — basic subatomic particle charges are foundational and often directly tested.",
    options=dict(a="A proton's charge is not neutral/zero — that describes a neutron.",
                 b="A proton's charge is fixed (always +1e); it doesn't vary by atom.",
                 c="Correct — a proton carries a positive charge.",
                 d="Negative charge describes an electron, not a proton.")
),
8284: dict(
    short="Beta-minus decay emits an electron and antineutrino as a neutron becomes a proton.",
    long="In beta-minus (β⁻) decay, a neutron in the nucleus converts into a proton, emitting an electron (the 'beta particle') and an antineutrino to conserve energy, momentum, and lepton number.",
    trick="Beta-minus decay increases the atomic number by 1 (neutron→proton) while mass number stays the same — don't confuse it with alpha decay (helium nucleus emission) or beta-plus/positron decay (proton→neutron).",
    options=dict(a="A photon alone (gamma decay) doesn't involve nucleon conversion; that's a different decay type.",
                 b="Two protons being emitted isn't what happens in beta-minus decay.",
                 c="A helium nucleus (2 protons + 2 neutrons) is emitted in ALPHA decay, not beta-minus decay.",
                 d="Correct — beta-minus decay emits an electron and antineutrino as a neutron converts to a proton.")
),
8285: dict(
    short="After 8 hours (4 half-lives of 2h each), 320g -> 320/2^4 = 20g remains.",
    long="Number of half-lives elapsed = total time / half-life = 8h / 2h = 4. Remaining amount = initial × (1/2)^n = 320 × (1/2)^4 = 320/16 = 20 g.",
    trick="Make sure to correctly count the number of half-lives (8÷2=4, not simply using 8 or 2 directly) before applying the (1/2)^n formula.",
    options=dict(a="80 g would come from only 2 half-lives, undercounting the actual number of half-lives elapsed.",
                 b="Correct — after 4 half-lives, 320g reduces to 20g (320/16).",
                 c="40 g would come from only 3 half-lives, one short of the actual 4 half-lives elapsed.",
                 d="10 g would come from 5 half-lives, one too many for the actual 8-hour duration given.")
),
8286: dict(
    short="Object between F and C on a concave mirror -> real, inverted, magnified image beyond C.",
    long="Using the mirror formula 1/v = 1/f - 1/u: for an object between F and C (say f=2, u=3, both on the same side), v = 1/(1/2 - 1/3) = 1/(1/6) = 6, which is beyond C (at 4). Since |v|>|u|, the magnification |v/u|=2 (magnified), and the image is inverted (real image sign convention), forming on the same (real) side as the object, beyond C.",
    trick="A common mix-up is assuming object-between-F-and-C gives a virtual image (that's only true for object INSIDE F) — between F and C, the image is REAL, inverted, and magnified, formed further out than C.",
    options=dict(a="Between F and C gives a MAGNIFIED (not diminished) image, and it's real (this option's other terms don't fit either).",
                 b="Virtual images form only when the object is WITHIN the focal length (inside F), not between F and C.",
                 c="Correct — the mirror formula confirms a real, inverted, magnified image beyond C for an object between F and C.",
                 d="Virtual, upright, magnified describes the object-within-F case, not between F and C.")
),
}

def main():
    root = Path(__file__).parent.parent
    out = []
    for qid, e in EXPL.items():
        out.append({"id": qid, "short": e["short"], "long": e["long"], "trick": e["trick"], "options": e["options"]})
    out_path = root / "scripts" / "mock19_explanations_physics.json"
    out_path.write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Wrote {len(out)} explanations to {out_path}")

if __name__ == "__main__":
    main()
