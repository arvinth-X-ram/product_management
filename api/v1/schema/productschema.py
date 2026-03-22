from pydantic import BaseModel
from typing import Optional

class ProductBase(BaseModel):
    name: str
    price: float

class ProductCreate(ProductBase):
    pass

class ProductUpdate(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None

class ProductOut(ProductBase):
    id: int
    is_deleted: bool
    class Config:
        from_attributes = True
