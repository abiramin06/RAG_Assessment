from src.query import answer

answerable_questions = [
    "How many casual leaves are provided?",
    "How many sick leaves are provided?",
    "How many days of advance notice is required for planned leave?",
    "Can casual leaves be carried forward?",
    "When is a medical certificate required?",
    "What is the company leave policy?"
]

unanswerable_questions = [
    "Who won the FIFA World Cup?",
    "What is the capital of Japan?",
    "Who is the CEO of Google?",
    "What is the population of Canada?"
]

print("\n========== ANSWERABLE QUESTIONS ==========")

for question in answerable_questions:
    print("\nQ:", question)
    print("A:", answer(question, k=4))


print("\n========== UNANSWERABLE QUESTIONS ==========")

for question in unanswerable_questions:
    print("\nQ:", question)
    print("A:", answer(question, k=4))