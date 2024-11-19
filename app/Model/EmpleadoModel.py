import re
from sqlalchemy.exc import IntegrityError
from .BaseDatosModel import Empleados, Departamentos, Puestos, Sucursales

class EmpleadosModel:
    def __init__(self, session):
        self.session = session

    def crear_empleado(self, id_empleado, nombre, apellido_paterno, apellido_materno, fecha_nacimiento,
                         estado_civil, curp, rfc, nivel_academico, carrera, correo_electronico,
                         numero_seguro_social, fecha_contratacion, fecha_despido, ciudad,
                         codigo_postal, estado, pais, numero_telefonico, nombre_contacto,
                         contacto_emergencia, parentesco_contacto, calles, avenidas, colonia,
                         num_interior, num_exterior, direccion_adicional, activo, foto,
                         puesto_id, usuario_id, departamento_id, sucursal_id):
        if id_empleado is not None:
            empleado_existente = self.session.query(Empleados).filter(Empleados.id == id_empleado)
            if empleado_existente:
                self.actualizar_empleado(empleado_existente, nombre, apellido_paterno, apellido_materno, 
                                      fecha_nacimiento, estado_civil, curp, rfc, nivel_academico, 
                                      carrera, correo_electronico, numero_seguro_social, fecha_contratacion, 
                                      fecha_despido, ciudad, codigo_postal, estado, pais, numero_telefonico, 
                                      nombre_contacto, contacto_emergencia, parentesco_contacto, calles, avenidas, colonia, 
                                      num_interior, num_exterior, direccion_adicional, activo, foto, puesto_id, 
                                      usuario_id, departamento_id, sucursal_id)
        try:
            # Crear la instancia de empleado
            nuevo_empleado = Empleados(
                nombre=nombre,
                apellido_paterno=apellido_paterno,
                apellido_materno=apellido_materno,
                fecha_nacimiento=fecha_nacimiento,
                estado_civil=estado_civil,
                curp=curp,
                rfc=rfc,
                nivel_academico=nivel_academico,
                carrera=carrera,
                correo_electronico=correo_electronico,
                numero_seguro_social=numero_seguro_social,
                fecha_contratacion=fecha_contratacion,
                fecha_despido=fecha_despido,
                ciudad=ciudad,
                codigo_postal=codigo_postal,
                estado=estado,
                pais=pais,
                numero_telefonico=numero_telefonico,
                nombre_contacto=nombre_contacto,
                contacto_emergencia=contacto_emergencia,
                parentesco_contacto=parentesco_contacto,
                calles=calles,
                avenidas=avenidas,
                colonia = colonia,
                num_interior=num_interior,
                num_exterior=num_exterior,
                direccion_adicional=direccion_adicional,
                activo=activo,
                foto=foto,
                puesto_id=puesto_id,
                usuario_id=usuario_id,
                departamento_id=departamento_id,
                sucursal_id=sucursal_id
            )
            
            
            # Agregar a la sesión, pero no hacer commit aquí
            self.session.add(nuevo_empleado)
            self.session.flush()  # Generar el ID sin hacer commit
            return nuevo_empleado.id
        
        except IntegrityError as e:
            mensaje_error = str(e.orig)
            mensaje_error = re.sub(r'Key\s*|\(|\)', '', mensaje_error)
            print(f'Error de integridad: {mensaje_error}')
            return None
        
        except Exception as e:
            print(f'Error general al insertar empleado: {e}')
            return None
        
    def obtener_empleados_detallados(self):
        try:
            empleados = self.session.query(Empleados).\
            outerjoin(Puestos).\
            outerjoin(Departamentos).\
            outerjoin(Sucursales).\
            all()

            if empleados:
                return empleados, True
            else:
                print("No se encontraron empleados.")
                return [], False
        except Exception as e:
            print("Error al obtener empleados:", e)
            return [], False

    def eliminar_empleado(self, id):
        empleado = self.session.query(Empleados).filter(Empleados.id == id).one_or_none()
        if empleado:
            self.session.delete(empleado)
            return True
        return False
    
    def filtrar_empleados(self, id = None, nombre = None):
        consulta = self.session.query(Empleados).outerjoin(Puestos).outerjoin(Departamentos).outerjoin(Sucursales)
    
        # Si se pasa un `id`, agrega el filtro por `id`
        if id:
            consulta = consulta.filter(Empleados.id == id)
        
        # Si se pasa un `nombre`, agrega el filtro por `nombre`
        if nombre:
            consulta = consulta.filter(Empleados.nombre.ilike(f"%{nombre}%"))
        
        # Ejecuta la consulta y guarda los resultados
        empleados = consulta.all()
        if empleados:
            return empleados, True
        return None, False
    
    def obtener_empleado_por_id(self, id):
        if id:
            empleado = self.session.query(Empleados).filter(Empleados.id == id).first()
            if empleado:
                return empleado, True
            else:
                return None, False
    def actualizar_empleado(self, empleado_existente, nombre, apellido_paterno, apellido_materno, fecha_nacimiento,
                        estado_civil, curp, rfc, nivel_academico, carrera, correo_electronico,
                        numero_seguro_social, fecha_contratacion, fecha_despido, ciudad,
                        codigo_postal, estado, pais, numero_telefonico, nombre_contacto,
                        contacto_emergencia, parentesco_contacto, calles, avenidas, colonia,
                        num_interior, num_exterior, direccion_adicional, activo, foto,
                        puesto_id, usuario_id, departamento_id, sucursal_id):
        try:
            # Actualizamos los campos que pueden haber cambiado
            empleado_existente.nombre = nombre
            empleado_existente.apellido_paterno = apellido_paterno
            empleado_existente.apellido_materno = apellido_materno
            empleado_existente.fecha_nacimiento = fecha_nacimiento
            empleado_existente.estado_civil = estado_civil
            empleado_existente.curp = curp
            empleado_existente.rfc = rfc
            empleado_existente.nivel_academico = nivel_academico
            empleado_existente.carrera = carrera
            empleado_existente.correo_electronico = correo_electronico
            empleado_existente.numero_seguro_social = numero_seguro_social
            empleado_existente.fecha_contratacion = fecha_contratacion
            empleado_existente.fecha_despido = fecha_despido
            empleado_existente.ciudad = ciudad
            empleado_existente.codigo_postal = codigo_postal
            empleado_existente.estado = estado
            empleado_existente.pais = pais
            empleado_existente.numero_telefonico = numero_telefonico
            empleado_existente.nombre_contacto = nombre_contacto
            empleado_existente.contacto_emergencia = contacto_emergencia
            empleado_existente.parentesco_contacto = parentesco_contacto
            empleado_existente.calles = calles
            empleado_existente.avenidas = avenidas
            empleado_existente.colonia = colonia
            empleado_existente.num_interior = num_interior
            empleado_existente.num_exterior = num_exterior
            empleado_existente.direccion_adicional = direccion_adicional
            empleado_existente.activo = activo
            empleado_existente.foto = foto
            empleado_existente.puesto_id = puesto_id
            empleado_existente.usuario_id = usuario_id
            empleado_existente.departamento_id = departamento_id
            empleado_existente.sucursal_id = sucursal_id
            
            print(f"Empleado con ID {empleado_existente.id} actualizado correctamente.")
        except Exception as e:
            print(f"Error al actualizar el empleado: {e}")
            self.session.rollback()  # Si algo falla, revertimos los cambios