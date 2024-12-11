from ..Model.BaseDatosModel import Areas_negocios
from ..Controller.MensajesAlertasController import Mensaje

class AreaNegocioClientesModel:
    def  __init__(self, session):
        self.session = session
        
    def agregar_area(self, nombre, descripcion = None):
        try:
            area = self.session.query(Areas_negocios).filter_by(nombre = nombre).first()
            if area:
                return  area
            else:
                area = Areas_negocios(nombre = nombre, descripcion = descripcion)
                self.session.add(area)
                self.session.flush()
                return area
        except Exception as e:
            Mensaje().mensaje_critico(f'error al insertar {e}')

    def obtener_areas(self):
        try:
            areas = self.session.query(Areas_negocios).all()
            if areas:
                return areas
            else:
                return None
        except Exception as e:
            Mensaje().mensaje_critico(f'error al obtener {e}')

    def obtener_id_area(self, nombre):
        try:
            area = self.session.query(Areas_negocios).filter_by(nombre = nombre).first()
            if area:
                return area.id
            else:
                return None
        except Exception as e:
            Mensaje().mensaje_critico(f'error al obtener {e}')
        