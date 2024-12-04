from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from ..DataBase.conexionBD import Conexion_base_datos
from ..Model.ProveedoresModel import ProveedoresModel
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
#// EDICION DE COMPONENTES:
        self.ui.decimal_altoDimensiones.setButtonSymbols(QSpinBox.NoButtons)
        self.ui.decimal_anchoDimensiones.setButtonSymbols(QSpinBox.NoButtons)
        self.ui.decimal_costoFinalProducto.setButtonSymbols(QSpinBox.NoButtons)
        self.ui.decimal_costoInicialProducto.setButtonSymbols(QSpinBox.NoButtons)
        self.ui.decimal_existenciaMaxProducto.setButtonSymbols(QSpinBox.NoButtons)
        self.ui.decimal_existenciaMinProducto.setButtonSymbols(QSpinBox.NoButtons)
        self.ui.decimal_existenciaProducto.setButtonSymbols(QSpinBox.NoButtons)
        self.ui.decimal_largoDimensiones.setButtonSymbols(QSpinBox.NoButtons)
        self.ui.decimal_precioVentaProducto.setButtonSymbols(QSpinBox.NoButtons)
        self.ui.decimal_pesoProducto.setButtonSymbols(QSpinBox.NoButtons)
        self.ui.fecha_fabricacionProducto.setDate(QDate.currentDate())
        self.ui.fecha_vencimientoProducto.setDate(QDate.currentDate())
        
        pantalla = self.frameGeometry()
        pantalla.moveCenter(self.screen().availableGeometry().center())
        self.move(pantalla.topLeft())
        
        self.proveedores = {}
        self.id_proveedor = None
        
        self.__obtener_proveedores()
        
        completar = QCompleter(list(self.proveedores.values()))  # Usamos los valores (nombres)
        completar.setCaseSensitivity(Qt.CaseInsensitive)  # Usamos CaseInsensitive o CaseSensitive, no `Qt.CaseSensitivity`
        self.ui.txt_proveedor.setCompleter(completar)
        
        self.ui.txt_proveedor.textChanged.connect(self.proveedor_seleccionado)
        
    def __obtener_proveedores(self):
        with Conexion_base_datos() as db:
            session = db.abrir_sesion()
            with session.begin():
                proveedores, estado = ProveedoresModel(session).obtener_proveedores()
            if estado:
                for proveedor in proveedores:
                    self.proveedores[proveedor.id] = proveedor.nombre
                    
    def proveedor_seleccionado(self, texto):
        # Buscar el ID del proveedor por su nombre (valor) en el diccionario
        for id_proveedor, nombre in self.proveedores.items():
            if nombre == texto:
                self.proveedor_id = id_proveedor  # Asignamos el id correspondiente
                print(f"Proveedor seleccionado: {nombre}, ID: {self.proveedor_id}")
                break
        else:
            self.proveedor_id = None 