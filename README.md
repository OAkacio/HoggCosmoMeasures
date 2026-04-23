# HoggCosmoMeasures

![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

This repository contains a numerical integrator developed in Python for calculating the Luminosity Distance ($d_L$) within Hogg's framework and Friedmann-Lemaître-Robertson-Walker (FLRW) cosmological models. The code enables the superposition and comparison of various universe models (Matter-dominated, Dark Energy-dominated, and Benchmark).

## Authorship

**Victor Moreira Acacio**

Institute of Astronomy, Geophysics and Atmospheric Sciences of the University of São Paulo

GitHub: [@OAkacio](https://github.com/OAkacio)

ORCID: [0009-0007-4484-2129](https://orcid.org/0009-0007-4484-2129)

## Installation

Clone this repository and install the dependencies by running the following commands in your terminal:

```bash
git clone [https://github.com/OAkacio/flrw-luminosity-distance-integrator.git](https://github.com/OAkacio/flrw-luminosity-distance-integrator.git)
cd flrw-luminosity-distance-integrator
pip install -r requirements.txt
```

## Usage

The codebase is highly modular. You can adjust inputs, run core integrations, and generate specific plots using dedicated scripts.

**1. Configure Parameters** 

Before running the integrator, define your custom cosmological parameters ($\Omega_m$, $\Omega_{EE}$, $w$, and maximum redshift $z$) in src/parameters.py. Physical constants and the integration step can be modified in src/constants.py.

**2. Generate Data (Single Model)** 

To run the full numerical integration routine for your custom model and export the results to .txt files inside the data/ directory, execute:

```bash
python main.py
```

**3. Plot Basic Graphs**

Once the data is generated, you can plot the individual curves for Luminosity Distance, Distance Modulus, and Approximation Errors for your custom model by running:

```bash
python basic_plots.py
```

**4. Superposition & Comparison**

To automatically run the integration for three distinct universe scenarios (Custom, Matter-only, and Dark Energy-only) and plot their superpositions, use the comparison script:

```bash
python comparison_plot.py
```

(All generated graphs will be saved in high resolution inside the figures/ directory).

## Theoretical Background

The mathematical foundation of this integrator is based on the classical definitions of cosmological distances for an FLRW model, as summarized in standard cosmography literature. The code calculates these quantities in a cascading sequence:

**1. Hubble Expansion Function ($E(z)$)**
The evolution of the universe's expansion rate as a function of redshift $z$ is described by $E(z)$, which depends on the density parameters for matter ($\Omega_m$), curvature ($\Omega_k$), and dark energy ($\Omega_{EE}$), considering its equation of state $w$:

$$E(z) = \sqrt{\Omega_m(1+z)^3 + \Omega_k(1+z)^2 + \Omega_{EE}(1+z)^{3(1+w)}}$$

**2. Comoving Distance (Line-of-Sight) ($D_C$)**
Represents the distance traveled by light along the line of sight, which is the primary target of the numerical integration:

$$D_C = \frac{c}{H_0} \int_0^z \frac{dz'}{E(z')}$$

**3. Comoving Distance (Transverse) ($D_M$)**
Accounts for the geometry of the universe. Given the Hubble distance $D_H = c/H_0$, the transverse distance is determined by the spatial curvature parameter ($\Omega_k = 1 - \Omega_m - \Omega_{EE}$):

$$D_M = \begin{cases} \frac{D_H}{\sqrt{\Omega_k}} \sinh\left(\sqrt{\Omega_k} \frac{D_C}{D_H}\right) & \text{if } \Omega_k > 0 \text{ (Open Universe)} \\ D_C & \text{if } \Omega_k = 0 \text{ (Flat Universe)} \\ \frac{D_H}{\sqrt{|\Omega_k|}} \sin\left(\sqrt{|\Omega_k|} \frac{D_C}{D_H}\right) & \text{if } \Omega_k < 0 \text{ (Closed Universe)} \end{cases}$$

**4. Luminosity Distance ($D_L$)**
Relates the absolute luminosity of an object to its observed flux on Earth, serving as the key parameter for studying "standard candles" (such as supernovae):

$$D_L = (1+z) D_M$$

**5. Distance Modulus ($\mu$)**
The logarithmic relationship between apparent and absolute magnitude, representing the direct astronomical observable from the simulation:

$$\mu = 5 \log_{10}\left(D_L\right) + 25$$
*(Where $D_L$ is expressed in Megaparsecs - Mpc).*

## Project Structure

```text
├── data/                  # Generated numerical data files (.txt)
├── figures/               # High-resolution plots (.png)
├── src/                   # Core source code
│   ├── constants.py       # Physical constants and step sizes
│   ├── core.py            # Mathematical functions and equations
│   ├── parameters.py      # Input cosmological parameters
│   ├── plot.py            # Plotting configurations (LaTeX style)
│   └── save_load.py       # I/O functions for handling .txt files
├── basic_plots.py         # Script to plot single-model graphs
├── comparison_plot.py     # Script to generate and plot model superpositions
├── main.py                # Core integration engine and data generator
└── requirements.txt       # Project dependencies
```

## Motivation

This repository was developed as part of a cosmology project focused on the study of supernovae. The central objective of this code is to provide an open-source and reproducible routine for the numerical integration of luminosity distance, allowing for direct comparison of the universe's expansion behavior under different matter and dark energy density parameters.

## References

The mathematical development of this integrator, as well as the cascading equations for cosmological distances, were strongly based on:

* HOGG, David W. **Distance measures in cosmology**. 1999. Available at: [https://arxiv.org/abs/astro-ph/9905116](https://arxiv.org/abs/astro-ph/9905116).
