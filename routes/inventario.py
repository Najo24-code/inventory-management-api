from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import Categoria, Producto
from schemas import CategoriaBase, CategoriaCreate, CategoriaResponse, ProductoBase
from auth import User, get_current_user

router = APIRouter()

@router.get("/categorias/", response_model=list[CategoriaResponse])
def read_categorias(db: Session = Depends(get_db)):
    return db.query(Categoria).all()

@router.get("/categorias/{categoria_id}", response_model=CategoriaResponse)
def read_categoria(categoria_id: int, db: Session = Depends(get_db)):
    db_categoria = db.query(Categoria).filter(Categoria.id == categoria_id).first()
    if db_categoria is None:
        raise HTTPException(status_code=404, detail="Categoria no encontrada")
    return db_categoria

@router.post("/categorias/", response_model=CategoriaResponse)
def create_categoria(categoria: CategoriaCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_categoria = Categoria(nombre=categoria.nombre, descripcion=categoria.descripcion)
    db.add(db_categoria)
    db.commit()
    db.refresh(db_categoria)
    return db_categoria

@router.delete("/categorias/{categoria_id}")
def delete_categoria(categoria_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_categoria = db.query(Categoria).filter(Categoria.id == categoria_id).first()
    if db_categoria is None:
        raise HTTPException(status_code=404, detail="Categoria no encontrada")
    db.delete(db_categoria)
    db.commit()
    return {"mensaje": "Categoria eliminada"}

@router.get("/productos/", response_model=list[ProductoBase])
def read_productos(db: Session = Depends(get_db)):
    return db.query(Producto).all()

@router.get("/productos/{producto_id}", response_model=ProductoBase)
def read_producto(producto_id: int, db: Session = Depends(get_db)):
    db_producto = db.query(Producto).filter(Producto.id == producto_id).first()
    if db_producto is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return db_producto

@router.post("/productos/", response_model=ProductoBase)
def create_producto(producto: ProductoBase, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_producto = Producto(nombre=producto.nombre, descripcion=producto.descripcion, precio=producto.precio, cantidad_en_stock=producto.cantidad_en_stock, categoria_id=producto.categoria_id)
    db.add(db_producto)
    db.commit()
    db.refresh(db_producto)
    return db_producto

@router.delete("/productos/{producto_id}")
def delete_producto(producto_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_producto = db.query(Producto).filter(Producto.id == producto_id).first()
    if db_producto is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    db.delete(db_producto)
    db.commit()
    return {"mensaje": "Producto eliminado"}