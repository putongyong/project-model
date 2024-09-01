from typing import List, Optional, Type, TypeVar, Generic
from sqlalchemy.orm import Session
from pydantic import BaseModel
from sqlalchemy.ext.declarative import as_declarative, declared_attr

T = TypeVar('T', bound=BaseModel)
M = TypeVar('M', bound=Type)

@as_declarative()
class Base:
    id: int
    __name__: str

    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()

class BaseRepository(Generic[T, M]):
    def __init__(self, db: Session, model: Type[M]):
        self.db = db
        self.model = model

    def create(self, entity: T) -> T:
        db_entity = self.model(**entity.model_dump())
        self.db.add(db_entity)
        self.db.commit()
        self.db.refresh(db_entity)
        return T.from_orm(db_entity)

    def get_by_id(self, entity_id: int) -> Optional[T]:
        db_entity = self.db.query(self.model).filter(self.model.id == entity_id).first()
        if db_entity:
            return T.from_orm(db_entity)
        return None

    def list_all(self) -> List[T]:
        entities = self.db.query(self.model).all()
        return [T.from_orm(entity) for entity in entities]

    def update(self, entity_id: int, entity: T) -> T:
        db_entity = self.db.query(self.model).filter(self.model.id == entity_id).first()
        if db_entity:
            for key, value in entity.dict(exclude_unset=True).items():
                setattr(db_entity, key, value)
            self.db.commit()
            self.db.refresh(db_entity)
            return T.from_orm(db_entity)
        else:
            raise ValueError(f"{self.model.__name__} not found")

    def delete(self, entity_id: int) -> None:
        db_entity = self.db.query(self.model).filter(self.model.id == entity_id).first()
        if db_entity:
            self.db.delete(db_entity)
            self.db.commit()
        else:
            raise ValueError(f"{self.model.__name__} not found")
