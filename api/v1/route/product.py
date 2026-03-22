from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from api.v1.db.session import get_db
from api.v1.schema.productschema import ProductCreate, ProductUpdate, ProductOut
from api.v1.service.productservice import ProductService

router = APIRouter(prefix="/products", tags=["Products"])

@router.get("/", response_model=list[ProductOut])
def list_prods(db: Session = Depends(get_db)):
    return ProductService.list_active(db)

@router.post("/", response_model=ProductOut)
def add_prod(data: ProductCreate, db: Session = Depends(get_db)):
    return ProductService.create(db, data)

@router.get("/{id}", response_model=ProductOut)
def get_prod(id: int, db: Session = Depends(get_db)):
    res = ProductService.get_by_id(db, id)
    if not res: raise HTTPException(status_code=404, detail="Product not found")
    return res

@router.patch("/{id}", response_model=ProductOut)
def up_prod(id: int, data: ProductUpdate, db: Session = Depends(get_db)):
    res = ProductService.update(db, id, data)
    if not res: raise HTTPException(status_code=404, detail="Product not found")
    return res

@router.delete("/{id}")
def del_prod(id: int, db: Session = Depends(get_db)):
    if not ProductService.soft_delete(db, id):
        raise HTTPException(status_code=404, detail="Product not found")
    return {"status": "soft-deleted"}
