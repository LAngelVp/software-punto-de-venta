from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from ..View.UserInterfacePy.UI_CONTROL_DEPARTAMENTOS import Ui_Control_departamentos

class DepartamentosController(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Control_departamentos()
        self.ui.setupUi(self)

        #botones:
        self.ui.btn_btn_guardar.clicked.connect(self.guardar)
        self.ui.btn_btn_eliminar.clicked.connect(self.eliminar)
        self.ui.btn_btn_vincular.clicked.connect(self.vincular_sucursal)
        self.ui.btn_btn_desvincular.clicked.connect(self.desvincular_sucursal)

    #funciones:
    def guardar(self):
        pass

    def eliminar(self):
        pass

    def vincular_sucursal(self):
        pass
    
    def desvincular_sucursal(self):
        pass
