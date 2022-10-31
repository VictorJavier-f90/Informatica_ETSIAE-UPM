# -*- coding: utf-8 -*-
"""
Ejercicio 5b bucles e iteraciones

@author: Víctor Javier
"""

S = 0.0

n = 1
while (abs((-1)**(n+1)/2**n) >= 1.0e-15):
    S += (-1)**(n+1)/2**n
    n += 1

print("S = ",S)