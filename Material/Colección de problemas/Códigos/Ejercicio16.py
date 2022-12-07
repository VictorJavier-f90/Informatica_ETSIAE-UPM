# -*- coding: utf-8 -*-
"""
Ejercicio 16

@author: Víctor Javier Llorente Lázaro
"""

from math import sqrt

def distancia(x, y):
    d = 0.0
    for i in range(3):
        d += (x[i] - y[i])**2
    return sqrt(d)

print(distancia((1.0, 1.0, 1.0), (0.0, 0.0, 0.0)))