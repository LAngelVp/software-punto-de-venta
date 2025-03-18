import sys
from sqlalchemy import MetaData, Table, select, func
from ..DataBase.conexionBD import Conexion_base_datos
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from ..View.UserInterfacePy.UI_INICIO_SESION import *
from ..Source.iconos_rc import *
from ..Source.ibootstrap_rc import *
from .CreadencialesUsuarioController import *
from ..Model.ValidacionesModel import Validaciones

class Login(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Inicio_Sesion()
        self.ui.setupUi(self)


        self.ui.imgFacebook.mousePressEvent = self.facebook()
        self.ui.imgLinkedin.mousePressEvent = self.linkedin()
        self.ui.imgWhatsapp.mousePressEvent = self.whatsapp()

        self.ui.labelNombreEmpresa.mouseDoubleClickEvent = self.empresa()

        self.setWindowFlags(self.windowFlags() | Qt.WindowType.FramelessWindowHint) 
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        self.ui.principal.setGraphicsEffect(QGraphicsDropShadowEffect(blurRadius=35, xOffset=10, yOffset=0))
        self.ui.btnAceptar.setGraphicsEffect(QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        
        pantalla = self.frameGeometry()
        pantalla.moveCenter(self.screen().availableGeometry().center())
        self.move(pantalla.topLeft())
        
        self.ui.txt_User.setValidator(Validaciones().get_text_validator)
        self.ui.txt_Password.setValidator(Validaciones().get_password_validator)
        
        self.ui.txt_User.setFocus()

        self.ui.btnCerrar.clicked.connect(self.cerrar)
        self.ui.btnMinimizar.clicked.connect(self.minimizar)
        self.ui.btnAceptar.clicked.connect(self.ingresar)
        self.ui.txt_Password.returnPressed.connect(self.ingresar)

    def ingresar(self):
        from .SistemaPrincipalController import SistemaPrincipal
        usuario = self.ui.txt_User.text().strip()
        password = self.ui.txt_Password.text().strip()
        if CredencialesModel().verificar_credenciales(usuario = usuario, contraseña = password):
            ventana =  SistemaPrincipal()
            self.close()
            ventana.show()
        else:
            Mensaje().mensaje_alerta("Las credenciales que estas ingresando son incorrectas, !vuelvelo a intentar¡")

    def facebook(self):
        pass
    
    def linkedin(self):
        pass
    
    def whatsapp(self):
        pass

    def empresa(self):
        pass

    def cerrar(self):
        sys.exit()

    def minimizar(self):
        self.showMinimized()
