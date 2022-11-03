# -*- coding: utf-8 -*-
"""
Ejercicio 8 estructuras de datos

@author: Víctor Javier
"""

a, b = [float(extr) for extr in input("Extremos del intervalo I in [a, b]: ").split()]

N = 10
h = (b - a) / float(N)
x = [a + h * i for i in range(0, N + 1)]

polinomio = [0] * len(x)
polinomio = [x[i] ** 3 - 4 * x[i] ** 2 + 8 for i in range(0, N + 1)]

print("x, P(x)")
for i in range(0, N + 1):
    print(x[i],polinomio[i])