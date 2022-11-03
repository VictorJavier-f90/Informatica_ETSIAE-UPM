"""
Tema 3. Estructura de datos

@author: Víctor Javier
"""

#############
# Conjuntos #
#############

# Acceder a los elementos del conjunto
s = {5, 4, 6, 8, 8, 1}
for elemento in s:
    print(elemento)

# Operaciones sobre conjuntos
s1 = {1, 2, 3, 4, 5, 6}
s2 = {2, 4, 6, 8, 10}
s3 = {1, 2, 3}
s4 = {4, 5, 6}
print("La longitud del conjunto s1 es ",len(s1))
print("La diferencia entre s1 y s2 es ",s1 - s2)
print("La diferencia simétrica entre s1 y s2 es ",s1 ^ s2)
print("La intersección entre s1, s2, s3, y s4 es ",s1 & s2 & s3 & s4)
print("La unión entre s1, s2, y s3 es ",s1 | s2 | s3)
print("¿s3 es subconjunto de s1? ",s3 < s1)
print("¿Esta 8 en s2 y no en s1? ",8 in s2 and 8 not in s1)

##########
# Listas #
##########

# Acceso a los elemento de una lista
pares = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
print(pares[1     ])
print(pares[ :3   ])
print(pares[0:5: 2]) 
print(pares[9:0:-1])

# Concatenar
pares = [0, 2, 4, 6, 8]
impares = [1, 3, 5, 7, 9]
numeros = pares + impares
print(numeros)

# Repetir
pares = [0, 2, 4, 6, 8]
pares = pares * 2 # pares *= 2
print(pares)

# Comparación
pares = [0, 2, 4, 6, 8]
impares = [1, 3, 5, 7, 9]
print(pares > impares, pares >= impares)
print(pares < impares, pares <= impares)
print(pares == impares, pares != impares)

# Bucles
pares = [0, 2, 4, 6, 8]
impares = [1, 3, 5, 7, 9]
numeros = pares + impares
for valor in numeros:
    if valor in pares:
        print(valor," es par")
    else:
        print(valor," es impar")
        
# Crear lista de cuadrados
N = 7
cuadrados = [0] * N
for i in range(N):
    cuadrados[i] = i ** 2
print(cuadrados) 

# Crear lista de cuadrados (manera pythoniana)
N = 7
cuadrados = [i ** 2 for i in range(N)]
print(cuadrados) 

# Entrada de lista
datos = input("Dame los números: ").split()
media = 0.0
for numero in datos:
    media += float(numero)
media /= len(datos)
print("La media de los números es: ",media)

# Copia profunda
cuadrados = [i ** 2 for i in range(4)]
cuadrados_cp = cuadrados
print(cuadrados, cuadrados_cp)
del cuadrados[2]
print(cuadrados, cuadrados_cp)

# Copia superficial
cuadrados = [i ** 2 for i in range(4)]
cuadrados_cp = cuadrados[:]
print(cuadrados, cuadrados_cp)
del cuadrados[2]
print(cuadrados, cuadrados_cp)

################
# Diccionarios #
################

d = {"nombre": "Felipe", "edad": 54, "DNI": 15264168}
# Imprime los key del diccionario
for llave in d:
    print(llave)
# Imprime los value del diccionario
for llave in d:
    print(d[llave])
# Imprime los key y value del diccionario
for llave, valor in d.items():
    print(llave, valor)
# Nueva llave
d["direccion"] = ("C/ Falsa 123", "C/ lacalle 25") 
