# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 16:27:37 2022

@author: javie
"""

import math
import random as rd
import os
#from math import *
#print(cos(2*pi))
#mkdir('Nueva Carpeta')

"""
print(math.pi)
pi = math.pi 
print(math.cos(2*pi))




print(math.e)

print(rd.randrange(10))

print(math.fabs(-4.87))

print(math.floor(5))
print(math.floor(-2.3))

print(math.ceil(5.1))
print(math.ceil(-2.3))

print(math.trunc(-2.3))


print(math.factorial(6))
print(math.factorial(3))

print(math.gcd(6,9))
print(math.gcd(-36, 12))

print(math.pow(2.0, 1.5))
print(math.pow(-3.2, 0.))
#print(math.pow(-1.0, 0.5))
print(math.pow(math.e,3))

print(math.log(20.0855))
print(math.log(20.0855, 2.))
print(math.log(20.0855, 10))

print(math.log2(20.0855))
print(math.log10(20.0855))

print(math.exp(3.0))

print(math.sqrt(25.0))

# Trigonometricas

x = (math.pi)/3
x_d = math.degrees(x)
x_r = math.radians(x_d)
print(f'{x_r:.3f} radianes son {round(x_d):.2f} grados')
print()
print(f'cos(60º)= {math.cos(x_r):.3f}')
print(f'sen(60º)= {math.sin(x_r):.3f}')
print(f'tan(60º)= {math.tan(x_r):.3f}')
print()
print(f'acos(0.500)= {math.acos(0.5):.3f}')
print(f'asen(0.866)= {math.asin(0.866):.3f}')
print(f'atan(1.732)= {math.atan(1.732):.3f}')
print()

x = 2. 
print(math.cosh(x))
print(math.sinh(x))
print(math.tanh(x))

print(math.acosh(3.7621))
print(math.asinh(3.6268))
print(math.atanh(0.9640))

# Modulo os

ruta = os.getcwd()

print(ruta)

os.mkdir(ruta+'\Prueba')

print(os.listdir(ruta))

os.rename('casting.py', 'conversion_tipo.py')

os.system('copy conversion_tipo.py \
          conversion_tipo_mal.py')
          
os.remove('conversion_tipo_mal.py')

os.rmdir(ruta+'\Prueba')
"""
# Modulo random

rd.seed()

x = rd.randint(1,10)
y = rd.randrange(10) + 1
z = rd.randrange(1,11,2)  

print('Entero entre 1 y 10: ',x)
print('Entero entre 1 y 10: ',y)
print('Impar entre 1 y 10: ',z)

x = rd.random()
y = rd.uniform(2.,2.5)
print('Real entre 0 y 1: ',x)
print('Real entre 2. y 2.5: ',y)






