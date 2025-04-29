from datetime import datetime
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QRegExpValidator
from ..Source.iconos_rc import *
# from .Source.img import *
from ..Source.ibootstrap_rc import *
from .FuncionesAuxiliares import *
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
from .FuncionesAuxiliares import FuncionesAuxiliaresController

from .ControlSucursalesController import SucursalesController
from .DepartamentosController import DepartamentosController
from .PuestosController import PuestosController

from .Ventana_espera import Modal_de_espera
from .Hilo_consultas import *

import traceback

class Registro_personal_inicial(QDialog):
    listar_sucursales_signal = pyqtSignal()
    listar_departamentos_signal = pyqtSignal()
    listar_puestos_signal = pyqtSignal()
    listar_depas_en_puestos_signal = pyqtSignal()
    listar_sucursales_en_departamentos_signal = pyqtSignal()
    tabla_puestos = pyqtSignal()
    registro_agregado_signal = pyqtSignal()
    VENTANA_REGISTRO_CERRADA = pyqtSignal()
    def __init__(self, parent = None, empleado = None):
        super().__init__(parent)
        # comment: variables globales:
        self.empleado = empleado
        self.estados_civiles = ['SOLTERO/A','CASADO/A','VIUDO/A','DIVORCIADO/A','UNION LIBRE']
        self.niveles_academicos = ['PRIMARIA', 'SECUNDARIA', 'BACHILLERATO', 'LICENCIATURA', 'CARRERA TRUNCA', 'MAESTRIA', 'DOCTORADO']
        self.parentesco_contacto = ['BISABUELO/A', 'ABUELO/A', 'MADRE', 'PADRE', 'TIO/A', 'ESPOSO/A', 'NIETO/A', 'HIJO/A', 'HERMANO/A', 'SOBRINO/A', 'PRIMO/A', 'CUÑADO/A' 'SUEGRO/A', 'YERNO', 'NUERA', 'OTRO']
        self.generos = ["MASCULINO","FEMENINO", "NO BINARIO", "TRANSEXUAL", "INTERGÉNERO", "AGÉNERO", "OTRO"]
        self.drag_start_position = None
        self.file_name = '' # ALMACENAMOS LA FOTO
        self.departamentos = None
        self.puestos = None
        # self.sucursales = SucursalesController()
        self.sucursales = None
        self.lista_puestos = []
        self.variable_primer_registro = False
        self.empleado_existente = None
        self._ventanaCerradaRegistro = False
        self.cargando = None
        self.consultor = None
        
        # comment: inicializacion de la ventana
        self.ui = Ui_RegistroAdministrador()
        self.ui.setupUi(self)

        #// edicion de la ventana:
        self.setWindowTitle("Formulario del perosonal")
        self.setWindowFlags(self.windowFlags() | Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.ui.contenedor_credencialesusuario.hide()
        self.ui.btn_btn_bajapersona.hide()
        self.ui.btn_btn_recontratar.hide()
        self.ui.etiqueta_status_empleado.hide()
        self.ui.etiqueta_fechadespido.hide()
        self.ui.fecha_fechadespido.hide()
        self.ui.opcion_actualizar_datoscredenciales.hide()
        self.ui.Button_actualizarcredenciales.hide()
        self.ui.Button_eliminar_credenciales.hide()
        self.ui.Button_actualizarcredenciales.setEnabled(False)
        self.ui.Button_eliminar_credenciales.setEnabled(False)
        self.ui.fecha_fechacontratacion.setDate(QDate.currentDate())
        self.ui.Button_actualizar.hide()
        self.ui.Button_agregarUsuario.hide()
        self.ui.btc_minimizar.hide()
        self.ui.btc_maximizar.hide()
        self.ui.txt_nombre.setFocus()
#// mostrar ventana en el centro de la pantalla:
        pantalla = self.frameGeometry()
        pantalla.moveCenter(self.screen().availableGeometry().center())
        self.move(pantalla.topLeft())
        
# señales: acciones de los botones
        self.ui.btc_cerrar.clicked.connect(self.close)
        self.ui.Button_cancelar.clicked.connect(self.close)
        self.ui.foto_usuario.mousePressEvent = self.cargar_imagen
        self.ui.btc_maximizar.clicked.connect(self.maximizar)
        self.ui.Button_nuevasucursal.clicked.connect(self.agregar_sucursal)
        self.ui.Button_aceptar.clicked.connect(self.agregar_nuevo_empleado)
        self.ui.Button_agregardepartamento.clicked.connect(self.ventana_departamentos)
        self.ui.Button_agregarpuesto.clicked.connect(self.ventana_puestos)
        self.ui.opcion_usodelsistema.toggled.connect(self.mostrar_agregar_credenciales)
        self.ui.btn_btn_bajapersona.clicked.connect(self.baja_empleado)
        self.ui.btn_btn_recontratar.clicked.connect(self.alta_empleado)
        self.ui.Button_actualizarcredenciales.clicked.connect(self.actualizar_credenciales)
        self.ui.Button_eliminar_credenciales.clicked.connect(self.eliminar_credenciales)
        self.ui.Button_actualizar.clicked.connect(self.actualizar_empleado)
        self.ui.Button_agregarUsuario.clicked.connect(self.agregar_usuario)
#// agregar elementos:
        
        self.ui.cajaopciones_nivelacademico.addItems(self.niveles_academicos)
        AjustarCajaOpciones().ajustar_cajadeopciones(self.ui.cajaopciones_nivelacademico)
        self.ui.cajaopciones_estadocvil.addItems(self.estados_civiles)
        AjustarCajaOpciones().ajustar_cajadeopciones(self.ui.cajaopciones_estadocvil)
        self.ui.cajaopciones_parentesco.addItems(self.parentesco_contacto)
        AjustarCajaOpciones().ajustar_cajadeopciones(self.ui.cajaopciones_parentesco)
        self.ui.cajaopciones_genero.addItems(self.generos)
        AjustarCajaOpciones().ajustar_cajadeopciones(self.ui.cajaopciones_genero)
        
#// variables globales:
        
        
#funciones principales:
        self.ingresar_validaciones()
        self.listar_grupo_permisos_rol()
        self.listar_departamentos()
        self.listar_puestos()
        self.listar_sucursales()
        self.listar_sucursales()

# señales y slots:
        
        if empleado is not None:
            self.cargar_datos_empleado()
    
    def showEvent(self, event):
        super().showEvent(event)
        if not self._ventanaCerradaRegistro:
            FuncionesAuxiliaresController.centrar_en_padre(self)
            self._ventanaCerradaRegistro = True
    
    def closeEvent(self, event):
        self.VENTANA_REGISTRO_CERRADA.emit()
        event.accept()
        
# FUNCIONES GENERALES:
    #// VENTANA DE SUCURSAL:
    def permiso_actualizar_credenciales(self):
        if self.ui.opcion_actualizar_datoscredenciales.isChecked():
            self.ui.txt_usuario_iniciosesion.setEnabled(True)
            self.ui.txt_contrasenia_usuario_iniciosesion.setEnabled(True)
            self.ui.Button_actualizarcredenciales.setEnabled(True)
            self.ui.Button_eliminar_credenciales.setEnabled(True)
        else:
            self.ui.txt_usuario_iniciosesion.setEnabled(False)
            self.ui.txt_contrasenia_usuario_iniciosesion.setEnabled(False)
            self.ui.Button_actualizarcredenciales.setEnabled(False)
            self.ui.Button_eliminar_credenciales.setEnabled(False)
            
    def eliminar_credenciales(self):
        id_empleado = self.id_empleado
        if id_empleado is not None:
            with Conexion_base_datos() as db:
                session = db.abrir_sesion()
                with session.begin():
                    credenciales = EmpleadosModel(session).eliminar_credenciales(id_empleado)
                    if credenciales:
                        Mensaje().mensaje_informativo("Se elimino el usuario del empleado.")
                    else:
                        Mensaje().mensaje_alerta("No se pudo eliminar el usuario del empleado. Por que no tiene uno asignado")
    
    def actualizar_credenciales(self):
        id_empleado = self.id_empleado
        id_usuario = self.empleado_existente.usuario.id
        usuario = self.ui.txt_usuario_iniciosesion.text()
        password = self.ui.txt_contrasenia_usuario_iniciosesion.text()
        fecha_actualizacion = datetime.now().date()
        rol = self.ui.cajaopciones_rol_usuario.currentData()
        if id_empleado is None or (usuario is None and password is None):
            Mensaje().mensaje_informativo("Para actualizar las credenciales, debe de contener un nombre de usuario y una contraseña.")
            return
        try:
            with Conexion_base_datos() as db:
                session = db.abrir_sesion()
                with session.begin():  # Inicia una transacción
                    # Intentamos actualizar el usuario
                    usuario_actualizado = UsuarioModel(session).actualizar_usuario(
                        id_usuario , usuario, password, fecha_actualizacion, rol
                    )
                    
                    if usuario_actualizado:
                        Mensaje().mensaje_informativo("Credenciales actualizadas con éxito.")
                        self.cerrar()  # Cierra la ventana o la acción correspondiente
                    else:
                        Mensaje().mensaje_informativo("No se pudo actualizar el usuario. Verifica los datos e intenta de nuevo.")
        except Exception as e:
            # Captura cualquier excepción no controlada durante la transacción
            print(f"Ocurrió un error al actualizar las credenciales: {e}")
            Mensaje().mensaje_alerta("Ocurrió un error al intentar actualizar las credenciales. Intenta nuevamente.")

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
        if self.empleado_existente is None:
            Mensaje().mensaje_informativo("No se logro dar de baja al empleado")
            return
        self.mostrar_modal_local()
        with Conexion_base_datos() as db:
            session = db.abrir_sesion()
            with session.begin():
                try:
                    empleado, estatus = EmpleadosModel(session).baja_empleado(self.empleado_existente.id, False, fecha_actual)
                    if estatus:
                        Mensaje().mensaje_informativo("Empleado dado de baja con exito")
                        self.cerrar()
                except Exception as e:
                    Mensaje().mensaje_critico(f'Surgio un error al dar de baja el registro debido a {e}')
            self.registro_agregado_signal.emit()
            return
        Mensaje().mensaje_informativo("Existio un error al dar de baja al empleado.")
        self.cargando_cerrar()
    
    def mostrar_agregar_credenciales(self):
        if self.ui.opcion_usodelsistema.isChecked():
            self.ui.contenedor_credencialesusuario.show()
        else:
            self.ui.contenedor_credencialesusuario.hide()
            
    def obtener_empleado(self, empleado_seleccionado = None):
        if empleado_seleccionado is not None:
            self.ui.btn_btn_bajapersona.show()
            self.ui.btn_btn_recontratar.show()
            self.empleado_existente = empleado_seleccionado
            self.cargar_datos_empleado(empleado_seleccionado)

    def cargar_datos_empleado(self, empleado_seleccionado = None):
        opciones_estado_civil = self.estados_civiles
        opciones_niveles_academicos = self.niveles_academicos
        opciones_parentesco = self.parentesco_contacto
        
        if not empleado_seleccionado:
            Mensaje().mensaje_informativo("No se ha seleccionado un empleado de la base de datos")
            return
        self.ui.txt_nombre.setText(empleado_seleccionado.nombre)
        self.ui.txt_apellidop.setText(empleado_seleccionado.apellido_paterno)
        self.ui.txt_apellidom.setText(empleado_seleccionado.apellido_materno)
        self.ui.fecha_fechanacimiento.setDate(empleado_seleccionado.fecha_nacimiento)
        self.ui.txt_curp.setText(empleado_seleccionado.curp)
        self.ui.txt_rfc.setText(empleado_seleccionado.rfc)
        self.ui.txt_carrera.setText(empleado_seleccionado.carrera)
        self.ui.txt_correoelectronico.setText(empleado_seleccionado.correo_electronico)
        self.ui.txt_numerosegurosicial.setText(empleado_seleccionado.numero_seguro_social)
        self.ui.fecha_fechacontratacion.setDate(empleado_seleccionado.fecha_contratacion)
        
        self.ui.txt_ciudad.setText(empleado_seleccionado.ciudad)
        self.ui.txt_codigopostal.setText(empleado_seleccionado.codigo_postal)
        self.ui.txt_estado.setText(empleado_seleccionado.estado)
        self.ui.txt_pais.setText(empleado_seleccionado.pais)
        self.ui.txt_numerotelefono.setText(empleado_seleccionado.numero_telefonico)
        self.ui.txt_nombrecontactoemergencia.setText(empleado_seleccionado.nombre_contacto)
        self.ui.txt_contactoemergencia.setText(empleado_seleccionado.contacto_emergencia)
        self.ui.txt_calles.setText(empleado_seleccionado.calles)
        self.ui.txt_avenidas.setText(empleado_seleccionado.avenidas)
        self.ui.txt_colonia.setText(empleado_seleccionado.colonia)
        self.ui.txt_ninterior.setText(empleado_seleccionado.num_interior)
        self.ui.txt_nexterior.setText(empleado_seleccionado.num_exterior)
        self.ui.txtlargo_direccion_completa.setPlainText(empleado_seleccionado.direccion_adicional)
        self.ui.foto_usuario.setPixmap(QPixmap(empleado_seleccionado.foto).scaled(self.ui.foto_usuario.size()))
        self.file_name = empleado_seleccionado.foto
        
        self.ui.Button_aceptar.hide()
        self.ui.Button_actualizar.show()
        

        if empleado_seleccionado.puesto:
            nombre = empleado_seleccionado.puesto.nombre
            FuncionesAuxiliaresController().caja_opciones_mover_elemento(self.ui.cajaopciones_puestos, nombre)
                
        if empleado_seleccionado.parentesco_contacto:
            nombre = empleado_seleccionado.parentesco_contacto
            FuncionesAuxiliaresController().caja_opciones_mover_elemento(self.ui.cajaopciones_parentesco, nombre)
        
        if empleado_seleccionado.nivel_academico:
            nombre = empleado_seleccionado.nivel_academico
            FuncionesAuxiliaresController().caja_opciones_mover_elemento(self.ui.cajaopciones_nivelacademico, nombre)
        
        if empleado_seleccionado.estado_civil:
            nombre = empleado_seleccionado.estado_civil
            FuncionesAuxiliaresController().caja_opciones_mover_elemento(self.ui.cajaopciones_estadocvil, nombre)
            
        if empleado_seleccionado.genero:
            nombre = empleado_seleccionado.genero
            FuncionesAuxiliaresController().caja_opciones_mover_elemento(self.ui.cajaopciones_genero, nombre)
            
        if empleado_seleccionado.sucursal:
            nombre = empleado_seleccionado.sucursal.nombre_sucursal
            FuncionesAuxiliaresController().caja_opciones_mover_elemento(self.ui.cajaopciones_sucursales, nombre)
        
        if empleado_seleccionado.departamento:
            nombre = empleado_seleccionado.departamento.nombre
            FuncionesAuxiliaresController().caja_opciones_mover_elemento(self.ui.cajaopciones_departamentos, nombre)
            
        if empleado_seleccionado.usuario and empleado_seleccionado.usuario.rol:
            nombre = empleado_seleccionado.usuario.rol.nombre
            FuncionesAuxiliaresController().caja_opciones_mover_elemento(self.ui.cajaopciones_rol_usuario, nombre)
            
        if empleado_seleccionado.usuario:
            self.ui.opcion_usodelsistema.setText("Cambiar Creadenciales")
            self.ui.opcion_actualizar_datoscredenciales.show()
            self.ui.Button_actualizarcredenciales.show()
            self.ui.Button_eliminar_credenciales.show()
            self.ui.txt_usuario_iniciosesion.setEnabled(False)
            self.ui.txt_contrasenia_usuario_iniciosesion.setEnabled(False)
            self.ui.opcion_actualizar_datoscredenciales.toggled.connect(self.permiso_actualizar_credenciales)
            
        if not empleado_seleccionado.usuario:
            self.ui.opcion_usodelsistema.setText("Crear usuario para acceso al sistema")
            self.ui.Button_agregarUsuario.show()
            
        self.mostrar_estatus_empleado(empleado_seleccionado)
                    
    def mostrar_estatus_empleado(self, empleado_seleccionado = None):
        if empleado_seleccionado.activo:
            # Si estatus es verdadero, mostrar el QLabel y aplicar un estilo indicativo de "activo".
            self.ui.etiqueta_status_empleado.show()
            self.ui.etiqueta_status_empleado.setText("Estado: Activo")  # Puedes poner un texto visible
            self.ui.etiqueta_status_empleado.setStyleSheet("""
                background: #68a67d;  /* Verde para activo */
                color: white;
            """)
            self.ui.fecha_fechadespido.hide()
            self.ui.etiqueta_fechadespido.hide()
            return
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
            if empleado_seleccionado.fecha_despido:
                self.ui.fecha_fechadespido.setDate(empleado_seleccionado.fecha_despido)
            else:
                self.ui.fecha_fechadespido.hide()
    
    def agregar_sucursal(self):
        if self.sucursales is None or not self.sucursales.isVisible():
            self.sucursales = SucursalesController()
            self.sucursales.setParent(self)
            self.listar_sucursales_signal.connect(self.sucursales.obtener_sucursales)
            self.sucursales.signal_sucursal_agregada.connect(self.listar_sucursales)
            self.sucursales.VENTANA_SUCURSALES_CERRADA.connect(self.ventana_sucursales_cerrada)
            self.listar_sucursales_signal.emit()
            self.sucursales.setModal(True)
            self.sucursales.exec_()
        else:
            self.sucursales.raise_()
            self.sucursales.activateWindow()

    def ventana_sucursales_cerrada(self):
        self.sucursales = None
    
    def ventana_departamentos(self):
        if self.departamentos is None or not self.departamentos.isVisible():
            self.departamentos = DepartamentosController()
            self.departamentos.setParent(self)
            self.listar_departamentos_signal.connect(self.departamentos.obtener_departamentos)
            self.listar_sucursales_en_departamentos_signal.connect(self.departamentos.listar_sucursales_existentes)
            self.departamentos.signal_departamento_agregado.connect(self.listar_departamentos)
            self.departamentos.VENTANA_DEPARTAMENTOS_CERRADA.connect(self.ventana_departamentos_cerrada)
            self.listar_sucursales_en_departamentos_signal.emit()
            self.listar_departamentos_signal.emit()
            self.departamentos.setModal(True)
            self.departamentos.exec_()
        else:
            self.departamentos.raise_()
            self.departamentos.activateWindow()
            
    def ventana_departamentos_cerrada(self):
        self.departamentos = None
    
    def ventana_puestos(self):
        if self.puestos is None or not self.puestos.isVisible():
            self.puestos = PuestosController()
            self.puestos.setParent(self)
            self.puestos.signal_puesto_agregado.connect(self.listar_puestos)
            self.puestos.VENTANA_PUESTOS_CERRADA.connect(self.ventana_puestos_cerrada)
            self.listar_puestos_signal.connect(self.puestos.listar_puestos)
            self.listar_depas_en_puestos_signal.connect(self.puestos.listar_departamentos)
            self.listar_depas_en_puestos_signal.emit()
            self.listar_puestos_signal.emit()
            self.puestos.exec_()
        else:
            self.puestos.raise_()
            self.puestos.activateWindow()
            
    def ventana_puestos_cerrada(self):
        self.puestos = None

    def listar_sucursales(self):
        self.ui.cajaopciones_sucursales.clear()
        sucursales = None
        try:
            with Conexion_base_datos() as db:
                session = db.session
                sucursales = SucursalesModel(session).obtener_todo()
            if sucursales:
                for sucursal in sucursales:
                    self.ui.cajaopciones_sucursales.addItem(sucursal.nombre_sucursal, sucursal)
                AjustarCajaOpciones().ajustar_cajadeopciones(self.ui.cajaopciones_sucursales)
        except Exception as e:
            Mensaje().mensaje_critico(f"Error al obtener sucursales debido a lo siguiente: {e}")

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
            Mensaje().mensaje_critico(f"Error al obtener grupos permisos roles: {e}")

    def listar_departamentos(self):
        self.ui.cajaopciones_departamentos.clear()
        departamentos = None
        try:
            with Conexion_base_datos() as db:
                session = db.session
                departamentos, estado = DepartamentosModel(session).obtener_todos()
            if departamentos:
                for departamento in departamentos:
                    self.ui.cajaopciones_departamentos.addItem(departamento.nombre, departamento)
                AjustarCajaOpciones().ajustar_cajadeopciones(self.ui.cajaopciones_departamentos)
        except Exception as e:
            Mensaje().mensaje_critico(f"Error al obtener departamentos: {e}")

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
                        self.ui.cajaopciones_puestos.addItem(puesto.nombre,  puesto)
                    AjustarCajaOpciones().ajustar_cajadeopciones(self.ui.cajaopciones_puestos)

        except Exception as e:
            Mensaje().mensaje_critico(f"Error al obtener puestos debido a lo siguiente: {e}")

    def cargar_imagen(self, event):
        options = QFileDialog.Options()
        self.file_name, _ = QFileDialog.getOpenFileName(self, 'SELECCIONA UNA IMAGEN', ' ', 'Archivo de Imagen (*.png *.jpg *.jpeg);; Todos los archivos (*)', options=options)
        image_accept = FuncionesAuxiliaresController().size_validator_image(self.file_name)
        if self.file_name:
            if image_accept:
                self.ui.foto_usuario.setText(self.file_name)
                pixmap = QPixmap(self.file_name)
                self.ui.foto_usuario.setPixmap(pixmap)
                self.ui.foto_usuario.setScaledContents(True)
                self.ui.foto_usuario.adjustSize()
            else:
                Mensaje().mensaje_alerta("El tamaño de la imagen sobre pasa los 5Mb")
        return
        
    def ingresar_validaciones(self):
        self.ui.txt_nombre.setMaxLength(60)
        self.ui.txt_apellidop.setMaxLength(60)
        self.ui.txt_apellidom.setMaxLength(60)
        self.ui.txt_curp.setMaxLength(18)
        self.ui.txt_rfc.setMaxLength(13)
        self.ui.txt_carrera.setMaxLength(150)
        self.ui.txt_correoelectronico.setMaxLength(100)
        self.ui.txt_numerosegurosicial.setMaxLength(13)
        self.ui.txt_ciudad.setMaxLength(50)
        self.ui.txt_codigopostal.setMaxLength(5)
        self.ui.txt_estado.setMaxLength(50)
        self.ui.txt_pais.setMaxLength(50)
        self.ui.txt_numerotelefono.setMaxLength(10)
        self.ui.txt_nombrecontactoemergencia.setMaxLength(100)
        self.ui.txt_contactoemergencia.setMaxLength(10)
        self.ui.txt_calles.setMaxLength(50)
        self.ui.txt_avenidas.setMaxLength(50)
        self.ui.txt_colonia.setMaxLength(50)
        self.ui.txt_ninterior.setMaxLength(10)
        self.ui.txt_nexterior.setMaxLength(10)
        self.ui.txt_usuario_iniciosesion.setMaxLength(60)
        self.ui.txt_contrasenia_usuario_iniciosesion.setMaxLength(10)
        
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
        self.ui.txt_carrera.setValidator(Validaciones().get_text_validator)
        self.ui.txt_contactoemergencia.setValidator(Validaciones().get_phone_validator)
        self.ui.txt_nombrecontactoemergencia.setValidator(Validaciones().get_text_validator)
        self.ui.txt_colonia.setValidator(Validaciones().get_text_validator)
        self.ui.txt_ninterior.setValidator(Validaciones().get_int_validator)
        self.ui.txt_nexterior.setValidator(Validaciones().get_int_validator)
        
    def campos(self):
        return {
            "nombre": self.ui.txt_nombre,
            "apellido_paterno": self.ui.txt_apellidop,
            "apellido_materno": self.ui.txt_apellidom,
            "fecha_nacimiento": self.ui.fecha_fechanacimiento,
            "genero": self.ui.cajaopciones_genero,
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
            "nivel_academico": self.ui.cajaopciones_nivelacademico,
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
            "rol": self.ui.cajaopciones_rol_usuario
        }
    
    def obtener_datos(self):
        datos = {}
        campos = self.campos()
        for nombre, campo in campos.items():
            if isinstance(campo, QLineEdit):
                datos[nombre] = campo.text().strip()
            elif isinstance(campo, QDateEdit):
                datos[nombre] = campo.date().toString('yyyy-MM-dd')
            elif isinstance(campo, QTimeEdit):
                datos[nombre] = campo.time().toString('HH:mm')
            elif isinstance(campo, QPlainTextEdit):
                datos[nombre] = campo.toPlainText().strip()
            elif isinstance(campo, (QDoubleSpinBox, QSpinBox)):
                datos[nombre] = campo.value()
            elif isinstance(campo, QComboBox):
                datos[nombre] = campo.currentData() if campo.currentData() is not None else campo.currentText()

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
    
    def agregar_nuevo_empleado(self):
        fecha_actual = datetime.now().date()
        uso_del_sistema = self.ui.opcion_usodelsistema.isChecked()
        id_empleado = self.empleado.id if self.empleado else None
        nombre_usuario = self.ui.txt_usuario_iniciosesion.text().strip()
        password_usuario = self.ui.txt_contrasenia_usuario_iniciosesion.text().strip()
        current_data_rol = self.ui.cajaopciones_rol_usuario.currentData()
        datos = self.obtener_datos()

        if self.validar_datos(datos=datos):
            self.mostrar_modal_local()
            self.consultor = Consultas_segundo_plano()
            self.consultor.error.connect(self.mostrar_error_hilo)
            self.consultor.terminado.connect(self.cargando_cerrar)
            self.consultor.resultado.connect(self.mostrar_estado_usuario)
            self.consultor.ejecutar_hilo(
                funcion=self.almacenar_informacion_query,
                uso_del_sistema=uso_del_sistema,
                id_empleado=id_empleado,
                imagen = self.file_name,
                nombre_usuario=nombre_usuario,
                password_usuario=password_usuario,
                fecha_creacion=fecha_actual,
                fecha_actualizacion=fecha_actual,
                current_data_rol=current_data_rol,
                datos=datos
            )

    def mostrar_estado_usuario(self, mensaje, estado):
        Mensaje().mensaje_informativo(mensaje)
        if estado:
            self.cerrar()
            self.registro_agregado_signal.emit()
            if self.empleado is None:
                self.abrir_inicio()

    def mostrar_error_hilo(self, error):
        Mensaje().mensaje_alerta(f"Ocurrió un error: {error}")

    def mostrar_modal_local(self):
        if self.cargando is None or not self.cargando.isVisible():
            self.cargando = Modal_de_espera()
            self.cargando.show()
        else:
            self.cargando.raise_()
            self.cargando.activateWindow()
            
    def cargando_cerrar(self):
        if self.cargando:
            self.cargando.close()
            self.cargando = None

    def almacenar_informacion_query(self, session, uso_del_sistema, id_empleado, imagen, nombre_usuario, password_usuario, fecha_creacion, fecha_actualizacion, current_data_rol, datos):
        try:
            if uso_del_sistema and id_empleado is None:
                usuario, status_usuario = UsuarioModel(session).crear_usuario(
                    usuario=nombre_usuario,
                    password=password_usuario,
                    fecha_creacion=fecha_creacion,
                    fecha_actualizacion=fecha_actualizacion,
                    rol_id=current_data_rol
                )
                if not status_usuario:
                    return "El usuario que estás intentando asignar ya existe.", False
            else:
                usuario = None

            empleado, status_empleado = EmpleadosModel(session).crear_empleado(
                nombre=datos['nombre'],
                apellido_paterno=datos['apellido_paterno'],
                apellido_materno=datos['apellido_materno'],
                fecha_nacimiento=datos['fecha_nacimiento'],
                estado_civil=datos['estado_civil'],  # ← no accedes self.ui aquí
                genero=datos['genero'],
                curp=datos['curp'],
                rfc=datos['rfc'],
                nivel_academico=datos['nivel_academico'],
                carrera=datos['carrera'],
                correo_electronico=datos['correo'],
                numero_seguro_social=datos['nss'],
                fecha_contratacion=datos['fecha_contratacion'],
                fecha_despido=None,
                ciudad=datos['ciudad'],
                codigo_postal=datos['cp'],
                estado=datos['estado'],
                pais=datos['pais'],
                numero_telefonico=datos['num_telefono'],
                nombre_contacto=datos['nombre_contacto_emergencia'],
                contacto_emergencia=datos['contacto_emergencia'],
                parentesco_contacto=datos['parentesco_contacto_emergencia'],
                calles=datos['calles'],
                avenidas=datos['avenidas'],
                colonia=datos['colonia'],
                num_interior=datos['num_interior'],
                num_exterior=datos['num_exterior'],
                direccion_adicional=datos['direccion_adicional'],
                activo=True,
                foto = imagen,
                puesto_id=datos['puesto'].id,
                usuario_id=usuario.id if usuario else None,
                departamento_id=datos['departamento'].id,
                sucursal_id=datos['sucursal'].id
            )

            if status_empleado:
                session.commit()
                return "Registro exitoso.", True
            else:
                return "No se pudo registrar el empleado.", False

        except Exception as e:
            session.rollback()
            traceback.print_exc()
            return f"Ocurrió un error inesperado: {str(e)}", False

    def mostrar_estado_usuario_actualizado(self, mensaje, estado):
        if estado:
            self.cerrar()
            self.registro_agregado_signal.emit()
            
        Mensaje().mensaje_informativo(mensaje)

    def actualizar_empleado(self):
        id_empleado = self.empleado_existente.id if self.empleado_existente else None
        datos = self.obtener_datos()
        print(self.empleado_existente, id_empleado)
        if self.validar_datos(datos) and id_empleado is not None:
            self.mostrar_modal_local()
            self.consultor = Consultas_segundo_plano()
            self.consultor.error.connect(self.mostrar_error_hilo)
            self.consultor.terminado.connect(self.cargando_cerrar)
            self.consultor.resultado.connect(self.mostrar_estado_usuario_actualizado)
            self.consultor.ejecutar_hilo(
                funcion=self.actualizar_empleado_query,
                id_empleado=id_empleado,
                imagen = self.file_name,
                datos=datos
            )
        else:
            Mensaje().mensaje_informativo("Todos los campos deben de estar completos")
    
    def actualizar_empleado_query(self, session, id_empleado, imagen,  datos):
        try:
            empleado, estado = EmpleadosModel(session).actualizar_empleado(
                id_empleado = id_empleado,
                nombre=datos['nombre'],
                apellido_paterno=datos['apellido_paterno'],
                apellido_materno=datos['apellido_materno'],
                fecha_nacimiento=datos['fecha_nacimiento'],
                estado_civil=datos['estado_civil'],
                genero=datos['genero'],
                curp=datos['curp'],
                rfc=datos['rfc'],
                nivel_academico=datos['nivel_academico'],
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
                parentesco_contacto=datos['parentesco_contacto_emergencia'],
                calles=datos["calles"],
                avenidas=datos["avenidas"],
                colonia=datos["colonia"],
                num_interior=datos["num_interior"],
                num_exterior=datos["num_exterior"],
                direccion_adicional=datos["direccion_adicional"],
                foto=imagen,
                puesto_id=datos['puesto'].id,
                departamento_id=datos['departamento'].id,
                sucursal_id=datos['sucursal'].id
            )
        except Exception as e:
            session.rollback()
            mensaje = f"Error al actualizar el empleado: {e}"
            return mensaje, False
        if estado:
            session.commit()
            mensaje = "Registro exitoso"
            return mensaje, True
        
        return "no se logro actualizar", False
            
            
    def agregar_usuario(self):
        print(self.empleado_existente.id)
        if not self.empleado_existente:
            Mensaje().mensaje_alerta("No se encuentra vinculado el empleado a la session de base de datos")
            return
        elif not self.ui.txt_usuario_iniciosesion.text() and not self.ui.txt_contrasenia_usuario_iniciosesion.text():
            Mensaje().mensaje_alerta("Debes de agregar un usuario y una contraseña para completar el registro del usuario para el empleado.")
            return
        fecha_actual = datetime.now().date()
        usuario = self.ui.txt_usuario_iniciosesion.text()
        password = self.ui.txt_contrasenia_usuario_iniciosesion.text()
        fecha_actualizacion = datetime.now().date()
        rol = self.ui.cajaopciones_rol_usuario.currentData()
        with Conexion_base_datos() as db:
            session = db.abrir_sesion()
            with session.begin():
                usuario, status_usuario = UsuarioModel(session).crear_usuario(
                                    usuario = usuario,
                                    password = password,
                                    fecha_creacion = fecha_actual,
                                    fecha_actualizacion = fecha_actual,
                                    rol_id = rol)
                if not status_usuario:
                    Mensaje().mensaje_alerta("El usuario que intentas crear ya esta ocupado.")
                    return
                
                self.empleado_existente.usuario_id = usuario.id
                
                # Agregar el empleado a la sesión para guardar los cambios
                session.add(self.empleado_existente)
                
                session.commit()
                Mensaje().mensaje_informativo("Usuario asignado correctamente al empleado.")
            
    
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

