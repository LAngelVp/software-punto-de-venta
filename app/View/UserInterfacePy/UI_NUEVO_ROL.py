# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UI_NUEVO_ROL.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QLabel, QLineEdit, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QWidget)

class Ui_Control_nuevo_rol(object):
    def setupUi(self, Control_nuevo_rol):
        if not Control_nuevo_rol.objectName():
            Control_nuevo_rol.setObjectName(u"Control_nuevo_rol")
        Control_nuevo_rol.resize(400, 400)
        Control_nuevo_rol.setMinimumSize(QSize(400, 400))
        Control_nuevo_rol.setMaximumSize(QSize(400, 400))
        Control_nuevo_rol.setStyleSheet(u"*{color: #1d1c1c;}\n"
"#Control_nuevo_rol{\n"
"background: #fffefb;\n"
"}\n"
"[objectName*=\"contenedor\"]{\n"
"background: #fffefb;\n"
"border:none;\n"
"}\n"
"[objectName*=\"etiquetaTitulo_\"]{\n"
"font-size:18px;\n"
"font-family:Arial;\n"
"font-weight:bold;\n"
"color: #1d1c1c;\n"
"}\n"
"[objectName*=\"etiquetasubtitulo_\"]{\n"
"font-size:16px;\n"
"font-family:Arial;\n"
"font-weight:bold;\n"
"color: #1d1c1c;\n"
"}\n"
"[objectName*=\"etiqueta_\"]{\n"
"font-size:14px;\n"
"font-family:Arial;\n"
"font-weight:bold;\n"
"color: #1d1c1c;\n"
"}\n"
"[objectName*=\"opcion_\"]{\n"
"font-size:14px;\n"
"font-family:Arial;\n"
"color: #1d1c1c;\n"
"}\n"
"#contenedor_permisos{\n"
"background: #fffefb;\n"
"}\n"
"#contenedor_permisosscroll{\n"
"background: #fffefb;\n"
"color: #1d1c1c;\n"
"}\n"
"\n"
"[objectName*=\"txt_\"]{\n"
"font-size:14px;\n"
"font-family:Arial;\n"
"font-weight:bold;\n"
"color: #1d1c1c;\n"
"background: #F5F5F5;\n"
"border: none;\n"
"border-radius: 5px;\n"
"border-bottom: 1px solid #1d1c1c;\n"
"}\n"
"[objectNa"
                        "me*=\"txt_\"]:focus{\n"
"border-bottom: 2px solid #023375;\n"
"}\n"
"[objectName*=\"btn_btn_\"]{\n"
"font-size:14px;\n"
"font-family:Arial;\n"
"font-weight:bold;\n"
"color: #fffefb;\n"
"background: #023375;\n"
"border:none;\n"
"border-radius: 5px;\n"
"padding-left: 10px;\n"
"padding-right: 10px;\n"
"height: 30px;\n"
"}\n"
"[objectName*=\"btn_btn_\"]:hover{\n"
"background: #2196F3;\n"
"}\n"
"")
        self.gridLayout = QGridLayout(Control_nuevo_rol)
        self.gridLayout.setObjectName(u"gridLayout")
        self.contenedor = QFrame(Control_nuevo_rol)
        self.contenedor.setObjectName(u"contenedor")
        self.contenedor.setFrameShape(QFrame.Shape.StyledPanel)
        self.contenedor.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_3 = QGridLayout(self.contenedor)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.etiquetaTitulo_rol = QLabel(self.contenedor)
        self.etiquetaTitulo_rol.setObjectName(u"etiquetaTitulo_rol")

        self.gridLayout_3.addWidget(self.etiquetaTitulo_rol, 0, 0, 1, 1)

        self.etiqueta_nombrerol = QLabel(self.contenedor)
        self.etiqueta_nombrerol.setObjectName(u"etiqueta_nombrerol")

        self.gridLayout_3.addWidget(self.etiqueta_nombrerol, 2, 0, 1, 1)

        self.contenedor_permisos = QScrollArea(self.contenedor)
        self.contenedor_permisos.setObjectName(u"contenedor_permisos")
        self.contenedor_permisos.setWidgetResizable(True)
        self.contenedor_permisosscroll = QWidget()
        self.contenedor_permisosscroll.setObjectName(u"contenedor_permisosscroll")
        self.contenedor_permisosscroll.setGeometry(QRect(0, 0, 337, 313))
        self.gridLayout_2 = QGridLayout(self.contenedor_permisosscroll)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.etiquetasubtitulo_proveedor = QLabel(self.contenedor_permisosscroll)
        self.etiquetasubtitulo_proveedor.setObjectName(u"etiquetasubtitulo_proveedor")

        self.gridLayout_2.addWidget(self.etiquetasubtitulo_proveedor, 4, 2, 1, 1)

        self.opcion_eliminarsucursal = QCheckBox(self.contenedor_permisosscroll)
        self.opcion_eliminarsucursal.setObjectName(u"opcion_eliminarsucursal")

        self.gridLayout_2.addWidget(self.opcion_eliminarsucursal, 10, 0, 1, 1)

        self.opcion_crearproveedor = QCheckBox(self.contenedor_permisosscroll)
        self.opcion_crearproveedor.setObjectName(u"opcion_crearproveedor")

        self.gridLayout_2.addWidget(self.opcion_crearproveedor, 5, 2, 1, 1)

        self.etiquetasubtitulo_cliente = QLabel(self.contenedor_permisosscroll)
        self.etiquetasubtitulo_cliente.setObjectName(u"etiquetasubtitulo_cliente")

        self.gridLayout_2.addWidget(self.etiquetasubtitulo_cliente, 4, 4, 1, 1)

        self.opcion_eliminarproveedor = QCheckBox(self.contenedor_permisosscroll)
        self.opcion_eliminarproveedor.setObjectName(u"opcion_eliminarproveedor")

        self.gridLayout_2.addWidget(self.opcion_eliminarproveedor, 6, 2, 1, 1)

        self.opcion_modificarproveedor = QCheckBox(self.contenedor_permisosscroll)
        self.opcion_modificarproveedor.setObjectName(u"opcion_modificarproveedor")

        self.gridLayout_2.addWidget(self.opcion_modificarproveedor, 7, 2, 1, 1)

        self.etiquetasubtitulo_sucursal = QLabel(self.contenedor_permisosscroll)
        self.etiquetasubtitulo_sucursal.setObjectName(u"etiquetasubtitulo_sucursal")

        self.gridLayout_2.addWidget(self.etiquetasubtitulo_sucursal, 8, 0, 1, 1)

        self.opcion_crearcliente = QCheckBox(self.contenedor_permisosscroll)
        self.opcion_crearcliente.setObjectName(u"opcion_crearcliente")

        self.gridLayout_2.addWidget(self.opcion_crearcliente, 5, 4, 1, 1)

        self.opcion_crearsucursal = QCheckBox(self.contenedor_permisosscroll)
        self.opcion_crearsucursal.setObjectName(u"opcion_crearsucursal")

        self.gridLayout_2.addWidget(self.opcion_crearsucursal, 9, 0, 1, 1)

        self.opcion_crearproducto = QCheckBox(self.contenedor_permisosscroll)
        self.opcion_crearproducto.setObjectName(u"opcion_crearproducto")

        self.gridLayout_2.addWidget(self.opcion_crearproducto, 1, 4, 1, 1)

        self.opcion_eliminarventa = QCheckBox(self.contenedor_permisosscroll)
        self.opcion_eliminarventa.setObjectName(u"opcion_eliminarventa")

        self.gridLayout_2.addWidget(self.opcion_eliminarventa, 2, 0, 1, 1)

        self.opcion_eliminarcompra = QCheckBox(self.contenedor_permisosscroll)
        self.opcion_eliminarcompra.setObjectName(u"opcion_eliminarcompra")

        self.gridLayout_2.addWidget(self.opcion_eliminarcompra, 2, 2, 1, 1)

        self.etiquetasubtitulo_compra = QLabel(self.contenedor_permisosscroll)
        self.etiquetasubtitulo_compra.setObjectName(u"etiquetasubtitulo_compra")

        self.gridLayout_2.addWidget(self.etiquetasubtitulo_compra, 0, 2, 1, 1)

        self.etiquetasubtitulo_venta = QLabel(self.contenedor_permisosscroll)
        self.etiquetasubtitulo_venta.setObjectName(u"etiquetasubtitulo_venta")

        self.gridLayout_2.addWidget(self.etiquetasubtitulo_venta, 0, 0, 1, 1)

        self.opcion_crearventa = QCheckBox(self.contenedor_permisosscroll)
        self.opcion_crearventa.setObjectName(u"opcion_crearventa")

        self.gridLayout_2.addWidget(self.opcion_crearventa, 1, 0, 1, 1)

        self.opcion_crearcompra = QCheckBox(self.contenedor_permisosscroll)
        self.opcion_crearcompra.setObjectName(u"opcion_crearcompra")

        self.gridLayout_2.addWidget(self.opcion_crearcompra, 1, 2, 1, 1)

        self.etiquetasubtitulo_producto = QLabel(self.contenedor_permisosscroll)
        self.etiquetasubtitulo_producto.setObjectName(u"etiquetasubtitulo_producto")

        self.gridLayout_2.addWidget(self.etiquetasubtitulo_producto, 0, 4, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 12, 2, 1, 1)

        self.opcion_eliminarproducto = QCheckBox(self.contenedor_permisosscroll)
        self.opcion_eliminarproducto.setObjectName(u"opcion_eliminarproducto")

        self.gridLayout_2.addWidget(self.opcion_eliminarproducto, 2, 4, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_3, 12, 4, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 12, 0, 1, 1)

        self.line_3 = QFrame(self.contenedor_permisosscroll)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_2.addWidget(self.line_3, 0, 3, 14, 1)

        self.line_2 = QFrame(self.contenedor_permisosscroll)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_2.addWidget(self.line_2, 0, 1, 14, 1)

        self.opcion_modificarventa = QCheckBox(self.contenedor_permisosscroll)
        self.opcion_modificarventa.setObjectName(u"opcion_modificarventa")

        self.gridLayout_2.addWidget(self.opcion_modificarventa, 3, 0, 1, 1)

        self.opcion_modificarcompra = QCheckBox(self.contenedor_permisosscroll)
        self.opcion_modificarcompra.setObjectName(u"opcion_modificarcompra")

        self.gridLayout_2.addWidget(self.opcion_modificarcompra, 3, 2, 1, 1)

        self.opcion_modificarproducto = QCheckBox(self.contenedor_permisosscroll)
        self.opcion_modificarproducto.setObjectName(u"opcion_modificarproducto")

        self.gridLayout_2.addWidget(self.opcion_modificarproducto, 3, 4, 1, 1)

        self.opcion_modificarempleado = QCheckBox(self.contenedor_permisosscroll)
        self.opcion_modificarempleado.setObjectName(u"opcion_modificarempleado")

        self.gridLayout_2.addWidget(self.opcion_modificarempleado, 7, 0, 1, 1)

        self.opcion_modificarcliente = QCheckBox(self.contenedor_permisosscroll)
        self.opcion_modificarcliente.setObjectName(u"opcion_modificarcliente")

        self.gridLayout_2.addWidget(self.opcion_modificarcliente, 7, 4, 1, 1)

        self.opcion_eliminarempleado = QCheckBox(self.contenedor_permisosscroll)
        self.opcion_eliminarempleado.setObjectName(u"opcion_eliminarempleado")

        self.gridLayout_2.addWidget(self.opcion_eliminarempleado, 6, 0, 1, 1)

        self.etiquetasubtitulo_empleado = QLabel(self.contenedor_permisosscroll)
        self.etiquetasubtitulo_empleado.setObjectName(u"etiquetasubtitulo_empleado")

        self.gridLayout_2.addWidget(self.etiquetasubtitulo_empleado, 4, 0, 1, 1)

        self.opcion_crearempleado = QCheckBox(self.contenedor_permisosscroll)
        self.opcion_crearempleado.setObjectName(u"opcion_crearempleado")

        self.gridLayout_2.addWidget(self.opcion_crearempleado, 5, 0, 1, 1)

        self.opcion_eliminarcliente = QCheckBox(self.contenedor_permisosscroll)
        self.opcion_eliminarcliente.setObjectName(u"opcion_eliminarcliente")

        self.gridLayout_2.addWidget(self.opcion_eliminarcliente, 6, 4, 1, 1)

        self.opcion_modificarsucursal = QCheckBox(self.contenedor_permisosscroll)
        self.opcion_modificarsucursal.setObjectName(u"opcion_modificarsucursal")

        self.gridLayout_2.addWidget(self.opcion_modificarsucursal, 11, 0, 1, 1)

        self.contenedor_permisos.setWidget(self.contenedor_permisosscroll)

        self.gridLayout_3.addWidget(self.contenedor_permisos, 4, 0, 1, 2)

        self.btn_btn_agregar = QPushButton(self.contenedor)
        self.btn_btn_agregar.setObjectName(u"btn_btn_agregar")
        self.btn_btn_agregar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout_3.addWidget(self.btn_btn_agregar, 5, 1, 1, 1, Qt.AlignmentFlag.AlignRight)

        self.txt_nombrerol = QLineEdit(self.contenedor)
        self.txt_nombrerol.setObjectName(u"txt_nombrerol")

        self.gridLayout_3.addWidget(self.txt_nombrerol, 3, 0, 1, 2)

        self.line = QFrame(self.contenedor)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_3.addWidget(self.line, 1, 0, 1, 2)


        self.gridLayout.addWidget(self.contenedor, 0, 0, 1, 1)


        self.retranslateUi(Control_nuevo_rol)

        QMetaObject.connectSlotsByName(Control_nuevo_rol)
    # setupUi

    def retranslateUi(self, Control_nuevo_rol):
        Control_nuevo_rol.setWindowTitle(QCoreApplication.translate("Control_nuevo_rol", u"Form", None))
        self.etiquetaTitulo_rol.setText(QCoreApplication.translate("Control_nuevo_rol", u"Nuevo Rol", None))
        self.etiqueta_nombrerol.setText(QCoreApplication.translate("Control_nuevo_rol", u"Nombre:", None))
        self.etiquetasubtitulo_proveedor.setText(QCoreApplication.translate("Control_nuevo_rol", u"Proveedores", None))
        self.opcion_eliminarsucursal.setText(QCoreApplication.translate("Control_nuevo_rol", u"Eliminar", None))
        self.opcion_crearproveedor.setText(QCoreApplication.translate("Control_nuevo_rol", u"Crear", None))
        self.etiquetasubtitulo_cliente.setText(QCoreApplication.translate("Control_nuevo_rol", u"Clientes", None))
        self.opcion_eliminarproveedor.setText(QCoreApplication.translate("Control_nuevo_rol", u"Eliminar", None))
        self.opcion_modificarproveedor.setText(QCoreApplication.translate("Control_nuevo_rol", u"Modificar", None))
        self.etiquetasubtitulo_sucursal.setText(QCoreApplication.translate("Control_nuevo_rol", u"Sucursales", None))
        self.opcion_crearcliente.setText(QCoreApplication.translate("Control_nuevo_rol", u"Crear", None))
        self.opcion_crearsucursal.setText(QCoreApplication.translate("Control_nuevo_rol", u"Crear", None))
        self.opcion_crearproducto.setText(QCoreApplication.translate("Control_nuevo_rol", u"Crear", None))
        self.opcion_eliminarventa.setText(QCoreApplication.translate("Control_nuevo_rol", u"Eliminar", None))
        self.opcion_eliminarcompra.setText(QCoreApplication.translate("Control_nuevo_rol", u"Eliminar", None))
        self.etiquetasubtitulo_compra.setText(QCoreApplication.translate("Control_nuevo_rol", u"Compras", None))
        self.etiquetasubtitulo_venta.setText(QCoreApplication.translate("Control_nuevo_rol", u"Ventas", None))
        self.opcion_crearventa.setText(QCoreApplication.translate("Control_nuevo_rol", u"Crear", None))
        self.opcion_crearcompra.setText(QCoreApplication.translate("Control_nuevo_rol", u"Crear", None))
        self.etiquetasubtitulo_producto.setText(QCoreApplication.translate("Control_nuevo_rol", u"Productos", None))
        self.opcion_eliminarproducto.setText(QCoreApplication.translate("Control_nuevo_rol", u"Eliminar", None))
        self.opcion_modificarventa.setText(QCoreApplication.translate("Control_nuevo_rol", u"Modificar", None))
        self.opcion_modificarcompra.setText(QCoreApplication.translate("Control_nuevo_rol", u"Modificar", None))
        self.opcion_modificarproducto.setText(QCoreApplication.translate("Control_nuevo_rol", u"Modificar", None))
        self.opcion_modificarempleado.setText(QCoreApplication.translate("Control_nuevo_rol", u"Modificar", None))
        self.opcion_modificarcliente.setText(QCoreApplication.translate("Control_nuevo_rol", u"Modificar", None))
        self.opcion_eliminarempleado.setText(QCoreApplication.translate("Control_nuevo_rol", u"Eliminar", None))
        self.etiquetasubtitulo_empleado.setText(QCoreApplication.translate("Control_nuevo_rol", u"Empleados", None))
        self.opcion_crearempleado.setText(QCoreApplication.translate("Control_nuevo_rol", u"Crear", None))
        self.opcion_eliminarcliente.setText(QCoreApplication.translate("Control_nuevo_rol", u"Eliminar", None))
        self.opcion_modificarsucursal.setText(QCoreApplication.translate("Control_nuevo_rol", u"Modificar", None))
        self.btn_btn_agregar.setText(QCoreApplication.translate("Control_nuevo_rol", u"Guardar", None))
    # retranslateUi

