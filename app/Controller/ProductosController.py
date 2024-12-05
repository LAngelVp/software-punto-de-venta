from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from .AjustarCajaOpcionesGlobal import AjustarCajaOpciones
from ..DataBase.conexionBD import Conexion_base_datos
from ..Model.ProveedoresModel import ProveedoresModel
from ..Model.CategoriaProductoModel import CategoriaProductoModel
from .MensajesAlertasController import Mensaje
from ..View.UserInterfacePy.UI_CONTROL_PRODUCTOS import Ui_Control_Productos
from ..View.UserInterfacePy.UI_AGREGARPRODUCTO import Ui_contenedor_agregar_productos
from ..View.UserInterfacePy.UI_NUEVA_CATEGORIA import Ui_Nueva_categoria


class CategoriaProductoController(QWidget):
    categoria_agregada = pyqtSignal()
    def __init__(self):
        super().__init__()
        self.ui = Ui_Nueva_categoria()
        self.ui.setupUi(self)
        self.ui.btn_btn_guardar.clicked.connect(self.__agregar_categoria)
        
    def __agregar_categoria(self):
        pass
        nombre = self.ui.txt_nombre.text().upper().strip()
        descripcion = self.ui.txtlargo_descripcion.toPlainText().strip().upper()
        if not nombre or not descripcion:
            Mensaje().mensaje_informativo("Debes de ingresar información del nombre de la categoria y la descripción para poder agregarla.")
            return
        with Conexion_base_datos() as db:
            session = db.abrir_sesion()
            with session.begin():
                categoria, estatus = CategoriaProductoModel(session).agregar(nombre, descripcion)
            if estatus:
                Mensaje().mensaje_informativo("Se registro la categoria con exito.")
                self.categoria_agregada.emit()
                self.close()
                
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
        
        pantalla = self.frameGeometry()
        pantalla.moveCenter(self.screen().availableGeometry().center())
        self.move(pantalla.topLeft())
#// variables globales:
        self.proveedores = {}
        self.id_proveedor = None
#// funciones principales:
        self.__obtener_proveedores()
        
        completar = QCompleter(list(self.proveedores.values()))  # Usamos los valores (nombres)
        completar.setCaseSensitivity(Qt.CaseInsensitive)  # Usamos CaseInsensitive o CaseSensitive, no `Qt.CaseSensitivity`
        self.ui.txt_proveedor.setCompleter(completar)
#// señales:
        self.ui.txt_proveedor.textChanged.connect(self.__proveedor_seleccionado)
#// botones de ventana:
        self.ui.btn_btn_actualizar_producto.clicked.connect(self.__actualizar_producto)
        self.ui.btn_btn_agregar_categoria.clicked.connect(self.__agregar_categoria)
        self.ui.btn_btn_agregar_producto.clicked.connect(self.__agregar_producto)
        self.ui.btn_btn_eliminar_producto.clicked.connect(self.__eliminar_producto)
        self.ui.btn_btn_guardar_producto.clicked.connect(self.__guardar_producto)
    def listar_categorias(self):
        with Conexion_base_datos() as db:
            session = db.abrir_sesion()
            with session.begin():
                categorias, estatus = CategoriaProductoModel(session).obtener_todo()
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
        self.categoria = CategoriaProductoController()
        self.categoria.categoria_agregada.connect(self.listar_categorias)
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
                print(f"Proveedor seleccionado: {nombre}, ID: {self.proveedor_id}")
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
        
        

            

                