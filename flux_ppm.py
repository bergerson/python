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
                               
                          
fig, ax = plt.subplots(figsize=(18, 6))
#ax.axis([2457818, 2457903, 3380000, 3440000])
#ax.axis([2985, 3070, 3380000, 3440000])
#plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
#ax.ticklabel_format(style='sci', axis='x', scilimits=(0,0))

# load and plot data
#df = pd.read_csv('c13_74.csv', names=["x", "y", "z", "w"])
#data = np.genfromtxt("test2.csv", delimiter=",", names=["x", "y"], usecols=[0,5])
data = np.genfromtxt("test2.csv", delimiter=",", names=["x", "y"])

#tempo = df.loc[:, 'x'] = df['x'].apply(lambda x: x - 2454833)

#plots
plt.plot(data['x'], data['y'], '-', color='blue', label = 'none')
#plt.plot(data['x'], data['y'], 's', fillstyle='none', color='red', label = r'$\mathrm{Experimental}$')

# set axis labels
xlabel(r'$\mathrm{Tempo \ [BJD-2454833]}$', fontsize=20)
ylabel(r'$\mathrm{Fluxo \ [ppm]}$', fontsize=20)

plt.title(r'$\mathrm{EPIC \ 247031423}$', fontsize=20)

# changing the fontsize of ticks 
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)

# legenda dos plots

leg = plt.legend()

ax.get_legend().remove()
#ax.legend()

#plt.legend()
#plt.show()

savefig('EPIC_247031423_flux_ppm.pdf')
