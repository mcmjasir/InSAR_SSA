
# InSAR Time-Series Decomposition and Reconstruction Using SSA

This repository contains Python scripts for decomposing and reconstructing InSAR time-series data using Singular Spectrum Analysis (SSA).

## Scripts

- **`ssa.py`**: A Python class for SSA, modified from [this Kaggle notebook](https://www.kaggle.com/code/jdarcy/introducing-ssa-for-time-series-decomposition).

- **`mintpy_ssa.py`**: Reads the InSAR time-series from [Mintpy](https://github.com/insarlab/MintPy) and provides the reconstructed time-series in HDF5 (`.h5`) format.

## Overview

- **Decomposition and Reconstruction**: Utilizes SSA to decompose InSAR time-series data into components and reconstructs the time-series.
- **Integration with Mintpy**: Designed to work with time-series data produced by Mintpy.
- **Output**: The reconstructed time-series is saved in HDF5 format for efficient storage and access.

## Requirements and Installation:

* Python3, numpy, scipy, matplotlib
* [Mintpy](https://github.com/insarlab/MintPy)

## Usage: 
The main executable for this library is ```mintpy_ssa.py```.

```mintpy_ssa.py <timeseries file> -w <Window Length> -o <Output file name>```.


An example run-string would be: 

```mintpy_ssa.py timeseries.h5 -w 7 -o timeseries_ssa.h5```

## Citing this work

1. **Jasir, M. C. M., Sreejith, K. M., Agrawal, R., and Begum, S. K. (2024). Application of Singular Spectrum Analysis to InSAR time-series for constraining the postseismic deformation due to moderate magnitude earthquakes: The case of 2019 Mw 6 Mirpur earthquake, NW Himalaya. *Geophysical Journal International*.[Under Review]**

2. **Sreejith, K. M., Jasir, M. C. M., Sunil, P. S., Rose, M. S., Saji, A. P., Agrawal, R., et al. (2024). Geodetic evidence for cascading landslide motion triggered by extreme rain events at Joshimath, NW Himalaya. *Geophysical Research Letters, 51*, e2023GL106427. [https://doi.org/10.1029/2023GL106427](https://doi.org/10.1029/2023GL106427)**

