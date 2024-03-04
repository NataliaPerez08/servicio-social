from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QLabel, QVBoxLayout
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QMainWindow, QLabel, QToolBar, QToolButton

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

import print_specs_control as psc
import control_modelos as cm
import recoverRegister as rr

"""
Clase principal de la aplicación de clasificación
"""
class Aplicacion(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setWindowTitle('Subir Archivo')
        self.setGeometry(100, 100, 900, 500)
        self.show()

    """"  Inicializa la interfaz de usuario"""
    def initUI(self):
        self.ruta = ""
        self.label = QLabel(self)
        self.label.move(10, 10)
        self.label.resize(500, 200)

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
        toolButoon.clicked.connect(self.perceptron_clicked)
        toolbar.addWidget(toolButoon)

        toolButoon = QToolButton()
        toolButoon.setText("Logistic Regression")
        toolButoon.setCheckable(True)
        toolButoon.clicked.connect(self.regresion_logistica_clicked)
        toolbar.addWidget(toolButoon)

        toolButoon = QToolButton()
        toolButoon.setText("Linear Regression")
        toolButoon.setCheckable(True)
        toolButoon.clicked.connect(self.regresion_lineal_clicked)
        toolbar.addWidget(toolButoon)

        toolButoon = QToolButton()
        toolButoon.setText("Naive Bayes")
        toolButoon.setCheckable(True)
        toolButoon.clicked.connect(self.gaussianNB_clicked)
        toolbar.addWidget(toolButoon)

        toolButoon = QToolButton()
        toolButoon.setText("Random Forest")
        toolButoon.setCheckable(True)
        toolButoon.clicked.connect(self.randomForest_clicked)
        toolbar.addWidget(toolButoon)

        toolButoon = QToolButton()
        toolButoon.setText("SVM")
        toolButoon.setCheckable(True)
        toolButoon.clicked.connect(self.svc_clicked)
        toolbar.addWidget(toolButoon)

        self.ventana = QMainWindow()

    """ Método que abre el archivo y lo envia al hilo para ser leido"""
    def abrirArchivo(self):
        nombreArchivo, _ = QFileDialog.getOpenFileName(self, 'Abrir Archivo')
        if nombreArchivo != '':
            self.hilo = Hilo(nombreArchivo)
            self.hilo.start()
            self.hilo.enviarTexto.connect(self.mostrarTexto)


    """ Método que busca el archivo y lo muestra en la interfaz"""
    def mostrarTexto(self, texto):
        if texto == "Error":
            self.label.setText("Error")
            return
        self.label.setText(texto.split("/")[-1])
        self.ruta = texto 
        
        psc.print_spec_from_ruta(self.ruta, texto.split("/")[-1])

    """ Método que realiza la predicción con el modelo de perceptron"""
    def perceptron_clicked(self):
        print("Perceptron")
        if self.ruta == "":
            self.label.setText("No hay archivo")
        else:
            nombre = self.ruta.split("/")[-1]
            resultado = nombre+"\n"+cm.haz_prediccion_perceptron(self.ruta)
            self.label.setText(resultado)

    """ Método que realiza la predicción con el modelo de regresión logística"""
    def regresion_logistica_clicked(self):
        print("Logistic Regression")
        if self.ruta == "":
            self.label.setText("No hay archivo")
        else:
            nombre = self.ruta.split("/")[-1]
            resultado = nombre+"\n"+cm.haz_prediccion_regresion_logistica(self.ruta)
            self.label.setText(resultado)

    """ Método que realiza la predicción con el modelo de regresión lineal"""
    def regresion_lineal_clicked(self):
        print("Linear Regression")
        if self.ruta == "":
            self.label.setText("No hay archivo")
        else:
            nombre = self.ruta.split("/")[-1]
            resultado = nombre+"\n"+cm.haz_prediccion_regresion_lineal(self.ruta)
            self.label.setText(resultado)

    """ Método que realiza la predicción con el modelo de Naive Bayes"""
    def gaussianNB_clicked(self):
        print("Naive Bayes")
        if self.ruta == "":
            self.label.setText("No hay archivo")
        else:
            nombre = self.ruta.split("/")[-1]
            resultado = nombre+"\n"+cm.haz_prediccion_GaussianNB(self.ruta)
            self.label.setText(resultado)

    """ Método que realiza la predicción con el modelo de Random Forest"""
    def randomForest_clicked(self):
        print("Random Forest")
        if self.ruta == "":
            self.label.setText("No hay archivo")
        else:
            nombre = self.ruta.split("/")[-1]
            resultado = nombre+"\n"+cm.haz_prediccion_RandomForest(self.ruta)
            self.label.setText(resultado)

    """ Método que realiza la predicción con el modelo de SVM"""
    def svc_clicked(self):
        print("SVM")
        if self.ruta == "":
            self.label.setText("No hay archivo")
        else:
            nombre = self.ruta.split("/")[-1]
            resultado = nombre+"\n"+cm.haz_prediccion_SVC(self.ruta)
            self.label.setText(resultado)


""" Clase que lee el archivo"""
class Hilo(QThread):
    enviarTexto = pyqtSignal(str)

    def __init__(self, nombreArchivo):
        super().__init__()
        self.nombreArchivo = nombreArchivo

    """ Método que lee el archivo y envia el texto al hilo principal"""
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