import bcrypt
from .BaseDatosModel import Usuarios
from app.DataBase.conexionBD import *
class hash_class:
    def __init__(self):
        self.conexion = Conexion_base_datos()
        
    def hashear_password(self, contraseña):
        self.password = bcrypt.hashpw(contraseña.encode(), bcrypt.gensalt())
        return self.password
    
    def verificar_credenciales(self, usuario, contraseña):
        with self.conexion as db:
            session = db.abrir_sesion()
            usuario_existe = session.query(Usuarios).filter_by(usuario = usuario).first()
            if usuario_existe:
                print(f"Usuario encontrado: {usuario}, Hash almacenado: {usuario_existe.contraseña}")
                is_valid = bcrypt.checkpw(contraseña.encode(), usuario_existe.contraseña)
                print(f"Contraseña válida: {is_valid}")
                return is_valid
            else:
                print("Usuario no encontrado")
            return False
