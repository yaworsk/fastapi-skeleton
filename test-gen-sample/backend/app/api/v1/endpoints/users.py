from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.api.deps import get_current_db
from app.controllers.user_controller import UserController
from app.schemas.user import UserCreate, UserResponse

router = APIRouter()

@router.post("/", response_model=UserResponse)
def create_user(
    user_data: UserCreate,
    db: Session = Depends(get_current_db)
):
    controller = UserController(db)
    return controller.create_user(user_data)

@router.get("/", response_model=List[UserResponse])
def get_users(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_current_db)
):
    controller = UserController(db)
    return controller.get_users(skip=skip, limit=limit)

@router.get("/{user_id}", response_model=UserResponse)
def get_user(
    user_id: int,
    db: Session = Depends(get_current_db)
):
    controller = UserController(db)
    user = controller.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
