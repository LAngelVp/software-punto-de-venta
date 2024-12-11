class Comprobacion:
    def __init__(self):
        pass
    def obtener_valor_o_vacio(self, objeto):
        """
        Devuelve el valor del atributo del objeto si no es None, de lo contrario devuelve una cadena vacía.
        """
        if objeto is None:
            return ''
        return objeto if objeto is not None else ''