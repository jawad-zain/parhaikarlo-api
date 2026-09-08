import json
from pathlib import Path

EXPL = {
8431: dict(
    short="Speed = distance/time = 150 km / 3 h = 50 km/h.",
    long="Constant speed is simply total distance divided by total time: 150 km ÷ 3 h = 50 km/h.",
    trick="Don't multiply distance and time by mistake (450) or invert the ratio (0.02) — always divide distance by time for speed.",
    options=dict(a="30 km/h would result from an incorrect division.",
                 b="450 km/h comes from multiplying instead of dividing.",
                 c="Correct — 150 km / 3 h = 50 km/h.",
                 d="0.02 km/h comes from inverting the division (time/distance).")
),
8432: dict(
    short="Acceleration = Δv/Δt = (20-8)/4 = 3 m/s^2.",
    long="Acceleration is the change in velocity divided by the time taken: (20 m/s − 8 m/s) / 4 s = 12/4 = 3 m/s^2.",
    trick="Don't divide by the wrong quantity — use the CHANGE in velocity (12 m/s), not the final velocity alone (20 m/s), divided by time.",
    options=dict(a="2 m/s^2 would come from an incorrect velocity change.",
                 b="5 m/s^2 doesn't match (20-8)/4=3.",
                 c="4 m/s^2 is close but not exact — 12/4 is exactly 3, not 4.",
                 d="Correct — (20-8)/4 = 3 m/s^2.")
),
8433: dict(
    short="At the highest point, v=0. Using v=u-gt: 0=u-10(2), so u=20 m/s.",
    long="At the top of the throw, the object's instantaneous velocity is zero. Using v = u − gt with v=0, g=10 m/s^2, t=2 s: 0 = u − 20, so u = 20 m/s.",
    trick="Remember the velocity is zero only momentarily AT the peak, not throughout the rise — use that specific condition to solve for initial velocity.",
    options=dict(a="Correct — u = g×t = 10×2 = 20 m/s.",
                 b="10 m/s would only account for half the time correctly used.",
                 c="5 m/s is far too small for a 2-second rise under g=10 m/s^2.",
                 d="40 m/s would result from doubling the correct value unnecessarily.")
),
8434: dict(
    short="Newton's first law: an object continues moving unless acted upon by an unbalanced (net) force.",
    long="Newton's first law of motion (law of inertia) states an object maintains its state of motion (or rest) unless a net (unbalanced) external force acts on it. Balanced forces produce no change in motion.",
    trick="A 'balanced force' by definition produces zero net force, so it can never change an object's motion — only an UNBALANCED force can.",
    options=dict(a="A balanced force means the net force is zero, so it cannot change the object's motion.",
                 b="Correct — an unbalanced (net) force is required to change an object's state of motion.",
                 c="'Internal force' isn't the standard formulation; external unbalanced force is what matters here.",
                 d="A frictionless surface is unrelated to the law's core statement about force and motion.")
),
8435: dict(
    short="Newton's second law: F=ma, so m=F/a=30/5=6 kg.",
    long="Rearranging F=ma to solve for mass: m = F/a = 30 N / 5 m/s^2 = 6 kg.",
    trick="Make sure to divide force by acceleration (not multiply) when solving for mass — F=ma means m=F/a.",
    options=dict(a="25 kg doesn't match 30/5=6.",
                 b="150 kg would come from multiplying 30×5 instead of dividing.",
                 c="Correct — 30 N / 5 m/s^2 = 6 kg.",
                 d="35 kg doesn't match the correct division.")
),
8436: dict(
    short="Momentum = mass x velocity (p=mv).",
    long="Momentum is defined as the product of an object's mass and its velocity: p = mv. It is a vector quantity in the direction of velocity.",
    trick="Don't confuse momentum (mass x velocity) with force (mass x acceleration) or impulse (force x time) — they use different variable pairs.",
    options=dict(a="Mass and displacement would relate to a different (non-standard) quantity.",
                 b="Mass and acceleration is the definition of force (F=ma), not momentum.",
                 c="Force and time is the definition of impulse, not momentum.",
                 d="Correct — momentum = mass x velocity.")
),
8437: dict(
    short="Friction = μmg = 0.3x6x10=18N; net force=30-18=12N; a=F/m=12/6=2 m/s^2.",
    long="Friction force = μ×N = μ×mg = 0.3×6×10 = 18 N. Net force = applied force − friction = 30 − 18 = 12 N. Acceleration = net force/mass = 12/6 = 2 m/s^2.",
    trick="Always subtract friction from the applied force to get the NET force before dividing by mass — using the applied 30 N directly (without subtracting friction) gives a wrong, larger acceleration.",
    options=dict(a="Correct — net force (30-18=12N) divided by mass (6kg) gives 2 m/s^2.",
                 b="5 m/s^2 would come from ignoring friction entirely (30/6).",
                 c="3 m/s^2 doesn't match the correctly computed net-force calculation.",
                 d="1 m/s^2 underestimates the net force even further than needed.")
),
8438: dict(
    short="The SI unit of work and energy is the Joule (J).",
    long="Work and energy share the same SI unit, the Joule (J), defined as 1 N·m. Newton is the unit of force, Pascal of pressure, and Watt of power.",
    trick="Don't confuse related but distinct units: Newton=force, Watt=power (energy per time), Pascal=pressure — only Joule measures energy/work itself.",
    options=dict(a="Correct — the Joule is the SI unit of work and energy.",
                 b="Newton is the unit of force, not energy.",
                 c="Pascal is the unit of pressure, not energy.",
                 d="Watt is the unit of power (energy per unit time), not energy itself.")
),
8439: dict(
    short="PE=mgh=3x10x6=180 J.",
    long="Gravitational potential energy is calculated as PE = mgh = 3 kg × 10 m/s^2 × 6 m = 180 J.",
    trick="Make sure to multiply all three quantities (mass, g, height) together — omitting or misplacing one factor gives one of the incorrect distractor values.",
    options=dict(a="18 J would result from omitting a factor of 10 (g).",
                 b="30 J doesn't include the height factor properly.",
                 c="Correct — 3x10x6=180 J.",
                 d="60 J would result from omitting a factor in the multiplication.")
),
8440: dict(
    short="KE = (1/2)mv^2 = 0.5x2x10^2 = 100 J.",
    long="Kinetic energy is KE = ½mv² = 0.5 × 2 kg × (10 m/s)² = 0.5 × 2 × 100 = 100 J.",
    trick="Remember velocity is SQUARED in the kinetic energy formula — forgetting to square v gives a much smaller (and wrong) answer.",
    options=dict(a="20 J would result from forgetting to square the velocity.",
                 b="10 J is far too small for these values.",
                 c="200 J would come from omitting the 1/2 factor.",
                 d="Correct — 0.5x2x10^2=100 J.")
),
8441: dict(
    short="Power = Work/time = 5000/25 = 200 W.",
    long="Power is the rate of doing work: P = W/t = 5000 J / 25 s = 200 W.",
    trick="Divide work by time (not multiply) to get power — multiplying gives an inflated, incorrect value.",
    options=dict(a="Correct — 5000/25=200 W.",
                 b="125000 W would come from multiplying 5000x25 instead of dividing.",
                 c="20 W is off by a factor of 10 from the correct division.",
                 d="2000 W is off by a factor of 10 from the correct value.")
),
8442: dict(
    short="In uniform circular motion, the velocity vector's direction constantly changes, always tangent to the circle.",
    long="Uniform circular motion has constant SPEED (magnitude), but the velocity vector's direction is always changing — it stays tangent to the circular path at every instant, which is why there's a centripetal acceleration even though speed doesn't change.",
    trick="Don't confuse the changing velocity DIRECTION (correct) with a changing velocity MAGNITUDE (which stays constant in uniform circular motion) — 'uniform' refers to constant speed only.",
    options=dict(a="Speed (magnitude) does NOT increase in uniform circular motion — it stays constant.",
                 b="Correct — the velocity direction constantly changes, staying tangent to the circle.",
                 c="The velocity vector points tangent to the circle, not toward the center (that's acceleration's direction).",
                 d="Velocity is not zero in circular motion — the object is continuously moving.")
),
8443: dict(
    short="Gravitational force F ∝ m1×m2; doubling one mass doubles the force (distance constant).",
    long="Newton's law of gravitation: F = Gm1m2/r². If one mass doubles while r stays constant, F is directly proportional to that mass, so F also doubles.",
    trick="Don't apply the inverse-square relationship (which is for DISTANCE) to mass — force is directly (linearly) proportional to each mass, not inversely or squared.",
    options=dict(a="Force would only halve if a mass were halved, not doubled.",
                 b="Four times would result from doubling BOTH masses, not just one.",
                 c="Correct — force is directly proportional to mass, so doubling one mass doubles the force.",
                 d="The force does change since it's directly proportional to the mass being doubled.")
),
8444: dict(
    short="The Moon's weaker gravity (due to smaller mass) means lower weight there than on Earth.",
    long="Weight depends on the gravitational field strength at the surface, which depends on the planet/moon's mass (and radius). The Moon has much less mass than Earth, producing about 1/6th the surface gravity, hence lower weight for the same object.",
    trick="Weight change is about the astronaut's MASS staying the same while the local gravitational pull changes — don't confuse mass (constant) with weight (which changes with location).",
    options=dict(a="A larger radius (with same mass) would actually decrease surface gravity further, but the Moon's radius is smaller than Earth's, not larger — mass is the key factor here.",
                 b="The Moon does NOT have the same mass as Earth; it's much less massive.",
                 c="The Moon does have gravity, just weaker than Earth's — it's not zero.",
                 d="Correct — the Moon's smaller mass produces weaker surface gravity, hence less weight.")
),
8445: dict(
    short="Fluid pressure at depth depends on density and depth (P=ρgh).",
    long="Hydrostatic pressure is given by P = ρgh, depending on the fluid's density (ρ), gravitational acceleration (g), and depth (h) below the surface.",
    trick="Container shape, fluid color, and temperature (directly) don't factor into the basic hydrostatic pressure formula — only density and depth (along with g) matter.",
    options=dict(a="Correct — pressure depends on density and depth (P=ρgh).",
                 b="Container shape does not affect fluid pressure at a given depth.",
                 c="Color has no physical effect on pressure.",
                 d="Temperature isn't part of the basic hydrostatic pressure formula (though it could indirectly affect density).")
),
8446: dict(
    short="Pascal's principle: pressure transmitted equally allows a larger piston to exert a proportionally larger force.",
    long="Pascal's principle states pressure applied to an enclosed fluid is transmitted equally in all directions. Since pressure = force/area, if the output piston has a larger area than the input piston, the same pressure produces a proportionally larger output force — allowing mechanical advantage without creating energy from nothing.",
    trick="It's not magic — no force is created 'from nothing'; energy is conserved because the larger piston moves a smaller distance, keeping work (force x distance) balanced.",
    options=dict(a="This would violate energy conservation — hydraulic lifts don't create force from nothing.",
                 b="Correct — equal pressure transmission plus a larger piston area yields proportionally larger force.",
                 c="The load does have weight; that's exactly what's being lifted.",
                 d="Friction is not the mechanism behind hydraulic force amplification — it's Pascal's principle.")
),
8447: dict(
    short="Buoyant force depends on the volume of fluid displaced, not the object's own density.",
    long="By Archimedes' principle, buoyant force equals the weight of fluid displaced, which depends on the object's VOLUME (and the fluid's density), not the object's own density. Two identical-sized objects of different density displace the same fluid volume, so they experience the same buoyant force (though the denser one may still sink if its weight exceeds that force).",
    trick="Don't assume 'denser = more buoyant force' — buoyant force is about displaced fluid volume, which is the same for two identical-sized objects regardless of their own density.",
    options=dict(a="Buoyant force does not depend directly on the object's own density, only on displaced volume.",
                 b="Both objects do experience some buoyant force since they're submerged in fluid.",
                 c="Correct — since the objects are identical in size (volume), they displace equal fluid and feel equal buoyant force.",
                 d="Buoyant force doesn't necessarily exceed weight — that would make the object float, which isn't a general truth here.")
),
8448: dict(
    short="Wavelength is the distance between two consecutive corresponding points, such as two crests.",
    long="Wavelength (λ) is defined as the distance between two consecutive crests (or troughs, or any two points in the same phase) of a wave.",
    trick="Don't confuse wavelength (a distance, spatial) with period (a time) or frequency (waves per second) — amplitude is the height of the wave, unrelated to crest spacing.",
    options=dict(a="Amplitude describes the height/intensity of the wave, not the spacing between crests.",
                 b="Period is a measure of TIME per cycle, not distance.",
                 c="Frequency is cycles per second, not a spatial distance.",
                 d="Correct — wavelength is the distance between consecutive crests.")
),
8449: dict(
    short="Amplitude of a sound wave corresponds to its loudness (volume).",
    long="A sound wave's amplitude (the size of the pressure variation) determines how loud it's perceived — larger amplitude means louder sound. Pitch is instead determined by frequency.",
    trick="Don't mix up amplitude (loudness) with frequency (pitch) — these are two independent properties of a sound wave.",
    options=dict(a="Correct — amplitude determines the perceived loudness (volume) of a sound.",
                 b="Pitch is determined by frequency, not amplitude.",
                 c="The speed of sound in a given medium is generally independent of amplitude.",
                 d="Wavelength is related to frequency and speed, not directly changed by increasing amplitude alone.")
),
8450: dict(
    short="Frequency = speed/wavelength = 340/0.5 = 680 Hz.",
    long="Using the wave equation v = fλ, rearranged to f = v/λ: f = 340 m/s / 0.5 m = 680 Hz.",
    trick="Make sure to divide speed by wavelength (not multiply) — v=fλ rearranges to f=v/λ, and dividing wavelength incorrectly by speed instead gives a very different, wrong number.",
    options=dict(a="0.68 Hz would come from a decimal-point/unit error.",
                 b="Correct — 340/0.5 = 680 Hz.",
                 c="340 Hz overlooks dividing by the 0.5 m wavelength.",
                 d="170 Hz would come from multiplying by 0.5 instead of dividing.")
),
8451: dict(
    short="Standing waves form when two identical waves travel in opposite directions and interfere, creating fixed nodes and antinodes.",
    long="A standing wave results from the superposition of two waves of the same frequency and amplitude traveling in OPPOSITE directions along the same medium (e.g. an incident wave and its reflection). Their interference creates stationary points of no displacement (nodes) and maximum displacement (antinodes).",
    trick="Waves traveling in the SAME direction just combine into a single traveling wave, not a standing wave — the opposite-direction condition is essential for the fixed node/antinode pattern.",
    options=dict(a="Different frequencies would generally produce beats or complex interference, not a clean standing wave pattern.",
                 b="Perpendicular waves don't produce the classic 1D standing-wave node/antinode pattern being described here.",
                 c="Correct — opposite-direction travel and interference produces the fixed nodes and antinodes of a standing wave.",
                 d="Waves in the same direction combine into a single traveling wave, not a standing wave pattern.")
),
8452: dict(
    short="Radiation transfers heat via electromagnetic waves, which can travel through a vacuum.",
    long="Radiation is heat transfer through electromagnetic waves (e.g. infrared), which do not require a medium — they can travel through empty space (a vacuum), unlike conduction or convection.",
    trick="Conduction requires direct particle contact, and convection requires fluid movement — only radiation among the three heat-transfer methods can cross a vacuum.",
    options=dict(a="Direct particle contact describes conduction, not radiation.",
                 b="Bulk fluid movement describes convection, not radiation.",
                 c="Conduction through solids is a separate heat-transfer mechanism from radiation.",
                 d="Correct — radiation transfers heat via electromagnetic waves, which can cross a vacuum.")
),
8453: dict(
    short="Isochoric (constant volume) process: no work is done since work requires a volume change.",
    long="Thermodynamic work done by a gas is W = PΔV. In an isochoric (constant-volume) process, ΔV = 0, so no work is done on or by the gas, regardless of any heat exchanged.",
    trick="Don't confuse 'no work' with 'no heat exchange' — an isochoric process can still absorb or release heat; it's specifically WORK that becomes zero because volume doesn't change.",
    options=dict(a="Correct — with ΔV=0, work (W=PΔV) is zero in an isochoric process.",
                 b="Maximum work would occur with maximum volume change, the opposite of constant volume.",
                 c="Work equaling heat absorbed would apply in an isothermal process for an ideal gas, not isochoric.",
                 d="Work isn't 'always negative' here — it's simply zero since there's no volume change.")
),
8454: dict(
    short="First law: ΔU = Q + W_on_gas = -500 J + 200 J = -300 J.",
    long="Using the first law of thermodynamics (ΔU = Q + W, where W is work done ON the gas): the gas releases 500 J of heat (Q = -500 J), and 200 J of work is done ON it by surroundings (W = +200 J). ΔU = -500 + 200 = -300 J.",
    trick="Be careful with sign conventions: heat RELEASED is negative Q, and work done ON the gas (not BY the gas) is positive W in this convention — mixing up either sign flips the answer.",
    options=dict(a="700 J would result from adding the magnitudes instead of using correct signs.",
                 b="Correct — Q=-500J (released) + W=+200J (done on gas) = -300 J.",
                 c="-700 J would result from treating both quantities as negative (heat released AND work as if done on the gas negatively).",
                 d="300 J (positive) has the wrong sign — the internal energy actually decreases overall.")
),
8455: dict(
    short="Extra electrons compared to protons gives an object a net negative charge.",
    long="Electric charge results from an imbalance between protons (positive) and electrons (negative). More electrons than protons means an excess of negative charge, giving the object a net negative charge overall.",
    trick="Remember: MORE electrons (negative particles) than protons means negative charge, not positive — it's easy to accidentally flip this.",
    options=dict(a="Positive charge would result from having FEWER electrons than protons, the opposite situation.",
                 b="A neutral charge requires equal protons and electrons, not an excess of either.",
                 c="Correct — excess electrons over protons gives a net negative charge.",
                 d="The charge doesn't 'constantly change' just from a static imbalance of electrons and protons.")
),
8456: dict(
    short="Electric field lines point radially outward from an isolated positive charge.",
    long="By convention, electric field lines point in the direction a small positive test charge would move. Around an isolated positive charge, this is directly away from the charge in all directions — radially outward.",
    trick="Field lines point TOWARD a negative charge and AWAY from a positive charge — don't mix up the direction convention for the two charge signs.",
    options=dict(a="Field lines point toward a NEGATIVE charge, not a positive one.",
                 b="Field lines do have a well-defined direction (radially outward for a positive charge), not a random one.",
                 c="Field lines don't circle around a point charge; that pattern is more characteristic of magnetic fields around a wire.",
                 d="Correct — field lines point radially outward from an isolated positive charge.")
),
8457: dict(
    short="Electrical resistance is measured in Ohms (Ω).",
    long="Resistance, a measure of how strongly a material opposes current flow, is measured in Ohms (Ω), by definition R=V/I.",
    trick="Don't mix up the related electrical units: Amperes measure current, Volts measure potential difference, and Watts measure power — only Ohms measure resistance.",
    options=dict(a="Correct — resistance is measured in Ohms.",
                 b="Amperes measure electric current, not resistance.",
                 c="Volts measure potential difference (voltage), not resistance.",
                 d="Watts measure power, not resistance.")
),
8458: dict(
    short="Three identical 6 Ω resistors in parallel: 1/R = 3x(1/6) = 1/2, so R = 2 Ω.",
    long="For resistors in parallel, 1/R_total = 1/R1 + 1/R2 + 1/R3. With three identical 6 Ω resistors: 1/R = 1/6+1/6+1/6 = 3/6 = 1/2, giving R_total = 2 Ω.",
    trick="Parallel resistance is always LESS than the smallest individual resistor (here, less than 6 Ω) — an answer of 18 Ω (series-style addition) or 6 Ω would be a clear sign the parallel formula wasn't applied.",
    options=dict(a="18 ohm would result from adding the resistors as if in series, not parallel.",
                 b="Correct — three 6 Ω resistors in parallel give 1/R=3/6, so R=2 ohm.",
                 c="6 ohm ignores the parallel combination entirely.",
                 d="3 ohm would result from an incorrect division (dividing by 2 instead of correctly summing reciprocals for three resistors).")
),
8459: dict(
    short="Series resistors simply add: 2+3+5 = 10 ohm.",
    long="For resistors connected in series, total resistance is just the sum of individual resistances: 2 + 3 + 5 = 10 Ω.",
    trick="Series addition is straightforward summation — don't apply the parallel reciprocal formula here, which is only for parallel circuits.",
    options=dict(a="5 ohm is far too small — that's not even close to the correct sum.",
                 b="30 ohm would come from multiplying instead of adding.",
                 c="Correct — 2+3+5=10 ohm for resistors in series.",
                 d="0.97 ohm looks like a (incorrect) parallel-style reciprocal calculation, not appropriate for series resistors.")
),
8460: dict(
    short="Current = Power/Voltage = 60/120 = 0.5 A.",
    long="Using P=IV rearranged to I=P/V: I = 60 W / 120 V = 0.5 A.",
    trick="Divide power by voltage (not multiply) to find current — multiplying gives a much larger, incorrect number (7200, which is actually P×V).",
    options=dict(a="5 A doesn't match the correct division (60/120=0.5).",
                 b="2 A doesn't match either.",
                 c="7200 A would come from multiplying 60x120 instead of dividing.",
                 d="Correct — 60/120=0.5 A.")
),
8461: dict(
    short="The direction of the magnetic force on a current-carrying wire is found using the right-hand (or left-hand) rule.",
    long="The force on a current in a magnetic field (F = IL×B) has a direction found using a hand rule — commonly the right-hand rule (or left-hand rule in some conventions) relating current direction, field direction, and force direction.",
    trick="Ohm's law, Coulomb's law, and energy conservation are important physics principles, but none of them describe the specific geometric direction-finding technique used for magnetic force — that's the hand-rule's job.",
    options=dict(a="Correct — the right-hand (or left-hand) rule determines the force direction on a current in a magnetic field.",
                 b="Ohm's law relates voltage, current, and resistance, not force direction.",
                 c="Coulomb's law describes force between static charges, not magnetic force on a current.",
                 d="Energy conservation is a general principle, not a direction-finding tool for magnetic force.")
),
8462: dict(
    short="A step-up transformer has MORE turns on the secondary coil than the primary.",
    long="Transformer voltage ratio follows Vs/Vp = Ns/Np (turns ratio). For a step-UP transformer (secondary voltage higher than primary), the secondary coil must have MORE turns than the primary.",
    trick="Step-UP means voltage increases, which requires MORE turns on the output (secondary) side — don't confuse this with a step-down transformer, which has fewer secondary turns.",
    options=dict(a="Fewer turns on the secondary would produce a step-DOWN transformer, not step-up.",
                 b="Correct — more secondary turns than primary turns produces a step-up in voltage.",
                 c="Equal turns would produce no voltage change (ratio of 1:1).",
                 d="Having no turns at all would mean no secondary coil/output exists.")
),
8463: dict(
    short="The electron is the negatively charged particle orbiting the nucleus.",
    long="Electrons are negatively charged subatomic particles found in orbitals/shells around the nucleus, which contains protons (positive) and neutrons (neutral).",
    trick="Positron is the electron's antimatter counterpart (positively charged) — don't confuse it with the ordinary electron.",
    options=dict(a="Protons are positively charged and reside in the nucleus, not orbiting it.",
                 b="Neutrons are neutral (uncharged) and reside in the nucleus.",
                 c="Correct — the electron is the negatively charged particle orbiting the nucleus.",
                 d="A positron is the positively charged antimatter counterpart of the electron, not the same particle.")
),
8464: dict(
    short="Gamma decay releases a high-energy photon with no change in atomic or mass number.",
    long="Gamma decay occurs when an excited (higher-energy) nucleus releases excess energy as a gamma-ray photon, without changing the number of protons or neutrons — so atomic number and mass number stay the same.",
    trick="Unlike alpha decay (helium nucleus emission) or beta decay (electron emission), gamma decay changes only the nucleus's energy state, not its composition — the atomic/mass numbers remain unchanged.",
    options=dict(a="A helium nucleus is emitted in ALPHA decay, not gamma decay.",
                 b="An electron is emitted in BETA decay, not gamma decay.",
                 c="A neutron isn't the characteristic emission of gamma decay.",
                 d="Correct — gamma decay emits a high-energy photon with no change in atomic or mass number.")
),
8465: dict(
    short="20 days = 4 half-lives (20/5). 800/(2^4) = 800/16 = 50 g.",
    long="Number of half-lives elapsed = 20 days / 5 days per half-life = 4 half-lives. Remaining amount = initial amount / 2^n = 800 / 2^4 = 800/16 = 50 g.",
    trick="Make sure to divide by 2 raised to the NUMBER of half-lives elapsed (2^4=16), not just multiply the half-life count by something linear — radioactive decay is exponential, not linear.",
    options=dict(a="Correct — after 4 half-lives, 800/16=50 g remains.",
                 b="100 g would correspond to only 3 half-lives (800/8), one short of the correct count.",
                 c="25 g would correspond to 5 half-lives (800/32), one too many.",
                 d="200 g would correspond to only 2 half-lives (800/4), well short of the actual 4 elapsed.")
),
8466: dict(
    short="Object at the focal point F of a convex lens: refracted rays emerge parallel, forming no real image (image at infinity).",
    long="When an object sits exactly at a convex lens's focal point, both standard construction rays emerge from the lens with the same slope, meaning they never converge or diverge relative to each other — they travel on as parallel rays, so no finite image is formed (the image is effectively 'at infinity').",
    trick="This is a classic special case distinct from object-at-2F (real image at 2F) or object-within-F (virtual, magnified image) — memorize that specifically object-AT-F gives parallel emergent rays and no real image.",
    options=dict(a="A real image at 2F occurs when the OBJECT is at 2F, not when it's at F.",
                 b="Correct — with the object at F, the refracted rays emerge parallel, forming no real image.",
                 c="A virtual image on the object's side occurs when the object is WITHIN F (between F and the lens), not exactly at F.",
                 d="A real, inverted, diminished image close to the lens would occur with the object very far away, not at F.")
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
    out_path = root / "scripts" / "mock20_explanations_physics.json"
    out_path.write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Wrote {len(out)} explanations to {out_path}")

if __name__ == "__main__":
    main()
