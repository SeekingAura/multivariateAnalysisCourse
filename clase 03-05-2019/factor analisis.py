import sys
import os

# Import required libraries
import pandas as pd

import matplotlib.pyplot as plt

from sklearn.decomposition import FactorAnalysis

if(len(sys.argv)!=3):
    sys.stderr.write('Usage: "{0}" $csvFileName $IndexOfX1 (csv headers should be must otherThink0, otherThink1, ... , otherThinnkn, "x1", "x2", ..., "xn", "Y")\n'.format(sys.argv[0]))
    os._exit(1)

data = pd.read_csv(sys.argv[1])
# Replace All space in column headers
data.rename(columns=lambda name: name.replace(" ", "_"), inplace=True)

# get column headers such as [keyX1, keyX2, keyX3, ..., keyY]
keyList=data.columns.values[int(sys.argv[2]):]

# print(data)

transformer = FactorAnalysis(n_components=2, random_state=0)
X_transformed = transformer.fit_transform(data[keyList])
principalData=pd.DataFrame(data = X_transformed
             , columns = ['principal component 1', 'principal component 2'])
print(principalData)