# Criado por Alan e adaptado por Bergerson Van Hallen
# 24/04/2021
# Plot das curvas de luz com seus periodogramas
# Plot do IVS após critérios de combinhações de frequência,
# 20% da frequência de maior amplitude e resolução 2.5/T

# import numpy lib
import numpy as np
# start pylab mode
from matplotlib.pyplot import *
import pylab
#from matplotlib.pyplot import *
import matplotlib.pyplot as plt
from pylab import *
#latex sintaxe
from matplotlib import rc
# for ticks
import matplotlib.ticker as tkr
#legend
import matplotlib.lines as mlines
import pandas as pd
import os  # obter nome da pasta
import glob # ler multiplos
#for mark references
from matplotlib.lines import Line2D
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

#start_time=time.time()

names=np.sort(['200173850', '200173864', '200173869', '200173871', '210650598', '210671425', '210737173', '210853356', '210873575', '246697679', '246698204', '246704649', '246788829', '246820783', '246937768', '246968117', '246970807', '246988320', '247031423', '247131891', '247146962', '247147343', '247147476', '247148453', '247153152', '247160983', '247164195', '247169098', '247169375', '247192878', '247211157', '247234723', '247264203', '247273628', '247278704', '247368219', '247430338', '247457814', '247495377', '247541278', '247551785', '247554799', '247559520', '247612547', '247682580', '247688426', '247692298', '247692420', '247695418', '247696147', '247698073', '247705729', '247709560', '247714018', '247714396', '247742016', '247745384', '247757517', '247759652', '247774959', '247786632', '247806245', '247889905', '247895553', '247935687', '248064520', '248150769', '248227339'])

#names=np.sort(['200173850', '200173864'])  

dir_entrada = '/home/bergerson/Documents/Astronomia/kepler/c13/photometry/k2sc_pdc_plot/k2sc_corte/csv_pol/'
dir_entrada1 = '/home/bergerson/Documents/Astronomia/kepler/c13/photometry/k2sc_pdc_plot/k2sc_corte/cleanest/plot_ivs/'
dir_entrada2 = '/home/bergerson/Documents/Astronomia/kepler/c13/photometry/k2sc_pdc_plot/k2sc_corte/cleanest/cleanest_c13_k2sc/'
dir_saida = '/home/bergerson/Documents/Astronomia/kepler/c13/photometry/k2sc_pdc_plot/k2sc_corte/lc_clean_ivs_criterios/'  



#chi_total=0
from matplotlib.backends.backend_pdf import PdfPages
i=0
with PdfPages('lc_clean_ivs_crite_c13.pdf') as pdf:
    for name in names:
       
       
        ##cleanest
        #folder_cleanest=(os.getcwd()[:-48]+'/home/bergerson/Documents/Astronomia/kepler/c13/photometry/k2sc_pdc_plot/k2sc_corte/cleanest/cleanest_c13_k2sc/')

        #DataCleanest=np.genfromtxt(folder_cleanest+'ccleanest_EPIC_'+name+'.dat')
        DataCleanest=np.genfromtxt(dir_entrada2+'ccleanest_EPIC_'+name+'.dat')

        freq_c=DataCleanest[:,0]
        power_c=DataCleanest[:,1]
        amplitude_c=DataCleanest[:,3]

        ###curva de luz
        #folder_lc=os.getcwd()[:-48]+dir_entrada
        #lc=np.loadtxt(folder_lc+'EPIC_'+name+'_k2sc_pol-2'+'.csv', delimiter=",")
        lc=np.loadtxt(dir_entrada+'EPIC_'+name+'_k2sc_pol-2'+'.csv', delimiter=",")
        time_lc=lc[:,0]
        flux_lc=lc[:,1]

        ########## IVS prewithening  
        #resultado_pw=np.load(os.getcwd()[:-48]+dir_entrada1+'EPIC_'+name+'_ivs'+'.npy')
        resultado_pw=np.load(dir_entrada1+'EPIC_'+name+'_ivs'+'.npy')

        #resultado_pw=resultado_pw[np.where(resultado_pw['stopcrit']>=5.0)]
        resultado_pw=resultado_pw[np.where(resultado_pw['freq']>0.1)]
        resultado_pw=resultado_pw[np.where(resultado_pw['freq']<23.99)]

        resultado_pw_ordenado_ampl=resultado_pw[np.argsort(resultado_pw,order=('ampl'))]
        if resultado_pw_ordenado_ampl['freq'].shape[0]>1:
            f0=resultado_pw_ordenado_ampl['ampl'][-1]
        else:
            f0=0
        resultado_pw_ordenado_ampl=resultado_pw_ordenado_ampl[np.where(resultado_pw_ordenado_ampl['ampl']>=0.2*f0)]
       
        if resultado_pw_ordenado_ampl.shape[0]==0:
            continue      
       
        f_resolution=2.5/(time_lc[-1]-time_lc[0])
        ############## resolução
        matrix_i=np.empty([0,0],dtype=int)
        for i in range(resultado_pw_ordenado_ampl.shape[0]-1):
            other_indices=np.delete(resultado_pw_ordenado_ampl,[i])
            matrix_j=np.empty([0,0],dtype=int)
            for j in range(i+1,other_indices.shape[0]):
                delta_freq=np.absolute(other_indices['freq'][j]-resultado_pw_ordenado_ampl['freq'][i])

                if delta_freq>f_resolution:
                    matrix_j=np.append(matrix_j,[0])
                else:
                    matrix_j=np.append(matrix_j,[1])
            matrix_i=np.append(matrix_i,np.sum(matrix_j,keepdims=True))
        matrix_i=np.append(matrix_i,[0])
        #print(matrix_i.sum())
        resultado_pw_ordenado_ampl_valid=resultado_pw_ordenado_ampl[(matrix_i<1).astype(bool)]
       
        #print(resultado_pw_ordenado_ampl_valid)
        resultado_pw_valid=resultado_pw_ordenado_ampl_valid[np.argsort(resultado_pw_ordenado_ampl_valid,order=('freq'))]

        resultado_pw=resultado_pw_valid
         
        ###########combinações
        if resultado_pw_ordenado_ampl_valid['freq'].shape[0]>1:

            f1=resultado_pw_valid['freq'][0]
            f2=resultado_pw_valid['freq'][1]
#             f3=0*resultado_pw_valid['freq'][2]
        else:
            f1=0
            f2=0
#             f3=0


        f_comb=np.empty([0,0],dtype=float)
#         n=np.arange(-4,4)
#         m=np.arange(-4,4)
#         o=np.arange(-4,4)        
        n=[0,1,2,3,4]
        m=[0,1,2,3,4]
        o=[0,1,2,3,4]
       
#         for n_i in n:
#             for m_j in m:
#                 for o_k in o:  
#                     f_comb_i_j_k=f1*n_i+f2*m_j+f3*o_k
#                     f_comb=np.append(f_comb,f_comb_i_j_k)
        for n_i in n:
            for m_j in m:
                 
                f_comb_i_j_k=f1*n_i+f2*m_j
                f_comb=np.append(f_comb,f_comb_i_j_k)            
        f_comb=f_comb[np.where(f_comb>(f2+f_resolution))]
       
    #harmonicos      
        for n_i in [2,3,4,5,6]:
            f_comb_h=n_i*f1
            f_comb=np.append(f_comb,f_comb_h)
            f_comb_h=n_i*f2
            f_comb=np.append(f_comb,f_comb_h)

        #freq_ivs_sorted=np.sort(freq_ivs)
        abs_f_comb=np.absolute(f_comb)
        abs_f_comb=(f_comb)
        abs_f_comb=abs_f_comb[np.where(abs_f_comb>0)]


       
        eliminadas=np.empty([0,0],dtype=int)
        for abs_f_comb_i in abs_f_comb:
            a=np.absolute(resultado_pw_valid['freq']-abs_f_comb_i)
            b=np.where(a<f_resolution)
#             c=np.where(b!=0)

            eliminadas=np.append(eliminadas,b)
        combination_indices=np.unique(eliminadas)

        resultado_pw_no_combination=np.delete(resultado_pw_valid,combination_indices,0)

        resultado_pw_only_combination=np.setdiff1d(resultado_pw,resultado_pw_no_combination)
        #########
        freq_ivs_only_combination=resultado_pw_only_combination['freq']#[np.where(resultado_pw['freq']>0.04)]
        amplt_ivs_only_combination=resultado_pw_only_combination['ampl']#[np.where(resultado_pw['freq']>0.04)]

        freq_ivs_no_combination=resultado_pw_no_combination['freq']#[np.where(resultado_pw['freq']>0.04)]
        amplt_ivs_no_combination=resultado_pw_no_combination['ampl']#[np.where(resultado_pw['freq']>0.04)]
       
        ###todas
        freq_ivs_all=np.append(freq_ivs_only_combination,freq_ivs_no_combination)
        resultado_pw_new=np.append(resultado_pw_no_combination,resultado_pw_only_combination)
        ################ termina combinações   #####
       
              
        ##### separa a estrela como tendo frequencias, e se sim, em quais regiões:
        numero_total_de_frequencias=freq_ivs_all.shape[0]
        numero_combinacoes_frequencias=freq_ivs_only_combination.shape[0]
        numero_de_frequencias_baixas=freq_ivs_all[np.where(freq_ivs_all<=5.0)].shape[0]
        numero_de_frequencias_altas=freq_ivs_all[np.where(freq_ivs_all>=5.0)].shape[0]

        #if numero_total_de_frequencias==0:
        #    obj_nenhuma_frequencia_encontrada=np.append(obj_nenhuma_frequencia_encontrada,name)
        #elif numero_de_frequencias_altas==0 and numero_de_frequencias_baixas>0:
        #    obj_frequencias_baixas=np.append(obj_frequencias_baixas,name)
        #elif numero_de_frequencias_altas>0 and numero_de_frequencias_baixas==0:
        #    obj_frequencias_altas=np.append(obj_frequencias_altas,name)
        #elif numero_de_frequencias_altas>0 and numero_de_frequencias_baixas>0:
        #    obj_frequencias_mistas=np.append(obj_frequencias_mistas,name)
        ######## fim da preclassificação^^.
   
        ######plots
        fig, (ax,ax1,ax2,ax3) = plt.subplots(4,1,figsize=(8,14))
       
       # Set general font size
        plt.rcParams['font.size']='11'
	##########IVS plot
        #######log
        ax.set_title(r'EPIC '+name, fontsize=18)
        ax.plot(time_lc,flux_lc,'-', color='blue')
        #ax.set(xlabel='Time (days)', ylabel='Flux variation (ppm)')
        ax.set(xlabel=r'$\mathrm{Time \ [BJD-2454833]}$', ylabel=r'$\mathrm{Flux \ variation \ [ppm]}$')
        #ax.set(xlabel=r'$\mathrm{Tempo \ [BJD-2454833]}$', ylabel=r'$\mathrm{Fluxo \ [ppm]}$')
        #ax.set_yscale("log")
        #######linear
        ax1.plot(1/freq_c,amplitude_c,lw=0.5, color='black', label=r'$\mathrm{CLEANEST}$')

        ax1.plot(1/freq_ivs_only_combination,amplt_ivs_only_combination,'v',color='orange',label=r'$\mathrm{IVS, comb.}$')
        ax1.plot(1/freq_ivs_no_combination,amplt_ivs_no_combination,'v',color='fuchsia',label=r'$\mathrm{IVS, prewhitened}$') #color='fuchsia'
        ax1.vlines(1/freq_ivs_no_combination,[0],amplt_ivs_no_combination,lw=0.8,color='blue', linestyle='dashed',label=r'$\mathrm{n^{o}. \ freq.: }$'+str(numero_total_de_frequencias))
        ax1.vlines(1/freq_ivs_only_combination,[0],amplt_ivs_only_combination,lw=0.5,linestyle='dashed')
        ax1.vlines([1/3.5], 0, 1, transform=ax1.get_xaxis_transform(),lw=1.0, colors='r',linestyle='dashed')
        ax1.set(xlabel=r'$\mathrm{Period \ [day]}$', ylabel=r'$\mathrm{Amplitude \ [ppm]}$')
        #ax1.set(xlabel=r'$\mathrm{\tau \ [dia]}$', ylabel=r'$\mathrm{Amplitude \ [ppm]}$')
        ax1.legend(fontsize= 'small')
        props = dict(boxstyle='round', facecolor='wheat', alpha=0.1)
        textstr = '\n'.join((
            r'$\tau_0=%.3f$' % (1/resultado_pw_valid['freq'][0], ),
            r'$\tau_1=%.3f$' % (1/resultado_pw_valid['freq'][1] if len(freq_ivs_all)>=2 else 0, ),
            r'$\tau_2=%.3f$' % (1/resultado_pw_valid['freq'][2] if len(freq_ivs_all)>=3 else 0, ),
            r'$\tau_3=%.3f$' % (1/resultado_pw_valid['freq'][3] if len(freq_ivs_all)>=4 else 0, )))                   
        ax1.text(0.5, 0.95, textstr, transform=ax1.transAxes, fontsize=7,verticalalignment='top', bbox=props)
        
        ax1.set_xlim(0,24)
       
#         ax2.plot(freq_c,amplitude_c,lw=0.5,label='cleanest')
       
        ##########IVS plot
        #######log
        ax2.plot(freq_c,amplitude_c,lw=0.5, color='black', label=r'$\mathrm{CLEANEST}$')
        ax2.plot(freq_ivs_only_combination,amplt_ivs_only_combination,'v',color='orange',label=r'$\mathrm{IVS, comb.}$')
        ax2.plot(freq_ivs_no_combination,amplt_ivs_no_combination,'v',color='fuchsia',label=r'$\mathrm{IVS, prewhitened}$')
        ax2.vlines(freq_ivs_no_combination,[0],amplt_ivs_no_combination,lw=0.8,color='blue',linestyle='dashed')
        ax2.vlines(freq_ivs_only_combination,[0],amplt_ivs_only_combination,lw=0.8,color='blue', linestyle='dashed')
        ax2.vlines([3.5], 0, 1, transform=ax2.get_xaxis_transform(),lw=1.0, colors='r',linestyle='dashed')
        ax2.set(xlabel=r'$\mathrm{Frequency \ [1/day]}$', ylabel=r'$\mathrm{Amplitude \ [ppm]}$')
        #ax2.set(xlabel=r'$ \nu \ \mathrm{[c/d]}$', ylabel=r'$\mathrm{Amplitude \ [ppm]}$')
        ax2.legend(fontsize= 'small')
        ax2.set_xlim(0.1,24)
        ax2.set_xscale("log")
        #ax.set_yscale("log")
        #######linear
       
        ax3.plot(freq_c,amplitude_c,lw=0.5, color='black', label=r'$\mathrm{CLEANEST}$')
        ax3.plot(freq_ivs_no_combination,amplt_ivs_no_combination,'v',color='fuchsia',label=r'$\mathrm{IVS, prewhitened}$')
        ax3.plot(freq_ivs_only_combination,amplt_ivs_only_combination,'v',color='orange',label=r'$\mathrm{IVS, comb.}$')
        ax3.vlines(freq_ivs_no_combination,[0],amplt_ivs_no_combination,lw=0.8,color='blue',linestyle='dashed')
        ax3.vlines(freq_ivs_only_combination,[0],amplt_ivs_only_combination,lw=0.8,color='blue',linestyle='dashed')
        ax3.vlines([3.5], 0, 1, transform=ax3.get_xaxis_transform(),lw=1.0, colors='r',linestyle='dashed')
        ax3.set(xlabel=r'$\mathrm{Frequency \ [1/day]}$', ylabel=r'$\mathrm{Amplitude \ [ppm]}$')
        #ax3.set(xlabel=r'$ \nu \ \mathrm{[c/d]}$', ylabel=r'$\mathrm{Amplitude \ [ppm]}$')
        ax3.legend(fontsize= 'small')
        props = dict(boxstyle='round', facecolor='wheat', alpha=0.1)
        textstr = '\n'.join((
            r'$\nu_0=%.3f$' % (resultado_pw_valid['freq'][0], ),
            r'$\nu_1=%.3f$' % (resultado_pw_valid['freq'][1] if len(freq_ivs_all)>=2 else 0, ),
            r'$\nu_2=%.3f$' % (resultado_pw_valid['freq'][2] if len(freq_ivs_all)>=3 else 0, ),
            r'$\nu_3=%.3f$' % (resultado_pw_valid['freq'][3] if len(freq_ivs_all)>=4 else 0, ),
            r'$\nu_4=%.3f$' % (resultado_pw_valid['freq'][4] if len(freq_ivs_all)>=5 else 0, ),
            r'$\mathrm{n^{o}. \ freq.=}$' + str(numero_total_de_frequencias),
            r'$\mathrm{combinations=}$' + str(numero_combinacoes_frequencias)))
        #    'class:'+classification[i]))        
        ax3.text(0.5, 0.95, textstr, transform=ax3.transAxes, fontsize=7,verticalalignment='top', bbox=props)
        ax3.set_xlim(0.1,24)

        #ax4.plot(freq_c,amplitude_c,lw=0.5,label='cleanest')
        #ax4.plot(freq_ivs_no_combination,amplt_ivs_no_combination,'v',color='fuchsia',label='IVS, prewhitened')
        #ax4.plot(freq_ivs_only_combination,amplt_ivs_only_combination,'v',color='orange',label='likely combination')
        #ax4.vlines(freq_ivs_no_combination,[0],amplt_ivs_no_combination,lw=0.5,linestyle='dashed')
        #ax4.vlines(freq_ivs_only_combination,[0],amplt_ivs_only_combination,lw=0.5,linestyle='dashed')
        #ax4.set(xlabel='Frequency [1/day]', ylabel='Amplitude')
        #ax4.legend()
        #ax4.set_xlim(0.1,3)
        
        # Set general font size
        #plt.rcParams['font.size']='16'       
             
        #plt.show()
        pdf.savefig(fig)  # or you can pass a Figure object to pdf.savefig
        plt.close()
       
        #folder_ivs=os.getcwd()+dir_saida
        folder_ivs=dir_saida
       
        np.save(folder_ivs+'no_combination/'+name+'_no_combination.npy',resultado_pw_no_combination)
        np.savetxt(folder_ivs+'no_combination/'+name+'_no_combination.dat',np.transpose([freq_ivs_no_combination,amplt_ivs_no_combination]),delimiter=',')

       
        np.save(folder_ivs+'only_combination/'+name+'_only_combination.npy',resultado_pw_only_combination)
        np.savetxt(folder_ivs+'only_combination/'+name+'_possible_combination.dat',np.transpose([freq_ivs_only_combination,amplt_ivs_only_combination]),delimiter=',')
#        numero_de_frequencias=np.append(numero_de_frequencias,np.array([[name,numero_total_de_frequencias,numero_total_de_frequencias-numero_combinacoes_frequencias,numero_combinacoes_frequencias]]),axis=0)
        i=i+1
       
        #chi_total=chi_total+chi_sqr
        resultado_pw_valid=resultado_pw_valid[np.argsort(resultado_pw_valid,order=('ampl'))]

        print(name,numero_combinacoes_frequencias,numero_total_de_frequencias,resultado_pw_valid['freq'][-1],resultado_pw_valid['ampl'][-1],1/resultado_pw_valid['freq'][-1])
       

# folder_ivs+'numero_de_frequencias'+'.npy'
