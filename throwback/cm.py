"""
This module provides a set of throwback colormaps.
"""
__author__ = "Alex Drlica-Wagner"
import pylab as plt

from root import root_cmap
from ds9 import ds9_b

cmap_d = dict()
cmap_d['root'] = root_cmap
cmap_d['ds9_b']  = ds9_b

locals().update(cmap_d)

# Register with matplotlib
plt.register_cmap(name='root', data=root_cmap)
plt.cm.root = plt.cm.get_cmap('root')

plt.register_cmap(name='ds9_b', data=ds9_b)
plt.cm.ds9_b = plt.cm.get_cmap('ds9_b')
