import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QWidget, QVBoxLayout, QScrollArea
from PyQt5.QtCore import QSize    
from control import controlador_busqueda
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

        self.button.clicked.connect(lambda: self.onChanged(cbfiltro.currentText(), self.textbox.text()))
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
        n_resultados = len(resultados)
        # Create layout and add widgets
        boxWidget = QWidget()
        boxLayout2 = QVBoxLayout()
        boxWidget.setLayout(boxLayout2)

        label = QtWidgets.QLabel("")
        label.setText(str(n_resultados)+"Resultados")
        for i in range(len(resultados)):
            # limpia resultado
            resultado = str(resultados[i]).replace("(","").replace(")","").replace(",","").replace("'","")
            label = QtWidgets.QLabel(resultado)
            boxLayout2.addWidget(label)
        box.setWidget(boxWidget)

    # Funcion para agregar un filtro a la lista de filtros
    def onChanged(self, llave, text):
        self.filtros.update({llave: text})
        return self.filtros
        


        

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = HelloWindow()
    mainWin.show()
    sys.exit( app.exec_() )