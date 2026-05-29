class DecisionEngine:

    def make_decision(
        self,
        emotion,
        priorities,
        strategy
    ):

        decisions = []

        if emotion in [
            "burnout",
            "sad",
            "fear",
            "anxious"
        ]:

            decisions.append(
                "Increase empathy depth"
            )

        if "Trigger reduction" in priorities:

            decisions.append(
                "Avoid emotionally activating language"
            )

        if strategy:

            decisions.append(
                "Align response with long-term recovery"
            )

        return decisions
