import os
import recoverRegister as rr
import pandas as pd
"""
Pigmentos:
(Tabla 1)
Acetato básico de cobre. Verdigris	(Y5: A1-A5)
Malaquita africana (Y5: B1:B5)
Tierra verde de Verona (Y5: C1:C5)
Negro de huesos (Y5: D1-D5)
Negro de humo(Y5: E1-E5)	

Carpeta,Tabla,Espectro,Pigmento,Aglutinante,Base de preparación
"""

def obtener_yeso_Y5_tablas_1():
    # Info de Tabla 1
    dir = "Espectros_FORS_2/Tablas 1/Y5"
    archivos=list()
    for f in os.listdir(dir):
        archivos.append(f)
    archivos.sort()
    
    acetato_cobre = list()
    malaquita_africana = list()
    tierra_verde_verona = list()
    negro_huesos = list()
    negro_humo = list()
    
    for f in archivos:
        dataframe = pd.DataFrame(columns=['wavelength','reflectance','pigmento','aglutinante','base','path','carpeta','tabla','espectro'])

        if f[0]=="A":
            df = rr.get_df_from_asd(dir+"/"+f)
            # crear dataframe
            dataframe['wavelength'] = df['Wavelength']
            dataframe['reflectance'] = df['reflectance']
            dataframe['pigmento'] = "Acetato basico de cobre"

            if f[1] == '1':
                dataframe['aglutinante'] = "Aceite de linaza"
            elif f[1] == '2':
                dataframe['aglutinante'] = "Aceite de nuez"
            elif f[1] == '3':
                dataframe['aglutinante'] = "Yema de huevo y aceite de linaza"
            elif f[1] == '4':
                dataframe['aglutinante'] = "Cola de conejo"
            elif f[1] == '5':
                dataframe['aglutinante'] = "Almaciga y aceite de linaza"

            dataframe['base'] = "Yeso"
            dataframe['path'] = dir+"/"+f

            dataframe['carpeta'] = "Tablas1"
            dataframe['tabla'] = "Y5"
            dataframe['espectro'] = f
            acetato_cobre.append(dataframe)

        elif f[0]=="B":
            df = rr.get_df_from_asd(dir+"/"+f)
            # crear dataframe
            dataframe['wavelength'] = df['Wavelength']
            dataframe['reflectance'] = df['reflectance']
            dataframe['pigmento'] = "Malaquita africana"

            if f[1] == '1':
                dataframe['aglutinante'] = "Aceite de linaza"
            elif f[1] == '2':
                dataframe['aglutinante'] = "Aceite de nuez"
            elif f[1] == '3':
                dataframe['aglutinante'] = "Yema de huevo y aceite de linaza"
            elif f[1] == '4':
                dataframe['aglutinante'] = "Cola de conejo"
            elif f[1] == '5':
                dataframe['aglutinante'] = "Almaciga y aceite de linaza"

            dataframe['base'] = "Yeso"
            dataframe['path'] = dir+"/"+f   
            dataframe['carpeta'] = "Tablas1"
            dataframe['tabla'] = "Y5"
            dataframe['espectro'] = f
            malaquita_africana.append(dataframe)

        elif f[0]=="C":
            df = rr.get_df_from_asd(dir+"/"+f)
            # crear dataframe
            dataframe['wavelength'] = df['Wavelength']
            dataframe['reflectance'] = df['reflectance']
            dataframe['pigmento'] = "Tierra verde de Verona"

            if f[1] == '1':
                dataframe['aglutinante'] = "Aceite de linaza"
            elif f[1] == '2':
                dataframe['aglutinante'] = "Aceite de nuez"
            elif f[1] == '3':
                dataframe['aglutinante'] = "Yema de huevo y aceite de linaza"
            elif f[1] == '4':
                dataframe['aglutinante'] = "Cola de conejo"
            elif f[1] == '5':
                dataframe['aglutinante'] = "Almaciga y aceite de linaza"

            dataframe['base'] = "Yeso"
            dataframe['path'] = dir+"/"+f
            dataframe['carpeta'] = "Tablas1"
            dataframe['tabla'] = "Y5"
            dataframe['espectro'] = f
            tierra_verde_verona.append(dataframe)

        elif f[0]=="D":
            df = rr.get_df_from_asd(dir+"/"+f)
            # crear dataframe
            dataframe['wavelength'] = df['Wavelength']
            dataframe['reflectance'] = df['reflectance']
            dataframe['pigmento'] = "Negro de huesos"

            if f[1] == '1':
                dataframe['aglutinante'] = "Aceite de linaza"
            elif f[1] == '2':
                dataframe['aglutinante'] = "Aceite de nuez"
            elif f[1] == '3':
                dataframe['aglutinante'] = "Yema de huevo y aceite de linaza"
            elif f[1] == '4':
                dataframe['aglutinante'] = "Cola de conejo"
            elif f[1] == '5':
                dataframe['aglutinante'] = "Almaciga y aceite de linaza"

            dataframe['base'] = "Yeso"
            dataframe['path'] = dir+"/"+f
            dataframe['carpeta'] = "Tablas1"
            dataframe['tabla'] = "Y5"
            dataframe['espectro'] = f
            negro_huesos.append(dataframe)

        elif f[0]=="E":
            df = rr.get_df_from_asd(dir+"/"+f)
            # crear dataframe
            dataframe['wavelength'] = df['Wavelength']
            dataframe['reflectance'] = df['reflectance']
            dataframe['pigmento'] = "Negro de humo"

            if f[1] == '1':
                dataframe['aglutinante'] = "Aceite de linaza"
            elif f[1] == '2':
                dataframe['aglutinante'] = "Aceite de nuez"
            elif f[1] == '3':
                dataframe['aglutinante'] = "Yema de huevo y aceite de linaza"
            elif f[1] == '4':
                dataframe['aglutinante'] = "Cola de conejo"
            elif f[1] == '5':
                dataframe['aglutinante'] = "Almaciga y aceite de linaza"

            dataframe['base'] = "Yeso"
            dataframe['path'] = dir+"/"+f
            dataframe['carpeta'] = "Tablas1"
            dataframe['tabla'] = "Y5"
            dataframe['espectro'] = f
            negro_humo.append(dataframe)
    
    return [acetato_cobre,malaquita_africana,tierra_verde_verona,negro_huesos,negro_humo]

def obtener_yeso_Y5_tablas_2():
    # Info de Tabla 2
    dir = "Espectros_FORS_2/Tablas 2/Tabla_Y5"
    archivos=list()
    for f in os.listdir(dir):
        archivos.append(dir+"/"+f)
    archivos.sort()
    
    tmp = archivos[0:5]
    acetato_cobre = obtener_dframes(tmp,"Acetato basico de cobre")

    tmp = archivos[5:10]
    malaquita_africana = obtener_dframes(tmp,"Malaquita africana")

    tmp = archivos[10:15]
    tierra_verde_verona = obtener_dframes(tmp,"Tierra verde de Verona")

    tmp = archivos[15:20]
    negro_huesos = obtener_dframes(tmp,"Negro de huesos")

    tmp = archivos[20:25]
    negro_humo = obtener_dframes(tmp,"Negro de humo")

    return [acetato_cobre,malaquita_africana,tierra_verde_verona,negro_huesos,negro_humo]

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
        dataframe['base'] = "Yeso"
        dataframe['carpeta'] = "Tablas2"
        dataframe['tabla'] = "Y5"
        dataframe['espectro'] = l.split("/")[-1]
        dframes.append(dataframe)

    dframes[0]['aglutinante'] = "Aceite de linaza"
    dframes[1]['aglutinante'] = "Aceite de nuez"
    dframes[2]['aglutinante'] = "Yema de huevo y aceite de linaza"
    dframes[3]['aglutinante'] = "Cola de conejo"
    dframes[4]['aglutinante'] = "Almaciga y aceite de linaza"
    return dframes


def obtener_yeso_Y5():
    tabla1 = obtener_yeso_Y5_tablas_1()
    tabla2 = obtener_yeso_Y5_tablas_2()

    acetato_cobre = tabla1[0]+tabla2[0]
    malaquita_africana = tabla1[1]+tabla2[1]
    tierra_verde_verona = tabla1[2]+tabla2[2]
    negro_huesos = tabla1[3]+tabla2[3]
    negro_humo = tabla1[4]+tabla2[4]

    return [acetato_cobre,malaquita_africana,tierra_verde_verona,negro_huesos,negro_humo]

def imprimir():
    yeso5 = obtener_yeso_Y5()
    for f in yeso5:
        for o in f:
            print(o['carpeta'][0]+" "+o['tabla'][0]+" "+o['espectro'][0]+" "+o['pigmento'][0]+" "+o['aglutinante'][0]+" "+o['base'][0])
