class LongTermSelfModel:

    def build(
        self,
        beliefs,
        narrative
    ):

        return {

            "long_term_self":
            "Persistent evolving self model maintained.",

            "belief_reference":
            beliefs,

            "narrative_reference":
            narrative
        }
