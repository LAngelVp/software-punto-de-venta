import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from app.View.UserInterfacePy.UI_CONTROL_EMPLEADOS import *
from app.Controller.RegistroInicialController import Registro_personal_inicial
from app.Controller.RolesController import *
from app.DataBase.conexionBD import Conexion_base_datos
from app.Model.EmpleadoModel import EmpleadosModel
from .MensajesAlertasController import Mensaje
from ..Model.ValidacionesModel import Validaciones
from .ComprobarValoresTablasController import Comprobacion
from .Ventana_espera import Modal_de_espera
from .Hilo_consultas import Consultas_segundo_plano

class EmpleadosController(QWidget):
    registro_listar_puestos = pyqtSignal()
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
        if self.cargando is None or not self.cargando.isVisible():
            self.cargando = Modal_de_espera()
            self.cargando.show()
        else:
            self.cargando.raise_()
            self.cargando.activateWindow()
            
        self.consultor = Consultas_segundo_plano()
        self.consultor.terminado.connect(self.cargando_cerrar)
        self.consultor.resultado.connect(self.llenar_tabla)
        self.consultor.ejecutar_hilo(funcion=self.buscar_empleado_query)
        
    def buscar_empleado_query(self, session):
        id_empleado = self.ui.txt_idempleado.text()
        nombre_empleado = self.ui.txt_nombreempleado.text().upper()
        tipo_filtro_nombre = self.ui.cajaopciones_filtroNombreEmpleado.currentIndex()
        empleados, estado = EmpleadosModel(session).filtrar_empleados(id_empleado, nombre_empleado, tipo_filtro_nombre)
        return empleados, estado
                
    def roles(self):
        # self.roles =  Control_rol()
        # self.roles.show()
        pass

    def eliminar_empleado(self):
        if self.id_empleado:
            with Conexion_base_datos() as db:
                session = db.abrir_sesion()
                with session.begin():
                    estado = EmpleadosModel(session).eliminar_empleado(self.id_empleado)
                if estado:
                    Mensaje().mensaje_informativo("Operacion exitosa")
                    # self.listar_empleados()
                return
            
    def editar_empleado_seleccionado(self):
        if self.empleado_actual:
            if self.ventana_registro is None or self.ventana_registro.isVisible():
                self.ventana_registro = Registro_personal_inicial(parent=self)
                self.ventana_registro.obtener_id(self.empleado_actual)
                # self.ventana_registro.registro_agregado_signal.connect(self.listar_empleados)
                self.ventana_registro.VENTANA_REGISTRO_CERRADA.connect(self.ventana_cerrada_nuevo_personal)
                self.ventana_registro.exec_()
            else:
                self.ventana_registro.raise_()
                self.ventana_registro.activateWindow()
        self.id_empleado = None
    
    def listar_empleados(self):
        if self.cargando is None or not self.cargando.isVisible():
            self.cargando = Modal_de_espera()
            self.cargando.show()
        else:
            self.cargando.raise_()
            self.cargando.activateWindow()
            
        self.consultor = Consultas_segundo_plano()
        self.consultor.error.connect(self.mostrar_error)
        self.consultor.terminado.connect(self.cargando_cerrar)
        self.consultor.resultado.connect(self.llenar_tabla)
        self.consultor.ejecutar_hilo(self.obtener_empleados_query)
        
    def mostrar_error(self, error):
        Mensaje().mensaje_alerta(f"Sucedio un error al momento de listar los empleados : {error}")
        return
    
    def obtener_empleados_query(self, session):
        empleados, estado = EmpleadosModel(session).obtener_empleados_detallados()
        return empleados, estado
    
    def llenar_tabla(self, empleados, estado):
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

        self.empleados = empleados  # Guardamos la lista de empleados si la quieres usar en otros métodos

        for empleado in empleados:
            list_items = []

            datos_empleado = [
                str(empleado.id),
                empleado.nombre or '',
                empleado.apellido_paterno or '',
                empleado.apellido_materno or '',
                empleado.fecha_nacimiento.strftime('%Y-%m-%d') if empleado.fecha_nacimiento else '',
                empleado.estado_civil or '',
                empleado.curp or '',
                empleado.rfc or '',
                empleado.nivel_academico or '',
                empleado.carrera or '',
                empleado.correo_electronico or '',
                empleado.numero_seguro_social or '',
                empleado.fecha_contratacion.strftime('%Y-%m-%d') if empleado.fecha_contratacion else '',
                empleado.fecha_despido.strftime('%Y-%m-%d') if empleado.fecha_despido else '',
                empleado.ciudad or '',
                empleado.codigo_postal or '',
                empleado.estado or '',
                empleado.pais or '',
                empleado.numero_telefonico or '',
                empleado.nombre_contacto or '',
                empleado.contacto_emergencia or '',
                empleado.parentesco_contacto or '',
                empleado.calles or '',
                empleado.avenidas or '',
                empleado.num_interior or '',
                empleado.num_exterior or '',
                empleado.direccion_adicional or '',
                str(empleado.activo),
                empleado.puesto.nombre if empleado.puesto else '',
                str(empleado.puesto.salario) if empleado.puesto else '',
                str(empleado.puesto.horas_laborales) if empleado.puesto else '',
                empleado.puesto.dias_laborales if empleado.puesto else '',
                empleado.puesto.hora_entrada.strftime('%H:%M') if empleado.puesto and empleado.puesto.hora_entrada else '',
                empleado.puesto.hora_salida.strftime('%H:%M') if empleado.puesto and empleado.puesto.hora_salida else '',
                empleado.departamento.nombre if empleado.departamento else '',
                empleado.sucursal.nombre_sucursal if empleado.sucursal else '',
            ]

            for idx, valor in enumerate(datos_empleado):
                item = QStandardItem(valor)
                item.setTextAlignment(Qt.AlignCenter)

                # 💡 Guardar el objeto empleado completo en la columna 0 (ID)
                if idx == 0:
                    item.setData(empleado, Qt.UserRole)

                list_items.append(item)

            self.modelo_empleados_vempleados.appendRow(list_items)

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

