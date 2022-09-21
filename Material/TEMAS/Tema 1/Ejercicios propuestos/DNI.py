# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 11:39:18 2022

@author: javie
"""

Letra_DNI ='TRWAGMYFPDXBNJZSQVHLCKE'
DNI = int(input('Dame tu número de DNI:'))
print('La letra correspondiente al número: ',DNI, ' es:', Letra_DNI[DNI%23])
