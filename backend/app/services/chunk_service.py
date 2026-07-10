from app.models.document_chunk import DocumentChunk
from app.services.embedding_service import EmbeddingService


class ChunkService:

    @staticmethod
    def split_text(
        text: str,
        document_id: int,
        chunk_size: int = 500
    ):

        chunks = []
        embeddings = []

        for index, start in enumerate(
            range(0, len(text), chunk_size)
        ):
            content = text[start:start + chunk_size]
            chunks.append(
                DocumentChunk(
                    document_id=document_id,
                    chunk_number=index,
                    content=content
                )
            )
            embeddings.append(EmbeddingService.generate_embedding(content))
        return (chunks, embeddings)