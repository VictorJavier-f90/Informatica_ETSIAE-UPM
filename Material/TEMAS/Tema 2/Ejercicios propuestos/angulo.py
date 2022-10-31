# -*- coding: utf-8 -*-
"""
Ejercicio 1 condicionales

@author: Víctor Javier
"""

from math import pi

print('CONVERSOR DE ANGULOS')
print('opcion 1: grados a radianes')
print('opcion 2: radianes a grados')

opcion = int(input("opcion = "))

if (opcion == 1):
    alpha_gra = float(input('angulo (grados) = '))
    alpha_rad = alpha_gra * pi / 180
    print(alpha_gra,"º = ",alpha_rad," rad")
elif (opcion == 2):
    alpha_rad = float(input('angulo (radianes) = '))
    alpha_gra = alpha_rad * 180 / pi
    print(alpha_rad,"rad = ",alpha_gra," º")
else:
    print("valor de opción no valido")