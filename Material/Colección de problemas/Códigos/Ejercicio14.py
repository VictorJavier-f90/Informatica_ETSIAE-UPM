# -*- coding: utf-8 -*-
"""
Ejercicio 14

@author: Víctor Javier Llorente Lázaro
"""

from math import pi, cos, factorial

def Taylor_coseno(x, tol):
    n = 0
    T = 1.0
    while abs(cos(x) - T) > tol:
        n += 1
        T += ((-1)**n * x**(2*n)) / factorial(2*n)
    return T

print(Taylor_coseno(0.0*pi, 1e-5))
print(Taylor_coseno(0.5*pi, 1e-5))
print(Taylor_coseno(-0.5*pi, 1e-5))