# Criado por Bergerson Van Hallen
# 27/03/2021
# Programa para a obtenção dos arquivos em .csv;
# Arquivos corrigidos pelo polinômio, mas sem estar em duas colunas.

# import numpy lib
import numpy as np
# start pylab mode
import pylab
import pandas as pd
from pandas import DataFrame
import csv
import os  # obter nome da pasta
import glob # ler multiplos

data2 = pd.read_csv('EPIC_200173850_k2sc_pol.csv')
df = pd.DataFrame(data2)
#t = df.iloc[0, :]
f = df.iloc[0, :]
#t1 = t.transpose()
#f2 = f.transpose()

#df1 = df.T
#print(df1)
#with open('EPIC_200173850_k2sc_pol-2.csv', 'w') as f:
#	writer = csv.writer(f, delimiter=',')
#	writer.writerows(zip(df))

df2 = f.transpose()
print(df2)
with open('EPIC_200173850_k2sc_pol-3.csv', 'w') as f:
	writer = csv.writer(f, delimiter=',')
	writer.writerows(zip(df, df2))
