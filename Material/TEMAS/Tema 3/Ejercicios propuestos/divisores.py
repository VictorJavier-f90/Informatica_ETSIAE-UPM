# -*- coding: utf-8 -*-
"""
Ejercicio 5 estructuras de datos

@author: Víctor Javier
"""

numero = int(input("Introduzca número: "))

divisores = []
for divisor in range(1,numero+1):
    if (numero % divisor) == 0:
        divisores.append(divisor) 
print("Los divisores de ",numero," son ",divisores)