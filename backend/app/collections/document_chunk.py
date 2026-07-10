from app.db.vector import vector_client
from qdrant_client.models import VectorParams, Distance


class CreateCollection:

    @staticmethod
    def create_collection():

        if not vector_client.collection_exists("document_chunks"):

            vector_client.create_collection(

                collection_name="document_chunks",

                vectors_config=VectorParams(
                    size=768,
                    distance=Distance.COSINE
                )

            )