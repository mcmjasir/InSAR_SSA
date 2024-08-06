# InSAR_SSA
This repo contains python script for decompose and reconstruct InSAR Time-series output from Mintpy software using Singular Spectrum Analysis (SSA). The basic SSA code is forked from https://www.kaggle.com/code/jdarcy/introducing-ssa-for-time-series-decomposition

### Requirements and Installation:
* Python3, numpy, scipy, matplotlib, pygmt
* Mintpy

### Usage: 
The main executable for this library is ```mintpy_ssa.py```.

An example run-string would be: 

```mintpy_ssa.py timeseries.h5```
