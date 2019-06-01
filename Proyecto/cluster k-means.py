import statistics
import sys
import os

import pandas as pd
import matplotlib.pyplot as plt

from matplotlib import colors as mcolors

# import KMeans
from sklearn.cluster import KMeans

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

	# get column headers such as [keyX1, keyX2, keyX3, ..., keyY]
	keyList=data.columns.values[int(sys.argv[2]):]
	print("data readed table \n", data)
	# create kmeans object
	kmeans = KMeans(n_clusters=4)
	# fit kmeans object to data
	kmeans.fit(data[keyList])
	# print location of clusters learned by kmeans object
	print(kmeans.cluster_centers_)
	# save new clusters for chart
	y_km = kmeans.fit_predict(data[keyList])

	print(y_km)
	# plt.scatter(data[y_km ==0,0], data[y_km == 0,1], s=100, c='red')
	# plt.scatter(data[y_km ==1,0], data[y_km == 1,1], s=100, c='black')
	# plt.scatter(data[y_km ==2,0], data[y_km == 2,1], s=100, c='blue')
	# plt.scatter(data[y_km ==3,0], data[y_km == 3,1], s=100, c='cyan')
	# plt.show()
	
	