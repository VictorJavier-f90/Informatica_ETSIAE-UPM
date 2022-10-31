# -*- coding: utf-8 -*-
"""
Ejercicio 4a bucles e iteraciones

@author: Víctor Javier
"""

Sn = 0.0

for n in range(1,6):
    Sn += (2*n - 1) / (n*(n + 1))

print("S5 = ",Sn)