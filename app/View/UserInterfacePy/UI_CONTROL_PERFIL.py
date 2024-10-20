# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_CONTROL_PERFIL.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Formulario_Datos_Empleado(object):
    def setupUi(self, Formulario_Datos_Empleado):
        Formulario_Datos_Empleado.setObjectName("Formulario_Datos_Empleado")
        Formulario_Datos_Empleado.resize(1101, 688)
        Formulario_Datos_Empleado.setStyleSheet("#Formulario_Datos_Empleado{\n"
"background-color: #fffefb;\n"
"}\n"
"#label_wp_titulo_usuario{\n"
"background-color: rgb(3, 51, 116);\n"
"max-height: 40px;\n"
"font-size:20px;\n"
"font-weight: bold;\n"
"color: #fffefb;\n"
"padding-left:5px;\n"
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
"    color: rgb(245, 244, 241);\n"
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
"border-radius: 5px;\n"
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
        self.gridLayout_6 = QtWidgets.QGridLayout(Formulario_Datos_Empleado)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setVerticalSpacing(0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.frame = QtWidgets.QFrame(Formulario_Datos_Empleado)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_7.setContentsMargins(5, 0, 5, 5)
        self.gridLayout_7.setSpacing(0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.widget_2 = QtWidgets.QWidget(self.frame)
        self.widget_2.setObjectName("widget_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        spacerItem = QtWidgets.QSpacerItem(200, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem, 1, 1, 1, 1)
        self.widget_3 = QtWidgets.QWidget(self.widget_2)
        self.widget_3.setMinimumSize(QtCore.QSize(350, 0))
        self.widget_3.setMaximumSize(QtCore.QSize(300, 16777215))
        self.widget_3.setObjectName("widget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget_3)
        self.gridLayout_3.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tarjeta_usuario = QtWidgets.QWidget(self.widget_3)
        self.tarjeta_usuario.setMinimumSize(QtCore.QSize(250, 100))
        self.tarjeta_usuario.setMaximumSize(QtCore.QSize(400, 177))
        self.tarjeta_usuario.setStyleSheet("")
        self.tarjeta_usuario.setObjectName("tarjeta_usuario")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tarjeta_usuario)
        self.gridLayout_2.setContentsMargins(10, 10, 10, 10)
        self.gridLayout_2.setHorizontalSpacing(10)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.etiquetaTituloDato_departamento = QtWidgets.QLabel(self.tarjeta_usuario)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.etiquetaTituloDato_departamento.setFont(font)
        self.etiquetaTituloDato_departamento.setStyleSheet("")
        self.etiquetaTituloDato_departamento.setObjectName("etiquetaTituloDato_departamento")
        self.gridLayout_2.addWidget(self.etiquetaTituloDato_departamento, 2, 1, 1, 1)
        self.etiquetaTituloDato_nombre = QtWidgets.QLabel(self.tarjeta_usuario)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.etiquetaTituloDato_nombre.setFont(font)
        self.etiquetaTituloDato_nombre.setStyleSheet("")
        self.etiquetaTituloDato_nombre.setObjectName("etiquetaTituloDato_nombre")
        self.gridLayout_2.addWidget(self.etiquetaTituloDato_nombre, 0, 1, 1, 1)
        self.etiquetaDato_nombre = QtWidgets.QLabel(self.tarjeta_usuario)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.etiquetaDato_nombre.setFont(font)
        self.etiquetaDato_nombre.setStyleSheet("")
        self.etiquetaDato_nombre.setWordWrap(True)
        self.etiquetaDato_nombre.setObjectName("etiquetaDato_nombre")
        self.gridLayout_2.addWidget(self.etiquetaDato_nombre, 1, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 4, 1, 1, 1)
        self.etiquetaDato_departamento = QtWidgets.QLabel(self.tarjeta_usuario)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.etiquetaDato_departamento.setFont(font)
        self.etiquetaDato_departamento.setStyleSheet("")
        self.etiquetaDato_departamento.setObjectName("etiquetaDato_departamento")
        self.gridLayout_2.addWidget(self.etiquetaDato_departamento, 3, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.tarjeta_usuario)
        self.label.setStyleSheet("image: url(:/Icons/Bootstrap/person-circle.svg);\n"
"background:none;")
        self.label.setText("")
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 5, 1)
        self.gridLayout_3.addWidget(self.tarjeta_usuario, 0, 0, 1, 1)
        self.frame_4 = QtWidgets.QFrame(self.widget_3)
        self.frame_4.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.line_3 = QtWidgets.QFrame(self.frame_4)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout_5.addWidget(self.line_3, 0, 0, 1, 4)
        self.etiqueta_puesto = QtWidgets.QLabel(self.frame_4)
        self.etiqueta_puesto.setObjectName("etiqueta_puesto")
        self.gridLayout_5.addWidget(self.etiqueta_puesto, 3, 0, 1, 1)
        self.etiqueta_salario = QtWidgets.QLabel(self.frame_4)
        self.etiqueta_salario.setObjectName("etiqueta_salario")
        self.gridLayout_5.addWidget(self.etiqueta_salario, 4, 0, 1, 1)
        self.numerodecimal_salario = QtWidgets.QDoubleSpinBox(self.frame_4)
        self.numerodecimal_salario.setObjectName("numerodecimal_salario")
        self.gridLayout_5.addWidget(self.numerodecimal_salario, 4, 1, 1, 1)
        self.etiqueta_horastrabajo = QtWidgets.QLabel(self.frame_4)
        self.etiqueta_horastrabajo.setObjectName("etiqueta_horastrabajo")
        self.gridLayout_5.addWidget(self.etiqueta_horastrabajo, 4, 2, 1, 1)
        self.numerodecimal_horastrabajo = QtWidgets.QDoubleSpinBox(self.frame_4)
        self.numerodecimal_horastrabajo.setObjectName("numerodecimal_horastrabajo")
        self.gridLayout_5.addWidget(self.numerodecimal_horastrabajo, 4, 3, 1, 1)
        self.etiqueta_horaentrada = QtWidgets.QLabel(self.frame_4)
        self.etiqueta_horaentrada.setObjectName("etiqueta_horaentrada")
        self.gridLayout_5.addWidget(self.etiqueta_horaentrada, 5, 0, 1, 1)
        self.tiempo_horaentrada = QtWidgets.QTimeEdit(self.frame_4)
        self.tiempo_horaentrada.setObjectName("tiempo_horaentrada")
        self.gridLayout_5.addWidget(self.tiempo_horaentrada, 5, 1, 1, 1)
        self.etiqueta_horasalida = QtWidgets.QLabel(self.frame_4)
        self.etiqueta_horasalida.setObjectName("etiqueta_horasalida")
        self.gridLayout_5.addWidget(self.etiqueta_horasalida, 5, 2, 1, 1)
        self.tiempo_horasalida = QtWidgets.QTimeEdit(self.frame_4)
        self.tiempo_horasalida.setObjectName("tiempo_horasalida")
        self.gridLayout_5.addWidget(self.tiempo_horasalida, 5, 3, 1, 1)
        self.etiqueta_diaslaborales = QtWidgets.QLabel(self.frame_4)
        self.etiqueta_diaslaborales.setObjectName("etiqueta_diaslaborales")
        self.gridLayout_5.addWidget(self.etiqueta_diaslaborales, 6, 0, 1, 1)
        self.txtlargo_descripcionpuesto = QtWidgets.QPlainTextEdit(self.frame_4)
        self.txtlargo_descripcionpuesto.setMaximumSize(QtCore.QSize(16777215, 61))
        self.txtlargo_descripcionpuesto.setObjectName("txtlargo_descripcionpuesto")
        self.gridLayout_5.addWidget(self.txtlargo_descripcionpuesto, 8, 0, 1, 4)
        self.line_2 = QtWidgets.QFrame(self.frame_4)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_5.addWidget(self.line_2, 9, 0, 1, 4)
        self.etiqueta_usuario = QtWidgets.QLabel(self.frame_4)
        self.etiqueta_usuario.setObjectName("etiqueta_usuario")
        self.gridLayout_5.addWidget(self.etiqueta_usuario, 11, 0, 1, 1)
        self.txt_usuario = QtWidgets.QLineEdit(self.frame_4)
        self.txt_usuario.setObjectName("txt_usuario")
        self.gridLayout_5.addWidget(self.txt_usuario, 11, 2, 1, 2)
        self.etiqueta_password = QtWidgets.QLabel(self.frame_4)
        self.etiqueta_password.setObjectName("etiqueta_password")
        self.gridLayout_5.addWidget(self.etiqueta_password, 12, 0, 1, 1)
        self.txt_password = QtWidgets.QLineEdit(self.frame_4)
        self.txt_password.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.txt_password.setObjectName("txt_password")
        self.gridLayout_5.addWidget(self.txt_password, 12, 2, 1, 2)
        self.txt_diaslaborales = QtWidgets.QLineEdit(self.frame_4)
        self.txt_diaslaborales.setObjectName("txt_diaslaborales")
        self.gridLayout_5.addWidget(self.txt_diaslaborales, 6, 1, 1, 3)
        self.etiquetaTitulo_datosusuario = QtWidgets.QLabel(self.frame_4)
        self.etiquetaTitulo_datosusuario.setObjectName("etiquetaTitulo_datosusuario")
        self.gridLayout_5.addWidget(self.etiquetaTitulo_datosusuario, 10, 0, 1, 4)
        self.etiqueta_descripcionpuesto = QtWidgets.QLabel(self.frame_4)
        self.etiqueta_descripcionpuesto.setObjectName("etiqueta_descripcionpuesto")
        self.gridLayout_5.addWidget(self.etiqueta_descripcionpuesto, 7, 0, 1, 4)
        self.txt_departamento = QtWidgets.QLineEdit(self.frame_4)
        self.txt_departamento.setObjectName("txt_departamento")
        self.gridLayout_5.addWidget(self.txt_departamento, 2, 2, 1, 2)
        self.txt_puesto = QtWidgets.QLineEdit(self.frame_4)
        self.txt_puesto.setObjectName("txt_puesto")
        self.gridLayout_5.addWidget(self.txt_puesto, 3, 2, 1, 2)
        self.etiquetaTitulo_datosempleo = QtWidgets.QLabel(self.frame_4)
        self.etiquetaTitulo_datosempleo.setObjectName("etiquetaTitulo_datosempleo")
        self.gridLayout_5.addWidget(self.etiquetaTitulo_datosempleo, 1, 0, 1, 4)
        self.etiqueta_departamento = QtWidgets.QLabel(self.frame_4)
        self.etiqueta_departamento.setObjectName("etiqueta_departamento")
        self.gridLayout_5.addWidget(self.etiqueta_departamento, 2, 0, 1, 1)
        self.gridLayout_3.addWidget(self.frame_4, 1, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem2, 2, 0, 1, 1)
        self.gridLayout_4.addWidget(self.widget_3, 0, 2, 2, 1, QtCore.Qt.AlignRight)
        self.contenedorIzquierdo = QtWidgets.QFrame(self.widget_2)
        self.contenedorIzquierdo.setMinimumSize(QtCore.QSize(0, 0))
        self.contenedorIzquierdo.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.contenedorIzquierdo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.contenedorIzquierdo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.contenedorIzquierdo.setObjectName("contenedorIzquierdo")
        self.gridLayout = QtWidgets.QGridLayout(self.contenedorIzquierdo)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(5)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 15, 0, 1, 1)
        self.txt_correo = QtWidgets.QLineEdit(self.contenedorIzquierdo)
        self.txt_correo.setObjectName("txt_correo")
        self.gridLayout.addWidget(self.txt_correo, 4, 3, 1, 3)
        self.txt_pais = QtWidgets.QLineEdit(self.contenedorIzquierdo)
        self.txt_pais.setObjectName("txt_pais")
        self.gridLayout.addWidget(self.txt_pais, 11, 3, 1, 1)
        self.etiqueta_apellidopaterno = QtWidgets.QLabel(self.contenedorIzquierdo)
        self.etiqueta_apellidopaterno.setObjectName("etiqueta_apellidopaterno")
        self.gridLayout.addWidget(self.etiqueta_apellidopaterno, 1, 2, 1, 1)
        self.etiqueta_nombre = QtWidgets.QLabel(self.contenedorIzquierdo)
        self.etiqueta_nombre.setObjectName("etiqueta_nombre")
        self.gridLayout.addWidget(self.etiqueta_nombre, 1, 0, 1, 1)
        self.txt_nombre = QtWidgets.QLineEdit(self.contenedorIzquierdo)
        self.txt_nombre.setObjectName("txt_nombre")
        self.gridLayout.addWidget(self.txt_nombre, 1, 1, 1, 1)
        self.etiquetaTitulo_datospersonales = QtWidgets.QLabel(self.contenedorIzquierdo)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.etiquetaTitulo_datospersonales.setFont(font)
        self.etiquetaTitulo_datospersonales.setObjectName("etiquetaTitulo_datospersonales")
        self.gridLayout.addWidget(self.etiquetaTitulo_datospersonales, 0, 0, 1, 2)
        self.etiqueta_apellidomaterno = QtWidgets.QLabel(self.contenedorIzquierdo)
        self.etiqueta_apellidomaterno.setObjectName("etiqueta_apellidomaterno")
        self.gridLayout.addWidget(self.etiqueta_apellidomaterno, 2, 0, 1, 1)
        self.etiqueta_curp = QtWidgets.QLabel(self.contenedorIzquierdo)
        self.etiqueta_curp.setObjectName("etiqueta_curp")
        self.gridLayout.addWidget(self.etiqueta_curp, 2, 2, 1, 1)
        self.txt_apellidomaterno = QtWidgets.QLineEdit(self.contenedorIzquierdo)
        self.txt_apellidomaterno.setObjectName("txt_apellidomaterno")
        self.gridLayout.addWidget(self.txt_apellidomaterno, 2, 1, 1, 1)
        self.etiqueta_numerosegurosocial = QtWidgets.QLabel(self.contenedorIzquierdo)
        self.etiqueta_numerosegurosocial.setObjectName("etiqueta_numerosegurosocial")
        self.gridLayout.addWidget(self.etiqueta_numerosegurosocial, 3, 0, 1, 1)
        self.txt_numerosocial = QtWidgets.QLineEdit(self.contenedorIzquierdo)
        self.txt_numerosocial.setObjectName("txt_numerosocial")
        self.gridLayout.addWidget(self.txt_numerosocial, 3, 1, 1, 1)
        self.etiqueta_cpostal = QtWidgets.QLabel(self.contenedorIzquierdo)
        self.etiqueta_cpostal.setObjectName("etiqueta_cpostal")
        self.gridLayout.addWidget(self.etiqueta_cpostal, 9, 0, 1, 1)
        self.etiqueta_estado = QtWidgets.QLabel(self.contenedorIzquierdo)
        self.etiqueta_estado.setObjectName("etiqueta_estado")
        self.gridLayout.addWidget(self.etiqueta_estado, 8, 2, 1, 1)
        self.etiqueta_ciudad = QtWidgets.QLabel(self.contenedorIzquierdo)
        self.etiqueta_ciudad.setObjectName("etiqueta_ciudad")
        self.gridLayout.addWidget(self.etiqueta_ciudad, 8, 0, 1, 1)
        self.etiqueta_calles = QtWidgets.QLabel(self.contenedorIzquierdo)
        self.etiqueta_calles.setObjectName("etiqueta_calles")
        self.gridLayout.addWidget(self.etiqueta_calles, 9, 2, 1, 1)
        self.etiqueta_fechanacimiento = QtWidgets.QLabel(self.contenedorIzquierdo)
        self.etiqueta_fechanacimiento.setObjectName("etiqueta_fechanacimiento")
        self.gridLayout.addWidget(self.etiqueta_fechanacimiento, 4, 0, 1, 1)
        self.fecha_fechanacimiento = QtWidgets.QDateEdit(self.contenedorIzquierdo)
        self.fecha_fechanacimiento.setCalendarPopup(True)
        self.fecha_fechanacimiento.setObjectName("fecha_fechanacimiento")
        self.gridLayout.addWidget(self.fecha_fechanacimiento, 4, 1, 1, 1)
        self.etiquetaTitulo_datosubicacion = QtWidgets.QLabel(self.contenedorIzquierdo)
        self.etiquetaTitulo_datosubicacion.setObjectName("etiquetaTitulo_datosubicacion")
        self.gridLayout.addWidget(self.etiquetaTitulo_datosubicacion, 7, 0, 1, 2)
        self.etiqueta_telefono = QtWidgets.QLabel(self.contenedorIzquierdo)
        self.etiqueta_telefono.setObjectName("etiqueta_telefono")
        self.gridLayout.addWidget(self.etiqueta_telefono, 10, 0, 1, 1)
        self.etiqueta_pais = QtWidgets.QLabel(self.contenedorIzquierdo)
        self.etiqueta_pais.setObjectName("etiqueta_pais")
        self.gridLayout.addWidget(self.etiqueta_pais, 11, 2, 1, 1)
        self.etiqueta_estadocivil = QtWidgets.QLabel(self.contenedorIzquierdo)
        self.etiqueta_estadocivil.setObjectName("etiqueta_estadocivil")
        self.gridLayout.addWidget(self.etiqueta_estadocivil, 3, 2, 1, 1)
        self.txt_rfc = QtWidgets.QLineEdit(self.contenedorIzquierdo)
        self.txt_rfc.setObjectName("txt_rfc")
        self.gridLayout.addWidget(self.txt_rfc, 5, 1, 1, 1)
        self.txt_estado = QtWidgets.QLineEdit(self.contenedorIzquierdo)
        self.txt_estado.setObjectName("txt_estado")
        self.gridLayout.addWidget(self.txt_estado, 8, 3, 1, 1)
        self.txt_numerotelefono = QtWidgets.QLineEdit(self.contenedorIzquierdo)
        self.txt_numerotelefono.setObjectName("txt_numerotelefono")
        self.gridLayout.addWidget(self.txt_numerotelefono, 10, 1, 1, 1)
        self.etiqueta_colonia = QtWidgets.QLabel(self.contenedorIzquierdo)
        self.etiqueta_colonia.setObjectName("etiqueta_colonia")
        self.gridLayout.addWidget(self.etiqueta_colonia, 10, 2, 1, 1)
        self.txt_calles = QtWidgets.QLineEdit(self.contenedorIzquierdo)
        self.txt_calles.setObjectName("txt_calles")
        self.gridLayout.addWidget(self.txt_calles, 9, 3, 1, 1)
        self.etiqueta_rfc = QtWidgets.QLabel(self.contenedorIzquierdo)
        self.etiqueta_rfc.setObjectName("etiqueta_rfc")
        self.gridLayout.addWidget(self.etiqueta_rfc, 5, 0, 1, 1)
        self.txt_ciudad = QtWidgets.QLineEdit(self.contenedorIzquierdo)
        self.txt_ciudad.setObjectName("txt_ciudad")
        self.gridLayout.addWidget(self.txt_ciudad, 8, 1, 1, 1)
        self.txt_codigopostal = QtWidgets.QLineEdit(self.contenedorIzquierdo)
        self.txt_codigopostal.setObjectName("txt_codigopostal")
        self.gridLayout.addWidget(self.txt_codigopostal, 9, 1, 1, 1)
        self.txt_colonia = QtWidgets.QLineEdit(self.contenedorIzquierdo)
        self.txt_colonia.setObjectName("txt_colonia")
        self.gridLayout.addWidget(self.txt_colonia, 10, 3, 1, 1)
        self.etiqueta_correo = QtWidgets.QLabel(self.contenedorIzquierdo)
        self.etiqueta_correo.setObjectName("etiqueta_correo")
        self.gridLayout.addWidget(self.etiqueta_correo, 4, 2, 1, 1)
        self.line = QtWidgets.QFrame(self.contenedorIzquierdo)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 6, 0, 1, 6)
        self.txtlargo_referenciadireccion = QtWidgets.QPlainTextEdit(self.contenedorIzquierdo)
        self.txtlargo_referenciadireccion.setMaximumSize(QtCore.QSize(16777215, 61))
        self.txtlargo_referenciadireccion.setTabChangesFocus(False)
        self.txtlargo_referenciadireccion.setTabStopWidth(80)
        self.txtlargo_referenciadireccion.setBackgroundVisible(False)
        self.txtlargo_referenciadireccion.setCenterOnScroll(False)
        self.txtlargo_referenciadireccion.setObjectName("txtlargo_referenciadireccion")
        self.gridLayout.addWidget(self.txtlargo_referenciadireccion, 14, 0, 1, 6)
        self.txt_avenidas = QtWidgets.QLineEdit(self.contenedorIzquierdo)
        self.txt_avenidas.setObjectName("txt_avenidas")
        self.gridLayout.addWidget(self.txt_avenidas, 11, 1, 1, 1)
        self.etiquetaTitulo_referencias = QtWidgets.QLabel(self.contenedorIzquierdo)
        self.etiquetaTitulo_referencias.setWordWrap(True)
        self.etiquetaTitulo_referencias.setObjectName("etiquetaTitulo_referencias")
        self.gridLayout.addWidget(self.etiquetaTitulo_referencias, 13, 0, 1, 2)
        self.etiqueta_avenidas = QtWidgets.QLabel(self.contenedorIzquierdo)
        self.etiqueta_avenidas.setObjectName("etiqueta_avenidas")
        self.gridLayout.addWidget(self.etiqueta_avenidas, 11, 0, 1, 1)
        self.txt_curp = QtWidgets.QLineEdit(self.contenedorIzquierdo)
        self.txt_curp.setObjectName("txt_curp")
        self.gridLayout.addWidget(self.txt_curp, 2, 3, 1, 3)
        self.txt_apellidopaterno = QtWidgets.QLineEdit(self.contenedorIzquierdo)
        self.txt_apellidopaterno.setObjectName("txt_apellidopaterno")
        self.gridLayout.addWidget(self.txt_apellidopaterno, 1, 3, 1, 3)
        self.cajaopciones_estadosocial = QtWidgets.QComboBox(self.contenedorIzquierdo)
        self.cajaopciones_estadosocial.setObjectName("cajaopciones_estadosocial")
        self.gridLayout.addWidget(self.cajaopciones_estadosocial, 3, 3, 1, 3)
        self.etiqueta_nexterior = QtWidgets.QLabel(self.contenedorIzquierdo)
        self.etiqueta_nexterior.setObjectName("etiqueta_nexterior")
        self.gridLayout.addWidget(self.etiqueta_nexterior, 12, 0, 1, 1)
        self.txt_numeroexterior = QtWidgets.QLineEdit(self.contenedorIzquierdo)
        self.txt_numeroexterior.setObjectName("txt_numeroexterior")
        self.gridLayout.addWidget(self.txt_numeroexterior, 12, 1, 1, 1)
        self.etiqueta_numinterior = QtWidgets.QLabel(self.contenedorIzquierdo)
        self.etiqueta_numinterior.setObjectName("etiqueta_numinterior")
        self.gridLayout.addWidget(self.etiqueta_numinterior, 12, 2, 1, 1)
        self.txt_numerointerior = QtWidgets.QLineEdit(self.contenedorIzquierdo)
        self.txt_numerointerior.setObjectName("txt_numerointerior")
        self.gridLayout.addWidget(self.txt_numerointerior, 12, 3, 1, 1)
        self.gridLayout_4.addWidget(self.contenedorIzquierdo, 1, 0, 1, 1)
        self.widget_4 = QtWidgets.QWidget(self.widget_2)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_btn_aceptar = QtWidgets.QToolButton(self.widget_4)
        self.btn_btn_aceptar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_btn_aceptar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_btn_aceptar.setAutoFillBackground(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/iconosBlancos/Icons/iconos/Blanco/guardar_blanco.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_btn_aceptar.setIcon(icon)
        self.btn_btn_aceptar.setIconSize(QtCore.QSize(24, 24))
        self.btn_btn_aceptar.setAutoRepeat(True)
        self.btn_btn_aceptar.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.btn_btn_aceptar.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.btn_btn_aceptar.setAutoRaise(False)
        self.btn_btn_aceptar.setArrowType(QtCore.Qt.NoArrow)
        self.btn_btn_aceptar.setObjectName("btn_btn_aceptar")
        self.horizontalLayout.addWidget(self.btn_btn_aceptar, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.gridLayout_4.addWidget(self.widget_4, 0, 0, 1, 1)
        self.gridLayout_7.addWidget(self.widget_2, 0, 0, 1, 1)
        self.gridLayout_6.addWidget(self.frame, 1, 0, 1, 1)
        self.label_wp_titulo_usuario = QtWidgets.QLabel(Formulario_Datos_Empleado)
        self.label_wp_titulo_usuario.setMinimumSize(QtCore.QSize(0, 0))
        self.label_wp_titulo_usuario.setMaximumSize(QtCore.QSize(16777215, 40))
        self.label_wp_titulo_usuario.setObjectName("label_wp_titulo_usuario")
        self.gridLayout_6.addWidget(self.label_wp_titulo_usuario, 0, 0, 1, 1)

        self.retranslateUi(Formulario_Datos_Empleado)
        QtCore.QMetaObject.connectSlotsByName(Formulario_Datos_Empleado)

    def retranslateUi(self, Formulario_Datos_Empleado):
        _translate = QtCore.QCoreApplication.translate
        Formulario_Datos_Empleado.setWindowTitle(_translate("Formulario_Datos_Empleado", "Form"))
        self.etiquetaTituloDato_departamento.setText(_translate("Formulario_Datos_Empleado", "Departamento"))
        self.etiquetaTituloDato_nombre.setText(_translate("Formulario_Datos_Empleado", "Nombre"))
        self.etiquetaDato_nombre.setText(_translate("Formulario_Datos_Empleado", "Luis Angel Vallejo Perez"))
        self.etiquetaDato_departamento.setText(_translate("Formulario_Datos_Empleado", "Business Intelligence"))
        self.etiqueta_puesto.setText(_translate("Formulario_Datos_Empleado", "Puesto"))
        self.etiqueta_salario.setText(_translate("Formulario_Datos_Empleado", "Salario"))
        self.etiqueta_horastrabajo.setText(_translate("Formulario_Datos_Empleado", "Hras. Trabajo"))
        self.etiqueta_horaentrada.setText(_translate("Formulario_Datos_Empleado", "Hora Entrada"))
        self.etiqueta_horasalida.setText(_translate("Formulario_Datos_Empleado", "Hora Salida"))
        self.etiqueta_diaslaborales.setText(_translate("Formulario_Datos_Empleado", "Dias Laborales"))
        self.txtlargo_descripcionpuesto.setPlaceholderText(_translate("Formulario_Datos_Empleado", "Ingresa detalles sobre el puesto"))
        self.etiqueta_usuario.setText(_translate("Formulario_Datos_Empleado", "Usuario"))
        self.etiqueta_password.setText(_translate("Formulario_Datos_Empleado", "Contraseña"))
        self.etiquetaTitulo_datosusuario.setText(_translate("Formulario_Datos_Empleado", "Datos sobre el usuario"))
        self.etiqueta_descripcionpuesto.setText(_translate("Formulario_Datos_Empleado", "Descripción del Puesto"))
        self.etiquetaTitulo_datosempleo.setText(_translate("Formulario_Datos_Empleado", "Datos del empleo"))
        self.etiqueta_departamento.setText(_translate("Formulario_Datos_Empleado", "Departamento"))
        self.etiqueta_apellidopaterno.setText(_translate("Formulario_Datos_Empleado", "Apellido Paterno"))
        self.etiqueta_nombre.setText(_translate("Formulario_Datos_Empleado", "Nombre"))
        self.etiquetaTitulo_datospersonales.setText(_translate("Formulario_Datos_Empleado", "Datos Personales"))
        self.etiqueta_apellidomaterno.setText(_translate("Formulario_Datos_Empleado", "Apellido Materno"))
        self.etiqueta_curp.setText(_translate("Formulario_Datos_Empleado", "CURP"))
        self.etiqueta_numerosegurosocial.setText(_translate("Formulario_Datos_Empleado", "NSS"))
        self.etiqueta_cpostal.setText(_translate("Formulario_Datos_Empleado", "Codigo Postal"))
        self.etiqueta_estado.setText(_translate("Formulario_Datos_Empleado", "Estado"))
        self.etiqueta_ciudad.setText(_translate("Formulario_Datos_Empleado", "Ciudad"))
        self.etiqueta_calles.setText(_translate("Formulario_Datos_Empleado", "Calle/s"))
        self.etiqueta_fechanacimiento.setText(_translate("Formulario_Datos_Empleado", "Fecha de Nacimiento"))
        self.etiquetaTitulo_datosubicacion.setText(_translate("Formulario_Datos_Empleado", "Datos sobre la ubicación"))
        self.etiqueta_telefono.setText(_translate("Formulario_Datos_Empleado", "Num. Telefono"))
        self.etiqueta_pais.setText(_translate("Formulario_Datos_Empleado", "Pais"))
        self.etiqueta_estadocivil.setText(_translate("Formulario_Datos_Empleado", "Estado Social"))
        self.etiqueta_colonia.setText(_translate("Formulario_Datos_Empleado", "Colonia"))
        self.etiqueta_rfc.setText(_translate("Formulario_Datos_Empleado", "RFC"))
        self.etiqueta_correo.setText(_translate("Formulario_Datos_Empleado", "Correo"))
        self.txtlargo_referenciadireccion.setPlaceholderText(_translate("Formulario_Datos_Empleado", "Ingresa detalles sobre la dirección del registro."))
        self.etiquetaTitulo_referencias.setText(_translate("Formulario_Datos_Empleado", "Referencias sobre la direccion"))
        self.etiqueta_avenidas.setText(_translate("Formulario_Datos_Empleado", "Avenida/s"))
        self.etiqueta_nexterior.setText(_translate("Formulario_Datos_Empleado", "Num. Ext."))
        self.etiqueta_numinterior.setText(_translate("Formulario_Datos_Empleado", "Num. Int"))
        self.btn_btn_aceptar.setText(_translate("Formulario_Datos_Empleado", "Guardar cambios"))
        self.label_wp_titulo_usuario.setText(_translate("Formulario_Datos_Empleado", "ADMINISTRACIÓN DEL PERFIL"))
from ...Source import ibootstrap_rc
from ...Source import iconosSVG_rc
