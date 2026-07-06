from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)


def generate_report(context: str, topic: str):

    prompt = f"""
Using the information below, write a professional research report.

Topic:
{topic}

Context:
{context}

Sections:
1. Introduction
2. Findings
3. Analysis
4. Future Scope
5. Conclusion
"""

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b:free",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content