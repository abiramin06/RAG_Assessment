from pathlib import Path
import fitz
from docx import Document
import csv


def load_pdf(path):
    """Extract text from PDF."""
    doc = fitz.open(path)
    pages = []

    for page_number, page in enumerate(doc, start=1):
        text = page.get_text().strip()

        if text:
            pages.append({
                "text": text,
                "source": str(path),
                "file_type": "pdf",
                "page": page_number
            })

    return pages


def load_docx(path):
    """Extract text from Word document."""
    doc = Document(path)
    text = "\n".join(
        p.text for p in doc.paragraphs if p.text.strip()
    )

    if not text:
        return []

    return [{
        "text": text,
        "source": str(path),
        "file_type": "docx",
        "page": None
    }]


def load_csv(path):
    documents = []

    with open(path, "r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)

        for row_number, row in enumerate(reader, start=1):
            text = "\n".join(
                f"{key}: {value}"
                for key, value in row.items()
                if value
            )

            documents.append({
                "text": text,
                "source": str(path),
                "file_type": "csv",
                "row": row_number,
                "id": row.get("id"),
                "department": row.get("department"),
                "topic": row.get("topic")
            })

    return documents


def load_documents(folder="data"):
    """Load all supported documents."""
    folder = Path(folder)
    documents = []
    skipped = []

    for path in sorted(folder.rglob("*")):
        if not path.is_file():
            continue

        try:
            if path.suffix.lower() == ".pdf":
                documents.extend(load_pdf(path))

            elif path.suffix.lower() == ".docx":
                documents.extend(load_docx(path))

            elif path.suffix.lower() == ".csv":
                documents.extend(load_csv(path))

        except Exception as error:
            skipped.append({
                "source": str(path),
                "error": str(error)
            })

    return documents, skipped