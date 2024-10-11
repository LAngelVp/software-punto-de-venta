import sys
import os
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from ..View.UserInterfacePy.UI_NUEVA_CATEGORIA import *
from ..DataBase.conexionBD import Conexion_base_datos
from ..Model.CategoriaClienteModel import CategoriaClienteModel
from .MensajesAlertasController import Mensaje

class CategoriaClienteController(QWidget):
    signal_categoria_cliente = pyqtSignal()
    def __init__(self):
        super().__init__()
        self.ui = Ui_Nueva_categoria()
        self.ui.setupUi(self)
        self.ui.btn_btn_guardar.clicked.connect(self.guardar_categoria)

    def guardar_categoria(self):
        nombre = self.ui.txt_nombre.text().upper().strip()
        descripcion = self.ui.txtlargo_descripcion.toPlainText().upper().strip()
        if not nombre and not descripcion:
            Mensaje().mensaje_informativo('Todos los campos deben de estar completos.')
            return
        try:
            with Conexion_base_datos() as db:
                session =  db.abrir_sesion()
                categoria = CategoriaClienteModel(session).agregar(nombre=nombre, descripcion=descripcion)
                session.commit()
                self.signal_categoria_cliente.emit()
                Mensaje().mensaje_alerta(f'Area de negocio agregada con exito. {categoria}')
                self.close()
        except Exception as e:
            print(f'error {e}')
