# -*- coding: utf-8 -*-
"""
Ejercicio 2 estructuras de datos

@author: Víctor Javier
"""

frase = list(input("Introduzca frase: "))

aux = []
for elemento in frase:
    if elemento.strip():
        aux.append(elemento)
frase = aux

frase_reves = frase[:]
frase_reves.reverse()

if (frase == frase_reves):
    print("La frase es un palíndromo")
else:
    print("La frase no es un palíndromo")