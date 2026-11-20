from sentence_transformers import CrossEncoder


MODEL_NAME = "cross-encoder/ms-marco-MiniLM-L-6-v2"

reranker = CrossEncoder(MODEL_NAME)


def rerank_chunks(query, chunks, top_k=5):

    if not chunks:
        return []

    pairs = [
        [query, chunk["text"]]
        for chunk in chunks
    ]

    scores = reranker.predict(pairs)

    ranked_results = []

    for chunk, score in zip(chunks, scores):

        result = dict(chunk)
        result["rerank_score"] = float(score)

        ranked_results.append(result)

    ranked_results.sort(
        key=lambda x: x["rerank_score"],
        reverse=True
    )

    return ranked_results[:top_k]