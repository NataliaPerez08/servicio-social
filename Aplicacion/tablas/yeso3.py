import os
import recoverRegister as rr
import pandas as pd
"""
Pigmentos:
Cinabrio. Kremer (Y3: A1-A5)
Almagre	(Y3: B1-B5)
Azarcón o minio (Y3: C1-C5)
Laca de cochinilla (Y3: D1-D5)
Laca de alizarina	(Y3: E1-E5)

Carpeta,Tabla,Espectro,Pigmento,Aglutinante,Base de preparación
"""
def obtener_yeso_Y3_tablas_2():
    # Info de Tabla 2
    dir = "Espectros_FORS_2/Tablas 2/Tabla_Y3"
    archivos=list()
    for f in os.listdir(dir):
        archivos.append(dir+"/"+f)
    archivos.sort()
    
    tmp = archivos[0:5]
    cinabrio = obtener_dframes(tmp,"Cinabrio")

    tmp = archivos[5:10]
    almagre = obtener_dframes(tmp,"Almagre")

    tmp = archivos[10:15]
    azarcon_o_minio = obtener_dframes(tmp,"Azarcon o minio")

    tmp = archivos[15:20]
    laca_de_cochinilla = obtener_dframes(tmp,"Laca de cochinilla")

    tmp = archivos[20:25]
    laca_de_alizarina = obtener_dframes(tmp,"Laca de alizarina")

    return [cinabrio,almagre,azarcon_o_minio,laca_de_cochinilla,laca_de_alizarina]

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
        dataframe['tabla'] = "Y3"
        dataframe['espectro'] = l.split("/")[-1]

        dframes.append(dataframe)

    dframes[0]['aglutinante'] = "Aceite de linaza"
    dframes[1]['aglutinante'] = "Yema de huevo"
    dframes[2]['aglutinante'] = "Yema de huevo y aceite de linaza"
    dframes[3]['aglutinante'] = "Cola de conejo"
    dframes[4]['aglutinante'] = "Almáciga y aceite de linaza"
    return dframes

def obtener_yeso_Y3():
    return obtener_yeso_Y3_tablas_2()


def imprimir():
    espectros = obtener_yeso_Y3_tablas_2()
    for f in espectros:
        for o in f:
            print(o['carpeta'][0]+" "+o['tabla'][0]+" "+o['espectro'][0]+" "+o['pigmento'][0]+" "+o['aglutinante'][0]+" "+o['base'][0])
