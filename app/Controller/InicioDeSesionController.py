import sys
from datetime import datetime
from ..Source.iconsdvg_rc import *
from sqlalchemy import MetaData, Table, select, func
from ..DataBase.conexionBD import Conexion_base_datos
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from ..View.UserInterfacePy.UI_INICIO_SESION import *
from ..View.UserInterfacePy.UI_VENTANA_SALUDO_INGRESO import Ui_Bienvenida
from .Hilo_consultas import *
from ..Source.iconos_rc import *
from ..Source.ibootstrap_rc import *
from .CreadencialesUsuarioController import *
from .Validaciones import Validaciones

class Login(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.ventana = None
        self.datos_usuario = None
        self.ventana_saludo = None
        self.ui = Ui_Inicio_Sesion()
        self.ui.setupUi(self)


        self.ui.imgFacebook.mousePressEvent = self.facebook()
        self.ui.imgLinkedin.mousePressEvent = self.linkedin()
        self.ui.imgWhatsapp.mousePressEvent = self.whatsapp()

        self.ui.labelNombreEmpresa.mouseDoubleClickEvent = self.empresa()
        self.setWindowIcon(QIcon(":Icons/IconosSVG/logo_devrous.svg"))
        self.setWindowTitle("Inicio de sesión")

        sombra = QGraphicsDropShadowEffect()
        sombra.setBlurRadius(25) 
        sombra.setOffset(0, 0)
        sombra.setColor(QColor(0, 102, 204)) 

        self.ui.contenedor_global.setGraphicsEffect(sombra)
        
        self.setWindowFlags(self.windowFlags() | Qt.WindowType.FramelessWindowHint) 
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        
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

    def mostrar_saludos(self):
        if self.ventana_saludo is None or not self.ventana_saludo.isVisible():
            self.ventana_saludo = SaludoIngreso(usuario=self.datos_usuario)
            # self.ventana_saludo = Ventana_proceso_cargando(parent=None)
            self.ventana_saludo.show()
        else:
            self.ventana_saludo.raise_()
    
    def ingresar(self):
        usuario = self.ui.txt_User.text().strip()
        password = self.ui.txt_Password.text().strip()
        usuario_existente, estatus_consulta = CredencialesModel().verificar_credenciales(usuario = usuario, contraseña = password)
        # usuario_nombre = str(usuario_existente.usuario)
        if estatus_consulta:
            self.datos_usuario =   {
                "id_usuario": usuario_existente.id,
                "nombre_usuario" : usuario_existente.usuario,
                "id_empleado": usuario_existente.empleado.id,
                "nombre_empleado": f'{usuario_existente.empleado.nombre} {usuario_existente.empleado.apellido_paterno} {usuario_existente.empleado.apellido_materno}' 
                }
            self.close()
            self.mostrar_saludos()
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

class SaludoIngreso(QWidget):
    def __init__(self, parent = None, usuario = None):
        super().__init__(parent)
        self.usuario = usuario
        self.ui = Ui_Bienvenida()
        self.ui.setupUi(self)
        pantalla = self.frameGeometry()
        pantalla.moveCenter(self.screen().availableGeometry().center())
        self.move(pantalla.topLeft())
        self.setWindowFlags(self.windowFlags() | Qt.WindowType.FramelessWindowHint) 
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        sombra = QGraphicsDropShadowEffect()
        sombra.setBlurRadius(25) 
        sombra.setOffset(0, 0)
        sombra.setColor(QColor(0, 102, 204)) 

        self.ui.contenedor.setGraphicsEffect(sombra)
        self.ui.btn_entrar.clicked.connect(self.entrar_al_sistema)
        
        self.saludar()
    
    def entrar_al_sistema(self):
        from .SistemaPrincipalController import SistemaPrincipal
        self.ventana =  SistemaPrincipal(parent=None, datos_usuario = self.usuario)
        self.close()
        self.ventana.show()
        
    def saludar(self):
        if self.usuario is None:
            Mensaje().mensaje_informativo("No hay informacion del usuario")
            return
        self.ui.etiquetaNombreUsuario.setText(self.usuario["nombre_empleado"])
        tiempo = self.diferenciar_tiempo_dia()
        self.ui.etiquetaBuendia.setText(f"Excelente {tiempo}")
        
        
    def diferenciar_tiempo_dia(self):
        hora_actual = datetime.now().hour
        saludo = None
        if 6 <= hora_actual < 12:
            saludo = "Mañana"
        elif 12 <= hora_actual < 18:
            saludo = "Tarde"
        else:
            saludo = "Noche"
        return saludo