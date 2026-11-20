from src.query import answer

test_cases = [
    {"question": "What should employees do according to company guidelines?", "expected": "answerable"},
    {"question": "What is the CEO's personal bank account number?", "expected": "unanswerable"},
    {"question": "What is the company's secret office Wi-Fi password?", "expected": "unanswerable"},
    {"question": "What is the approved company policy?", "expected": "answerable"},
    {"question": "What responsibility do managers have when reviewing requests?", "expected": "answerable"},
    {"question": "What is the company's private server password?", "expected": "unanswerable"},
    {"question": "How should confidential company information be protected?", "expected": "answerable"},
    {"question": "What is the CEO's home address?", "expected": "unanswerable"},
    {"question": "What should employees do when an approved change occurs?", "expected": "answerable"},
    {"question": "What is the personal phone number of the HR manager?", "expected": "unanswerable"}
]

print("\n===== HALLUCINATION DETECTION TEST =====")

correct = 0
total = len(test_cases)

for index, test in enumerate(test_cases, start=1):
    print(f"\nTEST {index}")
    print("Question:", test["question"])
    print("Expected:", test["expected"])

    response = answer(test["question"], k=5)

    print("Actual answer:", response)

    fallback = (
        not response
        or "i don't have information on that" in response.lower()
        or "cannot find" in response.lower()
    )

    if test["expected"] == "unanswerable":
        passed = fallback
    else:
        passed = not fallback

    if passed:
        correct += 1

    print("Test result:", "PASS" if passed else "FAIL")

print("\n===== FINAL HALLUCINATION RESULTS =====")
print("Total questions:", total)
print("Passed:", correct)
print("Failed:", total - correct)
print("Pass rate:", round(correct / total * 100, 2), "%")