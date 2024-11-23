from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from ..View.UserInterfacePy.UI_CONTROL_ROLES import *
from  ..View.UserInterfacePy.UI_NUEVO_ROL import *

# from ...RegistroInicialController import *

class Control_rol(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Control_Roles_Permisos()
        self.ui.setupUi(self)
        pantalla = self.frameGeometry()
        pantalla.moveCenter(self.screen().availableGeometry().center())
        self.move(pantalla.topLeft())
        self.ui.btn_btn_nuevorol.clicked.connect(self.nuevo_rol)

    def nuevo_rol(self):
        self.crear_rol = Nuevo_rol()
        self.crear_rol.show()

class Nuevo_rol(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Control_nuevo_rol()
        self.ui.setupUi(self)
        