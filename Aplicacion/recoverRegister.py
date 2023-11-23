import csv
import re
import specdal 
from pre_process import process_spectrum_txt,print_spec,process_spectrum_asd
import pandas as pd

registro=set()
with open('pr.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        registro.add(str(row))

       
archivos_txt=process_spectrum_txt()
archivos_asd=process_spectrum_asd()

def encuentra_spec_txt(base,etiqueta):
    etiquetas = ['A1','A2','A3','A4','A5',
             'B1','B2','B3','B4','B5',
             'C1','C2','C3','C4','C5',
             'D1','D2','D3','D4','D5',
             'E1','E2','E3','E4','E5',]
    ind=etiquetas.index(etiqueta)
    for atxt in archivos_txt:
        b=atxt.base[6:]
        if b in base:
            ruta=atxt.rutas[ind]
    return ruta

def encuentra_spec_asd(base,etiqueta):
    etiquetas = ['A1','A2','A3','A4','A5',
             'B1','B2','B3','B4','B5',
             'C1','C2','C3','C4','C5',
             'D1','D2','D3','D4','D5',
             'E1','E2','E3','E4','E5',]
    ind=etiquetas.index(etiqueta)
    for aasd in archivos_asd:
        b=aasd.base
        if b == base:
            ruta=aasd.rutas[ind]
            return ruta
    return None

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

print(".: Buscar registro :.")
ruta=encuentra_spec_txt('C1','A1')
print(ruta)
print_spec(get_df_from_txt(ruta),ruta)

#print(".: Buscar registro :.")
#ruta=encuentra_spec_asd('C1','A1')
#print(ruta)
#print_spec(get_df_from_asd(ruta),ruta)