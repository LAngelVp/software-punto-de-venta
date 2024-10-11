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
from app.Model.ValidacionesModel import Validaciones
from app.Model.EmpleadoModel import EmpleadosModel
from ..Model.RolesyPermisosModel import RolesModel, PermisosModel
from ..Model.UsuarioModel import UsuarioModel
from app.Model.PuestoModel import PuestoModel
from app.Model.DepartamentosModel import DepartamentosModel
from app.Model.SucursalesModel import SucursalesModel
from app.Controller.SucursalesController import SucursalesController



class Registro_personal_inicial(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_RegistroAdministrador()
        self.ui.setupUi(self)
        pantalla = self.frameGeometry()
        pantalla.moveCenter(self.screen().availableGeometry().center())
        self.move(pantalla.topLeft())
        self.drag_start_position = None
        # QUITAR EL FONDO Y BARRA DE ESTADO
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
        self.puesto_inicial = "ADMINISTRADOR"
        self.permiso_administrador = "ADMINISTRADOR"
        self.departamento_administrador = "ADMINISTRADOR"
        self.ui.label_fotousuario.mousePressEvent = self.cargar_imagen
        self.ui.btc_cerrar.clicked.connect(self.cerrar)
        self.ui.btc_minimizar.clicked.connect(self.minimizar)
        self.ui.btc_maximizar.clicked.connect(self.maximizar)
        self.ui.Button_nuevasucursal.clicked.connect(self.agregar_sucursal)
        self.ui.Button_aceptar.clicked.connect(self.almacenar_informacion)
        self.ui.Button_cancelar.clicked.connect(self.cancelar)
        # QUITAR LOS BOTONES DE LAS CASILLAS NUMERICAS
        self.ui.decimal_horas_laboralestotales.setButtonSymbols(QSpinBox.NoButtons)
        self.ui.decimal_salario.setButtonSymbols(QSpinBox.NoButtons)
        self.ui.tiempo_horaentrada.setButtonSymbols(QSpinBox.NoButtons)
        self.ui.tiempo_horasalida.setButtonSymbols(QSpinBox.NoButtons)
        
        

        self.ui.cajaopciones_estadocvil.addItems(['Soltero/a','Casado/a','Viudo/a','Divorciado/a','Union libre'])
        

        self.opciones_roles()

        self.dias_laborales = []
        self.ui.opcion_domingo.stateChanged.connect(self.checkbox_checked)
        self.ui.opcion_lunes.stateChanged.connect(self.checkbox_checked)
        self.ui.opcion_martes.stateChanged.connect(self.checkbox_checked)
        self.ui.opcion_miercoles.stateChanged.connect(self.checkbox_checked)
        self.ui.opcion_jueves.stateChanged.connect(self.checkbox_checked)
        self.ui.opcion_viernes.stateChanged.connect(self.checkbox_checked)
        self.ui.opcion_sabado.stateChanged.connect(self.checkbox_checked)
        self.file_name = ''

        self.ingresar_validaciones()
        self.listar_sucursales()

    # EVENTOS DEL MOUSE
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

    def cargar_imagen(self, event):
        options = QFileDialog.Options()
        self.file_name, _ = QFileDialog.getOpenFileName(self, 'SELECCIONA UNA IMAGEN', ' ', 'Archivo de Imagen (*.png *.jpg *.jpeg);; Todos los archivos (*)', options=options)
        if self.file_name:
            self.ui.label_fotousuario.setText(self.file_name)
            pixmap = QPixmap(self.file_name)
            self.ui.label_fotousuario.setPixmap(pixmap)
            self.ui.label_fotousuario.setScaledContents(True)
            self.ui.label_fotousuario.adjustSize()

    def opciones_roles(self):
        conexion = Conexion_base_datos()
        with conexion as db:
            session = db.abrir_sesion()
            roles = RolesModel(session).obtener_todos()
            departamentos = DepartamentosModel(session).obtener_todos()
            if  roles and  departamentos:
                if roles is not None:
                    self.ui.cajaopciones_rol_usuario.clear()
                    self.ui.cajaopciones_departamentos.clear()
                    nombres_roles = [rol.nombre for rol in roles]
                    self.ui.cajaopciones_rol_usuario.addItems(nombres_roles)
                    nombre_departamentos = [departamento.nombre for departamento in departamentos]
                    self.ui.cajaopciones_rol_usuario.addItems(nombre_departamentos)
                else:
                    pass
            else:
                pass
                self.ui.cajaopciones_rol_usuario.addItem(self.puesto_inicial)
                self.ui.cajaopciones_puestos.addItem(self.puesto_inicial)
                self.ui.cajaopciones_departamentos.addItem(self.departamento_administrador)
        
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

    def obtener_datos(self):
        return {
            "nombre": self.ui.txt_nombre.text().strip().upper(),
            "apellido_paterno": self.ui.txt_apellidop.text().strip().upper(),
            "apellido_materno": self.ui.txt_apellidom.text().strip().upper(),
            "fecha_nacimiento": self.ui.fecha_fechanacimiento.date().toString('yyyy/MM/dd'),
            "estado_civil": self.ui.cajaopciones_estadocvil.currentText().strip().upper(),
            "curp": self.ui.txt_curp.text().strip().upper(),
            "rfc": self.ui.txt_rfc.text().strip().upper(),
            "correo": self.ui.txt_correoelectronico.text().strip().upper(),
            "nss": self.ui.txt_numerosegurosicial.text().strip().upper(),
            "avenidas": self.ui.txt_avenidas.text().strip().upper(),
            "calles": self.ui.txt_calles.text().strip().upper(),
            "num_interior": self.ui.txt_ninterior.text().strip().upper(),
            "num_exterior": self.ui.txt_nexterior.text().strip().upper(),
            "fecha_contratacion": self.ui.fecha_fechacontratacion.date().toString('yyyy/MM/dd'),
            "ciudad": self.ui.txt_ciudad.text().strip().upper(),
            "cp": self.ui.txt_codigopostal.text().strip().upper(),
            "estado": self.ui.txt_estado.text().strip().upper(),
            "pais": self.ui.txt_pais.text().strip().upper(),
            "num_telefono": self.ui.txt_numerotelefono.text().strip().upper(),
            "puesto": self.ui.cajaopciones_puestos.currentText().strip().upper(),
            "departamento": self.ui.cajaopciones_departamentos.currentText().strip().upper(),
            "hora_entrada": self.ui.tiempo_horaentrada.time().toString("HH:mm:ss"),
            "hora_salida": self.ui.tiempo_horasalida.time().toString("HH:mm:ss"),
            "salario": self.ui.decimal_salario.value(),
            "horas_laborales": self.ui.decimal_horas_laboralestotales.value(),
            "descripcion_puesto": self.ui.txtlargo_descripcion_puesto.toPlainText().strip().upper(),
            "direccion_adicional": self.ui.txtlargo_direccion_completa.toPlainText().strip().upper(),
            "usuario": self.ui.txt_usuario_iniciosesion.text().strip().upper(),
            "password_usuario": self.ui.txt_contrasenia_usuario_iniciosesion.text().strip().upper(),
            "rol": self.ui.cajaopciones_rol_usuario.currentText().strip().upper()
        }
    
    def validar_datos(self, datos):
        required_fields = [
            "nombre", "apellido_paterno", "apellido_materno", "curp", "rfc", 
            "correo", "nss", "ciudad", "cp", "estado", "pais", "num_telefono","puesto",
            "descripcion_puesto", "direccion_adicional", "usuario", "password_usuario"
        ]
        for field in required_fields:
            if not datos[field]:
                QMessageBox.critical(self, "Error", f"El campo {field} no puede estar vacío.")
                return False
            
        if datos["salario"] <= 0:
            QMessageBox.critical(self, "Error", "El salario debe ser mayor a 0.")
            return False
        
        if datos["horas_laborales"] <= 0:
            QMessageBox.critical(self, "Error", "Las horas laborales deben ser mayores a 0.")
            return False
        
        return True
    
    def almacenar_informacion(self):
        fecha_actual = datetime.now().date()
        datos = self.obtener_datos()
        self.dias_laborales_str = ', '.join(self.dias_laborales)

        if self.validar_datos(datos):
            conexion = Conexion_base_datos()
            with conexion as db:
                session = db.abrir_sesion()
                try:
                    id_permiso = PermisosModel(session).crear_permiso(
                        nombre = datos["puesto"],
                        descripcion = ''
                        )
                
                    id_rol = RolesModel(session).crear_Rol(
                        nombre = datos["rol"], 
                        descripcion = '',
                        permisos = [id_permiso]
                        )
                    
                    nombre_sucursal = self.ui.cajaopciones_sucursales.currentText()
                    id_sucursal = SucursalesModel(session).obtener_sucursal_id(nombre_sucursal)
                    
                    id_departamento = DepartamentosModel(session).agregar_departamento(
                        nombre = datos['departamento'],
                        descripcion = '',
                        sucursal_id = id_sucursal
                    )

                    id_puesto = PuestoModel(session).crear_puesto(
                        nombre = datos['puesto'],
                        salario = datos['salario'],
                        horas_laborales = datos['horas_laborales'],
                        dias_laborales = self.dias_laborales_str,
                        descripcion_puesto = datos['descripcion_puesto'],
                        departamento_id = id_departamento
                    )

                    id_usuario = UsuarioModel(session).crear_usuario(
                        usuario = datos['usuario'],
                        password = datos['password_usuario'],
                        fecha_creacion = fecha_actual,
                        fecha_actualizacion = fecha_actual,
                        rol_id = id_rol)
                
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
                        puesto_id = id_puesto,
                        usuario_id=id_usuario,
                        departamento_id = id_departamento
                    )
                    session.commit()
                    print("Almacenamiento correcto")
                except Exception as e:
                    session.rollback()
                    print(f"Error al almacenar la información: {e}")
                finally:
                    db.cerrar_sesion()
                    self.close()
                    self.abrir_inicio()
        else:
            print("Datos no válidos. No se almacenará la información.")

    def agregar_sucursal(self):
        self.ui_sucursales = SucursalesController()
        self.ui_sucursales.show()
        self.ui_sucursales.signal_sucursal_agregada.connect(self.listar_sucursales)

    def listar_sucursales(self):
        self.ui.cajaopciones_sucursales.clear()
        sucursales = None
        try:
            with Conexion_base_datos() as db:
                session = db.session
                sucursales = SucursalesModel(session).obtener_todo()
            if sucursales:
                for sucursal in sucursales:
                    self.ui.cajaopciones_sucursales.addItem(sucursal.nombre_sucursal)
        except Exception as e:
            print(f"Error al obtener sucursales: {e}")
    
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

    def cerrar(self):
        self.close()

    def minimizar(self):
        self.showMinimized()

    def maximizar(self):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()

    def cancelar(self):
        self.close()




    


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = Registro_personal_inicial()
    ui.show()
    sys.exit(app.exec())