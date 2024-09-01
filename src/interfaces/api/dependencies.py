from sqlalchemy.orm import Session
from fastapi import Depends
from repositories.sql_database.connection import get_db
from repositories.sql_database.user_repository import UserRepository
from repositories.sql_database.product_repository import ProductRepository
from core.use_cases.user_use_cases import UserUseCases
from core.use_cases.product_use_cases import ProductUseCases


# User
def get_user_repository(db: Session = Depends(get_db)) -> UserRepository:
    return UserRepository(db)

def get_user_use_cases(user_repo: UserRepository = Depends(get_user_repository)) -> UserUseCases:
    return UserUseCases(user_repo)


# Product
def get_product_repository(db: Session = Depends(get_db)) -> ProductRepository:
    return ProductRepository(db)

def get_product_use_cases(product_repo: ProductRepository = Depends(get_product_repository)) -> ProductUseCases:
    return ProductUseCases(product_repo)
