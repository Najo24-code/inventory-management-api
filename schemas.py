from pydantic import BaseModel
from datetime import date
from typing import Optional, List

class CategoriaBase(BaseModel):
    nombre: str
    descripcion: Optional[str]

class CategoriaCreate(CategoriaBase):
    pass

class CategoriaResponse(CategoriaBase):
    id: int

    class Config:
        from_attributes = True

class ProductoBase(BaseModel):
    nombre: str
    descripcion: Optional[str]
    precio: float
    cantidad_en_stock: int
    categoria_id: int

class ProductoCreate(ProductoBase):
    pass

class ProductoResponse(ProductoBase):
    id: int
    categoria: CategoriaResponse

    class Config:
        from_attributes = True

class MovimientoBase(BaseModel):
    fecha: date
    cantidad: int
    tipo: str  # entrada, salida, ajuste
    producto_id: int

class MovimientoCreate(MovimientoBase):
    pass

class MovimientoResponse(MovimientoBase):
    id: int
    producto: ProductoResponse

    class Config:
        from_attributes = True