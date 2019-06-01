import sys
import os
from pandas import ExcelWriter
from pandas import ExcelFile

import pandas as pd

#Spss convert
import pyreadstat

if __name__=="__main__":
	if(len(sys.argv)!=2):
		sys.stderr.write('Usage: "{0}" $csvFileName\n'.format(sys.argv[0]))
		os._exit(1)

	if(".csv" in sys.argv[1]):
		data = pd.read_csv(sys.argv[1])
	else:
		data, meta = pyreadstat.read_sav(sys.argv[1])
	# Replace All space in column headers
	data.rename(columns=lambda name: name.replace(" ", "_"), inplace=True)

	# get column headers such as [keyX1, keyX2, keyX3, ..., keyY]
	keyList=data.columns.values

	# set dictionary of Town
	townKeys={
		"1":"Pereira".upper(),
		"45":"Apía".upper(), 
		"75":"Balboa".upper(),
		"88":"Belén de umbría".upper(), 
		"170":"Dosquebradas".upper(),
		"318":"Guática".upper(),
		"383":"La celia".upper(),
		"400":"La Virginia".upper(),
		"440":"Marsella".upper(),
		"456":"Mistrató".upper(),
		"572":"Pueblo Rico".upper(),
		"594":"Quinchía".upper(),
		"682":"Santa Rosa De Cabal".upper(),
		"687":"Santuario".upper()
	}



	#for i, row in data.iterrows():
	#	#print("i-{} row-{}".format(i,row[keyList[0]]))
	#	sideName,townCode=row[keyList[0]].split("/")
	#	data.at[i,keyList[0]] = sideName.upper()+" DE "+townKeys.get(townCode)
		
	newData=data.groupby(keyList[0]).mean()

	for i, row in newData.iterrows():
		#print("i-{} row-{}".format(i,row[keyList[0]]))
		newData.at[i,"Lugar_def"] = i
		
	print(newData)

	# newData.first()
	newData.to_excel("output5.xlsx", index=False)
	newData.to_csv("output5.csv", index=False)