import statistics
import sys
import os

import pandas as pd
import matplotlib.pyplot as plt

from matplotlib import colors as mcolors

from scipy.cluster.hierarchy import dendrogram, linkage  

import scipy.cluster.hierarchy as shc

from sklearn.cluster import AgglomerativeClustering


# normalize
from sklearn import preprocessing


#Spss convert
import pyreadstat

def normalize(df):
	result = df.copy()
	for feature_name in df.columns:
		max_value = df[feature_name].max()
		min_value = df[feature_name].min()
		print(df[feature_name])
		print(df[feature_name].max())
		print(df[feature_name].min())
		result[feature_name] = (df[feature_name] - min_value) / (max_value - min_value)
	return result

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

	# get column headers such as [keyX1, keyX2, keyX3, ..., keyY]
	keyList=data.columns.values[int(sys.argv[2]):]
	print("data readed table \n", data)
	
	#x = data.values #returns a numpy array
	#min_max_scaler = preprocessing.MinMaxScaler()
	#x_scaled = min_max_scaler.fit_transform(x)
	#data = pd.DataFrame(x_scaled)

	data=normalize(data[keyList[1:]])
	print(data)
	data=data.iloc[:, 1:6].values
	

	# Dendogram - Requiere  a fit
	plt.title("Customer Dendograms")  
	dend = shc.dendrogram(shc.linkage(data, method='ward')) 
	
	cluster = AgglomerativeClustering(n_clusters=5, affinity='euclidean', linkage='ward')  
	cluster.fit_predict(data)

	#plt.scatter(data[:,0], data[:,1], c=cluster.labels_, cmap='rainbow') 
	
	plt.show()


	#linked = linkage(data[keyList], 'single')
	#dendrogram(linked,  
	#        orientation='top',
	#        distance_sort='descending',
	#        show_leaf_counts=True)
	#plt.show()  

