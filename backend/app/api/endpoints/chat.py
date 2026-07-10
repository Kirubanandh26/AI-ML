from fastapi import APIRouter, Depends, Form
from sqlalchemy.orm import Session
from app.db.session import get_db

from app.schemas.chat import ChatResponse
from app.services.embedding_service import EmbeddingService
from app.services.vector_service import VectorService
from app.services.llm_service import LLMService
from app.models.user import User
from app.models.document import Document
from app.models.document_chunk import DocumentChunk


router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)


@router.post(
    "/queries"
    # response_model=ChatResponse
)
async def query_chat(
    query: str = Form(),
    user_id: int = Form(),
    db: Session = Depends(get_db)
):
    document = db.query(Document).filter(Document.user_id==user_id).first()

    if len(query)>500:
        raise ValueError("Query size limit exceeded 500.")

    embedding = EmbeddingService.generate_embedding(query)
    qdrant_data = VectorService.search_vector(embedding, document.id, 1)
    chunk_ids = [point.id for point in qdrant_data.points]

    chunks = (
        db.query(DocumentChunk)
        .filter(DocumentChunk.id.in_(chunk_ids))
        .all()
    )
    context = "\n\n".join(chunk.content for chunk in chunks)

    prompt = f"""
    You are an AI assistant.

    Answer the question ONLY using the provided context.

    If the answer cannot be found in the context,
    reply:
    "I couldn't find that information in the document."

    Context:
    {context}

    Question:
    {query}
    """
    print("promt", prompt)

    response = LLMService.generate_response(prompt)

    return response
