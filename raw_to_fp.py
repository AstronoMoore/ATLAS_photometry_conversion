# Basic scipt to convert forced photometry server output to be read by the clean_atlas_lc.py code. 
# T. Moore 3rd August 2022
# Inputs SN Name forced photometry file 
#
# Example command $ python fp_to_clean.py 2021ckj fored_photometry_file.txt

import pandas as pd 
import os
import sys
cwd = os.getcwd()

# raw forced phot file 
FP_file = str(sys.argv[1])
print(f'The FP file is {FP_file}')

# This is the raw FP input
#expname,ra,dec,mag,dm,snr,filter,zp,mjd,x,y,peakval,skyval,peakfit,dpeak,skyfit,flux,dflux,chin,major,minor,snrdet,snrlimit,apfit,uJy,duJy,mag5sig,texp

# This is the required output format
###MJD          m      dm   uJy   duJy F err chi/N     RA       Dec        x        y     maj  min   phi  apfit mag5sig Sky   Obs
df = pd.read_csv(FP_file)

df = df[['mjd', 'mag', 'dm', 'uJy', 'duJy', 'filter', 'mag', 'chin', 'ra', 'dec', 'x', 'y', 'major', 'minor', 'mag', 'apfit', 'mag5sig', 'skyval', '#expname']]
cols = [['###MJD','m','dm','uJy','duJy','F','err','chi/N','RA','Dec','x','y','maj','min','phi','apfit','mag5sig','Sky','Obs']]
df.columns = cols
print('Output filename = ' + FP_file +'_FP_format.txt')
df.to_csv('raw_to_FP_'+FP_file,'\t',index=False)