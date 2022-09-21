# -*- coding: utf-8 -*-
"""
Escribe un programa que pida el precio del litro de gasolina en euros y el 
número de litros que ha repostado un vehículo. 
A continuación mostrará por pantalla el precio del repostaje antes y 
después de aplicarle el descuento de 20 céntimos por litro. 

@author: javie
"""

precio_litro = float(input('Precio del litro de gasolina: '))
litros_rep   = float(input('Número de litros repostados: '))

descuento = litros_rep * 0.2
print('El precio antes del descuento es: ', precio_litro*litros_rep)
print('El precio después del descuento es: ', precio_litro*litros_rep-descuento)