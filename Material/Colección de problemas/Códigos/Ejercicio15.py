# -*- coding: utf-8 -*-
"""
Ejercicio 15

@author: Víctor Javier Llorente Lázaro
"""

from math import pi, sin, cos

def posicion(R, t):
    return (R*cos(t), R*sin(t))

print(posicion(1.0, 0.0))
print(posicion(1.0, 0.5*pi))
print(posicion(1.0, pi))