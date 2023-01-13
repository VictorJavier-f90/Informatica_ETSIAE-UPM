# -*- coding: utf-8 -*-
"""
Ejercicio 2 Vectores y Matrices

@author: Víctor Javier
"""

from numpy import array

def Traza(M):
    n = len(M)
    return sum([M[i,i] for i in range(n)])

M = array([[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]])
t = Traza(M)
print(t)