from src.citation_validator import validate_citations

retrieved_chunks = [
    {
        "source": "data/csv/records_01.csv",
        "page": None,
        "text": "Employees must follow company guidelines."
    },
    {
        "source": "data/pdf/employee_policy.pdf",
        "page": 3,
        "text": "Employees receive annual leave."
    }
]

# Test 1: Valid citation
valid_answer = (
    "Employees must follow company guidelines "
    "[data/csv/records_01.csv, p.None]."
)

# Test 2: Fake citation
fake_answer = (
    "Employees receive benefits "
    "[fake_document.pdf, p.10]."
)

print("\n===== CITATION VALIDATION =====")

result1 = validate_citations(valid_answer, retrieved_chunks)
print("\nValid citation test:")
print(result1)

result2 = validate_citations(fake_answer, retrieved_chunks)
print("\nFake citation test:")
print(result2)

assert result1["valid"] is True
assert result2["valid"] is False

print("\nAll citation tests passed!")