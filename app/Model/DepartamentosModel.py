from .BaseDatosModel import Departamentos, departamento_sucursal

class DepartamentosModel:
    def __init__(self, session):
        self.session = session

    def agregar_departamento(self,
                            nombre,
                            descripcion = None):
        departamento = self.session.query(Departamentos).filter_by(nombre = nombre). first()
        if departamento:
            return  departamento, False
        else:
            try:
                # Crear una instancia del nuevo departamento
                nuevo_departamento = Departamentos(
                    nombre=nombre,
                    descripcion=descripcion
                )

                # Agregar el nuevo departamento a la sesión
                self.session.add(nuevo_departamento)

                # Confirmar los cambios en la base de datos
                self.session.flush()

                return nuevo_departamento, True

            except Exception as e:
                # Revertir los cambios en caso de error
                self.session.rollback()
                return None, False

    def obtener_todos(self):
        try:
            departamentos =  self.session.query(Departamentos).all()
            if departamentos:
                return departamentos, True
            else:
                return None, False
        except Exception as e:
            return None

    def obtener_departamento_por_id(self, id):
        try:
            if id is not None:
                departamento = self.session.query(Departamentos).filter_by(id = id).first()
                return departamento
            else:
                return None
        except Exception as e:
            return None
        
    def eliminar_departamento(self,id):
        try:
            departamento = self.session.query(Departamentos).get(id)
            if departamento:
                for sucursal in departamento.sucursales:
                    sucursal.departamentos.remove(departamento)
                
                # Ahora puedes eliminar el departamento
                self.session.delete(departamento)
                return True
            else:
                return False
        except Exception as e:
            return False
        
    def actualizar_departamento(self,
                                id, 
                                nombre,
                                descripcion = None):
        departamento = self.session.query(Departamentos).filter(id == id).first()
        if departamento:
            departamento.nombre = nombre
            departamento.descripcion = descripcion
            self.session.flush()
            return departamento, True
        else:
            return None, False
        
    def filtrar_nombre(self, texto):
        try:
            texto_busqueda = f"%{texto}%"
            resultado = self.session.query(Departamentos).filter(Departamentos.nombre.ilike(texto_busqueda)).all()
            if resultado:
                return resultado, True
            return None, False
        except Exception as e:
            return None, False