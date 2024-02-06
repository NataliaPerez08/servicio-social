import sqlite3
# Modelo de la aplicación
# Funcion para crear la tabla de registro_espectros 
database_file = "Aplicacion/db_app.db"
msg = "La base de datos no existe"
def create_table_registro_espectros():
    # Establece el nombre de la base de datos
    # Revisa si la base de datos existe
    try:
        open(database_file)
    except IOError:
        print(msg)
        exit()
    # Crea la conexion a la base de datos
    connection = sqlite3.connect(database_file)
    # Crea el cursor para ejecutar las consultas
    cursor = connection.cursor()

    # Crea la tabla de registro de espectros
    cursor.execute("CREATE TABLE registro_espectros (Espectro text, Carpeta text, Tabla text, Pigmento text, Aglutinante text, Base_de_preparacion text)")
    # Confirma la creacion de la tabla
    connection.commit()

    # Cierre de la conexion a la base de datos
    connection.close()

# Funcion para realizar una consulta a la base de datos
def consulta_db(consulta):
    # Revisa si la base de datos existe
    try:
        open(database_file)
    except IOError:
        print(msg)
        exit()
    # Crea la conexion a la base de datos
    connection = sqlite3.connect(database_file)
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