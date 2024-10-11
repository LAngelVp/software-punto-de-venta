from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from ..View.UserInterfacePy.UI_CONTROL_PRODUCTOS import *

class Productos(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Control_Productos()
        self.ui.setupUi(self)