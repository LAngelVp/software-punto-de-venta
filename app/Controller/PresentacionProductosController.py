from PySide6 import QtCore, QtWidgets
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from .MensajesAlertasController import Mensaje
from ..View.UserInterfacePy.UI_AGREGAR_UN_DATO import Ui_Formulario
from ..Model.ProductosModel import ProductosModel
from ..DataBase.conexionBD import Conexion_base_datos

class PresentacionProductos(QWidget):
    SYGNAL_PRESENTACION_AGREGADA = Signal()
    def __init__(self):
        super().__init__()
        self.ui = Ui_Formulario()
        self.ui.setupUi(self)
        self.setWindowTitle("Presentación")
        self.ui.btn_btn_guardar.clicked.connect(self.agregar)
        
    def agregar(self):
        nombre = self.ui.txt_nombre.text().upper().strip()
        with Conexion_base_datos() as db:
            session = db.abrir_sesion()
            with session.begin():
                dato, estatus = ProductosModel(session).agregar_presentacion(nombre=nombre)
            if estatus:
                Mensaje().mensaje_informativo("Presentación agregada con exito")
                self.SYGNAL_PRESENTACION_AGREGADA.emit()
                self.close()
                return
            Mensaje().mensaje_alerta("No se logro agregar la presentación")
