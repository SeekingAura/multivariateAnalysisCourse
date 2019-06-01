# https://towardsdatascience.com/pca-using-python-scikit-learn-e653f8989e60
# Import Standard Python libraries
import statistics
import sys
import os
import random

import pandas as pd

from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

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

indexForNames=int(sys.argv[2])


features = keyList[indexForNames:]
# Separating out the features
x = data.loc[:, features].values
# Separating out the target
y = data.loc[:,[keyList[0]]].values#target
# Standardizing the features
x = StandardScaler().fit_transform(x)


pca = PCA(n_components=3, iterated_power=25)
principalComponents = pca.fit_transform(x)
principalDf = pd.DataFrame(data = principalComponents
             , columns = ['principal component 1', 'principal component 2', 'principal component 3'])

finalDf = pd.concat([principalDf, data[[keyList[0]]]], axis = 1)

print(finalDf)

# fig = plt.figure(figsize = (8,8))
# ax = fig.add_subplot(1,1,1) 
# ax.set_xlabel('Principal Component 1', fontsize = 15)
# ax.set_ylabel('Principal Component 2', fontsize = 15)
# ax.set_title('2 component PCA', fontsize = 20)
# targets = data[keyList[0]]

# colorsAll = dict(mcolors.BASE_COLORS, **mcolors.CSS4_COLORS)
# colorsAll = list(colorsAll.keys())
# colors=[]
# for i in range(len(targets)):
#     colors.append(colorsAll[random.randint(0, len(colorsAll)-1)])


# for target, color in zip(targets,colors):
#     indicesToKeep = finalDf[keyList[0]] == target
#     ax.scatter(finalDf.loc[indicesToKeep, 'principal component 1']
#                , finalDf.loc[indicesToKeep, 'principal component 2']
#                , c = color
#                , s = 50)
# ax.legend(targets)
# ax.grid()

# plt.show()