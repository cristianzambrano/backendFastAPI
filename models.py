from sqlalchemy import Column, String, Float, Integer
from database import Base

class Producto(Base):
    __tablename__ = "productos"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre = Column(String(255), nullable=False)
    categoria = Column(String(100), nullable=False)
    valor = Column(Float, nullable=False)
