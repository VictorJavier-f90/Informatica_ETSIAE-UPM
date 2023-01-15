"""
Tema 4. Funciones en Python

@author: Víctor Javier
"""

# Función sinc

import math

def sinc(x):
    if (x == 0.0):
        return 1.0
    else:
        return math.sin(x)/x

a = float(input('Deme un número: '))
print('sinc(',a,') = ',sinc(a))

# Norma L^p de vector en R^2

import numpy as np

def norma(v,p):
    if (p == 'inf'):
        Lp = max(abs(v[0]), abs(v[1]))
    else:
        Lp = (abs(v[0]) ** p + abs(v[1]) ** p) ** (1/p)
    return Lp

def normas(v):
    return norma(v,1), norma(v,2), norma(v,'inf')

w = np.array([5.6, 8.7])
norma1, norma2, normainf = normas(w)
print('norma(w,1) = ',norma(w, 1))
print('norma(w,4) = ',norma(w, 4))
print('L1 = ',norma1)
print('L2 = ',norma2)
print('Linf = ',normainf)

# Variables globales y locales

def f(x):
    def g(x):
        nonlocal y
        y = 3
        return x + y
    
    y = 1    
    x = g(x)
    print('x = ',x)
    print('y = ',y)
    return x

x = 3
y = 2
z = f(x)
print('z = ',z)
print('x = ',x)
print('y = ',y)

# Funciones como argumentos de funciones

def f(x):
    a = 21
    return a*x + b

def g(x):
    b = 3.2
    return a*x + b

a = 20
b = -2.5
print('f(g(1)) = ',f(g(1)))
print('g(f(1)) = ',g(f(1)))

# Función factorial iterativo

def fact(n):
    res = 1
    while n > 1:
        res = res * n
        n -= 1
    return res

n = 5
print(n,'! = ',fact(n))


# Función factorial recurrente

def fact(n):
    if n == 1:
        return n
    return n*fact(n-1)

n = 5
print(n,'! = ',fact(n))

# Uso de modulos

import vectores as mv
import numpy as np

v1 = np.array([5.3, 2.1, 8.6])
v2 = np.array([3.7, 1.2, 7.8])
print('v1 x v2 =',mv.vectorial(v1, v2))
print('norma 2 de v1 = ',mv.norma(v1))
print('norma 8 de v2 = ',mv.norma(p = 8, v = v2))

# ejemplo 1 de subrutina

import operaciones as op

minutos = horas = dias = 0.0
segundos_rest = minutos_rest = horas_rest = 0.0

tiempo = float(input('tiempo total en segundos? '))

args = [minutos, segundos_rest]
op.division(tiempo, 60, args)
minutos = args[0]; segundos_rest = args[1]

args = [horas, minutos_rest]
op.division(minutos, 60, args)
horas = args[0]; minutos_rest = args[1]

args = [dias, horas_rest]
op.division(horas, 24, args)
dias = args[0]; horas_rest = args[1]

print(dias, horas_rest, minutos_rest, segundos_rest)

# ejemplo 2 de subrutina

import operaciones as op

x = 1; y = 2
args = [x, y]
op.intercambia(args)
x = args[0]; y = args[1]
print(x, y)
