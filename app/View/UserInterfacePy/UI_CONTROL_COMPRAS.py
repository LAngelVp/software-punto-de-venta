# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UI_CONTROL_COMPRAS.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLayout, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QTabWidget, QTableView, QToolButton,
    QWidget)
from ...Source import ibootstrap_rc
from ...Source import iconosSVG_rc
from ...Source import iconsdvg_rc

class Ui_control_compras(object):
    def setupUi(self, control_compras):
        if not control_compras.objectName():
            control_compras.setObjectName(u"control_compras")
        control_compras.resize(1148, 610)
        control_compras.setStyleSheet(u"#Control_empleados{\n"
"background-color: #fffefb;\n"
"}\n"
"[objectName*=\"contenedor\"]{\n"
"background-color: #fffefb;\n"
"}\n"
"#panel_controles{\n"
"margin-bottom:20px;\n"
"}\n"
"#label_wc_titulo_compras{\n"
"color:#1d1c1c;\n"
"background-color: #fffefb;\n"
"font-size: 24px;\n"
"font-weight: bold;\n"
"padding-left: 5px;\n"
"text-transform: uppercase;\n"
"font-family: \"Arial\";\n"
"padding-top: 5px;\n"
"}\n"
"#tabla_listaempleados {\n"
"    border: 1px solid;\n"
"    background: #fffefb;\n"
"	max-height: 600px;\n"
"	font-family:  'Times New Roman';\n"
"}\n"
"#contenedortabglobal{\n"
"background-color: #fffefb;\n"
"}\n"
"#contenedortab_comprasrealizadas{\n"
"background-color: #fffefb;\n"
"border: 1px solid;\n"
"}\n"
"#contenedortab_compraspendientes{\n"
"background-color: #fffefb;\n"
"border: 1px solid;\n"
"}\n"
"[objectName*=\"etiquetaTitulo\"]{\n"
"font-family: Arial;\n"
"margin-left: 5px;\n"
"margin-right: 5px;\n"
"font-size: 16px;\n"
"font-weight:bold;\n"
"text-transform: uppercase;\n"
"color: #1d1c1c;"
                        "\n"
"}\n"
"*[objectName*=\"etiqueta_\"]{\n"
"font-family: Arial;\n"
"margin-left: 5px;\n"
"margin-right: 5px;\n"
"font-size: 14px;\n"
"font-weight:bold;\n"
"text-transform: capitalize;\n"
"color: #1d1c1c;\n"
"}\n"
"*[objectName*=\"txt_\"]{\n"
"background-color: #F5F5F5;\n"
"color: #1d1c1c;\n"
"border: none;\n"
"border-bottom: 1px solid;\n"
"border-radius: 5px;\n"
"font-size: 16px;\n"
"font-family: Arial;\n"
"height: 20px;\n"
"}\n"
"#txt_proveedor{\n"
"width: 350px;\n"
"font-family: Arial;\n"
"color: #1d1c1c\n"
"}\n"
"#cajaopciones_proveedor{\n"
"width: 250px;\n"
"max-width: 250px;\n"
"font-family: Arial;\n"
"background-color: #F5F5F5;\n"
"color: #1d1c1c;\n"
"}\n"
"*[objectName^=\"txt_\"]::focus{\n"
"border-bottom: 2px solid #00668c;\n"
"}\n"
"*[objectName*=\"btn_btn\"]{\n"
"border:none;\n"
"border-radius: 5px;\n"
"background-color: #00619a;\n"
"color: #fffefb;\n"
"font-family: Arial;\n"
"font-size: 16px;\n"
"font-weight: bold;\n"
"height: 25px;\n"
"margin-left: 5px;\n"
"margin-right: 5px;\n"
"text-align: cente"
                        "r;\n"
"text-transform: uppercase;\n"
"}\n"
"#btn_btn_eliminar:hover{\n"
"background-color: #EE1D52;\n"
"}\n"
"#btn_btn_agregar:hover{\n"
"background-color: #68a67d;\n"
"}\n"
"*[objectName*=\"btn_btn\"]:hover{\n"
"background-color: #4d648d;\n"
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
"/*-----------TABLA--------------*/\n"
"\n"
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
"    colo"
                        "r: white;\n"
"}\n"
"\n"
"/* Encabezado vertical */\n"
"[objectName*=\"tabla_\"] QHeaderView::vertical {\n"
"    background-color: #023375;\n"
"    color: white;\n"
"}\n"
"\n"
"/*-----------FECHA--------------*/\n"
"[objectName^=\"fecha_\"]{\n"
"border: none;\n"
"border-bottom: 1px solid #3b3c3d;\n"
"border-radius: 5px;\n"
"padding: 2px;\n"
"background-color: #f5f4f1;\n"
"font-size: 14px;\n"
"width:150px;\n"
"max-width:150px;\n"
"font-family: Arial;\n"
"color: #1d1c1c;\n"
"\n"
"}\n"
"*[objectName^=\"fecha_\"]::drop-down{\n"
"subcontrol-origin: padding;\n"
"subcontrol-position: top right;\n"
"padding-right:5px;\n"
"width: 20%;\n"
"border-left-width: 1px;\n"
"border-radius: 5px;\n"
"background-color: #F5F5F5;\n"
"}\n"
"*[objectName^=\"fecha_\"]::down-arrow{\n"
"image: url(:/Icons/Bootstrap/calendar2-date.svg);\n"
"padding-left:5px;\n"
"padding-right:5px;\n"
"}\n"
"*[objectName^=\"fecha_\"]::focus{\n"
"border-bottom: 2px solid #00668c;\n"
"}\n"
"/*----------CAJA OPCIONES---------------*/\n"
"[objectName^=\"cajaopc"
                        "iones_\"]{\n"
"border: none;\n"
"border-bottom: 1px solid rgb(29, 28, 28);\n"
"border-radius: 5px;\n"
"padding: 2px;\n"
"background-color: #F5F5F5;\n"
"border-radius: 5px;\n"
"font-size: 12px;\n"
"width:87px;\n"
"color: #1d1c1c;\n"
"}\n"
"[objectName^=\"cajaopciones_\"]::drop-down{\n"
"subcontrol-origin: padding;\n"
"subcontrol-position: top right;\n"
"padding-right:5px;\n"
"border-left-width: 1px;\n"
"border-radius: 5px;\n"
"background-color:#F5F5F5;\n"
"}\n"
"[objectName^=\"cajaopciones_\"]::down-arrow{\n"
"image: url(:/Icons/Bootstrap/filter-left.svg);\n"
"padding-left:5px;\n"
"padding-right:5px;\n"
"}")
        self.gridLayout = QGridLayout(control_compras)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_wc_titulo_compras = QLabel(control_compras)
        self.label_wc_titulo_compras.setObjectName(u"label_wc_titulo_compras")
        self.label_wc_titulo_compras.setMinimumSize(QSize(0, 40))
        self.label_wc_titulo_compras.setMaximumSize(QSize(16777215, 40))

        self.gridLayout.addWidget(self.label_wc_titulo_compras, 0, 0, 1, 1)

        self.contenedor_principal = QFrame(control_compras)
        self.contenedor_principal.setObjectName(u"contenedor_principal")
        self.contenedor_principal.setFrameShape(QFrame.StyledPanel)
        self.contenedor_principal.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.contenedor_principal)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(5, 0, 5, 5)
        self.contenedortabglobal = QTabWidget(self.contenedor_principal)
        self.contenedortabglobal.setObjectName(u"contenedortabglobal")
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(14)
        font.setBold(True)
        self.contenedortabglobal.setFont(font)
        self.contenedortabglobal.setStyleSheet(u"")
        self.contenedortabglobal.setIconSize(QSize(14, 14))
        self.contenedortab_comprasrealizadas = QWidget()
        self.contenedortab_comprasrealizadas.setObjectName(u"contenedortab_comprasrealizadas")
        self.gridLayout_5 = QGridLayout(self.contenedortab_comprasrealizadas)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.contenedortab_comprasrealizadas)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 0))
        self.widget.setMaximumSize(QSize(16777215, 16777215))
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.contenedor_contenido = QFrame(self.widget)
        self.contenedor_contenido.setObjectName(u"contenedor_contenido")
        self.contenedor_contenido.setFrameShape(QFrame.StyledPanel)
        self.contenedor_contenido.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.contenedor_contenido)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setHorizontalSpacing(10)
        self.gridLayout_4.setVerticalSpacing(5)
        self.gridLayout_4.setContentsMargins(5, 10, 5, 0)
        self.txt_proveedor = QLineEdit(self.contenedor_contenido)
        self.txt_proveedor.setObjectName(u"txt_proveedor")

        self.gridLayout_4.addWidget(self.txt_proveedor, 3, 3, 1, 1)

        self.etiqueta_fechalevantamientocompra = QLabel(self.contenedor_contenido)
        self.etiqueta_fechalevantamientocompra.setObjectName(u"etiqueta_fechalevantamientocompra")

        self.gridLayout_4.addWidget(self.etiqueta_fechalevantamientocompra, 4, 2, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(282, 25, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_2, 3, 9, 1, 1)

        self.etiquetaTitulo_buscar = QLabel(self.contenedor_contenido)
        self.etiquetaTitulo_buscar.setObjectName(u"etiquetaTitulo_buscar")

        self.gridLayout_4.addWidget(self.etiquetaTitulo_buscar, 0, 0, 1, 2)

        self.etiqueta_proveedor_2 = QLabel(self.contenedor_contenido)
        self.etiqueta_proveedor_2.setObjectName(u"etiqueta_proveedor_2")

        self.gridLayout_4.addWidget(self.etiqueta_proveedor_2, 4, 3, 1, 1)

        self.txt_idcompra = QLineEdit(self.contenedor_contenido)
        self.txt_idcompra.setObjectName(u"txt_idcompra")

        self.gridLayout_4.addWidget(self.txt_idcompra, 3, 0, 1, 3)

        self.fecha_fechacompra = QDateEdit(self.contenedor_contenido)
        self.fecha_fechacompra.setObjectName(u"fecha_fechacompra")
        self.fecha_fechacompra.setAlignment(Qt.AlignCenter)
        self.fecha_fechacompra.setCalendarPopup(True)

        self.gridLayout_4.addWidget(self.fecha_fechacompra, 6, 0, 1, 2)

        self.fecha_levantamientocompra = QDateEdit(self.contenedor_contenido)
        self.fecha_levantamientocompra.setObjectName(u"fecha_levantamientocompra")
        self.fecha_levantamientocompra.setAlignment(Qt.AlignCenter)
        self.fecha_levantamientocompra.setCalendarPopup(True)

        self.gridLayout_4.addWidget(self.fecha_levantamientocompra, 6, 2, 1, 1)

        self.etiqueta_fechacompra = QLabel(self.contenedor_contenido)
        self.etiqueta_fechacompra.setObjectName(u"etiqueta_fechacompra")

        self.gridLayout_4.addWidget(self.etiqueta_fechacompra, 4, 0, 1, 2)

        self.cajaopciones_proveedor = QComboBox(self.contenedor_contenido)
        self.cajaopciones_proveedor.setObjectName(u"cajaopciones_proveedor")
        self.cajaopciones_proveedor.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.gridLayout_4.addWidget(self.cajaopciones_proveedor, 6, 3, 1, 1)

        self.btn_btn_buscar = QToolButton(self.contenedor_contenido)
        self.btn_btn_buscar.setObjectName(u"btn_btn_buscar")
        self.btn_btn_buscar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/iconosBlancos/Icons/iconos/Blanco/buscar_filas_blanco.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_btn_buscar.setIcon(icon)
        self.btn_btn_buscar.setIconSize(QSize(25, 25))
        self.btn_btn_buscar.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.gridLayout_4.addWidget(self.btn_btn_buscar, 3, 10, 1, 1)


        self.gridLayout_2.addWidget(self.contenedor_contenido, 0, 0, 1, 1)

        self.tabla_comprasrealizadas = QTableView(self.widget)
        self.tabla_comprasrealizadas.setObjectName(u"tabla_comprasrealizadas")

        self.gridLayout_2.addWidget(self.tabla_comprasrealizadas, 1, 0, 1, 1)


        self.gridLayout_5.addWidget(self.widget, 0, 0, 1, 1)

        icon1 = QIcon()
        icon1.addFile(u":/Icons/Bootstrap/check-square.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.contenedortabglobal.addTab(self.contenedortab_comprasrealizadas, icon1, "")
        self.contenedortab_compraspendientes = QWidget()
        self.contenedortab_compraspendientes.setObjectName(u"contenedortab_compraspendientes")
        self.gridLayout_9 = QGridLayout(self.contenedortab_compraspendientes)
        self.gridLayout_9.setSpacing(0)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.contenedortab_compraspendientes)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(0, 0))
        self.widget_2.setMaximumSize(QSize(16777215, 16777215))
        self.gridLayout_7 = QGridLayout(self.widget_2)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.contenedor_contenidocompras_pendientes = QFrame(self.widget_2)
        self.contenedor_contenidocompras_pendientes.setObjectName(u"contenedor_contenidocompras_pendientes")
        self.contenedor_contenidocompras_pendientes.setFrameShape(QFrame.StyledPanel)
        self.contenedor_contenidocompras_pendientes.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.contenedor_contenidocompras_pendientes)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setHorizontalSpacing(10)
        self.gridLayout_8.setVerticalSpacing(5)
        self.gridLayout_8.setContentsMargins(5, 10, 5, 0)
        self.txt_idcompra_2 = QLineEdit(self.contenedor_contenidocompras_pendientes)
        self.txt_idcompra_2.setObjectName(u"txt_idcompra_2")

        self.gridLayout_8.addWidget(self.txt_idcompra_2, 3, 0, 1, 2)

        self.txt_proveedor_2 = QLineEdit(self.contenedor_contenidocompras_pendientes)
        self.txt_proveedor_2.setObjectName(u"txt_proveedor_2")

        self.gridLayout_8.addWidget(self.txt_proveedor_2, 3, 2, 1, 1)

        self.fecha_fechacompra_2 = QDateEdit(self.contenedor_contenidocompras_pendientes)
        self.fecha_fechacompra_2.setObjectName(u"fecha_fechacompra_2")
        self.fecha_fechacompra_2.setAlignment(Qt.AlignCenter)
        self.fecha_fechacompra_2.setCalendarPopup(True)

        self.gridLayout_8.addWidget(self.fecha_fechacompra_2, 5, 0, 1, 1)

        self.cajaopciones_proveedor_2 = QComboBox(self.contenedor_contenidocompras_pendientes)
        self.cajaopciones_proveedor_2.setObjectName(u"cajaopciones_proveedor_2")
        self.cajaopciones_proveedor_2.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.gridLayout_8.addWidget(self.cajaopciones_proveedor_2, 5, 2, 1, 1)

        self.etiquetaTitulo_buscar_2 = QLabel(self.contenedor_contenidocompras_pendientes)
        self.etiquetaTitulo_buscar_2.setObjectName(u"etiquetaTitulo_buscar_2")

        self.gridLayout_8.addWidget(self.etiquetaTitulo_buscar_2, 0, 0, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_3, 3, 8, 1, 1)

        self.btn_btn_buscar_2 = QToolButton(self.contenedor_contenidocompras_pendientes)
        self.btn_btn_buscar_2.setObjectName(u"btn_btn_buscar_2")
        self.btn_btn_buscar_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_btn_buscar_2.setIcon(icon)
        self.btn_btn_buscar_2.setIconSize(QSize(24, 24))
        self.btn_btn_buscar_2.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.gridLayout_8.addWidget(self.btn_btn_buscar_2, 3, 9, 1, 1)

        self.etiqueta_levantamientocompra = QLabel(self.contenedor_contenidocompras_pendientes)
        self.etiqueta_levantamientocompra.setObjectName(u"etiqueta_levantamientocompra")

        self.gridLayout_8.addWidget(self.etiqueta_levantamientocompra, 4, 0, 1, 1)

        self.etiqueta_proveedor = QLabel(self.contenedor_contenidocompras_pendientes)
        self.etiqueta_proveedor.setObjectName(u"etiqueta_proveedor")

        self.gridLayout_8.addWidget(self.etiqueta_proveedor, 4, 2, 1, 1)


        self.gridLayout_7.addWidget(self.contenedor_contenidocompras_pendientes, 0, 0, 1, 1)

        self.tabla_compraspendientes = QTableView(self.widget_2)
        self.tabla_compraspendientes.setObjectName(u"tabla_compraspendientes")

        self.gridLayout_7.addWidget(self.tabla_compraspendientes, 1, 0, 1, 1)


        self.gridLayout_9.addWidget(self.widget_2, 0, 0, 1, 1)

        icon2 = QIcon()
        icon2.addFile(u":/Icons/Bootstrap/pause-circle.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.contenedortabglobal.addTab(self.contenedortab_compraspendientes, icon2, "")

        self.gridLayout_6.addWidget(self.contenedortabglobal, 1, 0, 1, 2)

        self.panel_controles = QFrame(self.contenedor_principal)
        self.panel_controles.setObjectName(u"panel_controles")
        self.panel_controles.setMinimumSize(QSize(0, 0))
        self.panel_controles.setMaximumSize(QSize(16777215, 150))
        self.panel_controles.setFrameShape(QFrame.StyledPanel)
        self.panel_controles.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.panel_controles)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 10, 0, 0)
        self.frame_2 = QFrame(self.panel_controles)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 5, 5, 5)
        self.btn_btn_agregar = QToolButton(self.frame_2)
        self.btn_btn_agregar.setObjectName(u"btn_btn_agregar")
        self.btn_btn_agregar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/iconosBlancos/Icons/iconos/Blanco/agregar_documento_blanco.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_btn_agregar.setIcon(icon3)
        self.btn_btn_agregar.setIconSize(QSize(24, 24))
        self.btn_btn_agregar.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.horizontalLayout_2.addWidget(self.btn_btn_agregar)

        self.btn_btn_eliminar = QToolButton(self.frame_2)
        self.btn_btn_eliminar.setObjectName(u"btn_btn_eliminar")
        self.btn_btn_eliminar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/iconosBlancos/Icons/iconos/Blanco/eliminar_blanco.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_btn_eliminar.setIcon(icon4)
        self.btn_btn_eliminar.setIconSize(QSize(24, 24))
        self.btn_btn_eliminar.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.horizontalLayout_2.addWidget(self.btn_btn_eliminar)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.btn_RefrescarTabla = QPushButton(self.frame_2)
        self.btn_RefrescarTabla.setObjectName(u"btn_RefrescarTabla")
        self.btn_RefrescarTabla.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u":/Icons/IconosSVG/base_datos_refresh.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_RefrescarTabla.setIcon(icon5)

        self.horizontalLayout_2.addWidget(self.btn_RefrescarTabla)


        self.gridLayout_3.addWidget(self.frame_2, 0, 0, 1, 1, Qt.AlignTop)


        self.gridLayout_6.addWidget(self.panel_controles, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.contenedor_principal, 1, 0, 1, 1)


        self.retranslateUi(control_compras)

        self.contenedortabglobal.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(control_compras)
    # setupUi

    def retranslateUi(self, control_compras):
        control_compras.setWindowTitle(QCoreApplication.translate("control_compras", u"Form", None))
        self.label_wc_titulo_compras.setText(QCoreApplication.translate("control_compras", u"administraci\u00f3n de compras", None))
        self.txt_proveedor.setPlaceholderText(QCoreApplication.translate("control_compras", u"Quien realizo la compra", None))
        self.etiqueta_fechalevantamientocompra.setText(QCoreApplication.translate("control_compras", u"Fecha documento", None))
        self.etiquetaTitulo_buscar.setText(QCoreApplication.translate("control_compras", u"Buscar por:", None))
        self.etiqueta_proveedor_2.setText(QCoreApplication.translate("control_compras", u"Proveedor", None))
        self.txt_idcompra.setPlaceholderText(QCoreApplication.translate("control_compras", u"folio de la compra", None))
        self.etiqueta_fechacompra.setText(QCoreApplication.translate("control_compras", u"Fecha de compra", None))
        self.btn_btn_buscar.setText(QCoreApplication.translate("control_compras", u"Buscar", None))
        self.contenedortabglobal.setTabText(self.contenedortabglobal.indexOf(self.contenedortab_comprasrealizadas), QCoreApplication.translate("control_compras", u"Realizadas", None))
        self.txt_idcompra_2.setPlaceholderText(QCoreApplication.translate("control_compras", u"folio de la compra", None))
        self.txt_proveedor_2.setPlaceholderText(QCoreApplication.translate("control_compras", u"Quien realizo la compra", None))
        self.etiquetaTitulo_buscar_2.setText(QCoreApplication.translate("control_compras", u"Buscar por:", None))
        self.btn_btn_buscar_2.setText(QCoreApplication.translate("control_compras", u"Buscar", None))
        self.etiqueta_levantamientocompra.setText(QCoreApplication.translate("control_compras", u"Fecha documento", None))
        self.etiqueta_proveedor.setText(QCoreApplication.translate("control_compras", u"Proveedor", None))
        self.contenedortabglobal.setTabText(self.contenedortabglobal.indexOf(self.contenedortab_compraspendientes), QCoreApplication.translate("control_compras", u"Pendientes", None))
        self.btn_btn_agregar.setText(QCoreApplication.translate("control_compras", u"Agregar", None))
        self.btn_btn_eliminar.setText(QCoreApplication.translate("control_compras", u"Eliminar", None))
#if QT_CONFIG(tooltip)
        self.btn_RefrescarTabla.setToolTip(QCoreApplication.translate("control_compras", u"Actualizar tabla", None))
#endif // QT_CONFIG(tooltip)
        self.btn_RefrescarTabla.setText("")
    # retranslateUi

