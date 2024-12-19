from .BaseDatosModel import Productos, Presentacion_productos, Unidad_medida_productos

class ProductosModel:
    def __init__(self, session):
        self.session = session
    
    def agregar_presentacion(self, nombre):
        if not nombre:
            return False
        presentacion = Presentacion_productos(nombre = nombre)
        self.session.add(presentacion)
        self.session.flush()
        return presentacion, True
    
    def obtener_presentaciones(self):
        presentaciones = self.session.query(Presentacion_productos).all()
        if presentaciones:
            return presentaciones, True
        else:
            return None, False
    
    def agregar_unidad_medida(self, nombre):
        if not nombre:
            return False
        unidad = Unidad_medida_productos(unidad_medida = nombre)
        self.session.add(unidad)
        self.session.flush()
        return unidad, True
    
    def obtener_unidades_medida(self):
        unidades_medida = self.session.query(Unidad_medida_productos).all()
        if unidades_medida:
            return unidades_medida, True
        else:
            return None, False