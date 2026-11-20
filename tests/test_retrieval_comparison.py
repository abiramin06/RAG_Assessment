from src.bm25_retriever import bm25_search
from src.retriever import retrieve_chunks


questions = {
    "exact_term": [
        "casual leaves",
        "sick leaves",
        "salary payment",
        "office working hours",
        "planned leave notice",
        "medical certificate"
    ],
    "meaning_based": [
        "How much time off can employees take for personal reasons?",
        "What happens when an employee becomes ill?",
        "When do workers receive their monthly pay?",
        "What are the normal timings for employees?",
        "How early should someone request planned time off?",
        "What proof is needed for an extended illness?"
    ]
}


for category, question_list in questions.items():

    print(f"\n========== {category.upper()} ==========")

    for question in question_list:

        print("\nQUESTION:", question)

        bm25_results = bm25_search(question, top_k=3)
        vector_results = retrieve_chunks(question, k=3)

        print("\nBM25 TOP 3:")
        for rank, result in enumerate(bm25_results, start=1):
            print(rank, result["source"])

        print("\nVECTOR TOP 3:")
        for rank, result in enumerate(vector_results, start=1):
            print(rank, result["source"])