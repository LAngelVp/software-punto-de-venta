# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UI_PROCESO_CARGANDO.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QSizePolicy,
    QWidget)
from ...Source import iconsdvg_rc
from ...Source import iconosSVG_rc
from ...Source import gifs_rc

class Ui_Ventana_Cargando(object):
    def setupUi(self, Ventana_Cargando):
        if not Ventana_Cargando.objectName():
            Ventana_Cargando.setObjectName(u"Ventana_Cargando")
        Ventana_Cargando.resize(379, 230)
        Ventana_Cargando.setStyleSheet(u"#contenedor{\n"
"	background-color: rgb(255, 255, 255);\n"
"border-radius:20px;\n"
"}\n"
"#etiqueta_logo_cargando{\n"
"	image: url(:/Icons/IconosSVG/logo_devrous.png);\n"
"}")
        self.contenedor = QFrame(Ventana_Cargando)
        self.contenedor.setObjectName(u"contenedor")
        self.contenedor.setGeometry(QRect(50, 30, 290, 161))
        self.contenedor.setFrameShape(QFrame.StyledPanel)
        self.contenedor.setFrameShadow(QFrame.Raised)
        self.etiqueta_logo_cargando = QLabel(self.contenedor)
        self.etiqueta_logo_cargando.setObjectName(u"etiqueta_logo_cargando")
        self.etiqueta_logo_cargando.setGeometry(QRect(70, 0, 161, 101))
        self.etiqueta_spiner = QLabel(self.contenedor)
        self.etiqueta_spiner.setObjectName(u"etiqueta_spiner")
        self.etiqueta_spiner.setGeometry(QRect(114, 80, 71, 61))
        font = QFont()
        font.setPointSize(11)
        self.etiqueta_spiner.setFont(font)
        self.etiqueta_spiner.setTextFormat(Qt.AutoText)
        self.etiqueta_spiner.setScaledContents(True)
        self.etiqueta_spiner.setAlignment(Qt.AlignCenter)
        self.etiqueta_spiner.setWordWrap(False)

        self.retranslateUi(Ventana_Cargando)

        QMetaObject.connectSlotsByName(Ventana_Cargando)
    # setupUi

    def retranslateUi(self, Ventana_Cargando):
        Ventana_Cargando.setWindowTitle(QCoreApplication.translate("Ventana_Cargando", u"Form", None))
        self.etiqueta_logo_cargando.setText("")
        self.etiqueta_spiner.setText("")
    # retranslateUi

