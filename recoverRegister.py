import csv
from pre_process import process_spectrum_txt,print_spec
import pandas as pd
import numpy as np

registro=set()
with open('pr.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        registro.add(str(row))

       

archivos_txt=process_spectrum_txt()

def encuentra_spec(base,etiqueta):
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

def pget_df_from_txt(file):
    data = pd.read_csv(file,delimiter='\t')
    return data

def process_registers():
    n_regs=[]
    for r in registro:
        ev = eval(r)
        base=ev['Base']
        etiqueta=ev['Etiqueta']
        ruta=encuentra_spec(base,etiqueta)
        ev['Ruta']=ruta
        df = pget_df_from_txt(ruta)
        ev['Dataframe']=df
        n_regs.append(ev)
    return n_regs

#print(n_regs[0])
#specs_df=n_regs[0]['Dataframe']
#etiqueta=n_regs[0]['Etiqueta']
#base=n_regs[0]['Base']

#print_spec(specs_df,etiqueta,base)

print(".: Buscar registro :.")

print("1. Por base e etiqueta \n 2. Aglutianante")
entrada = int(input())


i_base=""
i_etiq=""
if entrada==1:
    print("Dar base, por ejemplo C1:")
    i_base=input()
    print("Dar etiqueta, por ejemplo B3:")
    i_etiq=input()
elif entrada==2:
    print("Da aglutinante")
    i_aglutinante=input()

n_regs = process_registers()

for elem in n_regs:
    e_base=elem['Base']
    e_etq=elem['Etiqueta']
    if e_base == i_base and e_etq == i_etiq:
        print_spec(elem['Dataframe'],elem['Etiqueta'],elem['Base'])
    if i_aglutinante == elem['Aglutinado']:
        print_spec(elem['Dataframe'],elem['Etiqueta'],elem['Base'])