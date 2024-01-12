import csv
import carbonato1 as c1
import carbonato2 as c2
import carbonato3 as c3
import carbonato4 as c4
import carbonato5 as c5
import carbonato6 as c6
import carbonato7 as c7

import yeso1 as y1
import yeso2 as y2
import yeso3 as y3
import yeso4 as y4
import yeso5 as y5
import yeso6 as y6
import yeso7 as y7

def obtener_cadena(ejemplares):
    l_obj = list() 
    for f in ejemplares:
        for o in f:
            # ['Carpeta','Tabla','Espectro','Pigmento','Aglutinante','Base de preparación']
            s_ejemplar = {'Carpeta':o['carpeta'][0],
                          'Tabla':o['tabla'][0],
                          'Espectro':o['espectro'][0],
                          'Pigmento':o['pigmento'][0],
                          'Aglutinante':o['aglutinante'][0],
                          'Base de preparación':o['base'][0]}
            l_obj.append(s_ejemplar)
            #s_ejemplar+=o['carpeta'][0]+","+o['tabla'][0]+","+o['espectro'][0]+","+o['pigmento'][0]+","+o['aglutinante'][0]+","+o['base'][0]+"\n"
    return l_obj

str_c1 = obtener_cadena(c1.obtener_carbonato_C1())
str_c2 = obtener_cadena(c2.obtener_carbonato_C2())
str_c3 = obtener_cadena(c3.obtener_carbonato_C3())
str_c4 = obtener_cadena(c4.obtener_carbonato_C4())
str_c5 = obtener_cadena(c5.obtener_carbonato_C5())
str_c6 = obtener_cadena(c6.obtener_carbonato_C6())

str_c7 = obtener_cadena(c7.obtener_carbonato_C7())
print("Termino de obtener espectros de base carbonato")

str_y1 = obtener_cadena(y1.obtener_yeso_Y1())
#str_y2 = obtener_cadena(y2.obtener_yeso_Y2())
str_y3 = obtener_cadena(y3.obtener_yeso_Y3())

str_y4 = y4.str_yeso_y4()

str_y5 = obtener_cadena(y5.obtener_yeso_Y5())
str_y6 = obtener_cadena(y6.obtener_yeso_Y6())

str_y7 = y7.str_yeso_y7()
print("Termino de obtener espectros de base yeso")

print("Escribiendo espectros en csv")
with open('espectros.csv', 'w', newline='') as csvfile:
    fieldnames = ['Carpeta','Tabla','Espectro','Pigmento','Aglutinante','Base de preparación']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for i in str_c1:
        writer.writerow(i)
    print("Termino de escribir carbonato 1")

    for i in str_c2:
        writer.writerow(i)
    print("Termino de escribir carbonato 2")

    for i in str_c3:
        writer.writerow(i)
    print("Termino de escribir carbonato 3")

    for i in str_c4:
        writer.writerow(i)
    print("Termino de escribir carbonato 4")

    for i in str_c5:
        writer.writerow(i)
    print("Termino de escribir carbonato 5")

    for i in str_c6:
        writer.writerow(i)
    print("Termino de escribir carbonato 6")

    for i in str_c7:
        writer.writerow(i)
    print("Termino de escribir carbonato 7")

    for i in str_y1:
        writer.writerow(i)
    print("Termino de escribir yeso 1")

    #for i in str_y2:
    #    writer.writerow(i)
    #print("Termino de escribir yeso 2")

    for i in str_y3:
        writer.writerow(i)
    print("Termino de escribir yeso 3")

    for i in str_y4:
        writer.writerow(i)
    print("Termino de escribir yeso 4")

    for i in str_y5:
        writer.writerow(i)
    print("Termino de escribir yeso 5")

    for i in str_y6:
        writer.writerow(i)
    print("Termino de escribir yeso 6")

    for i in str_y7:
        writer.writerow(i)
    print("Termino de escribir yeso 7")



