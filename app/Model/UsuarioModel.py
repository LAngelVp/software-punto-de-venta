from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .BaseDatosModel import Usuarios, Roles
from .CreadencialesUsuarioModel import *
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
            return usuario_existente.id

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
            
