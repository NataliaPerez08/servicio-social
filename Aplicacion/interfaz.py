import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget
from PyQt5.QtCore import QSize    

class HelloWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        # lista de filtro aplicados
        self.filtros = {'Carpeta': '','Tabla': '','Espectro': '','Pigmento': '','Aglutinante': '','Base de preparacion': ''}

        self.setMinimumSize(QSize(640, 480))    
        self.setWindowTitle("Registros de Espectros FORS") 

        centralWidget = QWidget(self)          
        self.setCentralWidget(centralWidget)   

        gridLayout = QGridLayout(self)     
        centralWidget.setLayout(gridLayout)  

        title = QLabel("Registros de Espectros FORS", self) 
        title.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft) 
        gridLayout.addWidget(title, 0, 0)

        #  Selecciona entre los filtros disponibles
        lfiltro = QLabel("Buscar por: ", self)
        lfiltro.setAlignment(QtCore.Qt.AlignCenter)
        # Inserta el label en la ventana en la esquina superior izquierda debajo del titulo
        gridLayout.addWidget(lfiltro, 3, 0)


        # Selecciona entre los filtros disponibles
        cbfiltro = QtWidgets.QComboBox(self)
        cbfiltro.addItem("Carpeta")
        cbfiltro.addItem("Tabla")
        cbfiltro.addItem("Espectro")
        cbfiltro.addItem("Pigmento")
        cbfiltro.addItem("Aglutinante")
        cbfiltro.addItem("Base de preparacion")
        gridLayout.addWidget(cbfiltro, 1, 0)

        # Para cada filtro se debe crear un campo de texto para ingresar el filtro
        # y un boton para agregarlo a la lista de filtros
        # Se crea el campo de texto
        self.textbox = QtWidgets.QLineEdit(self)
        gridLayout.addWidget(self.textbox, 1, 1)
        # Se crea el boton
        self.button = QtWidgets.QPushButton('Agregar', self)
        gridLayout.addWidget(self.button, 1, 2)


        # Se conecta el boton con la funcion que agrega el filtro
        # Presenta los filtros aplicados
        self.lfiltros = QtWidgets.QLabel("Filtros: ")
        self.lfiltros.setAlignment(QtCore.Qt.AlignCenter)
        gridLayout.addWidget(self.lfiltros, 2, 1)

        self.button.clicked.connect(lambda: self.onChanged(cbfiltro.currentText(), self.textbox.text()))
        # Imprime bonito los filtros aplicados
        self.button.clicked.connect(lambda: self.lfiltros.setText("Filtros: "+str(self.filtros).replace("{","").replace("}","").replace("'","").replace(",","\n")))

        
    


        # Se crea el boton para buscar
        self.button = QtWidgets.QPushButton('Buscar', self)
        gridLayout.addWidget(self.button, 2, 0)
        # Se conecta el boton con la funcion que busca
        self.button.clicked.connect(self.buscar)

        

    # Funcion para buscar el espectro en la base de datos usando el buscador 
    def buscar(self,text):
        print("Buscando espectro",text, " ", self.filtros) 

    # Funcion para agregar un filtro a la lista de filtros
    def onChanged(self, llave, text):
        self.filtros.update({llave: text})
        print("Filtros:", self.filtros)
        return self.filtros
        


        

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = HelloWindow()
    mainWin.show()
    sys.exit( app.exec_() )