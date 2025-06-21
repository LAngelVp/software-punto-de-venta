# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UI_CONTROL_VENTAS.ui'
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
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QTableView, QWidget)
from ...Source import ibootstrap_rc
from ...Source import iconosSVG_rc

class Ui_Control_Ventas(object):
    def setupUi(self, Control_Ventas):
        if not Control_Ventas.objectName():
            Control_Ventas.setObjectName(u"Control_Ventas")
        Control_Ventas.resize(775, 409)
        Control_Ventas.setStyleSheet(u"*{color: #1d1c1c;}\n"
"[objectName*=\"contenedor\"]{border:none;}\n"
"#Control_Ventas{\n"
"background: #fffefb;\n"
"}\n"
"#contenedor{\n"
"background: #fffefb;\n"
"}\n"
"#etiquetaTitulo_ventas{\n"
"color:#1d1c1c;\n"
"background-color: #fffefb;\n"
"font-size: 24px;\n"
"font-weight: bold;\n"
"padding-left: 5px;\n"
"text-transform: uppercase;\n"
"font-family: \"Arial\";\n"
"padding-top: 5px;\n"
"}\n"
"[objectName*=\"btn_btn_\"]{\n"
"height: 25px;\n"
"border:none;\n"
"border-radius:5px;\n"
"color:#fffefb;\n"
"background:#023375;\n"
"font-size:14px;\n"
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
"#btn_RefrescarTab"
                        "la:pressed{\n"
"background: #b6ccd8 ;\n"
"}\n"
"\n"
"#etiqueta_buscar{\n"
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
"    color: "
                        "white;\n"
"}\n"
"\n"
"/* Encabezado vertical */\n"
"[objectName*=\"tabla_\"] QHeaderView::vertical {\n"
"    background-color: #023375;\n"
"    color: white;\n"
"}")
        self.gridLayout = QGridLayout(Control_Ventas)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.contenedor = QFrame(Control_Ventas)
        self.contenedor.setObjectName(u"contenedor")
        self.contenedor.setFrameShape(QFrame.Shape.StyledPanel)
        self.contenedor.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.contenedor)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.etiquetaTitulo_ventas = QLabel(self.contenedor)
        self.etiquetaTitulo_ventas.setObjectName(u"etiquetaTitulo_ventas")
        self.etiquetaTitulo_ventas.setMinimumSize(QSize(0, 40))
        self.etiquetaTitulo_ventas.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_2.addWidget(self.etiquetaTitulo_ventas, 0, 0, 1, 1)

        self.contenedor_frame_2 = QFrame(self.contenedor)
        self.contenedor_frame_2.setObjectName(u"contenedor_frame_2")
        self.contenedor_frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.contenedor_frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_5 = QGridLayout(self.contenedor_frame_2)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, -1, 0, 0)
        self.contenedor_controles = QFrame(self.contenedor_frame_2)
        self.contenedor_controles.setObjectName(u"contenedor_controles")
        self.contenedor_controles.setFrameShape(QFrame.Shape.StyledPanel)
        self.contenedor_controles.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_3 = QGridLayout(self.contenedor_controles)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_btn_agregar = QPushButton(self.contenedor_controles)
        self.btn_btn_agregar.setObjectName(u"btn_btn_agregar")
        icon = QIcon()
        icon.addFile(u":/iconosBlancos/Icons/iconos/Blanco/agregar_blanco.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_btn_agregar.setIcon(icon)
        self.btn_btn_agregar.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.btn_btn_agregar)

        self.btn_btn_eliminar = QPushButton(self.contenedor_controles)
        self.btn_btn_eliminar.setObjectName(u"btn_btn_eliminar")
        icon1 = QIcon()
        icon1.addFile(u":/iconosBlancos/Icons/iconos/Blanco/eliminar_blanco.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_btn_eliminar.setIcon(icon1)
        self.btn_btn_eliminar.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.btn_btn_eliminar)

        self.btn_btn_modificar = QPushButton(self.contenedor_controles)
        self.btn_btn_modificar.setObjectName(u"btn_btn_modificar")
        icon2 = QIcon()
        icon2.addFile(u":/iconosBlancos/Icons/iconos/Blanco/editar_blanco.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_btn_modificar.setIcon(icon2)
        self.btn_btn_modificar.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.btn_btn_modificar)


        self.gridLayout_3.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_2, 0, 1, 1, 1)


        self.gridLayout_5.addWidget(self.contenedor_controles, 0, 0, 1, 1)

        self.contenedor_tabla = QFrame(self.contenedor_frame_2)
        self.contenedor_tabla.setObjectName(u"contenedor_tabla")
        self.contenedor_tabla.setFrameShape(QFrame.Shape.StyledPanel)
        self.contenedor_tabla.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_4 = QGridLayout(self.contenedor_tabla)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.etiqueta_buscar = QLabel(self.contenedor_tabla)
        self.etiqueta_buscar.setObjectName(u"etiqueta_buscar")

        self.horizontalLayout_2.addWidget(self.etiqueta_buscar)

        self.txt_buscar = QLineEdit(self.contenedor_tabla)
        self.txt_buscar.setObjectName(u"txt_buscar")

        self.horizontalLayout_2.addWidget(self.txt_buscar)

        self.btn_btn_buscar = QPushButton(self.contenedor_tabla)
        self.btn_btn_buscar.setObjectName(u"btn_btn_buscar")

        self.horizontalLayout_2.addWidget(self.btn_btn_buscar)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.btn_RefrescarTabla = QPushButton(self.contenedor_tabla)
        self.btn_RefrescarTabla.setObjectName(u"btn_RefrescarTabla")
        self.btn_RefrescarTabla.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/iconosBlancos/Icons/IconosSVG/base_datos_refresh.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_RefrescarTabla.setIcon(icon3)

        self.horizontalLayout_2.addWidget(self.btn_RefrescarTabla)


        self.gridLayout_4.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)

        self.tabla_ventas = QTableView(self.contenedor_tabla)
        self.tabla_ventas.setObjectName(u"tabla_ventas")

        self.gridLayout_4.addWidget(self.tabla_ventas, 1, 0, 1, 1)


        self.gridLayout_5.addWidget(self.contenedor_tabla, 1, 0, 1, 1)


        self.gridLayout_2.addWidget(self.contenedor_frame_2, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.contenedor, 0, 0, 1, 1)


        self.retranslateUi(Control_Ventas)

        QMetaObject.connectSlotsByName(Control_Ventas)
    # setupUi

    def retranslateUi(self, Control_Ventas):
        Control_Ventas.setWindowTitle(QCoreApplication.translate("Control_Ventas", u"Form", None))
        self.etiquetaTitulo_ventas.setText(QCoreApplication.translate("Control_Ventas", u"ADMINISTRACI\u00d3N DE VENTAS", None))
        self.btn_btn_agregar.setText(QCoreApplication.translate("Control_Ventas", u"AGREGAR", None))
        self.btn_btn_eliminar.setText(QCoreApplication.translate("Control_Ventas", u"ELIMINAR", None))
        self.btn_btn_modificar.setText(QCoreApplication.translate("Control_Ventas", u"MODIFICAR", None))
        self.etiqueta_buscar.setText("")
        self.btn_btn_buscar.setText(QCoreApplication.translate("Control_Ventas", u"Buscar", None))
#if QT_CONFIG(tooltip)
        self.btn_RefrescarTabla.setToolTip(QCoreApplication.translate("Control_Ventas", u"Refrescar tabla", None))
#endif // QT_CONFIG(tooltip)
        self.btn_RefrescarTabla.setText("")
    # retranslateUi

