from connectDB import consulta_db
from recoverRegister import get_df_from_txt

# Controlador de la aplicacion

# Construye consulta para la base de datos
def controlador_busqueda(filtros):
    consulta = "SELECT * FROM registro_espectros WHERE "
    for llave, valor in filtros.items():
        if valor != "": 
            consulta = consulta + llave + " LIKE '" + valor + "' AND "
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