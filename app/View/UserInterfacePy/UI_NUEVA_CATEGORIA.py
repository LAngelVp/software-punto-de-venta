# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UI_NUEVA_CATEGORIA.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QLineEdit, QPlainTextEdit, QPushButton, QSizePolicy,
    QWidget)

class Ui_Nueva_categoria(object):
    def setupUi(self, Nueva_categoria):
        if not Nueva_categoria.objectName():
            Nueva_categoria.setObjectName(u"Nueva_categoria")
        Nueva_categoria.resize(400, 300)
        Nueva_categoria.setMinimumSize(QSize(400, 300))
        Nueva_categoria.setMaximumSize(QSize(400, 300))
        Nueva_categoria.setStyleSheet(u"*{color: #1d1c1c;}\n"
"#Nueva_categoria{\n"
"background: #fffefb; \n"
"}\n"
"[objectName*=\"contenedor\"]{\n"
"background: #fffefb; \n"
"border:none;\n"
"}\n"
"[objectName*=\"etiquetaTitulo_\"]{\n"
"color: #1d1c1c;\n"
"font-size: 18px;\n"
"font-weight:bold;\n"
"font-family:Arial;\n"
"}\n"
"[objectName*=\"etiqueta_\"]{\n"
"color: #1d1c1c;\n"
"font-size: 14px;\n"
"font-weight:bold;\n"
"font-family:Arial;\n"
"}\n"
"[objectName*=\"txt_\"]{\n"
"color: #1d1c1c;\n"
"font-size: 14px;\n"
"font-weight:bold;\n"
"font-family:Arial;\n"
"background: #F5F5F5;\n"
"border:none;\n"
"border-bottom: 1px solid #1d1c1c;\n"
"border-radius:5px;\n"
"}\n"
"[objectName*=\"txtlargo_\"]{\n"
"color: #1d1c1c;\n"
"font-size: 14px;\n"
"font-weight:bold;\n"
"font-family:Arial;\n"
"background: #F5F5F5;\n"
"border:none;\n"
"border-bottom: 1px solid #1d1c1c;\n"
"border-radius:5px;\n"
"min-height:100px;\n"
"}\n"
"[objectName*=\"txt_\"]:focus{\n"
"border-bottom: 2px solid #023375;\n"
"}\n"
"[objectName*=\"txtlargo_\"]:focus{\n"
"border-bottom: 2px "
                        "solid #023375;\n"
"}\n"
"[objectName*=\"btn_btn_\"]{\n"
"color: #fffefb;\n"
"font-size: 14px;\n"
"font-weight:bold;\n"
"font-family:Arial;\n"
"background: #023375;\n"
"border-radius: 5px;\n"
"height: 25px;\n"
"}\n"
"[objectName*=\"btn_btn_\"]:hover{\n"
"background: #68a67d;\n"
"}\n"
"\n"
"")
        self.gridLayout = QGridLayout(Nueva_categoria)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.contenedor = QFrame(Nueva_categoria)
        self.contenedor.setObjectName(u"contenedor")
        self.contenedor.setFrameShape(QFrame.Shape.StyledPanel)
        self.contenedor.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_3 = QGridLayout(self.contenedor)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.etiquetaTitulo_nuevacategoria = QLabel(self.contenedor)
        self.etiquetaTitulo_nuevacategoria.setObjectName(u"etiquetaTitulo_nuevacategoria")

        self.gridLayout_3.addWidget(self.etiquetaTitulo_nuevacategoria, 0, 0, 1, 1)

        self.btn_btn_guardar = QPushButton(self.contenedor)
        self.btn_btn_guardar.setObjectName(u"btn_btn_guardar")
        self.btn_btn_guardar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout_3.addWidget(self.btn_btn_guardar, 3, 0, 1, 1)

        self.contenedor_datos = QFrame(self.contenedor)
        self.contenedor_datos.setObjectName(u"contenedor_datos")
        self.contenedor_datos.setFrameShape(QFrame.Shape.StyledPanel)
        self.contenedor_datos.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.contenedor_datos)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(0)
        self.gridLayout_2.setVerticalSpacing(10)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.etiqueta_nombre = QLabel(self.contenedor_datos)
        self.etiqueta_nombre.setObjectName(u"etiqueta_nombre")

        self.gridLayout_2.addWidget(self.etiqueta_nombre, 0, 0, 1, 1)

        self.txt_nombre = QLineEdit(self.contenedor_datos)
        self.txt_nombre.setObjectName(u"txt_nombre")

        self.gridLayout_2.addWidget(self.txt_nombre, 1, 0, 1, 1)

        self.etiqueta_descripcion = QLabel(self.contenedor_datos)
        self.etiqueta_descripcion.setObjectName(u"etiqueta_descripcion")

        self.gridLayout_2.addWidget(self.etiqueta_descripcion, 2, 0, 1, 1)

        self.txtlargo_descripcion = QPlainTextEdit(self.contenedor_datos)
        self.txtlargo_descripcion.setObjectName(u"txtlargo_descripcion")

        self.gridLayout_2.addWidget(self.txtlargo_descripcion, 3, 0, 1, 1)


        self.gridLayout_3.addWidget(self.contenedor_datos, 2, 0, 1, 1)

        self.line = QFrame(self.contenedor)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_3.addWidget(self.line, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.contenedor, 0, 0, 1, 1)


        self.retranslateUi(Nueva_categoria)

        QMetaObject.connectSlotsByName(Nueva_categoria)
    # setupUi

    def retranslateUi(self, Nueva_categoria):
        Nueva_categoria.setWindowTitle(QCoreApplication.translate("Nueva_categoria", u"Form", None))
        self.etiquetaTitulo_nuevacategoria.setText(QCoreApplication.translate("Nueva_categoria", u"Nueva Categoria", None))
        self.btn_btn_guardar.setText(QCoreApplication.translate("Nueva_categoria", u"Guardar", None))
        self.etiqueta_nombre.setText(QCoreApplication.translate("Nueva_categoria", u"Nombre", None))
        self.etiqueta_descripcion.setText(QCoreApplication.translate("Nueva_categoria", u"Descripci\u00f3n", None))
    # retranslateUi

