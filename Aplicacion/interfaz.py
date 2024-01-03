import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QWidget, QVBoxLayout, QScrollArea, QListWidget, QListWidgetItem
from PyQt5.QtCore import QSize
from sympy import li    
from control import controlador_busqueda
from controlSpec import imprimir_spec,get_df

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

# Vista de la aplicacion
class HelloWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        # lista de filtro aplicados
        self.filtros = {'Carpeta': '','Tabla': '','Espectro': '','Pigmento': '','Aglutinante': '','Base de preparacion': ''}

        self.setMinimumSize(QSize(640, 480))    
        self.setWindowTitle("Registros de Espectros FORS") 

        centralWidget = QWidget(self)          
        self.setCentralWidget(centralWidget)   

        boxLayout = QVBoxLayout(self)
        centralWidget.setLayout(boxLayout)

        #  Selecciona entre los filtros disponibles
        lfiltro = QLabel("Buscar por: ", self)
        lfiltro.setAlignment(QtCore.Qt.AlignTop)
        boxLayout.addWidget(lfiltro)


        # Selecciona entre los filtros disponibles
        cbfiltro = QtWidgets.QComboBox(self)
        cbfiltro.addItem("Carpeta")
        cbfiltro.addItem("Tabla")
        cbfiltro.addItem("Espectro")
        cbfiltro.addItem("Pigmento")
        cbfiltro.addItem("Aglutinante")
        cbfiltro.addItem("Base de preparacion")
        lfiltro.setAlignment(QtCore.Qt.AlignTop)
        boxLayout.addWidget(cbfiltro)

        # Para cada filtro se debe crear un campo de texto para ingresar el filtro
        # y un boton para agregarlo a la lista de filtros
        # Se crea el campo de texto
        self.textbox = QtWidgets.QLineEdit(self)
        boxLayout.addWidget(self.textbox)
        # Se crea el boton
        self.button = QtWidgets.QPushButton('Agregar', self)
        boxLayout.addWidget(self.button)


        # Se conecta el boton con la funcion que agrega el filtro
        # Presenta los filtros aplicados
        self.lfiltros = QtWidgets.QLabel("Filtros: ")
        self.lfiltros.setAlignment(QtCore.Qt.AlignTop)
        boxLayout.addWidget(self.lfiltros)

        self.button.clicked.connect(lambda: self.agregarFiltro(cbfiltro.currentText(), self.textbox.text()))
        # Imprime bonito los filtros aplicados
        self.button.clicked.connect(lambda: self.lfiltros.setText("Filtros: "+str(self.filtros).replace("{","").replace("}","").replace("'","").replace(",","\n")))

        scroll = QScrollArea()
        scroll.adjustSize()
        scroll.setWidgetResizable(True)
        scrollContent = QWidget(scroll)
        scrollLayout = QVBoxLayout(scrollContent)
        scrollContent.setLayout(scrollLayout)
        scroll.setWidget(scrollContent)
        
        # Se crea el boton para buscar
        self.button = QtWidgets.QPushButton('Buscar', self)
        boxLayout.addWidget(self.button)
        # Se conecta el boton con la funcion que busca
        self.button.clicked.connect(lambda: self.buscar(self.textbox.text(),scroll))
        boxLayout.addWidget(scroll)
        
    # Funcion para buscar el espectro en la base de datos usando el buscador 
    def buscar(self,text, box):
        resultados = controlador_busqueda(self.filtros)
        # Create layout and add widgets
        boxWidget = QListWidget()
        boxLayout2 = QVBoxLayout()
        boxWidget.setLayout(boxLayout2)

        for i in range(len(resultados)):
            # limpia resultado
            resultado = str(resultados[i]).replace("(","").replace(")","").replace(",","").replace("'","")
            qitem = QListWidgetItem(resultado)
            boxWidget.addItem(qitem)
        box.setWidget(boxWidget)
        ventanas = []
        # Se conecta el boton con la funcion que selecciona el espectro
        boxWidget.itemClicked.connect(lambda: self.seleccionar(boxWidget.currentItem().text(),ventanas))

    # Funcion para agregar un filtro a la lista de filtros
    def agregarFiltro(self, llave, text):
        self.filtros.update({llave: text})
        return self.filtros

    # Funcion para dar el espectro seleccionado
    def seleccionar(self, espectro,ventanas):
        # Crea la ventana para mostrar el espectro
        self.ventana = QtWidgets.QWidget()
        self.ventana.setWindowTitle("Espectro")
        self.ventana.setMinimumSize(QSize(640, 480))
        ventanas.append(self.ventana)
        
        # Imprime info el espectro
        boxLayout2 = QVBoxLayout(self.ventana)
        self.ventana.setLayout(boxLayout2)
        print(espectro)
        split_espectro = espectro.split()
        carpeta = split_espectro[0]
        tabla = split_espectro[1]
        espectro_name = split_espectro[2]
        pigmento = split_espectro[3]
        aglutinante = split_espectro[4]
        base = split_espectro[5]

        boxLayout2.addWidget(QtWidgets.QLabel("Carpeta: "+carpeta))
        boxLayout2.addWidget(QtWidgets.QLabel("Tabla: "+tabla))
        boxLayout2.addWidget(QtWidgets.QLabel("Espectro: "+espectro_name))
        boxLayout2.addWidget(QtWidgets.QLabel("Pigmento: "+pigmento))
        boxLayout2.addWidget(QtWidgets.QLabel("Aglutinante: "+aglutinante))
        boxLayout2.addWidget(QtWidgets.QLabel("Base: "+base))

        self.ventana.show()

        # Plot espectro
        #get_df(carpeta,tabla,espectro_name)
        #imprimir_spec(carpeta,tabla,espectro_name)
        # Include the matplotlib figure
        
        self.figure = Figure()
        self.canvas = FigureCanvasQTAgg(self.figure)
        boxLayout2.addWidget(self.canvas)
        self.ax = self.figure.add_subplot(111)
        df = get_df(carpeta,tabla,espectro_name)
        x=df.columns[0]
        y=df.columns[1]
        dev_x = df[x].to_numpy()
        dev_y = df[y].to_numpy()
        self.ax.plot(dev_x, dev_y)
        self.ax.set_title("Espectro "+espectro_name+" de la tabla "+tabla+" de la carpeta "+carpeta)
        self.ax.set_xlabel("Longitud de onda")
        self.ax.set_ylabel("Reflectancia")
        self.ax.grid()
        self.canvas.draw()
        self.ventana.show()
        
def create():
    app = QtWidgets.QApplication(sys.argv)
    mainWin = HelloWindow()
    mainWin.show()
    sys.exit( app.exec_() )

create()