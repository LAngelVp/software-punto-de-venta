from sqlite3 import IntegrityError
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, outerjoin
from .BaseDatosModel import Permisos, Roles, rol_permiso

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
    @property
    def crear_permisos_principal(self):
        # Verificar si los permisos ya existen en la base de datos
        permisos_existentes = self.session.query(Permisos.nombre).filter(Permisos.nombre.in_([p.upper() for p in self.lista_permisos])).all()
        permisos_existentes = set([p[0] for p in permisos_existentes])  # Convertir a set para eficiencia en las búsquedas

        # Añadir solo los permisos que no existen
        for permiso in self.lista_permisos:
            permiso_upper = permiso.upper()
            if permiso_upper not in permisos_existentes:
                permiso_creado = Permisos(nombre=permiso_upper)
                self.session.add(permiso_creado)

    def buscar_por_nombre(self, nombre):
        if nombre is not None:
            permiso = self.session.query(Permisos).filter_by(nombre=nombre.upper()).first()
            if permiso:
                return permiso
        return None
            
class RolesModel:
    def __init__(self, session):
        self.session = session
        self.rol_propietario = {
            'nombre' : 'administrador',
            'descripcion' :  'Administrador del sistema',
            'permisos' : 'administrador'
        }
    @property
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
        except Exception as e:
            pass

    def crear_Rol(self, nombre, descripcion = None, permisos=None):
        rol_existente = self.session.query(Roles).filter_by(nombre=nombre).first()
        if rol_existente:
            return rol_existente.id, True  # Devolver también el estado de éxito

        # Crear el nuevo rol
        nuevo_rol = Roles(
            nombre=nombre,
            descripcion=descripcion,
        )
        self.session.add(nuevo_rol)

        # Agregar los permisos si se proporcionan
        if permisos:
            # Asegúrate de que los permisos sean nombres válidos en la base de datos
            conjunto_permisos = self.session.query(Permisos).filter(Permisos.nombre.in_(permisos)).all()
            print(f"Permisos encontrados en la base de datos: {[permiso.nombre for permiso in conjunto_permisos]}")
            if conjunto_permisos:
                nuevo_rol.permisos.extend(conjunto_permisos)

        # Confirmar los cambios en la base de datos
        try:
            self.session.commit()  # Asegura que los cambios sean confirmados
            return nuevo_rol, True  # Devuelve el rol creado y el estado de éxito
        except IntegrityError as e:
            self.session.rollback()  # Revierte la transacción si ocurre un error
            return None, False  # Devolver None si hubo un error
        except Exception as e:
            self.session.rollback()  # Revierte la transacción en caso de otros errores
            print(f"Error al crear rol: {e}")  # Puedes loggear el error para diagnóstico
            return None, False

    def obtener_todos(self):
        try:
            roles_todos = self.session.query(Roles).all()
            if roles_todos:
                return roles_todos, True
            else:
                return [], False
        except Exception as e:
            return None
    
    def todos_roles_con_permisos(self):
        roles = self.session.query(Roles, Permisos).outerjoin(rol_permiso, rol_permiso.c.rol_id == Roles.id).outerjoin(Permisos, Permisos.id == rol_permiso.c.permiso_id).all()
        if not roles:
            return [], False
        return roles, True
    
    def eliminar_rol_con_permisos(self, id):
        rol = self.session.query(Roles).filter(Roles.id == id).first()
        if rol is None:
            return False
        self.session.delete(rol)
        return True
        