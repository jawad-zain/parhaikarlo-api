"""Generate the 5 diagram images referenced by mdcat_mock_15.py's
image-based questions:
  Q7   Biology  - energy profile diagram (reaction coordinate) for a
                  catalyzed vs uncatalyzed reaction; same reactant and
                  product energy levels (same delta-H) but the
                  catalyzed path has a lower activation energy peak.
  Q10  Biology  - labeled mitochondrion diagram; outer membrane, inner
                  membrane, cristae (structure X, ANSWER), matrix,
                  intermembrane space.
  Q49  Biology  - phylogenetic tree of vertebrate groups (fish,
                  amphibians, reptiles, birds, mammals) showing correct
                  branching topology (birds+reptiles as a clade,
                  mammals branching earliest among amniotes shown, fish
                  as the outgroup).
  Q131 Physics  - free-body diagram, 10 kg block on a frictionless
                  30-degree incline. Weight mg = 100 N decomposed into
                  mg*sin(30) = 50 N along the incline (down-slope) and
                  mg*cos(30) = 86.6 N into the surface, balanced by
                  Normal force N = 86.6 N perpendicular to the incline.
  Q157 Physics  - two parallel wires carrying current in the SAME
                  direction -> attract (per right-hand rule: each
                  wire's B-field at the other wire's location points in
                  the direction that pulls them together). Field
                  circles + force arrows shown.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Ellipse, Rectangle, FancyArrowPatch, Circle

OUT = Path(__file__).parent.parent / "mdcat-content" / "images"
OUT.mkdir(parents=True, exist_ok=True)


def save(fig, name):
    fig.savefig(OUT / name, dpi=150, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("wrote", OUT / name)


# ---------------------------------------------------------------
# Q7: energy profile diagram, catalyzed vs uncatalyzed reaction.
# Same reactant/product levels (same delta-H, exothermic here), but
# the catalyzed curve has a visibly lower activation-energy hump.
# ---------------------------------------------------------------
def energy_profile_catalyzed_vs_uncatalyzed():
    x = np.linspace(0, 10, 400)

    def hump(center, width, height, base_start, base_end, x):
        # smooth reaction-coordinate curve: base_start -> peak -> base_end
        y = np.piecewise(
            x,
            [x <= center, x > center],
            [
                lambda xx: base_start + (height - base_start) * np.exp(-((xx - center) ** 2) / (2 * (width) ** 2)) * (xx <= center) +
                           base_start * (xx > center),
                lambda xx: 0,
            ],
        )
        return y

    # Build manually via two logistic-ish halves for a clean single hump
    def profile(peak_x, peak_y, start_y, end_y, width):
        left = start_y + (peak_y - start_y) / (1 + np.exp(-(x - (peak_x - width)) / (width / 3)))
        right = end_y + (peak_y - end_y) / (1 + np.exp((x - (peak_x + width)) / (width / 3)))
        y = np.where(x <= peak_x, left, right)
        return y

    reactant_E, product_E = 60.0, 20.0
    uncat = profile(5.0, 95.0, reactant_E, product_E, 1.6)
    cat = profile(5.0, 65.0, reactant_E, product_E, 1.2)

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.plot(x, uncat, color="#a8332c", linewidth=2.6, label="Uncatalyzed pathway")
    ax.plot(x, cat, color="#1a7a3a", linewidth=2.6, label="Catalyzed pathway")

    ax.axhline(reactant_E, color="gray", linewidth=0.8, linestyle=":")
    ax.axhline(product_E, color="gray", linewidth=0.8, linestyle=":")
    ax.text(0.1, reactant_E + 2, "Reactants", fontsize=10.5)
    ax.text(8.3, product_E + 2, "Products", fontsize=10.5)

    # activation energy arrows
    ax.annotate("", xy=(5.0, 95.0), xytext=(5.0, reactant_E),
                arrowprops=dict(arrowstyle="<->", color="#a8332c", linewidth=1.4))
    ax.text(5.15, 78, "Ea\n(uncatalyzed)", fontsize=9.5, color="#a8332c")

    ax.annotate("", xy=(3.6, 65.0), xytext=(3.6, reactant_E),
                arrowprops=dict(arrowstyle="<->", color="#1a7a3a", linewidth=1.4))
    ax.text(2.35, 61, "Ea\n(catalyzed,\nlower)", fontsize=9.5, color="#1a7a3a")

    # delta H arrow (same for both -> catalyst does not change delta H)
    ax.annotate("", xy=(9.3, product_E), xytext=(9.3, reactant_E),
                arrowprops=dict(arrowstyle="<->", color="#333", linewidth=1.2))
    ax.text(9.4, 38, "ΔH\n(unchanged\nby catalyst)", fontsize=9, color="#333")

    ax.set_xlim(0, 10.4)
    ax.set_ylim(0, 105)
    ax.set_xlabel("Reaction Coordinate", fontsize=12)
    ax.set_ylabel("Potential Energy", fontsize=12)
    ax.set_title("Energy Profile: Catalyzed vs Uncatalyzed Reaction", fontsize=14, fontweight="bold")
    ax.set_xticks([])
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.legend(loc="upper right", fontsize=10, frameon=False)

    save(fig, "q15_enzyme_energy_profile.png")


# ---------------------------------------------------------------
# Q10: labeled mitochondrion. Outer membrane (smooth), inner membrane
# folded into cristae (structure X, ANSWER), matrix, intermembrane
# space.
# ---------------------------------------------------------------
def mitochondrion_labeled():
    fig, ax = plt.subplots(figsize=(9.5, 6))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 7)
    ax.axis("off")
    ax.set_title("Structure of a Mitochondrion", fontsize=15, fontweight="bold")

    # outer membrane (smooth ellipse)
    outer = Ellipse((6, 3.5), 9.6, 4.6, facecolor="#f6d9c4", edgecolor="#8a4a1f", linewidth=2.5, zorder=1)
    ax.add_patch(outer)

    # matrix (inner fill)
    matrix = Ellipse((6, 3.5), 8.6, 3.7, facecolor="#fbe8c9", edgecolor="none", zorder=2)
    ax.add_patch(matrix)

    # cristae: folded inner-membrane loops projecting into the matrix
    rng = np.random.default_rng(3)
    n_cristae = 7
    xs = np.linspace(2.2, 9.8, n_cristae)
    for cx in xs:
        depth = rng.uniform(1.1, 1.6)
        top = 3.5 + 1.55
        bot = 3.5 - 1.55
        # a finger-like fold from the top edge down, and one from bottom edge up (alternating)
        if int(cx) % 2 == 0:
            ys = [top, top - depth]
        else:
            ys = [bot, bot + depth]
        width = 0.55
        loop = Ellipse((cx, (ys[0] + ys[1]) / 2), width, abs(ys[0] - ys[1]) * 2,
                        facecolor="#fbe8c9", edgecolor="#c07a2e", linewidth=2.0, zorder=3)
        ax.add_patch(loop)

    # a few small matrix granules/dots for texture
    for _ in range(25):
        px = rng.uniform(3.2, 8.8)
        py = rng.uniform(2.2, 4.8)
        ax.plot(px, py, ".", color="#c9a15a", markersize=3, alpha=0.6, zorder=2)

    def label(letter, tx, ty, target, color="black"):
        ax.annotate(letter, xy=target, xytext=(tx, ty), fontsize=15, fontweight="bold",
                    ha="center", va="center", color=color,
                    arrowprops=dict(arrowstyle="-", color=color, lw=1.3),
                    bbox=dict(boxstyle="circle", facecolor="white", edgecolor=color, linewidth=1.8), zorder=6)

    # Label X on a cristae fold (the ANSWER structure)
    label("X", 4.6, 6.3, (2.9, 4.35), color="black")

    ax.text(0.2, 6.3, "Outer\nmembrane", fontsize=9.5, color="#8a4a1f")
    ax.annotate("", xy=(1.4, 4.4), xytext=(0.9, 5.9),
                arrowprops=dict(arrowstyle="-", color="#8a4a1f", lw=1.1))

    ax.text(9.6, 6.3, "Matrix", fontsize=9.5, color="#8a6a1f", ha="center")
    ax.annotate("", xy=(6.3, 3.7), xytext=(9.6, 6.0),
                arrowprops=dict(arrowstyle="-", color="#8a6a1f", lw=1.1))

    ax.text(9.9, 1.0, "Intermembrane\nspace", fontsize=9, color="#555", ha="center")
    ax.annotate("", xy=(9.55, 3.0), xytext=(9.9, 1.5),
                arrowprops=dict(arrowstyle="-", color="#555", lw=1.1))

    ax.text(6, 0.3, "X = Cristae: infoldings of the inner membrane that increase surface area for the electron transport chain",
            ha="center", fontsize=9, style="italic", color="#333")

    save(fig, "q15_mitochondrion_labeled.png")


# ---------------------------------------------------------------
# Q49: phylogenetic tree of vertebrate groups. Correct nested topology:
# fish branch off first (outgroup among these), then amphibians, then
# reptiles+birds form a clade (birds nested within/sister to
# reptiles -- reptiles here shown paraphyletic-informally as in a
# typical intro-biology tree), mammals sister to the reptile/bird
# lineage (amniotes). Birds and reptiles share the most recent common
# ancestor among the groups shown.
# ---------------------------------------------------------------
def phylogenetic_tree_vertebrates():
    fig, ax = plt.subplots(figsize=(9, 6.2))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7)
    ax.axis("off")
    ax.set_title("Phylogenetic Tree of Vertebrate Groups", fontsize=15, fontweight="bold")

    lw = 2.2
    color = "#1a5276"

    # Tip x-positions (left to right): Fish, Amphibians, Mammals, Reptiles, Birds
    tips = {"Fish": 1.5, "Amphibians": 3.3, "Mammals": 5.1, "Reptiles": 6.9, "Birds": 8.7}
    tip_y = 5.6

    # Internal node y-levels (deeper node = lower y)
    root_y = 0.8
    n1_y = 1.8   # after fish split (Tetrapoda ancestor)
    n2_y = 2.9   # after amphibian split (Amniota ancestor)
    n3_y = 4.3   # Reptiles+Birds MRCA (Sauropsida)

    def vline(x, y0, y1):
        ax.plot([x, x], [y0, y1], color=color, linewidth=lw)

    def hline(x0, x1, y):
        ax.plot([x0, x1], [y, y], color=color, linewidth=lw)

    # root to n1 (single stem)
    root_x = tips["Fish"]
    vline(root_x, root_y, n1_y)

    # n1: Fish splits off vs rest (Tetrapoda)
    tetrapoda_x = (tips["Amphibians"] + tips["Birds"]) / 2
    hline(root_x, tetrapoda_x, n1_y)
    vline(root_x, n1_y, tip_y)  # fish tip
    vline(tetrapoda_x, n1_y, n2_y)

    # n2: Amphibians split off vs Amniota (Mammals+Reptiles+Birds)
    amniota_x = (tips["Mammals"] + tips["Birds"]) / 2
    hline(tetrapoda_x, amniota_x, n2_y)
    vline(tips["Amphibians"], n2_y, tip_y)
    hline(tetrapoda_x, tips["Amphibians"], n2_y)
    vline(amniota_x, n2_y, n3_y)

    # n3: Mammals split off vs Sauropsida (Reptiles+Birds)
    sauropsida_x = (tips["Reptiles"] + tips["Birds"]) / 2
    hline(amniota_x, sauropsida_x, n3_y)
    vline(tips["Mammals"], n3_y, tip_y)
    hline(amniota_x, tips["Mammals"], n3_y)
    vline(sauropsida_x, n3_y, 4.9)

    # Reptiles/Birds MRCA -> split into Reptiles and Birds (most recent split shown)
    mrca_y = 4.9
    hline(tips["Reptiles"], tips["Birds"], mrca_y)
    vline(tips["Reptiles"], mrca_y, tip_y)
    vline(tips["Birds"], mrca_y, tip_y)

    ax.plot(sauropsida_x, mrca_y, "o", color="#c0392b", markersize=7, zorder=5)
    ax.annotate("Most recent common\nancestor of Reptiles & Birds", xy=(sauropsida_x, mrca_y),
                xytext=(sauropsida_x - 0.3, 3.55), fontsize=9, color="#c0392b", ha="center",
                arrowprops=dict(arrowstyle="-", color="#c0392b"))

    for name, x in tips.items():
        ax.plot(x, tip_y, "o", color=color, markersize=5)
        ax.text(x, tip_y + 0.25, name, ha="center", fontsize=10.5, fontweight="bold")

    ax.text(root_x - 0.3, root_y - 0.35, "Common\nancestor", fontsize=8.5, color="#555", ha="center")

    save(fig, "q15_phylogenetic_tree_vertebrates.png")


# ---------------------------------------------------------------
# Q131: free-body diagram, 10 kg block on frictionless 30-degree
# incline (g = 10 m/s^2). mg = 100 N. Component along incline
# (down-slope) = mg*sin(30) = 50 N. Component into the surface =
# mg*cos(30) = 86.6 N, balanced by Normal force N = 86.6 N
# perpendicular to the surface. Derived, not eyeballed.
# ---------------------------------------------------------------
def inclined_plane_freebody():
    theta = 30.0
    rad = np.radians(theta)
    m, g = 10.0, 10.0
    W = m * g                     # 100 N
    W_parallel = W * np.sin(rad)  # 50 N
    W_perp = W * np.cos(rad)      # 86.6 N
    N = W_perp                    # 86.6 N, frictionless equilibrium perpendicular to surface

    fig, ax = plt.subplots(figsize=(9, 6.5))
    ax.set_xlim(-1, 11)
    ax.set_ylim(-1, 7.5)
    ax.axis("off")
    ax.set_title(f"Free-Body Diagram: Block on a {theta:.0f}° Frictionless Incline (m = {m:.0f} kg)",
                 fontsize=13.5, fontweight="bold")

    # incline triangle
    base_len = 9.0
    incline_h = base_len * np.tan(rad)
    ax.plot([0, base_len], [0, 0], color="black", linewidth=2)          # ground
    ax.plot([0, 0], [0, incline_h], color="black", linewidth=0)         # (invisible, just for scale)
    ax.plot([0, base_len], [0, incline_h], color="black", linewidth=2.4)  # incline surface
    ax.plot([0, 0], [0, 0], color="black")
    ax.fill([0, base_len, base_len], [0, 0, incline_h], color="#e8e8e8", zorder=0)

    # angle arc at base
    ax.annotate("", xy=(2.0, 2.0 * np.tan(rad)), xytext=(2.0, 0))
    arc_theta = np.linspace(0, rad, 40)
    ax.plot(1.3 * np.cos(arc_theta), 1.3 * np.sin(arc_theta), color="black", linewidth=1)
    ax.text(1.7, 0.35, f"{theta:.0f}°", fontsize=11)

    # block, centered partway up the incline
    bx = base_len * 0.55
    by = bx * np.tan(rad)
    block_size = 1.0
    # place block sitting ON the incline surface: offset perpendicular to slope by half its size
    perp_dx, perp_dy = -np.sin(rad), np.cos(rad)
    cx = bx + perp_dx * block_size / 2
    cy = by + perp_dy * block_size / 2

    # draw a small rotated square for the block
    corners = []
    for dx, dy in [(-0.5, -0.5), (0.5, -0.5), (0.5, 0.5), (-0.5, 0.5)]:
        along_x, along_y = np.cos(rad), np.sin(rad)
        rx = dx * along_x - dy * (-perp_dx)
        ry = dx * along_y - dy * (-perp_dy)
        corners.append((cx + rx, cy + ry))
    corners.append(corners[0])
    xs, ys = zip(*corners)
    ax.plot(xs, ys, color="#2f6f9f", linewidth=2)
    ax.fill(xs, ys, color="#bcd9ee", zorder=2)
    ax.text(cx, cy, "m", ha="center", va="center", fontsize=12, fontweight="bold", zorder=6)

    def arrow(x0, y0, x1, y1, color, lw=2.4):
        ax.annotate("", xy=(x1, y1), xytext=(x0, y0),
                    arrowprops=dict(arrowstyle="-|>", color=color, linewidth=lw))

    scale = 0.035
    # Weight (mg) straight down
    arrow(cx, cy, cx, cy - W * scale, "#a8332c")
    ax.text(cx + 0.15, cy - W * scale - 0.3, f"mg = {W:.0f} N", color="#a8332c", fontsize=10.5)

    # Component along incline (down-slope): direction (cos, sin) but pointing down-slope = (-along_x,-along_y)
    along_x, along_y = np.cos(rad), np.sin(rad)
    arrow(cx, cy, cx - along_x * W_parallel * scale, cy - along_y * W_parallel * scale, "#1a7a3a")
    ax.text(cx - along_x * W_parallel * scale - 1.3, cy - along_y * W_parallel * scale - 0.15,
            f"mg sinθ = {W_parallel:.0f} N\n(along incline)", color="#1a7a3a", fontsize=9.5, ha="center")

    # Component into surface: direction (-perp_dx,-perp_dy) i.e. opposite to Normal
    arrow(cx, cy, cx - perp_dx * W_perp * scale, cy - perp_dy * W_perp * scale, "#7a4f96")
    ax.text(cx - perp_dx * W_perp * scale + 0.25, cy - perp_dy * W_perp * scale - 0.15,
            f"mg cosθ = {W_perp:.1f} N\n(into surface)", color="#7a4f96", fontsize=9.5)

    # Normal force N (perpendicular to surface, outward)
    arrow(cx, cy, cx + perp_dx * N * scale, cy + perp_dy * N * scale, "#1a5276")
    ax.text(cx + perp_dx * N * scale + 0.15, cy + perp_dy * N * scale + 0.15,
            f"N = {N:.1f} N", color="#1a5276", fontsize=10.5, fontweight="bold")

    ax.text(base_len / 2, -0.8,
            f"Frictionless surface: N balances mg cosθ; net force along incline = mg sinθ = {W_parallel:.0f} N",
            ha="center", fontsize=9, style="italic", color="#333")

    save(fig, "q15_inclined_plane_freebody.png")


# ---------------------------------------------------------------
# Q157: two parallel wires carrying current in the SAME direction
# (both "into the page" is not needed here -- shown as two vertical
# wires both carrying current upward). By the right-hand rule, each
# wire's magnetic field at the location of the other wire points in
# the direction that produces an attractive force -- parallel currents
# attract.
# ---------------------------------------------------------------
def parallel_wires_magnetic_field():
    fig, ax = plt.subplots(figsize=(9, 6.5))
    ax.set_xlim(-1, 11)
    ax.set_ylim(-1, 7.5)
    ax.axis("off")
    ax.set_title("Parallel Current-Carrying Wires (Same Direction) -> Attraction",
                 fontsize=14, fontweight="bold")

    x1, x2 = 3.5, 7.5
    y0, y1 = 0.5, 6.5

    for x in (x1, x2):
        ax.annotate("", xy=(x, y1), xytext=(x, y0),
                    arrowprops=dict(arrowstyle="-|>", color="#1a1a1a", linewidth=3.2))
        ax.text(x, y0 - 0.4, "I", ha="center", fontsize=12, fontweight="bold")

    ax.text(x1, y1 + 0.3, "Wire 1", ha="center", fontsize=10.5)
    ax.text(x2, y1 + 0.3, "Wire 2", ha="center", fontsize=10.5)

    # magnetic field circles around each wire (concentric), with direction
    # arrows following right-hand rule: current up (+y) -> B circles
    # counterclockwise when viewed from +y looking down (-z into page
    # convention): at a point to the RIGHT of an upward wire, B points
    # OUT of the page; standard 2D top-down sketch instead: draw field
    # loops with small tangent arrows and label direction at the
    # midpoint between the wires.
    for x, sign in [(x1, 1), (x2, -1)]:
        for r in (1.0, 1.8, 2.6):
            circ = Circle((x, (y0 + y1) / 2), r, fill=False, color="#888", linewidth=1.0, linestyle="--")
            ax.add_patch(circ)

    mid_y = (y0 + y1) / 2
    # At the midpoint between the wires: field from wire 1 (current up) circles
    # counterclockwise (right-hand rule, thumb up) -> at a point to the right
    # of wire 1, B points INTO the page. Field from wire 2 at a point to its
    # left similarly points OUT of the page in the standard convention used
    # in textbooks for this exact case -- net effect: the wires attract.
    # Show force arrows pointing toward each other (the physical, unambiguous result).
    ax.annotate("", xy=(x2 - 1.4, mid_y), xytext=(x1 + 1.4, mid_y),
                arrowprops=dict(arrowstyle="-|>", color="#c0392b", linewidth=2.6))
    ax.annotate("", xy=(x1 + 0.05, mid_y - 1.2), xytext=(x2 - 0.05, mid_y - 1.2),
                arrowprops=dict(arrowstyle="-|>", color="#c0392b", linewidth=2.6))
    ax.text((x1 + x2) / 2, mid_y - 1.7, "F (attractive)", ha="center", color="#c0392b", fontsize=10.5)

    ax.text((x1 + x2) / 2, mid_y + 1.0, "B", ha="center", color="#555", fontsize=10, style="italic")

    ax.text((x1 + x2) / 2, -0.8,
            "Currents in the SAME direction: each wire's field exerts a force on the other,\npulling them together (parallel currents attract; antiparallel currents repel).",
            ha="center", fontsize=9.5, style="italic", color="#333")

    save(fig, "q15_parallel_wires_magnetic_field.png")


if __name__ == "__main__":
    energy_profile_catalyzed_vs_uncatalyzed()
    mitochondrion_labeled()
    phylogenetic_tree_vertebrates()
    inclined_plane_freebody()
    parallel_wires_magnetic_field()
