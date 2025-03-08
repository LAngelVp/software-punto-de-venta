from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
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
        #-------------------
        #// VARIABLES
        self.permisos = []
        #-----------------
        # SEÑALES: BOTONES
        self.ui.btn_btn_agregar.clicked.connect(self.agregar_roles_al_sistema)
        self.ui.btn_btn_buscar.clicked.connect(self.buscar_roles_del_sistema)
        self.ui.btn_btn_eliminarrol.clicked.connect(self.eliminar_rol_del_sistema)
        self.ui.btn_btn_modificarrol.clicked.connect(self.modificar_rol_del_sistema)
        #--------------------

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
        nombre = self.ui.txt_nombrerol_2.text().strip().upper()
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
    
    def buscar_roles_del_sistema(self):
        pass
    
    def eliminar_rol_del_sistema(self):
        pass
    
    def modificar_rol_del_sistema(self):
        pass