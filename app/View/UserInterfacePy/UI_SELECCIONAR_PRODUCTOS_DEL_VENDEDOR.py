# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UI_SELECCIONAR_PRODUCTOS_DEL_VENDEDOR.ui'
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
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QTableView,
    QWidget)
from ...Source import ibootstrap_rc
from ...Source import iconsdvg_rc

class Ui_Seleccion_Productos_Proveedor(object):
    def setupUi(self, Seleccion_Productos_Proveedor):
        if not Seleccion_Productos_Proveedor.objectName():
            Seleccion_Productos_Proveedor.setObjectName(u"Seleccion_Productos_Proveedor")
        Seleccion_Productos_Proveedor.resize(877, 507)
        Seleccion_Productos_Proveedor.setStyleSheet(u"*{ color: #1d1c1c;	}\n"
"[objectName*=\"contenedor\"]{\n"
"background: #fffefb;\n"
"border: none;\n"
"}\n"
"#contenedor_encabezado{\n"
"background: #023375;\n"
"max-height: 25px;\n"
"}\n"
"#etiqueta_encabezado_productosProveedor{\n"
"color: #fffefb;\n"
"font-size: 18px;\n"
"font-weight:bold;\n"
"font-family:\"Arial\";\n"
"}\n"
"[objectName*=\"etiqueta_\"]{\n"
"font-size:14px;\n"
"font-family: Arial;\n"
"font-weight:bold;\n"
"color: #1d1c1c;\n"
"}\n"
"[objectName*=\"txt_\"]{\n"
"background: #F5F5F5;\n"
"border:none;\n"
"border-radius: 5px;\n"
"color: #1d1c1c;\n"
"font-size: 14px;\n"
"border-bottom: 1px solid #787878;\n"
"}\n"
"[objectName*=\"txt_\"]:focus{\n"
"border-bottom: 2px solid #023375;\n"
"}\n"
"[objectName*=\"btn_\"]{\n"
"background: #00619a;\n"
"font-size: 14px;\n"
"font-family: Arial;\n"
"font-weight: bold;\n"
"min-height: 25px;\n"
"border: none;\n"
"border-radius: 5px;\n"
"color: #fffefb;\n"
"padding: 3px 5px;\n"
"}\n"
"[objectName*=\"btn_aceptar\"]:hover{\n"
"background: #68a67d;\n"
"}\n"
"[objectN"
                        "ame*=\"btn_aceptar\"]:pressed{\n"
"background: #578B69;\n"
"}\n"
"#btn_cerrar{\n"
"background: #fffefb;\n"
"min-height:15px;\n"
"min-width:15px;\n"
"}\n"
"#btn_cerrar:pressed{\n"
"background: rgb(222, 221, 218);\n"
"}\n"
"\n"
"\n"
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
"/* Encabezad"
                        "o vertical */\n"
"[objectName*=\"tabla_\"] QHeaderView::vertical {\n"
"    background-color: #023375;\n"
"    color: white;\n"
"}")
        self.gridLayout = QGridLayout(Seleccion_Productos_Proveedor)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.contenedor_encabezado = QFrame(Seleccion_Productos_Proveedor)
        self.contenedor_encabezado.setObjectName(u"contenedor_encabezado")
        self.contenedor_encabezado.setFrameShape(QFrame.Shape.StyledPanel)
        self.contenedor_encabezado.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.contenedor_encabezado)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 2, -1, 2)
        self.etiqueta_encabezado_productosProveedor = QLabel(self.contenedor_encabezado)
        self.etiqueta_encabezado_productosProveedor.setObjectName(u"etiqueta_encabezado_productosProveedor")

        self.horizontalLayout.addWidget(self.etiqueta_encabezado_productosProveedor)

        self.horizontalSpacer = QSpacerItem(743, 4, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_cerrar = QPushButton(self.contenedor_encabezado)
        self.btn_cerrar.setObjectName(u"btn_cerrar")
        self.btn_cerrar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/Icons/Bootstrap/x-lg.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_cerrar.setIcon(icon)

        self.horizontalLayout.addWidget(self.btn_cerrar)


        self.gridLayout.addWidget(self.contenedor_encabezado, 0, 0, 1, 1)

        self.contenedor_cuerpo = QFrame(Seleccion_Productos_Proveedor)
        self.contenedor_cuerpo.setObjectName(u"contenedor_cuerpo")
        self.contenedor_cuerpo.setFrameShape(QFrame.Shape.StyledPanel)
        self.contenedor_cuerpo.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_4 = QGridLayout(self.contenedor_cuerpo)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.contenedor_opciones_superiores = QFrame(self.contenedor_cuerpo)
        self.contenedor_opciones_superiores.setObjectName(u"contenedor_opciones_superiores")
        self.contenedor_opciones_superiores.setFrameShape(QFrame.Shape.StyledPanel)
        self.contenedor_opciones_superiores.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.contenedor_opciones_superiores)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.etiqueta_nombredelproveedor = QLabel(self.contenedor_opciones_superiores)
        self.etiqueta_nombredelproveedor.setObjectName(u"etiqueta_nombredelproveedor")

        self.gridLayout_2.addWidget(self.etiqueta_nombredelproveedor, 0, 0, 1, 1)

        self.btn_aceptar = QPushButton(self.contenedor_opciones_superiores)
        self.btn_aceptar.setObjectName(u"btn_aceptar")
        self.btn_aceptar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout_2.addWidget(self.btn_aceptar, 0, 1, 1, 1, Qt.AlignmentFlag.AlignRight)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.txt_nombredelproducto = QLineEdit(self.contenedor_opciones_superiores)
        self.txt_nombredelproducto.setObjectName(u"txt_nombredelproducto")
        self.txt_nombredelproducto.setClearButtonEnabled(True)

        self.horizontalLayout_2.addWidget(self.txt_nombredelproducto)

        self.txt_codigodelproducto = QLineEdit(self.contenedor_opciones_superiores)
        self.txt_codigodelproducto.setObjectName(u"txt_codigodelproducto")
        self.txt_codigodelproducto.setClearButtonEnabled(True)

        self.horizontalLayout_2.addWidget(self.txt_codigodelproducto)


        self.gridLayout_2.addLayout(self.horizontalLayout_2, 1, 0, 1, 2)


        self.gridLayout_4.addWidget(self.contenedor_opciones_superiores, 0, 0, 1, 1)

        self.contenedor_area = QScrollArea(self.contenedor_cuerpo)
        self.contenedor_area.setObjectName(u"contenedor_area")
        self.contenedor_area.setWidgetResizable(True)
        self.contenedor_scrollAreaWidgetContents = QWidget()
        self.contenedor_scrollAreaWidgetContents.setObjectName(u"contenedor_scrollAreaWidgetContents")
        self.contenedor_scrollAreaWidgetContents.setGeometry(QRect(0, 0, 853, 351))
        self.gridLayout_3 = QGridLayout(self.contenedor_scrollAreaWidgetContents)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.etiqueta_tablaproductosproveedor = QLabel(self.contenedor_scrollAreaWidgetContents)
        self.etiqueta_tablaproductosproveedor.setObjectName(u"etiqueta_tablaproductosproveedor")

        self.gridLayout_3.addWidget(self.etiqueta_tablaproductosproveedor, 0, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(619, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_2, 0, 1, 1, 1)

        self.btn_RefrescarTabla = QPushButton(self.contenedor_scrollAreaWidgetContents)
        self.btn_RefrescarTabla.setObjectName(u"btn_RefrescarTabla")
        self.btn_RefrescarTabla.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/Icons/IconosSVG/base_datos_refresh.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_RefrescarTabla.setIcon(icon1)

        self.gridLayout_3.addWidget(self.btn_RefrescarTabla, 0, 2, 1, 1)

        self.tabla_productosProveedor = QTableView(self.contenedor_scrollAreaWidgetContents)
        self.tabla_productosProveedor.setObjectName(u"tabla_productosProveedor")

        self.gridLayout_3.addWidget(self.tabla_productosProveedor, 1, 0, 1, 3)

        self.etiqueta_tablaproductosparaorden = QLabel(self.contenedor_scrollAreaWidgetContents)
        self.etiqueta_tablaproductosparaorden.setObjectName(u"etiqueta_tablaproductosparaorden")

        self.gridLayout_3.addWidget(self.etiqueta_tablaproductosparaorden, 4, 0, 1, 3)

        self.tabla_productosParaOrden = QTableView(self.contenedor_scrollAreaWidgetContents)
        self.tabla_productosParaOrden.setObjectName(u"tabla_productosParaOrden")

        self.gridLayout_3.addWidget(self.tabla_productosParaOrden, 5, 0, 1, 3)

        self.line_2 = QFrame(self.contenedor_scrollAreaWidgetContents)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_3.addWidget(self.line_2, 3, 0, 1, 3)

        self.line = QFrame(self.contenedor_scrollAreaWidgetContents)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_3.addWidget(self.line, 2, 0, 1, 3)

        self.contenedor_area.setWidget(self.contenedor_scrollAreaWidgetContents)

        self.gridLayout_4.addWidget(self.contenedor_area, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.contenedor_cuerpo, 1, 0, 1, 1)


        self.retranslateUi(Seleccion_Productos_Proveedor)

        QMetaObject.connectSlotsByName(Seleccion_Productos_Proveedor)
    # setupUi

    def retranslateUi(self, Seleccion_Productos_Proveedor):
        Seleccion_Productos_Proveedor.setWindowTitle(QCoreApplication.translate("Seleccion_Productos_Proveedor", u"Form", None))
        self.etiqueta_encabezado_productosProveedor.setText(QCoreApplication.translate("Seleccion_Productos_Proveedor", u"Productos", None))
        self.btn_cerrar.setText("")
        self.etiqueta_nombredelproveedor.setText(QCoreApplication.translate("Seleccion_Productos_Proveedor", u"Nombre del proveedor: ", None))
#if QT_CONFIG(tooltip)
        self.btn_aceptar.setToolTip(QCoreApplication.translate("Seleccion_Productos_Proveedor", u"Terminar la selecci\u00f3n", None))
#endif // QT_CONFIG(tooltip)
        self.btn_aceptar.setText(QCoreApplication.translate("Seleccion_Productos_Proveedor", u"Aceptar", None))
        self.txt_nombredelproducto.setPlaceholderText(QCoreApplication.translate("Seleccion_Productos_Proveedor", u"Escribe el nombre del producto", None))
        self.txt_codigodelproducto.setPlaceholderText(QCoreApplication.translate("Seleccion_Productos_Proveedor", u"escribe el codigo del producto", None))
        self.etiqueta_tablaproductosproveedor.setText(QCoreApplication.translate("Seleccion_Productos_Proveedor", u"Productos del proveedor", None))
#if QT_CONFIG(tooltip)
        self.btn_RefrescarTabla.setToolTip(QCoreApplication.translate("Seleccion_Productos_Proveedor", u"Refrescar tabla productos proveedor", None))
#endif // QT_CONFIG(tooltip)
        self.btn_RefrescarTabla.setText("")
        self.etiqueta_tablaproductosparaorden.setText(QCoreApplication.translate("Seleccion_Productos_Proveedor", u"Productos para orden de compra", None))
    # retranslateUi

