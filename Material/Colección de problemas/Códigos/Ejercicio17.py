# -*- coding: utf-8 -*-
"""
Ejercicio 17

@author: Víctor Javier Llorente Lázaro
"""

from math import sqrt

def posicion_relativa(x, y, R):
    d = 0.0
    for i in range(3):
        d += (x[i] - y[i])**2
    d = sqrt(d)
    if (d <= R):
        return True
    else:
        return False

print(posicion_relativa((1.0, 1.0, 1.0), (0.0, 0.0, 0.0), 1.0))
print(posicion_relativa((0.5, 0.5, 0.5), (0.0, 0.0, 0.0), 1.0))