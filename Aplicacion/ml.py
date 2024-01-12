from math import e
import numpy as np
import tablas.carbonato1 as c1
import tablas.carbonato2 as c2
import tablas.carbonato3 as c3
import tablas.carbonato4 as c4
import tablas.carbonato5 as c5
import tablas.carbonato6 as c6
import tablas.carbonato7 as c7

import tablas.yeso1 as y1
import tablas.yeso2 as y2
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

from sklearn.metrics import accuracy_score, classification_report, precision_score
from sklearn.metrics import explained_variance_score
from sklearn.decomposition import PCA
# Import random forest model
from sklearn.ensemble import RandomForestClassifier


def encode_labels(label_names):
    label_names = list(label_names)
    label_names.sort()
    label_names = dict(zip(label_names,range(len(label_names))))
    return label_names

def obtener_features(ejemplares):
    features = list()
    for e in ejemplares:
        #aux0 = e['wavelength'].to_numpy()
        aux = e['reflectance'].to_numpy()
        #aux = np.stack((aux0,aux1),axis=1)
        features.append(aux)
    return features

def obtener_labels(ejemplares):
    labels = []
    for e in ejemplares:
        aux0 = e['pigmento'].iat[0]
        aux1 = e['aglutinante'].iat[0]
        aux2 = e['base'].iat[0]
        aux = (aux0,aux1,aux2)
        labels.append(aux)
    return labels

def etiquetar_ejemplares(labels,ejemplares):
    # lista de labels de los ejemplares de la forma [0,0,0,0,0,2,2,2,5,5,]
    y = []
    for e in ejemplares:
        aux0 = e['pigmento'].iat[0]
        aux1 = e['aglutinante'].iat[0]
        aux2 = e['base'].iat[0]
        aux = (aux0,aux1,aux2)
        if aux in labels:
            #print("Codigo: ",labels[aux], " Label: ",aux)
            y.append(labels[aux])
    return y

# Función para obtener los datos de entrenamiento y prueba
def get_X_y_Tabla(ejemplares):
    X = np.array([])
    y = np.array([])
    for l in ejemplares:
        features = obtener_features(l) 
        # Obtener etiquetas sin codificar de TODOS los ejemplares
        get_labels = obtener_labels(l)

        # Codificación de las etiquetas
        enco = encode_labels(get_labels)
        y_tmp = etiquetar_ejemplares(enco,l)
        if X.size == 0:
            y = np.array(y_tmp)
            X = np.array(features)
        y = np.concatenate((y,y_tmp),axis=0)
        X = np.concatenate((X,features),axis=0)
    return X,y

# Función para obtener el modelo de Naive Bayes
def get_GNB(ejemplares):
    X,y = get_X_y_Tabla(ejemplares)
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

def get_linear_regression(ejemplares):
    X,y = get_X_y_Tabla(ejemplares)
    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.2, random_state = 42)

    # Create Linear Regression object
    LRclf = LinearRegression()
    # Train model
    model = LRclf.fit(X_train, y_train)

    # Make predictions
    y_pred =  model.predict(X_test)


    # View accuracy score
    accuracy = explained_variance_score(y_test, y_pred)
    print("Precisión del modelo:", accuracy)


def get_logistic_Regression(ejemplares):
    X,y = get_X_y_Tabla(ejemplares)
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

def get_perceptron(ejemplares):
    X,y = get_X_y_Tabla(ejemplares)
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

def get_random_forest(ejemplares):
    X,y = get_X_y_Tabla(ejemplares)
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

if __name__ == "__main__":
    feature_names = ['wavelength','reflectance','pigmento','aglutinante','base','path','carpeta','tabla','espectro']

    ejemplares_c1 = c1.obtener_carbonato_C1()
    ejemplares_c2 = c2.obtener_carbonato_C2()
    
 
    ejemplares_c3 = c3.obtener_carbonato_C3()
    ejemplares_c4 = c4.obtener_carbonato_C4()
    ejemplares_c5 = c5.obtener_carbonato_C5()
    ejemplares_c6 = c6.obtener_carbonato_C6()
    ejemplares_c7 = c7.obtener_carbonato_C7()


    """
    ejemplares_y1 = y1.obtener_yeso_Y1()
    ejemplares_y2 = y2.obtener_yeso_Y2()
    ejemplares_y3 = y3.obtener_yeso_Y3()
    ejemplares_y4 = y4.obtener_yeso_Y4()
    ejemplares_y5 = y5.obtener_yeso_Y5()
    ejemplares_y6 = y6.obtener_yeso_Y6()
    ejemplares_y7 = y7.obtener_yeso_Y7()
    """

    #ejemplares = ejemplares_c1+ejemplares_c2+ejemplares_c3+ejemplares_c4+ejemplares_c5+ejemplares_c6+ejemplares_c7#+ejemplares_y1+ejemplares_y2+ejemplares_y3+ejemplares_y4+ejemplares_y5+ejemplares_y6+ejemplares_y7

    #print("Perceptron")
    #get_perceptron(ejemplares)

    #print("Logistic Regression")
    #get_logistic_Regression(ejemplares)

    #print("Linear Regression")
    #get_linear_regression(ejemplares)

    #print("Naive Bayes")
    #get_GNB(ejemplares)

    print("Random Forest")
    ejemplares = ejemplares_c1
    get_random_forest(ejemplares)
