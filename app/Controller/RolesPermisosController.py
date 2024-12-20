from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from .MensajesAlertasController import Mensaje
from ..DataBase.conexionBD import Conexion_base_datos
from ..View.UserInterfacePy.UI_CONTROL_ROLES import Ui_Control_Roles_Permisos


class ControlRolesController(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Control_Roles_Permisos()
        self.ui.setupUi(self)
        pantalla = self.frameGeometry()
        pantalla.moveCenter(self.screen().availableGeometry().center())
        self.move(pantalla.topLeft())

        self.permisos = []

        for atributo in dir(self.ui):
            if atributo.startswith('opcion_'):
                caja = getattr(self.ui, atributo)
                caja.stateChanged.connect(self.comprobar_caja_verificacion)

    def comprobar_caja_verificacion(self, state):
        sender = self.sender()
        verificacion = sender.objectName()
        if state == Qt.Checked:
            if verificacion not in self.permisos:
                self.permisos.append(verificacion.split('_')[1])
        else:
            if verificacion in self.permisos:
                self.permisos.remove(verificacion[1])