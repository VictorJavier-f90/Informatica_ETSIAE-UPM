# -*- coding: utf-8 -*-
"""
Ejercicio 4

@author: Víctor Javier Llorente Lázaro
"""

def palabras(p1,p2):
    return list(set(p1.lower()) & set(p2.lower()))

print(palabras('melón','tomate'))
print(palabras('Violín','lava'))