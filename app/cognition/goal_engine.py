class GoalEngine:

    def generate_goals(
        self,
        dominant_emotion,
        reinforcement
    ):

        goals = []

        if reinforcement > 0.7:

            goals.append(
                "provide_emotional_support"
            )

        if dominant_emotion in [
            "sad",
            "anxious",
            "lonely"
        ]:

            goals.append(
                "increase_emotional_stability"
            )

        if dominant_emotion == "happy":

            goals.append(
                "maintain_positive_state"
            )

        if len(goals) == 0:

            goals.append(
                "maintain_conversation"
            )

        return goals
