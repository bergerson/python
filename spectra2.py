import matplotlib.pylab as plt
import numpy as np
import os, glob
from glob import glob
from pylab import *
from astropy.io import ascii
from astropy.io import fits
from astropy.utils.data import get_pkg_data_filename
import scipy.constants as constants
from astropy.visualization import astropy_mpl_style
plt.style.use(astropy_mpl_style)


#add directory you have your files in
#dir = '/home/bergerson/Bergerson_PC3/16ago28' 
#dir = '.'

#def deal_with(single_filename):
    #file_handle = fits.open(single_filename)
    #result = do_whatever_processing(file_handle)
    # ...
    #return result
    


#OPEN ALL FILES AND STORE THEM INTO A LIST
#names = np.sort(['ret_247169098', 'ret_247368219', 'ret_247745384'])
#mylist = [ deal_with( 'ret_*.fits' % b ) for b in range(200) ]
#name = ('ret_247169098', 'ret_247368219', 'ret_247745384')
#list_of_filenames = sorted( glob.glob( 'ret_*.fit' ) )
#file = sorted( glob.glob( 'ret_*.fit' ) )
#mylist = [ deal_with( filename ) for filename in file ]

#file = [fits.open('*.fits' % i) for i in range(200)]
    
file = glob('hd32991_sum_norm.fits') 


#file = glob(dir + 'ret_247169098.fits')

#file = input('ret_247169098.fits')

# Einlesen von Header und Daten
#header = fits.getdata(file, header=True)
for fi in (file):
    #print(fi)
    name = fi[:-len('.fits')] #Remove '.fits' from the file name
    #name = ('ret_247169098', 'ret_247368219', 'ret_247745384')

    #with fits.open(dir + fi) as hdu:
    with fits.open(fi) as hdu:
        #fits.open(files)
        hdu.info()
        flux = hdu[0].data
        hdr = hdu[0].header #added to try2
        nax = hdr['NAXIS1']
        #a = hdr['NAXIS1']
        step = hdr['CDELT1'] #added to try2
        restw = hdr['CRVAL1'] #added to try2
        wave = zeros(nax)
        #wave = np.ones(['NAXIS1'], dtype=float)
for i in range(nax):
	wave[i] = restw + i*(step) #added to try
        	
# Writing the csv- and dat-files
#for y in name:
	ascii.write([wave, flux], name + '.csv', overwrite=True,
		names=['WAVE', 'FLUX'], format='csv')
#ascii.write([wave, flux], file.strip('.fits')+'.dat', overwrite=True,
	#names=['WAVE', 'FLUX'], format='tab') 
	
# if necessary, explicitly close the file here
#return result	

#plt.close()  

