# -*- coding: utf-8 -*-
"""
Ejercicio 10 funciones en python

@author: Víctor Javier
"""

from math import pi, sqrt, exp

def mallador(a, b, N):
    h = (b - a) / float(N - 1)
    return [a + h * i for i in range(0, N)]
    
def gaussian(x, m=0, s=1):
    return (1 / (sqrt(2 * pi) * s)) * exp(- 0.5 * ((x - m) / s) ** 2)

m, s = [float(parametros) for parametros in input("Introduzca media y desv. típica: ").split()]
N = int(input("Introduzca número de puntos a calcular: "))

a = m - 5 * s
b = m + 5 * s

x = mallador(a, b, N)
for i in range(N):
    print("f( ",x[i],") = ",gaussian(x[i], m, s))