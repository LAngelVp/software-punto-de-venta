# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CAMBIO_PRECIO_PRODUCTO_PROVEEDOR.ui'
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QDoubleSpinBox, QFrame,
    QGridLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QWidget)

class Ui_PreciosProductosProveedor(object):
    def setupUi(self, PreciosProductosProveedor):
        if not PreciosProductosProveedor.objectName():
            PreciosProductosProveedor.setObjectName(u"PreciosProductosProveedor")
        PreciosProductosProveedor.resize(313, 277)
        PreciosProductosProveedor.setStyleSheet(u"*{color: #1d1c1c;}\n"
"#PreciosProductosProveedor{\n"
"background: #fffefb;\n"
"}\n"
"[objectName*=\"contenedor\"]{\n"
"background: #fffefb;\n"
"border: none;\n"
"}\n"
"[objectName*=\"etiqueta\"]{\n"
"font-size: 14px;\n"
"font-weight: bold;\n"
"font-family: \"Arial\";\n"
"color: #1d1c1c;\n"
"}\n"
"#etiqueta_nombre_del_proveedor{\n"
"color: #585555;\n"
"}\n"
"[objectName*=\"txt\"]{\n"
"background: #f5f4f1;\n"
"border-radius: 4px;\n"
"font-size: 12px;\n"
"font-family:\"Arial\";\n"
"border-bottom: 1px solid #1d1c1c;\n"
"}\n"
"[objectName*=\"decimal\"]{\n"
"background: #F5F5F5;\n"
"border-bottom: 1px solid #1d1c1c;\n"
"font-size: 12px;\n"
"font-family: \"Arial\";\n"
"font-weight:bold;\n"
"border-radius:2px;\n"
"}\n"
"[objectName*=\"btn_precio_producto\"]{\n"
"background:#00619a;\n"
"font-size: 14px;\n"
"font-family:\"Arial\";\n"
"font-weight:bold;\n"
"color:#fffefb;\n"
"border-radius: 4px;\n"
"padding: 2px 4px;\n"
"}\n"
"[objectName*=\"aceptar\"]:hover{\n"
"background: #68a67d;\n"
"}\n"
"[objectName*=\"aceptar\"]:"
                        "pressed{\n"
"background: #578B69;\n"
"}\n"
"[objectName*=\"cancelar\"]:hover{\n"
"background: #ee1d52;\n"
"}\n"
"[objectName*=\"cancelar\"]:pressed{\n"
"background: #B13636;\n"
"}")
        self.gridLayout = QGridLayout(PreciosProductosProveedor)
        self.gridLayout.setObjectName(u"gridLayout")
        self.contenedor_principal = QFrame(PreciosProductosProveedor)
        self.contenedor_principal.setObjectName(u"contenedor_principal")
        self.contenedor_principal.setFrameShape(QFrame.Shape.StyledPanel)
        self.contenedor_principal.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_4 = QGridLayout(self.contenedor_principal)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.contenedor_datos_principales = QGridLayout()
        self.contenedor_datos_principales.setObjectName(u"contenedor_datos_principales")
        self.etiqueta_nombre_proveedor_titulo = QLabel(self.contenedor_principal)
        self.etiqueta_nombre_proveedor_titulo.setObjectName(u"etiqueta_nombre_proveedor_titulo")

        self.contenedor_datos_principales.addWidget(self.etiqueta_nombre_proveedor_titulo, 0, 0, 1, 1)

        self.etiqueta_nombre_del_proveedor = QLabel(self.contenedor_principal)
        self.etiqueta_nombre_del_proveedor.setObjectName(u"etiqueta_nombre_del_proveedor")

        self.contenedor_datos_principales.addWidget(self.etiqueta_nombre_del_proveedor, 1, 0, 1, 1)

        self.etiqueta_cod_producto = QLabel(self.contenedor_principal)
        self.etiqueta_cod_producto.setObjectName(u"etiqueta_cod_producto")
        self.etiqueta_cod_producto.setFrameShape(QFrame.Shape.NoFrame)
        self.etiqueta_cod_producto.setFrameShadow(QFrame.Shadow.Plain)
        self.etiqueta_cod_producto.setScaledContents(False)
        self.etiqueta_cod_producto.setWordWrap(False)

        self.contenedor_datos_principales.addWidget(self.etiqueta_cod_producto, 2, 0, 1, 1)

        self.txt_codigoupc_producto = QLineEdit(self.contenedor_principal)
        self.txt_codigoupc_producto.setObjectName(u"txt_codigoupc_producto")
        self.txt_codigoupc_producto.setEnabled(False)

        self.contenedor_datos_principales.addWidget(self.txt_codigoupc_producto, 3, 0, 1, 1)

        self.etiqueta_nombre_producto = QLabel(self.contenedor_principal)
        self.etiqueta_nombre_producto.setObjectName(u"etiqueta_nombre_producto")

        self.contenedor_datos_principales.addWidget(self.etiqueta_nombre_producto, 4, 0, 1, 1)

        self.txt_nombre_producto = QLineEdit(self.contenedor_principal)
        self.txt_nombre_producto.setObjectName(u"txt_nombre_producto")
        self.txt_nombre_producto.setEnabled(False)

        self.contenedor_datos_principales.addWidget(self.txt_nombre_producto, 5, 0, 1, 1)


        self.gridLayout_4.addLayout(self.contenedor_datos_principales, 0, 0, 1, 1)

        self.btn_precio_producto_aceptar = QPushButton(self.contenedor_principal)
        self.btn_precio_producto_aceptar.setObjectName(u"btn_precio_producto_aceptar")
        self.btn_precio_producto_aceptar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout_4.addWidget(self.btn_precio_producto_aceptar, 3, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 46, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer, 2, 0, 1, 1)

        self.contenedor_datos_precios = QGridLayout()
        self.contenedor_datos_precios.setObjectName(u"contenedor_datos_precios")
        self.etiqueta_costo_proveedor = QLabel(self.contenedor_principal)
        self.etiqueta_costo_proveedor.setObjectName(u"etiqueta_costo_proveedor")

        self.contenedor_datos_precios.addWidget(self.etiqueta_costo_proveedor, 0, 0, 1, 1)

        self.decimal_costo_venta_proveedor = QDoubleSpinBox(self.contenedor_principal)
        self.decimal_costo_venta_proveedor.setObjectName(u"decimal_costo_venta_proveedor")
        self.decimal_costo_venta_proveedor.setWrapping(False)
        self.decimal_costo_venta_proveedor.setFrame(True)
        self.decimal_costo_venta_proveedor.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.decimal_costo_venta_proveedor.setReadOnly(False)
        self.decimal_costo_venta_proveedor.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.decimal_costo_venta_proveedor.setMaximum(999999999999999983222784.000000000000000)

        self.contenedor_datos_precios.addWidget(self.decimal_costo_venta_proveedor, 0, 1, 1, 1)


        self.gridLayout_4.addLayout(self.contenedor_datos_precios, 1, 0, 1, 1)

        self.btn_precio_producto_cancelar = QPushButton(self.contenedor_principal)
        self.btn_precio_producto_cancelar.setObjectName(u"btn_precio_producto_cancelar")
        self.btn_precio_producto_cancelar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout_4.addWidget(self.btn_precio_producto_cancelar, 4, 0, 1, 1)


        self.gridLayout.addWidget(self.contenedor_principal, 0, 0, 1, 1)


        self.retranslateUi(PreciosProductosProveedor)

        QMetaObject.connectSlotsByName(PreciosProductosProveedor)
    # setupUi

    def retranslateUi(self, PreciosProductosProveedor):
        PreciosProductosProveedor.setWindowTitle(QCoreApplication.translate("PreciosProductosProveedor", u"Form", None))
        self.etiqueta_nombre_proveedor_titulo.setText(QCoreApplication.translate("PreciosProductosProveedor", u"Nombre del Proveedor", None))
        self.etiqueta_nombre_del_proveedor.setText(QCoreApplication.translate("PreciosProductosProveedor", u"Nombre", None))
        self.etiqueta_cod_producto.setText(QCoreApplication.translate("PreciosProductosProveedor", u"Cod. del Producto.", None))
        self.etiqueta_nombre_producto.setText(QCoreApplication.translate("PreciosProductosProveedor", u"Nombre del Producto", None))
        self.btn_precio_producto_aceptar.setText(QCoreApplication.translate("PreciosProductosProveedor", u"Guardar", None))
        self.etiqueta_costo_proveedor.setText(QCoreApplication.translate("PreciosProductosProveedor", u"Costo proveedor", None))
        self.btn_precio_producto_cancelar.setText(QCoreApplication.translate("PreciosProductosProveedor", u"Cancelar", None))
    # retranslateUi

