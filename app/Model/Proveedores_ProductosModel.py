from .BaseDatosModel import Productos, Presentacion_productos, Unidad_medida_productos, Categorias_proveedores, Representantes_proveedores, Proveedores, producto_proveedor
from sqlalchemy.orm import joinedload

class Proveedores_productoModel:
    def __init__(self, session):
        self.session = session
    
    def consultar_productos_del_proveedor(self, id_proveedor):
        productos_del_proveedor = self.session.query(Productos, producto_proveedor.c.precio_venta).join(
            producto_proveedor, producto_proveedor.c.producto_id == Productos.id
        ).filter(producto_proveedor.c.proveedor_id == id_proveedor).all()
        if productos_del_proveedor:
            print(producto_proveedor)
            return productos_del_proveedor, True
        else:
            return [], False
        
    def desvincular_producto_del_proveedor(self, proveedor_id, producto_id):
        try:
            self.session.query(producto_proveedor).filter(
                producto_proveedor.c.proveedor_id == proveedor_id,
                producto_proveedor.c.producto_id == producto_id
            ).delete(synchronize_session=False)
            return True
        except:
            return False
        
    def establecer_precio_producto_del_proveedor(self, proveedor_id, producto_id, precio):
        try:
            stmt = (
            self.session.query(producto_proveedor)
                .filter(
                    producto_proveedor.c.proveedor_id == proveedor_id,
                    producto_proveedor.c.producto_id == producto_id
                )
            )

            # Verificamos si ya existe
            record = stmt.first()
            if record:
                # Actualizar el precio existente
                self.session.execute(
                    producto_proveedor.update().where(
                        (producto_proveedor.c.proveedor_id == proveedor_id) &
                        (producto_proveedor.c.producto_id == producto_id)
                    ).values(precio_venta=precio)
                )
            # else:
            #     # Insertar si no existe
            #     self.session.execute(
            #         producto_proveedor.insert().values(
            #             proveedor_id=proveedor_id,
            #             producto_id=producto_id,
            #             precio_venta=precio
            #         )
            #     )
            return True
        except:
            return False