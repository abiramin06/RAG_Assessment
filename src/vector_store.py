from qdrant_client.models import Filter, FieldCondition, MatchValue
from pathlib import Path
from qdrant_client import QdrantClient
from qdrant_client.models import (
    Distance,
    VectorParams,
    PointStruct
)

from src.embedder import generate_embeddings, embed_query
import uuid
COLLECTION_NAME = "knowledge_documents"

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "qdrant_db"

client = QdrantClient(path=str(DB_PATH))


def create_collection():
    if client.collection_exists(COLLECTION_NAME):
        return

    client.create_collection(
        collection_name=COLLECTION_NAME,
        vectors_config=VectorParams(
            size=384,
            distance=Distance.COSINE
        )
    )


def store_chunks(chunks):
    create_collection()

    embeddings = generate_embeddings(
        [chunk["text"] for chunk in chunks]
    )

    points = []

    for chunk, embedding in zip(chunks, embeddings):
        points.append(
            PointStruct(
                id=str(uuid.UUID(hex=chunk["id"][:32])),
                vector=embedding.tolist(),
                payload=chunk
            )
        )

    client.upsert(
        collection_name=COLLECTION_NAME,
        points=points
    )

def vector_search(
    query,
    top_k=5,
    department=None,
    topic=None
):
    query_vector = embed_query(query)

    conditions = []

    if department:
        conditions.append(
            FieldCondition(
                key="department",
                match=MatchValue(value=department)
            )
        )

    if topic:
        conditions.append(
            FieldCondition(
                key="topic",
                match=MatchValue(value=topic)
            )
        )

    query_filter = Filter(must=conditions) if conditions else None

    response = client.query_points(
        collection_name=COLLECTION_NAME,
        query=query_vector,
        query_filter=query_filter,
        limit=top_k,
        with_payload=True
    )

    results = []

    for point in response.points:
        result = dict(point.payload)
        result["score"] = point.score
        results.append(result)

    return results
