import os

from matplotlib.pylab import f
import recoverRegister as rr
import pandas as pd
"""
Pigmentos:
(Tabla 1)
Ocre de mina ingles (marca KremerR, n. 40191) (C1: A1-A5) (C7:A1) (Y1:A1-A5) (Y4:A1)
Oropimente (molido en el LDOA)	(C1: B1-B5) (Y1:B1-B5)
Amarillo de plomo estaño (tipo II, marca KremerR, n. 10120) (C1: C1-C5) (Y1:C1-C5)
Ancorca (marca SennelierR, Reseda luteola, sp.) (C1:D1-D5)
Ancorca o gualda (marca ZecchiR, Reseda luteola, sp.) (C1:E1-E5) (Y1:E1-E5)

Carpeta,Tabla,Espectro,Pigmento,Aglutinante,Base de preparación
"""

def obtener_carbonato_C1_tablas_1():
    # Info de Tabla 1
    dir = "Espectros_FORS_2/Tablas 1/C1"
    archivos=list()
    for f in os.listdir(dir):
        archivos.append(f)
    archivos.sort()
    
    ocre_mina_ingles = list()
    oropimente = list()
    amarillo_plomo_estano = list()
    ancorca_sennelier = list()
    ancorca_zecchi = list()
    
    for f in archivos:
        dataframe = pd.DataFrame(columns=['wavelength','reflectance','pigmento','aglutinante','base','path','carpeta','tabla','espectro'])

        if f[0]=="A":
            df = rr.get_df_from_asd(dir+"/"+f)
            # crear dataframe
            dataframe['wavelength'] = df['Wavelength']
            dataframe['reflectance'] = df['reflectance']
            dataframe['pigmento'] = "Ocre de mina ingles"
            if f[1] == '1':
                dataframe['aglutinante'] = "Aceite de linaza"
            elif f[1] == '2':
                dataframe['aglutinante'] = "Yema de huevo"
            elif f[1] == '3':
                dataframe['aglutinante'] = "Yema de huevo y aceite de linaza"
            elif f[1] == '4':
                dataframe['aglutinante'] = "Cola de conejo"
            elif f[1] == '5':
                dataframe['aglutinante'] = "Almaciga y aceite de linaza"
            dataframe['base'] = "Carbonato de calcio"
            dataframe['path'] = dir+"/"+f

            dataframe['carpeta'] = "Tablas1"
            dataframe['tabla'] = "C1"
            dataframe['espectro'] = f

            ocre_mina_ingles.append(dataframe)
        elif f[0]=="B":
            df = rr.get_df_from_asd(dir+"/"+f)
            # crear dataframe
            dataframe['wavelength'] = df['Wavelength']
            dataframe['reflectance'] = df['reflectance']
            dataframe['pigmento'] = "Orpimente"

            if f[1] == '1':
                dataframe['aglutinante'] = "Aceite de linaza"
            elif f[1] == '2':
                dataframe['aglutinante'] = "Yema de huevo"
            elif f[1] == '3':
                dataframe['aglutinante'] = "Yema de huevo y aceite de linaza"
            elif f[1] == '4':
                dataframe['aglutinante'] = "Cola de conejo"
            elif f[1] == '5':
                dataframe['aglutinante'] = "Almaciga y aceite de linaza"

            dataframe['base'] = "Carbonato de calcio"
            dataframe['path'] = dir+"/"+f   
            dataframe['carpeta'] = "Tablas1"
            dataframe['tabla'] = "C1"
            dataframe['espectro'] = f
            oropimente.append(dataframe)

        elif f[0]=="C":
            df = rr.get_df_from_asd(dir+"/"+f)
            # crear dataframe
            dataframe['wavelength'] = df['Wavelength']
            dataframe['reflectance'] = df['reflectance']
            dataframe['pigmento'] = "Amarillo de plomo estaño"
            if f[1] == '1':
                dataframe['aglutinante'] = "Aceite de linaza"
            elif f[1] == '2':
                dataframe['aglutinante'] = "Yema de huevo"
            elif f[1] == '3':
                dataframe['aglutinante'] = "Yema de huevo y aceite de linaza"
            elif f[1] == '4':
                dataframe['aglutinante'] = "Cola de conejo"
            elif f[1] == '5':
                dataframe['aglutinante'] = "Almaciga y aceite de linaza"
            dataframe['base'] = "Carbonato de calcio"
            dataframe['path'] = dir+"/"+f
            dataframe['carpeta'] = "Tablas1"
            dataframe['tabla'] = "C1"
            dataframe['espectro'] = f
            amarillo_plomo_estano.append(dataframe)
        elif f[0]=="D":
            df = rr.get_df_from_asd(dir+"/"+f)
            # crear dataframe
            dataframe['wavelength'] = df['Wavelength']
            dataframe['reflectance'] = df['reflectance']
            dataframe['pigmento'] = "Ancorca Sennelier"
            if f[1] == '1':
                dataframe['aglutinante'] = "Aceite de linaza"
            elif f[1] == '2':
                dataframe['aglutinante'] = "Yema de huevo"
            elif f[1] == '3':
                dataframe['aglutinante'] = "Yema de huevo y aceite de linaza"
            elif f[1] == '4':
                dataframe['aglutinante'] = "Cola de conejo"
            elif f[1] == '5':
                dataframe['aglutinante'] = "Almaciga y aceite de linaza"
            dataframe['base'] = "Carbonato de calcio"
            dataframe['path'] = dir+"/"+f
            dataframe['carpeta'] = "Tablas1"
            dataframe['tabla'] = "C1"
            dataframe['espectro'] = f
            ancorca_sennelier.append(dataframe)
        elif f[0]=="E":
            df = rr.get_df_from_asd(dir+"/"+f)
            # crear dataframe
            dataframe['wavelength'] = df['Wavelength']
            dataframe['reflectance'] = df['reflectance']
            dataframe['pigmento'] = "Ancorca o gualda Zecchi"
            if f[1] == '1':
                dataframe['aglutinante'] = "Aceite de linaza"
            elif f[1] == '2':
                dataframe['aglutinante'] = "Yema de huevo"
            elif f[1] == '3':
                dataframe['aglutinante'] = "Yema de huevo y aceite de linaza"
            elif f[1] == '4':
                dataframe['aglutinante'] = "Cola de conejo"
            elif f[1] == '5':
                dataframe['aglutinante'] = "Almaciga y aceite de linaza"
            dataframe['base'] = "Carbonato de calcio"
            dataframe['path'] = dir+"/"+f
            dataframe['carpeta'] = "Tablas1"
            dataframe['tabla'] = "C1"
            dataframe['espectro'] = f
            ancorca_zecchi.append(dataframe)
    
    return [ocre_mina_ingles,oropimente,amarillo_plomo_estano,ancorca_sennelier,ancorca_zecchi]

def obtener_carbonato_C1_tablas_2():
    # Info de Tabla 2
    dir = "Espectros_FORS_2/Tablas 2/Tabla_C1"
    archivos=list()
    for f in os.listdir(dir):
        archivos.append(dir+"/"+f)
    archivos.sort()
    
    tmp = archivos[0:5]
    ocre_mina_ingles = obtener_dframes(tmp,"Ocre de mina ingles")

    tmp = archivos[5:10]
    oropimente = obtener_dframes(tmp,"Oropimente")

    tmp = archivos[10:15]
    amarillo_plomo_estano = obtener_dframes(tmp,"Amarillo de plomo estaño")

    tmp = archivos[15:20]
    ancorca_sennelier = obtener_dframes(tmp,"Ancorca Sennelier")

    tmp = archivos[20:25]
    ancorca_zecchi = obtener_dframes(tmp,"Ancorca o gualda Zecchi")
    return [ocre_mina_ingles,oropimente,amarillo_plomo_estano,ancorca_sennelier,ancorca_zecchi]

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
        dataframe['tabla'] = "C1"
        dataframe['espectro'] = l.split("/")[-1]
        dframes.append(dataframe)

    dframes[0]['aglutinante'] = "Aceite de linaza"
    dframes[1]['aglutinante'] = "Yema de huevo"
    dframes[2]['aglutinante'] = "Yema de huevo y aceite de linaza"
    dframes[3]['aglutinante'] = "Cola de conejo"
    dframes[4]['aglutinante'] = "Almaciga y aceite de linaza"

    return dframes


def obtener_carbonato_C1():
    tabla1 = obtener_carbonato_C1_tablas_1()
    tabla2 = obtener_carbonato_C1_tablas_2()

    ocre_mina_ingles = tabla1[0]+tabla2[0]
    oropimente = tabla1[1]+tabla2[1]
    amarillo_plomo_estano = tabla1[2]+tabla2[2]
    ancorca_sennelier = tabla1[3]+tabla2[3]
    ancorca_zecchi = tabla1[4]+tabla2[4]
    return [ocre_mina_ingles,oropimente,amarillo_plomo_estano,ancorca_sennelier,ancorca_zecchi]

def contenar_c1():
    ejemplares_c1 = obtener_carbonato_C1()
    ocre_mina_ingles = ejemplares_c1[0]
    oropimente = ejemplares_c1[1]
    amarillo_plomo_estano = ejemplares_c1[2]
    ancorca_sennelier = ejemplares_c1[3]
    ancorca_zecchi = ejemplares_c1[4]
    return ocre_mina_ingles+oropimente+amarillo_plomo_estano+ancorca_sennelier+ancorca_zecchi

def imprimir():
    ocre_mina_ingles = obtener_carbonato_C1()
    for f in ocre_mina_ingles:
        for o in f:
            print(o['carpeta'][0]+" "+o['tabla'][0]+" "+o['espectro'][0]+" "+o['pigmento'][0]+" "+o['aglutinante'][0]+" "+o['base'][0])