from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from ..View.UserInterfacePy.UI_CONTROL_EMPLEADOS import *
from .RolesController import *
# from ...RegistroInicialController import *


class Empleados(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Control_empleados()
        self.ui.setupUi(self)
        self.ui.btn_btn_agregar.clicked.connect(self.agregar_empleado)
        self.ui.btn_btn_controlroles.clicked.connect(self.roles)
    
    def roles(self):
        self.roles =  Control_rol()
        self.roles.show()

    def agregar_empleado(self):
        self.ventana = Registro_personal_inicial()
        self.ventana.show()

