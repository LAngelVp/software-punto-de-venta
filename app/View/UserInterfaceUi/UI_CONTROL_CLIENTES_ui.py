# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UI_CONTROL_CLIENTES.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractSpinBox, QApplication, QCheckBox,
    QComboBox, QDateEdit, QDoubleSpinBox, QFormLayout,
    QFrame, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QLayout, QLineEdit, QPlainTextEdit,
    QPushButton, QRadioButton, QScrollArea, QSizePolicy,
    QSpacerItem, QStackedWidget, QTableView, QWidget)
import ibootstrap_rc
import iconsdvg_rc
import iconosSVG_rc

class Ui_Control_Clientes(object):
    def setupUi(self, Control_Clientes):
        if not Control_Clientes.objectName():
            Control_Clientes.setObjectName(u"Control_Clientes")
        Control_Clientes.resize(1400, 590)
        Control_Clientes.setStyleSheet(u"*{color: #1d1c1c;}\n"
"#Control_Clientes{\n"
"background: #fffefb;\n"
"}\n"
"[objectName*=\"wpc\"]{\n"
"background-color: #fffefb;\n"
"border: none;\n"
"}\n"
"[objectName*=\"contenedor\"]{\n"
"background-color: #fffefb;\n"
"border: none;\n"
"}\n"
"#label_wp_titulo_clientes{\n"
"color:#1d1c1c;\n"
"background-color: #fffefb;\n"
"font-size: 24px;\n"
"font-weight: bold;\n"
"padding-left: 5px;\n"
"text-transform: uppercase;\n"
"font-family: \"Arial\";\n"
"padding-top: 5px;\n"
"}\n"
"#label_wpc_fotocliente{\n"
"min-height: 50px;\n"
"max-height:50px;\n"
"min-width: 50px;\n"
"max-width:50px;\n"
"}\n"
"\n"
"#contenedor_izquierda{\n"
"max-width: 450px;\n"
"}\n"
"\n"
"#wpc_menu_opciones_clientes{\n"
"min-height: 40px;\n"
"}\n"
"#wpc_lista_clientes{\n"
"background-color: #fffefb;\n"
"}\n"
"#wpc_buscar_clientes{\n"
"min-width:300px;\n"
"}\n"
"#etiqueta_iconobuscar{\n"
"image: url(:/iconosAzules/Icons/iconos/Azul/buscar_persona_azul.svg);\n"
"min-width:35px;\n"
"min-height:25px;\n"
"}\n"
"[objectName^=\"btn_btn_\"]{\n"
"bac"
                        "kground-color: #00619a;\n"
"border-radius: 3px;\n"
"color: #fffefb;\n"
"font-weight: bold;\n"
"font-family: Arial;\n"
"font-size: 16px;\n"
"}\n"
"[objectName*=\"btn_btn_\"]:hover{\n"
"background-color: #2196F3;\n"
"}\n"
"#btn_btn_cliente_agregar:hover{\n"
"	background: #68a67d;\n"
"}\n"
"#btn_btn_cliente_eliminar:hover{\n"
"	background: #EE1D52;\n"
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
"[objectName*=\"etiqueta_\"]{\n"
"font-family:Arial;\n"
"font-size: 14px;\n"
"font-weight:bold;\n"
"}\n"
"[objectName*=\"btnRadio_wpc\"]{\n"
"font-family:Arial;\n"
"font-size: 14px;\n"
"font-weight: bold;\n"
"}\n"
"/*  ESTILOS DE LAS CAJAS DE TEXTO */\n"
"[objectName*=\"txt_\"]{\n"
"font-family:Arial;\n"
"font-size: 15px;\n"
"border: none;\n"
"border-bottom: 1px solid rgb(0, 0, 0);\n"
"background: #F5F5F5;\n"
"border-radius: 2px"
                        ";\n"
"color: #1d1c1c;\n"
"min-width: 200px;\n"
"}\n"
"[objectName*=\"txt_\"]::focus{\n"
"border-bottom: 2px solid #00668c;\n"
"}\n"
"[objectName*=\"txtlargo_\"]{\n"
"font-family:Arial;\n"
"font-size: 15px;\n"
"border: none;\n"
"border-bottom: 1px solid rgb(0, 0, 0);\n"
"background: #F5F5F5;\n"
"border-radius: 2px;\n"
"color: #1d1c1c;\n"
"max-height: 100px;\n"
"}\n"
"[objectName*=\"txtlargo_\"]::focus{\n"
"border-bottom: 2px solid #00668c;\n"
"}\n"
"\n"
"/*  ESTILOS DE LAS CAJAS DE NUMERO  */\n"
"\n"
"[objectName*=\"cajaDecimal\"]{\n"
"font-family:Arial;\n"
"color: #1d1c1c;\n"
"font-size: 15px;\n"
"border: none;\n"
"border-bottom: 1px solid rgb(0, 0, 0);\n"
"background: #F5F5F5;\n"
"border-radius: 2px;\n"
"}\n"
"[objectName*=\"cajaDecimal_\"]::focus{\n"
"border-bottom: 2px solid #00668c;\n"
"}\n"
"\n"
"[objectName*=\"cajaOpciones\"] {\n"
"    border: none;\n"
"    border-bottom: 1px solid #787878 ;\n"
"    padding: 2px ;\n"
"    background-color: #F5F5F5 ;\n"
"    font-size: 14px ;\n"
"    min-width: 200px ;\n"
""
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
"/*TABLA*/\n"
"\n"
"[objectName*=\"tabla_"
                        "\"] {\n"
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
"[objectName*=\"casillaverificacion_\"]{\n"
"font-family:Arial;\n"
"font-size: 14px;\n"
"color:#1d1c1c;\n"
"font-weight: bold;\n"
"}\n"
"#wpc_clientes_contenedordatos{\n"
"max-width:800px;\n"
"background: #fffefb;\n"
"}\n"
"#label_wpc_fotocliente{\n"
"min-height:200px;\n"
"min-width:200px;\n"
"background: #F5F5F5;\n"
"border: 1px solid rgb(0, 0, 0);\n"
""
                        "}\n"
"#wpc_clientes_autorizacredito{\n"
"background: #fffefb;\n"
"}\n"
"\n"
"#wpc_clientes_autorizacredito_moral{\n"
"background: #fffefb;\n"
"max-width:450px;\n"
"}\n"
"\n"
"\n"
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
"border-bottom: 2px solid #00668c;\n"
"}\n"
"QCalendarWidget QWidget#qt_calendar_navigationbar {\n"
"    background-color: #00668c;\n"
"    color: white;\n"
""
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
"QCalendarWidget QAbstractItemView:disabled {\n"
"    color: #AAAAAA;\n"
"}\n"
"\n"
"/* EFECTO HOVER SOBRE D\u00cdAS */\n"
"QCalendarWidget QAbstractItemView::i"
                        "tem:hover {\n"
"    background-color: #e1f0f7;\n"
"    color: #1d1c1c;\n"
"}")
        self.gridLayout_17 = QGridLayout(Control_Clientes)
        self.gridLayout_17.setSpacing(0)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.gridLayout_17.setContentsMargins(0, 0, 0, 0)
        self.wpc_contenido_general = QWidget(Control_Clientes)
        self.wpc_contenido_general.setObjectName(u"wpc_contenido_general")
        self.wpc_contenido_general.setStyleSheet(u"")
        self.gridLayout_9 = QGridLayout(self.wpc_contenido_general)
        self.gridLayout_9.setSpacing(0)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setSizeConstraint(QLayout.SizeConstraint.SetMaximumSize)
        self.gridLayout_9.setContentsMargins(0, 0, 0, 5)
        self.wpc_clientes_contenido = QWidget(self.wpc_contenido_general)
        self.wpc_clientes_contenido.setObjectName(u"wpc_clientes_contenido")
        self.gridLayout_19 = QGridLayout(self.wpc_clientes_contenido)
        self.gridLayout_19.setSpacing(0)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.gridLayout_19.setContentsMargins(0, 0, 0, -1)
        self.wpc_contenedor_scroll = QScrollArea(self.wpc_clientes_contenido)
        self.wpc_contenedor_scroll.setObjectName(u"wpc_contenedor_scroll")
        self.wpc_contenedor_scroll.setWidgetResizable(True)
        self.wpc_scrooll_area = QWidget()
        self.wpc_scrooll_area.setObjectName(u"wpc_scrooll_area")
        self.wpc_scrooll_area.setGeometry(QRect(0, 0, 1385, 811))
        self.gridLayout_11 = QGridLayout(self.wpc_scrooll_area)
        self.gridLayout_11.setSpacing(0)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
        self.wpc_clientes_datos = QWidget(self.wpc_scrooll_area)
        self.wpc_clientes_datos.setObjectName(u"wpc_clientes_datos")
        self.gridLayout_4 = QGridLayout(self.wpc_clientes_datos)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(5, 10, 5, 0)
        self.wpc_contenedor_pila = QStackedWidget(self.wpc_clientes_datos)
        self.wpc_contenedor_pila.setObjectName(u"wpc_contenedor_pila")
        self.wpc_pagina_clientefisico = QWidget()
        self.wpc_pagina_clientefisico.setObjectName(u"wpc_pagina_clientefisico")
        self.gridLayout_3 = QGridLayout(self.wpc_pagina_clientefisico)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.wpc_contenedor_clientfisico = QWidget(self.wpc_pagina_clientefisico)
        self.wpc_contenedor_clientfisico.setObjectName(u"wpc_contenedor_clientfisico")
        self.wpc_contenedor_clientfisico.setMaximumSize(QSize(16777215, 16777215))
        self.wpc_contenedor_clientfisico.setStyleSheet(u"")
        self.gridLayout_7 = QGridLayout(self.wpc_contenedor_clientfisico)
        self.gridLayout_7.setSpacing(0)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.wpc_clientes_clienteFisico = QWidget(self.wpc_contenedor_clientfisico)
        self.wpc_clientes_clienteFisico.setObjectName(u"wpc_clientes_clienteFisico")
        self.wpc_clientes_clienteFisico.setMinimumSize(QSize(0, 0))
        self.gridLayout_5 = QGridLayout(self.wpc_clientes_clienteFisico)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.etiqueta_ciudad_fisico = QLabel(self.wpc_clientes_clienteFisico)
        self.etiqueta_ciudad_fisico.setObjectName(u"etiqueta_ciudad_fisico")

        self.gridLayout_5.addWidget(self.etiqueta_ciudad_fisico, 5, 2, 1, 1)

        self.txtlargo_direccionadicional_fisico = QPlainTextEdit(self.wpc_clientes_clienteFisico)
        self.txtlargo_direccionadicional_fisico.setObjectName(u"txtlargo_direccionadicional_fisico")

        self.gridLayout_5.addWidget(self.txtlargo_direccionadicional_fisico, 10, 1, 1, 3)

        self.cajaDecimal_wpc_ingresosclienteFisico = QDoubleSpinBox(self.wpc_clientes_clienteFisico)
        self.cajaDecimal_wpc_ingresosclienteFisico.setObjectName(u"cajaDecimal_wpc_ingresosclienteFisico")
        self.cajaDecimal_wpc_ingresosclienteFisico.setMinimumSize(QSize(0, 0))
        self.cajaDecimal_wpc_ingresosclienteFisico.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.cajaDecimal_wpc_ingresosclienteFisico.setMaximum(99999999.989999994635582)

        self.gridLayout_5.addWidget(self.cajaDecimal_wpc_ingresosclienteFisico, 8, 1, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.cajaOpciones_categoriaFisico = QComboBox(self.wpc_clientes_clienteFisico)
        self.cajaOpciones_categoriaFisico.addItem("")
        self.cajaOpciones_categoriaFisico.setObjectName(u"cajaOpciones_categoriaFisico")

        self.horizontalLayout_2.addWidget(self.cajaOpciones_categoriaFisico)

        self.btn_btn_nuevacategoriaFisico = QPushButton(self.wpc_clientes_clienteFisico)
        self.btn_btn_nuevacategoriaFisico.setObjectName(u"btn_btn_nuevacategoriaFisico")
        self.btn_btn_nuevacategoriaFisico.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/iconosBlancos/Icons/iconos/Blanco/agregar_blanco.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_btn_nuevacategoriaFisico.setIcon(icon)
        self.btn_btn_nuevacategoriaFisico.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.btn_btn_nuevacategoriaFisico)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)


        self.gridLayout_5.addLayout(self.horizontalLayout_2, 9, 3, 1, 1)

        self.txt_nombre_fisico = QLineEdit(self.wpc_clientes_clienteFisico)
        self.txt_nombre_fisico.setObjectName(u"txt_nombre_fisico")
        self.txt_nombre_fisico.setMinimumSize(QSize(200, 0))

        self.gridLayout_5.addWidget(self.txt_nombre_fisico, 0, 1, 1, 1)

        self.txt_ine_fisico = QLineEdit(self.wpc_clientes_clienteFisico)
        self.txt_ine_fisico.setObjectName(u"txt_ine_fisico")
        self.txt_ine_fisico.setMinimumSize(QSize(200, 0))

        self.gridLayout_5.addWidget(self.txt_ine_fisico, 7, 3, 1, 1)

        self.txt_codigopostal_fisico = QLineEdit(self.wpc_clientes_clienteFisico)
        self.txt_codigopostal_fisico.setObjectName(u"txt_codigopostal_fisico")

        self.gridLayout_5.addWidget(self.txt_codigopostal_fisico, 6, 3, 1, 1)

        self.txt_rfc_fisico = QLineEdit(self.wpc_clientes_clienteFisico)
        self.txt_rfc_fisico.setObjectName(u"txt_rfc_fisico")

        self.gridLayout_5.addWidget(self.txt_rfc_fisico, 3, 1, 1, 1)

        self.etiqueta_area_negocio_fisico = QLabel(self.wpc_clientes_clienteFisico)
        self.etiqueta_area_negocio_fisico.setObjectName(u"etiqueta_area_negocio_fisico")

        self.gridLayout_5.addWidget(self.etiqueta_area_negocio_fisico, 9, 0, 1, 1)

        self.etiqueta_wpc_comentarios_fisico = QLabel(self.wpc_clientes_clienteFisico)
        self.etiqueta_wpc_comentarios_fisico.setObjectName(u"etiqueta_wpc_comentarios_fisico")
        self.etiqueta_wpc_comentarios_fisico.setMinimumSize(QSize(0, 0))

        self.gridLayout_5.addWidget(self.etiqueta_wpc_comentarios_fisico, 12, 0, 1, 1)

        self.etiqueta_codigopostal_fisico = QLabel(self.wpc_clientes_clienteFisico)
        self.etiqueta_codigopostal_fisico.setObjectName(u"etiqueta_codigopostal_fisico")

        self.gridLayout_5.addWidget(self.etiqueta_codigopostal_fisico, 6, 2, 1, 1)

        self.etiqueta_wpc_calles_fisico = QLabel(self.wpc_clientes_clienteFisico)
        self.etiqueta_wpc_calles_fisico.setObjectName(u"etiqueta_wpc_calles_fisico")
        self.etiqueta_wpc_calles_fisico.setMinimumSize(QSize(0, 0))

        self.gridLayout_5.addWidget(self.etiqueta_wpc_calles_fisico, 3, 2, 1, 1)

        self.etiqueta_wpc_curp_fisico = QLabel(self.wpc_clientes_clienteFisico)
        self.etiqueta_wpc_curp_fisico.setObjectName(u"etiqueta_wpc_curp_fisico")
        self.etiqueta_wpc_curp_fisico.setMinimumSize(QSize(0, 0))

        self.gridLayout_5.addWidget(self.etiqueta_wpc_curp_fisico, 6, 0, 1, 1)

        self.fecha_fechanacimiento = QDateEdit(self.wpc_clientes_clienteFisico)
        self.fecha_fechanacimiento.setObjectName(u"fecha_fechanacimiento")
        self.fecha_fechanacimiento.setCalendarPopup(True)

        self.gridLayout_5.addWidget(self.fecha_fechanacimiento, 4, 3, 1, 1)

        self.etiqueta_wpc_ine_fisico = QLabel(self.wpc_clientes_clienteFisico)
        self.etiqueta_wpc_ine_fisico.setObjectName(u"etiqueta_wpc_ine_fisico")
        self.etiqueta_wpc_ine_fisico.setMinimumSize(QSize(0, 0))

        self.gridLayout_5.addWidget(self.etiqueta_wpc_ine_fisico, 7, 2, 1, 1)

        self.etiqueta_wpc_ocupacion_fisico = QLabel(self.wpc_clientes_clienteFisico)
        self.etiqueta_wpc_ocupacion_fisico.setObjectName(u"etiqueta_wpc_ocupacion_fisico")
        self.etiqueta_wpc_ocupacion_fisico.setMinimumSize(QSize(0, 0))

        self.gridLayout_5.addWidget(self.etiqueta_wpc_ocupacion_fisico, 8, 2, 1, 1)

        self.etiqueta_wpc__telefono_fisico = QLabel(self.wpc_clientes_clienteFisico)
        self.etiqueta_wpc__telefono_fisico.setObjectName(u"etiqueta_wpc__telefono_fisico")
        self.etiqueta_wpc__telefono_fisico.setMinimumSize(QSize(0, 0))

        self.gridLayout_5.addWidget(self.etiqueta_wpc__telefono_fisico, 1, 2, 1, 1)

        self.etiqueta_wpc_nacimiento_fisico = QLabel(self.wpc_clientes_clienteFisico)
        self.etiqueta_wpc_nacimiento_fisico.setObjectName(u"etiqueta_wpc_nacimiento_fisico")
        self.etiqueta_wpc_nacimiento_fisico.setMinimumSize(QSize(0, 0))

        self.gridLayout_5.addWidget(self.etiqueta_wpc_nacimiento_fisico, 4, 2, 1, 1)

        self.txt_calles_fisico = QLineEdit(self.wpc_clientes_clienteFisico)
        self.txt_calles_fisico.setObjectName(u"txt_calles_fisico")
        self.txt_calles_fisico.setMinimumSize(QSize(200, 0))

        self.gridLayout_5.addWidget(self.txt_calles_fisico, 3, 3, 1, 1)

        self.txt_avenidas_fisico = QLineEdit(self.wpc_clientes_clienteFisico)
        self.txt_avenidas_fisico.setObjectName(u"txt_avenidas_fisico")
        self.txt_avenidas_fisico.setMinimumSize(QSize(200, 0))

        self.gridLayout_5.addWidget(self.txt_avenidas_fisico, 2, 3, 1, 1)

        self.txtlargo_comentarioclientefisico = QPlainTextEdit(self.wpc_clientes_clienteFisico)
        self.txtlargo_comentarioclientefisico.setObjectName(u"txtlargo_comentarioclientefisico")

        self.gridLayout_5.addWidget(self.txtlargo_comentarioclientefisico, 12, 1, 1, 3)

        self.etiqueta_wpc_ingresos_fisico = QLabel(self.wpc_clientes_clienteFisico)
        self.etiqueta_wpc_ingresos_fisico.setObjectName(u"etiqueta_wpc_ingresos_fisico")
        self.etiqueta_wpc_ingresos_fisico.setMinimumSize(QSize(0, 0))

        self.gridLayout_5.addWidget(self.etiqueta_wpc_ingresos_fisico, 8, 0, 1, 1)

        self.etiqueta_rfc_fisico = QLabel(self.wpc_clientes_clienteFisico)
        self.etiqueta_rfc_fisico.setObjectName(u"etiqueta_rfc_fisico")

        self.gridLayout_5.addWidget(self.etiqueta_rfc_fisico, 3, 0, 1, 1)

        self.txt_estado_fisico = QLineEdit(self.wpc_clientes_clienteFisico)
        self.txt_estado_fisico.setObjectName(u"txt_estado_fisico")

        self.gridLayout_5.addWidget(self.txt_estado_fisico, 5, 1, 1, 1)

        self.etiqueta_wpc_apellidoM_fisico = QLabel(self.wpc_clientes_clienteFisico)
        self.etiqueta_wpc_apellidoM_fisico.setObjectName(u"etiqueta_wpc_apellidoM_fisico")
        self.etiqueta_wpc_apellidoM_fisico.setMinimumSize(QSize(0, 0))

        self.gridLayout_5.addWidget(self.etiqueta_wpc_apellidoM_fisico, 2, 0, 1, 1)

        self.etiqueta_wpc_nombre_fisico = QLabel(self.wpc_clientes_clienteFisico)
        self.etiqueta_wpc_nombre_fisico.setObjectName(u"etiqueta_wpc_nombre_fisico")
        self.etiqueta_wpc_nombre_fisico.setMinimumSize(QSize(0, 0))

        self.gridLayout_5.addWidget(self.etiqueta_wpc_nombre_fisico, 0, 0, 1, 1)

        self.etiqueta_estado_fisico = QLabel(self.wpc_clientes_clienteFisico)
        self.etiqueta_estado_fisico.setObjectName(u"etiqueta_estado_fisico")

        self.gridLayout_5.addWidget(self.etiqueta_estado_fisico, 5, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.cajaOpciones_areasnegocio_fisico = QComboBox(self.wpc_clientes_clienteFisico)
        self.cajaOpciones_areasnegocio_fisico.addItem("")
        self.cajaOpciones_areasnegocio_fisico.setObjectName(u"cajaOpciones_areasnegocio_fisico")
        self.cajaOpciones_areasnegocio_fisico.setSizeAdjustPolicy(QComboBox.SizeAdjustPolicy.AdjustToContents)

        self.horizontalLayout.addWidget(self.cajaOpciones_areasnegocio_fisico)

        self.btn_btn_nuevaareanegocio_fisico = QPushButton(self.wpc_clientes_clienteFisico)
        self.btn_btn_nuevaareanegocio_fisico.setObjectName(u"btn_btn_nuevaareanegocio_fisico")
        self.btn_btn_nuevaareanegocio_fisico.setMaximumSize(QSize(16777215, 16777215))
        self.btn_btn_nuevaareanegocio_fisico.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_btn_nuevaareanegocio_fisico.setIcon(icon)
        self.btn_btn_nuevaareanegocio_fisico.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.btn_btn_nuevaareanegocio_fisico)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.gridLayout_5.addLayout(self.horizontalLayout, 9, 1, 1, 1)

        self.etiqueta_direccionadicional_fisico = QLabel(self.wpc_clientes_clienteFisico)
        self.etiqueta_direccionadicional_fisico.setObjectName(u"etiqueta_direccionadicional_fisico")

        self.gridLayout_5.addWidget(self.etiqueta_direccionadicional_fisico, 10, 0, 1, 1)

        self.txt_ciudad_fisico = QLineEdit(self.wpc_clientes_clienteFisico)
        self.txt_ciudad_fisico.setObjectName(u"txt_ciudad_fisico")

        self.gridLayout_5.addWidget(self.txt_ciudad_fisico, 5, 3, 1, 1)

        self.txt_apellidop_fisico = QLineEdit(self.wpc_clientes_clienteFisico)
        self.txt_apellidop_fisico.setObjectName(u"txt_apellidop_fisico")
        self.txt_apellidop_fisico.setMinimumSize(QSize(200, 0))

        self.gridLayout_5.addWidget(self.txt_apellidop_fisico, 1, 1, 1, 1)

        self.txt_ocupacion_fisico = QLineEdit(self.wpc_clientes_clienteFisico)
        self.txt_ocupacion_fisico.setObjectName(u"txt_ocupacion_fisico")
        self.txt_ocupacion_fisico.setMinimumSize(QSize(200, 0))

        self.gridLayout_5.addWidget(self.txt_ocupacion_fisico, 8, 3, 1, 1)

        self.etiqueta_wpc_estadocivil_fisico = QLabel(self.wpc_clientes_clienteFisico)
        self.etiqueta_wpc_estadocivil_fisico.setObjectName(u"etiqueta_wpc_estadocivil_fisico")
        self.etiqueta_wpc_estadocivil_fisico.setMinimumSize(QSize(0, 0))

        self.gridLayout_5.addWidget(self.etiqueta_wpc_estadocivil_fisico, 7, 0, 1, 1)

        self.txt_correo_fisico = QLineEdit(self.wpc_clientes_clienteFisico)
        self.txt_correo_fisico.setObjectName(u"txt_correo_fisico")
        self.txt_correo_fisico.setMinimumSize(QSize(200, 0))

        self.gridLayout_5.addWidget(self.txt_correo_fisico, 0, 3, 1, 1)

        self.txt_apellidom_fisico = QLineEdit(self.wpc_clientes_clienteFisico)
        self.txt_apellidom_fisico.setObjectName(u"txt_apellidom_fisico")
        self.txt_apellidom_fisico.setMinimumSize(QSize(200, 0))

        self.gridLayout_5.addWidget(self.txt_apellidom_fisico, 2, 1, 1, 1)

        self.txt_pais_fisico = QLineEdit(self.wpc_clientes_clienteFisico)
        self.txt_pais_fisico.setObjectName(u"txt_pais_fisico")

        self.gridLayout_5.addWidget(self.txt_pais_fisico, 4, 1, 1, 1)

        self.etiqueta_wpc_avenidas_fisico = QLabel(self.wpc_clientes_clienteFisico)
        self.etiqueta_wpc_avenidas_fisico.setObjectName(u"etiqueta_wpc_avenidas_fisico")
        self.etiqueta_wpc_avenidas_fisico.setMinimumSize(QSize(0, 0))
        self.etiqueta_wpc_avenidas_fisico.setWordWrap(False)

        self.gridLayout_5.addWidget(self.etiqueta_wpc_avenidas_fisico, 2, 2, 1, 1)

        self.txt_curp_fisico = QLineEdit(self.wpc_clientes_clienteFisico)
        self.txt_curp_fisico.setObjectName(u"txt_curp_fisico")
        self.txt_curp_fisico.setMinimumSize(QSize(200, 0))

        self.gridLayout_5.addWidget(self.txt_curp_fisico, 6, 1, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_4, 14, 2, 1, 1)

        self.etiqueta_wpc_correo_fisico = QLabel(self.wpc_clientes_clienteFisico)
        self.etiqueta_wpc_correo_fisico.setObjectName(u"etiqueta_wpc_correo_fisico")
        self.etiqueta_wpc_correo_fisico.setMinimumSize(QSize(0, 0))

        self.gridLayout_5.addWidget(self.etiqueta_wpc_correo_fisico, 0, 2, 1, 1)

        self.cajaOpciones_estadocivil_fisico = QComboBox(self.wpc_clientes_clienteFisico)
        self.cajaOpciones_estadocivil_fisico.addItem("")
        self.cajaOpciones_estadocivil_fisico.addItem("")
        self.cajaOpciones_estadocivil_fisico.addItem("")
        self.cajaOpciones_estadocivil_fisico.addItem("")
        self.cajaOpciones_estadocivil_fisico.addItem("")
        self.cajaOpciones_estadocivil_fisico.setObjectName(u"cajaOpciones_estadocivil_fisico")

        self.gridLayout_5.addWidget(self.cajaOpciones_estadocivil_fisico, 7, 1, 1, 1)

        self.txt_telefono_fisico = QLineEdit(self.wpc_clientes_clienteFisico)
        self.txt_telefono_fisico.setObjectName(u"txt_telefono_fisico")
        self.txt_telefono_fisico.setMinimumSize(QSize(200, 0))

        self.gridLayout_5.addWidget(self.txt_telefono_fisico, 1, 3, 1, 1)

        self.etiqueta_pais_fisico = QLabel(self.wpc_clientes_clienteFisico)
        self.etiqueta_pais_fisico.setObjectName(u"etiqueta_pais_fisico")

        self.gridLayout_5.addWidget(self.etiqueta_pais_fisico, 4, 0, 1, 1)

        self.etiqueta_wpc_ApellidoP_fisico = QLabel(self.wpc_clientes_clienteFisico)
        self.etiqueta_wpc_ApellidoP_fisico.setObjectName(u"etiqueta_wpc_ApellidoP_fisico")
        self.etiqueta_wpc_ApellidoP_fisico.setMinimumSize(QSize(0, 0))

        self.gridLayout_5.addWidget(self.etiqueta_wpc_ApellidoP_fisico, 1, 0, 1, 1)

        self.etiqueta_categoriaFisico = QLabel(self.wpc_clientes_clienteFisico)
        self.etiqueta_categoriaFisico.setObjectName(u"etiqueta_categoriaFisico")

        self.gridLayout_5.addWidget(self.etiqueta_categoriaFisico, 9, 2, 1, 1)


        self.gridLayout_7.addWidget(self.wpc_clientes_clienteFisico, 0, 0, 1, 1)

        self.contenedor_izquierda = QFrame(self.wpc_contenedor_clientfisico)
        self.contenedor_izquierda.setObjectName(u"contenedor_izquierda")
        self.contenedor_izquierda.setFrameShape(QFrame.Shape.StyledPanel)
        self.contenedor_izquierda.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_6 = QGridLayout(self.contenedor_izquierda)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_wpc_fotocliente = QLabel(self.contenedor_izquierda)
        self.label_wpc_fotocliente.setObjectName(u"label_wpc_fotocliente")
        self.label_wpc_fotocliente.setMinimumSize(QSize(202, 202))
        self.label_wpc_fotocliente.setMaximumSize(QSize(52, 52))
        font = QFont()
        self.label_wpc_fotocliente.setFont(font)
        self.label_wpc_fotocliente.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.label_wpc_fotocliente.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_6.addWidget(self.label_wpc_fotocliente, 0, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.wpc_clientes_autorizacredito = QWidget(self.contenedor_izquierda)
        self.wpc_clientes_autorizacredito.setObjectName(u"wpc_clientes_autorizacredito")
        self.formLayout = QFormLayout(self.wpc_clientes_autorizacredito)
        self.formLayout.setObjectName(u"formLayout")
        self.casillaverificacion_wpc_credito_autorizado = QCheckBox(self.wpc_clientes_autorizacredito)
        self.casillaverificacion_wpc_credito_autorizado.setObjectName(u"casillaverificacion_wpc_credito_autorizado")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.SpanningRole, self.casillaverificacion_wpc_credito_autorizado)

        self.etiqueta_wpc_limitecredito = QLabel(self.wpc_clientes_autorizacredito)
        self.etiqueta_wpc_limitecredito.setObjectName(u"etiqueta_wpc_limitecredito")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.etiqueta_wpc_limitecredito)

        self.cajaDecimal_wpc_limite_credito = QDoubleSpinBox(self.wpc_clientes_autorizacredito)
        self.cajaDecimal_wpc_limite_credito.setObjectName(u"cajaDecimal_wpc_limite_credito")
        self.cajaDecimal_wpc_limite_credito.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.cajaDecimal_wpc_limite_credito.setMaximum(99999999.989999994635582)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.cajaDecimal_wpc_limite_credito)

        self.etiqueta_creditodisponible_fisico = QLabel(self.wpc_clientes_autorizacredito)
        self.etiqueta_creditodisponible_fisico.setObjectName(u"etiqueta_creditodisponible_fisico")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.etiqueta_creditodisponible_fisico)

        self.cajaDecimal_creditodisponible_fisico = QDoubleSpinBox(self.wpc_clientes_autorizacredito)
        self.cajaDecimal_creditodisponible_fisico.setObjectName(u"cajaDecimal_creditodisponible_fisico")
        self.cajaDecimal_creditodisponible_fisico.setEnabled(False)
        self.cajaDecimal_creditodisponible_fisico.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.cajaDecimal_creditodisponible_fisico.setMaximum(99999999.989999994635582)

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.cajaDecimal_creditodisponible_fisico)

        self.etiqueta_creditoutilizado_fisico = QLabel(self.wpc_clientes_autorizacredito)
        self.etiqueta_creditoutilizado_fisico.setObjectName(u"etiqueta_creditoutilizado_fisico")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.etiqueta_creditoutilizado_fisico)

        self.cajaDecimal_creditoutilizado_fisico = QDoubleSpinBox(self.wpc_clientes_autorizacredito)
        self.cajaDecimal_creditoutilizado_fisico.setObjectName(u"cajaDecimal_creditoutilizado_fisico")
        self.cajaDecimal_creditoutilizado_fisico.setEnabled(False)
        self.cajaDecimal_creditoutilizado_fisico.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.cajaDecimal_creditoutilizado_fisico.setMaximum(99999999.989999994635582)

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.cajaDecimal_creditoutilizado_fisico)

        self.etiqueta_estadodelcredito_fisico = QLabel(self.wpc_clientes_autorizacredito)
        self.etiqueta_estadodelcredito_fisico.setObjectName(u"etiqueta_estadodelcredito_fisico")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.SpanningRole, self.etiqueta_estadodelcredito_fisico)

        self.txt_estadodelcredito_fisico = QLineEdit(self.wpc_clientes_autorizacredito)
        self.txt_estadodelcredito_fisico.setObjectName(u"txt_estadodelcredito_fisico")
        self.txt_estadodelcredito_fisico.setEnabled(False)

        self.formLayout.setWidget(5, QFormLayout.ItemRole.SpanningRole, self.txt_estadodelcredito_fisico)

        self.etiqueta_porcentajeintereses_fisico = QLabel(self.wpc_clientes_autorizacredito)
        self.etiqueta_porcentajeintereses_fisico.setObjectName(u"etiqueta_porcentajeintereses_fisico")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.LabelRole, self.etiqueta_porcentajeintereses_fisico)

        self.cajaDecimal_interesesaplicados_fisico = QDoubleSpinBox(self.wpc_clientes_autorizacredito)
        self.cajaDecimal_interesesaplicados_fisico.setObjectName(u"cajaDecimal_interesesaplicados_fisico")
        self.cajaDecimal_interesesaplicados_fisico.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.cajaDecimal_interesesaplicados_fisico.setMaximum(99999999.989999994635582)

        self.formLayout.setWidget(6, QFormLayout.ItemRole.FieldRole, self.cajaDecimal_interesesaplicados_fisico)

        self.casillaverificacion_aplicadescuento_fisico = QCheckBox(self.wpc_clientes_autorizacredito)
        self.casillaverificacion_aplicadescuento_fisico.setObjectName(u"casillaverificacion_aplicadescuento_fisico")

        self.formLayout.setWidget(7, QFormLayout.ItemRole.SpanningRole, self.casillaverificacion_aplicadescuento_fisico)

        self.etiqueta_porcentajedescuento_fisico = QLabel(self.wpc_clientes_autorizacredito)
        self.etiqueta_porcentajedescuento_fisico.setObjectName(u"etiqueta_porcentajedescuento_fisico")

        self.formLayout.setWidget(8, QFormLayout.ItemRole.LabelRole, self.etiqueta_porcentajedescuento_fisico)

        self.cajaDecimal_porcentajedescuento_fisico = QDoubleSpinBox(self.wpc_clientes_autorizacredito)
        self.cajaDecimal_porcentajedescuento_fisico.setObjectName(u"cajaDecimal_porcentajedescuento_fisico")
        self.cajaDecimal_porcentajedescuento_fisico.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.cajaDecimal_porcentajedescuento_fisico.setMaximum(99999999.989999994635582)

        self.formLayout.setWidget(8, QFormLayout.ItemRole.FieldRole, self.cajaDecimal_porcentajedescuento_fisico)

        self.line_2 = QFrame(self.wpc_clientes_autorizacredito)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.formLayout.setWidget(9, QFormLayout.ItemRole.SpanningRole, self.line_2)

        self.etiqueta_entidadlegalizada_fisico = QLabel(self.wpc_clientes_autorizacredito)
        self.etiqueta_entidadlegalizada_fisico.setObjectName(u"etiqueta_entidadlegalizada_fisico")

        self.formLayout.setWidget(10, QFormLayout.ItemRole.SpanningRole, self.etiqueta_entidadlegalizada_fisico)

        self.casillaverificacion_entidadlegalizada_fisico = QCheckBox(self.wpc_clientes_autorizacredito)
        self.casillaverificacion_entidadlegalizada_fisico.setObjectName(u"casillaverificacion_entidadlegalizada_fisico")

        self.formLayout.setWidget(11, QFormLayout.ItemRole.SpanningRole, self.casillaverificacion_entidadlegalizada_fisico)

        self.etiqueta_fechaultimoreporte_fisico = QLabel(self.wpc_clientes_autorizacredito)
        self.etiqueta_fechaultimoreporte_fisico.setObjectName(u"etiqueta_fechaultimoreporte_fisico")

        self.formLayout.setWidget(13, QFormLayout.ItemRole.LabelRole, self.etiqueta_fechaultimoreporte_fisico)

        self.fecha_ultimoreporte_fisico = QDateEdit(self.wpc_clientes_autorizacredito)
        self.fecha_ultimoreporte_fisico.setObjectName(u"fecha_ultimoreporte_fisico")
        self.fecha_ultimoreporte_fisico.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)

        self.formLayout.setWidget(13, QFormLayout.ItemRole.FieldRole, self.fecha_ultimoreporte_fisico)

        self.verticalSpacer = QSpacerItem(149, 117, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.formLayout.setItem(14, QFormLayout.ItemRole.SpanningRole, self.verticalSpacer)


        self.gridLayout_6.addWidget(self.wpc_clientes_autorizacredito, 1, 0, 1, 1)


        self.gridLayout_7.addWidget(self.contenedor_izquierda, 0, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_7.addItem(self.verticalSpacer_2, 1, 0, 1, 1)


        self.gridLayout_3.addWidget(self.wpc_contenedor_clientfisico, 0, 0, 1, 1)

        self.wpc_contenedor_pila.addWidget(self.wpc_pagina_clientefisico)
        self.wpc_pagina_clientemoral = QWidget()
        self.wpc_pagina_clientemoral.setObjectName(u"wpc_pagina_clientemoral")
        self.gridLayout = QGridLayout(self.wpc_pagina_clientemoral)
        self.gridLayout.setObjectName(u"gridLayout")
        self.wpc_contenedor_clientmoral = QFrame(self.wpc_pagina_clientemoral)
        self.wpc_contenedor_clientmoral.setObjectName(u"wpc_contenedor_clientmoral")
        self.wpc_contenedor_clientmoral.setFrameShape(QFrame.Shape.StyledPanel)
        self.wpc_contenedor_clientmoral.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_18 = QGridLayout(self.wpc_contenedor_clientmoral)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.wpc_clientes_autorizacredito_moral = QWidget(self.wpc_contenedor_clientmoral)
        self.wpc_clientes_autorizacredito_moral.setObjectName(u"wpc_clientes_autorizacredito_moral")
        self.formLayout_2 = QFormLayout(self.wpc_clientes_autorizacredito_moral)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.casillaverificacion_wpc_credito_autorizado_moral = QCheckBox(self.wpc_clientes_autorizacredito_moral)
        self.casillaverificacion_wpc_credito_autorizado_moral.setObjectName(u"casillaverificacion_wpc_credito_autorizado_moral")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.SpanningRole, self.casillaverificacion_wpc_credito_autorizado_moral)

        self.etiqueta_wpc_limitecredito_moral = QLabel(self.wpc_clientes_autorizacredito_moral)
        self.etiqueta_wpc_limitecredito_moral.setObjectName(u"etiqueta_wpc_limitecredito_moral")

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.LabelRole, self.etiqueta_wpc_limitecredito_moral)

        self.cajaDecimal_wpc_limite_credito_moral = QDoubleSpinBox(self.wpc_clientes_autorizacredito_moral)
        self.cajaDecimal_wpc_limite_credito_moral.setObjectName(u"cajaDecimal_wpc_limite_credito_moral")
        self.cajaDecimal_wpc_limite_credito_moral.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.cajaDecimal_wpc_limite_credito_moral.setMaximum(99999999.989999994635582)

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.FieldRole, self.cajaDecimal_wpc_limite_credito_moral)

        self.etiqueta_entidadlegalizada_moral = QLabel(self.wpc_clientes_autorizacredito_moral)
        self.etiqueta_entidadlegalizada_moral.setObjectName(u"etiqueta_entidadlegalizada_moral")

        self.formLayout_2.setWidget(9, QFormLayout.ItemRole.SpanningRole, self.etiqueta_entidadlegalizada_moral)

        self.casillaverificacion_entidadlegalizada_moral = QCheckBox(self.wpc_clientes_autorizacredito_moral)
        self.casillaverificacion_entidadlegalizada_moral.setObjectName(u"casillaverificacion_entidadlegalizada_moral")

        self.formLayout_2.setWidget(10, QFormLayout.ItemRole.SpanningRole, self.casillaverificacion_entidadlegalizada_moral)

        self.etiqueta_estadocredito_moral = QLabel(self.wpc_clientes_autorizacredito_moral)
        self.etiqueta_estadocredito_moral.setObjectName(u"etiqueta_estadocredito_moral")

        self.formLayout_2.setWidget(4, QFormLayout.ItemRole.SpanningRole, self.etiqueta_estadocredito_moral)

        self.txt_estadocredito_moral = QLineEdit(self.wpc_clientes_autorizacredito_moral)
        self.txt_estadocredito_moral.setObjectName(u"txt_estadocredito_moral")
        self.txt_estadocredito_moral.setEnabled(False)

        self.formLayout_2.setWidget(5, QFormLayout.ItemRole.SpanningRole, self.txt_estadocredito_moral)

        self.etiqueta_creditodisponible_moral = QLabel(self.wpc_clientes_autorizacredito_moral)
        self.etiqueta_creditodisponible_moral.setObjectName(u"etiqueta_creditodisponible_moral")

        self.formLayout_2.setWidget(2, QFormLayout.ItemRole.LabelRole, self.etiqueta_creditodisponible_moral)

        self.cajaDecimal_creditodisponible_moral = QDoubleSpinBox(self.wpc_clientes_autorizacredito_moral)
        self.cajaDecimal_creditodisponible_moral.setObjectName(u"cajaDecimal_creditodisponible_moral")
        self.cajaDecimal_creditodisponible_moral.setEnabled(False)
        self.cajaDecimal_creditodisponible_moral.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.cajaDecimal_creditodisponible_moral.setMaximum(99999999.989999994635582)

        self.formLayout_2.setWidget(2, QFormLayout.ItemRole.FieldRole, self.cajaDecimal_creditodisponible_moral)

        self.etiqueta_creditoutilizado_moral = QLabel(self.wpc_clientes_autorizacredito_moral)
        self.etiqueta_creditoutilizado_moral.setObjectName(u"etiqueta_creditoutilizado_moral")

        self.formLayout_2.setWidget(3, QFormLayout.ItemRole.LabelRole, self.etiqueta_creditoutilizado_moral)

        self.cajaDecimal_creditoutilizado_moral = QDoubleSpinBox(self.wpc_clientes_autorizacredito_moral)
        self.cajaDecimal_creditoutilizado_moral.setObjectName(u"cajaDecimal_creditoutilizado_moral")
        self.cajaDecimal_creditoutilizado_moral.setEnabled(False)
        self.cajaDecimal_creditoutilizado_moral.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.cajaDecimal_creditoutilizado_moral.setMaximum(99999999.989999994635582)

        self.formLayout_2.setWidget(3, QFormLayout.ItemRole.FieldRole, self.cajaDecimal_creditoutilizado_moral)

        self.etiqueta_porcentajeintereses_moral = QLabel(self.wpc_clientes_autorizacredito_moral)
        self.etiqueta_porcentajeintereses_moral.setObjectName(u"etiqueta_porcentajeintereses_moral")

        self.formLayout_2.setWidget(6, QFormLayout.ItemRole.LabelRole, self.etiqueta_porcentajeintereses_moral)

        self.cajaDecimal_porcentajeintereses_moral = QDoubleSpinBox(self.wpc_clientes_autorizacredito_moral)
        self.cajaDecimal_porcentajeintereses_moral.setObjectName(u"cajaDecimal_porcentajeintereses_moral")
        self.cajaDecimal_porcentajeintereses_moral.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.cajaDecimal_porcentajeintereses_moral.setMaximum(99999999.989999994635582)

        self.formLayout_2.setWidget(6, QFormLayout.ItemRole.FieldRole, self.cajaDecimal_porcentajeintereses_moral)

        self.casillaverificacion_aplicadescuento_moral = QCheckBox(self.wpc_clientes_autorizacredito_moral)
        self.casillaverificacion_aplicadescuento_moral.setObjectName(u"casillaverificacion_aplicadescuento_moral")

        self.formLayout_2.setWidget(7, QFormLayout.ItemRole.SpanningRole, self.casillaverificacion_aplicadescuento_moral)

        self.etiqueta_porcentajedescuento_moral = QLabel(self.wpc_clientes_autorizacredito_moral)
        self.etiqueta_porcentajedescuento_moral.setObjectName(u"etiqueta_porcentajedescuento_moral")

        self.formLayout_2.setWidget(8, QFormLayout.ItemRole.LabelRole, self.etiqueta_porcentajedescuento_moral)

        self.cajaDecimal_porcentajedescuento_moral = QDoubleSpinBox(self.wpc_clientes_autorizacredito_moral)
        self.cajaDecimal_porcentajedescuento_moral.setObjectName(u"cajaDecimal_porcentajedescuento_moral")
        self.cajaDecimal_porcentajedescuento_moral.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.cajaDecimal_porcentajedescuento_moral.setMaximum(99999999.989999994635582)

        self.formLayout_2.setWidget(8, QFormLayout.ItemRole.FieldRole, self.cajaDecimal_porcentajedescuento_moral)

        self.etiqueta_ultimoreporte_moral = QLabel(self.wpc_clientes_autorizacredito_moral)
        self.etiqueta_ultimoreporte_moral.setObjectName(u"etiqueta_ultimoreporte_moral")

        self.formLayout_2.setWidget(11, QFormLayout.ItemRole.LabelRole, self.etiqueta_ultimoreporte_moral)

        self.fecha_ultimoreporte_moral = QDateEdit(self.wpc_clientes_autorizacredito_moral)
        self.fecha_ultimoreporte_moral.setObjectName(u"fecha_ultimoreporte_moral")
        self.fecha_ultimoreporte_moral.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)

        self.formLayout_2.setWidget(11, QFormLayout.ItemRole.FieldRole, self.fecha_ultimoreporte_moral)


        self.gridLayout_18.addWidget(self.wpc_clientes_autorizacredito_moral, 0, 1, 1, 1)

        self.wpc_contenedor_clienteMoral = QWidget(self.wpc_contenedor_clientmoral)
        self.wpc_contenedor_clienteMoral.setObjectName(u"wpc_contenedor_clienteMoral")
        self.wpc_contenedor_clienteMoral.setEnabled(True)
        self.wpc_contenedor_clienteMoral.setMaximumSize(QSize(16777215, 16777215))
        self.gridLayout_15 = QGridLayout(self.wpc_contenedor_clienteMoral)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.etiqueta_wpc_rfc_moral = QLabel(self.wpc_contenedor_clienteMoral)
        self.etiqueta_wpc_rfc_moral.setObjectName(u"etiqueta_wpc_rfc_moral")
        self.etiqueta_wpc_rfc_moral.setMinimumSize(QSize(0, 0))

        self.gridLayout_15.addWidget(self.etiqueta_wpc_rfc_moral, 4, 0, 1, 1)

        self.txt_calles_empre_moral = QLineEdit(self.wpc_contenedor_clienteMoral)
        self.txt_calles_empre_moral.setObjectName(u"txt_calles_empre_moral")
        self.txt_calles_empre_moral.setMinimumSize(QSize(200, 17))

        self.gridLayout_15.addWidget(self.txt_calles_empre_moral, 2, 4, 1, 1)

        self.txt_ciudad_moral = QLineEdit(self.wpc_contenedor_clienteMoral)
        self.txt_ciudad_moral.setObjectName(u"txt_ciudad_moral")

        self.gridLayout_15.addWidget(self.txt_ciudad_moral, 7, 1, 1, 2)

        self.gridLayout_13 = QGridLayout()
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.btn_btn_nuevacategoriaMoral = QPushButton(self.wpc_contenedor_clienteMoral)
        self.btn_btn_nuevacategoriaMoral.setObjectName(u"btn_btn_nuevacategoriaMoral")
        self.btn_btn_nuevacategoriaMoral.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_btn_nuevacategoriaMoral.setIcon(icon)
        self.btn_btn_nuevacategoriaMoral.setIconSize(QSize(20, 20))

        self.gridLayout_13.addWidget(self.btn_btn_nuevacategoriaMoral, 0, 1, 1, 1)

        self.cajaOpciones_categoriaMoral = QComboBox(self.wpc_contenedor_clienteMoral)
        self.cajaOpciones_categoriaMoral.addItem("")
        self.cajaOpciones_categoriaMoral.setObjectName(u"cajaOpciones_categoriaMoral")

        self.gridLayout_13.addWidget(self.cajaOpciones_categoriaMoral, 0, 0, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_13.addItem(self.horizontalSpacer_5, 0, 2, 1, 1)


        self.gridLayout_15.addLayout(self.gridLayout_13, 5, 4, 1, 1)

        self.txt_correo_repre_moral = QLineEdit(self.wpc_contenedor_clienteMoral)
        self.txt_correo_repre_moral.setObjectName(u"txt_correo_repre_moral")
        self.txt_correo_repre_moral.setMinimumSize(QSize(200, 17))

        self.gridLayout_15.addWidget(self.txt_correo_repre_moral, 13, 4, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.btn_btn_areasnegocio_moral = QPushButton(self.wpc_contenedor_clienteMoral)
        self.btn_btn_areasnegocio_moral.setObjectName(u"btn_btn_areasnegocio_moral")
        self.btn_btn_areasnegocio_moral.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_btn_areasnegocio_moral.setIcon(icon)
        self.btn_btn_areasnegocio_moral.setIconSize(QSize(20, 20))

        self.gridLayout_2.addWidget(self.btn_btn_areasnegocio_moral, 1, 1, 1, 1)

        self.cajaOpciones_areasnegocio_moral = QComboBox(self.wpc_contenedor_clienteMoral)
        self.cajaOpciones_areasnegocio_moral.addItem("")
        self.cajaOpciones_areasnegocio_moral.setObjectName(u"cajaOpciones_areasnegocio_moral")

        self.gridLayout_2.addWidget(self.cajaOpciones_areasnegocio_moral, 1, 0, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_4, 1, 2, 1, 1)


        self.gridLayout_15.addLayout(self.gridLayout_2, 8, 1, 1, 2)

        self.etiqueta_wpc_fechaconst_moral = QLabel(self.wpc_contenedor_clienteMoral)
        self.etiqueta_wpc_fechaconst_moral.setObjectName(u"etiqueta_wpc_fechaconst_moral")
        self.etiqueta_wpc_fechaconst_moral.setMinimumSize(QSize(0, 0))

        self.gridLayout_15.addWidget(self.etiqueta_wpc_fechaconst_moral, 3, 3, 1, 1)

        self.txt_estado_moral = QLineEdit(self.wpc_contenedor_clienteMoral)
        self.txt_estado_moral.setObjectName(u"txt_estado_moral")

        self.gridLayout_15.addWidget(self.txt_estado_moral, 6, 4, 1, 1)

        self.txt_codigopostal_moral = QLineEdit(self.wpc_contenedor_clienteMoral)
        self.txt_codigopostal_moral.setObjectName(u"txt_codigopostal_moral")

        self.gridLayout_15.addWidget(self.txt_codigopostal_moral, 7, 4, 1, 1)

        self.etiqueta_estado_moral = QLabel(self.wpc_contenedor_clienteMoral)
        self.etiqueta_estado_moral.setObjectName(u"etiqueta_estado_moral")

        self.gridLayout_15.addWidget(self.etiqueta_estado_moral, 6, 3, 1, 1)

        self.txt_sector_empre_moral = QLineEdit(self.wpc_contenedor_clienteMoral)
        self.txt_sector_empre_moral.setObjectName(u"txt_sector_empre_moral")
        self.txt_sector_empre_moral.setMinimumSize(QSize(200, 17))

        self.gridLayout_15.addWidget(self.txt_sector_empre_moral, 4, 4, 1, 1)

        self.txtlargo_comentarios_cliente_moral = QPlainTextEdit(self.wpc_contenedor_clienteMoral)
        self.txtlargo_comentarios_cliente_moral.setObjectName(u"txtlargo_comentarios_cliente_moral")

        self.gridLayout_15.addWidget(self.txtlargo_comentarios_cliente_moral, 10, 2, 1, 3)

        self.etiqueta_wpc_sector_moral = QLabel(self.wpc_contenedor_clienteMoral)
        self.etiqueta_wpc_sector_moral.setObjectName(u"etiqueta_wpc_sector_moral")
        self.etiqueta_wpc_sector_moral.setMinimumSize(QSize(0, 0))

        self.gridLayout_15.addWidget(self.etiqueta_wpc_sector_moral, 4, 3, 1, 1)

        self.etiqueta_wpc_pagina_moral = QLabel(self.wpc_contenedor_clienteMoral)
        self.etiqueta_wpc_pagina_moral.setObjectName(u"etiqueta_wpc_pagina_moral")
        self.etiqueta_wpc_pagina_moral.setMinimumSize(QSize(0, 0))

        self.gridLayout_15.addWidget(self.etiqueta_wpc_pagina_moral, 5, 0, 1, 1)

        self.txt_nombre_repre_moral = QLineEdit(self.wpc_contenedor_clienteMoral)
        self.txt_nombre_repre_moral.setObjectName(u"txt_nombre_repre_moral")
        self.txt_nombre_repre_moral.setMinimumSize(QSize(200, 0))

        self.gridLayout_15.addWidget(self.txt_nombre_repre_moral, 12, 2, 1, 1)

        self.txt_puesto_repre_moral = QLineEdit(self.wpc_contenedor_clienteMoral)
        self.txt_puesto_repre_moral.setObjectName(u"txt_puesto_repre_moral")
        self.txt_puesto_repre_moral.setMinimumSize(QSize(200, 17))

        self.gridLayout_15.addWidget(self.txt_puesto_repre_moral, 12, 4, 1, 1)

        self.etiqueta_wpc_puesto_representante_moral = QLabel(self.wpc_contenedor_clienteMoral)
        self.etiqueta_wpc_puesto_representante_moral.setObjectName(u"etiqueta_wpc_puesto_representante_moral")
        self.etiqueta_wpc_puesto_representante_moral.setMinimumSize(QSize(0, 0))

        self.gridLayout_15.addWidget(self.etiqueta_wpc_puesto_representante_moral, 12, 3, 1, 1)

        self.etiqueta_nif_moral = QLabel(self.wpc_contenedor_clienteMoral)
        self.etiqueta_nif_moral.setObjectName(u"etiqueta_nif_moral")

        self.gridLayout_15.addWidget(self.etiqueta_nif_moral, 1, 3, 1, 1)

        self.etiqueta_wpc_representante_moral = QLabel(self.wpc_contenedor_clienteMoral)
        self.etiqueta_wpc_representante_moral.setObjectName(u"etiqueta_wpc_representante_moral")
        self.etiqueta_wpc_representante_moral.setMinimumSize(QSize(0, 0))

        self.gridLayout_15.addWidget(self.etiqueta_wpc_representante_moral, 12, 0, 1, 1)

        self.txt_pais_moral = QLineEdit(self.wpc_contenedor_clienteMoral)
        self.txt_pais_moral.setObjectName(u"txt_pais_moral")

        self.gridLayout_15.addWidget(self.txt_pais_moral, 6, 1, 1, 2)

        self.txt_razonsocial_moral = QLineEdit(self.wpc_contenedor_clienteMoral)
        self.txt_razonsocial_moral.setObjectName(u"txt_razonsocial_moral")

        self.gridLayout_15.addWidget(self.txt_razonsocial_moral, 1, 1, 1, 2)

        self.etiqueta_codigopostal_moral = QLabel(self.wpc_contenedor_clienteMoral)
        self.etiqueta_codigopostal_moral.setObjectName(u"etiqueta_codigopostal_moral")

        self.gridLayout_15.addWidget(self.etiqueta_codigopostal_moral, 7, 3, 1, 1)

        self.txt_avenidas_empre_moral = QLineEdit(self.wpc_contenedor_clienteMoral)
        self.txt_avenidas_empre_moral.setObjectName(u"txt_avenidas_empre_moral")
        self.txt_avenidas_empre_moral.setMinimumSize(QSize(200, 0))

        self.gridLayout_15.addWidget(self.txt_avenidas_empre_moral, 3, 1, 1, 2)

        self.etiqueta_comentarios_cliente_moral = QLabel(self.wpc_contenedor_clienteMoral)
        self.etiqueta_comentarios_cliente_moral.setObjectName(u"etiqueta_comentarios_cliente_moral")

        self.gridLayout_15.addWidget(self.etiqueta_comentarios_cliente_moral, 10, 0, 1, 1)

        self.etiqueta_wpc_telefono_moral = QLabel(self.wpc_contenedor_clienteMoral)
        self.etiqueta_wpc_telefono_moral.setObjectName(u"etiqueta_wpc_telefono_moral")
        self.etiqueta_wpc_telefono_moral.setMinimumSize(QSize(0, 0))

        self.gridLayout_15.addWidget(self.etiqueta_wpc_telefono_moral, 0, 3, 1, 1)

        self.etiqueta_pais_moral = QLabel(self.wpc_contenedor_clienteMoral)
        self.etiqueta_pais_moral.setObjectName(u"etiqueta_pais_moral")

        self.gridLayout_15.addWidget(self.etiqueta_pais_moral, 6, 0, 1, 1)

        self.etiqueta_areanegocio_moral = QLabel(self.wpc_contenedor_clienteMoral)
        self.etiqueta_areanegocio_moral.setObjectName(u"etiqueta_areanegocio_moral")

        self.gridLayout_15.addWidget(self.etiqueta_areanegocio_moral, 8, 0, 1, 1)

        self.line = QFrame(self.wpc_contenedor_clienteMoral)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_15.addWidget(self.line, 11, 0, 1, 5)

        self.fecha_fechaconstitucion = QDateEdit(self.wpc_contenedor_clienteMoral)
        self.fecha_fechaconstitucion.setObjectName(u"fecha_fechaconstitucion")
        self.fecha_fechaconstitucion.setCalendarPopup(True)

        self.gridLayout_15.addWidget(self.fecha_fechaconstitucion, 3, 4, 1, 1)

        self.etiqueta_categoriaMoral = QLabel(self.wpc_contenedor_clienteMoral)
        self.etiqueta_categoriaMoral.setObjectName(u"etiqueta_categoriaMoral")

        self.gridLayout_15.addWidget(self.etiqueta_categoriaMoral, 5, 3, 1, 1)

        self.txt_nombre_empre_moral = QLineEdit(self.wpc_contenedor_clienteMoral)
        self.txt_nombre_empre_moral.setObjectName(u"txt_nombre_empre_moral")
        self.txt_nombre_empre_moral.setMinimumSize(QSize(200, 0))

        self.gridLayout_15.addWidget(self.txt_nombre_empre_moral, 0, 1, 1, 2)

        self.txtlargo_direccionadicional_moral = QPlainTextEdit(self.wpc_contenedor_clienteMoral)
        self.txtlargo_direccionadicional_moral.setObjectName(u"txtlargo_direccionadicional_moral")

        self.gridLayout_15.addWidget(self.txtlargo_direccionadicional_moral, 9, 2, 1, 3)

        self.txt_correo_empre_moral = QLineEdit(self.wpc_contenedor_clienteMoral)
        self.txt_correo_empre_moral.setObjectName(u"txt_correo_empre_moral")
        self.txt_correo_empre_moral.setMinimumSize(QSize(200, 0))

        self.gridLayout_15.addWidget(self.txt_correo_empre_moral, 2, 1, 1, 2)

        self.txt_telefono_empre_moral = QLineEdit(self.wpc_contenedor_clienteMoral)
        self.txt_telefono_empre_moral.setObjectName(u"txt_telefono_empre_moral")
        self.txt_telefono_empre_moral.setMinimumSize(QSize(200, 17))

        self.gridLayout_15.addWidget(self.txt_telefono_empre_moral, 0, 4, 1, 1)

        self.etiqueta_razonsocial_moral = QLabel(self.wpc_contenedor_clienteMoral)
        self.etiqueta_razonsocial_moral.setObjectName(u"etiqueta_razonsocial_moral")

        self.gridLayout_15.addWidget(self.etiqueta_razonsocial_moral, 1, 0, 1, 1)

        self.etiqueta_wpc_nombre_moral = QLabel(self.wpc_contenedor_clienteMoral)
        self.etiqueta_wpc_nombre_moral.setObjectName(u"etiqueta_wpc_nombre_moral")
        self.etiqueta_wpc_nombre_moral.setMinimumSize(QSize(0, 0))

        self.gridLayout_15.addWidget(self.etiqueta_wpc_nombre_moral, 0, 0, 1, 1)

        self.txt_rfc_empre_moral = QLineEdit(self.wpc_contenedor_clienteMoral)
        self.txt_rfc_empre_moral.setObjectName(u"txt_rfc_empre_moral")
        self.txt_rfc_empre_moral.setMinimumSize(QSize(200, 0))

        self.gridLayout_15.addWidget(self.txt_rfc_empre_moral, 4, 1, 1, 2)

        self.txt_nif_moral = QLineEdit(self.wpc_contenedor_clienteMoral)
        self.txt_nif_moral.setObjectName(u"txt_nif_moral")

        self.gridLayout_15.addWidget(self.txt_nif_moral, 1, 4, 1, 1)

        self.etiqueta_ciudad_moral = QLabel(self.wpc_contenedor_clienteMoral)
        self.etiqueta_ciudad_moral.setObjectName(u"etiqueta_ciudad_moral")

        self.gridLayout_15.addWidget(self.etiqueta_ciudad_moral, 7, 0, 1, 1)

        self.etiqueta_wpc_telefono_representante_moral = QLabel(self.wpc_contenedor_clienteMoral)
        self.etiqueta_wpc_telefono_representante_moral.setObjectName(u"etiqueta_wpc_telefono_representante_moral")
        self.etiqueta_wpc_telefono_representante_moral.setMinimumSize(QSize(0, 0))

        self.gridLayout_15.addWidget(self.etiqueta_wpc_telefono_representante_moral, 13, 0, 1, 1)

        self.etiqueta_wpc_correo_moral = QLabel(self.wpc_contenedor_clienteMoral)
        self.etiqueta_wpc_correo_moral.setObjectName(u"etiqueta_wpc_correo_moral")
        self.etiqueta_wpc_correo_moral.setMinimumSize(QSize(0, 0))

        self.gridLayout_15.addWidget(self.etiqueta_wpc_correo_moral, 2, 0, 1, 1)

        self.txt_telefono_repre_moral = QLineEdit(self.wpc_contenedor_clienteMoral)
        self.txt_telefono_repre_moral.setObjectName(u"txt_telefono_repre_moral")
        self.txt_telefono_repre_moral.setMinimumSize(QSize(200, 0))

        self.gridLayout_15.addWidget(self.txt_telefono_repre_moral, 13, 2, 1, 1)

        self.txt_pagina_empre_moral = QLineEdit(self.wpc_contenedor_clienteMoral)
        self.txt_pagina_empre_moral.setObjectName(u"txt_pagina_empre_moral")
        self.txt_pagina_empre_moral.setMinimumSize(QSize(200, 0))

        self.gridLayout_15.addWidget(self.txt_pagina_empre_moral, 5, 1, 1, 2)

        self.etiqueta_wpc_calles_moral = QLabel(self.wpc_contenedor_clienteMoral)
        self.etiqueta_wpc_calles_moral.setObjectName(u"etiqueta_wpc_calles_moral")
        self.etiqueta_wpc_calles_moral.setMinimumSize(QSize(0, 0))

        self.gridLayout_15.addWidget(self.etiqueta_wpc_calles_moral, 2, 3, 1, 1)

        self.etiqueta_wpc_avenidas_moral = QLabel(self.wpc_contenedor_clienteMoral)
        self.etiqueta_wpc_avenidas_moral.setObjectName(u"etiqueta_wpc_avenidas_moral")
        self.etiqueta_wpc_avenidas_moral.setMinimumSize(QSize(0, 0))

        self.gridLayout_15.addWidget(self.etiqueta_wpc_avenidas_moral, 3, 0, 1, 1)

        self.etiqueta_direccionadicional_moral = QLabel(self.wpc_contenedor_clienteMoral)
        self.etiqueta_direccionadicional_moral.setObjectName(u"etiqueta_direccionadicional_moral")

        self.gridLayout_15.addWidget(self.etiqueta_direccionadicional_moral, 9, 0, 1, 1)

        self.etiqueta_wpc_correo_repre_moral = QLabel(self.wpc_contenedor_clienteMoral)
        self.etiqueta_wpc_correo_repre_moral.setObjectName(u"etiqueta_wpc_correo_repre_moral")
        self.etiqueta_wpc_correo_repre_moral.setMinimumSize(QSize(0, 0))

        self.gridLayout_15.addWidget(self.etiqueta_wpc_correo_repre_moral, 13, 3, 1, 1)


        self.gridLayout_18.addWidget(self.wpc_contenedor_clienteMoral, 0, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_18.addItem(self.verticalSpacer_3, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.wpc_contenedor_clientmoral, 0, 0, 1, 1)

        self.wpc_contenedor_pila.addWidget(self.wpc_pagina_clientemoral)

        self.gridLayout_4.addWidget(self.wpc_contenedor_pila, 1, 0, 1, 1)

        self.contenedor_opcionesclientes = QWidget(self.wpc_clientes_datos)
        self.contenedor_opcionesclientes.setObjectName(u"contenedor_opcionesclientes")
        self.contenedor_opcionesclientes.setMaximumSize(QSize(16777215, 16777215))
        self.gridLayout_14 = QGridLayout(self.contenedor_opcionesclientes)
        self.gridLayout_14.setSpacing(0)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.gridLayout_14.setContentsMargins(0, 0, 0, 0)
        self.btnRadio_wpc_clienteFisico = QRadioButton(self.contenedor_opcionesclientes)
        self.btnRadio_wpc_clienteFisico.setObjectName(u"btnRadio_wpc_clienteFisico")
        self.btnRadio_wpc_clienteFisico.setMinimumSize(QSize(0, 0))

        self.gridLayout_14.addWidget(self.btnRadio_wpc_clienteFisico, 0, 1, 1, 1)

        self.btnRadio_wpc_clienteMoral = QRadioButton(self.contenedor_opcionesclientes)
        self.btnRadio_wpc_clienteMoral.setObjectName(u"btnRadio_wpc_clienteMoral")
        self.btnRadio_wpc_clienteMoral.setMinimumSize(QSize(0, 0))

        self.gridLayout_14.addWidget(self.btnRadio_wpc_clienteMoral, 0, 2, 1, 1)

        self.etiqueta_wpc_tipo_cliente = QLabel(self.contenedor_opcionesclientes)
        self.etiqueta_wpc_tipo_cliente.setObjectName(u"etiqueta_wpc_tipo_cliente")
        self.etiqueta_wpc_tipo_cliente.setMinimumSize(QSize(0, 0))

        self.gridLayout_14.addWidget(self.etiqueta_wpc_tipo_cliente, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.contenedor_opcionesclientes, 0, 0, 1, 1)

        self.wpc_buscar_clientes = QWidget(self.wpc_clientes_datos)
        self.wpc_buscar_clientes.setObjectName(u"wpc_buscar_clientes")
        self.gridLayout_12 = QGridLayout(self.wpc_buscar_clientes)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.etiqueta_titulo_tabla = QLabel(self.wpc_buscar_clientes)
        self.etiqueta_titulo_tabla.setObjectName(u"etiqueta_titulo_tabla")

        self.gridLayout_12.addWidget(self.etiqueta_titulo_tabla, 0, 0, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(1154, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_12.addItem(self.horizontalSpacer_6, 0, 1, 1, 1)

        self.btn_RefrescarTabla = QPushButton(self.wpc_buscar_clientes)
        self.btn_RefrescarTabla.setObjectName(u"btn_RefrescarTabla")
        self.btn_RefrescarTabla.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/Icons/IconosSVG/base_datos_refresh.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_RefrescarTabla.setIcon(icon1)

        self.gridLayout_12.addWidget(self.btn_RefrescarTabla, 0, 2, 1, 1)

        self.tabla_clientes = QTableView(self.wpc_buscar_clientes)
        self.tabla_clientes.setObjectName(u"tabla_clientes")
        self.tabla_clientes.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tabla_clientes.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tabla_clientes.setGridStyle(Qt.PenStyle.DashDotLine)
        self.tabla_clientes.horizontalHeader().setMinimumSectionSize(200)
        self.tabla_clientes.horizontalHeader().setDefaultSectionSize(200)
        self.tabla_clientes.horizontalHeader().setStretchLastSection(True)

        self.gridLayout_12.addWidget(self.tabla_clientes, 2, 0, 1, 3)

        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.etiqueta_iconobuscar = QLabel(self.wpc_buscar_clientes)
        self.etiqueta_iconobuscar.setObjectName(u"etiqueta_iconobuscar")

        self.gridLayout_8.addWidget(self.etiqueta_iconobuscar, 0, 0, 1, 1)

        self.txt_buscarcliente = QLineEdit(self.wpc_buscar_clientes)
        self.txt_buscarcliente.setObjectName(u"txt_buscarcliente")
        self.txt_buscarcliente.setClearButtonEnabled(True)

        self.gridLayout_8.addWidget(self.txt_buscarcliente, 0, 1, 1, 1)


        self.gridLayout_12.addLayout(self.gridLayout_8, 1, 0, 1, 3)


        self.gridLayout_4.addWidget(self.wpc_buscar_clientes, 2, 0, 1, 1)


        self.gridLayout_11.addWidget(self.wpc_clientes_datos, 0, 1, 1, 1)

        self.wpc_contenedor_scroll.setWidget(self.wpc_scrooll_area)

        self.gridLayout_19.addWidget(self.wpc_contenedor_scroll, 0, 0, 1, 1)


        self.gridLayout_9.addWidget(self.wpc_clientes_contenido, 2, 0, 1, 2)

        self.label_wp_titulo_clientes = QLabel(self.wpc_contenido_general)
        self.label_wp_titulo_clientes.setObjectName(u"label_wp_titulo_clientes")
        self.label_wp_titulo_clientes.setMinimumSize(QSize(0, 0))

        self.gridLayout_9.addWidget(self.label_wp_titulo_clientes, 0, 0, 1, 2)

        self.wpc_menu_opciones_clientes = QWidget(self.wpc_contenido_general)
        self.wpc_menu_opciones_clientes.setObjectName(u"wpc_menu_opciones_clientes")
        self.wpc_menu_opciones_clientes.setMinimumSize(QSize(0, 40))
        self.wpc_menu_opciones_clientes.setMaximumSize(QSize(16777215, 16777215))
        self.wpc_menu_opciones_clientes.setStyleSheet(u"")
        self.gridLayout_16 = QGridLayout(self.wpc_menu_opciones_clientes)
        self.gridLayout_16.setSpacing(0)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.gridLayout_16.setContentsMargins(4, 1, 4, 0)
        self.horizontalSpacer = QSpacerItem(768, 5, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_16.addItem(self.horizontalSpacer, 0, 1, 1, 1)

        self.wpc_contenedor_botones = QFrame(self.wpc_menu_opciones_clientes)
        self.wpc_contenedor_botones.setObjectName(u"wpc_contenedor_botones")
        self.gridLayout_10 = QGridLayout(self.wpc_contenedor_botones)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setHorizontalSpacing(10)
        self.gridLayout_10.setVerticalSpacing(0)
        self.gridLayout_10.setContentsMargins(10, 5, 10, 0)
        self.btn_btn_limpiarcampos = QPushButton(self.wpc_contenedor_botones)
        self.btn_btn_limpiarcampos.setObjectName(u"btn_btn_limpiarcampos")
        self.btn_btn_limpiarcampos.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/Icons/IconosSVG/borrador.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_btn_limpiarcampos.setIcon(icon2)
        self.btn_btn_limpiarcampos.setIconSize(QSize(20, 20))

        self.gridLayout_10.addWidget(self.btn_btn_limpiarcampos, 0, 4, 1, 1)

        self.btn_btn_cliente_eliminar = QPushButton(self.wpc_contenedor_botones)
        self.btn_btn_cliente_eliminar.setObjectName(u"btn_btn_cliente_eliminar")
        self.btn_btn_cliente_eliminar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/iconosBlancos/Icons/iconos/Blanco/eliminar_blanco.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_btn_cliente_eliminar.setIcon(icon3)
        self.btn_btn_cliente_eliminar.setIconSize(QSize(20, 20))

        self.gridLayout_10.addWidget(self.btn_btn_cliente_eliminar, 0, 1, 1, 1)

        self.btn_btn_cliente_agregar = QPushButton(self.wpc_contenedor_botones)
        self.btn_btn_cliente_agregar.setObjectName(u"btn_btn_cliente_agregar")
        self.btn_btn_cliente_agregar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/iconosBlancos/Icons/iconos/Blanco/guardar_blanco.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_btn_cliente_agregar.setIcon(icon4)
        self.btn_btn_cliente_agregar.setIconSize(QSize(20, 20))

        self.gridLayout_10.addWidget(self.btn_btn_cliente_agregar, 0, 0, 1, 1)

        self.btn_btn_cliente_modificar = QPushButton(self.wpc_contenedor_botones)
        self.btn_btn_cliente_modificar.setObjectName(u"btn_btn_cliente_modificar")
        self.btn_btn_cliente_modificar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u":/iconosBlancos/Icons/iconos/Blanco/actualizar_blanco.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_btn_cliente_modificar.setIcon(icon5)
        self.btn_btn_cliente_modificar.setIconSize(QSize(20, 20))

        self.gridLayout_10.addWidget(self.btn_btn_cliente_modificar, 0, 3, 1, 1)


        self.gridLayout_16.addWidget(self.wpc_contenedor_botones, 0, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)


        self.gridLayout_9.addWidget(self.wpc_menu_opciones_clientes, 1, 0, 1, 2)


        self.gridLayout_17.addWidget(self.wpc_contenido_general, 0, 0, 1, 1)

        QWidget.setTabOrder(self.btnRadio_wpc_clienteFisico, self.btnRadio_wpc_clienteMoral)
        QWidget.setTabOrder(self.btnRadio_wpc_clienteMoral, self.txt_nombre_fisico)
        QWidget.setTabOrder(self.txt_nombre_fisico, self.txt_apellidop_fisico)
        QWidget.setTabOrder(self.txt_apellidop_fisico, self.txt_apellidom_fisico)
        QWidget.setTabOrder(self.txt_apellidom_fisico, self.txt_rfc_fisico)
        QWidget.setTabOrder(self.txt_rfc_fisico, self.txt_pais_fisico)
        QWidget.setTabOrder(self.txt_pais_fisico, self.txt_estado_fisico)
        QWidget.setTabOrder(self.txt_estado_fisico, self.txt_curp_fisico)
        QWidget.setTabOrder(self.txt_curp_fisico, self.cajaDecimal_wpc_ingresosclienteFisico)
        QWidget.setTabOrder(self.cajaDecimal_wpc_ingresosclienteFisico, self.txt_correo_fisico)
        QWidget.setTabOrder(self.txt_correo_fisico, self.txt_telefono_fisico)
        QWidget.setTabOrder(self.txt_telefono_fisico, self.txt_avenidas_fisico)
        QWidget.setTabOrder(self.txt_avenidas_fisico, self.txt_calles_fisico)
        QWidget.setTabOrder(self.txt_calles_fisico, self.fecha_fechanacimiento)
        QWidget.setTabOrder(self.fecha_fechanacimiento, self.txt_ciudad_fisico)
        QWidget.setTabOrder(self.txt_ciudad_fisico, self.txt_codigopostal_fisico)
        QWidget.setTabOrder(self.txt_codigopostal_fisico, self.txt_ine_fisico)
        QWidget.setTabOrder(self.txt_ine_fisico, self.txt_ocupacion_fisico)
        QWidget.setTabOrder(self.txt_ocupacion_fisico, self.txtlargo_comentarioclientefisico)
        QWidget.setTabOrder(self.txtlargo_comentarioclientefisico, self.casillaverificacion_wpc_credito_autorizado)
        QWidget.setTabOrder(self.casillaverificacion_wpc_credito_autorizado, self.cajaDecimal_wpc_limite_credito)
        QWidget.setTabOrder(self.cajaDecimal_wpc_limite_credito, self.cajaDecimal_creditodisponible_fisico)
        QWidget.setTabOrder(self.cajaDecimal_creditodisponible_fisico, self.cajaDecimal_creditoutilizado_fisico)
        QWidget.setTabOrder(self.cajaDecimal_creditoutilizado_fisico, self.txt_estadodelcredito_fisico)
        QWidget.setTabOrder(self.txt_estadodelcredito_fisico, self.cajaDecimal_interesesaplicados_fisico)
        QWidget.setTabOrder(self.cajaDecimal_interesesaplicados_fisico, self.casillaverificacion_aplicadescuento_fisico)
        QWidget.setTabOrder(self.casillaverificacion_aplicadescuento_fisico, self.cajaDecimal_porcentajedescuento_fisico)
        QWidget.setTabOrder(self.cajaDecimal_porcentajedescuento_fisico, self.casillaverificacion_entidadlegalizada_fisico)
        QWidget.setTabOrder(self.casillaverificacion_entidadlegalizada_fisico, self.txt_nombre_empre_moral)
        QWidget.setTabOrder(self.txt_nombre_empre_moral, self.txt_razonsocial_moral)
        QWidget.setTabOrder(self.txt_razonsocial_moral, self.txt_correo_empre_moral)
        QWidget.setTabOrder(self.txt_correo_empre_moral, self.txt_avenidas_empre_moral)
        QWidget.setTabOrder(self.txt_avenidas_empre_moral, self.txt_rfc_empre_moral)
        QWidget.setTabOrder(self.txt_rfc_empre_moral, self.txt_pagina_empre_moral)
        QWidget.setTabOrder(self.txt_pagina_empre_moral, self.txt_pais_moral)
        QWidget.setTabOrder(self.txt_pais_moral, self.txt_ciudad_moral)
        QWidget.setTabOrder(self.txt_ciudad_moral, self.cajaOpciones_areasnegocio_moral)
        QWidget.setTabOrder(self.cajaOpciones_areasnegocio_moral, self.txt_telefono_empre_moral)
        QWidget.setTabOrder(self.txt_telefono_empre_moral, self.txt_nif_moral)
        QWidget.setTabOrder(self.txt_nif_moral, self.txt_calles_empre_moral)
        QWidget.setTabOrder(self.txt_calles_empre_moral, self.fecha_fechaconstitucion)
        QWidget.setTabOrder(self.fecha_fechaconstitucion, self.txt_sector_empre_moral)
        QWidget.setTabOrder(self.txt_sector_empre_moral, self.cajaOpciones_categoriaMoral)
        QWidget.setTabOrder(self.cajaOpciones_categoriaMoral, self.txt_estado_moral)
        QWidget.setTabOrder(self.txt_estado_moral, self.txt_codigopostal_moral)
        QWidget.setTabOrder(self.txt_codigopostal_moral, self.casillaverificacion_wpc_credito_autorizado_moral)
        QWidget.setTabOrder(self.casillaverificacion_wpc_credito_autorizado_moral, self.cajaDecimal_wpc_limite_credito_moral)
        QWidget.setTabOrder(self.cajaDecimal_wpc_limite_credito_moral, self.cajaDecimal_creditodisponible_moral)
        QWidget.setTabOrder(self.cajaDecimal_creditodisponible_moral, self.cajaDecimal_creditoutilizado_moral)
        QWidget.setTabOrder(self.cajaDecimal_creditoutilizado_moral, self.txt_estadocredito_moral)
        QWidget.setTabOrder(self.txt_estadocredito_moral, self.cajaDecimal_porcentajeintereses_moral)
        QWidget.setTabOrder(self.cajaDecimal_porcentajeintereses_moral, self.casillaverificacion_aplicadescuento_moral)
        QWidget.setTabOrder(self.casillaverificacion_aplicadescuento_moral, self.cajaDecimal_porcentajedescuento_moral)
        QWidget.setTabOrder(self.cajaDecimal_porcentajedescuento_moral, self.casillaverificacion_entidadlegalizada_moral)
        QWidget.setTabOrder(self.casillaverificacion_entidadlegalizada_moral, self.btn_btn_areasnegocio_moral)
        QWidget.setTabOrder(self.btn_btn_areasnegocio_moral, self.btn_btn_nuevacategoriaMoral)
        QWidget.setTabOrder(self.btn_btn_nuevacategoriaMoral, self.txtlargo_direccionadicional_moral)
        QWidget.setTabOrder(self.txtlargo_direccionadicional_moral, self.txt_nombre_repre_moral)
        QWidget.setTabOrder(self.txt_nombre_repre_moral, self.txt_telefono_repre_moral)
        QWidget.setTabOrder(self.txt_telefono_repre_moral, self.txt_puesto_repre_moral)
        QWidget.setTabOrder(self.txt_puesto_repre_moral, self.txt_correo_repre_moral)
        QWidget.setTabOrder(self.txt_correo_repre_moral, self.txt_buscarcliente)
        QWidget.setTabOrder(self.txt_buscarcliente, self.tabla_clientes)
        QWidget.setTabOrder(self.tabla_clientes, self.btn_btn_limpiarcampos)

        self.retranslateUi(Control_Clientes)

        self.wpc_contenedor_pila.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Control_Clientes)
    # setupUi

    def retranslateUi(self, Control_Clientes):
        Control_Clientes.setWindowTitle(QCoreApplication.translate("Control_Clientes", u"Form", None))
        self.etiqueta_ciudad_fisico.setText(QCoreApplication.translate("Control_Clientes", u"Ciudad", None))
        self.cajaDecimal_wpc_ingresosclienteFisico.setPrefix(QCoreApplication.translate("Control_Clientes", u"$ ", None))
        self.cajaDecimal_wpc_ingresosclienteFisico.setSuffix("")
        self.cajaOpciones_categoriaFisico.setItemText(0, QCoreApplication.translate("Control_Clientes", u"Sin Clasificaci\u00f3n", None))

#if QT_CONFIG(tooltip)
        self.btn_btn_nuevacategoriaFisico.setToolTip(QCoreApplication.translate("Control_Clientes", u"Agregar clasificaci\u00f3n", None))
#endif // QT_CONFIG(tooltip)
        self.btn_btn_nuevacategoriaFisico.setText("")
        self.etiqueta_area_negocio_fisico.setText(QCoreApplication.translate("Control_Clientes", u"Area de Negocio", None))
        self.etiqueta_wpc_comentarios_fisico.setText(QCoreApplication.translate("Control_Clientes", u"Comentarios", None))
        self.etiqueta_codigopostal_fisico.setText(QCoreApplication.translate("Control_Clientes", u"Codigo Postal", None))
        self.etiqueta_wpc_calles_fisico.setText(QCoreApplication.translate("Control_Clientes", u"Calle o entra calles", None))
        self.etiqueta_wpc_curp_fisico.setText(QCoreApplication.translate("Control_Clientes", u"CURP", None))
        self.etiqueta_wpc_ine_fisico.setText(QCoreApplication.translate("Control_Clientes", u"Num. INE", None))
        self.etiqueta_wpc_ocupacion_fisico.setText(QCoreApplication.translate("Control_Clientes", u"Ocupaci\u00f3n", None))
        self.etiqueta_wpc__telefono_fisico.setText(QCoreApplication.translate("Control_Clientes", u"Num. Telefono", None))
        self.etiqueta_wpc_nacimiento_fisico.setText(QCoreApplication.translate("Control_Clientes", u"Fecha Nacimiento", None))
        self.etiqueta_wpc_ingresos_fisico.setText(QCoreApplication.translate("Control_Clientes", u"Nivel de ingresos", None))
        self.etiqueta_rfc_fisico.setText(QCoreApplication.translate("Control_Clientes", u"RFC", None))
        self.etiqueta_wpc_apellidoM_fisico.setText(QCoreApplication.translate("Control_Clientes", u"Apellido Materno", None))
        self.etiqueta_wpc_nombre_fisico.setText(QCoreApplication.translate("Control_Clientes", u"Nombre", None))
        self.etiqueta_estado_fisico.setText(QCoreApplication.translate("Control_Clientes", u"Estado", None))
        self.cajaOpciones_areasnegocio_fisico.setItemText(0, QCoreApplication.translate("Control_Clientes", u"Sin \u00c1rea", None))

#if QT_CONFIG(tooltip)
        self.btn_btn_nuevaareanegocio_fisico.setToolTip(QCoreApplication.translate("Control_Clientes", u"Agregar \u00e1rea", None))
#endif // QT_CONFIG(tooltip)
        self.btn_btn_nuevaareanegocio_fisico.setText("")
        self.etiqueta_direccionadicional_fisico.setText(QCoreApplication.translate("Control_Clientes", u"Direcci\u00f3n Adicional", None))
        self.etiqueta_wpc_estadocivil_fisico.setText(QCoreApplication.translate("Control_Clientes", u"Estado Civil", None))
        self.etiqueta_wpc_avenidas_fisico.setText(QCoreApplication.translate("Control_Clientes", u"Avenida o entre avenidas", None))
        self.etiqueta_wpc_correo_fisico.setText(QCoreApplication.translate("Control_Clientes", u"Correo Electronico", None))
        self.cajaOpciones_estadocivil_fisico.setItemText(0, QCoreApplication.translate("Control_Clientes", u"Soltero/a", None))
        self.cajaOpciones_estadocivil_fisico.setItemText(1, QCoreApplication.translate("Control_Clientes", u"Casado/a", None))
        self.cajaOpciones_estadocivil_fisico.setItemText(2, QCoreApplication.translate("Control_Clientes", u"Viudo/a", None))
        self.cajaOpciones_estadocivil_fisico.setItemText(3, QCoreApplication.translate("Control_Clientes", u"Union Libre", None))
        self.cajaOpciones_estadocivil_fisico.setItemText(4, QCoreApplication.translate("Control_Clientes", u"Divorciado/a", None))

        self.etiqueta_pais_fisico.setText(QCoreApplication.translate("Control_Clientes", u"Pais", None))
        self.etiqueta_wpc_ApellidoP_fisico.setText(QCoreApplication.translate("Control_Clientes", u"Apellido Paterno", None))
        self.etiqueta_categoriaFisico.setText(QCoreApplication.translate("Control_Clientes", u"Clasificaci\u00f3n Cliente", None))
        self.label_wpc_fotocliente.setText(QCoreApplication.translate("Control_Clientes", u"<html><head/><body><p align=\"center\"><img src=\":/Icons/IconosSVG/subir_imagen.png\" width=\"90\" height=\"80\"/></p><p align=\"center\"><span style=\" font-size:16pt; font-weight:bold;font-family:Arial;\">Cargar Imagen</span></p></body></html>", None))
        self.casillaverificacion_wpc_credito_autorizado.setText(QCoreApplication.translate("Control_Clientes", u"Autoriza cr\u00e9dito", None))
        self.etiqueta_wpc_limitecredito.setText(QCoreApplication.translate("Control_Clientes", u"Limite:", None))
#if QT_CONFIG(tooltip)
        self.cajaDecimal_wpc_limite_credito.setToolTip(QCoreApplication.translate("Control_Clientes", u"Limite de cr\u00e9dito", None))
#endif // QT_CONFIG(tooltip)
        self.cajaDecimal_wpc_limite_credito.setPrefix(QCoreApplication.translate("Control_Clientes", u"$ ", None))
        self.etiqueta_creditodisponible_fisico.setText(QCoreApplication.translate("Control_Clientes", u"Disponible:", None))
#if QT_CONFIG(tooltip)
        self.cajaDecimal_creditodisponible_fisico.setToolTip(QCoreApplication.translate("Control_Clientes", u"Cr\u00e9dito disponible", None))
#endif // QT_CONFIG(tooltip)
        self.cajaDecimal_creditodisponible_fisico.setPrefix(QCoreApplication.translate("Control_Clientes", u"$ ", None))
        self.etiqueta_creditoutilizado_fisico.setText(QCoreApplication.translate("Control_Clientes", u"Utilizado:", None))
#if QT_CONFIG(tooltip)
        self.cajaDecimal_creditoutilizado_fisico.setToolTip(QCoreApplication.translate("Control_Clientes", u"Cr\u00e9dito utilizado", None))
#endif // QT_CONFIG(tooltip)
        self.cajaDecimal_creditoutilizado_fisico.setPrefix(QCoreApplication.translate("Control_Clientes", u"$ ", None))
        self.etiqueta_estadodelcredito_fisico.setText(QCoreApplication.translate("Control_Clientes", u"Estado del Cr\u00e9dito", None))
        self.etiqueta_porcentajeintereses_fisico.setText(QCoreApplication.translate("Control_Clientes", u"% Interes:", None))
#if QT_CONFIG(tooltip)
        self.cajaDecimal_interesesaplicados_fisico.setToolTip(QCoreApplication.translate("Control_Clientes", u"Interes sobre la deuda", None))
#endif // QT_CONFIG(tooltip)
        self.cajaDecimal_interesesaplicados_fisico.setSuffix(QCoreApplication.translate("Control_Clientes", u" %", None))
#if QT_CONFIG(tooltip)
        self.casillaverificacion_aplicadescuento_fisico.setToolTip(QCoreApplication.translate("Control_Clientes", u"Descuento sobre la compra", None))
#endif // QT_CONFIG(tooltip)
        self.casillaverificacion_aplicadescuento_fisico.setText(QCoreApplication.translate("Control_Clientes", u"Aplica descuento", None))
        self.etiqueta_porcentajedescuento_fisico.setText(QCoreApplication.translate("Control_Clientes", u"% Descuento", None))
#if QT_CONFIG(tooltip)
        self.cajaDecimal_porcentajedescuento_fisico.setToolTip(QCoreApplication.translate("Control_Clientes", u"Descuento sobre la compra", None))
#endif // QT_CONFIG(tooltip)
        self.cajaDecimal_porcentajedescuento_fisico.setSuffix(QCoreApplication.translate("Control_Clientes", u" %", None))
        self.etiqueta_entidadlegalizada_fisico.setText(QCoreApplication.translate("Control_Clientes", u"Entidad Legalizada:", None))
        self.casillaverificacion_entidadlegalizada_fisico.setText(QCoreApplication.translate("Control_Clientes", u"Si", None))
        self.etiqueta_fechaultimoreporte_fisico.setText(QCoreApplication.translate("Control_Clientes", u"\u00daltimo reporte:", None))
        self.casillaverificacion_wpc_credito_autorizado_moral.setText(QCoreApplication.translate("Control_Clientes", u"Autoriza cr\u00e9dito", None))
        self.etiqueta_wpc_limitecredito_moral.setText(QCoreApplication.translate("Control_Clientes", u"Limite", None))
#if QT_CONFIG(tooltip)
        self.cajaDecimal_wpc_limite_credito_moral.setToolTip(QCoreApplication.translate("Control_Clientes", u"Limite de cr\u00e9dito", None))
#endif // QT_CONFIG(tooltip)
        self.cajaDecimal_wpc_limite_credito_moral.setPrefix(QCoreApplication.translate("Control_Clientes", u"$ ", None))
        self.etiqueta_entidadlegalizada_moral.setText(QCoreApplication.translate("Control_Clientes", u"Entidad Legalizada:", None))
        self.casillaverificacion_entidadlegalizada_moral.setText(QCoreApplication.translate("Control_Clientes", u"Si", None))
        self.etiqueta_estadocredito_moral.setText(QCoreApplication.translate("Control_Clientes", u"Estado del Cr\u00e9dito", None))
        self.etiqueta_creditodisponible_moral.setText(QCoreApplication.translate("Control_Clientes", u"Disponible", None))
#if QT_CONFIG(tooltip)
        self.cajaDecimal_creditodisponible_moral.setToolTip(QCoreApplication.translate("Control_Clientes", u"Cr\u00e9dito disponible", None))
#endif // QT_CONFIG(tooltip)
        self.cajaDecimal_creditodisponible_moral.setPrefix(QCoreApplication.translate("Control_Clientes", u"$ ", None))
        self.etiqueta_creditoutilizado_moral.setText(QCoreApplication.translate("Control_Clientes", u"Utilizado", None))
#if QT_CONFIG(tooltip)
        self.cajaDecimal_creditoutilizado_moral.setToolTip(QCoreApplication.translate("Control_Clientes", u"Cr\u00e9dito utilizado", None))
#endif // QT_CONFIG(tooltip)
        self.cajaDecimal_creditoutilizado_moral.setPrefix(QCoreApplication.translate("Control_Clientes", u"$ ", None))
        self.etiqueta_porcentajeintereses_moral.setText(QCoreApplication.translate("Control_Clientes", u"% Interes:", None))
#if QT_CONFIG(tooltip)
        self.cajaDecimal_porcentajeintereses_moral.setToolTip(QCoreApplication.translate("Control_Clientes", u"Interes sobre la deuda", None))
#endif // QT_CONFIG(tooltip)
        self.cajaDecimal_porcentajeintereses_moral.setPrefix("")
        self.cajaDecimal_porcentajeintereses_moral.setSuffix(QCoreApplication.translate("Control_Clientes", u" %", None))
#if QT_CONFIG(tooltip)
        self.casillaverificacion_aplicadescuento_moral.setToolTip(QCoreApplication.translate("Control_Clientes", u"Descuento sobre la compra", None))
#endif // QT_CONFIG(tooltip)
        self.casillaverificacion_aplicadescuento_moral.setText(QCoreApplication.translate("Control_Clientes", u"Aplica descuento", None))
        self.etiqueta_porcentajedescuento_moral.setText(QCoreApplication.translate("Control_Clientes", u"% Descuento", None))
#if QT_CONFIG(tooltip)
        self.cajaDecimal_porcentajedescuento_moral.setToolTip(QCoreApplication.translate("Control_Clientes", u"Descuentos sobre las compras", None))
#endif // QT_CONFIG(tooltip)
        self.cajaDecimal_porcentajedescuento_moral.setSuffix(QCoreApplication.translate("Control_Clientes", u" %", None))
        self.etiqueta_ultimoreporte_moral.setText(QCoreApplication.translate("Control_Clientes", u"\u00daltimo reporte:", None))
        self.etiqueta_wpc_rfc_moral.setText(QCoreApplication.translate("Control_Clientes", u"RFC", None))
#if QT_CONFIG(tooltip)
        self.btn_btn_nuevacategoriaMoral.setToolTip(QCoreApplication.translate("Control_Clientes", u"Agregar clasificaci\u00f3n", None))
#endif // QT_CONFIG(tooltip)
        self.btn_btn_nuevacategoriaMoral.setText("")
        self.cajaOpciones_categoriaMoral.setItemText(0, QCoreApplication.translate("Control_Clientes", u"Sin Clasificaci\u00f3n", None))

#if QT_CONFIG(tooltip)
        self.btn_btn_areasnegocio_moral.setToolTip(QCoreApplication.translate("Control_Clientes", u"Agregar \u00e1rea", None))
#endif // QT_CONFIG(tooltip)
        self.btn_btn_areasnegocio_moral.setText("")
        self.cajaOpciones_areasnegocio_moral.setItemText(0, QCoreApplication.translate("Control_Clientes", u"Sin \u00c1rea", None))

        self.etiqueta_wpc_fechaconst_moral.setText(QCoreApplication.translate("Control_Clientes", u"Fecha de constituci\u00f3n", None))
        self.etiqueta_estado_moral.setText(QCoreApplication.translate("Control_Clientes", u"Estado", None))
        self.etiqueta_wpc_sector_moral.setText(QCoreApplication.translate("Control_Clientes", u"Sector", None))
        self.etiqueta_wpc_pagina_moral.setText(QCoreApplication.translate("Control_Clientes", u"Pagina web", None))
        self.etiqueta_wpc_puesto_representante_moral.setText(QCoreApplication.translate("Control_Clientes", u"Puesto", None))
        self.etiqueta_nif_moral.setText(QCoreApplication.translate("Control_Clientes", u"NIF", None))
        self.etiqueta_wpc_representante_moral.setText(QCoreApplication.translate("Control_Clientes", u"Nombre representante", None))
        self.etiqueta_codigopostal_moral.setText(QCoreApplication.translate("Control_Clientes", u"Codigo Postal", None))
        self.etiqueta_comentarios_cliente_moral.setText(QCoreApplication.translate("Control_Clientes", u"Comentarios", None))
        self.etiqueta_wpc_telefono_moral.setText(QCoreApplication.translate("Control_Clientes", u"Num. Telefono", None))
        self.etiqueta_pais_moral.setText(QCoreApplication.translate("Control_Clientes", u"Pais", None))
        self.etiqueta_areanegocio_moral.setText(QCoreApplication.translate("Control_Clientes", u"Area de Negocio", None))
        self.etiqueta_categoriaMoral.setText(QCoreApplication.translate("Control_Clientes", u"Clasificaci\u00f3n Cliente", None))
        self.etiqueta_razonsocial_moral.setText(QCoreApplication.translate("Control_Clientes", u"Raz\u00f3n Social", None))
        self.etiqueta_wpc_nombre_moral.setText(QCoreApplication.translate("Control_Clientes", u"Nombre", None))
        self.etiqueta_ciudad_moral.setText(QCoreApplication.translate("Control_Clientes", u"Ciudad", None))
        self.etiqueta_wpc_telefono_representante_moral.setText(QCoreApplication.translate("Control_Clientes", u"Telefono", None))
        self.etiqueta_wpc_correo_moral.setText(QCoreApplication.translate("Control_Clientes", u"Correo Electronico", None))
        self.etiqueta_wpc_calles_moral.setText(QCoreApplication.translate("Control_Clientes", u"Calle o entra calles", None))
        self.etiqueta_wpc_avenidas_moral.setText(QCoreApplication.translate("Control_Clientes", u"Avenida o entre avenidas", None))
        self.etiqueta_direccionadicional_moral.setText(QCoreApplication.translate("Control_Clientes", u"Direcci\u00f3 Adicional", None))
        self.etiqueta_wpc_correo_repre_moral.setText(QCoreApplication.translate("Control_Clientes", u"Correo electronico", None))
        self.btnRadio_wpc_clienteFisico.setText(QCoreApplication.translate("Control_Clientes", u"Fisico", None))
        self.btnRadio_wpc_clienteMoral.setText(QCoreApplication.translate("Control_Clientes", u"Moral", None))
        self.etiqueta_wpc_tipo_cliente.setText(QCoreApplication.translate("Control_Clientes", u"Tipo de cliente", None))
        self.etiqueta_titulo_tabla.setText(QCoreApplication.translate("Control_Clientes", u"LISTADO DE CLIENTES", None))
#if QT_CONFIG(tooltip)
        self.btn_RefrescarTabla.setToolTip(QCoreApplication.translate("Control_Clientes", u"Actualizar tabla", None))
#endif // QT_CONFIG(tooltip)
        self.btn_RefrescarTabla.setText("")
        self.etiqueta_iconobuscar.setText("")
        self.txt_buscarcliente.setPlaceholderText(QCoreApplication.translate("Control_Clientes", u"Nombre del cliente", None))
        self.label_wp_titulo_clientes.setText(QCoreApplication.translate("Control_Clientes", u"ADMINISTRACI\u00d3N DE CLIENTES", None))
#if QT_CONFIG(tooltip)
        self.btn_btn_limpiarcampos.setToolTip(QCoreApplication.translate("Control_Clientes", u"Limpiar campos", None))
#endif // QT_CONFIG(tooltip)
        self.btn_btn_limpiarcampos.setText("")
#if QT_CONFIG(tooltip)
        self.btn_btn_cliente_eliminar.setToolTip(QCoreApplication.translate("Control_Clientes", u"Eliminar cliente", None))
#endif // QT_CONFIG(tooltip)
        self.btn_btn_cliente_eliminar.setText(QCoreApplication.translate("Control_Clientes", u"Eliminar", None))
#if QT_CONFIG(tooltip)
        self.btn_btn_cliente_agregar.setToolTip(QCoreApplication.translate("Control_Clientes", u"Agregar cliente", None))
#endif // QT_CONFIG(tooltip)
        self.btn_btn_cliente_agregar.setText(QCoreApplication.translate("Control_Clientes", u"Agregar", None))
#if QT_CONFIG(tooltip)
        self.btn_btn_cliente_modificar.setToolTip(QCoreApplication.translate("Control_Clientes", u"Actualizar cliente", None))
#endif // QT_CONFIG(tooltip)
        self.btn_btn_cliente_modificar.setText(QCoreApplication.translate("Control_Clientes", u"Actualizar", None))
    # retranslateUi

