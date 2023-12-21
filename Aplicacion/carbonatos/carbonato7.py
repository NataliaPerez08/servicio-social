import os
from matplotlib.pylab import f
import recoverRegister as rr
import pandas as pd
"""
Pigmentos:
(Tabla 1)
Ocre de	mina inglés	(C7: A1)
Rejalgar (C7: A2)
Amarillo de plomo estaño (C7: A3)
Gualda (C7: A4)	
Arzica (C7: A5)

Pardo antílope (C7:B1)
Sombra tostada (C7:B2)
Ocre oscuro	(C7:B3)
Tierra de siena tostada	(C7:B4)
Betún de Judea (C7:B5)

Cinabrio. Kremer (C7:C1)
Almagre (C7:C2)
Minio	(C7:C3)
Laca carmín	(C7:C4)
Carmín de alizarina (C7:C5)

Laca rubia  (C7:D1)
Azurita	natural. Kremer	(C7:D2)
Esmalte	(C7:D3)
Lapislázuli	(C7:D4)
Azul añil (C7:D5)

Resinato de	cobre (C7:E1)
Malaquita	(C7:E2)
Tierra verde de	bohemia	(C7:E3)
Negro marfil o de huesos (C7:E4)
Negro de vid francés (C7:E5)

Carpeta,Tabla,Espectro,Pigmento,Aglutinante,Base de preparación
"""

def obtener_carbonato_C6_tablas_2():
    # Info de Tabla 2
    dir = "Espectros_FORS_2/Tablas 2/Tabla_C6"
    archivos=list()
    for f in os.listdir(dir):
        archivos.append(dir+"/"+f)
    archivos.sort()
    
    tmp = archivos[0:5]
    
    tmp = archivos[5:10]
    tmp = archivos[10:15]
    tmp = archivos[15:20]
    tmp = archivos[20:25]

