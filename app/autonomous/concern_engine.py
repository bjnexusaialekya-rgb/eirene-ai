class ConcernEngine:

    def evaluate_concerns(
        self,
        emotional_risk,
        dependency
    ):

        concern = "minimal"

        if emotional_risk == "high":
            concern = "elevated"

        if dependency == "high_attachment":
            concern = "monitor_closely"

        return {

            "concern_level": concern
        }
