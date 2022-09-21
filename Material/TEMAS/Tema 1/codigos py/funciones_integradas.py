# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 10:25:47 2022

@author: javie
"""
#import math

print(abs(-2.4))
print(abs(-7))
print(abs(1+1j))

print(bin(7))
print(oct(36))
print(hex(18))

print(divmod(32,5))
print(divmod(32.2,5.1))

print(max(12,3,-4,67,0,3))
print(min(3.2,8,-5.0,6.3))

print(round(6.5))
print(round(-3.234))
print(type(round(6.6)))

print(len('hola'))
print(len('mensaje de texto'))

print(max('a', 'A', '1', 'avión'))
print(min('a', 'A', '1', 'avión'))

mensaje = 'Esto es una cadena de caracteres'
posicion = mensaje.find('una')
print(posicion)

posicion = mensaje.find('melón')
print(posicion)

nombre = 'Juan'
print(nombre.upper())
print('hola'.upper())

print(nombre.lower())
print(nombre)
print(nombre.capitalize())

print('hola'.capitalize())

mensaje = "Soy estudiante de instituto"
mensaje.replace("instituto", "universidad")
print(mensaje)

mensaje = "Soy estudiante de instituto"
mensaje_1 = mensaje.replace("instituto", "universidad")
print(mensaje_1)

mensaje_2 = mensaje_1.replace("alumno", "profesor")
print(mensaje_2)

nombre = 'patata'
print(nombre.replace("a","o"))
print(nombre.replace("a","o",2))

#print(all(['a'=='a', 4 < 8, 0]))
#print(any(['a'=='a', 4 < 8, 0]))
