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

class SucursalesController(QWidget):
    signal_sucursal_agregada = pyqtSignal()
    def __init__(self):
        super().__init__()
        self.ui = Ui_Nueva_sucursal()
        self.ui.setupUi(self)
        self.ui.btn_btn_agregar.clicked.connect(self.agregar)
        self.ui.lista_sucursales.itemClicked.connect(self.obtenerId)
        self.ui.btn_btn_limpiar.clicked.connect(self.limpiar)
        self.ui.btn_btn_eliminar.clicked.connect(self.eliminar)
        self.listar_sucursales()
        self.id_sucursal = None

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
                    self.signal_sucursal_agregada.emit()
                    Mensaje().mensaje_informativo('Se ha agregado la sucursal con éxito')

                except Exception as e:
                    # Manejo de errores
                    Mensaje().mensaje_alerta(f'Error al agregar la sucursal: {e}')
        
        # Listar sucursales después de agregar
        self.listar_sucursales()
        self.limpiar()
                        
    def listar_sucursales(self):
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
                for  sucursal in sucursales:
                    # Crear un QListWidgetItem
                    item = QListWidgetItem(sucursal.nombre_sucursal)
                    
                    # Establecer el ícono en el ítem
                    item.setIcon(self.icon)
                    item.setData(Qt.UserRole, sucursal.id)
                    
                    # Agregar el ítem a la lista
                    self.ui.lista_sucursales.addItem(item)
        except Exception as e:
            print(f'Error al listar las sucursales : {e}')

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
                except Exception as e:
                    print(f'Error al obtener sucursal: {e}')
            
    def eliminar(self):
        sucursalId = self.id_sucursal
        print(sucursalId)
        with Conexion_base_datos() as db:
            session = db.abrir_sesion()
            with session.begin():
                try:
                    sucursal_eliminada = SucursalesModel(session).eliminar(sucursalId)
                    if sucursal_eliminada:
                        print("Sucursal eliminada con éxito")
                except Exception as e:
                        print(f"Error al eliminar la sucursal : {e}")
        self.limpiar()
        self.listar_sucursales()
