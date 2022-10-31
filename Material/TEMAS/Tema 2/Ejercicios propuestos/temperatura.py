# -*- coding: utf-8 -*-
"""
Ejercicio 2 condicionales

@author: Víctor Javier
"""

print("CONVERSOR DE TEMPERATURAS")
print("opcion 1: grados Celsius a Kelvin y grados Fahrenheit")
print("opcion 2: grados Fahrenheit a Kelvin y grados Celsius")
print("opcion 3: Kelvin a grados Celsius y grados Fahrenheit")

opcion = int(input("opcion = "))

if (opcion == 1):
    Tc = float(input("temperatura (ºC) = "))
    Tk = Tc + 273.15
    Tf = (9 / 5) * Tk - 459.67
    print(Tc,"ºC = ",Tf,"ºF = ",Tk,"K")
elif (opcion == 2):
    Tf = float(input("temperatura (ºF) = "))
    Tk = (5 / 9) * ( Tf + 459.67 )
    Tc = Tk - 273.15
    print(Tf,"ºF = ",Tc,"ºC = ",Tk,"K")
elif (opcion == 3):
	Tk = float(input("temperatura (K) = "))
	Tc = Tc - 273.15
	Tf = (9 / 5) * Tk - 459.67
	print(Tk,"K = ",Tc,"ºC = ",Tf,"ºF")	
else:
    print("valor de opción no valido")