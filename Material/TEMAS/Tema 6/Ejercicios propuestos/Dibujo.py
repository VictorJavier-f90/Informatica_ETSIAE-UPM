# -*- coding: utf-8 -*-
"""
Ejercicio 3 Ficheros-Matlibplot

@author: Víctor Javier
"""

from numpy import arange, pi, sqrt
from matplotlib.pyplot import subplots, plot, axis, grid, xlabel, ylabel, title, show

x = arange(0, 1, 0.01)
y = 1 / sqrt(1 - x**2)

fig, ax = subplots()

ax.plot(x, y)

axis([0, 1, 1, 3])
grid()
xlabel("v / c")
ylabel("m / m_0")
title("Factor de Lorentz")

show()