import csv
import sqlite3

# Conecta a la base de datos
def insertar_lista_a_registro_espectros(espectros: list):
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

    
    espectro = espectros[0]
    carpeta = espectros[1]
    tabla = espectros[2]
    pigmento = espectros[3]
    aglutinante = espectros[4]
    base = espectros[5]

    


    #qery = "INSERT INTO registro_espectros (Espectro, Carpeta, Tabla, Pigmento, Aglutinante) VALUES (?, ?, ?, ?, ?, ?)", (espectro, carpeta, tabla, pigmento, aglutinante, base)
    # Ejecuta la consulta
    qery = "INSERT INTO registro_espectros (Espectro, Carpeta, Tabla, Pigmento, Aglutinante, Base_de_preparacion) VALUES ('" + espectro + "', '" + carpeta + "', '" + tabla + "', '" + pigmento + "', '" + aglutinante + "', '" + base + "')"
    print(qery)

    cursor.execute(qery)

    # Confirma la creacion de la tabla
    connection.commit()

    # Cierre de la conexion a la base de datos
    connection.close()

# Recibe la ruta de un csv y actualiza la base de datos
def recibe_csv_actualiza_db(ruta: str):
    print("Recibiendo csv")
    # Lee el csv
    try:
        with open(ruta, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            # Recorre cada renglon del csv

            for row in reader:
                espectro = row['Espectro']
                carpeta = row['Carpeta']
                tabla = row['Tabla']
                pigmento = row['Pigmento']
                aglutinante = row['Aglutinante']
                base = row['Base de preparacion']

                insertar_lista_a_registro_espectros([espectro, carpeta, tabla, pigmento, aglutinante, base])
            
    except FileNotFoundError:
        print("El archivo no existe")
        exit()

print("Espectros_FORS_2/Datos tabla.csv")
recibe_csv_actualiza_db("Espectros_FORS_2/Datos tabla.csv")

