class BeliefEngine:

    def generate_beliefs(
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

        beliefs = []

        if dominant_emotion in [
            "sadness",
            "burnout",
            "fear",
            "anxious"
        ]:

            beliefs.append(
                "The user may currently feel emotionally overwhelmed."
            )

        if reinforcement_score > 0.7:

            beliefs.append(
                "Emotional reinforcement patterns are becoming persistent."
            )

        if len(beliefs) == 0:

            beliefs.append(
                "The emotional state appears relatively stable."
            )

        return beliefs