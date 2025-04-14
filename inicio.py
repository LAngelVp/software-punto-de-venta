from sqlalchemy import MetaData, Table, select, func
from app.DataBase.conexionBD import Conexion_base_datos
from app.Controller.InicioDeSesionController import Login
from app.Controller.VentanaInicialController import *
from app.Model.BaseDatosModel import Usuarios
from app.Controller.MensajesAlertasController import Mensaje
class Inicio_sistema:
    def __init__(self):
        super().__init__()
        self.ventana_principal = None
        self.Login = None
        self.app = QApplication(sys.argv)

    def comprobar_usuarios(self) -> int:
        try:
            with Conexion_base_datos() as db:
                session = db.abrir_sesion()
                consulta = select(func.count()).select_from(Usuarios)
                return session.execute(consulta).scalar() or 0
        except Exception as e:
            Mensaje().mensaje_alerta(f"Error al verificar usuarios: {e}")
            return 0

    def ejecutar(self):
        """Lógica principal para iniciar la aplicación."""
        num_usuarios = self.comprobar_usuarios()

        if num_usuarios > 0:
            self.login = Login()
            self.login.show()
        else:
            self.ventana_principal = Inicio_principal()
            self.ventana_principal.show()

        sys.exit(self.app.exec_())

if __name__ == "__main__":
    sistema = Inicio_sistema()
    sistema.ejecutar()