from .FuncionesAuxiliares import FuncionesAuxiliaresController
from ..Model.ProveedoresModel import ProveedoresModel
from ..DataBase.conexionBD import Conexion_base_datos
from PySide6 import QtCore, QtWidgets
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from ..View.UserInterfacePy.UI_CONTROL_COMPRAS import *
from ..View.UserInterfacePy.UI_CREAR_ORDEN_DE_COMPRA import *
from ..View.UserInterfacePy.UI_SELECCIONAR_PRODUCTOS_DEL_VENDEDOR import Ui_Seleccion_Productos_Proveedor

class Compras(QWidget):
    def __init__(self, parent = None, usuario = None):
        super().__init__(parent)
        self.usuario = usuario
        self.orden_compra = None
        self.ui = Ui_control_compras()
        self.ui.setupUi(self)
        self.clienteFisico = True
        self.ui.btn_btn_agregar.clicked.connect(self.nueva_orden_compra)
        
        
        

    def nueva_orden_compra(self):
        if self.orden_compra is None or not self.orden_compra.isVisible():
            self.orden_compra = Orden_compra(parent = self, usuario = self.usuario)
            self.orden_compra.VENTANA_CERRADA_NUEVA_COMPRA.connect(self.cerrar_ventana_orden_compra)
            self.orden_compra.show()
        else:
            self.orden_compra.raise_()
            self.orden_compra.activateWindow()
        
    def cerrar_ventana_orden_compra(self):
        self.orden_compra = None

class Orden_compra(QWidget):
    VENTANA_CERRADA_NUEVA_COMPRA = Signal()
    def __init__(self, parent = None, usuario = None):
        super().__init__(parent)
        self._ventanaCentradaNuevaCompra = False
        self.usuario = usuario
        self.proveedores = {}
        self.proveedor_id = None
        self.ventana_productos_proveedor = None
        self.ui = Ui_Orden_compra()
        self.ui.setupUi(self)
        self.ui.btn_btn_cerrar.clicked.connect(self.close)
        self.ui.btn_btn_productosProveedor.clicked.connect(self.mostrar_productos_proveedores)
        self.__obtener_proveedores()
        completar = QCompleter([proveedor.nombre for proveedor in self.proveedores.values()])
        completar.setCaseSensitivity(Qt.CaseInsensitive)
        self.ui.txt_buscarproveedor.setCompleter(completar)
        self.ui.txt_buscarproveedor.textChanged.connect(self.__proveedor_seleccionado)
        
    def mostrar_productos_proveedores(self):
        if self.ventana_productos_proveedor is None or not self.ventana_productos_proveedor.isVisible():
            self.ventana_productos_proveedor = SeleccionProductosProveedor(parent=self)
            self.ventana_productos_proveedor.exec_()
        else:
            self.ventana_productos_proveedor.raise_()
            self.ventana_productos_proveedor.activateWindow()
        
    def __obtener_proveedores(self):
        with Conexion_base_datos() as db:
            session = db.abrir_sesion()
            with session.begin():
                proveedores, estado = ProveedoresModel(session).obtener_proveedores()
            if estado:
                for proveedor in proveedores:
                    self.proveedores[proveedor.id] = proveedor
                    
    def __proveedor_seleccionado(self, texto):
        # Buscar el ID del proveedor por su nombre (valor) en el diccionario
        for id_proveedor, proveedor in self.proveedores.items():
            if proveedor.nombre == texto:
                self.proveedor_id = id_proveedor  # Asignamos el id correspondiente
                break
        else:
            self.proveedor_id = None
                    
    def showEvent(self, event):
        super().showEvent(event)
        if not self._ventanaCentradaNuevaCompra:
            FuncionesAuxiliaresController.centrar_en_padre(self)
            self._ventanaCentradaNuevaCompra = True
    
    def closeEvent(self, event):
        self.VENTANA_CERRADA_NUEVA_COMPRA.emit()
        event.accept()
        
class SeleccionProductosProveedor(QDialog):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.ui = Ui_Seleccion_Productos_Proveedor()
        self.ui.setupUi(self)
        self.setWindowFlags(self.windowFlags() | Qt.WindowType.FramelessWindowHint) 
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        
        pantalla = self.frameGeometry()
        pantalla.moveCenter(self.screen().availableGeometry().center())
        self.move(pantalla.topLeft())
        