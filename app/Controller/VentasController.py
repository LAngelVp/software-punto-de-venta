from PySide6 import QtCore, QtWidgets
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from ..View.UserInterfacePy.UI_CONTROL_VENTAS import *

class Ventas(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Control_Ventas()
        self.ui.setupUi(self)