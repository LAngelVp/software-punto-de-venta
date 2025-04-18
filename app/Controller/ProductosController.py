from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QValidator, QStandardItemModel, QStandardItem, QPixmap, QIcon, QCursor
from ..Source.iconsdvg_rc import *
import pandas as pd
import numpy as np
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


import traceback

class ExistenciasClase(QWidget):
    VENTANA_CERRADA_EXISTENCIA = pyqtSignal()
    def __init__(self, parent = None, datos_usuario = None, producto = None):
        super().__init__(parent)
        self._ventanaCentrada = False
        self.datos_usuario = datos_usuario
        self.producto = producto
        self.ui = Ui_UI_EXISTENCIA_PRODUCTO()
        self.ui.setupUi(self)
        self.ui.fecha_FechaMovimiento.setDate(QDate.currentDate())
        self.ui.etiqueta_ClaveProducto.setText(self.producto.codigo_upc)
        self.ui.etiqueta_NombreUsuario.setText(self.datos_usuario["nombre_empleado"].upper())
        self.ui.btn_existenciaProducto_aceptar.clicked.connect(self.ejecutar_existencias)
        self.ui.btn_existenciaProducto_cerrar.clicked.connect(self.close)
        
    def showEvent(self, event):
        super().showEvent(event)
        if not self._ventanaCentrada:
            FuncionesAuxiliaresController.centrar_en_padre(self)
            self._ventanaCentrada = True
    
    def closeEvent(self, event):
        self.VENTANA_CERRADA_EXISTENCIA.emit() 
        event.accept()
        
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
                        producto=self.producto,
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
    RECIBIR_PRODUCTO_ACTUALIZAR = pyqtSignal(object)
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
        self.proveedores = {}
        self.id_proveedor = None
        self.imagenProducto = None
        self.producto = None
        self.lista_productos = []
        self.lista_proveedores_a_asignar = {}
        self.proveedores_vinculados = {}
        self._ventanaCentradaProductoExistente = False 
#// funciones principales:
        self.__obtener_proveedores()
        completar = QCompleter([proveedor.nombre for proveedor in self.proveedores.values()])
        completar.setCaseSensitivity(Qt.CaseInsensitive)
        self.ui.txt_proveedor.setCompleter(completar)
        self.comprobar_existencia_modelo_tabla()
#// señales:
        self.ui.txt_proveedor.textChanged.connect(self.__proveedor_seleccionado)
        self.ui.etiqueta_fotoProducto.mousePressEvent = self.cargar_imagen
#// botones de ventana:
        self.ui.btn_btn_addProduct_actualizar_producto.clicked.connect(self.__actualizar_producto)
        self.ui.btn_btn_addProduct_agregar_categoria.clicked.connect(self.__agregar_categoria)
        self.ui.btn_btn_addProduct_agregar_unidadMedidaProducto.clicked.connect(self.agregar_unidad_medida)
        self.ui.btn_btn_addProduct_agregarPresentacionProducto.clicked.connect(self.agregar_presentacion)
        self.ui.btn_btn_addProduct_agregar_producto.clicked.connect(self.__agregar_producto)
        self.ui.btn_btn_addProduct_guardar_producto.clicked.connect(self.__guardar_producto)
        self.ui.btn_btn_addProduct_limpiarTablaProductos.clicked.connect(self.__limpiar_tabla_productos)
        self.ui.btn_btn_addProduct_cargar_CSVProductos.clicked.connect(self.agregarCSV)
        self.RECIBIR_PRODUCTO_ACTUALIZAR.connect(self.__cargar_datos_en_campos)
        self.ui.txt_buscar_proveedor_a_vincular.returnPressed.connect(self.buscar_proveedor_existente)
        self.ui.txt_buscar_proveedor_vinculado.returnPressed.connect(self.buscar_proveedor_vinculado)
        self.ui.lista_todos_los_proveedores.itemClicked.connect(self.vincular_proveedor_al_producto)
        self.ui.btn_btn_addProduct_desvincular_proveedores.clicked.connect(self.desvincular_proveedor_al_producto)
        self.ui.btn_btn_addProduct_eliminar_proveedor_a_vincular.clicked.connect(self.eliminar_proveedor_a_vincular)
        self.ui.entero_margenProducto.editingFinished.connect(self.calcular_precio_venta)
        self.ui.opcion_TieneCaducidad.stateChanged.connect(self.mostrar_fechas_caducidad)
        self.ui.btn_btn_addProduct_cerrar.clicked.connect(self.close)


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
            "proveedor": self.ui.txt_proveedor.text().strip().upper(),
            "codigo_barras": self.ui.txt_codBarras.text().strip(),
            "nombre": self.ui.txt_nombreProducto.text().strip().upper(),
            "categoria_producto": self.ui.cajaOpciones_categoriaProducto.currentData(),
            "marca_producto": self.ui.txt_marcaProducto.text().strip().upper(),
            "modelo_producto": self.ui.txt_modeloProducto.text().strip().upper(),
            "color_producto": self.ui.txt_colorProducto.text().strip().upper(),
            "material_producto": self.ui.txt_materialProducto.text().strip().upper(),
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
        productos_no_agregados = []
        print(self.lista_productos)
        with Conexion_base_datos() as db:
            session = db.abrir_sesion()
            try:
                with session.begin():  # Inicia la transacción
                    for producto in self.lista_productos:
                        dimensiones = str(producto["largo_dimensiones"]) + "-" + str(producto["alto_dimensiones"]) + "-" + str(producto["ancho_dimensiones"])
                        print(producto["presentacion"])
                        proveedor, estatus_proveedor = ProveedoresModel(session).consultar_proveedor(producto["proveedor"])
                        presentacion, status_presentacion = ProductosModel(session).agregar_presentacion(nombre=producto["presentacion"])
                        print(presentacion.nombre)
                        unidad_medida, status_unidad_medida = ProductosModel(session).agregar_unidad_medida(nombre=producto["unidad_medida"])
                        categoria, status_categoria = CategoriasModel(session).agregar(tipo_categoria="productos", nombre=producto["categoria"])
                        
                        if estatus_proveedor:
                            proveedores = [proveedor]
                        else:
                            proveedores = []  # Si no hay proveedor, pasa una lista vacía
                        
                        producto, estatus_producto = ProductosModel(session).agregar_producto(
                            codigo_upc=producto["codigo_barras"],
                            nombre_producto=producto["nombre"],
                            descripcion_producto=producto["descripcion"],
                            costo_inicial=producto["costo_inicial"],
                            costo_final=producto["costo_final"],
                            margen_porcentaje=f'{producto["margen_porcentaje"]} %',
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
                            fecha_fabricacion=producto["fecha_fabricacion"] if self.ui.opcion_TieneCaducidad.isChecked() or producto["fecha_fabricacion"] is not None else None,
                            fecha_vencimiento=producto["fecha_vencimiento"] if self.ui.opcion_TieneCaducidad.isChecked() or producto["fecha_fabricacion"] is not None else None,
                            imagen=self.imagenProducto if self.imagenProducto is not None else producto["imagen"],
                            notas=producto["notas"],
                            presentacion_producto_id=presentacion.id,
                            unidad_medida_productos_id=unidad_medida.id,
                            categoria_id=categoria.id,
                            sucursales=[],  # Si no tienes sucursales, pasa una lista vacía
                            proveedores=proveedores
                        )
                        
                        if not estatus_producto:
                            productos_no_agregados.append(producto)
                
                session.commit()  # Aquí se hace commit después de finalizar la transacción
            except Exception as e:
                session.rollback()  # Si ocurre un error, revertimos los cambios
                print(f"Error al guardar productos: {e}")
                Mensaje().mensaje_informativo("Ocurrió un error al guardar los productos. No se realizaron cambios.")
            
        if productos_no_agregados:
            Mensaje().mensaje_informativo("Existen productos que no se agregaron debido a que ya existen en la base de datos.")
            self.__cargar_datos_en_tabla(productos_no_agregados)

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
        lista_proveedores_a_asignar = []
        if not self.producto:
            Mensaje().mensaje_informativo("No se selecciono ningun producto para actualizar")
            return
        datos_producto = self.datos_campos()
        todos_los_proveedores = self.proveedores_vinculados | self.lista_proveedores_a_asignar
        
        for id_elemento, objeto in todos_los_proveedores.items():
            lista_proveedores_a_asignar.append(objeto)
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
                    proveedores = lista_proveedores_a_asignar
                )
        self.PRODUCTOS_AGREGADOS.emit()
        self.close()
    
    def __cargar_datos_en_campos(self, producto):
        self.ui.txt_codBarras.setEnabled(False)
        # self.producto = producto
        if producto is None:
            Mensaje().mensaje_informativo("No haz seleccionado ningun producto")
            return
        self.ui.contenedor_proveedores_vinculados.show()
        self.ui.contenedor_proveedores_existentes.show()
        self.ui.contenedor_proveedores_a_vincular.show()
        self.ui.txt_proveedor.hide()
        self.ui.etiqueta_proveedor.hide()
        
        self.producto = producto
        margenPorcentaje_mostrar = int(self.producto.margen_porcentaje.split(" ")[0])
        self.ui.tabla_productos.hide()
        self.ui.btn_btn_addProduct_agregar_producto.hide()
        self.ui.btn_btn_addProduct_guardar_producto.hide()
        self.ui.etiqueta_listaProductos.hide()
        self.ui.btn_btn_addProduct_cargar_CSVProductos.hide()
        self.ui.btn_btn_addProduct_limpiarTablaProductos.hide()
        self.ui.btn_btn_addProduct_actualizar_producto.show()
        with Conexion_base_datos() as db:
            session = db.abrir_sesion()
            with session.begin():
                categorias, estatuscategoria = CategoriasModel(session).obtener_todo(tipo_categoria="productos")
                unidadades_medida, estatusmedida = ProductosModel(session).obtener_unidades_medida()
                presentaciones, estatuspresentacion = ProductosModel(session).obtener_presentaciones()
            if estatuscategoria:
                for cate in categorias:
                    self.ui.cajaOpciones_categoriaProducto.addItem(cate.nombre, cate)
                    AjustarCajaOpciones().ajustar_cajadeopciones(self.ui.cajaOpciones_categoriaProducto)
            if estatusmedida:
                for medida in unidadades_medida:
                    self.ui.cajaOpciones_unidadMedidaProducto.addItem(medida.nombre, medida)
                    AjustarCajaOpciones().ajustar_cajadeopciones(self.ui.cajaOpciones_unidadMedidaProducto)
            if estatuspresentacion:
                for presentacion in presentaciones:
                    self.ui.cajaOpciones_presentacionProducto.addItem(presentacion.nombre, presentacion)
                    AjustarCajaOpciones().ajustar_cajadeopciones(self.ui.cajaOpciones_presentacionProducto)
        self.ui.txt_codBarras.setText(producto.codigo_upc)
        self.ui.txt_nombreProducto.setText(producto.nombre_producto)
        self.ui.txt_marcaProducto.setText(producto.marca)
        self.ui.txt_modeloProducto.setText(producto.modelo)
        self.ui.txt_colorProducto.setText(producto.color)
        self.ui.txt_materialProducto.setText(producto.material)
        self.ui.txtlargo_descripcionProducto.setPlainText(producto.descripcion_producto)
        self.ui.txtlargo_notasProducto.setPlainText(producto.notas)
        self.ui.decimal_costoInicialProducto.setValue(producto.costo_inicial)
        self.ui.decimal_costoFinalProducto.setValue(producto.costo_final)
        self.ui.entero_margenProducto.setValue(margenPorcentaje_mostrar)
        self.ui.decimal_precioVentaProducto.setValue(producto.precio)
        self.ui.decimal_existenciaProducto.setValue(producto.existencia)
        self.ui.decimal_existenciaMinProducto.setValue(producto.existencia_minima)
        self.ui.decimal_existenciaMaxProducto.setValue(producto.existencia_maxima)
        self.ui.decimal_pesoProducto.setValue(producto.peso)
        if producto.fecha_fabricacion:
            self.ui.opcion_TieneCaducidad.setChecked(True)
            self.ui.fecha_fabricacionProducto.setDate(producto.fecha_fabricacion)
            self.ui.fecha_vencimientoProducto.setDate(producto.fecha_vencimiento)
        if producto.imagen:
            self.ui.etiqueta_fotoProducto.setPixmap(QPixmap(producto.imagen).scaled(self.ui.etiqueta_fotoProducto.size()))
        
        if producto.dimensiones:
            dimensiones = producto.dimensiones.split("-")
            try:
                # Convertir las cadenas a flotantes
                alto = float(dimensiones[0])
                ancho = float(dimensiones[1])
                largo = float(dimensiones[2])
                
                # Establecer los valores en los QDoubleSpinBox
                self.ui.decimal_altoDimensiones.setValue(alto)
                self.ui.decimal_anchoDimensiones.setValue(ancho)
                self.ui.decimal_largoDimensiones.setValue(largo)
            except Exception as e:
                print(f"Error al cargar dimensiones: {e}")
        
        if producto.categoria:
            if estatuscategoria:
                area_nombre = producto.categoria.nombre
                caja_categorias = self.ui.cajaOpciones_categoriaProducto
                indice = caja_categorias.findText(area_nombre)

                if indice != -1:
                    caja_categorias.removeItem(indice)

                caja_categorias.insertItem(0, area_nombre)
                
                caja_categorias.setItemData(0, producto.categoria)

                caja_categorias.setCurrentIndex(0)
        
        if producto.unidad_medida_productos:
            if estatusmedida:
                medida_nombre = producto.unidad_medida_productos.nombre
                caja_medidas = self.ui.cajaOpciones_unidadMedidaProducto
                indice = caja_medidas.findText(medida_nombre)

                if indice != -1:
                    caja_medidas.removeItem(indice)

                caja_medidas.insertItem(0, medida_nombre)
                caja_medidas.setItemData(0, producto.unidad_medida_productos)

                caja_medidas.setCurrentIndex(0)
        
        if producto.presentacion_productos:
            if estatusmedida:
                presentacion_nombre = producto.presentacion_productos.nombre
                caja_presentaciones = self.ui.cajaOpciones_presentacionProducto
                indice = caja_presentaciones.findText(presentacion_nombre)

                if indice != -1:
                    caja_presentaciones.removeItem(indice)

                caja_presentaciones.insertItem(0, presentacion_nombre)
                
                caja_presentaciones.setItemData(0, producto.presentacion_productos)

                caja_presentaciones.setCurrentIndex(0)

        if producto.proveedores:
            self.proveedores_vinculados = {proveedor.id : proveedor for proveedor in producto.proveedores}
            self.listar_proveedores(self.proveedores_vinculados)
    
    def listar_proveedores(self, proveedores):
        self.ui.lista_proveedores_vinculados.clear()
        self.icono_proveedor = QIcon(":/Icons/Bootstrap/file-person.svg")
        for proveedor_id, proveedor in proveedores.items():
            # Crear un QListWidgetItem
                proveedor_nombre = proveedor.nombre
                item = QListWidgetItem(proveedor_nombre)
                
                # Establecer el ícono en el ítem
                item.setIcon(self.icono_proveedor)
                item.setData(Qt.UserRole, proveedor_id)
                
                # Agregar el ítem a la lista
                self.ui.lista_proveedores_vinculados.addItem(item)
    
    def __limpiar_tabla_productos(self):
        self.modelo_tabla_productos.removeRows(0, self.modelo_tabla_productos.rowCount())
        self.lista_productos = []
                
    def __obtener_proveedores(self):
        with Conexion_base_datos() as db:
            session = db.abrir_sesion()
            with session.begin():
                self.proveedores_generales, estado = ProveedoresModel(session).obtener_proveedores()
            if estado:
                for proveedor in self.proveedores_generales:
                    self.proveedores[proveedor.id] = proveedor
                    
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
            for proveedor_id, proveedor in self.proveedores.items():
                proveedor_nombre = proveedor.nombre
                item = QListWidgetItem(proveedor_nombre)
                item.setIcon(self.icono_proveedor)  # Establecer el ícono en el ítem
                item.setData(Qt.UserRole, proveedor)  # Establecer el ID del proveedor como datos
                # Agregar el ítem a la lista
                self.ui.lista_todos_los_proveedores.addItem(item)
        else:
            # Si hay proveedores vinculados, listar sólo aquellos que no estén vinculados
            for proveedor_id, proveedor in self.proveedores.items():
                # Comprobar si el proveedor ya está vinculado
                if proveedor_id not in self.proveedores_vinculados:
                    proveedor_nombre = proveedor.nombre
                    item = QListWidgetItem(proveedor_nombre)
                    item.setIcon(self.icono_proveedor)  # Establecer el ícono en el ítem
                    item.setData(Qt.UserRole, proveedor)  # Establecer el proveedor como datos
                    # Agregar el ítem a la lista
                    self.ui.lista_todos_los_proveedores.addItem(item)
    
    def buscar_proveedor_existente(self):
        nombre = self.ui.txt_buscar_proveedor_a_vincular.text().upper().strip()
        self.icono_proveedor = QIcon(":/Icons/Bootstrap/file-person.svg")
        if not self.producto.proveedores:
            return
        if nombre:
            self.ui.lista_todos_los_proveedores.clear()
            for proveedor_id, proveedor in self.proveedores.items():
                proveedor_nombre = proveedor.nombre
                if nombre in proveedor_nombre.upper():
                    item = QListWidgetItem(proveedor_nombre)
                    
                    # Establecer el ícono en el ítem
                    item.setIcon(self.icono_proveedor)
                    item.setData(Qt.UserRole, proveedor)
                    
                    # Agregar el ítem a la lista
                    self.ui.lista_todos_los_proveedores.addItem(item)
        else:
            self.ui.lista_todos_los_proveedores.clear()
            for proveedor_id, proveedor in self.proveedores.items():
                # Comprobar si el proveedor ya está vinculado
                if proveedor_id not in self.proveedores_vinculados:
                    proveedor_nombre = proveedor.nombre
                    item = QListWidgetItem(proveedor_nombre)
                    item.setIcon(self.icono_proveedor)  # Establecer el ícono en el ítem
                    item.setData(Qt.UserRole, proveedor)  # Establecer el proveedor como datos
                    # Agregar el ítem a la lista
                    self.ui.lista_todos_los_proveedores.addItem(item)
    
    def buscar_proveedor_vinculado(self):
        nombre = self.ui.txt_buscar_proveedor_vinculado.text().upper().strip()
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
        # Obtener el ícono, ID y nombre del proveedor
        icono = item.icon()
        proveedor = item.data(Qt.UserRole)
        proveedor_nombre = item.text()

        # Si no hay proveedores asignados, agregar el primero
        if len(self.lista_proveedores_a_asignar) <= 0:
            # Crear un nuevo ítem para el proveedor
            nuevo_proveedor = QListWidgetItem(proveedor_nombre)
            nuevo_proveedor.setIcon(icono)
            nuevo_proveedor.setData(Qt.UserRole, proveedor)

            # Agregar el proveedor al diccionario y a la lista visual
            self.lista_proveedores_a_asignar[proveedor.id] = proveedor
            self.ui.lista_proveedores_a_vincular.addItem(nuevo_proveedor)
            return

        # Si el proveedor no está ya en el diccionario, agregarlo
        if proveedor.id not in self.lista_proveedores_a_asignar:
            self.lista_proveedores_a_asignar[proveedor.id] = proveedor
            nuevo_proveedor = QListWidgetItem(proveedor.nombre)
            nuevo_proveedor.setIcon(icono)
            nuevo_proveedor.setData(Qt.UserRole, proveedor)
            self.ui.lista_proveedores_a_vincular.addItem(nuevo_proveedor)
    
    def desvincular_proveedor_al_producto(self):
        item = self.ui.lista_proveedores_vinculados.currentItem()
        if not item:
            Mensaje().mensaje_informativo("Debes de seleccionar un elemento de la lista")
            return
        try:
            proveedor_id = item.data(Qt.UserRole)
            self.ui.lista_proveedores_vinculados.takeItem(self.ui.lista_proveedores_vinculados.row(item))
            if proveedor_id in self.proveedores_vinculados:
                del self.proveedores_vinculados[proveedor_id]
        except Exception as e:
            Mensaje().mensaje_alerta(f"No se puede realizar la acción debido al siguiente error: {str(e)}")

    def eliminar_proveedor_a_vincular(self):
        item = self.ui.lista_proveedores_a_vincular.currentItem()
        if not item:
            Mensaje().mensaje_informativo("Debes de seleccionar un elemento de la lista")
            return
        proveedor = item.data(Qt.UserRole)
        self.ui.lista_proveedores_a_vincular.takeItem(self.ui.lista_proveedores_a_vincular.row(item))
        if proveedor.id in self.lista_proveedores_a_asignar:
            
            del self.lista_proveedores_a_asignar[proveedor.id]

    def agregarCSV(self):
        lista_duplicados_excel = []
        # Leer el archivo CSV
        df = self.__leer_archivo_csv()
        
        # Si no se pudo leer el archivo o si faltan columnas, salimos
        if df is None:
            return
        
        for row in range(len(df)):
            nuevo_producto = {
                "proveedor": str(df.iloc[row]["Proveedor"]).strip(),
                "codigo_barras": str(df.iloc[row]["Código de Barras"]).strip(),  # Aseguramos que el código esté limpio
                "nombre": str(df.iloc[row]["Nombre"]).strip(),
                "categoria": str(df.iloc[row]["Categoría"]).strip(),
                "marca": str(df.iloc[row]["Marca"]).strip(),
                "modelo": str(df.iloc[row]["Modelo"]).strip(),
                "color": str(df.iloc[row]["Color"]).strip(),
                "material": str(df.iloc[row]["Material"]).strip(),
                "unidad_medida": str(df.iloc[row]["Unidad de Medida"]).strip(),
                "presentacion": str(df.iloc[row]["Presentación"]).strip(),
                "costo_inicial": float(df.iloc[row]["Costo Inicial"]),
                "costo_final": float(df.iloc[row]["Costo Final"]),
                "margen_porcentaje": int(df.iloc[row]["Margen Porcentaje"]),
                "precio_venta": float(df.iloc[row]["Precio Venta"]),
                "existencia": float(df.iloc[row]["Existencia"]),
                "existencia_min": float(df.iloc[row]["Existencia Min"]),
                "existencia_max": float(df.iloc[row]["Existencia Max"]),
                "peso": float(df.iloc[row]["Peso"]),
                "largo_dimensiones": float(df.iloc[row]["Largo Dimensiones"]),
                "alto_dimensiones": float(df.iloc[row]["Alto Dimensiones"]),
                "ancho_dimensiones": float(df.iloc[row]["Ancho Dimensiones"]),
                "descripcion": df.iloc[row]["Descripción"].strip(),
                "notas": df.iloc[row]["Notas"],
                "fecha_vencimiento": df.iloc[row]["Fecha Vencimiento"],
                "fecha_fabricacion": df.iloc[row]["Fecha Fabricación"],
                "imagen": df.iloc[row]["Imagen"].strip()
            }

            # Verificación de duplicados: Compara código de barras limpio con los existentes
            producto_existente = any(str(p["codigo_barras"]).strip() == nuevo_producto["codigo_barras"] for p in self.lista_productos)

            if not producto_existente:
                self.lista_productos.append(nuevo_producto)
            else:
                lista_duplicados_excel.append(producto_existente)


        # Ahora puedes actualizar la tabla si es necesario
        self.__cargar_datos_en_tabla(self.lista_productos)
        
        if len(lista_duplicados_excel) > 0:
            Mensaje().mensaje_informativo("Se encontraron registros duplicados que no fueron agregados.\nSolo se agregaron los registros sin duplicar.")
            
    def __leer_archivo_csv(self):
        documento, _ = QFileDialog.getOpenFileName(self, "Selecciona un documento de Excel", "", "Archivos Excel (*.xlsx *.xls)")
        
        if not documento:
            return None
        
        # Definir las columnas esperadas
        columnas_esperadas = [
            "Proveedor", "Código de Barras", "Nombre", "Categoría", "Marca", "Modelo", "Color",
            "Material", "Unidad de Medida", "Presentación", "Costo Inicial","Costo Final", "Margen Porcentaje", "Precio Venta",
            "Existencia", "Existencia Min", "Existencia Max", "Peso",
            "Largo Dimensiones", "Alto Dimensiones", "Ancho Dimensiones",
            "Descripción", "Notas", "Fecha Vencimiento", "Fecha Fabricación", "Imagen"
        ]
        
        # Leer el archivo Excel
        df = pd.read_excel(documento)
        
        # Verificar si faltan columnas
        columnas_faltantes = [col for col in columnas_esperadas if col not in df.columns]
        if columnas_faltantes:
            Mensaje().mensaje_alerta(f"Error: Faltan las siguientes columnas: {', '.join(columnas_faltantes)}")
            return None
        
        # Reordenar las columnas según el orden esperado
        df = df[columnas_esperadas]
        
        # Verificar si hay columnas adicionales
        columnas_extra = [col for col in df.columns if col not in columnas_esperadas]
        if columnas_extra:
            Mensaje().mensaje_alerta(f"Advertencia: El archivo contiene columnas adicionales: {', '.join(columnas_extra)}")
        
        return df
    
    def __cargar_datos_en_tabla(self, lista_productos):
        self.modelo_tabla_productos.setHorizontalHeaderLabels([
            "Proveedor", "Código de Barras", "Nombre", "Categoría", "Marca", "Modelo", "Color", 
            "Material", "Unidad de Medida", "Presentación", "Costo Inicial","Costo Final", "Margen Porcentaje", "Precio Venta", 
            "Existencia", "Existencia Min", "Existencia Max", "Peso", 
            "Largo Dimensiones", "Alto Dimensiones", "Ancho Dimensiones", 
            "Descripción", "Notas", "Fecha Vencimiento", "Fecha Fabricación", "Imagen"
        ])
        
        row_count = self.modelo_tabla_productos.rowCount()
        self.modelo_tabla_productos.removeRows(0, row_count)
        
        # Recorrer la lista de productos y agregar los datos a la tabla
        for producto in lista_productos:
            self.lista_productos_tabla = []
            
            # Agregar cada valor del diccionario como una celda en la fila
            for key in producto:
                item = QStandardItem(str(producto[key]))
                item.setTextAlignment(Qt.AlignCenter)  # Centrar el texto
                self.lista_productos_tabla.append(item)
            
            # Agregar la fila completa al modelo
            self.modelo_tabla_productos.appendRow(self.lista_productos_tabla)
        
        # Asignar el modelo a la tabla
        self.ui.tabla_productos.setModel(self.modelo_tabla_productos)
        
        # Ajustar el tamaño de las columnas automáticamente
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
        
        
        
        self.datos_usuario = datos_usuario
        self.seleccion_conectada_productos = None
        self.codigo_upc_producto = None
        self.AdminProductos = None
        self.ventana_existencia_productos = None
        self.comprobar_modelo_tabla_productos()
        
    def  buscar_producto(self):
        nombre_producto = self.ui.txt_buscar.text().strip()
        with Conexion_base_datos() as db:
            session = db.abrir_sesion()
            with session.begin():
                productos, estatus = ProductosModel(session).consultar_por_nombre(nombre=nombre_producto)
            if estatus:
                self.listar_productos(productos)
    
    def agregar_producto(self):
        if self.AdminProductos is None or self.AdminProductos.isVisible():
            self.AdminProductos = Admin_productosController(self)
            self.LISTAR_CATEGORIAS_PRODUCTOS.connect(self.AdminProductos.listar_categorias)
            self.LISTAR_UNIDADES_MEDIDA_PRODUCTOS.connect(self.AdminProductos.listar_unidades_medida)
            self.LISTAR_PRESENTACIONES_PRODUCTOS.connect(self.AdminProductos.listar_presentaciones_productos)
            self.AdminProductos.VENTANA_CERRADA_PRODUCTOS.connect(self.ventana_productos_cerrada)
            self.AdminProductos.PRODUCTOS_AGREGADOS.connect(self.consultar_productos_db)
            self.LISTAR_CATEGORIAS_PRODUCTOS.emit()
            self.LISTAR_UNIDADES_MEDIDA_PRODUCTOS.emit()
            self.LISTAR_PRESENTACIONES_PRODUCTOS.emit()
            self.AdminProductos.show()
        else:
            self.AdminProductos.raise_()
            self.AdminProductos.activateWindow()
            
    def ventana_productos_cerrada(self):
        self.AdminProductos = None
    
    def eliminar_producto(self):
        if self.codigo_upc_producto is None:
            Mensaje().mensaje_informativo("Debes de seleccionar un producto de la tabla para proceder a eliminarlo")
            return
        estatus_eliminacion = False
        with Conexion_base_datos() as db:
            session = db.abrir_sesion()
            with session.begin():
                estatus_eliminacion = ProductosModel(session).eliminar_producto(codigo_producto=self.codigo_upc_producto)
        if estatus_eliminacion:
            Mensaje().mensaje_informativo("El producto ha sido eliminado con éxito")
            self.consultar_productos_db()
            self.codigo_upc_producto = None
    
    def modificar_producto(self):
        if self.codigo_upc_producto is None:
            Mensaje().mensaje_informativo("No has seleccionado un producto de la tabla para proceder a modificarlo")
            return
        if self.AdminProductos is None or not self.AdminProductos.isVisible():
            self.AdminProductos = Admin_productosController(self)
            
            self.AdminProductos.setParent(self)
            self.AdminProductos.setStyleSheet(self.AdminProductos.styleSheet())
            # Conexión de señales
            self.LISTAR_PROVEEDORES_EXISTENTES_SIGNAL.connect(
                self.AdminProductos.listar_proveedores_existentes
            )
            self.AdminProductos.PRODUCTOS_AGREGADOS.connect(
                self.consultar_productos_db
            )
            self.AdminProductos.VENTANA_CERRADA_PRODUCTOS.connect(self.ventana_productos_cerrada)
            self.AdminProductos.show()
        else:
            self.AdminProductos.raise_()
            self.AdminProductos.activateWindow()
            
        with Conexion_base_datos() as db:
            session = db.abrir_sesion()
            with session.begin():
                producto, estatus = ProductosModel(session).consultar_producto_por_codigoUPC(codigo_upc=self.codigo_upc_producto)
            if estatus:
                self.LISTAR_PROVEEDORES_EXISTENTES_SIGNAL.connect(self.AdminProductos.listar_proveedores_existentes)
                self.AdminProductos.PRODUCTOS_AGREGADOS.connect(self.consultar_productos_db)
                self.AdminProductos.RECIBIR_PRODUCTO_ACTUALIZAR.emit(producto)
                self.LISTAR_PROVEEDORES_EXISTENTES_SIGNAL.emit()
                
        self.codigo_upc_producto = None

    def listar_productos(self, productos):
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

        # Recorrer la lista de productos (ahora objetos de la clase Productos)
        for producto in productos:
            list_productos = []

            for col in cabeceras:
                value = ""

                if col.lower() == "proveedor":
                    value = ", ".join([proveedor.nombre for proveedor in producto.proveedores]) if producto.proveedores else ""
                elif col.lower() == "categoria":
                    value = producto.categoria.nombre if producto.categoria else ""
                elif col.lower() == "unidad de medida":
                    # Asegúrate de acceder correctamente a la relación 'unidad_medida_productos' y a su atributo 'unidad_medida'
                    if producto.unidad_medida_productos:
                        value = producto.unidad_medida_productos.nombre  # Accedemos al atributo 'unidad_medida'
                    else:
                        value = ""
                elif col.lower() == "presentacion":
                    # Asegúrate de acceder correctamente a la relación 'presentacion_productos' y a su atributo 'nombre'
                    if producto.presentacion_productos:
                        value = producto.presentacion_productos.nombre  # Accedemos al atributo 'nombre'
                    else:
                        value = ""
                elif hasattr(producto, col.lower().replace(" ", "_")):
                    value = getattr(producto, col.lower().replace(" ", "_"))
                
                item = QStandardItem(str(value))  
                item.setTextAlignment(Qt.AlignCenter)
                list_productos.append(item)

            self.modelo_tabla_productos.appendRow(list_productos)

        self.ui.tabla_productos.setModel(self.modelo_tabla_productos)
        self.ui.tabla_productos.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.tabla_productos.resizeColumnsToContents()
        
        if self.seleccion_conectada_productos:
            self.ui.tabla_productos.selectionModel().currentChanged.disconnect(self.obtener_id_elemento_tabla_productos)
            self.seleccion_conectada_productos = False  # Actualizar el estado

        # Conectar la señal a la función que obtiene el ID del elemento seleccionado
        self.ui.tabla_productos.selectionModel().currentChanged.connect(self.obtener_id_elemento_tabla_productos)
        self.seleccion_conectada_productos = True  # Marcar como conectada

    def consultar_productos_db(self):
        with Conexion_base_datos() as db:
            session = db.abrir_sesion()
            with session.begin():
                productos, estatus = ProductosModel(session).obtener_productos()
            if estatus:
                self.listar_productos(productos)
                
    def obtener_id_elemento_tabla_productos(self, current, previus):
        # Verifica si la celda seleccionada está en la primera columna
        if current.column() >= 0:  # Verifica si es la primera columna
            indice_fila = current.row()
            elemento = self.modelo_tabla_productos.item(indice_fila, 1)
            if elemento is not None:
                self.codigo_upc_producto= None
                self.codigo_upc_producto = elemento.text()
            else:
                return
    
    def comprobar_modelo_tabla_productos(self):
        # Si no existe el modelo de la tabla, crearlo como QStandardItemModel
        if not hasattr(self, 'modelo_tabla_productos'):
            self.modelo_tabla_productos = QStandardItemModel()

            # Asignar el modelo al QTableView si no está asignado
            self.ui.tabla_productos.setModel(self.modelo_tabla_productos)

    def existencia_productos(self):
        if self.codigo_upc_producto is None:
            Mensaje().mensaje_informativo('Selecciona un producto.')
            return
        with Conexion_base_datos() as db:
            session = db.abrir_sesion()
            with session.begin():
                producto, estatus = ProductosModel(session).consultar_producto_por_codigoUPC(codigo_upc=self.codigo_upc_producto)
            if not estatus:
                Mensaje().mensaje_informativo("No se logro obtener el producto en la base de datos.")
                return
            self.ventana_existencia_productos = ExistenciasClase(self, datos_usuario = self.datos_usuario, producto=producto)
            self.ventana_existencia_productos.VENTANA_CERRADA_EXISTENCIA.connect(self.ventana_cerrada_form_existencia)
            self.ventana_existencia_productos.show()
        
    def ventana_cerrada_form_existencia(self):
        self.ventana_existencia_productos = None