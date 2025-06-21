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
        control_compras.setStyleSheet(u"*{color: #1d1c1c;}\n"
"#Control_empleados{\n"
"background-color: #fffefb;\n"
"}\n"
"[objectName*=\"contenedor\"]{\n"
"background-color: #fffefb;\n"
"border:none;\n"
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
"QTabWidget::pane {\n"
"        border: none;\n"
"        position: absolute;\n"
"        top: 10px;\n"
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
"        border-top-left-radius: 4"
                        "px;\n"
"        border-top-right-radius: 4px;\n"
"        margin-right: 2px;\n"
"		margin-top:10px;\n"
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
"    /* \u00c1rea de las pesta\u00f1as */\n"
"    QTabBar {\n"
"        background: transparent;\n"
"    }\n"
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
"font-wei"
                        "ght:bold;\n"
"text-transform: uppercase;\n"
"color: #1d1c1c;\n"
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
"#cajaOpciones_proveedor{\n"
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
"ma"
                        "rgin-left: 5px;\n"
"margin-right: 5px;\n"
"text-align: center;\n"
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
"background: #E3E3E3;\n"
"border:none;\n"
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
""
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
"/*-----------FECHA--------------*/\n"
"[objectName*=\"fecha_\"]{\n"
"border: none;\n"
"border-bottom: 1px solid #3b3c3d;\n"
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
"border-bottom: 2px solid"
                        " #00668c;\n"
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
"    padding: 5px;\n"
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
"QCalendarWidget QAbstractI"
                        "temView:disabled {\n"
"    color: #AAAAAA;\n"
"}\n"
"\n"
"/* EFECTO HOVER SOBRE D\u00cdAS */\n"
"QCalendarWidget QAbstractItemView::item:hover {\n"
"    background-color: #e1f0f7;\n"
"    color: #1d1c1c;\n"
"}\n"
"/*----------CAJA OPCIONES---------------*/\n"
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
""
                        "    subcontrol-position: top right ;\n"
"    padding-right: 5px ;\n"
"    width: 20% ;\n"
"    border-left-width: 1px ;\n"
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
"")
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
        self.contenedor_principal.setFrameShape(QFrame.Shape.StyledPanel)
        self.contenedor_principal.setFrameShadow(QFrame.Shadow.Raised)
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
        self.contenedor_widget = QWidget(self.contenedortab_comprasrealizadas)
        self.contenedor_widget.setObjectName(u"contenedor_widget")
        self.contenedor_widget.setMinimumSize(QSize(0, 0))
        self.contenedor_widget.setMaximumSize(QSize(16777215, 16777215))
        self.gridLayout_2 = QGridLayout(self.contenedor_widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetMinAndMaxSize)
        self.contenedor_contenido = QFrame(self.contenedor_widget)
        self.contenedor_contenido.setObjectName(u"contenedor_contenido")
        self.contenedor_contenido.setFrameShape(QFrame.Shape.StyledPanel)
        self.contenedor_contenido.setFrameShadow(QFrame.Shadow.Raised)
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
        self.fecha_fechacompra.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.fecha_fechacompra.setCalendarPopup(True)

        self.gridLayout_4.addWidget(self.fecha_fechacompra, 6, 0, 1, 2)

        self.fecha_levantamientocompra = QDateEdit(self.contenedor_contenido)
        self.fecha_levantamientocompra.setObjectName(u"fecha_levantamientocompra")
        self.fecha_levantamientocompra.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.fecha_levantamientocompra.setCalendarPopup(True)

        self.gridLayout_4.addWidget(self.fecha_levantamientocompra, 6, 2, 1, 1)

        self.etiqueta_fechacompra = QLabel(self.contenedor_contenido)
        self.etiqueta_fechacompra.setObjectName(u"etiqueta_fechacompra")

        self.gridLayout_4.addWidget(self.etiqueta_fechacompra, 4, 0, 1, 2)

        self.cajaOpciones_proveedor = QComboBox(self.contenedor_contenido)
        self.cajaOpciones_proveedor.setObjectName(u"cajaOpciones_proveedor")
        self.cajaOpciones_proveedor.setSizeAdjustPolicy(QComboBox.SizeAdjustPolicy.AdjustToContents)

        self.gridLayout_4.addWidget(self.cajaOpciones_proveedor, 6, 3, 1, 1)

        self.btn_btn_buscar = QToolButton(self.contenedor_contenido)
        self.btn_btn_buscar.setObjectName(u"btn_btn_buscar")
        self.btn_btn_buscar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/iconosBlancos/Icons/iconos/Blanco/buscar_filas_blanco.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_btn_buscar.setIcon(icon)
        self.btn_btn_buscar.setIconSize(QSize(25, 25))
        self.btn_btn_buscar.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

        self.gridLayout_4.addWidget(self.btn_btn_buscar, 3, 10, 1, 1)


        self.gridLayout_2.addWidget(self.contenedor_contenido, 0, 0, 1, 1)

        self.tabla_comprasrealizadas = QTableView(self.contenedor_widget)
        self.tabla_comprasrealizadas.setObjectName(u"tabla_comprasrealizadas")

        self.gridLayout_2.addWidget(self.tabla_comprasrealizadas, 1, 0, 1, 1)


        self.gridLayout_5.addWidget(self.contenedor_widget, 0, 0, 1, 1)

        icon1 = QIcon()
        icon1.addFile(u":/Icons/Bootstrap/check-square.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.contenedortabglobal.addTab(self.contenedortab_comprasrealizadas, icon1, "")
        self.contenedortab_compraspendientes = QWidget()
        self.contenedortab_compraspendientes.setObjectName(u"contenedortab_compraspendientes")
        self.gridLayout_9 = QGridLayout(self.contenedortab_compraspendientes)
        self.gridLayout_9.setSpacing(0)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.contenedor_widget_2 = QWidget(self.contenedortab_compraspendientes)
        self.contenedor_widget_2.setObjectName(u"contenedor_widget_2")
        self.contenedor_widget_2.setMinimumSize(QSize(0, 0))
        self.contenedor_widget_2.setMaximumSize(QSize(16777215, 16777215))
        self.gridLayout_7 = QGridLayout(self.contenedor_widget_2)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setSizeConstraint(QLayout.SizeConstraint.SetMinAndMaxSize)
        self.contenedor_contenidocompras_pendientes = QFrame(self.contenedor_widget_2)
        self.contenedor_contenidocompras_pendientes.setObjectName(u"contenedor_contenidocompras_pendientes")
        self.contenedor_contenidocompras_pendientes.setFrameShape(QFrame.Shape.StyledPanel)
        self.contenedor_contenidocompras_pendientes.setFrameShadow(QFrame.Shadow.Raised)
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
        self.fecha_fechacompra_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.fecha_fechacompra_2.setCalendarPopup(True)

        self.gridLayout_8.addWidget(self.fecha_fechacompra_2, 5, 0, 1, 1)

        self.cajaOpciones_proveedor_2 = QComboBox(self.contenedor_contenidocompras_pendientes)
        self.cajaOpciones_proveedor_2.setObjectName(u"cajaOpciones_proveedor_2")
        self.cajaOpciones_proveedor_2.setSizeAdjustPolicy(QComboBox.SizeAdjustPolicy.AdjustToContents)

        self.gridLayout_8.addWidget(self.cajaOpciones_proveedor_2, 5, 2, 1, 1)

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
        self.btn_btn_buscar_2.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

        self.gridLayout_8.addWidget(self.btn_btn_buscar_2, 3, 9, 1, 1)

        self.etiqueta_levantamientocompra = QLabel(self.contenedor_contenidocompras_pendientes)
        self.etiqueta_levantamientocompra.setObjectName(u"etiqueta_levantamientocompra")

        self.gridLayout_8.addWidget(self.etiqueta_levantamientocompra, 4, 0, 1, 1)

        self.etiqueta_proveedor = QLabel(self.contenedor_contenidocompras_pendientes)
        self.etiqueta_proveedor.setObjectName(u"etiqueta_proveedor")

        self.gridLayout_8.addWidget(self.etiqueta_proveedor, 4, 2, 1, 1)


        self.gridLayout_7.addWidget(self.contenedor_contenidocompras_pendientes, 0, 0, 1, 1)

        self.tabla_compraspendientes = QTableView(self.contenedor_widget_2)
        self.tabla_compraspendientes.setObjectName(u"tabla_compraspendientes")

        self.gridLayout_7.addWidget(self.tabla_compraspendientes, 1, 0, 1, 1)


        self.gridLayout_9.addWidget(self.contenedor_widget_2, 0, 0, 1, 1)

        icon2 = QIcon()
        icon2.addFile(u":/Icons/Bootstrap/pause-circle.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.contenedortabglobal.addTab(self.contenedortab_compraspendientes, icon2, "")

        self.gridLayout_6.addWidget(self.contenedortabglobal, 1, 0, 1, 2)

        self.contenedor_panel_controles = QFrame(self.contenedor_principal)
        self.contenedor_panel_controles.setObjectName(u"contenedor_panel_controles")
        self.contenedor_panel_controles.setMinimumSize(QSize(0, 0))
        self.contenedor_panel_controles.setMaximumSize(QSize(16777215, 150))
        self.contenedor_panel_controles.setFrameShape(QFrame.Shape.StyledPanel)
        self.contenedor_panel_controles.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_3 = QGridLayout(self.contenedor_panel_controles)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 10, 0, 0)
        self.contenedor_frame_2 = QFrame(self.contenedor_panel_controles)
        self.contenedor_frame_2.setObjectName(u"contenedor_frame_2")
        self.contenedor_frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.contenedor_frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.contenedor_frame_2)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 5, 5, 5)
        self.btn_btn_agregar = QToolButton(self.contenedor_frame_2)
        self.btn_btn_agregar.setObjectName(u"btn_btn_agregar")
        self.btn_btn_agregar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/iconosBlancos/Icons/iconos/Blanco/agregar_documento_blanco.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_btn_agregar.setIcon(icon3)
        self.btn_btn_agregar.setIconSize(QSize(24, 24))
        self.btn_btn_agregar.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

        self.horizontalLayout_2.addWidget(self.btn_btn_agregar)

        self.btn_btn_eliminar = QToolButton(self.contenedor_frame_2)
        self.btn_btn_eliminar.setObjectName(u"btn_btn_eliminar")
        self.btn_btn_eliminar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/iconosBlancos/Icons/iconos/Blanco/eliminar_blanco.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_btn_eliminar.setIcon(icon4)
        self.btn_btn_eliminar.setIconSize(QSize(24, 24))
        self.btn_btn_eliminar.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

        self.horizontalLayout_2.addWidget(self.btn_btn_eliminar)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.btn_RefrescarTabla = QPushButton(self.contenedor_frame_2)
        self.btn_RefrescarTabla.setObjectName(u"btn_RefrescarTabla")
        self.btn_RefrescarTabla.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u":/Icons/IconosSVG/base_datos_refresh.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_RefrescarTabla.setIcon(icon5)

        self.horizontalLayout_2.addWidget(self.btn_RefrescarTabla)


        self.gridLayout_3.addWidget(self.contenedor_frame_2, 0, 0, 1, 1, Qt.AlignmentFlag.AlignTop)


        self.gridLayout_6.addWidget(self.contenedor_panel_controles, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.contenedor_principal, 1, 0, 1, 1)


        self.retranslateUi(control_compras)

        self.contenedortabglobal.setCurrentIndex(1)


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

