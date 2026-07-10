from fastapi import APIRouter, UploadFile, File, Depends, Form
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.document import DocumentResponse
from app.services.document_service import DocumentService
from app.models.document import Document
from app.services.chunk_service import ChunkService
from app.services.vector_service import VectorService
from app.models.user import User


router = APIRouter(
    prefix="/documents",
    tags=["Documents"]
)


@router.post(
    "/upload",
    response_model=DocumentResponse
)
async def upload_document(
    file: UploadFile = File(...),
    user_id: int = Form(),
    db: Session = Depends(get_db)
):
    user=db.query(User).filter(User.id==user_id).first()
    file_path, text_content=await DocumentService.upload_document(db, file, user.name)
    try:
        document = Document(
            user_id=user_id,
            filename=file.filename,
            filepath=str(file_path),
            created_by=user_id
        ) 
        db.add(document)
        db.flush()

        chunks, embeddings = ChunkService.split_text(
            text_content,
            document.id,
            chunk_size=500
        )
        db.add_all(chunks)
        db.flush()

        for chunk, embedding in zip(chunks, embeddings):
            VectorService.insert_vector(
                user_id,
                user.name,
                document.id,
                chunk.id,
                embedding
            )

        db.commit()
        
        return document
    except:
        db.rollback()

        if file_path.exists():
            file_path.unlink()

        raise
