class MoralReasoningEngine:

    def evaluate_moral_reasoning(
        self,
        decisions,
        beliefs,
        goals
    ):

        moral_alignment = "balanced"

        decision_text = str(
            decisions
        ).lower()

        belief_text = str(
            beliefs
        ).lower()

        goal_text = str(
            goals
        ).lower()

        if "protect" in decision_text:

            moral_alignment = (
                "Protection-oriented reasoning."
            )

        elif "trust" in belief_text:

            moral_alignment = (
                "Trust-centered emotional reasoning."
            )

        elif "growth" in goal_text:

            moral_alignment = (
                "Growth-oriented moral reasoning."
            )

        else:

            moral_alignment = (
                "Emotionally adaptive reasoning."
            )

        return {

            "moral_alignment": moral_alignment,

            "decision_reference": decisions,

            "belief_reference": beliefs,

            "goal_reference": goals
        }
