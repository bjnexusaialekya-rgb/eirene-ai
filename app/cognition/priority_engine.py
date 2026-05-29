class PriorityEngine:

    def prioritize(
        self,
        emotion,
        triggers,
        goals
    ):

        priorities = []

        if emotion in [
            "burnout",
            "sad",
            "fear",
            "anxious"
        ]:

            priorities.append(
                "Emotional stabilization"
            )

        if triggers:

            priorities.append(
                "Trigger reduction"
            )

        if goals:

            priorities.append(
                "Long-term wellbeing"
            )

        return priorities

