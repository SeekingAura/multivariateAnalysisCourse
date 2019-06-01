import sys
import os


# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

import matplotlib.pyplot as plt

import pandas as pd

from sklearn.decomposition import PCA

if(len(sys.argv)!=3):
    sys.stderr.write('Usage: "{0}" $csvFileName $IndexOfX1 (csv headers should be must otherThink0, otherThink1, ... , otherThinnkn, "x1", "x2", ..., "xn", "Y")\n'.format(sys.argv[0]))
    os._exit(1)

data = pd.read_csv(sys.argv[1])
# Replace All space in column headers
data.rename(columns=lambda name: name.replace(" ", "_"), inplace=True)

# get column headers such as [keyX1, keyX2, keyX3, ..., keyY]
keyList=data.columns.values
print("Tabla de datos leido\n{}\n".format(data))

X=data[keyList[int(sys.argv[2]):]]
y=data[keyList]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0) 

sc = StandardScaler()  
X_train = sc.fit_transform(X_train)  
X_test = sc.transform(X_test)

pca = PCA(n_components=2) 
X_train = pca.fit_transform(X_train)  
X_test = pca.transform(X_test) 

#The PCA class contains explained_variance_ratio_ which returns the variance caused by 
# each of the principal components. Execute the following line of code to find the "explained variance ratio".

explained_variance = pca.explained_variance_ratio_  


principalDf = pd.DataFrame(data = X_train
             , columns = ['principal component 1', 'principal component 2'])

print(principalDf)

finalDf = pd.concat([principalDf, data[[keyList[0]]]], axis = 1)

print(finalDf)
# print(X_test)