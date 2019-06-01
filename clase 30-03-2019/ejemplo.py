import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('ejemplo.csv')
print (data)
print("media X1={}, X2={}".format(data["X1"].mean(), data["X2"].mean()))
print("covariance \n{}".format(data.cov()))
print("correlation\n{}".format(data.corr()))
#plt.matshow(data.corr())
#plt.show()
# print (data)
# print (data[0:5]['salary'])
# print (data.loc[:,['salary','name']])
# print (data.loc[[1,3,5],['salary','name']])
# print (data.loc[2:6,['salary','name']])
