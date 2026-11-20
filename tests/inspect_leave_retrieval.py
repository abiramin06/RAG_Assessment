import json

with open("results/chunks.json", "r", encoding="utf-8") as file:
    chunks = json.load(file)

keywords = [
    "casual leave",
    "sick leave",
    "annual leave",
    "planned leave",
    "medical certificate"
]

print("\n===== LEAVE POLICY CONTENT SEARCH =====")

for chunk in chunks:
    text = chunk.get("text", "").lower()

    if any(keyword in text for keyword in keywords):
        print("\nSource:", chunk.get("source"))
        print("Page:", chunk.get("page"))
        print("Text:", chunk.get("text"))