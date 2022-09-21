# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 13:11:06 2022

@author: javier
"""

print(type(2))
print(type(2.0))
print(type('a'=='b'))
print(type('cadena'))

var_1 = 2
var_2 = 2.0
print('var_1 es ',type(var_1))
print('var_2 es ',type(var_2))

var_1 = var_2
print('var_1 es ',type(var_1))

print(int(7.2))
print(int(7.9))
print(int(-7.9))
print(int('3'))
print(int(3==2))
print(int('a'=='a'))

print(float(7))
print(float(-7.9))
print(float('3'))
print(float(3==2))
print(float('a'=='a'))

print(str(7))
print(str(-7.9))
print(str('casa'))
print(str(3==2))
print(str('a'=='a'))

print(complex(7))
print(complex(-7.9))
print(complex('3'))
print(complex(3==2))
print(complex('a'))

print(bool(7))
print(bool(-0.0))
print(bool(''))
print(bool(None))
print(bool('a'))

