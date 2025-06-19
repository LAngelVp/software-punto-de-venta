# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UI_CONTROL_PRODUCTOS.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QTableView,
    QVBoxLayout, QWidget)
from ...Source import ibootstrap_rc
from ...Source import iconosSVG_rc

class Ui_Control_Productos(object):
    def setupUi(self, Control_Productos):
        if not Control_Productos.objectName():
            Control_Productos.setObjectName(u"Control_Productos")
        Control_Productos.resize(743, 433)
        Control_Productos.setStyleSheet(u"#Control_Productos{\n"
"background: #fffefb;\n"
"}\n"
"#contenedor{\n"
"background: #fffefb;\n"
"}\n"
"#etiquetaTitulo_productos{\n"
"color:#1d1c1c;\n"
"background-color: #fffefb;\n"
"font-size: 24px;\n"
"font-weight: bold;\n"
"padding-left: 5px;\n"
"text-transform: uppercase;\n"
"font-family: \"Arial\";\n"
"padding-top: 5px;\n"
"}\n"
"[objectName*=\"btn_btn_adminProductos\"]{\n"
"height: 25px;\n"
"border:none;\n"
"border-radius:5px;\n"
"color:#fffefb;\n"
"background:#023375;\n"
"font-size:12px;\n"
"font-family:Arial;\n"
"font-weight:bold;\n"
"padding-left: 5px;\n"
"padding-right:5px;\n"
"}\n"
"[objectName*=\"btn_btn_\"]:hover{\n"
"background:#2196F3;\n"
"}\n"
"#btn_btn_agregar:hover{\n"
"background:#68a67d;\n"
"}\n"
"#btn_btn_eliminar:hover{\n"
"background:#EE1D52;\n"
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
"#e"
                        "tiqueta_buscar{\n"
"image: url(:/iconosAzules/Icons/iconos/Azul/buscar_filas_azul.svg);\n"
"min-width:25px;\n"
"min-height:25px;\n"
"}\n"
"[objectName*=\"txt_\"]{\n"
"font-size: 14px;\n"
"font-family:Arial;\n"
"color:#1d1c1c;\n"
"background: #F5F5F5;\n"
"border:none;\n"
"border-bottom:1px solid #1d1c1c;\n"
"border-radius: 5px;\n"
"}\n"
"[objectName*=\"txt_\"]:focus{\n"
"border-bottom:2px solid #023375;\n"
"}\n"
"/*TABLA*/\n"
"\n"
"[objectName*=\"tabla_\"] {\n"
"    font-family: Arial;\n"
"    font-size: 14px;\n"
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
"[objectName*=\"tabla_\"] QHeaderView::vertica"
                        "l {\n"
"    background-color: #023375;\n"
"    color: white;\n"
"}\n"
"\n"
"")
        self.gridLayout = QGridLayout(Control_Productos)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.contenedor = QFrame(Control_Productos)
        self.contenedor.setObjectName(u"contenedor")
        self.contenedor.setFrameShape(QFrame.StyledPanel)
        self.contenedor.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.contenedor)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.etiquetaTitulo_productos = QLabel(self.contenedor)
        self.etiquetaTitulo_productos.setObjectName(u"etiquetaTitulo_productos")
        self.etiquetaTitulo_productos.setMinimumSize(QSize(0, 40))
        self.etiquetaTitulo_productos.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_2.addWidget(self.etiquetaTitulo_productos, 0, 0, 1, 1)

        self.frame_2 = QFrame(self.contenedor)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_2)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.contenedor_controles = QFrame(self.frame_2)
        self.contenedor_controles.setObjectName(u"contenedor_controles")
        self.contenedor_controles.setFrameShape(QFrame.StyledPanel)
        self.contenedor_controles.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.contenedor_controles)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_btn_adminProductos_agregar = QPushButton(self.contenedor_controles)
        self.btn_btn_adminProductos_agregar.setObjectName(u"btn_btn_adminProductos_agregar")
        self.btn_btn_adminProductos_agregar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/iconosBlancos/Icons/iconos/Blanco/agregar_blanco.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_btn_adminProductos_agregar.setIcon(icon)
        self.btn_btn_adminProductos_agregar.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.btn_btn_adminProductos_agregar)

        self.btn_btn_adminProductos_eliminar = QPushButton(self.contenedor_controles)
        self.btn_btn_adminProductos_eliminar.setObjectName(u"btn_btn_adminProductos_eliminar")
        self.btn_btn_adminProductos_eliminar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/iconosBlancos/Icons/iconos/Blanco/eliminar_blanco.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_btn_adminProductos_eliminar.setIcon(icon1)
        self.btn_btn_adminProductos_eliminar.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.btn_btn_adminProductos_eliminar)

        self.btn_btn_adminProductos_modificar = QPushButton(self.contenedor_controles)
        self.btn_btn_adminProductos_modificar.setObjectName(u"btn_btn_adminProductos_modificar")
        self.btn_btn_adminProductos_modificar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/iconosBlancos/Icons/iconos/Blanco/editar_blanco.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_btn_adminProductos_modificar.setIcon(icon2)
        self.btn_btn_adminProductos_modificar.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.btn_btn_adminProductos_modificar)

        self.btn_btn_adminProductos_ExistenciaProducto = QPushButton(self.contenedor_controles)
        self.btn_btn_adminProductos_ExistenciaProducto.setObjectName(u"btn_btn_adminProductos_ExistenciaProducto")

        self.horizontalLayout.addWidget(self.btn_btn_adminProductos_ExistenciaProducto)


        self.gridLayout_3.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_2, 0, 1, 1, 1)


        self.gridLayout_5.addWidget(self.contenedor_controles, 0, 0, 1, 1)

        self.contenedor_tabla = QFrame(self.frame_2)
        self.contenedor_tabla.setObjectName(u"contenedor_tabla")
        self.contenedor_tabla.setFrameShape(QFrame.StyledPanel)
        self.contenedor_tabla.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.contenedor_tabla)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.contenedor_tabla)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.etiqueta_buscar = QLabel(self.frame)
        self.etiqueta_buscar.setObjectName(u"etiqueta_buscar")

        self.horizontalLayout_2.addWidget(self.etiqueta_buscar)

        self.txt_buscar_productoUPC = QLineEdit(self.frame)
        self.txt_buscar_productoUPC.setObjectName(u"txt_buscar_productoUPC")
        self.txt_buscar_productoUPC.setClearButtonEnabled(True)

        self.horizontalLayout_2.addWidget(self.txt_buscar_productoUPC)

        self.txt_buscar = QLineEdit(self.frame)
        self.txt_buscar.setObjectName(u"txt_buscar")
        self.txt_buscar.setClearButtonEnabled(True)

        self.horizontalLayout_2.addWidget(self.txt_buscar)

        self.btn_btn_adminProductos_buscar = QPushButton(self.frame)
        self.btn_btn_adminProductos_buscar.setObjectName(u"btn_btn_adminProductos_buscar")
        self.btn_btn_adminProductos_buscar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.btn_btn_adminProductos_buscar, 0, Qt.AlignVCenter)

        self.horizontalSpacer = QSpacerItem(290, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.btn_RefrescarTabla = QPushButton(self.frame)
        self.btn_RefrescarTabla.setObjectName(u"btn_RefrescarTabla")
        self.btn_RefrescarTabla.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/iconosBlancos/Icons/IconosSVG/base_datos_refresh.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_RefrescarTabla.setIcon(icon3)

        self.horizontalLayout_2.addWidget(self.btn_RefrescarTabla, 0, Qt.AlignVCenter)


        self.verticalLayout.addWidget(self.frame, 0, Qt.AlignVCenter)

        self.tabla_productos = QTableView(self.contenedor_tabla)
        self.tabla_productos.setObjectName(u"tabla_productos")
        self.tabla_productos.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tabla_productos.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tabla_productos.setGridStyle(Qt.DashDotLine)
        self.tabla_productos.horizontalHeader().setMinimumSectionSize(200)
        self.tabla_productos.horizontalHeader().setDefaultSectionSize(200)

        self.verticalLayout.addWidget(self.tabla_productos)


        self.gridLayout_5.addWidget(self.contenedor_tabla, 1, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame_2, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.contenedor, 0, 0, 1, 1)


        self.retranslateUi(Control_Productos)

        QMetaObject.connectSlotsByName(Control_Productos)
    # setupUi

    def retranslateUi(self, Control_Productos):
        Control_Productos.setWindowTitle(QCoreApplication.translate("Control_Productos", u"Form", None))
        self.etiquetaTitulo_productos.setText(QCoreApplication.translate("Control_Productos", u"ADMINISTRACI\u00d3N DE PRODUCTOS", None))
#if QT_CONFIG(tooltip)
        self.btn_btn_adminProductos_agregar.setToolTip(QCoreApplication.translate("Control_Productos", u"Agregar nuevo producto", None))
#endif // QT_CONFIG(tooltip)
        self.btn_btn_adminProductos_agregar.setText(QCoreApplication.translate("Control_Productos", u"AGREGAR", None))
#if QT_CONFIG(tooltip)
        self.btn_btn_adminProductos_eliminar.setToolTip(QCoreApplication.translate("Control_Productos", u"Eliminar producto", None))
#endif // QT_CONFIG(tooltip)
        self.btn_btn_adminProductos_eliminar.setText(QCoreApplication.translate("Control_Productos", u"ELIMINAR", None))
#if QT_CONFIG(tooltip)
        self.btn_btn_adminProductos_modificar.setToolTip(QCoreApplication.translate("Control_Productos", u"Editar producto", None))
#endif // QT_CONFIG(tooltip)
        self.btn_btn_adminProductos_modificar.setText(QCoreApplication.translate("Control_Productos", u"EDITAR", None))
        self.btn_btn_adminProductos_ExistenciaProducto.setText(QCoreApplication.translate("Control_Productos", u"Existencia", None))
        self.etiqueta_buscar.setText("")
        self.txt_buscar_productoUPC.setPlaceholderText(QCoreApplication.translate("Control_Productos", u"Codigo del producto", None))
        self.txt_buscar.setPlaceholderText(QCoreApplication.translate("Control_Productos", u"Nombre del producto", None))
#if QT_CONFIG(tooltip)
        self.btn_btn_adminProductos_buscar.setToolTip(QCoreApplication.translate("Control_Productos", u"Buscar producto", None))
#endif // QT_CONFIG(tooltip)
        self.btn_btn_adminProductos_buscar.setText(QCoreApplication.translate("Control_Productos", u"Buscar", None))
#if QT_CONFIG(tooltip)
        self.btn_RefrescarTabla.setToolTip(QCoreApplication.translate("Control_Productos", u"Actualizar tabla", None))
#endif // QT_CONFIG(tooltip)
        self.btn_RefrescarTabla.setText("")
    # retranslateUi

