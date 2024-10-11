from .BaseDatosModel import Clientes_fisicos, Clientes_morales, Clientes, Representantes_clientes_morales, Categorias_de_clientes, Areas_negocios
from sqlalchemy.orm import aliased
from sqlalchemy import or_

class ClientesFisicosAndMorales:
    def __init__(self, session):
        self.session = session

    def agregar_cliente_fisico(self, nombre, correo, rfc, telefono, pais, estado, ciudad, avenidas, calles, codigo_postal, direccion_adicional, entidad_legalizada, categoria_cliente_id, credito, estado_credito, limite_credito, porcentaje_interes, fecha_ultimo_reporte, credito_disponible, credito_utilizado, tipo_cliente, aplica_descuento, porcentaje_descuento, comentarios, areas_de_negocios_id, apellido_paterno, apellido_materno, curp, fecha_nacimiento, num_identificacion, ocupacion, ingresos, estado_civil, foto):
        try:
            cliente_existente = (self.session.query(Clientes_fisicos).filter(Clientes.nombre == nombre).filter(Clientes_fisicos.apellido_paterno == apellido_paterno and Clientes_fisicos.curp == curp).first())
            if cliente_existente:
                return True
            else:
                cliente = Clientes_fisicos(
                    nombre = nombre, correo = correo, rfc = rfc, telefono = telefono, pais = pais, estado = estado, ciudad = ciudad, avenidas = avenidas, calles = calles, codigo_postal = codigo_postal, direccion_adicional = direccion_adicional, entidad_legalizada = entidad_legalizada, categoria_cliente_id = categoria_cliente_id, credito = credito, estado_credito = estado_credito, limite_credito = limite_credito, porcentaje_interes = porcentaje_interes, fecha_ultimo_reporte = fecha_ultimo_reporte, credito_disponible = credito_disponible, credito_utilizado = credito_utilizado, tipo_cliente = tipo_cliente, aplica_descuento = aplica_descuento, porcentaje_descuento = porcentaje_descuento, comentarios = comentarios, areas_de_negocios_id = areas_de_negocios_id, apellido_paterno = apellido_paterno, apellido_materno = apellido_materno, curp = curp, fecha_nacimiento = fecha_nacimiento, num_identificacion = num_identificacion, ocupacion = ocupacion, ingresos = ingresos, estado_civil = estado_civil, foto = foto
                    )
                self.session.add(cliente)
                self.session.flush()
                return cliente
        except Exception as e:
            print(f"Error al agregar cliente fisico: {e}")

    def agregar_cliente_moral(self,nombre, correo, rfc, telefono, pais, estado, ciudad, avenidas, calles, codigo_postal, direccion_adicional, entidad_legalizada, categoria_cliente_id, credito, estado_credito, limite_credito, porcentaje_interes, fecha_ultimo_reporte, credito_disponible, credito_utilizado, tipo_cliente, aplica_descuento, porcentaje_descuento, comentarios, areas_de_negocios_id, razon_social, fecha_constitucion, web, sector, nif):
        try:
            cliente_existente = (self.session.query(Clientes_morales).filter(Clientes.nombre == nombre).filter(Clientes_morales.razon_social == razon_social).first())
            if cliente_existente:
                return cliente_existente
            else:
                cliente = Clientes_morales(
                    nombre=nombre, correo = correo , rfc = rfc, telefono = telefono, pais = pais, estado = estado, ciudad = ciudad, avenidas = avenidas, calles = calles, codigo_postal = codigo_postal, direccion_adicional = direccion_adicional, entidad_legalizada = entidad_legalizada, categoria_cliente_id = categoria_cliente_id, credito = credito, estado_credito = estado_credito, limite_credito = limite_credito, porcentaje_interes = porcentaje_interes, fecha_ultimo_reporte = fecha_ultimo_reporte, credito_disponible = credito_disponible, credito_utilizado = credito_utilizado, tipo_cliente = tipo_cliente, aplica_descuento = aplica_descuento,porcentaje_descuento = porcentaje_descuento, comentarios = comentarios, areas_de_negocios_id = areas_de_negocios_id, razon_social = razon_social, fecha_constitucion = fecha_constitucion,  web = web, sector = sector, NIF = nif
                )
                self.session.add(cliente)
                self.session.flush()
                return cliente
        except Exception as e:
            print(f"Error al agregar cliente moral: {e}")
        
    def agregar_representante_cliente_moral(self, nombre, telefono, correo, puesto):
    
        try:
            representante_existente = (self.session.query(Representantes_clientes_morales).filter(Representantes_clientes_morales.nombre == nombre, Representantes_clientes_morales.telefono == telefono).first())
            if representante_existente:
                print('representante existente')
                return representante_existente
            else:
                representante = Representantes_clientes_morales(nombre = nombre, telefono = telefono, correo = correo, puesto = puesto)
                self.session.add(representante)
                self.session.flush()
                print ('representante agregado')
                return representante
        except Exception as e:
            print(f"Error al agregar representante de cliente moral: {e}")

    def mostrar_clientes_fisicos(self):
        try:
            #comment: alias de la tabla
            clientes_fisicos_alias = aliased(Clientes_fisicos, flat=True)
            #comment: usar el alias en la consulta
            clientes = (
                self.session.query(Clientes, clientes_fisicos_alias)
                .filter(Clientes.tipo_cliente == 'FISICO')
                .join(clientes_fisicos_alias, Clientes.id == clientes_fisicos_alias.id)
                .all())
            print(clientes)
            if clientes:
                return clientes
            else:
                return None
        except Exception as e:
            print(f"Error al mostrar clientes fisicos: {e}")

    def mostrar_clientes_morales(self):
        try:
                # Alias explícito para Clientes_morales
            clientes_morales_alias = aliased(Clientes_morales, flat=True)
            
            # Consulta usando el alias
            clientes = (
                self.session.query(Clientes, clientes_morales_alias)
                .filter(Clientes.tipo_cliente == 'MORAL')
                .join(clientes_morales_alias, Clientes.id == clientes_morales_alias.id)
                .all()
            )
            return clientes
        except Exception as e:
            print(f"Error al mostrar clientes morales: {e}")

    def obtener_cliente_fisico_por_id(self, id):
        try:
            clientes_fisicos_alias = aliased(Clientes_fisicos)
            cliente = (self.session.query(Clientes, clientes_fisicos_alias)
                        .join(clientes_fisicos_alias, Clientes.id == clientes_fisicos_alias.id)
                        .filter(Clientes.id == id)
                        .first())
            if cliente:
                return cliente
            else:
                print(f"No se encontró cliente con ID: {id}")
                return None
        except Exception as e:
            print(f'error en la consulta:  {e}')

    def obtener_cliente_moral_por_id(self, id):
        try:
            clientes_morales_alias = aliased(Clientes_morales)
            cliente = (self.session.query(Clientes, clientes_morales_alias)
                        .join(clientes_morales_alias, Clientes.id == clientes_morales_alias.id)
                        .filter(Clientes.id == id)
                        .first())
            if cliente:
                return cliente
            else:
                print(f"No se encontró cliente con ID: {id}")
                return None
        except Exception as e:
            print(f'error en la consulta:  {e}')

    def filtrar_clientes_por_nombre(self, valor_buscado, tipo_cliente, modelo_tipo_cliente):
        try:
            clientes_tabla_alias = aliased(modelo_tipo_cliente)  # Usar el modelo, no una cadena
            clientes = (self.session.query(Clientes, clientes_tabla_alias)
                        .join(clientes_tabla_alias, Clientes.id == clientes_tabla_alias.id, isouter=True)
                        .filter(Clientes.tipo_cliente == tipo_cliente)
                        .filter(
                            or_(
                                Clientes.nombre.ilike(f'%{valor_buscado}%'),
                                clientes_tabla_alias.apellido_paterno.ilike(f'%{valor_buscado}%'),
                                clientes_tabla_alias.apellido_materno.ilike(f'%{valor_buscado}%'),
                                clientes_tabla_alias.curp.ilike(f'%{valor_buscado}%')
                            )
                        )
                        .all()
                    )
            return clientes
        except Exception as e:
            print(f'Error en la consulta: {e}')

    def actualizar_cliente_fisico(self, id, nombre, correo, rfc, telefono, pais, estado, ciudad, avenidas, calles, codigo_postal, direccion_adicional, entidad_legalizada, categoria_cliente_id, credito, estado_credito, limite_credito, porcentaje_interes, fecha_ultimo_reporte, credito_disponible, credito_utilizado, aplica_descuento, porcentaje_descuento, comentarios, areas_de_negocios_id, apellido_paterno, apellido_materno, curp, fecha_nacimiento, num_identificacion, ocupacion, ingresos, estado_civil, foto):
        try: 
            clientes_fisicos_alias = aliased(Clientes_fisicos)
            if id:
                # Consultar el cliente base y cliente físico
                cliente_base, cliente_fisico = (self.session.query(Clientes, Clientes_fisicos)
                                                .join(clientes_fisicos_alias, Clientes.id == clientes_fisicos_alias.id)
                                                .filter(Clientes.id == id)
                                                .first())
                
                if cliente_base and cliente_fisico:
                    # Actualizar los campos del cliente base
                    cliente_base.nombre = nombre
                    cliente_base.correo  = correo
                    cliente_base.rfc = rfc
                    cliente_base.telefono = telefono
                    cliente_base.pais = pais
                    cliente_base.estado = estado
                    cliente_base.ciudad = ciudad
                    cliente_base.avenidas = avenidas
                    cliente_base.calles = calles
                    cliente_base.codigo_postal = codigo_postal
                    cliente_base.direccion_adicional = direccion_adicional
                    cliente_base.entidad_legalizada = entidad_legalizada
                    cliente_base.credito = credito
                    cliente_base.estado_credito = estado_credito
                    cliente_base.limite_credito = limite_credito
                    cliente_base.porcentaje_interes = porcentaje_interes
                    cliente_base.fecha_ultimo_reporte = fecha_ultimo_reporte
                    cliente_base.credito_disponible = credito_disponible
                    cliente_base.credito_utilizado = credito_utilizado
                    cliente_base.aplica_descuento = aplica_descuento
                    cliente_base.porcentaje_descuento = porcentaje_descuento
                    cliente_base.comentarios = comentarios

                    # Actualizar los campos del cliente físico
                    cliente_fisico.apellido_paterno = apellido_paterno
                    cliente_fisico.apellido_materno = apellido_materno
                    cliente_fisico.curp = curp
                    cliente_fisico.fecha_nacimiento = fecha_nacimiento
                    cliente_fisico.num_identificacion = num_identificacion
                    cliente_fisico.ocupacion = ocupacion
                    cliente_fisico.ingresos = ingresos
                    cliente_fisico.estado_civil = estado_civil
                    cliente_fisico.foto = foto

                    # Actualizar categoría y área de negocios
                    if categoria_cliente_id:
                        categoria = self.session.query(Categorias_de_clientes).get(categoria_cliente_id)
                        if categoria:
                            cliente_base.categoria = categoria
                        else:
                            print(f"No se encontró categoría de cliente con ID: {categoria_cliente_id}")

                    if areas_de_negocios_id:
                        area = self.session.query(Areas_negocios).get(areas_de_negocios_id)
                        if area:
                            cliente_base.areas_de_negocios = area
                        else:
                            print(f'No se encontró área de negocio con ID: {areas_de_negocios_id}')
                    
                    # Confirmar cambios
                    self.session.commit()
                    print(f"Cliente con ID {id} actualizado correctamente")
                    return True
                else:
                    print(f"No se encontró cliente con ID: {id}")
                    return False
        except Exception as e:
            print(f'Error al hacer la actualización: {e}')
            self.session.rollback()
            return False

    def actualizar_cliente_moral(self, id, nombre, correo, rfc, telefono, pais, estado, ciudad, avenidas, calles, codigo_postal, direccion_adicional, entidad_legalizada, categoria_cliente_id, credito, estado_credito, limite_credito, porcentaje_interes, fecha_ultimo_reporte, credito_disponible, credito_utilizado, aplica_descuento, porcentaje_descuento, comentarios, areas_de_negocios_id, razon_social, fecha_constitucion, web, sector, nif, nombre_representante, telefono_representante, correo_representante, puesto_representante):
        try: 
            clientes_morales_alias = aliased(Clientes_morales)
            if id:
                # Consultar el cliente base y cliente físico
                cliente_base, cliente_moral = (self.session.query(Clientes, Clientes_morales)
                                                .join(clientes_morales_alias, Clientes.id == clientes_morales_alias.id)
                                                .filter(Clientes.id == id)
                                                .first())
                
                if cliente_base and cliente_moral:
                    # Actualizar los campos del cliente base
                    cliente_base.nombre = nombre
                    cliente_base.correo  = correo
                    cliente_base.rfc = rfc
                    cliente_base.telefono = telefono
                    cliente_base.pais = pais
                    cliente_base.estado = estado
                    cliente_base.ciudad = ciudad
                    cliente_base.avenidas = avenidas
                    cliente_base.calles = calles
                    cliente_base.codigo_postal = codigo_postal
                    cliente_base.direccion_adicional = direccion_adicional
                    cliente_base.entidad_legalizada = entidad_legalizada
                    cliente_base.credito = credito
                    cliente_base.estado_credito = estado_credito
                    cliente_base.limite_credito = limite_credito
                    cliente_base.porcentaje_interes = porcentaje_interes
                    cliente_base.fecha_ultimo_reporte = fecha_ultimo_reporte
                    cliente_base.credito_disponible = credito_disponible
                    cliente_base.credito_utilizado = credito_utilizado
                    cliente_base.aplica_descuento = aplica_descuento
                    cliente_base.porcentaje_descuento = porcentaje_descuento
                    cliente_base.comentarios = comentarios

                    # Actualizar el cliente moral
                    cliente_moral.razon_social = razon_social
                    cliente_moral.fecha_constitucion = fecha_constitucion
                    cliente_moral.NIF = nif
                    cliente_moral.web = web
                    cliente_moral.sector = sector

                    # Actualizar categoría y área de negocios
                    if categoria_cliente_id:
                        categoria = self.session.query(Categorias_de_clientes).get(categoria_cliente_id)
                        if categoria:
                            cliente_base.categoria = categoria
                        else:
                            print(f"No se encontró categoría de cliente con ID: {categoria_cliente_id}")

                    if areas_de_negocios_id:
                        area = self.session.query(Areas_negocios).get(areas_de_negocios_id)
                        if area:
                            cliente_base.areas_de_negocios = area
                        else:
                            print(f'No se encontró área de negocio con ID: {areas_de_negocios_id}')
                    # Actualizar o agregar representante
                    if cliente_moral.representante:
                        print('si contiene representante')
                        # Actualizar el primer representante si existe
                        representante = cliente_moral.representante  # O usa un índice adecuado
                        if not (nombre_representante and telefono_representante and correo_representante and puesto_representante):
                            cliente_moral.representante = None
                        else:
                            representante.nombre = nombre_representante
                            representante.telefono = telefono_representante
                            representante.correo = correo_representante
                            representante.puesto = puesto_representante
                    else:
                        # Si no hay representante, crear uno nuevo
                        if nombre_representante and  telefono_representante and correo_representante and puesto_representante:
                            nuevo_representante = self.agregar_representante_cliente_moral(
                                nombre=nombre_representante,
                                telefono=telefono_representante,
                                correo=correo_representante,
                                puesto=puesto_representante
                            )
                            self.session.add(nuevo_representante)
                            cliente_moral.representante = nuevo_representante
                    print(f"Cliente con ID {id} actualizado correctamente")
                    return True
                else:
                    print(f"No se encontró cliente con ID: {id}")
                    return False
        except Exception as e:
            print(f'Error al hacer la actualización: {e}')
            self.session.rollback()
            return False
        
    def eliminar_cliente(self, id, modelo):
        try:
            cliente = self.session.query(modelo).filter(modelo.id == id).one_or_none()
            if cliente:
                self.session.delete(cliente)
                print(f"se elimino el registro del cliente {modelo}")
                return True
            return False
        except Exception as e:
            print(f'Error al eliminar el cliente: {modelo} ---- {e}')
            return False


