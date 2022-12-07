# -*- coding: utf-8 -*-
"""
Ejercicio 13

@author: Víctor Javier Llorente Lázaro
"""

from math import pi, sin, factorial

def Taylor_seno(x, tol):
    n = 0
    T = x
    while abs(sin(x) - T) > tol:
        n += 1
        T += ((-1)**n * x**(2*n + 1)) / factorial(2*n + 1)
    return T

print(Taylor_seno(0.0*pi, 1e-5))
print(Taylor_seno(0.5*pi, 1e-5))
print(Taylor_seno(-0.5*pi, 1e-5))