from sqlite3 import IntegrityError
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .BaseDatosModel import Permisos, Roles

class PermisosModel:
    def __init__(self,session):
        self.session = session
        self.lista_permisos = [
                'administrador',
                'crearventa', 'eliminarventa', 'modificarventa',
                'crearcompra', 'eliminarcompra', 'modificarcompra',
                'crearproducto', 'eliminarproducto', 'modificarproducto',
                'crearempleado', 'eliminarempleado', 'modificarempleado',
                'crearproveedor', 'eliminarproveedor', 'modificarproveedor',
                'crearcliente', 'eliminarcliente', 'modificarcliente',
                'crearsucursal', 'eliminarsucursal', 'modificarsucursal',
                'creardepartamento', 'eliminardepartamento', 'modificardepartamento',
                'crearpuestos', 'eliminarpuesto', 'modificarpuesto',
                'creargrupopermisos', 'eliminargrupopermisos', 'modificargrupopermisos',
                'creartrasacciones', 'eliminartransacciones', 'modificartransacciones',
                'crearturnos', 'eliminarturnos', 'modificarturnos',
                'crearusuarios', 'eliminarusuarios', 'modificarusuarios'
        ]

    def crear_permiso(self):
        for permiso in self.lista_permisos:
            if not self.session.query(Permisos).filter_by(nombre = permiso).first():
                permiso_creado = Permisos(nombre = permiso.upper())
                self.session.add(permiso_creado)

    def buscar_por_nombre(self, nombre):
        if nombre is not None:
            permiso = self.session.query(Permisos).filter_by(nombre=nombre.upper()).first()
            if permiso:
                print(f"Permiso encontrado: {permiso.nombre}")
            else:
                print(f"No se encontró el permiso: {nombre}")
            return permiso
            
class RolesModel:
    def __init__(self, session):
        self.session = session
        self.rol_propietario = {
            'nombre' : 'administrador',
            'descripcion' :  'Administrador del sistema',
            'permisos' : 'administrador'
        }
    
    def crear_grupo_principal(self):
        try:
            rol_principal = self.session.query(Roles).filter_by(nombre = self.rol_propietario['nombre'].upper()).first()
            if not rol_principal:
                rol_creado = Roles(nombre = self.rol_propietario['nombre'].upper(),
                                descripcion = self.rol_propietario['descripcion'].upper(),
                                )
                permiso = PermisosModel(self.session).buscar_por_nombre(self.rol_propietario['permisos'].upper())
                if permiso:
                    rol_creado.permisos.append(permiso)
                self.session.add(rol_creado)
                print("rol creado")
            else:
                print("rol ya existe")
        except Exception as e:
            print(e)


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
                print('roles')
                return roles_todos, True
            else:
                print('no hay roles')
                return [], False
        except Exception as e:
            return None