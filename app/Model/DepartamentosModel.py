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

                print(f"Departamento '{nombre}' agregado correctamente.")
                return nuevo_departamento, True

            except Exception as e:
                # Revertir los cambios en caso de error
                self.session.rollback()
                print(f"Error al agregar departamento: {e}")
                return None, False

    def obtener_todos(self):
        try:
            departamentos =  self.session.query(Departamentos).all()
            return departamentos
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