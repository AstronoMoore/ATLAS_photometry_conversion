# Basic scipt to convert forced photometry server output to be read by the clean_atlas_lc.py code. 
# T. Moore 3rd August 2022
# Inputs SN Name forced photometry file 
#
# Example command $ python fp_to_clean.py 2021ckj fored_photometry_file.txt

import pandas as pd 
import os
import sys
cwd = os.getcwd()

# Name of the SN 
SN_name = str(sys.argv[1])
print(f'The SN Name is {SN_name}')

# Forced photometry sever filename 
FP_file = str(sys.argv[2])
print(f'The forced photometry file path {FP_file}')

# making the output folder in the format required for clean_atlas_lc.py to work 
output_folder = cwd + '/' + SN_name
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

df = pd.read_table(FP_file, delim_whitespace=True)
df = df.rename(columns={"###MJD": "MJD"})
df_c = df[df['F'] == 'c'].to_csv(SN_name + '/' + SN_name+'.c.lc.txt','\t',index=False)
df_o = df[df['F'] == 'o'].to_csv(SN_name + '/' + SN_name+'.o.lc.txt','\t',index=False)

print(f'The file has been returned to {output_folder}')

