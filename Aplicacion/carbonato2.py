import os
import pre_process as pp
import recoverRegister as rr
import pandas as pd
"""
Pigmentos:
Ocre claro (C2: A1-A5)
Sombra tostada de Chipre (C2: B1-B5)
Ocre oscuro Siena (C2: C1-C5)
Siena tostada	(C2: D1-D5)
Betún de Judea (C2: E1-E5)
"""

def obtener_carbonato_C2_tablas_1():
    dataframe = pd.DataFrame(columns=['wavelength','reflectance','pigmento','aglutinante','base','path'])
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
        if f[0]=="A":
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

            ocre_claro.append(dataframe)
        elif f[0]=="B":
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
            sombra_tostada_de_Chipre.append(dataframe)

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
                dataframe['aglutinante'] = "Yema de huevo"
            elif f[1] == '4':
                dataframe['aglutinante'] = "Cola de conejo"
            elif f[1] == '5':
                dataframe['aglutinante'] = "Almáciga y aceite de linaza"
            dataframe['base'] = "Carbonato de calcio"
            dataframe['path'] = dir+"/"+f
            ocre_oscuro_Siena.append(dataframe)
        elif f[0]=="D":
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
            siena_tostada.append(dataframe)
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
            betun_de_Judea.append(dataframe)
    
    return [ocre_claro,sombra_tostada_de_Chipre,ocre_oscuro_Siena,siena_tostada,betun_de_Judea]

def obtener_carbonato_C2_tablas_2():
    # Info de Tabla 2
    dir = "Espectros_FORS_2/Tablas 2/Tabla_C2"
    archivos=list()
    for f in os.listdir(dir):
        archivos.append(dir+"/"+f)
    archivos.sort()
    
    tmp = archivos[0:5]
    ocre_claro= obtener_dframes(tmp)

    tmp = archivos[5:10]
    sombra_tostada_de_Chipre = obtener_dframes(tmp)

    tmp = archivos[10:15]
    ocre_oscuro_Siena = obtener_dframes(tmp)

    tmp = archivos[15:20]
    siena_tostada = obtener_dframes(tmp)

    tmp = archivos[20:25]
    betun_de_Judea = obtener_dframes(tmp)

    return [ocre_claro,sombra_tostada_de_Chipre,ocre_oscuro_Siena,siena_tostada,betun_de_Judea]

def obtener_dframes(lista):
    dataframe = pd.DataFrame(columns=['wavelength','reflectance','pigmento','aglutinante','base','path'])
    dframes = list()
    j = 0
    for l in lista:
        df = rr.create_df_from_txt(l)
        # crear dataframe
        dataframe['wavelength'] = df['Wavelength']
        dataframe['reflectance'] = df['reflectance']
        dataframe['pigmento'] = "Ocre de mina inglés"
        if j in range(0,5):
            dataframe['aglutinante'] = "Aceite de linaza"
        elif j in range(5,10):
            dataframe['aglutinante'] = "Aceite de nuez"
        elif j in range(10,15):
            dataframe['aglutinante'] = "Yema de huevo"
        elif j in range(15,20):
            dataframe['aglutinante'] = "Cola de conejo"
        elif j in range(20,25):
            dataframe['aglutinante'] = "Almáciga y aceite de linaza"
        
        dataframe['path'] = l
        dataframe['base'] = "Carbonato de calcio"
        dframes.append(dataframe)
        j+=1
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
