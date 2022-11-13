# -*- coding: utf-8 -*-
"""
Ejercicio 3 funciones en python

@author: Víctor Javier
"""

def conversionBinaria(numero):
    binario = 0
    multiplicador = 1
    
    while (numero != 0):
        binario = binario + numero % 2 * multiplicador
        numero //= 2
        multiplicador *= 10
        
    return binario

numero = int(input("Introduzca número: "))

binario = conversionBinaria(numero)

print("El número ",numero," es ",binario," en base binaria")