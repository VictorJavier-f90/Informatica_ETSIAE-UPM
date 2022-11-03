# -*- coding: utf-8 -*-
"""
Ejercicio 4 estructuras de datos

@author: Víctor Javier
"""

cadena = input("Dame una cadena de caracteres: ")

vocales = set("aeiou")
s = set()
for caracter in cadena:
    if caracter in vocales:
        s.add(caracter)
    else:
        pass

if (len(s) == len(vocales)):
    print("Todas las vocales están presentes")
else:
    print("Todas las vocales excepto "," ".join(s ^ vocales)," están presentes")
