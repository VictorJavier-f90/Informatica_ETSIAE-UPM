# -*- coding: utf-8 -*-
"""
Ejercicio 2 Ficheros-Matplotlib

@author: Víctor Javier
"""

from numpy import pi, sin, linspace

def f(x):
    return x*sin( 2*pi*x )

def df(f, x, h):
    return ( f(x + h) - f(x) ) / h
    
a, b = [float(extremos) for extremos in input("Introduzca los extremos del intervalo: ").split()]
n = 10

x = linspace(a, b, n)
y1 = f(x)
h = x[1] - x[0]
y2 = df(f, x, h)

f = open("funcion.txt", mode="w")
for i in range(n):
  f.write(str(x[i]) + " " + str(y1[i]) + " " + str(y2[i]) + "\n")
f.close()