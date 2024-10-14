import sys
import os
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from app.View.UserInterfacePy.UI_SISTEMA_PRINCIPAL import *
from app.Controller.ClientesController import Clientes
from app.Controller.PerfilUsuarioController import *
from app.Controller.ComprasController import *
from app.Controller.ProveedoresController import Control_proveedores
from app.Controller.EmpleadosController import *
from app.Controller.VentaController import *
from app.Controller.VentasController import *
from app.Controller.ProductosController import *
from ControlSucursalesController import *



class SistemaPrincipal(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Principal_sistema()
        self.ui.setupUi(self)
        self.setWindowFlags(self.windowFlags() | Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.showFullScreen()
        
        
        self.p_inicial = 0
        self.p_venta = Venta()
        self.p_ventas = Ventas()
        self.p_compras = Compras()
        self.p_empleados = Empleados()
        self.p_proveedores = Control_proveedores()
        self.p_clientes = Clientes()
        self.p_perfil = Perfil()
        self.p_productos = Productos()

        self.ui.w_cuerpo_contenido.addWidget(self.p_clientes)
        self.ui.w_cuerpo_contenido.addWidget(self.p_perfil)
        self.ui.w_cuerpo_contenido.addWidget(self.p_compras)
        self.ui.w_cuerpo_contenido.addWidget(self.p_proveedores)
        self.ui.w_cuerpo_contenido.addWidget(self.p_empleados)
        self.ui.w_cuerpo_contenido.addWidget(self.p_venta)
        self.ui.w_cuerpo_contenido.addWidget(self.p_ventas)
        self.ui.w_cuerpo_contenido.addWidget(self.p_productos)

        self.ui.label_fotousuario.setCursor(QtCore.Qt.PointingHandCursor)
        self.ui.label_fotousuario.mousePressEvent = self.mostrar_perfil
        self.ui.btn_proceso_venta.clicked.connect(self.mostrar_venta)
        self.ui.btn_ventas.clicked.connect(self.mostrar_ventas)
        self.ui.btn_compras.clicked.connect(self.mostrar_compras)
        self.ui.btn_empleados.clicked.connect(self.mostrar_empleados)
        self.ui.btn_proveedores.clicked.connect(self.mostrar_proveedores)
        self.ui.btn_clientes.clicked.connect(self.mostrar_clientes)
        self.ui.btn_productos.clicked.connect(self.mostrar_productos)
        self.ui.btn_btn_sucursales.clicked.connect(self.control_de_sucursales)

        self.ui.btc_cerrar_2.clicked.connect(lambda:  sys.exit())
        self.ui.btc_minimizar_2.clicked.connect(lambda:  self.showMinimized())



        

    def mostrar_perfil(self, event):
        self.ui.w_cuerpo_contenido.setCurrentWidget(self.p_perfil)

    def mostrar_venta(self):
        self.ui.w_cuerpo_contenido.setCurrentWidget(self.p_venta)
    
    def mostrar_ventas(self):
        self.ui.w_cuerpo_contenido.setCurrentWidget(self.p_ventas)
    
    def mostrar_compras(self):
        self.ui.w_cuerpo_contenido.setCurrentWidget(self.p_compras)
    
    def mostrar_empleados(self):
        self.ui.w_cuerpo_contenido.setCurrentWidget(self.p_empleados)
    
    def mostrar_proveedores(self):
        self.ui.w_cuerpo_contenido.setCurrentWidget(self.p_proveedores)
    
    def mostrar_clientes(self):
        self.ui.w_cuerpo_contenido.setCurrentWidget(self.p_clientes)
    
    def mostrar_productos(self):
        self.ui.w_cuerpo_contenido.setCurrentWidget(self.p_productos)
    
    def control_de_sucursales(self):
        self.control_sucursales = ControlSucursalesController()
        self.control_sucursales.show()

    


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = SistemaPrincipal()
    ui.show()
    sys.exit(app.exec())