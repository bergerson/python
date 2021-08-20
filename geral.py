# Criado por Bergerson Van Hallen
# 22/03/2021
# Programa para retirada das colunas de fluxo e tempo dos
# arquivos de curva de luz. 
# Retira os valores nulos (NULL) da coluna do fluxo.
# Curvas de luz corrigidas pelo K2SC. 
# Fluxo subtraído da mediana e dividido por 1 milhão (ppm).

# import numpy lib
import numpy as np
# start pylab mode
import pylab
import pandas as pd
from pandas import DataFrame
import csv

data = pd.read_csv('../EPIC_247031423_mast_t1.txt', delimiter=",", skiprows=1)

df = pd.DataFrame(data)

tempo = df.iloc[:, 0]

fluxo = df.iloc[:, 5]

df1 = df[~fluxo.str.contains("NULL ")] #drop all rows that have any NULL/NaN values

#print(df1)

df1.to_csv('a.csv')

data2 = pd.read_csv('a.csv', delimiter=",", skiprows=1)

df0 = pd.DataFrame(data2)

teste_flux = df0.iloc[:, 6]

mediana = teste_flux.mean(axis = None, skipna=None)

print(mediana)

#df2 = df0.iloc[:, 6]

df2 = (df0.iloc[:, 6] - mediana).div(1000000)

print(df2)

with open('a.csv', 'w') as f:
	writer = csv.writer(f, delimiter=',') #delimiter='\t'
	writer.writerows(zip(tempo,df2))
			
