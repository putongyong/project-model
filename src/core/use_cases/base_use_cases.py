from typing import List, TypeVar, Generic
from repositories.sql_database.base_repository import BaseRepository
from pydantic import BaseModel

T = TypeVar('T', bound=BaseModel)

class BaseUseCases(Generic[T]):
    def __init__(self, repo: BaseRepository[T]):
        self.repo = repo

    def create(self, entity: T) -> T:
        return self.repo.create(entity)

    def get_by_id(self, entity_id: int) -> T:
        return self.repo.get_by_id(entity_id)

    def list_all(self) -> List[T]:
        return self.repo.list_all()

    def update(self, entity_id: int, entity: T) -> T:
        return self.repo.update(entity_id, entity)

    def delete(self, entity_id: int) -> None:
        self.repo.delete(entity_id)
