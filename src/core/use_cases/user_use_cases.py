from base_use_cases import BaseUseCases
from core.entities.user import User
from repositories.user_repository import UserRepository

class UserUseCases(BaseUseCases[User]):
    def __init__(self, repo: UserRepository):
        super().__init__(repo)
