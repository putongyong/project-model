from sqlalchemy.orm import Session
from core.entities.user import User
from base_repository import BaseRepository, Base
from sqlalchemy import Column, Integer, String

class UserModel(Base):
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    full_name = Column(String, nullable=True)

class UserRepository(BaseRepository[User, UserModel]):
    def __init__(self, db: Session):
        super().__init__(db, UserModel)
