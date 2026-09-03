"""Generate the 5 diagram/graph images referenced by mdcat_mock_14.py's
image-based questions:
  Q8   Biology  - enzyme activity vs temperature curve, rises to a
                  maximum near 37 C then falls sharply above 40 C
                  (denaturation).
  Q76  Biology  - labeled neuron diagram; structure X = axon (long thin
                  extension carrying the action potential away from the
                  cell body).
  Q110 Chemistry- pH titration curve, strong acid (HCl) titrated with
                  strong base (NaOH); equivalence point at exactly pH 7.
  Q129 Physics  - projectile trajectory diagram (angled launch, no air
                  resistance); at the apex, vertical velocity = 0,
                  horizontal velocity component constant throughout.
  Q154 Physics  - converging (convex) lens ray diagram, object placed
                  beyond 2F -> real, inverted, diminished image between
                  F and 2F on the far side (derived via 1/v = 1/f - 1/u,
                  not eyeballed).

Styled distinctly from the visually-similar diagrams already used in
earlier mocks (enzyme-temp curve differs from mock 1's; strong/strong
titration curve differs from mock 1's) to avoid duplicate-image MD5
collisions in the shared image library.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Ellipse, Circle, FancyArrowPatch

OUT = Path(__file__).parent.parent / "mdcat-content" / "images"
OUT.mkdir(parents=True, exist_ok=True)


def save(fig, name):
    fig.savefig(OUT / name, dpi=150, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("wrote", OUT / name)


# ---------------------------------------------------------------
# Q8: enzyme activity vs temperature (rises to max ~37C, sharp fall
# above 40C due to denaturation). Styled distinctly from mock 1's
# version (different color, dashed 37C marker, slightly different
# curve shape/width).
# ---------------------------------------------------------------
def enzyme_temperature_curve():
    t = np.linspace(0, 70, 400)
    rate = np.where(
        t <= 37,
        100 * (1 - np.exp(-t / 10.5)),
        100 * np.exp(-((t - 37) ** 2) / (2 * 5.2 ** 2)),
    )
    fig, ax = plt.subplots(figsize=(7.2, 5.6))
    ax.plot(t, rate, color="#8a3ab5", linewidth=2.8)
    ax.fill_between(t, rate, color="#8a3ab5", alpha=0.10)
    ax.axvline(37, color="#c0392b", linestyle="--", linewidth=1.3)
    ax.text(37.5, 95, "37°C\n(optimum)", fontsize=9.5, color="#c0392b")
    ax.axvline(40, color="gray", linestyle=":", linewidth=1.1)
    ax.text(40.5, 55, "40°C", fontsize=9, color="gray")
    ax.set_title("Enzyme Activity vs Temperature", fontsize=15, fontweight="bold")
    ax.set_xlabel("Temperature (°C)", fontsize=12)
    ax.set_ylabel("Rate of Enzyme Activity (%)", fontsize=12)
    ax.set_xlim(0, 70)
    ax.set_ylim(0, 110)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.grid(alpha=0.25)
    save(fig, "q14_enzyme_temperature_curve.png")


# ---------------------------------------------------------------
# Q76: labeled neuron diagram. Cell body (soma) with nucleus and
# dendrites on one side, a long axon (structure X, ANSWER) wrapped in
# a myelin sheath with visible Nodes of Ranvier, ending in axon
# terminals/synaptic knobs.
# ---------------------------------------------------------------
def neuron_diagram_labeled():
    fig, ax = plt.subplots(figsize=(10, 5.5))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 7)
    ax.axis("off")
    ax.set_title("Structure of a Neuron", fontsize=15, fontweight="bold")

    # cell body (soma)
    soma_center = (2.2, 3.6)
    ax.add_patch(Ellipse(soma_center, 2.0, 1.8, facecolor="#f4d9a0", edgecolor="#8a6a1f", linewidth=2, zorder=4))
    # nucleus
    ax.add_patch(Circle((2.2, 3.6), 0.45, facecolor="#8a6a1f", edgecolor="#5a4210", linewidth=1, zorder=5))

    # dendrites (branching lines from soma, left side)
    rng = np.random.default_rng(11)
    for ang in np.linspace(100, 260, 7):
        rad = np.radians(ang)
        x0 = soma_center[0] + 1.0 * np.cos(rad)
        y0 = soma_center[1] + 0.9 * np.sin(rad)
        x1 = x0 + 0.9 * np.cos(rad) + rng.uniform(-0.2, 0.2)
        y1 = y0 + 0.9 * np.sin(rad) + rng.uniform(-0.2, 0.2)
        ax.plot([x0, x1], [y0, y1], color="#2e7d32", linewidth=1.6)
        # small branch tips
        for d in (-0.25, 0.25):
            ax.plot([x1, x1 + 0.3 * np.cos(rad) + d], [y1, y1 + 0.3 * np.sin(rad) + d],
                     color="#2e7d32", linewidth=1.2)
    ax.text(0.3, 5.4, "Dendrites", fontsize=10.5, color="#2e7d32")

    # axon (structure X, ANSWER) -- long line from soma to axon terminals
    axon_start = (3.2, 3.4)
    axon_end = (9.6, 2.3)
    ax.plot([axon_start[0], axon_end[0]], [axon_start[1], axon_end[1]],
            color="#1a5276", linewidth=3.0, zorder=3)

    # myelin sheath segments (sausage-shaped) with gaps = Nodes of Ranvier
    n_seg = 6
    xs = np.linspace(axon_start[0] + 0.3, axon_end[0] - 1.0, n_seg)
    ys = np.linspace(axon_start[1] - 0.02, axon_end[1] + 0.15, n_seg)
    for i, (sx, sy) in enumerate(zip(xs, ys)):
        seg_len = 0.75
        ax.add_patch(Ellipse((sx, sy), seg_len, 0.55, facecolor="#d8e8f5", edgecolor="#5a9bd4",
                              linewidth=1.3, zorder=2, alpha=0.9))
        if i < n_seg - 1:
            gap_x = sx + seg_len / 2 + 0.13
            gap_y = sy + (ys[i + 1] - sy) * 0.15
            ax.plot(gap_x, gap_y, "o", color="#c0392b", markersize=3.5, zorder=5)
    ax.text(6.2, 4.4, "Myelin Sheath", fontsize=9.5, color="#5a9bd4")
    ax.text(6.0, 1.55, "Node of Ranvier", fontsize=8.5, color="#c0392b")

    # axon terminals (branching at the far end)
    for ang in np.linspace(-35, 35, 4):
        rad = np.radians(ang)
        tx = axon_end[0] + 0.7 * np.cos(rad)
        ty = axon_end[1] + 0.7 * np.sin(rad)
        ax.plot([axon_end[0], tx], [axon_end[1], ty], color="#1a5276", linewidth=1.8)
        ax.add_patch(Circle((tx, ty), 0.08, facecolor="#1a5276", zorder=5))
    ax.text(10.0, 2.0, "Axon Terminals", fontsize=9.5, color="#1a5276")

    def label(letter, tx, ty, target):
        ax.annotate(letter, xy=target, xytext=(tx, ty), fontsize=16, fontweight="bold",
                    ha="center", va="center", color="black",
                    arrowprops=dict(arrowstyle="-", color="black", lw=1.3),
                    bbox=dict(boxstyle="circle", facecolor="white", edgecolor="black", linewidth=1.8), zorder=6)

    # Label X on the axon (the ANSWER structure)
    mid_axon = ((axon_start[0] + axon_end[0]) / 2, (axon_start[1] + axon_end[1]) / 2 - 0.05)
    label("X", 6.4, 5.6, mid_axon)

    ax.text(2.2, 5.6, "Cell Body\n(Soma)", ha="center", fontsize=9.5, color="#8a6a1f")

    ax.text(6, 0.4, "X = Axon: carries the action potential away from the cell body toward the axon terminals",
            ha="center", fontsize=9, style="italic", color="#333")

    save(fig, "q14_neuron_diagram_labeled.png")


# ---------------------------------------------------------------
# Q110: titration curve, strong acid (HCl) titrated with strong base
# (NaOH). Sharp S-curve, equivalence point exactly at pH 7 (NaCl salt
# does not hydrolyze). Styled distinctly from mock 1's strong/strong
# curve (different color, steeper/narrower transition, different
# volume scale and annotation style) to avoid an MD5 duplicate.
# ---------------------------------------------------------------
def titration_strong_acid_strong_base():
    veq = 20.0
    v = np.linspace(0.01, 40, 500)
    ph = 1.2 + 12.6 / (1 + np.exp(-1.6 * (v - veq)))

    fig, ax = plt.subplots(figsize=(7.6, 5.8))
    ax.plot(v, ph, color="#16794f", linewidth=2.8)
    ax.axhline(7, color="gray", linewidth=0.9, linestyle=":")
    ax.axvline(veq, color="#c0392b", linewidth=1.0, linestyle="--")
    ax.plot(veq, 7.0, "o", color="#c0392b", markersize=8, zorder=5)
    ax.annotate("Equivalence point\n(pH = 7, NaCl does not hydrolyze)", xy=(veq, 7.0),
                xytext=(veq - 17, 9.6), fontsize=9.5, color="#c0392b",
                arrowprops=dict(arrowstyle="-", color="#c0392b"))

    ax.set_xlim(0, 40)
    ax.set_ylim(0, 14)
    ax.set_xlabel("Volume of NaOH added (mL)", fontsize=12)
    ax.set_ylabel("pH", fontsize=12)
    ax.set_title("Titration Curve: Strong Acid (HCl) with Strong Base (NaOH)", fontsize=13, fontweight="bold")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.grid(alpha=0.2)

    save(fig, "q14_titration_strong_acid_strong_base.png")


# ---------------------------------------------------------------
# Q129: projectile trajectory diagram. Parabolic path from launch
# point to landing point, with the horizontal velocity component (vx,
# constant throughout) and vertical velocity component (vy, zero at
# the apex) explicitly annotated at three points: launch, apex, and
# midway down.
# ---------------------------------------------------------------
def projectile_trajectory_diagram():
    v0 = 20.0
    angle = 50.0
    g = 9.8
    rad = np.radians(angle)
    vx = v0 * np.cos(rad)
    vy0 = v0 * np.sin(rad)
    t_flight = 2 * vy0 / g
    t = np.linspace(0, t_flight, 300)
    x = vx * t
    y = vy0 * t - 0.5 * g * t ** 2

    fig, ax = plt.subplots(figsize=(9, 5.5))
    ax.plot(x, y, color="#1a5276", linewidth=2.8)
    ax.axhline(0, color="black", linewidth=1.2)

    # apex
    t_apex = vy0 / g
    x_apex = vx * t_apex
    y_apex = vy0 * t_apex - 0.5 * g * t_apex ** 2
    ax.plot(x_apex, y_apex, "o", color="#c0392b", markersize=8, zorder=5)
    ax.annotate("Highest point\n(vertical velocity = 0,\nhorizontal velocity unchanged)",
                xy=(x_apex, y_apex), xytext=(x_apex - 2, y_apex + 6),
                fontsize=9.5, color="#c0392b", ha="center",
                arrowprops=dict(arrowstyle="-", color="#c0392b"))

    # velocity vector arrows at launch, apex, and a descending point
    def draw_vec(px, py, vxc, vyc, scale, color, label):
        ax.annotate("", xy=(px + vxc * scale, py + vyc * scale), xytext=(px, py),
                    arrowprops=dict(arrowstyle="-|>", color=color, linewidth=1.8))

    scale = 0.14
    # launch point vectors
    draw_vec(0, 0, vx, vy0, scale, "#1a7a3a", "launch")
    ax.text(vx * scale + 0.3, vy0 * scale, "v", fontsize=9, color="#1a7a3a")
    # horizontal component at launch (dashed, ground level projection)
    draw_vec(0, -1.6, vx, 0, scale, "#7a4f96", "")
    ax.text(vx * scale - 0.5, -1.9, "vx (constant)", fontsize=9, color="#7a4f96")

    # apex: only horizontal component (vy = 0)
    draw_vec(x_apex, y_apex + 1.2, vx, 0, scale, "#7a4f96", "")

    # descending point (mirror of a point before apex)
    t_desc = t_flight * 0.75
    x_desc = vx * t_desc
    y_desc = vy0 * t_desc - 0.5 * g * t_desc ** 2
    vy_desc = vy0 - g * t_desc
    draw_vec(x_desc, y_desc, vx, vy_desc, scale, "#c0392b", "")

    ax.plot(0, 0, "^", color="black", markersize=9)
    ax.text(0, -2.6, "Launch", ha="center", fontsize=9.5)
    ax.plot(x[-1], 0, "v", color="black", markersize=9)
    ax.text(x[-1], -2.6, "Landing", ha="center", fontsize=9.5)

    ax.set_xlim(-2, x[-1] + 3)
    ax.set_ylim(-3.5, y_apex + 9)
    ax.axis("off")
    ax.set_title("Projectile Motion Trajectory", fontsize=15, fontweight="bold")

    save(fig, "q14_projectile_trajectory_diagram.png")


# ---------------------------------------------------------------
# Q154: converging (convex) lens, object beyond 2F -> real, inverted,
# diminished image located between F and 2F on the far side. Image
# position derived from 1/v = 1/f - 1/u (sign convention: object
# distance negative), not eyeballed.
# ---------------------------------------------------------------
def converging_lens_ray_diagram():
    f = 2.0
    obj_x, obj_h = -3.0 * f, 1.5   # beyond 2F (object at 3F)

    slope = obj_h / obj_x
    img_x = 1.0 / (1.0 / f + 1.0 / obj_x)   # = 1/(1/f - 1/|u|) with sign convention folded in
    img_h = slope * img_x

    fig, ax = plt.subplots(figsize=(9, 5.5))
    ax.set_xlim(obj_x - 1, 2 * f + 2)
    ax.set_ylim(img_h - 1.5, obj_h + 1.5)
    ax.axis("off")
    ax.set_title("Ray Diagram: Converging Lens (Object beyond 2F)", fontsize=15, fontweight="bold")

    ax.axhline(0, color="black", linewidth=1.2)
    ax.plot([0, 0], [img_h - 1.2, obj_h + 1.2], color="#2f6f9f", linewidth=3)

    for x, lbl in [(-2 * f, "2F"), (-f, "F"), (f, "F"), (2 * f, "2F")]:
        ax.plot(x, 0, "o", color="gray", markersize=4)
        ax.text(x, 0.15, lbl, ha="center", va="bottom", fontsize=12, color="gray")

    # object (green, upright)
    ax.annotate("", xy=(obj_x, obj_h), xytext=(obj_x, 0),
                arrowprops=dict(arrowstyle="-|>", color="#1a7a3a", linewidth=2.5))
    ax.text(obj_x, obj_h + 0.25, "Object", color="#1a7a3a", fontsize=13, ha="center")

    # image (red, inverted, diminished, real -- between F and 2F)
    ax.annotate("", xy=(img_x, img_h), xytext=(img_x, 0),
                arrowprops=dict(arrowstyle="-|>", color="#a8332c", linewidth=2.5))
    ax.text(img_x, img_h - 0.35, "Image", color="#a8332c", fontsize=13, ha="center")

    # ray 1: parallel to axis -> refracts through far focal point -> image tip
    ax.plot([obj_x, 0], [obj_h, obj_h], color="#333", linewidth=1.6)
    ax.plot([0, img_x], [obj_h, img_h], color="#333", linewidth=1.6)

    # ray 2: through optical center, undeviated
    ax.plot([obj_x, img_x], [obj_h, img_h], color="#333", linewidth=1.2, linestyle="--")

    # ray 3: through near focal point -> emerges parallel to axis -> image tip
    ax.plot([obj_x, 0], [obj_h, 0], color="#333", linewidth=1.6)
    ax.plot([0, img_x], [0, img_h], color="#333", linewidth=1.6)

    ax.text(0, img_h - 1.3, f"u = {obj_x:.1f}, f = {f:.1f}  =>  v = {img_x:.2f} (between F and 2F, real/inverted/diminished)",
            ha="center", fontsize=9, style="italic", color="#333")

    save(fig, "q14_converging_lens_ray_diagram.png")


if __name__ == "__main__":
    enzyme_temperature_curve()
    neuron_diagram_labeled()
    titration_strong_acid_strong_base()
    projectile_trajectory_diagram()
    converging_lens_ray_diagram()
