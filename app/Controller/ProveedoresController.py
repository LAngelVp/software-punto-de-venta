import threading
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QMessageBox, QWidget, QTableView
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from app.View.UserInterfacePy.UI_CONTROL_PROVEEDORES import Ui_Control_Proveedores
from app.Controller.CategoriasController import CategoriasController
from app.Model.ProveedoresModel import ProveedoresModel
from app.Model.ProveedoresModel import ProveedoresModel
from app.DataBase.conexionBD import Conexion_base_datos
from app.Model.ValidacionesModel import Validaciones
from app.Model.CategoriasModel import CategoriasModel
from app.Model.RepresentanteProveedorModel import RepresentanteProveedorModel
from app.Model.BaseDatosModel import Proveedores
from app.Controller.MensajesAlertasController import *
from .AjustarCajaOpcionesGlobal import AjustarCajaOpciones
from .FuncionesAuxiliares import *
from .Productos_del_Proveedor import *
import traceback

class Control_proveedores(QWidget):
    PROVEEDOR_SELECCIONADO_SIGNAL = pyqtSignal(object)
    LISTAR_PROVEEDORES_EN_TABLA_SIGNAL = pyqtSignal()
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
        self.ui.btn_btn_listadeproductoyprecios.clicked.connect(self.mostrar_productos_y_precios)
        self.ui.txtlargo_descripcioncategoria.setReadOnly(True)
#comment : validaciones:

        self.ui.btn_btn_buscarproveedor.clicked.connect(self.buscar_proveedor)
        self.ui.btn_btn_actualizar.clicked.connect(self.control_actualizar_proveedor)
        self.ui.cajaopciones_categorias.currentIndexChanged.connect(self.mostrar_descripcion_categoria)
        
        self.ui.txt_nombre.setMaxLength(150)
        self.ui.txt_pais.setMaxLength(50)
        self.ui.txt_estado.setMaxLength(50)
        self.ui.txt_ciudad.setMaxLength(50)
        self.ui.txt_codigopostal.setMaxLength(5)
        self.ui.txt_calles.setMaxLength(60)
        self.ui.txt_avenida.setMaxLength(60)
        self.ui.txt_colonia.setMaxLength(50)
        self.ui.txt_rfc.setMaxLength(13)
        self.ui.txt_correo.setMaxLength(100)
        self.ui.txt_telefono.setMaxLength(10)
        # REPRESENTANTE
        self.ui.txt_nombrerepresentante.setMaxLength(100)
        self.ui.txt_apellidopaternorepresen.setMaxLength(60)
        self.ui.txt_apellidomaternorepresen.setMaxLength(60)
        self.ui.txt_telefonorepresentante.setMaxLength(10)
        self.ui.txt_correorepresentante.setMaxLength(100)
        self.ui.txt_puestorepresentante.setMaxLength(100)
        # VALIDACIONES
        self.ui.txt_telefono.setValidator(Validaciones().get_phone_validator)
        self.ui.txt_codigopostal.setValidator(Validaciones().get_int_validator)
        
        

        self.proveedores = None
        self.proveedor_seleccionado = None
        self.id_categoria = None
        self.representante = None
        self.seleccion_conectada_proveedores = None
        self.lista_categorias = {}
        

    def mostrar_productos_y_precios(self):
        if not self.proveedor_seleccionado:
            Mensaje().mensaje_informativo("No haz seleccionado un proveedor para poder visualizar la lista de productos y precios.")
            return
        if self.proveedor_seleccionado:
            self.ventana_productos_precios = Productos_de_proveedorController(self.proveedor_seleccionado)
            self.ventana_productos_precios.LISTAR_PRODUCTO_VINCULADOS_AL_PROVEEDOR.connect(self.ventana_productos_precios.mostrar_productos_proveedor)
            self.ventana_productos_precios.LISTAR_PRODUCTO_VINCULADOS_AL_PROVEEDOR.emit()
            self.ventana_productos_precios.show()
    
    def mostrar_categorias(self):
        with Conexion_base_datos() as db:
            session = db.abrir_sesion()
            with session.begin():
                categorias, estado = CategoriasModel(session).obtener_todo(tipo_categoria="proveedores")
                if estado:
                    self.ui.cajaopciones_categorias.clear()
                    for categoria in categorias:
                        self.ui.cajaopciones_categorias.addItem(categoria.nombre, (categoria.id, categoria.descripcion))
                    AjustarCajaOpciones().ajustar_cajadeopciones(self.ui.cajaopciones_categorias)
            
        self.mostrar_descripcion_categoria()
    
    def mostrar_descripcion_categoria(self):
        index_seleccion = self.ui.cajaopciones_categorias.currentIndex()

        # Si hay un ítem seleccionado válido
        if index_seleccion != -1:
            dato_seleccionado = self.ui.cajaopciones_categorias.currentData()

            # Verificar si currentData() devuelve datos válidos
            if dato_seleccionado is not None:
                # Acceder a la descripción (segundo valor de la tupla)
                descripcion = dato_seleccionado[1]
                self.ui.txtlargo_descripcioncategoria.setPlainText(descripcion)
            else:
                self.ui.txtlargo_descripcioncategoria.clear()  # Limpiar si no hay datos
        else:
            self.ui.txtlargo_descripcioncategoria.clear()

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
        self.ui.btnradio_representantefalse.setChecked(True)
        self.ui.btnradio_representantetrue.setChecked(False)
        self.proveedor_seleccionado = None
        self.representante = None
        self.mostrar_categorias()

#COMMENT FUNCION CORRECTA
    def representante(self):
        if self.ui.btnradio_representantetrue.isChecked():
            self.ui.contenedor_datosrepresentante.setVisible(True)
        else:
            self.ui.contenedor_datosrepresentante.setVisible(False)

    def nueva_categoria(self):
        self.categorias = CategoriasController(tipo_categoria="proveedores")
        self.categorias.categoria_agregada_signal.connect(self.mostrar_categorias)
        self.categorias.show()
    
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
            'clave_moneda': self.ui.cajaopciones_tipomoneda.currentText().upper().split(":")[0].strip(),
            'tipo_moneda': self.ui.cajaopciones_tipomoneda.currentText().upper().split(":")[1].strip()
        }
        campos_vacios = [clave for clave, valor in datos.items() if not valor]

        if campos_vacios:
            return None, campos_vacios
        return datos, None
    
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
        datos_proveedor, campos_vacios = self.obtener_datos_proveedor()
        datos_representante = self.obtener_datos_representante()
        categoriaid = self.ui.cajaopciones_categorias.currentData()[0]
        
        

        if not categoriaid:
            Mensaje().mensaje_alerta(cuerpo="La categoría no puede estar vacía.")
            return
        
        if datos_proveedor is None:
            # Si los datos son None, mostramos una alerta con los campos vacíos
            campos_faltantes = ', '.join(campos_vacios)  # Unir los nombres de los campos vacíos en un string
            Mensaje().mensaje_alerta(f"Completa los siguientes campos: {campos_faltantes}.")
            return  # Salir de la función si los datos no están completos

        with Conexion_base_datos() as db:
            session = db.abrir_sesion()
            with session.begin():
                try:

                    proveedor_existente, estado = ProveedoresModel(session).consultar_proveedor(datos_proveedor['nombre'])

                    if estado:
                        Mensaje().mensaje_informativo(cuerpo="El proveedor ya existe.")
                        return
                    # Agregar representante y proveedor
                    if self.ui.btnradio_representantetrue.isChecked():
                        if not datos_representante or not datos_proveedor:
                            Mensaje().mensaje_alerta(cuerpo="Completa los registros.")
                            return

                        # Agregar representante
                        self.represente, estado = RepresentanteProveedorModel(session).agregar_representante(**datos_representante)
                        if self.represente is not None:
                        # Agregar proveedor con representante
                            ProveedoresModel(session).agregar_proveedor(
                                categoria_id=categoriaid,
                                representante_id=self.represente.id,
                                **datos_proveedor
                            )
                        else:
                            Mensaje().mensaje_alerta("no se agrego el proveedor con reprentante")
                            return
                            
                    if self.ui.btnradio_representantefalse.isChecked():
                        # Agregar proveedor sin representante
                        print(categoriaid)
                        proveedor, status_proveedor = ProveedoresModel(session).agregar_proveedor(
                            categoria_id=categoriaid,
                            representante_id=None,  # Sin representante
                            **datos_proveedor
                        )
                        if not status_proveedor:
                            Mensaje().mensaje_informativo("No se logro agregar al proveedor")
                            return
                        Mensaje().mensaje_informativo("Proveedor agregado con éxito.")
                except Exception as e:
                    import traceback
                    print(traceback.format_exc)
                    Mensaje().mensaje_critico(f'No se logró agregar el proveedor: {e}')

        self.listar_proveedores_tabla()
        self.limpiar_campos()

    def listar_proveedores_tabla(self):
        estado = False
        with Conexion_base_datos() as db:
            session = db.abrir_sesion()
            with session.begin():
                self.proveedores, estado = ProveedoresModel(session).obtener_proveedores()
            if estado:
                self.llenar_tabla_proveedores(self.proveedores)

    def llenar_tabla_proveedores(self, proveedores = None):
        try:
            # Verificar si la tabla está inicializada
            if self.ui.tabla_proveedores is None:
                Mensaje().mensaje_critico("El widget tabla no está disponible.")
                return
            # Inicializar el modelo de la tabla si no existe
            if not hasattr(self, 'modelo_tabla_proveedores_vproveedores'):
                self.modelo_tabla_proveedores_vproveedores = QStandardItemModel()
            
            self.modelo_tabla_proveedores_vproveedores.clear()

            if proveedores is None:
                self.modelo_tabla_proveedores_vproveedores.setHorizontalHeaderLabels([
                    "id",
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
                    ])
                self.ui.tabla_proveedores.setModel(self.modelo_tabla_proveedores_vproveedores)
                return
            
            nombre_columnas = [
                "id",
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

            self.modelo_tabla_proveedores_vproveedores.setHorizontalHeaderLabels(nombre_columnas)

            for proveedor in proveedores:
                if proveedor is not None:
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
                for item in items:
                    item.setData(proveedor, Qt.UserRole)
                self.modelo_tabla_proveedores_vproveedores.appendRow(items)

            self.ui.tabla_proveedores.setModel(self.modelo_tabla_proveedores_vproveedores)
            self.ui.tabla_proveedores.setColumnHidden(0, True)

            # Desconectar la señal antes de conectar
            if self.seleccion_conectada_proveedores:
                self.ui.tabla_proveedores.selectionModel().currentChanged.disconnect(self.obtener_proveedor_seleccionado_tabla)
                self.seleccion_conectada_proveedores = False  # Actualizar el estado

            # Conectar la señal a la función que obtiene el ID del elemento seleccionado
            self.ui.tabla_proveedores.selectionModel().currentChanged.connect(self.obtener_proveedor_seleccionado_tabla)
            self.seleccion_conectada_proveedores = True  # Marcar como conectada

        except Exception as e:
            Mensaje().mensaje_critico(f'No se logro hacer el listado de los proveedores: {e}')

    def control_actualizar_proveedor(self):
        # Obtén los datos del proveedor y del representante
        datos_proveedor, campos_vacios = self.obtener_datos_proveedor()
        datos_representante = self.obtener_datos_representante()

        # Obtén el nombre de la categoría seleccionada
        categoria_nombre = self.ui.cajaopciones_categorias.currentText().strip()

        # Verifica si la categoría está vacía
        if not categoria_nombre:
            Mensaje().mensaje_alerta(cuerpo="La categoría no puede estar vacía.")
            return
        
        if datos_proveedor is None:
            # Si los datos son None, mostramos una alerta con los campos vacíos
            campos_faltantes = ', '.join(campos_vacios)  # Unir los nombres de los campos vacíos en un string
            Mensaje().mensaje_alerta(f"Completa los siguientes campos: {campos_faltantes}.")
            return  # Salir de la función si los datos no están completos

        if self.proveedor_seleccionado.id:  # Verifica si hay un ID de proveedor para actualizar
            with Conexion_base_datos() as db:
                session = db.abrir_sesion()
                with session.begin():
                    try:
                        # Obtener la categoría por su nombre
                        categoria_id = CategoriasModel(session).obtener_id_por_nombre(tipo_categoria="proveedores", nombre=categoria_nombre)
                        if not categoria_id:
                            Mensaje().mensaje_alerta(cuerpo="La categoría seleccionada no existe.")
                            return

                        # Buscar el proveedor por su ID
                        proveedor_modelo, estado = ProveedoresModel(session).obtener_proveedor_id(self.proveedor_seleccionado.id)
                        if not proveedor_modelo:
                            Mensaje().mensaje_alerta(cuerpo="El proveedor no existe.")
                            return

                        # Inicializar representante_dato como None
                        representante_dato = None

                        # Verificar si se ha marcado el proveedor con representante
                        if self.ui.btnradio_representantetrue.isChecked():
                            # Si el proveedor ya tiene un representante, se actualizan sus datos
                            if proveedor_modelo.representante:
                                representante = proveedor_modelo.representante
                                representante_dato = representante  # Asumimos que hay un solo representante

                                # Verifica que ambos registros (proveedor y representante) estén completos
                                if not datos_representante or not datos_proveedor:
                                    Mensaje().mensaje_alerta(cuerpo="Completa los registros.")
                                    return

                                # Actualizar los datos del representante
                                RepresentanteProveedorModel(session).actualizar_representante(
                                    id_representante=representante_dato.id,
                                    **datos_representante
                                )
                                Mensaje().mensaje_informativo("Datos del representante actualizados.")

                            else:
                                # Si no tiene representante, se agrega uno nuevo
                                if not datos_representante or not datos_proveedor:
                                    Mensaje().mensaje_alerta(cuerpo="Completa los registros.")
                                    return
                                
                                # Agregar un nuevo representante
                                representante_dato, estado = RepresentanteProveedorModel(session).agregar_representante(**datos_representante)
                                Mensaje().mensaje_informativo("Nuevo representante agregado.")

                        elif self.ui.btnradio_representantefalse.isChecked():
                            # Si no se tiene representante, se indicará y solo se actualizarán los datos del proveedor
                            Mensaje().mensaje_informativo("No se agregará un representante, solo se actualizará el proveedor.")

                        # Actualizar los datos del proveedor
                        ProveedoresModel(session).actualizar_proveedor(
                            proveedor_id=self.proveedor_seleccionado.id,
                            categoria_id=categoria_id,
                            representante_id=representante_dato.id if representante_dato else None,  # Usamos None si no hay representante
                            **datos_proveedor
                        )
                        Mensaje().mensaje_informativo("Proveedor actualizado con éxito.")

                    except Exception as e:
                        session.rollback()
                        # Añadir más detalles sobre el error
                        Mensaje().mensaje_critico(f'No se logró actualizar el proveedor: {e}')

            # Actualiza la tabla de proveedores y limpia los campos
            self.listar_proveedores_tabla()
            self.limpiar_campos()

    def obtener_proveedor_seleccionado_tabla(self, current, previus):
        self.limpiar_campos()
        # Verifica si la celda seleccionada está en la primera columna
        if current.column() > 0:  # Verifica si es la primera columna
            indice_fila = current.row()
            elemento = self.modelo_tabla_proveedores_vproveedores.item(indice_fila, 0)
            if elemento is not None:
                proveedor = elemento.data(Qt.UserRole)
                if proveedor:
                    self.proveedor_seleccionado = proveedor
                    self.cargar_datos_proveedor(self.proveedor_seleccionado)
            else:
                return

    def cargar_datos_proveedor(self, proveedor):
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
        
        if proveedor.categoria:
            nombre = None
            nombre = proveedor.categoria.nombre
            FuncionesAuxiliaresController().caja_opciones_mover_elemento(self.ui.cajaopciones_categorias, nombre)
        
        if proveedor.clave_moneda:
            nombre = f'{proveedor.clave_moneda}: {proveedor.tipo_moneda}'
            FuncionesAuxiliaresController().caja_opciones_mover_elemento(self.ui.cajaopciones_tipomoneda, nombre)
        
            
            # # Obtener el QComboBox
            # caja_categorias = self.ui.cajaopciones_categorias
            # caja_categorias.clear()  # Limpiar elementos existentes

            # # Crear un conjunto para rastrear categorías ya añadidas
            # categorias_agregadas = set()

            # for categoria in proveedor.categorias:
            #     categoria_nombre = categoria.nombre
                
            #     # Verificar si la categoría ya ha sido añadida
            #     if categoria_nombre not in categorias_agregadas:
            #         # Insertar la nueva categoría en la posición 0
            #         caja_categorias.insertItem(0, categoria_nombre)
            #         # Agregar la categoría al conjunto
            #         categorias_agregadas.add(categoria_nombre)

        # Cargar representantes
        if proveedor.representante:
            self.ui.btnradio_representantetrue.setChecked(True)
            self.ui.txt_nombrerepresentante.setText(proveedor.representante.nombre)
            self.ui.txt_apellidopaternorepresen.setText(proveedor.representante.apellido_paterno)
            self.ui.txt_apellidomaternorepresen.setText(proveedor.representante.apellido_materno)
            self.ui.txt_correorepresentante.setText(proveedor.representante.correo)
            self.ui.txt_telefonorepresentante.setText(proveedor.representante.telefono)
            self.ui.txt_puestorepresentante.setText(proveedor.representante.puesto)
        else:
            self.ui.btnradio_representantefalse.setChecked(True)
            # self.ui.contenedor_datosrepresentante.hide()

    def buscar_proveedor(self):
        texto = self.ui.txt_buscarproveedor.text()
        with Conexion_base_datos() as db:
            session = db.abrir_sesion()
            with session.begin():
                proveedores = ProveedoresModel(session).obtener_nombre_proveedor(texto=texto)
            if proveedores:
                self.llenar_tabla_proveedores(proveedores)

    def eliminar_proveedor(self):
        datos_proveedor = self.obtener_datos_proveedor()
        if not self.proveedor_seleccionado:
            Mensaje().mensaje_alerta("No haz seleccionado un proveedor de la tabla para eliminarlo.")
            return
        try:
            with Conexion_base_datos() as db:
                session = db.abrir_sesion()
                with session.begin():
                    respuesta = ProveedoresModel(session).eliminar_proveedor(self.proveedor_seleccionado.id)
                    if not respuesta:
                        Mensaje().mensaje_alerta("No se pudo eliminar el proveedor")
                        return
            self.listar_proveedores_tabla()
            self.limpiar_campos()
        except Exception as e:
            Mensaje().mensaje_critico(f"Error al eliminar proveedor: {e}")

