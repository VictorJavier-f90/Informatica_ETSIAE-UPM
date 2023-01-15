"""
Tema 6. Ficheros-Matplotlib

@author: Víctor Javier
"""

# Creación de un fichero
f = open("test.txt",mode = "w")
f.write("mi primer fichero\n")
f.write("Este fichero\n\n")
f.write("contiene tres lineas\n")
f.close()

# Creación de un fichero 2
f = open("primos.txt",mode = "w")
f.write("primeros 100 números primos\n")
for i in range(2, 101):
    primos = True
    for j in range(2,i):
        if (i == j):
           break
        elif (i % j == 0):
           primos = False
        else:
           continue
    if (primos == True):
        f.write(str(i) + " ")
f.close()

# Lectura de un fichero
f = open("primos.txt",mode = "r")
contenidos = f.readlines()
f.close()

# Dibujo sin(x) y cos(x)
from numpy import arange, pi, sin, cos
from matplotlib.pyplot import subplots, plot, show, legend, axis, grid, xlabel, title

x = arange(-pi, pi, 0.1)
y1 = sin(x)
y2 = cos(x)

fig, ax = subplots()

ax.plot(x, y1, label="sin(x)")
ax.plot(x, y2, label="cos(x)")

legend()
axis([-pi, pi, -1, 1])
grid()
xlabel("x")
title("Funciones trigonométricas")

show()

# Dibujo de contorno
from numpy import linspace, meshgrid
from matplotlib.pyplot import subplots, contourf, show, xlabel, ylabel

x = linspace(-2.0, 2.0, 100)
y = linspace(-2.0, 2.0, 100)
x, y = meshgrid(x, y)
z = x**2 + y**2

fig, axs = subplots()

axs.contourf(x, y, z)

xlabel("x")
ylabel("y")

show()