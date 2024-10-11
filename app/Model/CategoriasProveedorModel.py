from .BaseDatosModel import Categorias_proveedores

class CategoriaProveedorModel:
    def __init__(self, session):
        self.session = session

    def agregar_categoria(self,
                        nombre,
                        descripcion
                        ):
        categoria = self.session.query(Categorias_proveedores).filter_by(nombre = nombre).first()
        if categoria:
            return categoria.id
        else:
            nueva_categoria = Categorias_proveedores(
                nombre = nombre,
                descripcion = descripcion
                )
            self.session.add(nueva_categoria)
            self.session.flush()
            return nueva_categoria.id
        
    def obtener_todas(self):
        return self.session.query(Categorias_proveedores).all()
    def obtener_id_por_nombre(self, nombre):
        try:
            categoria = self.session.query(Categorias_proveedores).filter_by(nombre = nombre).first()
            return categoria.id
        except Exception as e:
            return None