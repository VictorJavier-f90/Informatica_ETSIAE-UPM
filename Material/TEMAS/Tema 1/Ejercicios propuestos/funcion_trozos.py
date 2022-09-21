# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 12:11:36 2022

@author: javie
"""
import math

x = 0.2

pi = math.pi

if (x<=-1.):
    y = math.exp(-x)
elif(x<1.):
    y = math.log((1+x)/(1-x))
else:
    y = math.cos(pi*x)

print(x,y)

