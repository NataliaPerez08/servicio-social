from matplotlib import pyplot as plt
import specdal as specdal

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