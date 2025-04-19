import threading
from ..DataBase.conexionBD import Conexion_base_datos
from PyQt5.QtCore import QObject, pyqtSignal


class Consultas_segundo_plano(QObject):
    terminado = pyqtSignal()
    def ejecutar_hilo(self, funcion, callback, *args, **kwargs):
        # Función para ejecutar la tarea en un hilo
        def tarea():
            try:
                # Abrir la conexión a la base de datos
                with Conexion_base_datos() as db:
                    session = db.abrir_sesion()
                    with session.begin():
                        # Llamamos a la función que recibe la session y otros argumentos
                        resultado, estado = funcion(session, *args, **kwargs)
                    
                    # Si la operación fue exitosa, llamamos al callback
                    if estado:
                        callback(resultado)
                    else:
                        callback(None)  # Si no fue exitoso
            except Exception as e:
                print(f"Error ejecutando la consulta en hilo: {e}")
            self.terminado.emit()
        # Crear e iniciar el hilo
        hilo = threading.Thread(target=tarea)
        hilo.start()