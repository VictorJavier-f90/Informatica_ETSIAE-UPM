# -*- coding: utf-8 -*-
"""
Ejercicio 8

@author: Víctor Javier Llorente Lázaro
"""

def quitar_elem_pos(lista, pos):
    lista.sort()
    N = len(lista)
    if (pos < N):
        lista.pop(pos - 1)
    return lista

print(quitar_elem_pos([2.3, 1.4, 9.1, -2.2, 7.0, 43.2], 3))
print(quitar_elem_pos([3, 4, 2, -1], 5))