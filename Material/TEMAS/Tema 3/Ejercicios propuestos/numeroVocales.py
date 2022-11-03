# -*- coding: utf-8 -*-
"""
Ejercicio 3 estructuras de datos

@author: Víctor Javier
"""

palabra = list(input("Introduzca palabra: "))

contadorVocales = {"a":0, "e":0, "i":0, "o":0, "u":0}

for letra in palabra:
    if (letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u"):
        contadorVocales[letra] += 1

print("En la palabra '","".join(palabra),"' hay: ")
contadorTotal = 0
for vocal, contador in contadorVocales.items():
    print("vocal ",vocal," = ", contador)
    contadorTotal += contador
print("En total: ",contadorTotal," vocales")