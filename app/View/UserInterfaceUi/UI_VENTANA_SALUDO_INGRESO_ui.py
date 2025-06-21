# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UI_VENTANA_SALUDO_INGRESO.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QPushButton,
    QSizePolicy, QWidget)

class Ui_Saludo_bienvenida(object):
    def setupUi(self, Saludo_bienvenida):
        if not Saludo_bienvenida.objectName():
            Saludo_bienvenida.setObjectName(u"Saludo_bienvenida")
        Saludo_bienvenida.resize(412, 416)
        Saludo_bienvenida.setStyleSheet(u"#contenedor{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"}\n"
"#btn_entrar{\n"
"background-color: #00668c;\n"
"border-top-left-radius: 4px;\n"
"border-bottom-right-radius: 4px;\n"
"color: #fffefb;\n"
"font-weight:bold;\n"
"font-size: 20px;\n"
"font-family:\"Arial\";\n"
"min-width: 150px;\n"
"min-height: 40px;\n"
"}\n"
"#btn_entrar:hover{\n"
"background-color: rgb(0, 122, 167);\n"
"}\n"
"#btn_entrar:pressed{\n"
"	background-color: rgb(0, 86, 118);\n"
"}\n"
"#etiquetaNombreUsuario{\n"
"font-family:\"Arial\";\n"
"font-weight:bold;\n"
"font-size: 40px;\n"
"color:rgb(36, 31, 49);\n"
"}\n"
"#etiquetaBuendia{\n"
"font-family:\"Arial\";\n"
"font-weight:bold;\n"
"font-size: 35px;\n"
"color:rgba(0, 0, 0, 158);\n"
"}\n"
"#etiquetaEslogan{\n"
"font-family:\"Arial\";\n"
"font-weight:bold;\n"
"font-size: 12px;\n"
"color:rgba(0, 0, 0, 158);\n"
"}")
        self.contenedor = QFrame(Saludo_bienvenida)
        self.contenedor.setObjectName(u"contenedor")
        self.contenedor.setGeometry(QRect(20, 10, 371, 391))
        self.contenedor.setFrameShape(QFrame.Shape.StyledPanel)
        self.contenedor.setFrameShadow(QFrame.Shadow.Raised)
        self.etiquetaBuendia = QLabel(self.contenedor)
        self.etiquetaBuendia.setObjectName(u"etiquetaBuendia")
        self.etiquetaBuendia.setEnabled(False)
        self.etiquetaBuendia.setGeometry(QRect(10, 40, 351, 31))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setBold(True)
        self.etiquetaBuendia.setFont(font)
        self.etiquetaBuendia.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.etiquetaNombreUsuario = QLabel(self.contenedor)
        self.etiquetaNombreUsuario.setObjectName(u"etiquetaNombreUsuario")
        self.etiquetaNombreUsuario.setGeometry(QRect(10, 100, 351, 151))
        self.etiquetaNombreUsuario.setFont(font)
        self.etiquetaNombreUsuario.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.etiquetaNombreUsuario.setWordWrap(True)
        self.etiquetaEslogan = QLabel(self.contenedor)
        self.etiquetaEslogan.setObjectName(u"etiquetaEslogan")
        self.etiquetaEslogan.setGeometry(QRect(10, 330, 351, 51))
        self.etiquetaEslogan.setFont(font)
        self.etiquetaEslogan.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.etiquetaEslogan.setWordWrap(True)
        self.btn_entrar = QPushButton(self.contenedor)
        self.btn_entrar.setObjectName(u"btn_entrar")
        self.btn_entrar.setGeometry(QRect(110, 260, 150, 40))
        self.btn_entrar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.retranslateUi(Saludo_bienvenida)

        QMetaObject.connectSlotsByName(Saludo_bienvenida)
    # setupUi

    def retranslateUi(self, Saludo_bienvenida):
        Saludo_bienvenida.setWindowTitle(QCoreApplication.translate("Saludo_bienvenida", u"Form", None))
        self.etiquetaBuendia.setText(QCoreApplication.translate("Saludo_bienvenida", u"Excelente Ma\u00f1ana", None))
        self.etiquetaNombreUsuario.setText(QCoreApplication.translate("Saludo_bienvenida", u"Luis Angel Vallejo Perez", None))
        self.etiquetaEslogan.setText(QCoreApplication.translate("Saludo_bienvenida", u"Los grandes vendedores no venden, hacen que la gente quiera comprar.", None))
        self.btn_entrar.setText(QCoreApplication.translate("Saludo_bienvenida", u"Entrar", None))
    # retranslateUi

