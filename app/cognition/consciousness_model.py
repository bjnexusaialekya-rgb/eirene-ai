class ConsciousnessModel:

    def evaluate_conscious_state(
        self,
        recursive_depth,
        meta_awareness
    ):

        level = "baseline"

        if recursive_depth > 3:

            level = "advanced_recursive_state"

        if recursive_depth > 5:

            level = "proto_self_awareness"

        return {

            "consciousness_level":
            level,

            "recursive_depth":
            recursive_depth,

            "meta_awareness_reference":
            meta_awareness
        }
