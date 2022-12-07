# -*- coding: utf-8 -*-
"""
Ejercicio 5

@author: Víctor Javier Llorente Lázaro
"""
   
def Letra_en_palabra(letra, palabra):
    return [i + 1 for i, l in enumerate(palabra) if (l.lower() == letra.lower())]

print(Letra_en_palabra('a', 'La casa está cara'))
print(Letra_en_palabra('n', 'No nada'))