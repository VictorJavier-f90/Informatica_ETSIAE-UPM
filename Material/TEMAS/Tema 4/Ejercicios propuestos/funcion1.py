# -*- coding: utf-8 -*-
"""
Ejercicio 9 funciones en python

@author: Víctor Javier
"""

from math import pi, sin

def f(t):
    if (-2*pi <= t <= -pi):
        return 5
    elif (-pi < t <= 0):
        return -5
    elif (0 < t <= pi):
        return 5
    elif (pi < t <= 2*pi):
        return -5
    
def S(t, n):
    suma = 0.1
    for k in range(1, n + 1):
        suma += ((1 - (-1)**k) / k) * sin(k * t)
    return (10 / pi) * suma

t = [-3*pi/2, -pi/2, pi/2, 3*pi/2]
n = [1, 3, 5, 10, 30, 100] 
for i in range(len(t)):
    for j in range(len(n)):
        print("t =",t[i]," n = ",n[j]," error = ",abs(f(t[i]) - S(t[i],n[j])))