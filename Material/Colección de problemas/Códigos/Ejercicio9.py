# -*- coding: utf-8 -*-
"""
Ejercicio 9

@author: Víctor Javier Llorente Lázaro
"""

def divisores(n):
     return [i for i in range(1, n) if n % i == 0]   

def es_perfecto(n): 
    return n == sum(divisores(n))

def perfectos(N): 
    p = []
    n = 1   
    while len(p) < N:
        if es_perfecto(n):
            p.append(n)
        n += 1  
    return p  

print(perfectos(3))