# https://www.python-course.eu/linear_discriminant_analysis.php
# https://sebastianraschka.com/Articles/2014_python_lda.htmlimport sys
import os
import sys

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import seaborn as sns

from sklearn.preprocessing import LabelEncoder
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA

#Spss convert
import pyreadstat

def plot_scikit_lda(X, title, label_dict):
	labelEdad={
		0 : "Menor de una hora ",
		1 : "Menor de un día",
		2 : "De 1 a 6 días",
		3 : "De 7 a 27 días",
		4 : "De 28 a 29 días",
		5 : "De 1 a 5 meses",
		6 : "De 6 a 11 meses",
		7 : "De 1 año",
		8 : "De 2 a 4 años",
		9 : "De 5 a 9 años",
		10 : "De 10 a 14 años",
		11 : "De 15 a 19 años",
		12 : "De 20 a 24 años",
		13 : "De 25 a 29 años",
		14 : "De 30 a 34 años",
		15 : "De 35 a 39 años",
		16 : "De 40 a 44 años",
		17 : "De 45 a 49 año",
		18 : "De 50 a 54 año",
		19 : "De 55 a 59 año",
		20 : "De 60 a 64 año",
		21 : "De 65 a 69 años",
		22 : "De 70 a 74 años",
		23 : "De 75 a 79 años",
		24 : "De 80 a 84 años",
		25 : "De 85 a 89 años",
		26 : "De 90 a 94 años",
		27 : "De 95 a 99 años",
		28 : "De 100 años y más",
		29 : "Edad desconocida"
	}

	labelSeg={
		1 : "Contributivo",
		2 : "Subsidiado",
		3 : "Excepción",
		4 : "Especial",
		5 : "No asegurado",
		9 : "Sin información"
	}

	labelEstudio={
		1 : "Preescolar",
		2 : "Básica primaria",
		3 : "Básica secundaria",
		4 : "Media académica o clásica",
		5 : "Media técnica",
		6 : "Normalista",
		7 : "Técnica profesional",
		8 : "Tecnológica",
		9 : "Profesional",
		10 : "Especialización",
		11 : "Maestría",
		12 : "Doctorado",
		13 : "Ninguno",
		99 : "Sin información"

	}


	numberIndex=range(0,70)[:len(label_dict)]
	markersIndex=('^', 's', 'o', '.', 'v', '<', '>', '1', '2', '3', '4', 
		'8', 's', 'p', 'P', '*', 'h', 'H', '+', 'x', 'X', 'D', 'd', '|', 
		'_', '_', '|', 'd', 'D', 'X', 'x', '+', 'H', 'h', '*', 'P', 'p', 
		's', '8', '4', '3', '2', '1', '>', '<', 'v', '.', 'o', 's', '^', 
		'^', 's', 'o', '.', 'v', '<', '>', '1', '2', '3', '4', '8', 's', 
		'p', 'P', '*', 'h', 'H', '+', 'x'
	)[:len(label_dict)]
	colorsIndex=('blue', 'red', 'green', 'darkcyan', 'navy', 'darkviolet', 
		'olive', 'yellow', 'grey', 'orange', 'blue', 'red', 'green', 
		'darkcyan', 'navy', 'darkviolet', 'olive', 'yellow', 'grey', 
		'orange', 'blue', 'red', 'green', 'darkcyan', 'navy', 'blue', 
		'red', 'green', 'darkcyan', 'navy', 'darkviolet', 'olive', 
		'yellow', 'grey', 'orange', 'blue', 'red', 'green', 'darkcyan', 
		'navy', 'darkviolet', 'olive', 'yellow', 'grey', 'orange', 
		'blue', 'red', 'green', 'darkcyan', 'navy', 'navy', 'darkcyan', 
		'green', 'red', 'blue', 'orange', 'grey', 'yellow', 'olive', 
		'darkviolet', 'navy', 'darkcyan', 'green', 'red', 'blue', 'orange', 
		'grey', 'yellow', 'olive', 'darkviolet'
	)[:len(label_dict)]
	print("number is", numberIndex)

	ax = plt.subplot(111)
	for label,marker,color in zip(numberIndex, markersIndex, colorsIndex):

		plt.scatter(x=X[:,0][y == label],
					y=X[:,1][y == label] * -1, # flip the figure
					marker=marker,
					color=color,
					alpha=0.5,
					label=label_dict.get(label))

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
	keyTarget=keyList[int(sys.argv[2])]
	keyList=np.delete(keyList, np.where(keyList == keyTarget)[0][0])# Remove target from main list key
	print("TARGET", keyTarget)
	print("keylist", keyList)
	#print("data readed table \n", data)

	# for lugar_def
	dictoLugar={}
	indexKey=0
	for i, row in data.iterrows():
		if(not row["Lugar_def"] in list(dictoLugar.keys())):
			dictoLugar[str(row["Lugar_def"])]=indexKey
			indexKey+=1
		data.at[i,"Lugar_def"] = dictoLugar.get(row["Lugar_def"])
	data["Lugar_def"]= data["Lugar_def"].astype(str)

	label_dict={}
	indexKey=0
	for keyValues in data[keyTarget].unique():
		if(not keyValues in list(label_dict.keys())):
			label_dict[indexKey]=keyValues
			indexKey+=1
		#data.at[i,keyTarget] = dictoNames.get(row[keyTarget])
	# data[keyTarget]= data[keyTarget].astype(str)
	print(label_dict)

	X=data[[keyList[1]]+[keyList[3]]+[keyList[-1]]]
	y=data[keyTarget]
	enc = LabelEncoder()
	label_encoder = enc.fit(y)
	y = label_encoder.transform(y) + 1

	sklearn_lda = LDA(n_components=2)
	X_lda_sklearn = sklearn_lda.fit_transform(X, y)

	plot_scikit_lda(X_lda_sklearn, 'Default LDA via scikit-learn', label_dict)

	# plt.show()