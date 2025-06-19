# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UI_SISTEMA_PRINCIPAL.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QToolButton,
    QVBoxLayout, QWidget)
from ...Source import iconsdvg_rc
from ...Source import ibootstrap_rc

class Ui_Principal_sistema(object):
    def setupUi(self, Principal_sistema):
        if not Principal_sistema.objectName():
            Principal_sistema.setObjectName(u"Principal_sistema")
        Principal_sistema.resize(1009, 974)
        Principal_sistema.setStyleSheet(u"#Principal_sistema{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"[objectName*=\"w_\"]{\n"
"background: #fffefb;\n"
"}\n"
"#label_logoempresa{\n"
"image: url(:/Icons/IconosSVG/logo_dev_rous_blanco.png);\n"
"min-width:80px;\n"
"margin-top: 2px;\n"
"}\n"
"#w_cuerpo_contenido{\n"
"background: #fffefb;\n"
"}\n"
"[objectName^=\"btc\"]{\n"
"background-color: rgb(255, 255, 255);\n"
"	border: none;\n"
"	border-radius: 9px;\n"
"	min-width:35px;\n"
"	min-height:25px;\n"
"}\n"
"[objectName^=\"btc\"]:hover{\n"
"	background-color: rgb(214, 214, 214);\n"
"}\n"
"#w_encabezado{\n"
"background-color:#1F3A5F;\n"
"height:30px;\n"
"min-height: 30px;\n"
"max-height: 30px;\n"
"}\n"
"[objectName^=\"w_\"]{\n"
"background-color: #fffefb;\n"
"}\n"
"[objectName^=\"p_\"]{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"#w_cuerpo_menu{\n"
"min-width:40px;\n"
"max-width:70px;\n"
"background-color: #1F3A5F;\n"
"}\n"
"#label_fotousuario{\n"
"image: url(:/Icons/IconosSVG/perfil.png);\n"
"max-height:40px;\n"
"min-height:40px;\n"
"bac"
                        "kground-repeat: no-repeat;\n"
"background-position: center;\n"
"}\n"
"[objectName^=\"btn_laterales\"]{\n"
"background-color: transparent;\n"
"border: none;\n"
"max-height:35px;\n"
"min-height:35px;\n"
"qproperty-iconSize: 35px 35px;\n"
"}\n"
"[objectName^=\"btn_laterales\"]:hover {\n"
"border-left:1px solid #fffefb;\n"
"}\n"
"[objectName^=\"p_\"]{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"#label_wp_fotousuario{\n"
"background-color:#71c4ef;\n"
"border:  1px solid #cccbc8;\n"
"}\n"
"#label_wp_fotousuario{\n"
"min-width: 100px;\n"
"max-width: 100px;\n"
"min-height: 100px;\n"
"max-height: 100px;\n"
"}\n"
"[objectName^=\"label_wp\"]{\n"
"font-family: Arial;\n"
"color: #1d1c1c;\n"
"font-size:12px;\n"
"}\n"
"#label_wp_nombreusuario{\n"
"font-size:20px;\n"
"font-weight:bold;\n"
"}\n"
"#label_wp_puestousuario{\n"
"font-size:16px;\n"
"}\n"
"#label_wp_telefonoempleado{\n"
"font-size:14px;\n"
"font-weight:bold;\n"
"color: #3b3c3d;\n"
"}\n"
"#w_datos_empleado{\n"
"background-color:#f5f4f1;\n"
"border-radius: 10p"
                        "x;\n"
"}\n"
"#btn_ver_datosempleado{\n"
"qproperty-iconSize: 20px 20px;\n"
"}")
        self.gridLayout_18 = QGridLayout(Principal_sistema)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.gridLayout_18.setContentsMargins(0, 0, 0, 0)
        self.w_contenedor = QWidget(Principal_sistema)
        self.w_contenedor.setObjectName(u"w_contenedor")
        self.verticalLayout = QVBoxLayout(self.w_contenedor)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.w_encabezado = QWidget(self.w_contenedor)
        self.w_encabezado.setObjectName(u"w_encabezado")
        self.gridLayout_2 = QGridLayout(self.w_encabezado)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(5)
        self.gridLayout_2.setVerticalSpacing(0)
        self.gridLayout_2.setContentsMargins(5, 0, 5, 0)
        self.btc_minimizar_2 = QPushButton(self.w_encabezado)
        self.btc_minimizar_2.setObjectName(u"btc_minimizar_2")
        self.btc_minimizar_2.setMinimumSize(QSize(35, 25))
        self.btc_minimizar_2.setMaximumSize(QSize(16777215, 16777215))
        self.btc_minimizar_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btc_minimizar_2.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/Icons/Bootstrap/arrows-angle-contract.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btc_minimizar_2.setIcon(icon)
        self.btc_minimizar_2.setIconSize(QSize(20, 15))

        self.gridLayout_2.addWidget(self.btc_minimizar_2, 0, 2, 1, 1)

        self.btc_cerrar_2 = QPushButton(self.w_encabezado)
        self.btc_cerrar_2.setObjectName(u"btc_cerrar_2")
        self.btc_cerrar_2.setMinimumSize(QSize(35, 25))
        self.btc_cerrar_2.setMaximumSize(QSize(16777215, 16777215))
        self.btc_cerrar_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/Icons/Bootstrap/x-lg.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btc_cerrar_2.setIcon(icon1)
        self.btc_cerrar_2.setIconSize(QSize(20, 15))

        self.gridLayout_2.addWidget(self.btc_cerrar_2, 0, 3, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 0, 1, 1, 1)

        self.label_logoempresa = QLabel(self.w_encabezado)
        self.label_logoempresa.setObjectName(u"label_logoempresa")
        self.label_logoempresa.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_logoempresa, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.w_encabezado)

        self.w_cuerpo = QWidget(self.w_contenedor)
        self.w_cuerpo.setObjectName(u"w_cuerpo")
        self.gridLayout_3 = QGridLayout(self.w_cuerpo)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.w_cuerpo_menu = QWidget(self.w_cuerpo)
        self.w_cuerpo_menu.setObjectName(u"w_cuerpo_menu")
        self.verticalLayout_2 = QVBoxLayout(self.w_cuerpo_menu)
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(3, 10, 3, 3)
        self.label_fotousuario = QLabel(self.w_cuerpo_menu)
        self.label_fotousuario.setObjectName(u"label_fotousuario")
        self.label_fotousuario.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.label_fotousuario.setScaledContents(False)
        self.label_fotousuario.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_fotousuario)

        self.btn_laterales_proceso_venta = QToolButton(self.w_cuerpo_menu)
        self.btn_laterales_proceso_venta.setObjectName(u"btn_laterales_proceso_venta")
        self.btn_laterales_proceso_venta.setMinimumSize(QSize(0, 35))
        self.btn_laterales_proceso_venta.setMaximumSize(QSize(16777215, 35))
        self.btn_laterales_proceso_venta.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/Icons/IconosSVG/ventas.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_laterales_proceso_venta.setIcon(icon2)

        self.verticalLayout_2.addWidget(self.btn_laterales_proceso_venta)

        self.btn_laterales_ventas = QToolButton(self.w_cuerpo_menu)
        self.btn_laterales_ventas.setObjectName(u"btn_laterales_ventas")
        self.btn_laterales_ventas.setMaximumSize(QSize(16777215, 35))
        self.btn_laterales_ventas.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/Icons/IconosSVG/operacion_ventas.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_laterales_ventas.setIcon(icon3)

        self.verticalLayout_2.addWidget(self.btn_laterales_ventas)

        self.btn_laterales_compras = QToolButton(self.w_cuerpo_menu)
        self.btn_laterales_compras.setObjectName(u"btn_laterales_compras")
        self.btn_laterales_compras.setMaximumSize(QSize(16777215, 35))
        self.btn_laterales_compras.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/Icons/IconosSVG/compras.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_laterales_compras.setIcon(icon4)

        self.verticalLayout_2.addWidget(self.btn_laterales_compras)

        self.btn_laterales_empleados = QToolButton(self.w_cuerpo_menu)
        self.btn_laterales_empleados.setObjectName(u"btn_laterales_empleados")
        self.btn_laterales_empleados.setMaximumSize(QSize(16777215, 35))
        self.btn_laterales_empleados.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u":/Icons/IconosSVG/empleados.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_laterales_empleados.setIcon(icon5)

        self.verticalLayout_2.addWidget(self.btn_laterales_empleados)

        self.btn_laterales_proveedores = QToolButton(self.w_cuerpo_menu)
        self.btn_laterales_proveedores.setObjectName(u"btn_laterales_proveedores")
        self.btn_laterales_proveedores.setMaximumSize(QSize(16777215, 35))
        self.btn_laterales_proveedores.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon6 = QIcon()
        icon6.addFile(u":/Icons/IconosSVG/vendedores.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_laterales_proveedores.setIcon(icon6)

        self.verticalLayout_2.addWidget(self.btn_laterales_proveedores)

        self.btn_laterales_clientes = QToolButton(self.w_cuerpo_menu)
        self.btn_laterales_clientes.setObjectName(u"btn_laterales_clientes")
        self.btn_laterales_clientes.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon7 = QIcon()
        icon7.addFile(u":/Icons/IconosSVG/clientes.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_laterales_clientes.setIcon(icon7)

        self.verticalLayout_2.addWidget(self.btn_laterales_clientes)

        self.btn_laterales_productos = QToolButton(self.w_cuerpo_menu)
        self.btn_laterales_productos.setObjectName(u"btn_laterales_productos")
        self.btn_laterales_productos.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon8 = QIcon()
        icon8.addFile(u":/Icons/IconosSVG/productos.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_laterales_productos.setIcon(icon8)
        self.btn_laterales_productos.setIconSize(QSize(35, 35))

        self.verticalLayout_2.addWidget(self.btn_laterales_productos)

        self.btn_laterales_btn_sucursales = QToolButton(self.w_cuerpo_menu)
        self.btn_laterales_btn_sucursales.setObjectName(u"btn_laterales_btn_sucursales")
        self.btn_laterales_btn_sucursales.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon9 = QIcon()
        icon9.addFile(u":/Icons/IconosSVG/sucursales.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_laterales_btn_sucursales.setIcon(icon9)

        self.verticalLayout_2.addWidget(self.btn_laterales_btn_sucursales)

        self.verticalSpacer = QSpacerItem(20, 45, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.gridLayout_3.addWidget(self.w_cuerpo_menu, 0, 0, 1, 1, Qt.AlignHCenter)

        self.w_cuerpo_contenido = QStackedWidget(self.w_cuerpo)
        self.w_cuerpo_contenido.setObjectName(u"w_cuerpo_contenido")
        self.w_cuerpo_contenido.setStyleSheet(u"")
        self.p_inicial = QWidget()
        self.p_inicial.setObjectName(u"p_inicial")
        self.gridLayout = QGridLayout(self.p_inicial)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget_3 = QWidget(self.p_inicial)
        self.widget_3.setObjectName(u"widget_3")
        self.gridLayout_19 = QGridLayout(self.widget_3)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.label = QLabel(self.widget_3)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"image: url(:/Icons/IconosSVG/logo_devrous.png);")

        self.gridLayout_19.addWidget(self.label, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.widget_3, 0, 0, 1, 1)

        self.w_cuerpo_contenido.addWidget(self.p_inicial)

        self.gridLayout_3.addWidget(self.w_cuerpo_contenido, 0, 1, 1, 1)


        self.verticalLayout.addWidget(self.w_cuerpo)


        self.gridLayout_18.addWidget(self.w_contenedor, 0, 0, 1, 1)


        self.retranslateUi(Principal_sistema)

        self.w_cuerpo_contenido.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Principal_sistema)
    # setupUi

    def retranslateUi(self, Principal_sistema):
        Principal_sistema.setWindowTitle(QCoreApplication.translate("Principal_sistema", u"Form", None))
#if QT_CONFIG(tooltip)
        self.btc_minimizar_2.setToolTip(QCoreApplication.translate("Principal_sistema", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Minimizar</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btc_minimizar_2.setText("")
#if QT_CONFIG(tooltip)
        self.btc_cerrar_2.setToolTip(QCoreApplication.translate("Principal_sistema", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Cerrar</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btc_cerrar_2.setText("")
        self.label_logoempresa.setText("")
#if QT_CONFIG(tooltip)
        self.label_fotousuario.setToolTip(QCoreApplication.translate("Principal_sistema", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Perfil</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_fotousuario.setText("")
#if QT_CONFIG(tooltip)
        self.btn_laterales_proceso_venta.setToolTip(QCoreApplication.translate("Principal_sistema", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Venta</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_laterales_proceso_venta.setText("")
#if QT_CONFIG(tooltip)
        self.btn_laterales_ventas.setToolTip(QCoreApplication.translate("Principal_sistema", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Ventas</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_laterales_ventas.setText("")
#if QT_CONFIG(tooltip)
        self.btn_laterales_compras.setToolTip(QCoreApplication.translate("Principal_sistema", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Compras</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_laterales_compras.setText("")
#if QT_CONFIG(tooltip)
        self.btn_laterales_empleados.setToolTip(QCoreApplication.translate("Principal_sistema", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Empleados</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_laterales_empleados.setText("")
#if QT_CONFIG(tooltip)
        self.btn_laterales_proveedores.setToolTip(QCoreApplication.translate("Principal_sistema", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Proveedores</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_laterales_proveedores.setText("")
#if QT_CONFIG(tooltip)
        self.btn_laterales_clientes.setToolTip(QCoreApplication.translate("Principal_sistema", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Clientes</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_laterales_clientes.setText("")
#if QT_CONFIG(tooltip)
        self.btn_laterales_productos.setToolTip(QCoreApplication.translate("Principal_sistema", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Productos</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_laterales_productos.setText(QCoreApplication.translate("Principal_sistema", u"...", None))
#if QT_CONFIG(tooltip)
        self.btn_laterales_btn_sucursales.setToolTip(QCoreApplication.translate("Principal_sistema", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Administrador de Sucursales</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_laterales_btn_sucursales.setText("")
        self.label.setText("")
    # retranslateUi

