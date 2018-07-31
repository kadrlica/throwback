"""
This module provides a set of throwback colormaps.
"""
__author__ = "Alex Drlica-Wagner"
import pylab as plt

from root import root_cmap
from ds9 import ds9_b

# Register with matplotlib
plt.register_cmap(name='root', cmap=root_cmap)
plt.cm.root = plt.cm.get_cmap('root')

plt.register_cmap(name='ds9_b', data=ds9_b)
plt.cm.ds9_b = plt.cm.get_cmap('ds9_b')

# Register here

cmap_d = dict()
cmap_d['root']   = plt.cm.root
cmap_d['ds9_b']  = plt.cm.ds9_b

locals().update(cmap_d)
