from datetime import date
from typing import Optional

from pydantic import BaseModel, root_validator


class CreateDrawing(BaseModel):
    title: str
    slug: str
    image: str
    description: Optional[str] = None

    @root_validator(pre=True)
    def generate_slug(cls, values):
        if 'title' in values:
            values['slug'] = values.get("title").replace(" ", "-").lower()
        return values


class ShowDrawing(BaseModel):
    id: int
    title: str
    image: str
    description: Optional[str]
    created_at: date

    class Config:
        orm_mode = True
