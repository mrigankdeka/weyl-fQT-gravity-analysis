# Weyl f(Q,T) Gravity Analysis

This project investigates whether Weyl f(Q,T) gravity can explain late-time cosmic acceleration without invoking dark energy. 

## Reference
This implementation is based on the Weyl f(Q,T) gravity model discussed in:

GN Gadbail et al. (8 Sep 2022)  
"Interaction of divergence-free deceleration parameter in Weyl-type f(Q,T) gravity"  
Chinese Journal of Physics

arXiv:2209.04348

Instead of directly solving the full modified gravity field equations, the analysis tests observational constraints under a divergence-free parameterization of the deceleration parameter inspired by Weyl f(Q,T) gravity.

## Method

The deceleration parameter is parameterized using free parameters:

q0  
q1  

which remain finite for all redshifts.

Markov Chain Monte Carlo (MCMC) using the emcee sampler is used to estimate posterior distributions of these parameters.

## Data

The model predictions are compared with observational cosmology datasets:

- BAO
- CMB
- eBOSS
- DESI

## Libraries Used

numpy  
scipy  
emcee  
corner  
matplotlib  
tqdm

## Repository Structure

data/ → observational datasets  
src/ → cosmology and MCMC implementation  
notebooks/ → analysis notebook reproducing results
