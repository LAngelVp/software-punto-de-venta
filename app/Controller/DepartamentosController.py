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
    signal_departamento_agregado = pyqtSignal()
    def __init__(self):
        super().__init__()
        self.ui = Ui_Control_departamentos()
        self.ui.setupUi(self)
        pantalla = self.frameGeometry()
        pantalla.moveCenter(self.screen().availableGeometry().center())
        self.move(pantalla.topLeft())

        #botones:
        self.ui.btn_btn_guardar.clicked.connect(self.guardar)
        self.ui.btn_btn_eliminar.clicked.connect(self.eliminar)
        self.ui.btn_btn_actualizar.clicked.connect(self.actualizar)
        self.ui.btn_btn_vincular.clicked.connect(self.vincular_sucursal)
        self.ui.btn_btn_desvincular.clicked.connect(self.desvincular_sucursal)
        self.ui.btn_btn_limpiar.clicked.connect(self.limpiar)

        # señales:
        self.ui.lista_departamentosexistentes.itemClicked.connect(self.obtenerId)
        self.ui.txt_buscardepartamento.returnPressed.connect(self.buscar)
        

        #// variables globales:
        self.sucursales = []
        self.idSucursales = None
        self.sucursales_seleccionadas = set()
        self.sucursales_seleccionadas_existentes = set()
        self.departamentos = []
        self.iconSucursal = QIcon(':/Icons/Bootstrap/building-fill-check.svg')
        self.iconDepartamento = QIcon(':/Icons/Bootstrap/diagram-2-fill.svg')

        #// funciones iniciales:

    
    #funciones:
    def buscar(self):
        with Conexion_base_datos() as db:
            session = db.abrir_sesion()
            with session.begin():
                self.departamentos, estado = DepartamentosModel(session).filtrar_nombre(self.ui.txt_buscardepartamento.text())
                if estado == True:
                    self.ui.lista_puestosasignados.clear()
                    self.listar_departamentos(self.departamentos)
    def limpiar(self):
        datos = self.campos()
        for campo in datos.values():
            # Limpiar QLineEdit
            if isinstance(campo, QLineEdit):
                campo.clear()
            # Limpiar QPlainTextEdit
            elif isinstance(campo, QPlainTextEdit):
                campo.clear()

        self.id_departamento = None
        self.ui.lista_sucursalesvinculadas.clear()
        self.sucursales_seleccionadas.clear()
        self.sucursales_seleccionadas_existentes.clear()

        self.listar_sucursales_existentes(set())
        self.obtener_departamentos()

    def campos(self):
        return{
            'nombre': self.ui.txt_nombredepartamento,
            'descripcion': self.ui.txtlargo_descripciondepartamento
        }
    
    def obtener_contenido_campos(self):
        return {
            nombre : widget.text().strip().upper() 
            if isinstance(widget, QLineEdit) 
                else widget.toPlainText().strip().upper() 
                for nombre, widget in self.campos().items()
        }
    
    def validar(self, campos):
        campos_vacios = [nombre for nombre, valor in campos.items() if not valor]
        if campos_vacios:
            return False
        return True
    
    def guardar(self):
        try:
            datos = self.obtener_contenido_campos()
            if not self.validar(datos):
                Mensaje().mensaje_informativo('campos incompletos')
                return

            with Conexion_base_datos() as db:
                session = db.abrir_sesion()
                with session.begin():
                    departamento, agregado = DepartamentosModel(session).agregar_departamento(**datos)
                    
                    if not agregado:
                        Mensaje().mensaje_informativo('Ya existe un departamento con ese mismo nombre')
                        return

                    # Agregar sucursales si hay
                    for sucursal_id in self.sucursales_seleccionadas:
                        sucursal = SucursalesModel(session).obtener_sucursal_por_id(sucursal_id)
                        if sucursal and sucursal not in departamento.sucursales:
                            departamento.sucursales.append(sucursal)

        except Exception as e:
            Mensaje().mensaje_critico(f'error al guardar: {e}')
        self.signal_departamento_agregado.emit()
        self.limpiar()  # Actualizar la lista de departamentos

    def eliminar(self):
        departamentoId = self.id_departamento
        if departamentoId is not None:
            try:
                respuesta = Mensaje().mensaje_pregunta('Estas seguro de eliminar el departamento?')
                if respuesta == QMessageBox.Yes:
                    with Conexion_base_datos() as db:
                        session = db.abrir_sesion()
                        with session.begin():
                            departamento_eliminado = DepartamentosModel(session).eliminar_departamento(departamentoId)
                            if departamento_eliminado:
                                Mensaje().mensaje_informativo('Departamento eliminado')
                            else:
                                Mensaje().mensaje_alerta('no se pudo eliminar el departamento por que no existe')
                                return
                else:
                    return
            except Exception as e:
                Mensaje().mensaje_critico(f'error al eliminar el departamento: {e}')
            self.signal_departamento_agregado.emit()
            self.limpiar()

    def actualizar(self):
        departamentoId = self.id_departamento
        nuevos_datos = self.obtener_contenido_campos()

        if not self.validar(nuevos_datos):
            Mensaje().mensaje_alerta('No puedes dejar campos de nombre y descripcion vacios')
            return
        sucursales_seleccionadas = self.sucursales_seleccionadas
        respuesta = Mensaje().mensaje_pregunta('Estas seguro de actualizar el departamento')
        if respuesta == QMessageBox.Yes:
            try:
                with Conexion_base_datos() as db:
                    session = db.abrir_sesion()
                    with session.begin():
                        departamento_actualizado, respuesta = DepartamentosModel(session).actualizar_departamento(departamentoId, **nuevos_datos)
                        if respuesta == False:
                            Mensaje().mensaje_alerta('El departamento no fue encontrado')
                            return
                        sucursales_relacionadas = {
                            sucursal.id for sucursal in departamento_actualizado.sucursales
                        }
                        nuevas_sucursales = set(sucursales_seleccionadas)

                        # Añadir las nuevas sucursales que no estaban en la lista actual
                        for sucursal_id in nuevas_sucursales - sucursales_relacionadas:
                            sucursal = SucursalesModel(session).obtener_sucursal_por_id(sucursal_id)
                            if sucursal:
                                departamento_actualizado.sucursales.append(sucursal)

                        # Eliminar las sucursales que ya no están seleccionadas
                        for sucursal_id in sucursales_relacionadas - nuevas_sucursales:
                            sucursal = SucursalesModel(session).obtener_sucursal_por_id(sucursal_id)
                            if sucursal:
                                departamento_actualizado.sucursales.remove(sucursal)

            except Exception as e:
                Mensaje().mensaje_critico(f'Error al actualizar el departamento por lo siguiente: {e}')

            self.limpiar()# Confirmar los cambios

    def vincular_sucursal(self):
        sucursal_seleccionada = self.ui.lista_sucursalesexistentes.currentItem()
        if sucursal_seleccionada:
            sucursal_id = sucursal_seleccionada.data(Qt.UserRole)

            if sucursal_id not in self.sucursales_seleccionadas:
                self.sucursales_seleccionadas.add(sucursal_id)
                self.sucursales_seleccionadas_existentes.remove(sucursal_id)

                # Mover a la lista de sucursales vinculadas
                elemento_vinculado = QListWidgetItem(sucursal_seleccionada.text())
                elemento_vinculado.setIcon(self.iconSucursal)
                elemento_vinculado.setData(Qt.UserRole, sucursal_id)

                self.ui.lista_sucursalesvinculadas.addItem(elemento_vinculado)
                self.ui.lista_sucursalesexistentes.takeItem(self.ui.lista_sucursalesexistentes.row(sucursal_seleccionada))

                self.actualizar_sucursales_existentes()

    def desvincular_sucursal(self):
        sucursal_seleccionada = self.ui.lista_sucursalesvinculadas.currentItem()
        if sucursal_seleccionada:
            sucursal_id = sucursal_seleccionada.data(Qt.UserRole)
            
            # Verificar si el ID está en la lista antes de intentar eliminarlo
            if sucursal_id in self.sucursales_seleccionadas:
                self.sucursales_seleccionadas.remove(sucursal_id)
                self.sucursales_seleccionadas_existentes.add(sucursal_id)

                # Devolver a la lista de sucursales existentes
                item_devolver = QListWidgetItem(sucursal_seleccionada.text())
                item_devolver.setIcon(self.iconSucursal)
                item_devolver.setData(Qt.UserRole, sucursal_id)

                self.ui.lista_sucursalesexistentes.addItem(item_devolver)
                self.ui.lista_sucursalesvinculadas.takeItem(self.ui.lista_sucursalesvinculadas.row(sucursal_seleccionada))

                # Actualizar la lista de sucursales existentes
                self.actualizar_sucursales_existentes()
            else:
                Mensaje().mensaje_alerta(f"Sucursal ID {sucursal_id} no encontrado en la lista de seleccionadas.")
        else:
            Mensaje().mensaje_informativo("No se ha seleccionado ninguna sucursal para desvincular.")

    def actualizar_sucursales_existentes(self):
        self.ui.lista_sucursalesexistentes.clear()
        # Filtrar sucursales no vinculadas
        sucursales_vinculadas_ids = self.sucursales_seleccionadas
        
        # Crear un conjunto con los IDs de todas las sucursales
        sucursales_no_vinculadas = [sucursal for sucursal in self.sucursales if sucursal.id not in sucursales_vinculadas_ids]

        for sucursal in sucursales_no_vinculadas:
            item = QListWidgetItem(sucursal.nombre_sucursal)
            item.setIcon(self.iconSucursal)
            item.setData(Qt.UserRole, sucursal.id)
            self.ui.lista_sucursalesexistentes.addItem(item)

    def listar_sucursales_existentes(self, sucursales_vinculadas = set()):
        self.ui.lista_sucursalesexistentes.clear()
        try:
            with Conexion_base_datos() as db:
                session = db.abrir_sesion()
                self.sucursales = SucursalesModel(session).obtener_todo()  # O ajusta esto a tus necesidades
                for sucursal in self.sucursales:
                    if sucursal.id not in sucursales_vinculadas:  # Solo agregar sucursales no vinculadas
                        self.sucursales_seleccionadas_existentes.add(sucursal.id)
                        item = QListWidgetItem(sucursal.nombre_sucursal)
                        item.setIcon(self.iconSucursal)
                        item.setData(Qt.UserRole, sucursal.id)
                        self.ui.lista_sucursalesexistentes.addItem(item)
        except Exception as e:
            Mensaje().mensaje_critico(f'Error al listar sucursales existentes por lo siguiente: {e}')
    
    def obtener_departamentos(self):
        self.ui.lista_departamentosexistentes.clear()
        try:
            with Conexion_base_datos() as db:
                session = db.abrir_sesion()
                try:
                    self.departamentos, estado = DepartamentosModel(session).obtener_todos()
                except Exception as e:
                    Mensaje().mensaje_alerta("Error al obtener departamentos")
                self.listar_departamentos(self.departamentos)
            
        except Exception as e:
            Mensaje().mensaje_critico(f'Error al listar las sucursales : {e}')

    def listar_puestos_asignados(self, puestos):
        if puestos is not None:
            self.ui.lista_puestosasignados.clear()
            for  puesto in puestos:
                # Crear un QListWidgetItem
                item = QListWidgetItem(puesto.nombre)
                
                # Establecer el ícono en el ítem
                item.setIcon(self.iconDepartamento)
                item.setData(Qt.UserRole, puesto.id)
                
                # Agregar el ítem a la lista
                
                self.ui.lista_puestosasignados.addItem(item)
        else:
            self.ui.lista_puestosasignados.clear()


    def listar_departamentos(self, departamentos):
        if departamentos:
                self.ui.lista_departamentosexistentes.clear()
                for  departamento in departamentos:
                    # Crear un QListWidgetItem
                    item = QListWidgetItem(departamento.nombre)
                    
                    # Establecer el ícono en el ítem
                    item.setIcon(self.iconDepartamento)
                    item.setData(Qt.UserRole, departamento.id)
                    
                    # Agregar el ítem a la lista
                    self.ui.lista_departamentosexistentes.addItem(item)
        else:
            self.ui.lista_departamentosexistentes.clear()

    def obtenerId(self, item):
        self.id_departamento = item.data(Qt.UserRole)
        self.ui.lista_sucursalesvinculadas.clear()
        self.sucursales_seleccionadas =  set()
        self.sucursales_seleccionadas_existentes = set()

        
        with Conexion_base_datos() as db:
            session = db.abrir_sesion()
            with session.begin():
                try:
                    departamento = DepartamentosModel(session).obtener_departamento_por_id(self.id_departamento)
                    if departamento:
                        self.ui.txt_nombredepartamento.setText(departamento.nombre)
                        self.ui.txtlargo_descripciondepartamento.setPlainText(departamento.descripcion)

                        # Lista para almacenar IDs de sucursales vinculadas
                        self.sucursales_seleccionadas = {sucursal.id for sucursal in departamento.sucursales}
                        
                        # Actualizar lista de sucursales vinculadas
                        for sucursal in departamento.sucursales:
                            item_vinculado = QListWidgetItem(sucursal.nombre_sucursal)
                            item_vinculado.setIcon(self.iconSucursal)
                            item_vinculado.setData(Qt.UserRole, sucursal.id)
                            self.ui.lista_sucursalesvinculadas.addItem(item_vinculado)
                            
                            if sucursal.id not in self.sucursales_seleccionadas:
                                self.sucursales_seleccionadas.add(sucursal.id)

                            if sucursal.id in self.sucursales_seleccionadas_existentes:
                                self.sucursales_seleccionadas_existentes.remove(sucursal.id)

                        # Actualizar lista de sucursales existentes
                        self.ui.lista_sucursalesexistentes.clear()
                        self.listar_sucursales_existentes(self.sucursales_seleccionadas)
                        self.listar_puestos_asignados(departamento.puestos)

                except Exception as e:
                    Mensaje().mensaje_critico(f'Error al obtener departamento: {e}')
                



    