# -*- coding: utf-8 -*-
"""
Ejercicio 3

@author: Víctor Javier Llorente Lázaro
"""

def es_primo(N):
    return all(N % i != 0 for i in range(2, N))

def primos(N):
    if (N < 2):
        return []
    else:
        return [i for i in range(2, N) if es_primo(i)]

print(primos(2))
print(primos(10))
print(primos(100))