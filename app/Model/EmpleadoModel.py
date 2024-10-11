import re
from sqlalchemy.exc import IntegrityError
from .BaseDatosModel import Empleados

class EmpleadosModel:
    def __init__(self, session):
        self.session = session

    def crear_empleado(self, nombre,apellido_paterno,apellido_materno, fecha_nacimiento, estado_civil, curp, rfc, correo, nss,fecha_contratacion, ciudad, cp, estado, pais, numero_telefono, direccion,activo, hora_entrada, hora_salida, foto=None, puesto_id=None, usuario_id=None, departamento_id=None):
        try:
            # Crear la instancia de empleado
            nuevo_empleado = Empleados(
                nombre=nombre,
                apellido_paterno = apellido_paterno,
                apellido_materno = apellido_materno,
                fecha_nacimiento=fecha_nacimiento,
                estado_civil=estado_civil,
                curp=curp,
                rfc=rfc,
                correo_electronico=correo,
                numero_seguro_social=nss,
                fecha_contratacion = fecha_contratacion,
                ciudad=ciudad,
                codigo_postal=cp,
                estado=estado,
                pais=pais,
                numero_telefonico=numero_telefono,
                direccion=direccion,
                activo = activo,
                hora_entrada = hora_entrada,
                hora_salida = hora_salida,
                foto=foto,
                puesto_id=puesto_id,
                usuario_id=usuario_id,
                departamento_id = departamento_id
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