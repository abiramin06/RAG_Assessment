from src.retriever import retrieve_chunks

results = retrieve_chunks(
    query="Company record 1-1",
    k=5,
    department="Salary and Payroll Policy",
    topic="Company record 1-1"
)

print("\n===== COMBINED QDRANT FILTER TEST =====")
print("Results found:", len(results))

for chunk in results:
    print("Department:", chunk.get("department"))
    print("Topic:", chunk.get("topic"))
    print("Source:", chunk.get("source"))