from  sqlalchemy.orm import joinedload
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
                # usuario_existe, estatus = UsuarioModel(session).consultar_usuario(nombre=usuario)
                usuario_existe = session.query(Usuarios).options(joinedload(Usuarios.empleado)).filter_by(usuario=usuario).first()
            if usuario_existe:
                if bcrypt.checkpw(contraseña.encode(), usuario_existe.contraseña):
                    return usuario_existe, True
                else:
                    return None, False
            return None, False
