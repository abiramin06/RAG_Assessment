import json
from pathlib import Path

path = Path("results/chunks.json")

with open(path, "r", encoding="utf-8") as file:
    chunks = json.load(file)

keywords = [
    "casual leave",
    "sick leave",
    "annual leave",
    "paid leave",
    "maternity leave",
    "leave days",
    "leave policy",
    "vacation"
]

print("===== LEAVE POLICY SEARCH =====")

for chunk in chunks:
    text = chunk.get("text", "").lower()

    if any(keyword in text for keyword in keywords):
        print("\nSource:", chunk.get("source"))
        print("Text:", chunk.get("text"))
        print("-" * 60)