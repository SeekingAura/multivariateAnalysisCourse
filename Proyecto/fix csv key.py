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



	# for i, row in data.iterrows():
	# 	#print("i-{} row-{}".format(i,row[keyList[0]]))
	# 	sideName,townCode=row[keyList[0]].split("/")
	# 	data.at[i,keyList[0]] = sideName.upper()+" DE "+townKeys.get(townCode)
		
	# 	if("SALUDCOOP" in sideName.upper() or "CRUZ BLANCA" in sideName.upper()):
	# 		data.at[i,keyList[0]] = "CLINICA SALUDCOOP"+" DE "+townKeys.get(townCode)

	# 	elif("ROSALES" in sideName.upper()):
	# 		data.at[i,keyList[0]] = "CLINICA LOS ROSALES"+" DE "+townKeys.get(townCode)

	# 	elif("DUMIAN" in sideName.upper()):
	# 		data.at[i,keyList[0]] = "CLINICA PINARES"+" DE "+townKeys.get(townCode)

	# 	elif("VICENTE DE PAUL" in sideName.upper()):
	# 		data.at[i,keyList[0]] = "HOSPITAL SAN VICENTE DE PAUL"+" DE "+townKeys.get(townCode)

	# 	elif("SAN JOSE" in sideName.upper()):
	# 		data.at[i,keyList[0]] = "HOSPITAL SAN JOSE"+" DE "+townKeys.get(townCode)

	# 	elif("SAN JORGE" in sideName.upper()):
	# 		data.at[i,keyList[0]] = "HOSPITAL SAN JOSE"+" DE "+townKeys.get(townCode)
		
	# 	elif("SAN PEDRO Y SAN PABLO" in sideName.upper()):
	# 		data.at[i,keyList[0]] = "HOSPITAL SAN PEDRO Y SAN PABLO"+" DE "+townKeys.get(townCode)
		
	# 	elif("NAZARETH" in sideName.upper()):
	# 		data.at[i,keyList[0]] = "HOSPITAL NAZARETH"+" DE "+townKeys.get(townCode)

	# 	elif("SANTA TERESITA" in sideName.upper()):
	# 		data.at[i,keyList[0]] = "CENTRO DE SALUD SANTA TERESITA"+" DE "+townKeys.get(townCode)

	# 	elif("ONCOLOGOS" in sideName.upper()):
	# 		data.at[i,keyList[0]] = "ONCOLOGOS DEL OCCIDENTE"+" DE "+townKeys.get(townCode)

	# 	elif("CL PIO" in sideName.upper()):
	# 		data.at[i,keyList[0]] = "CLINICA PIO XII"+" DE "+townKeys.get(townCode)

	# 	elif("CORPORACIËN MEDICA SALUD PARA LOS COLOMBIANOS" in sideName.upper() or "CORPORACI?N MEDICA SALUD PARA LOS COLOMBIANOS - CMS COLOMBIA LTDA" in sideName.upper()):
	# 		data.at[i,keyList[0]] = "CORPORACIÓN MEDICA SALUD PARA LOS COLOMBIANOS"+" DE "+townKeys.get(townCode)
		
	# 	elif("FUNDACIËN CL-NICA CARDIOVASCULAR DEL NIÐO DE RISARALDA" in sideName.upper()):
	# 		data.at[i,keyList[0]] = "FUNDACIÓN CLÍNICA CARDIOVASCULAR DEL NIÑO DE RISARALDA"+" DE "+townKeys.get(townCode)
		
	# 	elif("H KENNEDY" in sideName.upper()):
	# 		data.at[i,keyList[0]] = "HOSPITAL DE KENNEDY"+" DE "+townKeys.get(townCode)

	# 	elif("SANTA MONICA" in sideName.upper()):
	# 		data.at[i,keyList[0]] = "HOSPITAL SANTA MONICA"+" DE "+townKeys.get(townCode)

	# 	elif("HOSPITAL DE CUBA" in sideName.upper()):
	# 		data.at[i,keyList[0]] = "HOSPITAL SAN JOAQUIN-CUBA"+" DE "+townKeys.get(townCode)

	# 	elif("INVERSIONES CLINICA MARAÐON LTDA" in sideName.upper() or "INVERSIONES CLINICA MARA?ON LTDA" in sideName.upper()):
	# 		data.at[i,keyList[0]] = "CLINICA EL LAGO"+" DE "+townKeys.get(townCode)

	# 	elif("IPS CL?NICA SAN RAFAEL - SEDE MEGACENTRO" in sideName.upper()):
	# 		data.at[i,keyList[0]] = "CLINICA SAN RAFAEL MEGACENTRO"+" DE "+townKeys.get(townCode)

	# 	elif("SERVICIO DE EMERGENCIAS REGIONALSERVICIO DE AMBULANCIA PREPAGO S.A" in sideName.upper()):
	# 		data.at[i,keyList[0]] = "AMBULANCIA"+" DE "+townKeys.get(townCode)

	for i, row in data.iterrows():
		#print("i-{} row-{}".format(i,row[keyList[0]]))
		sideName,townCode=row[keyList[0]].split("/")
		data.at[i,keyList[0]] = townKeys.get(townCode)
		

	data.to_excel("output4.xlsx", index=False)
	data.to_csv("output4.csv", index=False)