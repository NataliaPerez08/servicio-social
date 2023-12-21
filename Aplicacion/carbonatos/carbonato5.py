import os
import recoverRegister as rr
import pandas as pd
"""
Pigmentos:
Acetato básico de cobre. Verdigris	(C5: A1-A5)
Malaquita africana (C5: B1:B5)
Tierra verde de Verona (C5: C1:C5)
Negro de huesos (C5: D1-D5)
Negro de humo(C5: E1-E5)	
"""

def obtener_carbonato_C5_tablas_2():
    # Info de Tabla 2
    dir = "Espectros_FORS_2/Tablas 2/Tabla_C4"
    archivos=list()
    for f in os.listdir(dir):
        archivos.append(dir+"/"+f)
    archivos.sort()

    tmp = archivos[0:5]
    acetato_cobre = obtener_dframes(tmp,"Acetato básico de cobre")

    tmp = archivos[5:10]
    malaquita = obtener_dframes(tmp,"Malaquita africana")

    tmp = archivos[10:15]
    tierra_verde = obtener_dframes(tmp,"Tierra verde de Verona")

    tmp = archivos[15:20]
    negro_huesos = obtener_dframes(tmp,"Negro de huesos")

    tmp = archivos[20:25]
    negro_humo = obtener_dframes(tmp,"Negro de humo")

    return [acetato_cobre,malaquita,tierra_verde,negro_huesos,negro_humo]

def obtener_dframes(lista,pigmento):
    dframes = list()

    for l in lista:
        dataframe = pd.DataFrame(columns=['wavelength','reflectance','pigmento','aglutinante','base','path','carpeta','tabla','espectro'])
        df = rr.create_df_from_txt(l)
        # crear dataframe
        dataframe['wavelength'] = df['Wavelength']
        dataframe['reflectance'] = df['reflectance']
        dataframe['pigmento'] = pigmento
        dataframe['path'] = l
        dataframe['base'] = "Carbonato de calcio"   
        dataframe['carpeta'] = "Tablas2"
        dataframe['tabla'] = "C2"
        dataframe['espectro'] = l.split("/")[-1]

        dframes.append(dataframe)

    dframes[0]['aglutinante'] = "Aceite de linaza"
    dframes[1]['aglutinante'] = "Aceite de nuez "
    dframes[2]['aglutinante'] = "Yema de huevo y aceite de linaza"
    dframes[3]['aglutinante'] = "Cola de conejo"
    dframes[4]['aglutinante'] = "Almáciga y aceite de linaza"
    return dframes


def imprimir():
    ocre_mina_ingles = obtener_carbonato_C5_tablas_2()
    for f in ocre_mina_ingles:
        for o in f:
            print(o['carpeta'][0]+" "+o['tabla'][0]+" "+o['espectro'][0]+" "+o['pigmento'][0]+" "+o['aglutinante'][0]+" "+o['base'][0])