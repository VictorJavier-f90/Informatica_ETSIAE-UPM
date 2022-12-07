# -*- coding: utf-8 -*-
"""
Ejercicio 7

@author: Víctor Javier Llorente Lázaro
"""

def lista_diff(lista1, lista2):
    return list(set(lista1) ^ set(lista2))

print(lista_diff([1, 3, 5, 7, 9], [1, 2, 3, 4, 5]))
print(lista_diff(['pera', 'pulpo', 'pasta'], ['manzana', 'pera']))