import csv
import re
# Programa que conecta con la base de datos
import connectDB as cdb

# Recibe la ruta de un csv y actualiza la base de datos
def recibe_csv_actualiza_db(ruta: str):
    print("Recibiendo csv")
    # Lee el csv
    try:
        with open(ruta, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            # Recorre cada renglon del csv
            print(reader.fieldnames)
            
    except FileNotFoundError:
        print("El archivo no existe")
        exit()

print("Espectros_FORS_2/Datos tabla.csv")
recibe_csv_actualiza_db("Espectros_FORS_2/Datos tabla.csv")
