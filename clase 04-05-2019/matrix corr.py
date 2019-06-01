import statistics
import sys
import os
import random

import pandas as pd

import matplotlib.pyplot as plt

from matplotlib import colors as mcolors

if(len(sys.argv)!=3):
    sys.stderr.write('Usage: "{0}" $csvFileName $IndexOfX1 (csv headers should be must otherThink0, otherThink1, ... , otherThinnkn, "x1", "x2", ..., "xn", "Y")\n'.format(sys.argv[0]))
    os._exit(1)

data = pd.read_csv(sys.argv[1])
# Replace All space in column headers
data.rename(columns=lambda name: name.replace(" ", "_"), inplace=True)

# get column headers such as [keyX1, keyX2, keyX3, ..., keyY]
keyList=data.columns.values
print("Tabla de datos leido\n{}\n".format(data))

print(data.corr())
# plt.matshow(data.corr())
corr=data.corr()
size=10
fig, ax = plt.subplots(figsize=(size, size))
ax.matshow(corr)
plt.xticks(range(len(corr.columns)), corr.columns)
plt.yticks(range(len(corr.columns)), corr.columns)

plt.show()

print(data.corr().style.background_gradient())