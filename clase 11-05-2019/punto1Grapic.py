import sys
import os
import random
import matplotlib.pyplot as plt

from matplotlib import colors as mcolors
import pandas as pd

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
		sys.stderr.write('Usage: "{0}" $csvFileName $IndexOfX1 (csv headers should be must otherThink0, otherThink1, ... , otherThinnkn, "x1", "x2", ..., "xn", "Y")\n'.format(sys.argv[0]))
		os._exit(1)

	if(".csv" in sys.argv[1]):
		data = pd.read_csv(sys.argv[1])
	# Replace All space in column headers
	data.rename(columns=lambda name: name.replace(" ", "_"), inplace=True)

	keyList=data.columns.values

	

	fig = plt.figure(figsize = (8,8))
	ax = fig.add_subplot(1,1,1) 
	ax.set_xlabel('Principal Component 1', fontsize = 15)
	ax.set_ylabel('Principal Component 2', fontsize = 15)
	ax.set_title('2 component PCA', fontsize = 20)
	targets = data[keyList[0]]

	

	colorsAll = dict(mcolors.BASE_COLORS, **mcolors.CSS4_COLORS)
	colorsAll = list(colorsAll.keys())
	colors=[]
	for i in ["ghostwhite", "floralwhite", "white", "whitesmoke"]:
		colorsAll.remove(i)
	for i in range(len(targets)):
		while True:
			colorTemp=colorsAll[random.randint(0, len(colorsAll)-1)]	
			if not colorTemp in colors:
				colors.append(colorTemp)
				break

	dataNorm=normalize(data[keyList[1:]])
	print(dataNorm)
	for target, color in zip(targets,colors):
		indicesToKeep = data[keyList[0]] == target
		ax.scatter(data.loc[indicesToKeep, keyList[1]]
				   , data.loc[indicesToKeep, keyList[2]]
				   , c = color
				   , s = 50)
	ax.legend(targets)
	ax.axhline(y=0, color='k')
	ax.axvline(x=0, color='k')
	plt.show()