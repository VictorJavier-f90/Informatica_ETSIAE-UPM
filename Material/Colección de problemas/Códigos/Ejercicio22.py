# -*- coding: utf-8 -*-
"""
Ejercicio 22

@author: Víctor Javier Llorente Lázaro
"""

def es_primo(N):
    if N == 1:
        return False
    else:
        return all(N % i != 0 for i in range(2, N))

def divide_lista(lista):
    lpar   = []
    limpar = []
    lprimo = []
    lista.sort()
    for i,l in enumerate(lista):
        if es_primo(l):
            lprimo.append(l)
        else:
            if (l % 2 == 0):
                lpar.append(l) 
            else:
                limpar.append(l)           
    return lpar, limpar, lprimo

print(divide_lista([2, 1, 10, 8, 4, 7, 6, 5, 9, 3]))