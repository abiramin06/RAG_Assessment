import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)


def generate_answer(question, chunks):

    if not chunks:
        return None

    context_parts = []

    for chunk in chunks:
        context_parts.append(
            f"Source: {chunk['source']}\n"
            f"Page: {chunk.get('page')}\n"
            f"Content: {chunk['text']}"
        )

    context = "\n\n".join(context_parts)

    prompt = f"""
You are an Enterprise Knowledge Assistant.

Answer ONLY using the supplied context.

Rules:
1. Do not invent information.
2. If information is missing, say you cannot find it.
3. Include at least one exact source citation.
4. Citation format: [filename, p.page_number]
5. Do not create fake citations.

Context:
{context}

Question:
{question}

Provide a clear and concise answer with citations.
"""

    response = client.chat.completions.create(
        model="gemini-3.5-flash-lite",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        
    )

    return response.choices[0].message.content