import os

from groq import Groq
from dotenv import load_dotenv


load_dotenv()


class GroqClient:

    def __init__(self):

        self.client = Groq(

            api_key=os.getenv("GROQ_API_KEY")
        )

    def generate_response(
        self,
        prompt
    ):

        completion = self.client.chat.completions.create(

            model="llama-3.1-8b-instant",

            messages=[

                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return completion.choices[0].message.content


if __name__ == "__main__":

    client = GroqClient()

    result = client.generate_response(
        "Explain emotional intelligence briefly."
    )

    print(result)