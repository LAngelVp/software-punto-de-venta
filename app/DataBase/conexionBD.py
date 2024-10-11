import sys
from sqlalchemy import create_engine, exc
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from app.Controller.MensajesAlertasController import *
# from Model.ModelsDataBase import Base
Base = declarative_base()
class Conexion_base_datos:
    def __init__(self):
        self.link_conexion = 'postgresql+psycopg2://DevelopmentTeam:Development@localhost:5432/DevelopmentTeam'
        self.conectar()

    def conectar(self):
        try:
            self.engine = create_engine(self.link_conexion)
            self.Session = sessionmaker(bind=self.engine)
            self.session = None
            Base.metadata.create_all(self.engine)
        except exc.SQLAlchemyError as e:
            mensaje = Mensaje().mensaje_critico('No se logró hacer conexión con la base de datos.')
            if mensaje == QMessageBox.Abort:
                sys.exit()
            elif mensaje == QMessageBox.Retry:
                self.conectar()
            elif mensaje == QMessageBox.Ignore:
                pass


    def abrir_sesion(self):
        if self.session is None:
            self.session = self.Session()
        return self.session
    

    def cerrar_sesion(self):
        if self.session is not None:
            self.session.close()
            self.session = None  

    def __enter__(self):
        self.abrir_sesion()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cerrar_sesion()
