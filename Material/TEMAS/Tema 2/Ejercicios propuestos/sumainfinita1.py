# -*- coding: utf-8 -*-
"""
Ejercicio 5a bucles e iteraciones

@author: Víctor Javier
"""

from math import factorial

S = 0.0

n = 0
while (1/factorial(n) >= 1.0e-15):
    S += 1/factorial(n)
    n += 1

print("S = ",S)