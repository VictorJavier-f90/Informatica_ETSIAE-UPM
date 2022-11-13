import numpy as np


# producto vectorial

pv = np.array([0.0, 0.0, 0.0])
def vectorial(u,v):
    pv[0] = u[1] * v[2] - u[2] * v[1]
    pv[1] = u[2] * v[0] - u[0] * v[2]
    pv[2] = u[0] * v[1] - u[1] * v[0]
    return pv

# norma Lp

def norma(v, p = 2):
    if (p == 'inf'):
        Lp = max(abs(v))
    else:
        Lp = sum(abs(v) ** p) ** (1.0 / float(p))
    return Lp 
            