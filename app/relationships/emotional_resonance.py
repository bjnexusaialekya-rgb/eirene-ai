class EmotionalResonance:

    def calculate_resonance(
        self,
        dominant_emotion,
        reinforcement
    ):

        if isinstance(reinforcement, dict):

            reinforcement_score = reinforcement.get(
                "reinforcement_score",
                0.0
            )

        else:

            reinforcement_score = reinforcement

        resonance_score = (
            reinforcement_score * 0.2
        )

        if dominant_emotion in [
            "sadness",
            "burnout",
            "fear",
            "anxious"
        ]:

            resonance_score += 0.5

        return round(
            min(resonance_score, 1.0),
            2
        )
