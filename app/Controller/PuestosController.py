from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from ..View.UserInterfacePy.UI_ADMINISTRAR_PUESTOS import Ui_Formulario_puestos

class PuestosController(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Formulario_puestos()
        self.ui.setupUi(self)

        #//: EDICION
        self.ui.decimal_salario.setButtonSymbols(QSpinBox.NoButtons)
        self.ui.decimal_horaslaborales.setButtonSymbols(QSpinBox.NoButtons)
        self.ui.tiempo_horaentrada.setButtonSymbols(QSpinBox.NoButtons)
        self.ui.tiempo_horasalida.setButtonSymbols(QSpinBox.NoButtons)

        #botones:
        self.ui.btn_btn_agregar.clicked.connect(self.agregar)
        self.ui.btn_btn_eliminar.clicked.connect(self.eliminar)
        self.ui.btn_btn_buscarpuesto.clicked.connect(self.buscar_puesto)
        self.ui.btn_btn_vincular.clicked.connect(self.vincular_departamento)
        self.ui.btn_btn_desvincular.clicked.connect(self.desvincular_departamento)


    #funciones:
    def agregar(self):
        pass

    def eliminar(self):
        pass

    def buscar_puesto(self):
        pass

    def vincular_departamento(self):
        pass

    def desvincular_departamento(self):
        pass