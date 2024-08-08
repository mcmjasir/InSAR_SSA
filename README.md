
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
