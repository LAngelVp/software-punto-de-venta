from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from ..View.UserInterfacePy.PRODUCTOS_PROVEEDORES import *
from .AjustarCajaOpcionesGlobal import *
from .MensajesAlertasController import Mensaje
class Productos_de_proveedorController(QWidget):
    PRODUCTO_DE_PROVEEDOR_SELECCIONADO_SIGNAL = pyqtSignal(object)
    
    def __init__(self, proveedor):
        super().__init__()
        self.ui = Ui_contenedor_productos_proveedores()
        self.ui.setupUi(self)
        self.proveedor = proveedor
        pantalla = self.frameGeometry()
        pantalla.moveCenter(self.screen().availableGeometry().center())
        self.move(pantalla.topLeft())
        self.ui.btn_btn_eliminar_producto_del_proveedor.clicked.connect(self.eliminar_producto_del_proveedor_metodo)
        AjustarCajaOpciones().ajustar_cajadeopciones(self.ui.cajaopciones_filtro_nombre)
        AjustarCajaOpciones().ajustar_cajadeopciones(self.ui.cajaopciones_filtro_nombre_productos_del_sistema)
        self.seleccion_conectada_productos = False
        self.producto_seleccionado = None
        
        if not self.proveedor:
            return
        
        self.ui.etiqueta_nombre_del_proveedor.setText(f'Nombre del Proveedor: {self.proveedor.nombre}')
        self.productos_proveedores_tabla()
        
        self.PRODUCTO_DE_PROVEEDOR_SELECCIONADO_SIGNAL.connect(self.eliminar_producto_del_proveedor_metodo)
        
        
    def productos_proveedores_tabla(self):
        try:
            if self.ui.tabla_productos_del_proveedor is None:
                return
            # Inicializar el modelo correctamente
            if not hasattr(self, 'modelo_tabla_productos_del_proveedor'):
                self.modelo_tabla_productos_del_proveedor = QStandardItemModel()
            
            # Limpiar el modelo y resetear cabeceras
            self.modelo_tabla_productos_del_proveedor.clear()
            self.modelo_tabla_productos_del_proveedor.setHorizontalHeaderLabels(["Codigo", "Nombre"])
            
            if not hasattr(self.proveedor, 'productos') or not self.proveedor.productos:
                self.ui.tabla_productos_del_proveedor.setModel(self.modelo_tabla_productos_del_proveedor)
                return
            
            # Rellenar la tabla con los productos
            for producto in self.proveedor.productos:
                if producto is not None:
                    # Crear los datos para cada fila
                    fila = [
                        str(producto.codigo_upc),
                        producto.nombre_producto
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
            
    def eliminar_producto_del_proveedor_metodo(self):
        
        print(self.producto_seleccionado.nombre_producto)
            
        
        
