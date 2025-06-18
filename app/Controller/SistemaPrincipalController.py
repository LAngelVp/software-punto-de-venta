import sys
from datetime import datetime
from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QWidget, QDialog
from ..View.UserInterfacePy.UI_SISTEMA_PRINCIPAL import Ui_Principal_sistema
from ..Controller.ClientesController import Clientes
from ..Controller.PerfilUsuarioController import Perfil
from ..Controller.ComprasController import Compras
from ..Controller.ProveedoresController import Control_proveedores
from ..Controller.EmpleadosController import EmpleadosController
from ..Controller.VentaController import Venta
from ..Controller.VentasController import Ventas
from ..Controller.ProductosController import Productos
from ..Controller.ControlSucursalesController import ControlSucursalesController
from .MensajesAlertasController import Mensaje

class SistemaPrincipal(QWidget):
    LISTAR_PROVEEDORES_VPROVEEDORES = Signal()
    LISTAR_CATEGORIAS_VPROVEEDORES = Signal()
    LIMPIAR_CAMPOS_PROVEEDORES = Signal()
    LISTAR_EMPLEADOS_VEMPLEADOS = Signal()
    LISTAR_PRODUCTOS_VPRODUCTOS = Signal()
    LISTAR_AREAS_VCLIENTES = Signal()
    LISTAR_CATEGORIAS_VCLIENTES = Signal()
    LISTAR_CLIENTES_VCLIENTES = Signal()
    def __init__(self, parent = None, datos_usuario = None):
        super().__init__(parent)
        self.ventana_saludo = None
        self.ui = Ui_Principal_sistema()
        self.ui.setupUi(self)
        self.datos_usuario = datos_usuario
        
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.showFullScreen()
        self.setWindowTitle("Sistema de ventas")
        self.ui.btn_laterales_btn_sucursales.clicked.connect(self.mostrar_sucursales)
        
        self.ui.label_fotousuario.setCursor(Qt.PointingHandCursor)
        self.ui.label_fotousuario.mousePressEvent = self.mostrar_perfil

        self.ui.btn_laterales_proceso_venta.clicked.connect(self.mostrar_venta)
        self.ui.btn_laterales_ventas.clicked.connect(self.mostrar_ventas)
        self.ui.btn_laterales_compras.clicked.connect(self.mostrar_compras)
        self.ui.btn_laterales_empleados.clicked.connect(self.mostrar_empleados)
        self.ui.btn_laterales_proveedores.clicked.connect(self.mostrar_proveedores)
        self.ui.btn_laterales_clientes.clicked.connect(self.mostrar_clientes)
        self.ui.btn_laterales_productos.clicked.connect(self.mostrar_productos)

        self.ui.btc_cerrar_2.clicked.connect(lambda: sys.exit())
        self.ui.btc_minimizar_2.clicked.connect(lambda: self.showMinimized())
        
        self.ventana_sucursales = None
        self.perfil= Perfil()
        self.venta= Venta()
        self.ventas= Ventas()
        self.compras= Compras(parent = self, usuario = self.datos_usuario)
        self.clientes= Clientes(parent=self)
        self.empleados= EmpleadosController(parent=self)
        self.proveedores= Control_proveedores(parent=self)
        self.productos= Productos(parent=self, datos_usuario = self.datos_usuario)
        self.ui.w_cuerpo_contenido.addWidget(self.perfil)
        self.ui.w_cuerpo_contenido.addWidget(self.venta)
        self.ui.w_cuerpo_contenido.addWidget(self.ventas)
        self.ui.w_cuerpo_contenido.addWidget(self.compras)
        self.ui.w_cuerpo_contenido.addWidget(self.empleados)
        self.ui.w_cuerpo_contenido.addWidget(self.proveedores)
        self.ui.w_cuerpo_contenido.addWidget(self.clientes)
        self.ui.w_cuerpo_contenido.addWidget(self.productos)

    def mostrar_perfil(self, event):
        if self.ui.w_cuerpo_contenido.currentWidget() != self.perfil:
            self.ui.w_cuerpo_contenido.setCurrentWidget(self.perfil)
    def mostrar_venta(self):
        if self.ui.w_cuerpo_contenido.currentWidget() != self.venta:
            self.ui.w_cuerpo_contenido.setCurrentWidget(self.venta)
    def mostrar_ventas(self):
        if self.ui.w_cuerpo_contenido.currentWidget() != self.ventas:
            self.ui.w_cuerpo_contenido.setCurrentWidget(self.ventas)
    def mostrar_compras(self):
        if self.ui.w_cuerpo_contenido.currentWidget() != self.compras:
            self.ui.w_cuerpo_contenido.setCurrentWidget(self.compras)  
    def mostrar_empleados(self):
        if self.ui.w_cuerpo_contenido.currentWidget() != self.empleados:
            self.ui.w_cuerpo_contenido.setCurrentWidget(self.empleados)
            # self.LISTAR_EMPLEADOS_VEMPLEADOS.connect(self.empleados.listar_empleados)
            self.LISTAR_EMPLEADOS_VEMPLEADOS.emit()
    def mostrar_proveedores(self):
        if self.ui.w_cuerpo_contenido.currentWidget() != self.proveedores:
            self.ui.w_cuerpo_contenido.setCurrentWidget(self.proveedores)
            self.LISTAR_CATEGORIAS_VPROVEEDORES.connect(self.proveedores.mostrar_categorias)
            self.LIMPIAR_CAMPOS_PROVEEDORES.connect(self.proveedores.limpiar_campos)
            self.LISTAR_CATEGORIAS_VPROVEEDORES.emit()
        self.LIMPIAR_CAMPOS_PROVEEDORES.emit()
    def mostrar_clientes(self):
        if self.ui.w_cuerpo_contenido.currentWidget() != self.clientes:
            self.ui.w_cuerpo_contenido.setCurrentWidget(self.clientes)
            self.LISTAR_AREAS_VCLIENTES.connect(self.clientes.listar_areas)
            self.LISTAR_CATEGORIAS_VCLIENTES.connect(self.clientes.listar_categorias)
            # self.LISTAR_CLIENTES_VCLIENTES.connect(self.clientes.tabla_listar_clientes)
            self.LISTAR_AREAS_VCLIENTES.emit()
            self.LISTAR_CATEGORIAS_VCLIENTES.emit()
            # self.LISTAR_CLIENTES_VCLIENTES.emit()
    def mostrar_productos(self):
        if self.ui.w_cuerpo_contenido.currentWidget() != self.productos:
            self.ui.w_cuerpo_contenido.setCurrentWidget(self.productos)
            
    def mostrar_sucursales(self):
        if self.ventana_sucursales is None or not self.ventana_sucursales.isVisible:
            self.ventana_sucursales = ControlSucursalesController(parent=self)
            self.ventana_sucursales.VENTANA_CERRADA_SUCUDEPAPUES.connect(self.ventana_cerrada_sucudepapues)
            self.ventana_sucursales.show()
        else:
            self.ventana_sucursales.raise_()
            self.ventana_sucursales.activateWindow()

    def ventana_cerrada_sucudepapues(self):
        self.ventana_sucursales = None