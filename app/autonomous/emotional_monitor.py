class EmotionalMonitor:

    def evaluate_emotional_risk(
        self,
        dominant_emotion,
        reinforcement
    ):

        risk_level = "low"

        reinforcement_score = 0.0

        if isinstance(reinforcement, dict):

            reinforcement_score = reinforcement.get(
                "reinforcement_score",
                0.0
            )

        elif isinstance(reinforcement, (int, float)):

            reinforcement_score = reinforcement

        high_risk_emotions = [
            "burnout",
            "depressed",
            "fear",
            "anxious"
        ]

        if dominant_emotion in high_risk_emotions:

            risk_level = "moderate"

        if reinforcement_score > 0.8:

            risk_level = "high"

        return {

            "dominant_emotion": dominant_emotion,

            "reinforcement_score": reinforcement_score,

            "risk_level": risk_level
        }
