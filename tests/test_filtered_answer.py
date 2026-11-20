from src.query import answer

question = "What should employees do according to the company guidelines?"

response = answer(
    question=question,
    k=5,
    department="Salary and Payroll Policy",
    topic="Company record 1-1"
)

print("\n===== FILTERED RAG ANSWER =====")
print("Question:", question)
print("Answer:", response)