# -*- coding: utf-8 -*-
"""
Ejercicio 20

@author: Víctor Javier Llorente Lázaro
"""

from Ejercicio18 import f1, f2, f3, f4, f5
from Ejercicio19 import derivada

print(derivada(0.0, 1e-5, f1))
print(derivada(0.0, 1e-5, f2))
print(derivada(0.0, 1e-5, f3))
print(derivada(0.0, 1e-5, f4))
print(derivada(1.0, 1e-5, f5))