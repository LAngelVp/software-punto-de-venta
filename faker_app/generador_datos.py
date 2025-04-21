import pandas as pd
import random
from faker import Faker
from datetime import datetime, timedelta
from openpyxl import *

fake = Faker()
random.seed(42)

# Columnas esperadas
columnas_esperadas = [
    "Proveedor", "Código de Barras", "Nombre", "Categoría", "Marca", "Modelo", "Color",
    "Material", "Unidad de Medida", "Presentación", "Costo Inicial", "Costo Final",
    "Margen Porcentaje", "Precio Venta", "Existencia", "Existencia Min", "Existencia Max", "Peso",
    "Largo Dimensiones", "Alto Dimensiones", "Ancho Dimensiones",
    "Descripción", "Notas", "Fecha Vencimiento", "Fecha Fabricación", "Imagen"
]

# Función para generar dimensiones aleatorias
def generar_dimensiones():
    largo = round(random.uniform(10.0, 100.0), 2)
    alto = round(random.uniform(10.0, 100.0), 2)
    ancho = round(random.uniform(10.0, 100.0), 2)
    return largo, alto, ancho

# Generar los datos
data = []
for _ in range(10000):
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

# Crear DataFrame
df = pd.DataFrame(data)

df.to_excel("documento_datos.xlsx", index=False)
