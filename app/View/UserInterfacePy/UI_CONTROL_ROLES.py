# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UI_CONTROL_ROLES.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QFrame,
    QGridLayout, QHeaderView, QLabel, QLineEdit,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QTabWidget, QTableView, QWidget)
from ...Source import iconosSVG_rc

class Ui_Control_Roles_Permisos(object):
    def setupUi(self, Control_Roles_Permisos):
        if not Control_Roles_Permisos.objectName():
            Control_Roles_Permisos.setObjectName(u"Control_Roles_Permisos")
        Control_Roles_Permisos.resize(700, 534)
        Control_Roles_Permisos.setMinimumSize(QSize(400, 0))
        Control_Roles_Permisos.setMaximumSize(QSize(800, 16777215))
        Control_Roles_Permisos.setStyleSheet(u"*{color: #1d1c1c;}\n"
"#Control_Roles_Permisos{\n"
"background: #fffefb;\n"
"}\n"
"#etiquetaTitulo_Roles{\n"
"font-size:24px;\n"
"font-family:Arial;\n"
"font-weight:bold;\n"
"color: #1d1c1c;\n"
"margin-bottom:10px;\n"
"}\n"
"[objectName*=\"contenedor\"]{\n"
"background: #fffefb;\n"
"border:none;\n"
"}\n"
"[objectName*=\"etiquetaTitulo_\"]{\n"
"font-size:18px;\n"
"color: #1d1c1c;\n"
"font-weight: bold;\n"
"font-family:Arial;\n"
"}\n"
"[objectName*=\"opcion_\"]{\n"
"font-size:14px;\n"
"color: #1d1c1c;\n"
"font-family:Arial;\n"
"}\n"
"[objectName*=\"etiquetasubtitulo_\"]{\n"
"font-size:14px;\n"
"color: #1d1c1c;\n"
"font-weight: bold;\n"
"font-family:Arial;\n"
"}\n"
"[objectName*=\"etiqueta_\"]{\n"
"font-size:14px;\n"
"color: #1d1c1c;\n"
"font-weight: bold;\n"
"font-family:Arial;\n"
"}\n"
"[objectName*=\"txt_\"]{\n"
"font-size:14px;\n"
"color: #1d1c1c;\n"
"font-family:Arial;\n"
"background: #F5F5F5;\n"
"border-radius:5px;\n"
"border: none;\n"
"border-bottom: 1px solid #1d1c1c;\n"
"min-width: 300px;\n"
"}\n"
"[obje"
                        "ctName*=\"btn_btn_\"]{\n"
"font-size:14px;\n"
"color: #fffefb;\n"
"font-family:Arial;\n"
"font-weight: bold;\n"
"background: #00619a;\n"
"border-radius:5px;\n"
"height: 25px;\n"
"border: none;\n"
"padding-left: 10px;\n"
"padding-right:10px;\n"
"}\n"
"[objectName*=\"txt_\"]:focus{\n"
"border: none;\n"
"border-bottom: 2px solid #023375;\n"
"}\n"
"[objectName*=\"btn_btn_\"]:hover{\n"
"background: #2196F3;\n"
"}\n"
"/*TABLA*/\n"
"\n"
"[objectName*=\"tabla_\"] {\n"
"    font-family: Arial;\n"
"    font-size: 14px;\n"
"background: #F5F5F5;\n"
"}\n"
"\n"
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
"[objectName*=\"tabla"
                        "_\"] QHeaderView::vertical {\n"
"    background-color: #023375;\n"
"    color: white;\n"
"}\n"
"\n"
"QTabWidget::pane {\n"
"        border: none;\n"
"        position: absolute;\n"
"        top: -20px;\n"
"    }\n"
"    \n"
"    /* Pesta\u00f1a no seleccionada */\n"
"    QTabBar::tab {\n"
"        background: #F5F4F1;\n"
"        color: #3B3C3D;\n"
"        border: 1px solid #D3D3D3;\n"
"        border-bottom: none;\n"
"        padding: 6px 15px;\n"
"        min-width: 80px;\n"
"        border-top-left-radius: 4px;\n"
"        border-top-right-radius: 4px;\n"
"        margin-right: 2px;\n"
"    }\n"
"    \n"
"    /* Pesta\u00f1a seleccionada */\n"
"    QTabBar::tab:selected {\n"
"        background: #4791F5;\n"
"        color: white;\n"
"        font-weight: bold;\n"
"    }\n"
"    \n"
"    /* Pesta\u00f1a al pasar el mouse */\n"
"    QTabBar::tab:hover {\n"
"        background: #E8E8E8;\n"
"    }\n"
"    \n"
"    /* Pesta\u00f1a deshabilitada */\n"
"    QTabBar::tab:disabled {\n"
"        background: #EEEEEE;"
                        "\n"
"        color: #AAAAAA;\n"
"    }\n"
"    \n"
"    /* \u00c1rea de las pesta\u00f1as */\n"
"    QTabBar {\n"
"        background: transparent;\n"
"    }")
        self.gridLayout = QGridLayout(Control_Roles_Permisos)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.contenedor = QFrame(Control_Roles_Permisos)
        self.contenedor.setObjectName(u"contenedor")
        self.contenedor.setFrameShape(QFrame.Shape.StyledPanel)
        self.contenedor.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_4 = QGridLayout(self.contenedor)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.etiquetaTitulo_Roles = QLabel(self.contenedor)
        self.etiquetaTitulo_Roles.setObjectName(u"etiquetaTitulo_Roles")

        self.gridLayout_4.addWidget(self.etiquetaTitulo_Roles, 0, 0, 1, 1)

        self.contenedor_funcionesroles = QTabWidget(self.contenedor)
        self.contenedor_funcionesroles.setObjectName(u"contenedor_funcionesroles")
        font = QFont()
        font.setPointSize(13)
        font.setBold(True)
        self.contenedor_funcionesroles.setFont(font)
        self.contenedor_funcionlistaroles = QWidget()
        self.contenedor_funcionlistaroles.setObjectName(u"contenedor_funcionlistaroles")
        self.gridLayout_2 = QGridLayout(self.contenedor_funcionlistaroles)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.contenedor_tabla = QFrame(self.contenedor_funcionlistaroles)
        self.contenedor_tabla.setObjectName(u"contenedor_tabla")
        self.contenedor_tabla.setFrameShape(QFrame.Shape.StyledPanel)
        self.contenedor_tabla.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_3 = QGridLayout(self.contenedor_tabla)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.btn_btn_buscar = QPushButton(self.contenedor_tabla)
        self.btn_btn_buscar.setObjectName(u"btn_btn_buscar")
        self.btn_btn_buscar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout_3.addWidget(self.btn_btn_buscar, 0, 3, 1, 1)

        self.txt_Buscar_nombrerol = QLineEdit(self.contenedor_tabla)
        self.txt_Buscar_nombrerol.setObjectName(u"txt_Buscar_nombrerol")

        self.gridLayout_3.addWidget(self.txt_Buscar_nombrerol, 1, 0, 1, 2)

        self.etiqueta_buscar = QLabel(self.contenedor_tabla)
        self.etiqueta_buscar.setObjectName(u"etiqueta_buscar")

        self.gridLayout_3.addWidget(self.etiqueta_buscar, 0, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 0, 1, 1, 2)

        self.tabla_listaroles = QTableView(self.contenedor_tabla)
        self.tabla_listaroles.setObjectName(u"tabla_listaroles")
        self.tabla_listaroles.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tabla_listaroles.setAlternatingRowColors(True)
        self.tabla_listaroles.setGridStyle(Qt.PenStyle.DashLine)
        self.tabla_listaroles.horizontalHeader().setStretchLastSection(True)

        self.gridLayout_3.addWidget(self.tabla_listaroles, 2, 0, 1, 4)


        self.gridLayout_2.addWidget(self.contenedor_tabla, 0, 0, 1, 5)

        self.btn_btn_eliminarrol = QPushButton(self.contenedor_funcionlistaroles)
        self.btn_btn_eliminarrol.setObjectName(u"btn_btn_eliminarrol")
        icon = QIcon()
        icon.addFile(u":/iconosBlancos/Icons/iconos/Blanco/eliminar_blanco.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_btn_eliminarrol.setIcon(icon)
        self.btn_btn_eliminarrol.setIconSize(QSize(20, 20))

        self.gridLayout_2.addWidget(self.btn_btn_eliminarrol, 2, 4, 1, 1, Qt.AlignmentFlag.AlignRight)

        self.btn_btn_modificarrol = QPushButton(self.contenedor_funcionlistaroles)
        self.btn_btn_modificarrol.setObjectName(u"btn_btn_modificarrol")
        icon1 = QIcon()
        icon1.addFile(u":/iconosBlancos/Icons/iconos/Blanco/actualizar_blanco.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_btn_modificarrol.setIcon(icon1)
        self.btn_btn_modificarrol.setIconSize(QSize(20, 20))

        self.gridLayout_2.addWidget(self.btn_btn_modificarrol, 2, 3, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 2, 1, 1, 1)

        self.contenedor_funcionesroles.addTab(self.contenedor_funcionlistaroles, "")
        self.contenedor_funcioncrearroles = QWidget()
        self.contenedor_funcioncrearroles.setObjectName(u"contenedor_funcioncrearroles")
        self.gridLayout_7 = QGridLayout(self.contenedor_funcioncrearroles)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.contenedor_2 = QFrame(self.contenedor_funcioncrearroles)
        self.contenedor_2.setObjectName(u"contenedor_2")
        self.contenedor_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.contenedor_2.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_5 = QGridLayout(self.contenedor_2)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.btn_btn_agregar = QPushButton(self.contenedor_2)
        self.btn_btn_agregar.setObjectName(u"btn_btn_agregar")
        self.btn_btn_agregar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/iconosBlancos/Icons/iconos/Blanco/guardar_blanco.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_btn_agregar.setIcon(icon2)
        self.btn_btn_agregar.setIconSize(QSize(20, 20))

        self.gridLayout_5.addWidget(self.btn_btn_agregar, 9, 1, 1, 1, Qt.AlignmentFlag.AlignRight)

        self.line = QFrame(self.contenedor_2)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_5.addWidget(self.line, 1, 0, 1, 2)

        self.contenedor_permisos = QScrollArea(self.contenedor_2)
        self.contenedor_permisos.setObjectName(u"contenedor_permisos")
        self.contenedor_permisos.setWidgetResizable(True)
        self.contenedor_permisosscroll = QWidget()
        self.contenedor_permisosscroll.setObjectName(u"contenedor_permisosscroll")
        self.contenedor_permisosscroll.setGeometry(QRect(0, 0, 597, 485))
        self.gridLayout_6 = QGridLayout(self.contenedor_permisosscroll)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.etiquetasubtitulo_puestos = QLabel(self.contenedor_permisosscroll)
        self.etiquetasubtitulo_puestos.setObjectName(u"etiquetasubtitulo_puestos")

        self.gridLayout_6.addWidget(self.etiquetasubtitulo_puestos, 8, 4, 1, 1)

        self.opcion_modificargrupopermisos = QCheckBox(self.contenedor_permisosscroll)
        self.opcion_modificargrupopermisos.setObjectName(u"opcion_modificargrupopermisos")

        self.gridLayout_6.addWidget(self.opcion_modificargrupopermisos, 17, 0, 1, 1)

        self.etiquetasubtitulo_grupopermisos = QLabel(self.contenedor_permisosscroll)
        self.etiquetasubtitulo_grupopermisos.setObjectName(u"etiquetasubtitulo_grupopermisos")

        self.gridLayout_6.addWidget(self.etiquetasubtitulo_grupopermisos, 14, 0, 1, 1)

        self.etiquetasubtitulo_transacciones = QLabel(self.contenedor_permisosscroll)
        self.etiquetasubtitulo_transacciones.setObjectName(u"etiquetasubtitulo_transacciones")

        self.gridLayout_6.addWidget(self.etiquetasubtitulo_transacciones, 14, 2, 1, 1)

        self.etiquetasubtitulo_usuarios = QLabel(self.contenedor_permisosscroll)
        self.etiquetasubtitulo_usuarios.setObjectName(u"etiquetasubtitulo_usuarios")

        self.gridLayout_6.addWidget(self.etiquetasubtitulo_usuarios, 18, 0, 1, 1)

        self.opcion_eliminartransacciones = QCheckBox(self.contenedor_permisosscroll)
        self.opcion_eliminartransacciones.setObjectName(u"opcion_eliminartransacciones")

        self.gridLayout_6.addWidget(self.opcion_eliminartransacciones, 16, 2, 1, 1)

        self.opcion_crearturnos = QCheckBox(self.contenedor_permisosscroll)
        self.opcion_crearturnos.setObjectName(u"opcion_crearturnos")

        self.gridLayout_6.addWidget(self.opcion_crearturnos, 15, 4, 1, 1)

        self.opcion_creargrupopermisos = QCheckBox(self.contenedor_permisosscroll)
        self.opcion_creargrupopermisos.setObjectName(u"opcion_creargrupopermisos")

        self.gridLayout_6.addWidget(self.opcion_creargrupopermisos, 15, 0, 1, 1)

        self.opcion_creartrasacciones = QCheckBox(self.contenedor_permisosscroll)
        self.opcion_creartrasacciones.setObjectName(u"opcion_creartrasacciones")

        self.gridLayout_6.addWidget(self.opcion_creartrasacciones, 15, 2, 1, 1)

        self.etiquetasubtitulo_cliente = QLabel(self.contenedor_permisosscroll)
        self.etiquetasubtitulo_cliente.setObjectName(u"etiquetasubtitulo_cliente")

        self.gridLayout_6.addWidget(self.etiquetasubtitulo_cliente, 4, 4, 1, 1)

        self.opcion_crearempleado = QCheckBox(self.contenedor_permisosscroll)
        self.opcion_crearempleado.setObjectName(u"opcion_crearempleado")

        self.gridLayout_6.addWidget(self.opcion_crearempleado, 5, 0, 1, 1)

        self.etiquetasubtitulo_empleado = QLabel(self.contenedor_permisosscroll)
        self.etiquetasubtitulo_empleado.setObjectName(u"etiquetasubtitulo_empleado")

        self.gridLayout_6.addWidget(self.etiquetasubtitulo_empleado, 4, 0, 1, 1)

        self.opcion_eliminarcliente = QCheckBox(self.contenedor_permisosscroll)
        self.opcion_eliminarcliente.setObjectName(u"opcion_eliminarcliente")

        self.gridLayout_6.addWidget(self.opcion_eliminarcliente, 6, 4, 1, 1)

        self.opcion_modificarsucursal = QCheckBox(self.contenedor_permisosscroll)
        self.opcion_modificarsucursal.setObjectName(u"opcion_modificarsucursal")

        self.gridLayout_6.addWidget(self.opcion_modificarsucursal, 11, 0, 1, 1)

        self.etiquetasubtitulo_venta = QLabel(self.contenedor_permisosscroll)
        self.etiquetasubtitulo_venta.setObjectName(u"etiquetasubtitulo_venta")

        self.gridLayout_6.addWidget(self.etiquetasubtitulo_venta, 0, 0, 1, 1)

        self.etiquetasubtitulo_compra = QLabel(self.contenedor_permisosscroll)
        self.etiquetasubtitulo_compra.setObjectName(u"etiquetasubtitulo_compra")

        self.gridLayout_6.addWidget(self.etiquetasubtitulo_compra, 0, 2, 1, 1)

        self.opcion_eliminarcompra = QCheckBox(self.contenedor_permisosscroll)
        self.opcion_eliminarcompra.setObjectName(u"opcion_eliminarcompra")

        self.gridLayout_6.addWidget(self.opcion_eliminarcompra, 2, 2, 1, 1)

        self.opcion_crearventa = QCheckBox(self.contenedor_permisosscroll)
        self.opcion_crearventa.setObjectName(u"opcion_crearventa")

        self.gridLayout_6.addWidget(self.opcion_crearventa, 1, 0, 1, 1)

        self.etiquetasubtitulo_departamentos = QLabel(self.contenedor_permisosscroll)
        self.etiquetasubtitulo_departamentos.setObjectName(u"etiquetasubtitulo_departamentos")

        self.gridLayout_6.addWidget(self.etiquetasubtitulo_departamentos, 8, 2, 1, 1)

        self.opcion_modificarpuesto = QCheckBox(self.contenedor_permisosscroll)
        self.opcion_modificarpuesto.setObjectName(u"opcion_modificarpuesto")

        self.gridLayout_6.addWidget(self.opcion_modificarpuesto, 11, 4, 1, 1)

        self.opcion_eliminarpuesto = QCheckBox(self.contenedor_permisosscroll)
        self.opcion_eliminarpuesto.setObjectName(u"opcion_eliminarpuesto")

        self.gridLayout_6.addWidget(self.opcion_eliminarpuesto, 10, 4, 1, 1)

        self.etiquetasubtitulo_proveedor = QLabel(self.contenedor_permisosscroll)
        self.etiquetasubtitulo_proveedor.setObjectName(u"etiquetasubtitulo_proveedor")

        self.gridLayout_6.addWidget(self.etiquetasubtitulo_proveedor, 4, 2, 1, 1)

        self.opcion_crearproveedor = QCheckBox(self.contenedor_permisosscroll)
        self.opcion_crearproveedor.setObjectName(u"opcion_crearproveedor")

        self.gridLayout_6.addWidget(self.opcion_crearproveedor, 5, 2, 1, 1)

        self.opcion_eliminarsucursal = QCheckBox(self.contenedor_permisosscroll)
        self.opcion_eliminarsucursal.setObjectName(u"opcion_eliminarsucursal")

        self.gridLayout_6.addWidget(self.opcion_eliminarsucursal, 10, 0, 1, 1)

        self.opcion_modificarcliente = QCheckBox(self.contenedor_permisosscroll)
        self.opcion_modificarcliente.setObjectName(u"opcion_modificarcliente")

        self.gridLayout_6.addWidget(self.opcion_modificarcliente, 7, 4, 1, 1)

        self.etiquetasubtitulo_sucursal = QLabel(self.contenedor_permisosscroll)
        self.etiquetasubtitulo_sucursal.setObjectName(u"etiquetasubtitulo_sucursal")

        self.gridLayout_6.addWidget(self.etiquetasubtitulo_sucursal, 8, 0, 1, 1)

        self.opcion_modificarproveedor = QCheckBox(self.contenedor_permisosscroll)
        self.opcion_modificarproveedor.setObjectName(u"opcion_modificarproveedor")

        self.gridLayout_6.addWidget(self.opcion_modificarproveedor, 7, 2, 1, 1)

        self.opcion_eliminarproveedor = QCheckBox(self.contenedor_permisosscroll)
        self.opcion_eliminarproveedor.setObjectName(u"opcion_eliminarproveedor")

        self.gridLayout_6.addWidget(self.opcion_eliminarproveedor, 6, 2, 1, 1)

        self.opcion_crearcliente = QCheckBox(self.contenedor_permisosscroll)
        self.opcion_crearcliente.setObjectName(u"opcion_crearcliente")

        self.gridLayout_6.addWidget(self.opcion_crearcliente, 5, 4, 1, 1)

        self.opcion_crearsucursal = QCheckBox(self.contenedor_permisosscroll)
        self.opcion_crearsucursal.setObjectName(u"opcion_crearsucursal")

        self.gridLayout_6.addWidget(self.opcion_crearsucursal, 9, 0, 1, 1)

        self.opcion_eliminarventa = QCheckBox(self.contenedor_permisosscroll)
        self.opcion_eliminarventa.setObjectName(u"opcion_eliminarventa")

        self.gridLayout_6.addWidget(self.opcion_eliminarventa, 2, 0, 1, 1)

        self.opcion_crearproducto = QCheckBox(self.contenedor_permisosscroll)
        self.opcion_crearproducto.setObjectName(u"opcion_crearproducto")

        self.gridLayout_6.addWidget(self.opcion_crearproducto, 1, 4, 1, 1)

        self.opcion_crearpuestos = QCheckBox(self.contenedor_permisosscroll)
        self.opcion_crearpuestos.setObjectName(u"opcion_crearpuestos")

        self.gridLayout_6.addWidget(self.opcion_crearpuestos, 9, 4, 1, 1)

        self.opcion_modificarempleado = QCheckBox(self.contenedor_permisosscroll)
        self.opcion_modificarempleado.setObjectName(u"opcion_modificarempleado")

        self.gridLayout_6.addWidget(self.opcion_modificarempleado, 7, 0, 1, 1)

        self.opcion_eliminarempleado = QCheckBox(self.contenedor_permisosscroll)
        self.opcion_eliminarempleado.setObjectName(u"opcion_eliminarempleado")

        self.gridLayout_6.addWidget(self.opcion_eliminarempleado, 6, 0, 1, 1)

        self.opcion_modificarcompra = QCheckBox(self.contenedor_permisosscroll)
        self.opcion_modificarcompra.setObjectName(u"opcion_modificarcompra")

        self.gridLayout_6.addWidget(self.opcion_modificarcompra, 3, 2, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer_3, 12, 4, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer_2, 12, 2, 1, 1)

        self.opcion_crearcompra = QCheckBox(self.contenedor_permisosscroll)
        self.opcion_crearcompra.setObjectName(u"opcion_crearcompra")

        self.gridLayout_6.addWidget(self.opcion_crearcompra, 1, 2, 1, 1)

        self.opcion_eliminarproducto = QCheckBox(self.contenedor_permisosscroll)
        self.opcion_eliminarproducto.setObjectName(u"opcion_eliminarproducto")

        self.gridLayout_6.addWidget(self.opcion_eliminarproducto, 2, 4, 1, 1)

        self.etiquetasubtitulo_producto = QLabel(self.contenedor_permisosscroll)
        self.etiquetasubtitulo_producto.setObjectName(u"etiquetasubtitulo_producto")

        self.gridLayout_6.addWidget(self.etiquetasubtitulo_producto, 0, 4, 1, 1)

        self.opcion_modificarventa = QCheckBox(self.contenedor_permisosscroll)
        self.opcion_modificarventa.setObjectName(u"opcion_modificarventa")

        self.gridLayout_6.addWidget(self.opcion_modificarventa, 3, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer, 12, 0, 1, 1)

        self.opcion_modificarproducto = QCheckBox(self.contenedor_permisosscroll)
        self.opcion_modificarproducto.setObjectName(u"opcion_modificarproducto")

        self.gridLayout_6.addWidget(self.opcion_modificarproducto, 3, 4, 1, 1)

        self.opcion_creardepartamento = QCheckBox(self.contenedor_permisosscroll)
        self.opcion_creardepartamento.setObjectName(u"opcion_creardepartamento")

        self.gridLayout_6.addWidget(self.opcion_creardepartamento, 9, 2, 1, 1)

        self.opcion_eliminardepartamento = QCheckBox(self.contenedor_permisosscroll)
        self.opcion_eliminardepartamento.setObjectName(u"opcion_eliminardepartamento")

        self.gridLayout_6.addWidget(self.opcion_eliminardepartamento, 10, 2, 1, 1)

        self.opcion_modificardepartamento = QCheckBox(self.contenedor_permisosscroll)
        self.opcion_modificardepartamento.setObjectName(u"opcion_modificardepartamento")

        self.gridLayout_6.addWidget(self.opcion_modificardepartamento, 11, 2, 1, 1)

        self.opcion_eliminarturnos = QCheckBox(self.contenedor_permisosscroll)
        self.opcion_eliminarturnos.setObjectName(u"opcion_eliminarturnos")

        self.gridLayout_6.addWidget(self.opcion_eliminarturnos, 16, 4, 1, 1)

        self.opcion_modificartransacciones = QCheckBox(self.contenedor_permisosscroll)
        self.opcion_modificartransacciones.setObjectName(u"opcion_modificartransacciones")

        self.gridLayout_6.addWidget(self.opcion_modificartransacciones, 17, 2, 1, 1)

        self.opcion_eliminarusuarios = QCheckBox(self.contenedor_permisosscroll)
        self.opcion_eliminarusuarios.setObjectName(u"opcion_eliminarusuarios")

        self.gridLayout_6.addWidget(self.opcion_eliminarusuarios, 20, 0, 1, 1)

        self.etiquetasubtitulo_turnos = QLabel(self.contenedor_permisosscroll)
        self.etiquetasubtitulo_turnos.setObjectName(u"etiquetasubtitulo_turnos")

        self.gridLayout_6.addWidget(self.etiquetasubtitulo_turnos, 14, 4, 1, 1)

        self.opcion_eliminargrupopermisos = QCheckBox(self.contenedor_permisosscroll)
        self.opcion_eliminargrupopermisos.setObjectName(u"opcion_eliminargrupopermisos")

        self.gridLayout_6.addWidget(self.opcion_eliminargrupopermisos, 16, 0, 1, 1)

        self.opcion_modificarturnos = QCheckBox(self.contenedor_permisosscroll)
        self.opcion_modificarturnos.setObjectName(u"opcion_modificarturnos")

        self.gridLayout_6.addWidget(self.opcion_modificarturnos, 17, 4, 1, 1)

        self.opcion_crearusuarios = QCheckBox(self.contenedor_permisosscroll)
        self.opcion_crearusuarios.setObjectName(u"opcion_crearusuarios")

        self.gridLayout_6.addWidget(self.opcion_crearusuarios, 19, 0, 1, 1)

        self.opcion_modificarusuarios = QCheckBox(self.contenedor_permisosscroll)
        self.opcion_modificarusuarios.setObjectName(u"opcion_modificarusuarios")

        self.gridLayout_6.addWidget(self.opcion_modificarusuarios, 21, 0, 1, 1)

        self.line_2 = QFrame(self.contenedor_permisosscroll)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_6.addWidget(self.line_2, 0, 1, 22, 1)

        self.line_3 = QFrame(self.contenedor_permisosscroll)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_6.addWidget(self.line_3, 0, 3, 22, 1)

        self.contenedor_permisos.setWidget(self.contenedor_permisosscroll)

        self.gridLayout_5.addWidget(self.contenedor_permisos, 8, 0, 1, 2)

        self.txt_descripcionrol = QLineEdit(self.contenedor_2)
        self.txt_descripcionrol.setObjectName(u"txt_descripcionrol")

        self.gridLayout_5.addWidget(self.txt_descripcionrol, 6, 0, 1, 2)

        self.etiqueta_descripcionrol = QLabel(self.contenedor_2)
        self.etiqueta_descripcionrol.setObjectName(u"etiqueta_descripcionrol")

        self.gridLayout_5.addWidget(self.etiqueta_descripcionrol, 4, 0, 1, 1)

        self.etiquetaTitulo_rol = QLabel(self.contenedor_2)
        self.etiquetaTitulo_rol.setObjectName(u"etiquetaTitulo_rol")

        self.gridLayout_5.addWidget(self.etiquetaTitulo_rol, 0, 0, 1, 1)

        self.etiqueta_nombrerol = QLabel(self.contenedor_2)
        self.etiqueta_nombrerol.setObjectName(u"etiqueta_nombrerol")

        self.gridLayout_5.addWidget(self.etiqueta_nombrerol, 2, 0, 1, 1)

        self.txt_nombrerol = QLineEdit(self.contenedor_2)
        self.txt_nombrerol.setObjectName(u"txt_nombrerol")

        self.gridLayout_5.addWidget(self.txt_nombrerol, 3, 0, 1, 2)


        self.gridLayout_7.addWidget(self.contenedor_2, 0, 0, 1, 1)

        self.contenedor_funcionesroles.addTab(self.contenedor_funcioncrearroles, "")

        self.gridLayout_4.addWidget(self.contenedor_funcionesroles, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.contenedor, 0, 0, 1, 1)

        QWidget.setTabOrder(self.txt_Buscar_nombrerol, self.tabla_listaroles)
        QWidget.setTabOrder(self.tabla_listaroles, self.btn_btn_modificarrol)
        QWidget.setTabOrder(self.btn_btn_modificarrol, self.btn_btn_eliminarrol)
        QWidget.setTabOrder(self.btn_btn_eliminarrol, self.btn_btn_buscar)
        QWidget.setTabOrder(self.btn_btn_buscar, self.txt_nombrerol)
        QWidget.setTabOrder(self.txt_nombrerol, self.txt_descripcionrol)
        QWidget.setTabOrder(self.txt_descripcionrol, self.opcion_crearventa)
        QWidget.setTabOrder(self.opcion_crearventa, self.opcion_eliminarventa)
        QWidget.setTabOrder(self.opcion_eliminarventa, self.opcion_modificarventa)
        QWidget.setTabOrder(self.opcion_modificarventa, self.opcion_crearcompra)
        QWidget.setTabOrder(self.opcion_crearcompra, self.opcion_eliminarcompra)
        QWidget.setTabOrder(self.opcion_eliminarcompra, self.opcion_modificarcompra)
        QWidget.setTabOrder(self.opcion_modificarcompra, self.opcion_crearproducto)
        QWidget.setTabOrder(self.opcion_crearproducto, self.opcion_eliminarproducto)
        QWidget.setTabOrder(self.opcion_eliminarproducto, self.opcion_modificarproducto)
        QWidget.setTabOrder(self.opcion_modificarproducto, self.opcion_crearempleado)
        QWidget.setTabOrder(self.opcion_crearempleado, self.opcion_eliminarempleado)
        QWidget.setTabOrder(self.opcion_eliminarempleado, self.opcion_modificarempleado)
        QWidget.setTabOrder(self.opcion_modificarempleado, self.opcion_crearproveedor)
        QWidget.setTabOrder(self.opcion_crearproveedor, self.opcion_eliminarproveedor)
        QWidget.setTabOrder(self.opcion_eliminarproveedor, self.opcion_modificarproveedor)
        QWidget.setTabOrder(self.opcion_modificarproveedor, self.opcion_crearcliente)
        QWidget.setTabOrder(self.opcion_crearcliente, self.opcion_eliminarcliente)
        QWidget.setTabOrder(self.opcion_eliminarcliente, self.opcion_modificarcliente)
        QWidget.setTabOrder(self.opcion_modificarcliente, self.opcion_crearsucursal)
        QWidget.setTabOrder(self.opcion_crearsucursal, self.opcion_eliminarsucursal)
        QWidget.setTabOrder(self.opcion_eliminarsucursal, self.opcion_modificarsucursal)
        QWidget.setTabOrder(self.opcion_modificarsucursal, self.btn_btn_agregar)
        QWidget.setTabOrder(self.btn_btn_agregar, self.contenedor_permisos)
        QWidget.setTabOrder(self.contenedor_permisos, self.contenedor_funcionesroles)

        self.retranslateUi(Control_Roles_Permisos)

        self.contenedor_funcionesroles.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Control_Roles_Permisos)
    # setupUi

    def retranslateUi(self, Control_Roles_Permisos):
        Control_Roles_Permisos.setWindowTitle(QCoreApplication.translate("Control_Roles_Permisos", u"Form", None))
        self.etiquetaTitulo_Roles.setText(QCoreApplication.translate("Control_Roles_Permisos", u"Roles y permisos", None))
        self.btn_btn_buscar.setText(QCoreApplication.translate("Control_Roles_Permisos", u"BUSCAR", None))
        self.txt_Buscar_nombrerol.setPlaceholderText(QCoreApplication.translate("Control_Roles_Permisos", u"Nombre del rol", None))
        self.etiqueta_buscar.setText(QCoreApplication.translate("Control_Roles_Permisos", u"Buscar:", None))
        self.btn_btn_eliminarrol.setText(QCoreApplication.translate("Control_Roles_Permisos", u"ELIMINAR", None))
        self.btn_btn_modificarrol.setText(QCoreApplication.translate("Control_Roles_Permisos", u"MODIFICAR", None))
        self.contenedor_funcionesroles.setTabText(self.contenedor_funcionesroles.indexOf(self.contenedor_funcionlistaroles), QCoreApplication.translate("Control_Roles_Permisos", u"Lista de roles", None))
        self.btn_btn_agregar.setText(QCoreApplication.translate("Control_Roles_Permisos", u"GUARDAR", None))
        self.etiquetasubtitulo_puestos.setText(QCoreApplication.translate("Control_Roles_Permisos", u"Puestos", None))
        self.opcion_modificargrupopermisos.setText(QCoreApplication.translate("Control_Roles_Permisos", u"Modificar", None))
        self.etiquetasubtitulo_grupopermisos.setText(QCoreApplication.translate("Control_Roles_Permisos", u"Grupo de permisos", None))
        self.etiquetasubtitulo_transacciones.setText(QCoreApplication.translate("Control_Roles_Permisos", u"Transacciones", None))
        self.etiquetasubtitulo_usuarios.setText(QCoreApplication.translate("Control_Roles_Permisos", u"Usuarios", None))
        self.opcion_eliminartransacciones.setText(QCoreApplication.translate("Control_Roles_Permisos", u"Eliminar", None))
        self.opcion_crearturnos.setText(QCoreApplication.translate("Control_Roles_Permisos", u"Crear", None))
        self.opcion_creargrupopermisos.setText(QCoreApplication.translate("Control_Roles_Permisos", u"Crear", None))
        self.opcion_creartrasacciones.setText(QCoreApplication.translate("Control_Roles_Permisos", u"Crear", None))
        self.etiquetasubtitulo_cliente.setText(QCoreApplication.translate("Control_Roles_Permisos", u"Clientes", None))
        self.opcion_crearempleado.setText(QCoreApplication.translate("Control_Roles_Permisos", u"Crear", None))
        self.etiquetasubtitulo_empleado.setText(QCoreApplication.translate("Control_Roles_Permisos", u"Empleados", None))
        self.opcion_eliminarcliente.setText(QCoreApplication.translate("Control_Roles_Permisos", u"Eliminar", None))
        self.opcion_modificarsucursal.setText(QCoreApplication.translate("Control_Roles_Permisos", u"Modificar", None))
        self.etiquetasubtitulo_venta.setText(QCoreApplication.translate("Control_Roles_Permisos", u"Ventas", None))
        self.etiquetasubtitulo_compra.setText(QCoreApplication.translate("Control_Roles_Permisos", u"Compras", None))
        self.opcion_eliminarcompra.setText(QCoreApplication.translate("Control_Roles_Permisos", u"Eliminar", None))
        self.opcion_crearventa.setText(QCoreApplication.translate("Control_Roles_Permisos", u"Crear", None))
        self.etiquetasubtitulo_departamentos.setText(QCoreApplication.translate("Control_Roles_Permisos", u"Departamentos", None))
        self.opcion_modificarpuesto.setText(QCoreApplication.translate("Control_Roles_Permisos", u"Modificar", None))
        self.opcion_eliminarpuesto.setText(QCoreApplication.translate("Control_Roles_Permisos", u"Eliminar", None))
        self.etiquetasubtitulo_proveedor.setText(QCoreApplication.translate("Control_Roles_Permisos", u"Proveedores", None))
        self.opcion_crearproveedor.setText(QCoreApplication.translate("Control_Roles_Permisos", u"Crear", None))
        self.opcion_eliminarsucursal.setText(QCoreApplication.translate("Control_Roles_Permisos", u"Eliminar", None))
        self.opcion_modificarcliente.setText(QCoreApplication.translate("Control_Roles_Permisos", u"Modificar", None))
        self.etiquetasubtitulo_sucursal.setText(QCoreApplication.translate("Control_Roles_Permisos", u"Sucursales", None))
        self.opcion_modificarproveedor.setText(QCoreApplication.translate("Control_Roles_Permisos", u"Modificar", None))
        self.opcion_eliminarproveedor.setText(QCoreApplication.translate("Control_Roles_Permisos", u"Eliminar", None))
        self.opcion_crearcliente.setText(QCoreApplication.translate("Control_Roles_Permisos", u"Crear", None))
        self.opcion_crearsucursal.setText(QCoreApplication.translate("Control_Roles_Permisos", u"Crear", None))
        self.opcion_eliminarventa.setText(QCoreApplication.translate("Control_Roles_Permisos", u"Eliminar", None))
        self.opcion_crearproducto.setText(QCoreApplication.translate("Control_Roles_Permisos", u"Crear", None))
        self.opcion_crearpuestos.setText(QCoreApplication.translate("Control_Roles_Permisos", u"Crear", None))
        self.opcion_modificarempleado.setText(QCoreApplication.translate("Control_Roles_Permisos", u"Modificar", None))
        self.opcion_eliminarempleado.setText(QCoreApplication.translate("Control_Roles_Permisos", u"Eliminar", None))
        self.opcion_modificarcompra.setText(QCoreApplication.translate("Control_Roles_Permisos", u"Modificar", None))
        self.opcion_crearcompra.setText(QCoreApplication.translate("Control_Roles_Permisos", u"Crear", None))
        self.opcion_eliminarproducto.setText(QCoreApplication.translate("Control_Roles_Permisos", u"Eliminar", None))
        self.etiquetasubtitulo_producto.setText(QCoreApplication.translate("Control_Roles_Permisos", u"Productos", None))
        self.opcion_modificarventa.setText(QCoreApplication.translate("Control_Roles_Permisos", u"Modificar", None))
        self.opcion_modificarproducto.setText(QCoreApplication.translate("Control_Roles_Permisos", u"Modificar", None))
        self.opcion_creardepartamento.setText(QCoreApplication.translate("Control_Roles_Permisos", u"Crear", None))
        self.opcion_eliminardepartamento.setText(QCoreApplication.translate("Control_Roles_Permisos", u"Eliminar", None))
        self.opcion_modificardepartamento.setText(QCoreApplication.translate("Control_Roles_Permisos", u"Modificar", None))
        self.opcion_eliminarturnos.setText(QCoreApplication.translate("Control_Roles_Permisos", u"Eliminar", None))
        self.opcion_modificartransacciones.setText(QCoreApplication.translate("Control_Roles_Permisos", u"Modificar", None))
        self.opcion_eliminarusuarios.setText(QCoreApplication.translate("Control_Roles_Permisos", u"Eliminar", None))
        self.etiquetasubtitulo_turnos.setText(QCoreApplication.translate("Control_Roles_Permisos", u"Turnos", None))
        self.opcion_eliminargrupopermisos.setText(QCoreApplication.translate("Control_Roles_Permisos", u"Eliminar", None))
        self.opcion_modificarturnos.setText(QCoreApplication.translate("Control_Roles_Permisos", u"Modificar", None))
        self.opcion_crearusuarios.setText(QCoreApplication.translate("Control_Roles_Permisos", u"Crear", None))
        self.opcion_modificarusuarios.setText(QCoreApplication.translate("Control_Roles_Permisos", u"Modificar", None))
        self.etiqueta_descripcionrol.setText(QCoreApplication.translate("Control_Roles_Permisos", u"Descripci\u00f3n:", None))
        self.etiquetaTitulo_rol.setText(QCoreApplication.translate("Control_Roles_Permisos", u"Nuevo Rol", None))
        self.etiqueta_nombrerol.setText(QCoreApplication.translate("Control_Roles_Permisos", u"Nombre:", None))
        self.contenedor_funcionesroles.setTabText(self.contenedor_funcionesroles.indexOf(self.contenedor_funcioncrearroles), QCoreApplication.translate("Control_Roles_Permisos", u"Agregar roles", None))
    # retranslateUi

