from sys import exit
from functions import *
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from datetime import date, datetime, timedelta


class CosmicObject:
    def __init__(self, name: str, rad: int, color: str, r: list, v: list) -> None:
        self.name = name
        self.r = np.array(r, dtype=np.float64)  # wektory promienia odległości od Słońca
        self.v = np.array(v, dtype=np.float64)  # wektory prędkości względem Słońca
        self.xs = []  # kolejne pozycje X
        self.ys = []  # kolejne pozycje Y
        self.plot = ax.scatter(
            r[0], r[1], color=color, s=rad ** 2, edgecolors=None, zorder=10
        )
        (self.line,) = ax.plot([], [], color=color, linewidth=1.4)


class SolarSystem:
    def __init__(self):
        self.planets = []
        self.time = None
        self.timestamp = ax.text(
            0.03, 0.94, "Data: ", color="w", transform=ax.transAxes,
            fontsize="x-large"
        )

    def add_planet(self, planet):
        self.planets.append(planet)

    def evolve(self):
        """Obliczamy kolejne punkty trajektorii"""
        dt = 1
        self.time += timedelta(dt)
        plots = []
        lines = []
        for i, planet in enumerate(self.planets):
            # obliczamy kolejne wektory promienia
            planet.r += planet.v * dt
            acc = -2.959e-4 * planet.r / np.sum(planet.r ** 2) ** (3/2)
            planet.v += acc * dt
            planet.xs.append(planet.r[0])
            planet.ys.append(planet.r[1])
            planet.plot.set_offsets(planet.r[:2])
            plots.append(planet.plot)
            planet.line.set_xdata(planet.xs)
            planet.line_set_ydata(planet.ys)
            lines.append(planet.line)

        if len(planet.xs) > 10000:
            raise SystemExit("Aby zapobiec przepełnieniu pamięci RAM.")
        self.timestamp.set_text(f"Data: {self.time.isoformat()}")
        return plots + lines + [self.timestamp]


load_module_ok = True

try:
    import numpy as np
    ok_module_info("numpy")
except ImportError:
    error_module_info("numpy")
    load_module_ok = False

try:
    import matplotlib
    ok_module_info("matplotlib")
except ImportError:
    error_module_info("matplotlib")
    load_module_ok = False

try:
    from astropy.time import Time
    ok_module_info("astropy")
except ImportError:
    error_module_info("astropy")
    load_module_ok = False

try:
    from astroquery.jplhorizons import Horizons
    ok_module_info("astroquery")
except ImportError:
    error_module_info("astroquery")
    load_module_ok = False

if not load_module_ok:
    print("Niestety wystąpiły błędy.")
    print("Nie mogę dalej działać.")
    exit(0)

print("Super! Możemy działać.")


nasaids = [1, 2, 3, 4]  # numery ID w bazie danych NASA
names = ["Merkury", "Venus", "Ziemia", "Mars"]
colors = ["grey", "orange", "green", "chocolate"]
sizes = [0.38, 0.95, 1.0, 0.53]
texty = [0.47, 0.73, 1, 1.5]
planet_datas = get_horizon_data(nasaids, names, colors, sizes)

plt.style.use("dark_background")
fig = plt.figure(
    "Układ Słoneczny", figsize=[8, 8]
)
ax = plt.axes([0.0, 0.0, 1.0, 1.0], xlim=(-1.8, 1.8), ylim=(-1.8, 1.8))


CosmicObject ("Słońce", 28, "yellow", [0, 0, 0], [0, 0, 0])
solar_system = SolarSystem()
solar_system.time = datetime.strptime("2018-01-01", "%Y-%m-%d").date()

# Generujemy dane do animacji
for nasaid in nasaids:
    planet = planet_datas[nasaid]

    # dodajemy planetę do Układu Słonecznego
    solar_system.add_planet(
        CosmicObject (
            planet["name"],
            planet["size"] * 20,
            planet["color"],
            planet["r"],
            planet["v"],
        )
    )
    # dodajemy do okna animacji nazwę planety
    ax.text(
        0,
        -(texty[nasaid - 1] + 0.1),
        planet["name"],
        color=planet["color"],
        zorder=1000,
        ha="center",
        fontsize="large",
    )

def animate(i):
    return solar_system.evolve()

solar_animation = animation.FuncAnimation(
    fig,
    animate,
    repeat=False,
    frames=365,
    blit=True,
    interval=10,
)

plt.show()