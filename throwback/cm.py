"""
This module provides a set of throwback colormaps.
"""
__author__ = "Alex Drlica-Wagner"

from root import root_cmap
from ds9 import ds9_b

cmap_d = dict()
cmap_d['root'] = root_cmap
cmap_d['ds9']  = ds9_cmap

locals().update(cmap_d)

