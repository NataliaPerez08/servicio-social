class Spec:
    # Carbonato/Yeso de la forma Y1 o C1
    base="" 
    # Etiqueta de la forma A1,A2
    etiqueta=""
    pigmento=""
    marca=""#Marca o molido:
    numero=0
    aglutinado=""
    mezcla=""
    notas=""
    
capas = list()

print("Base: ")
base=input()

print("Etiqueta: ")
etiqueta=input()

print("Pigmento: ")
pigmento=input()

print("Marca o molido: ")
marca=input()

print("Numero (si no aplica colocar 'No'): ")
numero=input()

print("Aglutinado (si no aplica colocar 'No'): ")
aglutinado=input()

print("Mezcla (si no aplica colocar 'No'): ")
mezcla=input()

print("Notas: ")
notas=input()