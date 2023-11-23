from calendar import c
from math import e
from connectDB import consulta_db
from recoverRegister import get_df_from_txt, encuentra_spec_txt

# Controlador de la aplicacion

# Construye consulta para la base de datos
def controlador_busqueda(filtros):
    consulta = "SELECT * FROM registro_espectros WHERE "
    for llave, valor in filtros.items():
        if valor != "": 
            consulta = consulta + llave + " = '" + valor + "' AND "
    consulta = consulta[:-5]
    print("Controlador de busqueda"+str(consulta))
    # consulta la base de datos
    resultados = consulta_db(consulta)
    return resultados

# Construye consulta para la insercion de un nuevo espectro
def controlador_nuevo_espectro(filtros):
    consulta = "INSERT INTO registro_espectros (Espectro, Carpeta, Tabla, Pigmento, Aglutinante, Base_de_preparacion) VALUES ("
    for llave, valor in filtros.items():
        consulta = consulta + "'" + valor + "', "
    consulta = consulta[:-2] + ")"
    # consulta la base de datos
    consulta_db(consulta)

# Construye consulta para la insercion de un nuevo espectro
def controlador_nuevo_espectro_txt(tabla,etiqueta):
    ruta = encuentra_spec_txt(tabla,etiqueta)
    df = get_df_from_txt(ruta)
    espectro = df.columns[1]
    x=df.columns[0]
    y=df.columns[1]

    list_x = list(df[x])
    list_y = list(df[y])
    instruccion = "INSERT INTO registro_espectro (Espectro, wavelenght, reflectance) VALUES ('"+espectro+"','"+str(list_x)+"', '"+str(list_y)+"')"
    consulta_db(instruccion)

# Recuperar espectro de la base de datos
def controlador_recuperar_espectro(id):
    # Obten datos del espectro
    consulta = "SELECT * FROM registro_espectros WHERE Espectro = '"+id+"' "  
    # Obten el espectro
    consulta_spec = "SELECT * FROM registro_espectro WHERE Espectro = '"+id+"' "

    resultados = consulta_db(consulta)
    print(resultados)
    resultados_spec = consulta_db(consulta_spec)
    print(resultados_spec)
    #return resultados

#controlador_nuevo_espectro_txt('C1','A1')
#controlador_recuperar_espectro('A100000.asd')