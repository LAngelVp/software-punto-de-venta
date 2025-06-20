import sys
from PySide6 import QtCore, QtWidgets
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from app.View.UserInterfacePy.UI_CONTROL_EMPLEADOS import *
from app.Controller.RegistroInicialController import Registro_personal_inicial
from app.Controller.RolesController import *
from app.DataBase.conexionBD import Conexion_base_datos
from app.Model.EmpleadoModel import EmpleadosModel
from .MensajesAlertasController import Mensaje
from .Validaciones import Validaciones
from .ComprobarValoresTablasController import Comprobacion
from .Ventana_espera import Modal_de_espera
from .Hilo_consultas import Consultas_segundo_plano

class EmpleadosController(QWidget):
    registro_listar_puestos = Signal()
    def __init__(self, parent = None):
        super().__init__(parent)
        self.ui = Ui_Control_empleados()
        self.ui.setupUi(self)
        self.ventana_registro = None
        self.ventana_registro_cerrada = False
        self.seleccion_conectada_empleados = None
        self.id_empleado = None
        self.empleados = None
        self.cargando = None
        self.consultor = None
        self.empleado_actual = None
        
        
        self.ui.txt_idempleado.setValidator(Validaciones().get_int_validator)
        self.ui.btn_btn_agregar.clicked.connect(self.agregar_empleado)
        self.ui.btn_btn_buscar.clicked.connect(self.buscar_empleado)
        self.ui.btn_RefrescarTabla.clicked.connect(self.limpiar)
        self.ui.btn_btn_eliminar.clicked.connect(self.eliminar_empleado)
        self.ui.btn_btn_editarempleado.clicked.connect(self.editar_empleado_seleccionado)
        self.ui.btn_RefrescarTabla.clicked.connect(self.listar_empleados)
        
        # SEÑALES: LISTAR PUESTOS EN EL REGISTRO INICIAL
        # self.ventana = 
        self.registro_listar_puestos.connect(Registro_personal_inicial().listar_puestos)

    def cargando_cerrar(self):
        if self.cargando is not None:
            self.cargando.close()
            self.cargando = None
            
    def ventana_cerrada_nuevo_personal(self):
        self.ventana_registro = None
        self.empleado_actual = None
        
    def agregar_empleado(self):
        if self.ventana_registro is None or self.ventana_registro.isVisible():
            self.ventana_registro = Registro_personal_inicial(parent=self)
            # self.ventana_registro.registro_agregado_signal.connect(self.listar_empleados)
            self.ventana_registro.VENTANA_REGISTRO_CERRADA.connect(self.ventana_cerrada_nuevo_personal)
            self.registro_listar_puestos.emit()
            self.ventana_registro.show()
        else:
            self.ventana_registro.raise_()
            self.ventana_registro.activateWindow()

    def limpiar(self):
        self.ui.txt_idempleado.clear()
        self.ui.txt_nombreempleado.clear()
        self.listar_empleados()
        
    def buscar_empleado(self):
        id_empleado = self.ui.txt_idempleado.text().strip()
        if id_empleado.isdigit():
            id_empleado = int(id_empleado)
        else:
            id_empleado = None
        nombre_empleado = self.ui.txt_nombreempleado.text().strip()
        tipo_filtro_nombre = self.ui.cajaOpciones_filtroNombreEmpleado.currentIndex()
        if not id_empleado and not nombre_empleado:
            Mensaje().mensaje_informativo("No haz ingresado datos para filtrar")
            return
        self.mostrar_modal_local()
        self.consultor = Consultas_segundo_plano()
        self.consultor.terminado.connect(self.cargando_cerrar)
        self.consultor.resultado.connect(self.llenar_tabla_empleados)
        self.consultor.ejecutar_hilo(
            funcion=self.buscar_empleado_query,
            id_empleado=id_empleado,
            nombre_empleado=nombre_empleado,
            tipo_filtro_nombre=tipo_filtro_nombre
        )
        
    def buscar_empleado_query(self, session, id_empleado, nombre_empleado, tipo_filtro_nombre):
        empleados, estado = EmpleadosModel(session).filtrar_empleados(id_empleado, nombre_empleado, tipo_filtro_nombre)
        return empleados, estado
                
    def roles(self):
        # self.roles =  Control_rol()
        # self.roles.show()
        pass

    def eliminar_empleado(self):
        if not self.empleado_actual:
            Mensaje().mensaje_informativo("No haz seleccionado un empleado")
            return
        print(self.empleado_actual.id)
        self.mostrar_modal_local()
        self.consultor = Consultas_segundo_plano()
        self.consultor.terminado.connect(self.cargando_cerrar)
        self.consultor.resultado.connect(self.mensaje_estado_eliminado)
        self.consultor.error.connect(self.mostrar_error)
        self.consultor.ejecutar_hilo(
            funcion=self.eliminar_empleado_query,
            id_empleado=self.empleado_actual.id,
        )
        
    def eliminar_empleado_query(self, session, id_empleado):
        empleado, estado = EmpleadosModel(session).eliminar_empleado(id_empleado)
        if estado:
            session.commit()
        return empleado, estado
    
    def mensaje_estado_eliminado(self, datos, estado):
        if estado:
            Mensaje().mensaje_informativo("Registro eliminado")
        else:
            Mensaje().mensaje_informativo("No se logro eliminar el registro")
        self.empleado_actual = None

    def editar_empleado_seleccionado(self):
        if not self.empleado_actual:
            Mensaje().mensaje_informativo("No haz seleccionado un empleado")
            return
        if self.ventana_registro is None or self.ventana_registro.isVisible():
            self.ventana_registro = Registro_personal_inicial(parent=self)
            self.ventana_registro.obtener_empleado(self.empleado_actual)
            self.ventana_registro.VENTANA_REGISTRO_CERRADA.connect(self.ventana_cerrada_nuevo_personal)
            self.ventana_registro.exec_()
        else:
            self.ventana_registro.raise_()
            self.ventana_registro.activateWindow()
    
    def listar_empleados(self):
        self.mostrar_modal_local()
        self.consultor = Consultas_segundo_plano()
        self.consultor.error.connect(self.mostrar_error)
        self.consultor.terminado.connect(self.cargando_cerrar)
        self.consultor.resultado.connect(self.llenar_tabla_empleados)
        self.consultor.ejecutar_hilo(self.obtener_empleados_query)
        
    def mostrar_error(self, error):
        Mensaje().mensaje_alerta(f"Sucedio un error al momento de listar los empleados : {error}")
        return
    
    def obtener_empleados_query(self, session):
        empleados, estado = EmpleadosModel(session).obtener_empleados_detallados()
        return empleados, estado

    def llenar_tabla_empleados(self, empleados, estado):
        if self.ui.tabla_listaempleados is None:
            Mensaje().mensaje_alerta("El widget tabla_listaempleados no está disponible.")
            return

        if not hasattr(self, 'modelo_empleados_vempleados'):
            self.modelo_empleados_vempleados = QStandardItemModel()

        self.modelo_empleados_vempleados.clear()

        cabeceras = [
            "ID", "Nombre", "Apellido Paterno", "Apellido Materno", "Fecha Nacimiento", "Estado Civil",
            "CURP", "RFC", "Nivel Académico", "Carrera", "Correo Electrónico", "Número Seguro Social",
            "Fecha Contratación", "Fecha Despido", "Ciudad", "Código Postal", "Estado", "País",
            "Número Telefónico", "Nombre Contacto", "Contacto Emergencia", "Parentesco Contacto",
            "Calles", "Avenidas", "Num Interior", "Num Exterior", "Dirección Adicional", "Activo",
            "Puesto", "Salario", "Horas Laborales", "Días Laborales",
            "Hora Entrada", "Hora Salida", "Departamento", "Sucursal"
        ]

        self.modelo_empleados_vempleados.setHorizontalHeaderLabels(cabeceras)

        if not estado or not empleados:
            Mensaje().mensaje_informativo("No hay empleados para mostrar")
            self.ui.tabla_listaempleados.setModel(self.modelo_empleados_vempleados)
            return

        self.empleados = empleados

        campos_extras = {
            "Puesto": lambda e: e.puesto.nombre if e.puesto else '',
            "Salario": lambda e: e.puesto.salario if e.puesto else '',
            "Horas Laborales": lambda e: e.puesto.horas_laborales if e.puesto else '',
            "Días Laborales": lambda e: e.puesto.dias_laborales if e.puesto else '',
            "Hora Entrada": lambda e: e.puesto.hora_entrada if e.puesto else '',
            "Hora Salida": lambda e: e.puesto.hora_salida if e.puesto else '',
            "Departamento": lambda e: e.departamento.nombre if e.departamento else '',
            "Sucursal": lambda e: e.sucursal.nombre_sucursal if e.sucursal else '',
        }

        for empleado in empleados:
            fila = []
            for col in cabeceras:
                valor = campos_extras[col](empleado) if col in campos_extras \
                    else getattr(empleado, col.lower().replace(" ", "_"), '')
                item = QStandardItem(str(valor))
                item.setTextAlignment(Qt.AlignCenter)
                if col == "ID":
                    item.setData(empleado, Qt.UserRole)
                fila.append(item)

            self.modelo_empleados_vempleados.appendRow(fila)

        self.ui.tabla_listaempleados.setModel(self.modelo_empleados_vempleados)
        self.ui.tabla_listaempleados.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.tabla_listaempleados.resizeColumnsToContents()

        if self.seleccion_conectada_empleados:
            self.ui.tabla_listaempleados.clicked.disconnect(self.obtener_id_elemento_tabla_empleados)
            self.seleccion_conectada_empleados = False

        self.ui.tabla_listaempleados.clicked.connect(self.obtener_id_elemento_tabla_empleados)
        self.seleccion_conectada_empleados = True

    def obtener_id_elemento_tabla_empleados(self, current, previus = None):
        if current.isValid():
            fila = current.row()
            item = self.modelo_empleados_vempleados.item(fila, 0)  # columna 0 = ID (donde guardamos el objeto)
            if item:
                empleado = item.data(Qt.UserRole)
                if empleado:
                    self.empleado_actual = empleado

    def obtencion_segura(atributo, default='Sin dato'):
        """Función auxiliar para obtener atributos de manera segura."""
        return atributo if atributo is not None else default

    def mostrar_modal_local(self):
        if self.cargando is None or not self.cargando.isVisible():
            self.cargando = Modal_de_espera(self)
            self.cargando.show()
        else:
            self.cargando.raise_()
            self.cargando.activateWindow()