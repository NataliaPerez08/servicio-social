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

def obtener_yeso_Y4_tablas_1():
    # Info de Tabla 2
    dir = "Espectros_FORS_2/Tablas 1/Y4"
    archivos=list()
    for f in os.listdir(dir):
        archivos.append(dir+"/"+f)
    archivos.sort()
    
    df_list = list()
    print(len(archivos))
    # A1
    tmp = archivos[0]
    df0 = crear_dataframe("Ocre de mina ingles",tmp)
    tmp = archivos[1]
    df1 = crear_dataframe("Ocre de mina ingles",tmp)
    tmp = archivos[2]
    df2 = crear_dataframe("Ocre de mina ingles",tmp)
    tmp = archivos[3]
    df3 = crear_dataframe("Ocre de mina ingles",tmp)
    tmp = archivos[4]
    df4 = crear_dataframe("Ocre de mina ingles",tmp)
    
    df_list.append(df0)
    df_list.append(df1)
    df_list.append(df2)
    df_list.append(df3)
    df_list.append(df4)

    # A2
    tmp = archivos[5]
    df0 = crear_dataframe("Oropimente",tmp)
    tmp = archivos[6]
    df1 = crear_dataframe("Oropimente",tmp)
    tmp = archivos[7]
    df2 = crear_dataframe("Oropimente",tmp)
    tmp = archivos[8]
    df3 = crear_dataframe("Oropimente",tmp)
    tmp = archivos[9]
    df4 = crear_dataframe("Oropimente",tmp)
    
    df_list.append(df0)
    df_list.append(df1)
    df_list.append(df2)
    df_list.append(df3)
    df_list.append(df4)

    # A3
    tmp = archivos[10]
    df = crear_dataframe("Amarillo de plomo",tmp)
    tmp = archivos[11]
    df = crear_dataframe("Amarillo de plomo",tmp)
    tmp = archivos[12]
    df = crear_dataframe("Amarillo de plomo",tmp)
    tmp = archivos[13]
    df = crear_dataframe("Amarillo de plomo",tmp)
    tmp = archivos[14]
    df = crear_dataframe("Amarillo de plomo",tmp)

    df_list.append(df0)
    df_list.append(df1)
    df_list.append(df2)
    df_list.append(df3)
    df_list.append(df4)

    # A4
    tmp = archivos[15]
    df0 = crear_dataframe("Gualda",tmp)
    tmp = archivos[16]
    df1 = crear_dataframe("Gualda",tmp)
    tmp = archivos[17]
    df2 = crear_dataframe("Gualda",tmp)
    tmp = archivos[18]
    df3 = crear_dataframe("Gualda",tmp)
    tmp = archivos[19]
    df4 = crear_dataframe("Gualda",tmp)

    df_list.append(df0)
    df_list.append(df1)
    df_list.append(df2)
    df_list.append(df3)
    df_list.append(df4)

    # A5
    tmp = archivos[20]
    df0 = crear_dataframe("Arzica",tmp)
    tmp = archivos[21]
    df1 = crear_dataframe("Arzica",tmp)
    tmp = archivos[22]
    df2 = crear_dataframe("Arzica",tmp)
    tmp = archivos[23]
    df3 = crear_dataframe("Arzica",tmp)
    tmp = archivos[24]
    df4 = crear_dataframe("Arzica",tmp)

    df_list.append(df0)
    df_list.append(df1)
    df_list.append(df2)
    df_list.append(df3)
    df_list.append(df4)

    # B1 
    tmp = archivos[25]
    df0 = crear_dataframe("Pardo antilope",tmp)
    tmp = archivos[26]
    df1 = crear_dataframe("Pardo antilope",tmp)
    tmp = archivos[27]
    df2 = crear_dataframe("Pardo antilope",tmp)
    tmp = archivos[28]
    df3 = crear_dataframe("Pardo antilope",tmp)
    tmp = archivos[29]
    df4 = crear_dataframe("Pardo antilope",tmp)

    df_list.append(df0)
    df_list.append(df1)
    df_list.append(df2)
    df_list.append(df3)
    df_list.append(df4)

    # B2
    tmp = archivos[30]
    df0 = crear_dataframe("Sombra tostada de Chipre",tmp)
    tmp = archivos[31]
    df1 = crear_dataframe("Sombra tostada de Chipre",tmp)
    tmp = archivos[32]
    df2 = crear_dataframe("Sombra tostada de Chipre",tmp)
    tmp = archivos[33]
    df3 = crear_dataframe("Sombra tostada de Chipre",tmp)
    tmp = archivos[34]
    df4 = crear_dataframe("Sombra tostada de Chipre",tmp)
    
    df_list.append(df0)
    df_list.append(df1)
    df_list.append(df2)
    df_list.append(df3)
    df_list.append(df4)

    # B3
    tmp = archivos[35]
    df0 = crear_dataframe("Ocre aleman oscuro",tmp)
    tmp = archivos[36]
    df1 = crear_dataframe("Ocre aleman oscuro",tmp)
    tmp = archivos[37]
    df2 = crear_dataframe("Ocre aleman oscuro",tmp)
    tmp = archivos[38]
    df3 = crear_dataframe("Ocre aleman oscuro",tmp)
    tmp = archivos[39]
    df4 = crear_dataframe("Ocre aleman oscuro",tmp)

    df_list.append(df0)
    df_list.append(df1)
    df_list.append(df2)
    df_list.append(df3)
    df_list.append(df4)

    # B4
    tmp = archivos[40]
    df0 = crear_dataframe("Tierra de Siena tostada oscura",tmp)
    tmp = archivos[41]
    df1 = crear_dataframe("Tierra de Siena tostada oscura",tmp)
    tmp = archivos[42]
    df2 = crear_dataframe("Tierra de Siena tostada oscura",tmp)
    tmp = archivos[43]
    df3 = crear_dataframe("Tierra de Siena tostada oscura",tmp)
    tmp = archivos[44]
    df4 = crear_dataframe("Tierra de Siena tostada oscura",tmp)

    df_list.append(df0)
    df_list.append(df1)
    df_list.append(df2)
    df_list.append(df3)
    df_list.append(df4)

    # B5
    tmp = archivos[45]
    df0 = crear_dataframe("Betun de Judea",tmp)
    
    # C1

    tmp = archivos[10]
    df = crear_dataframe("Cinabrio",tmp)
    df_list.append(df)

    tmp = archivos[11]
    df = crear_dataframe("Hematita natural",tmp)
    df_list.append(df)

    tmp = archivos[12]
    df = crear_dataframe("Minio",tmp)
    df_list.append(df)

    tmp = archivos[13]
    df = crear_dataframe("Cochinilla",tmp)
    df_list.append(df)

    tmp = archivos[14]
    df = crear_dataframe("Carmin de alizarina",tmp)
    df_list.append(df)

    # D1-D5

    tmp = archivos[15]
    df = crear_dataframe("Laca rubia",tmp)
    df_list.append(df)

    tmp = archivos[16]
    df = crear_dataframe("Azurita	natural",tmp)
    df_list.append(df)

    tmp = archivos[17]
    df = crear_dataframe("Esmalte",tmp)
    df_list.append(df)

    tmp = archivos[18]
    df = crear_dataframe("Lapislazuli",tmp)
    df_list.append(df)

    tmp = archivos[19]
    df = crear_dataframe("Anil o Indigo",tmp)
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
    df_list.append(df)

    tmp = archivos[23]
    df = crear_dataframe("Negro de huesos o marfil",tmp)
    df_list.append(df)

    tmp = archivos[24]
    df = crear_dataframe("Negro de vid frances",tmp)
    df_list.append(df)

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
    # A1
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
    #espectros_1 = obtener_yeso_Y4_tablas_1()
    espectros_2 = obtener_yeso_Y4_tablas_2()
    #espectros = espectros_1 + espectros_2
    for o in espectros_2:
        print(o['carpeta'][0]+" "+o['tabla'][0]+" "+o['espectro'][0]+" "+o['pigmento'][0]+" "+o['aglutinante'][0]+" "+o['base'][0])

imprimir()