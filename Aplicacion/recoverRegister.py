"""
Este archivo contiene las funciones para recuperar los datos de los archivos
"""
import specdal 
import pandas as pd

def get_df_from_txt(file):
    """ 
    Este método se encarga de obtener un dataframe a partir de un archivo txt 
        @param file: archivo txt
        @return: DataFrame
    """
    data = pd.read_csv(file,delimiter='\t')
    return data

def create_df_from_txt(file):
    """ 
    Este método se encarga de crear un dataframe a partir de un archivo txt
        @param file: archivo asd
        @return: DataFrame
    """
    data = pd.read_csv(file,delimiter='\t')
    # create pandas dataframe
    df = pd.DataFrame(columns=['Wavelength','reflectance'])
    x = data.columns[0]
    y = data.columns[1]
    df['Wavelength'] = data[x]
    df['reflectance'] = data[y]

    return df

def get_df_from_asd(file):
    """ 
    Este método se encarga de obtener un dataframe a partir de un archivo asd
        @param file: archivo asd
        @return: DataFrame
    """
    data = specdal.Spectrum(filepath=file)
    data_wl = data.measurement

    # create pandas dataframe
    df = pd.DataFrame(columns=['Wavelength','reflectance'])
    df['Wavelength'] = data_wl.index
    df['reflectance'] = data_wl.values
    return df


def get_df_from_ruta(ruta):
    """ 
    Este método se encarga de obtener un dataframe a partir de una ruta.
        @param ruta: ruta del archivo
        @return: DataFrame
    """
    ext = ruta.split(".")[-1]
    if ext == "txt":
        return get_df_from_txt(ruta)
    elif ext == "asd":
        return get_df_from_asd(ruta)
    else:
        return None