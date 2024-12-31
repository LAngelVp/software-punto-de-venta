from .BaseDatosModel import Productos, Presentacion_productos, Unidad_medida_productos
from sqlalchemy.orm import joinedload

class ProductosModel:
    def __init__(self, session):
        self.session = session
    
    def agregar_presentacion(self, nombre):
        if not nombre:
            return False
        presentacion = Presentacion_productos(nombre = nombre)
        self.session.add(presentacion)
        self.session.flush()
        return presentacion, True
    
    def obtener_presentaciones(self):
        presentaciones = self.session.query(Presentacion_productos).all()
        if presentaciones:
            return presentaciones, True
        else:
            return None, False
    
    def agregar_unidad_medida(self, nombre):
        if not nombre:
            return False
        unidad = Unidad_medida_productos(unidad_medida = nombre)
        self.session.add(unidad)
        self.session.flush()
        return unidad, True
    
    def obtener_unidades_medida(self):
        unidades_medida = self.session.query(Unidad_medida_productos).all()
        if unidades_medida:
            return unidades_medida, True
        else:
            return None, False
        
    def agregar_producto(
        self,
        codigo_upc,
        nombre_producto,
        descripcion_producto,
        costo_inicial,
        costo_final,
        precio,
        existencia,
        existencia_minima,
        existencia_maxima,
        marca,
        modelo,
        peso,
        dimensiones,
        color,
        material,
        fecha_fabricacion,
        fecha_vencimiento,
        imagen,
        notas,
        presentacion_producto_id,
        unidad_medida_productos_id,
        categoria_id,
        sucursales,
        proveedores
        ):
        try:
            producto = self.session.query(Productos).filter(Productos.codigo_upc == codigo_upc).first()
            if producto:
                return producto, False
            
            producto = Productos(
                codigo_upc=codigo_upc,
                nombre_producto=nombre_producto,
                descripcion_producto=descripcion_producto,
                costo_inicial=costo_inicial,
                costo_final=costo_final,
                precio=precio,
                existencia=existencia,
                existencia_minima=existencia_minima,
                existencia_maxima=existencia_maxima,
                marca=marca,
                modelo=modelo,
                peso=peso,
                dimensiones=dimensiones,
                color=color,
                material=material,
                fecha_fabricacion=fecha_fabricacion,
                fecha_vencimiento=fecha_vencimiento,
                imagen=imagen,
                notas=notas,
                presentacion_producto_id=presentacion_producto_id,
                unidad_medida_productos_id=unidad_medida_productos_id,
                categoria_id=categoria_id,
                sucursales=sucursales,
                proveedores=proveedores
            )
            
            self.session.add(producto)
            self.session.flush()  # Asegurarse de que el producto se agregue correctamente

            return producto, True
        except Exception as e:
            print(f"Error al agregar producto: {e}")
            return None, False
        
    def obtener_productos(self):
        productos = self.session.query(Productos).options(
                joinedload(Productos.proveedores),
                joinedload(Productos.categoria),
                joinedload(Productos.unidad_medida_productos),
                joinedload(Productos.presentacion_productos)
            ).all()
        if productos:
            return productos, True
        else:
            return None, False
        
    def eliminar_producto(self, codigo_producto):
        producto = self.session.query(Productos).filter(Productos.codigo_upc == codigo_producto).first()
        if producto:
            self.session.delete(producto)
            return True
        else:
            return False