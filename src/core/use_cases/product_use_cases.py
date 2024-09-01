from base_use_cases import BaseUseCases
from core.entities.product import Product
from repositories.product_repository import ProductRepository

class ProductUseCases(BaseUseCases[Product]):
    def __init__(self, repo: ProductRepository):
        super().__init__(repo)
