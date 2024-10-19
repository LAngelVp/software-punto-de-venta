import os
import sys
from datetime import datetime
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QRegExpValidator
from app.Source.iconos import *
from app.Source.img import *
from app.Source.ibootstrap import *
from app.DataBase.conexionBD import Conexion_base_datos
from app.View.UserInterfacePy.UI_REGISTRO_EMPLEADO import *
from app.Controller.MensajesAlertasController import Mensaje
from app.Model.ValidacionesModel import Validaciones
from app.Model.EmpleadoModel import EmpleadosModel
from app.Model.GruposyPermisosModel import RolesModel, PermisosModel
from app.Model.UsuarioModel import UsuarioModel
from app.Model.PuestoModel import PuestoModel
from app.Model.DepartamentosModel import DepartamentosModel
from app.Model.SucursalesModel import SucursalesModel
from app.Controller.AjustarCajaOpcionesGlobal import AjustarCajaOpciones

from app.Controller.SucursalesController import SucursalesController
from app.Controller.DepartamentosController import DepartamentosController
from app.Controller.PuestosController import PuestosController



class Registro_personal_inicial(QWidget):
    listar_sucursales_signal = pyqtSignal()
    listar_departamentos_signal = pyqtSignal()
    listar_puestos_signal = pyqtSignal()
    listar_depas_en_puestos_signal = pyqtSignal()
    listar_sucursales_en_departamentos_signal = pyqtSignal()
    tabla_puestos = pyqtSignal()
    def __init__(self):
        super().__init__()
        self.ui = Ui_RegistroAdministrador()
        self.ui.setupUi(self)

        #// edicion de la ventana:
        self.setWindowFlags(self.windowFlags() | Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.ui.label_fotousuario.setText("Agregar Imagen")
        self.ui.label_fotousuario.setStyleSheet('''
            QLabel {
                qproperty-alignment: AlignCenter;
                font-size:15px;
                font-weight:bold;
            }
            
        ''')
        self.ui.contenedor_baja.setVisible(False)
        self.ui.decimal_horas_laboralestotales.setButtonSymbols(QSpinBox.NoButtons)
        self.ui.decimal_salario.setButtonSymbols(QSpinBox.NoButtons)
        self.ui.tiempo_horaentrada.setButtonSymbols(QSpinBox.NoButtons)
        self.ui.tiempo_horasalida.setButtonSymbols(QSpinBox.NoButtons)
        self.ui.numero_antiguedadyear.setButtonSymbols(QSpinBox.NoButtons)
        self.ui.numero_antiguedadmes.setButtonSymbols(QSpinBox.NoButtons)
        self.ui.numero_antiguedaddias.setButtonSymbols(QSpinBox.NoButtons)
#// mostrar ventana en el centro de la pantalla:
        pantalla = self.frameGeometry()
        pantalla.moveCenter(self.screen().availableGeometry().center())
        self.move(pantalla.topLeft())
# señales: acciones de los botones
        self.ui.btc_cerrar.clicked.connect(lambda: self.close())
        self.ui.btc_minimizar.clicked.connect(lambda: self.showMinimized())
        self.ui.Button_cancelar.clicked.connect(lambda: self.close())
        self.ui.label_fotousuario.mousePressEvent = self.cargar_imagen
        self.ui.btc_maximizar.clicked.connect(self.maximizar)
        self.ui.Button_nuevasucursal.clicked.connect(self.agregar_sucursal)
        self.ui.Button_aceptar.clicked.connect(self.almacenar_informacion)
        self.ui.Button_agregardepartamento.clicked.connect(self.ventana_departamentos)
        self.ui.Button_agregarpuesto.clicked.connect(self.ventana_puestos)
#señales de las casillas de verificacion:
        self.ui.opcion_domingo.stateChanged.connect(self.checkbox_checked)
        self.ui.opcion_lunes.stateChanged.connect(self.checkbox_checked)
        self.ui.opcion_martes.stateChanged.connect(self.checkbox_checked)
        self.ui.opcion_miercoles.stateChanged.connect(self.checkbox_checked)
        self.ui.opcion_jueves.stateChanged.connect(self.checkbox_checked)
        self.ui.opcion_viernes.stateChanged.connect(self.checkbox_checked)
        self.ui.opcion_sabado.stateChanged.connect(self.checkbox_checked)
#// agregar elementos:
        self.ui.cajaopciones_estadocvil.addItems(['Soltero/a','Casado/a','Viudo/a','Divorciado/a','Union libre'])
#// variables globales:
        self.drag_start_position = None
        self.dias_laborales = []
        self.file_name = '' # ALMACENAMOS LA FOTO
        self.departamentos = DepartamentosController()
        self.puestos = PuestosController()
        self.sucursales = SucursalesController()
        
#funciones principales:
        self.listar_grupo_permisos_rol()
        self.ingresar_validaciones()
        self.listar_departamentos()
        self.listar_puestos()
        self.listar_sucursales()
        self.listar_sucursales()

# señales y slots:
        self.listar_sucursales_signal.connect(self.sucursales.obtener_sucursales)
        self.listar_departamentos_signal.connect(self.departamentos.obtener_departamentos)
        self.listar_puestos_signal.connect(self.puestos.listar_puestos)
        self.listar_depas_en_puestos_signal.connect(self.puestos.listar_departamentos)
        self.listar_sucursales_en_departamentos_signal.connect(self.departamentos.listar_sucursales_existentes)
        

# FUNCIONES GENERALES:
    #// VENTANA DE SUCURSAL:
    def agregar_sucursal(self):
        self.sucursales.signal_sucursal_agregada.connect(self.listar_sucursales)
        self.listar_sucursales_signal.emit()
        self.sucursales.show()

    def ventana_departamentos(self):
        self.departamentos.signal_departamento_agregado.connect(self.listar_departamentos)
        self.listar_sucursales_en_departamentos_signal.emit()
        self.listar_departamentos_signal.emit()
        self.departamentos.show()
    
    def ventana_puestos(self):
        self.puestos.signal_puesto_agregado.connect(self.listar_puestos)
        self.listar_depas_en_puestos_signal.emit()
        self.listar_puestos_signal.emit()
        self.puestos.show()

    def listar_sucursales(self):
        self.ui.cajaopciones_sucursales.clear()
        sucursales = None
        try:
            with Conexion_base_datos() as db:
                session = db.session
                sucursales = SucursalesModel(session).obtener_todo()
            if sucursales:
                for sucursal in sucursales:
                    self.ui.cajaopciones_sucursales.addItem(sucursal.nombre_sucursal, sucursal.id)
                AjustarCajaOpciones().ajustar_cajadeopciones(self.ui.cajaopciones_sucursales)
        except Exception as e:
            print(f"Error al obtener sucursales: {e}")

    def listar_grupo_permisos_rol(self):
        self.ui.cajaopciones_rol_usuario.clear()
        grupo_permiso = None
        try:
            with Conexion_base_datos() as db:
                session = db.session
                grupo_permiso, estado = RolesModel(session).obtener_todos()
            if estado:
                for grupo in grupo_permiso:
                    self.ui.cajaopciones_rol_usuario.addItem(grupo.nombre, grupo.id)
                AjustarCajaOpciones().ajustar_cajadeopciones(self.ui.cajaopciones_rol_usuario)
        except Exception as e:
            print(f"Error al obtener sucursales: {e}")

    def listar_departamentos(self):
        self.ui.cajaopciones_departamentos.clear()
        departamentos = None
        try:
            with Conexion_base_datos() as db:
                session = db.session
                departamentos, estado = DepartamentosModel(session).obtener_todos()
            if departamentos:
                for departamento in departamentos:
                    self.ui.cajaopciones_departamentos.addItem(departamento.nombre, departamento.id)
                AjustarCajaOpciones().ajustar_cajadeopciones(self.ui.cajaopciones_departamentos)
        except Exception as e:
            print(f"Error al obtener sucursales: {e}")

    def listar_puestos(self):
        self.ui.cajaopciones_puestos.clear()
        puestos = None
        try:
            with Conexion_base_datos() as db:
                session = db.session
                puestos, estado = PuestoModel(session).obtener_todos()
            if puestos:
                for puesto in puestos:
                    self.ui.cajaopciones_puestos.addItem(puesto.nombre,  puesto.id)

                AjustarCajaOpciones().ajustar_cajadeopciones(self.ui.cajaopciones_puestos)
        except Exception as e:
            print(f"Error al obtener sucursales: {e}")

    def cargar_imagen(self, event):
        options = QFileDialog.Options()
        self.file_name, _ = QFileDialog.getOpenFileName(self, 'SELECCIONA UNA IMAGEN', ' ', 'Archivo de Imagen (*.png *.jpg *.jpeg);; Todos los archivos (*)', options=options)
        if self.file_name:
            self.ui.label_fotousuario.setText(self.file_name)
            pixmap = QPixmap(self.file_name)
            self.ui.label_fotousuario.setPixmap(pixmap)
            self.ui.label_fotousuario.setScaledContents(True)
            self.ui.label_fotousuario.adjustSize()
        
    def ingresar_validaciones(self):
        self.ui.txt_nombre.setValidator(Validaciones().get_text_validator)
        self.ui.txt_apellidop.setValidator(Validaciones().get_text_validator)
        self.ui.txt_apellidom.setValidator(Validaciones().get_text_validator)
        self.ui.txt_curp.setValidator(Validaciones().get_curp_validator)
        self.ui.txt_rfc.setValidator(Validaciones().get_rfc_validator)
        self.ui.txt_correoelectronico.setValidator(Validaciones().get_email_validator)
        self.ui.txt_numerosegurosicial.setValidator(Validaciones().get_nss_validator)
        self.ui.txt_ciudad.setValidator(Validaciones().get_text_validator)
        self.ui.txt_codigopostal.setValidator(Validaciones().get_int_validator)
        self.ui.txt_estado.setValidator(Validaciones().get_text_validator)
        self.ui.txt_pais.setValidator(Validaciones().get_text_validator)
        self.ui.txt_numerotelefono.setValidator(Validaciones().get_phone_validator)
        self.ui.txt_usuario_iniciosesion.setValidator(Validaciones().get_text_validator)
        self.ui.txt_contrasenia_usuario_iniciosesion.setValidator(Validaciones().get_password_validator)

    def campos(self):
        return {
            "nombre": self.ui.txt_nombre,
            "apellido_paterno": self.ui.txt_apellidop,
            "apellido_materno": self.ui.txt_apellidom,
            "fecha_nacimiento": self.ui.fecha_fechanacimiento,
            "estado_civil": self.ui.cajaopciones_estadocvil,
            "curp": self.ui.txt_curp,
            "rfc": self.ui.txt_rfc,
            "correo": self.ui.txt_correoelectronico,
            "nss": self.ui.txt_numerosegurosicial,
            "avenidas": self.ui.txt_avenidas,
            "calles": self.ui.txt_calles,
            "num_interior": self.ui.txt_ninterior,
            "num_exterior": self.ui.txt_nexterior,
            "fecha_contratacion": self.ui.fecha_fechacontratacion,
            "ciudad": self.ui.txt_ciudad,
            "cp": self.ui.txt_codigopostal,
            "estado": self.ui.txt_estado,
            "pais": self.ui.txt_pais,
            "num_telefono": self.ui.txt_numerotelefono,
            "puesto": self.ui.cajaopciones_puestos,
            "departamento": self.ui.cajaopciones_departamentos,
            "hora_entrada": self.ui.tiempo_horaentrada,
            "hora_salida": self.ui.tiempo_horasalida,
            "salario": self.ui.decimal_salario,
            "horas_laborales": self.ui.decimal_horas_laboralestotales,
            "descripcion_puesto": self.ui.txtlargo_descripcion_puesto,
            "direccion_adicional": self.ui.txtlargo_direccion_completa,
            "usuario": self.ui.txt_usuario_iniciosesion,
            "password_usuario": self.ui.txt_contrasenia_usuario_iniciosesion,
            "rol": self.ui.cajaopciones_rol_usuario
        }
    
    def obtener_datos(self):
        datos = {}
        campos = self.campos()
        for nombre, campo in campos.items():
            if isinstance(campo, QLineEdit):
                datos[nombre] = campo.text().strip().upper()
            elif isinstance(campo, QComboBox):
                datos[nombre] = campo.currentText().strip().upper()
            elif isinstance(campo, QDateEdit):
                datos[nombre] = campo.date().toString('yyyy-MM-dd')
            elif isinstance(campo, QTimeEdit):
                datos[nombre] = campo.time().toString('HH:mm')
            elif isinstance(campo, QPlainTextEdit):
                datos[nombre] = campo.toPlainText().strip().upper()
            elif isinstance(campo, (QDoubleSpinBox, QSpinBox)):
                datos[nombre] = campo.value()

        return datos

    def validar_datos(self, datos):
        for nombre, valor in datos.items():
            if not valor:
                QMessageBox.critical(self, "Error", f"El campo {nombre} no puede estar vacío.")
                return False
            if isinstance(valor, (QDoubleSpinBox, QSpinBox)) and valor <= 0:
                QMessageBox.critical(self, "Error", "El salario debe ser mayor a 0.")
                return False
        return True
    
    def almacenar_informacion(self):
        fecha_actual = datetime.now().date() # Obtener la fecha actual, al momento.
        # // obtenemos los datos de los campos
        datos = self.obtener_datos()
        self.dias_laborales_str = ', '.join(self.dias_laborales)

        if self.validar_datos(datos):
            with Conexion_base_datos() as db:
                session = db.abrir_sesion()
                with session.begin():
                    try:
                        id_usuario = UsuarioModel(session).crear_usuario(
                            usuario = datos['usuario'],
                            password = datos['password_usuario'],
                            fecha_creacion = fecha_actual,
                            fecha_actualizacion = fecha_actual,
                            rol_id = self.ui.cajaopciones_rol_usuario.currentData())
                    
                        EmpleadosModel(session).crear_empleado(
                            nombre = datos['nombre'],
                            apellido_paterno = datos['apellido_paterno'],
                            apellido_materno = datos['apellido_materno'],
                            fecha_nacimiento = datos['fecha_nacimiento'],
                            estado_civil = datos['estado_civil'],
                            curp = datos['curp'],
                            rfc = datos['rfc'],
                            correo = datos['correo'],
                            nss = datos['nss'],
                            fecha_contratacion = datos['fecha_contratacion'],
                            ciudad = datos['ciudad'],
                            cp = datos['cp'],
                            estado = datos['estado'],
                            pais = datos['pais'],
                            numero_telefono = datos['num_telefono'],
                            direccion = datos['direccion_adicional'],
                            activo = True,
                            hora_entrada=datos['hora_entrada'],
                            hora_salida=datos['hora_salida'],
                            foto = self.file_name,
                            puesto_id = self.ui.cajaopciones_puestos.currentData(),
                            usuario_id=id_usuario,
                            departamento_id = self.ui.cajaopciones_departamentos.currentData()
                        )
                        self.close()
                        self.abrir_inicio()
                    except Exception as e:
                        print(e)
        else:
            print("Datos no válidos. No se almacenará la información.")

    def abrir_inicio(self):
        from app.Controller.InicioDeSesionController import Login  # Mover la importación aquí
        self.login_window = Login()  # Crear instancia de Login
        self.login_window.show()

    def checkbox_checked(self, state):
        sender = self.sender()
        if state == Qt.Checked:
            if sender.text() not in self.dias_laborales:
                self.dias_laborales.append(sender.text())
        else:
            if sender.text() in self.dias_laborales:
                self.dias_laborales.remove(sender.text())

    
#// funcionalidades de la ventana
    def cerrar(self):
        self.close()

    def maximizar(self):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()

#//movimiento de la ventana con el mause:
    def mousePressEvent(self, event):
        if event.buttons() & Qt.LeftButton:
            self.drag_start_position = event.globalPos() - self.pos()

    def mouseMoveEvent(self, event):
        if event.buttons() & Qt.LeftButton:
            if self.drag_start_position is not None:
                new_pos = event.globalPos() - self.drag_start_position
                self.move(new_pos)

    def mouseReleaseEvent(self, event):
        # Resetea drag_start_position al soltar el botón del mouse
        self.drag_start_position = None

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ui = Registro_personal_inicial()
#     ui.show()
#     sys.exit(app.exec())