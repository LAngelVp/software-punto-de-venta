from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .BaseDatosModel import Usuarios, Roles
from ..Controller.CodificarPasswordController import *
from datetime import datetime
class UsuarioModel:
    def __init__(self, session):
        self.session = session

    def crear_usuario(self, usuario, password, fecha_creacion, fecha_actualizacion = None, rol_id=None):
        # Hash de la contraseña
        contraseña_hasheada = EncriptarPasswordConrtoller(password).hashear_password()
        
        # Verificar si el usuario ya existe
        usuario_existente = self.session.query(Usuarios).filter_by(usuario=usuario).first()
        if usuario_existente:
            return usuario_existente, False
            # return self.actualizar_usuario(usuario_existente.id, usuario, password, fecha_actualizacion, rol_id)

        # Crear el nuevo usuario
        nuevo_usuario = Usuarios(usuario=usuario, contraseña=contraseña_hasheada, fecha_creacion = fecha_creacion, fecha_actualizacion  = fecha_actualizacion, rol_id = rol_id)


        # Si se especificó un rol, asociarlo
        if rol_id:
            rol = self.session.query(Roles).filter_by(id=rol_id).first()
            if rol:
                nuevo_usuario.rol = rol
            else:
                return None
        
        # Agregar el usuario a la sesión, pero no hacer commit aquí
        try:
            self.session.add(nuevo_usuario)
            self.session.flush()
            return nuevo_usuario, True
        except Exception as e:
            return None
    
    def consultar_usuario(self, nombre):
        usuario = self.session.query(Usuarios).filter_by(usuario=nombre).first()
        if usuario:
            return usuario, True
        return None, False
    
    def actualizar_usuario(self, id, nuevo_usuario, nuevo_password, fecha_actualizacion, nuevo_rol_id = None):
        # Aquí puedes actualizar los atributos del usuario según los parámetros que quieras cambiar
        if id:
            usuario = self.session.query(Usuarios).filter_by(id=id).first()
            if usuario:
                # Actualizar el nombre de usuario si se proporciona un nuevo nombre
                if nuevo_usuario:
                    usuario.usuario = nuevo_usuario  # Actualizamos el nombre de usuario

                # Si se proporciona una nueva contraseña, actualizamos la contraseña
                if nuevo_password:
                    nueva_contraseña_hash = EncriptarPasswordConrtoller(nuevo_password).hashear_password()  # Hasheamos la nueva contraseña
                    usuario.contraseña = nueva_contraseña_hash  # Actualizamos la contraseña

                # Actualizar la fecha de actualización
                usuario.fecha_actualizacion = fecha_actualizacion

                # Si se proporciona un nuevo rol, lo actualizamos
                if nuevo_rol_id:
                    rol = self.session.query(Roles).filter_by(id=nuevo_rol_id).first()
                    if rol:
                        usuario.rol = rol  # Actualizamos el rol
                    else:
                        return None  # Si el rol no existe, salimos de la función
                return True
            return False
        else:
            return False

    def eliminar(self, id):
        usuario = self.session.query(Usuarios).filter_by(id=id).first()
        if usuario:
            self.session.delete(usuario)
            return True
        return False
