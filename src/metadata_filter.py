def filter_by_metadata(
    chunks,
    department=None,
    topic=None
):
    filtered = chunks

    if department:
        filtered = [
            chunk for chunk in filtered
            if (chunk.get("department") or "").strip().lower()
            == department.strip().lower()
        ]

    if topic:
        filtered = [
            chunk for chunk in filtered
            if (chunk.get("topic") or "").strip().lower()
            == topic.strip().lower()
        ]

    return filtered