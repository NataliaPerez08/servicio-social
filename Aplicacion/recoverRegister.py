"""
Este archivo contiene las funciones para recuperar los datos de los archivos
"""
import specdal 
import pandas as pd

""" 
Este método se encarga de obtener un dataframe a partir de un archivo txt 
    Args:
        file: archivo txt
"""
def get_df_from_txt(file):
    data = pd.read_csv(file,delimiter='\t')
    return data

""" 
Este método se encarga de obtener un dataframe a partir de un archivo asd
    Args:
        file: archivo asd
"""
def create_df_from_txt(file):
    data = pd.read_csv(file,delimiter='\t')
    # create pandas dataframe
    df = pd.DataFrame(columns=['Wavelength','reflectance'])
    x = data.columns[0]
    y = data.columns[1]
    df['Wavelength'] = data[x]
    df['reflectance'] = data[y]

    return df

""" 
Este método se encarga de obtener un dataframe a partir de un archivo asd
    Args:
        file: archivo asd
"""
def get_df_from_asd(file):
    data = specdal.Spectrum(filepath=file)
    data_wl = data.measurement

    # create pandas dataframe
    df = pd.DataFrame(columns=['Wavelength','reflectance'])
    df['Wavelength'] = data_wl.index
    df['reflectance'] = data_wl.values
    return df