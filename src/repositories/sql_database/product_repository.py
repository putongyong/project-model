from sqlalchemy.orm import Session
from core.entities.product import Product
from base_repository import BaseRepository, Base
from sqlalchemy import Column, Integer, String, Float

class ProductModel(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    description = Column(String, nullable=True)
    price = Column(Float, nullable=False)

class ProductRepository(BaseRepository[Product, ProductModel]):
    def __init__(self, db: Session):
        super().__init__(db, ProductModel)
