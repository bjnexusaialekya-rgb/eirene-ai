class EmotionalDrift:

    def calculate_drift(
        self,
        current_emotion,
        dominant_pattern
    ):

        if current_emotion == dominant_pattern:

            return {
                "drift_detected": False,
                "drift_type": "stable"
            }

        negative_cluster = [
            "sad",
            "fear",
            "angry",
            "burnout",
            "anxious"
        ]

        if (
            dominant_pattern in negative_cluster
            and current_emotion in negative_cluster
        ):

            return {
                "drift_detected": True,
                "drift_type": "negative_reinforcement"
            }

        return {
            "drift_detected": True,
            "drift_type": "emotional_transition"
        }
