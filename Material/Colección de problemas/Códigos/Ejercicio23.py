# -*- coding: utf-8 -*-
"""
Ejercicio 23

@author: Víctor Javier Llorente Lázaro
"""

def f(x):
    if (x % 2 == 0):
        return x // 2
    else:
        return 3*x + 1

def collatz(N):
    a = N
    lista = [a]
    while (a != 1):
        lista.append(f(a))
        a = f(a)
    return lista

print(collatz(7))