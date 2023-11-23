from recoverRegister import get_df_from_asd,get_df_from_txt
from pre_process import print_spec

def obten_spec(carpeta,tabla,espectro):
    print(carpeta,tabla,espectro)
    if carpeta == 'Tablas1':
        if tabla=='Y4':
            return "Espectros_FORS_2/Y4/"+espectro
        else:
            return "Espectros_FORS_2/Tablas 1/"+tabla+"/"+espectro
    elif carpeta == 'Tablas2':
        return "Espectros_FORS_2/Tablas 2/"+espectro

def imprimir_spec(carpeta,tabla,espectro):
    ruta=obten_spec(carpeta,tabla,espectro)
    ext=ruta[-3:]
    if ext == 'txt':
        df=get_df_from_txt(ruta)
    elif ext == 'asd':
        df=get_df_from_asd(ruta)
    print_spec(df,ruta)