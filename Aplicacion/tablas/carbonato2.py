import os
import recoverRegister as rr
import pandas as pd
"""
Pigmentos:
Ocre claro (C2: A1-A5)
Sombra tostada de Chipre (C2: B1-B5)
Ocre oscuro Siena (C2: C1-C5)
Siena tostada	(C2: D1-D5)
Betún de Judea (C2: E1-E5)

Carpeta,Tabla,Espectro,Pigmento,Aglutinante,Base de preparación
"""

def obtener_carbonato_C2_tablas_1():
    # Info de Tabla 1
    dir = "Espectros_FORS_2/Tablas 1/C2"
    archivos=list()
    for f in os.listdir(dir):
        archivos.append(f)
    archivos.sort()
    
    ocre_claro = list()
    sombra_tostada_de_Chipre = list()
    ocre_oscuro_Siena = list()
    siena_tostada = list()
    betun_de_Judea = list()

    for f in archivos:
        dataframe = pd.DataFrame(columns=['wavelength','reflectance','pigmento','aglutinante','base','path','carpeta','tabla','espectro'])
        if f[0]=="A":
            df = rr.get_df_from_asd(dir+"/"+f)
            # crear dataframe
            dataframe['wavelength'] = df['Wavelength']
            dataframe['reflectance'] = df['reflectance']
            dataframe['pigmento'] = "Ocre claro"
            if f[1] == '1':
                dataframe['aglutinante'] = "Aceite de linaza"
            elif f[1] == '2':
                dataframe['aglutinante'] = "Aceite de nuez"
            elif f[1] == '3':
                dataframe['aglutinante'] = "Yema de huevo"
            elif f[1] == '4':
                dataframe['aglutinante'] = "Cola de conejo"
            elif f[1] == '5':
                dataframe['aglutinante'] = "Almaciga y aceite de linaza"
            dataframe['base'] = "Carbonato de calcio"
            dataframe['path'] = dir+"/"+f

            dataframe['carpeta'] = "Tablas1"
            dataframe['tabla'] = "C2"
            dataframe['espectro'] = f

            ocre_claro.append(dataframe)
        elif f[0]=="B":
            df = rr.get_df_from_asd(dir+"/"+f)
            # crear dataframe
            dataframe['wavelength'] = df['Wavelength']
            dataframe['reflectance'] = df['reflectance']
            dataframe['pigmento'] = "Sombra tostada de Chipre"

            if f[1] == '1':
                dataframe['aglutinante'] = "Aceite de linaza"
            elif f[1] == '2':
                dataframe['aglutinante'] = "Aceite de nuez"
            elif f[1] == '3':
                dataframe['aglutinante'] = "Yema de huevo"
            elif f[1] == '4':
                dataframe['aglutinante'] = "Cola de conejo"
            elif f[1] == '5':
                dataframe['aglutinante'] = "Almaciga y aceite de linaza"

            dataframe['base'] = "Carbonato de calcio"
            dataframe['path'] = dir+"/"+f   

            dataframe['carpeta'] = "Tablas1"
            dataframe['tabla'] = "C2"
            dataframe['espectro'] = f

            sombra_tostada_de_Chipre.append(dataframe)

        elif f[0]=="C":
            df = rr.get_df_from_asd(dir+"/"+f)
            # crear dataframe
            dataframe['wavelength'] = df['Wavelength']
            dataframe['reflectance'] = df['reflectance']
            dataframe['pigmento'] = "Ocre oscuro Siena"
            if f[1] == '1':
                dataframe['aglutinante'] = "Aceite de linaza"
            elif f[1] == '2':
                dataframe['aglutinante'] = "Aceite de nuez"
            elif f[1] == '3':
                dataframe['aglutinante'] = "Yema de huevo"
            elif f[1] == '4':
                dataframe['aglutinante'] = "Cola de conejo"
            elif f[1] == '5':
                dataframe['aglutinante'] = "Almaciga y aceite de linaza"
            dataframe['base'] = "Carbonato de calcio"
            dataframe['path'] = dir+"/"+f

            dataframe['carpeta'] = "Tablas1"
            dataframe['tabla'] = "C2"
            dataframe['espectro'] = f
            ocre_oscuro_Siena.append(dataframe)
        elif f[0]=="D":
            df = rr.get_df_from_asd(dir+"/"+f)
            # crear dataframe
            dataframe['wavelength'] = df['Wavelength']
            dataframe['reflectance'] = df['reflectance']
            dataframe['pigmento'] = "Siena tostada"
            if f[1] == '1':
                dataframe['aglutinante'] = "Aceite de linaza"
            elif f[1] == '2':
                dataframe['aglutinante'] = "Aceite de nuez"
            elif f[1] == '3':
                dataframe['aglutinante'] = "Yema de huevo"
            elif f[1] == '4':
                dataframe['aglutinante'] = "Cola de conejo"
            elif f[1] == '5':
                dataframe['aglutinante'] = "Almaciga y aceite de linaza"
            dataframe['base'] = "Carbonato de calcio"
            dataframe['path'] = dir+"/"+f

            dataframe['carpeta'] = "Tablas1"
            dataframe['tabla'] = "C2"
            dataframe['espectro'] = f
            siena_tostada.append(dataframe)
        elif f[0]=="E":
            df = rr.get_df_from_asd(dir+"/"+f)
            # crear dataframe
            dataframe['wavelength'] = df['Wavelength']
            dataframe['reflectance'] = df['reflectance']
            dataframe['pigmento'] = "Betun de Judea"
            if f[1] == '1':
                dataframe['aglutinante'] = "Aceite de linaza"
            elif f[1] == '2':
                dataframe['aglutinante'] = "Aceite de nuez"
            elif f[1] == '3':
                dataframe['aglutinante'] = "Yema de huevo"
            elif f[1] == '4':
                dataframe['aglutinante'] = "Cola de conejo"
            elif f[1] == '5':
                dataframe['aglutinante'] = "Almaciga y aceite de linaza"
            dataframe['base'] = "Carbonato de calcio"
            dataframe['path'] = dir+"/"+f

            dataframe['carpeta'] = "Tablas1"
            dataframe['tabla'] = "C2"
            dataframe['espectro'] = f
            betun_de_Judea.append(dataframe)
    
    return [ocre_claro,sombra_tostada_de_Chipre,ocre_oscuro_Siena,siena_tostada,betun_de_Judea]

def obtener_carbonato_C2_tablas_2():
    # Info de Tabla 2
    dir = "Espectros_FORS_2/Tablas 2/Tabla_C2"
    archivos=list()
    for f in os.listdir(dir):
        archivos.append(dir+"/"+f)
    archivos.sort()
    
    tmp = archivos[1:6]
    ocre_claro= obtener_dframes(tmp,"Ocre claro")

    tmp = archivos[6:11]
    sombra_tostada_de_Chipre = obtener_dframes(tmp,"Sombra tostada de Chipre")

    tmp = archivos[11:16]
    ocre_oscuro_Siena = obtener_dframes(tmp,"Ocre oscuro Siena")

    tmp = archivos[16:21]
    siena_tostada = obtener_dframes(tmp,"Siena tostada")

    tmp = archivos[21:26]
    betun_de_Judea = obtener_dframes(tmp,"Betún de Judea")

    return [ocre_claro,sombra_tostada_de_Chipre,ocre_oscuro_Siena,siena_tostada,betun_de_Judea]

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
    dframes[1]['aglutinante'] = "Aceite de nuez"
    dframes[2]['aglutinante'] = "Yema de huevo"
    dframes[3]['aglutinante'] = "Cola de conejo"
    dframes[4]['aglutinante'] = "Almaciga y aceite de linaza"
    return dframes


def obtener_carbonato_C2():
    tabla1 = obtener_carbonato_C2_tablas_1()
    tabla2 = obtener_carbonato_C2_tablas_2()
    ocre_claro = tabla1[0]+tabla2[0]
    sombra_tostada_de_Chipre = tabla1[1]+tabla2[1]
    ocre_oscuro_Siena = tabla1[2]+tabla2[2]
    siena_tostada = tabla1[3]+tabla2[3]
    betun_de_Judea = tabla1[4]+tabla2[4]
    return [ocre_claro,sombra_tostada_de_Chipre,ocre_oscuro_Siena,siena_tostada,betun_de_Judea]

def contenar_c1():
    ejemplares_c2 = obtener_carbonato_C2()
    ocre_claro = ejemplares_c2[0]
    sombra_tostada_de_Chipre = ejemplares_c2[1]
    ocre_oscuro_Siena = ejemplares_c2[2]
    siena_tostada = ejemplares_c2[3]
    betun_de_Judea = ejemplares_c2[4]
    return ocre_claro+sombra_tostada_de_Chipre+ocre_oscuro_Siena+siena_tostada+betun_de_Judea

def imprimir():
    ocre_mina_ingles = obtener_carbonato_C2()
    for f in ocre_mina_ingles:
        for o in f:
            print(o['carpeta'][0]+" "+o['tabla'][0]+" "+o['espectro'][0]+" "+o['pigmento'][0]+" "+o['aglutinante'][0]+" "+o['base'][0])