from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from datetime import  datetime, timedelta
from ..View.UserInterfacePy.UI_CONTROL_CLIENTES import *
from .CategoriasProveedorController import *
from .AreaNegocioClientesController import AreaNegocioClientesController
from ..Model.AreaNegocioClientesModel import AreaNegocioClientesModel
from .CategoriaClientesController import *
from ..Model.CategoriaClienteModel import CategoriaClienteModel
from .AjustarCajaOpcionesGlobal import AjustarCajaOpciones
from ..Model.ClientesFisicosAndMoralesModel import *

class Clientes(QWidget):
    cliente_seleccionado = pyqtSignal(str)
    def __init__(self):
        super().__init__()
        self.ui = Ui_Control_Clientes()
        self.ui.setupUi(self)
        self.clienteFisico = True
        self.ui.cajaDecimal_wpc_ingresosclienteFisico.setButtonSymbols(QSpinBox.NoButtons)
        self.ui.cajaDecimal_wpc_limite_credito.setButtonSymbols(QSpinBox.NoButtons)
        self.ui.cajaDecimal_wpc_limite_credito_moral.setButtonSymbols(QSpinBox.NoButtons)
        self.ui.cajaDecimal_creditodisponible_fisico.setButtonSymbols(QSpinBox.NoButtons)
        self.ui.cajaDecimal_creditodisponible_moral.setButtonSymbols(QSpinBox.NoButtons)
        self.ui.cajaDecimal_creditoutilizado_fisico.setButtonSymbols(QSpinBox.NoButtons)
        self.ui.cajaDecimal_creditoutilizado_moral.setButtonSymbols(QSpinBox.NoButtons)
        self.ui.cajaDecimal_interesesaplicados_fisico.setButtonSymbols(QSpinBox.NoButtons)
        self.ui.cajaDecimal_porcentajeintereses_moral.setButtonSymbols(QSpinBox.NoButtons)
        self.ui.cajaDecimal_porcentajedescuento_fisico.setButtonSymbols(QSpinBox.NoButtons)
        self.ui.cajaDecimal_porcentajedescuento_moral.setButtonSymbols(QSpinBox.NoButtons)
        self.ui.btnRadio_wpc_clienteFisico.setChecked(self.clienteFisico)
        self.ui.cajaDecimal_wpc_limite_credito.setEnabled(False)
        self.ui.cajaDecimal_wpc_limite_credito_moral.setEnabled(False)
        self.ui.txt_estadodelcredito_fisico.setText("SIN AUTORIZAR")
        self.ui.txt_estadocredito_moral.setText("SIN AUTORIZAR")
        self.ui.fecha_fechaconstitucion.setDate(QDate.currentDate())
        self.ui.fecha_fechanacimiento.setDate(QDate.currentDate())
        self.ui.fecha_ultimoreporte_fisico.setDate(QDate.currentDate())
        self.ui.fecha_ultimoreporte_moral.setDate(QDate.currentDate())
        self.ui.contenedor_clientmoral.hide()
        #//: VARIABLES GLOBALES
        self.foto_cliente = None
        self.clientes = None
        self.id_cliente = None
        self.id_area_del_cliente = None
        self.id_clasificacion_del_cliente = None
        self._translate = QtCore.QCoreApplication.translate
        #----------------------------------
        #// : FUNCIONES PRINCIPALES
        self.listar_areas()
        self.listar_categorias()
        self.tabla_listar_clientes()
        #------------------------------
        #//: CARGAR FOTO DEL CLIENTE FISICO
        self.ui.label_wpc_fotocliente.mousePressEvent = self.obtener_foto
        #------------------------------
        #// : AUTORIZAR CREDITOS
        self.ui.casillaverificacion_wpc_credito_autorizado.toggled.connect(self.autorizar_credito_fisico)
        self.ui.casillaverificacion_wpc_credito_autorizado_moral.toggled.connect(self.autorizar_credito_moral)
        #-----------------------------
        #// : MOSTRAR FORMULARIOS
        self.ui.btnRadio_wpc_clienteMoral.toggled.connect(self.mostrar_contenedor_cliente_moral)
        self.ui.btnRadio_wpc_clienteFisico.toggled.connect(self.mostrar_contenedor_cliente_fisico)
        #------------------------------
        #//: ACTIVAR CREDITOS
        self.ui.casillaverificacion_wpc_credito_autorizado.toggled.connect(self.activar_creditofisico)
        self.ui.casillaverificacion_wpc_credito_autorizado_moral.toggled.connect(self.activar_creditomoral)
        #------------------------------
        #// : AGREGAR AREA Y CATEGORIA
        self.ui.btn_btn_nuevacategoriaFisico.clicked.connect(self.nueva_categoria)
        self.ui.btn_btn_nuevacategoriaMoral.clicked.connect(self.nueva_categoria)
        self.ui.btn_btn_nuevaareanegocio_fisico.clicked.connect(self.nueva_area_cliente_fisico)
        self.ui.btn_btn_areasnegocio_moral.clicked.connect(self.nueva_area_cliente_moral)
        #-----------------------------
        #//: MOSTRAR DATOS DEL CLIENTES EN LOS CAMPOS
        self.cliente_seleccionado.connect(self.cargar_cliente)
        #----------------------------
        #//: AGREGAR CLIENTES
        self.ui.btn_btn_cliente_agregar.clicked.connect(self.agregar_cliente)
        #------------------------------
        #//: LIMPIAR CAMPOS
        self.ui.btn_btn_limpiarcampos.clicked.connect(self.limpiar_campos)
        #------------------------------
        #//: BUSCAR CLIENTES
        self.ui.txt_buscarcliente.returnPressed.connect(self.buscar_cliente)
        #------------------------------
        #//: ACTUALIZAR CLIENTES
        self.ui.btn_btn_cliente_modificar.clicked.connect(self.actualizar_clientes)
        #----------------------------
        #// : eliminar clientes
        self.ui.btn_btn_cliente_eliminar.clicked.connect(self.eliminar_clientes)
    #FUNCIONES:-----------------
    def buscar_cliente(self):
        tipo_cliente = None
        modelo_cliente = None
        with Conexion_base_datos() as db:
            session = db.abrir_sesion()
            with session.begin():
                if self.ui.btnRadio_wpc_clienteFisico.isChecked():
                    tipo_cliente = "FISICO"
                    modelo_cliente = Clientes_fisicos
                else:
                    tipo_cliente = "MORAL"
                    modelo_cliente = Clientes_morales
                
                self.clientes = ClientesFisicosAndMorales(session).filtrar_clientes_por_nombre(
                    self.ui.txt_buscarcliente.text(), tipo_cliente, modelo_cliente)

                self.llenar_tabla_clientes(self.clientes)
            self.clientes = None

    def limpiar_campos(self):
        try:
            if self.ui.btnRadio_wpc_clienteFisico.isChecked():
                fisicos = self.campos_cliente_fisico()
                for campo in fisicos.values():
                    # Limpiar QLineEdit
                    if isinstance(campo, QLineEdit) and campo != self.ui.txt_estadodelcredito_fisico:
                        campo.clear()
                    # Limpiar QPlainTextEdit
                    elif isinstance(campo, QPlainTextEdit):
                        campo.clear()
                    # Restablecer QComboBox al primer índice
                    elif isinstance(campo, QComboBox):
                        campo.setCurrentIndex(0)
                    # Restablecer QDoubleSpinBox a 0
                    elif isinstance(campo, QDoubleSpinBox):
                        campo.setValue(0.0)
                    # Restablecer QCheckBox a no marcado
                    elif isinstance(campo, QCheckBox):
                        campo.setChecked(False)
                    # Restablecer QDateEdit a la fecha actual
                    elif isinstance(campo, QDateEdit):
                        campo.setDate(QDate.currentDate())

                    self.listar_areas()
                    self.listar_categorias()
                self.ui.label_wpc_fotocliente.setText(self._translate("Control_Clientes", "Imagen"))

                    
                    

            elif self.ui.btnRadio_wpc_clienteMoral.isChecked():
                fisicos = self.campos_cliente_moral()
                for campo in fisicos.values():
                    # Limpiar QLineEdit
                    if isinstance(campo, QLineEdit) and campo != self.ui.txt_estadocredito_moral:
                        campo.clear()
                    # Limpiar QPlainTextEdit
                    elif isinstance(campo, QPlainTextEdit):
                        campo.clear()
                    # Restablecer QComboBox al primer índice
                    elif isinstance(campo, QComboBox):
                        campo.setCurrentIndex(0)
                    # Restablecer QDoubleSpinBox a 0
                    elif isinstance(campo, QDoubleSpinBox):
                        campo.setValue(0.0)
                    # Restablecer QCheckBox a no marcado
                    elif isinstance(campo, QCheckBox):
                        campo.setChecked(False)
                    # Restablecer QDateEdit a la fecha actual
                    elif isinstance(campo, QDateEdit):
                        campo.setDate(QDate.currentDate())

                    self.listar_areas()
                    self.listar_categorias()
        except Exception as e:
            print(f"Error al limpiar campos: {e}")

        self.foto_cliente = None
        self.clientes = None
        self.id_cliente = None

    def campos_cliente_fisico(self):
        return {
            "nombre": self.ui.txt_nombre_fisico,
            "correo electronico" : self.ui.txt_correo_fisico,
            "rfc" : self.ui.txt_rfc_fisico,
            "telefono" : self.ui.txt_telefono_fisico,
            "pais" : self.ui.txt_pais_fisico,
            "estado" : self.ui.txt_estado_fisico,
            "ciudad" : self.ui.txt_ciudad_fisico,
            "avenidas" : self.ui.txt_avenidas_fisico,
            "calles" : self.ui.txt_calles_fisico,
            "codigo postal" : self.ui.txt_codigopostal_fisico,
            "direccion adicional": self.ui.txtlargo_direccionadicional_fisico,
            "entidad legalizada": self.ui.casillaverificacion_entidadlegalizada_fisico,
            "categoria del cliente" : self.ui.cajaopciones_categoriaFisico,
            "tiene credito": self.ui.casillaverificacion_wpc_credito_autorizado,
            "estado del credito" : self.ui.txt_estadodelcredito_fisico,
            "limite de credito" : self.ui.cajaDecimal_wpc_limite_credito,
            "porcentaje de interes" : self.ui.cajaDecimal_interesesaplicados_fisico,
            "fecha del ultimo reporte" : self.ui.fecha_ultimoreporte_fisico,
            "credito disponible": self.ui.cajaDecimal_creditodisponible_fisico,
            "credito utilizado" : self.ui.cajaDecimal_creditoutilizado_fisico,
            "aplica descuento" : self.ui.casillaverificacion_aplicadescuento_fisico,
            "ocupacion" : self.ui.txt_ocupacion_fisico,
            "area de negocio" : self.ui.cajaopciones_areasnegocio_fisico,
            "comentarios": self.ui.txtlargo_comentarioclientefisico,
            "porcentaje de descuento" : self.ui.cajaDecimal_porcentajedescuento_fisico,
            "apellido paterno" : self.ui.txt_apellidop_fisico,
            "apellido materno" : self.ui.txt_apellidom_fisico,
            "curp": self.ui.txt_curp_fisico,
            "fecha de nacimiento" : self.ui.fecha_fechanacimiento,
            "numero de identificacion" : self.ui.txt_ine_fisico,
            "ingresos" : self.ui.cajaDecimal_wpc_ingresosclienteFisico,
            "estado civil" : self.ui.cajaopciones_estadocivil_fisico,
            "foto" : self.ui.label_wpc_fotocliente
        }
    
    def campos_cliente_moral(self):
        return {
            "nombre": self.ui.txt_nombre_empre_moral,
            "correo electronico" : self.ui.txt_correo_empre_moral,
            "rfc" : self.ui.txt_rfc_empre_moral,
            "telefono" : self.ui.txt_telefono_empre_moral,
            "pais" : self.ui.txt_pais_moral,
            "estado" : self.ui.txt_estado_moral,
            "ciudad" : self.ui.txt_ciudad_moral,
            "avenidas" : self.ui.txt_avenidas_empre_moral,
            "calles" : self.ui.txt_calles_empre_moral,
            "codigo postal" : self.ui.txt_codigopostal_moral,
            "direccion adicional": self.ui.txtlargo_direccionadicional_moral,
            "entidad legalizada": self.ui.casillaverificacion_entidadlegalizada_moral,
            "categoria del cliente" : self.ui.cajaopciones_categoriaMoral,
            "sector" : self.ui.txt_sector_empre_moral,
            "web" : self.ui.txt_pagina_empre_moral,
            "tiene credito": self.ui.casillaverificacion_wpc_credito_autorizado_moral,
            "estado del credito" : self.ui.txt_estadocredito_moral,
            "limite de credito" : self.ui.cajaDecimal_wpc_limite_credito_moral,
            "porcentaje de interes" : self.ui.cajaDecimal_porcentajeintereses_moral,
            "fecha del ultimo reporte" : self.ui.fecha_ultimoreporte_moral,
            "credito disponible": self.ui.cajaDecimal_creditodisponible_moral,
            "credito utilizado" : self.ui.cajaDecimal_creditoutilizado_moral,
            "aplica descuento" : self.ui.casillaverificacion_aplicadescuento_moral,
            "area de negocio" : self.ui.cajaopciones_areasnegocio_moral,
            "comentarios": self.ui.txtlargo_comentarios_cliente_moral,
            "porcentaje de descuento" : self.ui.cajaDecimal_porcentajedescuento_moral,
            "razon social": self.ui.txt_razonsocial_moral,
            "fecha de constitucion" : self.ui.fecha_fechaconstitucion,
            "numero de identificacion fiscal": self.ui.txt_nif_moral,
            'representante moral' : self.ui.txt_nombre_repre_moral,
            'telefono representante' : self.ui.txt_telefono_repre_moral,
            'puesto del representante' : self.ui.txt_puesto_repre_moral,
            'correo electronico representante' : self.ui.txt_correo_repre_moral,
        }

    def cargar_cliente(self, id):
        self.limpiar_campos()
        self.id_cliente = id
        with Conexion_base_datos() as db:
            session = db.abrir_sesion()
            with session.begin():
                try:
                    if self.ui.btnRadio_wpc_clienteFisico.isChecked():
                        cliente = ClientesFisicosAndMorales(session).obtener_cliente_fisico_por_id(id)
                        if  cliente:
                            campo, cliente_fisico = cliente
                            datos  = self.campos_cliente_fisico()

                            datos["nombre"].setText(campo.nombre)
                            datos["correo electronico"].setText(campo.correo)
                            datos["rfc"].setText(campo.rfc)
                            datos["telefono"].setText(campo.telefono)
                            datos["pais"].setText(campo.pais)
                            datos["estado"].setText(campo.estado)
                            datos["ciudad"].setText(campo.ciudad)
                            datos["codigo postal"].setText(campo.codigo_postal)
                            datos["avenidas"].setText(campo.avenidas)
                            datos["calles"].setText(campo.calles)
                            datos["direccion adicional"].setPlainText(campo.direccion_adicional)
                            datos["entidad legalizada"].setChecked(campo.entidad_legalizada)

                            
                            datos["tiene credito"].setChecked(campo.credito)
                            datos["estado del credito"].setText(campo.estado_credito)
                            datos["limite de credito"].setValue(campo.limite_credito)
                            datos["porcentaje de interes"].setValue(campo.porcentaje_interes)
                            datos["porcentaje de interes"].setValue(campo.porcentaje_interes)
                            datos["fecha del ultimo reporte"].setDate(campo.fecha_ultimo_reporte)
                            datos["credito disponible"].setValue(campo.credito_disponible)
                            datos["credito utilizado"].setValue(campo.credito_utilizado)
                            datos["aplica descuento"].setChecked(campo.aplica_descuento)
                            

                            datos["comentarios"].setPlainText(campo.comentarios)
                            datos["porcentaje de descuento"].setValue(campo.porcentaje_descuento)
                            datos["apellido paterno"].setText(campo.apellido_paterno)
                            datos["apellido materno"].setText(campo.apellido_materno)
                            datos["curp"].setText(campo.curp)
                            datos["fecha de nacimiento"].setDate(campo.fecha_nacimiento)
                            datos["numero de identificacion"].setText(campo.num_identificacion)
                            datos["ocupacion"].setText(campo.ocupacion)
                            datos["ingresos"].setValue(campo.ingresos)
                            datos["estado civil"].clear()
                            datos["estado civil"].addItem(campo.estado_civil)
                            datos["foto"].setPixmap(QPixmap(campo.foto).scaled(datos["foto"].size()))
                            self.foto_cliente = campo.foto

                            if campo.categoria:
                                categoria_nombre = campo.categoria.nombre
                                caja_categorias = datos["categoria del cliente"]
                                indice = caja_categorias.findText(categoria_nombre)
                                if  indice != -1:
                                    caja_categorias.removeItem(indice)

                                caja_categorias.insertItem(0, categoria_nombre)
                                caja_categorias.setCurrentIndex(0)


                            if campo.areas_de_negocios:
                                area_nombre = campo.areas_de_negocios.nombre
                                caja_areas = datos["area de negocio"]
                                indice = caja_areas.findText(area_nombre)
                                if  indice != -1:
                                    caja_areas.removeItem(indice)

                                caja_areas.insertItem(0, area_nombre)
                                caja_areas.setCurrentIndex(0)
                            
                    elif self.ui.btnRadio_wpc_clienteMoral.isChecked():
                        cliente = ClientesFisicosAndMorales(session).obtener_cliente_moral_por_id(id)
                        if  cliente:
                            campo, cliente_fisico = cliente
                            datos  = self.campos_cliente_moral()

                            datos["nombre"].setText(campo.nombre)
                            datos["correo electronico"].setText(campo.correo)
                            datos["rfc"].setText(campo.rfc)
                            datos["telefono"].setText(campo.telefono)
                            datos["pais"].setText(campo.pais)
                            datos["estado"].setText(campo.estado)
                            datos["ciudad"].setText(campo.ciudad)
                            datos["avenidas"].setText(campo.avenidas)
                            datos["calles"].setText(campo.calles)
                            datos["codigo postal"].setText(campo.codigo_postal)
                            datos["direccion adicional"].setPlainText(campo.direccion_adicional)
                            datos["entidad legalizada"].setChecked(campo.entidad_legalizada)

                            
                            datos["tiene credito"].setChecked(campo.credito)
                            datos["estado del credito"].setText(campo.estado_credito)
                            datos["limite de credito"].setValue(campo.limite_credito)
                            datos["porcentaje de interes"].setValue(campo.porcentaje_interes)
                            datos["porcentaje de interes"].setValue(campo.porcentaje_interes)
                            datos["fecha del ultimo reporte"].setDate(campo.fecha_ultimo_reporte)
                            datos["credito disponible"].setValue(campo.credito_disponible)
                            datos["credito utilizado"].setValue(campo.credito_utilizado)
                            datos["aplica descuento"].setChecked(campo.aplica_descuento)

                            

                            datos["comentarios"].setPlainText(campo.comentarios)
                            datos["porcentaje de descuento"].setValue(campo.porcentaje_descuento)
                            datos["razon social"].setText(campo.razon_social)
                            datos["fecha de constitucion"].setDate(campo.fecha_constitucion)
                            datos["numero de identificacion fiscal"].setText(campo.NIF)
                            datos["sector"].setText(campo.sector)
                            datos["web"].setText(campo.web)


                            if campo.representante:
                                representante = campo.representante
                                datos['representante moral'].setText(representante.nombre)
                                datos['telefono representante'].setText(representante.telefono)
                                datos['puesto del representante'].setText(representante.puesto)
                                datos['correo electronico representante'].setText(representante.correo)

                            if campo.categoria:
                                categoria_nombre = campo.categoria.nombre
                                caja_categorias = datos["categoria del cliente"]
                                indice = caja_categorias.findText(categoria_nombre)
                                if  indice != -1:
                                    caja_categorias.removeItem(indice)

                                caja_categorias.insertItem(0, categoria_nombre)
                                caja_categorias.setCurrentIndex(0)


                            if campo.areas_de_negocios:
                                area_nombre = campo.areas_de_negocios.nombre
                                caja_areas = datos["area de negocio"]
                                indice = caja_areas.findText(area_nombre)
                                if  indice != -1:
                                    caja_areas.removeItem(indice)

                                caja_areas.insertItem(0, area_nombre)
                                caja_areas.setCurrentIndex(0)

                except Exception as e:
                    print("Error al obtener proveedor : " + str(e))

    def tabla_listar_clientes(self):
        try:
            with Conexion_base_datos() as db:
                session = db.abrir_sesion()
                with session.begin():
                    if self.ui.btnRadio_wpc_clienteFisico.isChecked():
                        self.clientes = ClientesFisicosAndMorales(session).mostrar_clientes_fisicos()    
                    else:
                        self.clientes = ClientesFisicosAndMorales(session).mostrar_clientes_morales()
                    self.llenar_tabla_clientes(self.clientes)
        except Exception as e:
            print(e)
        self.clientes = None

    def llenar_tabla_clientes(self, clientes):
        try:
            # Verificar si la tabla está inicializada
            if self.ui.tabla_clientes is None:
                print("El widget tabla_clientes no está disponible.")
                return

            # Inicializar el modelo de la tabla si no existe
            if not hasattr(self, 'model'):
                self.model = QStandardItemModel()

            
            
            # Limpiar el modelo antes de llenarlo con nuevos datos
            self.model.clear()
            
            # Establecer los encabezados para el modelo
            if self.ui.btnRadio_wpc_clienteFisico.isChecked():
                # Verificar si clientes es None o una lista vacía
                if clientes is None or len(clientes) == 0:
                    self.model.clear()  # Limpiar el modelo
                    self.model.setHorizontalHeaderLabels([
                        "Id",
                        "Nombre",
                        "Apellido Paterno",
                        "Apellido Materno",
                        "RFC",
                        "CURP"
                        ])
                    self.ui.tabla_clientes.setModel(self.model) 
                    print("No se recibieron datos de clientes o la lista está vacía.")
                    return
                nombre_columnas = [
                    "Id",
                    "Nombre",
                    "Apellido Paterno",
                    "Apellido Materno",
                    "RFC",
                    "CURP"
                ]
                self.model.setHorizontalHeaderLabels(nombre_columnas)
                
                # Llenar el modelo con datos de clientes
                for cliente, cliente_fisico in clientes:
                    if cliente_fisico is not None:
                        row_data = [
                            str(cliente.id),
                            cliente.nombre,
                            cliente_fisico.apellido_paterno,
                            cliente_fisico.apellido_materno,
                            cliente.rfc,
                            cliente_fisico.curp
                        ]
                    else:
                        # Usar campos vacíos si no hay datos de cliente físico
                        row_data = [
                            str(cliente.id), cliente.nombre, "", "", cliente.rfc, ""
                        ]

                    items = [QStandardItem(item) for item in row_data]
                    self.model.appendRow(items)

            if self.ui.btnRadio_wpc_clienteMoral.isChecked():
                # Verificar si clientes es None o una lista vacía
                if clientes is None or len(clientes) == 0:
                    self.model.clear()  # Limpiar el modelo
                    self.model.setHorizontalHeaderLabels([
                        "Id",
                        "Nombre",
                        "RFC",
                        "RAZON SOCIAL",
                        "NIF"
                        ])
                    self.ui.tabla_clientes.setModel(self.model) 
                    print("No se recibieron datos de clientes o la lista está vacía.")
                    return
                nombre_columnas = [
                    "Id",
                    "Nombre",
                    "RFC",
                    "RAZON SOCIAL",
                    "NIF"

                ]
                self.model.setHorizontalHeaderLabels(nombre_columnas)
                for row_index, (cliente, cliente_moral) in enumerate(clientes):
                    if cliente_moral is not None:
                        row_data = [
                            str(cliente.id),
                            cliente.nombre,
                            cliente.rfc,
                            cliente.razon_social,
                            cliente.NIF
                        ]
                    else:
                        # En caso de que no haya datos de cliente físico, usar campos vacíos
                        row_data = [
                            str(cliente.id), cliente.nombre, "", "", cliente.rfc, ""
                        ]
                    items = [QStandardItem(item) for item in row_data]
                    self.model.appendRow(items)

            # Asignar el modelo a la tabla
            self.ui.tabla_clientes.setModel(self.model)
            self.ui.tabla_clientes.setColumnHidden(0, True)
        except Exception as e:
            print(e)
            print(f'No se logro hacer mostrar la tabla {e}')

        self.ui.tabla_clientes.selectionModel().currentChanged.connect(self.obtener_id_elemento_tabla)
        self.clientes = None

    def obtener_id_elemento_tabla(self, current, previus):
        # Verifica si la celda seleccionada está en la primera columna
        if current.column() >= 1:  # Verifica si es la primera columna
            indice_fila = current.row()
            self.id_cliente = self.model.item(indice_fila, 0).text()  # Obtener el ID del proveedor
            print(self.id_cliente)
            self.cliente_seleccionado.emit(self.id_cliente)

    def autorizar_credito_fisico(self):
        if self.ui.casillaverificacion_wpc_credito_autorizado.isChecked():
            self.ui.txt_estadodelcredito_fisico.setText("AUTORIZADO")
        else:
            self.ui.txt_estadodelcredito_fisico.setText("SIN AUTORIZAR")
            # self.ui.cajaDecimal_wpc_limite_credito.setValue(0)
    
    def autorizar_credito_moral(self):
        if self.ui.casillaverificacion_wpc_credito_autorizado_moral.isChecked():
            self.ui.txt_estadocredito_moral.setText("AUTORIZADO")
        else:
            self.ui.txt_estadocredito_moral.setText("SIN AUTORIZAR")
            # self.ui.cajaDecimal_wpc_limite_credito_moral.setValue(0)

    def obtener_foto(self, event):
        options = QFileDialog.Options()
        self.foto_cliente, _ = QFileDialog.getOpenFileName(self, 'SELECCIONA UNA IMAGEN', ' ', 'Archivo de Imagen (*.png *.jpg *.jpeg);; Todos los archivos (*)', options=options)
        if self.foto_cliente:
            self.ui.label_wpc_fotocliente.setText(self.foto_cliente)
            pixmap = QPixmap(self.foto_cliente)
            self.ui.label_wpc_fotocliente.setPixmap(pixmap)
            self.ui.label_wpc_fotocliente.setScaledContents(True)
            self.ui.label_wpc_fotocliente.adjustSize()
    
    def obtener_datos_cliente_fisico(self):
        return  {
                    "nombre": self.ui.txt_nombre_fisico.text().strip().upper(),
                    "apellido paterno" : self.ui.txt_apellidop_fisico.text().strip().upper(),
                    "apellido materno" : self.ui.txt_apellidom_fisico.text().strip().upper(),
                    "rfc": self.ui.txt_rfc_fisico.text().strip().upper(),
                    "numero telefono" : self.ui.txt_telefono_fisico.text().strip().upper(),
                    "pais": self.ui.txt_pais_fisico.text().strip().upper(),
                    "estado": self.ui.txt_estado_fisico.text().strip().upper(),
                    "ciudad": self.ui.txt_ciudad_fisico.text().strip().upper(),
                    "codigo postal": self.ui.txt_codigopostal_fisico.text().strip().upper(),
                    "direccion adicional": self.ui.txtlargo_direccionadicional_fisico.toPlainText().strip().upper(),
                    "curp": self.ui.txt_curp_fisico.text().strip().upper(),
                    "estado civil": self.ui.cajaopciones_estadocivil_fisico.currentText().strip().upper(),
                    "nivel de ingresos": self.ui.cajaDecimal_wpc_ingresosclienteFisico.value(),
                    "correo electronico" : self.ui.txt_correo_fisico.text().strip(),
                    "avenidas" : self.ui.txt_avenidas_fisico.text().strip().upper(),
                    "calles" : self.ui.txt_calles_fisico.text().strip().upper(),
                    "fecha de nacimiento" : self.ui.fecha_fechanacimiento.date().toPyDate(),
                    "numero identificacion" : self.ui.txt_ine_fisico.text().strip().upper(),
                    "ocupacion" : self.ui.txt_ocupacion_fisico.text().strip().upper(),
                    "area de negocio" : self.ui.cajaopciones_areasnegocio_fisico.currentText().strip().upper(),
                    "clasificacion cliente": self.ui.cajaopciones_areasnegocio_fisico.currentText().strip().upper(),
                    "estado civil": self.ui.cajaopciones_estadocivil_fisico.currentText().strip().upper(),
                    "comentarios" : self.ui.txtlargo_comentarioclientefisico.toPlainText().strip().upper(),
                    "entidad legalizada" : self.ui.casillaverificacion_entidadlegalizada_fisico.isChecked(),
                    "credito autorizado" : self.ui.casillaverificacion_wpc_credito_autorizado.isChecked(),
                    "estado del credito" : self.ui.txt_estadodelcredito_fisico.text().strip().upper(),
                    "limite del credito" : self.ui.cajaDecimal_wpc_limite_credito.value(),
                    "porcentaje del interes" : self.ui.cajaDecimal_interesesaplicados_fisico.value(),
                    "porcentaje del descuento" : self.ui.cajaDecimal_porcentajedescuento_fisico.value(),
                    "fecha del ultimo reporte" : self.ui.fecha_ultimoreporte_fisico.date(),
                    "credito utilizado" : self.ui.cajaDecimal_creditoutilizado_fisico.value(),
                    "aplica descuento" : self.ui.casillaverificacion_aplicadescuento_fisico.isChecked(),
                    "credito disponible" : self.ui.cajaDecimal_creditodisponible_fisico.value(),
                    "ingresos" : self.ui.cajaDecimal_wpc_ingresosclienteFisico.value(),
                    
                }

    def validacion_campos_cliente_fisico(self, datos):
        campos_requeridos = [
            "nombre",
            "apellido paterno",
            "apellido materno",
            "rfc",
            "pais",
            "estado",
            "curp",
            "estado civil",
            "nivel de ingresos",
            "correo electronico",
            "numero telefono",
            "avenidas",
            "calles",
            "fecha de nacimiento",
            "ciudad",
            "codigo postal",
            "numero identificacion",
            "ocupacion",
            "direccion adicional",
            "area de negocio",
            "clasificacion cliente",
            "comentarios"
        ]
        for campo in campos_requeridos:
            if not datos[campo]:
                Mensaje().mensaje_informativo(f'Existe un campo llamado "{campo}" que no haz completado')
                return False
        return True

    def obtener_datos_cliente_moral(self):
        return {
            'nombre' : self.ui.txt_nombre_empre_moral.text().strip().upper(),
            'razon social' : self.ui.txt_razonsocial_moral.text().strip().upper(),
            'correo electronico empresa' : self.ui.txt_correo_empre_moral.text().strip().upper(),
            'rfc' : self.ui.txt_rfc_empre_moral.text().strip().upper(),
            'avenidas' : self.ui.txt_avenidas_empre_moral.text().strip().upper(),
            'web' : self.ui.txt_pagina_empre_moral.text().strip(),
            'pais' : self.ui.txt_pais_moral.text().strip().upper(),
            'ciudad' : self.ui.txt_ciudad_moral.text().strip().upper(),
            'numero telefono' : self.ui.txt_telefono_empre_moral.text().strip().upper(),
            'numero de identificacion fiscal' : self.ui.txt_nif_moral.text().strip().upper(),
            'calles' : self.ui.txt_calles_empre_moral.text().strip().upper(),
            'sector' : self.ui.txt_sector_empre_moral.text().strip().upper(),
            'estado' : self.ui.txt_estado_moral.text().strip().upper(),
            'codigo postal' : self.ui.txt_codigopostal_moral.text().strip().upper(),
            'area de negocio' : self.ui.cajaopciones_areasnegocio_moral.currentText().strip().upper(),
            "fecha de constitucion" : self.ui.fecha_fechaconstitucion.date().toPyDate(),
            'clasificacion de cliente' : self.ui.cajaopciones_categoriaMoral.currentText().strip().upper(),
            'direccion adicional' : self.ui.txtlargo_direccionadicional_moral.toPlainText().strip().upper(),
            'representante moral' : self.ui.txt_nombre_repre_moral.text().strip().upper(),
            'telefono representante' : self.ui.txt_telefono_repre_moral.text().strip().upper(),
            'puesto del representante' : self.ui.txt_puesto_repre_moral.text().strip().upper(),
            'correo electronico representante' : self.ui.txt_correo_repre_moral.text().strip().upper(),
            'comentarios' : self.ui.txtlargo_comentarios_cliente_moral.toPlainText().strip().upper(),
            "credito autorizado": self.ui.casillaverificacion_wpc_credito_autorizado_moral.isChecked(),
            "limite del credito": self.ui.cajaDecimal_wpc_limite_credito_moral.value(),
            "credito disponible": self.ui.cajaDecimal_creditodisponible_moral.value(),
            "credito utilizado": self.ui.cajaDecimal_creditoutilizado_moral.value(),
            "estado del credito": self.ui.txt_estadocredito_moral.text().upper().strip(),
            "porcentaje del interes": self.ui.cajaDecimal_porcentajeintereses_moral.value(),
            "descuento autorizado": self.ui.casillaverificacion_aplicadescuento_moral.isChecked(),
            "porcentaje del descuento": self.ui.cajaDecimal_porcentajedescuento_moral.value(),
            "entidad legalizada": self.ui.casillaverificacion_entidadlegalizada_moral.isChecked(),
            "fecha del ultimo reporte": self.ui.fecha_ultimoreporte_moral.date()
        }

    def validacion_campos_cliente_moral(self, datos):
        campos_cliente_moral = [
            "nombre", "razon social", "correo electronico empresa", "avenidas", "web", "pais", "ciudad", "numero telefono", "numero de identificacion fiscal", "calles", "sector", "estado", "codigo postal", "area de negocio", "fecha de constitucion", "clasificacion de cliente", "direccion adicional", "representante moral", "telefono representante", "puesto del representante", "correo electronico representante", "comentarios"
        ]

        for campo in campos_cliente_moral:
            if not datos[campo]:
                Mensaje().mensaje_informativo(f'Existe un campo llamado "{campo}" que no esta completo.')
                return False
        return True
    
    def agregar_cliente(self):
        fecha_actual = datetime.now().date()
        if self.ui.btnRadio_wpc_clienteFisico.isChecked():
            datos = self.obtener_datos_cliente_fisico()
            if not self.validacion_campos_cliente_fisico(datos):
                return
            limite_credito = datos["limite del credito"]
            fecha_ultimo_reporte = fecha_actual.strftime("%Y/%m/%d")
            credito_disponible = limite_credito
            tipo_de_cliente = "FISICO"
            
            #comment: datos cliente fisico 
            
            foto = self.foto_cliente

            nombre_categoria = datos['clasificacion cliente']
            nombre_area_de_negocio = datos['area de negocio']

            #comment:_obetnemos los ids de categoria y area
            with Conexion_base_datos() as db:
                session = db.abrir_sesion()
                with session.begin():
                    try:
                        id_categoria_cliente = CategoriaClienteModel(session).agregar(nombre = nombre_categoria)
                        id_area_de_negocio = AreaNegocioClientesModel(session).agregar_area(nombre = nombre_area_de_negocio)

                        nuevo_cliente = ClientesFisicosAndMorales(session).agregar_cliente_fisico(
                            nombre=datos['nombre'], 
                            correo=datos['correo electronico'],
                            rfc=datos['rfc'],
                            telefono=datos['numero telefono'],
                            pais=datos['pais'], 
                            estado=datos['estado'], 
                            ciudad=datos['ciudad'],
                            avenidas=datos["avenidas"],
                            calles=datos["calles"],
                            codigo_postal=datos['codigo postal'], 
                            direccion_adicional=datos['direccion adicional'], 
                            entidad_legalizada=datos["entidad legalizada"], 
                            categoria_cliente_id=id_categoria_cliente,
                            credito=datos["limite del credito"], 
                            estado_credito=datos["estado del credito"], 
                            limite_credito=limite_credito, 
                            porcentaje_interes=datos["porcentaje del interes"],
                            fecha_ultimo_reporte=fecha_ultimo_reporte, 
                            credito_disponible=credito_disponible, 
                            credito_utilizado=datos["credito utilizado"], 
                            tipo_cliente=tipo_de_cliente, 
                            aplica_descuento=datos["aplica descuento"],
                            porcentaje_descuento = datos["porcentaje del descuento"],
                            comentarios = datos["comentarios"],
                            areas_de_negocios_id=id_area_de_negocio,
                            apellido_paterno=datos['apellido paterno'], 
                            apellido_materno=datos['apellido materno'], 
                            curp=datos['curp'], 
                            fecha_nacimiento=datos['fecha de nacimiento'], 
                            num_identificacion=datos['numero identificacion'],
                            ocupacion=datos['ocupacion'],
                            ingresos=datos["ingresos"],
                            estado_civil=datos["estado civil"],
                            foto=foto
                            )
                    except Exception as e:
                        Mensaje().mensaje_alerta(f'No se logro hacer la creacion del cliente fisico: ,  {str(e)}')
            self.tabla_listar_clientes()
            self.limpiar_campos()

        elif self.ui.btnRadio_wpc_clienteMoral.isChecked():
            datos = self.obtener_datos_cliente_moral()
            tipo_de_cliente = 'MORAL'
            if not self.validacion_campos_cliente_moral(datos):
                return
            #comment:_ obtener los datos de los campos numericos y checks
            credito_disponible = datos["limite del credito"]
            fecha_ultimo_reporte = fecha_actual.strftime("%Y/%m/%d")
            print(datos['fecha de constitucion'])

            with Conexion_base_datos() as db:
                session = db.abrir_sesion()
                with session.begin():
                    try:
                        id_categoria_cliente = CategoriaClienteModel(session).agregar(nombre = datos["clasificacion de cliente"])
                        id_area_de_negocio = AreaNegocioClientesModel(session).agregar_area(nombre = datos["area de negocio"])

                        nuevo_cliente = ClientesFisicosAndMorales(session).agregar_cliente_moral(
                            nombre=datos['nombre'], 
                            correo=datos['correo electronico empresa'],
                            rfc=datos['rfc'],
                            telefono=datos['numero telefono'],
                            pais=datos['pais'], 
                            estado=datos['estado'], 
                            ciudad=datos['ciudad'],
                            avenidas=datos["avenidas"],
                            calles=datos["calles"],
                            codigo_postal=datos['codigo postal'], 
                            direccion_adicional=datos['direccion adicional'], 
                            entidad_legalizada=datos["entidad legalizada"], 
                            categoria_cliente_id=id_categoria_cliente,
                            credito=datos["credito autorizado"], 
                            estado_credito=datos["estado del credito"], 
                            limite_credito=datos["limite del credito"], 
                            porcentaje_interes=datos["porcentaje del interes"],
                            fecha_ultimo_reporte=fecha_ultimo_reporte, 
                            credito_disponible=credito_disponible, 
                            credito_utilizado=datos["credito utilizado"], 
                            tipo_cliente=tipo_de_cliente, 
                            aplica_descuento=datos["descuento autorizado"], 
                            porcentaje_descuento = datos["porcentaje del descuento"],
                            comentarios = datos["comentarios"],
                            areas_de_negocios_id=id_area_de_negocio,
                            razon_social=datos["razon social"],
                            fecha_constitucion=datos["fecha de constitucion"],
                            web=datos["web"],
                            sector=datos["sector"],
                            nif=datos["numero de identificacion fiscal"]
                        )
                        
                        representante = ClientesFisicosAndMorales(session).agregar_representante_cliente_moral(
                            nombre=datos['representante moral'],
                            telefono=datos['telefono representante'],
                            correo=datos['correo electronico representante'],
                            puesto=datos['puesto del representante']
                        )

                        nuevo_cliente.representante = representante
                    except Exception as e:
                        print(f'No se logro hacer la creacion del cliente moral: ,  {str(e)}')
            self.tabla_listar_clientes()
            self.limpiar_campos()

    def actualizar_clientes(self):
        if self.ui.btnRadio_wpc_clienteFisico.isChecked():
            datos = self.obtener_datos_cliente_fisico()
            with Conexion_base_datos() as db:
                session = db.abrir_sesion()
                with session.begin():
                    try:
                        categoria_id = CategoriaClienteModel(session).agregar(datos["clasificacion cliente"])
                        print(categoria_id)
                        area_cliente_id = AreaNegocioClientesModel(session).agregar_area(datos["area de negocio"])
                        print(area_cliente_id)
                        print(self.id_cliente)
                        cliente = ClientesFisicosAndMorales(session).actualizar_cliente_fisico(
                            id = self.id_cliente,
                            nombre = datos['nombre'],
                            correo=datos["correo electronico"],
                            rfc=datos["rfc"],
                            telefono=datos["numero telefono"],
                            pais=datos["pais"],
                            estado=datos["estado"],
                            ciudad=datos["ciudad"],
                            avenidas=datos["avenidas"],
                            calles=datos["calles"],
                            codigo_postal=datos["codigo postal"],
                            direccion_adicional=datos["direccion adicional"],
                            entidad_legalizada=datos["entidad legalizada"],
                            categoria_cliente_id=categoria_id,
                            credito=datos["credito autorizado"],
                            estado_credito=datos["estado del credito"],
                            limite_credito=datos["limite del credito"],
                            porcentaje_interes=datos["porcentaje del interes"],
                            fecha_ultimo_reporte=datos["fecha del ultimo reporte"],
                            credito_disponible=datos["credito disponible"],
                            credito_utilizado=datos["credito utilizado"],
                            aplica_descuento=datos["aplica descuento"],
                            porcentaje_descuento=datos["porcentaje del descuento"],
                            comentarios=datos["comentarios"],
                            areas_de_negocios_id=area_cliente_id,
                            apellido_paterno=datos["apellido paterno"],
                            apellido_materno=datos["apellido materno"],
                            curp=datos["curp"],
                            fecha_nacimiento=datos["fecha de nacimiento"],
                            num_identificacion=datos["numero identificacion"],
                            ocupacion=datos["ocupacion"],
                            ingresos=datos["ingresos"],
                            estado_civil=datos["estado civil"],
                            foto=self.foto_cliente
                            
                        )
                        self.tabla_listar_clientes()
                        self.limpiar_campos()
                    except Exception as e:
                        print(f'No se logro hacer la actualizacion del cliente fisico: ,  {e}')

        elif self.ui.btnRadio_wpc_clienteMoral.isChecked():
            datos = self.obtener_datos_cliente_moral()
            with Conexion_base_datos() as db:
                session = db.abrir_sesion()
                with session.begin():
                    try:
                        categoria_id = CategoriaClienteModel(session).agregar(datos["clasificacion de cliente"])
                        area_cliente_id = AreaNegocioClientesModel(session).agregar_area(datos["area de negocio"])
                        cliente = ClientesFisicosAndMorales(session).actualizar_cliente_moral(
                            id = self.id_cliente,
                            nombre = datos['nombre'],
                            correo=datos["correo electronico empresa"],
                            rfc=datos["rfc"],
                            telefono=datos["numero telefono"],
                            pais=datos["pais"],
                            estado=datos["estado"],
                            ciudad=datos["ciudad"],
                            avenidas=datos["avenidas"],
                            calles=datos["calles"],
                            codigo_postal=datos["codigo postal"],
                            direccion_adicional=datos["direccion adicional"],
                            entidad_legalizada=datos["entidad legalizada"],
                            categoria_cliente_id=categoria_id,
                            credito=datos["credito autorizado"],
                            estado_credito=datos["estado del credito"],
                            limite_credito=datos["limite del credito"],
                            porcentaje_interes=datos["porcentaje del interes"],
                            fecha_ultimo_reporte=datos["fecha del ultimo reporte"],
                            credito_disponible=datos["credito disponible"],
                            credito_utilizado=datos["credito utilizado"],
                            aplica_descuento=datos["descuento autorizado"],
                            porcentaje_descuento=datos["porcentaje del descuento"],
                            comentarios=datos["comentarios"],
                            areas_de_negocios_id=area_cliente_id,
                            razon_social=datos["razon social"],
                            fecha_constitucion=datos["fecha de constitucion"],
                            web=datos["web"],
                            sector=datos["sector"],
                            nif=datos["numero de identificacion fiscal"],

                            nombre_representante=datos['representante moral'],
                            telefono_representante=datos['telefono representante'],
                            correo_representante=datos['correo electronico representante'],
                            puesto_representante=datos['puesto del representante']
                            ) 
                        self.tabla_listar_clientes()
                        self.limpiar_campos()
                    except Exception as e:
                        print(f'No se logro hacer la actualizacion del cliente moral: {e}')

    def eliminar_clientes(self):
        if self.ui.btnRadio_wpc_clienteFisico.isChecked():
            modelo = Clientes_fisicos
            id = self.id_cliente
            with Conexion_base_datos() as db:
                session = db.abrir_sesion()
                with session.begin():
                    try:
                        eliminar = ClientesFisicosAndMorales(session).eliminar_cliente(id, modelo)
                        if  eliminar:
                            Mensaje().mensaje_informativo("Se elimino el cliente de manera exitosa!")
                        else:
                            Mensaje().mensaje_alerta("No se logro hacer la operacion!")
                    except Exception as e:
                        print(f'No se logro eliminar el cliente fisico: {e}')

                self.tabla_listar_clientes()
                self.limpiar_campos()
        if self.ui.btnRadio_wpc_clienteMoral.isChecked():
            modelo = Clientes_morales
            id = self.id_cliente
            with Conexion_base_datos() as db:
                session = db.abrir_sesion()
                with session.begin():
                    try:
                        eliminar = ClientesFisicosAndMorales(session).eliminar_cliente(id, modelo)
                        if  eliminar:
                            Mensaje().mensaje_informativo("Se elimino el cliente de manera exitosa!")
                        else:
                            Mensaje().mensaje_alerta("No se logro hacer la operacion!")
                    except Exception as e:
                        print(f'No se logro eliminar el cliente fisico: {e}')
                self.tabla_listar_clientes()
                self.limpiar_campos()

    def nueva_area_cliente_fisico(self):
        self.ui_area_cliente_fisico =  AreaNegocioClientesController("Fisico")
        self.ui_area_cliente_fisico.show()
        self.ui_area_cliente_fisico.signal_area.connect(self.listar_areas)

    def nueva_area_cliente_moral(self):
        self.ui_area_cliente_fisico =  AreaNegocioClientesController("Moral")
        self.ui_area_cliente_fisico.show()
        self.ui_area_cliente_fisico.signal_area.connect(self.listar_areas)

    def listar_areas(self):
        if self.ui.btnRadio_wpc_clienteFisico.isChecked():
            self.ui.cajaopciones_areasnegocio_fisico.clear()
        else:
            self.ui.cajaopciones_areasnegocio_moral.clear()
        try:
            with Conexion_base_datos() as db:
                session = db.abrir_sesion()
                areas = AreaNegocioClientesModel(session).obtener_areas()
                if areas:
                    lista = [area.nombre for area in areas]
                    if self.ui.btnRadio_wpc_clienteFisico.isChecked():
                        self.ui.cajaopciones_areasnegocio_fisico.addItems(lista)
                        AjustarCajaOpciones().ajustar_cajadeopciones(self.ui.cajaopciones_areasnegocio_fisico)
                    else:
                        self.ui.cajaopciones_areasnegocio_moral.addItems(lista)
                        AjustarCajaOpciones().ajustar_cajadeopciones(self.ui.cajaopciones_areasnegocio_moral)
                else:
                    if self.ui.btnRadio_wpc_clienteFisico.isChecked():
                        self.ui.cajaopciones_areasnegocio_fisico.addItem("Sin Área")
                    else:
                        self.ui.cajaopciones_areasnegocio_moral.addItem("Sin Área")
        except Exception as e:
            print(e)

    def nueva_categoria(self):
        self.ui_categoria = CategoriaClienteController()
        self.ui_categoria.show()
        self.ui_categoria.signal_categoria_cliente.connect(self.listar_categorias)

    def listar_categorias(self):
        if self.ui.btnRadio_wpc_clienteFisico.isChecked():
            self.ui.cajaopciones_categoriaFisico.clear()
        else:
            self.ui.cajaopciones_categoriaMoral.clear()
        try:
            with Conexion_base_datos() as db:
                session = db.abrir_sesion()
                areas = CategoriaClienteModel(session).obtener_categorias()
                if areas:
                    lista = [area.nombre for area in areas]
                    if self.ui.btnRadio_wpc_clienteFisico.isChecked():
                        self.ui.cajaopciones_categoriaFisico.addItems(lista)
                        AjustarCajaOpciones().ajustar_cajadeopciones(self.ui.cajaopciones_categoriaFisico)
                    else:
                        self.ui.cajaopciones_categoriaMoral.addItems(lista)
                        AjustarCajaOpciones().ajustar_cajadeopciones(self.ui.cajaopciones_categoriaMoral)
                else:
                    if self.ui.btnRadio_wpc_clienteFisico.isChecked():
                        self.ui.cajaopciones_categoriaFisico.addItem("Sin Clasificación")
                    else:
                        self.ui.cajaopciones_categoriaMoral.addItem("Sin Clasificación")
        except Exception as e:
            print(e)

    def mostrar_contenedor_cliente_moral(self):
        if self.ui.btnRadio_wpc_clienteMoral.isChecked():
            self.listar_areas()
            self.listar_categorias()
            self.tabla_listar_clientes()
            self.ui.contenedor_clientfisico.hide()
            self.ui.contenedor_clientmoral.show()

    def mostrar_contenedor_cliente_fisico(self):
        if self.ui.btnRadio_wpc_clienteFisico.isChecked():
            self.listar_areas()
            self.listar_categorias()
            self.tabla_listar_clientes()
            self.ui.contenedor_clientmoral.hide()
            self.ui.contenedor_clientfisico.show()

    def activar_creditofisico(self):
        if self.ui.casillaverificacion_wpc_credito_autorizado.isChecked():
            self.ui.cajaDecimal_wpc_limite_credito.setEnabled(True)
        else:
            self.ui.cajaDecimal_wpc_limite_credito.setEnabled(False)

    def activar_creditomoral(self):
        if self.ui.casillaverificacion_wpc_credito_autorizado_moral.isChecked():
            self.ui.cajaDecimal_wpc_limite_credito_moral.setEnabled(True)
        else:
            self.ui.cajaDecimal_wpc_limite_credito_moral.setEnabled(False)


        