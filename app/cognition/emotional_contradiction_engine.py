class EmotionalContradictionEngine:

    def detect_contradictions(
        self,
        dominant_emotion,
        triggers,
        goals
    ):

        contradictions = []

        trigger_text = str(
            triggers
        ).lower()

        goal_text = str(
            goals
        ).lower()

        if dominant_emotion in [
            "burnout",
            "sadness"
        ] and "achievement" in goal_text:

            contradictions.append(
                "The user desires progress while emotionally exhausted."
            )

        if dominant_emotion == "fear" and "connection" in goal_text:

            contradictions.append(
                "The user seeks connection while fearing vulnerability."
            )

        if "abandonment" in trigger_text and "trust" in goal_text:

            contradictions.append(
                "The user seeks trust while expecting emotional loss."
            )

        if len(contradictions) == 0:

            contradictions.append(
                "No major emotional contradictions detected."
            )

        return contradictions
