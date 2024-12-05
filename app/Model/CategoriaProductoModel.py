from .BaseDatosModel import Categorias_productos

class CategoriaProductoModel:
    def __init__(self, session):
        self.session = session
        
    def agregar(self, nombre, descripcion):
        if not nombre and not descripcion:
            return None, False
        categoria = self.session.query(Categorias_productos).filter(Categorias_productos.nombre==nombre).first()
        if categoria:
            return None, False
        categoria = Categorias_productos(nombre=nombre, descripcion=descripcion)
        self.session.add(categoria)
        self.session.flush()
        return categoria, True
    
    def obtener_todo(self):
        categorias = self.session.query(Categorias_productos).all()
        if not categorias:
            return None, False
        return categorias, True