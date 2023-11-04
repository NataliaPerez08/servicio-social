import os
from specdal import Collection, Spectrum, read

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




datadir = "Espectros_FORS_2/Tablas 1"
archivos = list()
tablas = list()

for f in os.listdir(datadir):
    tablas.append(f)
tablas.sort()
print(tablas)

t=tablas[1]
dirT =datadir+"/"+t
print(t)
for ft in os.listdir(dirT)[0:1]:
    etiq=ft[0:1] 
    path=dirT+"/"+ft
    s = Spectrum(filepath=path)
    df=s.measurement.to_frame()
    tmp_spec = Spec(t,etiq,df,path)
        
"""
for t in tablas:
    dirT =datadir+"/"+t
    print(t)
    for ft in os.listdir(dirT):
        print(ft)
"""


