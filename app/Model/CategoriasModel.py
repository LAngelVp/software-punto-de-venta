from .BaseDatosModel import Categorias_productos, Categorias_de_clientes, Categorias_proveedores

class CategoriasModel:
    def __init__(self, session):
        self.session = session
        
    def agregar(self, tipo_categoria, nombre, descripcion = None):
        modelo = self.__tipo_categoria(tipo_categoria)
        categoria = self.session.query(modelo).filter(modelo.nombre==nombre).first()
        if categoria:
            return None, False
        categoria = modelo(nombre=nombre, descripcion=descripcion)
        self.session.add(categoria)
        self.session.flush()
        return categoria, True
    
    def obtener_todo(self, tipo_categoria):
        modelo = self.__tipo_categoria(tipo_categoria)
        categorias = self.session.query(modelo).all()
        if not categorias:
            return None, False
        return categorias, True
    
    def obtener_id_por_nombre(self, tipo_categoria, nombre):
        modelo = self.__tipo_categoria(tipo_categoria)
        try:
            categoria = self.session.query(modelo).filter_by(nombre = nombre).first()
            return categoria.id
        except Exception as e:
            return None
        
    def obtener_categoria_por_id(self, tipo_categoria, id):
        modelo = self.__tipo_categoria(tipo_categoria)
        try:
            Categoria = self.session.query(modelo).filter_by(id == id).first()
            if Categoria:
                return Categoria
            else:
                return None
        except Exception as e:
            print(f'error al obtener categoria por id {e}')
    
    def __tipo_categoria(self, tipo_categoria):
        if tipo_categoria == 'productos':
            return Categorias_productos
        elif tipo_categoria == 'clientes':
            return Categorias_de_clientes
        elif tipo_categoria == 'proveedores':
            return Categorias_proveedores
        return None
    