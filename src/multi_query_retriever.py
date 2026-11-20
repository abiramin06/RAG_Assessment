from src.query_rewriter import rewrite_query
from src.hybrid_retriever import hybrid_search, reciprocal_rank_fusion


def multi_query_search(question, top_k=5):

    # Original query
    queries = [question]

    # Generate 3 alternative queries
    rewritten = rewrite_query(question)

    queries.extend(rewritten)

    print("\nSEARCH QUERIES:")

    for query in queries:
        print("-", query)

    # Retrieve results for all queries
    rankings = []

    for query in queries:

        results = hybrid_search(
            query,
            top_k=50
        )

        rankings.append(results)

    # Merge using RRF
    final_results = reciprocal_rank_fusion(
        rankings,
        k=60,
        top_k=top_k
    )

    return final_results