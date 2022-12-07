# -*- coding: utf-8 -*-
"""
Ejercicio 10

@author: Víctor Javier Llorente Lázaro
"""

def divisores(n):
    return [i for i in range(1, n + 1) if n % i == 0]

def mcd(*numeros):
    k = set(divisores(numeros[0]))
    for n in numeros:
        k = k & set(divisores(n))
    return max(k)

print(divisores(26))
print(mcd(24, 30, 72))
print(mcd(180, 30, 45, 60))