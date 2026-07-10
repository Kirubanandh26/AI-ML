from sqlalchemy import Column, ForeignKey, Integer, Text
from sqlalchemy.orm import relationship

from app.db.base import Base


class DocumentChunk(Base):
    __tablename__ = "document_chunk"

    id = Column(Integer, primary_key=True)

    document_id = Column(
        Integer,
        ForeignKey("document.id"),
        nullable=False
    )

    chunk_number = Column(Integer)

    content = Column(Text)

    document = relationship(
        "Document",
        back_populates="chunk"
    )