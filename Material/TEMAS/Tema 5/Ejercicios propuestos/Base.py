# -*- coding: utf-8 -*-
"""
Ejercicio 4 Vectores y Matrices

@author: Víctor Javier
"""

from numpy import array, vstack
from numpy.linalg import det

def EsBase(*vectores):
    flag = 0
    for v in vectores:
        if (flag == 0):
            A = v
            flag = 1
        else:
            A = vstack((A,v))
    d = det(A.T)
    if (d == 0):
        return print("Los vectores no forman una base en R")
    else:
        return print("Los vectores forman una base en R")

v1 = array([ 1, 1, 1])
v2 = array([-2, 0, 2])
v3 = array([ 3,-1,-2])
EsBase(v1,v2,v3)