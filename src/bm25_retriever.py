import json
import re
from pathlib import Path

from rank_bm25 import BM25Okapi


CHUNKS_PATH = Path("results/chunks.json")


def tokenize(text):
    return re.findall(r"\b\w+\b", text.lower())


class BM25Retriever:

    def __init__(self, chunks=None):

        if chunks is None:
            if not CHUNKS_PATH.exists():
                raise FileNotFoundError(
                    "chunks.json not found. Run indexing first."
                )

            with open(CHUNKS_PATH, "r", encoding="utf-8") as file:
                chunks = json.load(file)

        # Initialize chunks
        self.chunks = chunks

        # Tokenize document collection
        self.tokenized_corpus = [
            tokenize(chunk["text"])
            for chunk in self.chunks
        ]

        # Build BM25 index
        if self.tokenized_corpus:
            self.bm25 = BM25Okapi(
                self.tokenized_corpus
            )
        else:
            self.bm25 = None

    def search(self, query, top_k=5):

        if not query.strip() or not self.chunks:
            return []

        if self.bm25 is None:
            return []

        query_tokens = tokenize(query)

        scores = self.bm25.get_scores(query_tokens)

        ranked_indices = sorted(
            range(len(scores)),
            key=lambda i: scores[i],
            reverse=True
        )[:top_k]

        results = []

        for index in ranked_indices:
            result = dict(self.chunks[index])

            result["bm25_score"] = float(scores[index])

            results.append(result)

        return results


_retriever = None


def bm25_search(query, top_k=5):

    global _retriever

    if _retriever is None:
        _retriever = BM25Retriever()

    return _retriever.search(
        query,
        top_k=top_k
    )