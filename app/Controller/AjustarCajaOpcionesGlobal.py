from PySide6.QtWidgets import QListView, QMenu, QMessageBox
from PySide6.QtGui import QAction
from PySide6.QtCore import Qt
from ..DataBase.conexionBD import Conexion_base_datos
from ..Model.BaseDatosModel import Unidad_medida_productos, Presentacion_productos
from ..Model.CategoriasModel import CategoriasModel
from ..Model.ProductosModel import ProductosModel
class AjustarcajaOpciones:
    def __init__(self, modelo = None, tipo_categoria = None):
        self.modelo = modelo  # El modelo que se pasará, como CategoriasModel o ProductosModel
        self.tipo_categoria = tipo_categoria  # El tipo de categoría ('productos', 'clientes', etc.)

    def ajustar_cajadeopciones(self, caja_opciones):
        # Usar un QListView para la vista del combo box
        vista_lista = QListView()
        vista_lista.setStyleSheet("""
        QListView { background: #F5F5F5; }
        """)
        caja_opciones.setView(vista_lista)

        # Obtener el ancho del combo box
        ancho_combo = caja_opciones.width()
        if caja_opciones.count() > 0:
            # Calcular el ancho máximo basado en los elementos
            max_ancho = max(
                caja_opciones.fontMetrics().horizontalAdvance(caja_opciones.itemText(i))
                for i in range(caja_opciones.count())
            )

            # Establecer el ancho del QListView
            vista_lista.setFixedWidth(max(ancho_combo, max_ancho))
        
        # Conectar el evento de clic derecho en el QListView del combo box
        vista_lista.setContextMenuPolicy(Qt.CustomContextMenu)
        if self.modelo is not None:
            vista_lista.customContextMenuRequested.connect(lambda pos: self.show_context_menu(pos, vista_lista, caja_opciones))

    def show_context_menu(self, pos, vista_lista, caja_opciones):
        index = vista_lista.indexAt(pos)
        if index.isValid():
            menu = QMenu(vista_lista)
            delete_action = QAction("Eliminar", vista_lista)
            delete_action.triggered.connect(lambda: self.delete_item(index, caja_opciones))
            menu.addAction(delete_action)
            menu.exec_(vista_lista.mapToGlobal(pos))

    def delete_item(self, index, caja_opciones):
        # Obtener el objeto asociado con el item (el objeto de modelo, como 'categoria' o 'producto')
        item_obj = caja_opciones.itemData(index.row())

        # Eliminar el ítem de la base de datos usando el modelo
        if self.eliminar_item_de_base_datos(item_obj):
            # Eliminar el ítem del QComboBox si se eliminó exitosamente de la base de datos
            caja_opciones.removeItem(index.row())
        else:
            # Mostrar mensaje de error si no se pudo eliminar
            QMessageBox.warning(caja_opciones, "Error", "No se pudo eliminar el ítem de la base de datos.")

    def eliminar_item_de_base_datos(self, item_obj):
        try:
            # Usamos el método adecuado de eliminación según el modelo
            if isinstance(self.modelo, CategoriasModel):
                return self.modelo.eliminar(self.tipo_categoria, item_obj)
            elif isinstance(self.modelo, ProductosModel):
                if isinstance(item_obj, Unidad_medida_productos):
                    return self.modelo.eliminar_unidad_medida(item_obj)
                elif isinstance(item_obj, Presentacion_productos):
                    return self.modelo.eliminar_presentacion_producto(item_obj)
            # Agregar más modelos si es necesario en el futuro
            return False
        except Exception as e:
            print(f"Error al eliminar el ítem de la base de datos: {e}")
            return False