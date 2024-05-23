#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 21:31:02 2024

@author: ricardo
"""

# Librerías externas NumPy, SciPy y Matplotlib
from scipy.signal import TransferFunction
import matplotlib.pyplot as plt
import numpy as np


# Librería de TC2, esta la vas a usar mucho
from pytc2.sistemas_lineales import pzmap, GroupDelay, bodePlot
from pytc2.general import Chebyshev_polynomials, s, w, print_subtitle

import sympy as sp
from IPython.display import display


w0 = 1
qq1 = 1


my_tf = TransferFunction( [1], [1 , 6 , 15 , 15] )


plt.close('all')

bodePlot(my_tf, fig_id=1, filter_description = 'Q={:3.3f}'.format(qq1) )

pzmap(my_tf, fig_id=2, filter_description = 'Q={:3.3f}'.format(qq1)) #S plane pole/zero plot

GroupDelay(my_tf, fig_id=3, filter_description = 'Q={:3.3f}'.format(qq1))

#%% análisis de lo obtenido

filter_names = []
all_sys = []

this_aprox = 'BESSEL'
this_label = this_aprox

print_subtitle(this_label)
# factorizamos en SOS's
pretty_print_SOS(my_tf, mode='omegayq')
