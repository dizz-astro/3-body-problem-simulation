import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from PIL import Image
from glob import glob

from astropy.time import Time
from astroquery.jplhorizons import Horizons


# Conver .aei to csv file
def aei2csv(aeipath:str) -> None:
    with open(aeipath) as file:
        lines = file.readlines()

    csvfile = open(aeipath.replace(".aei", ".csv"), "w")

    for i, line in enumerate(lines):
        line = line.strip()
        while "  " in line:
            line = line.replace("  ", " ")
        
        line = line.replace("Time (years)", "Time")
        line = line.replace(" ", ",")
        
        if len(line) > 0 and i > 2:
            csvfile.write(line+"\n")

    print(aeipath.replace(".aei", ".csv"), "was successfully generated!")

    return None
            
aei2csv("./ALPHA.aei")
aei2csv("./BETA.aei")

ALPHA = pd.read_csv("./ALPHA.csv")
BETA = pd.read_csv("./BETA.csv")

fig, ax = plt.subplots(1, 2, figsize=(10, 5))

limit = 110

# =========================
# ORBIT TRAILS
# =========================

# XY plane
ax[0].plot(
    ALPHA["x"].to_numpy(),
    ALPHA["y"].to_numpy(),
    color='green',
    alpha=0.6,
    linewidth=1.5,
    label="ALPHA"
)

ax[0].plot(
    BETA["x"].to_numpy(),
    BETA["y"].to_numpy(),
    color='red',
    alpha=0.6,
    linewidth=1.5,
    label="BETA"
)

# XZ plane
ax[1].plot(
    ALPHA["x"].to_numpy(),
    ALPHA["z"].to_numpy(),
    color='green',
    alpha=0.6,
    linewidth=1.5,
    label="ALPHA"
)

ax[1].plot(
    BETA["x"].to_numpy(),
    BETA["z"].to_numpy(),
    color='red',
    alpha=0.6,
    linewidth=1.5,
    label="BETA"
)

# =========================
# CURRENT POSITIONS
# =========================

# ALPHA current position
ax[0].scatter(
    ALPHA["x"].iloc[-1],
    ALPHA["y"].iloc[-1],
    color='green',
    s=80
)

ax[1].scatter(
    ALPHA["x"].iloc[-1],
    ALPHA["z"].iloc[-1],
    color='green',
    s=80
)

# BETA current position
ax[0].scatter(
    BETA["x"].iloc[-1],
    BETA["y"].iloc[-1],
    color='red',
    s=80
)

ax[1].scatter(
    BETA["x"].iloc[-1],
    BETA["z"].iloc[-1],
    color='red',
    s=80
)

# =========================
# SUN
# =========================

ax[0].scatter(
    0, 0,
    color='yellow',
    s=250,
    edgecolors='orange',
    label="SUN"
)

ax[1].scatter(
    0, 0,
    color='yellow',
    s=250,
    edgecolors='orange',
    label="SUN"
)

# =========================
# AXES
# =========================

ax[0].set_xlim(-limit, limit)
ax[0].set_ylim(-limit, limit)

ax[1].set_xlim(-limit, limit)
ax[1].set_ylim(-limit, limit)

ax[0].set_xlabel(r"$x_{\text{ICRF}}$ [au]")
ax[0].set_ylabel(r"$y_{\text{ICRF}}$ [au]")

ax[1].set_xlabel(r"$x_{\text{ICRF}}$ [au]")
ax[1].set_ylabel(r"$z_{\text{ICRF}}$ [au]")

ax[0].set_title("Top View (x-y)")
ax[1].set_title("Side View (x-z)")

ax[0].grid()
ax[1].grid()

ax[1].legend()

# =========================
# SAVE
# =========================

plt.savefig(
    "2D_3body_plot.png",
    dpi=300,
    bbox_inches='tight'
)

plt.show()

print("2D_3body_plot.png was created!")



