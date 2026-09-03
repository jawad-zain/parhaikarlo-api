"""Generate the 5 diagram/graph images referenced by mdcat_mock12.py's
image-based questions:
  Q12  Biology  - labeled nucleus diagram (1=nuclear envelope, 2=nucleolus,
                  3=nuclear pore, 4=chromatin); asks which produces
                  ribosomal subunits -> nucleolus (structure 2).
  Q68  Biology  - heart cross-section with 4 valves labeled W, X, Y, Z;
                  W/X = atrioventricular (tricuspid/mitral) valves, open
                  during ventricular diastole; Y/Z = semilunar
                  (pulmonary/aortic) valves, closed during diastole.
  Q93  Chemistry- heating curve (temperature vs heat added) for a pure
                  solid, with two flat plateaus = melting and boiling.
  Q154 Physics  - R1(10)+R2(10) in parallel -> 5 ohm, in series with
                  R3(2 ohm) -> 7 ohm total.
  Q162 Physics  - concave mirror, object WITHIN F -> virtual, upright,
                  magnified image formed behind the mirror.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Ellipse, Circle, FancyBboxPatch

OUT = Path(__file__).parent.parent / "mdcat-content" / "images"
OUT.mkdir(parents=True, exist_ok=True)


def save(fig, name):
    fig.savefig(OUT / name, dpi=150, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("wrote", OUT / name)


# ---------------------------------------------------------------
# Q12: Labeled cell nucleus.
#   1 = nuclear envelope (double membrane boundary)
#   2 = nucleolus (dense body inside -- makes ribosomal subunits)
#   3 = nuclear pore (opening in the envelope)
#   4 = chromatin (diffuse DNA-protein material filling the nucleus)
# ---------------------------------------------------------------
def nucleus_diagram():
    fig, ax = plt.subplots(figsize=(7.5, 7))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")
    ax.set_title("Cell Nucleus", fontsize=15, fontweight="bold")

    center = (5, 5)
    outer_r = 3.4

    # nuclear envelope: double membrane (draw as two concentric ellipses)
    ax.add_patch(Ellipse(center, outer_r * 2, outer_r * 2 * 0.95, facecolor="#eef3fb",
                          edgecolor="black", linewidth=2.2, zorder=1))
    ax.add_patch(Ellipse(center, outer_r * 2 - 0.22, (outer_r * 2 - 0.22) * 0.95, facecolor="none",
                          edgecolor="black", linewidth=1.0, zorder=2))

    # nuclear pores: small gaps/circles along the envelope
    pore_angles_deg = [20, 95, 160, 250, 320]
    for ang in pore_angles_deg:
        rad = np.deg2rad(ang)
        px = center[0] + outer_r * np.cos(rad)
        py = center[1] + outer_r * 0.95 * np.sin(rad)
        ax.add_patch(Circle((px, py), 0.16, facecolor="white", edgecolor="#2f6f9f", linewidth=1.8, zorder=3))

    # chromatin: diffuse squiggly threads filling the nucleoplasm
    rng = np.random.default_rng(7)
    for _ in range(14):
        cx0 = rng.uniform(center[0] - 2.1, center[0] + 2.1)
        cy0 = rng.uniform(center[1] - 1.9, center[1] + 1.9)
        if (cx0 - center[0]) ** 2 / 2.3 ** 2 + (cy0 - center[1]) ** 2 / 2.1 ** 2 > 0.9:
            continue
        t = np.linspace(0, 2 * np.pi, 30)
        xs = cx0 + 0.35 * np.cos(t + rng.uniform(0, 3))
        ys = cy0 + 0.18 * np.sin(2 * t + rng.uniform(0, 3))
        ax.plot(xs, ys, color="#7a4fa0", linewidth=1.1, alpha=0.75, zorder=2)

    # nucleolus: dense, roughly circular body off-center
    nuc_center = (5.9, 4.3)
    ax.add_patch(Circle(nuc_center, 0.85, facecolor="#8b1a4a", edgecolor="#5a0f30", linewidth=1.5, zorder=4))

    def label(num, tx, ty, target):
        ax.annotate(str(num), xy=target, xytext=(tx, ty), fontsize=13, fontweight="bold",
                    ha="center", va="center",
                    arrowprops=dict(arrowstyle="-", color="black", lw=1),
                    bbox=dict(boxstyle="circle", facecolor="white", edgecolor="black", linewidth=1.5), zorder=5)

    label(1, 8.9, 8.2, (center[0] + outer_r * np.cos(np.deg2rad(45)),
                         center[1] + outer_r * 0.95 * np.sin(np.deg2rad(45))))  # nuclear envelope
    label(2, 8.9, 4.3, nuc_center)                                             # nucleolus
    label(3, 1.1, 6.9, (center[0] + outer_r * np.cos(np.deg2rad(160)),
                         center[1] + outer_r * 0.95 * np.sin(np.deg2rad(160))))  # nuclear pore
    label(4, 1.1, 3.0, (3.4, 3.6))                                             # chromatin

    save(fig, "q_nucleus_diagram.png")


# ---------------------------------------------------------------
# Q68: Heart cross-section with 4 valves labeled W, X, Y, Z.
#   W = tricuspid valve (right AV valve)
#   X = mitral/bicuspid valve (left AV valve)
#   Y = pulmonary valve (semilunar, right side)
#   Z = aortic valve (semilunar, left side)
# AV valves (W, X) sit between atria and ventricles -> open during
# ventricular diastole. Semilunar valves (Y, Z) sit at the exits of the
# ventricles -> closed during ventricular diastole.
# ---------------------------------------------------------------
def heart_valves_diagram():
    fig, ax = plt.subplots(figsize=(7.5, 8))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 11)
    ax.axis("off")
    ax.set_title("Heart Cross-Section: Valves", fontsize=15, fontweight="bold")

    # heart outline
    ax.add_patch(Ellipse((5, 5.2), 7.6, 8.6, facecolor="#fbe9e7", edgecolor="black", linewidth=2))

    # septum dividing left/right sides
    ax.plot([5, 5], [1.4, 9.0], color="black", linewidth=1.6)

    # chamber labels
    ax.text(2.7, 7.6, "Right\nAtrium", ha="center", fontsize=10, color="#333")
    ax.text(7.3, 7.6, "Left\nAtrium", ha="center", fontsize=10, color="#333")
    ax.text(2.7, 3.0, "Right\nVentricle", ha="center", fontsize=10, color="#333")
    ax.text(7.3, 3.0, "Left\nVentricle", ha="center", fontsize=10, color="#333")

    # horizontal divider between atria and ventricles (AV valve level)
    ax.plot([1.5, 4.7], [5.6, 5.6], color="black", linewidth=1.2, linestyle=":")
    ax.plot([5.3, 8.5], [5.6, 5.6], color="black", linewidth=1.2, linestyle=":")

    def valve(cx, cy, letter, color):
        ax.add_patch(FancyBboxPatch((cx - 0.55, cy - 0.22), 1.1, 0.44,
                                     boxstyle="round,pad=0.02", facecolor=color,
                                     edgecolor="black", linewidth=1.6, zorder=4))
        ax.text(cx, cy, letter, ha="center", va="center", fontsize=13, fontweight="bold", zorder=5)

    # W: tricuspid (right AV valve) -- between right atrium and right ventricle
    valve(2.7, 5.6, "W", "#a8d5a2")
    # X: mitral/bicuspid (left AV valve) -- between left atrium and left ventricle
    valve(7.3, 5.6, "X", "#a8d5a2")
    # Y: pulmonary valve (semilunar) -- right ventricle outlet, upper area
    valve(2.9, 9.0, "Y", "#f4c07a")
    ax.plot([2.9, 2.9], [8.78, 8.2], color="black", linewidth=1.2)
    # Z: aortic valve (semilunar) -- left ventricle outlet, upper area
    valve(6.9, 9.2, "Z", "#f4c07a")
    ax.plot([6.9, 6.9], [8.98, 8.4], color="black", linewidth=1.2)

    ax.text(5, 0.5, "W, X = atrioventricular valves    Y, Z = semilunar valves",
            ha="center", fontsize=9.5, style="italic", color="#333")

    save(fig, "q_heart_valves_diagram.png")


# ---------------------------------------------------------------
# Q93: Heating curve for a pure solid heated at a constant rate.
# Two flat plateaus: melting (solid<->liquid) and boiling (liquid<->gas).
# ---------------------------------------------------------------
def heating_curve_graph():
    fig, ax = plt.subplots(figsize=(8, 6))

    # segments: (heat_start, heat_end, temp_start, temp_end)
    segs = [
        (0, 2, -20, 0),      # solid warming up to melting point
        (2, 4, 0, 0),         # melting plateau
        (4, 7, 0, 100),       # liquid warming up to boiling point
        (7, 10, 100, 100),    # boiling plateau
        (10, 12, 100, 130),   # gas warming further
    ]
    for x0, x1, y0, y1 in segs:
        xs = np.linspace(x0, x1, 20)
        ys = np.linspace(y0, y1, 20)
        ax.plot(xs, ys, color="#a8332c", linewidth=2.6)

    ax.axhline(0, color="gray", linewidth=0.7, linestyle=":")
    ax.axhline(100, color="gray", linewidth=0.7, linestyle=":")

    ax.annotate("Melting\n(solid -> liquid)", xy=(3, 0), xytext=(3, -35),
                ha="center", fontsize=10, color="#1b6e6e",
                arrowprops=dict(arrowstyle="-", color="#1b6e6e"))
    ax.annotate("Boiling\n(liquid -> gas)", xy=(8.5, 100), xytext=(8.5, 60),
                ha="center", fontsize=10, color="#1b6e6e",
                arrowprops=dict(arrowstyle="-", color="#1b6e6e"))

    ax.set_xlim(0, 12.5)
    ax.set_ylim(-45, 140)
    ax.set_xlabel("Heat added (arbitrary units)", fontsize=12)
    ax.set_ylabel("Temperature (°C)", fontsize=12)
    ax.set_title("Heating Curve of a Pure Solid Substance", fontsize=14, fontweight="bold")
    save(fig, "q_heating_curve_graph.png")


# ---------------------------------------------------------------
# Q154: R1 = 10 ohm and R2 = 10 ohm in PARALLEL (-> 5 ohm), that
# combination in SERIES with R3 = 2 ohm -> total = 7 ohm.
# ---------------------------------------------------------------
def circuit_r1r2_parallel_r3_series():
    fig, ax = plt.subplots(figsize=(7, 4.2))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis("off")

    ax.add_patch(plt.Circle((1, 3), 0.6, facecolor="white", edgecolor="black", linewidth=2))
    ax.text(1, 3.28, "+", ha="center", va="center", fontsize=13)
    ax.text(1, 2.72, "-", ha="center", va="center", fontsize=13)
    ax.text(1, 1.9, "Battery", ha="center", va="center", fontsize=11)

    def resistor(x0, y0, x1, y1, label):
        n = 7
        xs = np.linspace(x0, x1, n)
        ys = np.linspace(y0, y1, n)
        zig = np.array([0, 1, -1, 1, -1, 1, 0]) * 0.18
        if abs(x1 - x0) > abs(y1 - y0):
            ys = ys + zig
        else:
            xs = xs + zig
        ax.plot(xs, ys, color="black", linewidth=2)
        midx, midy = (x0 + x1) / 2, (y0 + y1) / 2
        if abs(x1 - x0) > abs(y1 - y0):
            ax.text(midx, midy + 0.55, label, ha="center", fontsize=11)
        else:
            ax.text(midx + 0.95, midy, label, ha="center", fontsize=11)

    # lead from battery up into the parallel section
    ax.plot([1, 1], [3.6, 5], color="black", linewidth=2)
    ax.plot([1, 3], [5, 5], color="black", linewidth=2)

    # R1 (10 ohm) -- left branch of the parallel pair
    ax.plot([3, 3], [5, 4.0], color="black", linewidth=2)
    resistor(3, 4.0, 3, 1.7, "R1 = 10 Ω")
    ax.plot([3, 3], [1.7, 0.5], color="black", linewidth=2)

    # R2 (10 ohm) -- right branch of the parallel pair
    ax.plot([4.6, 4.6], [5, 4.0], color="black", linewidth=2)
    resistor(4.6, 4.0, 4.6, 1.7, "R2 = 10 Ω")
    ax.plot([4.6, 4.6], [1.7, 0.5], color="black", linewidth=2)

    # top and bottom rails joining the two parallel branches
    ax.plot([3, 4.6], [5, 5], color="black", linewidth=2)
    ax.plot([3, 4.6], [0.5, 0.5], color="black", linewidth=2)

    # R3 (2 ohm) in series after the parallel combination
    ax.plot([4.6, 6.2], [5, 5], color="black", linewidth=2)
    resistor(6.2, 5, 7.9, 5, "R3 = 2 Ω")
    ax.plot([7.9, 8.5], [5, 5], color="black", linewidth=2)
    ax.plot([8.5, 8.5], [5, 0.5], color="black", linewidth=2)

    # return to battery
    ax.plot([1, 1], [2.4, 0.5], color="black", linewidth=2)
    ax.plot([1, 8.5], [0.5, 0.5], color="black", linewidth=2)

    ax.text(5, 0.05, "R1 ∥ R2 = 5 Ω, then + R3 (series) = 7 Ω total", ha="center", fontsize=9, style="italic")

    save(fig, "q_circuit_r1r2_parallel_r3_series.png")


# ---------------------------------------------------------------
# Q162: Concave mirror, object WITHIN F (between pole and focal point)
# -> virtual, upright, magnified image formed BEHIND the mirror.
#
# Mirror formula (real-is-positive convention, u positive = object
# distance in front of mirror): 1/v + 1/u = 1/f
#   f = 1.6, object placed at u = 0.7f (within F)
#   1/v = 1/f - 1/u  =>  v is negative => virtual image, behind mirror
#   magnification m = -v/u  (positive => upright, same orientation)
# ---------------------------------------------------------------
def concave_mirror_object_within_f():
    f = 1.6
    R = 2 * f
    u = 0.7 * f            # object distance (within F: u < f)
    obj_h = 1.1

    v = 1.0 / (1.0 / f - 1.0 / u)   # signed image distance (negative = virtual)
    m = -v / u                       # signed magnification
    img_h = m * obj_h

    assert v < 0, "expected a virtual image for object within F"
    assert m > 1, "expected a magnified, upright image for object within F"

    obj_x = -u          # object in front of mirror (negative side)
    img_x = -v          # virtual image location: -v is positive (behind mirror)

    fig, ax = plt.subplots(figsize=(9, 6))
    ax.set_xlim(obj_x - 1.2, img_x + 1.5)
    ax.set_ylim(-1.5, img_h + 1.5)
    ax.axis("off")
    ax.set_title("Ray Diagram: Concave Mirror (Object within F)", fontsize=15, fontweight="bold")

    ax.axhline(0, color="black", linewidth=1.2)
    # Concave mirror bulges TOWARD the object (negative-coefficient
    # parabola x(y) = -k*y**2).
    yy = np.linspace(-2.6, 2.6, 100)
    xx = -0.09 * yy**2
    ax.plot(xx, yy, color="#2f6f9f", linewidth=3)

    for x, lbl in [(-R, "C"), (-f, "F"), (0, "P")]:
        ax.plot(x, 0, "o", color="gray", markersize=4)
        ax.text(x, 0.15, lbl, ha="center", va="bottom", fontsize=12, color="gray")

    # object (green), close to the mirror, within F
    ax.annotate("", xy=(obj_x, obj_h), xytext=(obj_x, 0),
                arrowprops=dict(arrowstyle="-|>", color="#1a7a3a", linewidth=2.5))
    ax.text(obj_x, obj_h + 0.25, "Object", color="#1a7a3a", fontsize=13, ha="center")

    # virtual image (red, dashed, upright, magnified, BEHIND the mirror)
    ax.annotate("", xy=(img_x, img_h), xytext=(img_x, 0),
                arrowprops=dict(arrowstyle="-|>", color="#a8332c", linewidth=2.5, linestyle="dashed"))
    ax.text(img_x, img_h + 0.25, "Virtual Image", color="#a8332c", fontsize=13, ha="center")

    # ray 1: parallel to axis from object tip -> reflects through F.
    # Its backward extension (dashed) behind the mirror meets the other
    # backward-extended ray at the virtual image tip.
    ax.plot([obj_x, 0], [obj_h, obj_h], color="#333", linewidth=1.6)
    slope1 = (obj_h - 0) / (0 - (-f))
    ax.plot([0, img_x], [obj_h, obj_h - slope1 * (img_x - 0)], color="#333", linewidth=1.2, linestyle="--")

    # ray 2: from object tip through the mirror pole P, reflecting at the
    # same angle below the axis; extended backward it also passes through
    # the virtual image tip.
    ax.plot([obj_x, 0], [obj_h, 0], color="#555", linewidth=1.6)
    slope2 = obj_h / (0 - obj_x)
    reflect_y_at_imgx = -slope2 * (img_x - 0)
    ax.plot([0, img_x], [0, reflect_y_at_imgx], color="#555", linewidth=1.2, linestyle="--")
    # both dashed backward-extensions should meet at (img_x, img_h)
    ax.plot(img_x, img_h, "o", color="#a8332c", markersize=5, zorder=5)

    ax.text((obj_x + img_x) / 2, img_h + 0.9,
            f"u = {u:.2f}, f = {f}: virtual, upright, magnified (m = {m:.2f})",
            ha="center", fontsize=9.5, style="italic", color="#333")

    save(fig, "q_concave_mirror_object_within_f.png")


if __name__ == "__main__":
    nucleus_diagram()
    heart_valves_diagram()
    heating_curve_graph()
    circuit_r1r2_parallel_r3_series()
    concave_mirror_object_within_f()
