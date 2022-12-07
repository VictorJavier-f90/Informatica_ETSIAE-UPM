# -*- coding: utf-8 -*-
"""
Ejercicio 12

@author: Víctor Javier Llorente Lázaro
"""

from Ejercicio11 import particion
from math import pi, exp, sqrt

def gaussian(x, m = 0, s = 1):
    return (1.0 / (sqrt(2*pi)*s)) * exp(-0.5*((x - m) / s)**2)

m = 0
s = 1
N = 10

x = particion(m - 5*s, m + 5*s, N)
y = [gaussian(x[i], m, s) for i in range(N + 1)]

print(y)