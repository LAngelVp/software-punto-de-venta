import sys
from .FuncionesAuxiliares import FuncionesAuxiliaresController
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from ..Source.iconsdvg_rc import *
from app.View.UserInterfacePy.UI_CONTROL_SUCUDEPAPUESTO import Ui_Control_SucursalesDepartamentosPuestos

from app.Controller.SucursalesController import SucursalesController
from app.Controller.DepartamentosController import DepartamentosController
from app.Controller.PuestosController import PuestosController

class ControlSucursalesController(QDialog):
    listar_sucursales = pyqtSignal(set)
    listar_departamentos = pyqtSignal()
    listar_departamentos_puestos = pyqtSignal()
    VENTANA_CERRADA_SUCUDEPAPUES = pyqtSignal()
    def __init__(self, parent = None):
        super().__init__(parent)
        self._ventanaCentradaSucuDepaPues = False
        self.ui = Ui_Control_SucursalesDepartamentosPuestos()
        self.ui.setupUi(self)
        self.setWindowTitle("Administración de sucursales, puestos y departamentos")
        icon = QIcon(':Icons/IconosSVG/sucursales.png')
        self.setWindowIcon(icon)
        self.setWindowTitle("Administración de puestos")
        
        # pantalla = self.frameGeometry()
        # pantalla.moveCenter(self.screen().availableGeometry().center())
        # self.move(pantalla.topLeft())
        

        self.sucursales = SucursalesController(parent=self,cabecera=False)
        self.departamentos = DepartamentosController(parent=self, cabecera=False)
        self.puestos = PuestosController(parent=self, cabecera=False)


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
        
    def showEvent(self, event):
        super().showEvent(event)
        if not self._ventanaCentradaSucuDepaPues:
            FuncionesAuxiliaresController.centrar_en_padre(self)
            self._ventanaCentradaSucuDepaPues = True

    def closeEvent(self, event):
        self.VENTANA_CERRADA_SUCUDEPAPUES.emit() 
        event.accept()

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
