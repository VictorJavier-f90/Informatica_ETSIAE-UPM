# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 11:57:09 2022

@author: javie
"""
import random as rd
import numpy as np
import matplotlib.pyplot as plt
import math

x = rd.uniform(-5,5) 
A = -1.; B = 1. ; C = 2.  
y = A + (B - A)/(1.+math.exp(-C*x))

print(x,y)

N= 100
x = np.linspace(-5.,5,N)
y = A + (B - A)/(1.+np.exp(-C*x))
plt.plot(x,y)
plt.show()

