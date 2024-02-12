# Programa para Servicio social
## Requerimientos

Instalación de python 3.11.4
Se puede descargar el instalador en https://www.python.org/downloads/release/python-3117/

[alt text](image/install_python.png)

Elegir  el recomendado: Windows installer (64-bit)

### Ejecutar ambiente
Para ejecutar cualquiera de los programas es necesario iniciar un ambiente virtual de python:
#### En Windows

Desde el navegador de documentos de la carpeta 'servicio-social' dar click derecho como en la imagen y seleccionar 'Abrir en Terminal'
![alt text](image/image.png)

Ejecutar lo siguiente:
1. cd ss
2. cd bin
3. activate

Si fue activado exitosamente vera algo similar

![alt text](image/image-2.png)

Una vez activo proceder

### Ejecutar buscador
Ejecutar 
1. cd ../..
2. cd Aplicacion

![alt text](image/image-3.png)

3. python organizador.py
![alt text](image/image-4.png)

### Ejecutar Aproximador
Ejecutar: python clasificador.py
![alt text](image/image-5.png)

## Actualizar Base de Datos para el programa

Para ingresar una nueva tabla de mediciones es necesario incluir la nueva carpeta en 


Ejecutar el archivo actualizaCSV_DB.py, e introducir el nombre del archivo csv que debe estar en la misma carpeta que actualizaCSV_DB.py

![alt text](image/actualiza.png)

## PROGRAMA:ORGANIZADOR

El objetivo de este programa es proveer con una interfaz para mantener organizadas mediciones de espectros FORS proporcionando filtros y la posibilidad de gráficar y combinar gráficas. Notemos un ejemplo para utilizar los filtros:

|| Filtro  | Descripción | Ejemplo |
|:------------- |:---------------:| -------------:|
| Carpeta       | El nombre de la carpeta donde se encuentran las tablas      | Tabla 3     |
| Tablas     | *Italic*        | Cell 6        |
| Row 3         | ~~Strike~~      | Cell 9        |

