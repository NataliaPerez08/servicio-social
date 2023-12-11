import os
import recoverRegister as pre
import pandas as pd
# Path: modelos_all_tables.py

# Modelo del espectro
dataframe = pd.DataFrame(columns=['wavelength','reflectance','pigmento','aglutinante','base'])

# Obtener de la Tabla1 los espectro y etiquetar
pigmentos_t1 = ["Ocre de mina inglés (marca KremerR, n. 40191)", "Oropimente (molido en el LDOA)","Amarillo de plomo estaño (tipo II, marca KremerR, n. 10120)","Ancorca (marca SennelierR, Reseda luteola, sp.)","Ancorca o gualda (marca ZecchiR, Reseda luteola, sp.)"]

# Etiquetar los espectros con el mismo pigmento
# Ocre de mina inglés (marca KremerR, n. 40191) (C1: A1-A5) (C7:A1) (Y1:A1-A5) (Y4:A1)
# (C1: A1-A5)
dir = "Espectros_FORS_2/Tablas 1/C1/"
for spec in os.listdir(dir):
    if spec[0] =='A':
        path_c1 = dir+spec
        # obtener espectro
        df = pre.get_df_from_asd(path_c1)
        wl = df['Wavelength']
        ref = df['reflectance']

        if spec[1] == '1':
            aglutinante = "Aceite de linaza"
        elif spec[1] == '2':
            aglutinante = "Yema de huevo"
        elif spec[1] == '3':
            aglutinante = "Yema de huevo y aceite de linaza"
        elif spec[1] == '4':
            aglutinante = "Cola de conejo"
        elif spec[1] == '5':
            aglutinante = "Almáciga y aceite de linaza "
        # crear dataframe
        df = pd.DataFrame(columns=['wavelength','reflectance','pigmento','aglutinante','base'])
        df['wavelength'] = wl
        df['reflectance'] = ref
        df['pigmento'] = "Ocre de mina inglés"
        df['aglutinante'] = aglutinante
        df['base'] = "Carbonato de calcio"

        print(df)
        
        
# (C7:A1)
dir = "Espectros_FORS_2/Tablas 1/C7/"


# (C7:A1)
# (Y1:A1-A5)
# (Y4:A1)

# TODO
# TERMINAR CLASIFICACION
# VISUALIZAR VARIOS ESPECTROS

#diferenter medicions 1,2
