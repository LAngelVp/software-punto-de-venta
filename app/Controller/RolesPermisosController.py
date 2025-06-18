from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from ..Model.GruposyPermisosModel import RolesModel
from .MensajesAlertasController import Mensaje
from ..DataBase.conexionBD import Conexion_base_datos
from ..View.UserInterfacePy.UI_CONTROL_ROLES import Ui_Control_Roles_Permisos


class ControlRolesController(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Control_Roles_Permisos()
        self.ui.setupUi(self)
        #// MOSTRAR VENTANA EN EL CENTRO DE LA PANTALLA
        pantalla = self.frameGeometry()
        pantalla.moveCenter(self.screen().availableGeometry().center())
        self.move(pantalla.topLeft())
        #//LIMITE CARACTERES
        self.ui.txt_nombrerol.setMaxLength(100)
        #-------------------
        #// VARIABLES
        self.permisos = []
        self.seleccion_conectada_tabla = None
        self.registro_seleccionado = None
        self.rol_seleccinado= None
        #-----------------
        # SEÑALES: BOTONES
        self.ui.btn_btn_agregar.clicked.connect(self.agregar_roles_al_sistema)
        self.ui.btn_btn_buscar.clicked.connect(self.buscar_roles_del_sistema)
        self.ui.btn_btn_eliminarrol.clicked.connect(self.eliminar_rol_del_sistema)
        self.ui.btn_btn_modificarrol.clicked.connect(self.modificar_rol_del_sistema)
        #--------------------
        self.mostrar_roles_existentes()

        #COMMENT: RECORRER LOS ATRIBUTOS DE LA VENTANA QUE COMIENZAN CON "OPCION_"
        for atributo in dir(self.ui):
            if atributo.startswith('opcion_'):
                caja = getattr(self.ui, atributo)
                caja.stateChanged.connect(self.comprobar_caja_verificacion)  # COMMENTLINE: AL DAR CLIC, SE EJECUTA EL METODO

    def comprobar_caja_verificacion(self, state):
        sender = self.sender()
        verificacion = sender.objectName()
        if state == Qt.Checked:
            if verificacion not in self.permisos:
                self.permisos.append(verificacion.split('_')[1]) #COMMENTLINE: OBTIENE EL TEXTO VISIBLE DEL ELEMENTO, PERO LO QUE ESTA DESPUES DEL _
        else:
            if verificacion in self.permisos:
                self.permisos.remove(verificacion[1]) #COMMENTLINE: AL DESACTIVAR EL ELEMENTO, LO ELIMINA DE LA LISTA.
                
    def agregar_roles_al_sistema(self):
        nombre = self.ui.txt_nombrerol.text().strip().upper()
        descripcion = self.ui.txt_descripcionrol.text().strip().upper()
        if len(self.permisos) == 0:
            Mensaje().mensaje_informativo("Para que puedar almacenar un nuevo rol de usuario, debes de seleccionar por lo menos una familia de permisos.")
            return
        permisos_mayusculas = [permiso.upper() for permiso in self.permisos]
        with Conexion_base_datos() as db:
            session = db.abrir_sesion()
            with session.begin():
                rol, status_rol = RolesModel(session).crear_Rol(nombre=nombre, descripcion=descripcion, permisos=permisos_mayusculas)
        if not status_rol:
            Mensaje().mensaje_alerta("No se logro crear el rol")
            return
        Mensaje().mensaje_informativo("Rol Creado")
        self.mostrar_roles_existentes()
        return
    
    def mostrar_roles_existentes(self):
        with Conexion_base_datos() as db:
            session = db.abrir_sesion()
            with session.begin():
                lista_roles, status_lista_roles = RolesModel(session).todos_roles_con_permisos()
                if not status_lista_roles:
                    return
                print(lista_roles)
                self.mostrar_roles_en_tabla(lista_roles)
    
    def buscar_roles_del_sistema(self):
        pass
    
    def modificar_rol_del_sistema(self):
        pass
    
    # REVIEW
    def mostrar_roles_en_tabla(self, lista_elementos = None):
        if not lista_elementos:  # Verificar si la lista está vacía o es None
            return

        # Si no existe el modelo, lo creamos, sino lo limpiamos
        if not hasattr(self, 'modelo_lista_roles'):
            self.modelo_lista_roles = QStandardItemModel()
        else:
            self.modelo_lista_roles.clear()  # Limpiar el modelo si ya existe

        # Establecer los encabezados de las columnas
        self.modelo_lista_roles.setHorizontalHeaderLabels(["Id", "Nombre", "Descripción", "Permiso"])

        # Recorrer los roles y permisos y agregar cada uno como una fila en el modelo
        for rol, permiso in lista_elementos:  # Aquí 'lista_elementos' es una lista de tuplas (rol, permiso)
            if rol is not None:
                # Preparar los datos de la fila
                row_data = [
                    str(rol.id),  # Id del rol
                    rol.nombre,  # Nombre del rol
                    rol.descripcion if rol.descripcion else "No disponible",  # Descripción del rol
                    permiso.nombre if permiso else "Sin permiso"  # Nombre del permiso (si existe)
                ]

                # Crear los elementos de la fila para la tabla
                items = [QStandardItem(item) for item in row_data]

                # Asociar el rol y permiso con cada item para poder acceder a los objetos más tarde
                for item in items:
                    item.setData((rol, permiso), Qt.UserRole)

                # Añadir la fila al modelo
                self.modelo_lista_roles.appendRow(items)

        # Asignar el modelo al QTableView solo una vez, después de llenar el modelo
        self.ui.tabla_listaroles.setModel(self.modelo_lista_roles)
        
        # Desconectar la señal antes de conectar
        if self.seleccion_conectada_tabla:
            self.ui.tabla_listaroles.selectionModel().currentChanged.disconnect(self.seleccion_elemento_tabla_roles)
            self.seleccion_conectada_tabla = False  # Actualizar el estado

        # Conectar la señal a la función que obtiene el ID del elemento seleccionado
        self.ui.tabla_listaroles.selectionModel().currentChanged.connect(self.seleccion_elemento_tabla_roles)
        self.seleccion_conectada_tabla = True  # Marcar como conectada
        
    def seleccion_elemento_tabla_roles(self, current, previus):
        if current.column() >= 0:  # Verifica si es la primera columna
            indice_fila = current.row()
            elemento = self.modelo_lista_roles.item(indice_fila, 0)
            if elemento is not None:
                item = elemento.data(Qt.UserRole)
                if item:
                    self.registro_seleccionado = elemento.text()
            else:
                return
            
    def eliminar_rol_del_sistema(self):
        if self.registro_seleccionado is None:
            Mensaje().mensaje_informativo("Debes de seleccionar un registro para poder ejecutar la función de eliminar.")
            return
        
        with Conexion_base_datos() as db:
            session = db.abrir_sesion()
            with session.begin():
                status_rol_eliminado = RolesModel(session).eliminar_rol_con_permisos(id=self.registro_seleccionado)
                
                # Verifica el estado de la eliminación
                if not status_rol_eliminado:
                    Mensaje().mensaje_alerta("No se logró eliminar el registro de la base de datos.")
                    return
                
                # Mensaje informativo de eliminación exitosa
                Mensaje().mensaje_informativo("Se eliminó el rol de la base de datos de forma correcta.")
        self.mostrar_roles_existentes()  # Actualizamos la tabla