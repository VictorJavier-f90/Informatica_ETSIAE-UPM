# -*- coding: utf-8 -*-
"""
Ejercicio 7 funciones en python

@author: Víctor Javier
"""

def mallador(a, b, N):
    h = (b - a) / float(N)
    x = [a + h * i for i in range(0, N + 1)]
    return x
    
a, b = [float(extremos) for extremos in input("Introduzca los extremos del dominio: ").split()]
N = int(input("Introduzca el numero de intervalos: "))

x = mallador(a, b, N)
for i in range(N + 1):
    print(x[i])