# -*- coding: utf-8 -*-
"""
Ejercicio 2

@author: Víctor Javier Llorente Lázaro
"""

from math import sin, cos, pi

def f(x):
    if (x <= 0.0):
        return cos(pi * x)
    else:
        return 1.0 + sin(pi * x)

def funcion_trigonometrica(a, b, N):
    x = [a + i*(b-a)/N for i in range(N + 1)]
    return [f(x[i]) for i in range(N + 1)]

print(funcion_trigonometrica(0.0, 1.0, 10))