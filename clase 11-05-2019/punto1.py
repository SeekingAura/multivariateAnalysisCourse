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


#Spss convert
import pyreadstat

if __name__=="__main__":

	if(len(sys.argv)!=3):
		sys.stderr.write('Usage: "{0}" $csvFileName $IndexOfX1 (csv headers should be must otherThink0, otherThink1, ... , otherThinnkn, "x1", "x2", ..., "xn", "Y")\n'.format(sys.argv[0]))
		os._exit(1)

	if(".csv" in sys.argv[1]):
		data = pd.read_csv(sys.argv[1])
	else:
		data, meta = pyreadstat.read_sav(sys.argv[1])
	# Replace All space in column headers
	data.rename(columns=lambda name: name.replace(" ", "_"), inplace=True)

	# get column headers such as [keyX1, keyX2, keyX3, ..., keyY]
	keyList=data.columns.values
	print("Tabla de datos leido\n{}\n".format(data))

	indexForNames=int(sys.argv[2])


	features = keyList[indexForNames:]
	# Separating out the features
	# Separating out the features
	x = data.loc[:, features].values

	# Separating out the target, keylist[0] is target colum
	y = data.loc[:, [keyList[0]]].values

	sc = StandardScaler()  
	x = sc.fit_transform(x)  
	# X_test = sc.transform(X_test)

	pca = PCA(n_components=2) 
	principalComponents = pca.fit_transform(x)  

	#The PCA class contains explained_variance_ratio_ which returns the variance caused by 
	# each of the principal components. Execute the following line of code to find the "explained variance ratio".

	explained_variance = pca.explained_variance_ratio_  


	principalDf = pd.DataFrame(data = principalComponents
				, columns = ['principal component 1', 'principal component 2'])

	print(principalDf)

	finalDf = pd.concat([principalDf, data[[keyList[0]]]], axis = 1)

	print(finalDf)
	# print(X_test)

	

	fig = plt.figure(figsize = (8,8))
	ax = fig.add_subplot(1,1,1) 
	ax.set_xlabel('Principal Component 1', fontsize = 15)
	ax.set_ylabel('Principal Component 2', fontsize = 15)
	ax.set_title('2 component PCA', fontsize = 20)
	targets = data[keyList[0]]

	for i in ["ghostwhite", "floralwhite", "white", "whitesmoke"]:
		colorsAll.remove(i)
	for i in range(len(targets)):
		while True:
			colorTemp=colorsAll[random.randint(0, len(colorsAll)-1)]	
			if not colorTemp in colors:
				colors.append(colorTemp)
				break


	for target, color in zip(targets,colors):
	    indicesToKeep = finalDf[keyList[0]] == target
	    ax.scatter(finalDf.loc[indicesToKeep, 'principal component 1']
	               , finalDf.loc[indicesToKeep, 'principal component 2']
	               , c = color
	               , s = 50)
	ax.legend(targets)

	# print(keyList[1])
	# print(keyList[2])

	# fig, axs = plt.subplots(1, 1, constrained_layout=True)
	# fig.suptitle("Graficas", fontsize=16)

	# axs.set_title(keyList[1]+" vs "+keyList[2])
	# axs.scatter(data[keyList[1]], data[keyList[2]], color="red")
	# axs.grid()
	# axs.set_xlabel(keyList[1])
	# axs.set_ylabel(keyList[2])


	plt.show()