from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from .MensajesAlertasController import Mensaje
from ..View.UserInterfacePy.UI_AGREGAR_UN_DATO import Ui_Formulario

class FormularioAgregarDatoCombobox(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Formulario()
        self.ui.setupUi(self)