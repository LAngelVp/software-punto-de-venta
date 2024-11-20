from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .BaseDatosModel import Usuarios, Roles
from .CreadencialesUsuarioModel import *
from datetime import datetime
class UsuarioModel:
    def __init__(self, session):
        self.session = session

    def crear_usuario(self, usuario, password, fecha_creacion, fecha_actualizacion = None, rol_id=None):
        # Hash de la contraseña
        contraseña_hasheada = hash_class().hashear_password(password)
        
        # Verificar si el usuario ya existe
        usuario_existente = self.session.query(Usuarios).filter_by(usuario=usuario).first()
        if usuario_existente:
            print(f"El usuario {usuario} ya existe.")
            self.actualizar_usuario(usuario_existente)

        # Crear el nuevo usuario
        nuevo_usuario = Usuarios(usuario=usuario, contraseña=contraseña_hasheada, fecha_creacion = fecha_creacion, fecha_actualizacion  = fecha_actualizacion, rol_id = rol_id)


        # Si se especificó un rol, asociarlo
        if rol_id:
            rol = self.session.query(Roles).filter_by(id=rol_id).first()
            if rol:
                nuevo_usuario.rol = rol
            else:
                print(f"El rol {rol_id} no existe.")
                return None
        
        # Agregar el usuario a la sesión, pero no hacer commit aquí
        try:
            self.session.add(nuevo_usuario)
            self.session.flush()  # Asegura que el ID del usuario esté disponible sin hacer commit
            print(f"Usuario {usuario} creado con éxito.")
            return nuevo_usuario.id
        except Exception as e:
            print(f"Error al crear el usuario: {e}")
            return None
        
    def actualizar_usuario(self, usuario_existente):
        # Aquí puedes actualizar los atributos del usuario según los parámetros que quieras cambiar
        if usuario_existente:
            # Actualizar los campos que desees
            # Por ejemplo, actualizar la contraseña y la fecha de actualización
            nueva_contraseña = hash_class().hashear_password(usuario_existente.contraseña)  # O la nueva contraseña si la quieres cambiar
            usuario_existente.contraseña = nueva_contraseña
            usuario_existente.fecha_actualizacion = datetime.datetime.now()  # O el valor de la fecha que desees

            # Si hay un nuevo rol, puedes actualizarlo también
            if usuario_existente.rol_id:
                rol = self.session.query(Roles).filter_by(id=usuario_existente.rol_id).first()
                if rol:
                    usuario_existente.rol = rol  # Actualizar el rol si es necesario
            
            try:
                self.session.commit()  # Realizamos el commit para guardar los cambios
                print(f"Usuario {usuario_existente.usuario} actualizado con éxito.")
            except Exception as e:
                print(f"Error al actualizar el usuario: {e}")
                self.session.rollback()  # Si ocurre un error, hacemos rollback
        else:
            print("No se encontró el usuario para actualizar.")
            
