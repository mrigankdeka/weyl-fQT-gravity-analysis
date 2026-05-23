# Weyl-type f(Q,T) Gravity: Cosmological Constraints and Model Comparison

[![Python 3.9+](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![arXiv](https://img.shields.io/badge/arXiv-2403.12345-red.svg)](https://arxiv.org/abs/2403.12345)

**Author:** Mriganka Raj Deka (IISER Berhampur)  
**Supervisor:** Dr. Praveen Kumar Dhankar (Symbiosis Institute of Technology)

---

## Overview

This repository contains the complete analysis pipeline for testing the **Weyl-type f(Q,T) gravity** model against cosmological observations. The work reproduces and extends the results of Gadbail et al. (2024) by:

- Adding the **Pantheon+** supernova sample (1701 SNe Ia, 2022)
- Incorporating **DESI DR2 BAO** measurements (13 points, 2025)
- Performing **Bayesian model comparison** (AIC/BIC) against ΛCDM and wCDM

The key finding: while ΛCDM remains statistically preferred (ΔAIC = +5.38), the f(Q,T) model is a **viable alternative** that explains late-time cosmic acceleration without a cosmological constant.

---

## Physics Background

### The Model

We adopt a divergence-free parametrization of the deceleration parameter:

$$q(z) = q_0 + q_1 \frac{z(1+z)}{1+z^2}$$

This yields the Hubble parameter:

$$H(z) = H_0 (1+z)^{1+q_0} (1+z^2)^{q_1/2}$$

The parameters $(q_0, q_1)$ determine the expansion history. A negative $q_0$ indicates current acceleration; a positive $q_1$ controls the deceleration-to-acceleration transition.

### Modified Gravity Framework

Weyl-type f(Q,T) gravity couples the non-metricity scalar $Q$ to the trace $T$ of the energy-momentum tensor. The simplest linear form is:

$$f(Q,T) = \alpha Q + \frac{\beta}{6\kappa^2} T$$

For $\beta=0$ and $\alpha=-1$, this reduces to General Relativity.

### Datasets Used

| Dataset | Description | Redshift Range | Points |
|---------|-------------|----------------|--------|
| **OHD** | Hubble parameter from cosmic chronometers | 0.07 – 1.965 | 43 |
| **Pantheon+** | Type Ia supernovae (diagonal errors) | 0.001 – 2.26 | 1701 |
| **DESI BAO** | Distance ratios $D_M/r_s$, $D_H/r_s$, $D_V/r_s$ | 0.295 – 2.33 | 13 |

---

## Key Results

### Best-fit Parameters (OHD + Pantheon+ + BAO)

| Parameter | Value | Description |
|-----------|-------|-------------|
| $q_0$ | $-0.561 \pm 0.017$ | Present deceleration parameter |
| $q_1$ | $0.717 \pm 0.028$ | Transition sharpness |
| $\Omega_m$ | $0.352 \pm 0.085$ | Matter density parameter |
| $M_B$ | $-19.357 \pm 0.006$ | Supernova absolute magnitude |
| $z_t$ | $0.68$ | Transition redshift (where $q(z_t)=0$) |

Reduced chi-squared: $\chi^2_{\text{red}} \approx 1.05$ — excellent fit.

### Model Comparison (AIC/BIC)

| Model | Parameters | $\chi^2_{\min}$ | AIC | BIC | ΔAIC |
|-------|------------|-----------------|-----|-----|------|
| ΛCDM | 2 | 899.66 | **903.66** | 914.60 | 0 (baseline) |
| wCDM | 3 | 898.33 | 904.33 | 920.74 | +0.67 |
| f(Q,T) | 4 | 901.04 | 909.04 | 930.93 | **+5.38** |

**Interpretation:** ΛCDM is statistically preferred ($2 < \Delta\text{AIC} < 6$ indicates positive evidence against f(Q,T)). However, the actual fit difference ($\Delta\chi^2 = 1.38$) is modest, and f(Q,T) remains a viable alternative.

### CMB Incompatibility

Attempts to include Planck 2018 CMB distance priors led to MCMC non-convergence. This is expected: the $q(z)$ parametrization is designed only for low redshifts ($z \lesssim 2$) and cannot describe the high-redshift expansion history ($z \sim 1100$).

---

## Getting Started

### Prerequisites

- Python 3.9 or higher
- Required packages: `numpy`, `scipy`, `emcee`, `corner`, `matplotlib`

### Installation

```bash
git clone https://github.com/mrigankdeka/weyl-fQT-gravity-analysis.git
cd weyl-fQT-gravity-analysis
pip install -r requirements.txt
