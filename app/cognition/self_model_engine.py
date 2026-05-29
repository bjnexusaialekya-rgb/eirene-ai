class SelfModelEngine:

    def build_self_model(

        self,

        emotional_profile,

        triggers,

        reinforcement_patterns
    ):

        dominant_emotion = emotional_profile.get(
            "dominant_emotion",
            "neutral"
        )

        beliefs = []

        # -----------------------------------
        # Emotional identity patterns
        # -----------------------------------

        if dominant_emotion in [

            "sad",
            "anxious",
            "fear"
        ]:

            beliefs.append(

                "User may perceive life as emotionally overwhelming."
            )

        if dominant_emotion == "angry":

            beliefs.append(

                "User may feel emotionally misunderstood or pressured."
            )

        # -----------------------------------
        # Trigger identity
        # -----------------------------------

        if triggers:

            beliefs.append(

                f"Recurring emotional stress linked to: {', '.join(triggers)}"
            )

        # -----------------------------------
        # Reinforcement identity
        # -----------------------------------

        if reinforcement_patterns:

            beliefs.append(

                "Certain emotional cycles appear deeply reinforced psychologically."
            )

        # -----------------------------------
        # Default stabilization
        # -----------------------------------

        if not beliefs:

            beliefs.append(

                "User currently demonstrates relatively stable emotional patterns."
            )

        return beliefs