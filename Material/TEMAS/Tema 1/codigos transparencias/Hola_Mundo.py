# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 19:13:53 2022

Primer programa de todo curso de programación en cualquier lenguaje.
Escribir por pantalla "Hola Mundo"
"""
print('Hola Mundo')

a = 7
print(type(a))
if (a == 7):
    print('a vale:', a)


def operaciones(a, b):
    x = a+b
    y = a-b
    return x, y


x, y = operaciones(3, 4)
print(x, y)
