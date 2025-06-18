from PySide6 import QtCore, QtWidgets
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from ..Source.gifs_rc import *
from PySide6.QtGui import QValidator, QStandardItemModel, QStandardItem, QPixmap, QIcon, QCursor
from ..View.UserInterfacePy.UI_PROCESO_CARGANDO import Ui_Ventana_Cargando

class Modal_de_espera(QDialog):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.gif = ":gifs/Icons/Gif/loader.gif"
        self.ui = Ui_Ventana_Cargando()
        self.ui.setupUi(self)
        self.gif_movie = QMovie(self.gif)
        self.ui.etiqueta_spiner.setMovie(self.gif_movie)
        self.gif_movie.start()
        
        sombra = QGraphicsDropShadowEffect()
        sombra.setBlurRadius(25) 
        sombra.setOffset(0, 0)
        sombra.setColor(QColor(0, 102, 204)) 

        self.ui.contenedor.setGraphicsEffect(sombra)
        
        self.setWindowModality(Qt.ApplicationModal)  # Bloquea interacción con otras ventanas
        self.setWindowFlags(self.windowFlags() | Qt.WindowType.FramelessWindowHint) 
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        
        pantalla = self.frameGeometry()
        pantalla.moveCenter(self.screen().availableGeometry().center())
        self.move(pantalla.topLeft())
        