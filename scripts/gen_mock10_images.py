"""Generate the 5 diagram/graph images referenced by mdcat_mock_10.py's
image-based questions:
  Q33  Biology  - maternal (mitochondrial) inheritance pedigree
  Q56  Biology  - labeled leaf cross-section
  Q105 Chemistry- reactant concentration vs time kinetics graph
  Q154 Physics  - three-resistor series circuit (R1=2, R2=3, R3=5 -> 10 ohm)
  Q162 Physics  - concave (diverging) lens ray diagram
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Ellipse, Wedge, FancyArrow, Polygon

OUT = Path(__file__).parent.parent / "mdcat-content" / "images"
OUT.mkdir(parents=True, exist_ok=True)


def save(fig, name):
    fig.savefig(OUT / name, dpi=150, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("wrote", OUT / name)


# ---------------------------------------------------------------
# Q33: Maternal (mitochondrial) inheritance pedigree.
# Branch A: affected mother x unaffected father -> ALL children affected,
#           both sexes (mitochondrial signature).
# Branch B: unaffected mother x affected father -> NO children affected,
#           even though father is affected (paternal mitochondria are not
#           transmitted).
# ---------------------------------------------------------------
def pedigree_mitochondrial():
    fig, ax = plt.subplots(figsize=(9, 6.5))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 9)
    ax.axis("off")
    ax.set_title("Pedigree: Maternal (Mitochondrial) Inheritance", fontsize=15, fontweight="bold")

    def square(x, y, filled=False, label=""):
        s = 0.5
        ax.add_patch(plt.Rectangle((x - s / 2, y - s / 2), s, s,
                                    facecolor="black" if filled else "white", edgecolor="black", linewidth=1.5))
        if label:
            ax.text(x, y - 0.65, label, ha="center", va="top", fontsize=8.5, linespacing=1.4)

    def circle(x, y, filled=False, label=""):
        r = 0.28
        ax.add_patch(plt.Circle((x, y), r, facecolor="black" if filled else "white", edgecolor="black", linewidth=1.5))
        if label:
            ax.text(x, y - 0.65, label, ha="center", va="top", fontsize=8.5, linespacing=1.4)

    def marry(x1, y, x2):
        ax.plot([x1, x2], [y, y], color="black", linewidth=1.3)

    def descend(xmid, y_top, y_bot, children_x):
        y_bar = (y_top + y_bot) / 2
        ax.plot([xmid, xmid], [y_top, y_bar], color="black", linewidth=1.3)
        xs = children_x
        ax.plot([min(xs), max(xs)], [y_bar, y_bar], color="black", linewidth=1.3)
        for cx in xs:
            ax.plot([cx, cx], [y_bar, y_bot], color="black", linewidth=1.3)

    # --- Branch A (left): affected mother x unaffected father ---
    ax.text(2.5, 8.4, "Family A", fontsize=11, fontweight="bold", ha="center")
    circle(1.5, 7.5, filled=True, label="I-1\naffected mother")
    square(3.5, 7.5, filled=False, label="I-2\nunaffected father")
    marry(1.5, 7.5, 3.5)
    descend(2.5, 7.2, 5.3, [1.0, 2.5, 4.0])
    square(1.0, 5, filled=True, label="II-1\nson")
    circle(2.5, 5, filled=True, label="II-2\ndau.")
    square(4.0, 5, filled=True, label="II-3\nson")

    # --- Branch B (right): unaffected mother x affected father ---
    ax.text(9, 8.4, "Family B", fontsize=11, fontweight="bold", ha="center")
    circle(8, 7.5, filled=False, label="I-3\nunaffected mother")
    square(10, 7.5, filled=True, label="I-4\naffected father")
    marry(8, 7.5, 10)
    descend(9, 7.2, 5.3, [7.5, 9, 10.5])
    square(7.5, 5, filled=False, label="II-4\nson")
    circle(9, 5, filled=False, label="II-5\ndau.")
    square(10.5, 5, filled=False, label="II-6\nson")

    # legend
    circle(1.0, 2.2, filled=True, label="")
    ax.text(1.4, 2.2, "= affected female", fontsize=10, va="center")
    square(1.0, 1.3, filled=True, label="")
    ax.text(1.4, 1.3, "= affected male", fontsize=10, va="center")
    circle(6.2, 2.2, filled=False, label="")
    ax.text(6.6, 2.2, "= unaffected female", fontsize=10, va="center")
    square(6.2, 1.3, filled=False, label="")
    ax.text(6.6, 1.3, "= unaffected male", fontsize=10, va="center")

    save(fig, "q_pedigree_mitochondrial.png")


# ---------------------------------------------------------------
# Q56: Leaf cross-section, labeled 1-4 (top to bottom):
#   1 = upper epidermis (with cuticle)
#   2 = palisade mesophyll (tightly packed, chloroplast-rich -> main
#       site of photosynthesis)
#   3 = spongy mesophyll (loosely packed, air spaces, gas exchange)
#   4 = lower epidermis (with stomata / guard cells)
# A vascular bundle (xylem + phloem) is also shown for context.
# ---------------------------------------------------------------
def leaf_crosssection_diagram():
    fig, ax = plt.subplots(figsize=(9, 6))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 8)
    ax.axis("off")
    ax.set_title("Cross-Section of a Leaf", fontsize=15, fontweight="bold")

    x0, x1 = 1.0, 11.0

    # layer y-bands (top to bottom)
    bands = [
        ("cuticle", 7.2, 7.4, "#d8d8a0"),
        ("upper epidermis", 6.5, 7.2, "#f2e6b3"),      # structure 1
        ("palisade mesophyll", 4.9, 6.5, "#2e7d32"),   # structure 2
        ("spongy mesophyll", 2.6, 4.9, "#8fbf7a"),     # structure 3
        ("lower epidermis", 1.8, 2.6, "#f2e6b3"),      # structure 4
    ]
    for name, y0, y1, color in bands:
        ax.add_patch(plt.Rectangle((x0, y0), x1 - x0, y1 - y0, facecolor=color, edgecolor="black", linewidth=1.0))

    # palisade cells: tall tightly packed rectangles with green chloroplast dots
    for cx in np.arange(x0 + 0.3, x1, 0.55):
        ax.add_patch(plt.Rectangle((cx, 4.9), 0.45, 1.6, facecolor="#3d8b40", edgecolor="#1b5e20", linewidth=0.6))
        for dy in (5.15, 5.55, 5.95, 6.35):
            ax.plot(cx + 0.22, dy, "o", color="#1b5e20", markersize=1.8)

    # spongy mesophyll: irregular loosely packed cells with visible air spaces (white gaps)
    rng = np.random.default_rng(7)
    for _ in range(34):
        cx = rng.uniform(x0 + 0.2, x1 - 0.5)
        cy = rng.uniform(2.75, 4.75)
        r = rng.uniform(0.18, 0.3)
        ax.add_patch(Ellipse((cx, cy), r * 2, r * 1.6, facecolor="#5aa14a", edgecolor="#2e6b2e", linewidth=0.6))

    # stomata + guard cells on lower epidermis
    for cx in (2.5, 5.0, 7.5, 10.0):
        ax.add_patch(Ellipse((cx, 2.15), 0.5, 0.3, facecolor="white", edgecolor="black", linewidth=1.0))
        ax.add_patch(Ellipse((cx - 0.2, 2.15), 0.3, 0.42, facecolor="#c9e0b0", edgecolor="black", linewidth=0.8))
        ax.add_patch(Ellipse((cx + 0.2, 2.15), 0.3, 0.42, facecolor="#c9e0b0", edgecolor="black", linewidth=0.8))
        ax.plot(cx, 1.5, marker="v", markersize=4, color="black")

    # vascular bundle (xylem below, phloem above) embedded in the mesophyll
    vb_x, vb_y, vb_w, vb_h = 5.2, 3.1, 1.6, 2.1
    ax.add_patch(Ellipse((vb_x + vb_w / 2, vb_y + vb_h / 2), vb_w, vb_h, facecolor="#e8d3a0", edgecolor="black", linewidth=1.2))
    ax.add_patch(Ellipse((vb_x + vb_w / 2, vb_y + vb_h * 0.65), vb_w * 0.55, vb_h * 0.4, facecolor="#c9a15a", edgecolor="#7a5a1e", linewidth=0.8))
    ax.text(vb_x + vb_w / 2, vb_y + vb_h * 0.65, "phloem", ha="center", va="center", fontsize=6.5)
    ax.add_patch(Ellipse((vb_x + vb_w / 2, vb_y + vb_h * 0.3), vb_w * 0.6, vb_h * 0.42, facecolor="#a8783a", edgecolor="#5a3a10", linewidth=0.8))
    ax.text(vb_x + vb_w / 2, vb_y + vb_h * 0.3, "xylem", ha="center", va="center", fontsize=6.5, color="white")
    ax.text(vb_x + vb_w / 2, vb_y + vb_h + 0.25, "vascular bundle", ha="center", fontsize=8, style="italic")

    def label(num, tx, ty, ax_target_y):
        ax.annotate(
            str(num), xy=(11.6, ax_target_y), xytext=(tx, ty), fontsize=13, fontweight="bold",
            ha="center", va="center",
            arrowprops=dict(arrowstyle="-", color="black", lw=1),
            bbox=dict(boxstyle="circle", facecolor="white", edgecolor="black", linewidth=1.5),
        )

    ax.set_xlim(0, 13.2)
    label(1, 12.6, 6.85, 6.85)   # upper epidermis
    label(2, 12.6, 5.7, 5.7)    # palisade mesophyll
    label(3, 12.6, 3.75, 3.75)  # spongy mesophyll
    label(4, 12.6, 2.2, 2.2)    # lower epidermis

    save(fig, "q_leaf_crosssection_diagram.png")


# ---------------------------------------------------------------
# Q105: Reactant concentration vs time (exponential decay). The slope
# (rate) is steepest at t=0 and flattens as the reaction proceeds --
# consistent with the correct answer "initial rate = slope at the start".
# ---------------------------------------------------------------
def concentration_vs_time_graph():
    C0, k = 1.0, 0.6
    t = np.linspace(0, 8, 400)
    C = C0 * np.exp(-k * t)
    fig, ax = plt.subplots(figsize=(7, 5.5))
    ax.plot(t, C, color="#1b6e6e", linewidth=2.6)

    # tangent line at t=0 to visualize the initial slope
    slope0 = -k * C0
    t_tan = np.linspace(0, 2.2, 20)
    C_tan = C0 + slope0 * t_tan
    ax.plot(t_tan, C_tan, color="#a8332c", linestyle="--", linewidth=1.8)
    ax.text(1.3, C0 + slope0 * 1.3 + 0.06, "initial slope\n(steepest)", color="#a8332c", fontsize=10)

    ax.set_title("Reactant Concentration vs Time", fontsize=14, fontweight="bold")
    ax.set_xlabel("Time", fontsize=12)
    ax.set_ylabel("[Reactant]", fontsize=12)
    ax.set_xlim(0, 8)
    ax.set_ylim(0, 1.1)
    ax.grid(alpha=0.25, linestyle=":")
    save(fig, "q_concentration_vs_time_graph.png")


# ---------------------------------------------------------------
# Q154: R1 (2 ohm), R2 (3 ohm), R3 (5 ohm) all in series -> R_total = 10 ohm
# ---------------------------------------------------------------
def circuit_series_r1r2r3():
    fig, ax = plt.subplots(figsize=(7.5, 4.2))
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
            ax.text(midx, midy + 0.5, label, ha="center", fontsize=11)
        else:
            ax.text(midx + 1.05, midy, label, ha="center", fontsize=11)

    # single loop: battery -> R1 -> R2 -> R3 -> back to battery (all in series)
    ax.plot([1, 1], [3.6, 5], color="black", linewidth=2)
    ax.plot([1, 3], [5, 5], color="black", linewidth=2)

    resistor(3, 5, 5, 5, "R1 = 2 Ω")
    resistor(5, 5, 7, 5, "R2 = 3 Ω")

    ax.plot([7, 9], [5, 5], color="black", linewidth=2)
    ax.plot([9, 9], [5, 0.5], color="black", linewidth=2)
    resistor(9, 3.3, 9, 1.7, "R3 = 5 Ω")

    ax.plot([1, 1], [2.4, 0.5], color="black", linewidth=2)
    ax.plot([1, 9], [0.5, 0.5], color="black", linewidth=2)

    ax.text(5, 1.0, "Single loop -- all three resistors carry the same current (series)", ha="center", fontsize=9, style="italic")

    save(fig, "q_circuit_series_r1r2r3.png")


# ---------------------------------------------------------------
# Q162: Concave (diverging) lens ray diagram. For ANY object distance,
# a diverging lens forms a virtual, upright, diminished image on the
# SAME side of the lens as the object, located between the lens and its
# near focal point.
#   f = 3 (focal length magnitude), u = 6 (object distance magnitude)
#   v = f*u/(f+u) = 2   (image distance magnitude, same side as object)
#   h_obj = 1.6 -> h_img = h_obj * v/u = 0.5333 (upright, smaller)
# ---------------------------------------------------------------
def concave_lens_diverging():
    f = 3.0
    u = 6.0
    h_obj = 1.6
    v = (f * u) / (f + u)
    h_img = h_obj * v / u

    obj_x = -u
    img_x = -v

    fig, ax = plt.subplots(figsize=(9.5, 5.8))
    ax.set_xlim(obj_x - 1, 5)
    ax.set_ylim(-2.6, h_obj + 1.2)
    ax.axis("off")
    ax.set_title("Ray Diagram: Concave (Diverging) Lens", fontsize=15, fontweight="bold")

    ax.axhline(0, color="black", linewidth=1.2)

    # lens symbol at x=0: vertical line with inward-pointing arrowheads
    # (standard convention for a diverging lens)
    ax.plot([0, 0], [-2.2, 2.2], color="#3a5f8f", linewidth=2.5)
    ax.plot([-0.3, 0], [2.2, 1.9], color="#3a5f8f", linewidth=2.5)
    ax.plot([0.3, 0], [2.2, 1.9], color="#3a5f8f", linewidth=2.5)
    ax.plot([-0.3, 0], [-2.2, -1.9], color="#3a5f8f", linewidth=2.5)
    ax.plot([0.3, 0], [-2.2, -1.9], color="#3a5f8f", linewidth=2.5)

    # focal points: F (near/front, same side as object) and F' (far side)
    for x, lbl in [(-f, "F"), (f, "F'"), (0, "O")]:
        ax.plot(x, 0, "o", color="gray", markersize=4)
        ax.text(x, -0.22, lbl, ha="center", va="top", fontsize=12, color="gray")

    # object arrow
    ax.annotate("", xy=(obj_x, h_obj), xytext=(obj_x, 0),
                arrowprops=dict(arrowstyle="-|>", color="#1a7a3a", linewidth=2.5))
    ax.text(obj_x, h_obj + 0.25, "Object", color="#1a7a3a", fontsize=13, ha="center")

    # image arrow (virtual, upright, diminished, same side as object)
    ax.annotate("", xy=(img_x, h_img), xytext=(img_x, 0),
                arrowprops=dict(arrowstyle="-|>", color="#a8332c", linewidth=2.5))
    ax.text(img_x, h_img + 0.22, "Image\n(virtual)", color="#a8332c", fontsize=10, ha="center")

    # Ray 1: parallel to axis from object top to lens; after refraction it
    # diverges as though coming from the near focal point F. Solid ray
    # continues forward (right) diverging away from axis; its backward
    # extension (dashed, to the left) passes through F and the image point.
    slope_emerge = (h_obj - 0) / (0 - (-f))  # = h_obj / f
    ax.plot([obj_x, 0], [h_obj, h_obj], color="#333", linewidth=1.6)          # incident (solid)
    ax.plot([0, 4], [h_obj, h_obj + slope_emerge * 4], color="#333", linewidth=1.6)  # emergent (solid)
    ax.plot([img_x, 0], [h_img, h_obj], color="#333", linewidth=1.2, linestyle="--")  # backward ext. (dashed)
    ax.plot([-f, img_x], [0, h_img], color="#333", linewidth=1.0, linestyle=":")

    # Ray 2: chief ray through the optical center O -- undeviated (solid
    # throughout); at x = -v it already passes through the image height.
    slope_chief = (0 - h_obj) / (0 - obj_x)
    ax.plot([obj_x, 4], [h_obj, h_obj + slope_chief * (4 - obj_x)], color="#333", linewidth=1.6)

    ax.text(1.2, -2.4, "Virtual image forms between the lens and F, on the SAME side as the object\n"
                       "-> virtual, upright, diminished (true for any object distance)",
            fontsize=9, style="italic", ha="left")

    save(fig, "q_concave_lens_diverging.png")


if __name__ == "__main__":
    pedigree_mitochondrial()
    leaf_crosssection_diagram()
    concentration_vs_time_graph()
    circuit_series_r1r2r3()
    concave_lens_diverging()
