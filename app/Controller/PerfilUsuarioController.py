from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from ..View.UserInterfacePy.UI_CONTROL_PERFIL import *

class Perfil(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Formulario_Datos_Empleado()
        self.ui.setupUi(self)