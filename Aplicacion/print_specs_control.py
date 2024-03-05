"""
Este archivo contiene las funciones para imprimir las gráficas de los espectros
"""
from matplotlib import pyplot as plt
import specdal as specdal
import recoverRegister as rr

def print_spec(specs_df,ruta):
    """ 
    Este método se encarga de imprimir el espectro a partir de un dataframe y una ruta
        @param specs_df: dataframe con los espectros
        @param ruta: ruta del espectro
    """
    etiqueta=ruta.split('/')[2]
    base= ruta.split('/')[1]
    print(ruta.split('/'))
    if len(ruta.split('/')) > 3:
        tabla= ruta.split('/')[3]
    else:
        tabla=''
    x=specs_df.columns[0]
    y=specs_df.columns[1]
    dev_x = specs_df[x].to_numpy()
    dev_y = specs_df[y].to_numpy()
    plt.plot(dev_x, dev_y)
    plt.xlabel('Wavelength')
    plt.ylabel('Reflectance')
    t = base,etiqueta,tabla
    plt.title(t)
    plt.show()

def print_spec_from_df(specs_df,titulo=""):
    """ 
    Este método se encarga de imprimir el espectro a partir de un dataframe
        @param specs_df: dataframe con los espectros
        @param titulo (opcional): título de la gráfica
    """
    x=specs_df.columns[0]
    y=specs_df.columns[1]
    dev_x = specs_df[x].to_numpy()
    dev_y = specs_df[y].to_numpy()
    plt.plot(dev_x, dev_y)
    plt.xlabel('Wavelength')
    plt.ylabel('Reflectance')
    plt.title(titulo)
    plt.show()

def print_spec_from_ruta(ruta,titulo=""):
    """ 
    Este método se encarga de imprimir el espectro a partir de una ruta
        @param ruta: ruta del espectro
        @param titulo (opcional): título de la gráfica
    """
    ext = ruta.split(".")[-1]
    if ext == "txt":
        df = rr.create_df_from_txt(ruta)
        print_spec_from_df(df,titulo)

    elif ext == "asd":
        df = rr.get_df_from_asd(ruta)
        print_spec_from_df(df,titulo)
    else:
        print("Error")