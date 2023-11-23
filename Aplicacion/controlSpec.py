from math import e
from recoverRegister import encuentra_ruta_spec_Y4,encuentra_spec_asd,encuentra_spec_txt,get_df_from_asd,get_df_from_txt
from pre_process import print_spec

def obten_spec(carpeta,tabla,espectro):
    print(carpeta,tabla,espectro)
    if carpeta == 'Tablas1':
        if tabla=='Y4':
            return encuentra_ruta_spec_Y4(espectro)
        else:
            aux = espectro[0:2].upper()
            print(aux)
            return encuentra_spec_asd(tabla,aux)
    elif carpeta == 'Tablas2':
        return encuentra_spec_txt(tabla,espectro)

def imprimir_spec(carpeta,tabla,espectro):
    ruta=obten_spec(carpeta,tabla,espectro)
    print(ruta)
    ext=ruta[-3:]
    if ext == 'txt':
        df=get_df_from_txt(ruta)
    elif ext == 'asd':
        df=get_df_from_asd(ruta)
    print_spec(df,ruta)