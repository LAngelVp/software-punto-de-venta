import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from app.Source.iconos import *
from app.Source.img import *
from app.Source.iconsdvg_rc import *
from PyQt5.QtWidgets import QApplication, QWidget
from app.View.UserInterfacePy.UI_BIENVENIDA import *
from .RegistroInicialController import Registro_personal_inicial

class Inicio_principal(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Bienvenida()
        self.ui.setupUi(self)
        self.ui.etiqueta_imagen.setStyleSheet('image: url(:/Icons/SVG/DrawKit(17).svg)')
        self.setWindowIcon(QIcon(':/Icons/SVG/DrawKit(17).svg'))
        self.ui.btn_btn_registrar.clicked.connect(self.abrir_registro)
        
    def abrir_registro(self):
        self.registro = Registro_personal_inicial()
        self.registro.show()
        self.close()
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = Inicio_principal()
    ui.show()
    sys.exit(app.exec())