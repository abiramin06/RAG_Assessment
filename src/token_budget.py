import tiktoken


def count_tokens(text):
    """
    Count tokens using tiktoken.
    """
    encoding = tiktoken.get_encoding("cl100k_base")
    return len(encoding.encode(text))


def fit_context(chunks, budget=2000):
    """
    Select chunks without exceeding the token budget.
    """

    selected_chunks = []
    total_tokens = 0

    for chunk in chunks:

        text = chunk.get("text", "")

        chunk_tokens = count_tokens(text)

        if total_tokens + chunk_tokens <= budget:
            selected_chunks.append(chunk)
            total_tokens += chunk_tokens

    return selected_chunks


def get_context_token_count(chunks):
    """
    Calculate total tokens in selected chunks.
    """

    return sum(
        count_tokens(chunk.get("text", ""))
        for chunk in chunks
    )