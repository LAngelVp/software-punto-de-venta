from ..Source.gifs_rc import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QThread, pyqtSignal, QObject
from PyQt5.QtGui import QPixmap
import sys
import time
from ..View.UserInterfacePy.UI_PROCESO_CARGANDO import Ui_Ventana_Cargando


class AnimationController(QObject):
    trigger_animation = pyqtSignal()

    def __init__(self):
        super().__init__()
        self._running = True

    def run(self):
        while self._running:
            self.trigger_animation.emit()
            time.sleep(3)  # Pausa de 3 segundos antes de reiniciar la animación

    def stop(self):
        self._running = False


class Ventana_proceso_cargando(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Ventana_Cargando()
        self.ui.setupUi(self)
        
        self.setWindowFlags(self.windowFlags() | Qt.WindowType.FramelessWindowHint) 
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        # Cargar un gif de carga simple o animación circular
        gif_path = ':/gifs/Icons/Gif/loader.gif'  # Cambia esta ruta a tu propio GIF de carga
        self.movie = QtGui.QMovie(gif_path)
        self.ui.etiqueta_spiner.setMovie(self.movie)
        
        self.movie.start()

        # Crear escena gráfica para la animación
        self.scene = QtWidgets.QGraphicsScene()
        self.view = QtWidgets.QGraphicsView(self.scene, self)
        self.view.setStyleSheet("background: transparent; border: none;")
        self.view.setFixedSize(self.ui.etiqueta_spiner.size())
        self.view.setAlignment(Qt.AlignCenter)
        self.view.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.view.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        # Ubicar la vista donde estaba el QLabel original
        self.view.move(self.ui.etiqueta_spiner.pos())
        self.scene.addWidget(self.ui.etiqueta_spiner)

        # Hilo para controlar la animación
        self.controller = AnimationController()
        self.controller_thread = QThread()
        self.controller.moveToThread(self.controller_thread)

        self.controller.trigger_animation.connect(self.start_animation)
        self.controller_thread.started.connect(self.controller.run)
        self.controller_thread.start()

    def start_animation(self):
        # Aquí reiniciamos la animación para que empiece de nuevo cada 3 segundos
        self.movie.jumpToFrame(0)
        self.movie.start()

    def closeEvent(self, event):
        self.controller.stop()
        self.controller_thread.quit()
        self.controller_thread.wait()
        super().closeEvent(event)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Ventana_proceso_cargando()
    window.show()
    sys.exit(app.exec_())
