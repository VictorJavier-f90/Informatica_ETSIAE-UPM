# -*- coding: utf-8 -*-
"""
Ejercicio 3 condicionales

@author: Víctor Javier
"""

from numpy import exp, sin, cos, log10, pi

x = float(input("x = "))

if (x < 0):
	f = exp( -x ) * sin( x**2 )
elif (0 <= x <= pi / 2):
	f = log10( 1 + x**3 ) * cos( x )
elif (x > pi / 2):
	f = ( x - 5 ) / ( 1 + x**2 )
else:
    print("argumento x no valido")
print("f(",x,") = ",f)