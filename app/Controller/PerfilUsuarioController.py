from PySide6 import QtCore, QtWidgets
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from ..View.UserInterfacePy.UI_CONTROL_PERFIL import *

class Perfil(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Formulario_Datos_Empleado()
        self.ui.setupUi(self)