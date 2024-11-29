import re
from sqlalchemy.exc import IntegrityError
from .UsuarioModel import UsuarioModel
from .BaseDatosModel import Empleados, Departamentos, Puestos, Sucursales

class EmpleadosModel:
    def __init__(self, session):
        self.session = session

    def crear_empleado(self, nombre, apellido_paterno, apellido_materno, fecha_nacimiento,
                         estado_civil, genero, curp, rfc, nivel_academico, carrera, correo_electronico,
                         numero_seguro_social, fecha_contratacion, fecha_despido, ciudad,
                         codigo_postal, estado, pais, numero_telefonico, nombre_contacto,
                         contacto_emergencia, parentesco_contacto, calles, avenidas, colonia,
                         num_interior, num_exterior, direccion_adicional, activo, foto,
                         puesto_id, usuario_id, departamento_id, sucursal_id):
        try:
            empleado_existente = self.session.query((Empleados.curp == curp) | (Empleados.rfc == rfc)).first()
            if empleado_existente is not None:
                return None, False
            # Crear la instancia de empleado
            nuevo_empleado = Empleados(
                nombre=nombre,
                apellido_paterno=apellido_paterno,
                apellido_materno=apellido_materno,
                fecha_nacimiento=fecha_nacimiento,
                estado_civil=estado_civil,
                genero=genero,
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
            return nuevo_empleado, True
        
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
    
    def baja_empleado(self, id_empleado, estatus, fecha_baja):
        if id_empleado is None or estatus is None:
            print("dato vacio")
            return None, False
        empleado = self.session.query(Empleados).filter(Empleados.id == id_empleado).first()
        if empleado:
            print('empleado actualiza')
            empleado.activo = estatus
            empleado.fecha_despido = fecha_baja
            return empleado, True
        
    def alta_empleado(self, id_empleado, estatus, fecha_alta):
        if id_empleado is None or estatus is None:
            print("dato vacio")
            return None, False
        empleado = self.session.query(Empleados).filter(Empleados.id == id_empleado).first()
        if empleado:
            print('empleado actualiza')
            empleado.activo = estatus
            empleado.fecha_contratacion = fecha_alta
            empleado.fecha_despido = None
            return empleado, True
    
    def actualizar_empleado(self,id_empleado, nombre, apellido_paterno, apellido_materno, fecha_nacimiento,
                        estado_civil, genero, curp, rfc, nivel_academico, carrera, correo_electronico,
                        numero_seguro_social, fecha_contratacion, fecha_despido, ciudad,
                        codigo_postal, estado, pais, numero_telefonico, nombre_contacto,
                        contacto_emergencia, parentesco_contacto, calles, avenidas, colonia,
                        num_interior, num_exterior, direccion_adicional, foto,
                        puesto_id, departamento_id, sucursal_id):
        if id_empleado is not None:
            empleado = self.session.query(Empleados).filter(Empleados.id == id_empleado).first()
            if empleado is None:
                return None, False
        try:
            # Actualizamos los campos que pueden haber cambiado
            empleado.nombre = nombre
            empleado.apellido_paterno = apellido_paterno
            empleado.apellido_materno = apellido_materno
            empleado.fecha_nacimiento = fecha_nacimiento
            empleado.estado_civil = estado_civil
            empleado.genero = genero
            empleado.curp = curp
            empleado.rfc = rfc
            empleado.nivel_academico = nivel_academico
            empleado.carrera = carrera
            empleado.correo_electronico = correo_electronico
            empleado.numero_seguro_social = numero_seguro_social
            empleado.fecha_contratacion = fecha_contratacion
            empleado.fecha_despido = fecha_despido
            empleado.ciudad = ciudad
            empleado.codigo_postal = codigo_postal
            empleado.estado = estado
            empleado.pais = pais
            empleado.numero_telefonico = numero_telefonico
            empleado.nombre_contacto = nombre_contacto
            empleado.contacto_emergencia = contacto_emergencia
            empleado.parentesco_contacto = parentesco_contacto
            empleado.calles = calles
            empleado.avenidas = avenidas
            empleado.colonia = colonia
            empleado.num_interior = num_interior
            empleado.num_exterior = num_exterior
            empleado.direccion_adicional = direccion_adicional
            empleado.foto = foto
            empleado.puesto_id = puesto_id
            empleado.departamento_id = departamento_id
            empleado.sucursal_id = sucursal_id
            
            print(f"Empleado con ID {empleado.id} actualizado correctamente.")
            return empleado, True
        except Exception as e:
            print(f"Error al actualizar el empleado: {e}")
            self.session.rollback()
            return None, False
        

    def eliminar_credenciales(self, id):
        empleado = self.session.query(Empleados).filter(Empleados.id == id).first()
        if empleado is not None:
            if empleado.usuario is not None:
                usuario = UsuarioModel(self.session).eliminar(empleado.usuario_id)
            else:
                return False
            
            empleado.usuario_id = None
            return True
        return False
        