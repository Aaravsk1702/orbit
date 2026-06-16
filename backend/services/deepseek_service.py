import os
import requests
from dotenv import load_dotenv

load_dotenv()


def deepseek_response(prompt: str):

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {os.getenv('OPENROUTER_API_KEY')}",
            "Content-Type": "application/json"
        },
        json={
            "model": "deepseek/deepseek-chat",
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        }
    )

    response.raise_for_status()

    data = response.json()

    return data["choices"][0]["message"]["content"]