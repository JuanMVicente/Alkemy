from sqlalchemy import declarative_base
from sqlalchemy import Column,String,Integer, create_engine

Base = declarative_base()

engine = create_engine()

class general(Base):
    __tablename__='consolidado_general'
    cod_localidad = Column(String(8))
    id_provincia = Column(String(2))
    id_departamento = Column(String(6))
    categoria = Column(String(60))
    provincia = Column(String(60))
    localidad = Column(String(50))
    nombre = Column(String(120))
    domicilio = Column(String(100))
    cp = Column(String(10))
    telefono = Column(String(30))
    mail = Column(String(100))
    web = Column(String(150))
    fecha = Column(String(10))


class totales_categoria(Base):
    __tablename__ = 'totales_categoria'
    categoria = Column(String(40))
    total = Column(Integer)
    fecha = Column(String(10))


class totales_fuente(Base):
    __tablename__ = 'totales_fuente'
    fuente = Column(String(100))
    total = Column(Integer)
    fecha = Column(String(10))


class totales_provincia_categoria(Base):
    __tablename__ = 'totales_provincia_categoria'
    provincia = Column(String(60))
    categoria = Column(String(60))
    total = Column(Integer)
    fecha = Column(String(10))


class info_cine(Base):
    __tablename__ = 'info_salas_cine'
    provincia = Column(String(60))
    pantallas = Column(Integer)
    butacas = Column(Integer)
    incaa = Column(Integer)
    fecha = Column(String(10))