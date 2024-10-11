import sys
import os
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from ..View.UserInterfacePy.UI_NUEVA_CATEGORIA import *
from ..DataBase.conexionBD import Conexion_base_datos
from ..Model.CategoriasProveedorModel import CategoriaProveedorModel
from .MensajesAlertasController import Mensaje

class CategoriasController(QWidget):
    categoria_agregada_signal =  pyqtSignal()
    def __init__(self):
        super().__init__()

        self.ui = Ui_Nueva_categoria()
        self.ui.setupUi(self)
        self.ui.btn_btn_guardar.clicked.connect(self.guardar)

    def guardar(self):
        categoria = self.ui.txt_nombre.text()
        descripcion = self.ui.txtlargo_descripcion.toPlainText()
        with Conexion_base_datos() as db:
            session = db.abrir_sesion()
            try:
                categoria_bd = CategoriaProveedorModel(session).agregar_categoria(nombre=categoria, descripcion=descripcion)
                session.commit()
                self.categoria_agregada_signal.emit()
            except Exception as e:
                session.rollback()
                print(f'Error al guardar la categoria {e}')
            finally:
                db.cerrar_sesion()
        
        self.close()
            

