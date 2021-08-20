# start pylab mode
import pylab
# import mesa_reader
import mesa_reader as mr
# import plot
from matplotlib.pyplot import *
import matplotlib.pyplot as plt
#latex sintaxe
from matplotlib import rc
#for mark references
from matplotlib.lines import Line2D
import seaborn as sns
matplotlib.rcParams.update({'errorbar.capsize': 0.05})
#for cap in caps: cap.set_markeredgewidth(1)
#plt.style.use('seaborn')
#plt.rcParams.update({'lines.markeredgewidth': 1})
# for ticks
import matplotlib.ticker as tkr
#colors ; linestyle
from cycler import cycler
default_cycler = (cycler(color=['black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black',
				'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black'])+
                  cycler(linestyle=['-', '-', '-', '-', '-', '-', '-', '-', '-',
				    '-' , '-', '-', '-', '-', '-', '-', '-', '-']))

plt.rc('lines', linewidth=2, linestyle= '-')
plt.rc('axes', prop_cycle=default_cycler)

#fig, ax = plt.subplots()

#para LaTex
plt.rc('text', usetex=True)

#legend
import matplotlib.lines as mlines

#font
from matplotlib.font_manager import FontProperties

font = FontProperties()
#font.set_family('serif')
font.set_name('Times New Roman')

#title
plt.title(r'$\mathrm{C13 - Kepler/K2}$')

# load and plot data
h = mr.MesaData('LOGS3/history_2.0.data')
h1 = mr.MesaData('LOGS3/history_2.20.data')
h2 = mr.MesaData('LOGS3/history_2.40.data')
h3 = mr.MesaData('LOGS3/history_2.60.data')
h4 = mr.MesaData('LOGS3/history_2.80.data')
h5 = mr.MesaData('LOGS3/history_3.00.data')
h6 = mr.MesaData('LOGS3/history_3.20.data')
h7 = mr.MesaData('LOGS3/history_3.40.data')
h8 = mr.MesaData('LOGS3/history_3.60.data')
h9 = mr.MesaData('LOGS3/history_3.80.data')
h10 = mr.MesaData('LOGS3/history_4.00.data')
h11 = mr.MesaData('LOGS3/history_4.50.data')
h12 = mr.MesaData('LOGS3/history_5.00.data')
h13 = mr.MesaData('LOGS3/history_5.50.data')
h14 = mr.MesaData('LOGS3/history_6.0.data')
h15 = mr.MesaData('LOGS3/history_6.50.data')
h16 = mr.MesaData('LOGS3/history_7.0.data')
h17 = mr.MesaData('LOGS3/history_7.50.data')
h18 = mr.MesaData('LOGS3/history_8.0.data')
h19 = mr.MesaData('LOGS3/history_8.50.data')

#plots
plot(h.log_Teff, h.log_L)
plot(h1.log_Teff, h1.log_L)
plot(h2.log_Teff, h2.log_L)
plot(h3.log_Teff, h3.log_L)
plot(h4.log_Teff, h4.log_L)
plot(h5.log_Teff, h5.log_L)
plot(h6.log_Teff, h6.log_L)
plot(h7.log_Teff, h7.log_L)
plot(h8.log_Teff, h8.log_L)
plot(h9.log_Teff, h9.log_L)
plot(h10.log_Teff, h10.log_L)
plot(h11.log_Teff, h11.log_L)
plot(h12.log_Teff, h12.log_L)
plot(h13.log_Teff, h13.log_L)
plot(h14.log_Teff, h14.log_L)
plot(h15.log_Teff, h15.log_L)
plot(h16.log_Teff, h16.log_L)
plot(h17.log_Teff, h17.log_L)
plot(h18.log_Teff, h18.log_L)
plot(h19.log_Teff, h19.log_L)

#anote mass
plt.text(3.990, 1.125, r'$2 \mathrm{M_{\odot}}$', color='b')
plt.text(4.12, 1.82, r'$3 \mathrm{M_{\odot}}$', color='b')
plt.text(4.206, 2.299, r'$4 \mathrm{M_{\odot}}$', color='b')
plt.text(4.266, 2.66, r'$5 \mathrm{M_{\odot}}$', color='b')
plt.text(4.315, 2.93, r'$6 \mathrm{M_{\odot}}$', color='b')
plt.text(4.35, 3.16, r'$7 \mathrm{M_{\odot}}$', color='b')
plt.text(4.386, 3.37, r'$8 \mathrm{M_{\odot}}$', color='b')

#points of LxT_eff [x1= log(Teff) and y1 = log(L)] and errors dx1, dy1

x1 = (4.033, 4.012, 4.031, 4.102, 4.112, 4.126, 4.05, 4.162, 4.225, 4.143, 4.229)
y1 = (1.86, 2.45, 1.83, 2.22, 2.36, 3.10, 2.12, 3.20, 3.42, 2.98, 3.48)
dx1 = (0.016, 0.009, 0.015, 0.008, 0.002, 0.01, 0.016, 0.01, 0.009, 0.007, 0.006)
dy1 = (0.2, 0.12, 0.3, 0.06, 0.03, 0.1, 0.27, 0.1, 0.1, 0.14, 0.06)
#plt.text(x1, y1, r'$\bullet$', fontsize=18, color= 'blue';fmt = '[marker][line][color]fmt = 'o--b'')
(_, caps, _) = plt.errorbar(x1, y1, xerr=dx1, yerr=dy1, fmt = '.b', capsize=2.5,  elinewidth=0.8, markeredgewidth=0.02)

# star's numbers [i]

plt.text(4.030, 1.715, r'$[1]$', color='b')
plt.text(4.003, 2.42, r'$[2]$', color='b')
plt.text(4.028, 1.92, r'$[3]$', color='b')
plt.text(4.094, 2.236, r'$[4]$', color='b')
plt.text(4.121, 2.425, r'$[5]$', color='b')
plt.text(4.116, 3.09, r'$[6]$', color='b')
plt.text(4.078, 1.985, r'$[7]$', color='b')
plt.text(4.153, 3.25, r'$[8]$', color='b')
plt.text(4.214, 3.375, r'$[9]$', color='b')
plt.text(4.135, 2.901, r'$[10]$', color='b')
plt.text(4.245, 3.59, '[11]', color='b')

# ticks

# set axis labels
xlabel(r'$ \mathrm{log} \left(\mathrm{T_{eff}}\right)$')
ylabel(r'$\mathrm{log} \ \left(\mathrm{L/L_{\odot}} \right)$')

# invert the x-axis
plt.gca().invert_xaxis()

#fig.tight_layout()

#plt.show()

savefig('hr_diagram_c13.pdf')
