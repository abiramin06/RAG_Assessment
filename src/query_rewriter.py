import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)


def rewrite_query(question):

    prompt = f"""
You are a search query rewriting assistant.

Generate exactly 3 alternative search queries
for the given question.

Rules:
1. Preserve the original meaning.
2. Use different wording.
3. Keep queries short.
4. Return only 3 queries, one per line.
5. Do not answer the question.

Original question:
{question}
"""

    response = client.chat.completions.create(
        model="gemini-3.5-flash-lite",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    output = response.choices[0].message.content

    queries = [
        line.strip(" -123456789.)\t")
        for line in output.splitlines()
        if line.strip()
    ]

    return queries[:3]