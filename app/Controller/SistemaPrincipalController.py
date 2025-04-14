import sys
from PyQt5.QtCore import Qt, pyqtSignal
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
from .MensajesAlertasController import Mensaje

class SistemaPrincipal(QWidget):
    LISTAR_PROVEEDORES_VPROVEEDORES = pyqtSignal()
    LISTAR_CATEGORIAS_VPROVEEDORES = pyqtSignal()
    LIMPIAR_CAMPOS_PROVEEDORES = pyqtSignal()
    LISTAR_EMPLEADOS_VEMPLEADOS = pyqtSignal()
    LISTAR_PRODUCTOS_VPRODUCTOS = pyqtSignal()
    LISTAR_AREAS_VCLIENTES = pyqtSignal()
    LISTAR_CATEGORIAS_VCLIENTES = pyqtSignal()
    LISTAR_CLIENTES_VCLIENTES = pyqtSignal()
    def __init__(self, parent = None, datos_usuario = None):
        super().__init__(parent)
        self.ui = Ui_Principal_sistema()
        self.ui.setupUi(self)
        self.datos_usuario = datos_usuario
        
        Mensaje().mensaje_informativo(f'¡Quete encuentres de maravilla {self.datos_usuario["nombre_empleado"]}!\n¡Que tengas un excelente día y mucho éxito en tus ventas!')
        
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)
        self.showMaximized()
        self.setWindowTitle("RousPos")
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
        
        self.perfil= Perfil()
        self.venta= Venta()
        self.ventas= Ventas()
        self.compras= Compras()
        self.empleados= EmpleadosController(parent=self)
        self.proveedores= Control_proveedores(self)
        self.clientes= Clientes()
        self.productos= Productos(self, datos_usuario = self.datos_usuario)
        self.ui.w_cuerpo_contenido.addWidget(self.perfil)
        self.ui.w_cuerpo_contenido.addWidget(self.venta)
        self.ui.w_cuerpo_contenido.addWidget(self.ventas)
        self.ui.w_cuerpo_contenido.addWidget(self.compras)
        self.ui.w_cuerpo_contenido.addWidget(self.empleados)
        self.ui.w_cuerpo_contenido.addWidget(self.proveedores)
        self.ui.w_cuerpo_contenido.addWidget(self.clientes)
        self.ui.w_cuerpo_contenido.addWidget(self.productos)


        
    def mostrar_perfil(self, event):
        self.ui.w_cuerpo_contenido.setCurrentWidget(self.perfil)
    def mostrar_venta(self):
        self.ui.w_cuerpo_contenido.setCurrentWidget(self.venta)
    def mostrar_ventas(self):
        self.ui.w_cuerpo_contenido.setCurrentWidget(self.ventas)
    def mostrar_compras(self):
        self.ui.w_cuerpo_contenido.setCurrentWidget(self.compras)
    def mostrar_empleados(self):
        self.ui.w_cuerpo_contenido.setCurrentWidget(self.empleados)
        self.LISTAR_EMPLEADOS_VEMPLEADOS.connect(self.empleados.listar_empleados)
        self.LISTAR_EMPLEADOS_VEMPLEADOS.emit()
    def mostrar_proveedores(self):
        self.ui.w_cuerpo_contenido.setCurrentWidget(self.proveedores)
        self.LISTAR_PROVEEDORES_VPROVEEDORES.connect(self.proveedores.listar_proveedores_tabla)
        self.LISTAR_CATEGORIAS_VPROVEEDORES.connect(self.proveedores.mostrar_categorias)
        self.LIMPIAR_CAMPOS_PROVEEDORES.connect(self.proveedores.limpiar_campos)
        self.LIMPIAR_CAMPOS_PROVEEDORES.emit()
        self.LISTAR_PROVEEDORES_VPROVEEDORES.emit()
        self.LISTAR_CATEGORIAS_VPROVEEDORES.emit()
    def mostrar_clientes(self):
        self.ui.w_cuerpo_contenido.setCurrentWidget(self.clientes)
        self.LISTAR_AREAS_VCLIENTES.connect(self.clientes.listar_areas)
        self.LISTAR_CATEGORIAS_VCLIENTES.connect(self.clientes.listar_categorias)
        self.LISTAR_CLIENTES_VCLIENTES.connect(self.clientes.tabla_listar_clientes)
        self.LISTAR_AREAS_VCLIENTES.emit()
        self.LISTAR_CATEGORIAS_VCLIENTES.emit()
        self.LISTAR_CLIENTES_VCLIENTES.emit()
    def mostrar_productos(self):
        self.ui.w_cuerpo_contenido.setCurrentWidget(self.productos)
        self.LISTAR_PRODUCTOS_VPRODUCTOS.connect(self.productos.consultar_productos_db)
        self.LISTAR_PRODUCTOS_VPRODUCTOS.emit()
    
            
    def mostrar_sucursales(self):
        self.ventana_sucursales = ControlSucursalesController(self)
        self.ventana_sucursales.show()

