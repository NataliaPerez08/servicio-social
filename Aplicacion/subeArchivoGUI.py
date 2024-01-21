
import select
from tkinter import Widget
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QPushButton, QLabel
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtGui import QPixmap

from PyQt5.QtWidgets import QMainWindow, QLabel, QWidget, QVBoxLayout, QScrollArea, QListWidget, QListWidgetItem, QGridLayout,QDialog
from PyQt5.QtCore import QSize
from PyQt5 import QtGui
from matplotlib import widgets

import recoverRegister as rr 

# Aplicacion que recibe un archivo e imprime su contenido
class Aplicacion(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setWindowTitle('Subir Archivo')
        self.setGeometry(100, 100, 400, 400)
        self.show()

    def initUI(self):
        self.btn = QPushButton('Subir Archivo', self)
        self.btn.move(150, 100)
        self.btn.clicked.connect(self.abrirArchivo)

        self.label = QLabel(self)
        self.label.setPixmap(QPixmap('logo.png'))
        self.label.move(150, 150)
        self.label.resize(100, 100)

    def abrirArchivo(self):
        nombreArchivo, _ = QFileDialog.getOpenFileName(self, 'Abrir Archivo')
        if nombreArchivo != '':
            self.hilo = Hilo(nombreArchivo)
            self.hilo.start()
            self.hilo.enviarTexto.connect(self.mostrarTexto)

    def mostrarTexto(self, texto):
        print("Este es nu")
        self.label.setText(texto)
        # Crear boton
        self.btnLogic = Widget.QPushButton("Logic")
        self.btn.setText("Logic")
        print(self.layout)
        #self.btn = widgets.Button(ax=0,label="Aplicar regresion logistica")

# Hilo que lee el archivo
class Hilo(QThread):
    enviarTexto = pyqtSignal(str)

    def __init__(self, nombreArchivo):
        super().__init__()
        self.nombreArchivo = nombreArchivo

    def run(self):
        with open(self.nombreArchivo, 'r') as archivo:
            texto = archivo.read()
            self.enviarTexto.emit(texto)
            
if __name__ == '__main__':
    app = QApplication([])
    ex = Aplicacion()
    app.exec_()