import os
import pre_process as pp
import recoverRegister as rr
import pandas as pd
"""
Pigmentos:
(Tabla 1)
Ocre de mina inglés (marca KremerR, n. 40191) (C1: A1-A5) (C7:A1) (Y1:A1-A5) (Y4:A1)
Oropimente (molido en el LDOA)	(C1: B1-B5) (Y1:B1-B5)
Amarillo de plomo estaño (tipo II, marca KremerR, n. 10120) (C1: C1-C5) (Y1:C1-C5)
Ancorca (marca SennelierR, Reseda luteola, sp.) (C1:D1-D5)
Ancorca o gualda (marca ZecchiR, Reseda luteola, sp.) (C1:E1-E5) (Y1:E1-E5)
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
        if f[0]=="A":
            df = rr.get_df_from_asd(dir+"/"+f)
            ocre_mina_ingles.append(df)
        elif f[0]=="B":
            df = rr.get_df_from_asd(dir+"/"+f)
            oropimente.append(df)
        elif f[0]=="C":
            df = rr.get_df_from_asd(dir+"/"+f)
            amarillo_plomo_estano.append(df)
        elif f[0]=="D":
            df = rr.get_df_from_asd(dir+"/"+f)
            ancorca_sennelier.append(df)
        elif f[0]=="E":
            df = rr.get_df_from_asd(dir+"/"+f)
            ancorca_zecchi.append(df)
    
    return [ocre_mina_ingles,oropimente,amarillo_plomo_estano,ancorca_sennelier,ancorca_zecchi]

def obtener_carbonato_C1_tablas_2():
    # Info de Tabla 2
    dir = "Espectros_FORS_2/Tablas 2/Tabla_C1"
    archivos=list()
    for f in os.listdir(dir):
        archivos.append(dir+"/"+f)
    archivos.sort()
    
    tmp = archivos[0:5]
    ocre_mina_ingles = obtener_dframes(tmp)

    tmp = archivos[5:10]
    oropimente = obtener_dframes(tmp)

    tmp = archivos[10:15]
    amarillo_plomo_estano = obtener_dframes(tmp)

    tmp = archivos[15:20]
    ancorca_sennelier = obtener_dframes(tmp)

    tmp = archivos[20:25]
    ancorca_zecchi = obtener_dframes(tmp)
    return [ocre_mina_ingles,oropimente,amarillo_plomo_estano,ancorca_sennelier,ancorca_zecchi]

def obtener_dframes(lista):
    dframes = list()
    for l in lista:
        dframes.append(rr.get_df_from_txt(l))
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

print("Obteniendo carbonato C1")
carbonato_C1 = obtener_carbonato_C1()
print(len(carbonato_C1[0]))

ocre = carbonato_C1[0]
for o in ocre:
    pp.print_spec_from_df(o,"Ocre de mina inglés")