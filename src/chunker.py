import hashlib


def create_chunks(documents, chunk_size=500, overlap=50):
    chunks = []

    for document in documents:
        text = document["text"]
        start = 0

        while start < len(text):
            end = start + chunk_size
            chunk_text = text[start:end].strip()

            if chunk_text:
                chunk_id = hashlib.sha256(
                    (
                        document["source"]
                        + str(start)
                        + chunk_text
                    ).encode("utf-8")
                ).hexdigest()

                chunks.append({
                    "id": chunk_id,
                    "text": chunk_text,
                    "source": document["source"],
                    "file_type": document["file_type"],
                    "page": document.get("page"),
                    "row": document.get("row"),
                    "start": start,
                    "department": document.get("department"),
                    "topic": document.get("topic")
                })

            start += chunk_size - overlap

    return chunks