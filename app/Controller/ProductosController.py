from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from ..View.UserInterfacePy.UI_CONTROL_PRODUCTOS import *
from ..View.UserInterfacePy.UI_AGREGARPRODUCTO import *

class Productos(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Control_Productos()
        self.ui.setupUi(self)
        self.ui.btn_btn_agregar.clicked.connect(self.agregar_producto)
        
    def agregar_producto(self):
        self.agregar_producto = Admin_productos()
        self.agregar_producto.show()
        
        
class Admin_productos(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_contenedor_agregar_productos()
        self.ui.setupUi(self)
        
        pantalla = self.frameGeometry()
        pantalla.moveCenter(self.screen().availableGeometry().center())
        self.move(pantalla.topLeft())