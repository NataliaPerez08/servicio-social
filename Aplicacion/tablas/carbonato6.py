import os
import recoverRegister as rr
import pandas as pd
"""
Pigmentos:
(Tabla 1)
Bermellon	(C6: A1-A5)
Cochinilla (C6: B1:B5)
Azurita (C6: C6:C5)
Amarillo de plomo estaño (C6: D1-D5)
Blanco de plomo.Kremer (C6: E1-E5)	

Carpeta,Tabla,Espectro,Pigmento,Aglutinante,Base de preparación
"""

def obtener_carbonato_C6_tablas_1():
    # Info de Tabla 1
    dir = "Espectros_FORS_2/Tablas 1/C6"
    archivos=list()
    for f in os.listdir(dir):
        archivos.append(f)
    archivos.sort()
    
    bermellon = list()
    cochinilla = list()
    azurita = list()
    amarillo_plomo_estano = list()
    blanco_plomo = list()
    
    for f in archivos:
        dataframe = pd.DataFrame(columns=['wavelength','reflectance','pigmento','aglutinante','base','path','carpeta','tabla','espectro'])

        if f[0]=="A":
            df = rr.get_df_from_asd(dir+"/"+f)
            # crear dataframe
            dataframe['wavelength'] = df['Wavelength']
            dataframe['reflectance'] = df['reflectance']
            dataframe['pigmento'] = "Bermellon"

            if f[1] == '1':
                dataframe['aglutinante'] = "Copal"
            elif f[1] == '2':
                dataframe['aglutinante'] = "Almáciga"
            elif f[1] == '3':
                dataframe['aglutinante'] = "Colofonia"
            elif f[1] == '4':
                dataframe['aglutinante'] = "Sandaraca"
            elif f[1] == '5':
                dataframe['aglutinante'] = ""

            dataframe['base'] = "Carbonato de calcio"
            dataframe['path'] = dir+"/"+f

            dataframe['carpeta'] = "Tablas1"
            dataframe['tabla'] = "C6"
            dataframe['espectro'] = f

            bermellon.append(dataframe)
        elif f[0]=="B":
            df = rr.get_df_from_asd(dir+"/"+f)
            # crear dataframe
            dataframe['wavelength'] = df['Wavelength']
            dataframe['reflectance'] = df['reflectance']
            dataframe['pigmento'] = "Cochinilla"

            if f[1] == '1':
                dataframe['aglutinante'] = "Copal"
            elif f[1] == '2':
                dataframe['aglutinante'] = "Almáciga"
            elif f[1] == '3':
                dataframe['aglutinante'] = "Colofonia"
            elif f[1] == '4':
                dataframe['aglutinante'] = "Sandaraca"
            elif f[1] == '5':
                dataframe['aglutinante'] = ""

            dataframe['base'] = "Carbonato de calcio"
            dataframe['path'] = dir+"/"+f   
            dataframe['carpeta'] = "Tablas1"
            dataframe['tabla'] = "C6"
            dataframe['espectro'] = f
            cochinilla.append(dataframe)

        elif f[0]=="C":
            df = rr.get_df_from_asd(dir+"/"+f)
            # crear dataframe
            dataframe['wavelength'] = df['Wavelength']
            dataframe['reflectance'] = df['reflectance']
            dataframe['pigmento'] = "Azurita"

            if f[1] == '1':
                dataframe['aglutinante'] = "Copal"
            elif f[1] == '2':
                dataframe['aglutinante'] = "Almáciga"
            elif f[1] == '3':
                dataframe['aglutinante'] = "Colofonia"
            elif f[1] == '4':
                dataframe['aglutinante'] = "Sandaraca"
            elif f[1] == '5':
                dataframe['aglutinante'] = ""

            dataframe['base'] = "Carbonato de calcio"
            dataframe['path'] = dir+"/"+f
            dataframe['carpeta'] = "Tablas1"
            dataframe['tabla'] = "C6"
            dataframe['espectro'] = f
            azurita.append(dataframe)

        elif f[0]=="D":
            df = rr.get_df_from_asd(dir+"/"+f)
            # crear dataframe
            dataframe['wavelength'] = df['Wavelength']
            dataframe['reflectance'] = df['reflectance']
            dataframe['pigmento'] = "Amarillo de plomo estaño"

            if f[1] == '1':
                dataframe['aglutinante'] = "Copal"
            elif f[1] == '2':
                dataframe['aglutinante'] = "Almáciga"
            elif f[1] == '3':
                dataframe['aglutinante'] = "Colofonia"
            elif f[1] == '4':
                dataframe['aglutinante'] = "Sandaraca"
            elif f[1] == '5':
                dataframe['aglutinante'] = ""

            dataframe['base'] = "Carbonato de calcio"
            dataframe['path'] = dir+"/"+f
            dataframe['carpeta'] = "Tablas1"
            dataframe['tabla'] = "C6"
            dataframe['espectro'] = f
            amarillo_plomo_estano.append(dataframe)

        elif f[0]=="E":
            df = rr.get_df_from_asd(dir+"/"+f)
            # crear dataframe
            dataframe['wavelength'] = df['Wavelength']
            dataframe['reflectance'] = df['reflectance']
            dataframe['pigmento'] = "Blanco de plomo"

            if f[1] == '1':
                dataframe['aglutinante'] = "Copal"
            elif f[1] == '2':
                dataframe['aglutinante'] = "Almáciga"
            elif f[1] == '3':
                dataframe['aglutinante'] = "Colofonia"
            elif f[1] == '4':
                dataframe['aglutinante'] = "Sandaraca"
            elif f[1] == '5':
                dataframe['aglutinante'] = ""

            dataframe['base'] = "Carbonato de calcio"
            dataframe['path'] = dir+"/"+f
            dataframe['carpeta'] = "Tablas1"
            dataframe['tabla'] = "C6"
            dataframe['espectro'] = f
            blanco_plomo.append(dataframe)
    
    return [bermellon,cochinilla,azurita,amarillo_plomo_estano,blanco_plomo]

def obtener_carbonato_C6_tablas_2():
    # Info de Tabla 2
    dir = "Espectros_FORS_2/Tablas 2/Tabla_C6"
    archivos=list()
    for f in os.listdir(dir):
        archivos.append(dir+"/"+f)
    archivos.sort()
    
    tmp = archivos[1:6]
    bermellon = obtener_dframes(tmp,"Bermellon")

    tmp = archivos[6:11]
    cochinilla = obtener_dframes(tmp,"Cochinilla")

    tmp = archivos[11:16]
    azurita = obtener_dframes(tmp,"Azurita")

    tmp = archivos[16:21]
    amarillo_plomo_estano = obtener_dframes(tmp,"Amarillo de plomo estaño")

    tmp = archivos[21:26]
    blanco_plomo = obtener_dframes(tmp,"Blanco de plomo")

    return [bermellon,cochinilla,azurita,amarillo_plomo_estano,blanco_plomo]

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
        dataframe['tabla'] = "C6"
        dataframe['espectro'] = l.split("/")[-1]
        dframes.append(dataframe)

    dframes[0]['aglutinante'] = "Copal"
    dframes[1]['aglutinante'] = "Almáciga"
    dframes[2]['aglutinante'] = "Colofonia"
    dframes[3]['aglutinante'] = "Sandaraca"
    dframes[4]['aglutinante'] = ""

    return dframes


def obtener_carbonato_C6():
    tabla1 = obtener_carbonato_C6_tablas_1()
    tabla2 = obtener_carbonato_C6_tablas_2()

    bermellon = tabla1[0]+tabla2[0]
    cochinilla = tabla1[1]+tabla2[1]
    azurita = tabla1[2]+tabla2[2]
    amarillo_plomo_estano = tabla1[3]+tabla2[3]
    blanco_plomo = tabla1[4]+tabla2[4]

    return [bermellon,cochinilla,azurita,amarillo_plomo_estano,blanco_plomo]

def imprimir():
    carbonato_6 = obtener_carbonato_C6()
    for f in carbonato_6:
        for o in f:
            print(o['carpeta'][0]+" "+o['tabla'][0]+" "+o['espectro'][0]+" "+o['pigmento'][0]+" "+o['aglutinante'][0]+" "+o['base'][0])