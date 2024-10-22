from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QIcon
from ..Source.ibootstrap_rc import *
class Mensaje:
    def __init__(self):
        self.mensaje = QMessageBox()
        self.mensaje.setWindowIcon(QIcon(':/Icons/Bootstrap/chat-text.svg'))

    def mensaje_informativo(self, cuerpo):
        self.mensaje.setIcon(QMessageBox.Information)
        self.mensaje.setWindowTitle('Informacion')
        self.mensaje.setText(cuerpo)
        self.mensaje.setStandardButtons(QMessageBox.Ok)
        self.mensaje.exec_()

    def mensaje_alerta(self, cuerpo):
        self.mensaje.setIcon(QMessageBox.Warning)
        self.mensaje.setWindowTitle('Alerta')
        self.mensaje.setText(cuerpo)
        self.mensaje.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        # Personalizando los botones
        boton_reintentar = self.mensaje.button(QMessageBox.Cancel)
        boton_reintentar.setText("Cancelar")
        respuesta = self.mensaje.exec_()
        return respuesta
    def mensaje_critico(self, cuerpo ):
        self.mensaje.setIcon(QMessageBox.Critical)
        self.mensaje.setWindowTitle('Critico')
        self.mensaje.setText(cuerpo)
        self.mensaje.setStandardButtons(QMessageBox.Abort | QMessageBox.Retry | QMessageBox.Ignore)
        # Personalizando los botones
        boton_abortar = self.mensaje.button(QMessageBox.Abort)
        boton_abortar.setText("Detener")

        boton_reintentar = self.mensaje.button(QMessageBox.Retry)
        boton_reintentar.setText("Reintentar")

        boton_ignorar = self.mensaje.button(QMessageBox.Ignore)
        boton_ignorar.setText("Ignorar")

        respuesta = self.mensaje.exec_()
        
        return respuesta
    def mensaje_pregunta(self, cuerpo ):
        self.mensaje.setIcon(QMessageBox.Information)
        self.mensaje.setWindowTitle('Pregunta')
        self.mensaje.setText(cuerpo)
        self.mensaje.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        respuesta = self.mensaje.exec_()
        return respuesta