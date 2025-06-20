# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UI_BIENVENIDA.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QWidget)
from ...Source import ibootstrap_rc
from ...Source import iconsdvg_rc

class Ui_Bienvenida(object):
    def setupUi(self, Bienvenida):
        if not Bienvenida.objectName():
            Bienvenida.setObjectName(u"Bienvenida")
        Bienvenida.resize(600, 450)
        Bienvenida.setMinimumSize(QSize(600, 450))
        Bienvenida.setMaximumSize(QSize(600, 450))
        Bienvenida.setStyleSheet(u"#Bienvenida{\n"
"background-color: #fffefb;\n"
"}\n"
"#contenedor{\n"
"background-color: #fffefb;\n"
"border-radius: 20px;\n"
"}\n"
"#etiqueta_titulo{\n"
"font-family: Arial;\n"
"font-weight:bold;\n"
"font-size: 18px;\n"
"}\n"
"")
        self.contenedor = QWidget(Bienvenida)
        self.contenedor.setObjectName(u"contenedor")
        self.contenedor.setGeometry(QRect(40, 80, 521, 291))
        self.contenedor.setStyleSheet(u"#btn_btn_registrar{\n"
"background-color: rgb(0, 97, 154);\n"
"border-radius: 5px;\n"
"color:#fffefb;\n"
"}\n"
"#btn_btn_registrar:hover{\n"
"background-color:#68a67d;\n"
"}\n"
"#btn_btn_registrar:pressed{\n"
"background-color:#fffefb;\n"
"color:#1d1c1c;\n"
"}")
        self.etiqueta_imagen = QLabel(self.contenedor)
        self.etiqueta_imagen.setObjectName(u"etiqueta_imagen")
        self.etiqueta_imagen.setGeometry(QRect(100, 30, 351, 221))
        self.etiqueta_imagen.setStyleSheet(u"")
        self.etiqueta_imagen.setPixmap(QPixmap(u":/Icons/IconosSVG/ilustracion_hombre_con_computadora.png"))
        self.etiqueta_imagen.setScaledContents(True)
        self.etiqueta_titulo = QLabel(self.contenedor)
        self.etiqueta_titulo.setObjectName(u"etiqueta_titulo")
        self.etiqueta_titulo.setGeometry(QRect(20, 0, 331, 31))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setBold(True)
        self.etiqueta_titulo.setFont(font)
        self.etiqueta_titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.btn_btn_registrar = QPushButton(self.contenedor)
        self.btn_btn_registrar.setObjectName(u"btn_btn_registrar")
        self.btn_btn_registrar.setGeometry(QRect(140, 230, 251, 41))
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(True)
        self.btn_btn_registrar.setFont(font1)
        self.btn_btn_registrar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_btn_registrar.setStyleSheet(u"")
        self.label = QLabel(self.contenedor)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(360, 40, 131, 61))
        self.label.setStyleSheet(u"")
        self.label.setPixmap(QPixmap(u":/Icons/IconosSVG/logo_devrous.png"))
        self.label.setScaledContents(True)
        self.etiqueta_imagen.raise_()
        self.btn_btn_registrar.raise_()
        self.etiqueta_titulo.raise_()
        self.label.raise_()

        self.retranslateUi(Bienvenida)

        QMetaObject.connectSlotsByName(Bienvenida)
    # setupUi

    def retranslateUi(self, Bienvenida):
        Bienvenida.setWindowTitle(QCoreApplication.translate("Bienvenida", u"Form", None))
        self.etiqueta_imagen.setText("")
        self.etiqueta_titulo.setText(QCoreApplication.translate("Bienvenida", u"Bienvenido a tu sistema de negocios", None))
        self.btn_btn_registrar.setText(QCoreApplication.translate("Bienvenida", u"Comencemos a Trabajar", None))
        self.label.setText("")
    # retranslateUi

