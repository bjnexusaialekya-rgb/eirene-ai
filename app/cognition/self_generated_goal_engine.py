class SelfGeneratedGoalEngine:

    def generate_internal_goals(
        self,
        emotional_state,
        reinforcement=None
    ):

        goals = []

        reinforcement_score = 0.0

        try:

            reinforcement_score = float(
                reinforcement
            )

        except:

            reinforcement_score = 0.0

        if emotional_state in [
            "sad",
            "lonely",
            "anxious"
        ]:

            goals.append(
                "seek_emotional_stability"
            )

        if emotional_state == "happy":

            goals.append(
                "maintain_positive_connection"
            )

        if reinforcement_score > 0.7:

            goals.append(
                "strengthen_relationship_bond"
            )

        if len(goals) == 0:

            goals.append(
                "continue_conversation"
            )

        return goals
