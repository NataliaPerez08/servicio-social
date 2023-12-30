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
    s_ejemplar = ""
    for f in ejemplares:
        for o in f:
            print(o['carpeta'][0]+","+o['tabla'][0]+","+o['espectro'][0]+","+o['pigmento'][0]+","+o['aglutinante'][0]+","+o['base'][0])
                  
            s_ejemplar+=o['carpeta'][0]+","+o['tabla'][0]+","+o['espectro'][0]+","+o['pigmento'][0]+","+o['aglutinante'][0]+","+o['base'][0]+"\n"
    return s_ejemplar   


columnas = ['Carpeta','Tabla','Espectro','Pigmento','Aglutinante','Base de preparación']

str_c1 = obtener_cadena(c1.obtener_carbonato_C1())

""""
str_c2 = obtener_cadena(c2.obtener_carbonato_C2())
str_c3 = obtener_cadena(c3.obtener_carbonato_C3())
str_c4 = obtener_cadena(c4.obtener_carbonato_C4())
str_c5 = obtener_cadena(c5.obtener_carbonato_C5())
str_c6 = obtener_cadena(c6.obtener_carbonato_C6())

str_c7 = c7.str_carbonato_C7()

str_y1 = obtener_cadena(y1.obtener_yeso_Y1())
str_y2 = obtener_cadena(y2.obtener_yeso_Y2())
str_y3 = obtener_cadena(y3.obtener_yeso_Y3())
str_y4 = y4.str_yeso_y4()

str_y5 = obtener_cadena(y5.obtener_yeso_Y5())
str_y6 = obtener_cadena(y6.obtener_yeso_Y6())
str_y7 = y7.str_yeso_y7()
"""

print("Escribiendo espectros en csv")
with open('espectros.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(columnas)
    writer.writerow(str_c1)
    #writer.writerow(str_c2)
    #writer.writerow(str_c3)
    #writer.writerow(str_c4)
    #writer.writerow(str_c5)
    #writer.writerow(str_c6)
    #writer.writerow(str_c7)
    #writer.writerow(str_y1)
    #writer.writerow(str_y2)
    #writer.writerow(str_y3)
    #writer.writerow(str_y4)
    #writer.writerow(str_y5)
    #writer.writerow(str_y6)
    #writer.writerow(str_y7)

