# -*- coding: utf-8 -*-
"""
Ejercicio 6 funciones en python

@author: Víctor Javier
"""

def polinomio(a,x):
    n = len(a)
    p = 1.0
    for i in range(n):
        p *= x - a[i]
    return p
    
a = [float(raiz) for raiz in input("Introduzca las raices del polinomio P(x): ").split()]
x = float(input("Introduzca punto de evaluación: "))
print("P(",x,")=",polinomio(a,x))