from typing import List

from fastapi import APIRouter, status, HTTPException
from sqlalchemy.orm import Session
from fastapi import Depends

from schemas.drawing import CreateDrawing, ShowDrawing
from db.session import get_db
from db.repository.drawing import create_new_drawing, list_drawings, retrieve_drawing

router = APIRouter()


@router.get("/drawings", response_model=List[ShowDrawing])
def get_all_drawings(db: Session = Depends(get_db)):
    drawings = list_drawings(db=db)
    return drawings


@router.get("/drawings/{id}", response_model=ShowDrawing)
def get_drawing(id: int, db: Session =Depends(get_db)):
    drawing = retrieve_drawing(id=id, db=db)
    if not drawing:
        raise HTTPException(detail=f"Drawing with ID {id} does not exists.", status_code=status.HTTP_404_NOT_FOUND)
    return drawing


@router.post("/drawings", response_model=ShowDrawing, status_code=status.HTTP_201_CREATED)
def create_drawing(drawing: CreateDrawing, db: Session = Depends(get_db)):
    drawing = create_new_drawing(drawing=drawing, db=db, author_id=1)
    return drawing
