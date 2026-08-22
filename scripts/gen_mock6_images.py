"""Generate the 5 diagram/graph images referenced by mdcat_mock_6.py's
image-based questions (Q9 enzyme Km curve, Q33 X-linked pedigree,
Q111 weak-acid/strong-base titration, Q154 R1||R2 series R3 circuit,
Q162 concave mirror object beyond C).
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
# Q9: v vs [S] Michaelis-Menten curve, Vmax dashed, Km at half-Vmax
# ---------------------------------------------------------------
def enzyme_km_curve():
    Vmax, Km = 100.0, 4.0
    S = np.linspace(0, 30, 400)
    v = Vmax * S / (Km + S)
    fig, ax = plt.subplots(figsize=(7, 5.5))
    ax.plot(S, v, color="#1b6e6e", linewidth=2.5)
    ax.axhline(Vmax, color="gray", linestyle="--", linewidth=1.2)
    ax.axhline(Vmax / 2, color="#a8332c", linestyle=":", linewidth=1.2)
    ax.axvline(Km, color="#a8332c", linestyle=":", linewidth=1.2)
    ax.plot(Km, Vmax / 2, "o", color="#a8332c", markersize=7, zorder=5)
    ax.text(Km + 0.4, Vmax / 2 - 6, "Km", color="#a8332c", fontsize=12, fontweight="bold")
    ax.text(0.5, Vmax + 3, "Vmax", color="gray", fontsize=12)
    ax.set_title("Reaction Velocity vs Substrate Concentration", fontsize=14, fontweight="bold")
    ax.set_xlabel("[S] (substrate concentration)", fontsize=12)
    ax.set_ylabel("v (reaction velocity)", fontsize=12)
    ax.set_xlim(0, 30)
    ax.set_ylim(0, 115)
    ax.grid(alpha=0.25, linestyle=":")
    save(fig, "q_enzyme_km_curve.png")


# ---------------------------------------------------------------
# Q33: X-linked recessive pedigree, 3 generations.
# Gen I: affected father (filled square) x unaffected mother (open circle)
# Gen II: unaffected daughter (obligate carrier, half-filled) marries
#         unaffected non-carrier male (open square); their children in Gen III
#         include an unaffected son (open) and an affected son (filled).
# ---------------------------------------------------------------
def pedigree_xlinked():
    fig, ax = plt.subplots(figsize=(8, 6.5))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 9)
    ax.axis("off")
    ax.set_title("X-Linked Recessive Pedigree", fontsize=15, fontweight="bold")

    def square(x, y, filled=False, half=False, label=""):
        s = 0.5
        if half:
            ax.add_patch(plt.Rectangle((x - s/2, y - s/2), s/2, s, facecolor="black", edgecolor="black"))
            ax.add_patch(plt.Rectangle((x, y - s/2), s/2, s, facecolor="white", edgecolor="black"))
            ax.add_patch(plt.Rectangle((x - s/2, y - s/2), s, s, facecolor="none", edgecolor="black", linewidth=1.5))
        else:
            ax.add_patch(plt.Rectangle((x - s/2, y - s/2), s, s,
                                        facecolor="black" if filled else "white", edgecolor="black", linewidth=1.5))
        ax.text(x, y - 0.55, label, ha="center", fontsize=10)

    def circle(x, y, filled=False, half=False, label=""):
        r = 0.28
        if half:
            ax.add_patch(plt.Circle((x, y), r, facecolor="white", edgecolor="black", linewidth=1.5))
            ax.add_patch(Wedge((x, y), r, 90, 270, facecolor="black", edgecolor="black"))
        else:
            ax.add_patch(plt.Circle((x, y), r, facecolor="black" if filled else "white", edgecolor="black", linewidth=1.5))
        ax.text(x, y - 0.55, label, ha="center", fontsize=10)

    def marry(x1, y, x2):
        ax.plot([x1, x2], [y, y], color="black", linewidth=1.3)

    def descend(xmid, y_top, y_bot, x_child):
        ax.plot([xmid, xmid], [y_top, (y_top + y_bot) / 2], color="black", linewidth=1.3)
        ax.plot([xmid, x_child], [(y_top + y_bot) / 2, (y_top + y_bot) / 2], color="black", linewidth=1.3)
        ax.plot([x_child, x_child], [(y_top + y_bot) / 2, y_bot], color="black", linewidth=1.3)

    # Generation I
    square(3, 7.5, filled=True, label="I-1 (affected)")
    circle(5, 7.5, filled=False, label="I-2 (unaffected)")
    marry(3, 7.5, 5)

    # Generation II
    circle(4, 5, half=True, label="II-1 (carrier)")
    square(6, 5, filled=False, label="II-2 (unaffected)")
    marry(4, 5, 6)
    descend(4, 7.2, 5.3, 4)

    # Generation III
    square(3.3, 2.5, filled=False, label="III-1 (unaffected)")
    square(5, 2.5, filled=True, label="III-2 (affected)")
    ax.plot([5, 5], [4.7, 3.2], color="black", linewidth=1.3)
    ax.plot([3.3, 5], [3.2, 3.2], color="black", linewidth=1.3)
    ax.plot([3.3, 3.3], [3.2, 2.8], color="black", linewidth=1.3)
    ax.plot([5, 5], [3.2, 2.8], color="black", linewidth=1.3)

    ax.plot([0.6, 0.6], [7.5, 7.5], color="white")  # spacer
    ax.text(0.3, 7.5, "I", fontsize=12, fontweight="bold")
    ax.text(0.3, 5.0, "II", fontsize=12, fontweight="bold")
    ax.text(0.3, 2.5, "III", fontsize=12, fontweight="bold")

    save(fig, "q_pedigree_xlinked.png")


# ---------------------------------------------------------------
# Q111: weak acid (CH3COOH) titrated with strong base (NaOH) --
# equivalence point above pH 7 (basic), gentler initial slope + buffer
# plateau distinguishes it from a strong-acid/strong-base curve.
# ---------------------------------------------------------------
def titration_weak_acid_strong_base():
    v = np.linspace(0, 50, 400)
    # gentle rise (buffering) then steep jump near equivalence (25 mL), leveling
    ph = 4.0 + 1.3 * np.log10(np.clip(v, 0.5, None) / np.clip(25 - v, 0.01, None) + 1e-9)
    ph = np.nan_to_num(ph, nan=8.7, posinf=12.5, neginf=1.0)
    ph = np.clip(ph, 2.5, 12.8)
    # smooth override near/after equivalence with a logistic for the steep jump
    jump = 8.7 + 4.0 / (1 + np.exp(-0.9 * (v - 25)))
    ph = np.where(v > 20, jump, ph)
    ph = np.clip(ph, 2.8, 12.8)

    fig, ax = plt.subplots(figsize=(7, 5.5))
    ax.plot(v, ph, color="#a8332c", linewidth=2.5)
    ax.axvline(25, color="gray", linestyle="--", linewidth=1.2)
    ax.plot(25, 8.7, "o", color="#a8332c", markersize=7, zorder=5)
    ax.axhline(7, color="#888", linestyle=":", linewidth=1)
    ax.text(26, 9.3, "equivalence point\n(pH > 7, basic)", fontsize=10, color="#a8332c")
    ax.set_title("Titration: Weak Acid (CH3COOH) with Strong Base (NaOH)", fontsize=13, fontweight="bold")
    ax.set_xlabel("Volume of NaOH added (mL)", fontsize=12)
    ax.set_ylabel("pH", fontsize=12)
    ax.set_xlim(0, 50)
    ax.set_ylim(0, 14)
    ax.grid(alpha=0.25, linestyle=":")
    save(fig, "q_titration_weak_acid_strong_base.png")


# ---------------------------------------------------------------
# Q154: R1(5) || R2(5) = 2.5, in series with R3(3) -> 5.5 ohm
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

    ax.plot([1, 1], [3.6, 5], color="black", linewidth=2)
    ax.plot([1, 3], [5, 5], color="black", linewidth=2)

    ax.plot([3, 3], [5, 4.0], color="black", linewidth=2)
    resistor(3, 4.0, 3, 1.7, "R1 = 5 Ω")
    ax.plot([3, 3], [1.7, 0.5], color="black", linewidth=2)

    ax.plot([4.6, 4.6], [5, 4.0], color="black", linewidth=2)
    resistor(4.6, 4.0, 4.6, 1.7, "R2 = 5 Ω")
    ax.plot([4.6, 4.6], [1.7, 0.5], color="black", linewidth=2)

    ax.plot([3, 4.6], [5, 5], color="black", linewidth=2)
    ax.plot([3, 4.6], [0.5, 0.5], color="black", linewidth=2)

    ax.plot([4.6, 6.2], [5, 5], color="black", linewidth=2)
    resistor(6.2, 5, 7.9, 5, "R3 = 3 Ω")
    ax.plot([7.9, 8.5], [5, 5], color="black", linewidth=2)
    ax.plot([8.5, 8.5], [5, 0.5], color="black", linewidth=2)

    ax.plot([1, 1], [2.4, 0.5], color="black", linewidth=2)
    ax.plot([1, 8.5], [0.5, 0.5], color="black", linewidth=2)

    save(fig, "q_circuit_r1_r2_parallel_r3_series.png")


# ---------------------------------------------------------------
# Q162: concave mirror, object beyond C -> real, inverted, diminished,
# formed between F and C.
# ---------------------------------------------------------------
def concave_mirror_beyond_c():
    f = 2.0
    R = 2 * f
    obj_x, obj_h = -3.5 * f, 1.6   # beyond C (measuring distance from mirror pole, mirror at x=0, C at -R)

    # mirror formula 1/v + 1/u = 1/f, using magnitudes (positive distances
    # in front of the mirror)
    u_mag = abs(obj_x)
    v_mag = 1.0 / (1.0 / f - 1.0 / u_mag)
    img_x = -v_mag
    img_h = -obj_h * (v_mag / u_mag)  # inverted, diminished since v_mag < u_mag

    fig, ax = plt.subplots(figsize=(9, 5.5))
    ax.set_xlim(obj_x - 1, 2.5)
    ax.set_ylim(min(img_h, 0) - 1.5, obj_h + 1.5)
    ax.axis("off")
    ax.set_title("Ray Diagram: Concave Mirror (Object beyond C)", fontsize=15, fontweight="bold")

    ax.axhline(0, color="black", linewidth=1.2)
    # mirror as a curved arc at x=0. Concave mirror: center of curvature C
    # is on the SAME side as the object, so the mirror surface bulges
    # toward the object at the edges (x more negative as |y| grows) --
    # x(y) = -R + sqrt(R^2 - y^2), i.e. a NEGATIVE-coefficient parabola,
    # not positive (a positive coefficient draws a convex mirror instead).
    yy = np.linspace(-2.5, 2.5, 100)
    xx = -0.08 * yy**2
    ax.plot(xx, yy, color="#2f6f9f", linewidth=3)

    for x, lbl in [(-R, "C"), (-f, "F"), (0, "P")]:
        ax.plot(x, 0, "o", color="gray", markersize=4)
        ax.text(x, 0.15, lbl, ha="center", va="bottom", fontsize=12, color="gray")

    # object (green)
    ax.annotate("", xy=(obj_x, obj_h), xytext=(obj_x, 0),
                arrowprops=dict(arrowstyle="-|>", color="#1a7a3a", linewidth=2.5))
    ax.text(obj_x, obj_h + 0.25, "Object", color="#1a7a3a", fontsize=13, ha="center")

    # image (red, inverted, diminished, between F and C)
    ax.annotate("", xy=(img_x, img_h), xytext=(img_x, 0),
                arrowprops=dict(arrowstyle="-|>", color="#a8332c", linewidth=2.5))
    ax.text(img_x, img_h - 0.35, "Image", color="#a8332c", fontsize=13, ha="center")

    # ray 1: parallel to axis -> reflects through F -> image tip
    ax.plot([obj_x, 0], [obj_h, obj_h], color="#333", linewidth=1.6)
    ax.plot([0, img_x], [obj_h, img_h], color="#333", linewidth=1.6)

    # ray 2: through C, reflects back on itself (passes through image tip too)
    ax.plot([obj_x, img_x], [obj_h, img_h], color="#333", linewidth=1.2, linestyle="--")

    save(fig, "q_concave_mirror_beyond_c.png")


if __name__ == "__main__":
    enzyme_km_curve()
    pedigree_xlinked()
    titration_weak_acid_strong_base()
    circuit_r1r2_parallel_r3_series()
    concave_mirror_beyond_c()
