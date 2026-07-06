import requests

from app.config import (
    OPENROUTER_API_KEY,
    OPENROUTER_URL,
    MODEL_NAME
)


def generate_text(prompt: str) -> str:
    """
    Sends a prompt to OpenRouter and returns the AI response.
    """

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": MODEL_NAME,
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "temperature": 0.7
    }

    response = requests.post(
        OPENROUTER_URL,
        headers=headers,
        json=payload
    )

    response.raise_for_status()

    data = response.json()

    return data["choices"][0]["message"]["content"]