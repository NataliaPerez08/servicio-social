from math import e
from matplotlib.pylab import f
import numpy as np
import tablas.carbonato1 as c1
import tablas.carbonato2 as c2
import tablas.carbonato3 as c3
import tablas.carbonato4 as c4
import tablas.carbonato5 as c5
import tablas.carbonato6 as c6
import tablas.carbonato7 as c7

import tablas.yeso1 as y1
#import tablas.yeso2 as y2
import tablas.yeso3 as y3
import tablas.yeso4 as y4
import tablas.yeso5 as y5
import tablas.yeso6 as y6
import tablas.yeso7 as y7

from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import Perceptron

from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier

#Para importar los modelos de evaluación
from joblib import dump
from sklearn.metrics import accuracy_score, classification_report, mean_squared_error, precision_score
from sklearn.metrics import r2_score
from sklearn.decomposition import PCA
# Import random forest model

# One hot encoding
from sklearn.preprocessing import MultiLabelBinarizer, LabelEncoder

# Import OS
import os

# Import pandas
import pandas as pd

def guardar_modelo(modelo,nombre,etiqueta_a_usar):
    print("Guardando el modelo")
    #carpeta = "Modelos/"+nombre
    #if not os.path.exists(carpeta):
    #    os.makedirs(carpeta) 
    #dump(modelo, carpeta+"/"+nombre+etiqueta_a_usar+".joblib")

# Función para obtener los datos de entrenamiento y prueba
def get_X_y_Tabla(ejemplares,etiqueta_a_usar):
    #etiqueta_a_usar = 'pigmento'
    aux_y = list()
    aux_x = list()
    #for ejemplar

    for ejemplar in ejemplares:
        for e in ejemplar:
            eti = str(e[etiqueta_a_usar][0])
            #if e[etiqueta_a_usar][0] not in clases:
            #    clases.append(eti)
            aux_y.append(eti)
            aux_x.append(e['reflectance'].to_numpy())

    encoder = MultiLabelBinarizer()
    y = encoder.fit_transform([aux_y,])
    y = encoder.fit([aux_y,])
    X = np.array(aux_x)
    y = np.array(aux_y)
    return X,y

# Función para obtener el modelo de Naive Bayes
def get_GNB(ejemplares,etiqueta_a_usar):
    X,y = get_X_y_Tabla(ejemplares,etiqueta_a_usar)
    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.2, random_state = 42)

    # Create Gaussian Naive Bayes object with prior probabilities of each label
    GNBclf = GaussianNB()
    # Train model
    model = GNBclf.fit(X_train, y_train)

    # Make predictions
    y_pred =  model.predict(X_test)

    # View accuracy score
    accuracy = accuracy_score(y_test, y_pred)
    print("Precisión del modelo:", accuracy)
    print(classification_report(y_test, y_pred, zero_division=0))

    print("Guardando el modelo")
    guardar_modelo(model,"GaussianNB",etiqueta_a_usar)

def get_linear_regression(ejemplares,etiqueta_a_usar):
    X,y = get_X_y_Tabla(ejemplares,etiqueta_a_usar)
    lb = LabelEncoder()
    y = lb.fit_transform(y)
    
    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.2, random_state = 42)

    # Create Linear Regression object
    LRclf = LinearRegression()
    # Train model
    model = LRclf.fit(X_train, y_train)

    # Make predictions
    y_pred =  model.predict(X_test)
    # View accuracy score
    accuracy = r2_score(y_test, y_pred)
    #accuracy = explained_variance_score(y_test, y_pred)
    print("Precisión del modelo:", accuracy)

    print("Guardando el modelo")
    guardar_modelo(model,"LinearRegression",etiqueta_a_usar)


def get_logistic_Regression(ejemplares,etiqueta_a_usar):
    X,y = get_X_y_Tabla(ejemplares,etiqueta_a_usar)
    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.2, random_state = 42)
    # Create Logistic Regression object
    LRclf = LogisticRegression(penalty='l2',solver='lbfgs', max_iter=10500)
    # Train model
    model = LRclf.fit(X_train, y_train)
    print("Numero de features: ",LRclf.n_features_in_)

    # Make predictions
    y_pred = model.predict(X_test)

    # View accuracy score
    accuracy = accuracy_score(y_test, y_pred)
    print("Precisión del modelo:", accuracy)
    print(precision_score(y_test, y_pred, average='macro', zero_division=0))

    print(classification_report(y_test, y_pred, zero_division=0))
    print("Guardando el modelo")
    guardar_modelo(model,"LogisticRegression",etiqueta_a_usar)

def get_perceptron(ejemplares,etiqueta_a_usar):
    X,y = get_X_y_Tabla(ejemplares,etiqueta_a_usar)

    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.2, random_state = 42)
   
    # Create Perceptron object
    Pclf = Perceptron()
    # Train model
    model = Pclf.fit(X_train, y_train)

    # Make predictions
    y_pred =  model.predict(X_test)

    # View accuracy score
    accuracy = accuracy_score(y_test, y_pred)
    print("Precisión del modelo:", accuracy)
    print(precision_score(y_test, y_pred, average='macro', zero_division=0))
    print(classification_report(y_test, y_pred, zero_division=0))
    print("Guardando el modelo")
    guardar_modelo(model,"Perceptron",etiqueta_a_usar)


def get_random_forest(ejemplares,etiqueta_a_usar):
    X,y = get_X_y_Tabla(ejemplares,etiqueta_a_usar)
    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.2, random_state = 42)

    # Create Random Forest object
    RFclf = RandomForestClassifier()
    # Train model
    model = RFclf.fit(X_train, y_train)

    # Make predictions
    y_pred =  model.predict(X_test)

    # View accuracy score
    accuracy = accuracy_score(y_test, y_pred)
    print("Precisión del modelo:", accuracy)
    print(precision_score(y_test, y_pred, average='macro', zero_division=0))

    print(classification_report(y_test, y_pred, zero_division=0))

    print("Guardando el modelo")
    guardar_modelo(model,"RandomForest",etiqueta_a_usar)


# Función para obtener el modelo de SVM Support Vector Machine  
def get_svc(ejemplares,etiqueta_a_usar):
    X,y = get_X_y_Tabla(ejemplares,etiqueta_a_usar)
    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.35, random_state = 42)

    # Create Support Vector Classification
    SVCclf = SVC()
    # Train model
    model = SVCclf.fit(X_train, y_train)
    # Make predictions
    y_pred =  model.predict(X_test)

    # View accuracy score
    accuracy = accuracy_score(y_test, y_pred)
    print("Precisión del modelo:", accuracy)
    print(precision_score(y_test, y_pred, average='macro', zero_division=0))

    print(classification_report(y_test, y_pred, zero_division=0))
    print("Guardando el modelo")
    guardar_modelo(model,"SVC",etiqueta_a_usar)

# Función que se encarda de recuperar los ejemplares de las tablas
def recupera_ejemplares():
    ejemplares_c1 = c1.obtener_carbonato_C1()
    ejemplares_c2 = c2.obtener_carbonato_C2()

    ejemplares_c3 = c3.obtener_carbonato_C3()
    ejemplares_c4 = c4.obtener_carbonato_C4()
    ejemplares_c5 = c5.obtener_carbonato_C5()
    ejemplares_c6 = c6.obtener_carbonato_C6()
    ejemplares_c7 = c7.obtener_carbonato_C7()

    ejemplares_y1 = y1.obtener_yeso_Y1()
    ejemplares_y3 = y3.obtener_yeso_Y3()
    ejemplares_y4 = y4.obtener_yeso_Y4()
    ejemplares_y5 = y5.obtener_yeso_Y5()
    ejemplares_y6 = y6.obtener_yeso_Y6()
    ejemplares_y7 = y7.obtener_yeso_Y7()

    ejemplares = ejemplares_c1+ejemplares_c2+ejemplares_c3+ejemplares_c4+ejemplares_c5+ejemplares_c6+ejemplares_c7+ejemplares_y1+ejemplares_y3+ejemplares_y5+ejemplares_y6+ejemplares_y4+ejemplares_y7

    return ejemplares

def aplicar_PCA(X,y):
    pca = PCA(n_components=200)
    pca.fit(X)
    X_pca = pca.transform(X)
    print("Original shape:   ", X.shape)
    print("Transformed shape:", X_pca.shape)
    return X_pca


def haz_pca_regresion_logistica(ejemplares,etiqueta_a_usar):
    X,y = get_X_y_Tabla(ejemplares,etiqueta_a_usar)
    X_pca = aplicar_PCA(X,y)

    X_train, X_test, y_train, y_test = train_test_split(X_pca,y,test_size = 0.35, random_state = 42)
    # Create Logistic Regression object
    LRclf = LogisticRegression(penalty='l2',solver='lbfgs', max_iter=10500)
    # Train model
    model = LRclf.fit(X_train, y_train)
    print("Numero de features: ",LRclf.n_features_in_)
    # Make predictions
    y_pred = model.predict(X_test)

    # View accuracy score
    accuracy = accuracy_score(y_test, y_pred)
    print("Precisión del modelo:", accuracy)
    print(precision_score(y_test, y_pred, average='macro', zero_division=0))

    print(classification_report(y_test, y_pred, zero_division=0))
    print("Guardando el modelo")
    guardar_modelo(model,"LogisticRegressionPCA",etiqueta_a_usar)



if __name__ == "__main__":
    ejemplares = recupera_ejemplares()

    """
    print("Perceptron")
    print('Pigmento')
    get_perceptron(ejemplares, 'pigmento')
    print('Aglutinante')
    get_perceptron(ejemplares, 'aglutinante')

    print("Naive Bayes")
    print('Pigmento')
    get_GNB(ejemplares, 'pigmento')
    print('Aglutinante')
    get_GNB(ejemplares, 'aglutinante')

    print("Linear Regression")
    print('Pigmento')
    get_linear_regression(ejemplares, 'pigmento')
    print('Aglutinante')
    get_linear_regression(ejemplares, 'aglutinante')


    print("Logistic Regression")
    print('Pigmento')
    get_logistic_Regression(ejemplares, 'pigmento')
    print('Aglutinante')
    get_logistic_Regression(ejemplares, 'aglutinante')
    
    print("Random Forest")
    print('Pigmento')
    get_random_forest(ejemplares, 'pigmento')
    print('Aglutinante')
    get_random_forest(ejemplares, 'aglutinante')

    print("SVM")
    print('Pigmento')
    get_svc(ejemplares, 'pigmento')
    print('Aglutinante')
    get_svc(ejemplares, 'aglutinante')
    """
    print("Logistic Regression")
    #print('Pigmento')
    #get_logistic_Regression(ejemplares, 'pigmento')
    print('Aglutinante')
    get_logistic_Regression(ejemplares, 'aglutinante')
    
    print("Despues de aplicar PCA")
    #print('Pigmento')
    #haz_pca_regresion_logistica(ejemplares, 'pigmento')
    print('Aglutinante')
    haz_pca_regresion_logistica(ejemplares, 'aglutinante')
   

