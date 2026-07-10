from sentence_transformers import SentenceTransformer


class EmbeddingService:

    model = SentenceTransformer(
        "BAAI/bge-base-en-v1.5"
    )

    @classmethod
    def generate_embedding(cls, text: str):

        embedding = cls.model.encode(
            text,
            normalize_embeddings=True
        )

        return embedding.tolist()