# InSAR_SSA
This repo contains python script to decompose and reconstruct InSAR Time-series using Singular Spectrum Analysis (SSA). The basic SSA code is forked from https://www.kaggle.com/code/jdarcy/introducing-ssa-for-time-series-decomposition.  It reads the  InSAR Time-series from [Mintpy](https://github.com/insarlab/MintPy) and gives the reconstructed time-series in h5 format.

### Requirements and Installation:
* Python3, numpy, scipy, matplotlib
* [Mintpy](https://github.com/insarlab/MintPy)

### Usage: 
The main executable for this library is ```mintpy_ssa.py```.

An example run-string would be: 

```mintpy_ssa.py timeseries.h5 -w ```
