from src.retriever import retrieve_chunks
from src.answer_generator import generate_answer
from src.token_budget import fit_context, get_context_token_count


SCORE_THRESHOLD = 0.45
CONTEXT_BUDGET = 2000

FALLBACK_MESSAGE = "I don't have information on that."


def answer(question, k=4,department=None,topic=None):

    if not question or not question.strip():
        return FALLBACK_MESSAGE

    # Step 1: Retrieve relevant chunks
    chunks = retrieve_chunks(
        query=question,
        k=k,
        department=department,
        topic=topic
    )

    if not chunks:
        print("No relevant chunks found.")
        return FALLBACK_MESSAGE

    # Step 2: Similarity score fallback
    best_score = max(
        chunk.get("score", 0)
        for chunk in chunks
    )

    print("Best retrieval score:", round(best_score, 4))

    if best_score < SCORE_THRESHOLD:
        print("Fallback triggered. LLM not called.")
        return FALLBACK_MESSAGE

    # Step 3: Fit context within token budget
    selected_chunks = fit_context(
        chunks,
        budget=CONTEXT_BUDGET
    )

    if not selected_chunks:
        print("No chunks fit within context budget.")
        return FALLBACK_MESSAGE

    print(
        "Context tokens:",
        get_context_token_count(selected_chunks)
    )

    # Step 4: Generate grounded answer
    response = generate_answer(
        question,
        selected_chunks
    )

    if not response:
        return FALLBACK_MESSAGE

    return response