import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget
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

class SistemaPrincipal(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Principal_sistema()
        self.ui.setupUi(self)
        
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.showFullScreen()

        # Instanciación de los controladores
        self.controladores = {
            "perfil": Perfil(),
            "venta": Venta(),
            "ventas": Ventas(),
            "compras": Compras(),
            "empleados": EmpleadosController(),
            "proveedores": Control_proveedores(),
            "clientes": Clientes(),
            "productos": Productos(),
            "sucursales": ControlSucursalesController()
        }

        # Añadir los widgets al contenedor
        self._agregar_widgets()

        # Conexiones de señales
        self._conectar_señales()

    def _agregar_widgets(self):
        for widget in self.controladores.values():
            self.ui.w_cuerpo_contenido.addWidget(widget)

    def _conectar_señales(self):
        self.ui.label_fotousuario.setCursor(Qt.PointingHandCursor)
        self.ui.label_fotousuario.mousePressEvent = self.mostrar_perfil

        self.ui.btn_proceso_venta.clicked.connect(lambda: self.mostrar_contenido("venta"))
        self.ui.btn_ventas.clicked.connect(lambda: self.mostrar_contenido("ventas"))
        self.ui.btn_compras.clicked.connect(lambda: self.mostrar_contenido("compras"))
        self.ui.btn_empleados.clicked.connect(lambda: self.mostrar_contenido("empleados"))
        self.ui.btn_proveedores.clicked.connect(lambda: self.mostrar_contenido("proveedores"))
        self.ui.btn_clientes.clicked.connect(lambda: self.mostrar_contenido("clientes"))
        self.ui.btn_productos.clicked.connect(lambda: self.mostrar_contenido("productos"))
        self.ui.btn_btn_sucursales.clicked.connect(self.controladores["sucursales"].show)

        self.ui.btc_cerrar_2.clicked.connect(lambda: sys.exit())
        self.ui.btc_minimizar_2.clicked.connect(lambda: self.showMinimized())

    def mostrar_perfil(self, event):
        self.mostrar_contenido("perfil")

    def mostrar_contenido(self, contenido):
        """Muestra el widget correspondiente en el área de contenido."""
        widget = self.controladores.get(contenido)
        if widget:
            self.ui.w_cuerpo_contenido.setCurrentWidget(widget)
