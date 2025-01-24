from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from ..DataBase.conexionBD import Conexion_base_datos
from ..Model.ProductosModel import ProductosModel
from ..Model.ProveedoresModel import ProveedoresModel
from ..View.UserInterfacePy.PRODUCTOS_PROVEEDORES import *
from .AjustarCajaOpcionesGlobal import *
from .MensajesAlertasController import Mensaje
class Productos_de_proveedorController(QWidget):
    PRODUCTO_DE_PROVEEDOR_SELECCIONADO_SIGNAL = pyqtSignal(object)
    PRODUCTO_DE_SISTEMA_SELECCIONADO_SIGNAL=pyqtSignal(object)
    PRODUCTO_A_VINCULAR_SELECCIONADO_SIGNAL=pyqtSignal(object)
    def __init__(self, proveedor):
        super().__init__()
        self.ui = Ui_contenedor_productos_proveedores()
        self.ui.setupUi(self)
        self.proveedor = proveedor
        pantalla = self.frameGeometry()
        pantalla.moveCenter(self.screen().availableGeometry().center())
        self.move(pantalla.topLeft())
        self.ui.btn_btn_eliminar_producto_del_proveedor.clicked.connect(self.eliminar_producto_del_proveedor_metodo)
        self.ui.txt_nombre_productodelsistema.returnPressed.connect(self.filtrar_productos_sistema)
        self.ui.txt_nombre_producto.returnPressed.connect(self.filtrar_productos_de_proveedor)
        AjustarCajaOpciones().ajustar_cajadeopciones(self.ui.cajaopciones_filtro_nombre)
        AjustarCajaOpciones().ajustar_cajadeopciones(self.ui.cajaopciones_filtro_nombre_productos_del_sistema)
        self.seleccion_conectada_productos = False
        self.producto_seleccionado = None
        self.seleccion_conectada_productos_sistema=False
        producto_seleccionado_sistema=None
        self.producto_seleccionado_a_vincular = None
        self.seleccion_conectada_productos_a_vincular = False
        self.lista_productos_para_vincular = set()
        self.productos_de_sistema()
        
        if not self.proveedor:
            return
        
        self.ui.etiqueta_nombre_del_proveedor.setText(f'Nombre del Proveedor: {self.proveedor.nombre}')
        self.mostrar_productos_proveedor()
        
        self.PRODUCTO_DE_PROVEEDOR_SELECCIONADO_SIGNAL.connect(self.eliminar_producto_del_proveedor_metodo)
        
        self.PRODUCTO_DE_SISTEMA_SELECCIONADO_SIGNAL.connect(self.vincular_producto_al_proveedor_metodo)
        
        self.PRODUCTO_A_VINCULAR_SELECCIONADO_SIGNAL.connect(self.quitar_producto_para_vincular)
        
    def mostrar_productos_proveedor(self):
        if not self.proveedor:
            return
        self.productos_proveedores_tabla(self.proveedor.productos)
    
    def productos_proveedores_tabla(self, productos=None):
        try:
            if self.ui.tabla_productos_del_proveedor is None:
                return
            # Inicializar el modelo correctamente
            if not hasattr(self, 'modelo_tabla_productos_del_proveedor'):
                self.modelo_tabla_productos_del_proveedor = QStandardItemModel()
            
            # Limpiar el modelo y resetear cabeceras
            self.modelo_tabla_productos_del_proveedor.clear()
            self.modelo_tabla_productos_del_proveedor.setHorizontalHeaderLabels(["Codigo", "Nombre","Descripción", "Precio Proveedor"])
            
            if  not productos:
                self.ui.tabla_productos_del_proveedor.setModel(self.modelo_tabla_productos_del_proveedor)
                return
            
            # Rellenar la tabla con los productos
            for producto in productos:
                if producto is not None:
                    # Crear los datos para cada fila
                    fila = [
                        str(producto.codigo_upc),
                        producto.nombre_producto,
                        producto.descripcion_producto,
                    ]
                    
                    # Crear los QStandardItems para la fila
                    items = [QStandardItem(item) for item in fila]
                    for item in items:
                        item.setData(producto, Qt.UserRole)
                    self.modelo_tabla_productos_del_proveedor.appendRow(items)
            
            self.ui.tabla_productos_del_proveedor.setModel(self.modelo_tabla_productos_del_proveedor)

            # Desconectar la señal antes de conectar
            if self.seleccion_conectada_productos:
                self.ui.tabla_productos_del_proveedor.selectionModel().currentChanged.disconnect(self.obtener_elemento_seleccionado_productos)
            
            self.ui.tabla_productos_del_proveedor.selectionModel().currentChanged.connect(self.obtener_elemento_seleccionado_productos)
            self.seleccion_conectada_productos = True
            
        except Exception as e:
            print(f'Error en productos_proveedores_tabla: {e}')
            
    def obtener_elemento_seleccionado_productos(self, current, previus):
        # Verifica si la celda seleccionada está en la primera columna
        if current.column() >= 0:  # Verifica si es la primera columna
            indice_fila = current.row()
            elemento = self.modelo_tabla_productos_del_proveedor.item(indice_fila, 0)
            if elemento is not None:
                producto = elemento.data(Qt.UserRole)
                if producto:
                    self.producto_seleccionado = producto
                    self.PRODUCTO_DE_PROVEEDOR_SELECCIONADO_SIGNAL.emit(self.producto_seleccionado)
            else:
                return
    
    def filtrar_productos_de_proveedor(self):
        nombre_producto = self.ui.txt_nombre_producto.text().upper().strip()
        id_proveedor = self.proveedor.id
        with Conexion_base_datos() as db:
            session = db.abrir_sesion()
            with session.begin():
                if self.ui.cajaopciones_filtro_nombre.currentText() .lower()== "igual a":
                    productos, estatus = ProveedoresModel(session).filtrar_productos_del_proveedor_exacto_nombre(proveedor_id=id_proveedor, nombre=nombre_producto)
                # else:
                #     productos, estatus = ProductosModel(session).consultar_por_nombre(nombre=nombre)
            if estatus:
                self.productos_proveedores_tabla(productos)
    
    def filtrar_productos_sistema(self):
        nombre = self.ui.txt_nombre_productodelsistema.text().upper().strip()
        with Conexion_base_datos() as db:
            session = db.abrir_sesion()
            with session.begin():
                if self.ui.cajaopciones_filtro_nombre_productos_del_sistema.currentText() .lower()== "igual a":
                    productos, estatus = ProductosModel(session).consultar_por_nombre_exacto(nombre=nombre)
                else:
                    productos, estatus = ProductosModel(session).consultar_por_nombre(nombre=nombre)
            if estatus:
                self.productos_del_sistema_tabla(productos)
    
    def productos_de_sistema(self):
        productos_del_sistema = None
        with Conexion_base_datos() as db:
            session = db.abrir_sesion()
            with session.begin():
                productos_del_sistema, estatus = ProductosModel(session).obtener_productos()
            if estatus:
                self.productos_del_sistema_tabla(productos_del_sistema)
                
    def productos_del_sistema_tabla(self, productos):
        try:
            if self.ui.tabla_productos_del_sistema is None:
                return
            # Inicializar el modelo correctamente
            if not hasattr(self, 'modelo_tabla_productos_del_sistema'):
                self.modelo_tabla_productos_del_sistema = QStandardItemModel()
            
            # Limpiar el modelo y resetear cabeceras
            self.modelo_tabla_productos_del_sistema.clear()
            self.modelo_tabla_productos_del_sistema.setHorizontalHeaderLabels(["Codigo", "Nombre","Descripción"])
            
            # if not hasattr(self.proveedor, 'productos') or not self.proveedor.productos:
            #     self.ui.tabla_productos_del_sistema.setModel(self.modelo_tabla_productos_del_sistema)
            #     return
            
            # Rellenar la tabla con los productos
            for producto in productos:
                if producto is not None:
                    # Crear los datos para cada fila
                    fila = [
                        str(producto.codigo_upc),
                        producto.nombre_producto,
                        producto.descripcion_producto,
                    ]
                    
                    # Crear los QStandardItems para la fila
                    items = [QStandardItem(item) for item in fila]
                    for item in items:
                        item.setData(producto, Qt.UserRole)
                    self.modelo_tabla_productos_del_sistema.appendRow(items)
            
            self.ui.tabla_productos_del_sistema.setModel(self.modelo_tabla_productos_del_sistema)

            # Desconectar la señal antes de conectar
            if self.seleccion_conectada_productos_sistema:
                self.ui.tabla_productos_del_sistema.selectionModel().currentChanged.disconnect(self.obtener_elemento_seleccionado_productos_sistema)
            
            self.ui.tabla_productos_del_sistema.selectionModel().currentChanged.connect(self.obtener_elemento_seleccionado_productos_sistema)
            self.seleccion_conectada_productos_sistema = True
            
        except Exception as e:
            print(f'Error en productos_proveedores_tabla: {e}')
    
    def obtener_elemento_seleccionado_productos_sistema(self, current, previus):
        if current.column() >= 0:  # Verifica si es la primera columna
            indice_fila = current.row()
            elemento = self.modelo_tabla_productos_del_sistema.item(indice_fila, 0)
            if elemento is not None:
                producto = elemento.data(Qt.UserRole)
                if producto:
                    self.producto_seleccionado_sistema = producto
                    self.PRODUCTO_DE_SISTEMA_SELECCIONADO_SIGNAL.emit(self.producto_seleccionado_sistema)
            else:
                return
    
    def vincular_producto_al_proveedor_metodo(self, producto):
        if not producto:
            Mensaje().mensaje_alerta(f"No se esta pasando el producto al seleccionarlo.")
            return
        self.lista_productos_para_vincular.add(producto)
        self.producto_para_vincular_tabla(self.lista_productos_para_vincular)
        print(self.lista_productos_para_vincular)
        
    def producto_para_vincular_tabla(self, productos):
        try:
            if self.ui.tabla_Productos_A_VincularProveedor is None:
                return
            # Inicializar el modelo correctamente
            if not hasattr(self, 'modelo_tabla_Productos_A_VincularProveedor'):
                self.modelo_tabla_Productos_A_VincularProveedor = QStandardItemModel()
            
            # Limpiar el modelo y resetear cabeceras
            self.modelo_tabla_Productos_A_VincularProveedor.clear()
            self.modelo_tabla_Productos_A_VincularProveedor.setHorizontalHeaderLabels(["Codigo", "Nombre","Descripción"])
            
            # if not hasattr(self.proveedor, 'productos') or not self.proveedor.productos:
            #     self.ui.tabla_Productos_A_VincularProveedor.setModel(self.modelo_tabla_Productos_A_VincularProveedor)
            #     return
            
            # Rellenar la tabla con los productos
            for producto in productos:
                if producto is not None:
                    # Crear los datos para cada fila
                    fila = [
                        str(producto.codigo_upc),
                        producto.nombre_producto,
                        producto.descripcion_producto,
                    ]
                    
                    # Crear los QStandardItems para la fila
                    items = [QStandardItem(item) for item in fila]
                    for item in items:
                        item.setData(producto, Qt.UserRole)
                    self.modelo_tabla_Productos_A_VincularProveedor.appendRow(items)
            
            self.ui.tabla_Productos_A_VincularProveedor.setModel(self.modelo_tabla_Productos_A_VincularProveedor)

            # Desconectar la señal antes de conectar
            if self.seleccion_conectada_productos_a_vincular:
                self.ui.tabla_Productos_A_VincularProveedor.selectionModel().currentChanged.disconnect(self.obtener_elemento_seleccionado_a_vicular)
            
            self.ui.tabla_Productos_A_VincularProveedor.selectionModel().currentChanged.connect(self.obtener_elemento_seleccionado_a_vicular)
            self.seleccion_conectada_productos_a_vincular = True
            
        except Exception as e:
            print(f'Error en productos_proveedores_tabla: {e}')

    def obtener_elemento_seleccionado_a_vicular(self, current, previus):
        if current.column() >= 0:  # Verifica si es la primera columna
            indice_fila = current.row()
            elemento = self.modelo_tabla_Productos_A_VincularProveedor.item(indice_fila, 0)
            if elemento is not None:
                producto = elemento.data(Qt.UserRole)
                if producto:
                    self.producto_seleccionado_a_vincular = producto
                    self.PRODUCTO_A_VINCULAR_SELECCIONADO_SIGNAL.emit(self.producto_seleccionado_a_vincular)
            else:
                return
    
    def quitar_producto_para_vincular(self, producto):
        if not producto:
            Mensaje("No se paso ningun elemento para eliminar")
            return
        self.lista_productos_para_vincular.discard(producto)
        print(self.lista_productos_para_vincular)
        self.producto_para_vincular_tabla(self.lista_productos_para_vincular)
    
    def eliminar_producto_del_proveedor_metodo(self):
        print(f'producto del proveedor : {self.producto_seleccionado.nombre_producto}')
            

        
