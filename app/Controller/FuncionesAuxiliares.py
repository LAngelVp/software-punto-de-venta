import unicodedata, os
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QRect
class FuncionesAuxiliaresController:
    def __init__(self):
         pass
     
    def quitar_acentos(self, texto):
        return ''.join(c for c in unicodedata.normalize('NFD', texto) if unicodedata.category(c) != 'Mn')

    def size_validator_image(self, image):
            if image:
                file_size = os.path.getsize(image)
                if file_size > 1024 * 1024 * 5:
                    return False
                else:
                    return True
            return False

    def caja_opciones_mover_elemento(self, caja_opciones, elemento_a_mover):
            elementos = []
            max_elementos = caja_opciones.count()
            for i in range(max_elementos):
                nombre_elemento = caja_opciones.itemText(i)
                id_elemento = caja_opciones.itemData(i)
                elementos.append((nombre_elemento, id_elemento if id_elemento else None))
                
            elemento_encontrado = False
            for i, (nombre, id_elemento) in enumerate(elementos):
                if nombre.lower() == elemento_a_mover.lower():
                    print(nombre.lower())
                    print(elemento_a_mover.lower())
                    elementos.pop(i)
                    elementos.insert(0, (nombre, id_elemento))
                    elemento_encontrado = True
                    break
            if elemento_encontrado:
                caja_opciones.clear()
                for nombre, id_elemento in elementos:
                    caja_opciones.addItem(nombre, id_elemento)
                    
    @staticmethod
    def centrar_en_padre(ventana: QWidget):
        """
        Centra la ventana dada respecto a su ventana padre (si tiene).
        """
        padre = ventana.parentWidget()
        if padre:
            geo_padre: QRect = padre.geometry()  # usar geometry() en lugar de frameGeometry()
            centro_padre = geo_padre.center()

            # Asegúrate de que la ventana hija tenga una geometría válida
            if not ventana.isVisible():
                ventana.show()
                ventana.hide()  # opcional, si no quieres mostrarla aún

            geo_hija = ventana.frameGeometry()
            geo_hija.moveCenter(centro_padre)

            ventana.move(geo_hija.topLeft())
        # if padre:
        #     geo_padre: QRect = padre.frameGeometry()
        #     centro_padre = geo_padre.center()

        #     geo_hija = ventana.frameGeometry()
        #     geo_hija.moveCenter(centro_padre)

        #     ventana.move(geo_hija.topLeft())