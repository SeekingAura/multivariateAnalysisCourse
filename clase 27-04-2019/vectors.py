import numpy as np

import scipy as sp
from scipy.spatial import distance
from scipy.sparse.linalg import eigs

import fractions

# mostrar decimales en fraccionarios 
np.set_printoptions(formatter={'float':lambda x: str(fractions.Fraction(str(x)).limit_denominator())})

# A=(1.80, 80)
# B=(1.70, 72)
# C=(1.65, 81)


A = np.array([(180, 80)])
B = np.array([(170, 72)])
C = np.array([(165, 81)])

# Distancia euclideana
distanciaAB=distance.cdist(A, B, 'euclidean')
print("distancia de vector A y B", distanciaAB)

distanciaAC=distance.cdist(A, C, 'euclidean')
print("distancia de vector A y C", distanciaAC)

# Inversa de una matriz
A = np.matrix([[1, 1, 0], [-1, 2, 1], [0, 0, 3]])
AInverse=sp.linalg.inv(A)
ADet=sp.linalg.det(A)
print("A Inversa \n", AInverse)
print("A Determinante \n", ADet)

# Parametro T es la transpuesta
print("matrix final", (sp.linalg.inv(A).T*sp.linalg.det(A)))

print(np.matmul(A, AInverse))


# print(sp.linalg.eig(A)[1]*sp.linalg.eigvals(A))
# a = np.matrix([[3, -1, 4], [3, 4, -1], [2, 1, 1]])
# b = np.array([0, 0, 0])
# print(np.linalg.solve(a,b))

# a = np.matrix([[1, -1, 4], [3, 2, -1], [2, 1, -1]])
# b = np.matrix([[-1, -1, 1], [4, 1, 2], [1, 1, 1]])

# a = np.matrix([[-1, -1, 1], [4, 1, 2], [1, 1, 1]])
# b = np.matrix([[1, 0, 0], [0, -2, 0], [0, 0, 3]])
# print(a*b)
