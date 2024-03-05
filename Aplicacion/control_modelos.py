"""
Este módulo se encarga de hacer la predicción con los modelos de clasificación
"""

# Para importar los modelos de evaluación
from joblib import  load

# Para importar los datos para hacer predicciones
import recoverRegister as rr

def extraer_modelo(path):
    """ 
    Método encargado de cargar el modelo en la ruta especificada    
        @args: path: ruta del modelo a cargar
        @return: modelo cargado 
    """
    modelo = load(path)
    return modelo

def obtener_X(ruta):
    """
    Método encargado de obtener el espectro a predecir
        @args: ruta: ruta del espectro a predecir
        @return: espectro a predecir
    """
    # verificar si es un archivo txt o asd
    ext = ruta.split(".")[-1]
    if ext == "txt":
        df = rr.create_df_from_txt(ruta)
    elif ext == "asd":
        df = rr.get_df_from_asd(ruta)
    else:
        print("Error")
    # Extraer la columna de reflectancia
    X = df['reflectance'].to_numpy()
    return X

def haz_prediccion_regresion_logistica(ruta_predecir):
    """
    Método encargado de hacer la predicción con el modelo de regresión logística
        @args: ruta_predecir: ruta del espectro a predecir
        @return: mensaje con la predicción
    """
    mensaje = "\nHaciendo predicción con regresión logística"
    # Cambiar el path del espectro para pigmento
    path = "../Modelos/LogisticRegression/LogisticRegressionpigmento.joblib"
    modelo1 = extraer_modelo(path)

    # Cambiar el path del modelo para aglutinante
    path = "../Modelos/LogisticRegression/LogisticRegressionaglutinante.joblib"
    modelo2 = extraer_modelo(path)
    
    X=obtener_X(ruta_predecir)
    pred_pigmento = modelo1.predict([X,])
    mensaje += "\nPredicción de  pigmento:"+str(pred_pigmento)
  
    pred_aglutinante = modelo2.predict([X,])
    mensaje += "\nPredicción de aglutinante: "+str(pred_aglutinante)
    
    return mensaje
def haz_prediccion_perceptron(ruta_predecir):
    """
    Método encargado de hacer la predicción con el modelo de perceptron
       @args: ruta_predecir: ruta del espectro a predecir
       @return: mensaje con la predicción
    """
    mensaje = "\nHaciendo predicción con perceptron"
    #print("\nHaciendo predicción con perceptron")
    # Cambiar el path del espectro para pigmento
    path = "../Modelos/Perceptron/Perceptronpigmento.joblib"
    modelo1 = extraer_modelo(path)
    # Cambiar el path del modelo para aglutinante
    path = "../Modelos/Perceptron/Perceptronaglutinante.joblib"
    modelo2 = extraer_modelo(path)

    X=obtener_X(ruta_predecir)
    pred_pigmento = modelo1.predict([X,])
    mensaje += "\nPredicción de  pigmento:"+str(pred_pigmento)
    #print("Predicción de  pigmento:",pred_pigmento)
  
    pred_aglutinante = modelo2.predict([X,])
    mensaje += "\nPredicción de aglutinante: "+str(pred_aglutinante)
    #print("Predicción de aglutinante: ",pred_aglutinante)

    return mensaje

def haz_prediccion_regresion_lineal(ruta_predecir):
    """
    Método encargado de hacer la predicción con el modelo de regresión lineal
        @args: ruta_predecir: ruta del espectro a predecir
        @return: mensaje con la predicción
    """
    mensaje = "\nHaciendo predicción con regresión lineal"

    # Cambiar el path del espectro para pigmento
    path = "../Modelos/LogisticRegression/LogisticRegressionpigmento.joblib"
    modelo1 = extraer_modelo(path)

    # Cambiar el path del modelo para aglutinante
    path = "../Modelos/LogisticRegression/LogisticRegressionaglutinante.joblib"
    modelo2 = extraer_modelo(path)

    X=obtener_X(ruta_predecir)

    pred_pigmento = modelo1.predict([X,])
    mensaje += "\nPredicción de  pigmento:"+str(pred_pigmento)
  
    pred_aglutinante = modelo2.predict([X,])
    mensaje += "\nPredicción de aglutinante: "+str(pred_aglutinante)

    return mensaje
def haz_prediccion_GaussianNB(ruta_predecir):
    """
    Método encargado de hacer la predicción con el modelo de Gaussian Naive Bayes
        @args: ruta_predecir: ruta del espectro a predecir
        @return: mensaje con la predicción
    """
    mensaje = "\nHaciendo predicción con GaussianNB"

    # Cambiar el path del espectro para pigmento
    path = "../Modelos/GaussianNB/GaussianNBpigmento.joblib"
    modelo1 = extraer_modelo(path)

    # Cambiar el path del modelo para aglutinante
    path = "../Modelos/GaussianNB/GaussianNBaglutinante.joblib"
    modelo2 = extraer_modelo(path)

    X=obtener_X(ruta_predecir)

    pred_pigmento = modelo1.predict([X,])
    mensaje += "\nPredicción de  pigmento:"+str(pred_pigmento)

    pred_aglutinante = modelo2.predict([X,])
    mensaje += "\nPredicción de aglutinante: "+str(pred_aglutinante)

    return mensaje

def haz_prediccion_SVC(ruta_predecir):
    """
    Método encargado de hacer la predicción con el modelo de C-Support Vector Classification.
        @args: ruta_predecir: ruta del espectro a predecir
        @return: mensaje con la predicción
    """
    mensaje = "\nHaciendo predicción con SVC"

    # Cambiar el path del espectro para pigmento
    path = "../Modelos/SVC/SVCpigmento.joblib"
    modelo1 = extraer_modelo(path)

    # Cambiar el path del modelo para aglutinante
    path = "../Modelos/SVC/SVCaglutinante.joblib"
    modelo2 = extraer_modelo(path)

    X=obtener_X(ruta_predecir)

    pred_pigmento = modelo1.predict([X,])
    mensaje += "\nPredicción de  pigmento:"+str(pred_pigmento)

    pred_aglutinante = modelo2.predict([X,])
    mensaje += "\nPredicción de aglutinante: "+str(pred_aglutinante)

    return mensaje

def haz_prediccion_RandomForest(ruta_predecir):
    """
    Método encargado de hacer la predicción con el modelo de Random Forest Classifier
        @args: ruta_predecir: ruta del espectro a predecir
        @return: mensaje con la predicción
    """
    mensaje = "\nHaciendo predicción con RandomForest"

    # Cambiar el path del espectro para pigmento
    path = "../Modelos/RandomForest/RandomForestpigmento.joblib"
    modelo1 = extraer_modelo(path)

    # Cambiar el path del modelo para aglutinante
    path = "../Modelos/RandomForest/RandomForestaglutinante.joblib"
    modelo2 = extraer_modelo(path)

    X=obtener_X(ruta_predecir)

    pred_pigmento = modelo1.predict([X,])
    mensaje += "\nPredicción de  pigmento:"+str(pred_pigmento)

    pred_aglutinante = modelo2.predict([X,])
    mensaje += "\nPredicción de aglutinante: "+str(pred_aglutinante)

    return mensaje
