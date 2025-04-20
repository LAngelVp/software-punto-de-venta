# from PyQt5.QtCore import QObject, QThread, pyqtSignal
# from ..DataBase.conexionBD import Conexion_base_datos

# class Worker(QObject):
#     finished = pyqtSignal()
#     result_ready = pyqtSignal(object)  # Emitirá el resultado de la función
#     error = pyqtSignal(str)

#     def __init__(self, funcion, *args, **kwargs):
#         super().__init__()
#         self.funcion = funcion
#         self.args = args
#         self.kwargs = kwargs

#     def run(self):
#         try:
#             with Conexion_base_datos() as db:
#                 session = db.abrir_sesion()
#                 with session.begin():
#                     resultado, estado = self.funcion(session, *self.args, **self.kwargs)

#             if estado:
#                 self.result_ready.emit(resultado)
#             else:
#                 self.result_ready.emit(None)
#         except Exception as e:
#             self.error.emit(str(e))
#         self.finished.emit()

# class Consultas_segundo_plano(QObject):
#     terminado = pyqtSignal()

#     def __init__(self):
#         super().__init__()
#         self.thread = None
#         self.worker = None

#     def ejecutar_hilo(self, funcion, callback, *args, **kwargs):
#         if self.thread is None or not self.thread.isRunning():
#             self.thread = QThread()
#             self.worker = Worker(funcion, *args, **kwargs)
#             self.worker.moveToThread(self.thread)

#             # Conectar señales
#             self.thread.started.connect(self.worker.run)
#             self.worker.result_ready.connect(callback)
#             self.worker.finished.connect(self.thread.quit)
#             self.worker.finished.connect(self.worker.deleteLater)
#             self.thread.finished.connect(self.thread.deleteLater)
#             self.worker.finished.connect(self.terminado.emit)
#             self.worker.error.connect(lambda e: print(f"Error ejecutando la consulta en hilo: {e}"))

#             # Iniciar el hilo
#             self.thread.start()
#         else:
#             print("El hilo ya está en ejecución")





import threading
from PyQt5.QtCore import QObject, pyqtSignal
from ..DataBase.conexionBD import Conexion_base_datos

class Consultas_segundo_plano(QObject):
    terminado = pyqtSignal()
    resultado = pyqtSignal(object)
    error = pyqtSignal(str)

    def ejecutar_hilo(self, funcion, *args, **kwargs):
        # Función de tarea
        def tarea():
            try:
                with Conexion_base_datos() as db:
                    session = db.abrir_sesion()
                    productos, estado = funcion(session, *args, **kwargs)
                    if estado:
                        self.resultado.emit(productos)
                    else:
                        self.resultado.emit(None)
            except Exception as e:
                self.error.emit(str(e))
            finally:
                self.terminado.emit()

        hilo = threading.Thread(target=tarea, daemon=True)
        hilo.start()


