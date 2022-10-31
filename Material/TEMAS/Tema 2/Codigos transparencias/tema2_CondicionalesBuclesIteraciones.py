"""
Tema 2. Sentencias de Control de Flujo

@author: víctor javier
"""

###############
# Iteraciones #
###############

# if 

numero = int(input("Escribe un número:"))

if (numero > 5):
    print("el número ",numero," es mayor que cinco")
	
# if versión 2
nombre = input(“Dime tu nombre: ”)
numero = int(input(“Escribe un número: ”))

if (numero % 2 == 0):
    print(“Hola ”,nombre)	
    print(“el número ”,numero,” es par”)

# if con else
numero = int(input(“Escribe un número: ”))

if (numero > 5):
    print(“el número ”,numero,” es mayor que cinco”)
else:
    print(“el número ”,numero,” es menor que cinco”)
	
# if con else
numero = int(input(“Escribe un número: ”))

if (numero > 5):
    print(“el número ”,numero,” es mayor que cinco”)
else:
    print(“el número ”,numero,” es menor que cinco”)
	
	
##########
# Bucles #
##########

# Bucles tipo while

numero = 1
while (numero < 10):
    print(numero)
    numero +=1

# Dos condiciones con operadores lógico
print("Dos condiciones con operadores lógicos")
numero = 1
while (numero <10 or numero%2==0):
    print(numero)
    numero +=1
else:
    print(numero, "es un impar mayor de 9")
    
#Con variables de tipo string
print("Con palabras")
palabra = "aeropuerto"
letra = 0
while letra<len(palabra):
    print(palabra[letra])
    letra+=1
    
# Bucles for
"""
 General FOR variable IN objeto
 De momento solo vamos a trabajar con bucles en variables enteras
"""

""" 
Bucle for con valor final
"""
print("Bucle for con valor final")
for i in range(10):
    print(i)
print("Bucle for con valor inicial-final")   
for i in range(5,10):
    print(i)    

print("Bucle for con valor inicial-final-salto")
for i in range (1,10,2):
    print(i)
    
print("Bucle for regresivo con valor final-inicial-salto(negativo)")
for i in range (10,1,-1):
    print(i)

print("Bucle for con sentencias de control de ejecución")
for i in range(1,10):
    if (i==5):
        break
    print(i)
    
for i in range(1,10):
    if (i>=5 and i<8):
        print("Con los números 5,6 y 7 salto las órdenes debajo de continue ")
        continue
    print(i)

"""
Excepción al uso del for en enteros
"""
#Con variables de tipo string
print("Con palabras")
palabra = "aeropuerto"
for letra in palabra:
    print(letra)
       
    