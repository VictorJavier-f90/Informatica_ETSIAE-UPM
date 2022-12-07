# -*- coding: utf-8 -*-
"""
Ejercicio 11

@author: Víctor Javier Llorente Lázaro
"""

def particion(a, b, N):
    return [a + i*(b-a)/N for i in range(N + 1)]