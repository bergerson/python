# Criado por Bergerson Van Hallen
# 19/03/2021
# Programa para retirada das colunas de fluxo e tempo dos
# arquivos de curva de luz. Arquivos fits originais.

# import numpy lib
import numpy as np
# start pylab mode
import pylab
import pandas as pd
from pandas import DataFrame
import csv

data = pd.read_csv('ktwo246820783-c13.csv')

df = pd.DataFrame(data)

#tempo = df.loc[:, '0'] = df['0'].apply(lambda x: x - 2454833)

tempo = df.iloc[:, 0] - 2454833

fluxo = df.iloc[:, 3]

zip(tempo,fluxo)
#print([tempo, df.iloc[:, 3]].to_csv('c13_74_time.csv'))

#print((fluxo).to_csv('c13_74_time.csv'))

#print(tempo)

#print(fluxo)

with open('ktwo246820783-c13_time.csv', 'w') as f:
	writer = csv.writer(f, delimiter=',') #delimiter='\t'
	writer.writerows(zip(tempo,fluxo))
