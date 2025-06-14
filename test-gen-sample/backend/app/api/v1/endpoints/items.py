from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.api.deps import get_current_db
from app.controllers.item_controller import ItemController
from app.schemas.item import ItemCreate, ItemResponse

router = APIRouter()

@router.post("/", response_model=ItemResponse)
def create_item(
    item_data: ItemCreate,
    db: Session = Depends(get_current_db)
):
    controller = ItemController(db)
    return controller.create_item(item_data)

@router.get("/", response_model=List[ItemResponse])
def get_items(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_current_db)
):
    controller = ItemController(db)
    return controller.get_items(skip=skip, limit=limit)

@router.get("/{item_id}", response_model=ItemResponse)
def get_item(
    item_id: int,
    db: Session = Depends(get_current_db)
):
    controller = ItemController(db)
    item = controller.get_item(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item
