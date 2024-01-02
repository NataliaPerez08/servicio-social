import os
import recoverRegister as rr
import pandas as pd
"""
Pigmentos:
Resinato de	cobre, Blanco de plomo, ocre y negro de vid (Y7:A1)
Amarillo de plomo (estaño. Tipo I) (Y7: A2)
Amarillo de plomo (estaño. Tipo II) (Y7: A3)
Ancorca. Sennelier (Y7: A4)
Ancorca. Zeechi (Y7: A5)

Tierra de Sombra (Y7:B1)
Sombra tostada de Chipre (Y7: B2)
Siena (Y7:B3)
Siena tostada (Y7:B4)
Espalto (Y7:B5)

Cinabrio (Y7: C1)
Almagre	(Y7: C2)
Azarcón o minio (Y7: C3)
Cochinilla. Tlapanocheztli (Y7: C4)
Alizarina. Zeechi	(Y7: C5)

Laca rubia.Zeechi  (Y7:D1)
Azurita. Zeechi	(Y7:D2)
Esmalte	(Y7:D3)
Lapislázuli	(Y7:D4)
Índigo (Y7:D5)

Resinato de	cobre, Blanco de plomo, ocre y negro de vid (Y7:A1)
Malaquita africana	(Y7:E2)
Tierra verde de	bohemia	(Y7:E3)
Negro de huesos (Y7:E4)
Negro de humo. Kremer (Y7:E5)


Carpeta,Tabla,Espectro,Pigmento,Aglutinante,Base de preparación
"""

def obtener_yeso_Y7_tablas_2():
    # Info de Tabla 2
    dir = "Espectros_FORS_2/Tablas 2/Tabla_Y7"
    archivos=list()
    for f in os.listdir(dir):
        archivos.append(dir+"/"+f)
    archivos.sort()
    
    df_list = list()

    # A1-A5
    tmp = archivos[0]
    df = crear_dataframe("Resinato de cobre",tmp)
    df_list.append(df)

    tmp = archivos[1]
    df = crear_dataframe("Amarillo de plomo (estaño. Tipo I)",tmp)
    df_list.append(df)

    tmp = archivos[2]
    df = crear_dataframe("Amarillo de plomo (estaño. Tipo II)",tmp)
    df_list.append(df)

    tmp = archivos[3]
    df = crear_dataframe("Ancorca. Sennelier",tmp)
    df_list.append(df)

    tmp = archivos[4]
    df = crear_dataframe("Ancorca. Zeechi",tmp)
    df_list.append(df)

    # B1-B5
    tmp = archivos[5]
    df = crear_dataframe("Tierra de Sombra",tmp)
    df_list.append(df)

    tmp = archivos[6]
    df = crear_dataframe("Sombra tostada de Chipre",tmp)
    df_list.append(df)

    tmp = archivos[7]
    df = crear_dataframe("Siena",tmp)
    df_list.append(df)

    tmp = archivos[8]
    df = crear_dataframe("Siena tostada",tmp)
    df_list.append(df)

    tmp = archivos[9]
    df = crear_dataframe("Espalto",tmp)
    df_list.append(df)

    # C1-C5
    tmp = archivos[10]
    df = crear_dataframe("Cinabrio",tmp)
    df_list.append(df)

    tmp = archivos[11]
    df = crear_dataframe("Almagre",tmp)
    df_list.append(df)

    tmp = archivos[12]
    df = crear_dataframe("Azarcón o minio",tmp)
    df_list.append(df)

    tmp = archivos[13]
    df = crear_dataframe("Cochinilla. Tlapanocheztli",tmp)
    df_list.append(df)

    tmp = archivos[14]
    df = crear_dataframe("Alizarina",tmp)
    df_list.append(df)

    # D1-D5
    tmp = archivos[15]
    df = crear_dataframe("Laca rubia",tmp)
    df_list.append(df)

    tmp = archivos[16]
    df = crear_dataframe("Azurita",tmp)
    df_list.append(df)

    tmp = archivos[17]
    df = crear_dataframe("Esmalte",tmp)
    df_list.append(df)

    tmp = archivos[18]
    df = crear_dataframe("Lapislazuli",tmp)
    df_list.append(df)

    tmp = archivos[19]
    df = crear_dataframe("Indigo",tmp)
    df_list.append(df)

    # E1-E5
    tmp = archivos[20]
    df = crear_dataframe("Resinato de cobre",tmp)
    df_list.append(df)

    tmp = archivos[21]
    df = crear_dataframe("Malaquita africana",tmp)
    df_list.append(df)

    tmp = archivos[22]
    df = crear_dataframe("Tierra verde de bohemia",tmp)
    df_list.append(df)

    tmp = archivos[23]
    df = crear_dataframe("Negro de huesos",tmp)
    df_list.append(df)

    tmp = archivos[24]
    df = crear_dataframe("Negro de humo",tmp)
    df_list.append(df)

    return df_list


def obtener_yeso_Y7_tablas_1():
    # Info de Tabla 1
    dir = "Espectros_FORS_2/Tablas 1/Y1"
    archivos=list()
    for f in os.listdir(dir):
        archivos.append(f)
    archivos.sort()
    
    df_list = list()
    
    for f in archivos:
        dataframe = pd.DataFrame(columns=['wavelength','reflectance','pigmento','aglutinante','base','path','carpeta','tabla','espectro'])

        if f[0]=="A":
            df = rr.get_df_from_asd(dir+"/"+f)
            # crear dataframe
            dataframe['wavelength'] = df['Wavelength']
            dataframe['reflectance'] = df['reflectance']

            if f[1] == '1':
                dataframe['pigmento'] = "Resinato de cobre"
                dataframe['aglutinante'] = ""
            elif f[1] == '2':
                dataframe['pigmento'] = "Amarillo de plomo (estaño. Tipo I)"
                dataframe['aglutinante'] = "Aceite de linaza"
            elif f[1] == '3':
                dataframe['pigmento'] = "Amarillo de plomo (estaño. Tipo II)"
                dataframe['aglutinante'] = ""
            elif f[1] == '4':
                dataframe['pigmento'] = "Ancorca. Sennelier"
                dataframe['aglutinante'] = "Aceite de linaza"
            elif f[1] == '5':
                dataframe['pigmento'] = "Ancorca. Zeechi"
                dataframe['aglutinante'] = "Aceite de linaza"

            dataframe['base'] = "Yeso"
            dataframe['path'] = dir+"/"+f

            dataframe['carpeta'] = "Tablas1"
            dataframe['tabla'] = "Y7"
            dataframe['espectro'] = f

            df_list.append(dataframe)

        elif f[0]=="B":
            df = rr.get_df_from_asd(dir+"/"+f)
            # crear dataframe
            dataframe['wavelength'] = df['Wavelength']
            dataframe['reflectance'] = df['reflectance']

            if f[1] == '1':
                dataframe['pigmento'] = "Tierra de Sombra"
                dataframe['aglutinante'] = ""
            elif f[1] == '2':
                dataframe['pigmento'] = "Sombra tostada de Chipre"
                dataframe['aglutinante'] = "Aceite de linaza"
            elif f[1] == '3':
                dataframe['pigmento'] = "Siena"
                dataframe['aglutinante'] = "Aceite de linaza"
            elif f[1] == '4':
                dataframe['pigmento'] = "Siena tostada"
                dataframe['aglutinante'] = "Aceite de linaza"
            elif f[1] == '5':
                dataframe['pigmento'] = "Espalto"
                dataframe['aglutinante'] = ""

            dataframe['base'] = "Yeso"
            dataframe['path'] = dir+"/"+f

            dataframe['carpeta'] = "Tablas1"
            dataframe['tabla'] = "Y7"
            dataframe['espectro'] = f
            df_list.append(dataframe)

        elif f[0]=="C":
            df = rr.get_df_from_asd(dir+"/"+f)
            # crear dataframe
            dataframe['wavelength'] = df['Wavelength']
            dataframe['reflectance'] = df['reflectance']
            
            if f[1] == '1':
                dataframe['pigmento'] = "Cinabrio"
                dataframe['aglutinante'] = "Aceite de linaza"
            elif f[1] == '2':
                dataframe['pigmento'] = "Almagre"
                dataframe['aglutinante'] = "Aceite de linaza"
            elif f[1] == '3':
                dataframe['pigmento'] = "Azarcón o Minio"
                dataframe['aglutinante'] = "Aceite de linaza"
            elif f[1] == '4':
                dataframe['pigmento'] = "Cochinilla. Tlapanocheztli"
                dataframe['aglutinante'] = "Aceite de linaza"
            elif f[1] == '5':
                dataframe['pigmento'] = "Alizarina. Zeechi"
                dataframe['aglutinante'] = ""


            dataframe['base'] = "Yeso"
            dataframe['path'] = dir+"/"+f

            dataframe['carpeta'] = "Tablas1"
            dataframe['tabla'] = "Y7"
            dataframe['espectro'] = f

            df_list.append(dataframe)

        elif f[0]=="D":
            df = rr.get_df_from_asd(dir+"/"+f)
            # crear dataframe
            dataframe['wavelength'] = df['Wavelength']
            dataframe['reflectance'] = df['reflectance']

            if f[1] == '1':
                dataframe['pigmento'] = "Laca rubia"
                dataframe['aglutinante'] = "Aceite de linaza"
            elif f[1] == '2':
                dataframe['pigmento'] = "Azurita"
                dataframe['aglutinante'] = "Aceite de linaza"
            elif f[1] == '3':
                dataframe['pigmento'] = "Esmalte"
                dataframe['aglutinante'] = ""
            elif f[1] == '4':
                dataframe['pigmento'] = "Lapislazuli"
                dataframe['aglutinante'] = "Aceite de linaza"
            elif f[1] == '5':
                dataframe['pigmento'] = "Indigo"
                dataframe['aglutinante'] = ""

            dataframe['base'] = "Yeso"
            dataframe['path'] = dir+"/"+f

            dataframe['carpeta'] = "Tablas1"
            dataframe['tabla'] = "Y7"
            dataframe['espectro'] = f

            df_list.append(dataframe)

        elif f[0]=="E":
            df = rr.get_df_from_asd(dir+"/"+f)
            # crear dataframe
            dataframe['wavelength'] = df['Wavelength']
            dataframe['reflectance'] = df['reflectance']


            if f[1] == '1':
                dataframe['pigmento'] = "Resinato de cobre"
                dataframe['aglutinante'] = ""
            elif f[1] == '2':
                dataframe['pigmento'] = "Malaquita africana"
                dataframe['aglutinante'] = ""
            elif f[1] == '3':
                dataframe['pigmento'] = "Tierra verde de bohemia"
                dataframe['aglutinante'] = "Aceite de linaza"
            elif f[1] == '4':
                dataframe['pigmento'] = "Negro de huesos"
                dataframe['aglutinante'] = "Aceite de linaza"
            elif f[1] == '5':
                dataframe['pigmento'] = "Negro de humo"
                dataframe['aglutinante'] = ""

            dataframe['base'] = "Yeso"
            dataframe['path'] = dir+"/"+f
            dataframe['carpeta'] = "Tablas1"
            dataframe['tabla'] = "Y7"
            dataframe['espectro'] = f

            df_list.append(dataframe)
    
    return df_list

def crear_dataframe(pigmento,tmp):
    carpeta =  "Tablas2"
    base = "Yeso"
    tabla = "Y7"
    # Crear dataframe
    dataframe = pd.DataFrame(columns=['wavelength','reflectance','pigmento','aglutinante','base','path','carpeta','tabla','espectro'])

    tmp_df = rr.create_df_from_txt(tmp)

    dataframe['wavelength'] = tmp_df['Wavelength']
    dataframe['reflectance'] = tmp_df['reflectance']
    dataframe['pigmento'] = pigmento
    dataframe['path'] = tmp
    dataframe['base'] = base
    dataframe['carpeta'] = carpeta
    dataframe['tabla'] = tabla
    dataframe['aglutinante'] = ""
    dataframe['espectro'] = tmp.split("/")[-1]

    return dataframe

def imprimir():
    espectros_1 = obtener_yeso_Y7_tablas_1()
    espectros_2 = obtener_yeso_Y7_tablas_2()
    espectros = espectros_1 + espectros_2
    for o in espectros:
        print(o['carpeta'][0]+" "+o['tabla'][0]+" "+o['espectro'][0]+" "+o['pigmento'][0]+" "+o['aglutinante'][0]+" "+o['base'][0])

def obtener_yeso_Y7():
    espectros_1 = obtener_yeso_Y7_tablas_1()
    espectros_2 = obtener_yeso_Y7_tablas_2()
    espectros = espectros_1 + espectros_2
    return espectros

def str_yeso_y7():
    espectros_1 = obtener_yeso_Y7_tablas_1()
    espectros_2 = obtener_yeso_Y7_tablas_2()
    espectros = espectros_1 + espectros_2
    l_obj = list() 
    for o in espectros:
        s_ejemplar = {'Carpeta':o['carpeta'][0],
                            'Tabla':o['tabla'][0],
                            'Espectro':o['espectro'][0],
                            'Pigmento':o['pigmento'][0],
                            'Aglutinante':o['aglutinante'][0],
                            'Base de preparación':o['base'][0]}
        l_obj.append(s_ejemplar)
    return l_obj