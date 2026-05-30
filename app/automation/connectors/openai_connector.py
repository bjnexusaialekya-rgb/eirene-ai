import os
from pathlib import Path

from dotenv import load_dotenv
from groq import Groq

PROJECT_ROOT = Path(__file__).resolve().parents[3]
load_dotenv(PROJECT_ROOT / ".env")


class OpenAIConnector:

    def __init__(self):

        api_key = os.getenv("GROQ_API_KEY")

        if not api_key:
            raise ValueError(
                "GROQ_API_KEY not found in environment variables."
            )

        self.client = Groq(
            api_key=api_key
        )

    def ask(
        self,
        prompt: str,
        system_prompt: str = "You are a helpful AI assistant."
    ):

        response = self.client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.3
        )

        return response.choices[0].message.content

    def qualify_lead(
        self,
        lead_text: str
    ):

        prompt = f"""
You are an AI sales qualification assistant.

Evaluate the lead below.

Lead:
{lead_text}

Return exactly:

Score: <0-100>

Reason:
<short reason>

Category:
Hot / Warm / Cold

Recommended Action:
<next action>
"""

        return self.ask(
            prompt,
            "You are an expert sales qualification assistant."
        )
