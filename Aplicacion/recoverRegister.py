import csv
import specdal 
import pandas as pd

def get_df_from_txt(file):
    data = pd.read_csv(file,delimiter='\t')
    return data

def create_df_from_txt(file):
    data = pd.read_csv(file,delimiter='\t')
    # create pandas dataframe
    df = pd.DataFrame(columns=['Wavelength','reflectance'])
    x = data.columns[0]
    y = data.columns[1]
    df['Wavelength'] = data[x]
    df['reflectance'] = data[y]
    return df

def get_df_from_asd(file):
    data = specdal.Spectrum(filepath=file)
    data_wl = data.measurement

    # create pandas dataframe
    df = pd.DataFrame(columns=['Wavelength','reflectance'])
    df['Wavelength'] = data_wl.index
    df['reflectance'] = data_wl.values
    return df
