from PyQt5.QtWidgets import QListView
class AjustarCajaOpciones:
    def __init__(self):
        pass

    def ajustar_cajadeopciones(self, caja_opciones):
        # Calcular el ancho máximo basado en los elementos
        tamaño_maximo_ancho = 0
        for i in range(caja_opciones.count()):
            ancho_de_item = caja_opciones.fontMetrics().width(caja_opciones.itemText(i))
            tamaño_maximo_ancho = max(tamaño_maximo_ancho, ancho_de_item)

        # Usar un QListView para la vista del combo box
        vista_de_la_lista = QListView()
        caja_opciones.setView(vista_de_la_lista)

        # Ajustar el ancho del QListView al tamaño del contenido
        vista_de_la_lista.setFixedWidth(tamaño_maximo_ancho + 40)  # Ajusta el ancho del menú desplegable

        # (Opcional) Ajustar el tamaño de la lista según el número de elementos
        # vista_de_la_lista.setMinimumHeight(caja_opciones.sizeHint().height() * min(caja_opciones.count(), 5))  # Mostrar hasta 5 elementos