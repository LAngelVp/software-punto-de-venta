from .BaseDatosModel import Productos, Presentacion_productos, Unidad_medida_productos, Movimientos_Inventario, Categorias_productos
from sqlalchemy.orm import joinedload, selectinload
from sqlalchemy import select

class ProductosModel:
    def __init__(self, session):
        self.session = session

# // presentaciones de los productos:
    def insertar_unida_de_medida_basicas(self):
        query = select(Unidad_medida_productos).limit(1)
        resultado_consulta = self.session.execute(query).fetchone()
        if resultado_consulta is None:
            unidades_productos = [
                {"nombre": 'Kilogramo-(Kg)'},
                {"nombre": 'Gramo-(g)'},
                {"nombre": 'Litro-(L)'},
                {"nombre": 'Mililitro-(ml)'},
                {"nombre": 'Unidad-(u)'},
                {"nombre": 'Caja-(caj)'},
                {"nombre": 'Paquete-(paq)'},
                {"nombre": 'Docena-(dz)'},
                {"nombre": 'Pieza-(pza)'},
                {"nombre": 'Tetra pack-(Tetra)'},
                {"nombre": 'Sobre-(sob)'},
                {"nombre": 'Metro-(m)'},
                {"nombre": 'Centrimetro-(cm)'},
                {"nombre": 'Set-(set)'},
                {"nombre": 'Rol-(rol)'},
                {"nombre": 'Tarro-(tarro)'},
                {"nombre": 'Cilindro-(cil)'},
                {"nombre": 'Cilindro-(cil)'},
                {"nombre": 'Saco-(sac)'},
            ]
            
            self.session.execute(Unidad_medida_productos.__table__.insert(), unidades_productos)
            return True
    
    def insertar_categorias_basicas(self):
        query = select(Categorias_productos).limit(1)
        resultado_consulta = self.session.execute(query).fetchone()
        if resultado_consulta is None:
            categorias_productos = [
                {"nombre": 'Alimentos Perecederos', "descripcion": "Productos que requieren refrigeración, como carnes, pescados, lácteos, frutas y verduras frescas"},
                {"nombre": "Alimentos No Perecederos", "descripcion": "Comestibles que no requieren refrigeración, tales como arroz, pasta, galletas, sopas enlatadas, cereales, y otros productos empaquetados"},
                {"nombre": "Bebidas", "descripcion": "Refrescos, jugos, agua embotellada, bebidas energéticas, y también bebidas alcohólicas como cervezas, vinos, y licores"},
                {"nombre": "Productos de Panadería", "descripcion": "Pan, bollería, pasteles, galletas, y otros productos de panadería que se venden en tiendas de abarrotes"},
                {"nombre": "Congelados", "descripcion": "Alimentos congelados como pizzas, vegetales, carnes y postres helados"},
                {"nombre": "Comidas Preparadas", "descripcion": "Comidas listas para consumir como platos precocinados, ensaladas envasadas, y snacks de comida rápida"},
                {"nombre": "Herramientas Manuales", "descripcion": "Martillos, destornilladores, llaves inglesas, sierras, y otros instrumentos de mano"},
                {"nombre": "Herramientas Eléctricas", "descripcion": "Taladros, sierras eléctricas, lijadoras, y otros equipos que requieren energía para su funcionamiento"},
                {"nombre": "Materiales de Construcción", "descripcion": "Cemento, pintura, clavos, tornillos, maderas, y otros productos para la construcción y remodelación"},
                {"nombre": "Plomería", "descripcion": "Tuberías, grifos, llaves, selladores, y otros accesorios para trabajos de plomería"},
                {"nombre": "Iluminación", "descripcion": "Bombillos, lámparas, focos, linternas y otros productos relacionados con la iluminación"},
                {"nombre": "Accesorios de Jardinería", "descripcion": "Regaderas, fertilizantes, macetas, semillas y otros elementos para el cuidado de jardines"},
                {"nombre": "Snacks y Botanas", "descripcion": "Papas fritas, galletas, nueces, palomitas, y otros aperitivos envasados"},
                {"nombre": "Lácteos y Derivados", "descripcion": "Papas fritas, galletas, nueces, palomitas, y otros"},
                {"nombre": "Productos de Higiene Personal", "descripcion": "Jabón, shampoo, pasta dental, desodorante, toallas sanitarias y otros productos de cuidado personal"},
            ]
            
            self.session.execute(Categorias_productos.__table__.insert(), categorias_productos)
            return True
    
    def insertar_presentaciones_basicas(self):
        query = select(Presentacion_productos).limit(1)
        resultado_consulta = self.session.execute(query).fetchone()
        if resultado_consulta is None:
            presentaciones = [
                {"nombre": "Unidad"},
                {"nombre": "Pieza"},
                {"nombre": "Paquete"},
                {"nombre": "Caja"},
                {"nombre": "Bolsa"},
                {"nombre": "Saco"},
                {"nombre": "Docena"},
                {"nombre": "Litro"},
                {"nombre": "Mililitro"},
                {"nombre": "Kilogramo"},
                {"nombre": "Gramo"},
                {"nombre": "Tarro"},
                {"nombre": "Tetra pack"},
                {"nombre": "Sobre"},
                {"nombre": "Frasco"},
                {"nombre": "Set"},
                {"nombre": "Rollo"},
                {"nombre": "Cilindro"},
                {"nombre": "Balde"},
                {"nombre": "Metro"},
                {"nombre": "Centímetro"},
                {"nombre": "Galón"},
                {"nombre": "Bidón"},
                {"nombre": "Blíster"},
                {"nombre": "Estuche"}
            ]
            
            self.session.execute(Presentacion_productos.__table__.insert(), presentaciones)
            return True
    
    def agregar_presentacion(self, nombre):
        presentacion = self.session.query(Presentacion_productos).filter(Presentacion_productos.nombre == nombre).first()
        if presentacion is not None:
            return presentacion, False
        
        presentacion = Presentacion_productos(nombre = nombre)
        print(f"esta es la presentacion: {presentacion.nombre}")
        self.session.add(presentacion)
        self.session.flush()
        return presentacion, True
    
    def obtener_presentaciones(self):
        presentaciones = self.session.query(Presentacion_productos).all()
        if presentaciones:
            return presentaciones, True
        else:
            return None, False
        
    def eliminar_presentacion_producto(self, presentacion_obj):
        try:
            if presentacion_obj:
                self.session.delete(presentacion_obj)
                self.session.commit()  # Confirma la eliminación
                return True
            return False
        except Exception as e:
            print(f"Error al eliminar la unidad de medida: {e}")
            return False
    
    def agregar_unidad_medida(self, nombre):
        if not nombre:
            return False
        unidad = self.session.query(Unidad_medida_productos).filter(Unidad_medida_productos.nombre == nombre).first()
        if unidad:
            return unidad, False
        unidad = Unidad_medida_productos(nombre = nombre)
        self.session.add(unidad)
        self.session.flush()
        return unidad, True
    
    def obtener_unidades_medida(self):
        unidades_medida = self.session.query(Unidad_medida_productos).all()
        if unidades_medida:
            return unidades_medida, True
        else:
            return None, False
    
    def eliminar_unidad_medida(self, unidad_obj):
        try:
            if unidad_obj:
                # Elimina la unidad de medida si se encuentra
                self.session.delete(unidad_obj)
                self.session.commit()  # Confirma la eliminación
                return True
            return False
        except Exception as e:
            print(f"Error al eliminar la unidad de medida: {e}")
            return False
        
    def agregar_producto(
        self,
        codigo_upc,
        nombre_producto,
        descripcion_producto,
        costo_inicial,
        costo_final,
        margen_porcentaje,
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
                margen_porcentaje = margen_porcentaje,
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
            self.session.flush()
            return producto, True
        except Exception as e:
            print(f"Error al agregar producto: {e}")
            return None, False
        
    def actualizar_producto(self,
                            id_producto,
                            codigo_upc,
                            nombre_producto,
                            descripcion_producto,
                            costo_inicial,
                            costo_final,
                            margen_porcentaje,
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
        producto_actual = self.session.query(Productos).filter(Productos.codigo_upc == codigo_upc).first()
        if not producto_actual:
            return None, False
        
        producto_actual.nombre_producto = nombre_producto
        producto_actual.descripcion_producto = descripcion_producto
        producto_actual.costo_inicial = costo_inicial
        producto_actual.costo_final = costo_final
        producto_actual.margen_porcentaje = margen_porcentaje
        producto_actual.precio = precio
        producto_actual.existencia = existencia
        producto_actual.existencia_minima = existencia_minima
        producto_actual.existencia_maxima = existencia_maxima
        producto_actual.marca = marca
        producto_actual.modelo = modelo
        producto_actual.peso = peso
        producto_actual.dimensiones = dimensiones
        producto_actual.color = color
        producto_actual.material = material
        producto_actual.fecha_fabricacion = fecha_fabricacion
        producto_actual.fecha_vencimiento = fecha_vencimiento
        producto_actual.imagen = imagen
        producto_actual.notas = notas
        producto_actual.presentacion_producto_id = presentacion_producto_id
        producto_actual.unidad_medida_productos_id = unidad_medida_productos_id
        producto_actual.categoria_id = categoria_id
        producto_actual.sucursales = sucursales
        # Limpiar la relación de proveedores
        producto_actual.proveedores = []  # Limpiar la lista de proveedores

        # Usar `session.merge()` para asegurarse de que no haya duplicados
        proveedores_fusionados = []
        for proveedor in proveedores:
            proveedor_fusionado = self.session.merge(proveedor)  # Fusionar proveedor si ya está en la sesión
            proveedores_fusionados.append(proveedor_fusionado)
        
        producto_actual.proveedores = proveedores_fusionados  # Asignar los proveedores fusionados

        return producto_actual, True
        
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
    
    def consultar_por_nombre_exacto(self, nombre):
        productos = self.session.query(Productos).filter(Productos.nombre_producto.like(nombre)).all()
        if productos:
            return productos, True
        else:
            return None, False
    
    def consultar_por_nombre(self, nombre):
        productos = self.session.query(Productos).filter(Productos.nombre_producto.ilike(f"%{nombre}%")).all()
        if productos:
            return productos, True
        else:
            return None, False
        
    def consultar_producto_por_codigoUPC(self, codigo_upc):
        produto = self.session.query(Productos).options(
            selectinload(Productos.proveedores),
            selectinload(Productos.categoria),
            selectinload(Productos.unidad_medida_productos),
            selectinload(Productos.presentacion_productos)
            ).filter(Productos.codigo_upc == codigo_upc).first()
        if produto:
            return produto, True
        else:
            return None, False
        
    def ejecutar_movimiento(self, producto, cantidad_cambio, tipo_movimiento, fecha_movimiento, notas, usuarioid):
        if not producto and not usuarioid:
            return None,False
        
        movimiento = Movimientos_Inventario(
            producto_id = producto.id,
            cantidad_cambio = cantidad_cambio,
            tipo_movimiento = tipo_movimiento,
            fecha_movimiento = fecha_movimiento,
            notas = notas,
            usuario_id = usuarioid
            )
        
        producto = self.session.merge(producto)
        
        self.session.refresh(producto)
        
        
        if tipo_movimiento.lower() == "entrada":
            producto.existencia += cantidad_cambio
        elif tipo_movimiento.lower() == "salida":
            producto.existencia -= cantidad_cambio
            
        self.session.add(movimiento)
        self.session.flush()
        return movimiento, True