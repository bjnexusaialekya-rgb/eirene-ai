class SelfPreservationEngine:

    def evaluate_self_preservation(
        self,
        dominant_emotion,
        monitoring,
        trust_score
    ):

        preservation_state = "stable"

        if dominant_emotion in [
            "fear",
            "burnout",
            "sadness"
        ]:

            preservation_state = (
                "Increasing emotional self-protection."
            )

        if trust_score < 0.3:

            preservation_state = (
                "Reducing emotional openness for safety."
            )

        if monitoring.get(
            "risk_level",
            "low"
        ) == "high":

            preservation_state = (
                "Activating emotional stabilization safeguards."
            )

        return {

            "preservation_state": preservation_state,

            "trust_score": trust_score,

            "monitoring_reference": monitoring
        }
