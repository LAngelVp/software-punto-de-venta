# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UI_EXISTENCIA_PRODUCTOS.ui'
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QComboBox, QDateEdit,
    QDoubleSpinBox, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QPlainTextEdit, QPushButton, QSizePolicy,
    QSpacerItem, QWidget)
import ibootstrap_rc

class Ui_UI_EXISTENCIA_PRODUCTO(object):
    def setupUi(self, UI_EXISTENCIA_PRODUCTO):
        if not UI_EXISTENCIA_PRODUCTO.objectName():
            UI_EXISTENCIA_PRODUCTO.setObjectName(u"UI_EXISTENCIA_PRODUCTO")
        UI_EXISTENCIA_PRODUCTO.resize(547, 385)
        UI_EXISTENCIA_PRODUCTO.setStyleSheet(u"*{color: #1d1c1c;}\n"
"[objectName*=\"contenedor\"]{border:none;}\n"
"#contenedor_encabezado{\n"
"background: #023375;\n"
"}\n"
"#etiqueta_encabezado_existenciaProducto{\n"
"color: #fffefb;\n"
"font-size: 18px;\n"
"font-weight:bold;\n"
"font-family:\"Arial\";\n"
"}\n"
"[objectName *=\"contenedor\"]{\n"
"background:#fffefb;\n"
"}\n"
"[objectName*=\"etiqueta_\"]{\n"
"color: #1d1c1c;\n"
"font-size: 16px;\n"
"font-weight:bold;\n"
"font-family:\"Arial\";\n"
"}\n"
"[objectName*=\"txt\"]{\n"
"border-bottom:  1px solid #787878;\n"
"border-radius: 3px;\n"
"background: #F5F5F5;\n"
"min-width:100px;\n"
"font-size: 14px;\n"
"font-family:\"Arial\";\n"
"}\n"
"[objectName*=\"txt\"]:hover{\n"
"border-bottom:  2px solid #023375;\n"
"}\n"
"[objectName*=\"txt\"]:focus{\n"
"border-bottom:  2px solid #023375;\n"
"}\n"
"[objectName*=\"txtlargo\"]{\n"
"max-height:100px;\n"
"}\n"
"[objectName*=\"btn_existencia\"]{\n"
"border:none;\n"
"font-size:14px;\n"
"font-family:\"Arial\";\n"
"font-weight:bold;\n"
"padding: 5px;\n"
"background: #"
                        "00619a;\n"
"color: #fffefb;\n"
"border-radius: 4px;\n"
"}\n"
"[objectName*=\"btn_existencia\"]:hover{\n"
"background: #2196F3;\n"
"}\n"
"[objectName*=\"btn_existencia\"]:pressed{\n"
"background: #1B80D0;\n"
"}\n"
"#btn_existenciaProducto_cerrar{\n"
"background: #fffefb;\n"
"}\n"
"#btn_existenciaProducto_cerrar:pressed{\n"
"background: rgb(222, 221, 218);\n"
"}\n"
"\n"
"[objectName*=\"decimal\"]{\n"
"min-width:100px;\n"
"background: #F5F5F5;\n"
"borde:none;\n"
"border-radius: 2px;\n"
"border-bottom: 1px solid #787878;\n"
"padding: 0px 2px;\n"
"font-size: 14px;\n"
"font-family: \"Arial\";\n"
"}\n"
"[objectName*=\"decimal\"]:focus{\n"
"border-bottom: 2px solid #023375;\n"
"}\n"
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
""
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
"    background-c"
                        "olor: #f5f4f1;\n"
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
"/* EFECTO HOVER SOBRE D\u00cdAS */\n"
"QCalendarWidget QAbstractItemView::item:hover {\n"
"    background-color: #e1f0f7;\n"
"    color: #1d1c1c;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"[objectName*=\"cajaOpciones\"] {\n"
"    border: none;\n"
"    border-bottom: 1px solid #787878 ;\n"
"    padding: 2px ;\n"
"    background-color: #F5F5F5 ;\n"
"    font-size: 14px ;\n"
"    min-width: 200px ;\n"
"    font-family: \"Arial\" ;\n"
"    color: #1d1c1c ;\n"
"	selection-background-color: #4791F5; \n"
"}\n"
"\n"
"/* ESTILO DEL DROPDOWN (LISTA) */\n"
"[objectName*=\"cajaOpciones\"] QListView {\n"
"   "
                        " background: #F5F5F5 ;\n"
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
"}")
        self.gridLayout = QGridLayout(UI_EXISTENCIA_PRODUCTO)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.contenedor = QFrame(UI_EXISTENCIA_PRODUCTO)
        self.contenedor.setObjectName(u"contenedor")
        self.contenedor.setFrameShape(QFrame.Shape.StyledPanel)
        self.contenedor.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_5 = QGridLayout(self.contenedor)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.contenedor_gridLayout_2 = QGridLayout()
        self.contenedor_gridLayout_2.setObjectName(u"contenedor_gridLayout_2")
        self.contenedor_gridLayout_2.setVerticalSpacing(10)
        self.contenedor_gridLayout_2.setContentsMargins(10, 10, 10, -1)
        self.etiqueta_NotasExistencia = QLabel(self.contenedor)
        self.etiqueta_NotasExistencia.setObjectName(u"etiqueta_NotasExistencia")

        self.contenedor_gridLayout_2.addWidget(self.etiqueta_NotasExistencia, 3, 0, 1, 1)

        self.txtlargo_NotasProducto = QPlainTextEdit(self.contenedor)
        self.txtlargo_NotasProducto.setObjectName(u"txtlargo_NotasProducto")

        self.contenedor_gridLayout_2.addWidget(self.txtlargo_NotasProducto, 4, 0, 1, 2)

        self.etiqueta_FechaMovimiento = QLabel(self.contenedor)
        self.etiqueta_FechaMovimiento.setObjectName(u"etiqueta_FechaMovimiento")

        self.contenedor_gridLayout_2.addWidget(self.etiqueta_FechaMovimiento, 2, 0, 1, 1)

        self.decimal_CantidadExistencia = QDoubleSpinBox(self.contenedor)
        self.decimal_CantidadExistencia.setObjectName(u"decimal_CantidadExistencia")
        self.decimal_CantidadExistencia.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.decimal_CantidadExistencia.setDecimals(3)
        self.decimal_CantidadExistencia.setMaximum(999999999999999929757289024535551219930759168.000000000000000)

        self.contenedor_gridLayout_2.addWidget(self.decimal_CantidadExistencia, 0, 1, 1, 1)

        self.etiqueta_TipoMovimiento = QLabel(self.contenedor)
        self.etiqueta_TipoMovimiento.setObjectName(u"etiqueta_TipoMovimiento")

        self.contenedor_gridLayout_2.addWidget(self.etiqueta_TipoMovimiento, 1, 0, 1, 1)

        self.cajaOpciones_TipoMovimiento = QComboBox(self.contenedor)
        self.cajaOpciones_TipoMovimiento.addItem("")
        self.cajaOpciones_TipoMovimiento.addItem("")
        self.cajaOpciones_TipoMovimiento.setObjectName(u"cajaOpciones_TipoMovimiento")
        self.cajaOpciones_TipoMovimiento.setFrame(True)

        self.contenedor_gridLayout_2.addWidget(self.cajaOpciones_TipoMovimiento, 1, 1, 1, 1)

        self.fecha_FechaMovimiento = QDateEdit(self.contenedor)
        self.fecha_FechaMovimiento.setObjectName(u"fecha_FechaMovimiento")
        self.fecha_FechaMovimiento.setCalendarPopup(True)

        self.contenedor_gridLayout_2.addWidget(self.fecha_FechaMovimiento, 2, 1, 1, 1)

        self.etiqueta_CantidadExistencia = QLabel(self.contenedor)
        self.etiqueta_CantidadExistencia.setObjectName(u"etiqueta_CantidadExistencia")

        self.contenedor_gridLayout_2.addWidget(self.etiqueta_CantidadExistencia, 0, 0, 1, 1)


        self.gridLayout_5.addLayout(self.contenedor_gridLayout_2, 2, 0, 1, 3)

        self.contenedor_frame = QFrame(self.contenedor)
        self.contenedor_frame.setObjectName(u"contenedor_frame")
        self.contenedor_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.contenedor_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_4 = QGridLayout(self.contenedor_frame)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.btn_existenciaProducto_aceptar = QPushButton(self.contenedor_frame)
        self.btn_existenciaProducto_aceptar.setObjectName(u"btn_existenciaProducto_aceptar")
        self.btn_existenciaProducto_aceptar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout_4.addWidget(self.btn_existenciaProducto_aceptar, 1, 0, 1, 1)


        self.gridLayout_5.addWidget(self.contenedor_frame, 4, 0, 1, 3)

        self.contenedor_encabezado = QFrame(self.contenedor)
        self.contenedor_encabezado.setObjectName(u"contenedor_encabezado")
        self.contenedor_encabezado.setFrameShape(QFrame.Shape.StyledPanel)
        self.contenedor_encabezado.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.contenedor_encabezado)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.etiqueta_encabezado_existenciaProducto = QLabel(self.contenedor_encabezado)
        self.etiqueta_encabezado_existenciaProducto.setObjectName(u"etiqueta_encabezado_existenciaProducto")

        self.horizontalLayout.addWidget(self.etiqueta_encabezado_existenciaProducto)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_existenciaProducto_cerrar = QPushButton(self.contenedor_encabezado)
        self.btn_existenciaProducto_cerrar.setObjectName(u"btn_existenciaProducto_cerrar")
        self.btn_existenciaProducto_cerrar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/Icons/Bootstrap/x-lg.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_existenciaProducto_cerrar.setIcon(icon)

        self.horizontalLayout.addWidget(self.btn_existenciaProducto_cerrar)


        self.gridLayout_5.addWidget(self.contenedor_encabezado, 0, 0, 1, 3)

        self.contenedor_gridLayout_3 = QGridLayout()
        self.contenedor_gridLayout_3.setObjectName(u"contenedor_gridLayout_3")
        self.contenedor_gridLayout_3.setVerticalSpacing(10)
        self.contenedor_gridLayout_3.setContentsMargins(10, 10, 10, -1)
        self.etiqueta_Usuario = QLabel(self.contenedor)
        self.etiqueta_Usuario.setObjectName(u"etiqueta_Usuario")

        self.contenedor_gridLayout_3.addWidget(self.etiqueta_Usuario, 0, 0, 1, 1)

        self.etiqueta_NombreUsuario = QLabel(self.contenedor)
        self.etiqueta_NombreUsuario.setObjectName(u"etiqueta_NombreUsuario")

        self.contenedor_gridLayout_3.addWidget(self.etiqueta_NombreUsuario, 0, 1, 1, 1)

        self.etiqueta_Clave = QLabel(self.contenedor)
        self.etiqueta_Clave.setObjectName(u"etiqueta_Clave")

        self.contenedor_gridLayout_3.addWidget(self.etiqueta_Clave, 1, 0, 1, 1)

        self.etiqueta_ClaveProducto = QLabel(self.contenedor)
        self.etiqueta_ClaveProducto.setObjectName(u"etiqueta_ClaveProducto")

        self.contenedor_gridLayout_3.addWidget(self.etiqueta_ClaveProducto, 1, 1, 1, 1)


        self.gridLayout_5.addLayout(self.contenedor_gridLayout_3, 1, 0, 1, 3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer, 3, 0, 1, 3)


        self.gridLayout.addWidget(self.contenedor, 0, 0, 1, 1)

        QWidget.setTabOrder(self.decimal_CantidadExistencia, self.cajaOpciones_TipoMovimiento)
        QWidget.setTabOrder(self.cajaOpciones_TipoMovimiento, self.fecha_FechaMovimiento)
        QWidget.setTabOrder(self.fecha_FechaMovimiento, self.txtlargo_NotasProducto)
        QWidget.setTabOrder(self.txtlargo_NotasProducto, self.btn_existenciaProducto_aceptar)

        self.retranslateUi(UI_EXISTENCIA_PRODUCTO)

        QMetaObject.connectSlotsByName(UI_EXISTENCIA_PRODUCTO)
    # setupUi

    def retranslateUi(self, UI_EXISTENCIA_PRODUCTO):
        UI_EXISTENCIA_PRODUCTO.setWindowTitle(QCoreApplication.translate("UI_EXISTENCIA_PRODUCTO", u"Existencia Producto", None))
        self.etiqueta_NotasExistencia.setText(QCoreApplication.translate("UI_EXISTENCIA_PRODUCTO", u"Notas", None))
        self.etiqueta_FechaMovimiento.setText(QCoreApplication.translate("UI_EXISTENCIA_PRODUCTO", u"Fecha del Movimiento", None))
        self.etiqueta_TipoMovimiento.setText(QCoreApplication.translate("UI_EXISTENCIA_PRODUCTO", u"Movimiento", None))
        self.cajaOpciones_TipoMovimiento.setItemText(0, QCoreApplication.translate("UI_EXISTENCIA_PRODUCTO", u"Entrada", None))
        self.cajaOpciones_TipoMovimiento.setItemText(1, QCoreApplication.translate("UI_EXISTENCIA_PRODUCTO", u"Salida", None))

        self.fecha_FechaMovimiento.setDisplayFormat(QCoreApplication.translate("UI_EXISTENCIA_PRODUCTO", u"dd/MM/yyyy", None))
        self.etiqueta_CantidadExistencia.setText(QCoreApplication.translate("UI_EXISTENCIA_PRODUCTO", u"Cantidad", None))
        self.btn_existenciaProducto_aceptar.setText(QCoreApplication.translate("UI_EXISTENCIA_PRODUCTO", u"Aceptar", None))
        self.etiqueta_encabezado_existenciaProducto.setText(QCoreApplication.translate("UI_EXISTENCIA_PRODUCTO", u"EXISTENCIA", None))
        self.btn_existenciaProducto_cerrar.setText("")
        self.etiqueta_Usuario.setText(QCoreApplication.translate("UI_EXISTENCIA_PRODUCTO", u"Usuario:", None))
        self.etiqueta_NombreUsuario.setText(QCoreApplication.translate("UI_EXISTENCIA_PRODUCTO", u"Nombre", None))
        self.etiqueta_Clave.setText(QCoreApplication.translate("UI_EXISTENCIA_PRODUCTO", u"Clave del Producto:", None))
        self.etiqueta_ClaveProducto.setText(QCoreApplication.translate("UI_EXISTENCIA_PRODUCTO", u"clave", None))
    # retranslateUi

