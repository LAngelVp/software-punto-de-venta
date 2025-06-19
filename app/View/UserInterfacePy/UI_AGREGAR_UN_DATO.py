# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UI_AGREGAR_UN_DATO.ui'
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
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Formulario(object):
    def setupUi(self, Formulario):
        if not Formulario.objectName():
            Formulario.setObjectName(u"Formulario")
        Formulario.resize(368, 129)
        Formulario.setStyleSheet(u"#Formulario{\n"
"background: #fffefb;\n"
"}\n"
"[objectName*=\"contenedor\"]{\n"
"background: #fffefb;\n"
"}\n"
"[objectName*=\"etiqueta_\"]{\n"
"font-size:14px;\n"
"font-weight:bold;\n"
"font-family:\"Arial\";\n"
"}\n"
"[objectName*=\"txt\"]{\n"
"font-size:14px;\n"
"font-weight:bold;\n"
"font-family:\"Arial\";\n"
"color:#1d1c1c;\n"
"border:none;\n"
"border-radius:4px;\n"
"background: #F5F5F5;\n"
"border-bottom: 1px solid #1d1c1c;\n"
"}\n"
"[objectName*=\"txt\"]:hover{\n"
"border-bottom: 1px solid #023375;\n"
"}\n"
"[objectName*=\"txt\"]:focus{\n"
"border-bottom: 2px solid #023375;\n"
"}\n"
"[objectName*=\"btn_btn_\"]{\n"
"font-size:14px;\n"
"font-weight:bold;\n"
"font-family:\"Arial\";\n"
"color: #fffefb;\n"
"background: #00619a;\n"
"border:none;\n"
"border-radius:4px;\n"
"padding: 4px 0px;\n"
"}\n"
"#btn_btn_cancelar:hover{\n"
"background: #ee1d52;\n"
"}\n"
"#btn_btn_cancelar:pressed{\n"
"background: #B13636;\n"
"}\n"
"#btn_btn_guardar:hover{\n"
"background: #68a67d;\n"
"}\n"
"#btn_btn_guardar:pressed{\n"
"b"
                        "ackground: #578B69;\n"
"}")
        self.gridLayout = QGridLayout(Formulario)
        self.gridLayout.setObjectName(u"gridLayout")
        self.contenedor = QFrame(Formulario)
        self.contenedor.setObjectName(u"contenedor")
        self.contenedor.setFrameShape(QFrame.StyledPanel)
        self.contenedor.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.contenedor)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.etiqueta_nombre = QLabel(self.contenedor)
        self.etiqueta_nombre.setObjectName(u"etiqueta_nombre")

        self.verticalLayout.addWidget(self.etiqueta_nombre)

        self.txt_nombre = QLineEdit(self.contenedor)
        self.txt_nombre.setObjectName(u"txt_nombre")
        self.txt_nombre.setMaxLength(30)
        self.txt_nombre.setFrame(True)
        self.txt_nombre.setEchoMode(QLineEdit.Normal)
        self.txt_nombre.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.txt_nombre.setClearButtonEnabled(True)

        self.verticalLayout.addWidget(self.txt_nombre)

        self.frame = QFrame(self.contenedor)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_btn_cancelar = QPushButton(self.frame)
        self.btn_btn_cancelar.setObjectName(u"btn_btn_cancelar")
        self.btn_btn_cancelar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout.addWidget(self.btn_btn_cancelar)

        self.btn_btn_guardar = QPushButton(self.frame)
        self.btn_btn_guardar.setObjectName(u"btn_btn_guardar")
        self.btn_btn_guardar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout.addWidget(self.btn_btn_guardar)


        self.verticalLayout.addWidget(self.frame)


        self.gridLayout.addWidget(self.contenedor, 0, 0, 1, 1)


        self.retranslateUi(Formulario)

        QMetaObject.connectSlotsByName(Formulario)
    # setupUi

    def retranslateUi(self, Formulario):
        Formulario.setWindowTitle(QCoreApplication.translate("Formulario", u"Form", None))
        self.etiqueta_nombre.setText(QCoreApplication.translate("Formulario", u"Nombre", None))
        self.btn_btn_cancelar.setText(QCoreApplication.translate("Formulario", u"Cancelar", None))
        self.btn_btn_guardar.setText(QCoreApplication.translate("Formulario", u"Guardar", None))
    # retranslateUi

