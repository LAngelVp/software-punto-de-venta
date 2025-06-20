# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UI_INICIO_SESION.ui'
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
    QWidget)
from ...Source import iconos_rc
from ...Source import iconsdvg_rc
from ...Source import iconosSVG_rc

class Ui_Inicio_Sesion(object):
    def setupUi(self, Inicio_Sesion):
        if not Inicio_Sesion.objectName():
            Inicio_Sesion.setObjectName(u"Inicio_Sesion")
        Inicio_Sesion.resize(616, 468)
        Inicio_Sesion.setMinimumSize(QSize(600, 450))
        Inicio_Sesion.setMaximumSize(QSize(16777215, 16777215))
        Inicio_Sesion.setStyleSheet(u"*{color: #1d1c1c;}\n"
"\n"
"#principal{\n"
"	background-color: rgb(163, 158, 158);\n"
"	border-bottom-right-radius: 25px;\n"
"	border-top-right-radius: 25px;\n"
"}\n"
"#contenedor_global{\n"
"border-top-left-radius: 25px;\n"
"border-bottom-left-radius: 25px;\n"
"border-bottom-right-radius: 25px;\n"
"border-top-right-radius: 25px;\n"
"}\n"
"#contenedor_formulario{\n"
"border-top-left-radius: 25px;\n"
"border-bottom-left-radius: 25px;\n"
"border-bottom-right-radius: 25px;\n"
"border-top-right-radius: 25px;\n"
"}\n"
"#imgFormulario{\n"
"image: url(:/Icons/IconosSVG/logo_devrous.png);\n"
"background: #fffefb;\n"
"padding-left: 15px;\n"
"padding-right: 15px;\n"
"border-top-left-radius: 25px;\n"
"border-bottom-left-radius: 25px;\n"
"}\n"
"#img_Login{\n"
"image: url(:/iconosAzules/Icons/iconos/Azul/inicio_sesion_azul.svg);\n"
"}\n"
"#labelNombreEmpresa{\n"
"	background: transparent;\n"
"}\n"
"[objectName*=\"img_\"]{\n"
"	background: none;\n"
"}\n"
"[objectName^=\"txt\"]{\n"
"	border: none;\n"
"	border-bottom: 1px sol"
                        "id rgb(58, 137, 198);\n"
"	font-size: 14px;\n"
"	font-weight: Arial;\n"
"	background-color:#F5F5F5;\n"
"	border-radius: 4px;\n"
"}\n"
"[objectName^=\"txt\"]:focus{\n"
"	border: none;\n"
"	border-bottom: 1px solid rgb(0, 74, 173);\n"
"}\n"
"QPushButton{\n"
"background-color: #023375;\n"
"font-size:14px;\n"
"color:#fffefb;\n"
"font-weight:bold;\n"
"border-radius: 5px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #2196F3;\n"
"}\n"
"#labelNombreEmpresa{\n"
"	color: #313d44;\n"
"}\n"
"#btnCerrar{\n"
"background:transparent;\n"
"border:none;\n"
"}\n"
"#btnMinimizar{\n"
"background:transparent;\n"
"border:none;\n"
"}\n"
"#img_User{\n"
"background:transparent;\n"
"image: url(:/iconosBlancos/Icons/iconos/Blanco/datos_usuario.svg);\n"
"}\n"
"#img_Password{\n"
"background:transparent;\n"
"image: url(:/iconosBlancos/Icons/iconos/Blanco/password_blanco.svg);\n"
"}")
        self.contenedor_global = QFrame(Inicio_Sesion)
        self.contenedor_global.setObjectName(u"contenedor_global")
        self.contenedor_global.setGeometry(QRect(20, 20, 551, 421))
        self.contenedor_global.setFrameShape(QFrame.Shape.StyledPanel)
        self.contenedor_global.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_4 = QGridLayout(self.contenedor_global)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.contenedor_formulario = QFrame(self.contenedor_global)
        self.contenedor_formulario.setObjectName(u"contenedor_formulario")
        self.contenedor_formulario.setFrameShape(QFrame.Shape.StyledPanel)
        self.contenedor_formulario.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.contenedor_formulario)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.imgFormulario = QLabel(self.contenedor_formulario)
        self.imgFormulario.setObjectName(u"imgFormulario")
        self.imgFormulario.setStyleSheet(u"")

        self.gridLayout.addWidget(self.imgFormulario, 0, 0, 1, 1)

        self.principal = QWidget(self.contenedor_formulario)
        self.principal.setObjectName(u"principal")
        self.principal.setStyleSheet(u"")
        self.img_Login = QLabel(self.principal)
        self.img_Login.setObjectName(u"img_Login")
        self.img_Login.setGeometry(QRect(86, 70, 111, 81))
        self.img_Login.setStyleSheet(u"")
        self.btnAceptar = QPushButton(self.principal)
        self.btnAceptar.setObjectName(u"btnAceptar")
        self.btnAceptar.setGeometry(QRect(20, 270, 231, 31))
        self.btnAceptar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnAceptar.setStyleSheet(u"")
        self.labelNombreEmpresa = QLabel(self.principal)
        self.labelNombreEmpresa.setObjectName(u"labelNombreEmpresa")
        self.labelNombreEmpresa.setGeometry(QRect(60, 370, 141, 21))
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(10)
        font.setBold(True)
        self.labelNombreEmpresa.setFont(font)
        self.labelNombreEmpresa.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.widget = QWidget(self.principal)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(200, 10, 61, 31))
        self.widget.setStyleSheet(u"background: none;")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setSpacing(4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.btnMinimizar = QPushButton(self.widget)
        self.btnMinimizar.setObjectName(u"btnMinimizar")
        self.btnMinimizar.setMinimumSize(QSize(20, 20))
        self.btnMinimizar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnMinimizar.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/iconosBlancos/Icons/iconos/Blanco/minimizar_blanco.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnMinimizar.setIcon(icon)
        self.btnMinimizar.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.btnMinimizar)

        self.btnCerrar = QPushButton(self.widget)
        self.btnCerrar.setObjectName(u"btnCerrar")
        self.btnCerrar.setMinimumSize(QSize(20, 20))
        self.btnCerrar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnCerrar.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/iconosBlancos/Icons/iconos/Blanco/cerrar_blanco.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnCerrar.setIcon(icon1)
        self.btnCerrar.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.btnCerrar)

        self.widget_2 = QWidget(self.principal)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(40, 320, 191, 48))
        self.widget_2.setStyleSheet(u"background-color:none;")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.imgFacebook = QLabel(self.widget_2)
        self.imgFacebook.setObjectName(u"imgFacebook")
        self.imgFacebook.setMinimumSize(QSize(30, 30))
        self.imgFacebook.setMaximumSize(QSize(30, 30))
        self.imgFacebook.setStyleSheet(u"image: url(:/Icons/IconosSVG/facebook.svg);\n"
"background-color: none;")
        self.imgFacebook.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.imgFacebook)

        self.imgLinkedin = QLabel(self.widget_2)
        self.imgLinkedin.setObjectName(u"imgLinkedin")
        self.imgLinkedin.setMinimumSize(QSize(30, 30))
        self.imgLinkedin.setMaximumSize(QSize(30, 30))
        self.imgLinkedin.setStyleSheet(u"image: url(:/Icons/IconosSVG/linkedin.svg);\n"
"background-color: none;")
        self.imgLinkedin.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.imgLinkedin)

        self.imgWhatsapp = QLabel(self.widget_2)
        self.imgWhatsapp.setObjectName(u"imgWhatsapp")
        self.imgWhatsapp.setMinimumSize(QSize(30, 30))
        self.imgWhatsapp.setMaximumSize(QSize(30, 30))
        self.imgWhatsapp.setStyleSheet(u"image: url(:/Icons/IconosSVG/whatsapp.svg);\n"
"background-color: none;")
        self.imgWhatsapp.setScaledContents(False)
        self.imgWhatsapp.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.imgWhatsapp)

        self.layoutWidget = QWidget(self.principal)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(21, 220, 231, 22))
        self.gridLayout_2 = QGridLayout(self.layoutWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(5)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.img_Password = QLabel(self.layoutWidget)
        self.img_Password.setObjectName(u"img_Password")
        self.img_Password.setMinimumSize(QSize(25, 0))
        self.img_Password.setMaximumSize(QSize(25, 16777215))
        self.img_Password.setStyleSheet(u"")
        self.img_Password.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.img_Password, 0, 0, 1, 1)

        self.txt_Password = QLineEdit(self.layoutWidget)
        self.txt_Password.setObjectName(u"txt_Password")
        font1 = QFont()
        self.txt_Password.setFont(font1)
        self.txt_Password.setStyleSheet(u"")
        self.txt_Password.setEchoMode(QLineEdit.EchoMode.Password)
        self.txt_Password.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.txt_Password, 0, 1, 1, 1)

        self.layoutWidget1 = QWidget(self.principal)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(20, 180, 231, 22))
        self.gridLayout_3 = QGridLayout(self.layoutWidget1)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(5)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.img_User = QLabel(self.layoutWidget1)
        self.img_User.setObjectName(u"img_User")
        self.img_User.setMinimumSize(QSize(25, 0))
        self.img_User.setMaximumSize(QSize(25, 16777215))
        self.img_User.setStyleSheet(u"")
        self.img_User.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.img_User, 0, 0, 1, 1)

        self.txt_User = QLineEdit(self.layoutWidget1)
        self.txt_User.setObjectName(u"txt_User")
        self.txt_User.setFont(font1)
        self.txt_User.setStyleSheet(u"")
        self.txt_User.setEchoMode(QLineEdit.EchoMode.Normal)
        self.txt_User.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.txt_User, 0, 1, 1, 1)


        self.gridLayout.addWidget(self.principal, 0, 1, 1, 1)


        self.gridLayout_4.addWidget(self.contenedor_formulario, 0, 0, 1, 1)

        QWidget.setTabOrder(self.txt_User, self.txt_Password)
        QWidget.setTabOrder(self.txt_Password, self.btnAceptar)
        QWidget.setTabOrder(self.btnAceptar, self.btnMinimizar)
        QWidget.setTabOrder(self.btnMinimizar, self.btnCerrar)

        self.retranslateUi(Inicio_Sesion)

        QMetaObject.connectSlotsByName(Inicio_Sesion)
    # setupUi

    def retranslateUi(self, Inicio_Sesion):
        Inicio_Sesion.setWindowTitle(QCoreApplication.translate("Inicio_Sesion", u"Form", None))
        self.imgFormulario.setText("")
        self.img_Login.setText("")
        self.btnAceptar.setText(QCoreApplication.translate("Inicio_Sesion", u"Ingresar", None))
        self.labelNombreEmpresa.setText(QCoreApplication.translate("Inicio_Sesion", u"Systems Dev~Rous", None))
        self.btnMinimizar.setText("")
        self.btnCerrar.setText("")
        self.imgFacebook.setText("")
        self.imgLinkedin.setText("")
        self.imgWhatsapp.setText("")
        self.img_Password.setText("")
        self.txt_Password.setPlaceholderText(QCoreApplication.translate("Inicio_Sesion", u"Contrase\u00f1a", None))
        self.img_User.setText("")
        self.txt_User.setPlaceholderText(QCoreApplication.translate("Inicio_Sesion", u"Nombre de Usuario", None))
    # retranslateUi

