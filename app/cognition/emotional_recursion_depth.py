class EmotionalRecursionDepth:

    def calculate_recursion_depth(
        self,
        reinforcement,
        recursive_state,
        meta_awareness
    ):

        if isinstance(reinforcement, dict):

            reinforcement_score = reinforcement.get(
                "reinforcement_score",
                0.0
            )

        else:

            reinforcement_score = reinforcement

        depth = 1

        if reinforcement_score > 0.3:

            depth += 1

        if reinforcement_score > 0.5:

            depth += 1

        if reinforcement_score > 0.7:

            depth += 1

        if recursive_state:

            depth += 1

        if meta_awareness:

            depth += 1

        return {

            "recursion_depth": depth,

            "recursive_state": recursive_state,

            "meta_awareness_reference": meta_awareness
        }
