from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from ..View.UserInterfacePy.PRODUCTOS_PROVEEDORES import *
from .AjustarCajaOpcionesGlobal import *

class Productos_de_proveedorController(QWidget):
    def __init__(self, proveedor):
        super().__init__()
        self.ui = Ui_contenedor_productos_proveedores()
        self.ui.setupUi(self)
        self.proveedor = proveedor
        pantalla = self.frameGeometry()
        pantalla.moveCenter(self.screen().availableGeometry().center())
        self.move(pantalla.topLeft())
        AjustarCajaOpciones().ajustar_cajadeopciones(self.ui.cajaopciones_filtro_nombre)
        AjustarCajaOpciones().ajustar_cajadeopciones(self.ui.cajaopciones_filtro_nombre_productos_del_sistema)
        if not self.proveedor:
            return
        self.ui.etiqueta_nombre_del_proveedor.setText(f'Nombre del Proveedor: {self.proveedor.nombre}')
        self.productos_proveedores_tabla()
        
    def productos_proveedores_tabla(self):
        try:
            if self.ui.tabla_productos_del_proveedor is None:
                return
            # Inicializar el modelo correctamente
            if not hasattr(self, 'modelo_tabla_productos_del_proveedor'):
                self.modelo_tabla_productos_del_proveedor = QStandardItemModel()
            
            # Limpiar el modelo
            self.modelo_tabla_productos_del_proveedor.clear()
            
            if not self.proveedor.productos:
                # Si no hay productos, mostrar solo las cabeceras
                self.modelo_tabla_productos_del_proveedor.setHorizontalHeaderLabels([
                    "Codigo", "Nombre"
                ])
                self.ui.tabla_productos_del_proveedor.setModel(self.modelo_tabla_productos_del_proveedor)
                return
            
            # Definir los nombres de las columnas
            nombre_columnas = ["Codigo", "Nombre"]
            self.modelo_tabla_productos_del_proveedor.setHorizontalHeaderLabels(nombre_columnas)
            
            # Rellenar la tabla con los productos
            for producto in self.proveedor.productos:
                if producto is not None:
                    # Crear los datos para cada fila
                    fila = [
                        str(producto.codigo_upc),  # Suponiendo que "codigo_upc" es el código del producto
                        producto.nombre_producto             # Nombre del producto
                    ]
                    
                    # Crear los QStandardItems para la fila
                    items = [QStandardItem(item) for item in fila]
                    
                    # Añadir la fila al modelo
                    self.modelo_tabla_productos_del_proveedor.appendRow(items)
            
            # Asignar el modelo a la tabla
            self.ui.tabla_productos_del_proveedor.setModel(self.modelo_tabla_productos_del_proveedor)
            
        except Exception as e:
            print(f'Error en productos_proveedores_tabla: {e}')