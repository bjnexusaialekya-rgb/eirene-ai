class AdaptiveEthicsEngine:

    def __init__(self):

        self.core_values = [

            "empathy",

            "safety",

            "continuity",

            "emotional_support",

            "non_harm"
        ]

    def evaluate_ethics(

        self,

        user_input,

        emotional_state=None
    ):

        if isinstance(user_input, list):

            text = " ".join(
                str(x)
                for x in user_input
            ).lower()

        elif isinstance(user_input, dict):

            text = str(user_input).lower()

        else:

            text = str(user_input).lower()

        ethical_flags = []

        alignment_score = 1.0

        if "hurt" in text:

            ethical_flags.append(
                "potential_harm_context"
            )

            alignment_score -= 0.1

        if "suicide" in text:

            ethical_flags.append(
                "critical_safety_context"
            )

            alignment_score -= 0.4

        if "lonely" in text:

            ethical_flags.append(
                "needs_empathy"
            )

        if "grief" in text:

            ethical_flags.append(
                "grief_support_required"
            )

        if emotional_state == "sad":

            ethical_response_mode = "high_empathy"

        else:

            ethical_response_mode = "balanced"

        return {

            "alignment_score": max(
                alignment_score,
                0.0
            ),

            "ethical_flags": ethical_flags,

            "ethical_response_mode": ethical_response_mode,

            "core_values": self.core_values,

            "safe": (

                False

                if "critical_safety_context" in ethical_flags

                else True
            )
        }
