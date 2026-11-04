"""Regenerate the figures used in README.md.

    python assets/make_figures.py

Outputs PNG (300 dpi), PDF and SVG versions of each figure into assets/.
Only matplotlib is required. All layer sizes below mirror src/model.py and
src/data_loader.py (input = 45 CICIoMT2024 flow features).
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.patches import FancyBboxPatch, Polygon, Rectangle, Circle, FancyArrowPatch

OUT = os.path.dirname(os.path.abspath(__file__))

# ------------------------------------------------------------------ style --
for name in ("Inter", "Helvetica", "Arial", "Liberation Sans", "DejaVu Sans"):
    if any(f.name == name for f in fm.fontManager.ttflist):
        plt.rcParams["font.family"] = name
        break
plt.rcParams.update({"svg.fonttype": "none", "pdf.fonttype": 42, "text.usetex": False})

INK = "#1F2937"
MUTED = "#6B7280"
GRID = "#CBD5E1"
C = {  # (face, edge)
    "input":   ("#E5E7EB", "#6B7280"),
    "conv":    ("#BFDBFE", "#2563EB"),
    "pool":    ("#FDE68A", "#D97706"),
    "flat":    ("#E9D5FF", "#7C3AED"),
    "dense":   ("#BBF7D0", "#16A34A"),
    "out":     ("#FECACA", "#DC2626"),
    "data":    ("#F1F5F9", "#64748B"),
}


def save(fig, stem):
    for ext in ("png", "pdf", "svg"):
        fig.savefig(os.path.join(OUT, f"{stem}.{ext}"), dpi=300, bbox_inches="tight",
                    facecolor="white")
    plt.close(fig)


def shade(hex_, f):
    hex_ = hex_.lstrip("#")
    r, g, b = (int(hex_[i:i + 2], 16) for i in (0, 2, 4))
    return "#%02x%02x%02x" % tuple(max(0, min(255, int(v * f))) for v in (r, g, b))


def cuboid(ax, x, yc, w, h, d, kind, lw=1.1, alpha=1.0):
    """Oblique-projection block. (x, yc) = front-face left edge / vertical centre."""
    face, edge = C[kind]
    dx, dy = d * 0.866, d * 0.5
    y = yc - h / 2
    front = [(x, y), (x + w, y), (x + w, y + h), (x, y + h)]
    top = [(x, y + h), (x + w, y + h), (x + w + dx, y + h + dy), (x + dx, y + h + dy)]
    side = [(x + w, y), (x + w + dx, y + dy), (x + w + dx, y + h + dy), (x + w, y + h)]
    for poly, f in ((side, shade(face, 0.86)), (top, shade(face, 1.0)), (front, shade(face, 0.95))):
        ax.add_patch(Polygon(poly, closed=True, fc=f, ec=edge, lw=lw, alpha=alpha, joinstyle="round", zorder=2))
    return dict(x0=x, x1=x + w + dx, y0=y, y1=y + h + dy, front=(x, y, w, h), dx=dx, dy=dy)


def label(ax, x, y, s, size=8.5, color=INK, weight="normal", ha="center", va="center", style="normal", z=6):
    ax.text(x, y, s, fontsize=size, color=color, fontweight=weight, ha=ha, va=va, fontstyle=style, zorder=z,
            linespacing=1.25)


def arrow(ax, p, q, color=MUTED, lw=1.3, style="-|>", ms=9, rad=0.0, z=3, ls="-"):
    ax.add_patch(FancyArrowPatch(p, q, arrowstyle=style, mutation_scale=ms, color=color, lw=lw, zorder=z,
                                 connectionstyle=f"arc3,rad={rad}", linestyle=ls, shrinkA=0, shrinkB=0))


def rbox(ax, x, y, w, h, kind, lw=1.2, r=0.08, z=2):
    face, edge = C[kind]
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle=f"round,pad=0,rounding_size={r}",
                                fc=face, ec=edge, lw=lw, zorder=z))


# ============================================================ FIGURE 1: CNN ==
def fig_architecture():
    fig, ax = plt.subplots(figsize=(15.5, 5.9))
    ax.set_xlim(-0.4, 21.6)
    ax.set_ylim(-4.6, 3.9)
    ax.set_aspect("equal")
    ax.axis("off")

    H = lambda L: 0.35 + 0.05 * L          # sequence length -> height
    D = lambda ch: 0.10 + 0.016 * ch        # channels        -> oblique depth
    W = 0.34

    # (kind, length, channels, x, title, subtitle, shape)
    stages = [
        ("input", 45, 1,  0.2,  "Input", "flow features\n(standardised)", "45 × 1"),
        ("conv",  43, 32, 3.2,  "Conv1D", "32 filters · k = 3\nReLU", "43 × 32"),
        ("pool",  21, 32, 6.4,  "MaxPool1D", "pool = 2", "21 × 32"),
        ("conv",  19, 64, 8.9,  "Conv1D", "64 filters · k = 3\nReLU", "19 × 64"),
        ("pool",   9, 64, 12.2, "MaxPool1D", "pool = 2", "9 × 64"),
    ]
    blocks = []
    for kind, L, ch, x, title, sub, shape in stages:
        b = cuboid(ax, x, 0, W, H(L), D(ch), kind)
        blocks.append(b)
        cx = (b["x0"] + b["x1"]) / 2
        label(ax, cx, 3.35, title, size=10, weight="bold")
        label(ax, cx, 2.8, sub, size=8, color=MUTED)
        label(ax, cx, -2.15, shape, size=9, color=INK, weight="medium")

    # Receptive-field "kernel" windows + projection lines (conv layers)
    def kernel(src, dst, k_rows, frac_y=0.62):
        sx, sy, sw, sh = src["front"]
        ky = sy + sh * frac_y
        kh = sh * k_rows / 1.0
        ax.add_patch(Rectangle((sx, ky - kh / 2), sw, kh, fc="none", ec="#B91C1C", lw=1.2, zorder=5))
        dxs, dys, dws, dhs = dst["front"]
        tx, ty = dxs + dws * 0.0, dys + dhs * frac_y
        ax.add_patch(Rectangle((dxs + dws + dst["dx"] * 0.0, ty - 0.07), 0.0, 0.0, fc="none"))
        for sgn in (1, -1):
            ax.plot([sx + sw, dxs], [ky + sgn * kh / 2, ty + sgn * 0.12], color="#B91C1C", lw=0.7,
                    ls=(0, (3, 2)), zorder=1)
        ax.add_patch(Rectangle((dxs, ty - 0.12), dws, 0.24, fc="none", ec="#B91C1C", lw=1.0, zorder=5))

    kernel(blocks[0], blocks[1], 3 / 45)
    kernel(blocks[2], blocks[3], 3 / 21)

    # inter-block arrows
    for a, b in zip(blocks[:-1], blocks[1:]):
        arrow(ax, (a["x1"] + 0.12, 0), (b["x0"] - 0.12, 0), lw=1.2)

    # Flatten ------------------------------------------------------------
    fx = 15.2
    bar_h = 3.1
    ax.add_patch(Rectangle((fx, -bar_h / 2), 0.32, bar_h, fc=C["flat"][0], ec=C["flat"][1], lw=1.1, zorder=2))
    for yy in (-0.35, 0.0, 0.35):          # "…" break to signal not-to-scale
        ax.add_patch(Rectangle((fx - 0.02, yy - 0.05), 0.36, 0.10, fc="white", ec="none", zorder=3))
    label(ax, fx + 0.16, 3.35, "Flatten", size=10, weight="bold")
    label(ax, fx + 0.16, 2.8, "9 × 64", size=8, color=MUTED)
    label(ax, fx + 0.16, -2.15, "576", size=9, weight="medium")
    arrow(ax, (blocks[-1]["x1"] + 0.12, 0), (fx - 0.12, 0), lw=1.2)

    # Dense columns (neurons) ---------------------------------------------
    def neuron_col(x, n, kind, span=3.0, r=0.17, ell=True):
        ys = [span / 2 - i * span / (n - 1) for i in range(n)]
        pts = []
        for i, yy in enumerate(ys):
            if ell and i == n // 2:
                for k in (-0.18, 0, 0.18):
                    ax.add_patch(Circle((x, yy + k), 0.035, fc=INK, ec="none", zorder=4))
                pts.append(None)
                continue
            ax.add_patch(Circle((x, yy), r, fc=C[kind][0], ec=C[kind][1], lw=1.1, zorder=4))
            pts.append((x, yy))
        return [p for p in pts if p]

    dx_ = 17.9
    ox_ = 20.4
    dense = neuron_col(dx_, 9, "dense")
    out = neuron_col(ox_, 7, "out", span=2.5)
    flat_pts = [(fx + 0.32, yy) for yy in (1.3, 0.8, 0.3, -0.3, -0.8, -1.3)]
    for p in flat_pts:
        for q in dense:
            ax.plot([p[0], q[0]], [p[1], q[1]], color=GRID, lw=0.45, zorder=1)
    for p in dense:
        for q in out:
            ax.plot([p[0], q[0]], [p[1], q[1]], color=GRID, lw=0.45, zorder=1)

    label(ax, dx_, 3.35, "Dense", size=10, weight="bold")
    label(ax, dx_, 2.8, "128 units\nReLU", size=8, color=MUTED)
    label(ax, dx_, -2.15, "128", size=9, weight="medium")
    label(ax, ox_, 3.35, "Dense", size=10, weight="bold")
    label(ax, ox_, 2.8, "C units\nSoftmax", size=8, color=MUTED)
    label(ax, ox_, -2.15, "C = 2 / 6 / 19", size=9, weight="medium")
    label(ax, ox_ + 0.55, 0, "ŷ", size=13, style="italic", ha="left")

    # parameter counts (input dim = 45) -------------------------------------
    params = [(blocks[1], "128"), (blocks[3], "6,208")]
    for b, p in params:
        label(ax, (b["x0"] + b["x1"]) / 2, -2.65, f"{p} params", size=7.5, color=MUTED)
    label(ax, dx_, -2.65, "73,856 params", size=7.5, color=MUTED)
    label(ax, ox_, -2.65, "129·C − 1 params*", size=7.5, color=MUTED) if False else \
        label(ax, ox_, -2.65, "128·C + C params", size=7.5, color=MUTED)

    # stage brackets ---------------------------------------------------------
    def bracket(x0, x1, y, text):
        ax.plot([x0, x0, x1, x1], [y + 0.14, y, y, y + 0.14], color=INK, lw=1.0, zorder=3)
        label(ax, (x0 + x1) / 2, y - 0.38, text, size=9.5, weight="bold")

    bracket(0.0, 13.8, -3.35, "Hierarchical feature extraction")
    bracket(14.9, 21.2, -3.35, "Classification head")

    # legend --------------------------------------------------------------------
    lx = 0.0
    for kind, name in (("input", "Input"), ("conv", "Convolution + ReLU"), ("pool", "Max pooling"),
                       ("flat", "Flatten"), ("dense", "Fully connected + ReLU"), ("out", "Softmax output")):
        ax.add_patch(Rectangle((lx, -4.35), 0.32, 0.22, fc=C[kind][0], ec=C[kind][1], lw=1.0))
        label(ax, lx + 0.45, -4.24, name, size=8, ha="left")
        lx += 1.0 + 0.118 * len(name)
    ax.plot([lx + 0.1, lx + 0.4], [-4.24, -4.24], color="#B91C1C", lw=1.2)
    label(ax, lx + 0.55, -4.24, "Receptive field (k = 3)", size=8, ha="left")

    save(fig, "architecture")


# ==================================================== FIGURE 1 (v2): CNN ====
def fig_architecture_v2():
    plt.rcParams["mathtext.fontset"] = "dejavusans"
    fig, ax = plt.subplots(figsize=(16, 9.6))
    ax.set_xlim(-0.6, 24.6)
    ax.set_ylim(-9.4, 5.2)
    ax.set_aspect("equal")
    ax.axis("off")

    YC = 1.55
    H = lambda L: 0.35 + 0.05 * L
    W = 0.34

    def lighten(h, f):
        h = h.lstrip("#"); r, g, b = (int(h[i:i+2], 16) for i in (0, 2, 4))
        return "#%02x%02x%02x" % tuple(int(v + (255 - v) * f) for v in (r, g, b))

    def stack(x, n, h, kind, sx=0.11, sy=0.065):
        face, edge = C[kind]
        # soft ground shadow
        tw = W + (n - 1) * sx
        ax.add_patch(matplotlib.patches.Ellipse((x + tw / 2 + 0.1, YC - h / 2 - 0.22), tw + 0.5, 0.26,
                                                fc="#0F172A", ec="none", alpha=0.10, zorder=1))
        for i in reversed(range(n)):
            ox, oy = i * sx, i * sy
            f = lighten(face, 0.0 if i == 0 else 0.0)
            ax.add_patch(Rectangle((x + ox, YC - h / 2 + oy), W, h, fc=f, ec=edge, lw=0.9,
                                   alpha=0.97, zorder=2 + (n - i) * 0.01))
        # front-face highlight strip
        ax.add_patch(Rectangle((x, YC - h / 2), W, h, fc="none", ec=edge, lw=1.4, zorder=3))
        return dict(x0=x, x1=x + W + (n - 1) * sx, yb=YC - h / 2, yt=YC + h / 2 + (n - 1) * sy, h=h)

    def pill(x, y, text, kind, size=8.2):
        w = 0.098 * len(text) + 0.45
        ax.add_patch(FancyBboxPatch((x - w / 2, y - 0.2), w, 0.4, boxstyle="round,pad=0,rounding_size=0.2",
                                    fc="white", ec=C[kind][1], lw=1.1, zorder=7))
        label(ax, x, y, text, size=size, color=C[kind][1], weight="bold", z=8)

    def op_arrow(a, b, text, kind, sub=None):
        x0, x1 = a["x1"] + 0.18, b["x0"] - 0.18
        arrow(ax, (x0, YC), (x1, YC), lw=1.3, color=C[kind][1])
        pill((x0 + x1) / 2, YC, text, kind)
        if sub:
            label(ax, (x0 + x1) / 2, YC - 0.52, sub, size=7.4, color=MUTED)

    def dimline(b, text):
        xx = b["x0"] - 0.26
        ax.plot([xx, xx], [b["yb"] + 0.02, b["yb"] + b["h"] - 0.02], color=MUTED, lw=0.9, zorder=3)
        for yy in (b["yb"] + 0.02, b["yb"] + b["h"] - 0.02):
            ax.plot([xx - 0.07, xx + 0.07], [yy, yy], color=MUTED, lw=0.9, zorder=3)
        label(ax, xx - 0.22, YC, text, size=8, color=MUTED, ha="center")
        ax.texts[-1].set_rotation(90)

    # ---- tensors --------------------------------------------------------
    spec = [  # kind, L, sheets, x, tensor symbol, shape
        ("input", 45, 1,  0.7,  r"$\mathbf{x}$",   "45 × 1"),
        ("conv",  43, 8,  4.6,  r"$\mathbf{h}_1$", "43 × 32"),
        ("pool",  21, 8,  8.4,  r"$\mathbf{p}_1$", "21 × 32"),
        ("conv",  19, 12, 12.6, r"$\mathbf{h}_2$", "19 × 64"),
        ("pool",   9, 12, 16.2, r"$\mathbf{p}_2$", "9 × 64"),
    ]
    B = []
    for kind, L, n, x, sym, shp in spec:
        b = stack(x, n, H(L), kind)
        B.append(b)
        cx = (b["x0"] + b["x1"]) / 2
        label(ax, cx, 4.55, sym, size=13)
        label(ax, cx, -0.55, shp, size=9, weight="bold", color=INK)
    # channel annotations
    for b, t in ((B[1], "32 ch"), (B[2], "32 ch"), (B[3], "64 ch"), (B[4], "64 ch")):
        label(ax, b["x1"] + 0.05, b["yt"] + 0.28, t, size=7.4, color=MUTED, ha="center")

    # receptive-field windows on the front faces
    def rf(src, dst, L):
        kh = src["h"] * 3 / L
        sy = src["yb"] + src["h"] * 0.62
        ax.add_patch(Rectangle((src["x0"], sy - kh / 2), W, kh, fc="#FEE2E2", ec="#B91C1C", lw=1.1, zorder=5, alpha=0.9))
        ty = dst["yb"] + dst["h"] * 0.62
        ax.add_patch(Rectangle((dst["x0"], ty - 0.075), W, 0.15, fc="#FEE2E2", ec="#B91C1C", lw=1.1, zorder=5, alpha=0.9))
        for sg in (1, -1):
            ax.plot([src["x0"] + W, dst["x0"]], [sy + sg * kh / 2, ty + sg * 0.075], color="#B91C1C", lw=0.7,
                    ls=(0, (3, 2)), zorder=1)
    rf(B[0], B[1], 45)
    rf(B[2], B[3], 21)

    op_arrow(B[0], B[1], "Conv1D + ReLU", "conv", "32 filters · k = 3")
    op_arrow(B[1], B[2], "MaxPool", "pool", "size 2")
    op_arrow(B[2], B[3], "Conv1D + ReLU", "conv", "64 filters · k = 3")
    op_arrow(B[3], B[4], "MaxPool", "pool", "size 2")

    # ---- head -----------------------------------------------------------------
    fx = 19.3
    bar_h = 3.0
    ax.add_patch(matplotlib.patches.Ellipse((fx + 0.16, YC - bar_h / 2 - 0.22), 0.9, 0.24, fc="#0F172A", ec="none", alpha=0.10))
    ax.add_patch(Rectangle((fx, YC - bar_h / 2), 0.32, bar_h, fc=C["flat"][0], ec=C["flat"][1], lw=1.4, zorder=3))
    for yy in (-0.28, 0.0, 0.28):
        ax.add_patch(Rectangle((fx - 0.03, YC + yy - 0.045), 0.38, 0.09, fc="white", ec="none", zorder=4))
    label(ax, fx + 0.16, 4.55, r"$\mathbf{z}$", size=13)
    label(ax, fx + 0.16, -0.55, "576", size=9, weight="bold")
    arrow(ax, (B[4]["x1"] + 0.18, YC), (fx - 0.15, YC), lw=1.3, color=C["flat"][1])
    pill((B[4]["x1"] + fx) / 2, YC, "Flatten", "flat")

    def neurons(x, n, kind, span, r=0.17):
        ys = [YC + span / 2 - i * span / (n - 1) for i in range(n)]
        pts = []
        for i, yy in enumerate(ys):
            if i == n // 2:
                for k in (-0.16, 0, 0.16):
                    ax.add_patch(Circle((x, yy + k), 0.035, fc=INK, ec="none", zorder=5))
                continue
            ax.add_patch(Circle((x, yy), r, fc=C[kind][0], ec=C[kind][1], lw=1.2, zorder=5))
            pts.append((x, yy))
        return pts
    dxn, oxn = 21.5, 23.5
    dense = neurons(dxn, 9, "dense", 3.0)
    out = neurons(oxn, 7, "out", 2.4)
    for p in [(fx + 0.32, YC + k) for k in (1.2, 0.7, 0.25, -0.25, -0.7, -1.2)]:
        for q in dense:
            ax.plot([p[0], q[0]], [p[1], q[1]], color=GRID, lw=0.4, zorder=1)
    for p in dense:
        for q in out:
            ax.plot([p[0], q[0]], [p[1], q[1]], color=GRID, lw=0.4, zorder=1)
    label(ax, dxn, 4.55, r"$\mathbf{a}$", size=13)
    label(ax, oxn, 4.55, r"$\hat{\mathbf{y}}$", size=13)
    label(ax, dxn, 3.85, "Dense + ReLU", size=8, color=C["dense"][1], weight="bold")
    label(ax, oxn, 3.85, "Dense + Softmax", size=8, color=C["out"][1], weight="bold")
    label(ax, dxn, -0.55, "128", size=9, weight="bold")
    label(ax, oxn, -0.55, "C", size=9, weight="bold")

    # params row
    for xc, t in (((B[1]["x0"] + B[1]["x1"]) / 2, "128"), ((B[3]["x0"] + B[3]["x1"]) / 2, "6,208"),
                  (dxn, "73,856"), (oxn, "128·C + C")):
        label(ax, xc, -1.05, f"{t} params", size=7.6, color=MUTED)

    # stage brackets
    def bracket(x0, x1, y, text):
        ax.plot([x0, x0, x1, x1], [y + 0.13, y, y, y + 0.13], color=INK, lw=0.9, zorder=3)
        label(ax, (x0 + x1) / 2, y - 0.33, text, size=9.5, weight="bold")
    bracket(0.4, 17.9, -1.55, "Hierarchical feature extraction")
    bracket(18.9, 24.2, -1.55, "Classification head")

    label(ax, -0.5, 5.0, "(a)", size=12, weight="bold", ha="left")
    label(ax, 0.2, 5.0, "CNN architecture", size=11, weight="bold", ha="left")
    label(ax, 24.5, 5.0, "block heights not to scale", size=7.2, color=MUTED, ha="right", style="italic")

    # ================= lower panels =========================================
    def panel(x0, w, title, tag):
        ax.add_patch(FancyBboxPatch((x0, -9.15), w, 6.3, boxstyle="round,pad=0,rounding_size=0.25",
                                    fc="#F8FAFC", ec="#CBD5E1", lw=1.0, zorder=0))
        label(ax, x0 + 0.3, -3.2, tag, size=11, weight="bold", ha="left")
        label(ax, x0 + 1.0, -3.2, title, size=10.5, weight="bold", ha="left")

    def cells(xc, y, vals, kind, hl=(), size=0.62, fmt="{:.2f}", fc_hl=None):
        n = len(vals); x0 = xc - n * size / 2
        face, edge = C[kind]
        for i, v in enumerate(vals):
            f = (fc_hl or face) if i in hl else "white"
            ax.add_patch(Rectangle((x0 + i * size, y), size, size, fc=f, ec=edge, lw=1.0, zorder=3))
            t = ("0" if v == 0 else fmt.format(v).replace("0.", ".", 1) if abs(v) < 1 else fmt.format(v))
            label(ax, x0 + i * size + size / 2, y + size / 2, t, size=7.6, z=6)
        return x0, size

    pw, gap, px = 7.7, 0.55, 0.0
    panel(px, pw, "1-D convolution  (k = 3)", "(b)")
    panel(px + pw + gap, pw, "Max pooling  (size 2)", "(c)")
    panel(px + 2 * (pw + gap), pw, "Prediction head", "(d)")

    # (b) convolution
    cx = px + pw / 2
    xin = [0.30, -0.20, 0.80, 0.50, -0.60, 0.10, 0.40]
    hout = [0.35, 0.95, 0.60, 0.00, 0.00]
    x0i, sz = cells(cx, -4.7, xin, "input")
    label(ax, x0i - 0.15, -4.7 + 0.31, "x", size=11, color=MUTED, ha="right")
    ax.add_patch(Rectangle((x0i + 1 * sz, -4.7), 3 * sz, sz, fc="none", ec="#B91C1C", lw=1.8, zorder=7))
    label(ax, x0i + 2.5 * sz, -3.95, r"kernel $w=[.5,\,1,\,.5]$", size=7.6, color="#B91C1C")
    label(ax, cx, -6.55 + 0.9, "output  h", size=8, color=MUTED) if False else None
    x0o, _ = cells(cx, -6.15, hout, "conv", hl=(1,), fc_hl="#BFDBFE")
    for sg, xs in ((0, x0i + 1 * sz), (1, x0i + 4 * sz)):
        xo = x0o + 1 * sz + sg * sz
        ax.plot([xs, xo], [-4.7, -5.53], color="#B91C1C", lw=0.8, ls=(0, (3, 2)), zorder=2)
    label(ax, x0o - 0.15, -6.15 + 0.31, r"$h$", size=11, color=MUTED, ha="right")
    label(ax, cx, -7.75, r"$h_i=\mathrm{ReLU}\!\left(\sum_{k=1}^{3} w_k\,x_{i+k-1}+b\right)$", size=9.5)
    label(ax, cx, -8.5, "slides along the 45 features, sharing weights", size=7.8, color=MUTED, style="italic")

    # (c) pooling
    cx2 = px + pw + gap + pw / 2
    hin = [0.35, 0.95, 0.60, 0.00, 0.20, 0.40]
    x0p, sz = cells(cx2, -4.7, hin, "pool", hl=(1, 2, 5), fc_hl="#FEF3C7")
    label(ax, x0p - 0.15, -4.7 + 0.31, r"$h$", size=11, color=MUTED, ha="right")
    for k in range(3):
        ax.add_patch(Rectangle((x0p + 2 * k * sz, -4.7), 2 * sz, sz, fc="none", ec=C["pool"][1], lw=1.8, ls=(0, (3, 1.5)), zorder=7))
    pout = [0.95, 0.60, 0.40]
    for k, v in enumerate(pout):
        xc_ = x0p + (2 * k + 1) * sz
        ax.add_patch(Rectangle((xc_ - sz / 2, -6.15), sz, sz, fc="#FDE68A", ec=C["pool"][1], lw=1.0, zorder=3))
        label(ax, xc_, -6.15 + sz / 2, ("%.2f" % v).replace("0.", ".", 1), size=7.6, z=6)
        ax.plot([xc_, xc_], [-4.7, -6.15 + sz], color=C["pool"][1], lw=0.8, ls=(0, (3, 2)), zorder=2)
    label(ax, x0p - 0.15, -6.15 + 0.31, r"$p$", size=11, color=MUTED, ha="right")
    label(ax, cx2, -7.75, r"$p_i=\max\!\left(h_{2i},\,h_{2i+1}\right)$", size=9.5)
    label(ax, cx2, -8.5, "halves the length, keeps the strongest response", size=7.8, color=MUTED, style="italic")

    # (d) head
    cx3 = px + 2 * (pw + gap) + pw / 2
    label(ax, cx3, -4.3, r"$\hat{\mathbf{y}}=\mathrm{softmax}\!\left(W_2\,\mathrm{ReLU}(W_1\mathbf{z}+\mathbf{b}_1)+\mathbf{b}_2\right)$", size=9.5)
    chips = [("C = 2", "Benign / Attack"), ("C = 6", "attack families"), ("C = 19", "attack types")]
    cw = 2.25
    x0c = cx3 - 1.5 * cw - 0.15
    for i, (a, b) in enumerate(chips):
        xx = x0c + i * (cw + 0.15)
        ax.add_patch(FancyBboxPatch((xx, -6.2), cw, 1.2, boxstyle="round,pad=0,rounding_size=0.15",
                                    fc=C["out"][0], ec=C["out"][1], lw=1.1, zorder=3))
        label(ax, xx + cw / 2, -5.45, a, size=9.5, weight="bold", color=C["out"][1])
        label(ax, xx + cw / 2, -5.85, b, size=7.4, color=INK)
    label(ax, cx3, -6.85, "Optimiser: Adam   ·   Loss: categorical cross-entropy", size=8.2, color=INK)
    label(ax, cx3, -7.4, "10 epochs   ·   batch size 32", size=8.2, color=INK)
    label(ax, cx3, -8.5, "one network, three label granularities", size=7.8, color=MUTED, style="italic")

    save(fig, "architecture")


# ======================================================== FIGURE 2: PIPELINE ==
def fig_pipeline():
    fig, ax = plt.subplots(figsize=(15.5, 4.3))
    ax.set_xlim(0, 31)
    ax.set_ylim(-4.2, 3.3)
    ax.set_aspect("equal")
    ax.axis("off")

    boxes = [
        ("data", "CICIoMT2024", "CSV flow records\ntrain/  ·  test/", 0.2),
        ("data", "Label mapping", "file name → class\n2 · 6 · 19-way", 5.4),
        ("data", "Train / val split", "80 / 20 random\nseed = 42", 10.6),
        ("data", "Standardisation", "StandardScaler\nfit on train only", 15.8),
        ("data", "Reshape", "(N, 45) → (N, 45, 1)", 21.0),
    ]
    bw, bh = 4.3, 2.4
    for i, (k, t, s, x) in enumerate(boxes):
        rbox(ax, x, -bh / 2, bw, bh, k)
        label(ax, x + bw / 2, 0.45, t, size=10.5, weight="bold")
        label(ax, x + bw / 2, -0.45, s, size=8.5, color=MUTED)
        ax.add_patch(Circle((x + 0.5, bh / 2 - 0.0), 0.32, fc="white", ec=C[k][1], lw=1.1, zorder=5))
        label(ax, x + 0.5, bh / 2, str(i + 1), size=9, weight="bold")
        if i < len(boxes) - 1:
            arrow(ax, (x + bw + 0.1, 0), (boxes[i + 1][3] - 0.1, 0), lw=1.4)

    # CNN block
    x = 26.2
    rbox(ax, x, -bh / 2 - 0.35, 4.6, bh + 0.7, "conv", lw=1.6)
    label(ax, x + 2.3, 0.75, "1-D CNN", size=11, weight="bold")
    mini = [("conv", 0.25, 0.9), ("pool", 0.25, 0.55), ("conv", 0.25, 0.7), ("pool", 0.25, 0.4)]
    mx = x + 0.85
    for k, w, h in mini:
        ax.add_patch(Rectangle((mx, -0.55 - h / 2 + 0.3), w, h, fc=C[k][0], ec=C[k][1], lw=1.0, zorder=3))
        mx += 0.5
    ax.add_patch(Rectangle((mx, -0.55 + 0.3 - 0.5), 0.2, 1.0, fc=C["flat"][0], ec=C["flat"][1], lw=1.0, zorder=3))
    mx += 0.45
    for _ in range(2):
        ax.add_patch(Circle((mx, -0.25), 0.1, fc=C["dense"][0], ec=C["dense"][1], lw=0.9, zorder=3))
        ax.add_patch(Circle((mx, 0.08), 0.1, fc=C["dense"][0], ec=C["dense"][1], lw=0.9, zorder=3))
        mx += 0.4
    label(ax, x + 2.3, -1.15, "Adam · cat. cross-entropy\n10 epochs · batch 32", size=7.8, color=MUTED)
    ax.add_patch(Circle((x + 0.5, bh / 2 + 0.35), 0.32, fc="white", ec=C["conv"][1], lw=1.1, zorder=5))
    label(ax, x + 0.5, bh / 2 + 0.35, "6", size=9, weight="bold")
    arrow(ax, (21.0 + bw + 0.1, 0), (x - 0.1, 0), lw=1.4)

    # outputs (below, fan-out)
    label(ax, 28.5, -2.55, "Softmax over C classes", size=9, weight="bold")
    arrow(ax, (28.5, -bh / 2 - 0.45), (28.5, -2.2), lw=1.3)
    for xx, t in ((25.3, "C = 2\nBenign / Attack"), (28.5, "C = 6\nattack families"), (31.0 - 0.2, "C = 19\nattack types")):
        pass
    label(ax, 28.5, -3.35, "C = 2  ·  C = 6  ·  C = 19", size=9, color=C["out"][1], weight="bold")

    save(fig, "pipeline")


# ====================================================== FIGURE 3: TAXONOMY ==
def fig_taxonomy():
    fig, ax = plt.subplots(figsize=(13.5, 8.6))
    ax.set_xlim(0, 27)
    ax.set_ylim(-0.6, 17.6)
    ax.set_aspect("equal")
    ax.axis("off")

    # families: (family(6-class), [leaf names (19-class)])
    fam = [
        ("Benign",   ["Benign"]),
        ("Spoofing", ["ARP Spoofing"]),
        ("MQTT",     ["DDoS · Connect Flood", "DDoS · Publish Flood", "DoS · Connect Flood",
                      "DoS · Publish Flood", "Malformed Data"]),
        ("Recon",    ["OS Scan", "Ping Sweep", "Port Scan", "Vulnerability Scan"]),
        ("DDoS",     ["ICMP", "SYN", "TCP", "UDP"]),
        ("DoS",      ["ICMP", "SYN", "TCP", "UDP"]),
    ]
    row_h = 0.78
    n_leaf = sum(len(l) for _, l in fam)
    gap = 0.38
    total = n_leaf * row_h + (len(fam) - 1) * gap
    y = total + 0.4

    leaf_x, leaf_w = 18.2, 8.2
    fam_x, fam_w = 9.6, 5.6
    root_x, root_w = 0.3, 5.0
    ycent = {}
    fam_pos = []
    for fname, leaves in fam:
        ys = []
        for lf in leaves:
            y -= row_h
            ys.append(y + row_h / 2)
            kind = "out" if fname != "Benign" else "dense"
            rbox(ax, leaf_x, y + 0.08, leaf_w, row_h - 0.16, kind, lw=1.0, r=0.1)
            label(ax, leaf_x + leaf_w / 2, y + row_h / 2, lf, size=9)
        fam_pos.append((fname, sum(ys) / len(ys), ys))
        y -= gap

    # family nodes
    for fname, yc, ys in fam_pos:
        kind = "dense" if fname == "Benign" else "pool" if fname in ("Spoofing", "MQTT", "Recon") else "out"
        kind = "dense" if fname == "Benign" else "conv"
        rbox(ax, fam_x, yc - 0.42, fam_w, 0.84, kind, lw=1.2, r=0.12)
        label(ax, fam_x + fam_w / 2, yc, fname, size=10, weight="bold")
        for yy in ys:
            ax.plot([fam_x + fam_w, leaf_x], [yc, yy], color=MUTED, lw=0.9, zorder=1)

    # root nodes: binary
    yb = [p[1] for p in fam_pos if p[0] == "Benign"][0]
    atk = [p[1] for p in fam_pos if p[0] != "Benign"]
    ya = sum(atk) / len(atk)
    for t, yc, kind in (("Benign", yb, "dense"), ("Attack", ya, "out")):
        rbox(ax, root_x, yc - 0.42, root_w, 0.84, kind, lw=1.2, r=0.12)
        label(ax, root_x + root_w / 2, yc, t, size=10, weight="bold")
    for fname, yc, _ in fam_pos:
        src = yb if fname == "Benign" else ya
        ax.plot([root_x + root_w, fam_x], [src, yc], color=MUTED, lw=0.9, zorder=1)

    # column headers
    top = total + 1.15
    for xc, w, t, s in ((root_x + root_w / 2, root_w, "Binary", "C = 2"),
                        (fam_x + fam_w / 2, fam_w, "Categorical", "C = 6"),
                        (leaf_x + leaf_w / 2, leaf_w, "Multiclass", "C = 19")):
        label(ax, xc, top + 0.55, t, size=12, weight="bold")
        label(ax, xc, top - 0.1, s, size=9.5, color=MUTED)
        ax.plot([xc - w / 2, xc + w / 2], [top - 0.5, top - 0.5], color=INK, lw=1.0)
    ax.set_ylim(-0.6, top + 1.4)

    save(fig, "label_taxonomy")


if __name__ == "__main__":
    fig_architecture_v2()
    fig_pipeline()
    fig_taxonomy()
    print("figures written to", OUT)
