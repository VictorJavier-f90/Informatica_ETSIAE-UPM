# -*- coding: utf-8 -*-
"""
Ejercicio 5 funciones en python

@author: Víctor Javier
"""
    
def sumatorio(a, r, N):
    Sn = 0.0
    for k in range(N + 1):
        Sn += a * r ** k
    S = 0.0
    k = 0
    if (abs(r) < 1):
        convergencia = True
        while (abs(a * r ** k) >= 1.0e-15):
            S += a * r ** k
            k = k + 1
    else:
        convergencia = False  
    return Sn, S, convergencia

a, r = [float(numero) for numero in input("Introduzca a y r de la serie: ").split()]
N = int(input("Introduzca N de la serie: "))

sumaFinita, sumaInfinita, convergencia  = sumatorio(a, r, N)
print("La suma de ",N," términos es ",sumaFinita)
if (convergencia == True):
    print("La suma infinita es ",sumaInfinita)
else:
    print("La suma infinita no converge")
