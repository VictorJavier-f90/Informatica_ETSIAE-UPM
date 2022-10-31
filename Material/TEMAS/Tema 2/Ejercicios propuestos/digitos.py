# -*- coding: utf-8 -*-
"""
Ejercicio 2 bucles e iteraciones

@author: Víctor Javier
"""

numero = int(input("Intorduce número entero: "))

cifras = 0

if (numero == 0):
    print("El número ",numero," contiene ",cifras + 1," cifra")
else:
    n = numero
    while (n != 0):
        n = n // 10
        cifras += 1
    if (cifras == 1):
        print("El número ",numero," contiene ",cifras, " cifra")
    elif (cifras > 1):
        print("El número ",numero," contiene ",cifras, " cifras")
    else:
        print("Error")