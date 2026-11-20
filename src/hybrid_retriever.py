from src.bm25_retriever import bm25_search
from src.vector_store import vector_search


def reciprocal_rank_fusion(rankings, k=60, top_k=5):

    scores = {}
    documents = {}

    for ranking in rankings:

        for rank, result in enumerate(ranking, start=1):

            chunk_id = result["id"]

            rrf_score = 1 / (k + rank)

            scores[chunk_id] = (
                scores.get(chunk_id, 0) + rrf_score
            )

            documents[chunk_id] = result

    ranked_ids = sorted(
        scores,
        key=lambda chunk_id: scores[chunk_id],
        reverse=True
    )

    fused_results = []

    for chunk_id in ranked_ids[:top_k]:

        result = dict(documents[chunk_id])
        result["rrf_score"] = scores[chunk_id]

        fused_results.append(result)

    return fused_results


def hybrid_search(query, top_k=5):

    bm25_results = bm25_search(
        query,
        top_k=50
    )

    vector_results = vector_search(
        query,
        top_k=50
    )

    return reciprocal_rank_fusion(
        [bm25_results, vector_results],
        k=60,
        top_k=top_k
    )