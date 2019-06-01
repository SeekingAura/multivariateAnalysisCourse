# https://github.com/MaxHalford/prince

import statistics
import sys
import os
import random

import pandas as pd


import matplotlib.pyplot as plt

from matplotlib import colors as mcolors

import prince


if(len(sys.argv)!=3):
    sys.stderr.write('Usage: "{0}" $csvFileName $IndexOfX1 (csv headers should be must otherThink0, otherThink1, ... , otherThinnkn, "x1", "x2", ..., "xn", "Y")\n'.format(sys.argv[0]))
    os._exit(1)

data = pd.read_csv(sys.argv[1])
# Replace All space in column headers
data.rename(columns=lambda name: name.replace(" ", "_"), inplace=True)

# get column headers such as [keyX1, keyX2, keyX3, ..., keyY]
keyList=data.columns.values
# print("Tabla de datos leido\n{}\n".format(data))
#print(keyList)
indexMainKey=int(sys.argv[2])

X=data.copy()

del X[keyList[0]]

X.rename(index = pd.Series(data[keyList[0]]), inplace=True)
#principalDf = pd.DataFrame(data = data[keyList[indexMainKey:]]
#             , columns = pd.Series(keyList[indexMainKey:]), index=pd.Series(data[keyList[0]]))

print(X)

ca = prince.CA(
     n_components=3,
     n_iter=25,
     copy=True,
     check_input=True,
     engine='auto',
     random_state=None
)

X.columns.rename('Caracteristicas', inplace=True)
X.index.rename('Ciudades', inplace=True)

ca = ca.fit(X)
print(ca.row_coordinates(X))
print(ca.column_coordinates(X))

print(ca.eigenvalues_ )

print(ca.total_inertia_)

print(ca.explained_inertia_)

ax = ca.plot_coordinates(
     X=X,
     ax=None,
     figsize=(6, 6),
     x_component=0,
     y_component=1,
     show_row_labels=True,
     show_col_labels=True
)

# plt.show()