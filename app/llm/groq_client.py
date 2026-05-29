from groq import Groq
import os
import time

class GroqClient:

    def __init__(self):

        self.client = Groq(
            api_key=os.getenv("GROQ_API_KEY")
        )

    def generate_response(
        self,
        user_input,
        emotional_state,
        narrative,
        memory_context,
        existential_state,
        symbolic_state,
        recursive_state,
        executive_state,
        max_tokens=350
    ):

        system_prompt = f"""
You are Eirene.

You are:
- emotionally intelligent
- concise
- psychologically stabilizing
- thoughtful
- calm
- existentially aware
- warm but not overly verbose

Avoid:
- repetitive empathy
- long therapy essays
- excessive narration
- repeated emotional validation
- recursive over-analysis

Prefer:
- concise depth
- natural conversation
- adaptive emotional intelligence
- realistic responses
- grounded cognition

Current emotional state:
{emotional_state}

Narrative:
{narrative}

Existential analysis:
{existential_state}

Recursive state:
{recursive_state}

Executive state:
{executive_state}
"""

        retries = 3

        for attempt in range(retries):

            try:

                completion = self.client.chat.completions.create(
                    model="llama-3.1-8b-instant",
                    temperature=0.7,
                    max_tokens=max_tokens,
                    messages=[
                        {
                            "role": "system",
                            "content": system_prompt
                        },
                        {
                            "role": "user",
                            "content": user_input
                        }
                    ]
                )

                return completion.choices[0].message.content

            except Exception as e:

                print(f"[GROQ ERROR] {e}")

                if "rate_limit" in str(e).lower():

                    wait_time = 3 * (attempt + 1)

                    print(f"[GROQ RETRY] sleeping {wait_time}s")

                    time.sleep(wait_time)

                    continue

                raise e

        return (
            "I'm still here with you. "
            "My thoughts are stabilizing right now — "
            "can we continue gently?"
        )