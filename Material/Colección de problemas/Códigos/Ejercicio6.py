# -*- coding: utf-8 -*-
"""
Ejercicio 6

@author: Víctor Javier Llorente Lázaro
"""

def eval_poly(x, coeffs):
    N = len(coeffs)
    p = 0.0
    for i in range(N):
        p += coeffs[i] * x ** i
    return p

print(eval_poly(2, [1, 2, 3]))