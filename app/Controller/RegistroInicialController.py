import os
import sys
from datetime import datetime
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QRegExpValidator
from ..Source.iconos_rc import *
# from .Source.img import *
from ..Source.ibootstrap_rc import *
from ..DataBase.conexionBD import Conexion_base_datos
from ..View.UserInterfacePy.UI_REGISTRO_EMPLEADO import *
from .MensajesAlertasController import Mensaje
from ..Model.ValidacionesModel import Validaciones
from ..Model.EmpleadoModel import EmpleadosModel
from ..Model.GruposyPermisosModel import RolesModel, PermisosModel
from ..Model.UsuarioModel import UsuarioModel
from ..Model.PuestoModel import PuestoModel
from ..Model.DepartamentosModel import DepartamentosModel
from ..Model.SucursalesModel import SucursalesModel
from .AjustarCajaOpcionesGlobal import AjustarCajaOpciones

from .SucursalesController import SucursalesController
from .DepartamentosController import DepartamentosController
from .PuestosController import PuestosController

import traceback



class Registro_personal_inicial(QWidget):
    listar_sucursales_signal = pyqtSignal()
    listar_departamentos_signal = pyqtSignal()
    listar_puestos_signal = pyqtSignal()
    listar_depas_en_puestos_signal = pyqtSignal()
    listar_sucursales_en_departamentos_signal = pyqtSignal()
    tabla_puestos = pyqtSignal()
    registro_agregado_signal = pyqtSignal()
    def __init__(self, id_empleado = None):
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
        
        self.ui.contenedor_credencialesusuario.hide()
        self.ui.btn_btn_bajapersona.hide()
        self.ui.btn_btn_recontratar.hide()
        self.ui.etiqueta_status_empleado.hide()
        self.ui.etiqueta_fechadespido.hide()
        self.ui.fecha_fechadespido.hide()
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
        self.ui.opcion_usodelsistema.toggled.connect(self.mostrar_agregar_credenciales)
        self.ui.btn_btn_bajapersona.clicked.connect(self.baja_empleado)
        self.ui.btn_btn_recontratar.clicked.connect(self.alta_empleado)
#// agregar elementos:
        self.estados_civiles = ['SOLTERO/A','CASADO/A','VIUDO/A','DIVORCIADO/A','UNION LIBRE']
        self.niveles_academicos = ['PRIMARIA', 'SECUNDARIA', 'BACHILLERATO', 'LICENCIATURA', 'CARRERA TRUNCA', 'MAESTRIA', 'DOCTORADO']
        self.parentesco_contacto = ['BISABUELO/A', 'ABUELO/A', 'MADRE', 'PADRE', 'TIO/A', 'ESPOSO/A', 'NIETO/A', 'HIJO/A', 'HERMANO/A', 'SOBRINO/A', 'PRIMO/A', 'CUÑADO/A' 'SUEGRO/A', 'YERNO', 'NUERA', 'OTRO']
        
        self.ui.cajaopciones_nivelacademico.addItems(self.niveles_academicos)
        self.ui.cajaopciones_estadocvil.addItems(self.estados_civiles)
        self.ui.cajaopciones_parentesco.addItems(self.parentesco_contacto)
        
#// variables globales:
        self.drag_start_position = None
        self.file_name = '' # ALMACENAMOS LA FOTO
        self.departamentos = DepartamentosController()
        self.puestos = PuestosController()
        self.sucursales = SucursalesController()
        self.id_empleado = None
        self.lista_puestos = []
        self.variable_primer_registro = False
        
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
        
        if id_empleado is not None:
            self.cargar_datos_empleado()
        

# FUNCIONES GENERALES:
    #// VENTANA DE SUCURSAL:
    def alta_empleado(self):
        fecha_actual = datetime.now().date().strftime("%Y/%m/%d")
        if self.id_empleado is None:
            Mensaje().mensaje_informativo("No se logro dar de baja al empleado")
            return
        with Conexion_base_datos() as db:
            session = db.abrir_sesion()
            with session.begin():
                empleado, estatus = EmpleadosModel(session).alta_empleado(self.id_empleado, True, fecha_actual)
                if estatus:
                    Mensaje().mensaje_informativo("Empleado dado de alta con exito")
                    self.cerrar()
            self.registro_agregado_signal.emit()
            return
        Mensaje().mensaje_informativo("Existio un error al dar de alta al empleado.")
    
    def baja_empleado(self):
        fecha_actual = datetime.now().date().strftime("%Y/%m/%d")
        print(fecha_actual, self.id_empleado)
        if self.id_empleado is None:
            Mensaje().mensaje_informativo("No se logro dar de baja al empleado")
            return
        with Conexion_base_datos() as db:
            session = db.abrir_sesion()
            with session.begin():
                try:
                    empleado, estatus = EmpleadosModel(session).baja_empleado(self.id_empleado, False, fecha_actual)
                    if estatus:
                        Mensaje().mensaje_informativo("Empleado dado de baja con exito")
                        self.cerrar()
                except Exception as e:
                    print(e)
            self.registro_agregado_signal.emit()
            return
        Mensaje().mensaje_informativo("Existio un error al dar de baja al empleado.")
    
    def mostrar_agregar_credenciales(self):
        if self.ui.opcion_usodelsistema.isChecked():
            self.ui.contenedor_credencialesusuario.show()
        else:
            self.ui.contenedor_credencialesusuario.hide()
            
    def obtener_id(self, id_empleado = None):
        if id_empleado is not None:
            self.id_empleado = id_empleado
            self.ui.btn_btn_bajapersona.show()
            self.ui.btn_btn_recontratar.show()
            self.cargar_datos_empleado(self.id_empleado)

    def cargar_datos_empleado(self, id = None):
        opciones_estado_civil = self.estados_civiles
        opciones_niveles_academicos = self.niveles_academicos
        opciones_parentesco = self.parentesco_contacto
        if id is not None:
            with Conexion_base_datos() as db:
                session = db.abrir_sesion()
                with session.begin():
                    empleado_existente, estado = EmpleadosModel(session).obtener_empleado_por_id(id=id)
                if estado:
                    self.ui.txt_nombre.setText(empleado_existente.nombre)
                    self.ui.txt_apellidop.setText(empleado_existente.apellido_paterno)
                    self.ui.txt_apellidom.setText(empleado_existente.apellido_materno)
                    self.ui.fecha_fechanacimiento.setDate(empleado_existente.fecha_nacimiento)
                    self.ui.txt_curp.setText(empleado_existente.curp)
                    self.ui.txt_rfc.setText(empleado_existente.rfc)
                    self.ui.txt_carrera.setText(empleado_existente.carrera)
                    self.ui.txt_correoelectronico.setText(empleado_existente.correo_electronico)
                    self.ui.txt_numerosegurosicial.setText(empleado_existente.numero_seguro_social)
                    self.ui.fecha_fechacontratacion.setDate(empleado_existente.fecha_contratacion)
                    
                    self.ui.txt_ciudad.setText(empleado_existente.ciudad)
                    self.ui.txt_codigopostal.setText(empleado_existente.codigo_postal)
                    self.ui.txt_estado.setText(empleado_existente.estado)
                    self.ui.txt_pais.setText(empleado_existente.pais)
                    self.ui.txt_numerotelefono.setText(empleado_existente.numero_telefonico)
                    self.ui.txt_nombrecontactoemergencia.setText(empleado_existente.nombre_contacto)
                    self.ui.txt_contactoemergencia.setText(empleado_existente.contacto_emergencia)
                    self.ui.txt_calles.setText(empleado_existente.calles)
                    self.ui.txt_avenidas.setText(empleado_existente.avenidas)
                    self.ui.txt_colonia.setText(empleado_existente.colonia)
                    self.ui.txt_ninterior.setText(empleado_existente.num_interior)
                    self.ui.txt_nexterior.setText(empleado_existente.num_exterior)
                    self.ui.txtlargo_direccion_completa.setPlainText(empleado_existente.direccion_adicional)
                    self.ui.label_fotousuario.setPixmap(QPixmap(empleado_existente.foto).scaled(self.ui.label_fotousuario.size()))
                    self.file_name = empleado_existente.foto

                    if empleado_existente.puesto:
                        nombre = empleado_existente.puesto.nombre
                        self.caja_opciones_mover_elemento(self.ui.cajaopciones_puestos, nombre)
                            
                    if empleado_existente.parentesco_contacto:
                        nombre = empleado_existente.parentesco_contacto
                        self.caja_opciones_mover_elemento(self.ui.cajaopciones_parentesco, nombre)
                    
                    if empleado_existente.nivel_academico:
                        nombre = empleado_existente.nivel_academico
                        self.caja_opciones_mover_elemento(self.ui.cajaopciones_nivelacademico, nombre)
                    
                    if empleado_existente.estado_civil:
                        nombre = empleado_existente.estado_civil
                        self.caja_opciones_mover_elemento(self.ui.cajaopciones_estadocvil, nombre)
                    
                    self.mostrar_estatus_empleado(empleado_existente.activo)
                    
    def mostrar_estatus_empleado(self, estatus):
        if estatus:
            # Si estatus es verdadero, mostrar el QLabel y aplicar un estilo indicativo de "activo".
            self.ui.etiqueta_status_empleado.show()
            self.ui.etiqueta_status_empleado.setText("Estado: Activo")  # Puedes poner un texto visible
            self.ui.etiqueta_status_empleado.setStyleSheet("""
                background: #68a67d;  /* Verde para activo */
                color: white;
            """)
            self.ui.fecha_fechadespido.hide()
            self.ui.etiqueta_fechadespido.hide()
        else:
        # Si estatus es falso, cambiar el estilo y mostrar el QLabel (si es necesario).
            self.ui.etiqueta_status_empleado.show()
            self.ui.etiqueta_status_empleado.setText("Estado: Inactivo")  # Texto visible
            self.ui.etiqueta_status_empleado.setStyleSheet("""
                background: #EE1D52;  /* Rojo para inactivo */
                color: white;
            """)
            self.ui.fecha_fechadespido.show()
            self.ui.etiqueta_fechadespido.show()
            self.ui.fecha_fechadespido.setEnabled(False)
    
    def caja_opciones_mover_elemento(self, caja_opciones, elemento_a_mover):
        puestos = []
        max_elementos = caja_opciones.count()
        for i in range(max_elementos):
            nombre_puesto = caja_opciones.itemText(i)
            id_puesto = caja_opciones.itemData(i)
            puestos.append((nombre_puesto, id_puesto))
            
        puesto_encontrado = False
        for i, (nombre, id_puesto) in enumerate(puestos):
            if nombre == elemento_a_mover:
                puestos.pop(i)
                puestos.insert(0, (nombre, id_puesto))
                puesnto_encontrado = True
                break
        if puesnto_encontrado:
            caja_opciones.clear()
            for nombre, id_puesto in puestos:
                caja_opciones.addItem(nombre, id_puesto)

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
            print(f"Error al obtener grupos permisos roles: {e}")

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
            print(f"Error al obtener departamentos: {e}")

    def listar_puestos(self):
        self.ui.cajaopciones_puestos.clear()
        puestos = None
        try:
            with Conexion_base_datos() as db:
                session = db.session
                with session.begin():
                    puestos, estado = PuestoModel(session).obtener_todos()
                if estado:
                    for puesto in puestos:
                        self.ui.cajaopciones_puestos.addItem(puesto.nombre,  puesto.id)
                    AjustarCajaOpciones().ajustar_cajadeopciones(self.ui.cajaopciones_puestos)

        except Exception as e:
            print(f"Error al obtener puestos: {e}")

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
            "nivel_estudios": self.ui.cajaopciones_nivelacademico,
            "carrera": self.ui.txt_carrera,
            "correo": self.ui.txt_correoelectronico,
            "nss": self.ui.txt_numerosegurosicial,
            "fecha_contratacion": self.ui.fecha_fechacontratacion,
            "ciudad": self.ui.txt_ciudad,
            "cp": self.ui.txt_codigopostal,
            "estado": self.ui.txt_estado,
            "pais": self.ui.txt_pais,
            "num_telefono": self.ui.txt_numerotelefono,
            "contacto_emergencia": self.ui.txt_contactoemergencia,
            "parentesco_contacto_emergencia": self.ui.cajaopciones_parentesco,
            "nombre_contacto_emergencia": self.ui.txt_nombrecontactoemergencia,
            "calles": self.ui.txt_calles,
            "avenidas": self.ui.txt_avenidas,
            "colonia" : self.ui.txt_colonia,
            "num_interior": self.ui.txt_ninterior,
            "num_exterior": self.ui.txt_nexterior,
            "direccion_adicional": self.ui.txtlargo_direccion_completa,
            "sucursal": self.ui.cajaopciones_sucursales,
            "puesto": self.ui.cajaopciones_puestos,
            "departamento": self.ui.cajaopciones_departamentos,
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
                            id_empleado = self.id_empleado if self.id_empleado is not None else None,
                            nombre=datos['nombre'],
                            apellido_paterno=datos['apellido_paterno'],
                            apellido_materno=datos['apellido_materno'],
                            fecha_nacimiento=datos['fecha_nacimiento'],
                            estado_civil=self.ui.cajaopciones_estadocvil.currentText().strip().upper(),
                            curp=datos['curp'],
                            rfc=datos['rfc'],
                            nivel_academico=self.ui.cajaopciones_nivelacademico.currentText().strip().upper(),
                            carrera=datos["carrera"],
                            correo_electronico=datos["correo"],
                            numero_seguro_social=datos["nss"],
                            fecha_contratacion=datos["fecha_contratacion"],
                            fecha_despido=None,
                            ciudad=datos["ciudad"],
                            codigo_postal=datos["cp"],
                            estado=datos["estado"],
                            pais=datos["pais"],
                            numero_telefonico=datos["num_telefono"],
                            nombre_contacto=datos["nombre_contacto_emergencia"],
                            contacto_emergencia=datos["contacto_emergencia"],
                            parentesco_contacto=self.ui.cajaopciones_parentesco.currentText().strip().upper(),
                            calles=datos["calles"],
                            avenidas=datos["avenidas"],
                            colonia=datos["colonia"],
                            num_interior=datos["num_interior"],
                            num_exterior=datos["num_exterior"],
                            direccion_adicional=datos["direccion_adicional"],
                            activo=True,
                            foto=self.file_name,
                            puesto_id=self.ui.cajaopciones_puestos.currentData(),
                            usuario_id=id_usuario,
                            departamento_id=self.ui.cajaopciones_departamentos.currentData(),
                            sucursal_id=self.ui.cajaopciones_sucursales.currentData()
                        )
                        self.cerrar()
                        self.abrir_inicio()
                    except Exception as e:
                        # Imprimir detalles del error con traceback
                        print(f'Error tipo: {type(e)}')
                        print(f'Error mensaje: {e}')
                        print('Detalles del traceback:')
                        traceback.print_exc()
                        session.rollback()
            self.registro_agregado_signal.emit()
        else:
            print("Datos no válidos. No se almacenará la información.")

    def abrir_inicio(self):
        if self.variable_primer_registro:
            from app.Controller.InicioDeSesionController import Login  # Mover la importación aquí
            self.login_window = Login()  # Crear instancia de Login
            self.login_window.show()
            self.variable_primer_registro = False

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
        self.id_empleado = None
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

