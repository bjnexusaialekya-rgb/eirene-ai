class ProactiveSupport:

    def generate_support(
        self,
        drift_analysis
    ):

        drift_type = drift_analysis["drift_type"]

        if drift_type == "negative_reinforcement":

            return (
                "The user may be experiencing recurring emotional strain "
                "and could benefit from grounding, rest, or emotional decompression."
            )

        if drift_type == "emotional_transition":

            return (
                "The user may be shifting emotionally and could benefit "
                "from reflective exploration and reassurance."
            )

        return (
            "The user's emotional state appears relatively stable."
        )
