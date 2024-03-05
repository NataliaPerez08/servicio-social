"""
Este módulo se encarga de controlar la busqueda de espectros
"""

"""
@import recoverRegister
@import print_specs_control
"""
from recoverRegister import get_df_from_asd,get_df_from_txt
from print_specs_control import print_spec

def obten_spec(carpeta,tabla,espectro):
    """
    Método encargado de obtener el espectro de la carpeta y tabla especificada
    @args:
        carpeta: carpeta donde se encuentra el espectro
        tabla: tabla donde se encuentra el espectro
        espectro: nombre del espectro
    @returns:
        Ruta del espectro
    """
    #print("Tratando de obtener",carpeta,tabla,espectro)
    if carpeta == 'Tablas1' or carpeta == 'Tablas 1':
      # print("Espectros_FORS_2/Tablas 1/"+tabla+"/"+espectro)
        return "../Espectros_FORS_2/Tablas 1/"+tabla+"/"+espectro
    elif carpeta == 'Tablas2':
        return "../Espectros_FORS_2/Tablas 2/Tabla_"+tabla+"/"+espectro
    else:
        # Tratamos de obtener el espetro
        #print("Espectros_FORS_2/"+carpeta+"/"+tabla+"/"+espectro)
        return "../Espectros_FORS_2/"+carpeta+"/"+tabla+"/"+espectro

def imprimir_spec(carpeta,tabla,espectro):
    """
    Método encargado de imprimir el espectro de la carpeta y tabla especificada
    @args:
        carpeta: carpeta donde se encuentra el espectro
        tabla: tabla donde se encuentra el espectro
        espectro: nombre del espectro
    """
    ruta=obten_spec(carpeta,tabla,espectro)
    ext=ruta[-3:]
    if ext == 'txt':
        df=get_df_from_txt(ruta)
    elif ext == 'asd':
        df=get_df_from_asd(ruta)
    print_spec(df,ruta)

def get_df(carpeta,tabla,espectro):
    """
    Método encargado de obtener el espectro de la carpeta y tabla especificada
        @args:
            carpeta: carpeta donde se encuentra el espectro
            tabla: tabla donde se encuentra el espectro
            espectro: nombre del espectro
        @returns:
            Dataframe con el espectro
    """
    ruta=obten_spec(carpeta,tabla,espectro)
    try:
        ext=ruta[-3:]
        if ext == 'txt':
            df=get_df_from_txt(ruta)
        elif ext == 'asd':
            df=get_df_from_asd(ruta)
        return df
    except:
        print("No se pudo obtener el espectro")
        return None
    

    
