import os
import recoverRegister as rr
import pandas as pd
"""
Pigmentos:
Cinabrio (C3: A1-A5)
Almagre	(C3: B1-B5)
Azarcón o minio (C3: C3-C5)
Carmín de cochinilla (C3: D1-D5)
Laca de alizarina	(C3: E1-E5)
Carpeta,Tabla,Espectro,Pigmento,Aglutinante,Base de preparación
"""

def obtener_carbonato_C3_tablas_1():
    # Info de Tabla 1
    dir = "Espectros_FORS_2/Tablas 1/C3"
    archivos=list()
    for f in os.listdir(dir):
        archivos.append(f)
    archivos.sort()
    
    cinabrio = list()
    almagre = list()
    azarcon_o_minio = list()
    carmin_de_cochinilla = list()
    laca_de_alizarina = list()
    
    for f in archivos:
        dataframe = pd.DataFrame(columns=['wavelength','reflectance','pigmento','aglutinante','base','path','carpeta','tabla','espectro'])
        if f[0]=="A":
            df = rr.get_df_from_asd(dir+"/"+f)
            # crear dataframe
            dataframe['wavelength'] = df['Wavelength']
            dataframe['reflectance'] = df['reflectance']
            dataframe['pigmento'] = "Cinabrio"
            if f[1] == '1':
                dataframe['aglutinante'] = "Aceite de linaza"
            elif f[1] == '2':
                dataframe['aglutinante'] = "Aceite de nuez"
            elif f[1] == '3':
                dataframe['aglutinante'] = "Yema de huevo y aceite de linaza"
            elif f[1] == '4':
                dataframe['aglutinante'] = "Cola de conejo"
            elif f[1] == '5':
                dataframe['aglutinante'] = "Almáciga y aceite de linaza"
            dataframe['base'] = "Carbonato de calcio"
            dataframe['path'] = dir+"/"+f

            dataframe['carpeta'] = "Tablas1"
            dataframe['tabla'] = "C3"
            dataframe['espectro'] = f

            cinabrio.append(dataframe)
        elif f[0]=="B":
            df = rr.get_df_from_asd(dir+"/"+f)
            # crear dataframe
            dataframe['wavelength'] = df['Wavelength']
            dataframe['reflectance'] = df['reflectance']
            dataframe['pigmento'] = "Almagre"

            if f[1] == '1':
                dataframe['aglutinante'] = "Aceite de linaza"
            elif f[1] == '2':
                dataframe['aglutinante'] = "Aceite de nuez"
            elif f[1] == '3':
                dataframe['aglutinante'] = "Yema de huevo y aceite de linaza"
            elif f[1] == '4':
                dataframe['aglutinante'] = "Cola de conejo"
            elif f[1] == '5':
                dataframe['aglutinante'] = "Almáciga y aceite de linaza"

            dataframe['base'] = "Carbonato de calcio"
            dataframe['path'] = dir+"/"+f   

            dataframe['carpeta'] = "Tablas1"
            dataframe['tabla'] = "C3"
            dataframe['espectro'] = f

            almagre.append(dataframe)

        elif f[0]=="C":
            df = rr.get_df_from_asd(dir+"/"+f)
            # crear dataframe
            dataframe['wavelength'] = df['Wavelength']
            dataframe['reflectance'] = df['reflectance']
            dataframe['pigmento'] = "Ocre de mina inglés"
            if f[1] == '1':
                dataframe['aglutinante'] = "Aceite de linaza"
            elif f[1] == '2':
                dataframe['aglutinante'] = "Aceite de nuez"
            elif f[1] == '3':
                dataframe['aglutinante'] = "Yema de huevo y aceite de linaza"
            elif f[1] == '4':
                dataframe['aglutinante'] = "Cola de conejo"
            elif f[1] == '5':
                dataframe['aglutinante'] = "Almáciga y aceite de linaza"
            dataframe['base'] = "Carbonato de calcio"
            dataframe['path'] = dir+"/"+f

            dataframe['carpeta'] = "Tablas1"
            dataframe['tabla'] = "C3"
            dataframe['espectro'] = f
            azarcon_o_minio.append(dataframe)
        elif f[0]=="D":
            df = rr.get_df_from_asd(dir+"/"+f)
            # crear dataframe
            dataframe['wavelength'] = df['Wavelength']
            dataframe['reflectance'] = df['reflectance']
            dataframe['pigmento'] = "Carmín de cochinilla"
            if f[1] == '1':
                dataframe['aglutinante'] = "Aceite de linaza"
            elif f[1] == '2':
                dataframe['aglutinante'] = "Aceite de nuez"
            elif f[1] == '3':
                dataframe['aglutinante'] = "Yema de huevo y aceite de linaza"
            elif f[1] == '4':
                dataframe['aglutinante'] = "Cola de conejo"
            elif f[1] == '5':
                dataframe['aglutinante'] = "Almáciga y aceite de linaza"
            dataframe['base'] = "Carbonato de calcio"
            dataframe['path'] = dir+"/"+f

            dataframe['carpeta'] = "Tablas1"
            dataframe['tabla'] = "C3"
            dataframe['espectro'] = f

            carmin_de_cochinilla.append(dataframe)
        elif f[0]=="E":
            df = rr.get_df_from_asd(dir+"/"+f)
            # crear dataframe
            dataframe['wavelength'] = df['Wavelength']
            dataframe['reflectance'] = df['reflectance']
            dataframe['pigmento'] = "Ocre de mina inglés"
            if f[1] == '1':
                dataframe['aglutinante'] = "Aceite de linaza"
            elif f[1] == '2':
                dataframe['aglutinante'] = "Aceite de nuez"
            elif f[1] == '3':
                dataframe['aglutinante'] = "Yema de huevo"
            elif f[1] == '4':
                dataframe['aglutinante'] = "Cola de conejo"
            elif f[1] == '5':
                dataframe['aglutinante'] = "Almáciga y aceite de linaza"
            dataframe['base'] = "Carbonato de calcio"
            dataframe['path'] = dir+"/"+f

            dataframe['carpeta'] = "Tablas1"
            dataframe['tabla'] = "C3"
            dataframe['espectro'] = f

            laca_de_alizarina.append(dataframe)
    
    return [cinabrio,almagre,azarcon_o_minio,carmin_de_cochinilla,laca_de_alizarina]

def obtener_carbonato_C3():
    return obtener_carbonato_C3_tablas_1()

def imprimir():
    espectros = obtener_carbonato_C3_tablas_1()
    for f in espectros:
        for o in f:
            print(o['carpeta'][0]+" "+o['tabla'][0]+" "+o['espectro'][0]+" "+o['pigmento'][0]+" "+o['aglutinante'][0]+" "+o['base'][0])