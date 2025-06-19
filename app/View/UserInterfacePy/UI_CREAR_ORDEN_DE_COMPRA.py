# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UI_CREAR_ORDEN_DE_COMPRA.ui'
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
    QSizePolicy, QSpacerItem, QTableView, QToolButton,
    QWidget)
from ...Source import ibootstrap_rc

class Ui_Orden_compra(object):
    def setupUi(self, Orden_compra):
        if not Orden_compra.objectName():
            Orden_compra.setObjectName(u"Orden_compra")
        Orden_compra.resize(600, 556)
        Orden_compra.setMinimumSize(QSize(600, 556))
        Orden_compra.setMaximumSize(QSize(600, 556))
        Orden_compra.setStyleSheet(u"#Orden_compra{\n"
"background-color: #fffefb;\n"
"}\n"
"#contenedor_encabezado{\n"
"background-color: rgb(3, 51, 116);\n"
"height: 30px;\n"
"}\n"
"#label_wc_titulo_ordencompra{\n"
"color: #fffefb;\n"
"font-size: 18px;\n"
"font-weight:bold;\n"
"font-family:\"Arial\";\n"
"}\n"
"[objectName*=\"frame\"]{\n"
"background-color: #fffefb;\n"
"}\n"
"*[objectName*=\"etiqueta_\"]{\n"
"font-family: Arial;\n"
"font-size: 14px;\n"
"font-weight:bold;\n"
"}\n"
"*[objectName*=\"btn_btn_\"]{\n"
"background: #00619a;\n"
"font-size: 14px;\n"
"font-family: Arial;\n"
"font-weight: bold;\n"
"min-height: 25px;\n"
"border: none;\n"
"border-radius: 5px;\n"
"color: #fffefb;\n"
"padding: 3px 5px;\n"
"}\n"
"*[objectName*=\"btn_btn_agregar\"]{\n"
"background-color: #00619a;\n"
"}\n"
"*[objectName*=\"btn_btn_\"]:hover{\n"
"background-color: #59a5f5;\n"
"}\n"
"#btn_btn_agregar:hover{\n"
"background-color: #68a67d;\n"
"}\n"
"#btn_btn_terminar:hover{\n"
"background-color: #68a67d;\n"
"}\n"
"#btn_btn_cerrar{\n"
"background-color: #fffefb;\n"
"m"
                        "in-height:15px;\n"
"max-width:15px;\n"
"}\n"
"#btn_btn_cerrar:pressed{\n"
"background: rgb(222, 221, 218);\n"
"}\n"
"*[objectName*=\"txt_\"]{\n"
"background-color:#F5F5F5;\n"
"color: #1d1c1c;\n"
"border: none;\n"
"border-bottom: 1px solid;\n"
"border-radius: 5px;\n"
"font-size: 12px;\n"
"font-family: Arial;\n"
"}\n"
"*[objectName^=\"txt_\"]::focus{\n"
"border-bottom: 2px solid #00668c;\n"
"}\n"
"*[objectName*=\"numerodecimal_\"]{\n"
"background-color: #F5F5F5;\n"
"color: #1d1c1c;\n"
"border: none;\n"
"border-bottom: 1px solid;\n"
"border-radius: 5px;\n"
"font-size: 14px;\n"
"font-family: Arial;\n"
"}\n"
"*[objectName^=\"numerodecimal_\"]::focus{\n"
"border-bottom: 2px solid #00668c;\n"
"}\n"
"/*TABLA*/\n"
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
"    paddi"
                        "ng: 5px;\n"
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
        self.gridLayout = QGridLayout(Orden_compra)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(Orden_compra)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setHorizontalSpacing(0)
        self.gridLayout_4.setVerticalSpacing(5)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.contenedor_encabezado = QFrame(self.frame)
        self.contenedor_encabezado.setObjectName(u"contenedor_encabezado")
        self.contenedor_encabezado.setFrameShape(QFrame.StyledPanel)
        self.contenedor_encabezado.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.contenedor_encabezado)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(5, 2, 5, 2)
        self.label_wc_titulo_ordencompra = QLabel(self.contenedor_encabezado)
        self.label_wc_titulo_ordencompra.setObjectName(u"label_wc_titulo_ordencompra")
        self.label_wc_titulo_ordencompra.setMinimumSize(QSize(0, 0))
        self.label_wc_titulo_ordencompra.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout.addWidget(self.label_wc_titulo_ordencompra)

        self.horizontalSpacer_2 = QSpacerItem(411, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.btn_btn_cerrar = QPushButton(self.contenedor_encabezado)
        self.btn_btn_cerrar.setObjectName(u"btn_btn_cerrar")
        self.btn_btn_cerrar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/Icons/Bootstrap/x-lg.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_btn_cerrar.setIcon(icon)

        self.horizontalLayout.addWidget(self.btn_btn_cerrar)


        self.gridLayout_4.addWidget(self.contenedor_encabezado, 0, 0, 1, 1)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.btn_btn_productosProveedor = QPushButton(self.frame_4)
        self.btn_btn_productosProveedor.setObjectName(u"btn_btn_productosProveedor")
        self.btn_btn_productosProveedor.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.btn_btn_productosProveedor)

        self.horizontalSpacer = QSpacerItem(315, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.btn_btn_terminar = QToolButton(self.frame_4)
        self.btn_btn_terminar.setObjectName(u"btn_btn_terminar")
        self.btn_btn_terminar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.btn_btn_terminar)


        self.gridLayout_4.addWidget(self.frame_4, 1, 0, 1, 1)

        self.line = QFrame(self.frame)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_4.addWidget(self.line, 2, 0, 1, 1)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(5)
        self.gridLayout_2.setVerticalSpacing(0)
        self.gridLayout_2.setContentsMargins(10, 0, 10, 0)
        self.txt_buscarproveedor = QLineEdit(self.frame_2)
        self.txt_buscarproveedor.setObjectName(u"txt_buscarproveedor")

        self.gridLayout_2.addWidget(self.txt_buscarproveedor, 0, 1, 1, 1)

        self.etiqueta_proveedor = QLabel(self.frame_2)
        self.etiqueta_proveedor.setObjectName(u"etiqueta_proveedor")
        self.etiqueta_proveedor.setTextFormat(Qt.AutoText)

        self.gridLayout_2.addWidget(self.etiqueta_proveedor, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.frame_2, 3, 0, 1, 1)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(5)
        self.gridLayout_3.setVerticalSpacing(0)
        self.gridLayout_3.setContentsMargins(10, 0, 10, 0)
        self.etiqueta_codigobarras = QLabel(self.frame_3)
        self.etiqueta_codigobarras.setObjectName(u"etiqueta_codigobarras")

        self.gridLayout_3.addWidget(self.etiqueta_codigobarras, 0, 0, 1, 1)

        self.txt_buscarproducto = QLineEdit(self.frame_3)
        self.txt_buscarproducto.setObjectName(u"txt_buscarproducto")

        self.gridLayout_3.addWidget(self.txt_buscarproducto, 0, 1, 1, 1)

        self.btn_btn_agregar = QToolButton(self.frame_3)
        self.btn_btn_agregar.setObjectName(u"btn_btn_agregar")
        self.btn_btn_agregar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout_3.addWidget(self.btn_btn_agregar, 0, 2, 1, 1)


        self.gridLayout_4.addWidget(self.frame_3, 4, 0, 1, 1)

        self.tabla_ordencompra = QTableView(self.frame)
        self.tabla_ordencompra.setObjectName(u"tabla_ordencompra")

        self.gridLayout_4.addWidget(self.tabla_ordencompra, 5, 0, 1, 1)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)


        self.retranslateUi(Orden_compra)

        QMetaObject.connectSlotsByName(Orden_compra)
    # setupUi

    def retranslateUi(self, Orden_compra):
        Orden_compra.setWindowTitle(QCoreApplication.translate("Orden_compra", u"Form", None))
        self.label_wc_titulo_ordencompra.setText(QCoreApplication.translate("Orden_compra", u"orden de compra", None))
        self.btn_btn_cerrar.setText("")
        self.btn_btn_productosProveedor.setText(QCoreApplication.translate("Orden_compra", u"Productos del proveedor", None))
        self.btn_btn_terminar.setText(QCoreApplication.translate("Orden_compra", u"Terminar", None))
        self.txt_buscarproveedor.setPlaceholderText(QCoreApplication.translate("Orden_compra", u"Buscar por nombre", None))
        self.etiqueta_proveedor.setText(QCoreApplication.translate("Orden_compra", u"Proveedor", None))
        self.etiqueta_codigobarras.setText(QCoreApplication.translate("Orden_compra", u"Codigo del producto", None))
        self.btn_btn_agregar.setText(QCoreApplication.translate("Orden_compra", u"Agregar", None))
    # retranslateUi

