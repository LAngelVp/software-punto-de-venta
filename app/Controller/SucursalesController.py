from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from ..DataBase.conexionBD import *
from ..View.UserInterfacePy.UI_CONTROL_SUCURSALES import *
from .MensajesAlertasController import *
from ..Model.SucursalesModel import SucursalesModel

class SucursalesController(QWidget):
    signal_sucursal_agregada = pyqtSignal()
    def __init__(self):
        super().__init__()
        self.ui = Ui_Nueva_sucursal()
        self.ui.setupUi(self)
        self.ui.btn_btn_agregar.clicked.connect(self.agregar)
        self.listar_sucursales()

    def agregar(self):
        diccionario_campos = [
            self.ui.txt_nombre.text().strip(),
            self.ui.txt_codigopostal.text().strip(),
            self.ui.txt_ciudad.text().strip(),
            self.ui.txt_estado.text().strip(),
            self.ui.txt_pais.text().strip(),
            self.ui.txt_ntelefono.text().strip(),
            self.ui.txtlargo_direccion.toPlainText().strip()
        ]
        if any(campo == '' for campo in diccionario_campos):
            Mensaje().mensaje_alerta("Todos los campos deben de estar completos.")
        else:
            with Conexion_base_datos() as db:
                session = db.abrir_sesion()
                try:
                    sucursal_id = SucursalesModel(session).agregar_sucursal(
                        nombre_sucursal = self.ui.txt_nombre.text().strip(),
                        codigo_postal = self.ui.txt_codigopostal.text().strip(),
                        ciudad = self.ui.txt_ciudad.text().strip(),
                        estado = self.ui.txt_estado.text().strip(),
                        pais = self.ui.txt_pais.text().strip(),
                        num_telefono = self.ui.txt_ntelefono.text().strip(),
                        direccion = self.ui.txtlargo_direccion.toPlainText().strip()
                    )
                    session.commit()
                    self.signal_sucursal_agregada.emit()
                except Exception as e:
                    session.rollback()
                        
    def listar_sucursales(self):
        sucursales = None
        try:
            with Conexion_base_datos() as db:
                session = db.abrir_sesion()
                try:
                    sucursales = SucursalesModel(session).obtener_todo()

                except Exception as e:
                    Mensaje().mensaje_alerta("Error al obtener sucursales")
            if sucursales:
                for  sucursal in sucursales:
                    self.ui.lista_sucursales.addItem(sucursal.nombre_sucursal)
        except Exception as e:
            print(f'Error al listar las sucursales : {e}')

            
