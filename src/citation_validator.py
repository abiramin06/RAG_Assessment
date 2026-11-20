import re


def validate_citations(answer, retrieved_chunks):
    if not answer:
        return {
            "valid": False,
            "reason": "Empty answer",
            "citations": []
        }

    # Extract citations inside square brackets
    citations = re.findall(r"\[([^\]]+)\]", answer)

    if not citations:
        return {
            "valid": False,
            "reason": "No citations found",
            "citations": []
        }

    valid_sources = {
        chunk.get("source")
        for chunk in retrieved_chunks
        if chunk.get("source")
    }

    results = []

    for citation in citations:
        cited_source = citation.split(", p.")[0].strip()

        results.append({
            "citation": citation,
            "valid": cited_source in valid_sources
        })

    return {
        "valid": all(item["valid"] for item in results),
        "reason": "Citation validation completed",
        "citations": results
    }