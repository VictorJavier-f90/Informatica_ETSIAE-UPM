"""
Tema 5. Vectores y Matrices
@author: Víctor Javier
"""

# Listas
x = [1, 2, 3, ['p', 'q', [5, 6, 7]]]
print(x[3][0])
print(x[3][2][0]) 
print(x[3][2][2])

# Sumar dos listas
v1 = [1, 2, 3]
v2 = [4, 5, 6]
v3 = v1 + v2
print(v3)




# Importar librería numpy
import numpy as np

# Operaciones numéricas
# Sumar dos arrays
v4 = np.array([1, 2, 3])
v5 = np.array([4, 5, 6])
v6 = v4 + v5
print(v6)
# Producto escalar
p = np.dot(v4, v5)
print(p)
# Producto vectorial
v7 = np.cross(v4, v5)
print(v7)
# Producto matricial
m1 = np.array([[8, 14, -6], [12, 7, 4], [-11, 3, 21]])
m2 = np.array([[5, 1, 3], [1, 1, 1], [1, 2, 1]])
m3 = np.matmul(m1,m2)
print(m3)

# Operaciones sobre arrays
# Reformular array
v8 = np.array([2.0, 4.3, 5.2, 9.3, 6.8, 5.7])
m4 = np.reshape(v8,(2,3))
print(m4)
# Tamaño array
m5 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
tam = np.shape(m5)
print(tam)
# Vector espaciado
a = np.arange(5)
b = np.arange(1, 9, 2)
print(a)
print(b)
# Matriz de unos
U = np.ones((3, 3))
print(U)
# Matriz de ceros
C = np.zeros((3, 3))
print(C)
# Matriz identidad
I = np.eye(3)
print(I)
# Matriz diagonal
v = np.array([1.0, 2.0, 3.0])
D = np.diag(v)
print(D)

# Secciones de arrays
# Vectores
v9 = np.array([3.2, 6.3, 1.3, 9.1, 6.5, 4.1, 4.2, 1.6, 5.4, 9.0])
print(v9[0:9:2])
print(v9[ : :2])
print(v9[ :7:3])
print(v9[4: :3])
print(v9[6:   ])
print(v9[ :5  ])
# Matrices
v10 = (np.array([3, 6, 1, 9, 6, 4, 4, 6, 5, 9, 
       2, 4, 6, 5, 9, 6, 1, 3, 2, 8]))
m6 = np.reshape(v10, (5, 4))
print(m6[0:3,0:2])
print(m6[3:,1:])
print(m6[3,:])

# Asignación matriz
m7 = np.zeros((5, 4))
m7[0,:] = np.array([3, 6, 1, 9])
m7[1,:] = np.array([6, 4, 4, 6])
m7[2,:] = np.array([5, 9, 2, 4])
m7[3,:] = np.array([6, 5, 9, 6])
m7[4,:] = np.array([1, 3, 2, 8])
print(m7)
