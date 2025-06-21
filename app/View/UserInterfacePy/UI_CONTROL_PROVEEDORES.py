# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UI_CONTROL_PROVEEDORES.ui'
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
    QLineEdit, QPlainTextEdit, QPushButton, QRadioButton,
    QScrollArea, QSizePolicy, QSpacerItem, QTableView,
    QToolButton, QWidget)
from ...Source import ibootstrap_rc
from ...Source import iconsdvg_rc
from ...Source import iconosSVG_rc

class Ui_Control_Proveedores(object):
    def setupUi(self, Control_Proveedores):
        if not Control_Proveedores.objectName():
            Control_Proveedores.setObjectName(u"Control_Proveedores")
        Control_Proveedores.resize(1012, 621)
        Control_Proveedores.setStyleSheet(u"*{color: #1d1c1c;}\n"
"#Control_Proveedores{\n"
"background: #fffefb;\n"
"}\n"
"[objectName*=\"contenedor\"]{\n"
"background: #fffefb;\n"
"border:none;\n"
"}\n"
"#label_wp_titulo_proveedores{\n"
"color:#1d1c1c;\n"
"background-color: #fffefb;\n"
"font-size: 24px;\n"
"font-weight: bold;\n"
"padding-left: 5px;\n"
"text-transform: uppercase;\n"
"font-family: \"Arial\";\n"
"padding-top: 5px;\n"
"}\n"
"*[objectName*=\"etiquetaTitulo_\"]{\n"
"font-size:18px;\n"
"font-family: Arial;\n"
"font-weight:bold;\n"
"color: #1d1c1c;\n"
"}\n"
"*[objectName*=\"etiqueta_\"]{\n"
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
"border-bottom: 1px solid;\n"
"}\n"
"[objectName*=\"txtlargo_\"]{\n"
"background: #F5F5F5;\n"
"border:none;\n"
"border-radius: 5px;\n"
"color: #1d1c1c;\n"
"font-size: 14px;\n"
"border: 1px solid;\n"
"max-height: 100px;\n"
"}\n"
"[obj"
                        "ectName*=\"btn_btn\"]{\n"
"background: #00619a;\n"
"font-size: 12px;\n"
"font-family: Arial;\n"
"font-weight: bold;\n"
"border: none;\n"
"border-radius: 5px;\n"
"color: #fffefb;\n"
"padding-left:5px;\n"
"padding-right:5px;\n"
"}\n"
"#btn_btn_listadeproductoyprecios{\n"
"font-size: 14px;\n"
"}\n"
"[objectName*=\"btnradio\"]{\n"
"font-size:14px;\n"
"font-family:Arial;\n"
"color: #1d1c1c;\n"
"font-weight: bold;\n"
"}\n"
"[objectName*=\"btn_btn\"]:hover{\n"
"background: #2196F3;\n"
"}\n"
"#btn_btn_cancelar:hover{\n"
"background: #EE1D52;\n"
"}\n"
"#btn_btn_guardar:hover{\n"
"background: #68a67d;\n"
"}\n"
"\n"
"\n"
"[objectName*=\"txt_\"]:focus{\n"
"border-bottom: 2px solid #023375;\n"
"}\n"
"[objectName*=\"txtlargo_\"]:focus{\n"
"border-bottom: 2px solid #023375;\n"
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
"\n"
"/* c"
                        "aja opciones */\n"
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
"    border-radius: 3px ;\n"
"    background-color: #F5F5F5 ;\n"
"}\n"
"/* FLECHA DESPLEGABLE */\n"
"[objectName*=\"c"
                        "ajaOpciones\"]::down-arrow {\n"
"    image: url(:/Icons/Bootstrap/filter-left.svg);\n"
"    width: 17% ;\n"
"    height: 17% ;\n"
"    padding-left: 5px ;\n"
"    padding-right: 5px ;\n"
"}\n"
"\n"
"/*TABLA*/\n"
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
"")
        self.gridLayout = QGridLayout(Control_Proveedores)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_wp_titulo_proveedores = QLabel(Control_Proveedores)
        self.label_wp_titulo_proveedores.setObjectName(u"label_wp_titulo_proveedores")
        self.label_wp_titulo_proveedores.setMinimumSize(QSize(0, 0))
        self.label_wp_titulo_proveedores.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.label_wp_titulo_proveedores, 0, 0, 1, 1)

        self.contenedor = QFrame(Control_Proveedores)
        self.contenedor.setObjectName(u"contenedor")
        self.contenedor.setFrameShape(QFrame.Shape.StyledPanel)
        self.contenedor.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_8 = QGridLayout(self.contenedor)
        self.gridLayout_8.setSpacing(0)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.contenedor_scrollArea = QScrollArea(self.contenedor)
        self.contenedor_scrollArea.setObjectName(u"contenedor_scrollArea")
        self.contenedor_scrollArea.setWidgetResizable(True)
        self.contenedor_scroll_area_contenido = QWidget()
        self.contenedor_scroll_area_contenido.setObjectName(u"contenedor_scroll_area_contenido")
        self.contenedor_scroll_area_contenido.setGeometry(QRect(0, 0, 1151, 656))
        self.gridLayout_7 = QGridLayout(self.contenedor_scroll_area_contenido)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.contenedor_todoproveedor = QFrame(self.contenedor_scroll_area_contenido)
        self.contenedor_todoproveedor.setObjectName(u"contenedor_todoproveedor")
        self.contenedor_todoproveedor.setFrameShape(QFrame.Shape.StyledPanel)
        self.contenedor_todoproveedor.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.contenedor_todoproveedor)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.txt_codigopostal = QLineEdit(self.contenedor_todoproveedor)
        self.txt_codigopostal.setObjectName(u"txt_codigopostal")

        self.gridLayout_2.addWidget(self.txt_codigopostal, 10, 1, 1, 2)

        self.txt_colonia = QLineEdit(self.contenedor_todoproveedor)
        self.txt_colonia.setObjectName(u"txt_colonia")

        self.gridLayout_2.addWidget(self.txt_colonia, 6, 1, 1, 2)

        self.contenedor_datosrepresentante = QFrame(self.contenedor_todoproveedor)
        self.contenedor_datosrepresentante.setObjectName(u"contenedor_datosrepresentante")
        self.contenedor_datosrepresentante.setEnabled(True)
        self.contenedor_datosrepresentante.setFrameShape(QFrame.Shape.StyledPanel)
        self.contenedor_datosrepresentante.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_3 = QGridLayout(self.contenedor_datosrepresentante)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.txt_nombrerepresentante = QLineEdit(self.contenedor_datosrepresentante)
        self.txt_nombrerepresentante.setObjectName(u"txt_nombrerepresentante")

        self.gridLayout_3.addWidget(self.txt_nombrerepresentante, 0, 1, 1, 1)

        self.etiqueta_nombrerepresentante = QLabel(self.contenedor_datosrepresentante)
        self.etiqueta_nombrerepresentante.setObjectName(u"etiqueta_nombrerepresentante")

        self.gridLayout_3.addWidget(self.etiqueta_nombrerepresentante, 0, 0, 1, 1)

        self.etiqueta_apellidomaternorepresentante = QLabel(self.contenedor_datosrepresentante)
        self.etiqueta_apellidomaternorepresentante.setObjectName(u"etiqueta_apellidomaternorepresentante")

        self.gridLayout_3.addWidget(self.etiqueta_apellidomaternorepresentante, 2, 0, 1, 1)

        self.etiqueta_apellidopaternorepresentante = QLabel(self.contenedor_datosrepresentante)
        self.etiqueta_apellidopaternorepresentante.setObjectName(u"etiqueta_apellidopaternorepresentante")

        self.gridLayout_3.addWidget(self.etiqueta_apellidopaternorepresentante, 1, 0, 1, 1)

        self.etiqueta_puestorepresentante = QLabel(self.contenedor_datosrepresentante)
        self.etiqueta_puestorepresentante.setObjectName(u"etiqueta_puestorepresentante")

        self.gridLayout_3.addWidget(self.etiqueta_puestorepresentante, 0, 2, 1, 1)

        self.txt_puestorepresentante = QLineEdit(self.contenedor_datosrepresentante)
        self.txt_puestorepresentante.setObjectName(u"txt_puestorepresentante")

        self.gridLayout_3.addWidget(self.txt_puestorepresentante, 0, 3, 1, 1)

        self.etiqueta_telefonorepresentante = QLabel(self.contenedor_datosrepresentante)
        self.etiqueta_telefonorepresentante.setObjectName(u"etiqueta_telefonorepresentante")

        self.gridLayout_3.addWidget(self.etiqueta_telefonorepresentante, 1, 2, 1, 1)

        self.txt_telefonorepresentante = QLineEdit(self.contenedor_datosrepresentante)
        self.txt_telefonorepresentante.setObjectName(u"txt_telefonorepresentante")

        self.gridLayout_3.addWidget(self.txt_telefonorepresentante, 1, 3, 1, 1)

        self.etiqueta_correorepresentante = QLabel(self.contenedor_datosrepresentante)
        self.etiqueta_correorepresentante.setObjectName(u"etiqueta_correorepresentante")

        self.gridLayout_3.addWidget(self.etiqueta_correorepresentante, 2, 2, 1, 1)

        self.txt_correorepresentante = QLineEdit(self.contenedor_datosrepresentante)
        self.txt_correorepresentante.setObjectName(u"txt_correorepresentante")

        self.gridLayout_3.addWidget(self.txt_correorepresentante, 2, 3, 1, 1)

        self.txt_apellidopaternorepresen = QLineEdit(self.contenedor_datosrepresentante)
        self.txt_apellidopaternorepresen.setObjectName(u"txt_apellidopaternorepresen")

        self.gridLayout_3.addWidget(self.txt_apellidopaternorepresen, 1, 1, 1, 1)

        self.txt_apellidomaternorepresen = QLineEdit(self.contenedor_datosrepresentante)
        self.txt_apellidomaternorepresen.setObjectName(u"txt_apellidomaternorepresen")

        self.gridLayout_3.addWidget(self.txt_apellidomaternorepresen, 2, 1, 1, 1)


        self.gridLayout_2.addWidget(self.contenedor_datosrepresentante, 20, 0, 1, 6)

        self.btn_btn_agregarcategoria = QPushButton(self.contenedor_todoproveedor)
        self.btn_btn_agregarcategoria.setObjectName(u"btn_btn_agregarcategoria")
        self.btn_btn_agregarcategoria.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/iconosBlancos/Icons/iconos/Blanco/agregar_blanco.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_btn_agregarcategoria.setIcon(icon)
        self.btn_btn_agregarcategoria.setIconSize(QSize(20, 20))

        self.gridLayout_2.addWidget(self.btn_btn_agregarcategoria, 16, 2, 1, 1)

        self.etiqueta_telefono = QLabel(self.contenedor_todoproveedor)
        self.etiqueta_telefono.setObjectName(u"etiqueta_telefono")

        self.gridLayout_2.addWidget(self.etiqueta_telefono, 2, 0, 1, 1)

        self.etiqueta_avenidas = QLabel(self.contenedor_todoproveedor)
        self.etiqueta_avenidas.setObjectName(u"etiqueta_avenidas")

        self.gridLayout_2.addWidget(self.etiqueta_avenidas, 4, 4, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 22, 0, 1, 1)

        self.cajaOpciones_categorias = QComboBox(self.contenedor_todoproveedor)
        self.cajaOpciones_categorias.setObjectName(u"cajaOpciones_categorias")

        self.gridLayout_2.addWidget(self.cajaOpciones_categorias, 16, 1, 1, 1)

        self.etiqueta_direccionadicional = QLabel(self.contenedor_todoproveedor)
        self.etiqueta_direccionadicional.setObjectName(u"etiqueta_direccionadicional")

        self.gridLayout_2.addWidget(self.etiqueta_direccionadicional, 18, 0, 1, 1, Qt.AlignmentFlag.AlignTop)

        self.etiqueta_colonia = QLabel(self.contenedor_todoproveedor)
        self.etiqueta_colonia.setObjectName(u"etiqueta_colonia")

        self.gridLayout_2.addWidget(self.etiqueta_colonia, 6, 0, 1, 1)

        self.txtlargo_descripcioncategoria = QPlainTextEdit(self.contenedor_todoproveedor)
        self.txtlargo_descripcioncategoria.setObjectName(u"txtlargo_descripcioncategoria")

        self.gridLayout_2.addWidget(self.txtlargo_descripcioncategoria, 19, 1, 1, 5)

        self.txt_correo = QLineEdit(self.contenedor_todoproveedor)
        self.txt_correo.setObjectName(u"txt_correo")

        self.gridLayout_2.addWidget(self.txt_correo, 2, 5, 1, 1)

        self.etiqueta_calles = QLabel(self.contenedor_todoproveedor)
        self.etiqueta_calles.setObjectName(u"etiqueta_calles")

        self.gridLayout_2.addWidget(self.etiqueta_calles, 4, 0, 1, 1)

        self.txt_web = QLineEdit(self.contenedor_todoproveedor)
        self.txt_web.setObjectName(u"txt_web")

        self.gridLayout_2.addWidget(self.txt_web, 10, 5, 1, 1)

        self.txt_avenida = QLineEdit(self.contenedor_todoproveedor)
        self.txt_avenida.setObjectName(u"txt_avenida")

        self.gridLayout_2.addWidget(self.txt_avenida, 4, 5, 1, 1)

        self.etiqueta_pais = QLabel(self.contenedor_todoproveedor)
        self.etiqueta_pais.setObjectName(u"etiqueta_pais")

        self.gridLayout_2.addWidget(self.etiqueta_pais, 8, 4, 1, 1)

        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.etiqueta_tienerepresentante = QLabel(self.contenedor_todoproveedor)
        self.etiqueta_tienerepresentante.setObjectName(u"etiqueta_tienerepresentante")

        self.gridLayout_6.addWidget(self.etiqueta_tienerepresentante, 0, 1, 1, 1)

        self.btnradio_representantetrue = QRadioButton(self.contenedor_todoproveedor)
        self.btnradio_representantetrue.setObjectName(u"btnradio_representantetrue")

        self.gridLayout_6.addWidget(self.btnradio_representantetrue, 0, 2, 1, 1)

        self.btnradio_representantefalse = QRadioButton(self.contenedor_todoproveedor)
        self.btnradio_representantefalse.setObjectName(u"btnradio_representantefalse")

        self.gridLayout_6.addWidget(self.btnradio_representantefalse, 0, 3, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout_6, 16, 4, 1, 2)

        self.txt_nombre = QLineEdit(self.contenedor_todoproveedor)
        self.txt_nombre.setObjectName(u"txt_nombre")

        self.gridLayout_2.addWidget(self.txt_nombre, 0, 1, 1, 2)

        self.txt_pais = QLineEdit(self.contenedor_todoproveedor)
        self.txt_pais.setObjectName(u"txt_pais")

        self.gridLayout_2.addWidget(self.txt_pais, 8, 5, 1, 1)

        self.txt_ciudad = QLineEdit(self.contenedor_todoproveedor)
        self.txt_ciudad.setObjectName(u"txt_ciudad")

        self.gridLayout_2.addWidget(self.txt_ciudad, 6, 5, 1, 1)

        self.etiqueta_rfc = QLabel(self.contenedor_todoproveedor)
        self.etiqueta_rfc.setObjectName(u"etiqueta_rfc")

        self.gridLayout_2.addWidget(self.etiqueta_rfc, 0, 4, 1, 1)

        self.etiqueta_codigopostal = QLabel(self.contenedor_todoproveedor)
        self.etiqueta_codigopostal.setObjectName(u"etiqueta_codigopostal")

        self.gridLayout_2.addWidget(self.etiqueta_codigopostal, 10, 0, 1, 1)

        self.etiqueta_descripcioncategoria = QLabel(self.contenedor_todoproveedor)
        self.etiqueta_descripcioncategoria.setObjectName(u"etiqueta_descripcioncategoria")

        self.gridLayout_2.addWidget(self.etiqueta_descripcioncategoria, 19, 0, 1, 1, Qt.AlignmentFlag.AlignTop)

        self.txt_calles = QLineEdit(self.contenedor_todoproveedor)
        self.txt_calles.setObjectName(u"txt_calles")

        self.gridLayout_2.addWidget(self.txt_calles, 4, 1, 1, 2)

        self.btn_btn_limpiardatos = QPushButton(self.contenedor_todoproveedor)
        self.btn_btn_limpiardatos.setObjectName(u"btn_btn_limpiardatos")
        self.btn_btn_limpiardatos.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/Icons/IconosSVG/borrador.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_btn_limpiardatos.setIcon(icon1)
        self.btn_btn_limpiardatos.setIconSize(QSize(24, 24))

        self.gridLayout_2.addWidget(self.btn_btn_limpiardatos, 21, 0, 1, 1)

        self.etiqueta_web = QLabel(self.contenedor_todoproveedor)
        self.etiqueta_web.setObjectName(u"etiqueta_web")

        self.gridLayout_2.addWidget(self.etiqueta_web, 10, 4, 1, 1)

        self.etiqueta_estado = QLabel(self.contenedor_todoproveedor)
        self.etiqueta_estado.setObjectName(u"etiqueta_estado")

        self.gridLayout_2.addWidget(self.etiqueta_estado, 8, 0, 1, 1)

        self.txt_estado = QLineEdit(self.contenedor_todoproveedor)
        self.txt_estado.setObjectName(u"txt_estado")

        self.gridLayout_2.addWidget(self.txt_estado, 8, 1, 1, 2)

        self.etiqueta_nombre = QLabel(self.contenedor_todoproveedor)
        self.etiqueta_nombre.setObjectName(u"etiqueta_nombre")

        self.gridLayout_2.addWidget(self.etiqueta_nombre, 0, 0, 1, 1)

        self.etiqueta_categoria = QLabel(self.contenedor_todoproveedor)
        self.etiqueta_categoria.setObjectName(u"etiqueta_categoria")

        self.gridLayout_2.addWidget(self.etiqueta_categoria, 16, 0, 1, 1)

        self.etiqueta_ciudad = QLabel(self.contenedor_todoproveedor)
        self.etiqueta_ciudad.setObjectName(u"etiqueta_ciudad")

        self.gridLayout_2.addWidget(self.etiqueta_ciudad, 6, 4, 1, 1)

        self.txt_rfc = QLineEdit(self.contenedor_todoproveedor)
        self.txt_rfc.setObjectName(u"txt_rfc")

        self.gridLayout_2.addWidget(self.txt_rfc, 0, 5, 1, 1)

        self.etiqueta_correo = QLabel(self.contenedor_todoproveedor)
        self.etiqueta_correo.setObjectName(u"etiqueta_correo")

        self.gridLayout_2.addWidget(self.etiqueta_correo, 2, 4, 1, 1)

        self.txtlargo_direccionadicional = QPlainTextEdit(self.contenedor_todoproveedor)
        self.txtlargo_direccionadicional.setObjectName(u"txtlargo_direccionadicional")

        self.gridLayout_2.addWidget(self.txtlargo_direccionadicional, 18, 1, 1, 5)

        self.txt_telefono = QLineEdit(self.contenedor_todoproveedor)
        self.txt_telefono.setObjectName(u"txt_telefono")

        self.gridLayout_2.addWidget(self.txt_telefono, 2, 1, 1, 2)

        self.etiqueta_moneda = QLabel(self.contenedor_todoproveedor)
        self.etiqueta_moneda.setObjectName(u"etiqueta_moneda")

        self.gridLayout_2.addWidget(self.etiqueta_moneda, 17, 0, 1, 1)

        self.cajaOpciones_tipomoneda = QComboBox(self.contenedor_todoproveedor)
        self.cajaOpciones_tipomoneda.addItem("")
        self.cajaOpciones_tipomoneda.addItem("")
        self.cajaOpciones_tipomoneda.addItem("")
        self.cajaOpciones_tipomoneda.addItem("")
        self.cajaOpciones_tipomoneda.addItem("")
        self.cajaOpciones_tipomoneda.addItem("")
        self.cajaOpciones_tipomoneda.addItem("")
        self.cajaOpciones_tipomoneda.addItem("")
        self.cajaOpciones_tipomoneda.addItem("")
        self.cajaOpciones_tipomoneda.addItem("")
        self.cajaOpciones_tipomoneda.addItem("")
        self.cajaOpciones_tipomoneda.addItem("")
        self.cajaOpciones_tipomoneda.addItem("")
        self.cajaOpciones_tipomoneda.addItem("")
        self.cajaOpciones_tipomoneda.addItem("")
        self.cajaOpciones_tipomoneda.addItem("")
        self.cajaOpciones_tipomoneda.setObjectName(u"cajaOpciones_tipomoneda")
        self.cajaOpciones_tipomoneda.setMaxVisibleItems(10)
        self.cajaOpciones_tipomoneda.setModelColumn(0)

        self.gridLayout_2.addWidget(self.cajaOpciones_tipomoneda, 17, 1, 1, 2)


        self.gridLayout_7.addWidget(self.contenedor_todoproveedor, 1, 0, 1, 1)

        self.contenedor_tablareproveedores = QFrame(self.contenedor_scroll_area_contenido)
        self.contenedor_tablareproveedores.setObjectName(u"contenedor_tablareproveedores")
        self.contenedor_tablareproveedores.setFrameShape(QFrame.Shape.StyledPanel)
        self.contenedor_tablareproveedores.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_4 = QGridLayout(self.contenedor_tablareproveedores)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.etiquetaTitulo_proveedor = QLabel(self.contenedor_tablareproveedores)
        self.etiquetaTitulo_proveedor.setObjectName(u"etiquetaTitulo_proveedor")

        self.gridLayout_4.addWidget(self.etiquetaTitulo_proveedor, 0, 0, 1, 1)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setHorizontalSpacing(3)
        self.txt_buscarproveedor = QLineEdit(self.contenedor_tablareproveedores)
        self.txt_buscarproveedor.setObjectName(u"txt_buscarproveedor")
        self.txt_buscarproveedor.setClearButtonEnabled(True)

        self.gridLayout_5.addWidget(self.txt_buscarproveedor, 0, 0, 1, 1)

        self.btn_btn_buscarproveedor = QToolButton(self.contenedor_tablareproveedores)
        self.btn_btn_buscarproveedor.setObjectName(u"btn_btn_buscarproveedor")
        self.btn_btn_buscarproveedor.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/iconosBlancos/Icons/iconos/Blanco/buscar_persona_blanco.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_btn_buscarproveedor.setIcon(icon2)
        self.btn_btn_buscarproveedor.setIconSize(QSize(24, 24))

        self.gridLayout_5.addWidget(self.btn_btn_buscarproveedor, 0, 1, 1, 1)

        self.btn_RefrescarTabla = QPushButton(self.contenedor_tablareproveedores)
        self.btn_RefrescarTabla.setObjectName(u"btn_RefrescarTabla")
        self.btn_RefrescarTabla.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/iconosBlancos/Icons/IconosSVG/base_datos_refresh.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_RefrescarTabla.setIcon(icon3)
        self.btn_RefrescarTabla.setIconSize(QSize(16, 16))

        self.gridLayout_5.addWidget(self.btn_RefrescarTabla, 0, 2, 1, 1)

        self.tabla_proveedores = QTableView(self.contenedor_tablareproveedores)
        self.tabla_proveedores.setObjectName(u"tabla_proveedores")
        self.tabla_proveedores.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tabla_proveedores.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tabla_proveedores.setGridStyle(Qt.PenStyle.DashDotDotLine)
        self.tabla_proveedores.horizontalHeader().setCascadingSectionResizes(False)
        self.tabla_proveedores.horizontalHeader().setMinimumSectionSize(150)
        self.tabla_proveedores.horizontalHeader().setDefaultSectionSize(200)
        self.tabla_proveedores.horizontalHeader().setStretchLastSection(False)
        self.tabla_proveedores.verticalHeader().setVisible(False)
        self.tabla_proveedores.verticalHeader().setStretchLastSection(False)

        self.gridLayout_5.addWidget(self.tabla_proveedores, 1, 0, 1, 3)


        self.gridLayout_4.addLayout(self.gridLayout_5, 1, 0, 1, 1)

        self.contenedor_frame = QFrame(self.contenedor_tablareproveedores)
        self.contenedor_frame.setObjectName(u"contenedor_frame")
        self.contenedor_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.contenedor_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.contenedor_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.btn_btn_guardar = QToolButton(self.contenedor_frame)
        self.btn_btn_guardar.setObjectName(u"btn_btn_guardar")
        self.btn_btn_guardar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/iconosBlancos/Icons/iconos/Blanco/guardar_blanco.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_btn_guardar.setIcon(icon4)
        self.btn_btn_guardar.setIconSize(QSize(24, 24))
        self.btn_btn_guardar.setPopupMode(QToolButton.ToolButtonPopupMode.DelayedPopup)
        self.btn_btn_guardar.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.btn_btn_guardar.setAutoRaise(True)
        self.btn_btn_guardar.setArrowType(Qt.ArrowType.NoArrow)

        self.horizontalLayout_2.addWidget(self.btn_btn_guardar)

        self.btn_btn_actualizar = QPushButton(self.contenedor_frame)
        self.btn_btn_actualizar.setObjectName(u"btn_btn_actualizar")
        self.btn_btn_actualizar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u":/iconosBlancos/Icons/iconos/Blanco/actualizar_blanco.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_btn_actualizar.setIcon(icon5)
        self.btn_btn_actualizar.setIconSize(QSize(24, 26))

        self.horizontalLayout_2.addWidget(self.btn_btn_actualizar)

        self.btn_btn_eliminar = QToolButton(self.contenedor_frame)
        self.btn_btn_eliminar.setObjectName(u"btn_btn_eliminar")
        self.btn_btn_eliminar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon6 = QIcon()
        icon6.addFile(u":/iconosBlancos/Icons/iconos/Blanco/eliminar_blanco.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_btn_eliminar.setIcon(icon6)
        self.btn_btn_eliminar.setIconSize(QSize(24, 24))
        self.btn_btn_eliminar.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

        self.horizontalLayout_2.addWidget(self.btn_btn_eliminar)


        self.gridLayout_4.addWidget(self.contenedor_frame, 2, 0, 1, 1)

        self.contenedor_botones_inferior_derecha = QWidget(self.contenedor_tablareproveedores)
        self.contenedor_botones_inferior_derecha.setObjectName(u"contenedor_botones_inferior_derecha")
        self.horizontalLayout = QHBoxLayout(self.contenedor_botones_inferior_derecha)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_4.addWidget(self.contenedor_botones_inferior_derecha, 3, 0, 1, 1)


        self.gridLayout_7.addWidget(self.contenedor_tablareproveedores, 1, 1, 1, 1)

        self.btn_btn_listadeproductoyprecios = QPushButton(self.contenedor_scroll_area_contenido)
        self.btn_btn_listadeproductoyprecios.setObjectName(u"btn_btn_listadeproductoyprecios")
        self.btn_btn_listadeproductoyprecios.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout_7.addWidget(self.btn_btn_listadeproductoyprecios, 0, 0, 1, 1, Qt.AlignmentFlag.AlignLeft)

        self.contenedor_scrollArea.setWidget(self.contenedor_scroll_area_contenido)

        self.gridLayout_8.addWidget(self.contenedor_scrollArea, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.contenedor, 1, 0, 1, 1)

        QWidget.setTabOrder(self.txt_nombre, self.txt_telefono)
        QWidget.setTabOrder(self.txt_telefono, self.txt_calles)
        QWidget.setTabOrder(self.txt_calles, self.txt_colonia)
        QWidget.setTabOrder(self.txt_colonia, self.txt_estado)
        QWidget.setTabOrder(self.txt_estado, self.txt_codigopostal)
        QWidget.setTabOrder(self.txt_codigopostal, self.txt_rfc)
        QWidget.setTabOrder(self.txt_rfc, self.txt_correo)
        QWidget.setTabOrder(self.txt_correo, self.txt_avenida)
        QWidget.setTabOrder(self.txt_avenida, self.txt_ciudad)
        QWidget.setTabOrder(self.txt_ciudad, self.txt_pais)
        QWidget.setTabOrder(self.txt_pais, self.txt_web)
        QWidget.setTabOrder(self.txt_web, self.cajaOpciones_categorias)
        QWidget.setTabOrder(self.cajaOpciones_categorias, self.btn_btn_agregarcategoria)
        QWidget.setTabOrder(self.btn_btn_agregarcategoria, self.btnradio_representantetrue)
        QWidget.setTabOrder(self.btnradio_representantetrue, self.btnradio_representantefalse)
        QWidget.setTabOrder(self.btnradio_representantefalse, self.txtlargo_direccionadicional)
        QWidget.setTabOrder(self.txtlargo_direccionadicional, self.txt_nombrerepresentante)
        QWidget.setTabOrder(self.txt_nombrerepresentante, self.txt_apellidopaternorepresen)
        QWidget.setTabOrder(self.txt_apellidopaternorepresen, self.txt_apellidomaternorepresen)
        QWidget.setTabOrder(self.txt_apellidomaternorepresen, self.txt_puestorepresentante)
        QWidget.setTabOrder(self.txt_puestorepresentante, self.txt_telefonorepresentante)
        QWidget.setTabOrder(self.txt_telefonorepresentante, self.txt_correorepresentante)
        QWidget.setTabOrder(self.txt_correorepresentante, self.txt_buscarproveedor)
        QWidget.setTabOrder(self.txt_buscarproveedor, self.btn_btn_buscarproveedor)
        QWidget.setTabOrder(self.btn_btn_buscarproveedor, self.btn_btn_limpiardatos)
        QWidget.setTabOrder(self.btn_btn_limpiardatos, self.txtlargo_descripcioncategoria)

        self.retranslateUi(Control_Proveedores)

        QMetaObject.connectSlotsByName(Control_Proveedores)
    # setupUi

    def retranslateUi(self, Control_Proveedores):
        Control_Proveedores.setWindowTitle(QCoreApplication.translate("Control_Proveedores", u"Form", None))
        self.label_wp_titulo_proveedores.setText(QCoreApplication.translate("Control_Proveedores", u"REGISTRO DE PROVEEDOR", None))
        self.etiqueta_nombrerepresentante.setText(QCoreApplication.translate("Control_Proveedores", u"Nombre", None))
        self.etiqueta_apellidomaternorepresentante.setText(QCoreApplication.translate("Control_Proveedores", u"Apellido Materno", None))
        self.etiqueta_apellidopaternorepresentante.setText(QCoreApplication.translate("Control_Proveedores", u"Apellido Paterno", None))
        self.etiqueta_puestorepresentante.setText(QCoreApplication.translate("Control_Proveedores", u"Puesto", None))
        self.etiqueta_telefonorepresentante.setText(QCoreApplication.translate("Control_Proveedores", u"Telefono", None))
        self.etiqueta_correorepresentante.setText(QCoreApplication.translate("Control_Proveedores", u"Correo", None))
#if QT_CONFIG(tooltip)
        self.btn_btn_agregarcategoria.setToolTip(QCoreApplication.translate("Control_Proveedores", u"Nueva Categoria", None))
#endif // QT_CONFIG(tooltip)
        self.btn_btn_agregarcategoria.setText("")
        self.etiqueta_telefono.setText(QCoreApplication.translate("Control_Proveedores", u"Telefono", None))
        self.etiqueta_avenidas.setText(QCoreApplication.translate("Control_Proveedores", u"Avenida/s", None))
        self.etiqueta_direccionadicional.setText(QCoreApplication.translate("Control_Proveedores", u"Direccion Adiccional", None))
        self.etiqueta_colonia.setText(QCoreApplication.translate("Control_Proveedores", u"Colonia", None))
        self.etiqueta_calles.setText(QCoreApplication.translate("Control_Proveedores", u"Calle/s", None))
        self.etiqueta_pais.setText(QCoreApplication.translate("Control_Proveedores", u"Pais", None))
        self.etiqueta_tienerepresentante.setText(QCoreApplication.translate("Control_Proveedores", u"Tiene representante?", None))
        self.btnradio_representantetrue.setText(QCoreApplication.translate("Control_Proveedores", u"Si", None))
        self.btnradio_representantefalse.setText(QCoreApplication.translate("Control_Proveedores", u"No", None))
        self.etiqueta_rfc.setText(QCoreApplication.translate("Control_Proveedores", u"RFC", None))
        self.etiqueta_codigopostal.setText(QCoreApplication.translate("Control_Proveedores", u"Codigo Postal", None))
        self.etiqueta_descripcioncategoria.setText(QCoreApplication.translate("Control_Proveedores", u"Descripcion Cat.", None))
#if QT_CONFIG(tooltip)
        self.btn_btn_limpiardatos.setToolTip(QCoreApplication.translate("Control_Proveedores", u"Limpiar Campos", None))
#endif // QT_CONFIG(tooltip)
        self.btn_btn_limpiardatos.setText("")
        self.etiqueta_web.setText(QCoreApplication.translate("Control_Proveedores", u"Web", None))
        self.etiqueta_estado.setText(QCoreApplication.translate("Control_Proveedores", u"Estado", None))
        self.etiqueta_nombre.setText(QCoreApplication.translate("Control_Proveedores", u"Nombre", None))
        self.etiqueta_categoria.setText(QCoreApplication.translate("Control_Proveedores", u"Categoria", None))
        self.etiqueta_ciudad.setText(QCoreApplication.translate("Control_Proveedores", u"Ciudad", None))
        self.etiqueta_correo.setText(QCoreApplication.translate("Control_Proveedores", u"Correo", None))
        self.etiqueta_moneda.setText(QCoreApplication.translate("Control_Proveedores", u"Moneda", None))
        self.cajaOpciones_tipomoneda.setItemText(0, QCoreApplication.translate("Control_Proveedores", u"MXN: Peso Mexicano.", None))
        self.cajaOpciones_tipomoneda.setItemText(1, QCoreApplication.translate("Control_Proveedores", u"USD: D\u00f3lar estadounidense.", None))
        self.cajaOpciones_tipomoneda.setItemText(2, QCoreApplication.translate("Control_Proveedores", u"EUR: Euro.", None))
        self.cajaOpciones_tipomoneda.setItemText(3, QCoreApplication.translate("Control_Proveedores", u"GBP: Libra Esterlina.", None))
        self.cajaOpciones_tipomoneda.setItemText(4, QCoreApplication.translate("Control_Proveedores", u"JPY: Yen japon\u00e9s.", None))
        self.cajaOpciones_tipomoneda.setItemText(5, QCoreApplication.translate("Control_Proveedores", u"CAD: D\u00f3lar canadiense.", None))
        self.cajaOpciones_tipomoneda.setItemText(6, QCoreApplication.translate("Control_Proveedores", u"AUD: D\u00f3lar australiano.", None))
        self.cajaOpciones_tipomoneda.setItemText(7, QCoreApplication.translate("Control_Proveedores", u"CHF: Franco suizo.", None))
        self.cajaOpciones_tipomoneda.setItemText(8, QCoreApplication.translate("Control_Proveedores", u"CNY: Yuan chino.", None))
        self.cajaOpciones_tipomoneda.setItemText(9, QCoreApplication.translate("Control_Proveedores", u"BRL: Real brasile\u00f1o.", None))
        self.cajaOpciones_tipomoneda.setItemText(10, QCoreApplication.translate("Control_Proveedores", u"ARS: Peso argentino.", None))
        self.cajaOpciones_tipomoneda.setItemText(11, QCoreApplication.translate("Control_Proveedores", u"CLP: Peso chileno.", None))
        self.cajaOpciones_tipomoneda.setItemText(12, QCoreApplication.translate("Control_Proveedores", u"COP: Peso colombiano.", None))
        self.cajaOpciones_tipomoneda.setItemText(13, QCoreApplication.translate("Control_Proveedores", u"PEN: Nuevo sol peruano.", None))
        self.cajaOpciones_tipomoneda.setItemText(14, QCoreApplication.translate("Control_Proveedores", u"INR: Rupia india.", None))
        self.cajaOpciones_tipomoneda.setItemText(15, QCoreApplication.translate("Control_Proveedores", u"KRW: Won surcoreano.", None))

        self.etiquetaTitulo_proveedor.setText(QCoreApplication.translate("Control_Proveedores", u"Lista de proveedores", None))
        self.txt_buscarproveedor.setPlaceholderText(QCoreApplication.translate("Control_Proveedores", u"Nombre del proveedor", None))
#if QT_CONFIG(tooltip)
        self.btn_btn_buscarproveedor.setToolTip(QCoreApplication.translate("Control_Proveedores", u"Buscar Proveedor", None))
#endif // QT_CONFIG(tooltip)
        self.btn_btn_buscarproveedor.setText("")
#if QT_CONFIG(tooltip)
        self.btn_RefrescarTabla.setToolTip(QCoreApplication.translate("Control_Proveedores", u"Actualizar tabla", None))
#endif // QT_CONFIG(tooltip)
        self.btn_RefrescarTabla.setText("")
#if QT_CONFIG(tooltip)
        self.btn_btn_guardar.setToolTip(QCoreApplication.translate("Control_Proveedores", u"Guardar", None))
#endif // QT_CONFIG(tooltip)
        self.btn_btn_guardar.setText(QCoreApplication.translate("Control_Proveedores", u"GUARDAR", None))
#if QT_CONFIG(tooltip)
        self.btn_btn_actualizar.setToolTip(QCoreApplication.translate("Control_Proveedores", u"Actualizar", None))
#endif // QT_CONFIG(tooltip)
        self.btn_btn_actualizar.setText(QCoreApplication.translate("Control_Proveedores", u"ACTUALIZAR", None))
#if QT_CONFIG(tooltip)
        self.btn_btn_eliminar.setToolTip(QCoreApplication.translate("Control_Proveedores", u"Eliminar", None))
#endif // QT_CONFIG(tooltip)
        self.btn_btn_eliminar.setText(QCoreApplication.translate("Control_Proveedores", u"ELIMINAR", None))
#if QT_CONFIG(tooltip)
        self.btn_btn_listadeproductoyprecios.setToolTip(QCoreApplication.translate("Control_Proveedores", u"Lista de Precios y Produtos Relacionados", None))
#endif // QT_CONFIG(tooltip)
        self.btn_btn_listadeproductoyprecios.setText(QCoreApplication.translate("Control_Proveedores", u"Lista de Productos y Precios", None))
    # retranslateUi

