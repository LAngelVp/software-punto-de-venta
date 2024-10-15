from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from .MensajesAlertasController import Mensaje
from ..DataBase.conexionBD import Conexion_base_datos
from ..View.UserInterfacePy.UI_ADMINISTRAR_PUESTOS import Ui_Formulario_puestos
from ..Model.PuestoModel import PuestoModel
from ..Model.DepartamentosModel import DepartamentosModel


class PuestosController(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Formulario_puestos()
        self.ui.setupUi(self)

        #//: EDICION
        self.ui.decimal_salario.setButtonSymbols(QSpinBox.NoButtons)
        self.ui.decimal_horaslaborales.setButtonSymbols(QSpinBox.NoButtons)
        self.ui.tiempo_horaentrada.setButtonSymbols(QSpinBox.NoButtons)
        self.ui.tiempo_horasalida.setButtonSymbols(QSpinBox.NoButtons)

        #botones:
        self.ui.btn_btn_agregar.clicked.connect(self.agregar)
        self.ui.btn_btn_eliminar.clicked.connect(self.eliminar)
        self.ui.btn_btn_buscarpuesto.clicked.connect(self.buscar_puesto)
        self.ui.btn_btn_limpiar.clicked.connect(self.limpiar)

        # señales principales: 
        self.ui.cajaopcion_lunes.stateChanged.connect(self.comprobar_caja_verificacion)
        self.ui.cajaopcion_martes.stateChanged.connect(self.comprobar_caja_verificacion)
        self.ui.cajaopcion_miercoles.stateChanged.connect(self.comprobar_caja_verificacion)
        self.ui.cajaopcion_jueves.stateChanged.connect(self.comprobar_caja_verificacion)
        self.ui.cajaopcion_viernes.stateChanged.connect(self.comprobar_caja_verificacion)
        self.ui.cajaopcion_sabado.stateChanged.connect(self.comprobar_caja_verificacion)
        self.ui.cajaopcion_domingo.stateChanged.connect(self.comprobar_caja_verificacion)

        # // variables globales:
        self.diasLaborales = []
        self.diccionario_departamentos = set()
        self.diccionario_puestos = set()
        self.id_departamento = None


    #funciones:
    def comprobar_caja_verificacion(self, state):
        sender = self.sender()
        if state == Qt.Checked:
            if sender.text() not in self.diasLaborales:
                self.diasLaborales.append(sender.text())
        else:
            if sender.text() in self.diasLaborales:
                self.diasLaborales.remove(sender.text())

    def limpiar(self):
        for cajaVerificacion in self.findChildren(QCheckBox):
            cajaVerificacion.setChecked(False)
        
        for tiempo in self.findChildren(QTimeEdit):
            tiempo.setTime(QTime(0,0))
        
        for cajaTexto in self.findChildren(QLineEdit):
            cajaTexto.clear()
        
        for cajaDecimal in self.findChildren(QDoubleSpinBox):
            cajaDecimal.setValue(0)
        

    def agregar(self):
        diasLaborales = ', '.join(self.diasLaborales)
        datos = self.obtener_contenido_campos()

        departamento_seleccionado = self.ui.cajaopciones_departamentos.currentText()
        
        if self.diccionario_departamentos:
            for index, nombre in self.diccionario_departamentos.items():
                if nombre == departamento_seleccionado:
                    self.id_departamento = index
                    break
        if not self.validar(datos):
            print ("No se agregaron los campos")
            return
        
        with Conexion_base_datos() as db:
            session = db.abrir_sesion()
            with session.begin():
                try:
                    puesto, agregado = PuestoModel(session).crear_puesto(
                        nombre=datos['nombre'],
                        salario=datos['salario'],
                        horas_laborales=datos['horas_laborales'],
                        dias_laborales=diasLaborales,
                        descripcion_puesto=datos['descripcion_puesto'],
                        hora_entrada=datos['hora_entrada'],
                        hora_salida=datos['hora_salida'],
                        departamento_id=self.id_departamento
                    )
                    if agregado == True:
                        Mensaje().mensaje_informativo("Se registro con exito")
                    else:
                        Mensaje().mensaje_advertencia("No se pudo registrar")
                except Exception as e:
                    Mensaje().mensaje_critico(f'Surgio un error : {e}')
    
    def eliminar(self):
        pass

    def buscar_puesto(self):
        pass

    def listar_departamentos(self):
        try:
            with Conexion_base_datos() as db:
                session = db.abrir_sesion()
                with session.begin():
                    departamentos = DepartamentosModel(session).obtener_todos()
                    if departamentos is not None:
                        self.diccionario_departamentos = {
                            depa.id: depa.nombre for depa in departamentos
                        }
                        print(self.diccionario_departamentos)
                        self.ui.cajaopciones_departamentos.clear()
                        self.ui.cajaopciones_departamentos.addItems(self.diccionario_departamentos.values())

        except Exception as e:
            print(e)

    def listar_puestos(self):
        try:
            with Conexion_base_datos() as db:
                session = db.abrir_sesion()
                with session.begin():
                    puestos = PuestoModel(session).obtener_todos()
                    if puestos is not None:
                        self.llenar_tabla_clientes(puestos)
                        print(self.diccionario_puestos)

        except Exception as e:
            print(e)

    def llenar_tabla_clientes(self, puestos):
        try:
            # Verificar si la tabla está inicializada
            if self.ui.tabla_listapuestos is None:
                print("El widget tabla_puestos no está disponible.")
                return

            # Inicializar el modelo de la tabla si no existe
            if not hasattr(self, 'model'):
                self.model = QStandardItemModel()

            
            
            # Limpiar el modelo antes de llenarlo con nuevos datos
            self.model.clear()
            # Verificar si clientes es None o una lista vacía
            if puestos is None or len(puestos) == 0:
                self.model.setHorizontalHeaderLabels([
                    "Id",
                    "Nombre",
                    "Salario",
                    "Horas Laborales",
                    "Dias Laborales",
                    "Descripcion",
                    "Hora de Entrada",
                    "Hora de Salida"
                    ])
                self.ui.tabla_listapuestos.setModel(self.model) 
                print("No se recibieron datos de clientes o la lista está vacía.")
                return
            
            nombre_columnas = [
                "Id",
                "Nombre",
                "Salario",
                "Horas Laborales",
                "Dias Laborales",
                "Descripcion",
                "Hora de Entrada",
                "Hora de Salida"
            ]
            self.model.setHorizontalHeaderLabels(nombre_columnas)
            
            # Llenar el modelo con datos de clientes
            for puesto in puestos:
                if puesto is not None:
                    row_data = [
                        str(puesto.id),
                        puesto.nombre,
                        str(puesto.salario),
                        str(puesto.horas_laborales),
                        puesto.dias_laborales,
                        puesto.descripcion_puesto,
                        puesto.hora_entrada,
                        puesto.hora_salida
                    ]
                else:
                    # Usar campos vacíos si no hay datos de cliente físico
                    row_data = [""] * len(nombre_columnas)

                items = [QStandardItem(str(item)) for item in row_data]
                self.model.appendRow(items)

            # Asignar el modelo a la tabla
            self.ui.tabla_listapuestos.setModel(self.model)
            self.ui.tabla_listapuestos.setColumnHidden(0, True)

        except Exception as e:
            print(e)
            print(f'No se logro hacer mostrar la tabla {e}')

        self.ui.tabla_clientes.selectionModel().currentChanged.connect(self.obtener_id_elemento_tabla)
        self.clientes = None

    def campos(self):
        return{
            'nombre': self.ui.txt_nombrepuesto,
            'salario': self.ui.decimal_salario,
            'horas_laborales': self.ui.decimal_horaslaborales,
            'descripcion_puesto':self.ui.txtlargo_descripcionpuesto,
            'hora_entrada':self.ui.tiempo_horaentrada,
            'hora_salida':self.ui.tiempo_horasalida,
        }
    
    def obtener_contenido_campos(self):
        return {
            nombre: self.obtener_valor(widget)
            for nombre, widget in self.campos().items()
        }

    def obtener_valor(self, widget):
        if isinstance(widget, QLineEdit):
            return widget.text().strip().upper()
        elif isinstance(widget, QPlainTextEdit):
            return widget.toPlainText().strip().upper()
        elif isinstance(widget, QDoubleSpinBox):
            return widget.value()  # Devuelve el valor numérico
        elif isinstance(widget, QTimeEdit):
            return widget.time().toString()  # Devuelve la hora en formato de cadena
        return None  # En caso de que no coincida con ningún tipo

    def validar(self, campos):
        campos_vacios = [nombre for nombre, valor in campos.items() if not valor]
        if campos_vacios:
            print(f'Tienes campos vacíos: {", ".join(campos_vacios)}')
            return False
        return True