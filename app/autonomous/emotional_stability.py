class EmotionalStability:

    def evaluate_stability(
        self,
        reinforcement,
        drift
    ):

        stability = "stable"

        if reinforcement > 0.8:
            stability = "fragile"

        if drift == "high":
            stability = "unstable"

        return {

            "stability": stability,

            "drift": drift
        }
