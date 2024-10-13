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
            print(e)

    def obtener_sucursal_id(self, nombre):
        try:
            sucursal = self.session.query(Sucursales).filter_by(nombre_sucursal = nombre).first()
            return sucursal.id
        except Exception as e:
            print(e)
            return None
        
    def obtener_sucursal_por_id(self, id):
        try:
            sucursal = self.session.query(Sucursales).filter_by(id = id).first()
            if sucursal:
                return sucursal
            else:
                return None
        except Exception as e:
            print(e)

    
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
                print(f"se elimino el registro del sucursal")
                return True
            return False
        except Exception as e:
            print(f'Error al eliminar el sucursal: {e}')
            return False
            
