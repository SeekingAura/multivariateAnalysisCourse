import sys
import os

import pandas as pd

import math

if __name__ == "__main__":
	if(len(sys.argv)!=3):
		sys.stderr.write('Usage: "{0}" $csvOdds1 $csvOdds0\n'.format(sys.argv[0]))
		os._exit(1)


	# Calculando odds_1
	data = pd.read_csv(sys.argv[1])
	# Replace All space in column headers
	data.rename(columns=lambda name: name.replace(" ", "_"), inplace=True)
	
	# cast values to float, b0, b1, b2...
	betas=data["betas"][1:]
	x_n=data["x_n"]
	# print(betas)
	# print(x_n)
	#print(sys.float_info.epsilon)
	
	numerator=data["betas"][0]+(data["betas"][1:]*data["x_n"][1:]).sum()
	denominator=data["betas"][0]+(data["betas"][1:]*data["x_n"][1:]).sum()
	
	odds1=math.exp(numerator)/(1+math.exp(denominator))
	print("odds 1", odds1)

	data = pd.read_csv(sys.argv[2])
	# Replace All space in column headers
	data.rename(columns=lambda name: name.replace(" ", "_"), inplace=True)

	# cast values to float, b0, b1, b2...
	betas=data["betas"][1:]
	x_n=data["x_n"]
	# print(betas)
	# print(x_n)
	# print(sys.float_info.epsilon)
	
	numerator=data["betas"][0]+(data["betas"][1:]*data["x_n"][1:]).sum()
	denominator=data["betas"][0]+(data["betas"][1:]*data["x_n"][1:]).sum()
	
	odds0=math.exp(numerator)/(1+math.exp(denominator))
	print("odds 0", odds0)


	# Calculando coeficiente
	coeficiente=odds1/odds0
	print("coeficiente", coeficiente)



# 2.539
# 1.561
# -6.893