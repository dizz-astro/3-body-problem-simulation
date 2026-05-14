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

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# 1. Plot the SUN at the origin
ax.scatter(0, 0, 0, color='yellow', s=200, edgecolors='orange', label="SUN")

# 2. Plot the paths of ALPHA and BETA
ax.plot(ALPHA["x"], ALPHA["y"], ALPHA["z"], color='green', label="ALPHA", linewidth=1, alpha=0.7)
ax.plot(BETA["x"], BETA["y"], BETA["z"], color='red', label="BETA", linewidth=1, alpha=0.7)

# 3. Plot their current/final positions as points
ax.scatter(ALPHA["x"].iloc[-1], ALPHA["y"].iloc[-1], ALPHA["z"].iloc[-1], color='green', s=50)
ax.scatter(BETA["x"].iloc[-1], BETA["y"].iloc[-1], BETA["z"].iloc[-1], color='red', s=50)

# Set axis limits
limit = 110
ax.set_xlim(limit, -limit)
ax.set_ylim(limit, -limit)
ax.set_zlim(-limit, limit)

# Labels
ax.set_xlabel('X [AU]')
ax.set_ylabel('Y [AU]')
ax.set_zlabel('Z [AU]')
ax.set_title('3-Body Stellar Dynamics (3D View)')

ax.legend()

# Optional: Set the initial viewing angle
ax.view_init(elev=20, azim=45)

plt.show()
plt.savefig("3D_3body_plot.png", dpi=300, bbox_inches='tight')
print("3D_3body_plot.png was created!")
