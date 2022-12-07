# -*- coding: utf-8 -*-
"""
Ejercicio 1

@author: Víctor Javier Llorente Lázaro
"""

from cmath import sqrt 

def clasificacion(x1,x2,D):
    if (D > 0):
        if (x1.real < x2.real):
            return [x1.real, x2.real]
        else:
            return [x2.real, x1.real]
    elif (D == 0):
        return [x1.real]
    else:
        if (x1.imag > 0 and x2.imag < 0):
            return [[x1.real, x1.imag], [x2.real, x2.imag]]
        else:
            return [[x2.real, x2.imag], [x1.real, x1.imag]]

def ecuacion_grado_2(a,b,c):
    if (a == 0):
        return "El primer coeficiente debe ser distinto de cero"
    else:
        D = b**2 - 4*a*c
        x1 = (-b + sqrt(D)) / (2*a)
        x2 = (-b - sqrt(D)) / (2*a)
        solucion = clasificacion(x1,x2,D)
        return solucion

print(ecuacion_grado_2(0.0, 1.0, 1.0))
print(ecuacion_grado_2(1.0, 1.0, 1.0))
print(ecuacion_grado_2(-1.0, 0.0, 1.0))
print(ecuacion_grado_2(0.5, 1.0, 0.5))