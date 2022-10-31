# -*- coding: utf-8 -*-
"""
Ejercicio 1 bucles e iteraciones

@author: Víctor Javier
"""

numero= int(input("¿Qué número quieres saber si es primo? "))

if (numero < 2):
    primo = False
elif (numero == 2):
    primo = True
else:
    for i in range(2, numero):
        if (numero % i == 0):
            primo = False
            break
        primo = True
    
if (primo == True):
    print("El número ",numero," es primo")
elif (primo == False):
    print("El número ",numero," no es primo")
else:
    print("Error")