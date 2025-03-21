from sqlalchemy.orm import joinedload
from .BaseDatosModel import Proveedores, Categorias_proveedores, Representantes_proveedores, Productos, producto_proveedor
import logging

class ProveedoresModel:
    def __init__(self, session):
        self.session = session

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
        proveedores = self.session.query(Proveedores).options(
            joinedload(Proveedores.categoria),  # Carga anticipada de las categorías
            joinedload(Proveedores.productos),   # Carga anticipada de los productos
            joinedload(Proveedores.representante),  # Carga anticipada del representante
            joinedload(Proveedores.compras)  # Carga anticipada de las compras
        ).all()
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
            return proveedores
        return []
    
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
                return None

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
            if categoria_id:
                try:
                    categoria = self.session.query(Categorias_proveedores).get(categoria_id)
                    if categoria:
                        
                        # Limpiar las categorías existentes y agregar la nueva
                        proveedor.categoria = categoria
                except Exception as e:
                    self.session.rollback()
                    logging.error(f"Error al agregar categoria: {e}")
                    return None

            # Actualizar el representante si se proporciona
            if representante_id is not None:
                try:
                    representante = self.session.query(Representantes_proveedores).get(representante_id)
                    if representante:
                        proveedor.representante = representante
                except Exception as e:
                    self.session.rollback()
                    logging.error(f"Error al agregar representante: {e}")
                    return None
            else:
                # Si no se proporciona representante_id, eliminar los representantes existentes
                proveedor.representante = None
            return proveedor_id  # Retorna el ID del proveedor actualizado
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
                return True
            else:
                return False
        except Exception as e:
            return False

    def filtrar_productos_del_proveedor_exacto_nombre(self, proveedor_id, nombre):
        productos = self.session.query(Productos).join(
            producto_proveedor, Productos.id == producto_proveedor.c.producto_id
        ).join(
            Proveedores, Proveedores.id == producto_proveedor.c.proveedor_id
        ).filter(
            Productos.nombre_producto == nombre,
            Proveedores.id == proveedor_id
        ).all()
        
        if productos:
            return productos, True
        else:
            return None, False
    
    def actualizar_productos_al_proveedor(self, proveedor,  lista_productos):
        pass
        if not lista_productos or not proveedor:
            return None, False
        try:
            proveedor = self.session.query(Proveedores).filter(Proveedores.id == proveedor).first()
            if not proveedor:
                return None, False
            productos_a_agregar = []
            for producto in lista_productos:
                if producto not in proveedor.productos:
                    productos_a_agregar.append(producto)
            if productos_a_agregar:
                proveedor.productos.extend(productos_a_agregar)
        except Exception as e:
            print(f"error al meter el producto {e}")
                        