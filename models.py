from database import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Float, Text
from sqlalchemy.orm import relationship
from auth import User

class Categoria(Base):
    __tablename__ = 'categorias'
    id = Column(Integer, primary_key=True)
    nombre = Column(String, unique=True)
    descripcion = Column(Text)

    productos = relationship('Producto', back_populates='categoria')

class Producto(Base):
    __tablename__ = 'productos'
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    descripcion = Column(Text)
    precio = Column(Float)
    cantidad_en_stock = Column(Integer)
    categoria_id = Column(Integer, ForeignKey('categorias.id'))

    categoria = relationship('Categoria', back_populates='productos')
    movimientos = relationship('MovimientoInventario', back_populates='producto')
    usuario_id = Column(Integer, ForeignKey('users.id'))
    usuario = relationship('User', back_populates='productos')

class MovimientoInventario(Base):
    __tablename__ = 'movimientos_inventario'
    id = Column(Integer, primary_key=True)
    fecha = Column(String)
    cantidad = Column(Integer)
    tipo = Column(String)  # entrada, salida, ajuste
    producto_id = Column(Integer, ForeignKey('productos.id'))

    producto = relationship('Producto', back_populates='movimientos')