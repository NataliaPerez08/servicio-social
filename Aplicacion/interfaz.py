import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QWidget, QVBoxLayout, QScrollArea, QListWidget, QListWidgetItem
from PyQt5.QtCore import QSize
import matplotlib
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
        self.button.clicked.connect(lambda: self.buscar(scroll))
        boxLayout.addWidget(scroll)
        
    # Funcion para buscar el espectro en la base de datos usando el buscador 
    def buscar(self, box):
        resultados = controlador_busqueda(self.filtros)
        # Create layout and add widgets
        boxWidget = QListWidget()
        boxLayout2 = QVBoxLayout()
        boxWidget.setLayout(boxLayout2)

        for i in range(len(resultados)):
            # limpia resultado
            resultado = str(resultados[i]).replace("(","").replace(")","").replace("'","")
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
        print("Seleccionado: "+espectro+" para mostrar")
        # Crea la ventana para mostrar el espectro
        self.ventana = QtWidgets.QWidget()
        self.ventana.setWindowTitle("Espectro")
        self.ventana.setMinimumSize(QSize(640, 480))
        ventanas.append(self.ventana)
        
        # Imprime info el espectro
        boxLayout2 = QVBoxLayout(self.ventana)
        self.ventana.setLayout(boxLayout2)
        split_espectro = espectro.split(",")
        carpeta = split_espectro[0]
        tabla = split_espectro[1].replace(" ","")
        espectro_name = split_espectro[2].replace(" ","")
        pigmento = split_espectro[3]
        aglutinante = split_espectro[4]
        base = split_espectro[5]

        boxLayout2.addWidget(QtWidgets.QLabel("Carpeta: "+carpeta))
        boxLayout2.addWidget(QtWidgets.QLabel("Tabla: "+tabla))
        boxLayout2.addWidget(QtWidgets.QLabel("Espectro: "+espectro_name))
        boxLayout2.addWidget(QtWidgets.QLabel("Pigmento: "+pigmento))
        boxLayout2.addWidget(QtWidgets.QLabel("Aglutinante: "+aglutinante))
        boxLayout2.addWidget(QtWidgets.QLabel("Base de preparacion: "+base))

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
        self.ax.set_title("Espectro "+espectro_name)
        self.ax.set_ylabel("Reflectancia")
        self.ax.grid()
        self.canvas.draw()
        self.ventana.show()
        # Crear el boton para combinar ventanas
        self.button = QtWidgets.QPushButton('Combinar ventanas', self.ventana)
        boxLayout2.addWidget(self.button)
        # Se conecta el boton con la funcion que combina ventanas
        self.button.clicked.connect(lambda: combinar_ventanas(self,ventanas))

        
def combinar_ventanas(self,ventanas):
    eje_X = []
    lista_ys = []
    labels = []
    espectros = []
    print("Combinando ventanas")
    for i in range(len(ventanas)):
        #print(ventanas[i])
        #print(ventanas[i].children())
        hijos = ventanas[i].children()
        for j in range(len(hijos)):
            tipo_hijo = type(hijos[j])
            # Verifica que el hijo sea un matplotlib
            if tipo_hijo == matplotlib.backends.backend_qtagg.FigureCanvasQTAgg:
                # Obtiene la figura
                fig = hijos[j].figure
                # Obtiene el eje
                ax = fig.axes[0]
                # Obtiene los datos
                line = ax.lines[0]
                # Obtiene los datos de x
                x = line.get_xdata()
                # Obtiene los datos de y
                y = line.get_ydata()
                eje_X = x
                lista_ys.append(y)
            # Verifica que el hijo sea un label para obtener el nombre del espectro
            elif tipo_hijo == QtWidgets.QLabel:
                text = hijos[j].text()
                if "Espectro" in text:
                    espectros.append(text)
                labels.append(hijos[j].text())

        ventanas[i].close() 

    # Crea un matplotlib para combinar los espectros
    # Include the matplotlib figure
    self.ventana = QtWidgets.QWidget()
    self.ventana.setWindowTitle("Espectro")
    self.ventana.setMinimumSize(QSize(640, 480))
    boxLayout2 = QVBoxLayout(self.ventana)
    self.ventana.setLayout(boxLayout2)

    print("Creando matplotlib") 
    figure = Figure()
    canvas = FigureCanvasQTAgg(figure)
    self.ventana.layout().addWidget(canvas)
    ax = figure.add_subplot(111)
    ax.set_title("Espectro combinado")
    ax.set_ylabel("Reflectancia")
    ax.grid()
    # Combina los espectros
    for j in range(len(lista_ys)):
        ax.plot(eje_X, lista_ys[j])
        ax.legend(espectros)
    canvas.draw()
    # Imprime los nombres de los espectros
    boxLayout2.addWidget(QtWidgets.QLabel("Espectros: \n\n"+str(labels).replace("[","").replace("]","").replace("'","").replace(",","\n")))
    self.ventana.show()
    # Al cerrar la ventana se limpia la lista de ventanas
    self.ventana.destroyed.connect(lambda: ventanas.clear())

def create():
    app = QtWidgets.QApplication(sys.argv)
    mainWin = HelloWindow()
    mainWin.show()
    sys.exit( app.exec_() )

create()