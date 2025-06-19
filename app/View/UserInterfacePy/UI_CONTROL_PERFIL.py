# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UI_CONTROL_PERFIL.ui'
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
    QDoubleSpinBox, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QPlainTextEdit,
    QPushButton, QSizePolicy, QSpacerItem, QTimeEdit,
    QToolButton, QWidget)
from ...Source import ibootstrap_rc
from ...Source import iconosSVG_rc

class Ui_Formulario_Datos_Empleado(object):
    def setupUi(self, Formulario_Datos_Empleado):
        if not Formulario_Datos_Empleado.objectName():
            Formulario_Datos_Empleado.setObjectName(u"Formulario_Datos_Empleado")
        Formulario_Datos_Empleado.resize(1101, 772)
        Formulario_Datos_Empleado.setStyleSheet(u"#Formulario_Datos_Empleado{\n"
"background-color: #fffefb;\n"
"}\n"
"[objectName*=\"contenedor\"]{\n"
"background: #fffefb;\n"
"}\n"
"#contenedor_baja{\n"
"background:#EE1D52;\n"
"border-radius:5px;\n"
"}\n"
"#label_wp_titulo_usuario{\n"
"color:#1d1c1c;\n"
"background-color: #fffefb;\n"
"font-size: 24px;\n"
"font-weight: bold;\n"
"padding-left: 5px;\n"
"text-transform: uppercase;\n"
"font-family: \"Arial\";\n"
"padding-top: 5px;\n"
"}\n"
"#tarjeta_usuario{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.818455, y2:0.824, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(5, 95, 212, 219));\n"
"border-radius: 12px;\n"
"}\n"
"[objectName*=\"btn_btn_\"]{\n"
"font-family: Arial;\n"
"font-size: 14px;\n"
"font-weight: bold;\n"
"color: rgb(29, 28, 28);\n"
"min-height: 30px;\n"
"border-radius: 5px;\n"
"background-color: #00619a;\n"
"text-align: center;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"}\n"
"[objectName*=\"btn_btn_aceptar\"]{\n"
"background-color:#00619a;\n"
"	color: rgb(245, 244, 241);\n"
""
                        "}\n"
"[objectName*=\"btn_btn_aceptar\"]:hover{\n"
"background-color: #68a67d;\n"
"}\n"
"[objectName*=\"etiquetaTitulo\"]{\n"
"font-family: Arial;\n"
"font-size: 16px;\n"
"font-weight: bold;\n"
"max-height:17px;\n"
"}\n"
"[objectName*=\"etiqueta_\"]{\n"
"font-family: Arial;\n"
"font-size: 12px;\n"
"font-weight:bold;\n"
"text-transform: capitalize;\n"
"}\n"
"[objectName*=\"etiquetaTituloDato_\"]{\n"
"font-family: Arial;\n"
"font-size: 18px;\n"
"font-weight:bold;\n"
"color: rgb(0, 0, 0);\n"
"}\n"
"[objectName*=\"etiquetaDato_\"]{\n"
"font-family: Arial;\n"
"font-size: 17px;\n"
"font-weight:bold;\n"
"color: rgb(65, 65, 65);\n"
"}\n"
"[objectName*=\"txt_\"]{\n"
"background-color: rgb(245, 244, 241);\n"
"color: rgb(29, 28, 28);\n"
"border: none;\n"
"border-bottom: 1px solid;\n"
"border-radius: 5px;\n"
"font-size: 12px;\n"
"font-family: Arial;\n"
"}\n"
"[objectName^=\"txt_\"]::focus{\n"
"border-bottom: 2px solid #00668c;\n"
"}\n"
"[objectName^=\"fecha_\"]{\n"
"border: none;\n"
"border-bottom: 1px solid #3b3c3d;\n"
"b"
                        "order-radius: 5px;\n"
"padding: 2px;\n"
"background-color: #f5f4f1;\n"
"font-size: 12px;\n"
"width:87px;\n"
"}\n"
"[objectName^=\"fecha_\"]::drop-down{\n"
"subcontrol-origin: padding;\n"
"subcontrol-position: top right;\n"
"padding-right:5px;\n"
"width: 20%;\n"
"border-left-width: 1px;\n"
"border-radius: 5px;\n"
"background-color: #f5f4f1;\n"
"}\n"
"*[objectName^=\"fecha_\"]::down-arrow{\n"
"image: url(:/Icons/Bootstrap/calendar2-date.svg);\n"
"padding-left:5px;\n"
"padding-right:5px;\n"
"}\n"
"*[objectName^=\"fecha_\"]::focus{\n"
"border-bottom: 2px solid #00668c;\n"
"}\n"
"#fecha_baja{\n"
"background: transparent;\n"
"color:#fffefb;\n"
"border:none;\n"
"}\n"
"[objectName^=\"cajaopciones_\"]{\n"
"border: none;\n"
"border-bottom: 1px solid rgb(29, 28, 28);\n"
"border-radius: 5px;\n"
"padding: 2px;\n"
"background-color: #f5f4f1;\n"
"border-radius: 5px;\n"
"font-size: 12px;\n"
"width:87px;\n"
"}\n"
"[objectName^=\"cajaopciones_\"]::drop-down{\n"
"subcontrol-origin: padding;\n"
"subcontrol-position: top right;\n"
""
                        "padding-right:5px;\n"
"width: 20%;\n"
"border-left-width: 1px;\n"
"border-radius: 5px;\n"
"background-color: #f5f4f1;\n"
"}\n"
"[objectName^=\"cajaopciones_\"]::down-arrow{\n"
"image: url(:/Icons/Bootstrap/filter-left.svg);\n"
"padding-left:5px;\n"
"padding-right:5px;\n"
"}\n"
"[objectName*=\"numerodecimal_\"]{\n"
"background-color: rgb(245, 244, 241);\n"
"color: rgb(29, 28, 28);\n"
"border: none;\n"
"border-bottom: 1px solid;\n"
"border-radius: 5px;\n"
"font-size: 12px;\n"
"font-family: Arial;\n"
"}\n"
"[objectName^=\"numerodecimal_\"]::focus{\n"
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
"[objectName*=\"txtlargo_\"]{\n"
"background-color: rgb(245, 244, 241);\n"
"color: rgb(29, 28, 28);\n"
"border: none;\n"
""
                        "border-bottom: 1px solid;\n"
"border-radius: 5px;\n"
"font-size: 12px;\n"
"font-family: Arial;\n"
"max-height: 60px;\n"
"}\n"
"[objectName^=\"txtlargo\"]::focus{\n"
"border-bottom: 2px solid #00668c;\n"
"}\n"
"")
        self.gridLayout_6 = QGridLayout(Formulario_Datos_Empleado)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setVerticalSpacing(0)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.contenedor = QFrame(Formulario_Datos_Empleado)
        self.contenedor.setObjectName(u"contenedor")
        self.contenedor.setFrameShape(QFrame.StyledPanel)
        self.contenedor.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.contenedor)
        self.gridLayout_7.setSpacing(0)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(5, 0, 5, 5)
        self.widget_2 = QWidget(self.contenedor)
        self.widget_2.setObjectName(u"widget_2")
        self.gridLayout_4 = QGridLayout(self.widget_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.horizontalSpacer_2 = QSpacerItem(200, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_2, 1, 1, 1, 1)

        self.widget_3 = QWidget(self.widget_2)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(350, 0))
        self.widget_3.setMaximumSize(QSize(300, 16777215))
        self.gridLayout_3 = QGridLayout(self.widget_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(0)
        self.gridLayout_3.setVerticalSpacing(5)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.contenedor_baja = QFrame(self.widget_3)
        self.contenedor_baja.setObjectName(u"contenedor_baja")
        self.contenedor_baja.setFrameShape(QFrame.StyledPanel)
        self.contenedor_baja.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.contenedor_baja)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.etiqueta_baja = QLabel(self.contenedor_baja)
        self.etiqueta_baja.setObjectName(u"etiqueta_baja")

        self.horizontalLayout_3.addWidget(self.etiqueta_baja, 0, Qt.AlignHCenter)

        self.fecha_baja = QDateEdit(self.contenedor_baja)
        self.fecha_baja.setObjectName(u"fecha_baja")
        self.fecha_baja.setEnabled(False)

        self.horizontalLayout_3.addWidget(self.fecha_baja)


        self.gridLayout_3.addWidget(self.contenedor_baja, 0, 1, 1, 1)

        self.tarjeta_usuario = QWidget(self.widget_3)
        self.tarjeta_usuario.setObjectName(u"tarjeta_usuario")
        self.tarjeta_usuario.setMinimumSize(QSize(250, 100))
        self.tarjeta_usuario.setMaximumSize(QSize(400, 177))
        self.tarjeta_usuario.setStyleSheet(u"")
        self.gridLayout_2 = QGridLayout(self.tarjeta_usuario)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(10)
        self.gridLayout_2.setContentsMargins(10, 10, 10, 10)
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 2, 1, 1, 1)

        self.etiquetaDato_nombre = QLabel(self.tarjeta_usuario)
        self.etiquetaDato_nombre.setObjectName(u"etiquetaDato_nombre")
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setBold(True)
        self.etiquetaDato_nombre.setFont(font)
        self.etiquetaDato_nombre.setStyleSheet(u"")
        self.etiquetaDato_nombre.setWordWrap(True)

        self.gridLayout_2.addWidget(self.etiquetaDato_nombre, 1, 1, 1, 1)

        self.etiquetaTituloDato_nombre = QLabel(self.tarjeta_usuario)
        self.etiquetaTituloDato_nombre.setObjectName(u"etiquetaTituloDato_nombre")
        self.etiquetaTituloDato_nombre.setFont(font)
        self.etiquetaTituloDato_nombre.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.etiquetaTituloDato_nombre, 0, 1, 1, 1)

        self.label = QLabel(self.tarjeta_usuario)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"image: url(:/Icons/Bootstrap/person-circle.svg);\n"
"background:none;")
        self.label.setScaledContents(True)

        self.gridLayout_2.addWidget(self.label, 0, 0, 3, 1)


        self.gridLayout_3.addWidget(self.tarjeta_usuario, 1, 0, 1, 2)

        self.frame_4 = QFrame(self.widget_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 0))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_4)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.fecha_contrato = QDateEdit(self.frame_4)
        self.fecha_contrato.setObjectName(u"fecha_contrato")
        self.fecha_contrato.setEnabled(False)
        self.fecha_contrato.setCalendarPopup(True)

        self.gridLayout_5.addWidget(self.fecha_contrato, 7, 1, 1, 2)

        self.numerodecimal_salario = QDoubleSpinBox(self.frame_4)
        self.numerodecimal_salario.setObjectName(u"numerodecimal_salario")
        self.numerodecimal_salario.setEnabled(False)

        self.gridLayout_5.addWidget(self.numerodecimal_salario, 5, 1, 1, 1)

        self.etiqueta_horastrabajo = QLabel(self.frame_4)
        self.etiqueta_horastrabajo.setObjectName(u"etiqueta_horastrabajo")

        self.gridLayout_5.addWidget(self.etiqueta_horastrabajo, 5, 2, 1, 1)

        self.etiqueta_horaentrada = QLabel(self.frame_4)
        self.etiqueta_horaentrada.setObjectName(u"etiqueta_horaentrada")

        self.gridLayout_5.addWidget(self.etiqueta_horaentrada, 6, 0, 1, 1)

        self.etiqueta_departamento = QLabel(self.frame_4)
        self.etiqueta_departamento.setObjectName(u"etiqueta_departamento")

        self.gridLayout_5.addWidget(self.etiqueta_departamento, 3, 0, 1, 1)

        self.line_3 = QFrame(self.frame_4)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_5.addWidget(self.line_3, 0, 0, 1, 4)

        self.etiqueta_puesto = QLabel(self.frame_4)
        self.etiqueta_puesto.setObjectName(u"etiqueta_puesto")

        self.gridLayout_5.addWidget(self.etiqueta_puesto, 4, 0, 1, 1)

        self.etiquetaTitulo_datosempleo = QLabel(self.frame_4)
        self.etiquetaTitulo_datosempleo.setObjectName(u"etiquetaTitulo_datosempleo")

        self.gridLayout_5.addWidget(self.etiquetaTitulo_datosempleo, 1, 0, 1, 4)

        self.etiqueta_sucursal = QLabel(self.frame_4)
        self.etiqueta_sucursal.setObjectName(u"etiqueta_sucursal")

        self.gridLayout_5.addWidget(self.etiqueta_sucursal, 2, 0, 1, 1)

        self.numerodecimal_horastrabajo = QDoubleSpinBox(self.frame_4)
        self.numerodecimal_horastrabajo.setObjectName(u"numerodecimal_horastrabajo")
        self.numerodecimal_horastrabajo.setEnabled(False)

        self.gridLayout_5.addWidget(self.numerodecimal_horastrabajo, 5, 3, 1, 1)

        self.tiempo_horaentrada = QTimeEdit(self.frame_4)
        self.tiempo_horaentrada.setObjectName(u"tiempo_horaentrada")
        self.tiempo_horaentrada.setEnabled(False)

        self.gridLayout_5.addWidget(self.tiempo_horaentrada, 6, 1, 1, 1)

        self.etiqueta_horasalida = QLabel(self.frame_4)
        self.etiqueta_horasalida.setObjectName(u"etiqueta_horasalida")

        self.gridLayout_5.addWidget(self.etiqueta_horasalida, 6, 2, 1, 1)

        self.etiqueta_salario = QLabel(self.frame_4)
        self.etiqueta_salario.setObjectName(u"etiqueta_salario")

        self.gridLayout_5.addWidget(self.etiqueta_salario, 5, 0, 1, 1)

        self.tiempo_horasalida = QTimeEdit(self.frame_4)
        self.tiempo_horasalida.setObjectName(u"tiempo_horasalida")
        self.tiempo_horasalida.setEnabled(False)

        self.gridLayout_5.addWidget(self.tiempo_horasalida, 6, 3, 1, 1)

        self.etiqueta_descripcionpuesto = QLabel(self.frame_4)
        self.etiqueta_descripcionpuesto.setObjectName(u"etiqueta_descripcionpuesto")

        self.gridLayout_5.addWidget(self.etiqueta_descripcionpuesto, 8, 0, 1, 4)

        self.txtlargo_descripcionpuesto = QPlainTextEdit(self.frame_4)
        self.txtlargo_descripcionpuesto.setObjectName(u"txtlargo_descripcionpuesto")
        self.txtlargo_descripcionpuesto.setEnabled(False)
        self.txtlargo_descripcionpuesto.setMaximumSize(QSize(16777215, 61))

        self.gridLayout_5.addWidget(self.txtlargo_descripcionpuesto, 9, 0, 1, 4)

        self.etiqueta_fechacontrato = QLabel(self.frame_4)
        self.etiqueta_fechacontrato.setObjectName(u"etiqueta_fechacontrato")

        self.gridLayout_5.addWidget(self.etiqueta_fechacontrato, 7, 0, 1, 1)

        self.line_2 = QFrame(self.frame_4)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_5.addWidget(self.line_2, 10, 0, 1, 4)

        self.etiquetaTitulo_datosusuario = QLabel(self.frame_4)
        self.etiquetaTitulo_datosusuario.setObjectName(u"etiquetaTitulo_datosusuario")

        self.gridLayout_5.addWidget(self.etiquetaTitulo_datosusuario, 11, 0, 1, 4)

        self.txt_password = QLineEdit(self.frame_4)
        self.txt_password.setObjectName(u"txt_password")
        self.txt_password.setEnabled(False)
        self.txt_password.setEchoMode(QLineEdit.PasswordEchoOnEdit)

        self.gridLayout_5.addWidget(self.txt_password, 13, 2, 1, 2)

        self.etiqueta_usuario = QLabel(self.frame_4)
        self.etiqueta_usuario.setObjectName(u"etiqueta_usuario")

        self.gridLayout_5.addWidget(self.etiqueta_usuario, 12, 0, 1, 1)

        self.txt_usuario = QLineEdit(self.frame_4)
        self.txt_usuario.setObjectName(u"txt_usuario")
        self.txt_usuario.setEnabled(False)

        self.gridLayout_5.addWidget(self.txt_usuario, 12, 2, 1, 2)

        self.etiqueta_password = QLabel(self.frame_4)
        self.etiqueta_password.setObjectName(u"etiqueta_password")

        self.gridLayout_5.addWidget(self.etiqueta_password, 13, 0, 1, 1)

        self.cajaopciones_puestos = QComboBox(self.frame_4)
        self.cajaopciones_puestos.setObjectName(u"cajaopciones_puestos")
        self.cajaopciones_puestos.setEnabled(False)
        self.cajaopciones_puestos.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.gridLayout_5.addWidget(self.cajaopciones_puestos, 4, 1, 1, 3)

        self.cajaopciones_departamentos = QComboBox(self.frame_4)
        self.cajaopciones_departamentos.setObjectName(u"cajaopciones_departamentos")
        self.cajaopciones_departamentos.setEnabled(False)
        self.cajaopciones_departamentos.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.gridLayout_5.addWidget(self.cajaopciones_departamentos, 3, 1, 1, 3)

        self.cajaopciones_sucursales = QComboBox(self.frame_4)
        self.cajaopciones_sucursales.setObjectName(u"cajaopciones_sucursales")
        self.cajaopciones_sucursales.setEnabled(False)
        self.cajaopciones_sucursales.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.gridLayout_5.addWidget(self.cajaopciones_sucursales, 2, 1, 1, 3)


        self.gridLayout_3.addWidget(self.frame_4, 2, 0, 1, 2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_2, 3, 0, 1, 1)


        self.gridLayout_4.addWidget(self.widget_3, 0, 2, 2, 1, Qt.AlignRight)

        self.contenedorIzquierdo = QFrame(self.widget_2)
        self.contenedorIzquierdo.setObjectName(u"contenedorIzquierdo")
        self.contenedorIzquierdo.setMinimumSize(QSize(0, 0))
        self.contenedorIzquierdo.setMaximumSize(QSize(16777215, 16777215))
        self.contenedorIzquierdo.setFrameShape(QFrame.StyledPanel)
        self.contenedorIzquierdo.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.contenedorIzquierdo)
        self.gridLayout.setObjectName(u"gridLayout")
        self.etiqueta_diaslaborales_2 = QGroupBox(self.contenedorIzquierdo)
        self.etiqueta_diaslaborales_2.setObjectName(u"etiqueta_diaslaborales_2")
        self.etiqueta_diaslaborales_2.setEnabled(False)
        self.gridLayout_8 = QGridLayout(self.etiqueta_diaslaborales_2)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.opcion_lunes = QCheckBox(self.etiqueta_diaslaborales_2)
        self.opcion_lunes.setObjectName(u"opcion_lunes")

        self.gridLayout_8.addWidget(self.opcion_lunes, 0, 0, 1, 1)

        self.opcion_miercoles = QCheckBox(self.etiqueta_diaslaborales_2)
        self.opcion_miercoles.setObjectName(u"opcion_miercoles")

        self.gridLayout_8.addWidget(self.opcion_miercoles, 0, 1, 1, 1)

        self.opcion_viernes = QCheckBox(self.etiqueta_diaslaborales_2)
        self.opcion_viernes.setObjectName(u"opcion_viernes")

        self.gridLayout_8.addWidget(self.opcion_viernes, 0, 2, 1, 1)

        self.opcion_domingo = QCheckBox(self.etiqueta_diaslaborales_2)
        self.opcion_domingo.setObjectName(u"opcion_domingo")

        self.gridLayout_8.addWidget(self.opcion_domingo, 0, 3, 1, 1)

        self.opcion_martes = QCheckBox(self.etiqueta_diaslaborales_2)
        self.opcion_martes.setObjectName(u"opcion_martes")

        self.gridLayout_8.addWidget(self.opcion_martes, 1, 0, 1, 1)

        self.opcion_jueves = QCheckBox(self.etiqueta_diaslaborales_2)
        self.opcion_jueves.setObjectName(u"opcion_jueves")

        self.gridLayout_8.addWidget(self.opcion_jueves, 1, 1, 1, 1)

        self.opcion_sabado = QCheckBox(self.etiqueta_diaslaborales_2)
        self.opcion_sabado.setObjectName(u"opcion_sabado")

        self.gridLayout_8.addWidget(self.opcion_sabado, 1, 2, 1, 1)


        self.gridLayout.addWidget(self.etiqueta_diaslaborales_2, 19, 0, 1, 4)

        self.txt_codigopostal = QLineEdit(self.contenedorIzquierdo)
        self.txt_codigopostal.setObjectName(u"txt_codigopostal")
        self.txt_codigopostal.setEnabled(False)

        self.gridLayout.addWidget(self.txt_codigopostal, 9, 1, 1, 1)

        self.etiqueta_pais = QLabel(self.contenedorIzquierdo)
        self.etiqueta_pais.setObjectName(u"etiqueta_pais")

        self.gridLayout.addWidget(self.etiqueta_pais, 11, 2, 1, 1)

        self.txt_avenidas = QLineEdit(self.contenedorIzquierdo)
        self.txt_avenidas.setObjectName(u"txt_avenidas")
        self.txt_avenidas.setEnabled(False)

        self.gridLayout.addWidget(self.txt_avenidas, 11, 1, 1, 1)

        self.txt_colonia = QLineEdit(self.contenedorIzquierdo)
        self.txt_colonia.setObjectName(u"txt_colonia")
        self.txt_colonia.setEnabled(False)

        self.gridLayout.addWidget(self.txt_colonia, 10, 3, 1, 1)

        self.etiqueta_calles = QLabel(self.contenedorIzquierdo)
        self.etiqueta_calles.setObjectName(u"etiqueta_calles")

        self.gridLayout.addWidget(self.etiqueta_calles, 9, 2, 1, 1)

        self.etiqueta_telefono = QLabel(self.contenedorIzquierdo)
        self.etiqueta_telefono.setObjectName(u"etiqueta_telefono")

        self.gridLayout.addWidget(self.etiqueta_telefono, 10, 0, 1, 1)

        self.txt_numerotelefono = QLineEdit(self.contenedorIzquierdo)
        self.txt_numerotelefono.setObjectName(u"txt_numerotelefono")
        self.txt_numerotelefono.setEnabled(False)

        self.gridLayout.addWidget(self.txt_numerotelefono, 10, 1, 1, 1)

        self.etiqueta_nexterior = QLabel(self.contenedorIzquierdo)
        self.etiqueta_nexterior.setObjectName(u"etiqueta_nexterior")

        self.gridLayout.addWidget(self.etiqueta_nexterior, 12, 0, 1, 1)

        self.etiqueta_colonia = QLabel(self.contenedorIzquierdo)
        self.etiqueta_colonia.setObjectName(u"etiqueta_colonia")

        self.gridLayout.addWidget(self.etiqueta_colonia, 10, 2, 1, 1)

        self.txt_calles = QLineEdit(self.contenedorIzquierdo)
        self.txt_calles.setObjectName(u"txt_calles")
        self.txt_calles.setEnabled(False)

        self.gridLayout.addWidget(self.txt_calles, 9, 3, 1, 1)

        self.txt_numeroexterior = QLineEdit(self.contenedorIzquierdo)
        self.txt_numeroexterior.setObjectName(u"txt_numeroexterior")
        self.txt_numeroexterior.setEnabled(False)

        self.gridLayout.addWidget(self.txt_numeroexterior, 12, 1, 1, 1)

        self.etiqueta_numinterior = QLabel(self.contenedorIzquierdo)
        self.etiqueta_numinterior.setObjectName(u"etiqueta_numinterior")

        self.gridLayout.addWidget(self.etiqueta_numinterior, 12, 2, 1, 1)

        self.txt_numerointerior = QLineEdit(self.contenedorIzquierdo)
        self.txt_numerointerior.setObjectName(u"txt_numerointerior")
        self.txt_numerointerior.setEnabled(False)

        self.gridLayout.addWidget(self.txt_numerointerior, 12, 3, 1, 1)

        self.txtlargo_referenciadireccion = QPlainTextEdit(self.contenedorIzquierdo)
        self.txtlargo_referenciadireccion.setObjectName(u"txtlargo_referenciadireccion")
        self.txtlargo_referenciadireccion.setEnabled(False)
        self.txtlargo_referenciadireccion.setMaximumSize(QSize(16777215, 61))
        self.txtlargo_referenciadireccion.setTabChangesFocus(False)
        self.txtlargo_referenciadireccion.setTabStopWidth(80)
        self.txtlargo_referenciadireccion.setBackgroundVisible(False)
        self.txtlargo_referenciadireccion.setCenterOnScroll(False)

        self.gridLayout.addWidget(self.txtlargo_referenciadireccion, 14, 0, 1, 4)

        self.etiqueta_avenidas = QLabel(self.contenedorIzquierdo)
        self.etiqueta_avenidas.setObjectName(u"etiqueta_avenidas")

        self.gridLayout.addWidget(self.etiqueta_avenidas, 11, 0, 1, 1)

        self.line_4 = QFrame(self.contenedorIzquierdo)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_4, 15, 0, 1, 4)

        self.etiquetaTitulo_referencias = QLabel(self.contenedorIzquierdo)
        self.etiquetaTitulo_referencias.setObjectName(u"etiquetaTitulo_referencias")
        self.etiquetaTitulo_referencias.setWordWrap(True)

        self.gridLayout.addWidget(self.etiquetaTitulo_referencias, 13, 0, 1, 2)

        self.etiquetaTitulo_contactoemergencia = QLabel(self.contenedorIzquierdo)
        self.etiquetaTitulo_contactoemergencia.setObjectName(u"etiquetaTitulo_contactoemergencia")

        self.gridLayout.addWidget(self.etiquetaTitulo_contactoemergencia, 16, 0, 1, 4)

        self.etiqueta_nombrecontactoemergencia = QLabel(self.contenedorIzquierdo)
        self.etiqueta_nombrecontactoemergencia.setObjectName(u"etiqueta_nombrecontactoemergencia")

        self.gridLayout.addWidget(self.etiqueta_nombrecontactoemergencia, 17, 0, 1, 1)

        self.txt_pais = QLineEdit(self.contenedorIzquierdo)
        self.txt_pais.setObjectName(u"txt_pais")
        self.txt_pais.setEnabled(False)

        self.gridLayout.addWidget(self.txt_pais, 11, 3, 1, 1)

        self.txt_nombrecontactoemergencia = QLineEdit(self.contenedorIzquierdo)
        self.txt_nombrecontactoemergencia.setObjectName(u"txt_nombrecontactoemergencia")
        self.txt_nombrecontactoemergencia.setEnabled(False)

        self.gridLayout.addWidget(self.txt_nombrecontactoemergencia, 17, 1, 1, 1)

        self.etiqueta_numtelefonocontactoemergencia = QLabel(self.contenedorIzquierdo)
        self.etiqueta_numtelefonocontactoemergencia.setObjectName(u"etiqueta_numtelefonocontactoemergencia")

        self.gridLayout.addWidget(self.etiqueta_numtelefonocontactoemergencia, 18, 0, 1, 1)

        self.txt_numtelefonocontactoemergencia = QLineEdit(self.contenedorIzquierdo)
        self.txt_numtelefonocontactoemergencia.setObjectName(u"txt_numtelefonocontactoemergencia")
        self.txt_numtelefonocontactoemergencia.setEnabled(False)

        self.gridLayout.addWidget(self.txt_numtelefonocontactoemergencia, 18, 1, 1, 1)

        self.etiqueta_parentescocontactoemergencia = QLabel(self.contenedorIzquierdo)
        self.etiqueta_parentescocontactoemergencia.setObjectName(u"etiqueta_parentescocontactoemergencia")

        self.gridLayout.addWidget(self.etiqueta_parentescocontactoemergencia, 18, 2, 1, 1)

        self.cajaopciones_parentescocontactoemergencia = QComboBox(self.contenedorIzquierdo)
        self.cajaopciones_parentescocontactoemergencia.addItem("")
        self.cajaopciones_parentescocontactoemergencia.addItem("")
        self.cajaopciones_parentescocontactoemergencia.addItem("")
        self.cajaopciones_parentescocontactoemergencia.addItem("")
        self.cajaopciones_parentescocontactoemergencia.addItem("")
        self.cajaopciones_parentescocontactoemergencia.setObjectName(u"cajaopciones_parentescocontactoemergencia")
        self.cajaopciones_parentescocontactoemergencia.setEnabled(False)
        self.cajaopciones_parentescocontactoemergencia.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.gridLayout.addWidget(self.cajaopciones_parentescocontactoemergencia, 18, 3, 1, 1)

        self.etiquetaTitulo_datospersonales = QLabel(self.contenedorIzquierdo)
        self.etiquetaTitulo_datospersonales.setObjectName(u"etiquetaTitulo_datospersonales")
        self.etiquetaTitulo_datospersonales.setFont(font)

        self.gridLayout.addWidget(self.etiquetaTitulo_datospersonales, 0, 0, 1, 2)

        self.line = QFrame(self.contenedorIzquierdo)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line, 6, 0, 1, 4)

        self.txt_rfc = QLineEdit(self.contenedorIzquierdo)
        self.txt_rfc.setObjectName(u"txt_rfc")
        self.txt_rfc.setEnabled(False)

        self.gridLayout.addWidget(self.txt_rfc, 5, 1, 1, 1)

        self.etiqueta_apellidopaterno = QLabel(self.contenedorIzquierdo)
        self.etiqueta_apellidopaterno.setObjectName(u"etiqueta_apellidopaterno")

        self.gridLayout.addWidget(self.etiqueta_apellidopaterno, 1, 2, 1, 1)

        self.etiqueta_apellidomaterno = QLabel(self.contenedorIzquierdo)
        self.etiqueta_apellidomaterno.setObjectName(u"etiqueta_apellidomaterno")

        self.gridLayout.addWidget(self.etiqueta_apellidomaterno, 2, 0, 1, 1)

        self.etiqueta_nombre = QLabel(self.contenedorIzquierdo)
        self.etiqueta_nombre.setObjectName(u"etiqueta_nombre")

        self.gridLayout.addWidget(self.etiqueta_nombre, 1, 0, 1, 1)

        self.txt_apellidomaterno = QLineEdit(self.contenedorIzquierdo)
        self.txt_apellidomaterno.setObjectName(u"txt_apellidomaterno")
        self.txt_apellidomaterno.setEnabled(False)

        self.gridLayout.addWidget(self.txt_apellidomaterno, 2, 1, 1, 1)

        self.txt_nombre = QLineEdit(self.contenedorIzquierdo)
        self.txt_nombre.setObjectName(u"txt_nombre")
        self.txt_nombre.setEnabled(False)

        self.gridLayout.addWidget(self.txt_nombre, 1, 1, 1, 1)

        self.etiqueta_estadocivil = QLabel(self.contenedorIzquierdo)
        self.etiqueta_estadocivil.setObjectName(u"etiqueta_estadocivil")

        self.gridLayout.addWidget(self.etiqueta_estadocivil, 3, 2, 1, 1)

        self.txt_apellidopaterno = QLineEdit(self.contenedorIzquierdo)
        self.txt_apellidopaterno.setObjectName(u"txt_apellidopaterno")
        self.txt_apellidopaterno.setEnabled(False)

        self.gridLayout.addWidget(self.txt_apellidopaterno, 1, 3, 1, 1)

        self.etiqueta_numerosegurosocial = QLabel(self.contenedorIzquierdo)
        self.etiqueta_numerosegurosocial.setObjectName(u"etiqueta_numerosegurosocial")

        self.gridLayout.addWidget(self.etiqueta_numerosegurosocial, 3, 0, 1, 1)

        self.cajaopciones_estadosocial = QComboBox(self.contenedorIzquierdo)
        self.cajaopciones_estadosocial.setObjectName(u"cajaopciones_estadosocial")
        self.cajaopciones_estadosocial.setEnabled(False)
        self.cajaopciones_estadosocial.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.gridLayout.addWidget(self.cajaopciones_estadosocial, 3, 3, 1, 1)

        self.etiqueta_fechanacimiento = QLabel(self.contenedorIzquierdo)
        self.etiqueta_fechanacimiento.setObjectName(u"etiqueta_fechanacimiento")

        self.gridLayout.addWidget(self.etiqueta_fechanacimiento, 4, 0, 1, 1)

        self.etiqueta_curp = QLabel(self.contenedorIzquierdo)
        self.etiqueta_curp.setObjectName(u"etiqueta_curp")

        self.gridLayout.addWidget(self.etiqueta_curp, 2, 2, 1, 1)

        self.txt_curp = QLineEdit(self.contenedorIzquierdo)
        self.txt_curp.setObjectName(u"txt_curp")
        self.txt_curp.setEnabled(False)

        self.gridLayout.addWidget(self.txt_curp, 2, 3, 1, 1)

        self.etiqueta_correo = QLabel(self.contenedorIzquierdo)
        self.etiqueta_correo.setObjectName(u"etiqueta_correo")

        self.gridLayout.addWidget(self.etiqueta_correo, 4, 2, 1, 1)

        self.fecha_fechanacimiento = QDateEdit(self.contenedorIzquierdo)
        self.fecha_fechanacimiento.setObjectName(u"fecha_fechanacimiento")
        self.fecha_fechanacimiento.setEnabled(False)
        self.fecha_fechanacimiento.setCalendarPopup(True)

        self.gridLayout.addWidget(self.fecha_fechanacimiento, 4, 1, 1, 1)

        self.txt_correo = QLineEdit(self.contenedorIzquierdo)
        self.txt_correo.setObjectName(u"txt_correo")
        self.txt_correo.setEnabled(False)

        self.gridLayout.addWidget(self.txt_correo, 4, 3, 1, 1)

        self.txt_numerosocial = QLineEdit(self.contenedorIzquierdo)
        self.txt_numerosocial.setObjectName(u"txt_numerosocial")
        self.txt_numerosocial.setEnabled(False)

        self.gridLayout.addWidget(self.txt_numerosocial, 3, 1, 1, 1)

        self.etiqueta_rfc = QLabel(self.contenedorIzquierdo)
        self.etiqueta_rfc.setObjectName(u"etiqueta_rfc")

        self.gridLayout.addWidget(self.etiqueta_rfc, 5, 0, 1, 1)

        self.etiqueta_estado = QLabel(self.contenedorIzquierdo)
        self.etiqueta_estado.setObjectName(u"etiqueta_estado")

        self.gridLayout.addWidget(self.etiqueta_estado, 8, 2, 1, 1)

        self.txt_estado = QLineEdit(self.contenedorIzquierdo)
        self.txt_estado.setObjectName(u"txt_estado")
        self.txt_estado.setEnabled(False)

        self.gridLayout.addWidget(self.txt_estado, 8, 3, 1, 1)

        self.etiquetaTitulo_datosubicacion = QLabel(self.contenedorIzquierdo)
        self.etiquetaTitulo_datosubicacion.setObjectName(u"etiquetaTitulo_datosubicacion")

        self.gridLayout.addWidget(self.etiquetaTitulo_datosubicacion, 7, 0, 1, 2)

        self.etiqueta_cpostal = QLabel(self.contenedorIzquierdo)
        self.etiqueta_cpostal.setObjectName(u"etiqueta_cpostal")

        self.gridLayout.addWidget(self.etiqueta_cpostal, 9, 0, 1, 1)

        self.etiqueta_ciudad = QLabel(self.contenedorIzquierdo)
        self.etiqueta_ciudad.setObjectName(u"etiqueta_ciudad")

        self.gridLayout.addWidget(self.etiqueta_ciudad, 8, 0, 1, 1)

        self.txt_ciudad = QLineEdit(self.contenedorIzquierdo)
        self.txt_ciudad.setObjectName(u"txt_ciudad")
        self.txt_ciudad.setEnabled(False)

        self.gridLayout.addWidget(self.txt_ciudad, 8, 1, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 20, 0, 1, 1)


        self.gridLayout_4.addWidget(self.contenedorIzquierdo, 1, 0, 1, 1)

        self.widget_4 = QWidget(self.widget_2)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout = QHBoxLayout(self.widget_4)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_btn_aceptar = QToolButton(self.widget_4)
        self.btn_btn_aceptar.setObjectName(u"btn_btn_aceptar")
        self.btn_btn_aceptar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_btn_aceptar.setLayoutDirection(Qt.LeftToRight)
        self.btn_btn_aceptar.setAutoFillBackground(False)
        icon = QIcon()
        icon.addFile(u":/iconosBlancos/Icons/iconos/Blanco/guardar_blanco.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_btn_aceptar.setIcon(icon)
        self.btn_btn_aceptar.setIconSize(QSize(24, 24))
        self.btn_btn_aceptar.setAutoRepeat(True)
        self.btn_btn_aceptar.setPopupMode(QToolButton.DelayedPopup)
        self.btn_btn_aceptar.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.btn_btn_aceptar.setAutoRaise(False)
        self.btn_btn_aceptar.setArrowType(Qt.NoArrow)

        self.horizontalLayout.addWidget(self.btn_btn_aceptar, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.btn_btn_editar = QPushButton(self.widget_4)
        self.btn_btn_editar.setObjectName(u"btn_btn_editar")
        icon1 = QIcon()
        icon1.addFile(u":/iconosBlancos/Icons/iconos/Blanco/editar_blanco.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_btn_editar.setIcon(icon1)

        self.horizontalLayout.addWidget(self.btn_btn_editar)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.gridLayout_4.addWidget(self.widget_4, 0, 0, 1, 1)


        self.gridLayout_7.addWidget(self.widget_2, 0, 0, 1, 1)


        self.gridLayout_6.addWidget(self.contenedor, 1, 0, 1, 1)

        self.label_wp_titulo_usuario = QLabel(Formulario_Datos_Empleado)
        self.label_wp_titulo_usuario.setObjectName(u"label_wp_titulo_usuario")
        self.label_wp_titulo_usuario.setMinimumSize(QSize(0, 0))
        self.label_wp_titulo_usuario.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_6.addWidget(self.label_wp_titulo_usuario, 0, 0, 1, 1)


        self.retranslateUi(Formulario_Datos_Empleado)

        QMetaObject.connectSlotsByName(Formulario_Datos_Empleado)
    # setupUi

    def retranslateUi(self, Formulario_Datos_Empleado):
        Formulario_Datos_Empleado.setWindowTitle(QCoreApplication.translate("Formulario_Datos_Empleado", u"Form", None))
        self.etiqueta_baja.setText(QCoreApplication.translate("Formulario_Datos_Empleado", u"Baja:", None))
        self.etiquetaDato_nombre.setText(QCoreApplication.translate("Formulario_Datos_Empleado", u"Luis Angel Vallejo Perez", None))
        self.etiquetaTituloDato_nombre.setText(QCoreApplication.translate("Formulario_Datos_Empleado", u"Nombre", None))
        self.label.setText("")
        self.etiqueta_horastrabajo.setText(QCoreApplication.translate("Formulario_Datos_Empleado", u"Hras. Trabajo", None))
        self.etiqueta_horaentrada.setText(QCoreApplication.translate("Formulario_Datos_Empleado", u"Hora Entrada", None))
        self.etiqueta_departamento.setText(QCoreApplication.translate("Formulario_Datos_Empleado", u"Departamento", None))
        self.etiqueta_puesto.setText(QCoreApplication.translate("Formulario_Datos_Empleado", u"Puesto", None))
        self.etiquetaTitulo_datosempleo.setText(QCoreApplication.translate("Formulario_Datos_Empleado", u"Datos del empleo", None))
        self.etiqueta_sucursal.setText(QCoreApplication.translate("Formulario_Datos_Empleado", u"Sucursal", None))
        self.etiqueta_horasalida.setText(QCoreApplication.translate("Formulario_Datos_Empleado", u"Hora Salida", None))
        self.etiqueta_salario.setText(QCoreApplication.translate("Formulario_Datos_Empleado", u"Salario", None))
        self.etiqueta_descripcionpuesto.setText(QCoreApplication.translate("Formulario_Datos_Empleado", u"Descripci\u00f3n del Puesto", None))
        self.txtlargo_descripcionpuesto.setPlaceholderText(QCoreApplication.translate("Formulario_Datos_Empleado", u"Ingresa detalles sobre el puesto", None))
        self.etiqueta_fechacontrato.setText(QCoreApplication.translate("Formulario_Datos_Empleado", u"F.Contrato", None))
        self.etiquetaTitulo_datosusuario.setText(QCoreApplication.translate("Formulario_Datos_Empleado", u"Datos sobre el usuario", None))
        self.etiqueta_usuario.setText(QCoreApplication.translate("Formulario_Datos_Empleado", u"Usuario", None))
        self.etiqueta_password.setText(QCoreApplication.translate("Formulario_Datos_Empleado", u"Contrase\u00f1a", None))
        self.etiqueta_diaslaborales_2.setTitle(QCoreApplication.translate("Formulario_Datos_Empleado", u"Dias Laborales", None))
        self.opcion_lunes.setText(QCoreApplication.translate("Formulario_Datos_Empleado", u"Lunes", None))
        self.opcion_miercoles.setText(QCoreApplication.translate("Formulario_Datos_Empleado", u"Miercoles", None))
        self.opcion_viernes.setText(QCoreApplication.translate("Formulario_Datos_Empleado", u"Viernes", None))
        self.opcion_domingo.setText(QCoreApplication.translate("Formulario_Datos_Empleado", u"Domingo", None))
        self.opcion_martes.setText(QCoreApplication.translate("Formulario_Datos_Empleado", u"Martes", None))
        self.opcion_jueves.setText(QCoreApplication.translate("Formulario_Datos_Empleado", u"Jueves", None))
        self.opcion_sabado.setText(QCoreApplication.translate("Formulario_Datos_Empleado", u"Sabado", None))
        self.etiqueta_pais.setText(QCoreApplication.translate("Formulario_Datos_Empleado", u"Pais", None))
        self.etiqueta_calles.setText(QCoreApplication.translate("Formulario_Datos_Empleado", u"Calle/s", None))
        self.etiqueta_telefono.setText(QCoreApplication.translate("Formulario_Datos_Empleado", u"Num. Telefono", None))
        self.etiqueta_nexterior.setText(QCoreApplication.translate("Formulario_Datos_Empleado", u"Num. Ext.", None))
        self.etiqueta_colonia.setText(QCoreApplication.translate("Formulario_Datos_Empleado", u"Colonia", None))
        self.etiqueta_numinterior.setText(QCoreApplication.translate("Formulario_Datos_Empleado", u"Num. Int", None))
        self.txtlargo_referenciadireccion.setPlaceholderText(QCoreApplication.translate("Formulario_Datos_Empleado", u"Ingresa detalles sobre la direcci\u00f3n del registro.", None))
        self.etiqueta_avenidas.setText(QCoreApplication.translate("Formulario_Datos_Empleado", u"Avenida/s", None))
        self.etiquetaTitulo_referencias.setText(QCoreApplication.translate("Formulario_Datos_Empleado", u"Referencias sobre la direccion", None))
        self.etiquetaTitulo_contactoemergencia.setText(QCoreApplication.translate("Formulario_Datos_Empleado", u"Contacto de emergencia", None))
        self.etiqueta_nombrecontactoemergencia.setText(QCoreApplication.translate("Formulario_Datos_Empleado", u"Nombre", None))
        self.etiqueta_numtelefonocontactoemergencia.setText(QCoreApplication.translate("Formulario_Datos_Empleado", u"Contacto", None))
        self.etiqueta_parentescocontactoemergencia.setText(QCoreApplication.translate("Formulario_Datos_Empleado", u"Parentesco", None))
        self.cajaopciones_parentescocontactoemergencia.setItemText(0, QCoreApplication.translate("Formulario_Datos_Empleado", u"MADRE", None))
        self.cajaopciones_parentescocontactoemergencia.setItemText(1, QCoreApplication.translate("Formulario_Datos_Empleado", u"PADRE", None))
        self.cajaopciones_parentescocontactoemergencia.setItemText(2, QCoreApplication.translate("Formulario_Datos_Empleado", u"TIO/A", None))
        self.cajaopciones_parentescocontactoemergencia.setItemText(3, QCoreApplication.translate("Formulario_Datos_Empleado", u"ESPOSO/A", None))
        self.cajaopciones_parentescocontactoemergencia.setItemText(4, QCoreApplication.translate("Formulario_Datos_Empleado", u"OTRO", None))

        self.etiquetaTitulo_datospersonales.setText(QCoreApplication.translate("Formulario_Datos_Empleado", u"Datos Personales", None))
        self.etiqueta_apellidopaterno.setText(QCoreApplication.translate("Formulario_Datos_Empleado", u"Apellido Paterno", None))
        self.etiqueta_apellidomaterno.setText(QCoreApplication.translate("Formulario_Datos_Empleado", u"Apellido Materno", None))
        self.etiqueta_nombre.setText(QCoreApplication.translate("Formulario_Datos_Empleado", u"Nombre", None))
        self.etiqueta_estadocivil.setText(QCoreApplication.translate("Formulario_Datos_Empleado", u"Estado Civil", None))
        self.etiqueta_numerosegurosocial.setText(QCoreApplication.translate("Formulario_Datos_Empleado", u"NSS", None))
        self.etiqueta_fechanacimiento.setText(QCoreApplication.translate("Formulario_Datos_Empleado", u"Fecha de Nacimiento", None))
        self.etiqueta_curp.setText(QCoreApplication.translate("Formulario_Datos_Empleado", u"CURP", None))
        self.etiqueta_correo.setText(QCoreApplication.translate("Formulario_Datos_Empleado", u"Correo", None))
        self.etiqueta_rfc.setText(QCoreApplication.translate("Formulario_Datos_Empleado", u"RFC", None))
        self.etiqueta_estado.setText(QCoreApplication.translate("Formulario_Datos_Empleado", u"Estado", None))
        self.etiquetaTitulo_datosubicacion.setText(QCoreApplication.translate("Formulario_Datos_Empleado", u"Datos sobre la ubicaci\u00f3n", None))
        self.etiqueta_cpostal.setText(QCoreApplication.translate("Formulario_Datos_Empleado", u"Codigo Postal", None))
        self.etiqueta_ciudad.setText(QCoreApplication.translate("Formulario_Datos_Empleado", u"Ciudad", None))
        self.btn_btn_aceptar.setText(QCoreApplication.translate("Formulario_Datos_Empleado", u"Guardar cambios", None))
        self.btn_btn_editar.setText("")
        self.label_wp_titulo_usuario.setText(QCoreApplication.translate("Formulario_Datos_Empleado", u"ADMINISTRACI\u00d3N DEL PERFIL", None))
    # retranslateUi

