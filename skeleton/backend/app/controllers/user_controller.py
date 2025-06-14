from sqlalchemy.orm import Session
from typing import List, Optional
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate, UserUpdate
from app.models.user import User

class UserController:
    def __init__(self, db: Session):
        self.repository = UserRepository(db)
    
    def create_user(self, user_data: UserCreate) -> User:
        return self.repository.create(obj_in=user_data)
    
    def get_user(self, user_id: int) -> Optional[User]:
        return self.repository.get(user_id)
    
    def get_users(self, skip: int = 0, limit: int = 100) -> List[User]:
        return self.repository.get_multi(skip=skip, limit=limit)
    
    def update_user(self, user_id: int, user_data: UserUpdate) -> Optional[User]:
        user = self.repository.get(user_id)
        if user:
            return self.repository.update(db_obj=user, obj_in=user_data)
        return None
    
    def delete_user(self, user_id: int) -> bool:
        return self.repository.delete(id=user_id) is not None
