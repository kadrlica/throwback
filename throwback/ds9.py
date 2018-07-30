#!/usr/bin/env python
"""
DS9 colors and colormaps
"""
__author__ = "Alex Drlica-Wagner"

import pylab as plt


# http://tdc-www.harvard.edu/software/saoimage/saoimage.color.html
ds9_b = {
    'red'   : [[0.0 , 0.0 , 0.0],
               [0.25, 0.0 , 0.0],
               [0.50, 1.0 , 1.0],
               [0.75, 1.0 , 1.0],
               [1.0 , 1.0 , 1.0]],
    'green' : [[0.0 , 0.0 , 0.0],
               [0.25, 0.0 , 0.0],
               [0.50, 0.0 , 0.0],
               [0.75, 1.0 , 1.0],
               [1.0 , 1.0 , 1.0]],
    'blue'  : [[0.0 , 0.0 , 0.0],
               [0.25, 1.0 , 1.0],
               [0.50, 0.0 , 0.0],
               [0.75, 0.0 , 0.0],
               [1.0 , 1.0 , 1.0]]
    }

def load_ds9_cmap():
    plt.register_cmap(name='ds9_b', data=ds9_b)
    plt.cm.ds9_b = plt.cm.get_cmap('ds9_b')
    return plt.cm.ds9_b
