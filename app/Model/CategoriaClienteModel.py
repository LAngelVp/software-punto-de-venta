from .BaseDatosModel import Categorias_de_clientes

class CategoriaClienteModel:
    def __init__(self, session):
        self.session = session

    def agregar(self, nombre, descripcion = None):
        try:
            categoria = self.session.query(Categorias_de_clientes).filter_by(nombre = nombre).first()
            if categoria:
                return categoria.id
            else:
                categoria = Categorias_de_clientes(nombre = nombre, descripcion = descripcion)
                self.session.add(categoria)
                self.session.flush()
                return categoria.id
        except Exception as e:
            print(f"Error al agregar categoria: {e}")

    def obtener_categorias(self):
        try:
            categorias = self.session.query(Categorias_de_clientes).all()
            if categorias:
                return categorias
            else:
                return None
        except Exception as e:
            print(f'error al obtener {e}')

    #comment: obtener id de la categoria por su nombre
    def  obtener_id_categoria(self, nombre):
        try:
            categoria = self.session.query(Categorias_de_clientes).filter_by(nombre = nombre).first()
            if categoria:
                return categoria.id
            else:
                return None
        except Exception as e:
            print(f'error al obtener id de categoria {e}')

    def obtener_categoria_por_id(self, id):
        try:
            Categoria = self.session.query(Categorias_de_clientes).filter_by(id == id).first()
            if Categoria:
                return Categoria
            else:
                return None
        except Exception as e:
            print(f'error al obtener categoria por id {e}')
