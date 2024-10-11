from .BaseDatosModel import Departamentos

class DepartamentosModel:
    def __init__(self, session):
        self.session = session

    def agregar_departamento(self,
                            nombre,
                            descripcion = None,
                            sucursal_id=None):
        departamento = self.session.query(Departamentos).filter_by(nombre = nombre). first()
        if departamento:
            return  departamento.id
        else:
            try:
                # Crear una instancia del nuevo departamento
                nuevo_departamento = Departamentos(
                    nombre=nombre,
                    descripcion=descripcion,
                    sucursal_id=sucursal_id
                )

                # Agregar el nuevo departamento a la sesión
                self.session.add(nuevo_departamento)

                # Confirmar los cambios en la base de datos
                self.session.flush()

                print(f"Departamento '{nombre}' agregado correctamente.")
                return nuevo_departamento.id

            except Exception as e:
                # Revertir los cambios en caso de error
                self.session.rollback()
                print(f"Error al agregar departamento: {e}")
                return None


    def obtener_todos(self):
        try:
            departamentos =  self.session.query(Departamentos).all()
            return departamentos
        except Exception as e:
            return None
