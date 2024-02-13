"""
Este modulo contiene la vista de la aplicacion, la cual permite buscar espectros en la base de datos
"""
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QWidget, QScrollArea, QListWidget, QListWidgetItem, QGridLayout,QVBoxLayout
from PyQt5.QtCore import QSize
from PyQt5 import QtGui
import matplotlib
from matplotlib.pyplot import grid
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

        central_widget = QWidget(self)          
        self.setCentralWidget(central_widget)   

        box_layout = QVBoxLayout(self)
        central_widget.setLayout(box_layout)

        #  Selecciona entre los filtros disponibles
        lfiltro = QLabel("Buscar por: ", self)
        lfiltro.setAlignment(QtCore.Qt.AlignTop)
        box_layout.addWidget(lfiltro)


        # Selecciona entre los filtros disponibles
        cbfiltro = QtWidgets.QComboBox(self)
        cbfiltro.addItem("Carpeta")
        cbfiltro.addItem("Tabla")
        cbfiltro.addItem("Espectro")
        cbfiltro.addItem("Pigmento")
        cbfiltro.addItem("Aglutinante")
        cbfiltro.addItem("Base de preparacion")
        lfiltro.setAlignment(QtCore.Qt.AlignTop)
        box_layout.addWidget(cbfiltro)

        # Para cada filtro se debe crear un campo de texto para ingresar el filtro
        # y un boton para agregarlo a la lista de filtros
        # Se crea el campo de texto
        self.textbox = QtWidgets.QLineEdit(self)
        box_layout.addWidget(self.textbox)
        # Se crea el boton
        self.button = QtWidgets.QPushButton('Agregar', self)
        box_layout.addWidget(self.button)


        # Se conecta el boton con la funcion que agrega el filtro
        # Presenta los filtros aplicados
        self.lfiltros = QtWidgets.QLabel("Filtros: ")
        self.lfiltros.setAlignment(QtCore.Qt.AlignTop)
        box_layout.addWidget(self.lfiltros)

        self.button.clicked.connect(lambda: self.agregarFiltro(cbfiltro.currentText(), self.textbox.text()))
        # Imprime bonito los filtros aplicados
        self.button.clicked.connect(lambda: self.lfiltros.setText("Filtros: "+str(self.filtros).replace("{","").replace("}","").replace("'","").replace(",","\n")))

        scroll = QScrollArea()
        scroll.adjustSize()
        scroll.setWidgetResizable(True)
        scroll_content = QWidget(scroll)
        scroll_layout = QVBoxLayout(scroll_content)
        scroll_content.setLayout(scroll_layout)
        scroll.setWidget(scroll_content)
        
        # Se crea el boton para buscar
        self.button = QtWidgets.QPushButton('Buscar', self)
        box_layout.addWidget(self.button)
        # Se conecta el boton con la funcion que busca
        self.button.clicked.connect(lambda: self.buscar(scroll))
        box_layout.addWidget(scroll)
        
    """Método encargado de buscar el espectro en la base de datos usando el buscador"""
    def buscar(self, scroll):
        resultados = controlador_busqueda(self.filtros)
        # Create layout and add widgets
        box_widget = QListWidget()
        box_layout2 = QVBoxLayout()
        box_widget.setLayout(box_layout2)

        for i in range(len(resultados)):
            # limpia resultado
            resultado = str(resultados[i]).replace("(","").replace(")","").replace("'","")
            qitem = QListWidgetItem(resultado)
            box_widget.addItem(qitem)
        scroll.setWidget(box_widget)
        ventanas = []
        # Se conecta el boton con la funcion que selecciona el espectro
        box_widget.itemClicked.connect(lambda: self.seleccionar(box_widget.currentItem().text(),ventanas))

    """Método encargado de agregar un filtro a la lista de filtros"""
    def agregarFiltro(self, llave, text):
        self.filtros.update({llave: text})
        return self.filtros

    """Método encargado de seleccionar el espectro y mostrarlo"""
    def seleccionar(self, espectro,ventanas):
        print("Seleccionado: "+espectro+" para mostrar")
        # Crea la ventana para mostrar el espectro
        self.ventana = QtWidgets.QWidget()
        self.ventana.setWindowTitle("Espectro")
        self.ventana.setMinimumSize(QSize(640, 480))
        self.ventana.move(100,100)
        ventanas.append(self.ventana)
        
        # Imprime info el espectro
        box_layout2 = QVBoxLayout(self.ventana)
        self.ventana.setLayout(box_layout2)
        split_espectro = espectro.split(",")
        carpeta = split_espectro[0]
        tabla = split_espectro[1].strip()#.replace(" ","")
        espectro_name = split_espectro[2].strip()#.replace(" ","")
        pigmento = split_espectro[3]
        aglutinante = split_espectro[4]
        base = split_espectro[5]

        box_layout2.addWidget(QtWidgets.QLabel("Carpeta: "+carpeta))
        box_layout2.addWidget(QtWidgets.QLabel("Tabla: "+tabla))
        box_layout2.addWidget(QtWidgets.QLabel("Espectro: "+espectro_name))
        box_layout2.addWidget(QtWidgets.QLabel("Pigmento: "+pigmento))
        box_layout2.addWidget(QtWidgets.QLabel("Aglutinante: "+aglutinante))
        box_layout2.addWidget(QtWidgets.QLabel("Base de preparacion: "+base))

        # Plot espectro
        #get_df(carpeta,tabla,espectro_name)
        #imprimir_spec(carpeta,tabla,espectro_name)
        
        # Include the matplotlib figure
        self.figure = Figure()
        self.canvas = FigureCanvasQTAgg(self.figure)
        box_layout2.addWidget(self.canvas)
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
        box_layout2.addWidget(self.button)
        # Se conecta el boton con la funcion que combina ventanas
        self.button.clicked.connect(lambda: combinar_ventanas(self,ventanas))

""" Método encargado de combinar las ventanas de los espectros seleccionados """
def combinar_ventanas(self,ventanas):
    eje_X = []
    lista_ys = []
    labels = []
    espectros = []
    print("Combinando ventanas")
    for i in range(len(ventanas)):
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
    self.ventana.move(100,100)
    self.ventana.setWindowTitle("Espectro")
    self.ventana.setMinimumSize(QSize(640, 480))

    box_layout2 = QGridLayout(self.ventana)#QVBox_layout(self.ventana)
    self.ventana.setLayout(box_layout2)

    self.info = QtWidgets.QWidget()
    # Crear la ventana para mostrar la informacion de los espectros ligeramente a la izquierda de la ventana de combinacion
    self.info.move(100,600)
    self.info.setLayout(QGridLayout())
    self.info.setWindowTitle("Información espectros")
    self.info.setMinimumSize(QSize(440, 380))
    
    scroll = QScrollArea()
    scroll.adjustSize()
    scroll.setWidgetResizable(True)
    scroll_content = QWidget(scroll)
    
    scroll.setWidget(scroll_content)
    self.info.layout().addWidget(scroll)
    box_widget = QListWidget()
    box_layout2 = QVBoxLayout()
    box_widget.setLayout(box_layout2)

    for i in range(len(labels)):
        qitem = QListWidgetItem(labels[i])
        if "Espectro" in labels[i]:
            qitem.setBackground(QtGui.QColor("yellow"))
        box_widget.addItem(qitem)
    scroll.setWidget(box_widget)
    
    self.info.show()

    self.ventana.show()

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
    # Al cerrar la ventana se limpia la lista de ventanas y se cierra la ventana de informacion

    self.ventana.destroyed.connect(lambda: ventanas.clear())
    if self.ventana.destroyed and not self.info.destroyed:
        self.info.close()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_win = HelloWindow()
    main_win.show()
    sys.exit( app.exec_() )
