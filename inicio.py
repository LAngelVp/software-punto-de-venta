from sqlalchemy import MetaData, Table, select, func
from app.DataBase.conexionBD import Conexion_base_datos
from app.Controller.InicioDeSesionController import Login
from app.Controller.VentanaInicialController import *
from app.Model.BaseDatosModel import Usuarios
from app.Controller.MensajesAlertasController import Mensaje
class Inicio_sistema:
    def __init__(self):
        pass
#funciones principales:
        
    def comprobar_usuarios(self):
        with Conexion_base_datos() as db:
            session = db.abrir_sesion()
            with session.begin():
                consulta = select(func.count()).select_from(Usuarios)
                result = session.execute(consulta).scalar()
                return result

def main():
    app = QApplication(sys.argv)
    
    sistema = Inicio_sistema()
    resultado = sistema.comprobar_usuarios()


    if resultado > 0:
        login_window = Login()
        login_window.show()
    else:
        principal_window = Inicio_principal() 
        principal_window.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()