import csv
import specdal 
import pandas as pd

registro=set()
with open('pr.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        registro.add(str(row))

def get_df_from_txt(file):
    data = pd.read_csv(file,delimiter='\t')
    return data

def create_df_from_txt(file):
    data = pd.read_csv(file,delimiter='\t')
    # create pandas dataframe
    df = pd.DataFrame(columns=['Wavelength','reflectance'])
    x = data.columns[0]
    y = data.columns[1]
    df['Wavelength'] = data[x]
    df['reflectance'] = data[y]
    return df

def get_df_from_asd(file):
    data = specdal.Spectrum(filepath=file)
    #data = specdal.spectrum.Spectrum(file)
    data_wl = data.measurement

    # create pandas dataframe
    df = pd.DataFrame(columns=['Wavelength','reflectance'])
    df['Wavelength'] = data_wl.index
    df['reflectance'] = data_wl.values
    return df

#print(n_regs[0])
#specs_df=n_regs[0]['Dataframe']
#etiqueta=n_regs[0]['Etiqueta']
#base=n_regs[0]['Base']
#print_spec(specs_df,etiqueta,base)