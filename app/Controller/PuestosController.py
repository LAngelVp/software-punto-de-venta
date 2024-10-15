from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from ..DataBase.conexionBD import Conexion_base_datos
from ..View.UserInterfacePy.UI_ADMINISTRAR_PUESTOS import Ui_Formulario_puestos
from ..Model.PuestoModel import PuestoModel


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
        self.ui.btn_btn_vincular.clicked.connect(self.vincular_departamento)
        self.ui.btn_btn_desvincular.clicked.connect(self.desvincular_departamento)
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
        self.diasLaborales = set()


    #funciones:
    def comprobar_caja_verificacion(self, state):
        sender = self.sender()
        if state == Qt.Checked:
            if sender.text() not in self.diasLaborales:
                self.diasLaborales.add(sender.text())
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
        diasLaborales = self.diasLaborales
        datos = self.obtener_contenido_campos()
        print(datos)
        if not self.validar(datos):
            print ("No se agregaron los campos")
            return
        with Conexion_base_datos() as db:
            session = db.abrir_sesion()
            with session.begin():
                puesto, agregado = PuestoModel(session).crear_puesto(
                    nombre=datos['nombre'],
                    salario=datos['salario'],
                    horas_laborales=datos['horas_laborales'],
                    dias_laborales=diasLaborales,
                    descripcion=datos['descripcion'],
                    hora_entrada=datos['hora_entrada'],
                    hora_salida=datos['hora_salida'],
                )



    def eliminar(self):
        pass

    def buscar_puesto(self):
        pass

    def vincular_departamento(self):
        pass

    def desvincular_departamento(self):
        pass

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