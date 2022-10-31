# -*- coding: utf-8 -*-
"""
Ejercicio 4b bucles e iteraciones

@author: Víctor Javier
"""

from math import factorial

Sn = 0.0

for n in range(21):
    for k in range(n + 2):
        Sn += 1 / factorial(k)

print("S20 = ",Sn)