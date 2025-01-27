from .BaseDatosModel import Productos, Presentacion_productos, Unidad_medida_productos, Categorias_proveedores, Representantes_proveedores, Proveedores, producto_proveedor
from sqlalchemy.orm import joinedload

class Proveedores_productoModel:
    def __init__(self, session):
        self.session = session
    
    def consultar_productos_del_proveedor(self, id_proveedor):
        productos_del_proveedor = self.session.query(Productos).join(
            producto_proveedor, producto_proveedor.c.producto_id == Productos.codigo_upc
        ).filter(producto_proveedor.c.proveedor_id == id_proveedor).all()
        if productos_del_proveedor:
            return productos_del_proveedor, True
        else:
            return [], False