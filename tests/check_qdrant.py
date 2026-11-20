from src.vector_store import client, COLLECTION_NAME, DB_PATH

print("Database path:", DB_PATH)
print("Collection exists:", client.collection_exists(COLLECTION_NAME))

print("Collections:", client.get_collections())

if client.collection_exists(COLLECTION_NAME):
    info = client.get_collection(COLLECTION_NAME)
    print("Stored points:", info.points_count)