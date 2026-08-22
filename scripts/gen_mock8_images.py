"""Generate the 5 diagram/graph images referenced by mdcat_mock_8.py's
image-based questions (Q12 mitochondrion P/Q/R, Q33 autosomal-dominant
pedigree, Q110 strong-acid/strong-base titration, Q154 R1 series with
R2||R3, Q162 convex lens object at F).
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Ellipse, Wedge

OUT = Path(__file__).parent.parent / "mdcat-content" / "images"
OUT.mkdir(parents=True, exist_ok=True)


def save(fig, name):
    fig.savefig(OUT / name, dpi=150, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("wrote", OUT / name)


# ---------------------------------------------------------------
# Q12: mitochondrion cross-section, P=outer membrane, Q=cristae
# (folded inner membrane), R=matrix
# ---------------------------------------------------------------
def mitochondrion_diagram():
    fig, ax = plt.subplots(figsize=(8, 5.5))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7)
    ax.axis("off")
    ax.set_title("Cross-Section of a Mitochondrion", fontsize=16, fontweight="bold")

    # outer membrane (P)
    ax.add_patch(Ellipse((5, 3.5), 8.0, 4.4, facecolor="#f2d9c4", edgecolor="#a8663a", linewidth=2.5))
    # matrix (R) -- inner fill
    ax.add_patch(Ellipse((5, 3.5), 7.0, 3.6, facecolor="#f7e6d2", edgecolor="none"))

    # cristae (Q) -- folded inner membrane ridges
    for cx in np.linspace(2.2, 7.8, 6):
        ax.add_patch(Ellipse((cx, 3.5), 0.9, 3.2, facecolor="none", edgecolor="#a8663a", linewidth=2.0))

    def label(x, y, tx, ty, text):
        ax.annotate(
            text, xy=(x, y), xytext=(tx, ty), fontsize=13, fontweight="bold",
            ha="center", va="center",
            arrowprops=dict(arrowstyle="-", color="black", lw=1),
            bbox=dict(boxstyle="circle", facecolor="white", edgecolor="black", linewidth=1.5),
        )

    label(1.05, 3.5, -0.5, 5.6, "P")
    label(3.1, 4.9, 3.1, 6.4, "Q")
    label(5.0, 3.5, 5.0, 1.0, "R")

    save(fig, "q_mitochondrion_diagram.png")


# ---------------------------------------------------------------
# Q33: autosomal-dominant pedigree, 3 generations. Affected individuals
# appear in every generation (vertical transmission), consistent with
# autosomal dominant inheritance (unlike the X-linked recessive pattern
# used in mock_6's pedigree).
# ---------------------------------------------------------------
def pedigree_autosomal_dominant():
    fig, ax = plt.subplots(figsize=(8, 6.5))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 9)
    ax.axis("off")
    ax.set_title("Autosomal Dominant Pedigree", fontsize=15, fontweight="bold")

    def square(x, y, filled=False, label=""):
        s = 0.5
        ax.add_patch(plt.Rectangle((x - s/2, y - s/2), s, s,
                                    facecolor="black" if filled else "white", edgecolor="black", linewidth=1.5))
        ax.text(x, y - 0.55, label, ha="center", fontsize=10)

    def circle(x, y, filled=False, label=""):
        r = 0.28
        ax.add_patch(plt.Circle((x, y), r, facecolor="black" if filled else "white", edgecolor="black", linewidth=1.5))
        ax.text(x, y - 0.55, label, ha="center", fontsize=10)

    def marry(x1, y, x2):
        ax.plot([x1, x2], [y, y], color="black", linewidth=1.3)

    # Generation I: affected male x unaffected female
    square(3, 7.5, filled=True, label="I-1 (affected)")
    circle(5, 7.5, filled=False, label="I-2 (unaffected)")
    marry(3, 7.5, 5)

    # Generation II: two children -- one affected, one not; affected child
    # marries an unaffected spouse
    square(2.5, 5, filled=True, label="II-1 (affected)")
    circle(4.2, 5, filled=False, label="II-2 (unaffected)")
    ax.plot([4, 4], [7.2, 5.3], color="black", linewidth=1.3)
    ax.plot([2.5, 4], [5.3, 5.3], color="black", linewidth=1.3)
    ax.plot([2.5, 2.5], [5.3, 5.28], color="black", linewidth=1.3)

    square(6.5, 5, filled=False, label="II-3 (spouse)")
    marry(2.5, 5, 6.5)

    # Generation III: children of II-1 x II-3, one affected (dominant trait
    # continues vertically), one unaffected
    circle(3, 2.5, filled=True, label="III-1 (affected)")
    square(4.7, 2.5, filled=False, label="III-2 (unaffected)")
    ax.plot([4.5, 4.5], [4.7, 3.2], color="black", linewidth=1.3)
    ax.plot([3, 4.7], [3.2, 3.2], color="black", linewidth=1.3)
    ax.plot([3, 3], [3.2, 2.8], color="black", linewidth=1.3)
    ax.plot([4.7, 4.7], [3.2, 2.8], color="black", linewidth=1.3)

    ax.text(0.3, 7.5, "I", fontsize=12, fontweight="bold")
    ax.text(0.3, 5.0, "II", fontsize=12, fontweight="bold")
    ax.text(0.3, 2.5, "III", fontsize=12, fontweight="bold")

    save(fig, "q_pedigree_autosomal_dominant.png")


# ---------------------------------------------------------------
# Q110: strong acid (HCl) + strong base (NaOH), steep near-vertical jump
# at the equivalence point (25 mL), pH = 7 there.
# ---------------------------------------------------------------
def strong_acid_strong_base_curve():
    v = np.linspace(0, 50, 400)
    ph = 1.2 + 12.6 / (1 + np.exp(-0.85 * (v - 25)))
    fig, ax = plt.subplots(figsize=(7, 5.5))
    ax.plot(v, ph, color="#2f6f9f", linewidth=2.8)
    ax.axvline(25, color="gray", linestyle="--", linewidth=1.2)
    ax.plot(25, 7, "o", color="#2f6f9f", markersize=7, zorder=5)
    ax.text(26, 6.3, "equivalence point\n(pH = 7)", fontsize=10, color="#2f6f9f")
    ax.set_title("Titration: Strong Acid (HCl) with Strong Base (NaOH)", fontsize=13, fontweight="bold")
    ax.set_xlabel("Volume of NaOH added (mL)", fontsize=12)
    ax.set_ylabel("pH", fontsize=12)
    ax.set_xlim(0, 50)
    ax.set_ylim(0, 14)
    ax.grid(alpha=0.25, linestyle=":")
    save(fig, "q_strong_acid_strong_base_curve.png")


# ---------------------------------------------------------------
# Q154: R1(6) in series with [R2(4) || R3(4) = 2] -> 8 ohm
# ---------------------------------------------------------------
def circuit_r1_series_r2r3_parallel():
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

    # R1 in series (top-left segment), then splits into R2 || R3
    ax.plot([1, 1], [3.6, 5], color="black", linewidth=2)
    ax.plot([1, 2.2], [5, 5], color="black", linewidth=2)
    resistor(2.2, 5, 4.0, 5, "R1 = 6 Ω")
    ax.plot([4.0, 5.0], [5, 5], color="black", linewidth=2)

    ax.plot([5.0, 5.0], [5, 4.0], color="black", linewidth=2)
    resistor(5.0, 4.0, 5.0, 1.7, "R2 = 4 Ω")
    ax.plot([5.0, 5.0], [1.7, 0.5], color="black", linewidth=2)

    ax.plot([6.6, 6.6], [5, 4.0], color="black", linewidth=2)
    resistor(6.6, 4.0, 6.6, 1.7, "R3 = 4 Ω")
    ax.plot([6.6, 6.6], [1.7, 0.5], color="black", linewidth=2)

    ax.plot([5.0, 6.6], [5, 5], color="black", linewidth=2)
    ax.plot([5.0, 6.6], [0.5, 0.5], color="black", linewidth=2)

    ax.plot([1, 1], [2.4, 0.5], color="black", linewidth=2)
    ax.plot([1, 5.0], [0.5, 0.5], color="black", linewidth=2)

    save(fig, "q_circuit_r1_series_r2r3_parallel.png")


# ---------------------------------------------------------------
# Q162: convex lens, object exactly at F -> emergent rays parallel,
# image at infinity. Distinct f/height from mock_5's version of this
# same scenario so the PNG isn't byte-identical.
# ---------------------------------------------------------------
def convex_lens_object_at_f():
    f = 2.6
    obj_x, obj_h = -f, 1.7

    fig, ax = plt.subplots(figsize=(9, 5.5))
    ax.set_xlim(-7.5, 7.5)
    ax.set_ylim(-2.8, 4.0)
    ax.axis("off")
    ax.set_title("Ray Diagram: Convex Lens (Object at F)", fontsize=15, fontweight="bold")

    ax.axhline(0, color="black", linewidth=1.2)
    ax.plot([0, 0], [-3.6, 3.6], color="#3a5f8f", linewidth=3)

    for x, lbl in [(-2 * f, "2F"), (-f, "F"), (f, "F"), (2 * f, "2F")]:
        ax.plot(x, 0, "o", color="gray", markersize=4)
        ax.text(x, -0.35, lbl, ha="center", fontsize=12, color="gray")

    ax.annotate("", xy=(obj_x, obj_h), xytext=(obj_x, 0),
                arrowprops=dict(arrowstyle="-|>", color="#1a7a3a", linewidth=2.5))
    ax.text(obj_x, obj_h + 0.25, "Object (at F)", color="#1a7a3a", fontsize=13, ha="center")

    slope_emergent = -obj_h / f

    ax.plot([obj_x, 0], [obj_h, obj_h], color="#333", linewidth=1.6)
    ax.plot([0, 6.8], [obj_h, obj_h + slope_emergent * 6.8], color="#333", linewidth=1.6)

    slope2 = obj_h / obj_x
    ax.plot([obj_x, 6.8], [obj_h, slope2 * 6.8], color="#333", linewidth=1.6)

    ax.text(4.8, obj_h + 0.3, "emergent rays\nparallel to each other", color="#333",
            fontsize=10, ha="center")

    save(fig, "q_convex_lens_object_at_f.png")


if __name__ == "__main__":
    mitochondrion_diagram()
    pedigree_autosomal_dominant()
    strong_acid_strong_base_curve()
    circuit_r1_series_r2r3_parallel()
    convex_lens_object_at_f()
