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

class EmpleadosController(QWidget):
    registro_listar_puestos = pyqtSignal()
    def __init__(self):
        super().__init__()
        self.ui = Ui_Control_empleados()
        self.ui.setupUi(self)
        self.ui.txt_idempleado.setValidator(Validaciones().get_int_validator)
        self.ui.btn_btn_agregar.clicked.connect(self.agregar_empleado)
        self.ui.btn_btn_buscar.clicked.connect(self.buscar_empleado)
        self.ui.btn_btn_limpiar.clicked.connect(self.limpiar)
        self.ui.btn_btn_eliminar.clicked.connect(self.eliminar_empleado)
        self.ui.btn_btn_editarempleado.clicked.connect(self.editar_empleado_seleccionado)
        
        # SEÑALES: LISTAR PUESTOS EN EL REGISTRO INICIAL
        # self.ventana = 
        self.registro_listar_puestos.connect(Registro_personal_inicial().listar_puestos)

        self.seleccion_conectada = None
        self.id_empleado = None
        self.empleados = None

        self.listar_empleados()

    def limpiar(self):
        self.ui.txt_idempleado.clear()
        self.ui.txt_nombreempleado.clear()
        self.listar_empleados()
        
    def buscar_empleado(self):
        id_empleado = self.ui.txt_idempleado.text()
        nombre_empleado = self.ui.txt_nombreempleado.text()
        if not id_empleado and not nombre_empleado:
            Mensaje().mensaje_informativo("Para buscar a un empleado es necesario ingresar su ID o NOMBRE")
            return
        if id_empleado:
            id_empleado = int(id_empleado)
        with Conexion_base_datos() as db:
            session = db.abrir_sesion()
            with session.begin():
                empleados, estado = EmpleadosModel(session).filtrar_empleados(id_empleado, nombre_empleado)
            if estado:
                self.llenar_tabla(empleados)
                
    def roles(self):
        self.roles =  Control_rol()
        self.roles.show()

    def agregar_empleado(self):
        self.ventana = Registro_personal_inicial()
        self.registro_listar_puestos.emit()
        self.ventana.registro_agregado_signal.connect(self.listar_empleados)
        self.ventana.show()

    def eliminar_empleado(self):
        if self.id_empleado:
            with Conexion_base_datos() as db:
                session = db.abrir_sesion()
                with session.begin():
                    estado = EmpleadosModel(session).eliminar_empleado(self.id_empleado)
                if estado:
                    self.listar_empleados()
                return
            
    def editar_empleado_seleccionado(self):
        if self.id_empleado:
            id = int(self.id_empleado)
            self.ventana = Registro_personal_inicial()
            self.ventana.obtener_id(self.id_empleado)
            self.ventana.registro_agregado_signal.connect(self.listar_empleados)
            self.ventana.show()
            self.id_empleado = None
    
    def listar_empleados(self):
        with Conexion_base_datos() as db:
            session = db.abrir_sesion()
            with session.begin():
                try:
                    self.empleados, estado = EmpleadosModel(session).obtener_empleados_detallados()
                except Exception as e:
                    print(e)
            self.llenar_tabla(self.empleados)

    def llenar_tabla(self, empleados):
        try:
            # Verificar si la tabla está inicializada
            if self.ui.tabla_listaempleados is None:
                print("El widget tabla_puestos no está disponible.")
                return

            # Inicializar el modelo de la tabla si no existe
            if not hasattr(self, 'model'):
                self.model = QStandardItemModel()
                
            # Limpiar el modelo antes de llenarlo con nuevos datos
            self.model.clear()
            # Verificar si clientes es None o una lista vacía
            if empleados is None or len(empleados) == 0:
                self.model.setHorizontalHeaderLabels([
                    "id", "nombre", "apellido_paterno", "apellido_materno", "fecha_nacimiento", "estado_civil", "curp", "rfc", "nivel_academico", "carrera", "correo_electronico", "numero_seguro_social", "fecha_contratacion", "fecha_despido", "ciudad", "codigo_postal", "estado", "pais", "numero_telefonico", "nombre_contacto", "contacto_emergencia", "parentesco_contacto", "calles", "avenidas", "num_interior", "num_exterior", "direccion_adicional", "activo"
                    ])
                self.ui.tabla_listaempleados.setModel(self.model)
                return

            nombre_columnas = [
                "id", "nombre", "apellido_paterno", "apellido_materno", "fecha_nacimiento", "estado_civil",
                "curp", "rfc", "nivel_academico", "carrera", "correo_electronico", "numero_seguro_social",
                "fecha_contratacion", "fecha_despido", "ciudad", "codigo_postal", "estado", "pais",
                "numero_telefonico", "nombre_contacto", "contacto_emergencia", "parentesco_contacto",
                "calles", "avenidas", "num_interior", "num_exterior", "direccion_adicional", "activo",
                "nombre_puesto", "salario", "horas_laborales", "dias_laborales",
                "hora_entrada", "hora_salida", "nombre_departamento", "nombre_sucursal"
            ]
            self.model.setHorizontalHeaderLabels(nombre_columnas)

            # Llenar el modelo con datos de clientes
            for empleado in empleados:
                if empleado is not None:
                    row_data = [
                        str(empleado.id),  # ID del empleado
                        empleado.nombre,  # Nombre del empleado
                        empleado.apellido_paterno,  # Apellido paterno
                        empleado.apellido_materno,  # Apellido materno
                        empleado.fecha_nacimiento.strftime('%Y-%m-%d'),  # Fecha de nacimiento
                        empleado.estado_civil,  # Estado civil
                        empleado.curp,  # CURP
                        empleado.rfc,  # RFC
                        empleado.nivel_academico,  # Nivel académico
                        empleado.carrera,  # Carrera
                        empleado.correo_electronico,  # Correo electrónico
                        empleado.numero_seguro_social,  # Número de seguro social
                        empleado.fecha_contratacion.strftime('%Y-%m-%d') if empleado.fecha_contratacion else '',  # Fecha de contratación
                        empleado.fecha_despido.strftime('%Y-%m-%d') if empleado.fecha_despido else '',  # Fecha de despido
                        empleado.ciudad,  # Ciudad
                        empleado.codigo_postal,  # Código postal
                        empleado.estado,  # Estado
                        empleado.pais,  # País
                        empleado.numero_telefonico,  # Número telefónico
                        empleado.nombre_contacto,  # Nombre de contacto
                        empleado.contacto_emergencia,  # Contacto de emergencia
                        empleado.parentesco_contacto,  # Parentesco de contacto
                        empleado.calles,  # Calles
                        empleado.avenidas,  # Avenidas
                        empleado.num_interior,  # Número interior
                        empleado.num_exterior,  # Número exterior
                        empleado.direccion_adicional,  # Dirección adicional
                        str(empleado.activo),  # Estado activo
                        empleado.puesto.nombre if empleado.puesto else '',  # Nombre del puesto
                        str(empleado.puesto.salario) if empleado.puesto else '',  # Salario
                        str(empleado.puesto.horas_laborales) if empleado.puesto else '',  # Horas laborales
                        empleado.puesto.dias_laborales if empleado.puesto else '',  # Días laborales
                        empleado.puesto.hora_entrada.strftime('%H:%M') if empleado.puesto else '',  # Hora de entrada
                        empleado.puesto.hora_salida.strftime('%H:%M')  if empleado.puesto else '',  # Hora de salida
                        empleado.departamento.nombre if empleado.departamento else '',  # Nombre del departamento
                        empleado.sucursal.nombre_sucursal if empleado.sucursal else '',  # Nombre de la sucursal
                    ]
                else:
                    # Usar campos vacíos si no hay datos de cliente físico
                    row_data = [""] * len(nombre_columnas)

                items = [QStandardItem(str(item)) for item in row_data]
                self.model.appendRow(items)

            # Asignar el modelo a la tabla
            self.ui.tabla_listaempleados.setModel(self.model)
            # self.ui.tabla_listaempleados.setColumnHidden(0, True)

            # Desconectar la señal antes de conectar
            if self.seleccion_conectada:
                self.ui.tabla_listaempleados.selectionModel().currentChanged.disconnect(self.obtener_id_elemento_tabla)
                self.seleccion_conectada = False  # Actualizar el estado

            # Conectar la señal a la función que obtiene el ID del elemento seleccionado
            self.ui.tabla_listaempleados.selectionModel().currentChanged.connect(self.obtener_id_elemento_tabla)
            self.seleccion_conectada = True  # Marcar como conectada
        except Exception as e:
            print(f'No se logro hacer mostrar la tabla EMPLEADOS {e}')
        self.id_empleado = None

    def obtener_id_elemento_tabla(self, current, previus):
        if current.column() >= 0:
            indice_fila = current.row()
            self.id_empleado = self.model.item(indice_fila, 0).text()

    def obtencion_segura(atributo, default='Sin dato'):
        """Función auxiliar para obtener atributos de manera segura."""
        return atributo if atributo is not None else default

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = EmpleadosController()
    ui.show()
    sys.exit(app.exec())