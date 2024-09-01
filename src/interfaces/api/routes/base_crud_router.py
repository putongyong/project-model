from fastapi import APIRouter, Depends, HTTPException
from typing import Generic, Type, List, TypeVar
from pydantic import BaseModel
from core.use_cases.base_use_cases import BaseUseCases

T = TypeVar('T', bound=BaseModel)

class BaseCRUDRouter(Generic[T]):
    def __init__(self, entity: Type[T], use_cases: BaseUseCases[T]):
        self.entity = entity
        self.use_cases = use_cases
        self.router = APIRouter()

        @self.router.post("/", response_model=self.entity)
        def create_item(item: self.entity):
            return self.use_cases.create(item)

        @self.router.get("/{item_id}", response_model=self.entity)
        def get_item(item_id: int):
            item = self.use_cases.get_by_id(item_id)
            if not item:
                raise HTTPException(status_code=404, detail=f"{self.entity.__name__} not found")
            return item

        @self.router.get("/", response_model=List[self.entity])
        def list_items():
            return self.use_cases.list_all()

        @self.router.put("/{item_id}", response_model=self.entity)
        def update_item(item_id: int, item: self.entity):
            return self.use_cases.update(item_id, item)

        @self.router.delete("/{item_id}", status_code=204)
        def delete_item(item_id: int):
            self.use_cases.delete(item_id)
