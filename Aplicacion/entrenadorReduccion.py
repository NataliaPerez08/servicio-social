from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, classification_report
from entrenador import guardar_modelo
from control_entrenador import get_x_y, recupera_ejemplares, recupera_espectros

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

    return model,accuracy

etiqueta_a_usar = 'pigmento'
# Recupera los ejemplares
ejemplares = recupera_espectros()

no_ejem = len(ejemplares)

# Maxima accuracy
max_accuracy = 0
# Numero de componentes 
max_componentes = 0

for i in range(200,no_ejem,10):
    X,y = get_x_y(ejemplares,etiqueta_a_usar)
    model,accuracy = haz_pca_regresion_logistica(X,y,i,etiqueta_a_usar)
    if accuracy > max_accuracy:
        max_accuracy = accuracy
        max_componentes = i

print("Maxima accuracy: ",max_accuracy)
print("Numero de componentes: ",max_componentes)
# Guardar el modelo
guardar_modelo(model,"./ModelosPCAs/LogisticRegression/LogisticRegressionpigmento.joblib")

etiqueta_a_usar = 'aglutinante'
# Recupera los ejemplares
ejemplares = recupera_espectros()

# Maxima accuracy
max_accuracy = 0
# Numero de componentes
max_componentes = 0

for i in range(200,no_ejem,step=10):
    X,y = get_x_y(ejemplares,etiqueta_a_usar)
    model,accuracy = haz_pca_regresion_logistica(X,y,i,etiqueta_a_usar)
    if accuracy > max_accuracy:
        max_accuracy = accuracy
        max_componentes = i

print("Maxima accuracy: ",max_accuracy)
print("Numero de componentes: ",max_componentes)
# Guardar el modelo
guardar_modelo(model,"./ModelosPCAs/LogisticRegression/LogisticRegressionaglutinante.joblib")
