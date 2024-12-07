import sys
import os
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from ..View.UserInterfacePy.UI_NUEVA_CATEGORIA import *
from ..DataBase.conexionBD import Conexion_base_datos
from ..Model.CategoriasModel import CategoriasModel
from .MensajesAlertasController import Mensaje


class CategoriasController(QWidget):
    categoria_agregada_signal =  pyqtSignal()
    def __init__(self, tipo_categoria):
        super().__init__()
        self.tipo_categoria = tipo_categoria
        self.ui = Ui_Nueva_categoria()
        self.ui.setupUi(self)
        self.ui.btn_btn_guardar.clicked.connect(self.guardar)

    def guardar(self):
        categoria = self.ui.txt_nombre.text()
        descripcion = self.ui.txtlargo_descripcion.toPlainText()
        with Conexion_base_datos() as db:
            session = db.abrir_sesion()
            with session.begin():
                    categoria_bd, estatus = CategoriasModel(session).agregar(tipo_categoria=self.tipo_categoria, nombre=categoria, descripcion=descripcion)
            if estatus:
                Mensaje().mensaje_informativo("Categoria agregada con exito")
                self.categoria_agregada_signal.emit()
                self.close()
                return
            Mensaje().mensaje_alerta("La categoria no se pudo agregar")
        