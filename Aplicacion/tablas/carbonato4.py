import os
import recoverRegister as rr
import pandas as pd
"""
Pigmentos:
Rejalgar (molido en el LDOA) (C4: A1-A5) (Y6:)
Azurita	(C4: B1-B5)
Esmalte (C4: C1-C5)
Lapislázuli	(C4: D1-D5)
Índigo o añil (C4: E1-E5)	
"""

def obtener_carbonato_C4_tablas_1():
    # Info de Tabla 1
    dir = "Espectros_FORS_2/Tablas 1/C4"
    archivos=list()
    for f in os.listdir(dir):
        archivos.append(f)
    archivos.sort()
    
    rejalgar = list()
    azurita = list()
    esmalte = list()
    lapislazuli = list()
    indigo_o_anil = list()
    
    for f in archivos:
        dataframe = pd.DataFrame(columns=['wavelength','reflectance','pigmento','aglutinante','base','path','carpeta','tabla','espectro'])
        if f[0]=="A":
            df = rr.get_df_from_asd(dir+"/"+f)
            # crear dataframe
            dataframe['wavelength'] = df['Wavelength']
            dataframe['reflectance'] = df['reflectance']
            dataframe['pigmento'] = "Rejalgar"
            if f[1] == '1':
                dataframe['aglutinante'] = "Aceite de linaza"
            elif f[1] == '2':
                dataframe['aglutinante'] = "Yema de huevo"
            elif f[1] == '3':
                dataframe['aglutinante'] = "Yema de huevo y aceite de linaza"
            elif f[1] == '4':
                dataframe['aglutinante'] = "Cola de conejo"
            elif f[1] == '5':
                dataframe['aglutinante'] = "Almáciga y aceite de linaza"
            dataframe['base'] = "Carbonato de calcio"
            dataframe['path'] = dir+"/"+f

            dataframe['carpeta'] = "Tablas1"
            dataframe['tabla'] = "C4"
            dataframe['espectro'] = f

            rejalgar.append(dataframe)
        elif f[0]=="B":
            df = rr.get_df_from_asd(dir+"/"+f)
            # crear dataframe
            dataframe['wavelength'] = df['Wavelength']
            dataframe['reflectance'] = df['reflectance']
            dataframe['pigmento'] = "Azurita"

            if f[1] == '1':
                dataframe['aglutinante'] = "Aceite de linaza"
            elif f[1] == '2':
                dataframe['aglutinante'] = "Yema de huevo"
            elif f[1] == '3':
                dataframe['aglutinante'] = "Yema de huevo y aceite de linaza"
            elif f[1] == '4':
                dataframe['aglutinante'] = "Cola de conejo"
            elif f[1] == '5':
                dataframe['aglutinante'] = "Almáciga y aceite de linaza"

            dataframe['base'] = "Carbonato de calcio"
            dataframe['path'] = dir+"/"+f   

            dataframe['carpeta'] = "Tablas1"
            dataframe['tabla'] = "C4"
            dataframe['espectro'] = f

            azurita.append(dataframe)

        elif f[0]=="C":
            df = rr.get_df_from_asd(dir+"/"+f)
            # crear dataframe
            dataframe['wavelength'] = df['Wavelength']
            dataframe['reflectance'] = df['reflectance']
            dataframe['pigmento'] = "Esmalte"

            if f[1] == '1':
                dataframe['aglutinante'] = "Aceite de linaza"
            elif f[1] == '2':
                dataframe['aglutinante'] = "Yema de huevo"
            elif f[1] == '3':
                dataframe['aglutinante'] = "Yema de huevo y aceite de linaza"
            elif f[1] == '4':
                dataframe['aglutinante'] = "Cola de conejo"
            elif f[1] == '5':
                dataframe['aglutinante'] = "Almáciga y aceite de linaza"


            dataframe['base'] = "Carbonato de calcio"
            dataframe['path'] = dir+"/"+f

            dataframe['carpeta'] = "Tablas1"
            dataframe['tabla'] = "C4"
            dataframe['espectro'] = f
            
            esmalte.append(dataframe)
        elif f[0]=="D":
            df = rr.get_df_from_asd(dir+"/"+f)
            # crear dataframe
            dataframe['wavelength'] = df['Wavelength']
            dataframe['reflectance'] = df['reflectance']
            dataframe['pigmento'] = "Lapislázuli"

            if f[1] == '1':
                dataframe['aglutinante'] = "Aceite de linaza"
            elif f[1] == '2':
                dataframe['aglutinante'] = "Yema de huevo"
            elif f[1] == '3':
                dataframe['aglutinante'] = "Yema de huevo y aceite de linaza"
            elif f[1] == '4':
                dataframe['aglutinante'] = "Cola de conejo"
            elif f[1] == '5':
                dataframe['aglutinante'] = "Almáciga y aceite de linaza"


            dataframe['base'] = "Carbonato de calcio"
            dataframe['path'] = dir+"/"+f

            dataframe['carpeta'] = "Tablas1"
            dataframe['tabla'] = "C4"
            dataframe['espectro'] = f

            lapislazuli.append(dataframe)
        elif f[0]=="E":
            df = rr.get_df_from_asd(dir+"/"+f)
            # crear dataframe
            dataframe['wavelength'] = df['Wavelength']
            dataframe['reflectance'] = df['reflectance']
            dataframe['pigmento'] = "Índigo o añil"

            if f[1] == '1':
                dataframe['aglutinante'] = "Aceite de linaza"
            elif f[1] == '2':
                dataframe['aglutinante'] = "Yema de huevo"
            elif f[1] == '3':
                dataframe['aglutinante'] = "Yema de huevo y aceite de linaza"
            elif f[1] == '4':
                dataframe['aglutinante'] = "Cola de conejo"
            elif f[1] == '5':
                dataframe['aglutinante'] = "Almáciga y aceite de linaza"

            dataframe['base'] = "Carbonato de calcio"
            dataframe['path'] = dir+"/"+f

            dataframe['carpeta'] = "Tablas1"
            dataframe['tabla'] = "C4"
            dataframe['espectro'] = f

            indigo_o_anil.append(dataframe)

    return [rejalgar,azurita,esmalte,lapislazuli,indigo_o_anil]

def obtener_carbonato_C4_tablas_2():
    # Info de Tabla 2
    dir = "Espectros_FORS_2/Tablas 2/Tabla_C4"
    archivos=list()
    for f in os.listdir(dir):
        archivos.append(dir+"/"+f)
    archivos.sort()
    #Rejalgar (molido en el LDOA) (C4: A1-A5) (Y6:)
    #Azurita	(C4: B1-B5)
    #Esmalte (C4: C1-C5)
    #Lapislázuli	(C4: D1-D5)
    #Índigo o añil (C4: E1-E5)	
    tmp = archivos[1:6]
    rejalgar = obtener_dframes(tmp,"Rejalgar")

    tmp = archivos[6:11]
    azurita = obtener_dframes(tmp,"Azurita")

    tmp = archivos[11:16]
    esmalte = obtener_dframes(tmp,"Esmalte")

    tmp = archivos[16:21]
    lapislazuli = obtener_dframes(tmp,"Lapislázuli")

    tmp = archivos[21:26]
    indigo_o_anil = obtener_dframes(tmp,"Índigo o añil")

    return [rejalgar,azurita,esmalte,lapislazuli,indigo_o_anil]

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
        dataframe['tabla'] = "C4"
        dataframe['espectro'] = l.split("/")[-1]

        dframes.append(dataframe)

    dframes[0]['aglutinante'] = "Aceite de linaza"
    dframes[1]['aglutinante'] = "Yema de huevo"
    dframes[2]['aglutinante'] = "Yema de huevo y aceite de linaza"
    dframes[3]['aglutinante'] = "Cola de conejo"
    dframes[4]['aglutinante'] = "Almáciga y aceite de linaza"
    return dframes


def obtener_carbonato_C4():
    tabla1 = obtener_carbonato_C4_tablas_1()
    tabla2 = obtener_carbonato_C4_tablas_2()
    # [rejalgar,azurita,esmalte,lapislazuli,indigo_o_anil]
    rejalgar = tabla1[0]+tabla2[0]
    azurita = tabla1[1]+tabla2[1]
    esmalte = tabla1[2]+tabla2[2]
    lapislazuli = tabla1[3]+tabla2[3]
    indigo_o_anil = tabla1[4]+tabla2[4]
    return [rejalgar,azurita,esmalte,lapislazuli,indigo_o_anil]

def imprimir():
    ocre_mina_ingles = obtener_carbonato_C4()
    for f in ocre_mina_ingles:
        for o in f:
            print(o['carpeta'][0]+" "+o['tabla'][0]+" "+o['espectro'][0]+" "+o['pigmento'][0]+" "+o['aglutinante'][0]+" "+o['base'][0])