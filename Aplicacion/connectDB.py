import sqlite3

# Establece el nombre de la base de datos
database_file = "Aplicacion/db_app.db"
# Revisa si la base de datos existe
try:
    open(database_file)
except IOError:
    print("La base de datos no existe")
    exit()


# Crea la conexion a la base de datos
connection = sqlite3.connect(database_file)
# Crea el cursor para ejecutar las consultas
cursor = connection.cursor()
# Ejecuta una insercion
#cursor.execute("INSERT INTO registro_espectros VALUES (10, 10, 10, 10, 10, 10, 10, 10)")

# Confirma la insercion
#connection.commit()

# Ejecuta una consulta
cursor.execute("SELECT * FROM registro_espectros")
# Obtiene los resultados de la consulta
results = cursor.fetchall()
# Imprime los resultados
print(results)

# Cierre de la conexion a la base de datos
connection.close()
