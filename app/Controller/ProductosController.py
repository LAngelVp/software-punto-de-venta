from ..Source.iconsdvg_rc import *
from ..Source.iconosSVG_rc import *
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QValidator, QStandardItemModel, QStandardItem, QPixmap, QIcon, QCursor
from .FuncionesAuxiliares import FuncionesAuxiliaresController
from .AjustarCajaOpcionesGlobal import AjustarCajaOpciones
from ..DataBase.conexionBD import Conexion_base_datos
from ..Model.ProveedoresModel import ProveedoresModel
from ..Model.CategoriasModel import CategoriasModel
from ..Model.ProductosModel import ProductosModel
from ..Model.UsuarioModel import UsuarioModel
from .MensajesAlertasController import Mensaje
from .CategoriasController import CategoriasController
from ..View.UserInterfacePy.UI_CONTROL_PRODUCTOS import Ui_Control_Productos
from ..View.UserInterfacePy.UI_AGREGARPRODUCTO import Ui_contenedor_agregar_productos
from ..View.UserInterfacePy.UI_NUEVA_CATEGORIA import Ui_Nueva_categoria
from ..View.UserInterfacePy.UI_EXISTENCIA_PRODUCTOS import Ui_UI_EXISTENCIA_PRODUCTO
from .PresentacionProductosController import PresentacionProductos
from .UnidadMedidaProductosController import UnidadMedidaProductos

from .Hilo_consultas import *
from .Ventana_espera import *
import traceback

class ExistenciasClase(QWidget):
    VENTANA_CERRADA_EXISTENCIA = pyqtSignal()
    RECIBIR_PRODUCTO_ID_EXISTENCIA = pyqtSignal(object)
    def __init__(self, parent = None, datos_usuario = None):
        super().__init__(parent)
        self._ventanaCentrada = False
        self.datos_usuario = datos_usuario
        self.producto = None
        self.consultor = None
        self.cargando = None
        self.codigo_producto_upc = None
        self.ui = Ui_UI_EXISTENCIA_PRODUCTO()
        self.ui.setupUi(self)
        self.ui.fecha_FechaMovimiento.setDate(QDate.currentDate())
        self.ui.btn_existenciaProducto_aceptar.clicked.connect(self.ejecutar_existencias)
        self.ui.btn_existenciaProducto_cerrar.clicked.connect(self.close)
        self.RECIBIR_PRODUCTO_ID_EXISTENCIA.connect(self.mostrar_datos_en_ui)
        
    def showEvent(self, event):
        super().showEvent(event)
        if not self._ventanaCentrada:
            FuncionesAuxiliaresController.centrar_en_padre(self)
            self._ventanaCentrada = True
    
    def closeEvent(self, event):
        self.VENTANA_CERRADA_EXISTENCIA.emit() 
        event.accept()
        
    def mostrar_datos_en_ui(self, producto):
        print(f"este es el producto {self.producto}")
        self.producto = producto
        if self.producto:
            self.ui.etiqueta_ClaveProducto.setText(self.producto.codigo_upc)
            self.ui.etiqueta_NombreUsuario.setText(self.datos_usuario["nombre_empleado"])
            
    def ejecutar_existencias(self):
        cant_existencia = self.ui.decimal_CantidadExistencia.value()
        tipo_movimiento = self.ui.cajaOpciones_TipoMovimiento.currentText()
        fecha_movimiento = self.ui.fecha_FechaMovimiento.date().toString('yyyy-MM-dd')
        notas = self.ui.txtlargo_NotasProducto.toPlainText()
        if cant_existencia != 0:
            with Conexion_base_datos() as db:
                session = db.abrir_sesion()
                with session.begin():
                    movimiento, estatus_movimiento = ProductosModel(session).ejecutar_movimiento(
                        producto_id=self.producto.id,
                        cantidad_cambio=cant_existencia,
                        tipo_movimiento=tipo_movimiento,
                        fecha_movimiento=fecha_movimiento,
                        notas=notas,
                        usuarioid=self.datos_usuario["id_empleado"])
                if not estatus_movimiento:
                    Mensaje().mensaje_alerta("No se logro realizar el movimiento de la existencia.")
                    return
        Mensaje().mensaje_informativo("Se realizo el movimiento correctamente.")
        return
class Admin_productosController(QWidget):
    PRODUCTOS_AGREGADOS = pyqtSignal()
    RECIBIR_PRODUCTO_ACTUALIZAR_ID = pyqtSignal(object)
    VENTANA_CERRADA_PRODUCTOS = pyqtSignal()
    
    def __init__(self, parent = None):
        super().__init__(parent)
        # # Asegurar que no hay translucidez
        self.setAttribute(Qt.WA_TranslucentBackground, False)
        self.ui = Ui_contenedor_agregar_productos()
        self.ui.setupUi(self)
        # self.setStyleSheet(self.styleSheet())
        icon = QIcon(':Icons/IconosSVG/productos.png')
        self.setWindowIcon(icon)
        self.setWindowTitle("Administración de productos")
#// EDICION DE COMPONENTES:
        self.ui.fecha_fabricacionProducto.setDate(QDate.currentDate())
        self.ui.fecha_vencimientoProducto.setDate(QDate.currentDate())
        self.ui.contenedor_proveedores_vinculados.hide()
        self.ui.btn_btn_addProduct_actualizar_producto.hide()
        self.ui.contenedor_proveedores_existentes.hide()
        self.ui.contenedor_proveedores_a_vincular.hide()
        self.ui.contenedor_contenedorFechaCaducidad.hide()
        self.ui.txt_codBarras.setFocus()
        
#// Validaciones:
        self.ui.txt_codBarras.setMaxLength(255)
        self.ui.txt_nombreProducto.setMaxLength(255)
        self.ui.txt_marcaProducto.setMaxLength(100)
        self.ui.txt_modeloProducto.setMaxLength(50)
        self.ui.txt_colorProducto.setMaxLength(20)
        self.ui.txt_materialProducto.setMaxLength(255)
        
#// variables globales:
        self.consultor = None
        self.cargando = None
        self.producto = None
        self.id_proveedor = None
        self.imagenProducto = None
        self.producto = None
        self.productos_no_agregados = []
        self.codigo_producto_upc_recibido = None
        self.lista_productos = []
        self.lista_proveedores_a_asignar = {}
        self.proveedores_vinculados = {}
        self.proveedores_no_vinculados = {}
        self.proveedores_generales_del_sistema_dict = {}
        self._ventanaCentradaProductoExistente = False 
        self._translate = QtCore.QCoreApplication.translate
#// funciones principales:
        self.comprobar_existencia_modelo_tabla()
#// señales:
        self.ui.txt_proveedor.textChanged.connect(self.__proveedor_seleccionado)
        self.ui.etiqueta_fotoProducto.mousePressEvent = self.cargar_imagen
#// botones de ventana:
        self.RECIBIR_PRODUCTO_ACTUALIZAR_ID.connect(self.__cargar_datos_en_campos)
        self.ui.btn_btn_addProduct_actualizar_producto.clicked.connect(self.__actualizar_producto)
        self.ui.btn_btn_addProduct_agregar_categoria.clicked.connect(self.__agregar_categoria)
        self.ui.btn_btn_addProduct_agregar_unidadMedidaProducto.clicked.connect(self.agregar_unidad_medida)
        self.ui.btn_btn_addProduct_agregarPresentacionProducto.clicked.connect(self.agregar_presentacion)
        self.ui.btn_btn_addProduct_agregar_producto.clicked.connect(self.__agregar_producto)
        self.ui.btn_btn_addProduct_guardar_producto.clicked.connect(self.__guardar_producto)
        self.ui.btn_btn_addProduct_limpiarTablaProductos.clicked.connect(self.__limpiar_tabla_productos)
        self.ui.btn_btn_addProduct_cargar_CSVProductos.clicked.connect(self.__leer_archivo_csv)
        self.ui.txt_buscar_proveedor_a_vincular.returnPressed.connect(self.buscar_proveedor_existente)
        self.ui.txt_buscar_proveedor_vinculado.returnPressed.connect(self.buscar_proveedor_vinculado)
        self.ui.lista_todos_los_proveedores.itemClicked.connect(self.vincular_proveedor_al_producto)
        self.ui.btn_btn_addProduct_desvincular_proveedores.clicked.connect(self.desvincular_proveedor_al_producto)
        self.ui.btn_btn_addProduct_eliminar_proveedor_a_vincular.clicked.connect(self.eliminar_proveedor_a_vincular)
        self.ui.entero_margenProducto.editingFinished.connect(self.calcular_precio_venta)
        self.ui.opcion_TieneCaducidad.stateChanged.connect(self.mostrar_fechas_caducidad)
        self.ui.btn_btn_addProduct_cerrar.clicked.connect(self.close)

        completar = QCompleter([proveedor.nombre for proveedor in self.proveedores_generales_del_sistema_dict.values()])
        completar.setCaseSensitivity(Qt.CaseInsensitive)
        self.ui.txt_proveedor.setCompleter(completar)

    def showEvent(self, event):
        super().showEvent(event)
        if not self._ventanaCentradaProductoExistente:
            FuncionesAuxiliaresController.centrar_en_padre(self)
            self._ventanaCentradaProductoExistente = True

    def closeEvent(self, event):
        self.VENTANA_CERRADA_PRODUCTOS.emit() 
        event.accept()
        
#FUNCIONES-VENTANAS EMERGENTES: 
    def agregar_presentacion(self):
        self.ui_presentacion = PresentacionProductos()
        self.ui_presentacion.SYGNAL_PRESENTACION_AGREGADA.connect(self.listar_presentaciones_productos)
        self.ui_presentacion.show()

    def agregar_unidad_medida(self):
        self.ui_unidad_medida = UnidadMedidaProductos()
        self.ui_unidad_medida.SYGNAL_UNIDAD_MEDIDA_AGREGADA.connect(self.listar_unidades_medida)
        self.ui_unidad_medida.show()

    def __agregar_categoria(self):
        self.categoria = CategoriasController(tipo_categoria="productos")
        self.categoria.categoria_agregada_signal.connect(self.listar_categorias)
        self.categoria.show()

    def listar_presentaciones_productos(self):
        with Conexion_base_datos() as db:
            session = db.abrir_sesion()
            with session.begin():
                datos, estatus = ProductosModel(session).obtener_presentaciones()
            if estatus:
                self.ui.cajaOpciones_presentacionProducto.clear()
                for presentacion in datos:
                    self.ui.cajaOpciones_presentacionProducto.addItem(presentacion.nombre, presentacion)
                AjustarCajaOpciones(ProductosModel(session)).ajustar_cajadeopciones(self.ui.cajaOpciones_presentacionProducto)

    def listar_unidades_medida(self):
        with Conexion_base_datos() as db:
            session = db.abrir_sesion()
            with session.begin():
                datos, estatus = ProductosModel(session).obtener_unidades_medida()
            if estatus:
                self.ui.cajaOpciones_unidadMedidaProducto.clear()
                for unidad in datos:
                    self.ui.cajaOpciones_unidadMedidaProducto.addItem(unidad.nombre, unidad)
                AjustarCajaOpciones(ProductosModel(session)).ajustar_cajadeopciones(self.ui.cajaOpciones_unidadMedidaProducto)

    def listar_categorias(self):
        with Conexion_base_datos() as db:
            session = db.abrir_sesion()
            with session.begin():
                categorias, estatus = CategoriasModel(session).obtener_todo(tipo_categoria="productos")
            if estatus:
                self.ui.cajaOpciones_categoriaProducto.clear()
                for categoria in categorias:
                    self.ui.cajaOpciones_categoriaProducto.addItem(categoria.nombre, categoria)
                AjustarCajaOpciones(CategoriasModel(session), 'productos').ajustar_cajadeopciones(self.ui.cajaOpciones_categoriaProducto)
                
    
#########################
#FUNCIONES-INTERACCION CON EL PRODUCTO
    def mostrar_fechas_caducidad(self, state):
        if state in [1, 2]:
            self.ui.contenedor_contenedorFechaCaducidad.show()
        else:  # Si está desmarcado
            self.ui.contenedor_contenedorFechaCaducidad.hide()

    def campos_productos(self):
        # Crear un diccionario para almacenar los widgets
        datos = {
            "proveedor": self.ui.txt_proveedor,
            "codigo_barras": self.ui.txt_codBarras,
            "nombre": self.ui.txt_nombreProducto,
            "categoria_producto": self.ui.cajaOpciones_categoriaProducto,
            "marca_producto": self.ui.txt_marcaProducto,
            "modelo_producto": self.ui.txt_modeloProducto,
            "color_producto": self.ui.txt_colorProducto,
            "material_producto": self.ui.txt_materialProducto,
            "unidad_medida_producto": self.ui.cajaOpciones_unidadMedidaProducto,
            "presentacion_producto": self.ui.cajaOpciones_presentacionProducto,
            "costo_inicial_producto": self.ui.decimal_costoInicialProducto,
            "costo_final_producto": self.ui.decimal_costoFinalProducto,
            "margen_porcentaje": self.ui.entero_margenProducto,
            "precio_venta_producto": self.ui.decimal_precioVentaProducto,
            "existencia_producto": self.ui.decimal_existenciaProducto,
            "existencia_min_producto": self.ui.decimal_existenciaMinProducto,
            "existencia_max_producto": self.ui.decimal_existenciaMaxProducto,
            "peso_producto": self.ui.decimal_pesoProducto,
            "largo_dimensiones": self.ui.decimal_largoDimensiones,
            "alto_dimensiones": self.ui.decimal_altoDimensiones,
            "ancho_dimensiones": self.ui.decimal_anchoDimensiones,
            "descripcion_producto": self.ui.txtlargo_descripcionProducto,
            "notas_producto": self.ui.txtlargo_notasProducto,
            "fecha_vencimiento_producto": self.ui.fecha_vencimientoProducto,
            "fecha_fabricacion_producto": self.ui.fecha_fabricacionProducto,
        }
        
        # Retornar el diccionario con los widgets
        return datos

    def __limpiar_campos(self):
        datos = self.campos_productos()
        for campo in datos.values():
            if isinstance(campo, QLineEdit):
                campo.clear()
            elif isinstance(campo, QDoubleSpinBox):
                campo.setValue(0)
            elif isinstance(campo, QPlainTextEdit):
                campo.clear()
            elif isinstance(campo, QDateEdit):
                campo.setDate(QDate.currentDate())
        _translate = QtCore.QCoreApplication.translate
        self.ui.etiqueta_fotoProducto.setText(_translate("contenedor_agregar_productos", "<html><head/><body><p align=\"center\"><img src=\":/Icons/IconosSVG/subir_imagen.png\" width=\"80\" height=\"70\"/></p><p align=\"center\"><span style=\" font-size:16pt; font-family:Arial; font-weight:bold;\">Cargar Imagen</span></p></body></html>"))

    def cargar_imagen(self, event):
        options = QFileDialog.Options()
        self.imagenProducto, _ = QFileDialog.getOpenFileName(self, 'SELECCIONA UNA IMAGEN', ' ', 'Archivo de Imagen (*.png *.jpg *.jpeg);; Todos los archivos (*)', options=options)
        image_accept = FuncionesAuxiliaresController().size_validator_image(self.imagenProducto)
        if self.imagenProducto:
            if image_accept:
                self.ui.etiqueta_fotoProducto.setText(self.imagenProducto)
                pixmap = QPixmap(self.imagenProducto)
                self.ui.etiqueta_fotoProducto.setPixmap(pixmap)
                self.ui.etiqueta_fotoProducto.setScaledContents(True)
                self.ui.etiqueta_fotoProducto.adjustSize()
            else:
                Mensaje().mensaje_alerta("El tamaño de la imagen sobre pasa los 5Mb")
        return
    
    def datos_campos(self):
        # Crear un diccionario para almacenar los valores de los campos
        datos = {
            "proveedor": self.ui.txt_proveedor.text().strip(),
            "codigo_barras": self.ui.txt_codBarras.text().strip(),
            "nombre": self.ui.txt_nombreProducto.text().strip(),
            "categoria_producto": self.ui.cajaOpciones_categoriaProducto.currentData(),
            "marca_producto": self.ui.txt_marcaProducto.text().strip(),
            "modelo_producto": self.ui.txt_modeloProducto.text().strip(),
            "color_producto": self.ui.txt_colorProducto.text().strip(),
            "material_producto": self.ui.txt_materialProducto.text().strip(),
            "unidad_medida_producto": self.ui.cajaOpciones_unidadMedidaProducto.currentData(),
            "presentacion_producto": self.ui.cajaOpciones_presentacionProducto.currentData(),
            "costo_inicial_producto": self.ui.decimal_costoInicialProducto.value(),
            "margen_porcentaje": self.ui.entero_margenProducto.value(),
            "precio_venta_producto": self.ui.decimal_precioVentaProducto.value(),
            "costo_final_producto": self.ui.decimal_costoFinalProducto.value(),
            "existencia_producto": self.ui.decimal_existenciaProducto.value(),
            "existencia_min_producto": self.ui.decimal_existenciaMinProducto.value(),
            "existencia_max_producto": self.ui.decimal_existenciaMaxProducto.value(),
            "peso_producto": self.ui.decimal_pesoProducto.value(),
            "largo_dimensiones": self.ui.decimal_largoDimensiones.value(),
            "alto_dimensiones": self.ui.decimal_altoDimensiones.value(),
            "ancho_dimensiones": self.ui.decimal_anchoDimensiones.value(),
            "descripcion_producto": self.ui.txtlargo_descripcionProducto.toPlainText(),
            "notas_producto": self.ui.txtlargo_notasProducto.toPlainText(),
            "fecha_vencimiento_producto": self.ui.fecha_vencimientoProducto.date().toString('yyyy-MM-dd'),
            "fecha_fabricacion_producto": self.ui.fecha_fabricacionProducto.date().toString('yyyy-MM-dd'),
        }
        return datos
        
    def __agregar_producto(self):
        datos = self.datos_campos()
        if not datos["codigo_barras"]:
            Mensaje().mensaje_alerta("El campo Código de Barras es obligatorio")
            return
        
        self.comprobar_existencia_modelo_tabla()

        self.modelo_tabla_productos.setHorizontalHeaderLabels([
            "Proveedor", "Código de Barras", "Nombre", "Categoría", "Marca", "Modelo", "Color", 
            "Material", "Unidad de Medida", "Presentación", "Costo Inicial","Costo Final", "Margen Porcentaje", "Precio Venta", 
            "Existencia", "Existencia Min", "Existencia Max", "Peso", 
            "Largo Dimensiones", "Alto Dimensiones", "Ancho Dimensiones", 
            "Descripción", "Notas", "Fecha Vencimiento", "Fecha Fabricación", "Imagen"
        ])
        self.ui.tabla_productos.setModel(self.modelo_tabla_productos)
        
        # Crear un diccionario con los datos del producto
        nuevo_producto = {
            "proveedor": datos["proveedor"],
            "codigo_barras": datos["codigo_barras"],
            "nombre": datos["nombre"],
            "categoria": datos["categoria_producto"].nombre,
            "marca": datos["marca_producto"],
            "modelo": datos["modelo_producto"],
            "color": datos["color_producto"],
            "material": datos["material_producto"],
            "unidad_medida": datos["unidad_medida_producto"].nombre,
            "presentacion": datos["presentacion_producto"].nombre,
            "costo_inicial": datos["costo_inicial_producto"],
            "precio_venta": datos["precio_venta_producto"],
            "margen_porcentaje": datos["margen_porcentaje"],
            "costo_final": datos["costo_final_producto"],
            "existencia": datos["existencia_producto"],
            "existencia_min": datos["existencia_min_producto"],
            "existencia_max": datos["existencia_max_producto"],
            "peso": datos["peso_producto"],
            "largo_dimensiones": datos["largo_dimensiones"],
            "alto_dimensiones": datos["alto_dimensiones"],
            "ancho_dimensiones": datos["ancho_dimensiones"],
            "descripcion": datos["descripcion_producto"],
            "notas": datos["notas_producto"],
            "fecha_vencimiento": datos["fecha_vencimiento_producto"] if self.ui.opcion_TieneCaducidad.isChecked() else None,
            "fecha_fabricacion": datos["fecha_fabricacion_producto"] if self.ui.opcion_TieneCaducidad.isChecked() else None,
            "imagen": self.imagenProducto  
        }
        
        producto_existente = any(p["codigo_barras"] == nuevo_producto["codigo_barras"] for p in self.lista_productos)
        if not producto_existente:
            self.lista_productos.append(nuevo_producto)
        else:
            Mensaje().mensaje_alerta(f"El producto con código de barras {nuevo_producto['codigo_barras']} que intentas agregar ya existe en la lista")
            return
        
        nueva_fila = list(nuevo_producto.values())
        self._agregar_fila_a_tabla(nueva_fila)
        self.__limpiar_campos()

    def _agregar_fila_a_tabla(self, fila):
        # Convertir cada elemento de la fila en un QStandardItem y añadirlo al modelo
        items = [QStandardItem(str(dato)) for dato in fila]
        
        for item in items:
            item.setTextAlignment(Qt.AlignCenter)

        # Añadir la fila al modelo de datos
        self.modelo_tabla_productos.appendRow(items)
        self.ui.tabla_productos.resizeColumnsToContents()
        
    def agregar_productos_en_bd(self):
        if self.cargando is None or not self.cargando.isVisible():
            self.cargando = Modal_de_espera()
            self.cargando.show()
        else:
            self.cargando.raise_()
            self.cargando.activateWindow()
            
        self.consultor = Consultas_segundo_plano()
        self.consultor.resultado.connect(self.productos_agregados_finalizado)
        self.consultor.terminado.connect(self.cargando_cerrar)
        self.consultor.error.connect(self.__mostrar_error)
        self.consultor.ejecutar_hilo(funcion=self.agregar_productos_query)
        
    def __mostrar_error(self, mensaje_error):
        Mensaje().mensaje_informativo(f"Ocurrió un error: {mensaje_error}")
        
    def cargando_cerrar(self):
        if self.cargando is not None:
            self.cargando.close()
            self.cargando = None
            
    def productos_agregados_finalizado(self, productos_agregados, estado):
        if estado:
            # Aquí haces lo que quieras con los productos agregados:
            Mensaje().mensaje_informativo(f"{len(productos_agregados)} productos agregados con éxito.")
            # Podrías actualizar la UI o limpiar el formulario, por ejemplo
        else:
            Mensaje().mensaje_advertencia("No se pudieron agregar productos.")
            
    def agregar_productos_query(self, session):
            productos_no_agregados = []
            productos_agregados = []

            for producto in self.lista_productos:
                dimensiones = f"{producto['largo_dimensiones']}-{producto['alto_dimensiones']}-{producto['ancho_dimensiones']}"
                nombre_proveedor = producto["proveedor"].strip()
                nombre_presentacion = producto["presentacion"].strip()
                nombre_unidad_de_medida = producto["unidad_medida"].strip()
                nombre_categoria = producto["categoria"].strip()

                proveedor = None
                presentacion = None
                unidad_medida = None
                categoria = None

                if nombre_proveedor:
                    proveedor, _ = ProveedoresModel(session).consultar_proveedor(nombre_proveedor)
                if nombre_presentacion:
                    presentacion, _ = ProductosModel(session).agregar_presentacion(nombre=nombre_presentacion)
                if nombre_unidad_de_medida:
                    unidad_medida, _ = ProductosModel(session).agregar_unidad_medida(nombre=nombre_unidad_de_medida)
                if nombre_categoria:
                    categoria, _ = CategoriasModel(session).agregar(tipo_categoria="productos", nombre=nombre_categoria)

                proveedores = [proveedor] if proveedor else []

                producto_obj, estatus_producto = ProductosModel(session).agregar_producto(
                    codigo_upc=producto["codigo_barras"],
                    nombre_producto=producto["nombre"],
                    descripcion_producto=producto["descripcion"],
                    costo_inicial=producto["costo_inicial"],
                    costo_final=producto["costo_final"],
                    margen_porcentaje=f'{producto["margen_porcentaje"]}%',
                    precio=producto["precio_venta"],
                    existencia=producto["existencia"],
                    existencia_minima=producto["existencia_min"],
                    existencia_maxima=producto["existencia_max"],
                    marca=producto["marca"],
                    modelo=producto["modelo"],
                    peso=producto["peso"],
                    dimensiones=dimensiones,
                    color=producto["color"],
                    material=producto["material"],
                    fecha_fabricacion=producto["fecha_fabricacion"] if self.ui.opcion_TieneCaducidad.isChecked() else None,
                    fecha_vencimiento=producto["fecha_vencimiento"] if self.ui.opcion_TieneCaducidad.isChecked() else None,
                    imagen=self.imagenProducto if self.imagenProducto else producto["imagen"],
                    notas=producto["notas"],
                    presentacion_producto_id=presentacion.id if presentacion else None,
                    unidad_medida_productos_id=unidad_medida.id if unidad_medida else None,
                    categoria_id=categoria.id if categoria else None,
                    sucursales=[],
                    proveedores=proveedores
                )

                if estatus_producto:
                    productos_agregados.append(producto_obj)
                else:
                    productos_no_agregados.append(producto_obj)

            # Asegúrate de hacer commit de la sesión después de agregar los productos
            try:
                session.commit()  # Guardar cambios en la base de datos
            except Exception as e:
                session.rollback()  # Revertir cambios si algo sale mal
                raise e  # Propagar el error para que el hilo maneje la excepción

            return productos_agregados, True
            
    def resultado_de_agregar_produtos(self, resultado, estado):
        if self.productos_no_agregados:
            Mensaje().mensaje_informativo("Existen productos que no se agregaron debido a que ya existen en la base de datos.")
            self.__cargar_datos_en_tabla(self.produtos_no_agregados)
        self.PRODUCTOS_AGREGADOS.emit() 
    
    def __guardar_producto(self):
        try:
            if self.modelo_tabla_productos.rowCount() <= 0:
                Mensaje().mensaje_informativo("No se almaceno ningun producto por que no se encontro nada en la tabla de productos a almacenar")
                return
            self.agregar_productos_en_bd()
        except Exception as e:
            print(traceback.print_exc())
            print(f"Error al guardar producto: {e}")

    def __actualizar_producto(self):
        if not self.producto:
            Mensaje().mensaje_informativo("No se selecciono ningun producto para actualizar")
            return
        datos_producto = self.datos_campos()
        proveedores_vinculados = list(self.proveedores_vinculados.values())

        # Filtrar los proveedores de lista_proveedores_a_asignar para que no se repitan (por ID)
        proveedores_no_repetidos = [
            proveedor for proveedor_id, proveedor in self.lista_proveedores_a_asignar.items()
            if proveedor_id not in self.proveedores_vinculados  # Excluir los proveedores ya vinculados
        ]

        # Combinar los proveedores vinculados con los no repetidos
        todos_los_proveedores = proveedores_vinculados + proveedores_no_repetidos
        
        dimensiones = str(datos_producto["largo_dimensiones"]) + "-" + str(datos_producto["alto_dimensiones"]) + "-" + str(datos_producto["ancho_dimensiones"])
        with Conexion_base_datos() as db:
            session = db.abrir_sesion()
            with session.begin():
                ProductosModel(session).actualizar_producto(
                    id_producto = self.producto.id,
                    codigo_upc = datos_producto["codigo_barras"],
                    nombre_producto = datos_producto["nombre"],
                    descripcion_producto = datos_producto["descripcion_producto"],
                    costo_inicial = datos_producto["costo_inicial_producto"],
                    costo_final = datos_producto["costo_final_producto"],
                    margen_porcentaje=f'{datos_producto["margen_porcentaje"]} %',
                    precio = datos_producto["precio_venta_producto"],
                    existencia = datos_producto["existencia_producto"],
                    existencia_minima = datos_producto["existencia_min_producto"],
                    existencia_maxima = datos_producto["existencia_max_producto"],
                    marca = datos_producto["marca_producto"],
                    modelo = datos_producto["modelo_producto"],
                    peso = datos_producto["peso_producto"],
                    dimensiones = dimensiones,
                    color = datos_producto["color_producto"],
                    material = datos_producto["material_producto"],
                    fecha_fabricacion = datos_producto["fecha_fabricacion_producto"],
                    fecha_vencimiento = datos_producto["fecha_vencimiento_producto"],
                    imagen = self.imagenProducto if self.imagenProducto else None,
                    notas = datos_producto["notas_producto"],
                    presentacion_producto_id = datos_producto["presentacion_producto"].id,
                    unidad_medida_productos_id = datos_producto["unidad_medida_producto"].id,
                    categoria_id = datos_producto["categoria_producto"].id,
                    sucursales = [],
                    proveedores = todos_los_proveedores
                )
        self.PRODUCTOS_AGREGADOS.emit()
        self.close()
    
    def consultar_producto_por_id(self, session):
        producto, estado = ProductosModel(session).consultar_producto_por_codigoUPC(codigo_upc=self.codigo_producto_upc_recibido)
        return producto, estado
    
    def cerrar_cargando(self):
        self.cargando.close()
        self.cargando = None
        
    def __cargar_datos_en_campos(self, producto):
        self.producto = producto
        self.ui.txt_codBarras.setEnabled(False)
        self.ui.contenedor_proveedores_vinculados.show()
        self.ui.contenedor_proveedores_existentes.show()
        self.ui.contenedor_proveedores_a_vincular.show()
        self.ui.txt_proveedor.hide()
        self.ui.etiqueta_proveedor.hide()
        self.ui.tabla_productos.hide()
        self.ui.btn_btn_addProduct_agregar_producto.hide()
        self.ui.btn_btn_addProduct_guardar_producto.hide()
        self.ui.etiqueta_listaProductos.hide()
        self.ui.btn_btn_addProduct_cargar_CSVProductos.hide()
        self.ui.btn_btn_addProduct_limpiarTablaProductos.hide()
        self.ui.btn_btn_addProduct_actualizar_producto.show()
        self.ui.txt_codBarras.setText(self.producto.codigo_upc)
        self.ui.txt_codBarras.setText(self.producto.codigo_upc)
        self.ui.txt_nombreProducto.setText(self.producto.nombre_producto)
        self.ui.txt_marcaProducto.setText(self.producto.marca)
        self.ui.txt_modeloProducto.setText(self.producto.modelo)
        self.ui.txt_colorProducto.setText(self.producto.color)
        self.ui.txt_materialProducto.setText(self.producto.material)
        self.ui.txtlargo_descripcionProducto.setPlainText(self.producto.descripcion_producto)
        self.ui.txtlargo_notasProducto.setPlainText(self.producto.notas)

        self.ui.decimal_costoInicialProducto.setValue(self.producto.costo_inicial)
        self.ui.decimal_costoFinalProducto.setValue(self.producto.costo_final)
        
        if self.producto.imagen:
            try:
                # Verifica si la ruta de la imagen es válida
                pixmap = QPixmap(self.producto.imagen)
                if pixmap.isNull():  # Si no se puede cargar la imagen
                    raise ValueError("Imagen no válida")

                # Escala la imagen antes de establecerla
                pixmap_scaled = pixmap.scaled(self.ui.etiqueta_fotoProducto.size(), Qt.KeepAspectRatio)
                self.ui.etiqueta_fotoProducto.setPixmap(pixmap_scaled)
                self.imagenProducto = self.producto.imagen  # Guarda la imagen si todo está bien
            except Exception as e:
                # Si hay un error al cargar la imagen, muestra un mensaje y coloca el icono predeterminado
                Mensaje().mensaje_informativo(f"Error al cargar la imagen: {e}")
                _translate = QtCore.QCoreApplication.translate
                self.ui.etiqueta_fotoProducto.setText(_translate("contenedor_agregar_productos", "<html><head/><body><p align=\"center\"><img src=\":/Icons/IconosSVG/subir_imagen.png\" width=\"80\" height=\"70\"/></p><p align=\"center\"><span style=\" font-size:16pt; font-family:Arial; font-weight:bold;\">Cargar Imagen</span></p></body></html>"))
        else:
            # Si no hay imagen, coloca el mensaje predeterminado
            _translate = QtCore.QCoreApplication.translate
            self.ui.etiqueta_fotoProducto.setText(_translate("contenedor_agregar_productos", "<html><head/><body><p align=\"center\"><img src=\":/Icons/IconosSVG/subir_imagen.png\" width=\"80\" height=\"70\"/></p><p align=\"center\"><span style=\" font-size:16pt; font-family:Arial; font-weight:bold;\">Cargar Imagen</span></p></body></html>"))

        # Asumiendo que margen_porcentaje es tipo string como "25 %"
        try:
            margen = int(str(self.producto.margen_porcentaje).rstrip("%"))
        except Exception:
            margen = 0
        self.ui.entero_margenProducto.setValue(margen)
        self.ui.decimal_precioVentaProducto.setValue(self.producto.precio)
        self.ui.decimal_existenciaProducto.setValue(self.producto.existencia)
        self.ui.decimal_existenciaMinProducto.setValue(self.producto.existencia_minima)
        self.ui.decimal_existenciaMaxProducto.setValue(self.producto.existencia_maxima)
        self.ui.decimal_pesoProducto.setValue(self.producto.peso)

        if producto.fecha_fabricacion:
            self.ui.opcion_TieneCaducidad.setChecked(True)
            
            # Convertir datetime.date a string con formato "YYYY-MM-DD"
            fecha_fabricacion_str = producto.fecha_fabricacion.strftime("%Y-%m-%d")
            fecha_fabricacion = QDate.fromString(fecha_fabricacion_str, "yyyy-MM-dd")
            
            fecha_vencimiento_str = producto.fecha_vencimiento.strftime("%Y-%m-%d") if producto.fecha_vencimiento else None
            fecha_vencimiento = QDate.fromString(fecha_vencimiento_str, "yyyy-MM-dd") if fecha_vencimiento_str else QDate()

            # Establecer las fechas
            self.ui.fecha_fabricacionProducto.setDate(fecha_fabricacion)
            self.ui.fecha_vencimientoProducto.setDate(fecha_vencimiento)
        # if producto.imagen:
        #     self.ui.etiqueta_fotoProducto.setPixmap(
        #         QPixmap(self.producto.imagen).scaled(self.ui.etiqueta_fotoProducto.size())
        #     )

        # Cargar dimensiones si existen
        if producto.dimensiones:
            dimensiones = producto.dimensiones.split("-")
            try:
                alto = float(dimensiones[0])
                ancho = float(dimensiones[1])
                largo = float(dimensiones[2])

                self.ui.decimal_altoDimensiones.setValue(alto)
                self.ui.decimal_anchoDimensiones.setValue(ancho)
                self.ui.decimal_largoDimensiones.setValue(largo)
            except Exception as e:
                print(f"Error al cargar dimensiones: {e}")
        # Actualizar categoría del producto
        
        # Actualizar categoría del producto
        if producto.categoria:
            categoria_nombre = producto.categoria.nombre
            FuncionesAuxiliaresController().caja_opciones_mover_elemento(self.ui.cajaOpciones_categoriaProducto, categoria_nombre)

        if producto.unidad_medida_productos:
                medida_nombre = producto.unidad_medida_productos.nombre
                FuncionesAuxiliaresController().caja_opciones_mover_elemento(self.ui.cajaOpciones_unidadMedidaProducto, medida_nombre)

        # Actualizar presentación del producto
        if producto.presentacion_productos:
                presentacion_nombre = producto.presentacion_productos.nombre
                FuncionesAuxiliaresController().caja_opciones_mover_elemento(self.ui.cajaOpciones_presentacionProducto, presentacion_nombre)

        if producto.proveedores:
            self.proveedores_vinculados = {p.id: p for p in producto.proveedores}
            self.listar_proveedores(self.proveedores_vinculados)
    
    def listar_proveedores(self, proveedores):
        self.ui.lista_proveedores_vinculados.clear()
        self.icono_proveedor = QIcon(":/Icons/Bootstrap/file-person.svg")
        for id, proveedor in proveedores.items():
            item = QListWidgetItem(proveedor.nombre)
            item.setIcon(self.icono_proveedor)
            item.setData(Qt.UserRole, ((id, proveedor)))  # Guardamos el ID para referencia
            self.ui.lista_proveedores_vinculados.addItem(item)
    
    def __limpiar_tabla_productos(self):
        self.modelo_tabla_productos.removeRows(0, self.modelo_tabla_productos.rowCount())
        self.lista_productos = []
                
    def obtener_proveedores(self):
        self.consultor = Consultas_segundo_plano()
        self.consultor.resultado.connect(self.__almacenar_proveedores_del_sistema)
        self.consultor.ejecutar_hilo(funcion=self.__obtener_proveedores_query)
    
    def __obtener_proveedores_query(self, session):
        proveedores, estado = ProveedoresModel(session).obtener_proveedores()
        return proveedores, estado
        
    def __almacenar_proveedores_del_sistema(self, proveedores, estado):
        self.proveedores_generales_del_sistema_dict = {p.id : p for p in proveedores}
        self.__proveedores_desvinculados()
        
    def __proveedores_desvinculados(self):
        self.proveedores_no_vinculados = {
            pid: p for pid, p in self.proveedores_generales_del_sistema_dict.items()
            if pid not in self.proveedores_vinculados
        }
        self.listar_proveedores_existentes()
                    
    def __proveedor_seleccionado(self, texto):
        # Buscar el ID del proveedor por su nombre (valor) en el diccionario
        for id_proveedor, nombre in self.proveedores.items():
            if nombre == texto:
                self.proveedor_id = id_proveedor  # Asignamos el id correspondiente
                break
        else:
            self.proveedor_id = None

    def listar_proveedores_existentes(self):
            self.ui.lista_todos_los_proveedores.clear()
            self.icono_proveedor = QIcon(":/Icons/Bootstrap/file-person.svg")
            
            if not self.proveedores_vinculados:  # Si proveedores vinculados está vacío
                # Mostrar todos los proveedores
                for proveedor_id, proveedor in self.proveedores_generales_del_sistema_dict.items():
                    # Crear el item con el nombre del proveedor
                    item = QListWidgetItem(proveedor.nombre)  # Solo mostrar el nombre
                    item.setIcon(self.icono_proveedor)
                    
                    # Almacenar tanto el id como el objeto del proveedor en UserRole
                    item.setData(Qt.UserRole, (proveedor_id, proveedor))  # Guardamos el id y el objeto
                    
                    # Agregar el item a la lista
                    self.ui.lista_todos_los_proveedores.addItem(item)
            else:
                # Mostrar los proveedores no vinculados
                for proveedor_id, proveedor in self.proveedores_no_vinculados.items():
                    # Crear el item con el nombre del proveedor
                    item = QListWidgetItem(proveedor.nombre)  # Solo mostrar el nombre
                    item.setIcon(self.icono_proveedor)
                    
                    # Almacenar tanto el id como el objeto del proveedor en UserRole
                    item.setData(Qt.UserRole, (proveedor_id, proveedor))  # Guardamos el id y el objeto
                    
                    # Agregar el item a la lista
                    self.ui.lista_todos_los_proveedores.addItem(item)
    
    def buscar_proveedor_existente(self):
        nombre = self.ui.txt_buscar_proveedor_a_vincular.text().strip()
        self.icono_proveedor = QIcon(":/Icons/Bootstrap/file-person.svg")
        
        if not self.producto.proveedores:
            return
        
        if nombre:
            # Limpiar la lista antes de mostrar resultados de búsqueda
            self.ui.lista_todos_los_proveedores.clear()
            
            for proveedor_id, proveedor in self.proveedores_generales_del_sistema_dict.items():
                proveedor_nombre = proveedor.nombre
                # Comprobar si el nombre del proveedor contiene la búsqueda
                if nombre in proveedor_nombre:
                    # Crear el ítem solo con el nombre del proveedor
                    item = QListWidgetItem(proveedor_nombre)
                    
                    # Establecer el ícono en el ítem
                    item.setIcon(self.icono_proveedor)
                    
                    # Almacenar tanto el ID como el objeto del proveedor en UserRole
                    item.setData(Qt.UserRole, (proveedor_id, proveedor))  # Guardamos el ID y el objeto
                    
                    # Agregar el ítem a la lista
                    self.ui.lista_todos_los_proveedores.addItem(item)
        else:
            # Si no hay texto en el campo de búsqueda, mostrar todos los proveedores no vinculados
            self.ui.lista_todos_los_proveedores.clear()
            
            for proveedor_id, proveedor in self.proveedores_generales_del_sistema_dict.items():
                # Comprobar si el proveedor ya está vinculado
                if proveedor_id not in self.proveedores_vinculados:
                    proveedor_nombre = proveedor.nombre
                    item = QListWidgetItem(proveedor_nombre)
                    
                    # Establecer el ícono en el ítem
                    item.setIcon(self.icono_proveedor)
                    
                    # Almacenar el proveedor completo (ID y objeto) en UserRole
                    item.setData(Qt.UserRole, (proveedor_id, proveedor))
                    
                    # Agregar el ítem a la lista
                    self.ui.lista_todos_los_proveedores.addItem(item)
    
    def buscar_proveedor_vinculado(self):
        nombre = self.ui.txt_buscar_proveedor_vinculado.text().strip()
        if not self.proveedores_vinculados:
            Mensaje().mensaje_informativo("No se encuentran elementos para realizar el filtrado")
            return
        if nombre:
            self.ui.lista_proveedores_vinculados.clear()
            self.icono_proveedor = QIcon(":/Icons/Bootstrap/file-person.svg")
            for proveedor_id,  proveedor in self.proveedores_vinculados.items():
                proveedor_nombre = proveedor.nombre
                if nombre in proveedor_nombre:
                    item = QListWidgetItem(proveedor_nombre)
                    
                    # Establecer el ícono en el ítem
                    item.setIcon(self.icono_proveedor)
                    item.setData(Qt.UserRole, proveedor_id)
                    
                    # Agregar el ítem a la lista
                    self.ui.lista_proveedores_vinculados.addItem(item)
        else:
            self.ui.lista_proveedores_vinculados.clear()
            self.icono_proveedor = QIcon(":/Icons/Bootstrap/file-person.svg")
            for proveedor_id, proveedor in self.proveedores_vinculados.items():
                proveedor_nombre = proveedor.nombre
                item = QListWidgetItem(proveedor_nombre)
                
                # Establecer el ícono en el ítem
                item.setIcon(self.icono_proveedor)
                item.setData(Qt.UserRole, proveedor_id)
                
                # Agregar el ítem a la lista
                self.ui.lista_proveedores_vinculados.addItem(item)
    
    def vincular_proveedor_al_producto(self, item):
        # Obtener el ícono, ID y el objeto del proveedor desde UserRole
        icono = item.icon()
        proveedor_id, proveedor_objeto = item.data(Qt.UserRole)  # Obtener tanto ID como objeto del proveedor
        proveedor_nombre = item.text()  # Nombre visible del proveedor

        # Si no hay proveedores asignados, agregar el primero
        if len(self.lista_proveedores_a_asignar) == 0:
            # Crear un nuevo ítem para el proveedor
            nuevo_proveedor = QListWidgetItem(proveedor_nombre)
            nuevo_proveedor.setIcon(icono)
            nuevo_proveedor.setData(Qt.UserRole, (proveedor_id, proveedor_objeto))  # Guardamos ID y objeto del proveedor

            # Agregar el proveedor al diccionario y a la lista visual
            self.lista_proveedores_a_asignar[proveedor_id] = proveedor_objeto  # Guardamos ID como clave y objeto como valor
            self.ui.lista_proveedores_a_vincular.addItem(nuevo_proveedor)
            return

        # Si el proveedor no está ya en el diccionario, agregarlo
        if proveedor_id not in self.lista_proveedores_a_asignar:
            self.lista_proveedores_a_asignar[proveedor_id] = proveedor_objeto  # Guardamos el objeto completo
            nuevo_proveedor = QListWidgetItem(proveedor_nombre)
            nuevo_proveedor.setIcon(icono)
            nuevo_proveedor.setData(Qt.UserRole, (proveedor_id, proveedor_objeto))  # Guardamos ID y objeto del proveedor
            self.ui.lista_proveedores_a_vincular.addItem(nuevo_proveedor)
    
    def desvincular_proveedor_al_producto(self):
        item = self.ui.lista_proveedores_vinculados.currentItem()
        if not item:
            Mensaje().mensaje_informativo("Debes de seleccionar un elemento de la lista")
            return
        try:
            proveedor_id, proveedor_objeto = item.data(Qt.UserRole)  # Obtener ID y objeto del proveedor
            self.ui.lista_proveedores_vinculados.takeItem(self.ui.lista_proveedores_vinculados.row(item))
            
            # Desvincular el proveedor del diccionario
            if proveedor_id in self.proveedores_vinculados:
                del self.proveedores_vinculados[proveedor_id]  # Eliminarlo del diccionario de proveedores vinculados
        except Exception as e:
            Mensaje().mensaje_alerta(f"No se puede realizar la acción debido al siguiente error: {str(e)}")

    def eliminar_proveedor_a_vincular(self):
        item = self.ui.lista_proveedores_a_vincular.currentItem()
        if not item:
            Mensaje().mensaje_informativo("Debes de seleccionar un elemento de la lista")
            return
        proveedor_id, proveedor_objeto = item.data(Qt.UserRole)  # Obtener ID y objeto del proveedor
        proveedor_nombre = item.text()  # Obtener el nombre del proveedor (por si lo necesitas para algo)
        
        self.ui.lista_proveedores_a_vincular.takeItem(self.ui.lista_proveedores_a_vincular.row(item))
        
        # Eliminar el proveedor del diccionario de proveedores a asignar
        if proveedor_id in self.lista_proveedores_a_asignar:
            del self.lista_proveedores_a_asignar[proveedor_id]  # Eliminarlo del diccionario de proveedores a asignar

    def __leer_archivo_csv(self):
        documento, _ = QFileDialog.getOpenFileName(self, "Selecciona un documento de Excel", "", "Archivos Excel (*.xlsx *.xls)")
        if not documento:
            return
        if self.cargando is None or not self.cargando.isVisible():
            self.cargando = Modal_de_espera()
            self.cargando.show()
        else:
            self.cargando.raise_()
            self.cargando.activateWindow()

        self.consultor = Consultas_segundo_plano()
        self.consultor.error.connect(self.mensaje_error_docuemnto_xlsx)
        self.consultor.terminado.connect(self.cargando_cerrar)
        self.consultor.resultado_productos_masivos_excel.connect(self.resultado_documento_excel)
        self.consultor.lecturas_y_procesamiento(documento, self.lista_productos)

    def resultado_documento_excel(self, lista_nuevos_productos, duplicados):
        self.lista_productos.extend(lista_nuevos_productos)
        self.__cargar_datos_en_tabla(self.lista_productos)

        if duplicados:
            Mensaje().mensaje_informativo("Se encontraron registros duplicados que no fueron agregados.\nSolo se agregaron los registros sin duplicar.")

    def mensaje_error_docuemnto_xlsx(self, error):
        print(error)
        Mensaje().mensaje_alerta(f"Ocurrió un error con la lectura del documento de Excel.\nError: {error}")

    def __cargar_datos_en_tabla(self, lista_productos):
        self.modelo_tabla_productos.setHorizontalHeaderLabels([
            "Proveedor", "Código de Barras", "Nombre", "Categoría", "Marca", "Modelo", "Color",
            "Material", "Unidad de Medida", "Presentación", "Costo Inicial", "Costo Final", "Margen Porcentaje", "Precio Venta",
            "Existencia", "Existencia Min", "Existencia Max", "Peso",
            "Largo Dimensiones", "Alto Dimensiones", "Ancho Dimensiones",
            "Descripción", "Notas", "Fecha Vencimiento", "Fecha Fabricación", "Imagen"
        ])

        self.modelo_tabla_productos.removeRows(0, self.modelo_tabla_productos.rowCount())

        for producto in lista_productos:
            fila = [QStandardItem(str(producto[key])) for key in producto]
            for item in fila:
                item.setTextAlignment(Qt.AlignCenter)
            self.modelo_tabla_productos.appendRow(fila)

        self.ui.tabla_productos.setModel(self.modelo_tabla_productos)
        self.ui.tabla_productos.resizeColumnsToContents()
    
    def comprobar_existencia_modelo_tabla(self):
        if not hasattr(self, 'modelo_tabla_productos'):
                self.modelo_tabla_productos = QStandardItemModel()

    def calcular_precio_venta(self):
        costo_final = self.ui.decimal_costoFinalProducto.value()
        margen = self.ui.entero_margenProducto.value() / 100
        precio_venta = costo_final + (costo_final * margen)
        self.ui.decimal_precioVentaProducto.setValue(precio_venta)
        
class Productos(QWidget):
    LISTAR_CATEGORIAS_PRODUCTOS = pyqtSignal()
    LISTAR_UNIDADES_MEDIDA_PRODUCTOS = pyqtSignal()
    LISTAR_PRESENTACIONES_PRODUCTOS = pyqtSignal()
    LISTAR_PROVEEDORES_EXISTENTES_SIGNAL = pyqtSignal()
    MOSTRAR_DATOS_EXISTENCIAS = pyqtSignal()
    def __init__(self, parent = None, datos_usuario = None):
        super().__init__(parent)
        self.ui = Ui_Control_Productos()
        self.ui.setupUi(self)
        self.ui.btn_btn_adminProductos_agregar.clicked.connect(self.agregar_producto)
        self.ui.btn_btn_adminProductos_eliminar.clicked.connect(self.eliminar_producto)
        self.ui.btn_btn_adminProductos_modificar.clicked.connect(self.modificar_producto)
        self.ui.btn_btn_adminProductos_buscar.clicked.connect(self.buscar_producto)
        self.ui.btn_btn_adminProductos_ExistenciaProducto.clicked.connect(self.existencia_productos)
        self.ui.btn_RefrescarTabla.clicked.connect(self.consultar_productos_db)
        
        self.producto_actual = None
        self.consultor = None
        self.cargando = None
        self.datos_usuario = datos_usuario
        self.seleccion_conectada_productos = None
        self.codigo_upc_producto = None
        self.AdminProductos = None
        self.ventana_existencia_productos = None
        self.comprobar_modelo_tabla_productos()
        
        
        
    def  buscar_producto(self):
        if self.ui.txt_buscar.text().strip() == "":
            Mensaje().mensaje_informativo("No haz insertado texto para realizar la busqueda")
            return
        if self.cargando is None or not self.cargando.isVisible():
            self.cargando = Modal_de_espera()
            self.cargando.show()
        else:
            self.cargando.raise_()
            self.cargando.activateWindow()
            
        self.consultor = Consultas_segundo_plano()
        self.consultor.terminado.connect(self.cargando_cerrar)
        self.consultor.resultado.connect(self.listar_productos)
        self.consultor.ejecutar_hilo(funcion=self.busar_producto_query)
        
    def busar_producto_query(self, session):
        nombre_producto = self.ui.txt_buscar.text().strip()
        productos, estado = ProductosModel(session).consultar_por_nombre(nombre=nombre_producto)
        return productos, estado 
    
    def agregar_producto(self):
        if self.AdminProductos is None or self.AdminProductos.isVisible():
            self.AdminProductos = Admin_productosController(self)
            self.LISTAR_CATEGORIAS_PRODUCTOS.connect(self.AdminProductos.listar_categorias)
            self.LISTAR_UNIDADES_MEDIDA_PRODUCTOS.connect(self.AdminProductos.listar_unidades_medida)
            self.LISTAR_PRESENTACIONES_PRODUCTOS.connect(self.AdminProductos.listar_presentaciones_productos)
            self.AdminProductos.VENTANA_CERRADA_PRODUCTOS.connect(self.ventana_productos_cerrada)
            self.LISTAR_CATEGORIAS_PRODUCTOS.emit()
            self.LISTAR_UNIDADES_MEDIDA_PRODUCTOS.emit()
            self.LISTAR_PRESENTACIONES_PRODUCTOS.emit()
            self.AdminProductos.show()
        else:
            self.AdminProductos.raise_()
            self.AdminProductos.activateWindow()
            
    def ventana_productos_cerrada(self):
        self.AdminProductos = None
        self.producto_actual = None
    
    def eliminar_producto(self):
        if self.producto_actual is None:
            Mensaje().mensaje_informativo("Debes de seleccionar un producto de la tabla para proceder a eliminarlo")
            return
        if self.cargando is None or not self.cargando.isVisible():
            self.cargando = Modal_de_espera()
            self.cargando.show()
        else:
            self.cargando.raise_()
            self.cargando.activateWindow()
        
        self.consultor = Consultas_segundo_plano()
        self.consultor.terminado.connect(self.cargando_cerrar)
        self.consultor.resultado.connect(self.mensaje_hilo)
        self.consultor.ejecutar_hilo(
            funcion=self.eliminar_producto_query
            )
        
    def eliminar_producto_query(self, session):
        producto, estado = ProductosModel(session).eliminar_producto(codigo_producto=self.producto_actual.codigo_upc)
        return producto, estado
    
    def mensaje_hilo(self, resultado, estado):
        if estado:
            Mensaje().mensaje_informativo("Eliminado correctamente")
        else:
            Mensaje().mensaje_informativo("No se elimino el producto")
            
    def modificar_producto(self):
        if self.producto_actual is None:
            Mensaje().mensaje_informativo("No has seleccionado un producto de la tabla para proceder a modificarlo")
            return
        self.enviar_produto_al_ui(self.producto_actual)
        
    def enviar_produto_al_ui(self, producto):
        if self.AdminProductos is None or not self.AdminProductos.isVisible():
            self.AdminProductos = Admin_productosController(self)
            self.LISTAR_CATEGORIAS_PRODUCTOS.connect(self.AdminProductos.listar_categorias)
            self.LISTAR_PRESENTACIONES_PRODUCTOS.connect(self.AdminProductos.listar_presentaciones_productos)
            self.LISTAR_UNIDADES_MEDIDA_PRODUCTOS.connect(self.AdminProductos.listar_unidades_medida)
            self.AdminProductos.VENTANA_CERRADA_PRODUCTOS.connect(self.ventana_productos_cerrada)
            self.LISTAR_PROVEEDORES_EXISTENTES_SIGNAL.connect(self.AdminProductos.obtener_proveedores)
            self.AdminProductos.RECIBIR_PRODUCTO_ACTUALIZAR_ID.emit(self.producto_actual)
            self.LISTAR_PROVEEDORES_EXISTENTES_SIGNAL.emit()
            self.LISTAR_PRESENTACIONES_PRODUCTOS.emit()
            self.LISTAR_UNIDADES_MEDIDA_PRODUCTOS.emit()
            self.LISTAR_CATEGORIAS_PRODUCTOS.emit()
            self.AdminProductos.setParent(self)
            self.AdminProductos.setStyleSheet(self.AdminProductos.styleSheet())
            self.AdminProductos.show()
            # Si AdminProductos es None, se crea e inicializ
            # Ahora sí conectar las señales, ya que AdminProductos se ha creado
        else:
            # Si ya existe y está visible, solo elevar la ventana
            self.AdminProductos.raise_()
            self.AdminProductos.activateWindow()
        
        self.codigo_upc_producto = None
        
    def listar_productos(self, productos, estado):
        if not estado:
            Mensaje().mensaje_informativo("No hay productos para mostrar")
            self.comprobar_modelo_tabla_productos()
            self.modelo_tabla_productos.removeRows(0, self.modelo_tabla_productos.rowCount())
            return
        self.productos = productos
        self.comprobar_modelo_tabla_productos()
        self.modelo_tabla_productos.removeRows(0, self.modelo_tabla_productos.rowCount())

        # Establecer los encabezados de la tabla
        cabeceras = [
            "Proveedor", "Codigo upc", "Nombre Producto", "Categoria", "Marca", "Modelo", "Color", 
            "Material", "Unidad de Medida", "Presentacion", "Costo Inicial", "Costo Final", "Margen Porcentaje", "Precio", 
            "Existencia", "Existencia Minima", "Existencia Maxima", "Peso", 
            "Dimensiones", "Descripcion Producto", "Notas", "Fecha Vencimiento", "Fecha Fabricacion", "Imagen"
        ]
        self.modelo_tabla_productos.setHorizontalHeaderLabels(cabeceras)

        # Recorrer la lista de productos
        for producto in self.productos:
            list_productos = []

            for col in cabeceras:
                value = ""

                if col.lower() == "proveedor":
                    value = ", ".join([proveedor.nombre for proveedor in producto.proveedores]) if producto.proveedores else ""
                elif col.lower() == "categoria":
                    value = producto.categoria.nombre if producto.categoria else ""
                elif col.lower() == "unidad de medida":
                    value = producto.unidad_medida_productos.nombre if producto.unidad_medida_productos else ""
                elif col.lower() == "presentacion":
                    value = producto.presentacion_productos.nombre if producto.presentacion_productos else ""
                elif hasattr(producto, col.lower().replace(" ", "_")):
                    value = getattr(producto, col.lower().replace(" ", "_"))

                item = QStandardItem(str(value))
                item.setTextAlignment(Qt.AlignCenter)

                # 💡 Asociar el objeto completo al item de la columna "Codigo upc" (columna 1)
                if col.lower() == "codigo upc":
                    item.setData(producto, Qt.UserRole)

                list_productos.append(item)

            self.modelo_tabla_productos.appendRow(list_productos)

        # Establecer el modelo en la tabla
        self.ui.tabla_productos.setModel(self.modelo_tabla_productos)
        self.ui.tabla_productos.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.tabla_productos.resizeColumnsToContents()

        # Conectar señal solo si no está conectada
        if self.seleccion_conectada_productos:
            self.ui.tabla_productos.clicked.disconnect(self.obtener_id_elemento_tabla_productos)
            self.seleccion_conectada_productos = False

        self.ui.tabla_productos.clicked.connect(self.obtener_id_elemento_tabla_productos)
        self.seleccion_conectada_productos = True

    def consultar_productos_db(self):
        if self.cargando is None or not self.cargando.isVisible():

            self.cargando = Modal_de_espera(parent=self)
            self.cargando.show()
        else:
            self.cargando.raise_()
            self.cargando.activateWindow()
        self.consultor = Consultas_segundo_plano()
        self.consultor.terminado.connect(self.cargando_cerrar)
        self.consultor.resultado.connect(self.listar_productos)
        self.consultor.ejecutar_hilo(funcion=self.obtener_productos)
    
    def cargando_cerrar(self):
        if self.cargando is not None:
            self.cargando.close()
            self.cargando = None
            
    def obtener_productos(self, session):
        productos, estado = ProductosModel(session).obtener_productos()
        return productos, estado
    
    def mostrar_error_consulta(self, mensaje):
        print(f"❌ Error en la consulta: {mensaje}")
        # Aquí podrías usar un QMessageBox si estás en una GUI
        
    def obtener_id_elemento_tabla_productos(self, current, previus = None):
        if current.isValid():
            fila = current.row()
            # Accedemos al item de la columna que tiene el objeto (columna 1 = Codigo upc)
            item = self.modelo_tabla_productos.item(fila, 1)
            if item:
                producto = item.data(Qt.UserRole)
                if producto:
                    print(producto)
                    self.producto_actual = producto
    
    def comprobar_modelo_tabla_productos(self):
        # Si no existe el modelo de la tabla, crearlo como QStandardItemModel
        if not hasattr(self, 'modelo_tabla_productos'):
            self.modelo_tabla_productos = QStandardItemModel()

            # Asignar el modelo al QTableView si no está asignado
            self.ui.tabla_productos.setModel(self.modelo_tabla_productos)

    def existencia_productos(self):
        if self.producto_actual is None:
            Mensaje().mensaje_informativo('Selecciona un producto.')
            return
        if self.ventana_existencia_productos is None or not self.ventana_existencia_productos.isVisible():
            self.ventana_existencia_productos = ExistenciasClase(self, datos_usuario = self.datos_usuario)
            self.ventana_existencia_productos.VENTANA_CERRADA_EXISTENCIA.connect(self.ventana_cerrada_form_existencia)
            self.ventana_existencia_productos.RECIBIR_PRODUCTO_ID_EXISTENCIA.emit(self.producto_actual)
            self.MOSTRAR_DATOS_EXISTENCIAS.emit()
            self.ventana_existencia_productos.show()
        
    def ventana_cerrada_form_existencia(self):
        self.ventana_existencia_productos = None
        self.producto_actual = None