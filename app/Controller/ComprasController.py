from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from ..View.UserInterfacePy.UI_CONTROL_COMPRAS import *
from ..View.UserInterfacePy.UI_CREAR_ORDEN_DE_COMPRA import *

class Compras(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_control_compras()
        self.ui.setupUi(self)
        self.clienteFisico = True
        self.ui.btn_btn_agregar.clicked.connect(self.nueva_orden_compra)

    def nueva_orden_compra(self):
        self.orden_compra = Orden_compra()
        self.orden_compra.show()

class Orden_compra(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Orden_compra()
        self.ui.setupUi(self)