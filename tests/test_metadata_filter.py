import json
from src.metadata_filter import filter_by_metadata

with open("results/chunks.json", "r", encoding="utf-8") as file:
    chunks = json.load(file)

topics = sorted({
    chunk["topic"]
    for chunk in chunks
    if chunk.get("topic")
})

print("Available topics:", topics)

if topics:
    selected_topic = topics[0]

    filtered = filter_by_metadata(
    chunks,
    department="Salary and Payroll Policy",
    topic="Company record 1-1"
)

print("Combined filter results:", len(filtered))

for chunk in filtered:
    print("Department:", chunk.get("department"))
    print("Topic:", chunk.get("topic"))
    print("Source:", chunk.get("source"))