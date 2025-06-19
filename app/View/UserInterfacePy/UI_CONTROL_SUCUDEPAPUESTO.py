# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UI_CONTROL_SUCUDEPAPUESTO.ui'
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
    QLabel, QPushButton, QSizePolicy, QStackedWidget,
    QWidget)
from ...Source import iconsdvg_rc

class Ui_Control_SucursalesDepartamentosPuestos(object):
    def setupUi(self, Control_SucursalesDepartamentosPuestos):
        if not Control_SucursalesDepartamentosPuestos.objectName():
            Control_SucursalesDepartamentosPuestos.setObjectName(u"Control_SucursalesDepartamentosPuestos")
        Control_SucursalesDepartamentosPuestos.resize(900, 600)
        Control_SucursalesDepartamentosPuestos.setMinimumSize(QSize(900, 600))
        Control_SucursalesDepartamentosPuestos.setMaximumSize(QSize(900, 600))
        Control_SucursalesDepartamentosPuestos.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        Control_SucursalesDepartamentosPuestos.setStyleSheet(u"#Control_SucursalesDepartamentosPuestos{\n"
"background: #fffefb;\n"
"}\n"
"[objectName*=\"contenedor\"]{\n"
"background: #fffefb;\n"
"}\n"
"[objectName*=\"btn_btn\"]{\n"
"background: #023375;\n"
"color: #fffefb;\n"
"font-weight:bold;\n"
"font-size: 14px;\n"
"font-family: Arial;\n"
"height: 30px;\n"
"border:none;\n"
"border-radius:5px;\n"
"}\n"
"[objectName*=\"btn_btn\"]:hover{\n"
"background: #2196F3;\n"
"}\n"
"")
        self.gridLayout = QGridLayout(Control_SucursalesDepartamentosPuestos)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.contenedor = QFrame(Control_SucursalesDepartamentosPuestos)
        self.contenedor.setObjectName(u"contenedor")
        self.contenedor.setFrameShape(QFrame.StyledPanel)
        self.contenedor.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.contenedor)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contenedor_botones = QFrame(self.contenedor)
        self.contenedor_botones.setObjectName(u"contenedor_botones")
        self.contenedor_botones.setFrameShape(QFrame.StyledPanel)
        self.contenedor_botones.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.contenedor_botones)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_btn_sucursales = QPushButton(self.contenedor_botones)
        self.btn_btn_sucursales.setObjectName(u"btn_btn_sucursales")
        self.btn_btn_sucursales.setCursor(QCursor(Qt.CursorShape.ArrowCursor))

        self.horizontalLayout.addWidget(self.btn_btn_sucursales)

        self.btn_btn_departamentos = QPushButton(self.contenedor_botones)
        self.btn_btn_departamentos.setObjectName(u"btn_btn_departamentos")
        self.btn_btn_departamentos.setCursor(QCursor(Qt.CursorShape.ArrowCursor))

        self.horizontalLayout.addWidget(self.btn_btn_departamentos)

        self.btn_btn_puestos = QPushButton(self.contenedor_botones)
        self.btn_btn_puestos.setObjectName(u"btn_btn_puestos")
        self.btn_btn_puestos.setCursor(QCursor(Qt.CursorShape.ArrowCursor))

        self.horizontalLayout.addWidget(self.btn_btn_puestos)


        self.gridLayout_2.addWidget(self.contenedor_botones, 0, 0, 1, 1)

        self.contenedor_formularios = QFrame(self.contenedor)
        self.contenedor_formularios.setObjectName(u"contenedor_formularios")
        self.contenedor_formularios.setFrameShape(QFrame.StyledPanel)
        self.contenedor_formularios.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.contenedor_formularios)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.contenedor_paginas = QStackedWidget(self.contenedor_formularios)
        self.contenedor_paginas.setObjectName(u"contenedor_paginas")
        self.contenedor_paginas.setEnabled(True)
        self.contenedor_paginas.setStyleSheet(u"")
        self.pagina_inicial = QWidget()
        self.pagina_inicial.setObjectName(u"pagina_inicial")
        self.gridLayout_3 = QGridLayout(self.pagina_inicial)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label = QLabel(self.pagina_inicial)
        self.label.setObjectName(u"label")
        self.label.setEnabled(False)
        self.label.setMouseTracking(False)
        self.label.setStyleSheet(u"image: url(:/Icons/IconosSVG/logo_devrous.png);")

        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)

        self.contenedor_paginas.addWidget(self.pagina_inicial)

        self.gridLayout_5.addWidget(self.contenedor_paginas, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.contenedor_formularios, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.contenedor, 0, 0, 1, 1)


        self.retranslateUi(Control_SucursalesDepartamentosPuestos)

        self.contenedor_paginas.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Control_SucursalesDepartamentosPuestos)
    # setupUi

    def retranslateUi(self, Control_SucursalesDepartamentosPuestos):
        Control_SucursalesDepartamentosPuestos.setWindowTitle(QCoreApplication.translate("Control_SucursalesDepartamentosPuestos", u"Form", None))
        self.btn_btn_sucursales.setText(QCoreApplication.translate("Control_SucursalesDepartamentosPuestos", u"Sucursales", None))
        self.btn_btn_departamentos.setText(QCoreApplication.translate("Control_SucursalesDepartamentosPuestos", u"Departamentos", None))
        self.btn_btn_puestos.setText(QCoreApplication.translate("Control_SucursalesDepartamentosPuestos", u"Puestos", None))
        self.label.setText("")
    # retranslateUi

