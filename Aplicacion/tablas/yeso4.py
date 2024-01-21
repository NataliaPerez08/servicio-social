import os
import recoverRegister as rr
import pandas as pd
"""
Ocre de	mina inglés	(Y4: A1)
Oropimente	(Y4: A2)
Amarillo de plomo (Y4: A3)
Gualda (Y4: A4)	
Arzica (Y4: A5)

Pardo antílope (Y4:B1)
Sombra tostada de Chipre(Y4:B2)
Ocre alemán oscuro	(Y4:B3)
Tierra de Siena tostada oscura (Y4:B4)
Betún de Judea (Y4:B5)

Cinabrio (Y4:C1)
Hematita natural (Y4:C2)
Minio	(Y4:C3)
Cochinilla (Y4:C4)
Carmín de alizarina (Y4:C5)

Laca rubia  (Y4:D1)
Azurita	natural. Zeechi(Y4:D2)
Esmalte	(Y4:D3)
Lapislázuli	(Y4:D4)
Añil o Índigo(Y4:D5)

Resinato de	cobre, Blanco de plomo, ocre y negro de vid (Y4:E1)
Malaquita natural (Y4:E2)
Terra verde (Y4:E3)
Negro de huesos o marfil (Y4:E4)
Negro de vid francés (Y4:E5)
"""
def obtener_dframes(lista,pigmento,aglutinante):
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
        dataframe['carpeta'] = "Tablas1"
        dataframe['tabla'] = "Y4"
        dataframe['espectro'] = l.split("/")[-1]
        dataframe['aglutinante'] = aglutinante

        dframes.append(dataframe)

    return dframes

def obtener_yeso_Y4_tablas_1():
    # Info de Tabla 1
    dir = "Espectros_FORS_2/Tablas 1/Y4"
    archivos=list()
    for f in os.listdir(dir):
        archivos.append(dir+"/"+f)
    archivos.sort()

    df_list = list()
    # A1-A5
    l_tmp = archivos[0:5]
    pigmento = "Ocre de mina ingles"
    aglutinante = "Aceite de linaza"
    dframes = obtener_dframes(l_tmp,pigmento,aglutinante)
    df_list = df_list + dframes

    l_tmp = archivos[5:10]
    pigmento = "Oropimente"
    aglutinante = "Aceite de linaza"
    dframes = obtener_dframes(l_tmp,pigmento,aglutinante)
    df_list = df_list + dframes

    l_tmp = archivos[10:15]
    pigmento = "Amarillo de plomo"
    aglutinante = "Aceite de linaza"
    dframes = obtener_dframes(l_tmp,pigmento,aglutinante)
    df_list = df_list + dframes

    l_tmp = archivos[15:20]
    pigmento = "Gualda"
    dframes = obtener_dframes(l_tmp,pigmento,aglutinante)
    df_list = df_list + dframes

    l_tmp = archivos[20:25]
    pigmento = "Arzica"
    dframes = obtener_dframes(l_tmp,pigmento,aglutinante)
    df_list = df_list + dframes

    # B1-B5
    l_tmp = archivos[25:30]
    pigmento = "Pardo antilope"
    aglutinante = "Aceite de linaza"
    dframes = obtener_dframes(l_tmp,pigmento,aglutinante)
    df_list = df_list + dframes

    l_tmp = archivos[30:35]
    pigmento = "Sombra tostada de Chipre"
    dframes = obtener_dframes(l_tmp,pigmento,aglutinante)
    df_list = df_list + dframes

    l_tmp = archivos[35:40]
    pigmento = "Ocre aleman oscuro"
    aglutinante = "Aceite de linaza"
    dframes = obtener_dframes(l_tmp,pigmento,aglutinante)
    df_list = df_list + dframes

    l_tmp = archivos[40:45]
    pigmento = "Tierra de Siena tostada oscura"
    dframes = obtener_dframes(l_tmp,pigmento,aglutinante)
    df_list = df_list + dframes

    l_tmp = archivos[45:50]
    pigmento = "Betun de Judea"
    aglutinante = "Aceite de linaza"
    dframes = obtener_dframes(l_tmp,pigmento,aglutinante)
    df_list = df_list + dframes

    # C1-C5
    l_tmp = archivos[50:55]
    pigmento = "Cinabrio"
    aglutinante = "Aceite de linaza"
    dframes = obtener_dframes(l_tmp,pigmento,aglutinante)
    df_list = df_list + dframes

    l_tmp = archivos[55:60]
    pigmento = "Hematita natural"
    aglutinante = "Aceite de linaza"
    dframes = obtener_dframes(l_tmp,pigmento,aglutinante)
    df_list = df_list + dframes

    l_tmp = archivos[60:65]
    pigmento = "Minio"
    aglutinante = "Aceite de linaza"
    dframes = obtener_dframes(l_tmp,pigmento,aglutinante)
    df_list = df_list + dframes

    l_tmp = archivos[65:70]
    pigmento = "Cochinilla"
    aglutinante = "Aceite de linaza"
    dframes = obtener_dframes(l_tmp,pigmento,aglutinante)
    df_list = df_list + dframes

    l_tmp = archivos[70:75]
    pigmento = "Carmin de alizarina"
    aglutinante = "Aceite de linaza"
    dframes = obtener_dframes(l_tmp,pigmento,aglutinante)
    df_list = df_list + dframes

    # D1-D5
    l_tmp = archivos[75:80]
    pigmento = "Laca rubia"
    aglutinante = "Aceite de linaza"
    dframes = obtener_dframes(l_tmp,pigmento,aglutinante)
    df_list = df_list + dframes

    l_tmp = archivos[80:85]
    pigmento = "Azurita natural"
    aglutinante = "Aceite de linaza"
    dframes = obtener_dframes(l_tmp,pigmento,aglutinante)
    df_list = df_list +dframes

    l_tmp = archivos[85:90]
    pigmento = "Esmalte"
    dframes = obtener_dframes(l_tmp,pigmento,aglutinante)
    df_list = df_list +dframes

    l_tmp = archivos[90:95]
    pigmento = "Lapislazuli"
    aglutinante = "Aceite de linaza"
    dframes = obtener_dframes(l_tmp,pigmento,aglutinante)
    df_list= df_list + dframes

    l_tmp = archivos[95:100]
    pigmento = "Anil o Indigo"
    aglutinante = "Aceite de linaza"
    dframes = obtener_dframes(l_tmp,pigmento,aglutinante)
    df_list= df_list + dframes

    # E1-E5
    l_tmp = archivos[100:105]
    pigmento = "Resinato de cobre"
    dframes = obtener_dframes(l_tmp,pigmento,aglutinante)
    df_list = df_list + dframes

    l_tmp = archivos[105:110]
    pigmento = "Malaquita natural"
    dframes = obtener_dframes(l_tmp,pigmento,aglutinante)
    df_list = df_list + dframes

    l_tmp = archivos[110:115]
    pigmento = "Terra verde"
    aglutinante = "Aceite de linaza"
    dframes = obtener_dframes(l_tmp,pigmento,aglutinante)
    df_list= df_list + dframes

    l_tmp = archivos[115:120]
    pigmento = "Negro de huesos o marfil"
    dframes = obtener_dframes(l_tmp,pigmento,aglutinante)
    df_list = df_list + dframes

    l_tmp = archivos[120:125]
    pigmento = "Negro de vid frances"
    dframes = obtener_dframes(l_tmp,pigmento,aglutinante)
    df_list = df_list + dframes

    return df_list

def crear_dataframe(pigmento,tmp):
    carpeta =  "Tablas2"
    base = "Yeso"
    tabla = "Y4"
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

def obtener_yeso_Y4_tablas_2():
    # Info de Tabla 1
    dir = "Espectros_FORS_2/Tablas 2/Tabla_Y4"
    archivos=list()
    for f in os.listdir(dir):
        archivos.append(dir+"/"+f)
    archivos.sort()

    df_list = list()
    # A1-A5
    tmp = archivos[0]
    df = crear_dataframe("Ocre de mina ingles",tmp)
    df['aglutinante'] = "Aceite de linaza"
    df_list.append(df)
    
    tmp = archivos[1]
    df = crear_dataframe("Oropimente",tmp)
    df['aglutinante'] = "Aceite de linaza"
    df_list.append(df)
   
    tmp = archivos[2]
    df = crear_dataframe("Amarillo de plomo",tmp)
    df['aglutinante'] = "Aceite de linaza"
    df_list.append(df)

    tmp = archivos[3]
    df = crear_dataframe("Gualda",tmp)
    df_list.append(df)

    tmp = archivos[4]
    df = crear_dataframe("Arzica",tmp)
    df_list.append(df)

    # B1-B5
    tmp = archivos[5]
    df = crear_dataframe("Pardo antilope",tmp)
    df["aglutinante"] = "Aceite de linaza"
    df_list.append(df)

    tmp = archivos[6]
    df = crear_dataframe("Sombra tostada de Chipre",tmp)
    df_list.append(df)

    tmp = archivos[7]
    df = crear_dataframe("Ocre aleman oscuro",tmp)
    df["aglutinante"] = "Aceite de linaza"
    df_list.append(df)

    tmp = archivos[8]
    df = crear_dataframe("Tierra de Siena tostada oscura",tmp)
    df_list.append(df)

    tmp = archivos[9]
    df = crear_dataframe("Betun de Judea",tmp)
    df["aglutinante"] = "Aceite de linaza"
    df_list.append(df)

    
    # C1-C5
    tmp = archivos[10]
    df = crear_dataframe("Cinabrio",tmp)
    df["aglutinante"] = "Aceite de linaza"
    df_list.append(df)

    tmp = archivos[11]
    df = crear_dataframe("Hematita natural",tmp)
    df["aglutinante"] = "Aceite de linaza"
    df_list.append(df)

    tmp = archivos[12]
    df = crear_dataframe("Minio",tmp)
    df["aglutinante"] = "Aceite de linaza"
    df_list.append(df)

    tmp = archivos[13]
    df = crear_dataframe("Cochinilla",tmp)
    df["aglutinante"] = "Aceite de linaza"
    df_list.append(df)

    tmp = archivos[14]
    df = crear_dataframe("Carmin de alizarina",tmp)
    df["aglutinante"] = "Aceite de linaza"
    df_list.append(df)

    # D1-D5

    tmp = archivos[15]
    df = crear_dataframe("Laca rubia",tmp)
    df["aglutinante"] = "Aceite de linaza"
    df_list.append(df)

    tmp = archivos[16]
    df = crear_dataframe("Azurita	natural",tmp)
    df["aglutinante"] = "Aceite de linaza"
    df_list.append(df)

    tmp = archivos[17]
    df = crear_dataframe("Esmalte",tmp)
    df_list.append(df)

    tmp = archivos[18]
    df = crear_dataframe("Lapislazuli",tmp)
    df["aglutinante"] = "Aceite de linaza"
    df_list.append(df)

    tmp = archivos[19]
    df = crear_dataframe("Anil o Indigo",tmp)
    df["aglutinante"] = "Aceite de linaza"
    df_list.append(df)

    # E1-E5
    tmp = archivos[20]
    df = crear_dataframe("Resinato de cobre",tmp)
    df_list.append(df)

    tmp = archivos[21]
    df = crear_dataframe("Malaquita natural",tmp)
    df_list.append(df)

    tmp = archivos[22]
    df = crear_dataframe("Terra verde",tmp)
    df["aglutinante"] = "Aceite de linaza"
    df_list.append(df)

    tmp = archivos[23]
    df = crear_dataframe("Negro de huesos o marfil",tmp)
    df_list.append(df)

    tmp = archivos[24]
    df = crear_dataframe("Negro de vid frances",tmp)
    df_list.append(df)

    return df_list

def imprimir():
    espectros_1 = obtener_yeso_Y4_tablas_1()
    espectros_2 = obtener_yeso_Y4_tablas_2()
    espectros = espectros_1 + espectros_2
    for o in espectros:
       # print(o)
        print(o['carpeta'][0]+" "+o['tabla'][0]+" "+o['espectro'][0]+" "+o['pigmento'][0]+" "+o['aglutinante'][0]+" "+o['base'][0])

def obtener_yeso_Y4():
    espectros_1 = obtener_yeso_Y4_tablas_1()
    espectros_2 = obtener_yeso_Y4_tablas_2()
    espectros = [espectros_1,espectros_2]#espectros_1 + espectros_2
    return espectros

def str_yeso_y4():
    espectros_1 = obtener_yeso_Y4_tablas_1()
    espectros_2 = obtener_yeso_Y4_tablas_2()
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