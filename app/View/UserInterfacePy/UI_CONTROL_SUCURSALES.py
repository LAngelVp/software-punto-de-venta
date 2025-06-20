# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UI_CONTROL_SUCURSALES.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QPlainTextEdit, QPushButton, QSizePolicy, QSpacerItem,
    QWidget)
from ...Source import iconsdvg_rc
from ...Source import ibootstrap_rc
from ...Source import iconosSVG_rc

class Ui_Nueva_sucursal(object):
    def setupUi(self, Nueva_sucursal):
        if not Nueva_sucursal.objectName():
            Nueva_sucursal.setObjectName(u"Nueva_sucursal")
        Nueva_sucursal.resize(818, 512)
        Nueva_sucursal.setMinimumSize(QSize(0, 0))
        Nueva_sucursal.setMaximumSize(QSize(16777215, 16777215))
        Nueva_sucursal.setStyleSheet(u"*{color: #1d1c1c;}\n"
"#Nueva_sucursal{\n"
"background: #fffefb;\n"
"}\n"
"#contenedor_encabezado{\n"
"background: #023375\n"
"}\n"
"\n"
"#etiqueta_buscar{\n"
"image: url(:/iconosAzules/Icons/iconos/Azul/buscar_filas_azul.svg);\n"
"min-width: 25px;\n"
"min-height: 25px;\n"
"}\n"
"[objectName*=\"contenedor_\"]{\n"
"background: #fffefb;\n"
"border:none;\n"
"}\n"
"[objectName*=\"etiquetaTitulo_\"]{\n"
"color: #1d1c1c;\n"
"font-size:18px;\n"
"font-weight:bold;\n"
"font-family:Arial;\n"
"}\n"
"[objectName*=\"etiqueta_\"]{\n"
"color: #1d1c1c;\n"
"font-size:12px;\n"
"font-weight:bold;\n"
"font-family:Arial;\n"
"}\n"
"[objectName*=\"etiquetasubtitulo_\"]{\n"
"color: #1d1c1c;\n"
"font-size:15px;\n"
"font-weight:bold;\n"
"font-family:Arial;\n"
"}\n"
"#etiqueta_titulo_encabezado{\n"
"font-size: 18px;\n"
"color: #fffefb;\n"
"font-weight:bold;\n"
"font-family:Arial;\n"
"}\n"
"[objectName*=\"txt_\"]{\n"
"color: #1d1c1c;\n"
"font-size:12px;\n"
"font-family:Arial;\n"
"background: #F5F5F5;\n"
"border:none;\n"
"border-radius:5p"
                        "x;\n"
"border-bottom: 1px solid #1d1c1c;\n"
"}\n"
"[objectName*=\"txtlargo_\"]{\n"
"color: #1d1c1c;\n"
"font-size:12px;\n"
"font-family:Arial;\n"
"background: #F5F5F5;\n"
"border:none;\n"
"border-radius:5px;\n"
"border-bottom: 1px solid #1d1c1c;\n"
"}\n"
"[objectName*=\"txt_\"]:focus{\n"
"border-bottom: 1px solid #023375;\n"
"}\n"
"[objectName*=\"txtlargo_\"]:focus{\n"
"border-bottom: 1px solid #023375;\n"
"}\n"
"[objectName*=\"btn_btn_\"]{\n"
"color:#fffefb;\n"
"font-size:14px;\n"
"font-family:Arial;\n"
"font-weight:bold;\n"
"background: #023375;\n"
"border:none;\n"
"border-radius: 5px;\n"
"padding-left:5px;\n"
"padding-right: 5px;\n"
"height:25px;\n"
"}\n"
"[objectName*=\"btn_btn_\"]:hover{\n"
"background: #2196F3;\n"
"}\n"
"#btn_btn_agregar:hover{\n"
"background: #68a67d;\n"
"}\n"
"#btn_btn_eliminar:hover{\n"
"background: #EE1D52;\n"
"}\n"
"/*QLISTWIDGET*/\n"
"QListWidget {\n"
"    font-family: Arial;\n"
"    font-size: 14px;\n"
"	background: #F5F5F5;\n"
"}\n"
"")
        self.gridLayout_5 = QGridLayout(Nueva_sucursal)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.contenedor_global = QFrame(Nueva_sucursal)
        self.contenedor_global.setObjectName(u"contenedor_global")
        self.contenedor_global.setFrameShape(QFrame.Shape.StyledPanel)
        self.contenedor_global.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.contenedor_global)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.contenedor_encabezado = QFrame(self.contenedor_global)
        self.contenedor_encabezado.setObjectName(u"contenedor_encabezado")
        self.contenedor_encabezado.setFrameShape(QFrame.Shape.StyledPanel)
        self.contenedor_encabezado.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.contenedor_encabezado)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.etiqueta_titulo_encabezado = QLabel(self.contenedor_encabezado)
        self.etiqueta_titulo_encabezado.setObjectName(u"etiqueta_titulo_encabezado")

        self.horizontalLayout_2.addWidget(self.etiqueta_titulo_encabezado)

        self.horizontalSpacer_2 = QSpacerItem(665, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.btn_cerrar_encabezado = QPushButton(self.contenedor_encabezado)
        self.btn_cerrar_encabezado.setObjectName(u"btn_cerrar_encabezado")
        self.btn_cerrar_encabezado.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/Icons/Bootstrap/x-lg.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_cerrar_encabezado.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.btn_cerrar_encabezado)


        self.gridLayout.addWidget(self.contenedor_encabezado, 0, 0, 1, 2)

        self.contenedor_lista = QFrame(self.contenedor_global)
        self.contenedor_lista.setObjectName(u"contenedor_lista")
        self.contenedor_lista.setFrameShape(QFrame.Shape.StyledPanel)
        self.contenedor_lista.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_4 = QGridLayout(self.contenedor_lista)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.lista_sucursales = QListWidget(self.contenedor_lista)
        self.lista_sucursales.setObjectName(u"lista_sucursales")
        self.lista_sucursales.setMinimumSize(QSize(0, 0))
        self.lista_sucursales.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_4.addWidget(self.lista_sucursales, 2, 0, 1, 1)

        self.etiquetasubtitulo_sucursales = QLabel(self.contenedor_lista)
        self.etiquetasubtitulo_sucursales.setObjectName(u"etiquetasubtitulo_sucursales")

        self.gridLayout_4.addWidget(self.etiquetasubtitulo_sucursales, 1, 0, 1, 1)

        self.lista_departamentosasociados = QListWidget(self.contenedor_lista)
        self.lista_departamentosasociados.setObjectName(u"lista_departamentosasociados")

        self.gridLayout_4.addWidget(self.lista_departamentosasociados, 2, 1, 1, 1)

        self.etiquetasubtitulo_departamentosasociados = QLabel(self.contenedor_lista)
        self.etiquetasubtitulo_departamentosasociados.setObjectName(u"etiquetasubtitulo_departamentosasociados")

        self.gridLayout_4.addWidget(self.etiquetasubtitulo_departamentosasociados, 1, 1, 1, 1)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.etiqueta_buscar = QLabel(self.contenedor_lista)
        self.etiqueta_buscar.setObjectName(u"etiqueta_buscar")

        self.gridLayout_3.addWidget(self.etiqueta_buscar, 0, 0, 1, 1)

        self.txt_buscarsucursales = QLineEdit(self.contenedor_lista)
        self.txt_buscarsucursales.setObjectName(u"txt_buscarsucursales")

        self.gridLayout_3.addWidget(self.txt_buscarsucursales, 0, 1, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 0, 1, 2)


        self.gridLayout.addWidget(self.contenedor_lista, 1, 1, 1, 1)

        self.contenedor = QFrame(self.contenedor_global)
        self.contenedor.setObjectName(u"contenedor")
        self.contenedor.setMinimumSize(QSize(380, 0))
        self.contenedor.setMaximumSize(QSize(16777215, 16777215))
        self.contenedor.setFrameShape(QFrame.Shape.StyledPanel)
        self.contenedor.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.contenedor)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(0)
        self.gridLayout_2.setVerticalSpacing(5)
        self.gridLayout_2.setContentsMargins(10, -1, 10, 0)
        self.txt_pais = QLineEdit(self.contenedor)
        self.txt_pais.setObjectName(u"txt_pais")

        self.gridLayout_2.addWidget(self.txt_pais, 5, 2, 1, 2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 0, 2, 1, 1)

        self.etiqueta_nombre = QLabel(self.contenedor)
        self.etiqueta_nombre.setObjectName(u"etiqueta_nombre")

        self.gridLayout_2.addWidget(self.etiqueta_nombre, 1, 0, 1, 2)

        self.etiqueta_pais = QLabel(self.contenedor)
        self.etiqueta_pais.setObjectName(u"etiqueta_pais")

        self.gridLayout_2.addWidget(self.etiqueta_pais, 5, 0, 1, 2)

        self.txt_ntelefono = QLineEdit(self.contenedor)
        self.txt_ntelefono.setObjectName(u"txt_ntelefono")

        self.gridLayout_2.addWidget(self.txt_ntelefono, 6, 2, 1, 2)

        self.txt_codigopostal = QLineEdit(self.contenedor)
        self.txt_codigopostal.setObjectName(u"txt_codigopostal")

        self.gridLayout_2.addWidget(self.txt_codigopostal, 2, 2, 1, 2)

        self.etiqueta_estado = QLabel(self.contenedor)
        self.etiqueta_estado.setObjectName(u"etiqueta_estado")

        self.gridLayout_2.addWidget(self.etiqueta_estado, 4, 0, 1, 1)

        self.etiqueta_codigopostal = QLabel(self.contenedor)
        self.etiqueta_codigopostal.setObjectName(u"etiqueta_codigopostal")

        self.gridLayout_2.addWidget(self.etiqueta_codigopostal, 2, 0, 1, 2)

        self.txt_ciudad = QLineEdit(self.contenedor)
        self.txt_ciudad.setObjectName(u"txt_ciudad")

        self.gridLayout_2.addWidget(self.txt_ciudad, 3, 2, 1, 2)

        self.txtlargo_direccion = QPlainTextEdit(self.contenedor)
        self.txtlargo_direccion.setObjectName(u"txtlargo_direccion")

        self.gridLayout_2.addWidget(self.txtlargo_direccion, 8, 0, 1, 4)

        self.etiqueta_ciudad = QLabel(self.contenedor)
        self.etiqueta_ciudad.setObjectName(u"etiqueta_ciudad")

        self.gridLayout_2.addWidget(self.etiqueta_ciudad, 3, 0, 1, 1)

        self.etiqueta_direccion = QLabel(self.contenedor)
        self.etiqueta_direccion.setObjectName(u"etiqueta_direccion")

        self.gridLayout_2.addWidget(self.etiqueta_direccion, 7, 0, 1, 2)

        self.etiquetaTitulo_sucursal = QLabel(self.contenedor)
        self.etiquetaTitulo_sucursal.setObjectName(u"etiquetaTitulo_sucursal")

        self.gridLayout_2.addWidget(self.etiquetaTitulo_sucursal, 0, 0, 1, 2)

        self.txt_estado = QLineEdit(self.contenedor)
        self.txt_estado.setObjectName(u"txt_estado")

        self.gridLayout_2.addWidget(self.txt_estado, 4, 2, 1, 2)

        self.txt_nombre = QLineEdit(self.contenedor)
        self.txt_nombre.setObjectName(u"txt_nombre")

        self.gridLayout_2.addWidget(self.txt_nombre, 1, 2, 1, 2)

        self.btn_btn_limpiar = QPushButton(self.contenedor)
        self.btn_btn_limpiar.setObjectName(u"btn_btn_limpiar")
        self.btn_btn_limpiar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/Icons/IconosSVG/borrador.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_btn_limpiar.setIcon(icon1)
        self.btn_btn_limpiar.setIconSize(QSize(25, 25))

        self.gridLayout_2.addWidget(self.btn_btn_limpiar, 0, 3, 1, 1)

        self.contenedor_botones = QFrame(self.contenedor)
        self.contenedor_botones.setObjectName(u"contenedor_botones")
        self.contenedor_botones.setFrameShape(QFrame.Shape.StyledPanel)
        self.contenedor_botones.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.contenedor_botones)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(5, -1, 5, -1)
        self.btn_btn_eliminar = QPushButton(self.contenedor_botones)
        self.btn_btn_eliminar.setObjectName(u"btn_btn_eliminar")
        self.btn_btn_eliminar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/iconosBlancos/Icons/iconos/Blanco/eliminar_blanco.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_btn_eliminar.setIcon(icon2)
        self.btn_btn_eliminar.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.btn_btn_eliminar)

        self.btn_btn_actualizar = QPushButton(self.contenedor_botones)
        self.btn_btn_actualizar.setObjectName(u"btn_btn_actualizar")
        self.btn_btn_actualizar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/iconosBlancos/Icons/iconos/Blanco/actualizar_blanco.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_btn_actualizar.setIcon(icon3)
        self.btn_btn_actualizar.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.btn_btn_actualizar)

        self.btn_btn_agregar = QPushButton(self.contenedor_botones)
        self.btn_btn_agregar.setObjectName(u"btn_btn_agregar")
        self.btn_btn_agregar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/iconosBlancos/Icons/iconos/Blanco/guardar_blanco.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_btn_agregar.setIcon(icon4)
        self.btn_btn_agregar.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.btn_btn_agregar)


        self.gridLayout_2.addWidget(self.contenedor_botones, 10, 0, 1, 4)

        self.etiqueta_ntelefono = QLabel(self.contenedor)
        self.etiqueta_ntelefono.setObjectName(u"etiqueta_ntelefono")

        self.gridLayout_2.addWidget(self.etiqueta_ntelefono, 6, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 9, 0, 1, 4)


        self.gridLayout.addWidget(self.contenedor, 1, 0, 1, 1)


        self.gridLayout_5.addWidget(self.contenedor_global, 0, 0, 1, 1)

        QWidget.setTabOrder(self.txt_nombre, self.txt_codigopostal)
        QWidget.setTabOrder(self.txt_codigopostal, self.txt_ciudad)
        QWidget.setTabOrder(self.txt_ciudad, self.txt_estado)
        QWidget.setTabOrder(self.txt_estado, self.txt_pais)
        QWidget.setTabOrder(self.txt_pais, self.txt_ntelefono)
        QWidget.setTabOrder(self.txt_ntelefono, self.txtlargo_direccion)
        QWidget.setTabOrder(self.txtlargo_direccion, self.btn_btn_eliminar)
        QWidget.setTabOrder(self.btn_btn_eliminar, self.btn_btn_actualizar)
        QWidget.setTabOrder(self.btn_btn_actualizar, self.btn_btn_agregar)
        QWidget.setTabOrder(self.btn_btn_agregar, self.lista_sucursales)

        self.retranslateUi(Nueva_sucursal)

        QMetaObject.connectSlotsByName(Nueva_sucursal)
    # setupUi

    def retranslateUi(self, Nueva_sucursal):
        Nueva_sucursal.setWindowTitle(QCoreApplication.translate("Nueva_sucursal", u"Form", None))
        self.etiqueta_titulo_encabezado.setText(QCoreApplication.translate("Nueva_sucursal", u"Sucursales", None))
        self.btn_cerrar_encabezado.setText("")
        self.etiquetasubtitulo_sucursales.setText(QCoreApplication.translate("Nueva_sucursal", u"Sucursales", None))
        self.etiquetasubtitulo_departamentosasociados.setText(QCoreApplication.translate("Nueva_sucursal", u"Departamentos", None))
        self.etiqueta_buscar.setText("")
        self.txt_buscarsucursales.setPlaceholderText(QCoreApplication.translate("Nueva_sucursal", u" Buscar Sucursal", None))
        self.etiqueta_nombre.setText(QCoreApplication.translate("Nueva_sucursal", u"Nombre", None))
        self.etiqueta_pais.setText(QCoreApplication.translate("Nueva_sucursal", u"Pais", None))
        self.etiqueta_estado.setText(QCoreApplication.translate("Nueva_sucursal", u"Estado", None))
        self.etiqueta_codigopostal.setText(QCoreApplication.translate("Nueva_sucursal", u"Codigo Postal", None))
        self.etiqueta_ciudad.setText(QCoreApplication.translate("Nueva_sucursal", u"Ciudad", None))
        self.etiqueta_direccion.setText(QCoreApplication.translate("Nueva_sucursal", u"Direccion", None))
        self.etiquetaTitulo_sucursal.setText(QCoreApplication.translate("Nueva_sucursal", u"Nueva Sucursal", None))
        self.btn_btn_limpiar.setText("")
        self.btn_btn_eliminar.setText(QCoreApplication.translate("Nueva_sucursal", u"ELIMINAR", None))
        self.btn_btn_actualizar.setText(QCoreApplication.translate("Nueva_sucursal", u"ACTUALIZAR", None))
        self.btn_btn_agregar.setText(QCoreApplication.translate("Nueva_sucursal", u"AGREGAR", None))
        self.etiqueta_ntelefono.setText(QCoreApplication.translate("Nueva_sucursal", u"Num. Telefono", None))
    # retranslateUi

