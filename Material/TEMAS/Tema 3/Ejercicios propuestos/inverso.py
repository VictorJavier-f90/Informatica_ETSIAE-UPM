# -*- coding: utf-8 -*-
"""
Ejercicio 1 estructuras de datos

@author: Víctor Javier
"""

N = 10
numeros = [i for i in range(1, N + 1)]
for i in range(N - 1, -1, -1):
    if (i != 0):
        print(numeros[i], end=", ")
    else:
        print(numeros[i])