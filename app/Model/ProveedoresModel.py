from .BaseDatosModel import Proveedores, Categorias_proveedores, Representantes_proveedores

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
                        telefono
                        ):
        try:
            proveedor = self.session.query(Proveedores).filter_by(nombre = nombre).first()
            if proveedor:
                return proveedor
            else:
                nuevo_proveedor = Proveedores(
                    nombre = nombre,
                    pais = pais,
                    estado = estado,
                    ciudad = ciudad,
                    codigo_postal = codigo_postal,
                    calles = calles,
                    avenidas = avenidas,
                    colonia = colonia,
                    direccion_adicional = direccion_adicional,
                    rfc = rfc,
                    pagina_web = pagina_web,
                    correo  = correo,
                    telefono = telefono
                    )
                
                if categoria_id:
                    try:
                        categoria = self.session.query(Categorias_proveedores).get(categoria_id)
                        if categoria:
                            nuevo_proveedor.categorias.append(categoria)  # Asociar el objeto, no el id
                    except Exception as e:
                        print(f'Error al asociar categoría: {e}')
                        return None

                elif representante_id:
                    try:
                        representante = self.session.query(Representantes_proveedores).get(representante_id)
                        if representante:
                            nuevo_proveedor.representantes.append(representante)  # Asociar el objeto, no el id
                    except Exception as e:
                        print(f'Error al asociar representante: {e}')
                        self.session.rollback()
                    return None

                self.session.add(nuevo_proveedor)
                self.session.flush()
                return  nuevo_proveedor.id
        except Exception as e:
            print(f'error en el proveedor {e}')
        
    def obtener_proveedor_id(self, id):
        try:
            proveedor = self.session.query(Proveedores).get(id)
            if proveedor is None:
                print(f"No se encontró un proveedor con ID: {id}")
                return proveedor, False
            else:
                return proveedor, True
        except Exception as e:
            print(f"Error al obtener proveedor por ID {id}: {str(e)}")  # Imprimir el error para depuración
            return None

    def obtener_proveedores(self):
        proveedores = self.session.query(Proveedores).all()
        if len(proveedores) > 0:
            return proveedores, True
        else:
            return  None, False


    
    def obtener_nombre_proveedor(self, texto):
        try:
            texto_busqueda = f"%{texto}%"
            # Realizar la consulta utilizando ilike() para búsqueda insensible a mayúsculas
            proveedores = self.session.query(Proveedores).filter(Proveedores.nombre.ilike(texto_busqueda)).all()
            return proveedores
        except:
            pass
    
    def actualizar_proveedor(self, proveedor_id, 
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
                            ):
        try:
            # Buscar el proveedor por ID
            proveedor = self.session.query(Proveedores).get(proveedor_id)
            if not proveedor:
                print(f'Proveedor con ID {proveedor_id} no encontrado.')
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

            # Actualizar la categoría si se proporciona
            if categoria_id:
                try:
                    categoria = self.session.query(Categorias_proveedores).get(categoria_id)
                    if categoria:
                        # Limpiar las categorías existentes y agregar la nueva
                        proveedor.categorias.clear()
                        proveedor.categorias.append(categoria)
                    else:
                        print(f'Categoría con ID {categoria_id} no encontrada.')
                except Exception as e:
                    print(f'Error al asociar categoría: {e}')
                    self.session.rollback()
                    return None

            # Actualizar el representante si se proporciona
            if representante_id is not None:
                try:
                    representante = self.session.query(Representantes_proveedores).get(representante_id)
                    if representante:
                        proveedor.representante = representante
                    else:
                        print(f'Representante con ID {representante_id} no encontrado.')
                except Exception as e:
                    print(f'Error al asociar representante: {e}')
                    self.session.rollback()
                    return None
            else:
                # Si no se proporciona representante_id, eliminar los representantes existentes
                proveedor.representante = None
            print(f'Proveedor con ID {proveedor_id} actualizado con éxito.')
            return proveedor_id  # Retorna el ID del proveedor actualizado
        except Exception as e:
            print(f'Error al actualizar el proveedor: {e}')
            self.session.rollback()  # Hacer rollback en caso de error
            return None

    def consultar_proveedor(self, nombre):
        try:
            proveedor = self.session.query(Proveedores).filter(Proveedores.nombre == nombre).first()
            if proveedor is None:
                return proveedor, False
            else:
                return proveedor, True
        except Exception as e:
            print(f'Error al consultar el proveedor: {e}')
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
            print(f'Error al eliminar el proveedor: {e}')

