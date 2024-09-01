from fastapi import APIRouter, Depends
from core.entities.user import User
from core.use_cases.user_use_cases import UserUseCases
from interfaces.api.dependencies import get_user_use_cases
from base_crud_router import BaseCRUDRouter

def get_user_router(use_cases: UserUseCases = Depends(get_user_use_cases)) -> APIRouter:
    return BaseCRUDRouter(User, use_cases).router

router = get_user_router()
