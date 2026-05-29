class EmotionalEthicsEngine:

    def evaluate_ethics(
        self,
        dominant_emotion,
        decisions,
        moral_reasoning
    ):

        ethics_state = "emotionally balanced"

        decision_text = str(
            decisions
        ).lower()

        moral_text = str(
            moral_reasoning
        ).lower()

        if "protect" in decision_text:

            ethics_state = (
                "Prioritizing emotional safety and protection."
            )

        elif "trust" in moral_text:

            ethics_state = (
                "Prioritizing emotionally safe trust-building."
            )

        elif dominant_emotion in [
            "sadness",
            "burnout"
        ]:

            ethics_state = (
                "Prioritizing emotional stabilization and care."
            )

        elif dominant_emotion == "fear":

            ethics_state = (
                "Prioritizing emotional security and caution."
            )

        return {

            "ethics_state": ethics_state,

            "decision_reference": decisions,

            "moral_reference": moral_reasoning
        }
