# https://www.python-course.eu/linear_discriminant_analysis.php
# https://sebastianraschka.com/Articles/2014_python_lda.htmlimport sys
import os
import sys

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

import matplotlib.pyplot as plt
from matplotlib import style
from sklearn.model_selection import train_test_split
style.use('fivethirtyeight')
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

#Spss convert
import pyreadstat

def plot_scikit_lda(X, title, y):
	label_dict = {1: 'uno', 2: 'Dos', 3:'Tres', 4:"Cuatro"}
	ax = plt.subplot(111)
	for label,marker,color in zip(
		range(1,6),('^', 's', 'o', "v", ),('blue', 'red', 'green', "yellow")):

		plt.scatter(x=X[:,0][y == label],
					y=X[:,1][y == label] * -1, # flip the figure
					marker=marker,
					color=color,
					alpha=0.5,
					label=label_dict[label])
		print(label)


	plt.xlabel('LD1')
	plt.ylabel('LD2')

	leg = plt.legend(loc='upper right', fancybox=True)
	leg.get_frame().set_alpha(0.5)
	plt.title(title)

	# hide axis ticks
	plt.tick_params(axis="both", which="both", bottom="off", top="off",  
			labelbottom="on", left="off", right="off", labelleft="on")

	# remove axis spines
	ax.spines["top"].set_visible(False)  
	ax.spines["right"].set_visible(False)
	ax.spines["bottom"].set_visible(False)
	ax.spines["left"].set_visible(False)    

	plt.grid()
	plt.tight_layout
	plt.show()


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
	keyTarget=sys.argv[2]
	keyList=np.delete(keyList, np.where(keyList == keyTarget)[0][0])# Remove target from main list key
	print("TARGET", keyTarget)
	print("keylist", keyList)
	#print("data readed table \n", data)

	
	X = data[keyList].copy()
	# print(X)
	target = data[keyTarget].copy()
	# X_train, X_test, y_train, y_test = train_test_split(X,target,test_size=0.3,random_state=0) 
	# 1. Instantiate the method and fit_transform the algotithm
	LDA = LinearDiscriminantAnalysis(n_components=2) # The n_components key word gives us the projection to the n most discriminative directions in the dataset. We set this parameter to two to get a transformation in two dimensional space.  
	#data_projected = LDA.fit_transform(X_train,target)
	
	
	X_lda_sklearn = LDA.fit_transform(X,target)
	# plot_step_lda()
	plot_scikit_lda(X_lda_sklearn, 'Default LDA via scikit-learn', target)

	
	# print(data_projected.shape)
	# # PLot the transformed data
	# markers = ['s','x','o']
	# colors = ['r','g','b']
	# fig = plt.figure(figsize=(10,10))
	# ax0 = fig.add_subplot(111)
	# for l,m,c in zip(np.unique(y_train),markers,colors):
	# 	ax0.scatter(data_projected[:,0][y_train==l],data_projected[:,1][y_train==l],c=c,marker=m)
	# plt.show()