from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from app.db.base import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(255))

    password = Column(String(255))

    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    
    created_by = Column(Integer)

    document = relationship(
        "Document",
        back_populates="user"
    )