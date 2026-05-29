from collections import Counter

from app.memory.postgres_memory import PostgresMemory


class ProfileManager:

    def __init__(self):

        self.memory_db = PostgresMemory()

    def build_emotional_profile(

        self,

        user_id
    ):

        memories = self.memory_db.fetch_recent_memories(
            user_id,
            limit=50
        )

        if not memories:

            return {

                "dominant_emotion": "neutral",

                "memory_count": 0,

                "emotion_distribution": {},

                "identity_state": {},

                "relationship_state": {},

                "memory_depth": 0
            }

        emotions = []

        for memory in memories:

            emotional_state = memory.get(
                "emotional_state",
                "neutral"
            )

            if emotional_state is None:
                emotional_state = "neutral"

            emotions.append(emotional_state)

        emotion_counter = Counter(emotions)

        dominant_emotion = emotion_counter.most_common(1)[0][0]

        return {

            "dominant_emotion": dominant_emotion,

            "memory_count": len(memories),

            "emotion_distribution": dict(emotion_counter),

            "identity_state": {

                "stability": "stable",

                "dominant_emotion": dominant_emotion
            },

            "relationship_state": {

                "attachment_level": len(memories) / 10
            },

            "memory_depth": len(memories)
        }


if __name__ == "__main__":

    profile = ProfileManager()

    result = profile.build_emotional_profile(
        "user_1"
    )

    print(result)
