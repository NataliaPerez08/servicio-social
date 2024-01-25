#Para importar los modelos de evaluación
import encodings
from os import error
from joblib import  load
from sklearn.metrics import accuracy_score, classification_report, precision_score
from sklearn.metrics import explained_variance_score


# Para importar los datos para hacer predicciones
import recoverRegister as rr

def extraer_modelo(path):
    modelo = load(path)
    return modelo

def extraer_labels(path):
    # Crear diccionario de labels
    d_labels = {}
    with open(path,errors='replace') as f:
        #labels = f.readlines()
        labels = f.readlines()
    
    for label in labels:
        tmp_dic = eval(label)
        d_labels.update(tmp_dic)
        
    return d_labels

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
        df = rr.create_df_from_txt(ruta)
    elif ext == "asd":
        df = rr.get_df_from_asd(ruta)
    else:
        print("Error")
    X = df['reflectance'].to_numpy()
    return X

def haz_prediccion_ejemplo():
    path_modelo = "./Modelos/modeloRF/modeloRF.joblib"
    modelo = extraer_modelo(path_modelo)

    path_labels = "./Modelos/modeloRF/labels/modeloRF_labels.txt"
    labels = extraer_labels(path_labels)


    print("Modelo: ",modelo)
    #print("Labels: ",labels)

    #X,y = obtener_ejemplares_X_y()
    #evaluar_modelo(modelo,X,y)

    path2="reflexion/Echave.001.txt"
    path = "Espectros_FORS_2/Tablas 1/C1/A100000.asd"

    X=obtener_X(path)
    pred = modelo.predict([X,])
    print("Predicción: ",modelo.predict([X,]))   

    # Buscar valores en el diccionario
    for key, value in labels.items():
        if value == pred[0]:
            print("Label: ",key)
            break

def haz_prediccion_regresion_logistica(ruta_predecir):
    print("\nHaciendo predicción con regresión logística")
    # Cambiar el path del espectro para pigmento
    path = "./Modelos/LogisticRegression/LogisticRegressionpigmento.joblib"
    modelo1 = extraer_modelo(path)

    # Cambiar el path del modelo para aglutinante
    path = "./Modelos/LogisticRegression/LogisticRegressionaglutinante.joblib"
    modelo2 = extraer_modelo(path)
    
    X=obtener_X(ruta_predecir)

    pred_pigmento = modelo1.predict([X,])
    print("Predicción de  pigmento:",pred_pigmento)
  
    pred_aglutinante = modelo2.predict([X,])
    print("Predicción de aglutinante: ",pred_aglutinante)

def haz_prediccion_perceptron(ruta_predecir):
    print("\nHaciendo predicción con perceptron")
    # Cambiar el path del espectro para pigmento
    path = "./Modelos/Perceptron/Perceptronpigmento.joblib"
    modelo1 = extraer_modelo(path)
    # Cambiar el path del modelo para aglutinante
    path = "./Modelos/Perceptron/Perceptronaglutinante.joblib"
    modelo2 = extraer_modelo(path)

    X=obtener_X(ruta_predecir)
    pred_pigmento = modelo1.predict([X,])
    print("Predicción de  pigmento:",pred_pigmento)
  
    pred_aglutinante = modelo2.predict([X,])
    print("Predicción de aglutinante: ",pred_aglutinante)

def haz_prediccion_regresion_lineal(ruta_predecir):
    print("\nHaciendo predicción con regresión lineal")
    # Cambiar el path del espectro para pigmento
    path = "Modelos/LogisticRegression/LogisticRegressionpigmento.joblib"
    modelo1 = extraer_modelo(path)

    # Cambiar el path del modelo para aglutinante
    path = "Modelos/LogisticRegression/LogisticRegressionaglutinante.joblib"
    modelo2 = extraer_modelo(path)

    X=obtener_X(ruta_predecir)

    pred_pigmento = modelo1.predict([X,])
    print("Predicción de  pigmento:",pred_pigmento)
  
    pred_aglutinante = modelo2.predict([X,])
    print("Predicción de aglutinante: ",pred_aglutinante)

def haz_prediccion_GaussianNB(ruta_predecir):
    print("\nHaciendo predicción con GaussianNB")
    # Cambiar el path del espectro para pigmento
    path = "Modelos/GaussianNB/GaussianNBpigmento.joblib"
    modelo1 = extraer_modelo(path)

    # Cambiar el path del modelo para aglutinante
    path = "Modelos/GaussianNB/GaussianNBaglutinante.joblib"
    modelo2 = extraer_modelo(path)

    X=obtener_X(ruta_predecir)

    pred_pigmento = modelo1.predict([X,])
    print("Predicción de  pigmento:",pred_pigmento)

    pred_aglutinante = modelo2.predict([X,])
    print("Predicción de aglutinante: ",pred_aglutinante)

def haz_prediccion_SVC(ruta_predecir):
    print("\nHaciendo predicción con SVC")
    # Cambiar el path del espectro para pigmento
    path = "Modelos/SVC/SVCpigmento.joblib"
    modelo1 = extraer_modelo(path)

    # Cambiar el path del modelo para aglutinante
    path = "Modelos/SVC/SVCaglutinante.joblib"
    modelo2 = extraer_modelo(path)

    X=obtener_X(ruta_predecir)

    pred_pigmento = modelo1.predict([X,])
    print("Predicción de  pigmento:",pred_pigmento)

    pred_aglutinante = modelo2.predict([X,])
    print("Predicción de aglutinante: ",pred_aglutinante)

def haz_prediccion_RandomForest(ruta_predecir):
    print("'\nHaciendo predicción con RandomForest")
    # Cambiar el path del espectro para pigmento
    path = "Modelos/RandomForest/RandomForestpigmento.joblib"
    modelo1 = extraer_modelo(path)

    # Cambiar el path del modelo para aglutinante
    path = "Modelos/RandomForest/RandomForestaglutinante.joblib"
    modelo2 = extraer_modelo(path)

    X=obtener_X(ruta_predecir)

    pred_pigmento = modelo1.predict([X,])
    print("Predicción de  pigmento:",pred_pigmento)

    pred_aglutinante = modelo2.predict([X,])
    print("Predicción de aglutinante: ",pred_aglutinante)


if __name__ == "__main__":
    ruta_predecir = "Espectros_FORS_2/Tablas 1/Y1/A100003.asd"
    #path2="reflexion/Echave.001.txt"
    #ruta_predecir = path2
    print(ruta_predecir)
    haz_prediccion_ejemplo()
    haz_prediccion_GaussianNB(ruta_predecir)
    haz_prediccion_regresion_lineal(ruta_predecir)
    haz_prediccion_regresion_logistica(ruta_predecir)
    haz_prediccion_RandomForest(ruta_predecir)
    haz_prediccion_SVC(ruta_predecir)
    haz_prediccion_perceptron(ruta_predecir)
