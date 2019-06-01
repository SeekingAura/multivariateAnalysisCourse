# Import Standard Python libraries
import statistics

import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.formula.api as sm

# calcular modelo de regresion
# calcular varianzas y covarianzas
# calcular coeficiente de correlacion

# covarianza con formula principal
def pcov(*dataFrames):
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
	keyX1="Posicion_X1"
	keyX2="PESO_x2"
	keyX3="TIEMPO_x3"
	keyY="Rating_y"

	data = pd.read_csv('ejemplo football.csv')
	print(data)
	#print (data)
	# x1 barra
	mediaX=data[keyX1].mean()
	# x2 barra
	mediaX=data[keyX2].mean()
	# y barra
	mediaY=data[keyY].mean()
	print("media LlamadasVentas(X)={}, CopiadorasVendidas(Y)={}".format(mediaX, mediaY))
	n=len(data[keyX1])
	print("valor n={}".format(n))

	#covarianza (calculado con division n-1)
	covMatrix=data.cov()
	covValue=data.cov()
	print("covarianza calculado con n-1 ={}".format(covValue))
	print("\ncovarianza matrix con n-1=\n{}\n".format(covMatrix))

	# Covarianza
	pcovValue=pcov(data[keyX1],data[keyX2],data[keyY])
	print("covarianza calculado con n={}".format(pcovValue))

	# varianza de x (calculado con division n-1)
	# varX=data[keyX].var()
	# print("varianza x={}".format(varX))

	# varianza de x (calculado con division n)
	varX1=statistics.pvariance(data[keyX1])
	print("varianza x1 calculado con n ={}".format(varX1))

	# varianza de x (calculado con division n)
	varX2=statistics.pvariance(data[keyX2])
	print("varianza x2 con n ={}".format(varX2))

	# varianza de y (calculado con division n-1) 
	# varY=data[keyY].var()
	# print("varianza y={}".format(varY))

	# varianza de y (calculado con division n) 
	varY=statistics.pvariance(data[keyY])
	print("varianza y calculada con n ={}".format(varY))

	# Correlación
	corr=data.corr()
	print("\ncoeficiente de correlación entre 'x' y 'y'\n{}\n".format(corr))

	# Sumatoria de x1_i
	sumX1=data[keyX1].sum()
	print("sumatoria x1_i={}".format(sumX1))

	# Sumatoria de x2_i
	sumX2=data[keyX2].sum()
	print("sumatoria x2_i={}".format(sumX2))

	# Sumatoria de y_i
	sumY=data[keyY].sum()
	print("sumatoria y_i={}".format(sumY))

	# Sumatoria de x1_i y_y
	sumXY=(data[keyX1]*data[keyY]).sum()
	print("sumatoria x1_i*y_i={}".format(sumXY))

	# Sumatoria de x^2_i
	sumXX=(data[keyX1]**2).sum()
	print("sumatoria xx1_i={}".format(sumXX))

	# valor A de X1
	valueA_x1=calcA(data[keyX1], data[keyY])
	print("valor A: {}".format(valueA_x1))

	# valor B de X1
	valueB_x1=calcB(data[keyX1], data[keyY])
	print("valor B: {}".format(valueB_x1))

	# valor A de X2
	valueA_x2=calcA(data[keyX2], data[keyY])
	print("valor A: {}".format(valueA_x2))

	# valor B de X2
	valueB_x2=calcB(data[keyX2], data[keyY])
	print("valor B: {}".format(valueB_x2))


	# dataFrameSCE=SCEDataFrame(data[keyX], data[keyY])
	#valueSCE=dataFrameSCE.sum()
	#print("SCE value = ", valueSCE.values[0])

	# OLS Regression
	#model = sm.OLS(data[keyY], data[[keyX1, keyX2]]).fit()
	#predictions = model.predict(data[[keyX1, keyX2]]) # make the predictions by the model


	# Print out the statistics
	#print(model.summary())

	#smf.ols(formula, data).fit()
	results = sm.ols(formula=keyY+' ~ '+keyX1+" + "+keyX2+" + "+keyX3, data=data).fit()
	print(results.summary())
	print("correlation value=", results.rsquared**(1/2))

	





	# Instance of figure (Window)
	plt.figure("Recorridos")

	plt.scatter(data[keyX1], data[keyY], color="red")
	plt.scatter(data[keyX2], data[keyY], color="blue")
	# for data param (third param) see also https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html
	plt.plot(data[keyX1], valueA_x1 + valueB_x1*data[keyX1], linestyle="-", color="black")
	plt.plot(data[keyX2], valueA_x2 + valueB_x2*data[keyX1], linestyle="-", color="yellow")
	plt.grid()
	plt.xlabel("recorrido")
	plt.ylabel("tiempo")
	plt.title("Regresión lineal", loc="center")

	plt.show()

	# some operations https://pandas.pydata.org/pandas-docs/stable/getting_started/basics.html
	# https://stackoverflow.com/questions/19991445/run-an-ols-regression-with-pandas-data-frame
	# https://pythonfordatascience.org/anova-python/