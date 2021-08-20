# Criado por Bergerson Van Hallen
# 25/03/2021
# Utiliza a função polinomial para ajuste das curvas de luz.
# Ajuste polinomial para remover as trends longas.
# t0 e f0 são o tempo e fluxo de entrada.
# Arquivos já corrigidos em posição e com corte.
# Programa para a confecção das curvas de luz (K2SC).

# import numpy lib
import numpy as np
# start pylab mode
import pylab
from matplotlib.pyplot import *
import matplotlib.pyplot as plt
#latex sintaxe
from matplotlib import rc
# for ticks
import matplotlib.ticker as tkr
#legend
import matplotlib.lines as mlines
#font
from matplotlib.font_manager import FontProperties
import pandas as pd
from matplotlib.pyplot import figure
from matplotlib.backends.backend_pdf import PdfPages

import os  # para obter nome da pasta
import matplotlib.gridspec as gridspec #para layout das figuras
import time
from astropy.io import ascii
from astropy.timeseries import LombScargle
from matplotlib.gridspec import GridSpec
#from PyAstronomy.pyasl import foldAt
import sys
from astropy.table import Table
#for mark references
from matplotlib.lines import Line2D
#import seaborn as sns
#matplotlib.rcParams.update({'errorbar.capsize': 0.05})
#font
from matplotlib.font_manager import FontProperties
#para LaTex
plt.rc('text', usetex=True)

font = FontProperties()
#font.set_family('serif')
font.set_name('Times New Roman')

# ticks
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,
                               AutoMinorLocator)
                               
                          
def DataTreatmentO3(t0,f0):  #Bernardo, provided by Prof Cristina
    #Retira NaNs
    isnum = np.isfinite(t0) & np.isfinite(f0)
    t = t0[isnum]
    f = f0[isnum]
    # No caso de não haver Nans
    #t = t0
    #f = f0
    
    #Fluxo -> Fluxo relativo
    # f = f/np.median(f) - 1.
    f -= np.median(f)
    
    #Remove "pontos fora da curva"
    std = np.std(f)
    isin = (np.abs(f) <= 3*std)
    t = t[isin]
    f = f[isin]
    
    #Desloca série temporal
    # t += -t[0]
    
    #Subtrai um polinômio de terceiro grau
    p = np.polyfit(t,f,3)
    f += -1 * ( p[0]*t**3+p[1]*t**2+p[2]*t + p[3] )
    
    #Calcula a cadência mediana da curva de luz
    cd = np.median( np.diff(t) )
    
    #Finaliza
    return t,f,cd
    #return pd.Series(t, f)
  
names=np.sort(['200173850', '200173864', '200173869', '200173871', '210650598', '210671425', '210737173', '210853356', '210873575', '246697679', '246698204', '246704649', '246788829', '246820783', '246937768', '246968117', '246970807', '246988320', '247031423', '247131891', '247146962', '247147343', '247147476', '247148453', '247153152', '247160983', '247164195', '247169098', '247169375', '247192878', '247211157', '247234723', '247264203', '247273628', '247278704', '247368219', '247430338', '247457814', '247495377', '247541278', '247551785', '247554799', '247559520', '247612547', '247682580', '247688426', '247692298', '247692420', '247695418', '247696147', '247698073', '247705729', '247709560', '247714018', '247714396', '247742016', '247745384', '247757517', '247759652', '247774959', '247786632', '247806245', '247889905', '247895553', '247935687', '248064520', '248150769', '248227339'])

#names=np.sort(['200173850', '200173864'])  

dir_entrada = '/home/bergerson/Documents/Astronomia/kepler/c13/photometry/k2sc_pdc_plot/k2sc_corte/csv_corr/'
dir_saida = '/home/bergerson/Documents/Astronomia/kepler/c13/photometry/k2sc_pdc_plot/k2sc_corte/plot_polin/'  

i=0
for name in names:
	data = pd.read_csv(dir_entrada+'EPIC_'+name+'_k2sc_correct'+'.csv', delimiter=",")
	df = pd.DataFrame(data)
	tempo = df.iloc[:, 0]
	fluxo = df.iloc[:, 1]
	t, f, cd = DataTreatmentO3(tempo,fluxo)


	fig, ax = plt.subplots(figsize=(18, 6))
	#ax.plot(t,f)
	#ax.set(xlabel='Time [days]', ylabel='Corrected')
	plt.plot(t, f, '-', color='blue', label = 'none')
	xlabel(r'$\mathrm{Tempo \ [BJD-2454833]}$', fontsize=20)
	ylabel(r'$\mathrm{Fluxo \ [ppm]}$', fontsize=20)

	plt.title(r'EPIC '+name, fontsize=25)

	# changing the fontsize of ticks 
	plt.xticks(fontsize=18.2)
	plt.yticks(fontsize=18.5)

	# legenda dos plots

	leg = plt.legend()

	ax.get_legend().remove()
	
	savefig(dir_saida+'EPIC_'+name+'_k2sc_pol'+'.pdf')
	
	i=i+1
	
