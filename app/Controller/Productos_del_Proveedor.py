from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from ..View.UserInterfacePy.PRODUCTOS_PROVEEDORES import *
from .AjustarCajaOpcionesGlobal import *

class Productos_de_proveedorController(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_contenedor_productos_proveedores()
        self.ui.setupUi(self)
        
        pantalla = self.frameGeometry()
        pantalla.moveCenter(self.screen().availableGeometry().center())
        self.move(pantalla.topLeft())
        AjustarCajaOpciones().ajustar_cajadeopciones(self.ui.cajaopciones_filtro_nombre)
        AjustarCajaOpciones().ajustar_cajadeopciones(self.ui.cajaopciones_filtro_nombre_productos_del_sistema)