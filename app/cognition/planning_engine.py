class PlanningEngine:

    def create_plan(
        self,
        goals,
        cognitive_state
    ):

        plan = []

        for goal in goals:

            if "Reduce emotional exhaustion" in goal:

                plan.append(
                    "Encourage rest and emotional decompression"
                )

            if "Improve emotional resilience" in goal:

                plan.append(
                    "Promote sustainable coping strategies"
                )

            if "Interrupt recurring emotional cycles" in goal:

                plan.append(
                    "Increase emotional self-awareness"
                )

        if cognitive_state == "overloaded":

            plan.append(
                "Avoid emotionally overwhelming responses"
            )

        return plan
