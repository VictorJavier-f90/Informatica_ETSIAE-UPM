# -*- coding: utf-8 -*-
"""
Ejercicio 21

@author: Víctor Javier Llorente Lázaro
"""

from Ejercicio11 import particion
from Ejercicio18 import f1
from Ejercicio19 import derivada

a = 0
b = 1
N = 10
h = 1e-5

x = particion(a, b, N)
y = [derivada(x[i], h, f1) for i in range(N + 1)]

print(y)