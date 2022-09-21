# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 10:16:16 2022

@author: javie
"""

texto_1 = 'cadena de texto'
texto_2 = "cadena de texto"
texto_3 = """ cadena de texto 
 que ocupa varias líneas"""
 
print("La variable 'texto_1' es igual que la variable 'texto_2'")
print(texto_3)

print('Aquí     va un tabulador')
print('Aquí \t va un tabulador')

castigo = 'Escribe 100 veces "No lanzaré aviones en clase"'
texto_1 = "No lanzaré aviones en clase \n"
print(2*texto_1)

texto = "cadena de texto"
print(texto[5:10])

nombre = 'abión'
print(nombre[1])
#nombre[1]='v'
print(nombre)
nombre = nombre[0]+'v'+nombre[2:]
print(nombre)

print('a' < 'b')
print('a' > 'A')
print('abc' < 'abcd')
print('ab' < 'ac')
print('a' > '1')
