class ExistentialReasoningEngine:

    def __init__(self):
        pass

    def process_existential_state(
        self,
        user_input,
        emotional_state=None
    ):

        existential_keywords = [
            "meaning",
            "purpose",
            "existence",
            "death",
            "consciousness",
            "identity",
            "suffering",
            "why"
        ]

        detected = any(
            word in user_input.lower()
            for word in existential_keywords
        )

        return {
            "existential_detected": detected,
            "emotional_state": emotional_state,
            "reflection": (
                "User is engaging in existential reasoning."
                if detected
                else "No existential crisis detected."
            )
        }
