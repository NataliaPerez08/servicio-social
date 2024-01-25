from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QPushButton, QLabel
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QAction
from PyQt5.QtWidgets import QMainWindow, QLabel, QToolBar, QToolButton
from PyQt5.QtCore import QSize
from PyQt5 import QtGui
from matplotlib import widgets

import recoverRegister as rr 
import print_specs_control as psc
import control_modelos as cm

# Aplicacion que recibe un archivo e imprime su contenido
class Aplicacion(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setWindowTitle('Subir Archivo')
        self.setGeometry(100, 100, 400, 400)
        self.show()

    def initUI(self):
        self.label = QLabel(self)
        self.label.move(150, 150)
        self.label.resize(100, 100)

        toolbar = QToolBar()
        self.addToolBar(toolbar)

        toolButoon = QToolButton()
        toolButoon.setText("Subir Archivo")
        toolButoon.setCheckable(True)
        toolButoon.clicked.connect(self.abrirArchivo)
        toolbar.addWidget(toolButoon)

        toolButoon = QToolButton()
        toolButoon.setText("Perceptron")
        toolButoon.setCheckable(True)
        toolButoon.clicked.connect(self.button1_clicked)
        toolbar.addWidget(toolButoon)

        toolButoon = QToolButton()
        toolButoon.setText("Logistic Regression")
        toolButoon.setCheckable(True)
        toolButoon.clicked.connect(self.button2_clicked)
        toolbar.addWidget(toolButoon)

        toolButoon = QToolButton()
        toolButoon.setText("Linear Regression")
        toolButoon.setCheckable(True)
        toolButoon.clicked.connect(self.button3_clicked)
        toolbar.addWidget(toolButoon)

        toolButoon = QToolButton()
        toolButoon.setText("Naive Bayes")
        toolButoon.setCheckable(True)
        toolButoon.clicked.connect(self.button4_clicked)
        toolbar.addWidget(toolButoon)

        toolButoon = QToolButton()
        toolButoon.setText("Random Forest")
        toolButoon.setCheckable(True)
        toolButoon.clicked.connect(self.button5_clicked)
        toolbar.addWidget(toolButoon)

        toolButoon = QToolButton()
        toolButoon.setText("SVM")
        toolButoon.setCheckable(True)
        toolButoon.clicked.connect(self.button6_clicked)
        toolbar.addWidget(toolButoon)



    def abrirArchivo(self):
        nombreArchivo, _ = QFileDialog.getOpenFileName(self, 'Abrir Archivo')
        if nombreArchivo != '':
            self.hilo = Hilo(nombreArchivo)
            self.hilo.start()
            self.hilo.enviarTexto.connect(self.mostrarTexto)

    def mostrarTexto(self, texto):
        if texto == "Error":
            self.label.setText("Error")
            return
        #self.label.setText(texto)
        ruta = texto
        psc.print_spec_from_ruta(ruta)


    def button1_clicked(self):
        print("Perceptron")
        print("Botón 1 presionado")

    def button2_clicked(self):
        print("Botón 2 presionado")

    def button3_clicked(self):
        print("Botón 3 presionado")

    def button4_clicked(self):
        print("Botón 4 presionado")

    def button5_clicked(self):
        print("Botón 5 presionado")

    def button6_clicked(self):
        print("Botón 6 presionado")

# Hilo que lee el archivo
class Hilo(QThread):
    enviarTexto = pyqtSignal(str)

    def __init__(self, nombreArchivo):
        super().__init__()
        self.nombreArchivo = nombreArchivo

    def run(self):
        print("Nombre archivo: ",self.nombreArchivo)
        # Obtener extension del archivo
        ext = self.nombreArchivo.split(".")[-1]
        print("Extension: ",ext)
        if ext == "txt" or ext == "asd":
            self.enviarTexto.emit(self.nombreArchivo)
        else:
            self.enviarTexto.emit("Error")

if __name__ == '__main__':
    app = QApplication([])
    ex = Aplicacion()
    app.exec_()