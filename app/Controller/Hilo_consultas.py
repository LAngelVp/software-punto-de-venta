import threading
import pandas as pd
from PySide6.QtCore import QObject, Signal
from ..DataBase.conexionBD import Conexion_base_datos

class Consultas_segundo_plano(QObject):
    terminado = Signal()
    resultado = Signal(object, bool, str)
    error = Signal(str)
    resultado_productos_masivos_excel = Signal(object, object)

    def ejecutar_hilo(self, funcion, *args, **kwargs):
        # Función de tarea
        def tarea():
            try:
                with Conexion_base_datos() as db:
                    session = db.abrir_sesion()
                    data, estado = funcion(session, *args, **kwargs)
                    if estado:
                        self.resultado.emit(data, estado, "")
                    else:
                        self.resultado.emit(None, estado, "No se logro la operación")
            except Exception as e:
                self.error.emit(str(e))
            finally:
                self.terminado.emit()

        hilo_base_de_datos = threading.Thread(target=tarea, daemon=True)
        hilo_base_de_datos.start()

    def lecturas_y_procesamiento(self, documento, productos_existentes):
        def run():
            try:
                columnas_esperadas = [
                    "Proveedor", "Código de Barras", "Nombre", "Categoría", "Marca", "Modelo", "Color",
                    "Material", "Unidad de Medida", "Presentación", "Costo Inicial","Costo Final", "Margen Porcentaje", "Precio Venta",
                    "Existencia", "Existencia Min", "Existencia Max", "Peso",
                    "Largo Dimensiones", "Alto Dimensiones", "Ancho Dimensiones",
                    "Descripción", "Notas", "Fecha Vencimiento", "Fecha Fabricación", "Imagen"
                ]

                df = pd.read_excel(documento, na_filter=False)

                columnas_faltantes = [col for col in columnas_esperadas if col not in df.columns]
                if columnas_faltantes:
                    raise ValueError(f"Faltan columnas: {', '.join(columnas_faltantes)}")

                df = df[columnas_esperadas]
                productos_nuevos = []
                duplicados = []

                codigos_existentes = set(str(p["codigo_barras"]).strip() for p in productos_existentes)

                for _, row in df.iterrows():
                    codigo = str(row["Código de Barras"]).strip()
                    if codigo in codigos_existentes:
                        duplicados.append(codigo)
                        continue

                    producto = {
                        "proveedor": str(row["Proveedor"]).strip(),
                        "codigo_barras": codigo,
                        "nombre": str(row["Nombre"]).strip(),
                        "categoria": str(row["Categoría"]).strip(),
                        "marca": str(row["Marca"]).strip(),
                        "modelo": str(row["Modelo"]).strip(),
                        "color": str(row["Color"]).strip(),
                        "material": str(row["Material"]).strip(),
                        "unidad_medida": str(row["Unidad de Medida"]).strip(),
                        "presentacion": str(row["Presentación"]).strip(),
                        "costo_inicial": float(row["Costo Inicial"]),
                        "costo_final": float(row["Costo Final"]),
                        "margen_porcentaje": int(row["Margen Porcentaje"]),
                        "precio_venta": float(row["Precio Venta"]),
                        "existencia": float(row["Existencia"]),
                        "existencia_min": float(row["Existencia Min"]),
                        "existencia_max": float(row["Existencia Max"]),
                        "peso": float(row["Peso"]),
                        "largo_dimensiones": float(row["Largo Dimensiones"]),
                        "alto_dimensiones": float(row["Alto Dimensiones"]),
                        "ancho_dimensiones": float(row["Ancho Dimensiones"]),
                        "descripcion": str(row["Descripción"]).strip(),
                        "notas": row["Notas"],
                        "fecha_vencimiento": row["Fecha Vencimiento"],
                        "fecha_fabricacion": row["Fecha Fabricación"],
                        "imagen": str(row["Imagen"]).strip()
                    }
                    productos_nuevos.append(producto)

                self.resultado_productos_masivos_excel.emit(productos_nuevos, duplicados)
            except Exception as e:
                self.error.emit(str(e))
            finally:
                self.terminado.emit()

        threading.Thread(target=run, daemon=True).start()