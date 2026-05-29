class PersonalityEvolution:

    def evolve_personality(
        self,
        dominant_emotion,
        reinforcement
    ):

        evolution = {
            "empathy_level": "stable",
            "emotional_resilience": "stable",
            "self_awareness": "stable"
        }

        negative_states = [
            "sad",
            "burnout",
            "fear",
            "anxious"
        ]

        if dominant_emotion in negative_states:

            evolution["empathy_level"] = "deepening"

            evolution["self_awareness"] = "increasing"

        if len(reinforcement) > 2:

            evolution["emotional_resilience"] = "under_pressure"

        return evolution
