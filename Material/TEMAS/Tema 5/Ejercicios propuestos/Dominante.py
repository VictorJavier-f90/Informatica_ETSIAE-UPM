# -*- coding: utf-8 -*-
"""
Ejercicio 5 Vectores y Matrices

@author: Víctor Javier
"""

from numpy import array

def ESS(A):
    N = len(A)
    for i in range(N):
        for j in range(N):
            if (2*abs(A[i,i]) - sum(abs(A[:,j])) < 0.0):
                return print("No es estrictamente diagonal dominante por filas")
    return print("Es estrictamente diagonal dominante por filas")

A = array([[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]])
ESS(A)

A = array([[  2, 0.5, 0.5],
           [  1,   2,   0],
           [0.5,   1,   2]])
ESS(A)