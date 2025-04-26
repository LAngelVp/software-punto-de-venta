from sqlalchemy import create_engine
import pandas as pd
import csv
import random
from faker import Faker
from datetime import datetime, timedelta
from openpyxl import Workbook

fake = Faker('es_MX')
random.seed(42)

class Generador_tablas:
    def __init__(self):
        self.cantidad_registros = 10000
        self.conexion = 'postgresql+psycopg2://Dev_Rous:Dev_Rous73@localhost:5432/Dev_Rous'
        self.engine = create_engine(self.conexion)
        
    def creacion_de_productos(self):
        columnas_esperadas = [
            "Proveedor", "Código de Barras", "Nombre", "Categoría", "Marca", "Modelo", "Color",
            "Material", "Unidad de Medida", "Presentación", "Costo Inicial", "Costo Final",
            "Margen Porcentaje", "Precio Venta", "Existencia", "Existencia Min", "Existencia Max", "Peso",
            "Largo Dimensiones", "Alto Dimensiones", "Ancho Dimensiones",
            "Descripción", "Notas", "Fecha Vencimiento", "Fecha Fabricación", "Imagen"
        ]

        def generar_dimensiones():
            largo = round(random.uniform(10.0, 100.0), 2)
            alto = round(random.uniform(10.0, 100.0), 2)
            ancho = round(random.uniform(10.0, 100.0), 2)
            return largo, alto, ancho

        data = []
        for _ in range(self.cantidad_registros):
            largo, alto, ancho = generar_dimensiones()
            costo_inicial = round(random.uniform(10, 100), 2)
            margen = round(random.uniform(5, 50), 2)
            costo_final = round(costo_inicial * (1 + margen / 100), 2)
            precio_venta = round(costo_final * 1.2, 2)

            producto = {
                "Proveedor": fake.company(),
                "Código de Barras": fake.unique.ean(length=13),
                "Nombre": fake.word().capitalize() + " " + fake.word().capitalize(),
                "Categoría": fake.word().capitalize(),
                "Marca": fake.company(),
                "Modelo": fake.bothify(text='??-####'),
                "Color": fake.color_name(),
                "Material": fake.word().capitalize(),
                "Unidad de Medida": random.choice(["Unidad", "Caja", "Litro", "Metro"]),
                "Presentación": random.choice(["Botella", "Caja", "Bolsa", "Paquete"]),
                "Costo Inicial": costo_inicial,
                "Costo Final": costo_final,
                "Margen Porcentaje": f"{margen}%",
                "Precio Venta": precio_venta,
                "Existencia": round(random.uniform(0, 500), 2),
                "Existencia Min": round(random.uniform(0, 50), 2),
                "Existencia Max": round(random.uniform(100, 1000), 2),
                "Peso": round(random.uniform(0.1, 10.0), 2),
                "Largo Dimensiones": largo,
                "Alto Dimensiones": alto,
                "Ancho Dimensiones": ancho,
                "Descripción": fake.text(max_nb_chars=100),
                "Notas": fake.sentence(nb_words=6),
                "Fecha Vencimiento": fake.date_between(start_date='today', end_date='+2y'),
                "Fecha Fabricación": fake.date_between(start_date='-2y', end_date='today'),
                "Imagen": fake.image_url()
            }
            data.append(producto)

        df = pd.DataFrame(data)
        df.to_excel("documento_datos.xlsx", index=False)
        print(f"✅ Se generó documento_datos.xlsx con {self.cantidad_registros} productos.")

    def creacion_empleados(self):
        def generar_empleado():
            genero = random.choice(['Masculino', 'Femenino'])
            fecha_despido = None
            if random.random() < 0.2:
                fecha_despido = fake.date_between(start_date='-5y', end_date='today')

            return {
                "nombre": fake.first_name_male() if genero == "Masculino" else fake.first_name_female(),
                "apellido_paterno": fake.last_name(),
                "apellido_materno": fake.last_name(),
                "genero": genero,
                "fecha_nacimiento": fake.date_of_birth(minimum_age=18, maximum_age=60).strftime("%Y-%m-%d"),
                "estado_civil": random.choice(['Soltero', 'Casado', 'Divorciado', 'Viudo']),
                "curp": fake.unique.bothify(text='????######??????', letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ'),
                "rfc": fake.unique.bothify(text='????######???', letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ'),
                "nivel_academico": random.choice(['Licenciatura', 'Maestría', 'Doctorado', 'Técnico', 'Bachillerato']),
                "carrera": fake.job(),
                "correo_electronico": fake.unique.email(),
                "numero_seguro_social": fake.unique.numerify(text='###########'),
                "fecha_contratacion": fake.date_between(start_date='-10y', end_date='today').strftime("%Y-%m-%d"),
                "fecha_despido": fecha_despido.strftime("%Y-%m-%d") if fecha_despido else None,
                "ciudad": fake.city(),
                "codigo_postal": fake.postcode()[:5],
                "estado": fake.state(),
                "pais": "México",
                "numero_telefonico": fake.numerify(text='##########'),
                "nombre_contacto": fake.name(),
                "contacto_emergencia": fake.numerify(text='##########'),
                "parentesco_contacto": random.choice(['Padre', 'Madre', 'Hermano', 'Esposo', 'Amigo']),
                "calles": fake.street_name(),
                "avenidas": fake.street_name(),
                "colonia": fake.city_suffix(),
                "num_interior": fake.building_number() if random.random() > 0.3 else None,
                "num_exterior": fake.building_number(),
                "direccion_adicional": fake.address(),
                "activo": random.choice([True, False]),
                "foto": None,
                "puesto_id": None,
                "usuario_id": None,
                "departamento_id": None,
                "sucursal_id": None,
            }

        empleados = [generar_empleado() for _ in range(self.cantidad_registros)]
        df_empleados = pd.DataFrame(empleados)
        columnas_bol=df_empleados.select_dtypes(include=bool).columns.tolist()
        df_empleados[columnas_bol] = df_empleados[columnas_bol].astype(str)
        # df_empleados.to_csv("empleados_fake.csv",sep=';', index=False, encoding="utf-8-sig", quoting=csv.QUOTE_ALL)
        df_empleados.to_sql('Empleados', con=self.engine, if_exists='append', index=False)
        print(f"✅ Se generó empleados_fake.xlsx con {self.cantidad_registros} empleados.")


# Generador_tablas().creacion_empleados()