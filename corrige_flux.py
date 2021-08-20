# Criado por Bergerson Van Hallen
# 24/03/2021
# Programa para correção de fluxo. 
# Há os fluxos PDC dos fits originais ktwo.. e do K2SC
# Se forem idênticos o fluxo corrigido de sistemática vai ser:
# fluxo_c='flux'-'trposi'+median('trposi')
# onde 'trposi' é a correcao da posição

# import numpy lib
import numpy as np
# start pylab mode
import pylab
import pandas as pd
from pandas import DataFrame
import csv
import os  # obter nome da pasta
import glob # ler multiplos

names=np.sort(['200173850', '200173864', '200173869', '200173871', '210650598', '210671425', '210737173', '210853356', '210873575', '246697679', '246698204', '246704649', '246788829', '246820783', '246937768', '246968117', '246970807', '246988320', '247031423', '247131891', '247146962', '247147343', '247147476', '247148453', '247153152', '247160983', '247164195', '247169098', '247169375', '247192878', '247211157', '247234723', '247264203', '247273628', '247278704', '247368219', '247430338', '247457814', '247495377', '247541278', '247551785', '247554799', '247559520', '247612547', '247682580', '247688426', '247692298', '247692420', '247695418', '247696147', '247698073', '247705729', '247709560', '247714018', '247714396', '247742016', '247745384', '247757517', '247759652', '247774959', '247786632', '247806245', '247889905', '247895553', '247935687', '248064520', '248150769', '248227339'])

#names=np.sort(['200173850', '200173864'])
#names = open('epic_c13.txt').read().splitlines()

dir_entrada = '/home/bergerson/Documents/Astronomia/kepler/c13/photometry/k2sc_pdc_plot/k2sc_txt/'
dir_saida = '/home/bergerson/Documents/Astronomia/kepler/c13/photometry/k2sc_pdc_plot/flux_corrigido/'

i=0
for name in names:
	#data = pd.read_csv('../EPIC_247031423_mast_t1.txt', delimiter=",", skiprows=1)
	data = pd.read_csv(dir_entrada+'EPIC_'+name+'_mast_t1'+'.txt', delimiter=",", skiprows=1)
	df = pd.DataFrame(data)
	tempo = df.iloc[:, 0]
	fluxo = df.iloc[:, 5]
	df1 = df[~fluxo.str.contains("NULL ")] #drop all rows that have any NULL/NaN values
	
	df1.to_csv(dir_saida+'EPIC_'+name+'.csv')

	data2 = pd.read_csv(dir_saida+'EPIC_'+name+'.csv', delimiter=",", skiprows=1)
	df0 = pd.DataFrame(data2)
	tempo1 = df0.iloc[:, 1]
	fluxo2 = df0.iloc[:, 6]
	trposi = df0.iloc[:, 10]
	
	mediana = trposi.mean(axis = None, skipna=None)
	
	fluxo_c = fluxo2 - trposi + mediana
	
	with open(dir_saida+'EPIC_'+name+'_k2sc'+'.csv', 'w') as f:
		writer = csv.writer(f, delimiter=',') #delimiter='\t'
		writer.writerows(zip(tempo1,fluxo_c))
	
	i=i+1	
