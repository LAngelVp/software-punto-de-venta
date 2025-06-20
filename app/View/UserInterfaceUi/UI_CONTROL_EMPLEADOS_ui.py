# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UI_CONTROL_EMPLEADOS.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLayout, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QTableView, QToolButton, QWidget)
import ibootstrap_rc
import iconosSVG_rc

class Ui_Control_empleados(object):
    def setupUi(self, Control_empleados):
        if not Control_empleados.objectName():
            Control_empleados.setObjectName(u"Control_empleados")
        Control_empleados.resize(840, 709)
        Control_empleados.setStyleSheet(u"*{color: #1d1c1c;}\n"
"#Control_empleados{\n"
"background-color: #fffefb;\n"
"}\n"
"#panel_controles{\n"
"margin-bottom:20px;\n"
"}\n"
"[objectName*=\"contenedor\"]{\n"
"background-color: #fffefb;\n"
"border:none;\n"
"}\n"
"#label_we_titulo_empleado{\n"
"color:#1d1c1c;\n"
"background-color: #fffefb;\n"
"font-size: 24px;\n"
"font-weight: bold;\n"
"padding-left: 5px;\n"
"text-transform: uppercase;\n"
"font-family: \"Arial\";\n"
"padding-top: 5px;\n"
"}\n"
"#tabla_listaempleados {\n"
"    border: 1px solid;\n"
"    background: #fffefb;\n"
"}\n"
"*[objectName*=\"etiqueta\"]{\n"
"font-family: Arial;\n"
"margin-left: 5px;\n"
"margin-right: 5px;\n"
"font-size: 16px;\n"
"font-weight:bold;\n"
"text-transform: uppercase;\n"
"}\n"
"*[objectName*=\"txt_\"]{\n"
"background-color: #F5F5F5;\n"
"color:#1d1c1c;\n"
"border: none;\n"
"border-bottom: 1px solid;\n"
"border-radius: 5px;\n"
"font-size: 16px;\n"
"font-family: Arial;\n"
"height: 20px;\n"
"}\n"
"*[objectName^=\"txt_\"]::focus{\n"
"border-bottom: 2px solid #023375;\n"
""
                        "}\n"
"*[objectName*=\"btn_btn\"]{\n"
"border:none;\n"
"border-radius: 3px;\n"
"background-color: #00619a;\n"
"font-family: Arial;\n"
"font-size: 14px;\n"
"font-weight: bold;\n"
"text-align: center;\n"
"text-transform: uppercase;\n"
"color: #fffefb;\n"
"padding:2px;\n"
"}\n"
"\n"
"[objectName*=\"btn_btn\"]:hover{\n"
"background-color: #2196F3;\n"
"}\n"
"#btn_btn_eliminar:hover{\n"
"background-color:#EE1D52;\n"
"}\n"
"#btn_btn_agregar:hover{\n"
"background-color: #68a67d;\n"
"}\n"
"#btn_RefrescarTabla{\n"
"border-radius: 2px;\n"
"background: #e0e0e0;\n"
"padding: 5px;\n"
"}\n"
"#btn_RefrescarTabla:hover{\n"
"background: rgb(179, 179, 179);\n"
"}\n"
"#btn_RefrescarTabla:pressed{\n"
"background: #b6ccd8 ;\n"
"}\n"
"[objectName*=\"cajaOpciones\"] {\n"
"    border: none;\n"
"    border-bottom: 1px solid #787878 ;\n"
"    padding: 2px ;\n"
"    background-color: #F5F5F5 ;\n"
"    font-size: 14px ;\n"
"    min-width: 200px ;\n"
"    font-family: \"Arial\" ;\n"
"    color: #1d1c1c ;\n"
"	selection-background-color: #47"
                        "91F5; \n"
"}\n"
"\n"
"/* ESTILO DEL DROPDOWN (LISTA) */\n"
"[objectName*=\"cajaOpciones\"] QListView {\n"
"    background: #F5F5F5 ;\n"
"    border-radius: 3px;\n"
"    outline: none;\n"
"}\n"
"\n"
"/* ESTILO DE LOS \u00cdTEMS */\n"
"[objectName*=\"cajaOpciones\"] QListView::item {\n"
"    padding: 6px 10px ;\n"
"    margin: 2px ;\n"
"}\n"
"/* BOT\u00d3N DESPLEGABLE */\n"
"[objectName*=\"cajaOpciones\"]::drop-down {\n"
"    subcontrol-origin: padding ;\n"
"    subcontrol-position: top right ;\n"
"    padding-right: 5px ;\n"
"    width: 20% ;\n"
"    border-left-width: 1px ;\n"
"    border-radius: 3px ;\n"
"    background-color: #F5F5F5 ;\n"
"}\n"
"/* FLECHA DESPLEGABLE */\n"
"[objectName*=\"cajaOpciones\"]::down-arrow {\n"
"    image: url(:/Icons/Bootstrap/filter-left.svg);\n"
"    width: 17% ;\n"
"    height: 17% ;\n"
"    padding-left: 5px ;\n"
"    padding-right: 5px ;\n"
"}\n"
"/*TABLA*/\n"
"[objectName*=\"tabla_\"] {\n"
"    font-family: Arial;\n"
"    font-size: 14px;\n"
"background: #F5F5F5;\n"
"}\n"
"\n"
""
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
"    color: white;\n"
"}\n"
"\n"
"/* Encabezado vertical */\n"
"[objectName*=\"tabla_\"] QHeaderView::vertical {\n"
"    background-color: #023375;\n"
"    color: white;\n"
"}")
        self.gridLayout = QGridLayout(Control_empleados)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_we_titulo_empleado = QLabel(Control_empleados)
        self.label_we_titulo_empleado.setObjectName(u"label_we_titulo_empleado")
        self.label_we_titulo_empleado.setMinimumSize(QSize(0, 40))
        self.label_we_titulo_empleado.setMaximumSize(QSize(16777215, 40))

        self.gridLayout.addWidget(self.label_we_titulo_empleado, 0, 0, 1, 1)

        self.contenedor = QFrame(Control_empleados)
        self.contenedor.setObjectName(u"contenedor")
        self.contenedor.setFrameShape(QFrame.Shape.StyledPanel)
        self.contenedor.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_5 = QGridLayout(self.contenedor)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setHorizontalSpacing(0)
        self.gridLayout_5.setVerticalSpacing(5)
        self.gridLayout_5.setContentsMargins(5, 0, 5, 5)
        self.contenedor_cuerpo = QWidget(self.contenedor)
        self.contenedor_cuerpo.setObjectName(u"contenedor_cuerpo")
        self.contenedor_cuerpo.setMinimumSize(QSize(0, 0))
        self.contenedor_cuerpo.setMaximumSize(QSize(16777215, 16777215))
        self.gridLayout_2 = QGridLayout(self.contenedor_cuerpo)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetMinAndMaxSize)
        self.contenedor_botones = QWidget(self.contenedor_cuerpo)
        self.contenedor_botones.setObjectName(u"contenedor_botones")
        self.horizontalLayout = QHBoxLayout(self.contenedor_botones)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.btn_btn_agregar = QToolButton(self.contenedor_botones)
        self.btn_btn_agregar.setObjectName(u"btn_btn_agregar")
        self.btn_btn_agregar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/iconosBlancos/Icons/iconos/Blanco/agregar_blanco.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_btn_agregar.setIcon(icon)
        self.btn_btn_agregar.setIconSize(QSize(16, 16))
        self.btn_btn_agregar.setAutoRepeat(False)
        self.btn_btn_agregar.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

        self.horizontalLayout.addWidget(self.btn_btn_agregar)

        self.btn_btn_eliminar = QToolButton(self.contenedor_botones)
        self.btn_btn_eliminar.setObjectName(u"btn_btn_eliminar")
        self.btn_btn_eliminar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/iconosBlancos/Icons/iconos/Blanco/eliminar_blanco.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_btn_eliminar.setIcon(icon1)
        self.btn_btn_eliminar.setIconSize(QSize(16, 16))
        self.btn_btn_eliminar.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

        self.horizontalLayout.addWidget(self.btn_btn_eliminar)

        self.btn_btn_editarempleado = QPushButton(self.contenedor_botones)
        self.btn_btn_editarempleado.setObjectName(u"btn_btn_editarempleado")
        self.btn_btn_editarempleado.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/iconosBlancos/Icons/iconos/Blanco/editar_blanco.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_btn_editarempleado.setIcon(icon2)
        self.btn_btn_editarempleado.setIconSize(QSize(19, 19))

        self.horizontalLayout.addWidget(self.btn_btn_editarempleado)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_RefrescarTabla = QToolButton(self.contenedor_botones)
        self.btn_RefrescarTabla.setObjectName(u"btn_RefrescarTabla")
        self.btn_RefrescarTabla.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/iconosBlancos/Icons/IconosSVG/base_datos_refresh.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_RefrescarTabla.setIcon(icon3)
        self.btn_RefrescarTabla.setIconSize(QSize(16, 16))

        self.horizontalLayout.addWidget(self.btn_RefrescarTabla, 0, Qt.AlignmentFlag.AlignVCenter)


        self.gridLayout_2.addWidget(self.contenedor_botones, 1, 0, 1, 1, Qt.AlignmentFlag.AlignVCenter)

        self.tabla_listaempleados = QTableView(self.contenedor_cuerpo)
        self.tabla_listaempleados.setObjectName(u"tabla_listaempleados")
        self.tabla_listaempleados.setMinimumSize(QSize(0, 0))
        self.tabla_listaempleados.setMaximumSize(QSize(16777215, 16777215))
        self.tabla_listaempleados.setFrameShape(QFrame.Shape.WinPanel)
        self.tabla_listaempleados.setFrameShadow(QFrame.Shadow.Plain)
        self.tabla_listaempleados.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tabla_listaempleados.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tabla_listaempleados.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tabla_listaempleados.setShowGrid(True)
        self.tabla_listaempleados.setGridStyle(Qt.PenStyle.DashDotLine)
        self.tabla_listaempleados.horizontalHeader().setMinimumSectionSize(200)
        self.tabla_listaempleados.horizontalHeader().setDefaultSectionSize(200)

        self.gridLayout_2.addWidget(self.tabla_listaempleados, 3, 0, 1, 1)

        self.contenedor_cabeceraopcionbusqueda = QFrame(self.contenedor_cuerpo)
        self.contenedor_cabeceraopcionbusqueda.setObjectName(u"contenedor_cabeceraopcionbusqueda")
        self.contenedor_cabeceraopcionbusqueda.setFrameShape(QFrame.Shape.StyledPanel)
        self.contenedor_cabeceraopcionbusqueda.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_4 = QGridLayout(self.contenedor_cabeceraopcionbusqueda)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setHorizontalSpacing(10)
        self.gridLayout_4.setVerticalSpacing(0)
        self.gridLayout_4.setContentsMargins(5, 10, 5, 5)
        self.btn_btn_buscar = QToolButton(self.contenedor_cabeceraopcionbusqueda)
        self.btn_btn_buscar.setObjectName(u"btn_btn_buscar")
        self.btn_btn_buscar.setMaximumSize(QSize(16777215, 16777215))
        self.btn_btn_buscar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/iconosBlancos/Icons/iconos/Blanco/buscar_persona_blanco.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_btn_buscar.setIcon(icon4)
        self.btn_btn_buscar.setIconSize(QSize(18, 18))

        self.gridLayout_4.addWidget(self.btn_btn_buscar, 1, 3, 1, 1, Qt.AlignmentFlag.AlignVCenter)

        self.txt_nombreempleado = QLineEdit(self.contenedor_cabeceraopcionbusqueda)
        self.txt_nombreempleado.setObjectName(u"txt_nombreempleado")

        self.gridLayout_4.addWidget(self.txt_nombreempleado, 1, 2, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_2, 1, 4, 1, 1)

        self.txt_idempleado = QLineEdit(self.contenedor_cabeceraopcionbusqueda)
        self.txt_idempleado.setObjectName(u"txt_idempleado")

        self.gridLayout_4.addWidget(self.txt_idempleado, 1, 0, 1, 1)

        self.cajaOpciones_filtroNombreEmpleado = QComboBox(self.contenedor_cabeceraopcionbusqueda)
        self.cajaOpciones_filtroNombreEmpleado.addItem("")
        self.cajaOpciones_filtroNombreEmpleado.addItem("")
        self.cajaOpciones_filtroNombreEmpleado.setObjectName(u"cajaOpciones_filtroNombreEmpleado")

        self.gridLayout_4.addWidget(self.cajaOpciones_filtroNombreEmpleado, 1, 1, 1, 1)

        self.etiqueta_buscar = QLabel(self.contenedor_cabeceraopcionbusqueda)
        self.etiqueta_buscar.setObjectName(u"etiqueta_buscar")

        self.gridLayout_4.addWidget(self.etiqueta_buscar, 0, 0, 1, 5)


        self.gridLayout_2.addWidget(self.contenedor_cabeceraopcionbusqueda, 0, 0, 1, 1)


        self.gridLayout_5.addWidget(self.contenedor_cuerpo, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.contenedor, 1, 0, 1, 1)


        self.retranslateUi(Control_empleados)

        QMetaObject.connectSlotsByName(Control_empleados)
    # setupUi

    def retranslateUi(self, Control_empleados):
        Control_empleados.setWindowTitle(QCoreApplication.translate("Control_empleados", u"Form", None))
        self.label_we_titulo_empleado.setText(QCoreApplication.translate("Control_empleados", u"ADMINISTRACI\u00d3N DE EMPLEADOS", None))
#if QT_CONFIG(tooltip)
        self.btn_btn_agregar.setToolTip(QCoreApplication.translate("Control_empleados", u"Agregar empleado", None))
#endif // QT_CONFIG(tooltip)
        self.btn_btn_agregar.setText(QCoreApplication.translate("Control_empleados", u"Agregar", None))
#if QT_CONFIG(tooltip)
        self.btn_btn_eliminar.setToolTip(QCoreApplication.translate("Control_empleados", u"Eliminar empleado", None))
#endif // QT_CONFIG(tooltip)
        self.btn_btn_eliminar.setText(QCoreApplication.translate("Control_empleados", u"Eliminar", None))
#if QT_CONFIG(tooltip)
        self.btn_btn_editarempleado.setToolTip(QCoreApplication.translate("Control_empleados", u"Editar empleado", None))
#endif // QT_CONFIG(tooltip)
        self.btn_btn_editarempleado.setText(QCoreApplication.translate("Control_empleados", u"EDItar", None))
#if QT_CONFIG(tooltip)
        self.btn_RefrescarTabla.setToolTip(QCoreApplication.translate("Control_empleados", u"Actualizar tabla", None))
#endif // QT_CONFIG(tooltip)
        self.btn_RefrescarTabla.setText("")
#if QT_CONFIG(tooltip)
        self.btn_btn_buscar.setToolTip(QCoreApplication.translate("Control_empleados", u"Buscar empleado", None))
#endif // QT_CONFIG(tooltip)
        self.btn_btn_buscar.setText("")
        self.txt_nombreempleado.setPlaceholderText(QCoreApplication.translate("Control_empleados", u"Nombre de empleado", None))
        self.txt_idempleado.setPlaceholderText(QCoreApplication.translate("Control_empleados", u"Id del empleado", None))
        self.cajaOpciones_filtroNombreEmpleado.setItemText(0, QCoreApplication.translate("Control_empleados", u"IGUAL A", None))
        self.cajaOpciones_filtroNombreEmpleado.setItemText(1, QCoreApplication.translate("Control_empleados", u"QUE CONTENGA", None))

        self.etiqueta_buscar.setText(QCoreApplication.translate("Control_empleados", u"Filtros de Busqueda:", None))
    # retranslateUi

