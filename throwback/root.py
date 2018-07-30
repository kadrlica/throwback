#!/usr/bin/env python
"""
Generic python script.
"""
__author__ = "Alex Drlica-Wagner"
import matplotlib
from collections import OrderedDict as odict


# A more modern version from TColor...
# https://github.com/root-project/root/blob/2762a32343f57664b42558cd3af4031fe2f4f086/core/base/src/TColor.cxx#L2404-L2408
PALETTE = [19,18,17,16,15,14,13,12,11,20,
           21,22,23,24,25,26,27,28,29,30, 8,
           31,32,33,34,35,36,37,38,39,40, 9,
           41,42,43,44,45,47,48,49,46,50, 2,
            7, 6, 5, 4, 3, 2,1]
            #7, 6, 5, 4, 3, 112,1] # original with typo
            #7, 6, 5, 4, 3, 5,1]   # corrected to match

# Going back in time, here was the origin palette
# Note the typo in entry 48: 112 (pink) not 2 (red)
# https://github.com/root-project/root/blob/9294cc60a9a70dece4f24f0bc0399cc00c0f78b5/base/src/TStyle.cxx#L1445-L1449
PALETTE99 = list(PALETTE)
PALETTE99[-2] = 5 # typo was 112, but end up being magenta

# These are the basic root colors. 
# https://github.com/root-project/root/blob/2762a32343f57664b42558cd3af4031fe2f4f086/core/base/src/TColor.cxx#L1077
# This list was generated with:
# for (int i=1; i<51; i++) {gROOT->GetColor()->Print; }
TCOLORS = [
 (1.000000, 1.000000, 1.000000), # Name=background
 (0.000000, 0.000000, 0.000000), # Name=black
 (1.000000, 0.000000, 0.000000), # Name=red
 (0.000000, 1.000000, 0.000000), # Name=green
 (0.000000, 0.000000, 1.000000), # Name=blue
 (1.000000, 0.000000, 1.000000), # Name=magenta
 (0.000000, 1.000000, 0.800000), # Name=teal
 (1.000000, 0.800000, 0.000000), # Name=orange
 (0.350000, 0.830000, 0.330000), # Name=Color8
 (0.350000, 0.330000, 0.850000), # Name=Color9
 (0.999000, 0.999000, 0.999000), # Name=white
 (0.754000, 0.715000, 0.676000), # Name=editcol
 (0.300000, 0.300000, 0.300000), # Name=grey12
 (0.400000, 0.400000, 0.400000), # Name=grey13
 (0.500000, 0.500000, 0.500000), # Name=grey14
 (0.600000, 0.600000, 0.600000), # Name=grey15
 (0.700000, 0.700000, 0.700000), # Name=grey16
 (0.800000, 0.800000, 0.800000), # Name=grey17
 (0.900000, 0.900000, 0.900000), # Name=grey18
 (0.950000, 0.950000, 0.950000), # Name=grey19
 (0.800000, 0.780000, 0.670000), # Name=Color20
 (0.800000, 0.780000, 0.670000), # Name=Color21
 (0.760000, 0.750000, 0.660000), # Name=Color22
 (0.730000, 0.710000, 0.640000), # Name=Color23
 (0.700000, 0.650000, 0.590000), # Name=Color24
 (0.720000, 0.640000, 0.610000), # Name=Color25
 (0.680000, 0.600000, 0.550000), # Name=Color26
 (0.610000, 0.560000, 0.510000), # Name=Color27
 (0.530000, 0.400000, 0.340000), # Name=Color28
 (0.690000, 0.810000, 0.780000), # Name=Color29
 (0.520000, 0.760000, 0.640000), # Name=Color30
 (0.540000, 0.660000, 0.630000), # Name=Color31
 (0.510000, 0.620000, 0.550000), # Name=Color32
 (0.680000, 0.740000, 0.780000), # Name=Color33
 (0.480000, 0.560000, 0.600000), # Name=Color34
 (0.460000, 0.540000, 0.570000), # Name=Color35
 (0.410000, 0.510000, 0.590000), # Name=Color36
 (0.430000, 0.480000, 0.520000), # Name=Color37
 (0.490000, 0.600000, 0.820000), # Name=Color38
 (0.500000, 0.500000, 0.610000), # Name=Color39
 (0.670000, 0.650000, 0.750000), # Name=Color40
 (0.830000, 0.810000, 0.530000), # Name=Color41
 (0.870000, 0.730000, 0.530000), # Name=Color42
 (0.740000, 0.620000, 0.510000), # Name=Color43
 (0.780000, 0.600000, 0.490000), # Name=Color44
 (0.750000, 0.510000, 0.470000), # Name=Color45
 (0.810000, 0.370000, 0.380000), # Name=Color46
 (0.670000, 0.560000, 0.580000), # Name=Color47
 (0.650000, 0.470000, 0.480000), # Name=Color48
 (0.580000, 0.410000, 0.440000), # Name=Color49
 (0.830000, 0.350000, 0.330000), # Name=Color50
]

root = matplotlib.colors.ListedColormap([TCOLORS[i] for i in PALETTE99])


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    args = parser.parse_args()
    import numpy as np
    import pylab as plt
    from mpl_toolkits.mplot3d import Axes3D

    def fn(x,y):
        return 0.1+(1-(x-2)*(x-2))*(1-(y-2)*(y-2))
    xx,yy = np.meshgrid(np.linspace(1,3,100),np.linspace(1,3,100))

    plt.figure()
    plt.contourf(fn(xx,yy),20,vmin=0,vmax=1.08,cmap=root)
    plt.colorbar(ticks=np.arange(0,1.2,0.1))

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    im = ax.plot_surface(xx,yy,fn(xx,yy),vmin=0,vmax=1.08,cmap=root)
    plt.colorbar(ticks=np.arange(0,1.2,0.1))
