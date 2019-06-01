# https://www.python-course.eu/linear_discriminant_analysis.php
# https://sebastianraschka.com/Articles/2014_python_lda.htmlimport sys
import os
import sys

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import seaborn as sns

from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA

#Spss convert
import pyreadstat


if __name__=="__main__":
	if(len(sys.argv)!=3):
		sys.stderr.write('Usage: "{0}" $csvFileName $IndexOfX1\n'.format(sys.argv[0]))
		os._exit(1)

	if(".csv" in sys.argv[1]):
		data = pd.read_csv(sys.argv[1])
	else:
		data, meta = pyreadstat.read_sav(sys.argv[1])
	# Replace All space in column headers
	data.rename(columns=lambda name: name.replace(" ", "_"), inplace=True)

	# H -> 1
	# M -> 2
	
	# U -> 1
	# R -> 2

	# get column headers such as [keyX1, keyX2, keyX3, ..., keyY]
	keyList=data.columns.values
	keyTarget=keyList[int(sys.argv[2])]
	keyList=np.delete(keyList, np.where(keyList == keyTarget)[0][0])# Remove target from main list key
	print("TARGET", keyTarget)
	print("keylist", keyList)
	#print("data readed table \n", data)

	dictoNames={}
	indexKey=0
	for i, row in data.iterrows():
		if(not row["Lugar_def"] in list(dictoNames.keys())):
			print(row["Lugar_def"])
			dictoNames[str(row["Lugar_def"])]=indexKey
			indexKey+=1
		data.at[i,"Lugar_def"] = dictoNames.get(row["Lugar_def"])
	data["Lugar_def"]= data["Lugar_def"].astype(str)
	print(dictoNames)
	print("nueva tabla", data)
	model = LDA(n_components=2)
	X_lda = model.fit_transform(data[keyList], data[keyTarget])
	#data["PC1"] = X_lda[:,0]
	#sns.regplot(data = data[["PC1",keyTarget]], x = "PC1",y = keyTarget, fit_reg=False,scatter_kws = {'s':50}, )
	#vis = sns.lmplot(data = data[["PC1","PC2",keyTarget]], x = "PC1", y = "PC2",fit_reg=False, hue = keyTarget,\
	#			 size = 6, aspect=1.5, scatter_kws = {'s':50}, )

	plt.show()

	# Plot values
	# f, ax = plt.subplots(1, 7, figsize=(10,3))

	# # vis1=sns.distplot(data[keyTarget],bins=10, ax= ax[0])
	# vis2=sns.distplot(data[keyList[0]],bins=10, ax= ax[1])
	# vis3=sns.distplot(data[keyList[1]],bins=10, ax=ax[2])
	# vis4=sns.distplot(data[keyList[2]],bins=10, ax= ax[3])
	# vis5=sns.distplot(data[keyList[3]],bins=10, ax=ax[4])
	# vis6=sns.distplot(data[keyList[4]],bins=10, ax=ax[5])
	# vis7=sns.distplot(data[keyList[5]],bins=10, ax=ax[6])
	# plt.show()

	# Plot complete about all
	sns.pairplot(data, hue=keyTarget)
	plt.show()