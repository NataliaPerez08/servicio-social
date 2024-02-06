from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import Perceptron

from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC

#Para importar los modelos de evaluación
from joblib import dump
from sklearn.metrics import accuracy_score, classification_report, mean_squared_error, precision_score
from sklearn.metrics import r2_score
from sklearn.decomposition import PCA

# One hot encoding
from sklearn.preprocessing import MultiLabelBinarizer, LabelEncoder
import os

from control_entrenador import get_x_y,recupera_espectros

GUARDANDO_MODELO_MSG = "Guardando el modelo"

def guardar_modelo(modelo,nombre,etiqueta_a_usar):
    print(GUARDANDO_MODELO_MSG)
    carpeta = "Modelos/"+nombre
    if not os.path.exists(carpeta):
        os.makedirs(carpeta) 
    dump(modelo, carpeta+"/"+nombre+etiqueta_a_usar+".joblib")

# Función para obtener el modelo de Naive Bayes
def get_GNB(ejemplares,etiqueta_a_usar):
    X,y = get_x_y(ejemplares,etiqueta_a_usar)
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
    X,y = get_x_y(ejemplares,etiqueta_a_usar)
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
    X,y = get_x_y(ejemplares,etiqueta_a_usar)
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
    X,y = get_x_y(ejemplares,etiqueta_a_usar)

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
    X,y = get_x_y(ejemplares,etiqueta_a_usar)
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
    X,y = get_x_y(ejemplares,etiqueta_a_usar)
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

def aplicar_PCA(X,y):
    pca = PCA(n_components=200)
    pca.fit(X)
    X_pca = pca.transform(X)
    print("Original shape:   ", X.shape)
    print("Transformed shape:", X_pca.shape)
    return X_pca


def haz_pca_regresion_logistica(ejemplares,etiqueta_a_usar):
    X,y = get_x_y(ejemplares,etiqueta_a_usar)
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


def realizar_entrenamiento():
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


    print("Logistic Regression")
    print('Pigmento')
    get_logistic_Regression(ejemplares, 'pigmento')
    print('Aglutinante')
    get_logistic_Regression(ejemplares, 'aglutinante')

if __name__ == "__main__":
    print("Entrenando modelos")
    #ejemplares = recupera_espectros()
    #realizar_entrenamiento()
    #print("Entrenamiento terminado")

