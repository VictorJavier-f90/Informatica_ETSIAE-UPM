# -*- coding: utf-8 -*-
"""
Escribe un código que pida un número entero por teclado 
estrictamente menor que 1000.

Primero hallará el número de cifras que tiene y lo mostrara por pantalla:
El numero:  ____ tiene _ cifras
Lo descompodrá en unidades (U), decenas (D) y centenas (C) y lo 
mostrará por pantalla
CDU     

"""

numero = int(input('Introduce un numero entero menor que 1000: '))
numero_str = str(numero)
print(numero, 'tiene: ', len(numero_str), 'cifras')
C = numero//100
D = (numero%100)//10
U = (numero%100)%10

numero_str2 = str(C)+str(D)+str(U)
