from sqlalchemy.orm import Session
from app.repositories.base import BaseRepository
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate

class UserRepository(BaseRepository[User, UserCreate, UserUpdate]):
    def __init__(self, db: Session):
        super().__init__(User, db)
    
    def get_by_email(self, email: str):
        return self.db.query(User).filter(User.email == email).first()
