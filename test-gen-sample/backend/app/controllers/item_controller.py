from sqlalchemy.orm import Session
from typing import List, Optional
from app.repositories.item_repository import ItemRepository
from app.schemas.item import ItemCreate, ItemUpdate
from app.models.item import Item

class ItemController:
    def __init__(self, db: Session):
        self.repository = ItemRepository(db)
    
    def create_item(self, item_data: ItemCreate) -> Item:
        return self.repository.create(obj_in=item_data)
    
    def get_item(self, item_id: int) -> Optional[Item]:
        return self.repository.get(item_id)
    
    def get_items(self, skip: int = 0, limit: int = 100) -> List[Item]:
        return self.repository.get_multi(skip=skip, limit=limit)
    
    def update_item(self, item_id: int, item_data: ItemUpdate) -> Optional[Item]:
        item = self.repository.get(item_id)
        if item:
            return self.repository.update(db_obj=item, obj_in=item_data)
        return None
    
    def delete_item(self, item_id: int) -> bool:
        return self.repository.delete(id=item_id) is not None
