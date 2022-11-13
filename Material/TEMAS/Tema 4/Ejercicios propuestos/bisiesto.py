# -*- coding: utf-8 -*-
"""
Ejercicio 4 funciones en python

@author: Víctor Javier
"""

def esBisiesto(fecha):
    if fecha % 400 == 0 or (fecha % 100 != 0 and fecha % 4 == 0):
        return True
    else:
        return False


fecha = int(input("Escriba un año: "))
if esBisiesto(fecha):
    print("Es bisiesto")
else:
    print("No es bisiesto")