"""Generate the 5 diagram/graph images referenced by mock5_data.json's
image-based questions (Q8, Q14, Q110, Q154, Q162).
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Ellipse, FancyBboxPatch

OUT = Path(__file__).parent.parent / "mdcat-content" / "images"
OUT.mkdir(parents=True, exist_ok=True)


def save(fig, name):
    fig.savefig(OUT / name, dpi=150, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("wrote", OUT / name)


# ---------------------------------------------------------------
# Q8: Michaelis-Menten saturation curve, rate vs substrate concentration
# ---------------------------------------------------------------
def enzyme_substrate_saturation_graph():
    s = np.linspace(0, 20, 400)
    vmax, km = 100, 3.0
    rate = vmax * s / (km + s)
    fig, ax = plt.subplots(figsize=(7, 5.5))
    ax.plot(s, rate, color="#1b6e6e", linewidth=2.5)
    ax.axhline(vmax, color="gray", linestyle="--", linewidth=1.2)
    ax.text(15, vmax + 3, "Vmax", color="gray", fontsize=11)
    ax.set_title("Enzyme Reaction Rate vs Substrate Concentration", fontsize=14, fontweight="bold")
    ax.set_xlabel("Substrate Concentration [S]", fontsize=12)
    ax.set_ylabel("Initial Reaction Rate", fontsize=12)
    ax.set_xlim(0, 20)
    ax.set_ylim(0, 115)
    ax.grid(alpha=0.3)
    save(fig, "q5_enzyme_substrate_saturation_graph.png")


# ---------------------------------------------------------------
# Q14: plant cell, M=chloroplast, N=central vacuole, O=cell wall, P=nucleus
# ---------------------------------------------------------------
def plant_cell_diagram_mnop():
    fig, ax = plt.subplots(figsize=(7.5, 7))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")
    ax.set_title("Structure of a Plant Cell", fontsize=16, fontweight="bold")

    ax.add_patch(FancyBboxPatch((0.7, 0.9), 8.6, 8.2, boxstyle="round,pad=0,rounding_size=0.5",
                                 facecolor="#eef7e3", edgecolor="#5a7a2a", linewidth=4))
    ax.add_patch(FancyBboxPatch((1.0, 1.2), 8.0, 7.6, boxstyle="round,pad=0,rounding_size=0.4",
                                 facecolor="#eef7e3", edgecolor="#8fae5a", linewidth=1.5))

    ax.add_patch(Ellipse((5.3, 4.6), 5.0, 4.2, facecolor="#bfe3f0", edgecolor="#5aa9c4", linewidth=1.5))

    ax.add_patch(Ellipse((2.3, 7.3), 1.8, 1.6, facecolor="#c9a2d8", edgecolor="#7a4f96", linewidth=1.5))
    ax.add_patch(Ellipse((2.4, 7.25), 0.7, 0.7, facecolor="#7a4f96", edgecolor="#5a3570", linewidth=1))

    for cx, cy, ang in [(2.0, 3.0, 25), (7.7, 6.7, -15), (7.6, 2.6, 10)]:
        ell = Ellipse((cx, cy), 1.3, 0.7, angle=ang, facecolor="#4c8f3f", edgecolor="#2e5c26", linewidth=1.3)
        ax.add_patch(ell)

    def label(x, y, tx, ty, text):
        ax.annotate(
            text, xy=(x, y), xytext=(tx, ty), fontsize=13, fontweight="bold",
            ha="center", va="center",
            arrowprops=dict(arrowstyle="-", color="black", lw=1),
            bbox=dict(boxstyle="circle", facecolor="white", edgecolor="black", linewidth=1.5),
        )

    label(7.7, 6.7, 9.4, 8.0, "M")
    label(5.3, 4.6, 5.3, 2.0, "N")
    label(1.0, 5.0, -0.6, 5.0, "O")
    label(2.3, 7.3, 0.6, 9.0, "P")

    save(fig, "q5_plant_cell_diagram_mnop.png")


# ---------------------------------------------------------------
# Q110: weak acid (acetic acid) titrated with NaOH -- equivalence pH > 7
# ---------------------------------------------------------------
def titration_curve_weak_acid():
    v = np.linspace(0, 50, 400)
    # weak acid start higher than strong acid (~pH 2.9), gentler rise, buffer
    # region flatter, equivalence point above pH 7 (~8.7), plateau ~12.5
    ph = 2.9 + 9.6 / (1 + np.exp(-0.55 * (v - 25)))
    fig, ax = plt.subplots(figsize=(7, 5.5))
    ax.plot(v, ph, color="#a8332c", linewidth=2.5)
    ax.axvline(25, color="gray", linestyle="--", linewidth=1.2)
    ax.axhline(7, color="#999", linestyle=":", linewidth=1)
    ax.text(1, 7.2, "pH 7", color="#999", fontsize=10)
    eq_ph = 2.9 + 9.6 / (1 + np.exp(-0.55 * (25 - 25)))
    ax.plot(25, eq_ph, "o", color="#a8332c", markersize=6)
    ax.set_title("Titration Curve: Weak Acid (Acetic Acid) + NaOH", fontsize=14, fontweight="bold")
    ax.set_xlabel("Volume of NaOH added (mL)", fontsize=12)
    ax.set_ylabel("pH", fontsize=12)
    ax.set_xlim(0, 50)
    ax.set_ylim(0, 14)
    ax.grid(alpha=0.3)
    save(fig, "q5_titration_curve_weak_acid.png")


# ---------------------------------------------------------------
# Q154: R1(4) || R2(4) = 2, series with R3(3) -> 5 ohm
# ---------------------------------------------------------------
def circuit_diagram_r1r2r3():
    fig, ax = plt.subplots(figsize=(7, 4.2))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis("off")

    ax.add_patch(plt.Circle((1, 3), 0.6, facecolor="white", edgecolor="black", linewidth=2))
    ax.text(1, 3.28, "+", ha="center", va="center", fontsize=13)
    ax.text(1, 2.72, "-", ha="center", va="center", fontsize=13)
    ax.text(1, 1.9, "12 V", ha="center", va="center", fontsize=12)

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

    ax.plot([1, 1], [3.6, 5], color="black", linewidth=2)
    ax.plot([1, 3], [5, 5], color="black", linewidth=2)

    ax.plot([3, 3], [5, 4.0], color="black", linewidth=2)
    resistor(3, 4.0, 3, 1.7, "R1 = 4 Ω")
    ax.plot([3, 3], [1.7, 0.5], color="black", linewidth=2)

    ax.plot([4.6, 4.6], [5, 4.0], color="black", linewidth=2)
    resistor(4.6, 4.0, 4.6, 1.7, "R2 = 4 Ω")
    ax.plot([4.6, 4.6], [1.7, 0.5], color="black", linewidth=2)

    ax.plot([3, 4.6], [5, 5], color="black", linewidth=2)
    ax.plot([3, 4.6], [0.5, 0.5], color="black", linewidth=2)

    ax.plot([4.6, 6.2], [5, 5], color="black", linewidth=2)
    resistor(6.2, 5, 7.9, 5, "R3 = 3 Ω")
    ax.plot([7.9, 8.5], [5, 5], color="black", linewidth=2)
    ax.plot([8.5, 8.5], [5, 0.5], color="black", linewidth=2)

    ax.plot([1, 1], [2.4, 0.5], color="black", linewidth=2)
    ax.plot([1, 8.5], [0.5, 0.5], color="black", linewidth=2)

    save(fig, "q5_circuit_diagram_r1r2r3.png")


# ---------------------------------------------------------------
# Q162: convex lens, object exactly at F -> emergent rays parallel
# ---------------------------------------------------------------
def lens_diagram_object_at_f():
    f = 2.0
    obj_x, obj_h = -f, 1.4

    fig, ax = plt.subplots(figsize=(9, 5.5))
    ax.set_xlim(-6.5, 6.5)
    ax.set_ylim(-2.5, 3.5)
    ax.axis("off")
    ax.set_title("Ray Diagram: Convex Lens (Object at F)", fontsize=15, fontweight="bold")

    ax.axhline(0, color="black", linewidth=1.2)
    ax.plot([0, 0], [-3.2, 3.2], color="#2f6f9f", linewidth=3)

    for x, lbl in [(-2 * f, "2F"), (-f, "F"), (f, "F"), (2 * f, "2F")]:
        ax.plot(x, 0, "o", color="gray", markersize=4)
        ax.text(x, -0.35, lbl, ha="center", fontsize=12, color="gray")

    ax.annotate("", xy=(obj_x, obj_h), xytext=(obj_x, 0),
                arrowprops=dict(arrowstyle="-|>", color="#1a7a3a", linewidth=2.5))
    ax.text(obj_x, obj_h + 0.25, "Object (at F)", color="#1a7a3a", fontsize=13, ha="center")

    # Object sits exactly at F, so both standard rays emerge with the SAME
    # slope (-obj_h/f) after the lens -- that's the "parallel emergent rays,
    # image at infinity" fact this question is testing.
    slope_emergent = -obj_h / f

    # ray 1: parallel to axis into the lens, then refracts through the far
    # focal point (f, 0) and continues at slope_emergent beyond it
    ax.plot([obj_x, 0], [obj_h, obj_h], color="#333", linewidth=1.6)
    ax.plot([0, 6], [obj_h, obj_h + slope_emergent * 6], color="#333", linewidth=1.6)

    # ray 2: through optical center, undeviated -- same incoming slope,
    # which for an object at F equals slope_emergent too
    slope2 = obj_h / obj_x
    ax.plot([obj_x, 6], [obj_h, slope2 * 6], color="#333", linewidth=1.6)

    ax.text(4.5, obj_h + 0.25, "emergent rays\nparallel to each other", color="#333",
            fontsize=10, ha="center")

    save(fig, "q5_lens_diagram_object_at_f.png")


if __name__ == "__main__":
    enzyme_substrate_saturation_graph()
    plant_cell_diagram_mnop()
    titration_curve_weak_acid()
    circuit_diagram_r1r2r3()
    lens_diagram_object_at_f()
