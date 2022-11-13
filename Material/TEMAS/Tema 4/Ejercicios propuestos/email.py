# -*- coding: utf-8 -*-
"""
Ejercicio 2 funciones en python

@author: Víctor Javier
"""
    
def isEmail(email):
    for caracter in email:
        if (caracter == "@"):
            return True
    else:
        return False


email = input("Ingrese su correo electronico: ")

if isEmail(email):
    print('La dirección de email es valida')
else:
    print('La dirección de email no es valida')