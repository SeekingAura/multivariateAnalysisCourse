# Import Standard Python libraries
import statistics

import pandas as pd
import matplotlib.pyplot as plt

# calcular modelo de regresion
# calcular varianzas y covarianzas
# calcular coeficiente de correlacion

# covarianza con formula principal
def pcov(DataFrameX, DataFrameY):
    mediaX=DataFrameX.mean()
    mediaY=DataFrameY.mean()
    n=len(DataFrameX)
    result=0
    for i in range(n):
        result+=((DataFrameX[i]-mediaX)*(DataFrameY[i]-mediaY))
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




data = pd.read_csv('ejemplo llamadas.csv')
#print (data)
# x barra
mediaX=data["LlamadasVentas(X)"].mean()
# y barra
mediaY=data["CopiadorasVendidas(Y)"].mean()
print("media LlamadasVentas(X)={}, CopiadorasVendidas(Y)={}".format(mediaX, mediaY))
n=len(data["LlamadasVentas(X)"])
print("valor n={}".format(n))

#covarianza (calculado con division n-1)
covMatrix=data.cov()
covValue=data["LlamadasVentas(X)"].cov(data["CopiadorasVendidas(Y)"])
print("covarianza value={}".format(covValue))
print("\ncovarianza matrix=\n{}\n".format(covMatrix))

# Covarianza
pcovValue=pcov(data["LlamadasVentas(X)"],data["CopiadorasVendidas(Y)"])
print("covarianza con n={}".format(pcovValue))

# varianza de x (calculado con division n-1)
# varX=data["LlamadasVentas(X)"].var()
# print("varianza x={}".format(varX))

# varianza de x (calculado con division n)
varX=statistics.pvariance(data["LlamadasVentas(X)"])
print("varianza x otra={}".format(varX))

# varianza de y (calculado con division n-1) 
# varY=data["CopiadorasVendidas(Y)"].var()
# print("varianza y={}".format(varY))

# varianza de y (calculado con division n) 
varX=statistics.pvariance(data["CopiadorasVendidas(Y)"])
print("varianza y={}".format(varX))

# Correlación
corr=data.corr()
print("\ncoeficiente de correlación entre 'x' y 'y'\n{}\n".format(corr))

# Sumatoria de x_i
sumX=data["LlamadasVentas(X)"].sum()
print("sumatoria x_i={}".format(sumX))

# Sumatoria de y_i
sumY=data["CopiadorasVendidas(Y)"].sum()
print("sumatoria y_i={}".format(sumY))

# Sumatoria de x_i y_y
sumXY=(data["LlamadasVentas(X)"]*data["CopiadorasVendidas(Y)"]).sum()
print("sumatoria x_i*y_i={}".format(sumXY))

# Sumatoria de x^2_i
sumXX=(data["LlamadasVentas(X)"]**2).sum()
print("sumatoria xx_i={}".format(sumXX))

# valor A
valueA=calcA(data["LlamadasVentas(X)"], data["CopiadorasVendidas(Y)"])
print("valor A: {}".format(valueA))

# valor B
valueB=calcB(data["LlamadasVentas(X)"], data["CopiadorasVendidas(Y)"])
print("valor B: {}".format(valueB))

newdata=data["LlamadasVentas(X)"]

dataFrameSCE=SCEDataFrame(data["LlamadasVentas(X)"], data["CopiadorasVendidas(Y)"])
valueSCE=dataFrameSCE.sum()
print("SCE value = ", valueSCE.values[0])





# Instance of figure (Window)
plt.figure("llamadas")

plt.scatter(data["LlamadasVentas(X)"], data["CopiadorasVendidas(Y)"], color="red")
# for data param (third param) see also https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html
plt.plot(data["LlamadasVentas(X)"], valueA + valueB*data["LlamadasVentas(X)"], linestyle="-", color="black")
plt.grid()
plt.xlabel("Llamadas Ventas")
plt.ylabel("Copiadoras Vendidas")
plt.title("Regresión lineal", loc="center")

plt.show()
