import threading
from PyQt5.QtCore import QObject, pyqtSignal
from ..DataBase.conexionBD import Conexion_base_datos

class Consultas_segundo_plano(QObject):
    terminado = pyqtSignal()
    resultado = pyqtSignal(object, bool)
    error = pyqtSignal(str)

    def ejecutar_hilo(self, funcion, *args, **kwargs):
        # Función de tarea
        def tarea():
            try:
                with Conexion_base_datos() as db:
                    session = db.abrir_sesion()
                    productos, estado = funcion(session, *args, **kwargs)
                    if estado:
                        self.resultado.emit(productos, estado)
                    else:
                        self.resultado.emit(None, estado)
            except Exception as e:
                self.error.emit(str(e))
            finally:
                self.terminado.emit()

        hilo = threading.Thread(target=tarea, daemon=True)
        hilo.start()


