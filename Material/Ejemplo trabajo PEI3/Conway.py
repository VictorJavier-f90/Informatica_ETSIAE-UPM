# -*- coding: utf-8 -*-
"""
Juego de la vida de Conway

El tablero es un array de NumPy, donde 0 significa célula muerta y 1 célula
viva.

@author: Víctor Javier Llorente Lázaro
"""

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
# Importar librerías
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

# Librería numérica
import numpy as np
# Librería de gráficos
import matplotlib.pyplot as plt
# Librería de colores
from matplotlib.colors import ListedColormap

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
# Definición de funciones
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

def vecindario(b):
    """
    Array de células vivas en el vecindario
    """
    N = b.shape[0]
    M = b.shape[1]
    vecinos = np.zeros((N, M), dtype = int)
    for i in range(N):
        for j in range(M):
            if (i == 0 and j == 0): 							
				# Esquina superior izquierda
                vecinos[i,j] = np.sum(b[i  :i+2,j  :j+2]) - b[i,j]
            elif (i == N-1 and j == 0): 						
				# Esquina superior derecha
                vecinos[i,j] = np.sum(b[i-1:i  ,j  :j+2]) - b[i,j]
            elif (i == 0 and j == M-1): 						
				# Esquina inferior izquierda
                vecinos[i,j] = np.sum(b[i  :i+2,j-1:j  ]) - b[i,j]
            elif (i == N-1 and j == M-1): 						
				# Esquina inferior derecha
                vecinos[i,j] = np.sum(b[i-1:i  ,j-1:j  ]) - b[i,j]
            elif (j == 0): 										
				# Contorno superior
                vecinos[i,j] = np.sum(b[i-1:i+2,j  :j+2]) - b[i,j]
            elif (i == 0): 										
				# Contorno izquierda
                vecinos[i,j] = np.sum(b[i  :i+2,j-1:j+2]) - b[i,j]
            elif (i == N-1): 									
				# Contorno derecha
                vecinos[i,j] = np.sum(b[i-1:i  ,j-1:j+2]) - b[i,j]    
            elif (j == M-1):									
				# Contorno inferior
                vecinos[i,j] = np.sum(b[i-1:i+2,j-1:j  ]) - b[i,j]
            else:											
				# Interno
                vecinos[i,j] = np.sum(b[i-1:i+2,j-1:j+2]) - b[i,j]
    return vecinos

def paso(b):
    """
    Paso en el juego de la vida de Conway
    """
    v = vecindario(b)
    bc = b[:,:]
    N = bc.shape[0]
    M = bc.shape[1]
    for i in range(N):
        for j in range(M):
            if v[i, j] == 3 or (v[i, j] == 2 and bc[i, j] == 1):
                bc[i, j] = 1
            else:
                bc[i, j] = 0
    return bc

def imprimir(b,gen):
    """
    Imprimo el dominio de las celulas
    """
    plt.title("Generación: " + str(gen))
    cmap = ListedColormap(["green", "orangered"])
    plt.imshow(b, cmap=cmap)
    plt.show()
    
def dominio(p):
    """
    Dimensiones del dominio
    """
    if (p == "nave"):
        return 8,8
    elif (p == "oscilante" or p == "estable"):
        return 13,13
    elif (p == "vj"):
        return 9,14
    elif (p == "upm"):
        return 15,24
    
def inicial(p,b):
    """
    Patrón de celulas vivas
    """
    if (p == "nave"):
        b[1,1:4] = 1
        b[2,1  ] = 1
        b[3,2  ] = 1
    elif (p == "oscilante"):
        b[6   ,2:5 ] = 1
        b[6   ,8:11] = 1
        b[2:5 ,6   ] = 1
        b[8:11,6   ] = 1
    elif (p == "estable"):
        b[5:7,5:7] = 1
    elif (p == "vj"):
        b[2:4,2    ] = 1 
        b[4:6,3    ] = 1
        b[6  ,4    ] = 1
        b[4:6,5    ] = 1
        b[2:4,6    ] = 1
        b[2  ,9 :12] = 1
        b[3:6,11   ] = 1
        b[6  ,9 :11] = 1
        b[5  ,8    ] = 1
    elif (p == "upm"):
        b[5:10,5    ] = 1
        b[9   ,6 :8 ] = 1
        b[5:10,8    ] = 1
        b[5:10,10   ] = 1
        b[5   ,11:13] = 1
        b[7   ,11:13] = 1
        b[6   ,12   ] = 1
        b[5:10,14   ] = 1
        b[6   ,15   ] = 1
        b[7   ,16   ] = 1
        b[6   ,17   ] = 1
        b[5:10,18   ] = 1
    return b

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
# Programa principal
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

# Elección del problema
problema = "upm"

# Parámetros del problema
GENERACIONES = 60
N,M = dominio(problema)

# Construimos el tablero
tablero = np.zeros((N, M), dtype=int)

# Estado celular inicial
tablero = inicial(problema,tablero)

# Bucle
for generacion in range(GENERACIONES + 1):
    imprimir(tablero,generacion)
    tablero = paso(tablero)

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
# Final del código
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------