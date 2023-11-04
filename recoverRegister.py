import csv
from pre_process import process_spectrum_txt

"""
registro=set()
with open('pr.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        registro.add(str(row))
"""
       

archivos_txt=process_spectrum_txt()

def encuentra_spec(base,etiqueta):
    etiquetas = ['A1','A2','A3','A4','A5',
             'B1','B2','B3','B4','B5',
             'C1','C2','C3','C4','C5',
             'D1','D2','D3','D4','D5',
             'E1','E2','E3','E4','E5',]
    ind=etiquetas.index(etiqueta)
    print(ind)
    for atxt in archivos_txt:
        b=atxt.base[6:]
        if b in base:
            print("Encontre la tabla")
            print(atxt.rutas[ind])


"""
base=set()
for r in registro:
    etiquetas_presentes=set()
    ev = eval(r)
    base.add(row['Base'])
    print(ev['Etiqueta'])
"""
encuentra_spec('C1','A1')