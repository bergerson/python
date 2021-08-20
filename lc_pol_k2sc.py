# Criado por Bergerson Van Hallen
# 28/03/2021
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

                               
names=np.sort(['200173850', '200173864', '200173869', '200173871', '210650598', '210671425', '210737173', '210853356', '210873575', '246697679', '246698204', '246704649', '246788829', '246820783', '246937768', '246968117', '246970807', '246988320', '247031423', '247131891', '247146962', '247147343', '247147476', '247148453', '247153152', '247160983', '247164195', '247169098', '247169375', '247192878', '247211157', '247234723', '247264203', '247273628', '247278704', '247368219', '247430338', '247457814', '247495377', '247541278', '247551785', '247554799', '247559520', '247612547', '247682580', '247688426', '247692298', '247692420', '247695418', '247696147', '247698073', '247705729', '247709560', '247714018', '247714396', '247742016', '247745384', '247757517', '247759652', '247774959', '247786632', '247806245', '247889905', '247895553', '247935687', '248064520', '248150769', '248227339'])

#names=np.sort(['200173850', '200173864'])  

dir_entrada = '/home/bergerson/Documents/Astronomia/kepler/c13/photometry/k2sc_pdc_plot/k2sc_corte/csv_pol/'
dir_saida = '/home/bergerson/Documents/Astronomia/kepler/c13/photometry/k2sc_pdc_plot/k2sc_corte/plot_polin_en/'  

i=0
for name in names:
	try:
		data = pd.read_csv(dir_entrada+'EPIC_'+name+'_k2sc_pol-2'+'.csv', delimiter=",", names=["x", "y"])
		df = pd.DataFrame(data)
	
		fig, ax = plt.subplots(figsize=(18, 6))
		#ax.plot(t,f)
		#ax.set(xlabel='Time [days]', ylabel='Corrected')
		plt.plot(data['x'], data['y'], '-', color='blue', label = 'none')
		#xlabel(r'$\mathrm{Tempo \ [BJD-2454833]}$', fontsize=19.5)
		#ylabel(r'$\mathrm{Fluxo \ [ppm]}$', fontsize=21)
		xlabel(r'$\mathrm{Time \ [BJD-2454833]}$', fontsize=19.5)
		ylabel(r'$\mathrm{Flux \ [ppm]}$', fontsize=21)

		plt.title(r'EPIC '+name, fontsize=25)

		# changing the fontsize of ticks 
		plt.xticks(fontsize=18.2)
		plt.yticks(fontsize=18.5)

		# legenda dos plots

		leg = plt.legend()

		ax.get_legend().remove()
	
		savefig(dir_saida+'EPIC_'+name+'_k2sc_pol-en'+'.pdf')
		
	except:
		pass
	
		i=i+1                                                  
