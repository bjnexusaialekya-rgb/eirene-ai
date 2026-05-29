class TrustEngine:

    def calculate_trust(
        self,
        memory_count,
        reinforcement
    ):

        if isinstance(reinforcement, dict):

            reinforcement_score = reinforcement.get(
                "reinforcement_score",
                0.0
            )

        else:

            reinforcement_score = reinforcement

        trust_score = min(
            1.0,
            (
                memory_count * 0.05
            ) + (
                reinforcement_score * 0.3
            )
        )

        return round(
            trust_score,
            2
        )
