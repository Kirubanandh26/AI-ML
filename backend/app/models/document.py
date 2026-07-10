from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.db.base import Base


class Document(Base):
    __tablename__ = "document"

    id = Column(Integer, primary_key=True, index=True)

    filename = Column(String(255))

    filepath = Column(String(500))

    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    
    created_by = Column(Integer)

    user_id = Column(
        Integer,
        ForeignKey("user.id"),
        nullable=False
    )

    user = relationship(
        "User",
        back_populates="document")

    chunk = relationship(
        "DocumentChunk",
        back_populates="document")