import numpy as np

import scipy as sp
from scipy.spatial import distance
from scipy.sparse.linalg import eigs

import fractions


# mostrar decimales en fraccionarios 
np.set_printoptions(formatter={'float':lambda x: str(fractions.Fraction(str(x)).limit_denominator())})

# Eigenvalues, valores y vectore spropios
A = np.matrix([[1, 1, -1], [-1, 3, -1], [-1, 2, 0]])

eigenvalues, eigenvectors= eigs(A)
print("valores propios\n", eigenvalues.real)
print("vectores propios\n", eigenvectors)
print(eigenvectors.shape)

lista=[]
for enum, i in enumerate(eigenvalues.real):
	listaTemp=[0]*len(eigenvalues)
	listaTemp[enum]=i
	lista.append(listaTemp)

# eigenvector es P
D=np.matrix(lista)
print("matrix d\n", D)
print("A * P\n", A*eigenvectors)
print("P * D\n", eigenvectors*D)

print("D is\n",D)

value=A*eigenvectors
print("print last \n",sp.linalg.inv(eigenvectors)*value)