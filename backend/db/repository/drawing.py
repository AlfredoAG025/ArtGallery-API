from sqlalchemy.orm import Session

from schemas.drawing import CreateDrawing
from db.models.drawing import Drawing


def list_drawings(db: Session):
    drawings = db.query(Drawing).all()
    return drawings


def retrieve_drawing(id: int, db: Session):
    drawing = db.query(Drawing).filter(Drawing.id == id).first()
    return drawing


def create_new_drawing(drawing: CreateDrawing, db: Session, author_id: int = 1):
    drawing = Drawing(**drawing.dict(), author_id=author_id)
    db.add(drawing)
    db.commit()
    db.refresh(drawing)
    return drawing
