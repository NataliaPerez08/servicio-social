import numpy as np
import carbonatos.carbonato1 as c1
import carbonatos.carbonato2 as c2
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB


feature_names = ['wavelength','reflectance','pigmento','aglutinante','base','path','carpeta','tabla','espectro']

ejemplares_c1 = c1.obtener_carbonato_C1()
#ejemplares_c2 = c2.contenar_c2()

#train, test=train_test_split(ejemplares_c1, test_size=0.3, random_state=0)

#train, test, train_labels, test_labels = train_test_split(
#   features,labels,test_size = 1, random_state = 22
#)
#X = [e['reflectance'] for e in ejemplares_c1]

def crear_labels(ejemplares):
    labels = set()
    for e in ejemplares:
        aux0 = e['pigmento'].iat[0]
        aux1 = e['aglutinante'].iat[0]
        aux2 = e['base'].iat[0]
        aux = (aux0,aux1,aux2)
        labels.add(aux)
    return labels

def encode_labels(label_names):
    label_names = list(label_names)
    label_names.sort()
    label_names = dict(zip(label_names,range(len(label_names))))
    return label_names

def obtener_features(ejemplares):
    features = list()
    for e in ejemplares:
        aux0 = e['wavelength'].to_numpy()
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

#features = obtener_features(ejemplares_c1[0])
#labels = crear_labels(ejemplares_c1[0])
#labels = encode_labels(labels)
#print(labels.values())


# Obtener features de TODOS los ejemplares
features = obtener_features(ejemplares_c1[0]) 

# Obtener etiquetas sin codificar de TODOS los ejemplares
get_labels = obtener_labels(ejemplares_c1[0])

# Codificación de las etiquetas
enco = encode_labels(get_labels)
y = etiquetar_ejemplares(enco,ejemplares_c1[0])
y = np.array(y)
X = np.array(features)

print(X.shape)
print(y.shape)


# Create Gaussian Naive Bayes object with prior probabilities of each
# label
gnb = GaussianNB(priors=None)
# Train model
model = gnb.fit(X, y)

train,test = train_test_split(X, y, test_size=0.3, random_state=0)


# Make predictions
preds = gnb.predict(train)
print(preds)

# Evaluate accuracy
print(np.mean(preds == y))

