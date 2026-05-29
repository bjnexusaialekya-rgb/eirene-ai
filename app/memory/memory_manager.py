from app.memory.postgres_memory import PostgresMemory


class MemoryManager:

    def __init__(self):

        self.memory_db = PostgresMemory()

    def calculate_importance(
        self,
        emotional_state,
        message
    ):

        emotional_state = emotional_state.lower()

        high_priority = [
            "sad",
            "angry",
            "fear",
            "depressed",
            "anxious",
            "burnout"
        ]

        if emotional_state in high_priority:
            return 0.9

        if len(message.split()) > 20:
            return 0.6

        return 0.3

    def should_store_memory(
        self,
        importance_score
    ):

        return importance_score >= 0.5

    def store_memory(
        self,
        user_id,
        message,
        emotional_state
    ):

        importance = self.calculate_importance(
            emotional_state,
            message
        )

        if self.should_store_memory(importance):

            self.memory_db.store_memory(
                user_id=user_id,
                memory_text=message,
                emotional_state=emotional_state,
                importance_score=importance
            )

    def get_recent_memories(
        self,
        user_id,
        limit=5
    ):

        return self.memory_db.fetch_recent_memories(
            user_id,
            limit
        )