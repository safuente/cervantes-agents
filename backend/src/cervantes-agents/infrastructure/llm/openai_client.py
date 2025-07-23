
import os
from openai import OpenAI

class OpenAIClient:
    def __init__(self):
        self.client = OpenAI(
            api_key=os.getenv("OPENAI_API_KEY")
        )

    def chat(self, messages: list[dict], temperature: float = 0.7) -> str:
        response = self.client.chat.completions.create(
            model="gpt-4",
            messages=messages,
            temperature=temperature
        )
        return response.choices[0].message.content.strip()