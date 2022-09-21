# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 12:54:39 2022

@author: javie
"""
from numpy import real, imag 
from re import split

c = 2 + 3j
print(type(c))
print(c.real)
print(c.imag)

print(real(c))
print(imag(c))


x,y = split(' ',input("Dime dos números:"))
x = float(x)
y = float(y)
print(x,y,x+y)

x,y = input("Dime dos números:").split()
x = float(x)
y = float(y)
print(x,y,x+y)