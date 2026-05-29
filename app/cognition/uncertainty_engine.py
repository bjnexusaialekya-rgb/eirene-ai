class UncertaintyEngine:

    def calculate_uncertainty(
        self,
        emotional_state,
        reasoning=None
    ):

        uncertainty_score = 0.3

        if emotional_state in [
            "anxious",
            "confused",
            "fear"
        ]:

            uncertainty_score = 0.8

        return {
            "uncertainty_score": uncertainty_score,
            "emotional_state": emotional_state
        }
