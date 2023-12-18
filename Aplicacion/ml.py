import numpy as np
import carbonatos.carbonato1 as c1
import carbonatos.carbonato2 as c2
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB


feature_names = ['wavelength','reflectance','pigmento','aglutinante','base','path','carpeta','tabla','espectro']

ejemplares_c1 = c1.contenar_c1()
#ejemplares_c2 = c2.contenar_c2()

#train, test=train_test_split(ejemplares_c1, test_size=0.3, random_state=0)

#train, test, train_labels, test_labels = train_test_split(
#   features,labels,test_size = 1, random_state = 22
#)
#X = [e['reflectance'] for e in ejemplares_c1]

def obtener_labels(ejemplares):
    labels = set()
    for e in ejemplares:
        aux0 = e['pigmento'].iat[0]
        aux1 = e['aglutinante'].iat[0]
        aux2 = e['base'].iat[0]
        aux = (aux0,aux1,aux2)
        labels.add(aux)
    return labels

labels = obtener_labels(ejemplares_c1)
for l in labels:
    print(l)