import csv
class Spec:
    # Carbonato/Yeso de la forma Y1 o C1
    base="" 
    # Etiqueta de la forma A1,A2
    etiqueta=""
    pigmento=""
    marca=""#Marca o molido:
    numero=""
    aglutinado=""
    mezcla=""
    notas=""
    ruta=""
    #tmp_spec=Spec(base,etiqueta,pigmento,marca,numero,aglutinado,mezcla,notas,ruta)
    def __init__(self,base,etiqueta,pigmento,marca,numero,aglutinado,mezcla,notas,ruta):
        self.base=base 
        self.etiqueta=etiqueta
        self.pigmento=pigmento
        self.marca=marca
        self.numero=numero
        self.aglutinado=aglutinado
        self.mezcla=mezcla
        self.notas=notas
        self.ruta=ruta
    def __str__(self):
        return self.base+","+self.etiqueta+","+self.pigmento+","+self.marca+","+self.numero+","+self.aglutinado+","+self.mezcla+","+self.notas+","+self.ruta
    
capas = list()
print("1. Para ingresar más datos, 2.Para salir")
opt=int(input())
while opt==1:
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

    print("Ruta relativa: ")
    ruta=input()

    tmp_spec = {'Base': base, 'Etiqueta':etiqueta,'Pigmento':pigmento,'Marca':marca,'Numero':numero,'Aglutinado':aglutinado,'Mezcla':mezcla,'Notas':notas,'Ruta':ruta}

    print("1. Para ingresar más datos, 2.Para salir")
    opt=input()

    capas.append(tmp_spec)

with open('pr.csv', 'a') as csvfile:
    fieldnames = ['Base','Etiqueta','Pigmento','Marca','Numero','Aglutinado','Mezcla','Notas','Ruta']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    #writer.writeheader()

    for sp in capas:
        writer.writerow(sp)
