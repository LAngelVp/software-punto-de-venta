from .BaseDatosModel import Representantes_proveedores

class RepresentanteProveedorModel:
    def __init__(self, session):
        self.session = session

    def agregar_representante(self, nombre, apellido_paterno, apellido_materno, correo, telefono, puesto):
        try:
            representante = self.session.query(Representantes_proveedores).filter(Representantes_proveedores.nombre == nombre, Representantes_proveedores.apellido_paterno == apellido_paterno, Representantes_proveedores.apellido_materno == apellido_materno).first()
            if representante:
                return representante, False
            else:
                nuevo_representante = Representantes_proveedores(
                    nombre =  nombre,
                    apellido_paterno = apellido_paterno,
                    apellido_materno = apellido_materno,
                    correo = correo,
                    telefono = telefono,
                    puesto = puesto
                )
                self.session.add(nuevo_representante)
                self.session.flush()
                return nuevo_representante, True
        except Exception as e:
            print(e)

    
    def actualizar_representante(self, id_representante, **kwargs):
        # Busca el representante en la base de datos usando su ID
        representante = self.session.query(Representantes_proveedores).filter(Representantes_proveedores.id == id_representante).first()
        
        if representante:
            # Itera sobre los argumentos keyword (kwargs) para actualizar los atributos
            try:
                for key, value in kwargs.items():
                    if hasattr(representante, key) and value is not None:
                        setattr(representante, key, value)
                
                print("Datos del representante actualizados con éxito.")
                return representante.id
            except Exception as e:
                # Manejo de excepciones para problemas durante la actualización
                self.session.rollback()
                print(f"Error al actualizar los datos del representante: {e}")
                return None
        else:
            print("Representante no encontrado")
            return None

        
    def eliminar_representante(self, id):
        try:
            representante = self.session(RepresentanteProveedorModel).filter(id == id).first()
            if representante:
                self.session.delete(representante)
            else:
                print("Proveedor no encontrado")
        except Exception as e:
            print(f"Error al eliminar el proveedor: {e}")

