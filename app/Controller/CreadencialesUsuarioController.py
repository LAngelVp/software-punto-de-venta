import bcrypt
from ..Model.BaseDatosModel import Usuarios
from ..Model.UsuarioModel import UsuarioModel
from app.DataBase.conexionBD import *

class CredencialesModel:
    def __init__(self):
        self.conexion = Conexion_base_datos()
        
    def verificar_credenciales(self, usuario, contraseña):
        with self.conexion as db:
            session = db.abrir_sesion()
            with session.begin():
                usuario_existe, estatus = UsuarioModel(session).consultar_usuario(nombre=usuario)
                if estatus:
                    if bcrypt.checkpw(contraseña.encode(), usuario_existe.contraseña):
                        return True
                    else:
                        return False
                return False
