# -*- coding: utf-8 -*-
"""
Ejercicio 1 Vectores y Matrices

@author: Víctor Javier
"""

from numpy import array

def Vandermonde(alpha):
    n = len(alpha)
    return array([[alpha[i]**j for j in range(n)] for i in range(n)])

alpha = array([1, 2, 3])
V = Vandermonde(alpha)
print(V)