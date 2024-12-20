from .BaseDatosModel import Sucursales

class SucursalesModel:
    def __init__(self, session):
        self.session = session

    def agregar_sucursal(self,
                        nombre_sucursal,
                        codigo_postal,
                        ciudad,
                        estado,
                        pais,
                        num_telefono,
                        direccion
                        ):
        try:
            sucursal = self.session.query(Sucursales).filter_by(nombre_sucursal = nombre_sucursal).first()
            if sucursal:
                return sucursal, False
            else:
                sucursal = Sucursales(nombre_sucursal=nombre_sucursal, codigo_postal=codigo_postal, ciudad = ciudad,  estado = estado, pais = pais, num_telefono=num_telefono, direccion = direccion)
                self.session.add(sucursal)
                self.session.flush()
                return sucursal, True
        except Exception as e:
            return None

    def obtener_sucursal_id(self, nombre):
        try:
            sucursal = self.session.query(Sucursales).filter_by(nombre_sucursal = nombre).first()
            return sucursal.id
        except Exception as e:
            return None
        
    def obtener_sucursal_por_id(self, id):
        try:
            sucursal = self.session.query(Sucursales).filter_by(id = id).first()
            if sucursal:
                return sucursal
            else:
                return None
        except Exception as e:
            return None

    def obtener_todo(self):
        try:
            sucursales = self.session.query(Sucursales).all()
            return sucursales
        except Exception as e:
            return None

    def eliminar(self, id):
        try:
            sucursal = self.session.query(Sucursales).filter(Sucursales.id == id).one_or_none()
            if sucursal:
                self.session.delete(sucursal)
                return True
            return False
        except Exception as e:
            return False
    
    def actualizar(self, 
                id,
                nombre_sucursal,
                codigo_postal,
                ciudad,
                estado,
                pais,
                num_telefono,
                direccion):
        try:
            sucursal = self.session.query(Sucursales).filter_by(id = id).first()
            if sucursal:
                sucursal.nombre_sucursal = nombre_sucursal
                sucursal.codigo_postal = codigo_postal
                sucursal.ciudad = ciudad
                sucursal.estado = estado
                sucursal.pais = pais
                sucursal.num_telefono = num_telefono
                sucursal.direccion = direccion
                return sucursal, True
            else:
                return None, False
        except Exception as e:
            return None, False
    
    def filtrar_nombre(self, texto):
        try:
            texto_busqueda = f"%{texto}%"
            sucursales = self.session.query(Sucursales).filter(Sucursales.nombre_sucursal.ilike(texto_busqueda)).all()
            if sucursales:
                return sucursales, True
            return None, False
        except Exception as e:
            return None, False
