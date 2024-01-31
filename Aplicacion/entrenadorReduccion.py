from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, classification_report
from entrenador import guardar_modelo

# Conexion a la base de datos
from connectDB import consulta_db

# Función para imprimir
from print_specs_control import print_spec_from_ruta

# Función que se encarga de realizar la reducción de dimensionalidad y la regresión logística
def haz_pca_regresion_logistica(X,y,componentes: int,etiqueta_a_usar):
    pca = PCA(n_components=componentes)
    pca.fit(X)
    X_pca = pca.transform(X)

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

# Función que se encarda de recuperar los ejemplares de las tablas
def recupera_ejemplares():
    # Consulta la base de datos
    resultados = consulta_db("SELECT * FROM registro_espectros WHERE Carpeta LIKE 'Tablas2'")
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

print("Recuperando espectros")
ejemplares = recupera_ejemplares()
# Recupera los espectros
espectros = []
for ejemplar in ejemplares:
    print("Ejemplar: ",ejemplar[0])
    # Contruye la ruta del espectro
    carpeta = ejemplar[0]
    etiqueta = ejemplar[1]
    espectro = ejemplar[2]
    ruta = "Espectros_FORS_2/"+carpeta+"/"+etiqueta+"/"+espectro
    # Lee el espectro
    print(ruta)
    pigmento = ejemplar[3]
    aglutinante = ejemplar[4]
    base = ejemplar[5]
    print_spec_from_ruta(ruta,pigmento+" "+aglutinante+" "+base)
    
