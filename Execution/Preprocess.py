import numpy as np
import matplotlib.pyplot as plt 
import scipy
import pandas as pd
import re
import os

def loaddata(datacsvfn,b2f_csv):
    """
    ######  b2fcsv format ####### 
    # #Observed Passband,filter
    # FUV_(GALEX)_AB,FUV
    # NUV_(GALEX)_AB,NUV
    # u_(SDSS_Model)_AB,sdss.up
    # u_(SDSS)_AB,sdss.up
    # ...
    #############################
    """
    ## read file
    df = pd.read_csv(datacsvfn, header=0)
    df['NED Uncertainty'] = df['NED Uncertainty'].fillna("0")
    ## rename column, modifying data
    df = df.rename(columns={'Flux Density':'Flux Density(Jy)', 'NED Uncertainty':'NED Uncertainty(Jy)'})
    ## delete '+/-' and '...'
    df['NED Uncertainty(Jy)'] = df['NED Uncertainty(Jy)'].apply(lambda x: float(x.replace('+/-','').replace('...','0')))
    ## join each word in each string value with '_'
    df['Published frequency'] = df['Published frequency'].apply(lambda x: "_".join(x.split()))
    df['Observed Passband'] = df['Observed Passband'].apply(lambda x: "_".join(x.split()))
    
    ## rename and chg the flux density units from Jy to mJys
    df_tmp = df.rename(columns={'Flux Density(Jy)':'Flux Density(mJy)'})
    df_tmp = df_tmp.rename(columns={'NED Uncertainty(Jy)':'NED Uncertainty(mJy)'})
    df_tmp['Flux Density(mJy)'] = df['Flux Density(Jy)'].apply(lambda x:x*1000)
    df_tmp['NED Uncertainty(mJy)'] = df['NED Uncertainty(Jy)'].apply(lambda x:x*1000)
    if 'NED Units' in df_tmp.columns.to_list():
        df_tmp = df_tmp.drop(['NED Units'], axis=1)
    df_tmp['Flux Density(mJy)'][0]

    ## load bands to filter list
    ## add filter list to the data frame.
    key_, val_ = np.loadtxt(b2f_csv, dtype=str, delimiter=',', skiprows=0, unpack=True)
    df_tmp['filter']=df_tmp['Observed Passband'].copy()

    for i in range(len(key_)):
        df_tmp['filter'] = df_tmp['filter'].replace([key_[i]],val_[i])

    return df_tmp

def mkheader(filterlistfn):
    """  filter list format
    ###### hdrcsvfn format####
    # #filter
    # FUV
    # NUV
    # sdss.up
    # WISE4
    # MIPS1
    # ...
    ##########################
    # """
    val_ = np.loadtxt(filterlistfn, dtype=str, delimiter=',', skiprows=1, unpack=True)
    hdr = ["id", "redshift"]
    for i in  range(len(val_)):
        if val_[i] != 'Nan':
            hdr = hdr + [val_[i], val_[i]+'_err']
    return hdr

## cigale input data format: idname redshift flux1 flux1_err .... 
def mkdata(idname,redz, df, hdr):
    data=[f"{idname}", f"{redz}"]
    for i in range(2, len(hdr), 2): #len(hdr)
        if df.index[df['filter'] == hdr[i]].size > 0 :
            idx = df.index[df['filter'] == hdr[i]][0]
            flux = df['Flux Density(mJy)'].iloc[idx]
            flux_str = re.sub(r'0+$', r'0', f"{flux:.3e}")
            if df['NED Uncertainty(mJy)'].iloc[idx] != 0:
                flux_err = df['NED Uncertainty(mJy)'].iloc[idx]
            else:
                flux_err = flux*0.1
            flux_err_str = re.sub(r'0+$', r'0', f"{flux_err:.3e}")
        else:
            flux_str, flux_err_str = "-99.999e+00", "-99.99e+00"
        data = data + [flux_str, flux_err_str]
    return data

def main(datafnlist, redzlist, filtertxt, b2fcsv):
    dflist=[]
    datalist=[]
    hdr  = mkheader(filtertxt)
    for datafn,redz in zip(datafnlist,redzlist):
        databn = os.path.basename(datafn)
        idname, ext = os.path.splitext(databn)
        ## load data
        df = loaddata(datafn,b2fcsv)
        dflist += [df]
        ## make data
        datalist += [mkdata(idname, redz, df, hdr)]
    return hdr, datalist


# ## input data file will expected to be comma-separated values file . 
# datafnlist=["../NGC5813/Test.csv"]  ## input
# redzlist = ['0.0653'] ## input

# ## filter list
# filtertxtfn = 'filters.txt'  ## input

# ## band 2 filter list name
# b2fcsv = "bands_to_filter_full_v1.csv"  ## input

# ## make header make data
# hdr, datalist = main(datafnlist, redzlist, filtertxtfn, b2fcsv)

# print(f"There are {len(datafnlist)} obj loaded.")

# df = pd.DataFrame(datalist, columns = hdr)
# df['id'][0] = "NGC5813"


# ## save the data into cigale input txtfile
# fn = "../NGC5813/cigale_input.txt"   ### input
# np.savetxt(fn, df.values ,fmt='%s', header=" ".join(hdr))

def preprocess(datafnlist, redzlist, filtertxtfn, b2fcsv):
    hdr, datalist = main(datafnlist, redzlist, filtertxtfn, b2fcsv)
    print(f"There are {len(datafnlist)} obj loaded.")
    df = pd.DataFrame(datalist, columns = hdr)
    df['id'][0] = "NGC5813"
    ## save the data into cigale input txtfile
    fn = "../NGC5813/cigale_input.txt"   ### input
    np.savetxt(fn, df.values ,fmt='%s', header=" ".join(hdr))

# preprocess(["../NGC5813/Test.csv"], ['0.0653'], "./filters.txt", "./bands_to_filter_full_v1.csv")