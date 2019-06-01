import sys
import os
import random

# Import required libraries
import pandas as pd

import matplotlib.pyplot as plt
from matplotlib import colors as mcolors


from sklearn.decomposition import FactorAnalysis

if(len(sys.argv)!=3):
    sys.stderr.write('Usage: "{0}" $csvFileName $IndexOfX1 (csv headers should be must otherThink0, otherThink1, ... , otherThinnkn, "x1", "x2", ..., "xn", "Y")\n'.format(sys.argv[0]))
    os._exit(1)

data = pd.read_csv(sys.argv[1])
# Replace All space in column headers
data.rename(columns=lambda name: name.replace(" ", "_"), inplace=True)

# get column headers such as [keyX1, keyX2, keyX3, ..., keyY]
keyList=data.columns.values

# print(data)

transformer = FactorAnalysis(n_components=2, random_state=0)
X_transformed = transformer.fit_transform(data[keyList[int(sys.argv[2]):]])
principalData=pd.DataFrame(data = X_transformed
             , columns = ['principal component 1', 'principal component 2'])


finalDf = pd.concat([principalData, data[[keyList[0]]]], axis = 1)
print(finalDf)



fig = plt.figure(figsize = (8,8))
ax = fig.add_subplot(1,1,1) 
ax.set_xlabel('Principal Component 1', fontsize = 15)
ax.set_ylabel('Principal Component 2', fontsize = 15)
ax.set_title('2 component PCA', fontsize = 20)
targets = data[keyList[0]]

colorsAll = dict(mcolors.BASE_COLORS, **mcolors.CSS4_COLORS)
colorsAll = list(colorsAll.keys())
colors=[]
for i in range(len(targets)):
    colors.append(colorsAll[random.randint(0, len(colorsAll)-1)])


for target, color in zip(targets,colors):
    indicesToKeep = finalDf[keyList[0]] == target
    ax.scatter(finalDf.loc[indicesToKeep, 'principal component 1']
               , finalDf.loc[indicesToKeep, 'principal component 2']
               , c = color
               , s = 50)
ax.legend(targets)
ax.grid()

plt.show()