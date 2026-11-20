import hashlib
import json
import time
from pathlib import Path

from src.loader import load_documents
from src.chunker import create_chunks
from src.vector_store import store_chunks

MANIFEST_PATH = Path("results/manifest.json")
CHUNKS_PATH = Path("results/chunks.json")


def calculate_file_hash(path):
    sha256 = hashlib.sha256()

    with open(path, "rb") as file:
        for block in iter(lambda: file.read(4096), b""):
            sha256.update(block)

    return sha256.hexdigest()


def ingest_documents(folder="data"):
    start_time = time.time()

    # Step 1: Load documents
    documents, skipped = load_documents(folder)

    print("Documents loaded:", len(documents))

    # Step 2: Create chunks
    chunks = create_chunks(documents)

    print("Chunks created:", len(chunks))

    # Step 3: Store embeddings in Qdrant
    if chunks:
        store_chunks(chunks)
        print("Qdrant storage completed.")
    else:
        print("No chunks available for storage.")

    # Step 4: Create file manifest
    files = [
        p for p in Path(folder).rglob("*")
        if p.is_file()
        and p.suffix.lower() in [".pdf", ".docx", ".csv"]
    ]

    manifest = {
        str(path): calculate_file_hash(path)
        for path in files
    }

    # Step 5: Save manifest and chunks
    MANIFEST_PATH.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    MANIFEST_PATH.write_text(
        json.dumps(manifest, indent=2),
        encoding="utf-8"
    )

    CHUNKS_PATH.write_text(
        json.dumps(chunks, indent=2),
        encoding="utf-8"
    )

    # Step 6: Summary
    elapsed = round(time.time() - start_time, 2)

    print("\n===== INGESTION SUMMARY =====")
    print("Total files:", len(files))
    print("Documents loaded:", len(documents))
    print("Total chunks:", len(chunks))
    print("Skipped files:", len(skipped))
    print("Time taken:", elapsed, "seconds")


if __name__ == "__main__":
    ingest_documents()