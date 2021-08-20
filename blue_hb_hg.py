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
#para LaTex
plt.rc('text', usetex=True)

font = FontProperties()
#font.set_family('serif')
font.set_name('Times New Roman')

# ticks
#fig, ax = plt.subplots()
#ax.axis([0.001, 1000000000, 1, 350000])
#ax.loglog()

# load and plot data
data = np.genfromtxt("lsv211_ret_norm.csv", delimiter=",", names=["x", "y"])
#data2 = np.genfromtxt("chi.csv", delimiter=",", names=["x", "y"])

#plots
plt.plot(data['x'], data['y'], linewidth=0.2, color='blue', label= r'$\mathrm{07/09/2017}$')
#plt.plot(data2['x'], data2['y'], 'o', fillstyle='none', color = 'blue', label = r'$\mathrm{-\chi}$')

plt.xlim([4300, 4400]) #H-Gamma
#plt.xlim([4800, 4900]) #H-Beta
plt.ylim([0.5, 1.05])


#plt.text(x, y, '*', fontsize=15, color= 'green');


# set axis labels
xlabel(r'$\mathrm{Comprimento \ de \ onda \ \left(\AA \right)}$', fontsize=13.5) #\ \lef(\AA \right)
ylabel(r'$\mathrm{Fluxo}$', fontsize=15)
#xlabel(r'$ \mathrm{log} \left(\mathrm{T_{eff}}\right)$')
#ylabel(r'$\mathrm{log} \ \left(\mathrm{L/L_{\odot}} \right)$')

# invert the x-axis
#plt.gca().invert_xaxis()

plt.title(r'$\mathrm{EPIC \ 247368219}$', fontsize=18)

plt.legend()
#plt.show()

savefig('epic_247368219_blue_hga.pdf')

