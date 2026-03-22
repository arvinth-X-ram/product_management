from sqlalchemy.orm import Session
from api.v1.model.productmodel import Product
from api.v1.schema.productschema import ProductCreate, ProductUpdate

class ProductService:
    @staticmethod
    def list_active(db: Session):
        return db.query(Product).filter(Product.is_deleted == False).all()

    @staticmethod
    def get_by_id(db: Session, p_id: int):
        return db.query(Product).filter(Product.id == p_id, Product.is_deleted == False).first()

    @staticmethod
    def create(db: Session, data: ProductCreate):
        new_p = Product(**data.model_dump())
        db.add(new_p)
        db.commit()
        db.refresh(new_p)
        return new_p

    @staticmethod
    def update(db: Session, p_id: int, data: ProductUpdate):
        p = ProductService.get_by_id(db, p_id)
        if p:
            for k, v in data.model_dump(exclude_unset=True).items():
                setattr(p, k, v)
            db.commit()
            db.refresh(p)
        return p

    @staticmethod
    def soft_delete(db: Session, p_id: int):
        p = ProductService.get_by_id(db, p_id)
        if p:
            p.is_deleted = True
            db.commit()
            return True
        return False
