# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UI_CONTROL_VENTA.ui'
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QColumnView, QDateEdit,
    QDoubleSpinBox, QFormLayout, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QToolButton, QWidget)
from ...Source import ibootstrap_rc
from ...Source import iconosSVG_rc

class Ui_Venta(object):
    def setupUi(self, Venta):
        if not Venta.objectName():
            Venta.setObjectName(u"Venta")
        Venta.resize(1076, 460)
        Venta.setStyleSheet(u"*{color: #1d1c1c;}\n"
"#Venta{\n"
"background: #fffefb;\n"
"}\n"
"#contenedor_controlcentral{\n"
"min-height: 200px;\n"
"}\n"
"#contenedor_detallesventa{\n"
"background: #B0C5D1;\n"
"border-radius: 10px;\n"
"min-width: 300px;\n"
"}\n"
"[objectName*=\"contenedor\"]{\n"
"background: #fffefb;\n"
"border:none;\n"
"}\n"
"[objectName*=\"etiqueta_\"]{\n"
"font-size: 14px;\n"
"font-family:Arial;\n"
"font-weight:bold;\n"
"color: #1d1c1c;\n"
"}\n"
"[objectName*=\"txt_\"]{\n"
"font-size: 14px;\n"
"font-family:Arial;\n"
"color: #1d1c1c;\n"
"background: #F5F5F5;\n"
"border-radius: 5px;\n"
"border:none;\n"
"border-bottom: 1px solid;\n"
"}\n"
"[objectName*=\"etiquetaTitulo_\"]{\n"
"font-size: 20px;\n"
"font-family:Arial;\n"
"font-weight:bold;\n"
"color: #1d1c1c;\n"
"}\n"
"[objectName*=\"etiquetaresultado_\"]{\n"
"font-size: 16px;\n"
"font-family:Arial;\n"
"font-weight:bold;\n"
"color: #1d1c1c;\n"
"}\n"
"#etiqueta_iconocodigobarras{\n"
"image: url(:/Icons/Bootstrap/upc-scan.svg);\n"
"min-width: 20px;\n"
"}\n"
"[objectName*=\""
                        "btn_btn_\"]{\n"
"height: 25px;\n"
"color: #fffefb;\n"
"background: #00619a;\n"
"border-radius: 5px;\n"
"font-family: Arial;\n"
"font-weight: bold;\n"
"font-size: 14px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"}\n"
"[objectName*=\"btn_btn_\"]:hover{\n"
"background: #2196F3;\n"
"}\n"
"#btn_btn_cobrar{\n"
"min-height:70px;\n"
"min-width: 90px;\n"
"font-size:20px;\n"
"}\n"
"#btn_btn_cobrar:hover{\n"
"background: #68a67d;\n"
"}\n"
"[objectName*=\"txt_\"]:focus{\n"
"border-bottom: 2px solid #023375;\n"
"}\n"
"\n"
"/*------TABLA-----*/\n"
"[objectName*=\"tabla_\"] {\n"
"    font-family: Arial;\n"
"    font-size: 14px;\n"
"background: #E3E3E3;\n"
"border:none;\n"
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
"[objectName*=\"tabla_\"] QHeaderView::hori"
                        "zontal {\n"
"    background-color: #023375;\n"
"    color: white;\n"
"}\n"
"\n"
"/* Encabezado vertical */\n"
"[objectName*=\"tabla_\"] QHeaderView::vertical {\n"
"    background-color: #023375;\n"
"    color: white;\n"
"}\n"
"\n"
"\n"
"[objectName*=\"fecha_\"]{\n"
"border: none;\n"
"border-bottom: 1px solid #3b3c3d;\n"
"border-radius: 5px;\n"
"padding: 2px;\n"
"background-color: #f5f4f1;\n"
"font-size: 14px;\n"
"min-width:100px;\n"
"}\n"
"*[objectName*=\"fecha_\"]::drop-down{\n"
"subcontrol-origin: padding;\n"
"subcontrol-position: top right;\n"
"padding-right:5px;\n"
"width: 20%;\n"
"border-left-width: 1px;\n"
"borde-radius: 5px;\n"
"background-color: #F5F5F5;\n"
"}\n"
"*[objectName*=\"fecha_\"]::down-arrow{\n"
"image: url(:/Icons/Bootstrap/calendar2-date.svg);\n"
"width: 17%;\n"
"height: 17%;\n"
"padding-left:5px;\n"
"padding-right:5px;\n"
"background: #F5F5F5;\n"
"}\n"
"*[objectName*=\"fecha_\"]::focus{\n"
"border-bottom: 2px solid #00668c;\n"
"}\n"
"QCalendarWidget QWidget#qt_calendar_navigationbar {\n"
""
                        "    background-color: #00668c;\n"
"    color: white;\n"
"    border-top-left-radius: 5px;\n"
"    border-top-right-radius: 5px;\n"
"}\n"
"\n"
"/* BOTONES DE NAVEGACI\u00d3N */\n"
"QCalendarWidget QToolButton {\n"
"    background-color: transparent;\n"
"    color: white;\n"
"    font-weight: bold;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"/* DESPLEGABLE DE MESES */\n"
"QCalendarWidget QMenu {\n"
"    background-color: #FFFFFF;\n"
"    border: 1px solid #3b3c3d;\n"
"}\n"
"\n"
"/* D\u00cdAS DE LA SEMANA */\n"
"QCalendarWidget QWidget#qt_calendar_weekdaybar {\n"
"    background-color: #f5f4f1;\n"
"    color: #3b3c3d;\n"
"}\n"
"\n"
"/* D\u00cdAS DEL MES */\n"
"QCalendarWidget QAbstractItemView:enabled {\n"
"    background-color: #FFFFFF;\n"
"    color: #1d1c1c;\n"
"    selection-background-color: #00668c;  /* Color al seleccionar fecha */\n"
"    selection-color: white;\n"
"}\n"
"\n"
"/* D\u00cdAS DE OTROS MESES */\n"
"QCalendarWidget QAbstractItemView:disabled {\n"
"    color: #AAAAAA;\n"
"}\n"
"\n"
"/* EFECTO HOVER SO"
                        "BRE D\u00cdAS */\n"
"QCalendarWidget QAbstractItemView::item:hover {\n"
"    background-color: #e1f0f7;\n"
"    color: #1d1c1c;\n"
"}\n"
"\n"
"*[objectName*=\"numerodecimal_\"]{\n"
"background-color: rgb(245, 244, 241);\n"
"color: rgb(29, 28, 28);\n"
"border: none;\n"
"border-bottom: 1px solid;\n"
"border-radius: 5px;\n"
"font-size: 12px;\n"
"font-family: Arial;\n"
"}\n"
"*[objectName^=\"numerodecimal_\"]::focus{\n"
"border-bottom: 2px solid #00668c;\n"
"}\n"
"\n"
"#contenedor_controlesinferior{\n"
"max-height: 200px;\n"
"}\n"
"\n"
"#contenedor_creditos{\n"
"min-width: 450px;\n"
"}\n"
"#contenedordescuentosaplicardescuento{\n"
"min-width: 450px;\n"
"}\n"
"")
        self.gridLayout = QGridLayout(Venta)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.contenedor_general = QFrame(Venta)
        self.contenedor_general.setObjectName(u"contenedor_general")
        self.contenedor_general.setFrameShape(QFrame.Shape.StyledPanel)
        self.contenedor_general.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_3 = QGridLayout(self.contenedor_general)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(5, 0, 5, 5)
        self.contenedor_controlcentral = QWidget(self.contenedor_general)
        self.contenedor_controlcentral.setObjectName(u"contenedor_controlcentral")
        self.contenedor_controlcentral.setMinimumSize(QSize(0, 200))
        self.contenedor_controlcentral.setMaximumSize(QSize(16777215, 16777215))
        self.gridLayout_4 = QGridLayout(self.contenedor_controlcentral)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.btn_btn_cancelarticket = QPushButton(self.contenedor_controlcentral)
        self.btn_btn_cancelarticket.setObjectName(u"btn_btn_cancelarticket")
        self.btn_btn_cancelarticket.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout_4.addWidget(self.btn_btn_cancelarticket, 0, 4, 1, 1)

        self.etiqueta_iconocodigobarras = QLabel(self.contenedor_controlcentral)
        self.etiqueta_iconocodigobarras.setObjectName(u"etiqueta_iconocodigobarras")

        self.gridLayout_4.addWidget(self.etiqueta_iconocodigobarras, 0, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer, 0, 3, 1, 1)

        self.etiqueta_buscarproducto = QLabel(self.contenedor_controlcentral)
        self.etiqueta_buscarproducto.setObjectName(u"etiqueta_buscarproducto")

        self.gridLayout_4.addWidget(self.etiqueta_buscarproducto, 0, 0, 1, 1)

        self.txt_buscarproducto = QLineEdit(self.contenedor_controlcentral)
        self.txt_buscarproducto.setObjectName(u"txt_buscarproducto")

        self.gridLayout_4.addWidget(self.txt_buscarproducto, 0, 1, 1, 1)

        self.contenedor_detallesventa = QFrame(self.contenedor_controlcentral)
        self.contenedor_detallesventa.setObjectName(u"contenedor_detallesventa")
        self.contenedor_detallesventa.setStyleSheet(u"")
        self.contenedor_detallesventa.setFrameShape(QFrame.Shape.StyledPanel)
        self.contenedor_detallesventa.setFrameShadow(QFrame.Shadow.Raised)
        self.formLayout = QFormLayout(self.contenedor_detallesventa)
        self.formLayout.setObjectName(u"formLayout")
        self.etiquetaTitulo_ = QLabel(self.contenedor_detallesventa)
        self.etiquetaTitulo_.setObjectName(u"etiquetaTitulo_")
        self.etiquetaTitulo_.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.SpanningRole, self.etiquetaTitulo_)

        self.line_2 = QFrame(self.contenedor_detallesventa)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.SpanningRole, self.line_2)

        self.etiqueta_subtotal = QLabel(self.contenedor_detallesventa)
        self.etiqueta_subtotal.setObjectName(u"etiqueta_subtotal")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.etiqueta_subtotal)

        self.etiquetaresultado_subtotalresultado = QLabel(self.contenedor_detallesventa)
        self.etiquetaresultado_subtotalresultado.setObjectName(u"etiquetaresultado_subtotalresultado")
        self.etiquetaresultado_subtotalresultado.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.etiquetaresultado_subtotalresultado)

        self.etiqueta_descuento = QLabel(self.contenedor_detallesventa)
        self.etiqueta_descuento.setObjectName(u"etiqueta_descuento")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.etiqueta_descuento)

        self.etiquetaresultado_descuentoresultado = QLabel(self.contenedor_detallesventa)
        self.etiquetaresultado_descuentoresultado.setObjectName(u"etiquetaresultado_descuentoresultado")
        self.etiquetaresultado_descuentoresultado.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.etiquetaresultado_descuentoresultado)

        self.etiqueta_impuesto = QLabel(self.contenedor_detallesventa)
        self.etiqueta_impuesto.setObjectName(u"etiqueta_impuesto")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.etiqueta_impuesto)

        self.etiquetaresultado_impuestoresultado = QLabel(self.contenedor_detallesventa)
        self.etiquetaresultado_impuestoresultado.setObjectName(u"etiquetaresultado_impuestoresultado")
        self.etiquetaresultado_impuestoresultado.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.etiquetaresultado_impuestoresultado)

        self.etiquetaTitulo_total = QLabel(self.contenedor_detallesventa)
        self.etiquetaTitulo_total.setObjectName(u"etiquetaTitulo_total")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.etiquetaTitulo_total)

        self.etiquetaTitulo_totalresultado = QLabel(self.contenedor_detallesventa)
        self.etiquetaTitulo_totalresultado.setObjectName(u"etiquetaTitulo_totalresultado")
        self.etiquetaTitulo_totalresultado.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.etiquetaTitulo_totalresultado)


        self.gridLayout_4.addWidget(self.contenedor_detallesventa, 3, 4, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.tabla_productos = QColumnView(self.contenedor_controlcentral)
        self.tabla_productos.setObjectName(u"tabla_productos")

        self.gridLayout_4.addWidget(self.tabla_productos, 3, 0, 1, 4)


        self.gridLayout_3.addWidget(self.contenedor_controlcentral, 0, 0, 1, 1)

        self.contenedor_controlesinferior = QFrame(self.contenedor_general)
        self.contenedor_controlesinferior.setObjectName(u"contenedor_controlesinferior")
        self.contenedor_controlesinferior.setFrameShape(QFrame.Shape.StyledPanel)
        self.contenedor_controlesinferior.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.contenedor_controlesinferior)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.contenedor_descuentosaplicardescuento = QFrame(self.contenedor_controlesinferior)
        self.contenedor_descuentosaplicardescuento.setObjectName(u"contenedor_descuentosaplicardescuento")
        self.contenedor_descuentosaplicardescuento.setMinimumSize(QSize(0, 0))
        self.contenedor_descuentosaplicardescuento.setMaximumSize(QSize(16777215, 16777215))
        self.contenedor_descuentosaplicardescuento.setFrameShape(QFrame.Shape.StyledPanel)
        self.contenedor_descuentosaplicardescuento.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_5 = QGridLayout(self.contenedor_descuentosaplicardescuento)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.etiquetaTitulo_descuentos = QLabel(self.contenedor_descuentosaplicardescuento)
        self.etiquetaTitulo_descuentos.setObjectName(u"etiquetaTitulo_descuentos")

        self.gridLayout_5.addWidget(self.etiquetaTitulo_descuentos, 0, 0, 1, 3)

        self.etiqueta_idclientedescuento = QLabel(self.contenedor_descuentosaplicardescuento)
        self.etiqueta_idclientedescuento.setObjectName(u"etiqueta_idclientedescuento")

        self.gridLayout_5.addWidget(self.etiqueta_idclientedescuento, 1, 0, 1, 1)

        self.etiqueta_nombredescuento = QLabel(self.contenedor_descuentosaplicardescuento)
        self.etiqueta_nombredescuento.setObjectName(u"etiqueta_nombredescuento")

        self.gridLayout_5.addWidget(self.etiqueta_nombredescuento, 2, 0, 1, 1)

        self.etiqueta_tipodescuento = QLabel(self.contenedor_descuentosaplicardescuento)
        self.etiqueta_tipodescuento.setObjectName(u"etiqueta_tipodescuento")

        self.gridLayout_5.addWidget(self.etiqueta_tipodescuento, 3, 0, 1, 1)

        self.txt_tipodescuento = QLineEdit(self.contenedor_descuentosaplicardescuento)
        self.txt_tipodescuento.setObjectName(u"txt_tipodescuento")

        self.gridLayout_5.addWidget(self.txt_tipodescuento, 3, 1, 1, 1)

        self.etiqueta_porcientodescuento = QLabel(self.contenedor_descuentosaplicardescuento)
        self.etiqueta_porcientodescuento.setObjectName(u"etiqueta_porcientodescuento")

        self.gridLayout_5.addWidget(self.etiqueta_porcientodescuento, 3, 2, 1, 1)

        self.txt_porcientodescuento = QLineEdit(self.contenedor_descuentosaplicardescuento)
        self.txt_porcientodescuento.setObjectName(u"txt_porcientodescuento")

        self.gridLayout_5.addWidget(self.txt_porcientodescuento, 3, 3, 1, 1)

        self.btn_btn_aplicardescuento = QPushButton(self.contenedor_descuentosaplicardescuento)
        self.btn_btn_aplicardescuento.setObjectName(u"btn_btn_aplicardescuento")
        self.btn_btn_aplicardescuento.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout_5.addWidget(self.btn_btn_aplicardescuento, 4, 3, 1, 1)

        self.txt_nombredescuento = QLineEdit(self.contenedor_descuentosaplicardescuento)
        self.txt_nombredescuento.setObjectName(u"txt_nombredescuento")

        self.gridLayout_5.addWidget(self.txt_nombredescuento, 2, 1, 1, 3)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.txt_iddescuento = QLineEdit(self.contenedor_descuentosaplicardescuento)
        self.txt_iddescuento.setObjectName(u"txt_iddescuento")

        self.gridLayout_2.addWidget(self.txt_iddescuento, 0, 0, 1, 1)

        self.btn_btn_buscarclientedescuento = QPushButton(self.contenedor_descuentosaplicardescuento)
        self.btn_btn_buscarclientedescuento.setObjectName(u"btn_btn_buscarclientedescuento")
        self.btn_btn_buscarclientedescuento.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/iconosBlancos/Icons/iconos/Blanco/buscar_persona_blanco.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_btn_buscarclientedescuento.setIcon(icon)
        self.btn_btn_buscarclientedescuento.setIconSize(QSize(24, 24))

        self.gridLayout_2.addWidget(self.btn_btn_buscarclientedescuento, 0, 1, 1, 1)


        self.gridLayout_5.addLayout(self.gridLayout_2, 1, 1, 1, 3)


        self.horizontalLayout.addWidget(self.contenedor_descuentosaplicardescuento)

        self.contenedor_creditos = QFrame(self.contenedor_controlesinferior)
        self.contenedor_creditos.setObjectName(u"contenedor_creditos")
        self.contenedor_creditos.setMinimumSize(QSize(450, 0))
        self.contenedor_creditos.setMaximumSize(QSize(16777215, 16777215))
        self.contenedor_creditos.setFrameShape(QFrame.Shape.StyledPanel)
        self.contenedor_creditos.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_8 = QGridLayout(self.contenedor_creditos)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.etiquetaTitulo_creditos = QLabel(self.contenedor_creditos)
        self.etiquetaTitulo_creditos.setObjectName(u"etiquetaTitulo_creditos")

        self.gridLayout_8.addWidget(self.etiquetaTitulo_creditos, 0, 0, 1, 2)

        self.etiqueta_idclientecredito = QLabel(self.contenedor_creditos)
        self.etiqueta_idclientecredito.setObjectName(u"etiqueta_idclientecredito")

        self.gridLayout_8.addWidget(self.etiqueta_idclientecredito, 1, 0, 1, 1)

        self.etiqueta_nombreclientecredito = QLabel(self.contenedor_creditos)
        self.etiqueta_nombreclientecredito.setObjectName(u"etiqueta_nombreclientecredito")

        self.gridLayout_8.addWidget(self.etiqueta_nombreclientecredito, 2, 0, 1, 1)

        self.etiqueta_creditodisponible = QLabel(self.contenedor_creditos)
        self.etiqueta_creditodisponible.setObjectName(u"etiqueta_creditodisponible")
        self.etiqueta_creditodisponible.setWordWrap(False)

        self.gridLayout_8.addWidget(self.etiqueta_creditodisponible, 3, 0, 1, 1)

        self.numerodecimal_cantidadcredito = QDoubleSpinBox(self.contenedor_creditos)
        self.numerodecimal_cantidadcredito.setObjectName(u"numerodecimal_cantidadcredito")
        self.numerodecimal_cantidadcredito.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.numerodecimal_cantidadcredito.setMaximum(10000000000000000000000.000000000000000)

        self.gridLayout_8.addWidget(self.numerodecimal_cantidadcredito, 3, 1, 1, 1)

        self.etiqueta_fechapago = QLabel(self.contenedor_creditos)
        self.etiqueta_fechapago.setObjectName(u"etiqueta_fechapago")

        self.gridLayout_8.addWidget(self.etiqueta_fechapago, 3, 2, 1, 1)

        self.fecha_fechapagocredito = QDateEdit(self.contenedor_creditos)
        self.fecha_fechapagocredito.setObjectName(u"fecha_fechapagocredito")
        self.fecha_fechapagocredito.setCalendarPopup(True)

        self.gridLayout_8.addWidget(self.fecha_fechapagocredito, 3, 3, 1, 1)

        self.btn_btn_cobrarconcredito = QPushButton(self.contenedor_creditos)
        self.btn_btn_cobrarconcredito.setObjectName(u"btn_btn_cobrarconcredito")
        self.btn_btn_cobrarconcredito.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout_8.addWidget(self.btn_btn_cobrarconcredito, 4, 3, 1, 1)

        self.txt_nombreclientecredito = QLineEdit(self.contenedor_creditos)
        self.txt_nombreclientecredito.setObjectName(u"txt_nombreclientecredito")

        self.gridLayout_8.addWidget(self.txt_nombreclientecredito, 2, 1, 1, 3)

        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.txt_idclientecredito = QLineEdit(self.contenedor_creditos)
        self.txt_idclientecredito.setObjectName(u"txt_idclientecredito")

        self.gridLayout_6.addWidget(self.txt_idclientecredito, 0, 0, 1, 1)

        self.btn_btn_buscarcreditocliente = QPushButton(self.contenedor_creditos)
        self.btn_btn_buscarcreditocliente.setObjectName(u"btn_btn_buscarcreditocliente")
        self.btn_btn_buscarcreditocliente.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_btn_buscarcreditocliente.setIcon(icon)
        self.btn_btn_buscarcreditocliente.setIconSize(QSize(24, 24))

        self.gridLayout_6.addWidget(self.btn_btn_buscarcreditocliente, 0, 1, 1, 1)


        self.gridLayout_8.addLayout(self.gridLayout_6, 1, 1, 1, 3)


        self.horizontalLayout.addWidget(self.contenedor_creditos)

        self.contenedor_btn_cobrar = QFrame(self.contenedor_controlesinferior)
        self.contenedor_btn_cobrar.setObjectName(u"contenedor_btn_cobrar")
        self.contenedor_btn_cobrar.setFrameShape(QFrame.Shape.StyledPanel)
        self.contenedor_btn_cobrar.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_7 = QGridLayout(self.contenedor_btn_cobrar)
        self.gridLayout_7.setSpacing(0)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_2, 0, 0, 1, 1)

        self.btn_btn_cobrar = QToolButton(self.contenedor_btn_cobrar)
        self.btn_btn_cobrar.setObjectName(u"btn_btn_cobrar")
        self.btn_btn_cobrar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/iconosBlancos/Icons/iconos/Blanco/dinero_blanco.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_btn_cobrar.setIcon(icon1)
        self.btn_btn_cobrar.setIconSize(QSize(35, 35))
        self.btn_btn_cobrar.setPopupMode(QToolButton.ToolButtonPopupMode.InstantPopup)
        self.btn_btn_cobrar.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.btn_btn_cobrar.setAutoRaise(False)

        self.gridLayout_7.addWidget(self.btn_btn_cobrar, 0, 1, 1, 1)


        self.horizontalLayout.addWidget(self.contenedor_btn_cobrar)


        self.gridLayout_3.addWidget(self.contenedor_controlesinferior, 2, 0, 1, 1)

        self.line = QFrame(self.contenedor_general)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_3.addWidget(self.line, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.contenedor_general, 0, 0, 1, 1)


        self.retranslateUi(Venta)

        QMetaObject.connectSlotsByName(Venta)
    # setupUi

    def retranslateUi(self, Venta):
        Venta.setWindowTitle(QCoreApplication.translate("Venta", u"Form", None))
        self.btn_btn_cancelarticket.setText(QCoreApplication.translate("Venta", u"Cancelar Ticket", None))
        self.etiqueta_iconocodigobarras.setText("")
        self.etiqueta_buscarproducto.setText(QCoreApplication.translate("Venta", u"Codigo del Producto: ", None))
        self.etiquetaTitulo_.setText(QCoreApplication.translate("Venta", u"Resumen de venta", None))
        self.etiqueta_subtotal.setText(QCoreApplication.translate("Venta", u"Subtotal", None))
        self.etiquetaresultado_subtotalresultado.setText(QCoreApplication.translate("Venta", u"cantidad", None))
        self.etiqueta_descuento.setText(QCoreApplication.translate("Venta", u"Descuento (100%)", None))
        self.etiquetaresultado_descuentoresultado.setText(QCoreApplication.translate("Venta", u"Cantidad", None))
        self.etiqueta_impuesto.setText(QCoreApplication.translate("Venta", u"Impuesto (100%)", None))
        self.etiquetaresultado_impuestoresultado.setText(QCoreApplication.translate("Venta", u"cantidad", None))
        self.etiquetaTitulo_total.setText(QCoreApplication.translate("Venta", u"Total", None))
        self.etiquetaTitulo_totalresultado.setText(QCoreApplication.translate("Venta", u"cantidad", None))
        self.etiquetaTitulo_descuentos.setText(QCoreApplication.translate("Venta", u"Aplicaci\u00f3n de descuentos", None))
        self.etiqueta_idclientedescuento.setText(QCoreApplication.translate("Venta", u"Id del cliente", None))
        self.etiqueta_nombredescuento.setText(QCoreApplication.translate("Venta", u"Nombre", None))
        self.etiqueta_tipodescuento.setText(QCoreApplication.translate("Venta", u"Tipo", None))
        self.etiqueta_porcientodescuento.setText(QCoreApplication.translate("Venta", u"Descuento", None))
        self.btn_btn_aplicardescuento.setText(QCoreApplication.translate("Venta", u"Aplicar descuento", None))
        self.btn_btn_buscarclientedescuento.setText("")
        self.etiquetaTitulo_creditos.setText(QCoreApplication.translate("Venta", u"Cobros a cr\u00e9dito", None))
        self.etiqueta_idclientecredito.setText(QCoreApplication.translate("Venta", u"Id del cliente", None))
        self.etiqueta_nombreclientecredito.setText(QCoreApplication.translate("Venta", u"Nombre", None))
        self.etiqueta_creditodisponible.setText(QCoreApplication.translate("Venta", u"Credito disponible", None))
        self.etiqueta_fechapago.setText(QCoreApplication.translate("Venta", u"Fecha Pago", None))
        self.fecha_fechapagocredito.setDisplayFormat(QCoreApplication.translate("Venta", u"dd/MM/yyyy", None))
        self.btn_btn_cobrarconcredito.setText(QCoreApplication.translate("Venta", u"A credito", None))
        self.btn_btn_buscarcreditocliente.setText("")
        self.btn_btn_cobrar.setText(QCoreApplication.translate("Venta", u"Cobrar", None))
    # retranslateUi

