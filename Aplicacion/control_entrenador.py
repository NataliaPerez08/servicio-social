
"""
Modulo encargado de recuperar los ejemplares de la base de datos
"""
import numpy as np
# Conexion a la base de datos
from connectDB import consulta_db
# Función para obtener dataframes
from controlSpec import get_df

# Dataframe
import pandas as pd

# Función para obtener los datos de entrenamiento y prueba

"""
Método encargado de obtener los datos de entrenamiento y prueba
    Args:
        ejemplares: lista de ejemplares
        etiqueta_a_usar: etiqueta a usar (Aglutinante, Pigmento)
    Returns:
        X: datos de entrenamiento
        y: etiquetas
"""
def get_x_y(ejemplares,etiqueta_a_usar):
    aux_y = list()
    aux_x = list()

    for e in ejemplares:
        eti = str(e[etiqueta_a_usar][0])
        aux_y.append(eti)
        aux_x.append(e['reflectance'].to_numpy())
    X = np.array(aux_x)
    y = np.array(aux_y)
    return X,y

"""
Método encargado de recuperar los ejemplares de las tablas
    Returns:
        ejemplares: lista de ejemplares
"""
def recupera_ejemplares():
    # Consulta la base de datos
    resultados = consulta_db("SELECT * FROM registro_espectros")
    # Recupera los ejemplares
    ejemplares = []
    for resultado in resultados:
        ejemplar = []
        ejemplar.append(resultado[0])
        ejemplar.append(resultado[1])
        ejemplar.append(resultado[2])
        ejemplar.append(resultado[3])
        ejemplar.append(resultado[4])
        ejemplar.append(resultado[5])
        ejemplares.append(ejemplar)
    return ejemplares


# Recupera los espectros
"""
Método encargado de recuperar los espectros
    Returns:
        espectros: lista de espectros en formato DataFrame
"""
def recupera_espectros():
    ejemplares = recupera_ejemplares()
    espectros = []
    for ejemplar in ejemplares:
        carpeta = ejemplar[0]
        etiqueta = ejemplar[1]
        espectro = ejemplar[2]
        pigmento = ejemplar[3]
        aglutinante = ejemplar[4]
        base = ejemplar[5]
        df = get_df(carpeta,etiqueta,espectro)
        if df is None:
            continue
        # Crear el DataFrame
        dataframe = pd.DataFrame(columns=['wavelength','reflectance','pigmento','aglutinante','base','carpeta','tabla','espectro'])

        # Agrega los datos al DataFrame
        dataframe['wavelength'] = df['Wavelength']
        ext = espectro.split(".")[-1]
        if ext == "txt":
            nombre = espectro.replace("."+ext,"")
            dataframe['reflectance'] = df[nombre]
        elif ext == "asd":
            dataframe['reflectance'] = df['reflectance']
        dataframe['pigmento'] = pigmento
        dataframe['aglutinante'] = aglutinante
        dataframe['base'] = base
        dataframe['carpeta'] = carpeta
        dataframe['tabla'] = etiqueta
        dataframe['espectro'] = espectro
        # Recupera el DataFrame del espectro
        # Agrega el DataFrame a la lista de espectros
        espectros.append(dataframe)

    return espectros