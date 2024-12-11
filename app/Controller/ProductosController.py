from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QValidator
from .AjustarCajaOpcionesGlobal import AjustarCajaOpciones
from ..DataBase.conexionBD import Conexion_base_datos
from ..Model.ProveedoresModel import ProveedoresModel
from ..Model.CategoriasModel import CategoriasModel
from .MensajesAlertasController import Mensaje
from .CategoriasController import CategoriasController
from ..View.UserInterfacePy.UI_CONTROL_PRODUCTOS import Ui_Control_Productos
from ..View.UserInterfacePy.UI_AGREGARPRODUCTO import Ui_contenedor_agregar_productos
from ..View.UserInterfacePy.UI_NUEVA_CATEGORIA import Ui_Nueva_categoria
from .AgregarUnDatoCombobox import FormularioAgregarDatoCombobox
                
class Admin_productosController(QWidget):
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
        self.ui.txt_codBarras.setFocus()
        
        pantalla = self.frameGeometry()
        pantalla.moveCenter(self.screen().availableGeometry().center())
        self.move(pantalla.topLeft())
        
#// Validaciones:
        self.ui.txt_codBarras.setMaxLength(255)
        self.ui.txt_nombreProducto.setMaxLength(255)
        self.ui.txt_marcaProducto.setMaxLength(100)
        self.ui.txt_modeloProducto.setMaxLength(50)
        self.ui.txt_colorProducto.setMaxLength(20)
        self.ui.txt_materialProducto.setMaxLength(255)
        
#// variables globales:
        self.proveedores = {}
        self.id_proveedor = None
#// funciones principales:
        self.__obtener_proveedores()
        completar = QCompleter(list(self.proveedores.values()))
        completar.setCaseSensitivity(Qt.CaseInsensitive)
        self.ui.txt_proveedor.setCompleter(completar)
#// señales:
        self.ui.txt_proveedor.textChanged.connect(self.__proveedor_seleccionado)
#// botones de ventana:
        self.ui.btn_btn_actualizar_producto.clicked.connect(self.__actualizar_producto)
        self.ui.btn_btn_agregar_categoria.clicked.connect(self.__agregar_categoria)
        self.ui.btn_btn_agregar_producto.clicked.connect(self.__agregar_producto)
        self.ui.btn_btn_eliminar_producto.clicked.connect(self.__eliminar_producto)
        self.ui.btn_btn_guardar_producto.clicked.connect(self.__guardar_producto)
        self.ui.btn_btn_agregar_unidadMedidaProducto.clicked.connect(self.agregar_elemento)
        self.ui.btn_btn_agregarPresentacionProducto.clicked.connect(self.agregar_elemento)
        
        
    def agregar_elemento(self):
        self.ui = FormularioAgregarDatoCombobox()
        self.ui.show()
    def listar_categorias(self):
        with Conexion_base_datos() as db:
            session = db.abrir_sesion()
            with session.begin():
                categorias, estatus = CategoriasModel(session).obtener_todo(tipo_categoria="productos")
                
            if estatus:
                self.ui.cajaOpciones_categoriaProducto.clear()
                for categoria in categorias:
                    self.ui.cajaOpciones_categoriaProducto.addItem(categoria.nombre, categoria.id)
                AjustarCajaOpciones().ajustar_cajadeopciones(self.ui.cajaOpciones_categoriaProducto)
                    
    def __actualizar_producto(self):
        pass
    def __agregar_producto(self):
        pass
    def __agregar_categoria(self):
        self.categoria = CategoriasController(tipo_categoria="productos")
        self.categoria.categoria_agregada_signal.connect(self.listar_categorias)
        self.categoria.show()
        
    def __eliminar_producto(self):
        pass
    def __guardar_producto(self):
        pass
    def __obtener_proveedores(self):
        with Conexion_base_datos() as db:
            session = db.abrir_sesion()
            with session.begin():
                proveedores, estado = ProveedoresModel(session).obtener_proveedores()
            if estado:
                for proveedor in proveedores:
                    self.proveedores[proveedor.id] = proveedor.nombre
                    
    def __proveedor_seleccionado(self, texto):
        # Buscar el ID del proveedor por su nombre (valor) en el diccionario
        for id_proveedor, nombre in self.proveedores.items():
            if nombre == texto:
                self.proveedor_id = id_proveedor  # Asignamos el id correspondiente
                break
        else:
            self.proveedor_id = None

class Productos(QWidget):
    LISTAR_CATEGORIAS_PRODUCTOS = pyqtSignal()
    def __init__(self):
        super().__init__()
        self.ui = Ui_Control_Productos()
        self.ui.setupUi(self)
        self.ui.btn_btn_agregar.clicked.connect(self.agregar_producto)
        self.AdminProductos = Admin_productosController()
        self.LISTAR_CATEGORIAS_PRODUCTOS.connect(self.AdminProductos.listar_categorias)
    
    def agregar_producto(self):
        self.LISTAR_CATEGORIAS_PRODUCTOS.emit()
        self.AdminProductos.show()
        
        

            

                