# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UI_REGISTRO_EMPLEADO.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateEdit,
    QFormLayout, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QPlainTextEdit, QPushButton,
    QSizePolicy, QSpacerItem, QToolButton, QVBoxLayout,
    QWidget)
import ibootstrap_rc
import iconsdvg_rc
import iconosSVG_rc

class Ui_RegistroAdministrador(object):
    def setupUi(self, RegistroAdministrador):
        if not RegistroAdministrador.objectName():
            RegistroAdministrador.setObjectName(u"RegistroAdministrador")
        RegistroAdministrador.resize(1192, 764)
        RegistroAdministrador.setStyleSheet(u"*{\n"
"color: black;\n"
"}\n"
"#frame{border:none;}\n"
"#widget_contenedor{border-radius: 10px;}\n"
"#RegistroAdministrador{\n"
"background: #fffefb;\n"
"}\n"
"#logotipo_cabecera_ventana{\n"
"image: url(:/Icons/IconosSVG/logo_dev_rous_blanco.png);\n"
"min-width:85px;\n"
"}\n"
"#contenedor_baja{\n"
"background:#EE1D52;\n"
"border-radius:5px;\n"
"}\n"
"[objectName*=\"contenedor_\"]{\n"
"background: #fffefb;\n"
"}\n"
"#widget_cabecera_ventana{\n"
" background-color:#1F3A5F;;\n"
"	min-height: 30px;\n"
"}\n"
"#etiqueta_status_empleado{\n"
"font-size: 18px;\n"
"background: #68a67d;\n"
"color: #1d1c1c;\n"
"margin: 0px;\n"
"padding: 2px 5px;\n"
"border-radius: 4px;\n"
"text-transform: uppercase;\n"
"}\n"
"[objectName^=\"btc\"]{\n"
"background-color: rgb(255, 255, 255);\n"
"	border: none;\n"
"	border-radius: 9px;\n"
"	max-width:20px;\n"
"	max-height:20px;\n"
"	min-width:20px;\n"
"	min-height:20px;\n"
"}\n"
"[objectName^=\"btc\"]:hover{\n"
"	background-color: rgb(214, 214, 214);\n"
"}\n"
"#btc_cerrar::hover{\n"
"	backgr"
                        "ound-color: rgb(255, 0, 0);\n"
"}\n"
"\n"
"#widget_contenedor{\n"
"	background-color: #fffefb;\n"
"}\n"
"\n"
"#opcion_usodelsistema{\n"
"	font-family: Arial;\n"
"	font-size: 14px;\n"
"	font-weight: bold;\n"
"}\n"
"[objectName^=\"etiquetaTitulo_\"]{\n"
"	font-family: Arial;\n"
"	font-size: 18px;\n"
"	font-weight: bold;\n"
"}\n"
"[objectName^=\"etiquetasubtitulo_\"]{\n"
"	font-family: Arial;\n"
"	font-size: 16px;\n"
"	font-weight: bold;\n"
"	max-height:30px;\n"
"	min-height:30px;\n"
"}\n"
"[objectName^=\"etiqueta_\"]{\n"
"	font-family: Arial;\n"
"	font-size: 14px;\n"
"	font-weight: bold;\n"
"}\n"
"[objectName^=\"txt_\"]{\n"
"	font-family: Arial;\n"
"	font-size: 14px;\n"
"	border:none;\n"
"border-radius: 4px;\n"
"	border-bottom: 1px solid #3b3c3d;\n"
"	background-color: #F5F5F5;\n"
"padding: 2px;\n"
"}\n"
"[objectName^=\"txt_\"]::focus{\n"
"border-bottom: 2px solid #00668c;\n"
"}\n"
"[objectName^=\"decimal_\"]{\n"
"border: none;\n"
"border-bottom: 1px solid #3b3c3d;\n"
"border-radius: 4px;\n"
"background-color: #"
                        "F5F5F5;\n"
"font-size: 14px;\n"
"padding: 2px;\n"
"}\n"
"[objectName^=\"decimal_\"]::focus{\n"
"border-bottom: 2px solid #00668c;\n"
"}\n"
"[objectName^=\"numero_\"]{\n"
"border: none;\n"
"border-bottom: 1px solid #3b3c3d;\n"
"border-radius: 4px;\n"
"background-color: #F5F5F5;\n"
"font-size: 14px;\n"
"padding: 2px;\n"
"}\n"
"[objectName^=\"numero_\"]::focus{\n"
"border-bottom: 2px solid #00668c;\n"
"}\n"
"[objectName^=\"opcion_\"]{\n"
"font-size: 14px;\n"
"font-family:Arial;\n"
"font-weight:bold;\n"
"}\n"
"\n"
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
"/* ES"
                        "TILO DE LOS \u00cdTEMS */\n"
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
"\n"
"\n"
"[objectName^=\"txtlargo_\"]{\n"
"	font-family: Arial;\n"
"	font-size: 14px;\n"
"	max-height: 100px;\n"
"	min-height: 100px;\n"
"border-radius: 4px;\n"
"background-color: #F5F5F5;\n"
"border: 1px solid #787878;\n"
"}\n"
"[objectName*=\"fecha_\"]{\n"
"border: none;\n"
"border-bottom: 1px solid #3b3c3d;\n"
"border-radius: 5px"
                        ";\n"
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
"#fecha_baja{\n"
"background: transparent;\n"
"color:#fffefb;\n"
"border:none;\n"
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
""
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
"QCalendarWidget QAbstractItemView::item:hover {\n"
"    background-color: #e1f0f7;\n"
"    color: #1d1c1c;\n"
"}\n"
"\n"
"[objectName^=\"Button\"]{\n"
"	font-family: Arial;\n"
"	font-size: 14px;\n"
"	font-weight:bold;\n"
"color: #ff"
                        "fefb;\n"
"background: #00619a;\n"
"border:none;\n"
"border-radius:5px;\n"
"height:25px;\n"
"padding: 0px 3px;\n"
"}\n"
"[objectName^=\"Button\"]:hover{\n"
"background: #2196F3;\n"
"}\n"
"#Button_aceptar{\n"
"	border: none;\n"
"	border-radius: 5px;\n"
"	min-width: 45px;\n"
"	width: 70px;\n"
"	min-height: 30px;\n"
"	height: 30px;\n"
"	background-color: #00619a;\n"
"}\n"
"#Button_aceptar:hover{\n"
"	background-color: #68a67d;\n"
"}\n"
"#Button_cancelar{\n"
"	border: none;\n"
"	border-radius: 5px;	\n"
"	min-width: 45px;\n"
"	width: 70px;\n"
"	min-height: 30px;\n"
"	height: 30px;\n"
"	background-color: #00619a;	\n"
"}\n"
"#Button_cancelar:hover{\n"
"	background-color: #EE1D52;\n"
"}\n"
"#Button_actualizar{\n"
"	border: none;\n"
"	border-radius: 5px;\n"
"	min-width: 45px;\n"
"	width: 70px;\n"
"	min-height: 33px;\n"
"	height: 30px;\n"
"	background-color: #00619a;\n"
"}\n"
"#Button_actualizar:hover{\n"
"	background-color: #2196F3;\n"
"}\n"
"#btn_btn_bajapersona{\n"
"	border: none;\n"
"	padding: 2px 5px;\n"
"	border-ra"
                        "dius: 5px;	\n"
"	background-color: #00619a;	\n"
"	text-transform: uppercase;\n"
"	font-size: 14px;\n"
"	font-weight:bold;\n"
"	color:#fffefb;\n"
"}\n"
"#btn_btn_bajapersona:hover{\n"
"	background-color: #EE1D52;\n"
"}\n"
"#btn_btn_recontratar{\n"
"	border: none;\n"
"	padding: 2px 5px;\n"
"	border-radius: 5px;	\n"
"	background-color: #00619a;	\n"
"	text-transform: uppercase;\n"
"	font-size: 14px;\n"
"	font-weight:bold;\n"
"	color:#fffefb;\n"
"}\n"
"#btn_btn_recontratar:hover{\n"
"	background-color: #68a67d;\n"
"}\n"
"#foto_usuario{\n"
"	min-height: 180px;\n"
"	min-width: 180px;\n"
"	max-height: 180px;\n"
"	max-width: 180px;\n"
"	height: 180px;\n"
"	width: 180px;\n"
"background-color: #F5F5F5;\n"
"border: 1px solid #1f3a5f;\n"
"}\n"
"[objectName^=\"fecha_\"]{\n"
"border: none;\n"
"border-bottom: 1px solid #3b3c3d;\n"
"border-radius: 5px;\n"
"padding: 2px;\n"
"background-color: #f5f4f1;\n"
"font-size: 12px;\n"
"width:87px;\n"
"}\n"
"*[objectName^=\"fecha_\"]::drop-down{\n"
"subcontrol-origin: padding;\n"
"subcont"
                        "rol-position: top right;\n"
"padding-right:5px;\n"
"width: 20%;\n"
"border-left-width: 1px;\n"
"border-radius: 5px;\n"
"background-color: #f5f4f1;\n"
"}\n"
"*[objectName^=\"fecha_\"]::down-arrow{\n"
"image: url(:/Icons/Bootstrap/calendar2-date.svg);\n"
"width: 17%;\n"
"height: 17%;\n"
"padding-left:5px;\n"
"padding-right:5px;\n"
"}\n"
"*[objectName^=\"fecha_\"]::focus{\n"
"border-bottom: 2px solid #00668c;\n"
"}\n"
"[objectName*=\"tiempo_\"]{\n"
"background-color: rgb(245, 244, 241);\n"
"color: rgb(29, 28, 28);\n"
"border: none;\n"
"border-bottom: 1px solid;\n"
"border-radius: 5px;\n"
"font-size: 12px;\n"
"font-family: Arial;\n"
"}\n"
"[objectName^=\"tiempo_\"]::focus{\n"
"border-bottom: 2px solid #00668c;\n"
"}\n"
"")
        self.verticalLayout = QVBoxLayout(RegistroAdministrador)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_contenedor = QWidget(RegistroAdministrador)
        self.widget_contenedor.setObjectName(u"widget_contenedor")
        self.widget_contenedor.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(self.widget_contenedor)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget_cabecera_ventana = QWidget(self.widget_contenedor)
        self.widget_cabecera_ventana.setObjectName(u"widget_cabecera_ventana")
        self.widget_cabecera_ventana.setMinimumSize(QSize(0, 30))
        self.widget_cabecera_ventana.setMaximumSize(QSize(16777215, 16777215))
        self.widget_cabecera_ventana.setStyleSheet(u"")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_cabecera_ventana)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.widget_cabecera_ventana)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.widget_2)
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(5, 0, 5, 0)
        self.logotipo_cabecera_ventana = QLabel(self.widget_2)
        self.logotipo_cabecera_ventana.setObjectName(u"logotipo_cabecera_ventana")

        self.horizontalLayout.addWidget(self.logotipo_cabecera_ventana)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btc_minimizar = QPushButton(self.widget_2)
        self.btc_minimizar.setObjectName(u"btc_minimizar")
        self.btc_minimizar.setMinimumSize(QSize(20, 20))
        self.btc_minimizar.setMaximumSize(QSize(20, 20))
        self.btc_minimizar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btc_minimizar.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/Icons/Bootstrap/arrows-angle-contract.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btc_minimizar.setIcon(icon)
        self.btc_minimizar.setIconSize(QSize(20, 15))

        self.horizontalLayout.addWidget(self.btc_minimizar)

        self.btc_maximizar = QPushButton(self.widget_2)
        self.btc_maximizar.setObjectName(u"btc_maximizar")
        self.btc_maximizar.setMinimumSize(QSize(20, 20))
        self.btc_maximizar.setMaximumSize(QSize(20, 20))
        self.btc_maximizar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/Icons/Bootstrap/arrows-angle-expand.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btc_maximizar.setIcon(icon1)
        self.btc_maximizar.setIconSize(QSize(20, 15))

        self.horizontalLayout.addWidget(self.btc_maximizar)

        self.btc_cerrar = QPushButton(self.widget_2)
        self.btc_cerrar.setObjectName(u"btc_cerrar")
        self.btc_cerrar.setMinimumSize(QSize(20, 20))
        self.btc_cerrar.setMaximumSize(QSize(20, 20))
        self.btc_cerrar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/Icons/Bootstrap/x-lg.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btc_cerrar.setIcon(icon2)
        self.btc_cerrar.setIconSize(QSize(20, 15))

        self.horizontalLayout.addWidget(self.btc_cerrar)


        self.horizontalLayout_2.addWidget(self.widget_2)


        self.verticalLayout_2.addWidget(self.widget_cabecera_ventana)

        self.contenedor_general = QWidget(self.widget_contenedor)
        self.contenedor_general.setObjectName(u"contenedor_general")
        self.gridLayout_4 = QGridLayout(self.contenedor_general)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.btn_btn_bajapersona = QPushButton(self.contenedor_general)
        self.btn_btn_bajapersona.setObjectName(u"btn_btn_bajapersona")
        self.btn_btn_bajapersona.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/iconosBlancos/Icons/iconos/Blanco/eliminar_persona_blanco.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_btn_bajapersona.setIcon(icon3)

        self.gridLayout_4.addWidget(self.btn_btn_bajapersona, 0, 6, 1, 1, Qt.AlignmentFlag.AlignRight)

        self.etiqueta_status_empleado = QLabel(self.contenedor_general)
        self.etiqueta_status_empleado.setObjectName(u"etiqueta_status_empleado")

        self.gridLayout_4.addWidget(self.etiqueta_status_empleado, 0, 7, 1, 1, Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignVCenter)

        self.contenedor_datosderecha = QWidget(self.contenedor_general)
        self.contenedor_datosderecha.setObjectName(u"contenedor_datosderecha")
        self.contenedor_datosderecha.setMaximumSize(QSize(200, 16777215))
        self.gridLayout_3 = QGridLayout(self.contenedor_datosderecha)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.etiqueta_rol_usuario = QLabel(self.contenedor_datosderecha)
        self.etiqueta_rol_usuario.setObjectName(u"etiqueta_rol_usuario")

        self.gridLayout_3.addWidget(self.etiqueta_rol_usuario, 8, 0, 1, 1)

        self.etiqueta_departamento = QLabel(self.contenedor_datosderecha)
        self.etiqueta_departamento.setObjectName(u"etiqueta_departamento")

        self.gridLayout_3.addWidget(self.etiqueta_departamento, 4, 0, 1, 1)

        self.etiqueta_puesto = QLabel(self.contenedor_datosderecha)
        self.etiqueta_puesto.setObjectName(u"etiqueta_puesto")

        self.gridLayout_3.addWidget(self.etiqueta_puesto, 6, 0, 1, 1)

        self.cajaOpciones_departamentos = QComboBox(self.contenedor_datosderecha)
        self.cajaOpciones_departamentos.setObjectName(u"cajaOpciones_departamentos")
        self.cajaOpciones_departamentos.setSizeAdjustPolicy(QComboBox.SizeAdjustPolicy.AdjustToContents)

        self.gridLayout_3.addWidget(self.cajaOpciones_departamentos, 5, 0, 1, 2)

        self.cajaOpciones_puestos = QComboBox(self.contenedor_datosderecha)
        self.cajaOpciones_puestos.setObjectName(u"cajaOpciones_puestos")
        self.cajaOpciones_puestos.setSizeAdjustPolicy(QComboBox.SizeAdjustPolicy.AdjustToContents)

        self.gridLayout_3.addWidget(self.cajaOpciones_puestos, 7, 0, 1, 2)

        self.etiqueta_sucursal = QLabel(self.contenedor_datosderecha)
        self.etiqueta_sucursal.setObjectName(u"etiqueta_sucursal")

        self.gridLayout_3.addWidget(self.etiqueta_sucursal, 1, 0, 1, 1)

        self.foto_usuario = QLabel(self.contenedor_datosderecha)
        self.foto_usuario.setObjectName(u"foto_usuario")
        self.foto_usuario.setMinimumSize(QSize(182, 182))
        self.foto_usuario.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.foto_usuario.setScaledContents(False)

        self.gridLayout_3.addWidget(self.foto_usuario, 0, 0, 1, 1)

        self.Button_nuevasucursal = QPushButton(self.contenedor_datosderecha)
        self.Button_nuevasucursal.setObjectName(u"Button_nuevasucursal")
        self.Button_nuevasucursal.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/iconosBlancos/Icons/iconos/Blanco/agregar_blanco.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Button_nuevasucursal.setIcon(icon4)
        self.Button_nuevasucursal.setIconSize(QSize(24, 24))

        self.gridLayout_3.addWidget(self.Button_nuevasucursal, 1, 1, 1, 1)

        self.cajaOpciones_sucursales = QComboBox(self.contenedor_datosderecha)
        self.cajaOpciones_sucursales.setObjectName(u"cajaOpciones_sucursales")
        self.cajaOpciones_sucursales.setSizeAdjustPolicy(QComboBox.SizeAdjustPolicy.AdjustToContents)

        self.gridLayout_3.addWidget(self.cajaOpciones_sucursales, 2, 0, 1, 2)

        self.Button_agregardepartamento = QPushButton(self.contenedor_datosderecha)
        self.Button_agregardepartamento.setObjectName(u"Button_agregardepartamento")
        self.Button_agregardepartamento.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.Button_agregardepartamento.setIcon(icon4)
        self.Button_agregardepartamento.setIconSize(QSize(24, 24))

        self.gridLayout_3.addWidget(self.Button_agregardepartamento, 4, 1, 1, 1)

        self.Button_agregarpuesto = QPushButton(self.contenedor_datosderecha)
        self.Button_agregarpuesto.setObjectName(u"Button_agregarpuesto")
        self.Button_agregarpuesto.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.Button_agregarpuesto.setIcon(icon4)
        self.Button_agregarpuesto.setIconSize(QSize(24, 24))

        self.gridLayout_3.addWidget(self.Button_agregarpuesto, 6, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 203, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer, 11, 0, 1, 2)

        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.etiqueta_fechadespido = QLabel(self.contenedor_datosderecha)
        self.etiqueta_fechadespido.setObjectName(u"etiqueta_fechadespido")

        self.gridLayout_9.addWidget(self.etiqueta_fechadespido, 2, 0, 1, 1)

        self.fecha_fechacontratacion = QDateEdit(self.contenedor_datosderecha)
        self.fecha_fechacontratacion.setObjectName(u"fecha_fechacontratacion")
        self.fecha_fechacontratacion.setCalendarPopup(True)

        self.gridLayout_9.addWidget(self.fecha_fechacontratacion, 1, 0, 1, 1)

        self.etiqueta_fechacontratacion = QLabel(self.contenedor_datosderecha)
        self.etiqueta_fechacontratacion.setObjectName(u"etiqueta_fechacontratacion")

        self.gridLayout_9.addWidget(self.etiqueta_fechacontratacion, 0, 0, 1, 1)

        self.fecha_fechadespido = QDateEdit(self.contenedor_datosderecha)
        self.fecha_fechadespido.setObjectName(u"fecha_fechadespido")
        self.fecha_fechadespido.setCalendarPopup(True)

        self.gridLayout_9.addWidget(self.fecha_fechadespido, 3, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_9, 10, 0, 1, 2)

        self.cajaOpciones_rol_usuario = QComboBox(self.contenedor_datosderecha)
        self.cajaOpciones_rol_usuario.setObjectName(u"cajaOpciones_rol_usuario")
        self.cajaOpciones_rol_usuario.setSizeAdjustPolicy(QComboBox.SizeAdjustPolicy.AdjustToContents)

        self.gridLayout_3.addWidget(self.cajaOpciones_rol_usuario, 9, 0, 1, 2)


        self.gridLayout_4.addWidget(self.contenedor_datosderecha, 2, 7, 1, 1)

        self.etiquetaTitulo_agregarpersona = QLabel(self.contenedor_general)
        self.etiquetaTitulo_agregarpersona.setObjectName(u"etiquetaTitulo_agregarpersona")
        self.etiquetaTitulo_agregarpersona.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.gridLayout_4.addWidget(self.etiquetaTitulo_agregarpersona, 0, 0, 1, 1)

        self.btn_btn_recontratar = QPushButton(self.contenedor_general)
        self.btn_btn_recontratar.setObjectName(u"btn_btn_recontratar")
        self.btn_btn_recontratar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u":/iconosBlancos/Icons/iconos/Blanco/mover.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_btn_recontratar.setIcon(icon5)

        self.gridLayout_4.addWidget(self.btn_btn_recontratar, 0, 5, 1, 1, Qt.AlignmentFlag.AlignRight)

        self.contenedor_datosizquierda = QWidget(self.contenedor_general)
        self.contenedor_datosizquierda.setObjectName(u"contenedor_datosizquierda")
        self.gridLayout_2 = QGridLayout(self.contenedor_datosizquierda)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.etiqueta_nombrecontactoemergencia = QLabel(self.contenedor_datosizquierda)
        self.etiqueta_nombrecontactoemergencia.setObjectName(u"etiqueta_nombrecontactoemergencia")

        self.gridLayout_7.addWidget(self.etiqueta_nombrecontactoemergencia, 0, 2, 1, 1)

        self.txt_nombrecontactoemergencia = QLineEdit(self.contenedor_datosizquierda)
        self.txt_nombrecontactoemergencia.setObjectName(u"txt_nombrecontactoemergencia")

        self.gridLayout_7.addWidget(self.txt_nombrecontactoemergencia, 0, 3, 1, 1)

        self.txt_contactoemergencia = QLineEdit(self.contenedor_datosizquierda)
        self.txt_contactoemergencia.setObjectName(u"txt_contactoemergencia")

        self.gridLayout_7.addWidget(self.txt_contactoemergencia, 0, 1, 1, 1)

        self.etiqueta_contactoemergencia = QLabel(self.contenedor_datosizquierda)
        self.etiqueta_contactoemergencia.setObjectName(u"etiqueta_contactoemergencia")

        self.gridLayout_7.addWidget(self.etiqueta_contactoemergencia, 0, 0, 1, 1)


        self.gridLayout_8.addLayout(self.gridLayout_7, 0, 0, 1, 1)

        self.formLayout_5 = QFormLayout()
        self.formLayout_5.setObjectName(u"formLayout_5")
        self.etiqueta_parentesco = QLabel(self.contenedor_datosizquierda)
        self.etiqueta_parentesco.setObjectName(u"etiqueta_parentesco")

        self.formLayout_5.setWidget(0, QFormLayout.ItemRole.LabelRole, self.etiqueta_parentesco)

        self.cajaOpciones_parentesco = QComboBox(self.contenedor_datosizquierda)
        self.cajaOpciones_parentesco.setObjectName(u"cajaOpciones_parentesco")
        self.cajaOpciones_parentesco.setSizeAdjustPolicy(QComboBox.SizeAdjustPolicy.AdjustToContents)

        self.formLayout_5.setWidget(0, QFormLayout.ItemRole.FieldRole, self.cajaOpciones_parentesco)


        self.gridLayout_8.addLayout(self.formLayout_5, 0, 1, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout_8, 4, 0, 1, 2)

        self.txtlargo_direccion_completa = QPlainTextEdit(self.contenedor_datosizquierda)
        self.txtlargo_direccion_completa.setObjectName(u"txtlargo_direccion_completa")
        self.txtlargo_direccion_completa.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.txtlargo_direccion_completa, 7, 0, 1, 2)

        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.etiqueta_nivelestudios = QLabel(self.contenedor_datosizquierda)
        self.etiqueta_nivelestudios.setObjectName(u"etiqueta_nivelestudios")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.etiqueta_nivelestudios)

        self.cajaOpciones_nivelacademico = QComboBox(self.contenedor_datosizquierda)
        self.cajaOpciones_nivelacademico.setObjectName(u"cajaOpciones_nivelacademico")
        self.cajaOpciones_nivelacademico.setSizeAdjustPolicy(QComboBox.SizeAdjustPolicy.AdjustToContents)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.cajaOpciones_nivelacademico)


        self.gridLayout_6.addLayout(self.formLayout, 0, 0, 1, 1)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.etiqueta_carrera = QLabel(self.contenedor_datosizquierda)
        self.etiqueta_carrera.setObjectName(u"etiqueta_carrera")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.LabelRole, self.etiqueta_carrera)

        self.txt_carrera = QLineEdit(self.contenedor_datosizquierda)
        self.txt_carrera.setObjectName(u"txt_carrera")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.FieldRole, self.txt_carrera)


        self.gridLayout_6.addLayout(self.formLayout_2, 0, 1, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout_6, 1, 0, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.txt_nexterior = QLineEdit(self.contenedor_datosizquierda)
        self.txt_nexterior.setObjectName(u"txt_nexterior")

        self.horizontalLayout_3.addWidget(self.txt_nexterior)

        self.txt_ninterior = QLineEdit(self.contenedor_datosizquierda)
        self.txt_ninterior.setObjectName(u"txt_ninterior")

        self.horizontalLayout_3.addWidget(self.txt_ninterior)

        self.txt_codigopostal = QLineEdit(self.contenedor_datosizquierda)
        self.txt_codigopostal.setObjectName(u"txt_codigopostal")
        self.txt_codigopostal.setClearButtonEnabled(False)

        self.horizontalLayout_3.addWidget(self.txt_codigopostal)


        self.horizontalLayout_6.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.txt_numerotelefono = QLineEdit(self.contenedor_datosizquierda)
        self.txt_numerotelefono.setObjectName(u"txt_numerotelefono")
        self.txt_numerotelefono.setClearButtonEnabled(False)

        self.horizontalLayout_5.addWidget(self.txt_numerotelefono)

        self.txt_correoelectronico = QLineEdit(self.contenedor_datosizquierda)
        self.txt_correoelectronico.setObjectName(u"txt_correoelectronico")
        self.txt_correoelectronico.setClearButtonEnabled(False)

        self.horizontalLayout_5.addWidget(self.txt_correoelectronico)


        self.horizontalLayout_6.addLayout(self.horizontalLayout_5)


        self.gridLayout_2.addLayout(self.horizontalLayout_6, 3, 0, 1, 2)

        self.etiquetasubtitulo_direccion = QLabel(self.contenedor_datosizquierda)
        self.etiquetasubtitulo_direccion.setObjectName(u"etiquetasubtitulo_direccion")
        self.etiquetasubtitulo_direccion.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.gridLayout_2.addWidget(self.etiquetasubtitulo_direccion, 6, 0, 1, 1)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.txt_nombre = QLineEdit(self.contenedor_datosizquierda)
        self.txt_nombre.setObjectName(u"txt_nombre")
        self.txt_nombre.setCursorMoveStyle(Qt.CursorMoveStyle.LogicalMoveStyle)
        self.txt_nombre.setClearButtonEnabled(False)

        self.gridLayout.addWidget(self.txt_nombre, 0, 0, 1, 1)

        self.txt_curp = QLineEdit(self.contenedor_datosizquierda)
        self.txt_curp.setObjectName(u"txt_curp")
        self.txt_curp.setClearButtonEnabled(False)

        self.gridLayout.addWidget(self.txt_curp, 0, 1, 1, 1)

        self.txt_apellidop = QLineEdit(self.contenedor_datosizquierda)
        self.txt_apellidop.setObjectName(u"txt_apellidop")
        self.txt_apellidop.setClearButtonEnabled(False)

        self.gridLayout.addWidget(self.txt_apellidop, 1, 0, 1, 1)

        self.txt_rfc = QLineEdit(self.contenedor_datosizquierda)
        self.txt_rfc.setObjectName(u"txt_rfc")
        self.txt_rfc.setClearButtonEnabled(False)

        self.gridLayout.addWidget(self.txt_rfc, 1, 1, 1, 1)

        self.txt_apellidom = QLineEdit(self.contenedor_datosizquierda)
        self.txt_apellidom.setObjectName(u"txt_apellidom")
        self.txt_apellidom.setClearButtonEnabled(False)

        self.gridLayout.addWidget(self.txt_apellidom, 2, 0, 1, 1)

        self.txt_numerosegurosicial = QLineEdit(self.contenedor_datosizquierda)
        self.txt_numerosegurosicial.setObjectName(u"txt_numerosegurosicial")
        self.txt_numerosegurosicial.setClearButtonEnabled(False)

        self.gridLayout.addWidget(self.txt_numerosegurosicial, 2, 1, 1, 1)


        self.gridLayout_5.addLayout(self.gridLayout, 0, 0, 2, 1)

        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.etiqueta_genero = QLabel(self.contenedor_datosizquierda)
        self.etiqueta_genero.setObjectName(u"etiqueta_genero")

        self.formLayout_3.setWidget(0, QFormLayout.ItemRole.LabelRole, self.etiqueta_genero)

        self.cajaOpciones_genero = QComboBox(self.contenedor_datosizquierda)
        self.cajaOpciones_genero.setObjectName(u"cajaOpciones_genero")

        self.formLayout_3.setWidget(0, QFormLayout.ItemRole.FieldRole, self.cajaOpciones_genero)

        self.etiqueta_estado_civil = QLabel(self.contenedor_datosizquierda)
        self.etiqueta_estado_civil.setObjectName(u"etiqueta_estado_civil")

        self.formLayout_3.setWidget(1, QFormLayout.ItemRole.LabelRole, self.etiqueta_estado_civil)

        self.cajaOpciones_estadocvil = QComboBox(self.contenedor_datosizquierda)
        self.cajaOpciones_estadocvil.setObjectName(u"cajaOpciones_estadocvil")
        self.cajaOpciones_estadocvil.setMinimumSize(QSize(204, 0))
        self.cajaOpciones_estadocvil.setSizeAdjustPolicy(QComboBox.SizeAdjustPolicy.AdjustToContents)

        self.formLayout_3.setWidget(1, QFormLayout.ItemRole.FieldRole, self.cajaOpciones_estadocvil)


        self.gridLayout_5.addLayout(self.formLayout_3, 0, 1, 1, 1)

        self.formLayout_4 = QFormLayout()
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.etiqueta_fecha_nacimiento = QLabel(self.contenedor_datosizquierda)
        self.etiqueta_fecha_nacimiento.setObjectName(u"etiqueta_fecha_nacimiento")
        self.etiqueta_fecha_nacimiento.setMaximumSize(QSize(150, 16777215))

        self.formLayout_4.setWidget(0, QFormLayout.ItemRole.LabelRole, self.etiqueta_fecha_nacimiento)

        self.fecha_fechanacimiento = QDateEdit(self.contenedor_datosizquierda)
        self.fecha_fechanacimiento.setObjectName(u"fecha_fechanacimiento")
        self.fecha_fechanacimiento.setMaximumSize(QSize(16777215, 16777215))
        self.fecha_fechanacimiento.setProperty(u"showGroupSeparator", False)
        self.fecha_fechanacimiento.setCalendarPopup(True)

        self.formLayout_4.setWidget(0, QFormLayout.ItemRole.FieldRole, self.fecha_fechanacimiento)


        self.gridLayout_5.addLayout(self.formLayout_4, 1, 1, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout_5, 0, 0, 1, 2)

        self.opcion_usodelsistema = QCheckBox(self.contenedor_datosizquierda)
        self.opcion_usodelsistema.setObjectName(u"opcion_usodelsistema")

        self.gridLayout_2.addWidget(self.opcion_usodelsistema, 8, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.txt_pais = QLineEdit(self.contenedor_datosizquierda)
        self.txt_pais.setObjectName(u"txt_pais")
        self.txt_pais.setClearButtonEnabled(False)

        self.horizontalLayout_4.addWidget(self.txt_pais)

        self.txt_estado = QLineEdit(self.contenedor_datosizquierda)
        self.txt_estado.setObjectName(u"txt_estado")
        self.txt_estado.setClearButtonEnabled(False)

        self.horizontalLayout_4.addWidget(self.txt_estado)

        self.txt_ciudad = QLineEdit(self.contenedor_datosizquierda)
        self.txt_ciudad.setObjectName(u"txt_ciudad")
        self.txt_ciudad.setClearButtonEnabled(False)

        self.horizontalLayout_4.addWidget(self.txt_ciudad)

        self.txt_colonia = QLineEdit(self.contenedor_datosizquierda)
        self.txt_colonia.setObjectName(u"txt_colonia")

        self.horizontalLayout_4.addWidget(self.txt_colonia)

        self.txt_avenidas = QLineEdit(self.contenedor_datosizquierda)
        self.txt_avenidas.setObjectName(u"txt_avenidas")

        self.horizontalLayout_4.addWidget(self.txt_avenidas)

        self.txt_calles = QLineEdit(self.contenedor_datosizquierda)
        self.txt_calles.setObjectName(u"txt_calles")

        self.horizontalLayout_4.addWidget(self.txt_calles)


        self.gridLayout_2.addLayout(self.horizontalLayout_4, 2, 0, 1, 2)

        self.contenedor_credencialesusuario = QFrame(self.contenedor_datosizquierda)
        self.contenedor_credencialesusuario.setObjectName(u"contenedor_credencialesusuario")
        self.contenedor_credencialesusuario.setFrameShape(QFrame.Shape.StyledPanel)
        self.contenedor_credencialesusuario.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_10 = QGridLayout(self.contenedor_credencialesusuario)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.Button_actualizarcredenciales = QPushButton(self.contenedor_credencialesusuario)
        self.Button_actualizarcredenciales.setObjectName(u"Button_actualizarcredenciales")
        self.Button_actualizarcredenciales.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout_10.addWidget(self.Button_actualizarcredenciales, 3, 1, 1, 1)

        self.etiquetasubtitulo_datos_uniciosesion = QLabel(self.contenedor_credencialesusuario)
        self.etiquetasubtitulo_datos_uniciosesion.setObjectName(u"etiquetasubtitulo_datos_uniciosesion")

        self.gridLayout_10.addWidget(self.etiquetasubtitulo_datos_uniciosesion, 0, 0, 1, 1)

        self.Button_eliminar_credenciales = QPushButton(self.contenedor_credencialesusuario)
        self.Button_eliminar_credenciales.setObjectName(u"Button_eliminar_credenciales")
        self.Button_eliminar_credenciales.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout_10.addWidget(self.Button_eliminar_credenciales, 3, 2, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_10.addItem(self.horizontalSpacer_2, 1, 4, 1, 1)

        self.txt_usuario_iniciosesion = QLineEdit(self.contenedor_credencialesusuario)
        self.txt_usuario_iniciosesion.setObjectName(u"txt_usuario_iniciosesion")
        self.txt_usuario_iniciosesion.setClearButtonEnabled(False)

        self.gridLayout_10.addWidget(self.txt_usuario_iniciosesion, 1, 0, 1, 1)

        self.opcion_actualizar_datoscredenciales = QCheckBox(self.contenedor_credencialesusuario)
        self.opcion_actualizar_datoscredenciales.setObjectName(u"opcion_actualizar_datoscredenciales")

        self.gridLayout_10.addWidget(self.opcion_actualizar_datoscredenciales, 1, 1, 1, 2)

        self.txt_contrasenia_usuario_iniciosesion = QLineEdit(self.contenedor_credencialesusuario)
        self.txt_contrasenia_usuario_iniciosesion.setObjectName(u"txt_contrasenia_usuario_iniciosesion")
        self.txt_contrasenia_usuario_iniciosesion.setEchoMode(QLineEdit.EchoMode.Password)
        self.txt_contrasenia_usuario_iniciosesion.setClearButtonEnabled(False)

        self.gridLayout_10.addWidget(self.txt_contrasenia_usuario_iniciosesion, 3, 0, 1, 1)

        self.Button_agregarUsuario = QPushButton(self.contenedor_credencialesusuario)
        self.Button_agregarUsuario.setObjectName(u"Button_agregarUsuario")
        self.Button_agregarUsuario.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout_10.addWidget(self.Button_agregarUsuario, 3, 3, 1, 1)


        self.gridLayout_2.addWidget(self.contenedor_credencialesusuario, 9, 0, 1, 2)

        self.frame = QFrame(self.contenedor_datosizquierda)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame)
        self.horizontalLayout_7.setSpacing(5)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.Button_actualizar = QPushButton(self.frame)
        self.Button_actualizar.setObjectName(u"Button_actualizar")
        self.Button_actualizar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_7.addWidget(self.Button_actualizar, 0, Qt.AlignmentFlag.AlignLeft)

        self.Button_aceptar = QToolButton(self.frame)
        self.Button_aceptar.setObjectName(u"Button_aceptar")
        self.Button_aceptar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_7.addWidget(self.Button_aceptar, 0, Qt.AlignmentFlag.AlignLeft)

        self.Button_cancelar = QToolButton(self.frame)
        self.Button_cancelar.setObjectName(u"Button_cancelar")
        self.Button_cancelar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_7.addWidget(self.Button_cancelar, 0, Qt.AlignmentFlag.AlignLeft)


        self.gridLayout_2.addWidget(self.frame, 11, 0, 1, 1, Qt.AlignmentFlag.AlignLeft)

        self.line_3 = QFrame(self.contenedor_datosizquierda)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_2.addWidget(self.line_3, 5, 0, 1, 2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 10, 0, 1, 1)


        self.gridLayout_4.addWidget(self.contenedor_datosizquierda, 2, 0, 1, 7)


        self.verticalLayout_2.addWidget(self.contenedor_general)


        self.verticalLayout.addWidget(self.widget_contenedor)

        QWidget.setTabOrder(self.txt_nombre, self.txt_apellidop)
        QWidget.setTabOrder(self.txt_apellidop, self.txt_apellidom)
        QWidget.setTabOrder(self.txt_apellidom, self.txt_curp)
        QWidget.setTabOrder(self.txt_curp, self.txt_rfc)
        QWidget.setTabOrder(self.txt_rfc, self.txt_numerosegurosicial)
        QWidget.setTabOrder(self.txt_numerosegurosicial, self.cajaOpciones_genero)
        QWidget.setTabOrder(self.cajaOpciones_genero, self.cajaOpciones_estadocvil)
        QWidget.setTabOrder(self.cajaOpciones_estadocvil, self.fecha_fechanacimiento)
        QWidget.setTabOrder(self.fecha_fechanacimiento, self.cajaOpciones_nivelacademico)
        QWidget.setTabOrder(self.cajaOpciones_nivelacademico, self.txt_carrera)
        QWidget.setTabOrder(self.txt_carrera, self.txt_pais)
        QWidget.setTabOrder(self.txt_pais, self.txt_estado)
        QWidget.setTabOrder(self.txt_estado, self.txt_ciudad)
        QWidget.setTabOrder(self.txt_ciudad, self.txt_colonia)
        QWidget.setTabOrder(self.txt_colonia, self.txt_avenidas)
        QWidget.setTabOrder(self.txt_avenidas, self.txt_calles)
        QWidget.setTabOrder(self.txt_calles, self.txt_nexterior)
        QWidget.setTabOrder(self.txt_nexterior, self.txt_ninterior)
        QWidget.setTabOrder(self.txt_ninterior, self.txt_codigopostal)
        QWidget.setTabOrder(self.txt_codigopostal, self.txt_numerotelefono)
        QWidget.setTabOrder(self.txt_numerotelefono, self.txt_correoelectronico)
        QWidget.setTabOrder(self.txt_correoelectronico, self.txt_contactoemergencia)
        QWidget.setTabOrder(self.txt_contactoemergencia, self.txt_nombrecontactoemergencia)
        QWidget.setTabOrder(self.txt_nombrecontactoemergencia, self.cajaOpciones_parentesco)
        QWidget.setTabOrder(self.cajaOpciones_parentesco, self.txtlargo_direccion_completa)
        QWidget.setTabOrder(self.txtlargo_direccion_completa, self.opcion_usodelsistema)
        QWidget.setTabOrder(self.opcion_usodelsistema, self.txt_usuario_iniciosesion)
        QWidget.setTabOrder(self.txt_usuario_iniciosesion, self.txt_contrasenia_usuario_iniciosesion)
        QWidget.setTabOrder(self.txt_contrasenia_usuario_iniciosesion, self.Button_nuevasucursal)
        QWidget.setTabOrder(self.Button_nuevasucursal, self.cajaOpciones_sucursales)
        QWidget.setTabOrder(self.cajaOpciones_sucursales, self.Button_agregardepartamento)
        QWidget.setTabOrder(self.Button_agregardepartamento, self.cajaOpciones_departamentos)
        QWidget.setTabOrder(self.cajaOpciones_departamentos, self.Button_agregarpuesto)
        QWidget.setTabOrder(self.Button_agregarpuesto, self.cajaOpciones_puestos)
        QWidget.setTabOrder(self.cajaOpciones_puestos, self.cajaOpciones_rol_usuario)
        QWidget.setTabOrder(self.cajaOpciones_rol_usuario, self.fecha_fechacontratacion)
        QWidget.setTabOrder(self.fecha_fechacontratacion, self.fecha_fechadespido)
        QWidget.setTabOrder(self.fecha_fechadespido, self.btn_btn_recontratar)
        QWidget.setTabOrder(self.btn_btn_recontratar, self.btn_btn_bajapersona)
        QWidget.setTabOrder(self.btn_btn_bajapersona, self.btc_minimizar)
        QWidget.setTabOrder(self.btc_minimizar, self.btc_maximizar)
        QWidget.setTabOrder(self.btc_maximizar, self.btc_cerrar)

        self.retranslateUi(RegistroAdministrador)

        QMetaObject.connectSlotsByName(RegistroAdministrador)
    # setupUi

    def retranslateUi(self, RegistroAdministrador):
        RegistroAdministrador.setWindowTitle(QCoreApplication.translate("RegistroAdministrador", u"Form", None))
        self.logotipo_cabecera_ventana.setText("")
        self.btc_minimizar.setText("")
        self.btc_maximizar.setText("")
        self.btc_cerrar.setText("")
        self.btn_btn_bajapersona.setText(QCoreApplication.translate("RegistroAdministrador", u"dar de baja", None))
        self.etiqueta_status_empleado.setText("")
        self.etiqueta_rol_usuario.setText(QCoreApplication.translate("RegistroAdministrador", u"Rol del usuario:", None))
        self.etiqueta_departamento.setText(QCoreApplication.translate("RegistroAdministrador", u"Departamento", None))
        self.etiqueta_puesto.setText(QCoreApplication.translate("RegistroAdministrador", u"Puesto", None))
        self.etiqueta_sucursal.setText(QCoreApplication.translate("RegistroAdministrador", u"Sucursal", None))
        self.foto_usuario.setText(QCoreApplication.translate("RegistroAdministrador", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Cantarell'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/Icons/IconosSVG/subir_imagen.png\" width=\"90\" height=\"80\" /></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:bold;font-family:Arial\">Cargar Imagen</span></p></body></html>", None))
        self.Button_nuevasucursal.setText("")
        self.Button_agregardepartamento.setText("")
        self.Button_agregarpuesto.setText("")
        self.etiqueta_fechadespido.setText(QCoreApplication.translate("RegistroAdministrador", u"Fecha de despido", None))
        self.fecha_fechacontratacion.setDisplayFormat(QCoreApplication.translate("RegistroAdministrador", u"dd/MM/yyyy", None))
        self.etiqueta_fechacontratacion.setText(QCoreApplication.translate("RegistroAdministrador", u"Fecha de contrataci\u00f3n:", None))
        self.fecha_fechadespido.setDisplayFormat(QCoreApplication.translate("RegistroAdministrador", u"dd/MM/yyyy", None))
        self.etiquetaTitulo_agregarpersona.setText(QCoreApplication.translate("RegistroAdministrador", u"REGISTRO DE PERSONAL", None))
        self.btn_btn_recontratar.setText(QCoreApplication.translate("RegistroAdministrador", u"recontratar", None))
        self.etiqueta_nombrecontactoemergencia.setText(QCoreApplication.translate("RegistroAdministrador", u"Nombre", None))
        self.etiqueta_contactoemergencia.setText(QCoreApplication.translate("RegistroAdministrador", u"Contacto Emergencia", None))
        self.etiqueta_parentesco.setText(QCoreApplication.translate("RegistroAdministrador", u"Parentesco", None))
        self.txtlargo_direccion_completa.setPlaceholderText(QCoreApplication.translate("RegistroAdministrador", u"Direcci\u00f3n completa y datos de referencia.", None))
        self.etiqueta_nivelestudios.setText(QCoreApplication.translate("RegistroAdministrador", u"Nivel Academico", None))
        self.etiqueta_carrera.setText(QCoreApplication.translate("RegistroAdministrador", u"Carrera", None))
        self.txt_nexterior.setPlaceholderText(QCoreApplication.translate("RegistroAdministrador", u"N-Exterior", None))
        self.txt_ninterior.setPlaceholderText(QCoreApplication.translate("RegistroAdministrador", u"N-Interior", None))
        self.txt_codigopostal.setPlaceholderText(QCoreApplication.translate("RegistroAdministrador", u"Codigo Postal", None))
        self.txt_numerotelefono.setPlaceholderText(QCoreApplication.translate("RegistroAdministrador", u"N\u00famero de telefono", None))
        self.txt_correoelectronico.setPlaceholderText(QCoreApplication.translate("RegistroAdministrador", u"Correo electronico", None))
        self.etiquetasubtitulo_direccion.setText(QCoreApplication.translate("RegistroAdministrador", u"Direcci\u00f3n exacta", None))
        self.txt_nombre.setPlaceholderText(QCoreApplication.translate("RegistroAdministrador", u"Nombre", None))
        self.txt_curp.setPlaceholderText(QCoreApplication.translate("RegistroAdministrador", u"Curp", None))
        self.txt_apellidop.setPlaceholderText(QCoreApplication.translate("RegistroAdministrador", u"Apellido Paterno", None))
        self.txt_rfc.setPlaceholderText(QCoreApplication.translate("RegistroAdministrador", u"Rfc", None))
        self.txt_apellidom.setPlaceholderText(QCoreApplication.translate("RegistroAdministrador", u"Apellido Materno", None))
        self.txt_numerosegurosicial.setPlaceholderText(QCoreApplication.translate("RegistroAdministrador", u"N\u00famero seguro social", None))
        self.etiqueta_genero.setText(QCoreApplication.translate("RegistroAdministrador", u"Genero", None))
        self.etiqueta_estado_civil.setText(QCoreApplication.translate("RegistroAdministrador", u"Estado civil:", None))
        self.etiqueta_fecha_nacimiento.setText(QCoreApplication.translate("RegistroAdministrador", u"Fecha de nacimiento:", None))
        self.fecha_fechanacimiento.setDisplayFormat(QCoreApplication.translate("RegistroAdministrador", u"dd/MM/yyyy", None))
        self.opcion_usodelsistema.setText(QCoreApplication.translate("RegistroAdministrador", u"Asignar Usuario", None))
        self.txt_pais.setPlaceholderText(QCoreApplication.translate("RegistroAdministrador", u"Pais", None))
        self.txt_estado.setPlaceholderText(QCoreApplication.translate("RegistroAdministrador", u"Estado", None))
        self.txt_ciudad.setPlaceholderText(QCoreApplication.translate("RegistroAdministrador", u"Ciudad", None))
        self.txt_colonia.setPlaceholderText(QCoreApplication.translate("RegistroAdministrador", u"Colonia", None))
        self.txt_avenidas.setPlaceholderText(QCoreApplication.translate("RegistroAdministrador", u"Avenida/s", None))
        self.txt_calles.setPlaceholderText(QCoreApplication.translate("RegistroAdministrador", u"Calle/s", None))
        self.Button_actualizarcredenciales.setText(QCoreApplication.translate("RegistroAdministrador", u"Actualizar Credenciales", None))
        self.etiquetasubtitulo_datos_uniciosesion.setText(QCoreApplication.translate("RegistroAdministrador", u"Datos de inicio de sesi\u00f3n", None))
        self.Button_eliminar_credenciales.setText(QCoreApplication.translate("RegistroAdministrador", u"Eliminar", None))
        self.txt_usuario_iniciosesion.setPlaceholderText(QCoreApplication.translate("RegistroAdministrador", u"Usuario de inicio de sesi\u00f3n", None))
        self.opcion_actualizar_datoscredenciales.setText(QCoreApplication.translate("RegistroAdministrador", u"Actualizar Credenciales", None))
        self.txt_contrasenia_usuario_iniciosesion.setPlaceholderText(QCoreApplication.translate("RegistroAdministrador", u"Contrase\u00f1a de inicio de sesi\u00f3n", None))
        self.Button_agregarUsuario.setText(QCoreApplication.translate("RegistroAdministrador", u"Agregar Usuario", None))
        self.Button_actualizar.setText(QCoreApplication.translate("RegistroAdministrador", u"Actualizar", None))
        self.Button_aceptar.setText(QCoreApplication.translate("RegistroAdministrador", u"Aceptar", None))
        self.Button_cancelar.setText(QCoreApplication.translate("RegistroAdministrador", u"Cancelar", None))
    # retranslateUi

