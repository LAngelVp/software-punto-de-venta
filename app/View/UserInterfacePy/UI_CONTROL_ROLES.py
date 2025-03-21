# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/hackl/Documentos/projects/software-punto-de-venta/app/View/UserInterfaceUi/UI_CONTROL_ROLES.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Control_Roles_Permisos(object):
    def setupUi(self, Control_Roles_Permisos):
        Control_Roles_Permisos.setObjectName("Control_Roles_Permisos")
        Control_Roles_Permisos.resize(700, 534)
        Control_Roles_Permisos.setMinimumSize(QtCore.QSize(400, 0))
        Control_Roles_Permisos.setMaximumSize(QtCore.QSize(800, 16777215))
        Control_Roles_Permisos.setStyleSheet("#Control_Roles_Permisos{\n"
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
"[objectName*=\"btn_btn_\"]{\n"
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
"}\n"
"\n"
"/* Barra vertical */\n"
"[objectName*=\"tabla_\"] QScrollBar:vertical {\n"
"    border: 1px solid gray;\n"
"    background: #023375;\n"
"    width: 12px;  /* Fijamos el tamaño de la barra vertical */\n"
"    border-radius: 4px;\n"
"    margin: 22px 0 22px 0;\n"
"}\n"
"\n"
"/* Manejador de la barra vertical */\n"
"[objectName*=\"tabla_\"] QScrollBar::handle:vertical {\n"
"    background: #023375;\n"
"    min-height: 20px;  /* Altura mínima del manejador */\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"/* Elementos de la flecha de la barra vertical */\n"
"[objectName*=\"tabla_\"] QScrollBar::add-line:vertical,\n"
"[objectName*=\"tabla_\"] QScrollBar::sub-line:vertical {\n"
"    background-color: none;\n"
"}\n"
"\n"
"/* Barra horizontal */\n"
"[objectName*=\"tabla_\"] QScrollBar:horizontal {\n"
"    background: #023375;\n"
"    height: 12px;  /* Fijamos el tamaño de la barra horizontal */\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"/* Manejador de la barra horizontal */\n"
"[objectName*=\"tabla_\"] QScrollBar::handle:horizontal {\n"
"    background: #023375;\n"
"    height: 12px;  /* Altura del manejador horizontal */\n"
"    border-radius: 4px;\n"
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
"[objectName*=\"tabla_\"] QHeaderView::vertical {\n"
"    background-color: #023375;\n"
"    color: white;\n"
"}")
        self.gridLayout = QtWidgets.QGridLayout(Control_Roles_Permisos)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.contenedor = QtWidgets.QFrame(Control_Roles_Permisos)
        self.contenedor.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.contenedor.setFrameShadow(QtWidgets.QFrame.Raised)
        self.contenedor.setObjectName("contenedor")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.contenedor)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.etiquetaTitulo_Roles = QtWidgets.QLabel(self.contenedor)
        self.etiquetaTitulo_Roles.setObjectName("etiquetaTitulo_Roles")
        self.gridLayout_4.addWidget(self.etiquetaTitulo_Roles, 0, 0, 1, 1)
        self.contenedor_funcionesroles = QtWidgets.QTabWidget(self.contenedor)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.contenedor_funcionesroles.setFont(font)
        self.contenedor_funcionesroles.setObjectName("contenedor_funcionesroles")
        self.contenedor_funcionlistaroles = QtWidgets.QWidget()
        self.contenedor_funcionlistaroles.setObjectName("contenedor_funcionlistaroles")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.contenedor_funcionlistaroles)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.contenedor_tabla = QtWidgets.QFrame(self.contenedor_funcionlistaroles)
        self.contenedor_tabla.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.contenedor_tabla.setFrameShadow(QtWidgets.QFrame.Raised)
        self.contenedor_tabla.setObjectName("contenedor_tabla")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.contenedor_tabla)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.btn_btn_buscar = QtWidgets.QPushButton(self.contenedor_tabla)
        self.btn_btn_buscar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_btn_buscar.setObjectName("btn_btn_buscar")
        self.gridLayout_3.addWidget(self.btn_btn_buscar, 0, 3, 1, 1)
        self.txt_Buscar_nombrerol = QtWidgets.QLineEdit(self.contenedor_tabla)
        self.txt_Buscar_nombrerol.setObjectName("txt_Buscar_nombrerol")
        self.gridLayout_3.addWidget(self.txt_Buscar_nombrerol, 1, 0, 1, 2)
        self.etiqueta_buscar = QtWidgets.QLabel(self.contenedor_tabla)
        self.etiqueta_buscar.setObjectName("etiqueta_buscar")
        self.gridLayout_3.addWidget(self.etiqueta_buscar, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 1, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 0, 1, 1, 2)
        self.tabla_listaroles = QtWidgets.QTableView(self.contenedor_tabla)
        self.tabla_listaroles.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tabla_listaroles.setAlternatingRowColors(True)
        self.tabla_listaroles.setGridStyle(QtCore.Qt.DashLine)
        self.tabla_listaroles.setObjectName("tabla_listaroles")
        self.tabla_listaroles.horizontalHeader().setStretchLastSection(True)
        self.gridLayout_3.addWidget(self.tabla_listaroles, 2, 0, 1, 4)
        self.gridLayout_2.addWidget(self.contenedor_tabla, 0, 0, 1, 5)
        self.btn_btn_eliminarrol = QtWidgets.QPushButton(self.contenedor_funcionlistaroles)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/iconosBlancos/Icons/iconos/Blanco/eliminar_blanco.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_btn_eliminarrol.setIcon(icon)
        self.btn_btn_eliminarrol.setIconSize(QtCore.QSize(20, 20))
        self.btn_btn_eliminarrol.setObjectName("btn_btn_eliminarrol")
        self.gridLayout_2.addWidget(self.btn_btn_eliminarrol, 2, 4, 1, 1, QtCore.Qt.AlignRight)
        self.btn_btn_modificarrol = QtWidgets.QPushButton(self.contenedor_funcionlistaroles)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/iconosBlancos/Icons/iconos/Blanco/actualizar_blanco.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_btn_modificarrol.setIcon(icon1)
        self.btn_btn_modificarrol.setIconSize(QtCore.QSize(20, 20))
        self.btn_btn_modificarrol.setObjectName("btn_btn_modificarrol")
        self.gridLayout_2.addWidget(self.btn_btn_modificarrol, 2, 3, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 2, 1, 1, 1)
        self.contenedor_funcionesroles.addTab(self.contenedor_funcionlistaroles, "")
        self.contenedor_funcioncrearroles = QtWidgets.QWidget()
        self.contenedor_funcioncrearroles.setObjectName("contenedor_funcioncrearroles")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.contenedor_funcioncrearroles)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.contenedor_2 = QtWidgets.QFrame(self.contenedor_funcioncrearroles)
        self.contenedor_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.contenedor_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.contenedor_2.setObjectName("contenedor_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.contenedor_2)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.btn_btn_agregar = QtWidgets.QPushButton(self.contenedor_2)
        self.btn_btn_agregar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/iconosBlancos/Icons/iconos/Blanco/guardar_blanco.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_btn_agregar.setIcon(icon2)
        self.btn_btn_agregar.setIconSize(QtCore.QSize(20, 20))
        self.btn_btn_agregar.setObjectName("btn_btn_agregar")
        self.gridLayout_5.addWidget(self.btn_btn_agregar, 9, 1, 1, 1, QtCore.Qt.AlignRight)
        self.line = QtWidgets.QFrame(self.contenedor_2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_5.addWidget(self.line, 1, 0, 1, 2)
        self.contenedor_permisos = QtWidgets.QScrollArea(self.contenedor_2)
        self.contenedor_permisos.setWidgetResizable(True)
        self.contenedor_permisos.setObjectName("contenedor_permisos")
        self.contenedor_permisosscroll = QtWidgets.QWidget()
        self.contenedor_permisosscroll.setGeometry(QtCore.QRect(0, 0, 622, 548))
        self.contenedor_permisosscroll.setObjectName("contenedor_permisosscroll")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.contenedor_permisosscroll)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.etiquetasubtitulo_puestos = QtWidgets.QLabel(self.contenedor_permisosscroll)
        self.etiquetasubtitulo_puestos.setObjectName("etiquetasubtitulo_puestos")
        self.gridLayout_6.addWidget(self.etiquetasubtitulo_puestos, 8, 4, 1, 1)
        self.opcion_modificargrupopermisos = QtWidgets.QCheckBox(self.contenedor_permisosscroll)
        self.opcion_modificargrupopermisos.setObjectName("opcion_modificargrupopermisos")
        self.gridLayout_6.addWidget(self.opcion_modificargrupopermisos, 17, 0, 1, 1)
        self.etiquetasubtitulo_grupopermisos = QtWidgets.QLabel(self.contenedor_permisosscroll)
        self.etiquetasubtitulo_grupopermisos.setObjectName("etiquetasubtitulo_grupopermisos")
        self.gridLayout_6.addWidget(self.etiquetasubtitulo_grupopermisos, 14, 0, 1, 1)
        self.etiquetasubtitulo_transacciones = QtWidgets.QLabel(self.contenedor_permisosscroll)
        self.etiquetasubtitulo_transacciones.setObjectName("etiquetasubtitulo_transacciones")
        self.gridLayout_6.addWidget(self.etiquetasubtitulo_transacciones, 14, 2, 1, 1)
        self.etiquetasubtitulo_usuarios = QtWidgets.QLabel(self.contenedor_permisosscroll)
        self.etiquetasubtitulo_usuarios.setObjectName("etiquetasubtitulo_usuarios")
        self.gridLayout_6.addWidget(self.etiquetasubtitulo_usuarios, 18, 0, 1, 1)
        self.opcion_eliminartransacciones = QtWidgets.QCheckBox(self.contenedor_permisosscroll)
        self.opcion_eliminartransacciones.setObjectName("opcion_eliminartransacciones")
        self.gridLayout_6.addWidget(self.opcion_eliminartransacciones, 16, 2, 1, 1)
        self.opcion_crearturnos = QtWidgets.QCheckBox(self.contenedor_permisosscroll)
        self.opcion_crearturnos.setObjectName("opcion_crearturnos")
        self.gridLayout_6.addWidget(self.opcion_crearturnos, 15, 4, 1, 1)
        self.opcion_creargrupopermisos = QtWidgets.QCheckBox(self.contenedor_permisosscroll)
        self.opcion_creargrupopermisos.setObjectName("opcion_creargrupopermisos")
        self.gridLayout_6.addWidget(self.opcion_creargrupopermisos, 15, 0, 1, 1)
        self.opcion_creartrasacciones = QtWidgets.QCheckBox(self.contenedor_permisosscroll)
        self.opcion_creartrasacciones.setObjectName("opcion_creartrasacciones")
        self.gridLayout_6.addWidget(self.opcion_creartrasacciones, 15, 2, 1, 1)
        self.etiquetasubtitulo_cliente = QtWidgets.QLabel(self.contenedor_permisosscroll)
        self.etiquetasubtitulo_cliente.setObjectName("etiquetasubtitulo_cliente")
        self.gridLayout_6.addWidget(self.etiquetasubtitulo_cliente, 4, 4, 1, 1)
        self.opcion_crearempleado = QtWidgets.QCheckBox(self.contenedor_permisosscroll)
        self.opcion_crearempleado.setObjectName("opcion_crearempleado")
        self.gridLayout_6.addWidget(self.opcion_crearempleado, 5, 0, 1, 1)
        self.etiquetasubtitulo_empleado = QtWidgets.QLabel(self.contenedor_permisosscroll)
        self.etiquetasubtitulo_empleado.setObjectName("etiquetasubtitulo_empleado")
        self.gridLayout_6.addWidget(self.etiquetasubtitulo_empleado, 4, 0, 1, 1)
        self.opcion_eliminarcliente = QtWidgets.QCheckBox(self.contenedor_permisosscroll)
        self.opcion_eliminarcliente.setObjectName("opcion_eliminarcliente")
        self.gridLayout_6.addWidget(self.opcion_eliminarcliente, 6, 4, 1, 1)
        self.opcion_modificarsucursal = QtWidgets.QCheckBox(self.contenedor_permisosscroll)
        self.opcion_modificarsucursal.setObjectName("opcion_modificarsucursal")
        self.gridLayout_6.addWidget(self.opcion_modificarsucursal, 11, 0, 1, 1)
        self.etiquetasubtitulo_venta = QtWidgets.QLabel(self.contenedor_permisosscroll)
        self.etiquetasubtitulo_venta.setObjectName("etiquetasubtitulo_venta")
        self.gridLayout_6.addWidget(self.etiquetasubtitulo_venta, 0, 0, 1, 1)
        self.etiquetasubtitulo_compra = QtWidgets.QLabel(self.contenedor_permisosscroll)
        self.etiquetasubtitulo_compra.setObjectName("etiquetasubtitulo_compra")
        self.gridLayout_6.addWidget(self.etiquetasubtitulo_compra, 0, 2, 1, 1)
        self.opcion_eliminarcompra = QtWidgets.QCheckBox(self.contenedor_permisosscroll)
        self.opcion_eliminarcompra.setObjectName("opcion_eliminarcompra")
        self.gridLayout_6.addWidget(self.opcion_eliminarcompra, 2, 2, 1, 1)
        self.opcion_crearventa = QtWidgets.QCheckBox(self.contenedor_permisosscroll)
        self.opcion_crearventa.setObjectName("opcion_crearventa")
        self.gridLayout_6.addWidget(self.opcion_crearventa, 1, 0, 1, 1)
        self.etiquetasubtitulo_departamentos = QtWidgets.QLabel(self.contenedor_permisosscroll)
        self.etiquetasubtitulo_departamentos.setObjectName("etiquetasubtitulo_departamentos")
        self.gridLayout_6.addWidget(self.etiquetasubtitulo_departamentos, 8, 2, 1, 1)
        self.opcion_modificarpuesto = QtWidgets.QCheckBox(self.contenedor_permisosscroll)
        self.opcion_modificarpuesto.setObjectName("opcion_modificarpuesto")
        self.gridLayout_6.addWidget(self.opcion_modificarpuesto, 11, 4, 1, 1)
        self.opcion_eliminarpuesto = QtWidgets.QCheckBox(self.contenedor_permisosscroll)
        self.opcion_eliminarpuesto.setObjectName("opcion_eliminarpuesto")
        self.gridLayout_6.addWidget(self.opcion_eliminarpuesto, 10, 4, 1, 1)
        self.etiquetasubtitulo_proveedor = QtWidgets.QLabel(self.contenedor_permisosscroll)
        self.etiquetasubtitulo_proveedor.setObjectName("etiquetasubtitulo_proveedor")
        self.gridLayout_6.addWidget(self.etiquetasubtitulo_proveedor, 4, 2, 1, 1)
        self.opcion_crearproveedor = QtWidgets.QCheckBox(self.contenedor_permisosscroll)
        self.opcion_crearproveedor.setObjectName("opcion_crearproveedor")
        self.gridLayout_6.addWidget(self.opcion_crearproveedor, 5, 2, 1, 1)
        self.opcion_eliminarsucursal = QtWidgets.QCheckBox(self.contenedor_permisosscroll)
        self.opcion_eliminarsucursal.setObjectName("opcion_eliminarsucursal")
        self.gridLayout_6.addWidget(self.opcion_eliminarsucursal, 10, 0, 1, 1)
        self.opcion_modificarcliente = QtWidgets.QCheckBox(self.contenedor_permisosscroll)
        self.opcion_modificarcliente.setObjectName("opcion_modificarcliente")
        self.gridLayout_6.addWidget(self.opcion_modificarcliente, 7, 4, 1, 1)
        self.etiquetasubtitulo_sucursal = QtWidgets.QLabel(self.contenedor_permisosscroll)
        self.etiquetasubtitulo_sucursal.setObjectName("etiquetasubtitulo_sucursal")
        self.gridLayout_6.addWidget(self.etiquetasubtitulo_sucursal, 8, 0, 1, 1)
        self.opcion_modificarproveedor = QtWidgets.QCheckBox(self.contenedor_permisosscroll)
        self.opcion_modificarproveedor.setObjectName("opcion_modificarproveedor")
        self.gridLayout_6.addWidget(self.opcion_modificarproveedor, 7, 2, 1, 1)
        self.opcion_eliminarproveedor = QtWidgets.QCheckBox(self.contenedor_permisosscroll)
        self.opcion_eliminarproveedor.setObjectName("opcion_eliminarproveedor")
        self.gridLayout_6.addWidget(self.opcion_eliminarproveedor, 6, 2, 1, 1)
        self.opcion_crearcliente = QtWidgets.QCheckBox(self.contenedor_permisosscroll)
        self.opcion_crearcliente.setObjectName("opcion_crearcliente")
        self.gridLayout_6.addWidget(self.opcion_crearcliente, 5, 4, 1, 1)
        self.opcion_crearsucursal = QtWidgets.QCheckBox(self.contenedor_permisosscroll)
        self.opcion_crearsucursal.setObjectName("opcion_crearsucursal")
        self.gridLayout_6.addWidget(self.opcion_crearsucursal, 9, 0, 1, 1)
        self.opcion_eliminarventa = QtWidgets.QCheckBox(self.contenedor_permisosscroll)
        self.opcion_eliminarventa.setObjectName("opcion_eliminarventa")
        self.gridLayout_6.addWidget(self.opcion_eliminarventa, 2, 0, 1, 1)
        self.opcion_crearproducto = QtWidgets.QCheckBox(self.contenedor_permisosscroll)
        self.opcion_crearproducto.setObjectName("opcion_crearproducto")
        self.gridLayout_6.addWidget(self.opcion_crearproducto, 1, 4, 1, 1)
        self.opcion_crearpuestos = QtWidgets.QCheckBox(self.contenedor_permisosscroll)
        self.opcion_crearpuestos.setObjectName("opcion_crearpuestos")
        self.gridLayout_6.addWidget(self.opcion_crearpuestos, 9, 4, 1, 1)
        self.opcion_modificarempleado = QtWidgets.QCheckBox(self.contenedor_permisosscroll)
        self.opcion_modificarempleado.setObjectName("opcion_modificarempleado")
        self.gridLayout_6.addWidget(self.opcion_modificarempleado, 7, 0, 1, 1)
        self.opcion_eliminarempleado = QtWidgets.QCheckBox(self.contenedor_permisosscroll)
        self.opcion_eliminarempleado.setObjectName("opcion_eliminarempleado")
        self.gridLayout_6.addWidget(self.opcion_eliminarempleado, 6, 0, 1, 1)
        self.opcion_modificarcompra = QtWidgets.QCheckBox(self.contenedor_permisosscroll)
        self.opcion_modificarcompra.setObjectName("opcion_modificarcompra")
        self.gridLayout_6.addWidget(self.opcion_modificarcompra, 3, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_6.addItem(spacerItem3, 12, 4, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_6.addItem(spacerItem4, 12, 2, 1, 1)
        self.opcion_crearcompra = QtWidgets.QCheckBox(self.contenedor_permisosscroll)
        self.opcion_crearcompra.setObjectName("opcion_crearcompra")
        self.gridLayout_6.addWidget(self.opcion_crearcompra, 1, 2, 1, 1)
        self.opcion_eliminarproducto = QtWidgets.QCheckBox(self.contenedor_permisosscroll)
        self.opcion_eliminarproducto.setObjectName("opcion_eliminarproducto")
        self.gridLayout_6.addWidget(self.opcion_eliminarproducto, 2, 4, 1, 1)
        self.etiquetasubtitulo_producto = QtWidgets.QLabel(self.contenedor_permisosscroll)
        self.etiquetasubtitulo_producto.setObjectName("etiquetasubtitulo_producto")
        self.gridLayout_6.addWidget(self.etiquetasubtitulo_producto, 0, 4, 1, 1)
        self.opcion_modificarventa = QtWidgets.QCheckBox(self.contenedor_permisosscroll)
        self.opcion_modificarventa.setObjectName("opcion_modificarventa")
        self.gridLayout_6.addWidget(self.opcion_modificarventa, 3, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_6.addItem(spacerItem5, 12, 0, 1, 1)
        self.opcion_modificarproducto = QtWidgets.QCheckBox(self.contenedor_permisosscroll)
        self.opcion_modificarproducto.setObjectName("opcion_modificarproducto")
        self.gridLayout_6.addWidget(self.opcion_modificarproducto, 3, 4, 1, 1)
        self.opcion_creardepartamento = QtWidgets.QCheckBox(self.contenedor_permisosscroll)
        self.opcion_creardepartamento.setObjectName("opcion_creardepartamento")
        self.gridLayout_6.addWidget(self.opcion_creardepartamento, 9, 2, 1, 1)
        self.opcion_eliminardepartamento = QtWidgets.QCheckBox(self.contenedor_permisosscroll)
        self.opcion_eliminardepartamento.setObjectName("opcion_eliminardepartamento")
        self.gridLayout_6.addWidget(self.opcion_eliminardepartamento, 10, 2, 1, 1)
        self.opcion_modificardepartamento = QtWidgets.QCheckBox(self.contenedor_permisosscroll)
        self.opcion_modificardepartamento.setObjectName("opcion_modificardepartamento")
        self.gridLayout_6.addWidget(self.opcion_modificardepartamento, 11, 2, 1, 1)
        self.opcion_eliminarturnos = QtWidgets.QCheckBox(self.contenedor_permisosscroll)
        self.opcion_eliminarturnos.setObjectName("opcion_eliminarturnos")
        self.gridLayout_6.addWidget(self.opcion_eliminarturnos, 16, 4, 1, 1)
        self.opcion_modificartransacciones = QtWidgets.QCheckBox(self.contenedor_permisosscroll)
        self.opcion_modificartransacciones.setObjectName("opcion_modificartransacciones")
        self.gridLayout_6.addWidget(self.opcion_modificartransacciones, 17, 2, 1, 1)
        self.opcion_eliminarusuarios = QtWidgets.QCheckBox(self.contenedor_permisosscroll)
        self.opcion_eliminarusuarios.setObjectName("opcion_eliminarusuarios")
        self.gridLayout_6.addWidget(self.opcion_eliminarusuarios, 20, 0, 1, 1)
        self.etiquetasubtitulo_turnos = QtWidgets.QLabel(self.contenedor_permisosscroll)
        self.etiquetasubtitulo_turnos.setObjectName("etiquetasubtitulo_turnos")
        self.gridLayout_6.addWidget(self.etiquetasubtitulo_turnos, 14, 4, 1, 1)
        self.opcion_eliminargrupopermisos = QtWidgets.QCheckBox(self.contenedor_permisosscroll)
        self.opcion_eliminargrupopermisos.setObjectName("opcion_eliminargrupopermisos")
        self.gridLayout_6.addWidget(self.opcion_eliminargrupopermisos, 16, 0, 1, 1)
        self.opcion_modificarturnos = QtWidgets.QCheckBox(self.contenedor_permisosscroll)
        self.opcion_modificarturnos.setObjectName("opcion_modificarturnos")
        self.gridLayout_6.addWidget(self.opcion_modificarturnos, 17, 4, 1, 1)
        self.opcion_crearusuarios = QtWidgets.QCheckBox(self.contenedor_permisosscroll)
        self.opcion_crearusuarios.setObjectName("opcion_crearusuarios")
        self.gridLayout_6.addWidget(self.opcion_crearusuarios, 19, 0, 1, 1)
        self.opcion_modificarusuarios = QtWidgets.QCheckBox(self.contenedor_permisosscroll)
        self.opcion_modificarusuarios.setObjectName("opcion_modificarusuarios")
        self.gridLayout_6.addWidget(self.opcion_modificarusuarios, 21, 0, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.contenedor_permisosscroll)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_6.addWidget(self.line_2, 0, 1, 22, 1)
        self.line_3 = QtWidgets.QFrame(self.contenedor_permisosscroll)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout_6.addWidget(self.line_3, 0, 3, 22, 1)
        self.contenedor_permisos.setWidget(self.contenedor_permisosscroll)
        self.gridLayout_5.addWidget(self.contenedor_permisos, 8, 0, 1, 2)
        self.txt_descripcionrol = QtWidgets.QLineEdit(self.contenedor_2)
        self.txt_descripcionrol.setObjectName("txt_descripcionrol")
        self.gridLayout_5.addWidget(self.txt_descripcionrol, 6, 0, 1, 2)
        self.etiqueta_descripcionrol = QtWidgets.QLabel(self.contenedor_2)
        self.etiqueta_descripcionrol.setObjectName("etiqueta_descripcionrol")
        self.gridLayout_5.addWidget(self.etiqueta_descripcionrol, 4, 0, 1, 1)
        self.etiquetaTitulo_rol = QtWidgets.QLabel(self.contenedor_2)
        self.etiquetaTitulo_rol.setObjectName("etiquetaTitulo_rol")
        self.gridLayout_5.addWidget(self.etiquetaTitulo_rol, 0, 0, 1, 1)
        self.etiqueta_nombrerol = QtWidgets.QLabel(self.contenedor_2)
        self.etiqueta_nombrerol.setObjectName("etiqueta_nombrerol")
        self.gridLayout_5.addWidget(self.etiqueta_nombrerol, 2, 0, 1, 1)
        self.txt_nombrerol = QtWidgets.QLineEdit(self.contenedor_2)
        self.txt_nombrerol.setObjectName("txt_nombrerol")
        self.gridLayout_5.addWidget(self.txt_nombrerol, 3, 0, 1, 2)
        self.gridLayout_7.addWidget(self.contenedor_2, 0, 0, 1, 1)
        self.contenedor_funcionesroles.addTab(self.contenedor_funcioncrearroles, "")
        self.gridLayout_4.addWidget(self.contenedor_funcionesroles, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.contenedor, 0, 0, 1, 1)

        self.retranslateUi(Control_Roles_Permisos)
        self.contenedor_funcionesroles.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Control_Roles_Permisos)
        Control_Roles_Permisos.setTabOrder(self.txt_Buscar_nombrerol, self.tabla_listaroles)
        Control_Roles_Permisos.setTabOrder(self.tabla_listaroles, self.btn_btn_modificarrol)
        Control_Roles_Permisos.setTabOrder(self.btn_btn_modificarrol, self.btn_btn_eliminarrol)
        Control_Roles_Permisos.setTabOrder(self.btn_btn_eliminarrol, self.btn_btn_buscar)
        Control_Roles_Permisos.setTabOrder(self.btn_btn_buscar, self.txt_nombrerol)
        Control_Roles_Permisos.setTabOrder(self.txt_nombrerol, self.txt_descripcionrol)
        Control_Roles_Permisos.setTabOrder(self.txt_descripcionrol, self.opcion_crearventa)
        Control_Roles_Permisos.setTabOrder(self.opcion_crearventa, self.opcion_eliminarventa)
        Control_Roles_Permisos.setTabOrder(self.opcion_eliminarventa, self.opcion_modificarventa)
        Control_Roles_Permisos.setTabOrder(self.opcion_modificarventa, self.opcion_crearcompra)
        Control_Roles_Permisos.setTabOrder(self.opcion_crearcompra, self.opcion_eliminarcompra)
        Control_Roles_Permisos.setTabOrder(self.opcion_eliminarcompra, self.opcion_modificarcompra)
        Control_Roles_Permisos.setTabOrder(self.opcion_modificarcompra, self.opcion_crearproducto)
        Control_Roles_Permisos.setTabOrder(self.opcion_crearproducto, self.opcion_eliminarproducto)
        Control_Roles_Permisos.setTabOrder(self.opcion_eliminarproducto, self.opcion_modificarproducto)
        Control_Roles_Permisos.setTabOrder(self.opcion_modificarproducto, self.opcion_crearempleado)
        Control_Roles_Permisos.setTabOrder(self.opcion_crearempleado, self.opcion_eliminarempleado)
        Control_Roles_Permisos.setTabOrder(self.opcion_eliminarempleado, self.opcion_modificarempleado)
        Control_Roles_Permisos.setTabOrder(self.opcion_modificarempleado, self.opcion_crearproveedor)
        Control_Roles_Permisos.setTabOrder(self.opcion_crearproveedor, self.opcion_eliminarproveedor)
        Control_Roles_Permisos.setTabOrder(self.opcion_eliminarproveedor, self.opcion_modificarproveedor)
        Control_Roles_Permisos.setTabOrder(self.opcion_modificarproveedor, self.opcion_crearcliente)
        Control_Roles_Permisos.setTabOrder(self.opcion_crearcliente, self.opcion_eliminarcliente)
        Control_Roles_Permisos.setTabOrder(self.opcion_eliminarcliente, self.opcion_modificarcliente)
        Control_Roles_Permisos.setTabOrder(self.opcion_modificarcliente, self.opcion_crearsucursal)
        Control_Roles_Permisos.setTabOrder(self.opcion_crearsucursal, self.opcion_eliminarsucursal)
        Control_Roles_Permisos.setTabOrder(self.opcion_eliminarsucursal, self.opcion_modificarsucursal)
        Control_Roles_Permisos.setTabOrder(self.opcion_modificarsucursal, self.btn_btn_agregar)
        Control_Roles_Permisos.setTabOrder(self.btn_btn_agregar, self.contenedor_permisos)
        Control_Roles_Permisos.setTabOrder(self.contenedor_permisos, self.contenedor_funcionesroles)

    def retranslateUi(self, Control_Roles_Permisos):
        _translate = QtCore.QCoreApplication.translate
        Control_Roles_Permisos.setWindowTitle(_translate("Control_Roles_Permisos", "Form"))
        self.etiquetaTitulo_Roles.setText(_translate("Control_Roles_Permisos", "Roles y permisos"))
        self.btn_btn_buscar.setText(_translate("Control_Roles_Permisos", "BUSCAR"))
        self.txt_Buscar_nombrerol.setPlaceholderText(_translate("Control_Roles_Permisos", "Nombre del rol"))
        self.etiqueta_buscar.setText(_translate("Control_Roles_Permisos", "Buscar:"))
        self.btn_btn_eliminarrol.setText(_translate("Control_Roles_Permisos", "ELIMINAR"))
        self.btn_btn_modificarrol.setText(_translate("Control_Roles_Permisos", "MODIFICAR"))
        self.contenedor_funcionesroles.setTabText(self.contenedor_funcionesroles.indexOf(self.contenedor_funcionlistaroles), _translate("Control_Roles_Permisos", "Lista de roles"))
        self.btn_btn_agregar.setText(_translate("Control_Roles_Permisos", "GUARDAR"))
        self.etiquetasubtitulo_puestos.setText(_translate("Control_Roles_Permisos", "Puestos"))
        self.opcion_modificargrupopermisos.setText(_translate("Control_Roles_Permisos", "Modificar"))
        self.etiquetasubtitulo_grupopermisos.setText(_translate("Control_Roles_Permisos", "Grupo de permisos"))
        self.etiquetasubtitulo_transacciones.setText(_translate("Control_Roles_Permisos", "Transacciones"))
        self.etiquetasubtitulo_usuarios.setText(_translate("Control_Roles_Permisos", "Usuarios"))
        self.opcion_eliminartransacciones.setText(_translate("Control_Roles_Permisos", "Eliminar"))
        self.opcion_crearturnos.setText(_translate("Control_Roles_Permisos", "Crear"))
        self.opcion_creargrupopermisos.setText(_translate("Control_Roles_Permisos", "Crear"))
        self.opcion_creartrasacciones.setText(_translate("Control_Roles_Permisos", "Crear"))
        self.etiquetasubtitulo_cliente.setText(_translate("Control_Roles_Permisos", "Clientes"))
        self.opcion_crearempleado.setText(_translate("Control_Roles_Permisos", "Crear"))
        self.etiquetasubtitulo_empleado.setText(_translate("Control_Roles_Permisos", "Empleados"))
        self.opcion_eliminarcliente.setText(_translate("Control_Roles_Permisos", "Eliminar"))
        self.opcion_modificarsucursal.setText(_translate("Control_Roles_Permisos", "Modificar"))
        self.etiquetasubtitulo_venta.setText(_translate("Control_Roles_Permisos", "Ventas"))
        self.etiquetasubtitulo_compra.setText(_translate("Control_Roles_Permisos", "Compras"))
        self.opcion_eliminarcompra.setText(_translate("Control_Roles_Permisos", "Eliminar"))
        self.opcion_crearventa.setText(_translate("Control_Roles_Permisos", "Crear"))
        self.etiquetasubtitulo_departamentos.setText(_translate("Control_Roles_Permisos", "Departamentos"))
        self.opcion_modificarpuesto.setText(_translate("Control_Roles_Permisos", "Modificar"))
        self.opcion_eliminarpuesto.setText(_translate("Control_Roles_Permisos", "Eliminar"))
        self.etiquetasubtitulo_proveedor.setText(_translate("Control_Roles_Permisos", "Proveedores"))
        self.opcion_crearproveedor.setText(_translate("Control_Roles_Permisos", "Crear"))
        self.opcion_eliminarsucursal.setText(_translate("Control_Roles_Permisos", "Eliminar"))
        self.opcion_modificarcliente.setText(_translate("Control_Roles_Permisos", "Modificar"))
        self.etiquetasubtitulo_sucursal.setText(_translate("Control_Roles_Permisos", "Sucursales"))
        self.opcion_modificarproveedor.setText(_translate("Control_Roles_Permisos", "Modificar"))
        self.opcion_eliminarproveedor.setText(_translate("Control_Roles_Permisos", "Eliminar"))
        self.opcion_crearcliente.setText(_translate("Control_Roles_Permisos", "Crear"))
        self.opcion_crearsucursal.setText(_translate("Control_Roles_Permisos", "Crear"))
        self.opcion_eliminarventa.setText(_translate("Control_Roles_Permisos", "Eliminar"))
        self.opcion_crearproducto.setText(_translate("Control_Roles_Permisos", "Crear"))
        self.opcion_crearpuestos.setText(_translate("Control_Roles_Permisos", "Crear"))
        self.opcion_modificarempleado.setText(_translate("Control_Roles_Permisos", "Modificar"))
        self.opcion_eliminarempleado.setText(_translate("Control_Roles_Permisos", "Eliminar"))
        self.opcion_modificarcompra.setText(_translate("Control_Roles_Permisos", "Modificar"))
        self.opcion_crearcompra.setText(_translate("Control_Roles_Permisos", "Crear"))
        self.opcion_eliminarproducto.setText(_translate("Control_Roles_Permisos", "Eliminar"))
        self.etiquetasubtitulo_producto.setText(_translate("Control_Roles_Permisos", "Productos"))
        self.opcion_modificarventa.setText(_translate("Control_Roles_Permisos", "Modificar"))
        self.opcion_modificarproducto.setText(_translate("Control_Roles_Permisos", "Modificar"))
        self.opcion_creardepartamento.setText(_translate("Control_Roles_Permisos", "Crear"))
        self.opcion_eliminardepartamento.setText(_translate("Control_Roles_Permisos", "Eliminar"))
        self.opcion_modificardepartamento.setText(_translate("Control_Roles_Permisos", "Modificar"))
        self.opcion_eliminarturnos.setText(_translate("Control_Roles_Permisos", "Eliminar"))
        self.opcion_modificartransacciones.setText(_translate("Control_Roles_Permisos", "Modificar"))
        self.opcion_eliminarusuarios.setText(_translate("Control_Roles_Permisos", "Eliminar"))
        self.etiquetasubtitulo_turnos.setText(_translate("Control_Roles_Permisos", "Turnos"))
        self.opcion_eliminargrupopermisos.setText(_translate("Control_Roles_Permisos", "Eliminar"))
        self.opcion_modificarturnos.setText(_translate("Control_Roles_Permisos", "Modificar"))
        self.opcion_crearusuarios.setText(_translate("Control_Roles_Permisos", "Crear"))
        self.opcion_modificarusuarios.setText(_translate("Control_Roles_Permisos", "Modificar"))
        self.etiqueta_descripcionrol.setText(_translate("Control_Roles_Permisos", "Descripción:"))
        self.etiquetaTitulo_rol.setText(_translate("Control_Roles_Permisos", "Nuevo Rol"))
        self.etiqueta_nombrerol.setText(_translate("Control_Roles_Permisos", "Nombre:"))
        self.contenedor_funcionesroles.setTabText(self.contenedor_funcionesroles.indexOf(self.contenedor_funcioncrearroles), _translate("Control_Roles_Permisos", "Agregar roles"))
from ...Source import iconosSVG_rc
