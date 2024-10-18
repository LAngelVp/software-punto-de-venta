from PyQt5.QtWidgets import QListView
class AjustarCajaOpciones:
    def __init__(self):
        pass

    def ajustar_cajadeopciones(self, caja_opciones):
        # Usar un QListView para la vista del combo box
        vista_lista = QListView()
        vista_lista.setStyleSheet("""
        QListView { background: #F5F5F5; }
        """)
        caja_opciones.setView(vista_lista)

        # Obtener el ancho del combo box
        ancho_combo = caja_opciones.width()

        # Calcular el ancho máximo basado en los elementos
        max_ancho = max(
            caja_opciones.fontMetrics().width(caja_opciones.itemText(i))
            for i in range(caja_opciones.count())
        )

        # Establecer el ancho del QListView
        # Tomar el mayor entre el ancho del combo box y el ancho máximo
        vista_lista.setFixedWidth(max(ancho_combo, max_ancho))