# -*- coding: utf-8 -*-
"""
Ejercicio 8 funciones en python

@author: Víctor Javier
"""

from math import log

def mallador(a, b, r, N, h0):
    x = [0.0] * (N + 1)
    x[0] = a
    h = h0
    for i in range(1, N + 1):
        x[i] = x[i - 1] + h
        h *= r
    x[N] = b
    return x
    
def parametros(a, b, r):
    if (r == 1.0):
        N = int(input("Introduzca el número de intervalos: "))
        h0 = (b - a) / float(N)
        print("La longitud de los intervalos es ",h0)
    elif (r > 1.0):
        h0 = float(input("Introduzca longitud del primer intervalo: "))
        N = int(log(1 - (1 - r) * (b - a) / h0) / log(r))
        print("El número de intervalos es ",N)
    else:
        h0 = float(input("Introduzca longitud del primer intervalo: "))
        N = int(log(1 - (1 - 1 / r) * (b - a) / h0) / log(1 / r))
        print("El número de intervalos es ",N)        
    return N, h0
    
a, b = [float(extremos) for extremos in input("Introduzca los extremos del dominio: ").split()]
r = float(input("Introduzca ratio de expansión/contracción: "))
N, h0 = parametros(a, b, r)

x = mallador(a, b, r, N, h0)
for i in range(N + 1):
    print(x[i])