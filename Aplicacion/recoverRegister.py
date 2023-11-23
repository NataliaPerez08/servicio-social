import csv
from math import e
import re
import specdal 
from pre_process import process_spectrum_tabla2,print_spec,process_spectrum_tabla1,process_spectrum_tablaY4
import pandas as pd

registro=set()
with open('pr.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        registro.add(str(row))

def get_df_from_txt(file):
    data = pd.read_csv(file,delimiter='\t')
    return data

def get_df_from_asd(file):
    data = specdal.Spectrum(filepath=file)
    #data = specdal.spectrum.Spectrum(file)
    data_wl = data.measurement

    # create pandas dataframe
    df = pd.DataFrame(columns=['Wavelength','reflectance'])
    df['Wavelength'] = data_wl.index
    df['reflectance'] = data_wl.values
    return df

def process_registers_txt():
    n_regs=[]
    for r in registro:
        ev = eval(r)
        base=ev['Base']
        etiqueta=ev['Etiqueta']
        ruta=encuentra_spec_txt(base,etiqueta)
        ev['Ruta']=ruta
        df = get_df_from_txt(ruta)
        ev['Dataframe']=df
        n_regs.append(ev)
    return n_regs

#print(n_regs[0])
#specs_df=n_regs[0]['Dataframe']
#etiqueta=n_regs[0]['Etiqueta']
#base=n_regs[0]['Base']
#print_spec(specs_df,etiqueta,base)

def ejemplos():
    print(".: Buscar registro Tablas 1:.")
    ruta=encuentra_spec_asd('C1','A1')
    print(ruta)
    print_spec(get_df_from_asd(ruta),ruta)

    print(".: Buscar registro Tablas 2:.")
    ruta=encuentra_spec_txt('C1','B1')
    print(ruta)
    print_spec(get_df_from_txt(ruta),ruta)


    print(".: Buscar registro Tabla Y4:.")
    ruta=encuentra_ruta_spec_Y4('Tablay400125.asd.txt')
    print(ruta)
    print_spec(get_df_from_txt(ruta),ruta)