from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from ..Source.ibootstrap_rc import  *
from .MensajesAlertasController import Mensaje
from ..DataBase.conexionBD import Conexion_base_datos
from ..View.UserInterfacePy.UI_CONTROL_DEPARTAMENTOS import Ui_Control_departamentos
from ..Model.SucursalesModel import SucursalesModel
from ..Model.DepartamentosModel import DepartamentosModel

class DepartamentosController(QWidget):
    
    def __init__(self):
        super().__init__()
        self.ui = Ui_Control_departamentos()
        self.ui.setupUi(self)

        #botones:
        self.ui.btn_btn_guardar.clicked.connect(self.guardar)
        self.ui.btn_btn_eliminar.clicked.connect(self.eliminar)
        self.ui.btn_btn_vincular.clicked.connect(self.vincular_sucursal)
        self.ui.btn_btn_desvincular.clicked.connect(self.desvincular_sucursal)
        

        #// variables globales:
        self.sucursales = []
        self.idSucursales = None
        self.sucursales_seleccionadas = []
        self.icon = QIcon(':/Icons/Bootstrap/building-fill-check.svg')

        #// funciones iniciales:
        self.listar_sucursales_existentes()

    
    #funciones:
    def campos(self):
        return{
            'nombre': self.ui.txt_nombredepartamento,
            'descripcion': self.ui.txtlargo_descripciondepartamento
        }
    
    def obtener_contenido_campos(self):
        return {
            nombre : widget.text().strip().upper() for nombre, widget in self.campos().items()
        }
    
    def validar(self, campos):
        campos_vacios = [nombre for nombre, valor in campos.items() if not valor]
        if campos_vacios:
            print(f'tienes campos vacios')
            return False
        return True
    
    def guardar(self):
        try:
            datos = self.obtener_contenido_campos()
            if not self.validar(datos):
                print('campos incompletos')
                return
            with Conexion_base_datos() as db:
                session = db.abrir_sesion()
                with session.begin():
                    departamentos_sucursales, agregado = DepartamentosModel(session).agregar_departamento(**datos)
                    if agregado:
                        print('departamento agregado')
                    else:
                        print('no se pudo agregar')
        except Exception as e:
            print(f'error al guardar: {e}')

    def eliminar(self):
        pass

    def vincular_sucursal(self):
        sucursal_seleccionada = self.ui.lista_sucursalesexistentes.currentItem()
        print(sucursal_seleccionada)
        if sucursal_seleccionada:
            sucursal_id = sucursal_seleccionada.data(Qt.UserRole)

            if sucursal_id not in self.sucursales_seleccionadas:
                self.sucursales_seleccionadas.append(sucursal_id)
                
                # Crear un nuevo QListWidgetItem para agregarlo a la lista de sucursales vinculadas
                elemento_vinculado = QListWidgetItem(sucursal_seleccionada.text())
                elemento_vinculado.setIcon(self.icon)
                elemento_vinculado.setData(Qt.UserRole, sucursal_id)

                # Añadir el elemento a la lista de sucursales vinculadas
                self.ui.lista_sucursalesvinculadas.addItem(elemento_vinculado)

                self.ui.lista_sucursalesexistentes.takeItem(self.ui.lista_sucursalesexistentes.row(sucursal_seleccionada))


    
    def desvincular_sucursal(self):
        sucursal_seleccionada = self.ui.lista_sucursalesvinculadas.currentItem()
        if sucursal_seleccionada:
            sucursal_id = sucursal_seleccionada.data(Qt.UserRole)
            self.sucursales_seleccionadas.remove(sucursal_id)  # Remover de la lista temporal

            # Agregar de nuevo a la lista de sucursales existentes
            item_devolver = QListWidgetItem(sucursal_seleccionada.text())
            item_devolver.setIcon(self.icon)
            item_devolver.setData(Qt.UserRole, sucursal_id)
            self.ui.lista_sucursalesexistentes.addItem(item_devolver)

            # Eliminar de la lista de sucursales vinculadas
            self.ui.lista_sucursalesvinculadas.takeItem(self.ui.lista_sucursalesvinculadas.row(sucursal_seleccionada))

    def listar_sucursales_existentes(self):
        sucursales = None
        self.ui.lista_sucursalesexistentes.clear()
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
                    self.ui.lista_sucursalesexistentes.addItem(item)

        
        except Exception as e:
            print(f'Error al listar las sucursales : {e}')