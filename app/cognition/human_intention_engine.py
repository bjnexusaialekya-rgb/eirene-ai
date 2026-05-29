class HumanIntentionEngine:

    def infer_intention(
        self,
        user_input
    ):

        lowered = user_input.lower()

        intention = "general_emotional_expression"

        if "help" in lowered:

            intention = "support_seeking"

        elif "fear" in lowered:

            intention = "safety_seeking"

        elif "alone" in lowered:

            intention = "connection_seeking"

        return {

            "inferred_intention":
            intention
        }
