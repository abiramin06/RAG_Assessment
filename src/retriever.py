from src.vector_store import vector_search
from src.metadata_filter import filter_by_metadata


def retrieve_chunks(
    query,
    k=5,
    min_score=None,
    department=None,
    topic=None
):
    if not query or not query.strip():
        return []

    # Retrieve extra candidates when metadata filters are used
    if department or topic:
        search_k = 460
    else:
        search_k = k

    results = vector_search(
        query=query,
        top_k=search_k
    )

    if min_score is not None:
        results = [
            chunk for chunk in results
            if chunk.get("score", 0) >= min_score
        ]

    if department or topic:
        results = filter_by_metadata(
            results,
            department=department,
            topic=topic
        )

    return results[:k]