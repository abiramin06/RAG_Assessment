from src.retriever import retrieve_chunks
from src.token_budget import (
    fit_context,
    get_context_token_count
)

question = "How many casual leaves are provided?"

budget = 2000

for k in [2, 5, 10]:

    print(f"\n===== TESTING K = {k} =====")

    chunks = retrieve_chunks(question, k=k)

    selected_chunks = fit_context(
        chunks,
        budget=budget
    )

    token_count = get_context_token_count(
        selected_chunks
    )

    print("Retrieved chunks:", len(chunks))
    print("Selected chunks:", len(selected_chunks))
    print("Context tokens:", token_count)
    print("Budget:", budget)
    print("Within budget:", token_count <= budget)