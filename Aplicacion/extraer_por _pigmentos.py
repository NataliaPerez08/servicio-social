import os
from matplotlib.pylab import f

from numpy import arange
import recoverRegister as pre
import pandas as pd
# Path: modelos_all_tables.py

# Modelo del espectro
dataframe = pd.DataFrame(columns=['wavelength','reflectance','pigmento','aglutinante','base'])

# Método para crear el dataframe de un espectro
def crearC1(dir, pigmento, lista_a, base):
    archivos =[]
    for file in os.listdir(dir):
        if file.endswith(".asd"):
            archivos.append(file)
    archivos.sort() 
    lista_df = []
    for spec in archivos:
        if spec[0] =='A':
            path_c1 = dir+spec
            # obtener espectro
            df = pre.get_df_from_asd(path_c1)
            wl = df['Wavelength']
            ref = df['reflectance']
            if spec[1] == '1':
                aglutinante = lista_a[0]
            elif spec[1] == '2':
                aglutinante = lista_a[1]
            elif spec[1] == '3':
                aglutinante = lista_a[2]
            elif spec[1] == '4':
                aglutinante = lista_a[3]
            elif spec[1] == '5':
                aglutinante = lista_a[4]
            # crear dataframe
            df = pd.DataFrame(columns=['wavelength','reflectance','pigmento','aglutinante','base'])
            df['wavelength'] = wl
            df['reflectance'] = ref
            df['pigmento'] = pigmento
            df['aglutinante'] = aglutinante
            df['base'] = base
            lista_df.append(df)
    return lista_df         


# Etiquetar los espectros con el mismo pigmento
# Ocre de mina inglés (marca KremerR, n. 40191) (C1: A1-A5) (C7:A1) (Y1:A1-A5) (Y4:A1)
# (C1: A1-A5)

dir = "Espectros_FORS_2/Tablas 1/C1/"
pigmento = "Ocre de mina inglés"
lista_a = ["Aceite de linaza", "Yema de huevo", "Yema de huevo y aceite de linaza", "Cola de conejo", "Almáciga y aceite de linaza "]
base = "Carbonato de calcio"

l_df_c1_a = crearC1(dir, pigmento, lista_a, base)

# (C7:A1)
dir = "Espectros_FORS_2/Tablas 2/Tabla_C7"
archivos_tablaC7 = []
for file in os.listdir(dir):
    archivos_tablaC7.append(file)
archivos_tablaC7.sort()

# crear dataframe
df_c7_a1 = pd.DataFrame(columns=['wavelength','reflectance','pigmento','aglutinante','base'])
wl = pre.get_df_from_txt(dir+"/"+archivos_tablaC7[0])
df_c7_a1['wavelength'] = wl['Wavelength']
df_c7_a1['reflectance'] = wl[archivos_tablaC7[0][:-4]]
df_c7_a1['pigmento'] = pigmento
df_c7_a1['base'] = "Carbonato de calcio"


# (Y1:A1-A5)
dir = "Espectros_FORS_2/Tablas 1/Y1/"
pigmento = "Ocre de mina inglés"
lista_a = ["Aceite de linaza", "Yema de huevo", "Yema de huevo y aceite de linaza", "Cola de conejo", "Almáciga y aceite de linaza "]
base = "Yeso"

l_df_y1_a = crearC1(dir, pigmento, lista_a, base)

# (Y4:A1)
dir = "Espectros_FORS_2/Tablas 1/Y4/"
archivos_tablaY4 = []
for file in os.listdir(dir):
    archivos_tablaY4.append(file)
archivos_tablaY4.sort()

# crear dataframe
df_y4_a1 = pd.DataFrame(columns=['wavelength','reflectance','pigmento','aglutinante','base'])
df = pre.get_df_from_txt(dir+"/"+archivos_tablaY4[0])
df_y4_a1['wavelength'] = df['Wavelength']
df_y4_a1['reflectance'] = df[archivos_tablaY4[0][:-4]]
pigmento = "Ocre de mina inglés"
df_y4_a1['pigmento'] = pigmento
df_y4_a1['base'] = "Yeso"


# Ocre de mina inglés (marca KremerR, n. 40191) (C1: A1-A5) (C7:A1) (Y1:A1-A5) (Y4:A1)
dataframes_ocre_mina_ingles= l_df_c1_a + [df_c7_a1] + l_df_y1_a + [df_y4_a1]

# Oropimente (molido en el LDOA) (C1: B1-B5) (Y1:B1-B5)

# (C1: B1-B5)
dir = "Espectros_FORS_2/Tablas 1/C1/"
pigmento = "Oropimente"
lista_a = ["Aceite de linaza", "Yema de huevo", "Yema de huevo y aceite de linaza", "Cola de conejo", "Almáciga y aceite de linaza "]
base = "Carbonato de calcio"

l_df_c1_b = crearC1(dir, pigmento, lista_a, base)

# (Y1:B1-B5)
dir = "Espectros_FORS_2/Tablas 1/Y1/"
pigmento = "Oropimente"
lista_a = ["Aceite de linaza", "Yema de huevo", "Yema de huevo y aceite de linaza", "Cola de conejo", "Almáciga y aceite de linaza "]
base = "Yeso"

l_df_y1_b = crearC1(dir, pigmento, lista_a, base)

# Oropimente (molido en el LDOA) (C1: B1-B5) (Y1:B1-B5)
dataframes_oropimente= l_df_c1_b + l_df_y1_b

#Amarillo de plomo estaño (tipo II, marca KremerR, n. 10120) (C1: C1-C5) (Y1:C1-C5)
# (C1: C1-C5)
dir = "Espectros_FORS_2/Tablas 1/C1/"
pigmento = "Amarillo de plomo estaño"
lista_a = ["Aceite de linaza", "Yema de huevo", "Yema de huevo y aceite de linaza", "Cola de conejo", "Almáciga y aceite de linaza "]
base = "Carbonato de calcio"

l_df_c1_c = crearC1(dir, pigmento, lista_a, base)

# (Y1:C1-C5)
dir = "Espectros_FORS_2/Tablas 1/Y1/"
pigmento = "Amarillo de plomo estaño"
lista_a = ["Aceite de linaza", "Yema de huevo", "Yema de huevo y aceite de linaza", "Cola de conejo", "Almáciga y aceite de linaza "]
base = "Yeso"

l_df_y1_c = crearC1(dir, pigmento, lista_a, base)

# Amarillo de plomo estaño (tipo II, marca KremerR, n. 10120) (C1: C1-C5) (Y1:C1-C5)
dataframes_amarillo_plomo_estano= l_df_c1_c + l_df_y1_c

#Ancorca (marca SennelierR, Reseda luteola, sp.) (C1:D1-D5)
# (C1:D1-D5)
dir = "Espectros_FORS_2/Tablas 1/C1/"
pigmento = "Ancorca"
lista_a = ["Aceite de linaza", "Yema de huevo", "Yema de huevo y aceite de linaza", "Cola de conejo", "Almáciga y aceite de linaza "]
base = "Carbonato de calcio"

l_df_c1_d = crearC1(dir, pigmento, lista_a, base)
# Ancorca (marca SennelierR, Reseda luteola, sp.) (C1:D1-D5)
dataframes_ancorca= l_df_c1_d

# Ancorca o gualda (marca ZecchiR, Reseda luteola, sp.) (C1:E1-E5) (Y1:E1-E5)
# (C1:E1-E5)
dir = "Espectros_FORS_2/Tablas 1/C1/"
pigmento = "Ancorca o gualda"
lista_a = ["Aceite de linaza", "Yema de huevo", "Yema de huevo y aceite de linaza", "Cola de conejo", "Almáciga y aceite de linaza "]
base = "Carbonato de calcio"

l_df_c1_e = crearC1(dir, pigmento, lista_a, base)

# (Y1:E1-E5)
dir = "Espectros_FORS_2/Tablas 1/Y1/"
pigmento = "Ancorca o gualda"
lista_a = ["Aceite de linaza", "Yema de huevo", "Yema de huevo y aceite de linaza", "Cola de conejo", "Almáciga y aceite de linaza "]
base = "Yeso"

l_df_y1_e = crearC1(dir, pigmento, lista_a, base)

# Ancorca o gualda (marca ZecchiR, Reseda luteola, sp.) (C1:E1-E5) (Y1:E1-E5)
dataframes_ancorca_gualda= l_df_c1_e + l_df_y1_e

# Ocre claro (fawn ochre marca KremerR, n. 40241) (C2: A1-A5) (tabla 2 (Y2:A1-A5))
dir = "Espectros_FORS_2/Tablas 1/C2/"
pigmento = "Ocre claro"
lista_a = ["Aceite de linaza", "Aceite de nuez", "Yema de huevo", "Cola de conejo", "Almáciga y aceite de linaza"]
base = "Carbonato de calcio"

l_df_c2_a = crearC1(dir, pigmento, lista_a, base)

"""
(tabla 2 (Y2:A1-A5))
dir = "Espectros_FORS_2/Tablas 2/Tabla_Y2"
pigmento = "Ocre claro"
lista_a = ["Aceite de linaza","Yema de huevo", "Yema de huevo y aceite de linaza", "Cola de conejo", "Almáciga y aceite de linaza"]
base = "Yeso"

l_df_y2_a = crearC1(dir, pigmento, lista_a, base)
"""
#Sombra tostada de Chipre (marca KremerR, n. 40720) (C2: B1-B5) (tabla 2(Y2:B1-B5)) (Y4:B2) (Y7:B2)
# (C2: B1-B5)
dir = "Espectros_FORS_2/Tablas 1/C2/"
pigmento = "Sombra tostada de Chipre"
lista_a = ["Aceite de linaza", "Aceite de nuez", "Yema de huevo", "Cola de conejo", "Almáciga y aceite de linaza"]
