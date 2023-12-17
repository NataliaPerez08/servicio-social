import os
from matplotlib import pyplot as plt
import specdal as specdal

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


# Funcion que procesa los espectros de la carpeta Tablas 2 (txt)
def process_spectrum_tabla2():
    datadir = "Espectros_FORS_2/Tablas 2"
    return process_spectrum(datadir)

# Funcion que procesa los espectros de la carpeta Tablas 1 (asd)
def process_spectrum_tabla1():
    datadir = "Espectros_FORS_2/Tablas 1"
    return process_spectrum(datadir)

# Funcion que procesa los espectros de la carpeta Tablas Y4 (txt)
def process_spectrum_tablaY4():
    datadir = "Espectros_FORS_2/Y4"
    archivos=list()
    for f in os.listdir(datadir):
        archivos.append(datadir+"/"+f)
    archivos.sort()
    return archivos

# Funcion que extrae los espectros de la carpeta especificada
def process_spectrum(directorio):
    tablas = list()
    archivos=list()
    for f in os.listdir(directorio):
        tablas.append(f)
    tablas.sort()
    i=0
    while i < len(tablas):
        t=tablas[i]
        dirT =directorio+"/"+t
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

# Devuelve el intervalo de longitudes de onda para el espectro
def dar_intervalo(inicio,fin):
    return [inicio-350,fin-350]


def print_spec(specs_df,ruta):
    etiqueta=ruta.split('/')[2]
    base= ruta.split('/')[1]
    print(ruta.split('/'))
    if len(ruta.split('/')) > 3:
        tabla= ruta.split('/')[3]
    else:
        tabla=''
    x=specs_df.columns[0]
    y=specs_df.columns[1]
    dev_x = specs_df[x].to_numpy()
    dev_y = specs_df[y].to_numpy()
    plt.plot(dev_x, dev_y)
    plt.xlabel('Wavelength')
    plt.ylabel('Reflectance')
    t = base,etiqueta,tabla
    plt.title(t)
    plt.show()

def print_spec_from_df(specs_df,titulo=""):
    x=specs_df.columns[0]
    y=specs_df.columns[1]
    dev_x = specs_df[x].to_numpy()
    dev_y = specs_df[y].to_numpy()
    plt.plot(dev_x, dev_y)
    plt.xlabel('Wavelength')
    plt.ylabel('Reflectance')
    plt.title(titulo)
    plt.show()


#archivos_txt=process_spectrum_tabla2()
#for atxt in archivos_txt:
#    print(atxt)
#    for ar in atxt.rutas:
#        print(ar)

#archivosY4 = process_spectrum_tablaY4()
#for a in archivosY4:
#    print(a)