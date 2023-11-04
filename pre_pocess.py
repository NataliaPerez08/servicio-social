import os
from specdal import Collection, Spectrum, read
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

class Spec:
    # Carbonato/Yeso de la forma Y1 o C1
    base="" 
    # Etiqueta de la forma A1,A2
    etiqueta=""
    # Dataframe
    dataFrame=None
    # Path
    path =""
    def __init__(self,base,etiqueta,dataFrame,path):
        self.base=base
        self.etiqueta=etiqueta
        self.dataFrame=dataFrame
        self.path=path
    def __str__(self):
        return str(self.base)+", "+str(self.etiqueta)

class Tabla:
    base=""
    # Rutas de la forma {etiqueta:ruta}
    rutas=[]
    def __init__(self,base):
        self.base=base
    def __str__(self):
        return str(self.base)



def process_spectrum_txt():
    datadir = "Espectros_FORS_2/Tablas 2"
    tablas = list()
    archivos=list()
    for f in os.listdir(datadir):
        tablas.append(f)
    tablas.sort()
    i=0
    t=tablas[i]
    while i < len(tablas):
        dirT =datadir+"/"+t
        tabla_rep = Tabla(t)
        specs=[]
        for ft in os.listdir(dirT):
            path=dirT+"/"+ft
            specs.append(path)
        specs.sort()
        tabla_rep.rutas=specs
        archivos.append(tabla_rep)
        i+=1
    return archivos

def dar_intervalo(inicio,fin):
    return [inicio-350,fin-350]

def process_table(table,interval):
    specs_df = []
    features = []
    archivos = table.rutas
    ini=interval[0]
    fin=interval[1]
    for f in archivos:
        data = pd.read_csv(f,delimiter='\t')
        title =str(f)[:-4]
        dev_x = data.columns[0][ini:fin]
        dev_y = data.columns[1][ini:fin]
        specs_df.append(data)
        tmp = np.array(dev_y)
        features.append(tmp)
    return specs_df

archivos_txt=process_spectrum_txt()
interval=dar_intervalo(450,2151)
process_table(archivos_txt[0],interval)

