import os
from matplotlib.pylab import f
import recoverRegister as rr
import pandas as pd
"""
Pigmentos:
(Tabla 1)
Ocre de	mina inglés	(C7: A1)
Rejalgar (C7: A2)
Amarillo de plomo estaño (C7: A3)
Gualda (C7: A4)	
Arzica (C7: A5)

Pardo antílope (C7:B1)
Sombra tostada (C7:B2)
Ocre oscuro	(C7:B3)
Tierra de siena tostada	(C7:B4)
Betún de Judea (C7:B5)

Cinabrio. Kremer (C7:C1)
Almagre (C7:C2)
Minio	(C7:C3)
Laca carmín	(C7:C4)
Carmín de alizarina (C7:C5)

Laca rubia  (C7:D1)
Azurita	natural. Kremer	(C7:D2)
Esmalte	(C7:D3)
Lapislázuli	(C7:D4)
Azul añil (C7:D5)

Resinato de	cobre (C7:E1)
Malaquita	(C7:E2)
Tierra verde de	bohemia	(C7:E3)
Negro marfil o de huesos (C7:E4)
Negro de vid francés (C7:E5)

Carpeta,Tabla,Espectro,Pigmento,Aglutinante,Base de preparación
"""

def obtener_carbonato_C7_tablas_2():
    # Info de Tabla 2
    dir = "Espectros_FORS_2/Tablas 2/Tabla_C7"
    archivos=list()
    for f in os.listdir(dir):
        archivos.append(dir+"/"+f)
    archivos.sort()
    
    df_list = []

    # A1-A2
    tmp = archivos[0]
    df = crear_dataframe("Ocre de mina ingles",tmp)
    df_list.append(df)

    tmp = archivos[1]
    df = crear_dataframe("Rejalgar",tmp)
    df_list.append(df)

    tmp = archivos[2]
    df = crear_dataframe("Amarillo de Plomo",tmp)
    df_list.append(df)

    tmp = archivos[3]
    df = crear_dataframe("Gualda",tmp)
    df_list.append(df)

    tmp = archivos[4]
    df = crear_dataframe("Arzica",tmp)
    df_list.append(df)
    
    # B1 - B5
    tmp = archivos[5]
    df = crear_dataframe("Pardo Antilope",tmp)
    df_list.append(df)

    tmp = archivos[6]
    df = crear_dataframe("Sombra tostada",tmp)
    df_list.append(df)

    tmp = archivos[7]
    df = crear_dataframe("Ocre oscuro",tmp)
    df_list.append(df)

    tmp = archivos[8]
    df = crear_dataframe("Tierra de siena tostada",tmp)
    df_list.append(df)

    tmp = archivos[9]
    df = crear_dataframe("Betun de Judea",tmp)
    df_list.append(df)

    # C1 - C5

    tmp = archivos[10]
    df = crear_dataframe("Cinabrio",tmp)
    df_list.append(df)

    tmp = archivos[11]
    df = crear_dataframe("Almagre",tmp)
    df_list.append(df)

    tmp = archivos[12]
    df = crear_dataframe("Minio",tmp)
    df_list.append(df)

    tmp = archivos[13]
    df = crear_dataframe("Laca carmin",tmp)
    df_list.append(df)

    tmp = archivos[14]
    df = crear_dataframe("Carmin de alizariona",tmp)
    df_list.append(df)

    # D1 - D5
    tmp = archivos[15]
    df = crear_dataframe("Laca rubia",tmp)
    df_list.append(df)

    tmp = archivos[16]
    df = crear_dataframe("Azurita natural",tmp)
    df_list.append(df)
    
    tmp = archivos[17]
    df = crear_dataframe("Esmalte",tmp)
    df_list.append(df)

    tmp = archivos[18]
    df = crear_dataframe("Lapislazuli",tmp)
    df_list.append(df)

    tmp = archivos[19]
    df = crear_dataframe("Azul anil",tmp)
    df_list.append(df)

    # E1 - E5
    tmp = archivos[20]
    df = crear_dataframe("Resinato de cobre",tmp)
    df_list.append(df)

    tmp = archivos[21]
    df = crear_dataframe("Malaquita",tmp)
    df_list.append(df)

    tmp = archivos[22]
    df = crear_dataframe("Tierra verde de bohemia",tmp)
    df_list.append(df)

    tmp = archivos[23]
    df = crear_dataframe("Negro marfil o de huesos",tmp)
    df_list.append(df)

    tmp = archivos[24]
    df = crear_dataframe("Negro de vid frances",tmp)
    df_list.append(df)

    return df_list
def crear_dataframe(pigmento,tmp):
    carpeta =  "Tablas2"
    base = "Carbonato de calcio"
    tabla = "C7"
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
    espectros = obtener_carbonato_C7_tablas_2()
    print(len(espectros))
    for o in espectros:
        print(o['carpeta'][0]+" "+o['tabla'][0]+" "+o['espectro'][0]+" "+o['pigmento'][0]+" "+o['aglutinante'][0]+" "+o['base'][0])

imprimir()

