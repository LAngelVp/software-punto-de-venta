# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PRODUCTOS_PROVEEDORES.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QTabWidget, QTableView, QVBoxLayout,
    QWidget)
import ibootstrap_rc
import iconosSVG_rc

class Ui_contenedor_productos_proveedores(object):
    def setupUi(self, contenedor_productos_proveedores):
        if not contenedor_productos_proveedores.objectName():
            contenedor_productos_proveedores.setObjectName(u"contenedor_productos_proveedores")
        contenedor_productos_proveedores.resize(1020, 468)
        contenedor_productos_proveedores.setStyleSheet(u"*{color: #1d1c1c;}\n"
"#contenedor_encabezado{\n"
"background: #023375;\n"
"}\n"
"#etiqueta_encabezado_productosProveedor{\n"
"color: #fffefb;\n"
"font-size: 18px;\n"
"font-weight:bold;\n"
"font-family:\"Arial\";\n"
"}\n"
"[objectName*=\"contenedor\"]{\n"
"background: #fffefb;\n"
"border:none;\n"
"}\n"
"[objectName*=\"etiqueta_\"]{\n"
"font-size:14px;\n"
"font-family: Arial;\n"
"font-weight:bold;\n"
"color: #1d1c1c;\n"
"}\n"
"[objectName*=\"txt_\"]{\n"
"background: #F5F5F5;\n"
"border:none;\n"
"border-radius: 5px;\n"
"color: #1d1c1c;\n"
"font-size: 14px;\n"
"border-bottom: 1px solid #787878;\n"
"}\n"
"[objectName*=\"txt_\"]:focus{\n"
"border-bottom: 2px solid #023375;\n"
"}\n"
"[objectName*=\"btn_producto_del_proveedor\"]{\n"
"background: #00619a;\n"
"font-size: 14px;\n"
"font-family: Arial;\n"
"font-weight: bold;\n"
"min-height: 25px;\n"
"border: none;\n"
"border-radius: 5px;\n"
"color: #fffefb;\n"
"padding: 3px 5px;\n"
"}\n"
"[objectName*=\"btn_producto_del_proveedor\"]:hover{\n"
"background: #2196F3;\n"
"}\n"
""
                        "[objectName*=\"btn_producto_del_proveedor\"]:pressed{\n"
"background: #1B80D0;\n"
"}\n"
"[objectName*=\"btn_producto_del_proveedor_eliminar\"]:hover{\n"
"background: #ee1d52;\n"
"}\n"
"[objectName*=\"btn_producto_del_proveedor_eliminar\"]:pressed{\n"
"background: #B13636;\n"
"}\n"
"[objectName*=\"btn_producto_del_proveedor_agregar\"]:hover{\n"
"background: #68a67d;\n"
"}\n"
"[objectName*=\"btn_producto_del_proveedor_agregar\"]:pressed{\n"
"background: #578B69;\n"
"}\n"
"#btn_producto_del_proveedor_cerrar{\n"
"background: #fffefb;\n"
"min-height:15px;\n"
"max-width:15px;\n"
"}\n"
"#btn_producto_del_proveedor_cerrar:pressed{\n"
"background: rgb(222, 221, 218);\n"
"}\n"
"#btn_RefrescarTabla{\n"
"border-radius: 2px;\n"
"background: #e0e0e0;\n"
"padding: 5px;\n"
"}\n"
"#btn_RefrescarTabla:hover{\n"
"background: rgb(179, 179, 179);\n"
"}\n"
"#btn_RefrescarTabla:pressed{\n"
"background: #b6ccd8 ;\n"
"}\n"
"#btn_RefrescarTablaProductos{\n"
"border-radius: 2px;\n"
"background: #e0e0e0;\n"
"padding: 5px;\n"
"}\n"
"#btn_"
                        "RefrescarTablaProductos:hover{\n"
"background: rgb(179, 179, 179);\n"
"}\n"
"#btn_RefrescarTablaProductos:pressed{\n"
"background: #b6ccd8 ;\n"
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
"    border-left-wi"
                        "dth: 1px ;\n"
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
"\n"
"[objectName*=\"tabla_\"] {\n"
"    font-family: Arial;\n"
"    font-size: 14px;\n"
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
"\n"
"/* C"
                        "ONTENEDOR TABS */\n"
"\n"
"QTabWidget::pane {\n"
"        border: none;\n"
"        position: absolute;\n"
"        top: -20px;\n"
"    }\n"
"    \n"
"    /* Pesta\u00f1a no seleccionada */\n"
"    QTabBar::tab {\n"
"        background: #F5F4F1;\n"
"        color: #3B3C3D;\n"
"        border: 1px solid #D3D3D3;\n"
"        border-bottom: none;\n"
"        padding: 6px 15px;\n"
"        min-width: 80px;\n"
"        border-top-left-radius: 4px;\n"
"        border-top-right-radius: 4px;\n"
"        margin-right: 2px;\n"
"    }\n"
"    \n"
"    /* Pesta\u00f1a seleccionada */\n"
"    QTabBar::tab:selected {\n"
"        background: #4791F5;\n"
"        color: white;\n"
"        font-weight: bold;\n"
"    }\n"
"    \n"
"    /* Pesta\u00f1a al pasar el mouse */\n"
"    QTabBar::tab:hover {\n"
"        background: #E8E8E8;\n"
"    }\n"
"    \n"
"    /* Pesta\u00f1a deshabilitada */\n"
"    QTabBar::tab:disabled {\n"
"        background: #EEEEEE;\n"
"        color: #AAAAAA;\n"
"    }\n"
"    \n"
"    /* \u00c1rea de la"
                        "s pesta\u00f1as */\n"
"    QTabBar {\n"
"        background: transparent;\n"
"    }")
        self.verticalLayout = QVBoxLayout(contenedor_productos_proveedores)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.contenedor_encabezado = QFrame(contenedor_productos_proveedores)
        self.contenedor_encabezado.setObjectName(u"contenedor_encabezado")
        self.contenedor_encabezado.setFrameShape(QFrame.Shape.StyledPanel)
        self.contenedor_encabezado.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.contenedor_encabezado)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 2, -1, 2)
        self.etiqueta_encabezado_productosProveedor = QLabel(self.contenedor_encabezado)
        self.etiqueta_encabezado_productosProveedor.setObjectName(u"etiqueta_encabezado_productosProveedor")

        self.horizontalLayout_3.addWidget(self.etiqueta_encabezado_productosProveedor)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.btn_producto_del_proveedor_cerrar = QPushButton(self.contenedor_encabezado)
        self.btn_producto_del_proveedor_cerrar.setObjectName(u"btn_producto_del_proveedor_cerrar")
        self.btn_producto_del_proveedor_cerrar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/Icons/Bootstrap/x-lg.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_producto_del_proveedor_cerrar.setIcon(icon)

        self.horizontalLayout_3.addWidget(self.btn_producto_del_proveedor_cerrar)


        self.verticalLayout.addWidget(self.contenedor_encabezado)

        self.contenedor_scrollarea = QScrollArea(contenedor_productos_proveedores)
        self.contenedor_scrollarea.setObjectName(u"contenedor_scrollarea")
        self.contenedor_scrollarea.setWidgetResizable(True)
        self.contenedor_contenido_scrollarea = QWidget()
        self.contenedor_contenido_scrollarea.setObjectName(u"contenedor_contenido_scrollarea")
        self.contenedor_contenido_scrollarea.setGeometry(QRect(0, 0, 1020, 442))
        self.gridLayout = QGridLayout(self.contenedor_contenido_scrollarea)
        self.gridLayout.setObjectName(u"gridLayout")
        self.etiqueta_nombre_del_proveedor = QLabel(self.contenedor_contenido_scrollarea)
        self.etiqueta_nombre_del_proveedor.setObjectName(u"etiqueta_nombre_del_proveedor")

        self.gridLayout.addWidget(self.etiqueta_nombre_del_proveedor, 0, 0, 1, 1)

        self.contenedor_tabs = QTabWidget(self.contenedor_contenido_scrollarea)
        self.contenedor_tabs.setObjectName(u"contenedor_tabs")
        font = QFont()
        font.setBold(True)
        self.contenedor_tabs.setFont(font)
        self.contenedor_tab_productos_de_proveedor = QWidget()
        self.contenedor_tab_productos_de_proveedor.setObjectName(u"contenedor_tab_productos_de_proveedor")
        self.gridLayout_3 = QGridLayout(self.contenedor_tab_productos_de_proveedor)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.contenedor_productos_proveedor = QFrame(self.contenedor_tab_productos_de_proveedor)
        self.contenedor_productos_proveedor.setObjectName(u"contenedor_productos_proveedor")
        self.contenedor_productos_proveedor.setFrameShape(QFrame.Shape.StyledPanel)
        self.contenedor_productos_proveedor.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_5 = QGridLayout(self.contenedor_productos_proveedor)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setHorizontalSpacing(0)
        self.gridLayout_5.setVerticalSpacing(10)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.contenedor_botones_superior = QFrame(self.contenedor_productos_proveedor)
        self.contenedor_botones_superior.setObjectName(u"contenedor_botones_superior")
        self.contenedor_botones_superior.setFrameShape(QFrame.Shape.StyledPanel)
        self.contenedor_botones_superior.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_4 = QGridLayout(self.contenedor_botones_superior)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.btn_producto_del_proveedor_editar = QPushButton(self.contenedor_botones_superior)
        self.btn_producto_del_proveedor_editar.setObjectName(u"btn_producto_del_proveedor_editar")
        self.btn_producto_del_proveedor_editar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/iconosBlancos/Icons/iconos/Blanco/editar_blanco.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_producto_del_proveedor_editar.setIcon(icon1)

        self.gridLayout_4.addWidget(self.btn_producto_del_proveedor_editar, 1, 3, 1, 1, Qt.AlignmentFlag.AlignRight)

        self.btn_RefrescarTabla = QPushButton(self.contenedor_botones_superior)
        self.btn_RefrescarTabla.setObjectName(u"btn_RefrescarTabla")
        self.btn_RefrescarTabla.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/iconosBlancos/Icons/IconosSVG/base_datos_refresh.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_RefrescarTabla.setIcon(icon2)

        self.gridLayout_4.addWidget(self.btn_RefrescarTabla, 1, 1, 1, 1)

        self.btn_producto_del_proveedor_eliminar = QPushButton(self.contenedor_botones_superior)
        self.btn_producto_del_proveedor_eliminar.setObjectName(u"btn_producto_del_proveedor_eliminar")
        self.btn_producto_del_proveedor_eliminar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/iconosBlancos/Icons/iconos/Blanco/cerrar_blanco.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_producto_del_proveedor_eliminar.setIcon(icon3)

        self.gridLayout_4.addWidget(self.btn_producto_del_proveedor_eliminar, 1, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer, 1, 0, 1, 1)


        self.gridLayout_5.addWidget(self.contenedor_botones_superior, 0, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.etiqueta_nombre_producto = QLabel(self.contenedor_productos_proveedor)
        self.etiqueta_nombre_producto.setObjectName(u"etiqueta_nombre_producto")

        self.horizontalLayout.addWidget(self.etiqueta_nombre_producto)

        self.cajaOpciones_filtro_nombre = QComboBox(self.contenedor_productos_proveedor)
        self.cajaOpciones_filtro_nombre.addItem("")
        self.cajaOpciones_filtro_nombre.addItem("")
        self.cajaOpciones_filtro_nombre.setObjectName(u"cajaOpciones_filtro_nombre")

        self.horizontalLayout.addWidget(self.cajaOpciones_filtro_nombre)

        self.txt_nombre_producto = QLineEdit(self.contenedor_productos_proveedor)
        self.txt_nombre_producto.setObjectName(u"txt_nombre_producto")
        self.txt_nombre_producto.setClearButtonEnabled(True)

        self.horizontalLayout.addWidget(self.txt_nombre_producto)


        self.gridLayout_5.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        self.tabla_productos_del_proveedor = QTableView(self.contenedor_productos_proveedor)
        self.tabla_productos_del_proveedor.setObjectName(u"tabla_productos_del_proveedor")
        self.tabla_productos_del_proveedor.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tabla_productos_del_proveedor.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tabla_productos_del_proveedor.setGridStyle(Qt.PenStyle.DashLine)
        self.tabla_productos_del_proveedor.horizontalHeader().setMinimumSectionSize(150)
        self.tabla_productos_del_proveedor.horizontalHeader().setDefaultSectionSize(200)
        self.tabla_productos_del_proveedor.horizontalHeader().setStretchLastSection(True)
        self.tabla_productos_del_proveedor.verticalHeader().setVisible(False)
        self.tabla_productos_del_proveedor.verticalHeader().setStretchLastSection(False)

        self.gridLayout_5.addWidget(self.tabla_productos_del_proveedor, 2, 0, 1, 1)


        self.gridLayout_3.addWidget(self.contenedor_productos_proveedor, 0, 0, 1, 1)

        icon4 = QIcon()
        icon4.addFile(u":/Icons/Bootstrap/box-seam.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.contenedor_tabs.addTab(self.contenedor_tab_productos_de_proveedor, icon4, "")
        self.contenedor_tab_productos_de_sistema = QWidget()
        self.contenedor_tab_productos_de_sistema.setObjectName(u"contenedor_tab_productos_de_sistema")
        self.gridLayout_9 = QGridLayout(self.contenedor_tab_productos_de_sistema)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.contenedor_botones_superior_productos_del_sistema = QFrame(self.contenedor_tab_productos_de_sistema)
        self.contenedor_botones_superior_productos_del_sistema.setObjectName(u"contenedor_botones_superior_productos_del_sistema")
        self.contenedor_botones_superior_productos_del_sistema.setFrameShape(QFrame.Shape.StyledPanel)
        self.contenedor_botones_superior_productos_del_sistema.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_7 = QGridLayout(self.contenedor_botones_superior_productos_del_sistema)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.horizontalSpacer_2 = QSpacerItem(577, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_2, 0, 0, 1, 1)

        self.btn_producto_del_proveedor_para_agregar = QPushButton(self.contenedor_botones_superior_productos_del_sistema)
        self.btn_producto_del_proveedor_para_agregar.setObjectName(u"btn_producto_del_proveedor_para_agregar")
        self.btn_producto_del_proveedor_para_agregar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u":/iconosBlancos/Icons/iconos/Blanco/vincular.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_producto_del_proveedor_para_agregar.setIcon(icon5)

        self.gridLayout_7.addWidget(self.btn_producto_del_proveedor_para_agregar, 0, 2, 1, 1)

        self.btn_RefrescarTablaProductos = QPushButton(self.contenedor_botones_superior_productos_del_sistema)
        self.btn_RefrescarTablaProductos.setObjectName(u"btn_RefrescarTablaProductos")
        self.btn_RefrescarTablaProductos.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_RefrescarTablaProductos.setIcon(icon2)

        self.gridLayout_7.addWidget(self.btn_RefrescarTablaProductos, 0, 1, 1, 1)


        self.gridLayout_9.addWidget(self.contenedor_botones_superior_productos_del_sistema, 0, 0, 1, 2)

        self.contenedor_contenido_tab_productos_del_sistema = QFrame(self.contenedor_tab_productos_de_sistema)
        self.contenedor_contenido_tab_productos_del_sistema.setObjectName(u"contenedor_contenido_tab_productos_del_sistema")
        self.contenedor_contenido_tab_productos_del_sistema.setFrameShape(QFrame.Shape.StyledPanel)
        self.contenedor_contenido_tab_productos_del_sistema.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_8 = QGridLayout(self.contenedor_contenido_tab_productos_del_sistema)
        self.gridLayout_8.setSpacing(10)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.etiqueta_nombreproducto_del_sistema = QLabel(self.contenedor_contenido_tab_productos_del_sistema)
        self.etiqueta_nombreproducto_del_sistema.setObjectName(u"etiqueta_nombreproducto_del_sistema")

        self.horizontalLayout_2.addWidget(self.etiqueta_nombreproducto_del_sistema)

        self.cajaOpciones_filtro_nombre_productos_del_sistema = QComboBox(self.contenedor_contenido_tab_productos_del_sistema)
        self.cajaOpciones_filtro_nombre_productos_del_sistema.addItem("")
        self.cajaOpciones_filtro_nombre_productos_del_sistema.addItem("")
        self.cajaOpciones_filtro_nombre_productos_del_sistema.setObjectName(u"cajaOpciones_filtro_nombre_productos_del_sistema")

        self.horizontalLayout_2.addWidget(self.cajaOpciones_filtro_nombre_productos_del_sistema)

        self.txt_nombre_productodelsistema = QLineEdit(self.contenedor_contenido_tab_productos_del_sistema)
        self.txt_nombre_productodelsistema.setObjectName(u"txt_nombre_productodelsistema")
        self.txt_nombre_productodelsistema.setClearButtonEnabled(True)

        self.horizontalLayout_2.addWidget(self.txt_nombre_productodelsistema)


        self.gridLayout_8.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)

        self.tabla_productos_del_sistema = QTableView(self.contenedor_contenido_tab_productos_del_sistema)
        self.tabla_productos_del_sistema.setObjectName(u"tabla_productos_del_sistema")
        self.tabla_productos_del_sistema.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tabla_productos_del_sistema.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tabla_productos_del_sistema.setGridStyle(Qt.PenStyle.DashLine)
        self.tabla_productos_del_sistema.horizontalHeader().setMinimumSectionSize(150)
        self.tabla_productos_del_sistema.horizontalHeader().setDefaultSectionSize(200)
        self.tabla_productos_del_sistema.horizontalHeader().setStretchLastSection(True)
        self.tabla_productos_del_sistema.verticalHeader().setVisible(False)

        self.gridLayout_8.addWidget(self.tabla_productos_del_sistema, 2, 0, 1, 1)


        self.gridLayout_9.addWidget(self.contenedor_contenido_tab_productos_del_sistema, 1, 0, 1, 1)

        self.contenedor_frame = QFrame(self.contenedor_tab_productos_de_sistema)
        self.contenedor_frame.setObjectName(u"contenedor_frame")
        self.contenedor_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.contenedor_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_6 = QGridLayout(self.contenedor_frame)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.etiqueta_producto_agregarAProveedor = QLabel(self.contenedor_frame)
        self.etiqueta_producto_agregarAProveedor.setObjectName(u"etiqueta_producto_agregarAProveedor")

        self.gridLayout_6.addWidget(self.etiqueta_producto_agregarAProveedor, 0, 0, 1, 1)

        self.tabla_Productos_A_VincularProveedor = QTableView(self.contenedor_frame)
        self.tabla_Productos_A_VincularProveedor.setObjectName(u"tabla_Productos_A_VincularProveedor")
        self.tabla_Productos_A_VincularProveedor.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tabla_Productos_A_VincularProveedor.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tabla_Productos_A_VincularProveedor.horizontalHeader().setStretchLastSection(True)

        self.gridLayout_6.addWidget(self.tabla_Productos_A_VincularProveedor, 1, 0, 1, 1)


        self.gridLayout_9.addWidget(self.contenedor_frame, 1, 1, 1, 1)

        icon6 = QIcon()
        icon6.addFile(u":/Icons/Bootstrap/boxes.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.contenedor_tabs.addTab(self.contenedor_tab_productos_de_sistema, icon6, "")

        self.gridLayout.addWidget(self.contenedor_tabs, 1, 0, 1, 1)

        self.contenedor_scrollarea.setWidget(self.contenedor_contenido_scrollarea)

        self.verticalLayout.addWidget(self.contenedor_scrollarea)


        self.retranslateUi(contenedor_productos_proveedores)

        self.contenedor_tabs.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(contenedor_productos_proveedores)
    # setupUi

    def retranslateUi(self, contenedor_productos_proveedores):
        contenedor_productos_proveedores.setWindowTitle(QCoreApplication.translate("contenedor_productos_proveedores", u"Form", None))
        self.etiqueta_encabezado_productosProveedor.setText(QCoreApplication.translate("contenedor_productos_proveedores", u"PRODUCTOS DEL PROVEEDOR", None))
        self.btn_producto_del_proveedor_cerrar.setText("")
        self.etiqueta_nombre_del_proveedor.setText("")
        self.btn_producto_del_proveedor_editar.setText(QCoreApplication.translate("contenedor_productos_proveedores", u"Manejar Precio", None))
#if QT_CONFIG(tooltip)
        self.btn_RefrescarTabla.setToolTip(QCoreApplication.translate("contenedor_productos_proveedores", u"Refrescar tabla", None))
#endif // QT_CONFIG(tooltip)
        self.btn_RefrescarTabla.setText("")
        self.btn_producto_del_proveedor_eliminar.setText(QCoreApplication.translate("contenedor_productos_proveedores", u"Quitar", None))
        self.etiqueta_nombre_producto.setText(QCoreApplication.translate("contenedor_productos_proveedores", u"Buscar Producto", None))
        self.cajaOpciones_filtro_nombre.setItemText(0, QCoreApplication.translate("contenedor_productos_proveedores", u"Igual A", None))
        self.cajaOpciones_filtro_nombre.setItemText(1, QCoreApplication.translate("contenedor_productos_proveedores", u"Que Contenga", None))

        self.txt_nombre_producto.setPlaceholderText(QCoreApplication.translate("contenedor_productos_proveedores", u"Nombre del Producto", None))
        self.contenedor_tabs.setTabText(self.contenedor_tabs.indexOf(self.contenedor_tab_productos_de_proveedor), QCoreApplication.translate("contenedor_productos_proveedores", u"Productos del Proveedor", None))
        self.btn_producto_del_proveedor_para_agregar.setText(QCoreApplication.translate("contenedor_productos_proveedores", u"Vincular al proveedor", None))
#if QT_CONFIG(tooltip)
        self.btn_RefrescarTablaProductos.setToolTip(QCoreApplication.translate("contenedor_productos_proveedores", u"Refrescar tabla", None))
#endif // QT_CONFIG(tooltip)
        self.btn_RefrescarTablaProductos.setText("")
        self.etiqueta_nombreproducto_del_sistema.setText(QCoreApplication.translate("contenedor_productos_proveedores", u"Nombre del Producto:", None))
        self.cajaOpciones_filtro_nombre_productos_del_sistema.setItemText(0, QCoreApplication.translate("contenedor_productos_proveedores", u"Es Igual", None))
        self.cajaOpciones_filtro_nombre_productos_del_sistema.setItemText(1, QCoreApplication.translate("contenedor_productos_proveedores", u"Que Contenga", None))

        self.txt_nombre_productodelsistema.setPlaceholderText(QCoreApplication.translate("contenedor_productos_proveedores", u"Nombre del Producto", None))
        self.etiqueta_producto_agregarAProveedor.setText(QCoreApplication.translate("contenedor_productos_proveedores", u"Productos a vincular con el proveedor", None))
        self.contenedor_tabs.setTabText(self.contenedor_tabs.indexOf(self.contenedor_tab_productos_de_sistema), QCoreApplication.translate("contenedor_productos_proveedores", u"Productos del Sistema", None))
    # retranslateUi

