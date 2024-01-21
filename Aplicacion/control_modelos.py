# pandas
import pandas as pd

#Para importar los modelos de evaluación
from joblib import  load
from sklearn.metrics import accuracy_score, classification_report, precision_score
from sklearn.metrics import explained_variance_score

# Para importar los datos para hacer predicciones
import recoverRegister as rr

# Desde ml.py
from ml import obtener_ejemplares_X_y

def extraer_modelo(path):
    modelo = load(path)
    return modelo

def evaluar_modelo(modelo,X,y):
    y_pred = modelo.predict(X)
    print("Accuracy: ",accuracy_score(y,y_pred))
    print("Precision: ",precision_score(y,y_pred,average='macro'))
    print("Reporte de clasificación: \n",classification_report(y,y_pred))
    print("Varianza explicada: ",explained_variance_score(y,y_pred))
    return y_pred

def obtener_X(ruta):
    ext = ruta.split(".")[-1]
    if ext == "txt":
        print("txt")
        df = rr.create_df_from_txt(ruta)
    elif ext == "asd":
        print("asd")
        df = rr.get_df_from_asd(ruta)
    else:
        print("Error")
    X = df['reflectance'].to_numpy()
    return X

path = "./modeloRF.joblib"
modelo = extraer_modelo(path)
#X,y = obtener_ejemplares_X_y()
#evaluar_modelo(modelo,X,y)

path2="reflexion/Echave.001.txt"
path = "Espectros_FORS_2\Tablas 1\C1\A100000.asd"

X=obtener_X(path)

print("Predicción: ",modelo.predict([X,]))   