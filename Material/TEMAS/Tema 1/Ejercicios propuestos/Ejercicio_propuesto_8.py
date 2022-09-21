# -*- coding: utf-8 -*-
"""
Escribe un código que use el módulo math y el módulo random. El programa debe:

Generar un valor aleatorio en el intervalo  –pi y pi , calcular su coseno y 
escribirlo por pantalla.
Generar un entero aleatorio entre 0 y 360. Convertir el valor a radianes, 
calcular el seno y escribirlo por pantalla. 
Generar 3 números enteros: a,b,c entre 0 y 7. Con esos número formará el 
entero en base octal abc que convertirá a base decimal. 
Por pantalla saldrán ambos números.

"""

import math
import random as rd

pi = math.pi
x = rd.uniform(-pi,pi)

print('coseno de ', x, 'es: ', math.cos(x))

y = rd.randrange(361)
x = math.radians(y)

print('seno de ', x, 'es: ', math.sin(x))

a = rd.randrange(8)
b = rd.randrange(8)
c = rd.randrange(8)

octal = str(a)+str(b)+str(c)
decimal = a*8**2 + b*8 + c
print('el numero en base 8:', octal, 'es el decimal ', decimal)

octal = str(a*100+b*10+c)
decimal = int(octal, 8)
print('el numero en base 8:', octal, 'es el decimal ', decimal)
