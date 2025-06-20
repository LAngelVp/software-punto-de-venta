# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UI_ADMINISTRAR_PUESTOS.ui'
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
    QDoubleSpinBox, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QPlainTextEdit,
    QPushButton, QSizePolicy, QSpacerItem, QTableView,
    QTimeEdit, QWidget)
import iconsdvg_rc
import iconosSVG_rc
import ibootstrap_rc

class Ui_Formulario_puestos(object):
    def setupUi(self, Formulario_puestos):
        if not Formulario_puestos.objectName():
            Formulario_puestos.setObjectName(u"Formulario_puestos")
        Formulario_puestos.resize(895, 600)
        Formulario_puestos.setMinimumSize(QSize(0, 0))
        Formulario_puestos.setMaximumSize(QSize(16777215, 16777215))
        Formulario_puestos.setStyleSheet(u"*{color: #1d1c1c;}\n"
"#Formulario_puestos{\n"
"background: #fffefb;\n"
"}\n"
"[objectName*=\"contenedor\"]{\n"
"background: #fffefb;\n"
"border: none;\n"
"}\n"
"#contenedor_encabezado{\n"
"background: #023375;\n"
"}\n"
"[objectName*=\"etiquetaTitulo_\"]{\n"
"font-size: 18px;\n"
"font-weight:bold;\n"
"font-family:Arial;\n"
"color: #fffefb;\n"
"}\n"
"[objectName*=\"etiqueta_\"]{\n"
"font-size: 14px;\n"
"font-weight:bold;\n"
"font-family:Arial;\n"
"color: #1d1c1c;\n"
"}\n"
"[objectName*=\"etiquetasubtitulo_\"]{\n"
"font-size: 15px;\n"
"font-weight:bold;\n"
"font-family:Arial;\n"
"color: #1d1c1c;\n"
"}\n"
"[objectName*=\"txt_\"]{\n"
"font-size: 14px;\n"
"font-family:Arial;\n"
"color: #1d1c1c;\n"
"background: #F5F5F5;\n"
"border:none;\n"
"border-radius: 5px;\n"
"border-bottom: 1px solid #1d1c1c;\n"
"}\n"
"[objectName*=\"txt_\"]:focus{\n"
"border-bottom: 2px solid #023375;\n"
"}\n"
"[objectName*=\"txtlargo_\"]{\n"
"font-size: 14px;\n"
"font-family:Arial;\n"
"color: #1d1c1c;\n"
"background: #F5F5F5;\n"
"border:none;"
                        "\n"
"border-radius: 5px;\n"
"border-bottom: 1px solid #1d1c1c;\n"
"max-height: 100px;\n"
"}\n"
"[objectName*=\"txtlargo_\"]:focus{\n"
"border-bottom: 2px solid #023375;\n"
"}\n"
"[objectName*=\"cajaopcion_\"]{\n"
"font-size: 14px;\n"
"font-weight:bold;\n"
"font-family:Arial;\n"
"color: #1d1c1c;\n"
"}\n"
"[objectName^=\"decimal_\"]{\n"
"border: none;\n"
"border-bottom: 1px solid #3b3c3d;\n"
"border-radius: 4px;\n"
"background-color: #F5F5F5;\n"
"font-size: 14px;\n"
"padding: 2px;\n"
"}\n"
"[objectName^=\"decimal_\"]::focus{\n"
"border-bottom: 2px solid #00668c;\n"
"}\n"
"[objectName^=\"tiempo_\"]{\n"
"border: none;\n"
"border-bottom: 1px solid #3b3c3d;\n"
"border-radius: 4px;\n"
"background-color: #F5F5F5;\n"
"font-size: 14px;\n"
"padding: 2px;\n"
"}\n"
"[objectName^=\"tiempo_\"]::focus{\n"
"border-bottom: 2px solid #00668c;\n"
"}\n"
"[objectName^=\"btn_btn_\"]{\n"
"background: #00619a;\n"
"font-size: 14px;\n"
"font-weight: bold;\n"
"color: #fffefb;\n"
"border: none;\n"
"border-radius:5px;\n"
"min-height: 25px;"
                        "\n"
"padding-right:10px;\n"
"padding-left:10px;\n"
"}\n"
"[objectName^=\"btn_btn_\"]:hover{\n"
"background: #2196F3;\n"
"}\n"
"#btn_btn_agregar:hover{\n"
"background: #68a67d;\n"
"}\n"
"#btn_btn_eliminar:hover{\n"
"background: #EE1D52;\n"
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
"    subcontrol"
                        "-position: top right ;\n"
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
"/*TABLA*/\n"
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
"[objectName"
                        "*=\"tabla_\"] QHeaderView::vertical {\n"
"    background-color: #023375;\n"
"    color: white;\n"
"}	")
        self.gridLayout_7 = QGridLayout(Formulario_puestos)
        self.gridLayout_7.setSpacing(0)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.contenedor_frame_2 = QFrame(Formulario_puestos)
        self.contenedor_frame_2.setObjectName(u"contenedor_frame_2")
        self.contenedor_frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.contenedor_frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.contenedor_frame_2)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.contenedor_encabezado = QFrame(self.contenedor_frame_2)
        self.contenedor_encabezado.setObjectName(u"contenedor_encabezado")
        self.contenedor_encabezado.setFrameShape(QFrame.Shape.StyledPanel)
        self.contenedor_encabezado.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.contenedor_encabezado)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.etiquetaTitulo_administrarpuestos = QLabel(self.contenedor_encabezado)
        self.etiquetaTitulo_administrarpuestos.setObjectName(u"etiquetaTitulo_administrarpuestos")

        self.horizontalLayout.addWidget(self.etiquetaTitulo_administrarpuestos)

        self.horizontalSpacer_2 = QSpacerItem(755, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.btn_cerrar = QPushButton(self.contenedor_encabezado)
        self.btn_cerrar.setObjectName(u"btn_cerrar")
        self.btn_cerrar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/Icons/Bootstrap/x-lg.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_cerrar.setIcon(icon)

        self.horizontalLayout.addWidget(self.btn_cerrar)


        self.gridLayout.addWidget(self.contenedor_encabezado, 0, 0, 1, 1)

        self.contenedor = QFrame(self.contenedor_frame_2)
        self.contenedor.setObjectName(u"contenedor")
        self.contenedor.setStyleSheet(u"")
        self.contenedor.setFrameShape(QFrame.Shape.StyledPanel)
        self.contenedor.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_6 = QGridLayout(self.contenedor)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.contenedor_frame = QFrame(self.contenedor)
        self.contenedor_frame.setObjectName(u"contenedor_frame")
        self.contenedor_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.contenedor_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.contenedor_frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.tabla_listapuestos = QTableView(self.contenedor_frame)
        self.tabla_listapuestos.setObjectName(u"tabla_listapuestos")
        self.tabla_listapuestos.setMinimumSize(QSize(420, 0))
        self.tabla_listapuestos.horizontalHeader().setMinimumSectionSize(200)
        self.tabla_listapuestos.horizontalHeader().setDefaultSectionSize(200)
        self.tabla_listapuestos.horizontalHeader().setStretchLastSection(False)

        self.gridLayout_2.addWidget(self.tabla_listapuestos, 2, 0, 1, 3)

        self.etiqueta_puestosexistentes = QLabel(self.contenedor_frame)
        self.etiqueta_puestosexistentes.setObjectName(u"etiqueta_puestosexistentes")

        self.gridLayout_2.addWidget(self.etiqueta_puestosexistentes, 0, 0, 1, 1)

        self.txt_buscarpuesto = QLineEdit(self.contenedor_frame)
        self.txt_buscarpuesto.setObjectName(u"txt_buscarpuesto")

        self.gridLayout_2.addWidget(self.txt_buscarpuesto, 1, 0, 1, 3)


        self.gridLayout_6.addWidget(self.contenedor_frame, 1, 1, 1, 1)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.btn_btn_limpiar = QPushButton(self.contenedor)
        self.btn_btn_limpiar.setObjectName(u"btn_btn_limpiar")
        self.btn_btn_limpiar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/Icons/IconosSVG/borrador.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_btn_limpiar.setIcon(icon1)
        self.btn_btn_limpiar.setIconSize(QSize(25, 25))

        self.gridLayout_3.addWidget(self.btn_btn_limpiar, 0, 0, 1, 1)

        self.btn_btn_agregar = QPushButton(self.contenedor)
        self.btn_btn_agregar.setObjectName(u"btn_btn_agregar")
        font = QFont()
        font.setBold(True)
        self.btn_btn_agregar.setFont(font)
        self.btn_btn_agregar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_btn_agregar.setAutoFillBackground(False)
        icon2 = QIcon()
        icon2.addFile(u":/iconosBlancos/Icons/iconos/Blanco/guardar_blanco.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_btn_agregar.setIcon(icon2)
        self.btn_btn_agregar.setIconSize(QSize(16, 16))

        self.gridLayout_3.addWidget(self.btn_btn_agregar, 0, 1, 1, 1)

        self.btn_btn_actualizar = QPushButton(self.contenedor)
        self.btn_btn_actualizar.setObjectName(u"btn_btn_actualizar")
        self.btn_btn_actualizar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/iconosBlancos/Icons/iconos/Blanco/actualizar_blanco.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_btn_actualizar.setIcon(icon3)
        self.btn_btn_actualizar.setIconSize(QSize(16, 16))

        self.gridLayout_3.addWidget(self.btn_btn_actualizar, 0, 2, 1, 1)

        self.btn_btn_eliminar = QPushButton(self.contenedor)
        self.btn_btn_eliminar.setObjectName(u"btn_btn_eliminar")
        self.btn_btn_eliminar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/iconosBlancos/Icons/iconos/Blanco/eliminar_blanco.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_btn_eliminar.setIcon(icon4)
        self.btn_btn_eliminar.setIconSize(QSize(16, 16))

        self.gridLayout_3.addWidget(self.btn_btn_eliminar, 0, 3, 1, 1)


        self.gridLayout_6.addLayout(self.gridLayout_3, 0, 1, 1, 1)

        self.contenedor_formulario = QFrame(self.contenedor)
        self.contenedor_formulario.setObjectName(u"contenedor_formulario")
        self.contenedor_formulario.setStyleSheet(u"")
        self.contenedor_formulario.setFrameShape(QFrame.Shape.StyledPanel)
        self.contenedor_formulario.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_4 = QGridLayout(self.contenedor_formulario)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.etiqueta_nombrepuesto = QLabel(self.contenedor_formulario)
        self.etiqueta_nombrepuesto.setObjectName(u"etiqueta_nombrepuesto")

        self.gridLayout_4.addWidget(self.etiqueta_nombrepuesto, 0, 0, 1, 1)

        self.txt_nombrepuesto = QLineEdit(self.contenedor_formulario)
        self.txt_nombrepuesto.setObjectName(u"txt_nombrepuesto")

        self.gridLayout_4.addWidget(self.txt_nombrepuesto, 0, 1, 1, 1)

        self.etiqueta_salario = QLabel(self.contenedor_formulario)
        self.etiqueta_salario.setObjectName(u"etiqueta_salario")

        self.gridLayout_4.addWidget(self.etiqueta_salario, 1, 0, 1, 1)

        self.decimal_salario = QDoubleSpinBox(self.contenedor_formulario)
        self.decimal_salario.setObjectName(u"decimal_salario")
        self.decimal_salario.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.decimal_salario.setMaximum(9999999999999999635896294965248.000000000000000)

        self.gridLayout_4.addWidget(self.decimal_salario, 1, 1, 1, 1)

        self.etiqueta_horas_laborales = QLabel(self.contenedor_formulario)
        self.etiqueta_horas_laborales.setObjectName(u"etiqueta_horas_laborales")

        self.gridLayout_4.addWidget(self.etiqueta_horas_laborales, 2, 0, 1, 1)

        self.decimal_horaslaborales = QDoubleSpinBox(self.contenedor_formulario)
        self.decimal_horaslaborales.setObjectName(u"decimal_horaslaborales")
        self.decimal_horaslaborales.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.decimal_horaslaborales.setMaximum(9999999999999999635896294965248.000000000000000)

        self.gridLayout_4.addWidget(self.decimal_horaslaborales, 2, 1, 1, 1)

        self.etiqueta_horaentrada = QLabel(self.contenedor_formulario)
        self.etiqueta_horaentrada.setObjectName(u"etiqueta_horaentrada")

        self.gridLayout_4.addWidget(self.etiqueta_horaentrada, 3, 0, 1, 1)

        self.tiempo_horaentrada = QTimeEdit(self.contenedor_formulario)
        self.tiempo_horaentrada.setObjectName(u"tiempo_horaentrada")
        self.tiempo_horaentrada.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.tiempo_horaentrada.setCalendarPopup(True)

        self.gridLayout_4.addWidget(self.tiempo_horaentrada, 3, 1, 1, 1)

        self.etiqueta_horasalida = QLabel(self.contenedor_formulario)
        self.etiqueta_horasalida.setObjectName(u"etiqueta_horasalida")

        self.gridLayout_4.addWidget(self.etiqueta_horasalida, 4, 0, 1, 1)

        self.tiempo_horasalida = QTimeEdit(self.contenedor_formulario)
        self.tiempo_horasalida.setObjectName(u"tiempo_horasalida")
        self.tiempo_horasalida.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.tiempo_horasalida.setCalendarPopup(True)

        self.gridLayout_4.addWidget(self.tiempo_horasalida, 4, 1, 1, 1)

        self.etiqueta_descripcion = QLabel(self.contenedor_formulario)
        self.etiqueta_descripcion.setObjectName(u"etiqueta_descripcion")

        self.gridLayout_4.addWidget(self.etiqueta_descripcion, 5, 0, 1, 1)

        self.txtlargo_descripcionpuesto = QPlainTextEdit(self.contenedor_formulario)
        self.txtlargo_descripcionpuesto.setObjectName(u"txtlargo_descripcionpuesto")

        self.gridLayout_4.addWidget(self.txtlargo_descripcionpuesto, 6, 0, 1, 2)

        self.etiqueta_seleciondepartamento = QLabel(self.contenedor_formulario)
        self.etiqueta_seleciondepartamento.setObjectName(u"etiqueta_seleciondepartamento")
        self.etiqueta_seleciondepartamento.setWordWrap(False)

        self.gridLayout_4.addWidget(self.etiqueta_seleciondepartamento, 7, 0, 1, 1)

        self.cajaOpciones_departamentos = QComboBox(self.contenedor_formulario)
        self.cajaOpciones_departamentos.setObjectName(u"cajaOpciones_departamentos")

        self.gridLayout_4.addWidget(self.cajaOpciones_departamentos, 7, 1, 1, 1)

        self.line = QFrame(self.contenedor_formulario)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_4.addWidget(self.line, 8, 0, 1, 2)

        self.etiqueta_diaslaborales = QLabel(self.contenedor_formulario)
        self.etiqueta_diaslaborales.setObjectName(u"etiqueta_diaslaborales")

        self.gridLayout_4.addWidget(self.etiqueta_diaslaborales, 9, 0, 1, 1)

        self.contenedor_diaslaborales = QFrame(self.contenedor_formulario)
        self.contenedor_diaslaborales.setObjectName(u"contenedor_diaslaborales")
        self.contenedor_diaslaborales.setFrameShape(QFrame.Shape.StyledPanel)
        self.contenedor_diaslaborales.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_5 = QGridLayout(self.contenedor_diaslaborales)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.cajaopcion_martes = QCheckBox(self.contenedor_diaslaborales)
        self.cajaopcion_martes.setObjectName(u"cajaopcion_martes")

        self.gridLayout_5.addWidget(self.cajaopcion_martes, 1, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer, 4, 0, 1, 1)

        self.cajaopcion_lunes = QCheckBox(self.contenedor_diaslaborales)
        self.cajaopcion_lunes.setObjectName(u"cajaopcion_lunes")

        self.gridLayout_5.addWidget(self.cajaopcion_lunes, 0, 0, 1, 1)

        self.cajaopcion_miercoles = QCheckBox(self.contenedor_diaslaborales)
        self.cajaopcion_miercoles.setObjectName(u"cajaopcion_miercoles")

        self.gridLayout_5.addWidget(self.cajaopcion_miercoles, 2, 0, 1, 1)

        self.cajaopcion_jueves = QCheckBox(self.contenedor_diaslaborales)
        self.cajaopcion_jueves.setObjectName(u"cajaopcion_jueves")

        self.gridLayout_5.addWidget(self.cajaopcion_jueves, 0, 1, 1, 1)

        self.cajaopcion_viernes = QCheckBox(self.contenedor_diaslaborales)
        self.cajaopcion_viernes.setObjectName(u"cajaopcion_viernes")

        self.gridLayout_5.addWidget(self.cajaopcion_viernes, 1, 1, 1, 1)

        self.cajaopcion_sabado = QCheckBox(self.contenedor_diaslaborales)
        self.cajaopcion_sabado.setObjectName(u"cajaopcion_sabado")

        self.gridLayout_5.addWidget(self.cajaopcion_sabado, 2, 1, 1, 1)

        self.cajaopcion_domingo = QCheckBox(self.contenedor_diaslaborales)
        self.cajaopcion_domingo.setObjectName(u"cajaopcion_domingo")

        self.gridLayout_5.addWidget(self.cajaopcion_domingo, 0, 2, 1, 1)


        self.gridLayout_4.addWidget(self.contenedor_diaslaborales, 10, 0, 1, 2)

        self.btn_btn_roles = QPushButton(self.contenedor_formulario)
        self.btn_btn_roles.setObjectName(u"btn_btn_roles")
        self.btn_btn_roles.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout_4.addWidget(self.btn_btn_roles, 11, 0, 1, 1)


        self.gridLayout_6.addWidget(self.contenedor_formulario, 1, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.contenedor, 1, 0, 1, 1)


        self.gridLayout_7.addWidget(self.contenedor_frame_2, 0, 0, 1, 1)

        QWidget.setTabOrder(self.txt_nombrepuesto, self.decimal_salario)
        QWidget.setTabOrder(self.decimal_salario, self.decimal_horaslaborales)
        QWidget.setTabOrder(self.decimal_horaslaborales, self.tiempo_horaentrada)
        QWidget.setTabOrder(self.tiempo_horaentrada, self.tiempo_horasalida)
        QWidget.setTabOrder(self.tiempo_horasalida, self.txtlargo_descripcionpuesto)
        QWidget.setTabOrder(self.txtlargo_descripcionpuesto, self.cajaOpciones_departamentos)
        QWidget.setTabOrder(self.cajaOpciones_departamentos, self.cajaopcion_lunes)
        QWidget.setTabOrder(self.cajaopcion_lunes, self.cajaopcion_martes)
        QWidget.setTabOrder(self.cajaopcion_martes, self.cajaopcion_miercoles)
        QWidget.setTabOrder(self.cajaopcion_miercoles, self.cajaopcion_jueves)
        QWidget.setTabOrder(self.cajaopcion_jueves, self.cajaopcion_viernes)
        QWidget.setTabOrder(self.cajaopcion_viernes, self.cajaopcion_sabado)
        QWidget.setTabOrder(self.cajaopcion_sabado, self.cajaopcion_domingo)
        QWidget.setTabOrder(self.cajaopcion_domingo, self.btn_btn_roles)
        QWidget.setTabOrder(self.btn_btn_roles, self.txt_buscarpuesto)
        QWidget.setTabOrder(self.txt_buscarpuesto, self.tabla_listapuestos)

        self.retranslateUi(Formulario_puestos)

        QMetaObject.connectSlotsByName(Formulario_puestos)
    # setupUi

    def retranslateUi(self, Formulario_puestos):
        Formulario_puestos.setWindowTitle(QCoreApplication.translate("Formulario_puestos", u"Form", None))
        self.etiquetaTitulo_administrarpuestos.setText(QCoreApplication.translate("Formulario_puestos", u"PUESTOS", None))
        self.btn_cerrar.setText("")
        self.etiqueta_puestosexistentes.setText(QCoreApplication.translate("Formulario_puestos", u"Puestos Existentes", None))
        self.txt_buscarpuesto.setPlaceholderText(QCoreApplication.translate("Formulario_puestos", u"Nombre del puesto", None))
        self.btn_btn_limpiar.setText("")
#if QT_CONFIG(accessibility)
        self.btn_btn_agregar.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        self.btn_btn_agregar.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.btn_btn_agregar.setText(QCoreApplication.translate("Formulario_puestos", u"Agregar", None))
        self.btn_btn_actualizar.setText(QCoreApplication.translate("Formulario_puestos", u"Actualizar", None))
        self.btn_btn_eliminar.setText(QCoreApplication.translate("Formulario_puestos", u"Eliminar", None))
        self.etiqueta_nombrepuesto.setText(QCoreApplication.translate("Formulario_puestos", u"Nombre:", None))
        self.txt_nombrepuesto.setPlaceholderText(QCoreApplication.translate("Formulario_puestos", u"Nombre", None))
        self.etiqueta_salario.setText(QCoreApplication.translate("Formulario_puestos", u"Salario:", None))
        self.etiqueta_horas_laborales.setText(QCoreApplication.translate("Formulario_puestos", u"Horas laborales:", None))
        self.etiqueta_horaentrada.setText(QCoreApplication.translate("Formulario_puestos", u"Hora entrada", None))
        self.etiqueta_horasalida.setText(QCoreApplication.translate("Formulario_puestos", u"Hora salida", None))
        self.etiqueta_descripcion.setText(QCoreApplication.translate("Formulario_puestos", u"Descripci\u00f3n del puesto", None))
        self.etiqueta_seleciondepartamento.setText(QCoreApplication.translate("Formulario_puestos", u"Asignaci\u00f3n del departamento:", None))
        self.etiqueta_diaslaborales.setText(QCoreApplication.translate("Formulario_puestos", u"Dias laborales:", None))
        self.cajaopcion_martes.setText(QCoreApplication.translate("Formulario_puestos", u"Martes", None))
        self.cajaopcion_lunes.setText(QCoreApplication.translate("Formulario_puestos", u"Lunes", None))
        self.cajaopcion_miercoles.setText(QCoreApplication.translate("Formulario_puestos", u"Miercoles", None))
        self.cajaopcion_jueves.setText(QCoreApplication.translate("Formulario_puestos", u"Jueves", None))
        self.cajaopcion_viernes.setText(QCoreApplication.translate("Formulario_puestos", u"Viernes", None))
        self.cajaopcion_sabado.setText(QCoreApplication.translate("Formulario_puestos", u"Sabado", None))
        self.cajaopcion_domingo.setText(QCoreApplication.translate("Formulario_puestos", u"Domingo", None))
        self.btn_btn_roles.setText(QCoreApplication.translate("Formulario_puestos", u"Grupos", None))
    # retranslateUi

