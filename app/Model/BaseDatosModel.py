import uuid
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import (
    Column,
    Integer,
    String,
    Date,
    Text,
    Float,
    ForeignKey,
    Table,
    Index,
    BigInteger,
    LargeBinary,
    Boolean,
    CHAR,
    DateTime,
    Time,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers

configure_mappers()
Base = declarative_base()

# Tabla M:M entre Roles y Permisos
rol_permiso = Table(
    "rol_permisos",
    Base.metadata,
    Column("rol_id", BigInteger, ForeignKey("Roles.id"), primary_key=True),
    Column("permiso_id", BigInteger, ForeignKey("Permisos.id"), primary_key=True),
)

usuario_rol = Table(
    "usuario_rol",
    Base.metadata,
    Column("usuario_id", BigInteger, ForeignKey("Usuarios.id"), primary_key=True),
    Column("rol_id", BigInteger, ForeignKey("Roles.id"), primary_key=True),
)

sucursal_producto = Table(
    "sucursal_producto",
    Base.metadata,
    Column("sucursal_id", BigInteger, ForeignKey("Sucursales.id"), primary_key=True),
    Column("producto_id", Text, ForeignKey("Productos.codigo_upc"), primary_key=True),
)

producto_proveedor = Table(
    "producto_proveedor",
    Base.metadata,
    Column("producto_id", Text, ForeignKey("Productos.codigo_upc"), primary_key=True),
    Column("proveedor_id", Integer, ForeignKey("Proveedores.id"), primary_key=True),
)

proveedor_categoria = Table(
    "proveedor_categoria",
    Base.metadata,
    Column("proveedor_id", Integer, ForeignKey("Proveedores.id"), primary_key=True),
    Column(
        "categoria_id",
        Integer,
        ForeignKey("Categorias_proveedores.id"),
        primary_key=True,
    ),
)
departamento_sucursal = Table(
    "departamento_sucursal",
    Base.metadata,
    Column(
        "departamento_id", BigInteger, ForeignKey("Departamentos.id"), primary_key=True
    ),
    Column("sucursal_id", BigInteger, ForeignKey("Sucursales.id"), primary_key=True),
)


# Apartado de Permisos
class Permisos(Base):
    __tablename__ = "Permisos"
    id = Column(BigInteger, primary_key=True, autoincrement=True, nullable=False)
    nombre = Column(String(255), unique=True)
    roles = relationship(
        "Roles", secondary=rol_permiso, back_populates="permisos", 
        )


# Apartado de Roles
class Roles(Base):
    __tablename__ = "Roles"
    id = Column(BigInteger, primary_key=True, autoincrement=True, nullable=False)
    nombre = Column(String(150), unique=True)
    descripcion = Column(Text)
    permisos = relationship(
        "Permisos", secondary=rol_permiso, back_populates="roles", 
        )
    usuarios = relationship("Usuarios", back_populates="rol")


# Apartado de Usuarios
class Usuarios(Base):
    __tablename__ = "Usuarios"
    id = Column(BigInteger, primary_key=True, autoincrement=True, nullable=False)
    usuario = Column(String(100), unique=True, nullable=True)
    contraseña = Column(LargeBinary, nullable=True)
    fecha_creacion = Column(Date, nullable=False)
    fecha_actualizacion = Column(Date, nullable=True)
    rol_id = Column(Integer, ForeignKey("Roles.id"))
    rol = relationship("Roles", back_populates="usuarios")
    empleado = relationship("Empleados", uselist=False, back_populates="usuario")


# Apartado de Puestos
class Puestos(Base):
    __tablename__ = "Puestos"
    id = Column(BigInteger, primary_key=True, autoincrement=True, nullable=False)
    nombre = Column(String(150))
    salario = Column(Float)
    horas_laborales = Column(Float)
    dias_laborales = Column(Text)
    descripcion_puesto = Column(Text)
    hora_entrada = Column(Time)
    hora_salida = Column(Time)
    empleados = relationship("Empleados", back_populates="puesto")
    departamento_id = Column(
        BigInteger, ForeignKey("Departamentos.id")
    )  # Clave foránea hacia Departamentos
    departamento = relationship(
        "Departamentos", back_populates="puestos"
    )  # Relación inversa


# Apartado de Empleados
class Empleados(Base):
    __tablename__ = "Empleados"
    id = Column(BigInteger, primary_key=True, autoincrement=True, nullable=False)
    nombre = Column(String(100), nullable=False)
    apellido_paterno = Column(String(100), nullable=False)
    apellido_materno = Column(String(100), nullable=False)
    fecha_nacimiento = Column(Date, nullable=False)
    estado_civil = Column(String(30), nullable=False)
    curp = Column(String(18), nullable=False, unique=True)
    rfc = Column(String(13), nullable=False, unique=True)
    correo_electronico = Column(String(150), nullable=True, unique=True)
    numero_seguro_social = Column(String(13), nullable=False, unique=True)
    fecha_contratacion = Column(Date, nullable=False)
    fecha_despido = Column(Date, nullable=True)
    ciudad = Column(String(100), nullable=True)
    codigo_postal = Column(String(100), nullable=True)
    estado = Column(String(100), nullable=True)
    pais = Column(String(100), nullable=True)
    numero_telefonico = Column(String(20), nullable=True)
    direccion = Column(String(255), nullable=True)
    activo = Column(Boolean, nullable=False, default=True)
    hora_entrada = Column(Time, nullable=True)
    hora_salida = Column(Time, nullable=True)
    foto = Column(Text, nullable=True)
    puesto_id = Column(Integer, ForeignKey("Puestos.id"))
    puesto = relationship("Puestos", back_populates="empleados")
    usuario_id = Column(Integer, ForeignKey("Usuarios.id"))
    usuario = relationship("Usuarios", back_populates="empleado")
    ventas = relationship("Ventas", back_populates="empleado")
    turnos = relationship("Turnos", back_populates="empleado")
    departamento_id = Column(
        BigInteger, ForeignKey("Departamentos.id")
    )  # Clave foránea hacia Departamentos
    departamento = relationship(
        "Departamentos", back_populates="empleados"
    )  # Relación inversa


class Sucursales(Base):
    __tablename__ = "Sucursales"
    id = Column(
        Integer, primary_key=True, autoincrement=True, unique=True, nullable=False
    )
    nombre_sucursal = Column(String(100))
    codigo_postal = Column(String(10))
    ciudad = Column(String(100))
    estado = Column(String(100))
    pais = Column(String(50))
    num_telefono = Column(String(15))
    direccion = Column(Text)
    productos = relationship(
        "Productos", secondary=sucursal_producto, back_populates="sucursales", 
    )
    departamentos = relationship(
        "Departamentos", secondary=departamento_sucursal, back_populates="sucursales", 
    )  # Relación muchos a muchos con Departamentos


class Departamentos(Base):
    __tablename__ = "Departamentos"
    id = Column(BigInteger, primary_key=True, autoincrement=True, nullable=False)
    nombre = Column(String(150))
    descripcion = Column(Text)
    empleados = relationship(
        "Empleados", back_populates="departamento"
    )  # Relación con la tabla de empleados
    puestos = relationship(
        "Puestos", back_populates="departamento"
    )  # Relación uno a muchos con Puestos
    sucursales = relationship(
        "Sucursales", secondary=departamento_sucursal, back_populates="departamentos", 
    )  # Relación muchos a muchos con Sucursales


class Productos(Base):
    __tablename__ = "Productos"
    id = Column(
        Integer, primary_key=True, autoincrement=True, unique=True, nullable=False
    )
    codigo_upc = Column(Text, nullable=False, unique=True)
    nombre_producto = Column(String(100))
    descripcion_producto = Column(Text)
    presentacion = Column(Text)
    costo_inicial = Column(Float)
    costo_final = Column(Float)
    precio = Column(Float)
    existencia = Column(Float)
    existencia_minima = Column(Float)
    existencia_maxima = Column(Float)
    unidad_medida = Column(String(25))
    marca = Column(String(100))
    modelo = Column(Text)
    peso = Column(Float)
    dimensiones = Column(Text)
    color = Column(String(50))
    material = Column(String(255))
    fecha_fabricacion = Column(Date)
    fecha_vencimiento = Column(Date)
    imagen = Column(Text)
    notas = Column(Text)
    categoria = Column(String(55))
    sucursales = relationship(
        "Sucursales", secondary=sucursal_producto, back_populates="productos", 
    )
    proveedores = relationship(
        "Proveedores", secondary=producto_proveedor, back_populates="productos", 
    )
    detalles_compras = relationship("Detalles_compras", back_populates="producto")
    detalles_ventas = relationship("Detalles_ventas", back_populates="producto")


class Proveedores(Base):
    __tablename__ = "Proveedores"
    id = Column(
        Integer, primary_key=True, autoincrement=True, unique=True, nullable=False
    )
    nombre = Column(String(255))
    pais = Column(String(100))
    estado = Column(String(100))
    ciudad = Column(String(100))
    codigo_postal = Column(String(50))
    calles = Column(String(255))
    avenidas = Column(String(255))
    colonia = Column(String(255))
    direccion_adicional = Column(Text)
    rfc = Column(String(255))
    pagina_web = Column(Text)
    correo = Column(String(255))
    telefono = Column(String(15))
    productos = relationship(
        "Productos", secondary=producto_proveedor, back_populates="proveedores", 
    )
    representantes = relationship(
        "Representantes_proveedores", back_populates="proveedor", uselist=True
    )
    categorias = relationship(
        "Categorias_proveedores",
        secondary=proveedor_categoria,
        back_populates="proveedores",
        
    )
    compras = relationship("Compras", back_populates="proveedor")


class Representantes_proveedores(Base):
    __tablename__ = "Representantes_proveedores"
    id = Column(
        Integer, primary_key=True, autoincrement=True, unique=True, nullable=False
    )
    nombre = Column(String(255))
    apellido_paterno = Column(String(255))
    apellido_materno = Column(String(255))
    telefono = Column(String(15))
    correo = Column(String(255))
    puesto = Column(String(255))
    proveedor_id = Column(Integer, ForeignKey("Proveedores.id"))
    proveedor = relationship("Proveedores", back_populates="representantes")


class Categorias_proveedores(Base):
    __tablename__ = "Categorias_proveedores"
    id = Column(
        Integer, primary_key=True, autoincrement=True, unique=True, nullable=False
    )
    nombre = Column(String(100))
    descripcion = Column(Text)
    proveedores = relationship(
        "Proveedores", secondary=proveedor_categoria, back_populates="categorias", 
    )


class Ventas(Base):
    __tablename__ = "Ventas"
    id = Column(BigInteger, primary_key=True, autoincrement=True, nullable=False)
    fecha = Column(DateTime)
    total = Column(Float)
    estado = Column(String(100))
    comentarios = Column(Text)
    cliente_id = Column(Integer, ForeignKey("Clientes.id"), nullable=False)
    empleado_id = Column(Integer, ForeignKey("Empleados.id"), nullable=False)
    metodos_pagos_id = Column(Integer, ForeignKey("Metodos_pagos.id"), nullable=False)

    cliente = relationship("Clientes", back_populates="ventas")
    empleado = relationship("Empleados", back_populates="ventas")
    metodos_de_pago = relationship("Metodos_pagos", back_populates="ventas")
    detalles = relationship("Detalles_ventas", back_populates="venta")


class Clientes(Base):
    __tablename__ = "Clientes"
    id = Column(
        Integer, primary_key=True, autoincrement=True, unique=True, nullable=False
    )
    nombre = Column(String(255))
    correo = Column(String(255))
    rfc = Column(String(20))
    telefono = Column(String(15))
    pais = Column(String(100))
    estado = Column(String(100))
    ciudad = Column(String(255))
    avenidas = Column(String(255))
    calles = Column(String(255))
    codigo_postal = Column(String(20))
    direccion_adicional = Column(Text)
    entidad_legalizada = Column(Boolean)
    categoria_cliente_id = Column(Integer, ForeignKey("Categorias_de_clientes.id"))
    credito = Column(Boolean)
    estado_credito = Column(String(25))
    limite_credito = Column(Float)
    porcentaje_interes = Column(Float)
    fecha_ultimo_reporte = Column(DateTime)
    credito_disponible = Column(Float)
    credito_utilizado = Column(Float)
    tipo_cliente = Column(String(50))
    aplica_descuento = Column(Boolean)
    porcentaje_descuento = Column(Float)
    comentarios = Column(Text)

    ventas = relationship("Ventas", back_populates="cliente")
    areas_de_negocios_id = Column(
        Integer, ForeignKey("Areas_negocios.id"), nullable=False
    )  # Asegúrate de que esto sea correcto
    areas_de_negocios = relationship("Areas_negocios", back_populates="clientes")
    categoria = relationship("Categorias_de_clientes", back_populates="clientes")

    __mapper_args__ = {"polymorphic_on": tipo_cliente, "polymorphic_identity": "clientes"}

    


class Categorias_de_clientes(Base):
    __tablename__ = "Categorias_de_clientes"
    id = Column(
        Integer, primary_key=True, autoincrement=True, unique=True, nullable=False
    )
    nombre = Column(String(100))
    descripcion = Column(Text)
    clientes = relationship("Clientes", back_populates="categoria")


class Detalles_ventas(Base):
    __tablename__ = "Detalles_ventas"
    id = Column(BigInteger, primary_key=True, autoincrement=True, nullable=False)
    venta_id = Column(BigInteger, ForeignKey("Ventas.id"), nullable=False)
    producto_id = Column(Text, ForeignKey("Productos.codigo_upc"), nullable=False)
    cantidad = Column(Float)
    precio_unitario = Column(Float)
    subtotal = Column(Float)
    descuento = Column(Float)
    total = Column(Float)

    venta = relationship("Ventas", back_populates="detalles")
    producto = relationship("Productos", back_populates="detalles_ventas")


class Compras(Base):
    __tablename__ = "Compras"
    id = Column(
        Integer, primary_key=True, autoincrement=True, unique=True, nullable=False
    )
    proveedor_id = Column(Integer, ForeignKey("Proveedores.id"), nullable=False)
    fecha_compra = Column(DateTime)
    total_compra = Column(Float)
    metodos_pago_id = Column(Integer, ForeignKey("Metodos_pagos.id"), nullable=False)
    detalles = relationship("Detalles_compras", back_populates="compra")
    proveedor = relationship("Proveedores", back_populates="compras")
    metodos_de_pago = relationship("Metodos_pagos", back_populates="compras")


class Detalles_compras(Base):
    __tablename__ = "Detalles_compras"
    id = Column(
        Integer, primary_key=True, autoincrement=True, unique=True, nullable=False
    )
    compra_id = Column(Integer, ForeignKey("Compras.id"), nullable=False)
    producto_id = Column(Text, ForeignKey("Productos.codigo_upc"), nullable=False)
    cantidad = Column(Float)
    precio_unitario = Column(Float)
    subtotal = Column(Float)
    compra = relationship("Compras", back_populates="detalles")
    producto = relationship("Productos", back_populates="detalles_compras")


class Turnos(Base):
    __tablename__ = "Turnos"
    id = Column(
        Integer, primary_key=True, autoincrement=True, unique=True, nullable=False
    )
    empleado_id = Column(Integer, ForeignKey("Empleados.id"), nullable=False)
    fecha_turno = Column(DateTime)
    hora_inicio = Column(DateTime)
    hora_fin = Column(DateTime)
    empleado = relationship("Empleados", back_populates="turnos")
    transacciones = relationship("Transacciones", back_populates="turno")


class Transacciones(Base):
    __tablename__ = "Transacciones"
    id = Column(
        Integer, primary_key=True, autoincrement=True, unique=True, nullable=False
    )
    tipo = Column(String(100))
    monto = Column(Float)
    fecha = Column(DateTime)
    turno_id = Column(
        Integer, ForeignKey("Turnos.id"), nullable=False
    )  # Relación con Turnos

    # Relación con Turnos
    turno = relationship("Turnos", back_populates="transacciones")


class Areas_negocios(Base):
    __tablename__ = "Areas_negocios"
    id = Column(
        Integer, primary_key=True, autoincrement=True, unique=True, nullable=False
    )
    nombre = Column(String(100))
    descripcion = Column(Text)
    clientes = relationship("Clientes", back_populates="areas_de_negocios")


class Clientes_fisicos(Clientes):
    __tablename__ = "Clientes_fisicos"
    id = Column(Integer, ForeignKey("Clientes.id", ondelete='CASCADE'), primary_key=True)
    apellido_paterno = Column(String(255))
    apellido_materno = Column(String(255))
    curp = Column(String(18))
    fecha_nacimiento = Column(Date)
    num_identificacion = Column(String(20))
    ocupacion = Column(String(150))
    ingresos = Column(Float)
    estado_civil = Column(String(15))
    foto = Column(Text)

    __mapper_args__ = {
        "polymorphic_identity": "FISICO",
    }


class Clientes_morales(Clientes):
    __tablename__ = "Clientes_morales"
    id = Column(Integer, ForeignKey("Clientes.id", ondelete="CASCADE"), primary_key=True)
    razon_social = Column(String(255))
    fecha_constitucion = Column(Date)
    web =  Column(String(255))
    sector = Column(String(255))
    NIF = Column(String(20))
    representante_id = Column(Integer, ForeignKey("Representantes_clientes_morales.id"))
    representante = relationship(
        "Representantes_clientes_morales", back_populates="clientes_morales"
    )

    __mapper_args__ = {
        "polymorphic_identity": "MORAL",
    }


class Metodos_pagos(Base):
    __tablename__ = "Metodos_pagos"
    id = Column(
        Integer, primary_key=True, autoincrement=True, unique=True, nullable=False
    )
    nombre = Column(String(100))
    compras = relationship("Compras", back_populates="metodos_de_pago")
    ventas = relationship("Ventas", back_populates="metodos_de_pago")


class Representantes_clientes_morales(Base):
    __tablename__ = "Representantes_clientes_morales"
    id = Column(
        Integer, primary_key=True, autoincrement=True, unique=True, nullable=False
    )
    nombre = Column(String(100))
    telefono = Column(String(20))
    correo = Column(String(100))
    puesto = Column(String(100))
    clientes_morales = relationship("Clientes_morales", back_populates="representante")


# Índices para mejorar el rendimiento en búsquedas
Index("idx_usuario", Usuarios.usuario)
Index("idx_curp", Empleados.curp)
Index("idx_rfc", Empleados.rfc)
