from sqlalchemy import Column, Integer, String, Text, ForeignKey, TIMESTAMP, text
from sqlalchemy.orm import relationship
from .database import Base

class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)

class Proyecto(Base):
    __tablename__ = "proyecto"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(255), nullable=False)
    descripcion = Column(Text)

class Bitacora(Base):
    __tablename__ = "bitacora"
    id = Column(Integer, primary_key=True, index=True)
    id_usuario = Column(Integer, ForeignKey("usuarios.id"))
    id_proyecto = Column(Integer, ForeignKey("proyecto.id"))
    actividad = Column(Text)
    fecha = Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'))

class Log(Base):
    __tablename__ = "log"
    id = Column(Integer, primary_key=True, index=True)
    id_usuario = Column(Integer, ForeignKey("usuarios.id"))
    fecha = Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'))
    accion = Column(Text)

class Gasolinera(Base):
    __tablename__ = "gasolineras"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(255), nullable=False)
    direccion = Column(String(255), nullable=False)

class Rol(Base):
    __tablename__ = "rol"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(255), nullable=False)

class Vehiculo(Base):
    __tablename__ = "vehiculos"
    id = Column(Integer, primary_key=True, index=True)
    modelo = Column(String(255), nullable=False)
    marca = Column(String(255), nullable=False)
    year = Column(Integer, nullable=False)
