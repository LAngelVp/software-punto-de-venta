from sqlite3 import IntegrityError
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .BaseDatosModel import Puestos, Empleados

class PuestoModel:
    def __init__(self,session):
        self.session = session
        
    def crear_puesto(self, nombre,salario,horas_laborales,dias_laborales,descripcion_puesto, hora_entrada, hora_salida, departamento_id):
            puesto = self.session.query(Puestos).filter_by(nombre =  nombre).first()
            if  puesto:
                return puesto, False
            else:
                nuevo_puesto = Puestos(nombre = nombre, salario = salario, horas_laborales = horas_laborales,  dias_laborales = dias_laborales, descripcion_puesto = descripcion_puesto, hora_entrada = hora_entrada, hora_salida = hora_salida, departamento_id = departamento_id)

                self.session.add(nuevo_puesto)
                self.session.flush()
                return nuevo_puesto, True

    def actualizar(self, id_elemento, nombre,salario,horas_laborales,dias_laborales,descripcion_puesto, hora_entrada, hora_salida, departamento_id):
        puesto = self.session.query(Puestos).filter_by(id = id_elemento).first()
        if puesto is not None:
            puesto.nombre = nombre
            puesto.salario = salario
            puesto.horas_laborales = horas_laborales
            puesto.dias_laborales = dias_laborales
            puesto.descripcion_puesto = descripcion_puesto
            puesto.hora_entrada = hora_entrada
            puesto.hora_salida = hora_salida
            puesto.departamento_id = departamento_id
            return puesto, True
        return None, False
    
    def obtener_todos(self):
        try:
            puestos = self.session.query(Puestos).all()
            if puestos:
                print('roles')
                return puestos, True
            else:
                print('no hay roles')
                return [], False
        except Exception as e:
            return None
    
    def obtener_puesto_por_id(self, id_elemento):
        puesto = self.session.query(Puestos).filter(Puestos.id == id_elemento).first()
        if puesto is not None:
            return  puesto, True
        else:
            return None, False

    def eliminar_puesto(self, id):
        try:
            empleado_asociados = self.session.query(Empleados).filter(Empleados.puesto_id == id).all()
            if  empleado_asociados:
                for empleado in empleado_asociados:
                    empleado.puesto_id = None

            resultado = self.session.query(Puestos).filter(Puestos.id == id).delete()
            if resultado > 0:
                return True
        except Exception as e:
            print(e)
            return  False
