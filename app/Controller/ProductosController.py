from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QValidator, QStandardItemModel, QStandardItem, QPixmap
from .FuncionesAuxiliares import *
from .AjustarCajaOpcionesGlobal import AjustarCajaOpciones
from ..DataBase.conexionBD import Conexion_base_datos
from ..Model.ProveedoresModel import ProveedoresModel
from ..Model.CategoriasModel import CategoriasModel
from ..Model.ProductosModel import ProductosModel
from .MensajesAlertasController import Mensaje
from .CategoriasController import CategoriasController
from ..View.UserInterfacePy.UI_CONTROL_PRODUCTOS import Ui_Control_Productos
from ..View.UserInterfacePy.UI_AGREGARPRODUCTO import Ui_contenedor_agregar_productos
from ..View.UserInterfacePy.UI_NUEVA_CATEGORIA import Ui_Nueva_categoria
from .PresentacionProductosController import PresentacionProductos
from .UnidadMedidaProductosController import UnidadMedidaProductos
                
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
        self.imagenProducto = None
#// funciones principales:
        self.__obtener_proveedores()
        completar = QCompleter(list(self.proveedores.values()))
        completar.setCaseSensitivity(Qt.CaseInsensitive)
        self.ui.txt_proveedor.setCompleter(completar)
#// señales:
        self.ui.txt_proveedor.textChanged.connect(self.__proveedor_seleccionado)
        self.ui.etiqueta_fotoProducto.mousePressEvent = self.cargar_imagen
#// botones de ventana:
        self.ui.btn_btn_actualizar_producto.clicked.connect(self.__actualizar_producto)
        self.ui.btn_btn_agregar_categoria.clicked.connect(self.__agregar_categoria)
        self.ui.btn_btn_agregar_unidadMedidaProducto.clicked.connect(self.agregar_unidad_medida)
        self.ui.btn_btn_agregarPresentacionProducto.clicked.connect(self.agregar_presentacion)
        self.ui.btn_btn_agregar_producto.clicked.connect(self.__agregar_producto)
        self.ui.btn_btn_eliminar_producto.clicked.connect(self.__eliminar_producto)
        self.ui.btn_btn_guardar_producto.clicked.connect(self.__guardar_producto)
        self.ui.btn_btn_cargar_CSVProductos.clicked.connect(self.agregarCSV)
        
#FUNCIONES-VENTANAS EMERGENTES: 
    def agregar_presentacion(self):
        self.ui_presentacion = PresentacionProductos()
        self.ui_presentacion.SYGNAL_PRESENTACION_AGREGADA.connect(self.listar_presentaciones_productos)
        self.ui_presentacion.show()

    def agregar_unidad_medida(self):
        self.ui_unidad_medida = UnidadMedidaProductos()
        self.ui_unidad_medida.SYGNAL_UNIDAD_MEDIDA_AGREGADA.connect(self.listar_unidades_medida)
        self.ui_unidad_medida.show()

    def __agregar_categoria(self):
        self.categoria = CategoriasController(tipo_categoria="productos")
        self.categoria.categoria_agregada_signal.connect(self.listar_categorias)
        self.categoria.show()

    def listar_presentaciones_productos(self):
        with Conexion_base_datos() as db:
            session = db.abrir_sesion()
            with session.begin():
                datos, estatus = ProductosModel(session).obtener_presentaciones()
            if estatus:
                self.ui.cajaOpciones_presentacionProducto.clear()
                for unidad in datos:
                    self.ui.cajaOpciones_presentacionProducto.addItem(unidad.nombre, unidad.id)
                AjustarCajaOpciones().ajustar_cajadeopciones(self.ui.cajaOpciones_presentacionProducto)

    def listar_unidades_medida(self):
        with Conexion_base_datos() as db:
            session = db.abrir_sesion()
            with session.begin():
                datos, estatus = ProductosModel(session).obtener_unidades_medida()
            if estatus:
                self.ui.cajaOpciones_unidadMedidaProducto.clear()
                for unidad in datos:
                    self.ui.cajaOpciones_unidadMedidaProducto.addItem(unidad.unidad_medida, unidad.id)
                AjustarCajaOpciones().ajustar_cajadeopciones(self.ui.cajaOpciones_unidadMedidaProducto)

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
#########################
#FUNCIONES-INTERACCION CON EL PRODUCTO

    def cargar_imagen(self, event):
        options = QFileDialog.Options()
        self.imagenProducto, _ = QFileDialog.getOpenFileName(self, 'SELECCIONA UNA IMAGEN', ' ', 'Archivo de Imagen (*.png *.jpg *.jpeg);; Todos los archivos (*)', options=options)
        image_accept = size_validator_image(self.imagenProducto)
        if self.imagenProducto:
            if image_accept:
                self.ui.etiqueta_fotoProducto.setText(self.imagenProducto)
                pixmap = QPixmap(self.imagenProducto)
                self.ui.etiqueta_fotoProducto.setPixmap(pixmap)
                self.ui.etiqueta_fotoProducto.setScaledContents(True)
                self.ui.etiqueta_fotoProducto.adjustSize()
            else:
                Mensaje().mensaje_alerta("El tamaño de la imagen sobre pasa los 5Mb")
        return
    
    def datos_campos(self):
        # Crear un diccionario para almacenar los valores de los campos
        datos = {
            "proveedor": self.ui.txt_proveedor.text().strip().upper(),
            "codigo_barras": self.ui.txt_codBarras.text().strip().upper(),
            "categoria_producto": self.ui.cajaOpciones_categoriaProducto.currentData(),
            "marca_producto": self.ui.txt_marcaProducto.text().strip().upper(),
            "modelo_producto": self.ui.txt_modeloProducto.text().strip().upper(),
            "color_producto": self.ui.txt_colorProducto.text().strip().upper(),
            "material_producto": self.ui.txt_materialProducto.text().strip().upper(),
            "unidad_medida_producto": self.ui.cajaOpciones_unidadMedidaProducto.currentData(),
            "presentacion_producto": self.ui.cajaOpciones_presentacionProducto.currentData(),
            "costo_inicial_producto": self.ui.decimal_costoInicialProducto.value(),
            "precio_venta_producto": self.ui.decimal_precioVentaProducto.value(),
            "costo_final_producto": self.ui.decimal_costoFinalProducto.value(),
            "existencia_producto": self.ui.decimal_existenciaProducto.value(),
            "existencia_min_producto": self.ui.decimal_existenciaMinProducto.value(),
            "existencia_max_producto": self.ui.decimal_existenciaMaxProducto.value(),
            "peso_producto": self.ui.decimal_pesoProducto.value(),
            "largo_dimensiones": self.ui.decimal_largoDimensiones.value(),
            "alto_dimensiones": self.ui.decimal_altoDimensiones.value(),
            "ancho_dimensiones": self.ui.decimal_anchoDimensiones.value(),
            "descripcion_producto": self.ui.txtlargo_descripcionProducto.toPlainText(),
            "notas_producto": self.ui.txtlargo_notasProducto.toPlainText(),
            "fecha_vencimiento_producto": self.ui.fecha_vencimientoProducto.date().toString('yyyy-MM-dd'),
            "fecha_fabricacion_producto": self.ui.fecha_fabricacionProducto.date().toString('yyyy-MM-dd')
        }
        
        # Retornar el diccionario con los valores
        return datos
        
        
    def __agregar_producto(self):
        datos = self.datos_campos()
        if not datos["codigo_barras"]:
            Mensaje().mensaje_alerta("El campo Código de Barras es obligatorio")
            return
        
        if not hasattr(self, 'modelo_tabla_productos'):
                self.modelo_tabla_productos = QStandardItemModel()
            
        # self.model.clear()
        self.modelo_tabla_productos.setHorizontalHeaderLabels([
            "Proveedor", "Código de Barras", "Categoría", "Marca", "Modelo", "Color", 
            "Material", "Unidad de Medida", "Presentación", "Costo Inicial", "Precio Venta", 
            "Costo Final", "Existencia", "Existencia Min", "Existencia Max", "Peso", 
            "Largo Dimensiones", "Alto Dimensiones", "Ancho Dimensiones", 
            "Descripción", "Notas", "Fecha Vencimiento", "Fecha Fabricación"
        ])
        self.ui.tabla_productos.setModel(self.modelo_tabla_productos)
        
        nueva_fila = [
            datos["proveedor"], datos["codigo_barras"], datos["categoria_producto"],
            datos["marca_producto"], datos["modelo_producto"], datos["color_producto"],
            datos["material_producto"], datos["unidad_medida_producto"], datos["presentacion_producto"],
            datos["costo_inicial_producto"], datos["precio_venta_producto"], datos["costo_final_producto"],
            datos["existencia_producto"], datos["existencia_min_producto"], datos["existencia_max_producto"],
            datos["peso_producto"], datos["largo_dimensiones"], datos["alto_dimensiones"], 
            datos["ancho_dimensiones"], datos["descripcion_producto"], datos["notas_producto"],
            datos["fecha_vencimiento_producto"], datos["fecha_fabricacion_producto"]
        ]
        
        self._agregar_fila_a_tabla(nueva_fila)

    def _agregar_fila_a_tabla(self, fila):
        # Convertir cada elemento de la fila en un QStandardItem y añadirlo al modelo
        items = [QStandardItem(str(dato)) for dato in fila]

        # Añadir la fila al modelo de datos
        self.modelo_tabla_productos.appendRow(items)

    def __actualizar_producto(self):
        pass

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
            
    def agregarCSV(self):
        pass
    

class Productos(QWidget):
    LISTAR_CATEGORIAS_PRODUCTOS = pyqtSignal()
    LISTAR_UNIDADES_MEDIDA_PRODUCTOS = pyqtSignal()
    LISTAR_PRESENTACIONES_PRODUCTOS = pyqtSignal()
    def __init__(self):
        super().__init__()
        self.ui = Ui_Control_Productos()
        self.ui.setupUi(self)
        self.ui.btn_btn_agregar.clicked.connect(self.agregar_producto)
    
    def agregar_producto(self):
        self.AdminProductos = Admin_productosController()
        self.LISTAR_CATEGORIAS_PRODUCTOS.connect(self.AdminProductos.listar_categorias)
        self.LISTAR_UNIDADES_MEDIDA_PRODUCTOS.connect(self.AdminProductos.listar_unidades_medida)
        self.LISTAR_PRESENTACIONES_PRODUCTOS.connect(self.AdminProductos.listar_presentaciones_productos)
        self.LISTAR_CATEGORIAS_PRODUCTOS.emit()
        self.LISTAR_UNIDADES_MEDIDA_PRODUCTOS.emit()
        self.LISTAR_PRESENTACIONES_PRODUCTOS.emit()
        self.AdminProductos.show()
        
        

            

                