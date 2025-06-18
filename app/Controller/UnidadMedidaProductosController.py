from PySide6 import QtCore, QtWidgets
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from .MensajesAlertasController import Mensaje
from ..View.UserInterfacePy.UI_AGREGAR_UN_DATO import Ui_Formulario
from ..Model.ProductosModel import ProductosModel
from ..DataBase.conexionBD import Conexion_base_datos

class UnidadMedidaProductos(QWidget):
    SYGNAL_UNIDAD_MEDIDA_AGREGADA = Signal()
    def __init__(self):
        super().__init__()
        self.ui = Ui_Formulario()
        self.ui.setupUi(self)
        self.setWindowTitle("Unidad de Medida")
        self.ui.btn_btn_guardar.clicked.connect(self.agregar)
        
    def agregar(self):
        nombre = self.ui.txt_nombre.text().upper().strip()
        with Conexion_base_datos() as db:
            session = db.abrir_sesion()
            with session.begin():
                dato, estatus = ProductosModel(session).agregar_unidad_medida(nombre=nombre)
            if estatus:
                Mensaje().mensaje_informativo("Unidad de medida agregada con exito")
                self.SYGNAL_UNIDAD_MEDIDA_AGREGADA.emit()
                self.close()
                return
            Mensaje().mensaje_alerta("No se logro agregar la Unidad de medida")
            
