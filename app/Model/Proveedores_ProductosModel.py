from .BaseDatosModel import Productos, Presentacion_productos, Unidad_medida_productos, Categorias_proveedores, Representantes_proveedores, Proveedores, producto_proveedor
from sqlalchemy.orm import joinedload

class Proveedores_productoModel:
    def __init__(self, session):
        self.session = session
    
    def consultar_productos_del_proveedor(self, id_proveedor):
        productos_del_proveedor = self.session.query(Productos).join(
            producto_proveedor, producto_proveedor.c.producto_id == Productos.id
        ).filter(producto_proveedor.c.proveedor_id == id_proveedor).all()
        if productos_del_proveedor:
            print(producto_proveedor)
            return productos_del_proveedor, True
        else:
            return [], False
        
    def desvincular_producto_del_proveedor(self, proveedor_id, producto_id):
        # Paso 1: Buscar la relación entre producto y proveedor en la tabla intermedia
        # Eliminar la relación entre el producto y el proveedor
        try:
            self.session.query(producto_proveedor).filter(
                producto_proveedor.c.proveedor_id == proveedor_id,
                producto_proveedor.c.producto_id == producto_id
            ).delete(synchronize_session=False)
            return True
        except:
            return False