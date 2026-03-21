# Weyl f(Q,T) Gravity Analysis

This project investigates whether the Weyl f(Q,T) gravity model can explain late-time cosmic acceleration without invoking dark energy.

The analysis compares theoretical predictions with observational cosmology datasets using Markov Chain Monte Carlo (MCMC).

## Datasets
- BAO
- CMB
- eBOSS
- DESI

## Parameters fitted
- q0
- q1
- MB

Assumption:
H0 = 70 km/s/Mpc

## Method
Posterior distributions are obtained using the emcee MCMC sampler and visualized with corner plots.

## Libraries
numpy, scipy, emcee, matplotlib, corner, tqdm
