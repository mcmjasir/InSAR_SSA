#!/usr/bin/env python3
# Load the usual suspects:
import os
import sys
import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
from mintpy.utils import utils as ut
from ssa import SSA
from sklearn.metrics import mean_squared_error

dir = './SBAS_atm_gacos'
tsfile = 'geo/geo_timeseries_SET_GACOS_ramp_demErr.h5'
lat, lon = 27.98826, 85.91211
L = 8  # Window Length

# dir = sys.argv[1]  # dir eg SBAS_s1a_atm
# tsfile = sys.argv[2]  # ts file eg; geo_timeseries_SET_GACOS_ramp_demErr.h5
# lat = float(sys.argv[3])
# lon = float(sys.argv[4])
# L = float(sys.argv[5])

out_file = 'ssa_ts.txt'


def DecYr(x):
    return x.dt.to_period('D').dt.to_timestamp().dt.year + x.dt.to_period('D').dt.to_timestamp().dt.dayofyear / 365.25


def rms(a, b):
    return math.sqrt(mean_squared_error(a, b))


def sigma_sum(Sigma):
    sigma_sumsq = (Sigma**2).sum()
    return Sigma**2 / sigma_sumsq * 100


proj_dir = os.path.expanduser(dir)
ts_file = os.path.join(proj_dir, tsfile)
# obj = tsview(ts_file, yx=(33.110,73.779))
geom_file = None
dates, dis, std = ut.read_timeseries_lalo(lat=lat, lon=lon, ts_file=ts_file, lookup_file=geom_file)

# Convert from meter to mm and save to panda df

df = pd.DataFrame({'date': dates, 'dis': dis*1000})

# Decompositon

L = 8
F_ssa = SSA(dis*1000, L)
contri = sigma_sum(F_ssa.Sigma)
df_ssa = pd.concat([F_ssa.components_to_df()], axis=1)
np.savetxt('sigma_ssa.txt', np.c_[np.arange(1, L+1), contri], fmt="%.2f")
df_comp = pd.concat([df['date'], F_ssa.components_to_df()], axis=1)
print('\n \n', 'Writing SSA all components  to: ssa_all_compo.txt ', '\n')
df_comp.to_csv('ssa_all_compo.txt', index=False, header=True, sep='\t')

plt.rcParams.update({'font.size': 10})
fig, ax = plt.subplots(nrows=L, ncols=1, sharex=True, figsize=(5, 11*L))
for i, column in enumerate(df_ssa.columns):
    ax[i].plot(df_ssa.index, df_ssa[column], label=column)
    ax[i].set_title(f'{column} ({contri[i]:.1f}%)')
    plt.subplots_adjust(hspace=.5)

# fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5))
# ax1.scatter(np.arange(1, L+1), sigma_sum(F_ssa.Sigma))
# plt.show()

# Reconstruction

df['ssa_trend'] = pd.DataFrame(F_ssa.reconstruct([0, 1]))
df['noise'] = pd.DataFrame(F_ssa.reconstruct([2, 3, 4, 5, 6]))
print('\n \n', 'Writing to:  ', out_file, '\n')
df.to_csv(out_file, index=False, header=True, sep='\t')


fig, ax = plt.subplots(nrows=3, ncols=1, sharex=True, figsize=(10, 10))

ax[0].plot(df['date'], df['dis'], label='InSAR')
ax[0].set_title('InSAR')
ax[1].plot(df['date'], df['noise'], label='Noise')
ax[1].set_title('Periodic+Noise')
ax[2].plot(df['date'], df['ssa_trend'], label='Trend')
ax[2].set_title('Trend')
plt.show()
