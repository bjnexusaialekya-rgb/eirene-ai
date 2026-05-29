class EmotionalReasoningEngine:

    def analyze(

        self,

        dominant_emotion,

        triggers,

        reinforcement_patterns
    ):

        reasoning = []

        # -----------------------------------
        # Burnout reasoning
        # -----------------------------------

        if dominant_emotion in [

            "sad",
            "anxious",
            "fear"
        ]:

            reasoning.append(

                "The user may be experiencing prolonged emotional fatigue or burnout."
            )

        # -----------------------------------
        # Trigger reasoning
        # -----------------------------------

        if triggers:

            reasoning.append(

                f"Recurring emotional triggers detected: {', '.join(triggers)}"
            )

        # -----------------------------------
        # Reinforcement reasoning
        # -----------------------------------

        if reinforcement_patterns:

            reasoning.append(

                "Certain emotional states appear repeatedly reinforced over time."
            )

        # -----------------------------------
        # Cognitive synthesis
        # -----------------------------------

        if not reasoning:

            reasoning.append(

                "No major emotional instability patterns currently detected."
            )

        return reasoning