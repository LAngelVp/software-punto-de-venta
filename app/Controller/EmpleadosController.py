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
# from ...RegistroInicialController import *


class EmpleadosController(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Control_empleados()
        self.ui.setupUi(self)
        self.ui.btn_btn_agregar.clicked.connect(self.agregar_empleado)

        self.seleccion_conectada = None
        # self.empleados = None

        self.listar_empleados()
    
    def roles(self):
        self.roles =  Control_rol()
        self.roles.show()

    def agregar_empleado(self):
        self.ventana = Registro_personal_inicial()
        self.ventana.registro_agregado_signal.connect(self.listar_empleados)
        self.ventana.show()


    def listar_empleados(self):
        with Conexion_base_datos() as db:
            session = db.abrir_sesion()
            with session.begin():
                try:
                    self.empleados, estado = EmpleadosModel(session).obtener_empleados_detallados()
                    if estado == True:
                        print("hay empleados")
                        for i in self.empleados:
                            print(i.nombre)
                        self.llenar_tabla(self.empleados)
                            
                    if estado == False:
                        print("no hay empleados")
                except Exception as e:
                    print(e)

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
                print("No se recibieron datos de empleados o la lista está vacía.")
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
                        empleado.fecha_contratacion.strftime('%Y-%m-%d'),  # Fecha de contratación
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
                        empleado.puesto.nombre,  # Nombre del puesto
                        str(empleado.puesto.salario),  # Salario
                        str(empleado.puesto.horas_laborales),  # Horas laborales
                        empleado.puesto.dias_laborales,  # Días laborales
                        empleado.puesto.hora_entrada.strftime('%H:%M') if empleado.puesto.hora_entrada else '',  # Hora de entrada
                        empleado.puesto.hora_salida.strftime('%H:%M') if empleado.puesto.hora_salida else '',  # Hora de salida
                        empleado.departamento.nombre,  # Nombre del departamento
                        empleado.sucursal.nombre_sucursal if empleado.sucursal else '',  # Nombre de la sucursal
                    ]
                else:
                    # Usar campos vacíos si no hay datos de cliente físico
                    row_data = [""] * len(nombre_columnas)

                items = [QStandardItem(str(item)) for item in row_data]
                self.model.appendRow(items)

            # Asignar el modelo a la tabla
            self.ui.tabla_listaempleados.setModel(self.model)
            self.ui.tabla_listaempleados.setColumnHidden(0, True)

            # Desconectar la señal antes de conectar
            if self.seleccion_conectada:
                self.ui.tabla_listaempleados.selectionModel().currentChanged.disconnect(self.obtener_id_elemento_tabla)
                self.seleccion_conectada = False  # Actualizar el estado

            # Conectar la señal a la función que obtiene el ID del elemento seleccionado
            self.ui.tabla_listaempleados.selectionModel().currentChanged.connect(self.obtener_id_elemento_tabla)
            self.seleccion_conectada = True  # Marcar como conectada
        except Exception as e:
            print(f'No se logro hacer mostrar la tabla {e}')

        self.empleados = None

    def obtener_id_elemento_tabla(self):
        pass

    def obtencion_segura(atributo, default='Sin dato'):
        """Función auxiliar para obtener atributos de manera segura."""
        return atributo if atributo is not None else default


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = EmpleadosController()
    ui.show()
    sys.exit(app.exec())