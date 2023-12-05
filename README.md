# ATLAS_photometry_conversion
These python scripts are used to convert ATLAS photometry betweent the formats required for using the SN group tools 

There are three formats of ATLAS forced photometry (FP) used within the group. 

1. raw FP downloaded from the ATLAS pages 
2. FP files from the FP server https://fallingstar-data.com/forcedphot/ 
3. Single filter files used as inputs to the new clean_atlas_lc.py tool 

# Motivation
The new light curve cleaning code downloads photometry from the forced server in a format ready to be used by clean_atlas_lc.py. 
However, we have a significant amount of compiled photometry for the 100 Mpc Rates & ATLAS long risers papers - the photometry needs to be converted to be used by clean_atlas_lc.py. In principle we could rerequest this photometry but this is wasteful especially since this is just a simple pandas problem. 
Photometry from telescopes 03 and 04 have not yet been added to the FP server and therfore our only access to FP is from the atlas pages. The goal of raw_to_fp.py is to convert from the atlas pages FP format to the format of the FP server. 

# Use case 

FP server output -> fp_to_clean.py -> clean_atlas_lc.py -> cleaned photometry 

Atlas page output -> raw to fp.py -> fp_to_clean.py -> clean_atlas_lc.py -> cleaned photometry


# Code

fp_to_clean.py is a hastily written code to convert the photometry (from the FP server) we already have to be compatible with clean_atlas_lc.py

raw_to_fp.py converts raw photometry from the atlas eyeballing page to be the same format as the output from the FP server. 


Goal is to take a raw output from the atlas page through to beinf compatible with the clean_atlas_lc.py python code.
 
