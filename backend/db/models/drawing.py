from datetime import datetime

from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship

from db.base_class import Base


class Drawing(Base):
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    image = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    author_id = Column(Integer, ForeignKey("user.id"))
    author = relationship("User", back_populates="drawings")
    created_at = Column(DateTime, default=datetime.now)
    is_active = Column(Boolean, default=False)