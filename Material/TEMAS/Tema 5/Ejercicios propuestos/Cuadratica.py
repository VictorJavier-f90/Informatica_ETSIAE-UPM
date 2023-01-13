# -*- coding: utf-8 -*-
"""
Ejercicio 3 Vectores y Matrices

@author: Víctor Javier
"""

from numpy import array,matmul

def Cuadratica(v, M):
    return matmul(v, matmul(M, v))
    
v = array([1, 2, 3])
M = array([[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]])
q = Cuadratica(v, M)
print(q)