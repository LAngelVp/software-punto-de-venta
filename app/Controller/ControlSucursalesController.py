import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from app.View.UserInterfacePy.UI_CONTROL_SUCUDEPAPUESTO import Ui_Control_SucursalesDepartamentosPuestos

from app.Controller.SucursalesController import SucursalesController
from app.Controller.DepartamentosController import DepartamentosController
from app.Controller.PuestosController import PuestosController

class ControlSucursalesController(QWidget):
    listar_sucursales = pyqtSignal(set)
    listar_departamentos = pyqtSignal()
    listar_departamentos_puestos = pyqtSignal()
    def __init__(self):
        super().__init__()
        self.ui = Ui_Control_SucursalesDepartamentosPuestos()
        self.ui.setupUi(self)
        pantalla = self.frameGeometry()
        pantalla.moveCenter(self.screen().availableGeometry().center())
        self.move(pantalla.topLeft())

        self.sucursales = SucursalesController()
        self.departamentos = DepartamentosController()
        self.puestos = PuestosController()


        self.ui.contenedor_paginas.addWidget(self.sucursales)
        self.ui.contenedor_paginas.addWidget(self.departamentos)
        self.ui.contenedor_paginas.addWidget(self.puestos)


        self.ui.btn_btn_sucursales.clicked.connect(self.formulario_sucursales)
        self.ui.btn_btn_departamentos.clicked.connect(self.formulario_departamentos)
        self.ui.btn_btn_puestos.clicked.connect(self.formulario_puestos)

        #funciones-iniciales:
        self.listar_sucursales.connect(self.departamentos.listar_sucursales_existentes)
        self.listar_departamentos.connect(self.departamentos.obtener_departamentos)
        self.listar_departamentos_puestos.connect(self.puestos.listar_departamentos)
        self.listar_departamentos_puestos.connect(self.puestos.listar_puestos)

    def formulario_sucursales(self):
        self.ui.contenedor_paginas.setCurrentWidget(self.sucursales)
    
    def formulario_departamentos(self):
        if self.ui.contenedor_paginas.currentWidget() != self.departamentos:
            self.listar_sucursales.emit(set())
            self.listar_departamentos.emit()
            self.ui.contenedor_paginas.setCurrentWidget(self.departamentos)
    
    def formulario_puestos(self):
        if self.ui.contenedor_paginas.currentWidget() != self.puestos:
            self.listar_departamentos_puestos.emit()
            self.ui.contenedor_paginas.setCurrentWidget(self.puestos)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = ControlSucursalesController()
    ui.show()
    sys.exit(app.exec())