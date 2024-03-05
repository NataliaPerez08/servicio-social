"""
Este modulo contiene las funciones para crear la tabla de registro de espectros y para realizar consultas a la base de datos
"""

import sqlite3

""" 
Localización de la base de datos 
"""
DATABASE_FILE = "../Aplicacion/db_app.db"

# Mensaje a mostrar
msg = "La base de datos no existe"

def create_table_registro_espectros():
    """
    Método para crear la tabla de registro de espectros
    """
    # Establece el nombre de la base de datos
    # Revisa si la base de datos existe
    try:
        open(DATABASE_FILE)
    except IOError:
        print(msg)
        exit()
    # Crea la conexion a la base de datos
    connection = sqlite3.connect(DATABASE_FILE)
    # Crea el cursor para ejecutar las consultas
    cursor = connection.cursor()

    # Crea la tabla de registro de espectros
    cursor.execute("CREATE TABLE registro_espectros (Espectro text, Carpeta text, Tabla text, Pigmento text, Aglutinante text, Base_de_preparacion text)")
    # Confirma la creacion de la tabla
    connection.commit()

    # Cierre de la conexion a la base de datos
    connection.close()


def consulta_db(consulta):
    """
    Método para realizar una consulta a la base de datos
        @args: consulta: consulta (query) a realizar
        @return: resultados de la consulta
    """
    # Revisa si la base de datos existe
    try:
        open(DATABASE_FILE)
    except IOError:
        print(msg)
        exit()
    # Crea la conexion a la base de datos
    connection = sqlite3.connect(DATABASE_FILE)
    # Crea el cursor para ejecutar las consultas
    cursor = connection.cursor()
    # Ejecuta la consulta
    cursor.execute(consulta)
    # Guarda los resultados
    resultados = cursor.fetchall()
    # Confirma la creacion de la tabla
    connection.commit()
    # Cierre de la conexion a la base de datos
    connection.close()
    # Retorna los resultados
    return resultados