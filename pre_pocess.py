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
    def __str__(self):
        return str(self.base)+", "+str(self.etiqueta)

class Tabla:
    base=""
    # Capas lista de Spec(s)
    capas=list()
    def __init__(self,base):
        self.base=base
    def __str__(self):
        return str(self.base)




datadir = "Espectros_FORS_2/Tablas 1"
tablas = list()
archivos=list()

for f in os.listdir(datadir):
    tablas.append(f)
tablas.sort()

i=0

t=tablas[i]

dirT =datadir+"/"+t
specs = list()

tabla_rep = Tabla(t)
for ft in os.listdir(dirT):
    etiq=ft[0:2] 
    path=dirT+"/"+ft
    s = Spectrum(filepath=path)
    df=s.measurement.to_frame()
    tmp_spec = Spec(t,etiq,df,path)
    specs.append(tmp_spec)
tabla_rep.capas=specs

archivos.insert(tabla_rep)




