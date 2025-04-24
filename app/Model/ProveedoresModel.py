from sqlalchemy.orm import joinedload
from sqlalchemy import select
from .BaseDatosModel import Proveedores, Categorias_proveedores, Representantes_proveedores, Productos, producto_proveedor
import logging

class ProveedoresModel:
    def __init__(self, session):
        self.session = session
        
    
    def insertar_categoria_proveedor_basicas(self):
        query = select(Categorias_proveedores).limit(1)
        resultado_consulta = self.session.execute(query).fetchone()
        if resultado_consulta is None:
            categorias_proveedor = [
                {"nombre": 'Bebidas Alcohólicas', "descripcion": "Proveedores que distribuyen cervezas, vinos, tequilas y mezcales, tanto nacionales como internacionales, en diferentes presentaciones. Sus productos son clave en la industria de bebidas para restaurantes, tiendas y supermercados, ofreciendo opciones variadas en calidad y presentación"},
                {"nombre": 'Bebidas No Alcohólicas', "descripcion": "Proveedores que comercializan refrescos, jugos, agua embotellada y bebidas energéticas. Estas marcas están presentes en el mercado ofreciendo productos refrescantes y saludables, con opciones en diferentes sabores y fórmulas, disponibles en varios tamaños y presentaciones"},
                {"nombre": 'Productos Lácteos', "descripcion": "Proveedores que ofrecen leche, yogurt, queso, crema y mantequilla. Estos productos son esenciales en la canasta básica mexicana, garantizando calidad en la producción y distribución en tiendas, supermercados y puntos de venta"},
                {"nombre": 'Alimentos Empacados', "descripcion": "Proveedores que distribuyen productos alimenticios como pan, galletas, cereales, alimentos congelados, sopas, entre otros. Estos productos están disponibles en tiendas de abarrotes, supermercados y puntos de venta especializados, ofreciendo conveniencia y variedad al consumidor"},
                {"nombre": 'Snacks y Botanas', "descripcion": "Proveedores de botanas saladas y dulces, como papas fritas, galletas, nachos y otros aperitivos. Este sector es popular en tiendas de abarrotes, gasolineras y supermercados, proporcionando opciones de snack para diferentes gustos"},
                {"nombre": 'Productos de Higiene y Cuidado Personal', "descripcion": "Proveedores de artículos para la higiene personal, como jabones, champús, cremas, desodorantes y toallas sanitarias. Estos productos son esenciales para el bienestar y cuidado diario, y están disponibles en tiendas y grandes cadenas de distribución"},
                {"nombre": 'Productos de Limpieza', "descripcion": "Proveedores de productos para limpieza del hogar y oficina, como detergentes, desinfectantes, limpiadores multiusos, blanqueadores, entre otros. Estos productos cubren todas las necesidades de limpieza, desde productos para pisos hasta limpieza de superficies"},
                {"nombre": 'Tecnología y Electrónica', "descripcion": "Proveedores de dispositivos electrónicos como computadoras, smartphones, televisores, cámaras y accesorios tecnológicos. Estas empresas ofrecen productos innovadores, siendo esenciales tanto para el hogar como para el ámbito profesional"},
                {"nombre": 'Ferretería y Herramientas', "descripcion": "Proveedores que ofrecen herramientas manuales y eléctricas, materiales de construcción, pinturas, tornillos y otros suministros para proyectos domésticos o industriales. Están presentes en tiendas especializadas y cadenas de ferreterías, ofreciendo productos de alta calidad"},
                {"nombre": 'Automotriz y Repuestos', "descripcion": "Proveedores de autopartes y accesorios para vehículos, como frenos, aceites, filtros, llantas y herramientas automotrices. Estos proveedores garantizan la disponibilidad de repuestos y accesorios necesarios para mantener y reparar vehículos en talleres, distribuidores y tiendas especializadas"},
                {"nombre": 'Ropa y Calzado', "descripcion": "Proveedores que ofrecen ropa y calzado para hombres, mujeres y niños, incluyendo desde ropa casual hasta deportiva, formal y accesorios de moda. Estos productos están disponibles en tiendas de moda, grandes almacenes y comercios en línea"},
                {"nombre": 'Muebles y Decoración', "descripcion": "Proveedores que ofrecen muebles para el hogar, oficina y jardín, como sofás, mesas, camas, sillas y artículos decorativos. Estos productos buscan combinar estética y funcionalidad, y son distribuidos en grandes almacenes y tiendas de decoración"},
                {"nombre": 'Herramientas y Material de Construcción', "descripcion": "Proveedores de materiales para la construcción, como cemento, bloques, varilla, y herramientas como martillos, sierras y taladros. Estos productos son fundamentales para proyectos de obra, desde pequeños proyectos en el hogar hasta grandes desarrollos inmobiliarios"},
                {"nombre": 'Productos para Mascotas', "descripcion": "Proveedores de alimentos, juguetes, accesorios, camas, y artículos de cuidado para mascotas como perros, gatos, aves, entre otros. Estos productos están disponibles en tiendas especializadas y grandes cadenas, atendiendo las necesidades de los dueños de mascotas"},
                {"nombre": 'Artículos de Oficina', "descripcion": "Proveedores que distribuyen productos para oficina como papelería, mobiliario, equipos de computo y accesorios. Estos artículos son necesarios tanto para oficinas corporativas como para el hogar, ayudando a optimizar el trabajo diario con calidad y funcionalidad"},
            ]
            
            self.session.execute(Categorias_proveedores.__table__.insert(), categorias_proveedor)
            # self.session.commit()
            return True

    def agregar_proveedor(self, 
                        categoria_id,
                        representante_id,
                        nombre,
                        pais,
                        estado, 
                        ciudad,
                        codigo_postal,
                        calles,
                        avenidas,
                        colonia,
                        direccion_adicional,
                        rfc,
                        pagina_web,
                        correo,
                        telefono,
                        clave_moneda,
                        tipo_moneda
                        ):
        try:
            proveedor = self.session.query(Proveedores).filter_by(nombre=nombre).first()
            if proveedor:
                return proveedor, False  # Proveedor ya existe, no agregarlo

            nuevo_proveedor = Proveedores(
                nombre=nombre,
                pais=pais,
                estado=estado,
                ciudad=ciudad,
                codigo_postal=codigo_postal,
                calles=calles,
                avenidas=avenidas,
                colonia=colonia,
                direccion_adicional=direccion_adicional,
                rfc=rfc,
                pagina_web=pagina_web,
                correo=correo,
                telefono=telefono,
                clave_moneda=clave_moneda,
                tipo_moneda=tipo_moneda,
                representante_id=representante_id,
                categoria_id=categoria_id
            )

            if representante_id:
                try:
                    representante = self.session.query(Representantes_proveedores).filter(
                        Representantes_proveedores.id == representante_id).first()
                    if representante:
                        nuevo_proveedor.representante = representante
                except Exception as e:
                    self.session.rollback()
                    # Agregar el mensaje de error para el rollback
                    logging.error(f"Error al agregar representante: {e}")

            self.session.add(nuevo_proveedor)
            self.session.flush()
            return nuevo_proveedor, True  # Si todo va bien, devolver el nuevo proveedor y un estado True
        except Exception as e:
            # Asegúrate de devolver siempre una tupla, incluso cuando hay un error
            logging.error(f"Error al agregar proveedor: {e}")
            return None, False  # Devolver None y False si hay un error
        
    def obtener_proveedor_id(self, id):
        try:
            proveedor = self.session.query(Proveedores).get(id)
            if proveedor is None:
                return proveedor, False
            else:
                return proveedor, True
        except Exception as e:
            return None

    def obtener_proveedores(self):
        proveedores = (self.session.query(Proveedores).options(
            joinedload(Proveedores.categoria),  # Carga anticipada de las categorías
            joinedload(Proveedores.productos),   # Carga anticipada de los productos
            joinedload(Proveedores.representante),  # Carga anticipada del representante
            joinedload(Proveedores.compras)  # Carga anticipada de las compras
        )
        .order_by(Proveedores.nombre.asc())
        .all()
        )
        if len(proveedores) > 0:
            return proveedores, True
        else:
            return  None, False

    def obtener_nombre_proveedor(self, texto):
        texto_busqueda = f"%{texto}%"
        # Realizar la consulta utilizando ilike() para búsqueda insensible a mayúsculas
        proveedores = self.session.query(Proveedores).options(
            joinedload(Proveedores.categoria),  # Carga anticipada de las categorías
            joinedload(Proveedores.productos),   # Carga anticipada de los productos
            joinedload(Proveedores.representante),  # Carga anticipada del representante
            joinedload(Proveedores.compras)  # Carga anticipada de las compras
        ).filter(Proveedores.nombre.ilike(texto_busqueda)).all()
        if len(proveedores) > 0:
            return proveedores, True
        return [], False
    
    def actualizar_proveedor(self, 
                            proveedor_id, 
                            categoria_id,
                            representante_id,
                            nombre,
                            pais,
                            estado, 
                            ciudad,
                            codigo_postal,
                            calles,
                            avenidas,
                            colonia,
                            direccion_adicional,
                            rfc,
                            pagina_web,
                            correo,
                            telefono,
                            clave_moneda,
                            tipo_moneda
                            ):
        try:
            # Buscar el proveedor por ID
            
            proveedor = self.session.query(Proveedores).get(proveedor_id)
            if not proveedor:
                return None, False

            # Actualizar los atributos del proveedor
            proveedor.nombre = nombre
            proveedor.pais = pais
            proveedor.estado = estado
            proveedor.ciudad = ciudad
            proveedor.codigo_postal = codigo_postal
            proveedor.calles = calles
            proveedor.avenidas = avenidas
            proveedor.colonia = colonia
            proveedor.direccion_adicional = direccion_adicional
            proveedor.rfc = rfc
            proveedor.pagina_web = pagina_web
            proveedor.correo = correo
            proveedor.telefono = telefono
            proveedor.clave_moneda = clave_moneda
            proveedor.tipo_moneda = tipo_moneda

            # Actualizar la categoría si se proporciona
            if categoria_id is None:
                return None, False
            
            try:
                categoria = self.session.query(Categorias_proveedores).get(categoria_id)
                if categoria:
                    # Limpiar las categorías existentes y agregar la nueva
                    proveedor.categoria = categoria
            except Exception as e:
                self.session.rollback()
                return None, False

            # Actualizar el representante si se proporciona
            if representante_id is None:
                # Si no se proporciona representante_id, eliminar los representantes existentes
                proveedor.representante = None
            try:
                representante = self.session.query(Representantes_proveedores).get(representante_id)
                if representante:
                    proveedor.representante = representante
            except Exception as e:
                self.session.rollback()
                return None, False
                
            return proveedor, True  # Retorna el ID del proveedor actualizado
        except Exception as e:
            self.session.rollback()  # Hacer rollback en caso de error
            logging.error(f"Error al agregar proveedor: {e}")
            return None

    def consultar_proveedor(self, nombre):
        try:
            if nombre is None:
                return None, False
            proveedor = self.session.query(Proveedores).filter(Proveedores.nombre == nombre).first()
            if proveedor is None:
                return proveedor, False
            else:
                return proveedor, True
        except Exception as e:
            return None, False

    def eliminar_proveedor(self, id):
        try:
            proveedor = self.session.query(Proveedores).filter(Proveedores.id == id).first()
            if proveedor:
                self.session.delete(proveedor)
                return None, True
            else:
                return False, False
        except Exception as e:
            return None, False

    def filtrar_productos_del_proveedor_exacto_nombre(self, proveedor_id, nombre):
        productos = self.session.query(Productos, producto_proveedor.c.precio_venta).join(
            producto_proveedor, Productos.id == producto_proveedor.c.producto_id
        ).join(
            Proveedores, Proveedores.id == producto_proveedor.c.proveedor_id
        ).filter(
            Productos.nombre_producto.ilike(nombre),
            Proveedores.id == proveedor_id
        ).all()
        
        if productos:
            return productos, True
        else:
            return None, False
        
    def filtrar_productos_del_proveedor_contenga_nombre(self, proveedor_id, nombre):
        productos = self.session.query(Productos, producto_proveedor.c.precio_venta).join(
            producto_proveedor, Productos.id == producto_proveedor.c.producto_id
        ).join(
            Proveedores, Proveedores.id == producto_proveedor.c.proveedor_id
        ).filter(
            Productos.nombre_producto.ilike(f"%{nombre}%"),
            Proveedores.id == proveedor_id
        ).all()
        
        if productos:
            return productos, True
        else:
            return None, False
    
    def actualizar_productos_al_proveedor(self, proveedor_id,  lista_productos):
        if not lista_productos or not proveedor_id:
            return None, False
        try:
            proveedor = self.session.query(Proveedores).filter_by(id=proveedor_id).first()
            if not proveedor:
                return None, False

            productos_a_agregar = []
            for producto in lista_productos:
                producto_db = self.session.get(Productos, producto.id)  # importante
                if producto_db and producto_db not in proveedor.productos:
                    productos_a_agregar.append(producto_db)

            if productos_a_agregar:
                proveedor.productos.extend(productos_a_agregar)

            return proveedor, True

        except Exception as e:
            print(f"error al meter el producto {e}")
            return None, False
