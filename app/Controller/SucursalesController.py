from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from ..Source.ibootstrap_rc import  *
from .MensajesAlertasController import Mensaje
from ..DataBase.conexionBD import *
from ..View.UserInterfacePy.UI_CONTROL_SUCURSALES import *
from .MensajesAlertasController import *
from ..Model.SucursalesModel import SucursalesModel
from ..Model.DepartamentosModel import DepartamentosModel

class SucursalesController(QWidget):
    signal_sucursal_agregada = pyqtSignal()
    def __init__(self):
        super().__init__()
        self.ui = Ui_Nueva_sucursal()
        self.ui.setupUi(self)
        pantalla = self.frameGeometry()
        pantalla.moveCenter(self.screen().availableGeometry().center())
        self.move(pantalla.topLeft())
        
        #// LIMITE CARACTERES
        self.ui.txt_nombre.setMaxLength(50)
        self.ui.txt_codigopostal.setMaxLength(5)
        self.ui.txt_ciudad.setMaxLength(50)
        self.ui.txt_estado.setMaxLength(50)
        self.ui.txt_pais.setMaxLength(50)
        self.ui.txt_ntelefono.setMaxLength(10)
        
        self.ui.btn_btn_agregar.clicked.connect(self.agregar)
        self.ui.lista_sucursales.itemClicked.connect(self.obtenerId)
        self.ui.btn_btn_limpiar.clicked.connect(self.limpiar)
        self.ui.btn_btn_eliminar.clicked.connect(self.eliminar)
        self.ui.btn_btn_actualizar.clicked.connect(self.actualizar)


        # señales:
        self.ui.txt_buscarsucursales.returnPressed.connect(self.buscar_sucursal)
        self.obtener_sucursales()
        self.id_sucursal = None
        self.sucursales = None


    def buscar_sucursal(self):
        nombre_sucursal = self.ui.txt_buscarsucursales.text()
        with Conexion_base_datos() as db:
            session = db.abrir_sesion()
            with session.begin():
                self.sucursales, estado = SucursalesModel(session).filtrar_nombre(nombre_sucursal)
                if estado == True:
                    self.listar_sucursales(self.sucursales)

    def limpiar(self):
        for campo in self.campos_nomales().values():
            # Limpiar QLineEdit
            if isinstance(campo, QLineEdit):
                campo.clear()
            # Limpiar QPlainTextEdit
            elif isinstance(campo, QPlainTextEdit):
                campo.clear()
        self.id_sucursal = None

        
    def campos_nomales(self):
        return {
            'nombre_sucursal': self.ui.txt_nombre,
            'codigo_postal': self.ui.txt_codigopostal,
            'ciudad': self.ui.txt_ciudad,
            'estado': self.ui.txt_estado,
            'pais': self.ui.txt_pais,
            'num_telefono': self.ui.txt_ntelefono,
            'direccion': self.ui.txtlargo_direccion
        }
    
    def obtener_datos_campos(self):
        return {
            'nombre_sucursal': self.ui.txt_nombre.text().strip().upper(),
            'codigo_postal': self.ui.txt_codigopostal.text().strip().upper(),
            'ciudad': self.ui.txt_ciudad.text().strip().upper(),
            'estado': self.ui.txt_estado.text().strip().upper(),
            'pais': self.ui.txt_pais.text().strip().upper(),
            'num_telefono': self.ui.txt_ntelefono.text().strip().upper(),
            'direccion': self.ui.txtlargo_direccion.toPlainText().strip().upper()
        }

    def agregar(self):
        # Obtener los datos de los campos
        datos = self.obtener_datos_campos()

        # Verifica si todos los campos están completos
        if any(value == '' for value in datos.values()):
            Mensaje().mensaje_alerta("Todos los campos deben de estar completos.")
            return  # Salir del método si hay campos vacíos

        # Iniciar la conexión a la base de datos
        with Conexion_base_datos() as db:
            session = db.abrir_sesion()
            with session.begin():
                try:
                    # Agregar la sucursal a la base de datos
                    sucursal, creada = SucursalesModel(session).agregar_sucursal(**datos)
                    if creada == False:
                        if sucursal.nombre_sucursal == datos['nombre_sucursal']:
                            Mensaje().mensaje_informativo('El nombre de la sucursal que intentas agregar ya existe.')
                            return
                    Mensaje().mensaje_informativo('Se ha agregado la sucursal con éxito')
                except Exception as e:
                    # Manejo de errores
                    Mensaje().mensaje_alerta(f'Error al agregar la sucursal: {e}')
                    return
        
        self.signal_sucursal_agregada.emit()
        # Listar sucursales después de agregar
        self.obtener_sucursales()
        self.limpiar()
                        
    def obtener_sucursales(self):
        sucursales = None
        self.ui.lista_sucursales.clear()
        self.icon = QIcon(':/Icons/Bootstrap/building-fill-check.svg')
        try:
            with Conexion_base_datos() as db:
                session = db.abrir_sesion()
                try:
                    sucursales = SucursalesModel(session).obtener_todo()
                except Exception as e:
                    Mensaje().mensaje_alerta("Error al obtener sucursales")
            if sucursales:
                self.listar_sucursales(sucursales)
        except Exception as e:
            Mensaje().mensaje_critico(f'Error al listar las sucursales : {e}')

    def listar_sucursales(self, sucursales):
        if sucursales:
            self.ui.lista_sucursales.clear()
            for  sucursal in sucursales:
                # Crear un QListWidgetItem
                item = QListWidgetItem(sucursal.nombre_sucursal)
                
                # Establecer el ícono en el ítem
                item.setIcon(self.icon)
                item.setData(Qt.UserRole, sucursal.id)
                
                # Agregar el ítem a la lista
                self.ui.lista_sucursales.addItem(item)

    def obtenerId(self, item):
        self.id_sucursal = item.data(Qt.UserRole)
        with Conexion_base_datos() as db:
            session = db.abrir_sesion()
            with session.begin():
                try:
                    sucursal = SucursalesModel(session).obtener_sucursal_por_id(self.id_sucursal)
                    if sucursal is not None:
                        self.ui.txt_nombre.setText(sucursal.nombre_sucursal)
                        self.ui.txt_codigopostal.setText(sucursal.codigo_postal)  # Asegúrate de que sea `codigo_postal`
                        self.ui.txt_ciudad.setText(sucursal.ciudad)  # Aquí debe ser `ciudad`
                        self.ui.txt_estado.setText(sucursal.estado)  # Aquí debe ser `estado`
                        self.ui.txt_pais.setText(sucursal.pais)  # Aquí debe ser `pais`
                        self.ui.txt_ntelefono.setText(sucursal.num_telefono)  # Aquí debe ser `num_telefono`
                        self.ui.txtlargo_direccion.setPlainText(sucursal.direccion)
                        self.listar_departamentos_asignados(sucursal.departamentos)
                except Exception as e:
                    Mensaje().mensaje_critico(f'Error al obtener sucursal: {e}')

    def listar_departamentos_asignados(self, departamentos):
        if departamentos:
            self.ui.lista_departamentosasociados.clear()
            for  nombre in departamentos:
                # Crear un QListWidgetItem
                item = QListWidgetItem(nombre.nombre)
                
                # Establecer el ícono en el ítem
                item.setIcon(self.icon)
                item.setData(Qt.UserRole, nombre.id)
                
                # Agregar el ítem a la lista
                self.ui.lista_departamentosasociados.addItem(item)
        else:
            self.ui.lista_departamentosasociados.clear()
            
    def eliminar(self):
        sucursalId = self.id_sucursal
        with Conexion_base_datos() as db:
            session = db.abrir_sesion()
            with session.begin():
                try:
                    sucursal_eliminada = SucursalesModel(session).eliminar(sucursalId)
                    if sucursal_eliminada:
                        Mensaje().mensaje_informativo("Sucursal eliminada con éxito")
                except Exception as e:
                        Mensaje().mensaje_alerta(f"Error al eliminar la sucursal : {e}")

        self.signal_sucursal_agregada.emit()
        self.limpiar()
        self.obtener_sucursales()

    def actualizar(self):
        sucursalId = self.id_sucursal
        datos = self.obtener_datos_campos()  # Asumo que esto retorna los campos correctamente
        
        # Verifica que todos los campos estén completos
        if any(value == '' for value in datos.values()):
            Mensaje().mensaje_informativo("Error: Todos los campos deben estar completos")
            return
        
        # Iniciar la conexión a la base de datos
        with Conexion_base_datos() as db:
            session = db.abrir_sesion()
            with session.begin():  # La transacción comienza aquí
                try:
                    # Actualizar la sucursal sin hacer commit aún
                    sucursal_actualizada, actualizado = SucursalesModel(session).actualizar(sucursalId, **datos)
                    
                    # Validar si la actualización fue exitosa
                    if actualizado:
                        Mensaje().mensaje_informativo("Sucursal actualizada con éxito")
                    else:
                        Mensaje().mensaje_alerta("No se pudo actualizar la sucursal")
                    
                    # Aquí es donde el commit ocurrirá automáticamente si todo sale bien
                except Exception as e:
                    Mensaje().mensaje_critico(f"Error al actualizar la sucursal: {e}")
                    # Si ocurre una excepción, la transacción se hará rollback automáticamente
        self.limpiar()
        self.obtener_sucursales()
