from connectDB import consulta_db
# Controlador de la aplicacion
def controlador_busqueda(filtros):
    # construye consulta para la base de datos
    consulta = "SELECT * FROM registro_espectros WHERE "
    for llave, valor in filtros.items():
        if valor != "": 
            consulta = consulta + llave + " = '" + valor + "' AND "
    consulta = consulta[:-5]
    print("Controlador de busqueda"+str(consulta))
    # consulta la base de datos
    resultados = consulta_db(consulta)
    return resultados


