from collections import Counter

from app.memory.postgres_memory import PostgresMemory


class ReflectionEngine:

    def __init__(self):

        self.memory_db = PostgresMemory()

    def generate_reflection(

        self,

        user_id
    ):

        memories = self.memory_db.fetch_recent_memories(
            user_id,
            limit=20
        )

        if not memories:

            return "I do not yet have enough emotional history to form reflections."

        emotions = [

            memory["emotional_state"]

            for memory in memories
        ]

        emotion_counter = Counter(emotions)

        dominant_emotion = emotion_counter.most_common(1)[0][0]

        reflection = f"""
Over recent conversations, I’ve noticed recurring emotional patterns.

Dominant emotional state:
{dominant_emotion}

Emotion distribution:
{dict(emotion_counter)}

You seem to be experiencing repeated emotional themes that may deserve deeper attention and care.
"""

        return reflection.strip()


if __name__ == "__main__":

    engine = ReflectionEngine()

    result = engine.generate_reflection(
        "user_1"
    )

    print(result)