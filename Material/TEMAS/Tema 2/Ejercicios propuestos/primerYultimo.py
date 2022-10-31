# -*- coding: utf-8 -*-
"""
Ejercicio 3 bucles e iteraciones

@author: Víctor Javier
"""

numero = int(input("Introduce número entero: "))

if (numero <= 9):
    print("El número solo contiene una cifra")
else:
    ultimo = numero % 10
    while (numero != 0):
        numero = numero // 10
        if (numero <= 9):
            primero = numero
            break
    print("El primer número es ",primero," y el último número es ",ultimo)