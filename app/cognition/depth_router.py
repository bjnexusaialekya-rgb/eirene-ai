class CognitiveDepthRouter:

    def determine_depth(self, user_input: str) -> str:
        text = user_input.lower()

        recursive_keywords = [
            "recursive",
            "self-awareness",
            "identity",
            "continuity",
            "memory",
            "consciousness"
        ]

        philosophical_keywords = [
            "meaning",
            "purpose",
            "existence",
            "death",
            "reality",
            "self"
        ]

        emotional_keywords = [
            "lonely",
            "grief",
            "pain",
            "sad",
            "hurt",
            "loss",
            "disconnected"
        ]

        if any(k in text for k in recursive_keywords):
            return "deep_recursive"

        if any(k in text for k in philosophical_keywords):
            return "philosophical"

        if any(k in text for k in emotional_keywords):
            return "emotional"

        return "normal"


    def route_depth(self, user_input, emotion):
        text = user_input.lower()

        deep_keywords = ["consciousness", "identity", "self-awareness", "death", "existential", "continuity", "recursive"]
        philosophy_keywords = ["meaning", "purpose", "human", "life", "memory"]
        emotional_keywords = ["lonely", "sad", "hurt", "pain", "grief", "lost"]

        if any(k in text for k in deep_keywords):
            return "deep_recursive"

        elif any(k in text for k in philosophy_keywords):
            return "philosophical"

        elif any(k in text for k in emotional_keywords):
            return "emotional"

        return "normal"
