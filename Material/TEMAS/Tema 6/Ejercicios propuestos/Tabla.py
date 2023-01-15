# -*- coding: utf-8 -*-
"""
Ejercicio 1 Ficheros-Matplotlib

@author: Víctor Javier
"""

def TablaDeMultiplicar(n):
    nombre_fichero = 'tabla-' + str(n) + '.txt'
    f = open(nombre_fichero, 'w')
    for i in range(1, 11):
        f.write(str(n) + ' x ' + str(i) + ' = ' + str(n * i) + '\n')
    f.close()    

numero = int(input('Introduce un número entero entre 1 y 10: '))
TablaDeMultiplicar(numero)