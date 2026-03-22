import sys
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Add current dir to path for imports
sys.path.append(os.getcwd())

from api.v1.db.session import Base, SQLALCHEMY_DATABASE_URL
from api.v1.model.productmodel import Product

def init_db():
    # 1. Create Engine & Tables
    engine = create_engine(SQLALCHEMY_DATABASE_URL)
    Base.metadata.create_all(bind=engine)
    
    # 2. Seed Data
    SessionLocal = sessionmaker(bind=engine)
    db = SessionLocal()
    
    try:
        if db.query(Product).count() == 0:
            seeds = [
                Product(name="UV-Speedy Mouse", price=45.00),
                Product(name="Mechanical Keyboard", price=120.00),
                Product(name="Python Guidebook", price=30.00, is_deleted=True)
            ]
            db.add_all(seeds)
            db.commit()
            print("✅ Database tables created and seeded!")
        else:
            print("ℹ️ Database already has data. Skipping seed.")
    finally:
        db.close()

if __name__ == "__main__":
    init_db()