# -*- coding: utf-8 -*-
"""
Conversor altura en metros en pies y pulgadas

@author: javie
"""

altura = 1.88

pies = (altura*100/2.54)//12
pulgadas =(altura*100/2.54)%12

print(str(altura) +' metros son: '+ str(pies) + ' pies y '+
      str(pulgadas) + ' pulgadas')
