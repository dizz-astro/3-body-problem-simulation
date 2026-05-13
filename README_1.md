# 🌌 Celestial Chaos: A 3-Body Problem Simulator

Welcome to **Celestial Chaos**, a chaotic little playground for simulating the infamous **3-Body Problem** using a customized implementation of the Mercury6 N-body integrator.

Whether you're trying to discover a stable orbital configuration or simply want to watch three stars violently fling each other into deep space, this repository has you covered.

> **Recommended Reading:**  
> If you're the kind of person who actually reads documentation before pressing buttons, check out smirik’s Mercury6 guide first.
>
> If you're more of a *"learn by accidentally creating a stellar catastrophe"* kind of person, continue below.

---

# 🚀 Quick Start
## *(The "I’m Too Lazy to Read Documentation" Guide)*

All commands below should be run in a **Bash terminal**, preferably inside a GitHub Codespace.

---

## 1. Environment Setup

Update packages and install the Fortran compiler:

```bash
sudo apt update
sudo apt install gfortran -y
```

---

## 2. Installation & Build

Clone the repository and compile Mercury6:

```bash
git clone https://github.com/dizz-astro/3-body-problem-simulation.git

cd mercury

make build
```

If your terminal starts screaming about `gfortran` and eventually produces `./mercury6`, congratulations — you are now legally allowed to pretend you're an astrophysicist.

---

## 3. Generate Input Files

Create editable simulation files from the provided templates:

```bash
make gen-in
```

This generates all required `.in` configuration files.

The default parameters are already tuned for a relatively stable system, so you can immediately test the simulation pipeline without accidentally vaporizing your stars.

---

# 🛠 Configuration
## *(The "God Complex" Section)*

Most of your universe-building will happen inside these four files:

|     File     |              Purpose             |               Main Things You Edit               |

|   `big.in`   | Massive bodies (your Suns/stars) |       Mass, density, positions, velocities       |
|  `small.in`  | Small bodies (planets/asteroids) |             Optional chaos enhancers             |
|  `param.in`  |    Global simulation settings    | Stop time, output intervals, integrator settings |
| `element.in` |         Output formatting        |         Output intervals and formatting          |

---

## `big.in`

This file defines your stars.

You’ll mainly edit:

- Mass, Radius, Density
- Initial positions `(x, y, z)`
- Initial velocities `(vx, vy, vz)`
- Initial angular momentum `(Lx, Ly, Lz)`

Example:

```text
ALPHA      m=1.0d0 r=0.005d0 d=1.41d0
  50.000000000000000D+00  0.0000000000000000D+00  0.0000000000000000D+00
  0.0000000000000000D+00  2.4000000000000000D-03  0.0000000000000000D+00
  0.0000000000000000D+00  0.0000000000000000D+00  0.0000000000000000D+00
```

---

## `small.in`

Optional file for adding:

- Planets
- Asteroids
- Test particles
- Tiny future victims of gravitational instability

If you add extra bodies here, you may also need to update `plot.py` so the new objects are visualized correctly.

If you do want to add them, they should look like this:

```text
 APOLLO   ep=2455225.5d0
 1.470254335318451d0 0.5599303688003985d0  6.352971824171815d0 285.850770935019d0  35.73775143515774d0  161.3598005722214d0 0.d0 0.d0 0.d0
```

---

## `param.in`

Controls global simulation behavior.

Important settings include:

- Total simulation time
- Timestep
- Output frequency
- Integrator algorithm

For most chaotic systems, the **Hybrid (`HYBRID`)** integrator works well.

---

## `element.in`

Controls how output files are written.

A good rule:

> Keep output intervals consistent with the values in `param.in`.

Otherwise your data files may look cursed.

---

## ⚠️ Important Survival Advice

### Keep velocities reasonable.

If your initial velocities are too high:

- your stars may escape instantly,
- your simulation files may end up empty,
- and your carefully crafted solar system will become an interstellar crime scene.

Also:

> If you rename or add stars, update the body names inside `plot.py`.

Otherwise, Python will emotionally detach from your simulation and refuse to plot anything useful.

---

# 🏃 Running the Simulation

---

## 1. Run Mercury6

Start the integrator:

```bash
./mercury6
```

You’ll see lots of output showing:

- simulation dates,
- timestep progress,
- energy conservation values (`dE/E`),
- and potentially signs that your stars are about to commit orbital violence.

When the terminal says:

```text
Integration complete.
```

check:

```text
info.out
```

to see whether your stars:

- survived,
- collided,
- or got gravitationally YEETed into the void.

---

## 2. Convert Binary Output

Mercury stores results in binary files first.

Convert them into readable orbital element files:

```bash
./element6
```

This generates `.aei` files for each body.

### If no files appear:

Your system probably exploded immediately.

Check the initial conditions in `big.in`.

---

## 3. Visualization & Animation

Install Python dependencies:

```bash
python3 -m pip install numpy pandas matplotlib pillow astropy astroquery
```

Generate plots and CSV data:

```bash
python3 plot.py
```

Create the animation:

```bash
python3 animation.py
```

If everything worked, you should now have:

```text
3body_simulation.gif
```

which contains several stars making increasingly questionable life decisions.

---

# 📁 Expected Output Files

|          File          |         Description       |

|        `*.aei`         |  Orbital element outputs  |
|        `*.csv`         | Processed coordinate data |
|    `3_body_img.png`    |   Static trajectory plot  |
| `3body_simulation.gif` | Final animated simulation |
|       `info.out`       |  Collision/ejection logs  |

---

# 🧹 Resetting the Universe

If your simulation turned into a cosmic car crash and you want to start over:

---

## Clean Mercury Files

```bash
make clean
```

---

## Delete Generated Files

Manually remove:

```text
ALPHA.csv
BETA.csv
3_body_img.png
3body_simulation.gif
visualization/              (folder)
```

Then rerun the simulation pipeline.

---

# 💡 Tips for Experimenting

Try changing:

- stellar masses,
- starting distances,
- orbital velocities,
- or adding additional stars.

Some systems become surprisingly stable.
Others become astrophysical horror movies.
And that’s the utter beauty of astronomy.

---

# 📚 Credits

- **Mercury6 Core:** smirik’s Mercury implementation    (https://github.com/smirik/mercury.git)
- **Physics Engine:** Isaac Newton (mostly)
- **Chaos:** You (and me, lol)

---