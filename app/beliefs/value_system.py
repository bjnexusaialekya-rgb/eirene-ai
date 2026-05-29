class ValueSystem:

    def derive_values(
        self,
        goals
    ):

        values = []

        for goal in goals:

            if "stability" in goal.lower():

                values.append(
                    "emotional stability"
                )

            if "growth" in goal.lower():

                values.append(
                    "personal growth"
                )

        return list(set(values))
