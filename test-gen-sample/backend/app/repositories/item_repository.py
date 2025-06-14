from sqlalchemy.orm import Session
from app.repositories.base import BaseRepository
from app.models.item import Item
from app.schemas.item import ItemCreate, ItemUpdate

class ItemRepository(BaseRepository[Item, ItemCreate, ItemUpdate]):
    def __init__(self, db: Session):
        super().__init__(Item, db)
    
    def get_by_title(self, title: str):
        return self.db.query(Item).filter(Item.title == title).first()
