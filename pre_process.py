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
    while i < len(tablas):
        t=tablas[i]
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
    archivos = table.rutas
    ini=interval[0]
    fin=interval[1]
    for f in archivos:
        data = pd.read_csv(f,delimiter='\t')
        dev_x = data.columns[0][ini:fin]
        dev_y = data.columns[1][ini:fin]
        specs_df.append(data)
        tmp = np.array(dev_y)
    return specs_df

def extract_features(archivos_txt,interval):
    features = []
    ini=interval[0]
    fin=interval[1]
    for f_txt in archivos_txt:
        for f in f_txt.rutas:
            data = pd.read_csv(f,delimiter='\t')
            dev_x = data.columns[0][ini:fin]
            dev_y = data.columns[1][ini:fin]
            tmp = np.array(dev_y)
            features.append(tmp)
    return features

def print_table(specs_df,tabla):
    cont=0
    etiquetas = ['A1','A2','A3','A4','A5',
             'B1','B2','B3','B4','B5',
             'C1','C2','C3','C4','C5',
             'D1','D2','D3','D4','D5',
             'E1','E2','E3','E4','E5',]
    for f in specs_df:
        x=f.columns[0]
        y=f.columns[1]
        dev_x = f[x].to_numpy()
        dev_y = f[y].to_numpy()
        plt.plot(dev_x, dev_y)
        plt.xlabel('Wavelength')
        plt.ylabel('Reflectance')
        t = tabla,etiquetas[cont]
        plt.title(t)
        plt.show()
        cont+=1
    

archivos_txt=process_spectrum_txt()
interval=dar_intervalo(450,2151)
#features = extract_features(archivos_txt,interval)

table=archivos_txt[8]
specs_df=process_table(table,interval)
print_table(specs_df,table.base)

#for atxt in archivos_txt:
#    print(atxt)
#    for ar in atxt.rutas:
#        print(ar)
