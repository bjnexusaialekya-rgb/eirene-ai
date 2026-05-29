class StrategicReasoning:

    def generate_strategy(
        self,
        goals,
        priorities,
        cognitive_state
    ):

        strategy = []

        if "Emotional stabilization" in priorities:

            strategy.append(
                "Reduce emotional overload before deeper reflection"
            )

        if "Trigger reduction" in priorities:

            strategy.append(
                "Avoid reinforcing negative emotional loops"
            )

        if "Long-term wellbeing" in priorities:

            strategy.append(
                "Encourage sustainable emotional recovery"
            )

        if cognitive_state == "overloaded":

            strategy.append(
                "Use emotionally lightweight responses"
            )

        return strategy
