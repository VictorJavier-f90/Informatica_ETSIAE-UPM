# -*- coding: utf-8 -*-
"""
Ejercicio 6 estructuras de datos

@author: Víctor Javier
"""

cesta = {}

continuar = True
while continuar:
    item = input("Introduce un artículo: ")
    precio = float(input("Introduce el precio de "+item+": "))
    cesta[item] = precio
    continuar = input("¿Quieres añadir artículos a la lista (Si/No)? ") == "Si"

print("Lista de la compra")
coste = 0.0
for item, precio in cesta.items():
    print(item," : ", precio)
    coste += precio
print("Coste total: ", coste)