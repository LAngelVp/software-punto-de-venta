import threading
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QMessageBox, QWidget, QTableView
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from ..View.UserInterfacePy.UI_CONTROL_PROVEEDORES import Ui_Control_Proveedores
from .CategoriasProveedorController import CategoriasController
from ..Model.ProveedoresModel import ProveedoresModel
from ..Model.ProveedoresModel import ProveedoresModel
from ..DataBase.conexionBD import Conexion_base_datos
from ..Model.ValidacionesModel import Validaciones
from ..Model.CategoriasProveedorModel import CategoriaProveedorModel
from ..Model.RepresentanteProveedorModel import RepresentanteProveedorModel
from ..Model.BaseDatosModel import Proveedores
from .MensajesAlertasController import *
import logging

class Control_proveedores(QWidget):
    proveedor_seleccionado = pyqtSignal(str)
    def __init__(self):
        super().__init__()
        self.ui = Ui_Control_Proveedores()
        self.ui.setupUi(self)
        self.ejecutando_trabajo = False
        self.lista_categorias = {}
        
        self.ui.btnradio_representantefalse.setChecked(True)
        self.ui.contenedor_datosrepresentante.setVisible(False)
        self.ui.btnradio_representantetrue.toggled.connect(self.representante)
        self.ui.btn_btn_agregarcategoria.clicked.connect(self.nueva_categoria)
        self.ui.btn_btn_guardar.clicked.connect(self.control_agregar_proveedor)
        self.ui.btn_btn_limpiardatos.clicked.connect(self.limpiar_campos)
        self.ui.btn_btn_eliminar.clicked.connect(self.eliminar_proveedor)
        self.ui.txtlargo_descripcioncategoria.setReadOnly(True)
        # self.tabla.setEditTriggers(QTableWidget.NoEditTriggers)

        self.ui.btn_btn_buscarproveedor.clicked.connect(self.buscar_proveedor)
        self.ui.btn_btn_actualizar.clicked.connect(self.control_actualizar_proveedor)
        self.ui.cajaopciones_categorias.currentIndexChanged.connect(self.mostrar_descripcion_categoria)
        
        self.proveedor_seleccionado.connect(self.cargar_datos_proveedor)

        self.proveedores = None
        self.id_proveedor = None
        self.id_categoria = None
        self.id_representante = None
        self.lista_categorias = {}
        self.mostrar_categorias()
        self.listar_proveedores_tabla()

    def mostrar_categorias(self):
        try:
            with Conexion_base_datos() as db:
                session = db.abrir_sesion()  # Si tu método abrir_sesion() ya está gestionado dentro del contexto, esta línea es opcional
                try:
                    categorias = CategoriaProveedorModel(session).obtener_todas()
                except Exception as e:
                    session.rollback()

            self.lista_categorias = {categoria.nombre : categoria.descripcion for categoria in categorias}
            self.ui.cajaopciones_categorias.clear()
            self.ui.cajaopciones_categorias.addItems(self.lista_categorias.keys())
            self.mostrar_descripcion_categoria()
        except Exception as e:
            Mensaje().mensaje_alerta("Error")
    def mostrar_descripcion_categoria(self):
        categoria_seleccionada = self.ui.cajaopciones_categorias.currentText()
        descripcion = self.lista_categorias.get(categoria_seleccionada, '')
        self.ui.txtlargo_descripcioncategoria.setPlainText(descripcion)
#COMMENT METODO CORRECTO
    def limpiar_campos(self):
        self.ui.txt_nombre.clear()
        self.ui.txt_pais.clear()
        self.ui.txt_estado.clear()
        self.ui.txt_ciudad.clear()
        self.ui.txt_codigopostal.clear()
        self.ui.txt_calles.clear()
        self.ui.txt_avenida.clear()
        self.ui.txt_colonia.clear()
        self.ui.txtlargo_direccionadicional.clear()
        self.ui.txt_rfc.clear()
        self.ui.txt_web.clear()
        self.ui.txt_correo.clear()
        self.ui.txt_telefono.clear()
        self.ui.txt_nombrerepresentante.clear()
        self.ui.txt_apellidopaternorepresen.clear()
        self.ui.txt_apellidomaternorepresen.clear()
        self.ui.txt_telefonorepresentante.clear()
        self.ui.txt_correorepresentante.clear()
        self.ui.txt_puestorepresentante.clear()
        self.ui.btnradio_representantetrue.setChecked(False)
        self.ui.btnradio_representantefalse.setChecked(True)
        self.id_proveedor = None
        self.mostrar_categorias()
#COMMENT FUNCION CORRECTA
    def representante(self):
        if self.ui.btnradio_representantetrue.isChecked():
            self.ui.contenedor_datosrepresentante.setVisible(True)
        else:
            self.ui.contenedor_datosrepresentante.setVisible(False)
    def nueva_categoria(self):
        self.categorias = CategoriasController()
        self.categorias.categoria_agregada_signal.connect(self.mostrar_categorias)
        self.categorias.show()

        validaciones = {
            self.ui.txt_nombrerepresentante: Validaciones().get_text_validator,
            self.ui.txt_apellidopaternorepresen: Validaciones().get_text_validator,
            self.ui.txt_apellidomaternorepresen: Validaciones().get_text_validator,
            self.ui.txt_puestorepresentante: Validaciones().get_text_validator,
            self.ui.txt_correorepresentante: Validaciones().get_email_validator,
            self.ui.txt_telefonorepresentante: Validaciones().get_phone_validator,
        }

        for campo, validacion in validaciones.items():
            campo.setValidator(validacion)
    def obtener_datos_proveedor(self):
        datos = {
            'nombre': self.ui.txt_nombre.text().strip().upper(),
            'pais': self.ui.txt_pais.text().strip().upper(),
            'estado': self.ui.txt_estado.text().strip().upper(),
            'ciudad': self.ui.txt_ciudad.text().strip().upper(),
            'codigo_postal': self.ui.txt_codigopostal.text().strip().upper(),
            'calles': self.ui.txt_calles.text().strip().upper(),
            'avenidas': self.ui.txt_avenida.text().strip().upper(),
            'colonia': self.ui.txt_colonia.text().strip().upper(),
            'direccion_adicional': self.ui.txtlargo_direccionadicional.toPlainText().strip().upper(),
            'rfc': self.ui.txt_rfc.text().strip().upper(),
            'pagina_web': self.ui.txt_web.text().strip().upper(),
            'correo': self.ui.txt_correo.text().strip().upper(),
            'telefono': self.ui.txt_telefono.text().strip().upper(),
        }
        campos_vacios = [clave for clave, valor in datos.items() if not valor]

        if campos_vacios:
            return None
        return datos
    def obtener_datos_representante(self):
        datos = {
            'nombre': self.ui.txt_nombrerepresentante.text().strip().upper(),
            'apellido_paterno': self.ui.txt_apellidopaternorepresen.text().strip().upper(),
            'apellido_materno': self.ui.txt_apellidomaternorepresen.text().strip().upper(),
            'telefono': self.ui.txt_telefonorepresentante.text().strip().upper(),
            'correo': self.ui.txt_correorepresentante.text().strip().upper(),
            'puesto': self.ui.txt_puestorepresentante.text().strip().upper(),
        }
        campos_vacios = [clave for clave, valor in datos.items() if not valor]
        if campos_vacios:
            return None
        return datos
#comment agregamos proveedor
    def control_agregar_proveedor(self):
        datos_proveedor = self.obtener_datos_proveedor()
        print(datos_proveedor)
        datos_representante = self.obtener_datos_representante()
        print(datos_representante)
        categoria_nombre = self.ui.cajaopciones_categorias.currentText().strip()

        if not categoria_nombre:
            Mensaje().mensaje_alerta(cuerpo="La categoría no puede estar vacía.")
            return

        with Conexion_base_datos() as db:
            session = db.abrir_sesion()

            try:
                # Obtener la categoría
                categoria_id = CategoriaProveedorModel(session).obtener_id_por_nombre(nombre=categoria_nombre)
                if not categoria_id:
                    Mensaje().mensaje_alerta(cuerpo="La categoría seleccionada no existe.")
                    return
                proveedor_existente = ProveedoresModel(session).consultar_proveedor(datos_proveedor['nombre'])
                if  proveedor_existente:
                    Mensaje().mensaje_informativo(cuerpo="El proveedor ya existe.")
                    return

                # Agregar representante y proveedor
                if self.ui.btnradio_representantetrue.isChecked():
                    if not datos_representante or not datos_proveedor:
                        Mensaje().mensaje_alerta(cuerpo="Completa los registros.")
                        return

                    # Agregar representante y obtener su ID
                    id_representante = RepresentanteProveedorModel(session).agregar_representante(**datos_representante)

                    # Agregar proveedor con representante
                    ProveedoresModel(session).agregar_proveedor(
                        categoria_id=categoria_id,
                        representante_id=id_representante,
                        **datos_proveedor
                    )
                    session.commit()
                    print("Proveedor y representante agregados con éxito.")
                else:
                    if not datos_proveedor:
                        Mensaje().mensaje_alerta("Completa los datos del proveedor.")
                        return

                    # Agregar proveedor sin representante
                    ProveedoresModel(session).agregar_proveedor(
                        categoria_id=categoria_id,
                        representante_id=None,  # Sin representante
                        **datos_proveedor
                    )
                    session.commit()
                    print("Proveedor agregado con éxito.")
            except Exception as e:
                session.rollback()
                print(f'No se logró agregar el proveedor: {e}')
        self.listar_proveedores_tabla()
        self.limpiar_campos()

    def listar_proveedores_tabla(self):
        with Conexion_base_datos() as db:
            session = db.abrir_sesion()
            try:
                self.proveedores = ProveedoresModel(session).obtener_proveedores()
                self.llenar_tabla_proveedores(self.proveedores)
            except Exception as e:
                print(f"Error al listar proveedores: {e}")

    def llenar_tabla_proveedores(self, proveedores):
        try:
            # Verificar si la tabla está inicializada
            if self.ui.tabla_proveedores is None:
                print("El widget tabla no está disponible.")
                return
            
            
            nombre_columnas = [
                "ID",
                "Nombre",
                "País",
                "Estado",
                "Ciudad",
                "Código Postal",
                "Calles",
                "Avenidas",
                "Colonia",
                "Dirección Adicional",
                "RFC",
                "Página Web",
                "Correo",
                "Teléfono"
            ]

            self.model = QStandardItemModel()
            self.model.setHorizontalHeaderLabels(nombre_columnas)

            for row_index, proveedor in enumerate(proveedores):
                row_data = [
                    str(proveedor.id),
                    proveedor.nombre,
                    proveedor.pais,
                    proveedor.estado,
                    proveedor.ciudad,
                    proveedor.codigo_postal,
                    proveedor.calles,
                    proveedor.avenidas,
                    proveedor.colonia,
                    proveedor.direccion_adicional,
                    proveedor.rfc,
                    proveedor.pagina_web,
                    proveedor.correo,
                    proveedor.telefono
                ]
                items = [QStandardItem(item) for item in row_data]
                self.model.appendRow(items)
            # Asignar el modelo a la tabla
            self.ui.tabla_proveedores.setModel(self.model)
            self.proveedores = None
        except Exception as e:
            print(e)
            print(f'No se logro hacer la creacion del proveedor {e}')
        self.ui.tabla_proveedores.selectionModel().currentChanged.connect(self.obtener_id_elemento_tabla)

    def control_actualizar_proveedor(self):
        datos_proveedor = self.obtener_datos_proveedor()  # Obtén los datos del proveedor
        datos_representante = self.obtener_datos_representante()  # Obtén los datos del representante
        categoria_nombre = self.ui.cajaopciones_categorias.currentText().strip()  # Nombre de la categoría

        if not categoria_nombre:
            Mensaje().mensaje_alerta(cuerpo="La categoría no puede estar vacía.")
            return

        if self.id_proveedor:  # Verifica si tienes un ID de proveedor para actualizar
            with Conexion_base_datos() as db:
                session = db.abrir_sesion()

                try:
                    # Obtener la categoría por nombre y su ID
                    categoria_id = CategoriaProveedorModel(session).obtener_id_por_nombre(nombre=categoria_nombre)
                    if not categoria_id:
                        Mensaje().mensaje_alerta(cuerpo="La categoría seleccionada no existe.")
                        return

                    # Buscar el proveedor por su ID
                    proveedor_modelo = ProveedoresModel(session).obtener_proveedor_id(self.id_proveedor)
                    if not proveedor_modelo:
                        Mensaje().mensaje_alerta(cuerpo="El proveedor no existe.")
                        return

                    # Inicializar representante_id como None
                    representante_id = None

                    # Verificar y manejar los representantes
                    if self.ui.btnradio_representantetrue.isChecked():
                        # Si el proveedor tiene un representante, actualiza sus datos
                        if proveedor_modelo.representantes:
                            representante = proveedor_modelo.representantes[0]  # Supongo que solo hay un representante
                            representante_id = representante.id

                            if not datos_representante or not datos_proveedor:
                                Mensaje().mensaje_alerta(cuerpo="Completa los registros.")
                                return

                            # Actualiza el representante existente
                            RepresentanteProveedorModel(session).actualizar_representante(
                                id_representante=representante_id,  # Asegúrate de pasar el ID
                                **datos_representante
                            )
                            print("Datos del representante actualizados.")

                        else:
                            # Si no tiene representante, agrega uno nuevo y lo asocia al proveedor
                            if not datos_representante or not datos_proveedor:
                                Mensaje().mensaje_alerta(cuerpo="Completa los registros.")
                                return
                            
                            # Agrega un nuevo representante
                            representante_id = RepresentanteProveedorModel(session).agregar_representante(**datos_representante)
                            print("Nuevo representante agregado.")

                    elif self.ui.btnradio_representantefalse.isChecked():
                        # Si el botón de radio de no tener representante está chequeado,
                        # simplemente actualiza el proveedor sin representante
                        print("No se agregará un representante, solo se actualizará el proveedor.")

                    # Actualizar los datos del proveedor
                    ProveedoresModel(session).actualizar_proveedor(
                        proveedor_id=self.id_proveedor,
                        categoria_id=categoria_id,
                        representante_id=representante_id,
                        **datos_proveedor
                    )

                    session.commit()
                    print("Proveedor actualizado con éxito.")

                except Exception as e:
                    session.rollback()
                    print(f'No se logró actualizar el proveedor: {e}')

            # Actualiza la tabla de proveedores y limpia los campos
            self.listar_proveedores_tabla()
            self.limpiar_campos()

    def obtener_id_elemento_tabla(self, current, previus):
        # Verifica si la celda seleccionada está en la primera columna
        if current.column() == 0:  # Verifica si es la primera columna
            self.id_proveedor = current.data()  # Obtener el ID del proveedor
            self.proveedor_seleccionado.emit(self.id_proveedor)

    def cargar_datos_proveedor(self, id_proveedor):
        with Conexion_base_datos() as db:
            session = db.abrir_sesion()
            try:
                proveedor = ProveedoresModel(session).obtener_proveedor_id(id_proveedor)
                if proveedor is None:
                    self.mostrar_error(f"No se encontró el proveedor con ID: {id_proveedor}")
                    return
                
                # Cargar los datos en la UI
                self.ui.txt_nombre.setText(proveedor.nombre)
                self.ui.txt_pais.setText(proveedor.pais)
                self.ui.txt_estado.setText(proveedor.estado)
                self.ui.txt_ciudad.setText(proveedor.ciudad)
                self.ui.txt_codigopostal.setText(proveedor.codigo_postal)
                self.ui.txt_calles.setText(proveedor.calles)
                self.ui.txt_avenida.setText(proveedor.avenidas)
                self.ui.txt_colonia.setText(proveedor.colonia)
                self.ui.txtlargo_direccionadicional.setPlainText(proveedor.direccion_adicional)
                self.ui.txt_rfc.setText(proveedor.rfc)
                self.ui.txt_web.setText(proveedor.pagina_web)
                self.ui.txt_correo.setText(proveedor.correo)
                self.ui.txt_telefono.setText(proveedor.telefono)

                # Cargar categorías
                if proveedor.categorias:
                    self.ui.cajaopciones_categorias.clear()
                    for categoria in proveedor.categorias:
                        self.ui.cajaopciones_categorias.addItem(categoria.nombre) 

                # Cargar representantes
                if proveedor.representantes:
                    print(proveedor.representantes)
                    self.ui.btnradio_representantetrue.setChecked(True)
                    for representante in proveedor.representantes:
                        print(representante.nombre)
                        self.ui.txt_nombrerepresentante.setText(representante.nombre)
                        self.ui.txt_apellidopaternorepresen.setText(representante.apellido_paterno)
                        self.ui.txt_apellidomaternorepresen.setText(representante.apellido_materno)
                        self.ui.txt_correorepresentante.setText(representante.correo)
                        self.ui.txt_telefonorepresentante.setText(representante.telefono)
                        self.ui.txt_puestorepresentante.setText(representante.puesto)
                else:
                    self.ui.btnradio_representantefalse.setChecked(True)
                    # self.ui.contenedor_datosrepresentante.hide()
            except Exception as e:
                self.mostrar_error("Error al obtener proveedor : " + str(e))

    def buscar_proveedor(self):
        texto = self.ui.txt_buscarproveedor.text()  # Obtener el texto del campo de búsqueda
        conexion = Conexion_base_datos()
        with conexion as db:
            session = db.abrir_sesion()
            try:
                # Buscar los proveedores que coincidan con el texto de búsqueda
                proveedores = ProveedoresModel(session).obtener_nombre_proveedor(texto=texto)
                # Llamar a la función para llenar la tabla con los resultados de la búsqueda
                self.llenar_tabla_proveedores(proveedores)
            except Exception as e:
                self.mostrar_error(f"Error al buscar proveedores: {e}")

    def eliminar_proveedor(self):
        datos_proveedor = self.obtener_datos_proveedor()
        if not datos_proveedor:
            Mensaje().mensaje_alerta("o haz seleccionado un proveedor de la tabla para eliminarlo.")

        try:
            with Conexion_base_datos() as db:
                session = db.abrir_sesion()
                ProveedoresModel(session).eliminar_proveedor(self.id_proveedor)
                session.commit()
                self.listar_proveedores_tabla()
        except Exception as e:
            print(f"Error al eliminar proveedor: {e}")