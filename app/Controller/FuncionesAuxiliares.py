import unicodedata, os
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