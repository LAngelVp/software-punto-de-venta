from sqlite3 import IntegrityError
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .BaseDatosModel import Puestos

class PuestoModel:
    def __init__(self,session):
        self.session = session
        
    def crear_puesto(self, nombre,salario,horas_laborales,dias_laborales,descripcion_puesto, hora_entrada, hora_salida, departamento_id):
            puesto = self.session.query(Puestos).filter_by(nombre =  nombre).first()
            if  puesto:
                return puesto.id
            else:
                nuevo_puesto = Puestos(nombre = nombre, salario = salario, horas_laborales = horas_laborales,  dias_laborales = dias_laborales, descripcion_puesto = descripcion_puesto, hora_entrada = hora_entrada, hora_salida = hora_salida, departamento_id = departamento_id)

                self.session.add(nuevo_puesto)
                self.session.flush()
                return nuevo_puesto.id


        