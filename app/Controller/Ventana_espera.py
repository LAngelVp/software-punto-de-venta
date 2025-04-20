from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from ..Source.gifs_rc import *
from PyQt5.QtGui import QValidator, QStandardItemModel, QStandardItem, QPixmap, QIcon, QCursor
from ..View.UserInterfacePy.UI_PROCESO_CARGANDO import Ui_Ventana_Cargando

class Modal_de_espera(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.gif = ":gifs/Icons/Gif/loader.gif"
        self.ui = Ui_Ventana_Cargando()
        self.ui.setupUi(self)
        self.gif_movie = QMovie(self.gif)
        self.ui.etiqueta_spiner.setMovie(self.gif_movie)
        self.gif_movie.start()
        
        self.setWindowModality(Qt.ApplicationModal)  # Bloquea interacción con otras ventanas
        self.setWindowFlags(Qt.Dialog | Qt.FramelessWindowHint)
        