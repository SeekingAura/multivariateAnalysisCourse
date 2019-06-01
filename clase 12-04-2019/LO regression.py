# Import Standard Python libraries
import statistics
import sys
import os

import pandas as pd
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import statsmodels.formula.api as sm
from matplotlib import cm

from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import seaborn as sns


# to 3D graphic https://stackoverflow.com/questions/26431800/plot-linear-model-in-3d-with-matplotlib

# calcular modelo de regresion
# calcular varianzas y covarianzas
# calcular coeficiente de correlacion

# covarianza con formula principal
def pcov(dataFrames):
	meanList=[]
	for i in dataFrames:
		meanList.append(i.mean())
	n=len(dataFrames[0])
	result=0
	for i in range(n):
		dataTemp=1
		for enum,j in enumerate(dataFrames):
			dataTemp*=j[i]-meanList[enum]
		result+=dataTemp
	return result/n

def calcA(DataFrameX, DataFrameY):
	n=len(DataFrameX)
	sumX=DataFrameX.sum()
	sumXX=(DataFrameX**2).sum()
	sumY=DataFrameY.sum()
	sumXY=(DataFrameX*DataFrameY).sum()
	return (sumXX*sumY-(sumX*sumXY))/(n*sumXX-(sumX**2))

def calcB(DataFrameX, DataFrameY):
	n=len(DataFrameX)
	sumX=DataFrameX.sum()
	sumY=DataFrameY.sum()
	sumXX=(DataFrameX**2).sum()
	sumXY=(DataFrameX*DataFrameY).sum()

	return (n*sumXY-(sumX*sumY))/(n*sumXX-(sumX**2))

def SCEDataFrame(DataFrameX, DataFrameY):
	valueA=calcA(DataFrameX, DataFrameY)
	valueB=calcB(DataFrameX, DataFrameY)
	result=pd.DataFrame(columns=["data SCE"])
	for i in (DataFrameX):
		result=result.append({"data SCE" : valueA+valueB*i}, ignore_index=True)
	return result

if __name__=="__main__":
	if(len(sys.argv)!=3):
		sys.stderr.write('Usage: "{0}" $csvFileName $IndexOfX1 (csv headers should be must otherThink0, otherThink1, ... , otherThinnkn, "x1", "x2", ..., "xn", "Y")\n'.format(sys.argv[0]))
		os._exit(1)
	data = pd.read_csv(sys.argv[1])
	# Replace All space in column headers
	data.rename(columns=lambda name: name.replace(" ", "_"), inplace=True)

	# get column headers such as [keyX1, keyX2, keyX3, ..., keyY]
	keyList=data.columns.values[int(sys.argv[2]):]
	print("Tabla de datos leido\n{}\n".format(data))

	for enum, i in enumerate(keyList):
		if(enum!=len(keyList)-1):
			print("media de x{}\n→ {}".format(enum+1, data[i].mean()))
		else:
			print("media de y\n→{}\n".format(data[i].mean()))
	

	

	# Logistic regression
	X_train, X_test, y_train, y_test = train_test_split(data.drop('Card',axis=1),data['Card'])# test_size=0.50,random_state=101
	
	logmodel = LogisticRegression()
	logmodel.fit(X_train,y_train)
	predictions = logmodel.predict(X_test)

	print("coefiente ",logmodel.coef_)
	
	
	print(classification_report(y_test,predictions))
	print("Accuracy:",accuracy_score(y_test, predictions))

	plt.figure(1)
	sns.heatmap(data.isnull(),yticklabels=False,cbar=False,cmap='viridis')

	plt.figure(2)
	sns.set_style('whitegrid')

	# Count data
	sns.countplot(x='Card',data=data,palette='RdBu_r')

	plt.figure(3)
	sns.set_style('whitegrid')
	sns.countplot(x='Card',hue='Coupon',data=data,palette='RdBu_r')


	plt.show()
	# Plot 2d
	# calculate number of rows and cols
	# rows=0
	# cols=0
	# foundIt=False
	# for irows in range(1, len(keyList[:-1])+1):
		
	# 	for icols in range(1, irows+1):
	# 		if(irows*icols>=len(keyList[:-1])):
	# 			rows=irows
	# 			cols=icols
	# 			break
	# 	if(foundIt):
	# 		break

	

	# fig, axs = plt.subplots(rows, cols, constrained_layout=True)
	# fig.suptitle("Graficas", fontsize=16)

	# for enum, i in enumerate(keyList[:-1]):
	# 	axs[enum].set_title(keyList[enum]+" vs "+keyList[-1])
	# 	axs[enum].scatter(data[i], data[keyList[-1]], color="red")
	# 	# for data param (third param) see also https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html
	# 	axs[enum].plot(data[i], valueABList[enum].get("valueA") + valueABList[enum].get("valueB")*data[i], linestyle="-", color="black")
	# 	axs[enum].grid()
	# 	axs[enum].set_xlabel(i)
	# 	axs[enum].set_ylabel(keyList[-1])
	
	# plt.show()










	# 3d plotting
	# https://gist.github.com/iros/18d9b953f2c907f31489
	# xx1, xx2 = np.meshgrid(np.linspace(data[keyList[0]].min(), data[keyList[0]].max(), 20), 
	# 				   np.linspace(data[keyList[1]].min(), data[keyList[1]].max(), 20))
	# Z = resultOLS.params[0] + resultOLS.params[1] * xx1 + resultOLS.params[2] * xx2

	# fig = plt.figure(figsize=(8, 3))
	# ax = Axes3D(fig, azim=-135, elev=15)

	# surf = ax.plot_surface(xx1, xx2, Z, cmap=plt.cm.RdBu_r, alpha=0.6, linewidth=0)

	# # plot data points - points over the HP are white, points below are black
	# resid = data[keyList[-1]] - resultOLS.predict(data[keyList[:2]])
	# ax.scatter(data[resid >= 0][keyList[0]], data[resid >= 0][keyList[1]], data[resid >= 0][keyList[-1]], color='aqua', alpha=0.4, facecolor='black')
	# ax.scatter(data[resid < 0][keyList[0]], data[resid < 0][keyList[1]], data[resid < 0][keyList[-1]], color='lime', alpha=0.4)


	# ax.plot(data[keyList[0]], valueABList[0].get("valueA")+valueABList[0].get("valueB")*data[keyList[0]], zs=0, zdir='z', color="blue",label='')
	# ax.plot(data[keyList[1]], valueABList[1].get("valueA")+valueABList[1].get("valueB")*data[keyList[1]], zs=0, zdir='z', color="green",label='')

	# # set axis labels
	# ax.set_xlabel('X1')
	# ax.set_ylabel('X2')
	# ax.set_zlabel('Y')

	# plt.show()


	# fig = plt.figure()
	# ax = fig.gca(projection='3d')

	# Plot a sin curve using the x and y axes.
	#x = np.linspace(0, 1, 100)
	#y = np.sin(x * 2 * np.pi) / 2 + 0.5
	#ax.plot(x, y, zs=0, zdir='z', label='curve in (x,y)')

	# ax.scatter(data[keyX1], data[keyY], zs=0, zdir='y', c=c_list, label='points in (x,z)')


	# some operations https://pandas.pydata.org/pandas-docs/stable/getting_started/basics.html
	# https://stackoverflow.com/questions/19991445/run-an-ols-regression-with-pandas-data-frame
	# https://pythonfordatascience.org/anova-python/