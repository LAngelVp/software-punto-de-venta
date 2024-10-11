from PyQt5 import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from ..View.UserInterfacePy.UI_NUEVA_AREA_NEGOCIO import *
from ..DataBase.conexionBD import Conexion_base_datos
from ..Model.AreaNegocioClientesModel import  *
from .MensajesAlertasController import Mensaje
from ..Model.AreaNegocioClientesModel import  AreaNegocioClientesModel


class AreaNegocioClientesController(QWidget):
    signal_area = pyqtSignal()
    def __init__(self, tipo_cliente = None):
        super().__init__()
        self.ui = Ui_Nueva_area_negocio()
        self.ui.setupUi(self)
        self.tipo_de_cliente = tipo_cliente
        self.ui.btn_btn_guardar.clicked.connect(self.agregar_area)

    def agregar_area(self):
        if not self.ui.txt_nombre.text() and not self.ui.txtlargo_descripcion.toPlainText():
            Mensaje().mensaje_alerta("Los datos estan incompletos.")
            return
        try:
            with Conexion_base_datos() as db:
                session =  db.abrir_sesion()
                area = AreaNegocioClientesModel(session).agregar_area(
                    nombre = self.ui.txt_nombre.text().upper().strip(),
                    descripcion = self.ui.txtlargo_descripcion.toPlainText().upper().strip()
                )
                session.commit()
                Mensaje().mensaje_alerta(f'Area de negocio agregada con exito. {area}')
                self.signal_area.emit()
        except Exception as e:
            print(f'Error al agregar el area de negocio. {e}')
        self.close()
                        