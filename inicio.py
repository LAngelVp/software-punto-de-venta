from sqlalchemy import MetaData, Table, select, func
from app.DataBase.conexionBD import Conexion_base_datos
from app.Controller.InicioDeSesionController import Login
from app.Controller.VentanaInicialController import *
from app.Model.BaseDatosModel import Usuarios
from app.Model.GruposyPermisosModel import PermisosModel, RolesModel
class Inicio_sistema:
    def __init__(self):
        self.conexion = Conexion_base_datos()

#funciones principales:
        
    def comprobar_usuarios(self):
        with self.conexion as db:
            consulta = select(func.count()).select_from(Usuarios)
            result = self.conexion.session.execute(consulta).scalar()
            self.conexion.cerrar_sesion()
            return result
        
    def crear_datos_principales(self):
        with Conexion_base_datos() as db:
            session = db.abrir_sesion()
            with session.begin():
                try:
                    PermisosModel(session).crear_permiso()
                    RolesModel(session).crear_grupo_principal()
                except Exception as e:
                    print(e)

def main():
    app = QApplication(sys.argv)
    
    sistema = Inicio_sistema()
    resultado = sistema.comprobar_usuarios()
    sistema.crear_datos_principales()


    if resultado > 0:
        login_window = Login()
        login_window.show()
    else:
        principal_window = Inicio_principal() 
        principal_window.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()