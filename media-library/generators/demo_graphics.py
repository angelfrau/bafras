"""Gráficos demostrativos generados con datos sintéticos (E01, E07, D06).
Todos llevan un sello visible: no representan resultados de ninguna instalación real."""
import numpy as np, io, os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from PIL import Image

for f in fm.findSystemFonts():
    if "Inter" in f:
        fm.fontManager.addfont(f)
plt.rcParams.update({"font.family": "Inter", "font.size": 13, "axes.edgecolor": "#9aa59f",
                     "axes.labelcolor": "#27332c", "xtick.color": "#4b5a51", "ytick.color": "#4b5a51",
                     "axes.spines.top": False, "axes.spines.right": False})
G1, G2, G3, AC, GR = "#0f3d2e", "#2f7a55", "#8cc5a3", "#c98b2b", "#e9eeea"
STAMP = "DATOS SINTÉTICOS · GRÁFICO DEMOSTRATIVO · No corresponde a ninguna instalación real"
OUT = "/home/claude/bafras/pkg/BAFRAS_Website_Visual_Assets_V1/assets/images/"
rng = np.random.default_rng(42)
h = np.arange(0, 24, 0.25)


def demand(day_scale=1.0):
    base = 120 + 40 * np.exp(-((h - 8.5) / 1.6) ** 2) + 90 * np.exp(-((h - 13.5) / 3.2) ** 2) \
        + 55 * np.exp(-((h - 20.5) / 1.8) ** 2)
    return day_scale * base + rng.normal(0, 4, h.size)


def pv():
    return np.clip(260 * np.exp(-((h - 13.2) / 2.9) ** 2) - 12, 0, None) * (1 + rng.normal(0, 0.02, h.size))


def save(fig, path):
    fig.text(0.5, 0.012, STAMP, ha="center", va="bottom", fontsize=11, color="#7a2e0e",
             bbox=dict(boxstyle="round,pad=0.35", fc="#fff4e5", ec="#c98b2b", lw=1))
    buf = io.BytesIO(); fig.savefig(buf, dpi=100, format="png", facecolor="white"); plt.close(fig)
    im = Image.open(buf).convert("RGB").resize((1600, 1200), Image.LANCZOS)
    os.makedirs(os.path.dirname(OUT + path), exist_ok=True)
    im.save(OUT + path, "WEBP", quality=88, method=6)
    print(path, os.path.getsize(OUT + path))


# E01 — curva de carga y balance
d, p = demand(), pv()
fig, ax = plt.subplots(figsize=(16, 12))
fig.subplots_adjust(left=0.08, right=0.97, top=0.86, bottom=0.12)
ax.fill_between(h, 0, d, color=G3, alpha=0.45, label="Demanda del edificio")
ax.plot(h, d, color=G1, lw=2.4)
ax.fill_between(h, 0, np.minimum(d, p), color=AC, alpha=0.55, label="Generación FV autoconsumida")
ax.plot(h, p, color=AC, lw=2, ls="--", label="Generación FV disponible")
ax.fill_between(h, d, p, where=p > d, color="#e8c37e", alpha=0.6, label="Excedente (almacenable / exportable)")
ax.set_xlim(0, 24); ax.set_xticks(range(0, 25, 2)); ax.set_xticklabels([f"{x:02d}:00" for x in range(0, 25, 2)])
ax.set_ylabel("Potencia (kW)"); ax.set_xlabel("Hora del día (resolución cuartohoraria)")
ax.grid(axis="y", color=GR); ax.legend(loc="upper left", frameon=False, fontsize=13)
fig.text(0.08, 0.93, "Perfil de demanda y balance energético diario", fontsize=26, weight="bold", color=G1)
fig.text(0.08, 0.895, "Ejemplo ilustrativo de caracterización de consumos: curva de carga, generación y excedentes",
         fontsize=14, color="#4b5a51")
save(fig, "capabilities/energy/analysis/energy-demand-analysis.webp")

# E07 — dashboard de gestión energética
fig = plt.figure(figsize=(16, 12)); fig.patch.set_facecolor("white")
fig.text(0.04, 0.95, "Panel de gestión energética — DEMO", fontsize=24, weight="bold", color=G1)
fig.text(0.04, 0.925, "Interfaz de ejemplo generada para la web · valores ficticios", fontsize=13, color="#4b5a51")
kpis = [("Consumo hoy", "3.412 kWh"), ("Autoconsumo FV", "61 %"), ("Potencia máx.", "287 kW"), ("Estado batería", "74 %")]
for i, (k, v) in enumerate(kpis):
    a = fig.add_axes([0.04 + i * 0.235, 0.78, 0.215, 0.11]); a.set_axis_off()
    a.add_patch(plt.Rectangle((0, 0), 1, 1, fc=GR, ec="none", transform=a.transAxes))
    a.text(0.06, 0.66, k, fontsize=13, color="#4b5a51", transform=a.transAxes)
    a.text(0.06, 0.2, v, fontsize=26, weight="bold", color=G1, transform=a.transAxes)
a1 = fig.add_axes([0.06, 0.42, 0.9, 0.3])
d2, p2 = demand(), pv(); grid = np.clip(d2 - p2, 0, None)
a1.stackplot(h, np.minimum(d2, p2), grid, colors=[AC, G2], alpha=0.8, labels=["FV", "Red"])
a1.plot(h, d2, color=G1, lw=1.8, label="Demanda")
a1.set_xlim(0, 24); a1.set_xticks(range(0, 25, 3)); a1.set_xticklabels([f"{x:02d}h" for x in range(0, 25, 3)])
a1.set_ylabel("kW"); a1.grid(axis="y", color=GR); a1.legend(loc="upper left", ncol=3, frameon=False)
a1.set_title("Potencia por origen (día en curso)", loc="left", fontsize=15, color=G1)
a2 = fig.add_axes([0.13, 0.1, 0.36, 0.24])
uses = ["Climatización", "ACS", "Iluminación", "Cocinas", "Otros"]; vals = [38, 21, 14, 17, 10]
a2.barh(uses[::-1], vals[::-1], color=[G3, G3, G2, G2, G1][::-1]); a2.set_xlabel("% del consumo")
a2.set_title("Desglose por usos", loc="left", fontsize=15, color=G1); a2.grid(axis="x", color=GR)
a3 = fig.add_axes([0.56, 0.1, 0.4, 0.24])
days = np.arange(1, 31); kwh = 3200 + 300 * np.sin(days / 4) + rng.normal(0, 90, 30)
a3.bar(days, kwh, color=G2); a3.axhline(kwh.mean(), color=AC, lw=2, ls="--")
a3.set_title("Energía diaria (mes)", loc="left", fontsize=15, color=G1); a3.set_ylabel("kWh"); a3.grid(axis="y", color=GR)
save(fig, "capabilities/energy/management/energy-management-dashboard.webp")

# D06 — análisis de datos operativos: tendencias y alarmas
t = np.arange(0, 7 * 24, 0.25)
tsup = 7 + 0.6 * np.sin(t / 24 * 2 * np.pi) + rng.normal(0, 0.12, t.size)
tsup[(t > 70) & (t < 79)] += np.linspace(0, 3.2, ((t > 70) & (t < 79)).sum())
cop = 3.6 - 0.25 * (tsup - 7) + rng.normal(0, 0.06, t.size)
fig, (b1, b2) = plt.subplots(2, 1, figsize=(16, 12), sharex=True)
fig.subplots_adjust(left=0.08, right=0.97, top=0.86, bottom=0.12, hspace=0.12)
b1.plot(t, tsup, color=G2, lw=1.4, label="T impulsión agua fría (°C)")
b1.axhline(9, color="#b4432b", lw=1.5, ls="--", label="Umbral de alarma")
al = tsup > 9; b1.fill_between(t, 5, 11, where=al, color="#f2c4b8", alpha=0.6, label="Alarma activa")
b1.set_ylim(5, 11); b1.legend(loc="upper right", frameon=False); b1.grid(color=GR); b1.set_ylabel("°C")
b2.plot(t, cop, color=G1, lw=1.4, label="COP instantáneo enfriadora")
b2.plot(t, np.convolve(np.pad(cop, 48, mode="edge"), np.ones(96) / 96, mode="same")[48:-48], color=AC, lw=2.4, label="Media móvil 24 h")
b2.legend(loc="lower right", frameon=False); b2.grid(color=GR); b2.set_ylabel("COP")
b2.set_xticks(range(0, 7 * 24 + 1, 24)); b2.set_xticklabels(["Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom", ""])
fig.text(0.08, 0.93, "Tendencias, alarmas e indicadores de funcionamiento", fontsize=26, weight="bold", color=G1)
fig.text(0.08, 0.895, "Ejemplo ilustrativo: detección de desviaciones en una producción de frío a partir de datos de supervisión",
         fontsize=14, color="#4b5a51")
save(fig, "capabilities/digital/data/digital-data-analysis.webp")
