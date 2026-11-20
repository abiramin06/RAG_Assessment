from src.vector_store import client, COLLECTION_NAME

points, next_page = client.scroll(
    collection_name=COLLECTION_NAME,
    limit=460,
    with_payload=True,
    with_vectors=False
)

print("\n===== QDRANT METADATA CHECK =====")
print("Total points retrieved:", len(points))

found = False

for point in points:
    payload = point.payload or {}

    if payload.get("department"):
        print("\nDepartment:", payload.get("department"))
        print("Topic:", payload.get("topic"))
        print("Source:", payload.get("source"))
        found = True
        break

if not found:
    print("No department metadata found in Qdrant.")