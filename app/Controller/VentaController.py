from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from ..View.UserInterfacePy.UI_CONTROL_VENTA import *

class Venta(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Venta()
        self.ui.setupUi(self)