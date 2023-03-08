## galactic EXtinction correction
import numpy as np
import pandas as pd
from numpy import log as ln
from numpy import log10 as log
from numpy import arcsinh
from numpy import sinh

def extinction_correction(fv, EBV, filt):
    """
    fv : flux density  (units=mJy)
    EBV : E(B-V) value
    filt : FUV, NUV, sdss.up, sdss.gp, sdss.rp, sdss.ip, sdss.zp
    Note: This script convert flux to AB mag 
          then do the galactic extinciton, 
          after that convert back to flux.
    """
    mag = -2.5*log(fv/1000/3631)
    if filt == "FUV":
        A = 10.47*(EBV) + 8.59*(EBV)**2 - 82.8*(EBV)**3
    elif filt == "NUV":
        A = 8.36*(EBV) + 14.3*(EBV)**2 - 82.8*(EBV)**3
    elif filt == "sdss.up" or filt == "u_prime":
        A = 4.39*EBV
    elif filt == "sdss.gp" or filt == "g_prime":
        A = 3.30*EBV
    elif filt == "sdss.rp" or filt == "r_prime":
        A = 2.31*EBV
    elif filt == "sdss.ip" or filt == "i_prime":
        A = 1.71*EBV
    elif filt == "sdss.zp" or filt == "z_prime":
        A = 1.29*EBV
    elif filt == "DECaLS_g":
        A = 3.214*EBV
    elif filt == "DECaLS_r":
        A = 2.165*EBV
    elif filt == "DECaLS_z":
        A = 1.211*EBV
    else:
        A = 0
    # print("A",A)
    flux = 10**((mag-A)/(-2.5))*3631*1000 ## mJy
    return flux

# this part is just for the transformation of ABmag to flux density
# if not needed, just cite it with "#"
def mkflux (mag):
    flux = pow(10, (8.9 - mag) / (2.5))
    return flux*1000

def calcunc (mag, unc):
    fluxunc = 0.5*(mkflux(mag-unc)-mkflux(mag+unc))
    return fluxunc

## 根据需求更改一下脚本
###input ###
objname="NGC5813"    ## which obj in input txt to do
inputtxtfn="../"+objname+"/cigale_input.txt"
#bandtocorr=["FUV","NUV", "u_prime", "g_prime", "r_prime", "i_prime", "z_prime"] ## which band in input txt to filter
bandtocorr=["FUV", "NUV",]
#"sdss.up", "sdss.gp", "sdss.rp", "sdss.ip", "sdss.zp", "FUV", "NUV", "WISE1", "WISE2", "WISE3", "WISE4", "IRAC1", "IRAC2", "IRAC3", "IRAC4", "IRAS1", "IRAS2", "IRAS3", "IRAS4", "MIPS1", "MIPS2", "MIPS3"
EBV=0.0197     ## obtain from website
# 0.0308 for UGC842
# 0.0878 for NGC6482
# 0.0370 for NGC1600
# 0.0557 for NGC1132
# 0.0119 for OGC1248
# 0.0344 for M84
# 0.0197 for M87
# 
# 
# 
# 
# 
# #
##########
def extinctioncorr(objname, inputtxtfn, bandtocorr, EBV):

    ## load input txt
    hdr = np.loadtxt(inputtxtfn, dtype=str, max_rows=1, comments=None)[1:].tolist()
    data = np.loadtxt(inputtxtfn, dtype=str, ndmin=2).tolist()
    df = pd.DataFrame( data, columns=hdr )
    print(df)

    ## main loop
    df_new=df.copy()
    for band in bandtocorr:
        idx = df.index[ df['id'] == objname ][0]
        flux_mag = float(df[band].iloc[idx])
        flux = mkflux(flux_mag)
        flux_corr = extinction_correction(flux, EBV, band)
        
        unc = float(df[band+"_err"].iloc[idx])
        flux_unc = calcunc(flux_mag, unc)
        
        df_new[band][idx] = f"{flux_corr:.3e}"
        df_new[band+"_err"][idx] = f"{flux_unc:.3e}"
        
    ## save new extinction corrected file
    fn="../"+objname+"/cigale_input_corr.txt"
    np.savetxt(fn, df_new.values, fmt='%s', header=" ".join(hdr))

# extinctioncorr(objname, "../"+objname+"/cigale_input.txt", bandtocorr, EBV)