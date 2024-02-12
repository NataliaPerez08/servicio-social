"""
Este módulo se encarga de controlar la aplicación, es decir, de manejar la lógica de la aplicación.
"""

from connectDB import consulta_db


"""
Método encargado de hacer la consulta a la base de datos
    Args:
        filtros: diccionario con los filtros de la consulta
"""
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