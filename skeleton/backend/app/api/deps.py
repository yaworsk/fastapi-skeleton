from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db

def get_current_db(db: Session = Depends(get_db)) -> Session:
    return db
