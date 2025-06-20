# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UI_AGREGARPRODUCTO.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QCheckBox, QComboBox,
    QDateEdit, QDoubleSpinBox, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLayout,
    QLineEdit, QListWidget, QListWidgetItem, QPlainTextEdit,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QSpinBox, QTableView, QVBoxLayout, QWidget)
import ibootstrap_rc
import iconosSVG_rc
import iconsdvg_rc

class Ui_contenedor_agregar_productos(object):
    def setupUi(self, contenedor_agregar_productos):
        if not contenedor_agregar_productos.objectName():
            contenedor_agregar_productos.setObjectName(u"contenedor_agregar_productos")
        contenedor_agregar_productos.setWindowModality(Qt.WindowModality.WindowModal)
        contenedor_agregar_productos.resize(1162, 592)
        contenedor_agregar_productos.setAutoFillBackground(False)
        contenedor_agregar_productos.setStyleSheet(u"*{color: #1d1c1c;}\n"
"#etiqueta_barras{\n"
"image: url(:/Icons/Bootstrap/upc-scan.svg);\n"
"min-width:30px;\n"
"}\n"
"[objectName*=\"contenedor\"]{\n"
"background: #fffefb;\n"
"border:none;\n"
"}\n"
"#contenedor_encabezado{\n"
"background: #023375;\n"
"}\n"
"#etiqueta_titulo_ventana{\n"
"font-size: 20px;\n"
"max-height:40px;\n"
"padding-left: 2px;\n"
"color:#fffefb;\n"
"font-weight:bold;\n"
"}\n"
"#etiqueta_fotoProducto{\n"
"min-height: 200px;\n"
"min-width:200px;\n"
"max-height: 200px;\n"
"max-width:200px;\n"
"border: 1px solid #023375;\n"
"}\n"
"[objectName*=\"etiqueta\"]{\n"
"font-size: 14px;\n"
"font-weight:bold;\n"
"font-family: \"Arial\";\n"
"}\n"
"[objectName*=\"txt\"]{\n"
"border-bottom:  1px solid #787878;\n"
"border-radius: 3px;\n"
"background: #F5F5F5;\n"
"min-width:100px;\n"
"font-size: 14px;\n"
"font-family:\"Arial\";\n"
"}\n"
"[objectName*=\"txt\"]:hover{\n"
"border-bottom:  2px solid #023375;\n"
"}\n"
"[objectName*=\"txt\"]:focus{\n"
"border-bottom:  2px solid #023375;\n"
"}\n"
"[objectName*=\""
                        "txtlargo\"]{\n"
"max-height:100px;\n"
"}\n"
"[objectName*=\"btn_btn_addProduct\"]{\n"
"border:none;\n"
"font-size:14px;\n"
"font-family:\"Arial\";\n"
"font-weight:bold;\n"
"padding: 5px;\n"
"background: #00619a;\n"
"color: #fffefb;\n"
"border-radius: 4px;\n"
"max-height: 15px;\n"
"}\n"
"#btn_btn_addProduct_agregar_categoria{\n"
"padding: 3px;\n"
"}\n"
"[objectName*=\"btn_btn\"]:hover{\n"
"background:#2196F3;\n"
"}\n"
"[objectName*=\"btn_btn\"]:pressed{\n"
"background:#1B80D0;\n"
"}\n"
"#btn_btn_addProduct_guardar_producto:hover{\n"
"background:#68a67d;\n"
"}\n"
"#btn_btn_addProduct_agregar_producto:pressed{\n"
"background:#578B69;\n"
"}\n"
"[objectName*=\"btn_btn_addProduct_eliminar\"]:hover{\n"
"background:#ee1d52;\n"
"}\n"
"[objectName*=\"btn_btn_addProduct_eliminar\"]:pressed{\n"
"background:#B13636;\n"
"}\n"
"#btn_btn_addProduct_cerrar{\n"
"background: #fffefb;\n"
"}\n"
"#btn_btn_addProduct_cerrar:pressed{\n"
"background: rgb(222, 221, 218);\n"
"}\n"
"[objectName*=\"opcion_\"]{\n"
"font-size: 14px;\n"
"fon"
                        "t-weight:bold;\n"
"font-family: \"Arial\";\n"
"}\n"
"[objectName*=\"lista\"]{\n"
"background: #F5F5F5;\n"
"min-height: 150px;\n"
"}\n"
"[objectName*=\"cajaOpciones\"] {\n"
"    border: none;\n"
"    border-bottom: 1px solid #787878 ;\n"
"    padding: 2px ;\n"
"    background-color: #F5F5F5 ;\n"
"    font-size: 14px ;\n"
"    min-width: 200px ;\n"
"    font-family: \"Arial\" ;\n"
"    color: #1d1c1c ;\n"
"	selection-background-color: #4791F5; \n"
"}\n"
"\n"
"/* ESTILO DEL DROPDOWN (LISTA) */\n"
"[objectName*=\"cajaOpciones\"] QListView {\n"
"    background: #F5F5F5 ;\n"
"    border-radius: 3px;\n"
"    outline: none;\n"
"}\n"
"\n"
"/* ESTILO DE LOS \u00cdTEMS */\n"
"[objectName*=\"cajaOpciones\"] QListView::item {\n"
"    padding: 6px 10px ;\n"
"    margin: 2px ;\n"
"}\n"
"/* BOT\u00d3N DESPLEGABLE */\n"
"[objectName*=\"cajaOpciones\"]::drop-down {\n"
"    subcontrol-origin: padding ;\n"
"    subcontrol-position: top right ;\n"
"    padding-right: 5px ;\n"
"    width: 20% ;\n"
"    border-left-width: 1px ;\n"
""
                        "    border-radius: 3px ;\n"
"    background-color: #F5F5F5 ;\n"
"}\n"
"/* FLECHA DESPLEGABLE */\n"
"[objectName*=\"cajaOpciones\"]::down-arrow {\n"
"    image: url(:/Icons/Bootstrap/filter-left.svg);\n"
"    width: 17% ;\n"
"    height: 17% ;\n"
"    padding-left: 5px ;\n"
"    padding-right: 5px ;\n"
"}\n"
"[objectName*=\"decimal\"]{\n"
"min-width:100px;\n"
"background: #F5F5F5;\n"
"borde:none;\n"
"border-radius: 2px;\n"
"border-bottom: 1px solid #787878;\n"
"padding: 0px 2px;\n"
"font-size: 14px;\n"
"font-family: \"Arial\";\n"
"}\n"
"[objectName*=\"decimal\"]:focus{\n"
"border-bottom: 2px solid #023375;\n"
"}\n"
"[objectName*=\"entero\"]{\n"
"min-width:100px;\n"
"background: #F5F5F5;\n"
"borde:none;\n"
"border-radius: 2px;\n"
"border-bottom: 1px solid #787878;\n"
"padding: 0px 2px;\n"
"font-size: 14px;\n"
"font-family: \"Arial\";\n"
"}\n"
"[objectName*=\"entero\"]:focus{\n"
"border-bottom: 2px solid #023375;\n"
"}\n"
"/* FECHA */\n"
"[objectName*=\"fecha_\"]{\n"
"border: none;\n"
"border-bottom: 1px solid #3"
                        "b3c3d;\n"
"border-radius: 5px;\n"
"padding: 2px;\n"
"background-color: #f5f4f1;\n"
"font-size: 14px;\n"
"min-width:100px;\n"
"}\n"
"*[objectName*=\"fecha_\"]::drop-down{\n"
"subcontrol-origin: padding;\n"
"subcontrol-position: top right;\n"
"padding-right:5px;\n"
"width: 20%;\n"
"border-left-width: 1px;\n"
"borde-radius: 5px;\n"
"background-color: #F5F5F5;\n"
"}\n"
"*[objectName*=\"fecha_\"]::down-arrow{\n"
"image: url(:/Icons/Bootstrap/calendar2-date.svg);\n"
"width: 17%;\n"
"height: 17%;\n"
"padding-left:5px;\n"
"padding-right:5px;\n"
"background: #F5F5F5;\n"
"}\n"
"*[objectName*=\"fecha_\"]::focus{\n"
"border-bottom: 2px solid #00668c;\n"
"}\n"
"QCalendarWidget QWidget#qt_calendar_navigationbar {\n"
"    background-color: #00668c;\n"
"    color: white;\n"
"    border-top-left-radius: 5px;\n"
"    border-top-right-radius: 5px;\n"
"}\n"
"\n"
"/* BOTONES DE NAVEGACI\u00d3N */\n"
"QCalendarWidget QToolButton {\n"
"    background-color: transparent;\n"
"    color: white;\n"
"    font-weight: bold;\n"
"    paddin"
                        "g: 5px;\n"
"}\n"
"\n"
"/* DESPLEGABLE DE MESES */\n"
"QCalendarWidget QMenu {\n"
"    background-color: #FFFFFF;\n"
"    border: 1px solid #3b3c3d;\n"
"}\n"
"\n"
"/* D\u00cdAS DE LA SEMANA */\n"
"QCalendarWidget QWidget#qt_calendar_weekdaybar {\n"
"    background-color: #f5f4f1;\n"
"    color: #3b3c3d;\n"
"}\n"
"\n"
"/* D\u00cdAS DEL MES */\n"
"QCalendarWidget QAbstractItemView:enabled {\n"
"    background-color: #FFFFFF;\n"
"    color: #1d1c1c;\n"
"    selection-background-color: #00668c;  /* Color al seleccionar fecha */\n"
"    selection-color: white;\n"
"}\n"
"\n"
"/* D\u00cdAS DE OTROS MESES */\n"
"QCalendarWidget QAbstractItemView:disabled {\n"
"    color: #AAAAAA;\n"
"}\n"
"\n"
"/* EFECTO HOVER SOBRE D\u00cdAS */\n"
"QCalendarWidget QAbstractItemView::item:hover {\n"
"    background-color: #e1f0f7;\n"
"    color: #1d1c1c;\n"
"}\n"
"#etiqueta_listaProductos{\n"
"min-height: 0px;\n"
"max-height: 35px;\n"
"}\n"
"/*TABLA*/\n"
"\n"
"[objectName*=\"tabla_\"] {\n"
"    font-family: Arial;\n"
"    font-size: 14"
                        "px;\n"
"background: #F5F5F5;\n"
"}\n"
"\n"
"/* Encabezados de la tabla */\n"
"[objectName*=\"tabla_\"] QHeaderView::section {\n"
"    background-color: #023375;\n"
"    color: white;\n"
"    font-family: \"Arial\";\n"
"    font-size: 16px;\n"
"    padding: 5px;\n"
"    border: 1px solid gray;\n"
"}\n"
"\n"
"/* Encabezado horizontal */\n"
"[objectName*=\"tabla_\"] QHeaderView::horizontal {\n"
"    background-color: #023375;\n"
"    color: white;\n"
"}\n"
"\n"
"/* Encabezado vertical */\n"
"[objectName*=\"tabla_\"] QHeaderView::vertical {\n"
"    background-color: #023375;\n"
"    color: white;\n"
"}\n"
"#tabla_productos{\n"
"min-height: 350px;\n"
"}")
        self.gridLayout = QGridLayout(contenedor_agregar_productos)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.contenedor_general = QFrame(contenedor_agregar_productos)
        self.contenedor_general.setObjectName(u"contenedor_general")
        self.contenedor_general.setFrameShape(QFrame.Shape.StyledPanel)
        self.contenedor_general.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_14 = QGridLayout(self.contenedor_general)
        self.gridLayout_14.setSpacing(0)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.gridLayout_14.setContentsMargins(0, 0, 0, 0)
        self.contenedor_encabezado = QFrame(self.contenedor_general)
        self.contenedor_encabezado.setObjectName(u"contenedor_encabezado")
        self.contenedor_encabezado.setFrameShape(QFrame.Shape.StyledPanel)
        self.contenedor_encabezado.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.contenedor_encabezado)
        self.horizontalLayout_13.setSpacing(5)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 5, 5, 5)
        self.etiqueta_titulo_ventana = QLabel(self.contenedor_encabezado)
        self.etiqueta_titulo_ventana.setObjectName(u"etiqueta_titulo_ventana")

        self.horizontalLayout_13.addWidget(self.etiqueta_titulo_ventana)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_4)

        self.btn_btn_addProduct_cerrar = QPushButton(self.contenedor_encabezado)
        self.btn_btn_addProduct_cerrar.setObjectName(u"btn_btn_addProduct_cerrar")
        self.btn_btn_addProduct_cerrar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/Icons/Bootstrap/x-lg.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_btn_addProduct_cerrar.setIcon(icon)

        self.horizontalLayout_13.addWidget(self.btn_btn_addProduct_cerrar)


        self.gridLayout_14.addWidget(self.contenedor_encabezado, 0, 0, 1, 1)

        self.contenedor_informacion = QFrame(self.contenedor_general)
        self.contenedor_informacion.setObjectName(u"contenedor_informacion")
        self.contenedor_informacion.setFrameShape(QFrame.Shape.StyledPanel)
        self.contenedor_informacion.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_3 = QGridLayout(self.contenedor_informacion)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.contenedor_formulario_izquierda = QScrollArea(self.contenedor_informacion)
        self.contenedor_formulario_izquierda.setObjectName(u"contenedor_formulario_izquierda")
        self.contenedor_formulario_izquierda.setWidgetResizable(True)
        self.contenedor_scroll_formulario = QWidget()
        self.contenedor_scroll_formulario.setObjectName(u"contenedor_scroll_formulario")
        self.contenedor_scroll_formulario.setGeometry(QRect(0, 0, 1361, 1212))
        self.gridLayout_13 = QGridLayout(self.contenedor_scroll_formulario)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.etiqueta_material = QLabel(self.contenedor_scroll_formulario)
        self.etiqueta_material.setObjectName(u"etiqueta_material")

        self.horizontalLayout_10.addWidget(self.etiqueta_material)

        self.txt_materialProducto = QLineEdit(self.contenedor_scroll_formulario)
        self.txt_materialProducto.setObjectName(u"txt_materialProducto")

        self.horizontalLayout_10.addWidget(self.txt_materialProducto)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.etiqueta_marca = QLabel(self.contenedor_scroll_formulario)
        self.etiqueta_marca.setObjectName(u"etiqueta_marca")

        self.horizontalLayout_3.addWidget(self.etiqueta_marca)

        self.txt_marcaProducto = QLineEdit(self.contenedor_scroll_formulario)
        self.txt_marcaProducto.setObjectName(u"txt_marcaProducto")

        self.horizontalLayout_3.addWidget(self.txt_marcaProducto)

        self.etiqueta_modelo = QLabel(self.contenedor_scroll_formulario)
        self.etiqueta_modelo.setObjectName(u"etiqueta_modelo")

        self.horizontalLayout_3.addWidget(self.etiqueta_modelo)

        self.txt_modeloProducto = QLineEdit(self.contenedor_scroll_formulario)
        self.txt_modeloProducto.setObjectName(u"txt_modeloProducto")

        self.horizontalLayout_3.addWidget(self.txt_modeloProducto)

        self.etiqueta_color = QLabel(self.contenedor_scroll_formulario)
        self.etiqueta_color.setObjectName(u"etiqueta_color")

        self.horizontalLayout_3.addWidget(self.etiqueta_color)

        self.txt_colorProducto = QLineEdit(self.contenedor_scroll_formulario)
        self.txt_colorProducto.setObjectName(u"txt_colorProducto")

        self.horizontalLayout_3.addWidget(self.txt_colorProducto)


        self.horizontalLayout_10.addLayout(self.horizontalLayout_3)


        self.gridLayout_13.addLayout(self.horizontalLayout_10, 3, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 25, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_13.addItem(self.verticalSpacer, 7, 1, 1, 1)

        self.contenedor_FechasCaducidades = QFrame(self.contenedor_scroll_formulario)
        self.contenedor_FechasCaducidades.setObjectName(u"contenedor_FechasCaducidades")
        self.contenedor_FechasCaducidades.setFrameShape(QFrame.Shape.StyledPanel)
        self.contenedor_FechasCaducidades.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_4 = QGridLayout(self.contenedor_FechasCaducidades)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setHorizontalSpacing(0)
        self.gridLayout_4.setVerticalSpacing(-1)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.contenedor_contenedorFechaCaducidad = QFrame(self.contenedor_FechasCaducidades)
        self.contenedor_contenedorFechaCaducidad.setObjectName(u"contenedor_contenedorFechaCaducidad")
        self.contenedor_contenedorFechaCaducidad.setFrameShape(QFrame.Shape.StyledPanel)
        self.contenedor_contenedorFechaCaducidad.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_12 = QGridLayout(self.contenedor_contenedorFechaCaducidad)
        self.gridLayout_12.setSpacing(0)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setContentsMargins(0, 0, 0, 0)
        self.contenedor_fechas = QGridLayout()
        self.contenedor_fechas.setObjectName(u"contenedor_fechas")
        self.fecha_vencimientoProducto = QDateEdit(self.contenedor_contenedorFechaCaducidad)
        self.fecha_vencimientoProducto.setObjectName(u"fecha_vencimientoProducto")
        self.fecha_vencimientoProducto.setWrapping(False)
        self.fecha_vencimientoProducto.setFrame(True)
        self.fecha_vencimientoProducto.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.fecha_vencimientoProducto.setCorrectionMode(QAbstractSpinBox.CorrectionMode.CorrectToPreviousValue)
        self.fecha_vencimientoProducto.setCalendarPopup(True)

        self.contenedor_fechas.addWidget(self.fecha_vencimientoProducto, 2, 1, 1, 1)

        self.etiqueta_fechaVencimiento = QLabel(self.contenedor_contenedorFechaCaducidad)
        self.etiqueta_fechaVencimiento.setObjectName(u"etiqueta_fechaVencimiento")

        self.contenedor_fechas.addWidget(self.etiqueta_fechaVencimiento, 2, 0, 1, 1)


        self.gridLayout_12.addLayout(self.contenedor_fechas, 2, 0, 1, 1)


        self.gridLayout_4.addWidget(self.contenedor_contenedorFechaCaducidad, 3, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_3, 4, 0, 1, 1)

        self.etiqueta_fechaFabricacion = QLabel(self.contenedor_FechasCaducidades)
        self.etiqueta_fechaFabricacion.setObjectName(u"etiqueta_fechaFabricacion")

        self.gridLayout_4.addWidget(self.etiqueta_fechaFabricacion, 0, 0, 1, 1)

        self.fecha_fabricacionProducto = QDateEdit(self.contenedor_FechasCaducidades)
        self.fecha_fabricacionProducto.setObjectName(u"fecha_fabricacionProducto")
        self.fecha_fabricacionProducto.setCalendarPopup(True)

        self.gridLayout_4.addWidget(self.fecha_fabricacionProducto, 1, 0, 1, 1)

        self.opcion_TieneCaducidad = QCheckBox(self.contenedor_FechasCaducidades)
        self.opcion_TieneCaducidad.setObjectName(u"opcion_TieneCaducidad")

        self.gridLayout_4.addWidget(self.opcion_TieneCaducidad, 2, 0, 1, 1)


        self.gridLayout_13.addWidget(self.contenedor_FechasCaducidades, 0, 1, 4, 2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.etiqueta_nombreProducto = QLabel(self.contenedor_scroll_formulario)
        self.etiqueta_nombreProducto.setObjectName(u"etiqueta_nombreProducto")

        self.horizontalLayout_2.addWidget(self.etiqueta_nombreProducto)

        self.txt_nombreProducto = QLineEdit(self.contenedor_scroll_formulario)
        self.txt_nombreProducto.setObjectName(u"txt_nombreProducto")

        self.horizontalLayout_2.addWidget(self.txt_nombreProducto)


        self.gridLayout_13.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.etiqueta_categoriaProducto = QLabel(self.contenedor_scroll_formulario)
        self.etiqueta_categoriaProducto.setObjectName(u"etiqueta_categoriaProducto")

        self.horizontalLayout_7.addWidget(self.etiqueta_categoriaProducto)

        self.cajaOpciones_categoriaProducto = QComboBox(self.contenedor_scroll_formulario)
        self.cajaOpciones_categoriaProducto.setObjectName(u"cajaOpciones_categoriaProducto")

        self.horizontalLayout_7.addWidget(self.cajaOpciones_categoriaProducto)

        self.btn_btn_addProduct_agregar_categoria = QPushButton(self.contenedor_scroll_formulario)
        self.btn_btn_addProduct_agregar_categoria.setObjectName(u"btn_btn_addProduct_agregar_categoria")
        self.btn_btn_addProduct_agregar_categoria.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/iconosBlancos/Icons/iconos/Blanco/agregar_blanco.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_btn_addProduct_agregar_categoria.setIcon(icon1)

        self.horizontalLayout_7.addWidget(self.btn_btn_addProduct_agregar_categoria)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.etiqueta_presentacionProducto = QLabel(self.contenedor_scroll_formulario)
        self.etiqueta_presentacionProducto.setObjectName(u"etiqueta_presentacionProducto")

        self.horizontalLayout_5.addWidget(self.etiqueta_presentacionProducto)

        self.cajaOpciones_presentacionProducto = QComboBox(self.contenedor_scroll_formulario)
        self.cajaOpciones_presentacionProducto.setObjectName(u"cajaOpciones_presentacionProducto")

        self.horizontalLayout_5.addWidget(self.cajaOpciones_presentacionProducto)

        self.btn_btn_addProduct_agregarPresentacionProducto = QPushButton(self.contenedor_scroll_formulario)
        self.btn_btn_addProduct_agregarPresentacionProducto.setObjectName(u"btn_btn_addProduct_agregarPresentacionProducto")
        self.btn_btn_addProduct_agregarPresentacionProducto.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_btn_addProduct_agregarPresentacionProducto.setIcon(icon1)

        self.horizontalLayout_5.addWidget(self.btn_btn_addProduct_agregarPresentacionProducto)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.etiqueta_unidadMedida = QLabel(self.contenedor_scroll_formulario)
        self.etiqueta_unidadMedida.setObjectName(u"etiqueta_unidadMedida")

        self.horizontalLayout_9.addWidget(self.etiqueta_unidadMedida)

        self.cajaOpciones_unidadMedidaProducto = QComboBox(self.contenedor_scroll_formulario)
        self.cajaOpciones_unidadMedidaProducto.setObjectName(u"cajaOpciones_unidadMedidaProducto")
        self.cajaOpciones_unidadMedidaProducto.setSizeAdjustPolicy(QComboBox.SizeAdjustPolicy.AdjustToContentsOnFirstShow)

        self.horizontalLayout_9.addWidget(self.cajaOpciones_unidadMedidaProducto)

        self.btn_btn_addProduct_agregar_unidadMedidaProducto = QPushButton(self.contenedor_scroll_formulario)
        self.btn_btn_addProduct_agregar_unidadMedidaProducto.setObjectName(u"btn_btn_addProduct_agregar_unidadMedidaProducto")
        self.btn_btn_addProduct_agregar_unidadMedidaProducto.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_btn_addProduct_agregar_unidadMedidaProducto.setIcon(icon1)

        self.horizontalLayout_9.addWidget(self.btn_btn_addProduct_agregar_unidadMedidaProducto)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_9)


        self.horizontalLayout_7.addLayout(self.horizontalLayout_5)


        self.gridLayout_13.addLayout(self.horizontalLayout_7, 4, 0, 1, 3)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.btn_btn_addProduct_limpiarTablaProductos = QPushButton(self.contenedor_scroll_formulario)
        self.btn_btn_addProduct_limpiarTablaProductos.setObjectName(u"btn_btn_addProduct_limpiarTablaProductos")
        self.btn_btn_addProduct_limpiarTablaProductos.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_11.addWidget(self.btn_btn_addProduct_limpiarTablaProductos)

        self.btn_btn_addProduct_cargar_CSVProductos = QPushButton(self.contenedor_scroll_formulario)
        self.btn_btn_addProduct_cargar_CSVProductos.setObjectName(u"btn_btn_addProduct_cargar_CSVProductos")
        self.btn_btn_addProduct_cargar_CSVProductos.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_11.addWidget(self.btn_btn_addProduct_cargar_CSVProductos)


        self.gridLayout_13.addLayout(self.horizontalLayout_11, 7, 2, 1, 1)

        self.contenedor_formulario_derecha = QFrame(self.contenedor_scroll_formulario)
        self.contenedor_formulario_derecha.setObjectName(u"contenedor_formulario_derecha")
        self.contenedor_formulario_derecha.setFrameShape(QFrame.Shape.StyledPanel)
        self.contenedor_formulario_derecha.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contenedor_formulario_derecha)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.contenedor_foto = QFrame(self.contenedor_formulario_derecha)
        self.contenedor_foto.setObjectName(u"contenedor_foto")
        self.contenedor_foto.setFrameShape(QFrame.Shape.StyledPanel)
        self.contenedor_foto.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.contenedor_foto)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.etiqueta_fotoProducto = QLabel(self.contenedor_foto)
        self.etiqueta_fotoProducto.setObjectName(u"etiqueta_fotoProducto")
        self.etiqueta_fotoProducto.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.etiqueta_fotoProducto.setFrameShape(QFrame.Shape.NoFrame)
        self.etiqueta_fotoProducto.setFrameShadow(QFrame.Shadow.Plain)
        self.etiqueta_fotoProducto.setTextFormat(Qt.TextFormat.AutoText)
        self.etiqueta_fotoProducto.setScaledContents(True)

        self.gridLayout_2.addWidget(self.etiqueta_fotoProducto, 0, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.contenedor_foto)

        self.verticalSpacer_2 = QSpacerItem(20, 473, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)


        self.gridLayout_13.addWidget(self.contenedor_formulario_derecha, 0, 3, 14, 1)

        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.txtlargo_notasProducto = QPlainTextEdit(self.contenedor_scroll_formulario)
        self.txtlargo_notasProducto.setObjectName(u"txtlargo_notasProducto")

        self.gridLayout_9.addWidget(self.txtlargo_notasProducto, 1, 1, 1, 1)

        self.etiqueta_notasProducto = QLabel(self.contenedor_scroll_formulario)
        self.etiqueta_notasProducto.setObjectName(u"etiqueta_notasProducto")

        self.gridLayout_9.addWidget(self.etiqueta_notasProducto, 0, 1, 1, 1)

        self.etiqueta_descripcionProducto = QLabel(self.contenedor_scroll_formulario)
        self.etiqueta_descripcionProducto.setObjectName(u"etiqueta_descripcionProducto")

        self.gridLayout_9.addWidget(self.etiqueta_descripcionProducto, 0, 0, 1, 1)

        self.txtlargo_descripcionProducto = QPlainTextEdit(self.contenedor_scroll_formulario)
        self.txtlargo_descripcionProducto.setObjectName(u"txtlargo_descripcionProducto")

        self.gridLayout_9.addWidget(self.txtlargo_descripcionProducto, 1, 0, 1, 1)


        self.gridLayout_13.addLayout(self.gridLayout_9, 6, 0, 1, 3)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.decimal_pesoProducto = QDoubleSpinBox(self.contenedor_scroll_formulario)
        self.decimal_pesoProducto.setObjectName(u"decimal_pesoProducto")
        self.decimal_pesoProducto.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.decimal_pesoProducto.setMaximum(10000000000.000000000000000)

        self.gridLayout_5.addWidget(self.decimal_pesoProducto, 2, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_3, 0, 8, 1, 1)

        self.decimal_existenciaProducto = QDoubleSpinBox(self.contenedor_scroll_formulario)
        self.decimal_existenciaProducto.setObjectName(u"decimal_existenciaProducto")
        self.decimal_existenciaProducto.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.decimal_existenciaProducto.setMaximum(10000000000.000000000000000)

        self.gridLayout_5.addWidget(self.decimal_existenciaProducto, 1, 1, 1, 1)

        self.etiqueta_pesoProducto = QLabel(self.contenedor_scroll_formulario)
        self.etiqueta_pesoProducto.setObjectName(u"etiqueta_pesoProducto")

        self.gridLayout_5.addWidget(self.etiqueta_pesoProducto, 2, 0, 1, 1)

        self.decimal_costoInicialProducto = QDoubleSpinBox(self.contenedor_scroll_formulario)
        self.decimal_costoInicialProducto.setObjectName(u"decimal_costoInicialProducto")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.decimal_costoInicialProducto.sizePolicy().hasHeightForWidth())
        self.decimal_costoInicialProducto.setSizePolicy(sizePolicy)
        self.decimal_costoInicialProducto.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.decimal_costoInicialProducto.setMaximum(10000000000.000000000000000)

        self.gridLayout_5.addWidget(self.decimal_costoInicialProducto, 0, 1, 1, 1)

        self.etiqueta_existenciaProducto = QLabel(self.contenedor_scroll_formulario)
        self.etiqueta_existenciaProducto.setObjectName(u"etiqueta_existenciaProducto")

        self.gridLayout_5.addWidget(self.etiqueta_existenciaProducto, 1, 0, 1, 1)

        self.etiqueta_costoInicialProducto = QLabel(self.contenedor_scroll_formulario)
        self.etiqueta_costoInicialProducto.setObjectName(u"etiqueta_costoInicialProducto")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.etiqueta_costoInicialProducto.sizePolicy().hasHeightForWidth())
        self.etiqueta_costoInicialProducto.setSizePolicy(sizePolicy1)

        self.gridLayout_5.addWidget(self.etiqueta_costoInicialProducto, 0, 0, 1, 1)

        self.gridLayout_11 = QGridLayout()
        self.gridLayout_11.setObjectName(u"gridLayout_11")

        self.gridLayout_5.addLayout(self.gridLayout_11, 1, 8, 2, 1)

        self.etiqueta_precioVentaProducto = QLabel(self.contenedor_scroll_formulario)
        self.etiqueta_precioVentaProducto.setObjectName(u"etiqueta_precioVentaProducto")
        sizePolicy1.setHeightForWidth(self.etiqueta_precioVentaProducto.sizePolicy().hasHeightForWidth())
        self.etiqueta_precioVentaProducto.setSizePolicy(sizePolicy1)

        self.gridLayout_5.addWidget(self.etiqueta_precioVentaProducto, 0, 6, 1, 1)

        self.decimal_precioVentaProducto = QDoubleSpinBox(self.contenedor_scroll_formulario)
        self.decimal_precioVentaProducto.setObjectName(u"decimal_precioVentaProducto")
        self.decimal_precioVentaProducto.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.decimal_precioVentaProducto.setMaximum(10000000000.000000000000000)

        self.gridLayout_5.addWidget(self.decimal_precioVentaProducto, 0, 7, 1, 1)

        self.etiqueta_existenciaMinProducto = QLabel(self.contenedor_scroll_formulario)
        self.etiqueta_existenciaMinProducto.setObjectName(u"etiqueta_existenciaMinProducto")

        self.gridLayout_5.addWidget(self.etiqueta_existenciaMinProducto, 1, 2, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.etiqueta_dimensiones = QLabel(self.contenedor_scroll_formulario)
        self.etiqueta_dimensiones.setObjectName(u"etiqueta_dimensiones")

        self.horizontalLayout_4.addWidget(self.etiqueta_dimensiones)

        self.decimal_largoDimensiones = QDoubleSpinBox(self.contenedor_scroll_formulario)
        self.decimal_largoDimensiones.setObjectName(u"decimal_largoDimensiones")
        self.decimal_largoDimensiones.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.decimal_largoDimensiones.setMaximum(10000000000.000000000000000)

        self.horizontalLayout_4.addWidget(self.decimal_largoDimensiones)

        self.etiqueta_espacioDimensiones = QLabel(self.contenedor_scroll_formulario)
        self.etiqueta_espacioDimensiones.setObjectName(u"etiqueta_espacioDimensiones")

        self.horizontalLayout_4.addWidget(self.etiqueta_espacioDimensiones)

        self.decimal_altoDimensiones = QDoubleSpinBox(self.contenedor_scroll_formulario)
        self.decimal_altoDimensiones.setObjectName(u"decimal_altoDimensiones")
        self.decimal_altoDimensiones.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.decimal_altoDimensiones.setMaximum(10000000000.000000000000000)

        self.horizontalLayout_4.addWidget(self.decimal_altoDimensiones)

        self.etiqueta_espacioDimensiones_2 = QLabel(self.contenedor_scroll_formulario)
        self.etiqueta_espacioDimensiones_2.setObjectName(u"etiqueta_espacioDimensiones_2")

        self.horizontalLayout_4.addWidget(self.etiqueta_espacioDimensiones_2)

        self.decimal_anchoDimensiones = QDoubleSpinBox(self.contenedor_scroll_formulario)
        self.decimal_anchoDimensiones.setObjectName(u"decimal_anchoDimensiones")
        self.decimal_anchoDimensiones.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.decimal_anchoDimensiones.setMaximum(10000000000.000000000000000)

        self.horizontalLayout_4.addWidget(self.decimal_anchoDimensiones)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)


        self.gridLayout_5.addLayout(self.horizontalLayout_4, 2, 2, 1, 6)

        self.decimal_existenciaMinProducto = QDoubleSpinBox(self.contenedor_scroll_formulario)
        self.decimal_existenciaMinProducto.setObjectName(u"decimal_existenciaMinProducto")
        self.decimal_existenciaMinProducto.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.decimal_existenciaMinProducto.setMaximum(10000000000.000000000000000)

        self.gridLayout_5.addWidget(self.decimal_existenciaMinProducto, 1, 3, 1, 1)

        self.etiqueta_existenciaMaxProducto = QLabel(self.contenedor_scroll_formulario)
        self.etiqueta_existenciaMaxProducto.setObjectName(u"etiqueta_existenciaMaxProducto")
        self.etiqueta_existenciaMaxProducto.setAutoFillBackground(False)
        self.etiqueta_existenciaMaxProducto.setScaledContents(False)

        self.gridLayout_5.addWidget(self.etiqueta_existenciaMaxProducto, 1, 4, 1, 1)

        self.decimal_existenciaMaxProducto = QDoubleSpinBox(self.contenedor_scroll_formulario)
        self.decimal_existenciaMaxProducto.setObjectName(u"decimal_existenciaMaxProducto")
        self.decimal_existenciaMaxProducto.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.decimal_existenciaMaxProducto.setMaximum(10000000000.000000000000000)

        self.gridLayout_5.addWidget(self.decimal_existenciaMaxProducto, 1, 5, 1, 1)

        self.etiqueta_margenProducto = QLabel(self.contenedor_scroll_formulario)
        self.etiqueta_margenProducto.setObjectName(u"etiqueta_margenProducto")
        self.etiqueta_margenProducto.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.gridLayout_5.addWidget(self.etiqueta_margenProducto, 0, 4, 1, 1)

        self.etiqueta_costoFinalProducto = QLabel(self.contenedor_scroll_formulario)
        self.etiqueta_costoFinalProducto.setObjectName(u"etiqueta_costoFinalProducto")
        sizePolicy1.setHeightForWidth(self.etiqueta_costoFinalProducto.sizePolicy().hasHeightForWidth())
        self.etiqueta_costoFinalProducto.setSizePolicy(sizePolicy1)

        self.gridLayout_5.addWidget(self.etiqueta_costoFinalProducto, 0, 2, 1, 1)

        self.decimal_costoFinalProducto = QDoubleSpinBox(self.contenedor_scroll_formulario)
        self.decimal_costoFinalProducto.setObjectName(u"decimal_costoFinalProducto")
        self.decimal_costoFinalProducto.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.decimal_costoFinalProducto.setMaximum(10000000000.000000000000000)

        self.gridLayout_5.addWidget(self.decimal_costoFinalProducto, 0, 3, 1, 1)

        self.entero_margenProducto = QSpinBox(self.contenedor_scroll_formulario)
        self.entero_margenProducto.setObjectName(u"entero_margenProducto")
        self.entero_margenProducto.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.entero_margenProducto.setMaximum(100)

        self.gridLayout_5.addWidget(self.entero_margenProducto, 0, 5, 1, 1)


        self.gridLayout_13.addLayout(self.gridLayout_5, 5, 0, 1, 3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.etiqueta_codBarras = QLabel(self.contenedor_scroll_formulario)
        self.etiqueta_codBarras.setObjectName(u"etiqueta_codBarras")

        self.horizontalLayout.addWidget(self.etiqueta_codBarras)

        self.txt_codBarras = QLineEdit(self.contenedor_scroll_formulario)
        self.txt_codBarras.setObjectName(u"txt_codBarras")

        self.horizontalLayout.addWidget(self.txt_codBarras)

        self.etiqueta_barras = QLabel(self.contenedor_scroll_formulario)
        self.etiqueta_barras.setObjectName(u"etiqueta_barras")

        self.horizontalLayout.addWidget(self.etiqueta_barras)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.gridLayout_13.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.etiqueta_proveedor = QLabel(self.contenedor_scroll_formulario)
        self.etiqueta_proveedor.setObjectName(u"etiqueta_proveedor")

        self.horizontalLayout_8.addWidget(self.etiqueta_proveedor)

        self.txt_proveedor = QLineEdit(self.contenedor_scroll_formulario)
        self.txt_proveedor.setObjectName(u"txt_proveedor")
        self.txt_proveedor.setDragEnabled(False)
        self.txt_proveedor.setClearButtonEnabled(True)

        self.horizontalLayout_8.addWidget(self.txt_proveedor)


        self.gridLayout_13.addLayout(self.horizontalLayout_8, 0, 0, 1, 1)

        self.contenedor_formulario_inferior = QFrame(self.contenedor_scroll_formulario)
        self.contenedor_formulario_inferior.setObjectName(u"contenedor_formulario_inferior")
        self.contenedor_formulario_inferior.setFrameShape(QFrame.Shape.StyledPanel)
        self.contenedor_formulario_inferior.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_7 = QGridLayout(self.contenedor_formulario_inferior)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.contenedor_botones = QFrame(self.contenedor_formulario_inferior)
        self.contenedor_botones.setObjectName(u"contenedor_botones")
        self.contenedor_botones.setFrameShape(QFrame.Shape.StyledPanel)
        self.contenedor_botones.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.contenedor_botones)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.btn_btn_addProduct_agregar_producto = QPushButton(self.contenedor_botones)
        self.btn_btn_addProduct_agregar_producto.setObjectName(u"btn_btn_addProduct_agregar_producto")
        self.btn_btn_addProduct_agregar_producto.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_6.addWidget(self.btn_btn_addProduct_agregar_producto)

        self.btn_btn_addProduct_actualizar_producto = QPushButton(self.contenedor_botones)
        self.btn_btn_addProduct_actualizar_producto.setObjectName(u"btn_btn_addProduct_actualizar_producto")
        self.btn_btn_addProduct_actualizar_producto.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_6.addWidget(self.btn_btn_addProduct_actualizar_producto)


        self.gridLayout_7.addWidget(self.contenedor_botones, 0, 0, 1, 1, Qt.AlignmentFlag.AlignLeft)

        self.btn_btn_addProduct_guardar_producto = QPushButton(self.contenedor_formulario_inferior)
        self.btn_btn_addProduct_guardar_producto.setObjectName(u"btn_btn_addProduct_guardar_producto")
        self.btn_btn_addProduct_guardar_producto.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout_7.addWidget(self.btn_btn_addProduct_guardar_producto, 0, 1, 1, 1, Qt.AlignmentFlag.AlignRight)


        self.gridLayout_13.addWidget(self.contenedor_formulario_inferior, 13, 0, 1, 3)

        self.widget = QWidget(self.contenedor_scroll_formulario)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_12 = QHBoxLayout(self.widget)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.contenedor_proveedores_vinculados = QFrame(self.widget)
        self.contenedor_proveedores_vinculados.setObjectName(u"contenedor_proveedores_vinculados")
        self.contenedor_proveedores_vinculados.setFrameShape(QFrame.Shape.StyledPanel)
        self.contenedor_proveedores_vinculados.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_8 = QGridLayout(self.contenedor_proveedores_vinculados)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.btn_btn_addProduct_desvincular_proveedores = QPushButton(self.contenedor_proveedores_vinculados)
        self.btn_btn_addProduct_desvincular_proveedores.setObjectName(u"btn_btn_addProduct_desvincular_proveedores")
        self.btn_btn_addProduct_desvincular_proveedores.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout_8.addWidget(self.btn_btn_addProduct_desvincular_proveedores, 4, 0, 1, 1)

        self.etiqueta_proveedores_vinculados = QLabel(self.contenedor_proveedores_vinculados)
        self.etiqueta_proveedores_vinculados.setObjectName(u"etiqueta_proveedores_vinculados")

        self.gridLayout_8.addWidget(self.etiqueta_proveedores_vinculados, 1, 0, 1, 1)

        self.lista_proveedores_vinculados = QListWidget(self.contenedor_proveedores_vinculados)
        self.lista_proveedores_vinculados.setObjectName(u"lista_proveedores_vinculados")

        self.gridLayout_8.addWidget(self.lista_proveedores_vinculados, 3, 0, 1, 1)

        self.txt_buscar_proveedor_vinculado = QLineEdit(self.contenedor_proveedores_vinculados)
        self.txt_buscar_proveedor_vinculado.setObjectName(u"txt_buscar_proveedor_vinculado")
        self.txt_buscar_proveedor_vinculado.setClearButtonEnabled(True)

        self.gridLayout_8.addWidget(self.txt_buscar_proveedor_vinculado, 2, 0, 1, 1)


        self.horizontalLayout_12.addWidget(self.contenedor_proveedores_vinculados)

        self.contenedor_proveedores_a_vincular = QFrame(self.widget)
        self.contenedor_proveedores_a_vincular.setObjectName(u"contenedor_proveedores_a_vincular")
        self.contenedor_proveedores_a_vincular.setFrameShape(QFrame.Shape.StyledPanel)
        self.contenedor_proveedores_a_vincular.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_6 = QGridLayout(self.contenedor_proveedores_a_vincular)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.etiqueta_proveedores_a_vincular = QLabel(self.contenedor_proveedores_a_vincular)
        self.etiqueta_proveedores_a_vincular.setObjectName(u"etiqueta_proveedores_a_vincular")

        self.gridLayout_6.addWidget(self.etiqueta_proveedores_a_vincular, 0, 0, 1, 1)

        self.lista_proveedores_a_vincular = QListWidget(self.contenedor_proveedores_a_vincular)
        self.lista_proveedores_a_vincular.setObjectName(u"lista_proveedores_a_vincular")

        self.gridLayout_6.addWidget(self.lista_proveedores_a_vincular, 1, 0, 1, 1)

        self.btn_btn_addProduct_eliminar_proveedor_a_vincular = QPushButton(self.contenedor_proveedores_a_vincular)
        self.btn_btn_addProduct_eliminar_proveedor_a_vincular.setObjectName(u"btn_btn_addProduct_eliminar_proveedor_a_vincular")
        self.btn_btn_addProduct_eliminar_proveedor_a_vincular.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout_6.addWidget(self.btn_btn_addProduct_eliminar_proveedor_a_vincular, 2, 0, 1, 1)


        self.horizontalLayout_12.addWidget(self.contenedor_proveedores_a_vincular)

        self.contenedor_proveedores_existentes = QFrame(self.widget)
        self.contenedor_proveedores_existentes.setObjectName(u"contenedor_proveedores_existentes")
        self.contenedor_proveedores_existentes.setFrameShape(QFrame.Shape.StyledPanel)
        self.contenedor_proveedores_existentes.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_10 = QGridLayout(self.contenedor_proveedores_existentes)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.txt_buscar_proveedor_a_vincular = QLineEdit(self.contenedor_proveedores_existentes)
        self.txt_buscar_proveedor_a_vincular.setObjectName(u"txt_buscar_proveedor_a_vincular")
        self.txt_buscar_proveedor_a_vincular.setClearButtonEnabled(True)

        self.gridLayout_10.addWidget(self.txt_buscar_proveedor_a_vincular, 1, 0, 1, 1)

        self.lista_todos_los_proveedores = QListWidget(self.contenedor_proveedores_existentes)
        self.lista_todos_los_proveedores.setObjectName(u"lista_todos_los_proveedores")

        self.gridLayout_10.addWidget(self.lista_todos_los_proveedores, 2, 0, 1, 1)

        self.btn_btn_addProduct_vincular_proveedor = QPushButton(self.contenedor_proveedores_existentes)
        self.btn_btn_addProduct_vincular_proveedor.setObjectName(u"btn_btn_addProduct_vincular_proveedor")
        self.btn_btn_addProduct_vincular_proveedor.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout_10.addWidget(self.btn_btn_addProduct_vincular_proveedor, 3, 0, 1, 1)

        self.etiqueta_proveedores_existentes = QLabel(self.contenedor_proveedores_existentes)
        self.etiqueta_proveedores_existentes.setObjectName(u"etiqueta_proveedores_existentes")

        self.gridLayout_10.addWidget(self.etiqueta_proveedores_existentes, 0, 0, 1, 1)


        self.horizontalLayout_12.addWidget(self.contenedor_proveedores_existentes)


        self.gridLayout_13.addWidget(self.widget, 8, 0, 1, 3)

        self.tabla_productos = QTableView(self.contenedor_scroll_formulario)
        self.tabla_productos.setObjectName(u"tabla_productos")

        self.gridLayout_13.addWidget(self.tabla_productos, 12, 0, 1, 3)

        self.etiqueta_tituloProductos = QLabel(self.contenedor_scroll_formulario)
        self.etiqueta_tituloProductos.setObjectName(u"etiqueta_tituloProductos")
        self.etiqueta_tituloProductos.setMinimumSize(QSize(0, 0))

        self.gridLayout_13.addWidget(self.etiqueta_tituloProductos, 11, 0, 1, 1)

        self.contenedor_formulario_izquierda.setWidget(self.contenedor_scroll_formulario)

        self.gridLayout_3.addWidget(self.contenedor_formulario_izquierda, 0, 0, 1, 1)


        self.gridLayout_14.addWidget(self.contenedor_informacion, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.contenedor_general, 0, 0, 1, 1)


        self.retranslateUi(contenedor_agregar_productos)

        QMetaObject.connectSlotsByName(contenedor_agregar_productos)
    # setupUi

    def retranslateUi(self, contenedor_agregar_productos):
        contenedor_agregar_productos.setWindowTitle(QCoreApplication.translate("contenedor_agregar_productos", u"Agregar Producto", None))
        self.etiqueta_titulo_ventana.setText(QCoreApplication.translate("contenedor_agregar_productos", u"AGREGAR PRODUCTO", None))
        self.btn_btn_addProduct_cerrar.setText("")
        self.etiqueta_material.setText(QCoreApplication.translate("contenedor_agregar_productos", u"Material", None))
        self.etiqueta_marca.setText(QCoreApplication.translate("contenedor_agregar_productos", u"Marca", None))
        self.etiqueta_modelo.setText(QCoreApplication.translate("contenedor_agregar_productos", u"Modelo", None))
        self.etiqueta_color.setText(QCoreApplication.translate("contenedor_agregar_productos", u"Color", None))
        self.fecha_vencimientoProducto.setDisplayFormat(QCoreApplication.translate("contenedor_agregar_productos", u"dd/MM/yyyy", None))
        self.etiqueta_fechaVencimiento.setText(QCoreApplication.translate("contenedor_agregar_productos", u"Fecha Vencimiento", None))
        self.etiqueta_fechaFabricacion.setText(QCoreApplication.translate("contenedor_agregar_productos", u"Fecha Fabricaci\u00f3n", None))
        self.fecha_fabricacionProducto.setDisplayFormat(QCoreApplication.translate("contenedor_agregar_productos", u"dd/MM/yyyy", None))
        self.opcion_TieneCaducidad.setText(QCoreApplication.translate("contenedor_agregar_productos", u"\u00bfTiene Fecha Caducidad?", None))
        self.etiqueta_nombreProducto.setText(QCoreApplication.translate("contenedor_agregar_productos", u"Nombre", None))
        self.etiqueta_categoriaProducto.setText(QCoreApplication.translate("contenedor_agregar_productos", u"Categoria", None))
        self.btn_btn_addProduct_agregar_categoria.setText("")
        self.etiqueta_presentacionProducto.setText(QCoreApplication.translate("contenedor_agregar_productos", u"Presentaci\u00f3n", None))
        self.btn_btn_addProduct_agregarPresentacionProducto.setText("")
        self.etiqueta_unidadMedida.setText(QCoreApplication.translate("contenedor_agregar_productos", u"Unidad de Medida", None))
        self.btn_btn_addProduct_agregar_unidadMedidaProducto.setText("")
        self.btn_btn_addProduct_limpiarTablaProductos.setText(QCoreApplication.translate("contenedor_agregar_productos", u"Limpiar tabla", None))
        self.btn_btn_addProduct_cargar_CSVProductos.setText(QCoreApplication.translate("contenedor_agregar_productos", u"Cargar excel", None))
        self.etiqueta_fotoProducto.setText(QCoreApplication.translate("contenedor_agregar_productos", u"<html><head/><body><p align=\"center\"><img src=\":/Icons/IconosSVG/subir_imagen.png\" width=\"80\" height=\"70\"/></p><p align=\"center\"><span style=\" font-size:16pt; font-family:Arial; font-weight:bold;\">Cargar Imagen</span></p></body></html>", None))
        self.etiqueta_notasProducto.setText(QCoreApplication.translate("contenedor_agregar_productos", u"Notas", None))
        self.etiqueta_descripcionProducto.setText(QCoreApplication.translate("contenedor_agregar_productos", u"Descripci\u00f3n", None))
        self.etiqueta_pesoProducto.setText(QCoreApplication.translate("contenedor_agregar_productos", u"Peso", None))
        self.etiqueta_existenciaProducto.setText(QCoreApplication.translate("contenedor_agregar_productos", u"Existencia", None))
        self.etiqueta_costoInicialProducto.setText(QCoreApplication.translate("contenedor_agregar_productos", u"Costo Inicial", None))
        self.etiqueta_precioVentaProducto.setText(QCoreApplication.translate("contenedor_agregar_productos", u"Precio Venta", None))
        self.etiqueta_existenciaMinProducto.setText(QCoreApplication.translate("contenedor_agregar_productos", u"Existencia Min.", None))
        self.etiqueta_dimensiones.setText(QCoreApplication.translate("contenedor_agregar_productos", u"Dimensiones", None))
        self.decimal_largoDimensiones.setPrefix("")
        self.decimal_largoDimensiones.setSuffix(QCoreApplication.translate("contenedor_agregar_productos", u"  Alto", None))
        self.etiqueta_espacioDimensiones.setText(QCoreApplication.translate("contenedor_agregar_productos", u"-", None))
        self.decimal_altoDimensiones.setSuffix(QCoreApplication.translate("contenedor_agregar_productos", u"  Largo", None))
        self.etiqueta_espacioDimensiones_2.setText(QCoreApplication.translate("contenedor_agregar_productos", u"-", None))
        self.decimal_anchoDimensiones.setSuffix(QCoreApplication.translate("contenedor_agregar_productos", u"  Ancho", None))
        self.etiqueta_existenciaMaxProducto.setText(QCoreApplication.translate("contenedor_agregar_productos", u"Existencia Max.", None))
        self.etiqueta_margenProducto.setText(QCoreApplication.translate("contenedor_agregar_productos", u"Ganancia Margen", None))
        self.etiqueta_costoFinalProducto.setText(QCoreApplication.translate("contenedor_agregar_productos", u"Costo Final", None))
        self.entero_margenProducto.setSuffix(QCoreApplication.translate("contenedor_agregar_productos", u"%", None))
        self.entero_margenProducto.setPrefix("")
        self.etiqueta_codBarras.setText(QCoreApplication.translate("contenedor_agregar_productos", u"Cod. Barras", None))
        self.etiqueta_barras.setText("")
        self.etiqueta_proveedor.setText(QCoreApplication.translate("contenedor_agregar_productos", u"Proveedor", None))
        self.txt_proveedor.setPlaceholderText(QCoreApplication.translate("contenedor_agregar_productos", u"Escribe el nombre del proveedor", None))
        self.btn_btn_addProduct_agregar_producto.setText(QCoreApplication.translate("contenedor_agregar_productos", u"Agregar producto", None))
        self.btn_btn_addProduct_actualizar_producto.setText(QCoreApplication.translate("contenedor_agregar_productos", u"Actualizar", None))
        self.btn_btn_addProduct_guardar_producto.setText(QCoreApplication.translate("contenedor_agregar_productos", u"Guardar", None))
        self.btn_btn_addProduct_desvincular_proveedores.setText(QCoreApplication.translate("contenedor_agregar_productos", u"Desvincular Proveedor", None))
        self.etiqueta_proveedores_vinculados.setText(QCoreApplication.translate("contenedor_agregar_productos", u"Proveedores Asignados", None))
        self.txt_buscar_proveedor_vinculado.setPlaceholderText(QCoreApplication.translate("contenedor_agregar_productos", u"Nombre del Proveedor", None))
        self.etiqueta_proveedores_a_vincular.setText(QCoreApplication.translate("contenedor_agregar_productos", u"Proveedores a Vincular", None))
        self.btn_btn_addProduct_eliminar_proveedor_a_vincular.setText(QCoreApplication.translate("contenedor_agregar_productos", u"Remover Proveedor", None))
        self.txt_buscar_proveedor_a_vincular.setPlaceholderText(QCoreApplication.translate("contenedor_agregar_productos", u"Nombre del proveedor", None))
        self.btn_btn_addProduct_vincular_proveedor.setText(QCoreApplication.translate("contenedor_agregar_productos", u"Vincular Proveedor", None))
        self.etiqueta_proveedores_existentes.setText(QCoreApplication.translate("contenedor_agregar_productos", u"Proveedores Existentes", None))
        self.etiqueta_tituloProductos.setText(QCoreApplication.translate("contenedor_agregar_productos", u"Lista de Productos", None))
    # retranslateUi

