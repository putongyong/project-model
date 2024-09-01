from fastapi import APIRouter, Depends
from core.entities.product import Product
from core.use_cases.product_use_cases import ProductUseCases
from interfaces.api.dependencies import get_product_use_cases
from base_crud_router import BaseCRUDRouter

def get_product_router(use_cases: ProductUseCases = Depends(get_product_use_cases)) -> APIRouter:
    return BaseCRUDRouter(Product, use_cases).router

router = get_product_router()
