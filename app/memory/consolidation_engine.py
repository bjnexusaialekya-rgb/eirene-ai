from collections import Counter


class ConsolidationEngine:

    def consolidate_memories(
        self,
        memories
    ):

        if not memories:
            return {}

        emotions = [
            memory["emotional_state"]
            for memory in memories
        ]

        emotion_frequency = Counter(emotions)

        dominant_pattern = emotion_frequency.most_common(1)[0][0]

        recurring_topics = []

        for memory in memories:

            text = memory["memory_text"]

            if len(text.split()) > 5:
                recurring_topics.append(text[:80])

        return {
            "dominant_pattern": dominant_pattern,
            "emotion_frequency": dict(emotion_frequency),
            "recurring_topics": recurring_topics[:5]
        }
