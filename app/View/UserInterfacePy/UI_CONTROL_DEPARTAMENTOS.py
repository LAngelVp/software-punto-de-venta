# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UI_CONTROL_DEPARTAMENTOS.ui'
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

class Ui_Control_departamentos(object):
    def setupUi(self, Control_departamentos):
        if not Control_departamentos.objectName():
            Control_departamentos.setObjectName(u"Control_departamentos")
        Control_departamentos.resize(878, 565)
        Control_departamentos.setStyleSheet(u"*{color: #1d1c1c;}\n"
"#Control_departamentos{\n"
"background: #fffefb;\n"
"}\n"
"[objectName*=\"contenedor\"]{\n"
"background: #fffefb;\n"
"border:none;\n"
"}\n"
"#contenedor_encabezado{\n"
"background: #023375;\n"
"}\n"
"#etiquetaTituloEncabezado{\n"
"color: #fffefb;\n"
"font-size:18px;\n"
"font-weight:bold;\n"
"font-family:Arial;\n"
"}\n"
"[objectName*=\"etiqueta_\"]{\n"
"color: #1d1c1c;\n"
"font-size:14px;\n"
"font-weight:bold;\n"
"font-family:Arial;\n"
"}\n"
"#etiqueta_buscardepartamento{\n"
"max-width:25px;\n"
"max-height:25px;\n"
"width:25px;\n"
"height:25px;\n"
"}\n"
"[objectName*=\"etiquetasubtitulo_\"]{\n"
"color: #1d1c1c;\n"
"font-size:15px;\n"
"font-weight:bold;\n"
"font-family:Arial;\n"
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
"margin-left: 3px;\n"
"margin-right:3px;\n"
"}\n"
"[objectName*=\""
                        "btn_btn_\"]:hover{\n"
"background: #2196F3;\n"
"}\n"
"#btn_btn_eliminar:hover{\n"
"background:#EE1D52;\n"
"}\n"
"[objectName*=\"txt_\"]{\n"
"background: #F5F5F5;\n"
"font-size: 12px;\n"
"border: none;\n"
"border-radius: 5px;\n"
"border-bottom: 1px solid #1d1c1c;\n"
"font-family:Arial;\n"
"}\n"
"[objectName*=\"txt_\"]:focus{\n"
"background: #F5F5F5;\n"
"border-bottom: 2px solid #023375;\n"
"}\n"
"[objectName*=\"txtlargo_\"]{\n"
"background: #F5F5F5;\n"
"font-size: 12px;\n"
"border: none;\n"
"border-radius: 5px;\n"
"border-bottom: 1px solid #1d1c1c;\n"
"font-family:Arial;\n"
"height: 100px;\n"
"max-height: 100px;\n"
"}\n"
"[objectName*=\"txtlargo_\"]:focus{\n"
"background: #F5F5F5;\n"
"border-bottom: 2px solid #023375;\n"
"}\n"
"QListWidget {\n"
"    font-family: Arial;\n"
"    font-size: 14px;\n"
"	background: #F5F5F5;\n"
"}\n"
"/* Barra vertical */\n"
"QListWidget::vertical-scrollbar {\n"
"    border: 1px solid gray;\n"
"    background: #023375;\n"
"    width: 10px;  /* Tama\u00f1o de la barra vertical */\n"
""
                        "    border-radius: 4px;\n"
"}\n"
"\n"
"/* Manejador de la barra vertical */\n"
"QListWidget::vertical-scrollbar::handle {\n"
"    background: #023375;  /* Color del \"manejador\" */\n"
"    min-height: 20px;  /* Altura m\u00ednima del manejador */\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"/* Barra horizontal */\n"
"QListWidget::horizontal-scrollbar {\n"
"    background: #023375;\n"
"    height: 10px;  /* Tama\u00f1o de la barra horizontal */\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"/* Manejador de la barra horizontal */\n"
"QListWidget::horizontal-scrollbar::handle {\n"
"    background: #023375;  /* Color del \"manejador\" */\n"
"    height: 10px;  /* Altura del manejador horizontal */\n"
"    border-radius: 4px;\n"
"}\n"
"")
        self.gridLayout_6 = QGridLayout(Control_departamentos)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(Control_departamentos)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.contenedor_encabezado = QFrame(self.frame)
        self.contenedor_encabezado.setObjectName(u"contenedor_encabezado")
        self.contenedor_encabezado.setFrameShape(QFrame.Shape.StyledPanel)
        self.contenedor_encabezado.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.contenedor_encabezado)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.etiquetaTituloEncabezado = QLabel(self.contenedor_encabezado)
        self.etiquetaTituloEncabezado.setObjectName(u"etiquetaTituloEncabezado")

        self.horizontalLayout.addWidget(self.etiquetaTituloEncabezado)

        self.horizontalSpacer_3 = QSpacerItem(692, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.btn_cerrar = QPushButton(self.contenedor_encabezado)
        self.btn_cerrar.setObjectName(u"btn_cerrar")
        self.btn_cerrar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/Icons/Bootstrap/x-lg.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_cerrar.setIcon(icon)

        self.horizontalLayout.addWidget(self.btn_cerrar)


        self.gridLayout.addWidget(self.contenedor_encabezado, 0, 0, 1, 1)

        self.contenedor = QFrame(self.frame)
        self.contenedor.setObjectName(u"contenedor")
        self.contenedor.setFrameShape(QFrame.Shape.StyledPanel)
        self.contenedor.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.contenedor)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(0)
        self.gridLayout_2.setVerticalSpacing(15)
        self.gridLayout_2.setContentsMargins(0, 10, 0, 0)
        self.btn_btn_eliminar = QPushButton(self.contenedor)
        self.btn_btn_eliminar.setObjectName(u"btn_btn_eliminar")
        self.btn_btn_eliminar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/iconosBlancos/Icons/iconos/Blanco/eliminar_blanco.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_btn_eliminar.setIcon(icon1)
        self.btn_btn_eliminar.setIconSize(QSize(24, 24))

        self.gridLayout_2.addWidget(self.btn_btn_eliminar, 0, 5, 1, 1)

        self.btn_btn_guardar = QPushButton(self.contenedor)
        self.btn_btn_guardar.setObjectName(u"btn_btn_guardar")
        self.btn_btn_guardar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/iconosBlancos/Icons/iconos/Blanco/guardar_blanco.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_btn_guardar.setIcon(icon2)
        self.btn_btn_guardar.setIconSize(QSize(24, 24))

        self.gridLayout_2.addWidget(self.btn_btn_guardar, 0, 3, 1, 1)

        self.btn_btn_actualizar = QPushButton(self.contenedor)
        self.btn_btn_actualizar.setObjectName(u"btn_btn_actualizar")
        self.btn_btn_actualizar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/iconosBlancos/Icons/iconos/Blanco/actualizar_blanco.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_btn_actualizar.setIcon(icon3)
        self.btn_btn_actualizar.setIconSize(QSize(24, 24))

        self.gridLayout_2.addWidget(self.btn_btn_actualizar, 0, 4, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 0, 1, 1, 1)

        self.contenedor_formulario = QFrame(self.contenedor)
        self.contenedor_formulario.setObjectName(u"contenedor_formulario")
        self.contenedor_formulario.setFrameShape(QFrame.Shape.StyledPanel)
        self.contenedor_formulario.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_5 = QGridLayout(self.contenedor_formulario)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.etiqueta_nombredepartamento = QLabel(self.contenedor_formulario)
        self.etiqueta_nombredepartamento.setObjectName(u"etiqueta_nombredepartamento")

        self.gridLayout_5.addWidget(self.etiqueta_nombredepartamento, 0, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_2, 0, 2, 1, 1)

        self.etiquetasubtitulo_departamentosexistentes = QLabel(self.contenedor_formulario)
        self.etiquetasubtitulo_departamentosexistentes.setObjectName(u"etiquetasubtitulo_departamentosexistentes")

        self.gridLayout_5.addWidget(self.etiquetasubtitulo_departamentosexistentes, 1, 4, 1, 1)

        self.etiquetasubtitulo_puestosasignados = QLabel(self.contenedor_formulario)
        self.etiquetasubtitulo_puestosasignados.setObjectName(u"etiquetasubtitulo_puestosasignados")

        self.gridLayout_5.addWidget(self.etiquetasubtitulo_puestosasignados, 1, 5, 1, 1)

        self.etiqueta_descripciondepartamento = QLabel(self.contenedor_formulario)
        self.etiqueta_descripciondepartamento.setObjectName(u"etiqueta_descripciondepartamento")

        self.gridLayout_5.addWidget(self.etiqueta_descripciondepartamento, 2, 0, 1, 2)

        self.lista_departamentosexistentes = QListWidget(self.contenedor_formulario)
        self.lista_departamentosexistentes.setObjectName(u"lista_departamentosexistentes")

        self.gridLayout_5.addWidget(self.lista_departamentosexistentes, 2, 4, 4, 1)

        self.lista_puestosasignados = QListWidget(self.contenedor_formulario)
        self.lista_puestosasignados.setObjectName(u"lista_puestosasignados")

        self.gridLayout_5.addWidget(self.lista_puestosasignados, 2, 5, 4, 1)

        self.txtlargo_descripciondepartamento = QPlainTextEdit(self.contenedor_formulario)
        self.txtlargo_descripciondepartamento.setObjectName(u"txtlargo_descripciondepartamento")
        self.txtlargo_descripciondepartamento.viewport().setProperty(u"cursor", QCursor(Qt.CursorShape.IBeamCursor))

        self.gridLayout_5.addWidget(self.txtlargo_descripciondepartamento, 3, 0, 1, 4)

        self.etiquetasubtitulo_sucursalesexistentes = QLabel(self.contenedor_formulario)
        self.etiquetasubtitulo_sucursalesexistentes.setObjectName(u"etiquetasubtitulo_sucursalesexistentes")

        self.gridLayout_5.addWidget(self.etiquetasubtitulo_sucursalesexistentes, 4, 0, 1, 1)

        self.etiquetasubtitulo_sucursalesvinculadas = QLabel(self.contenedor_formulario)
        self.etiquetasubtitulo_sucursalesvinculadas.setObjectName(u"etiquetasubtitulo_sucursalesvinculadas")
        self.etiquetasubtitulo_sucursalesvinculadas.setWordWrap(True)

        self.gridLayout_5.addWidget(self.etiquetasubtitulo_sucursalesvinculadas, 4, 2, 1, 2)

        self.lista_sucursalesexistentes = QListWidget(self.contenedor_formulario)
        self.lista_sucursalesexistentes.setObjectName(u"lista_sucursalesexistentes")

        self.gridLayout_5.addWidget(self.lista_sucursalesexistentes, 5, 0, 1, 1)

        self.contenedor_botonesvincular = QFrame(self.contenedor_formulario)
        self.contenedor_botonesvincular.setObjectName(u"contenedor_botonesvincular")
        self.contenedor_botonesvincular.setFrameShape(QFrame.Shape.StyledPanel)
        self.contenedor_botonesvincular.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_3 = QGridLayout(self.contenedor_botonesvincular)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.btn_btn_vincular = QPushButton(self.contenedor_botonesvincular)
        self.btn_btn_vincular.setObjectName(u"btn_btn_vincular")
        self.btn_btn_vincular.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/iconosBlancos/Icons/iconos/Blanco/flecha_derecha_blanco.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_btn_vincular.setIcon(icon4)
        self.btn_btn_vincular.setIconSize(QSize(24, 24))

        self.gridLayout_3.addWidget(self.btn_btn_vincular, 0, 0, 1, 1)

        self.btn_btn_desvincular = QPushButton(self.contenedor_botonesvincular)
        self.btn_btn_desvincular.setObjectName(u"btn_btn_desvincular")
        self.btn_btn_desvincular.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u":/iconosBlancos/Icons/iconos/Blanco/flecha_izquierda_blanco.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_btn_desvincular.setIcon(icon5)
        self.btn_btn_desvincular.setIconSize(QSize(24, 24))

        self.gridLayout_3.addWidget(self.btn_btn_desvincular, 1, 0, 1, 1)


        self.gridLayout_5.addWidget(self.contenedor_botonesvincular, 5, 1, 1, 1)

        self.lista_sucursalesvinculadas = QListWidget(self.contenedor_formulario)
        self.lista_sucursalesvinculadas.setObjectName(u"lista_sucursalesvinculadas")

        self.gridLayout_5.addWidget(self.lista_sucursalesvinculadas, 5, 2, 1, 2)

        self.txt_nombredepartamento = QLineEdit(self.contenedor_formulario)
        self.txt_nombredepartamento.setObjectName(u"txt_nombredepartamento")

        self.gridLayout_5.addWidget(self.txt_nombredepartamento, 1, 0, 1, 2)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.txt_buscardepartamento = QLineEdit(self.contenedor_formulario)
        self.txt_buscardepartamento.setObjectName(u"txt_buscardepartamento")

        self.gridLayout_4.addWidget(self.txt_buscardepartamento, 0, 1, 1, 1)

        self.etiqueta_buscardepartamento = QLabel(self.contenedor_formulario)
        self.etiqueta_buscardepartamento.setObjectName(u"etiqueta_buscardepartamento")
        self.etiqueta_buscardepartamento.setPixmap(QPixmap(u":/iconosAzules/Icons/iconos/Azul/buscar_filas_azul.svg"))
        self.etiqueta_buscardepartamento.setScaledContents(True)
        self.etiqueta_buscardepartamento.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.etiqueta_buscardepartamento, 0, 0, 1, 1)


        self.gridLayout_5.addLayout(self.gridLayout_4, 0, 4, 1, 2)


        self.gridLayout_2.addWidget(self.contenedor_formulario, 1, 0, 1, 7)

        self.btn_btn_limpiar = QPushButton(self.contenedor)
        self.btn_btn_limpiar.setObjectName(u"btn_btn_limpiar")
        self.btn_btn_limpiar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon6 = QIcon()
        icon6.addFile(u":/Icons/IconosSVG/borrador.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_btn_limpiar.setIcon(icon6)
        self.btn_btn_limpiar.setIconSize(QSize(25, 25))

        self.gridLayout_2.addWidget(self.btn_btn_limpiar, 0, 2, 1, 1)


        self.gridLayout.addWidget(self.contenedor, 1, 0, 1, 1)


        self.gridLayout_6.addWidget(self.frame, 0, 0, 1, 1)

        QWidget.setTabOrder(self.txt_nombredepartamento, self.txtlargo_descripciondepartamento)
        QWidget.setTabOrder(self.txtlargo_descripciondepartamento, self.btn_btn_vincular)
        QWidget.setTabOrder(self.btn_btn_vincular, self.btn_btn_desvincular)
        QWidget.setTabOrder(self.btn_btn_desvincular, self.lista_sucursalesexistentes)
        QWidget.setTabOrder(self.lista_sucursalesexistentes, self.lista_sucursalesvinculadas)
        QWidget.setTabOrder(self.lista_sucursalesvinculadas, self.txt_buscardepartamento)
        QWidget.setTabOrder(self.txt_buscardepartamento, self.lista_departamentosexistentes)
        QWidget.setTabOrder(self.lista_departamentosexistentes, self.lista_puestosasignados)
        QWidget.setTabOrder(self.lista_puestosasignados, self.btn_btn_guardar)
        QWidget.setTabOrder(self.btn_btn_guardar, self.btn_btn_actualizar)
        QWidget.setTabOrder(self.btn_btn_actualizar, self.btn_btn_eliminar)

        self.retranslateUi(Control_departamentos)

        QMetaObject.connectSlotsByName(Control_departamentos)
    # setupUi

    def retranslateUi(self, Control_departamentos):
        Control_departamentos.setWindowTitle(QCoreApplication.translate("Control_departamentos", u"Form", None))
        self.etiquetaTituloEncabezado.setText(QCoreApplication.translate("Control_departamentos", u"DEPARTAMENTOS", None))
        self.btn_cerrar.setText("")
        self.btn_btn_eliminar.setText(QCoreApplication.translate("Control_departamentos", u"Eliminar", None))
        self.btn_btn_guardar.setText(QCoreApplication.translate("Control_departamentos", u"Guardar", None))
        self.btn_btn_actualizar.setText(QCoreApplication.translate("Control_departamentos", u"Actualizar", None))
        self.etiqueta_nombredepartamento.setText(QCoreApplication.translate("Control_departamentos", u"Nombre del departamento:", None))
        self.etiquetasubtitulo_departamentosexistentes.setText(QCoreApplication.translate("Control_departamentos", u"Departamentos existentes", None))
        self.etiquetasubtitulo_puestosasignados.setText(QCoreApplication.translate("Control_departamentos", u"Puestos Asignados", None))
        self.etiqueta_descripciondepartamento.setText(QCoreApplication.translate("Control_departamentos", u"Descripcion del departamento:", None))
        self.etiquetasubtitulo_sucursalesexistentes.setText(QCoreApplication.translate("Control_departamentos", u"Sucursales existentes:", None))
        self.etiquetasubtitulo_sucursalesvinculadas.setText(QCoreApplication.translate("Control_departamentos", u"Sucusales vinculadas", None))
#if QT_CONFIG(tooltip)
        self.btn_btn_vincular.setToolTip(QCoreApplication.translate("Control_departamentos", u"Vincular", None))
#endif // QT_CONFIG(tooltip)
        self.btn_btn_vincular.setText("")
#if QT_CONFIG(tooltip)
        self.btn_btn_desvincular.setToolTip(QCoreApplication.translate("Control_departamentos", u"Desvincular", None))
#endif // QT_CONFIG(tooltip)
        self.btn_btn_desvincular.setText("")
        self.txt_buscardepartamento.setPlaceholderText(QCoreApplication.translate("Control_departamentos", u" Buscar Departamento", None))
        self.etiqueta_buscardepartamento.setText("")
        self.btn_btn_limpiar.setText("")
    # retranslateUi

