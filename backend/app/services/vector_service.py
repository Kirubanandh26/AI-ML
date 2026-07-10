from app.db.vector import vector_client
from qdrant_client.models import PointStruct
from app.collections.document_chunk import CreateCollection
from qdrant_client.models import (
    Filter,
    FieldCondition,
    MatchValue,
)


class VectorService:

    @staticmethod 
    def insert_vector(
        user_id: int,
        user_name: str,
        document_id: int,
        chunk_id: int,
        embedding: list[float]
    ):
        CreateCollection.create_collection()
        vector_client.upsert(

            collection_name="document_chunks",

            points=[

                PointStruct(

                    id=chunk_id,

                    vector=embedding,

                    payload={
                        "user_id": user_id,
                        "user_name": user_name,
                        "document_id": document_id
                    }

                )

            ]

        )


    @staticmethod
    def search_vector(
        embedding: list[float],
        document_id: int,
        limit: int = 5
    ):
        query_filter = Filter(
            must=[
                FieldCondition(
                    key="document_id",
                    match=MatchValue(value=document_id)
                )
            ]
        )
        results = vector_client.query_points(
            collection_name="document_chunks",
            query=embedding,
            query_filter=query_filter,
            limit=limit
        )

        return results