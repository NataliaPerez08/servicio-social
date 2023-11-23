import controlSpec,recoverRegister
import os
# Path: modelos_all_tables.py

# Obtener de la Tabla1 los espectro y etiquetar
pigmentos_t1 = ["Ocre de mina inglés (marca KremerR, n. 40191)", "Oropimente (molido en el LDOA)","Amarillo de plomo estaño (tipo II, marca KremerR, n. 10120)","Ancorca (marca SennelierR, Reseda luteola, sp.)","Ancorca o gualda (marca ZecchiR, Reseda luteola, sp.)"]

# Etiquetar los espectros con el mismo pigmento
# Ocre de mina inglés (marca KremerR, n. 40191) (C1: A1-A5) (C7:A1) (Y1:A1-A5) (Y4:A1)
# (C1: A1-A5)
Ocre_files=list()
dir = "Espectros_FORS_2/Tablas 1/C1/"
for spec in os.listdir(dir):
    if spec[0] =='A':
        Ocre_files.append(dir+spec)

for spec in Ocre_files:
    print(spec)
    #controlSpec.imprimir_spec('Tablas1','C1',spec)
#controlSpec.obten_spec('Tablas1','C1','A1.txt')

# (C7:A1)
# (Y1:A1-A5)
# (Y4:A1)

