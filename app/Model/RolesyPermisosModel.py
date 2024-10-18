from sqlite3 import IntegrityError
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .BaseDatosModel import Permisos, Roles
class PermisosModel:
    def __init__(self,session):
        self.session = session

    def crear_permiso(self, nombre, descripcion = None):
            permiso_existente = self.session.query(Permisos).filter_by(nombre=nombre).first()
            if permiso_existente:
                return permiso_existente.id
            else:
                nuevo_permiso = Permisos(
                    nombre=nombre,
                    descripcion = descripcion)
                self.session.add(nuevo_permiso)
                self.session.flush()
                return nuevo_permiso.id

class RolesModel:
    def __init__(self, session):
        self.session = session

    def crear_Rol(self, nombre, descripcion, permisos=None):
        # Verificar si el rol ya existe
        rol_existente = self.session.query(Roles).filter_by(nombre=nombre).first()
        if rol_existente:
            print(f"El rol '{nombre}' ya existe.")
            return rol_existente.id

        # Crear el nuevo rol
        nuevo_rol = Roles(
            nombre=nombre,
            descripcion = descripcion,
            )
        self.session.add(nuevo_rol)

        # Agregar los permisos si se proporcionan
        if permisos:
            conjunto_permisos = self.session.query(Permisos).filter(Permisos.id.in_(permisos)).all()
            nuevo_rol.permisos.extend(conjunto_permisos)

        # No hacer commit aquí, ya que será manejado externamente
        try:
            self.session.flush()  # Asegura que el ID del rol esté disponible sin hacer commit
            return nuevo_rol.id
        except IntegrityError as e:
            print(f"Error al crear el rol: {e}")
            return None

    def obtener_todos(self):
        try:
            roles_todos = self.session.query(Roles).all()
            if roles_todos:
                return roles_todos, True
            else:
                return [], False
        except Exception as e:
            return None